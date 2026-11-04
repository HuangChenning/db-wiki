---
title: "字符类型"
book: "数据类型"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/guide/guide_eight_text9.html"
tags:
  - highgo
  - highgo-v9
  - guide-data-types
---

## 字符类型

| 名字 | 描述 |
| --- | --- |
| character varying(n)，varchar(n) | 有限制的变长 |
| character(n)，char(n) | 定长，空格填充 |
| text | 无限变长 |

SQL 定义了两种基本的字符类型： character varying(n)和 character(n) ， 其 中 n 是一个正整数。两种类型都可以存储最多 n 个字符长的串。试图存储更长的 串到这些类型的列里会产生一个错误， 除非超出长度的字符都是空白，这种情 况下该串将被截断为最大长度（这个看上去有点怪异的例外是 SQL 标准要求的）。

varchar(n)和 char(n)的概念分别是 character varying(n)和 character(n)的别名。 另外，瀚高数据库提供 text 类型，它可以存储任何长度的串。

**提示：**

这三种类型之间没有性能差别，只不过是在使用填充空白的类型的时候需要更 多存储尺寸，以及在存储到一个有长度约束的列时需要少量额外 CPU 周期来 检查长度。虽然在某些其它的数据库系统里，character(n)有一定的性能优势， 但在瀚高数据库里没有。事实上，character(n)通常是这三种类型之中最慢的一 个，因为它需要额外的存储开销。在大多数情况下，应该使用 text 或者 character varying（varchar）。