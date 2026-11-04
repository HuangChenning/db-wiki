---
title: ORDER BY
book: "数据查询"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/sql/ORDER_BY.html"
tags:
  - highgo
  - highgo-v45
  - sql-data-query
---

## ORDER BY

我们可以使用 ORDER BY 子句指定查询的输出顺序。

ORDER BY 的语句如下：

```sql
SELECT select-list
FROM table_expression
[ORDER BY sort_expression [ASC|DESC][NULLS{FIRST|LAST}];
```

ASC表示升序，DESC表示降序，NULLS FIRST 和 NULLS LAST 选项可以决定在排序顺序中，空值是出现在非空值之前或者之后。默认情况下，空值被认为比任何非空值都要大。

一个 sort\_expression 可以是列标签也可以是一个输出列的编号。

例如下面这两种用法，两者都根据第一个输出列排序：

```sql
highgo=# SELECT a+b AS sum, c FROM table1 ORDER BY sum;
 sum | c 
-----+---
   3 | 3
   5 | 4
   9 | 5
(3 行记录)

highgo=# SELECT a, max(b) FROM table1 GROUP BY a ORDER BY 1;
 a | max 
---+-----
 1 |   2
 2 |   3
 4 |   5
(3 行记录)
```

注意输出列的名字必须孤立，即它不能被用在一个表达式中。

```sql
SELECT a + b AS sum, c FROM table1 ORDER BY sum + c; -- 错误
```