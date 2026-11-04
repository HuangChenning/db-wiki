---
title: "日期时间类型"
book: "数据类型"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/sql/date.html"
tags:
  - highgo
  - highgo-v45
  - sql-data-types
---

## 日期/时间类型

HGDB 支持 SQL 中所有的日期和时间类型，日期根据公历来计算，对于该历法被引入之前的年份也一样。

下表是 HGDB 中的日期/时间类型。

| 名字 | 存储尺寸 | 描述 | 最小值 | 最大值 | 解析度 |
| --- | --- | --- | --- | --- | --- |
| timestamp \[ (p) \] \[ without time zone \] | 8字节 | 包括日期和时间（无时区） | 4713BC | 294276AD | 1微秒 |
| timestamp \[ (p) \] with time zone | 8字节 | 包括日期和时间，有时区 | 4713BC | 294276AD | 1微秒 |
| date | 4字节 | 日期（没有一天中的时间） | 4713BC | 5874897AD | 1日 |
| time \[ (p) \] \[ without time zone \] | 8字节 | 一天中的时间（无日期） | 00:00:00 | 24:00:00 | 1微秒 |
| time \[ (p) \] with time zone | 12字节 | 仅仅是一天中的时间（没有日期），带有时区 | 00:00:00+1459 | 24:00:00-1459 | 1微秒 |
| interval \[ fields \] \[ (p) \] | 16字节 | 时间间隔 | \-178000000年 | 178000000年 | 1微秒 |

HGDB 中，timestamp 等效于 timestamp without time zone，timestamptz 被接受为 timestamp with time zone 的一种简写。

time、timestamp 和 interval 接受一个可选的精度值 p，这个精度值声明在秒域中小数点之后保留的位数，p 允许的范围是从0到6，缺省情况下，在精度上没有明确的边界。

interval 类型有一个附加选项，可以通过写下面之一的短语来限制存储的 fields 的集合：

YEAR、MONTH、DAY、HOUR、MINUTE、SECOND、

YEAR TO MONTH、DAY TO HOUR、DAY TO MINUTE、DAY TO SECOND、

HOUR TO MINUTE、HOUR TO SECOND、MINUTE TO SECOND

注意如果 fields 和 p 被指定，fields 必须包括 SECOND，因为精度只应用于秒。

### 日期/时间输入

所有日期或者时间在输入时都需要由单引号包围，就像一个文本字符串一样。

日期和时间的输入可以接受几乎任何合理的格式，包括 ISO 8601、SQL-兼容的、传统的和其他的形式。DateStyle 参数可以指定日期输入的格式，MDY 是“月-日-年”，DMY 是“日-月-年”，YMD 是“年-月-日”。

下表显示了 date 类型可能的输入方式。

| 例子 | 描述 |
| --- | --- |
| 1999-01-08 | ISO 8601；任何模式下的1月8日（推荐格式） |
| January 8,1999 | 在任何 DateStyle 输入模式下都无歧义 |
| 1/8/1999 | MDY 模式中的1月8日；DMY 模式中的8月1日 |
| 1/18/1999 | MDY 模式中的1月18日；在其他模式中被拒绝 |
| 01/02/03 | MDY 模式中的2003年1月2日；   DMY 模式中的2003年2月1日；   YMD 模式中的2001年2月3日 |
| 1999-Jan-08；   Jan-08-1999;   08-Jan-1999 | 任何模式下的1月8日 |
| 99-Jan-08 | YMD 模式中的1月8日，否则错误 |
| 08-Jan-99   Jan-08-99 | 1月8日，除了在 YMD 模式中错误 |
| 19990108   990108 | ISO 8601；任何模式中的1999年1月8日 |
| 1999.008 | 年和一年中的日子 |
| J2451187 | 儒略日期 |
| January 8, 99 BC | 公元前99年 |

时间：当日时间类型是 time \[ (p) \] without time zone 和 time \[ (p) \] with time zone，只写 time 等效于 time without time zone。这些类型的有效输入由当日时间后面跟着可选的时区组成，时间类型中指定的日期会被忽略，除非使用了一个涉及到夏令时规则的时区，例如 America/New\_York。time without time zone 中指定的时区也会被无声地忽略。

| 例子 | 描述 |
| --- | --- |
| 04:05:06.789 | ISO 8601 |
| 04:05:06 | ISO 8601 |
| 04:05 | ISO 8601 |
| 040506 | ISO 8601 |
| 04:05 AM | 和 04:05 一样，AM 并不影响值 |
| 04:05 PM | 和 16:05 一样，输入的小时必须 <= 12 |
| 04:05:06.789-8 | ISO 8601 |
| 04:05:06-08:99 | ISO 8601 |
| 04:05-08:00 | ISO 8601 |
| 040506-08 | ISO 8601 |
| 04:05:06 PST | 缩写指定的时区 |
| 2003-04-12 04:05:06 America/New\_York | 全名指定的时区 |