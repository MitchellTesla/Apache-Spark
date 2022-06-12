/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package org.apache.spark.sql.catalyst.expressions

import org.apache.spark.sql.catalyst.InternalRow
import org.apache.spark.sql.catalyst.analysis.TypeCheckResult
import org.apache.spark.sql.catalyst.expressions.Cast.{forceNullable, resolvableNullability}
import org.apache.spark.sql.catalyst.expressions.codegen.{CodegenContext, CodeGenerator, ExprCode}
import org.apache.spark.sql.catalyst.expressions.codegen.Block._
import org.apache.spark.sql.catalyst.trees.TreePattern.{RUNTIME_REPLACEABLE, TreePattern}
import org.apache.spark.sql.types.{ArrayType, DataType, MapType, StructType}

case class TryEval(child: Expression) extends UnaryExpression with NullIntolerant {
  override def doGenCode(ctx: CodegenContext, ev: ExprCode): ExprCode = {
    val childGen = child.genCode(ctx)
    ev.copy(code = code"""
      boolean ${ev.isNull} = true;
      ${CodeGenerator.javaType(dataType)} ${ev.value} = ${CodeGenerator.defaultValue(dataType)};
      try {
        ${childGen.code}
        ${ev.isNull} = ${childGen.isNull};
        ${ev.value} = ${childGen.value};
      } catch (Exception e) {
      }"""
    )
  }

  override def eval(input: InternalRow): Any =
    try {
      child.eval(input)
    } catch {
      case _: Exception =>
        null
    }

  override def dataType: DataType = child.dataType

  override def nullable: Boolean = true

  override protected def withNewChildInternal(newChild: Expression): Expression =
    copy(child = newChild)
}

/**
 * A special version of [[Cast]] with ansi mode on. It performs the same operation (i.e. converts a
 * value of one data type into another data type), but returns a NULL value instead of raising an
 * error when the conversion can not be performed.
 */
@ExpressionDescription(
  usage = """
    _FUNC_(expr AS type) - Casts the value `expr` to the target data type `type`.
      This expression is identical to CAST with configuration `spark.sql.ansi.enabled` as
      true, except it returns NULL instead of raising an error. Note that the behavior of this
      expression doesn't depend on configuration `spark.sql.ansi.enabled`.
  """,
  examples = """
    Examples:
      > SELECT _FUNC_('10' as int);
       10
      > SELECT _FUNC_(1234567890123L as int);
       null
  """,
  since = "3.2.0",
  group = "conversion_funcs")
case class TryCast(child: Expression, toType: DataType, timeZoneId: Option[String] = None)
  extends UnaryExpression with RuntimeReplaceable with TimeZoneAwareExpression {

  override def withTimeZone(timeZoneId: String): TimeZoneAwareExpression =
    copy(timeZoneId = Option(timeZoneId))

  override def nodePatternsInternal(): Seq[TreePattern] = Seq(RUNTIME_REPLACEABLE)

  // When this cast involves TimeZone, it's only resolved if the timeZoneId is set;
  // Otherwise behave like Expression.resolved.
  override lazy val resolved: Boolean = childrenResolved && checkInputDataTypes().isSuccess &&
    (!Cast.needsTimeZone(child.dataType, toType) || timeZoneId.isDefined)

  override lazy val replacement = {
    TryEval(Cast(child, toType, timeZoneId = timeZoneId, ansiEnabled = true))
  }

  // If the target data type is a complex type which can't have Null values, we should guarantee
  // that the casting between the element types won't produce Null results.
  private def canCast(from: DataType, to: DataType): Boolean = (from, to) match {
    case (ArrayType(fromType, fn), ArrayType(toType, tn)) =>
      canCast(fromType, toType) &&
        resolvableNullability(fn || forceNullable(fromType, toType), tn)

    case (MapType(fromKey, fromValue, fn), MapType(toKey, toValue, tn)) =>
      canCast(fromKey, toKey) &&
        (!forceNullable(fromKey, toKey)) &&
        canCast(fromValue, toValue) &&
        resolvableNullability(fn || forceNullable(fromValue, toValue), tn)

    case (StructType(fromFields), StructType(toFields)) =>
      fromFields.length == toFields.length &&
        fromFields.zip(toFields).forall {
          case (fromField, toField) =>
            canCast(fromField.dataType, toField.dataType) &&
              resolvableNullability(
                fromField.nullable || forceNullable(fromField.dataType, toField.dataType),
                toField.nullable)
        }

    case _ =>
      Cast.canAnsiCast(from, to)
  }

  override def checkInputDataTypes(): TypeCheckResult = {
    if (canCast(child.dataType, dataType)) {
      TypeCheckResult.TypeCheckSuccess
    } else {
      TypeCheckResult.TypeCheckFailure(Cast.typeCheckFailureMessage(child.dataType, toType, None))
    }
  }

  override def toString: String = s"try_cast($child as ${dataType.simpleString})"

  override def sql: String = s"TRY_CAST(${child.sql} AS ${dataType.sql})"

  override protected def withNewChildInternal(newChild: Expression): Expression =
    this.copy(child = newChild)
}

// scalastyle:off line.size.limit
@ExpressionDescription(
  usage = "_FUNC_(expr1, expr2) - Returns the sum of `expr1`and `expr2` and the result is null on overflow. " +
    "The acceptable input types are the same with the `+` operator.",
  examples = """
    Examples:
      > SELECT _FUNC_(1, 2);
       3
      > SELECT _FUNC_(2147483647, 1);
       NULL
      > SELECT _FUNC_(date'2021-01-01', 1);
       2021-01-02
      > SELECT _FUNC_(date'2021-01-01', interval 1 year);
       2022-01-01
      > SELECT _FUNC_(timestamp'2021-01-01 00:00:00', interval 1 day);
       2021-01-02 00:00:00
      > SELECT _FUNC_(interval 1 year, interval 2 year);
       3-0
  """,
  since = "3.2.0",
  group = "math_funcs")
// scalastyle:on line.size.limit
case class TryAdd(left: Expression, right: Expression, replacement: Expression)
    extends RuntimeReplaceable with InheritAnalysisRules {
  def this(left: Expression, right: Expression) =
    this(left, right, TryEval(Add(left, right, failOnError = true)))

  override def prettyName: String = "try_add"

  override def parameters: Seq[Expression] = Seq(left, right)

  override protected def withNewChildInternal(newChild: Expression): Expression =
    this.copy(replacement = newChild)
}

// scalastyle:off line.size.limit
@ExpressionDescription(
  usage = "_FUNC_(dividend, divisor) - Returns `dividend`/`divisor`. It always performs floating point division. Its result is always null if `expr2` is 0. " +
    "`dividend` must be a numeric or an interval. `divisor` must be a numeric.",
  examples = """
    Examples:
      > SELECT _FUNC_(3, 2);
       1.5
      > SELECT _FUNC_(2L, 2L);
       1.0
      > SELECT _FUNC_(1, 0);
       NULL
      > SELECT _FUNC_(interval 2 month, 2);
       0-1
      > SELECT _FUNC_(interval 2 month, 0);
       NULL
  """,
  since = "3.2.0",
  group = "math_funcs")
// scalastyle:on line.size.limit
case class TryDivide(left: Expression, right: Expression, replacement: Expression)
  extends RuntimeReplaceable with InheritAnalysisRules {
  def this(left: Expression, right: Expression) =
    this(left, right, TryEval(Divide(left, right, failOnError = true)))

  override def prettyName: String = "try_divide"

  override def parameters: Seq[Expression] = Seq(left, right)

  override protected def withNewChildInternal(newChild: Expression): Expression = {
    copy(replacement = newChild)
  }
}

@ExpressionDescription(
  usage = "_FUNC_(expr1, expr2) - Returns `expr1`-`expr2` and the result is null on overflow. " +
    "The acceptable input types are the same with the `-` operator.",
  examples = """
    Examples:
      > SELECT _FUNC_(2, 1);
       1
      > SELECT _FUNC_(-2147483648, 1);
       NULL
      > SELECT _FUNC_(date'2021-01-02', 1);
       2021-01-01
      > SELECT _FUNC_(date'2021-01-01', interval 1 year);
       2020-01-01
      > SELECT _FUNC_(timestamp'2021-01-02 00:00:00', interval 1 day);
       2021-01-01 00:00:00
      > SELECT _FUNC_(interval 2 year, interval 1 year);
       1-0
  """,
  since = "3.3.0",
  group = "math_funcs")
case class TrySubtract(left: Expression, right: Expression, replacement: Expression)
  extends RuntimeReplaceable with InheritAnalysisRules {
  def this(left: Expression, right: Expression) =
    this(left, right, TryEval(Subtract(left, right, failOnError = true)))

  override def prettyName: String = "try_subtract"

  override def parameters: Seq[Expression] = Seq(left, right)

  override protected def withNewChildInternal(newChild: Expression): Expression =
    this.copy(replacement = newChild)
}

@ExpressionDescription(
  usage = "_FUNC_(expr1, expr2) - Returns `expr1`*`expr2` and the result is null on overflow. " +
    "The acceptable input types are the same with the `*` operator.",
  examples = """
    Examples:
      > SELECT _FUNC_(2, 3);
       6
      > SELECT _FUNC_(-2147483648, 10);
       NULL
      > SELECT _FUNC_(interval 2 year, 3);
       6-0
  """,
  since = "3.3.0",
  group = "math_funcs")
case class TryMultiply(left: Expression, right: Expression, replacement: Expression)
  extends RuntimeReplaceable with InheritAnalysisRules {
  def this(left: Expression, right: Expression) =
    this(left, right, TryEval(Multiply(left, right, failOnError = true)))

  override def prettyName: String = "try_multiply"

  override def parameters: Seq[Expression] = Seq(left, right)

  override protected def withNewChildInternal(newChild: Expression): Expression =
    this.copy(replacement = newChild)
}

// scalastyle:off line.size.limit
@ExpressionDescription(
  usage = "_FUNC_(str[, fmt]) - This is a special version of `to_binary` that performs the same operation, but returns a NULL value instead of raising an error if the conversion cannot be performed.",
  examples = """
    Examples:
      > SELECT _FUNC_('abc', 'utf-8');
       abc
      > select _FUNC_('a!', 'base64');
       NULL
      > select _FUNC_('abc', 'invalidFormat');
       NULL
  """,
  since = "3.3.0",
  group = "string_funcs")
// scalastyle:on line.size.limit
case class TryToBinary(
    expr: Expression,
    format: Option[Expression],
    replacement: Expression) extends RuntimeReplaceable
  with InheritAnalysisRules {
  def this(expr: Expression) =
    this(expr, None, TryEval(ToBinary(expr, None, nullOnInvalidFormat = true)))

  def this(expr: Expression, formatExpression: Expression) =
    this(expr, Some(formatExpression),
      TryEval(ToBinary(expr, Some(formatExpression), nullOnInvalidFormat = true)))

  override def prettyName: String = "try_to_binary"

  override def parameters: Seq[Expression] = expr +: format.toSeq

  override protected def withNewChildInternal(newChild: Expression): Expression =
    this.copy(replacement = newChild)
}
