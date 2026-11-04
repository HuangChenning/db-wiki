---
title: "VALUES 列表"
book: "数据查询DQL"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/guide/guide_five_text6.html"
tags:
  - highgo
  - highgo-v9
  - guide-dql
---

## VALUES 列表

VALUES 提供了一种生成“常量表”的方法，它可以被使用在一个查询中而不需要实际在磁盘上创建一个表。

VALUES 的语句如下所示：

```
VALUES ( expression [, ...] ) [, ...]
```

每一个被圆括号包围的表达式列表生成表中的一行。列表内必须具有相同数据的元素（即表中列的数目），并且在每个列表中对应的项必须具有可兼容的数据类型。

在默认情况下，数据库将 column1、column2 等名字分配给一个 VALUES 表的列。这些列名不是由 SQL 标准指定的，并且不同的数据库系统的做法也不同，因此通常最好使用表别名列表来重写这些默认的名字。

例如将 VALUES 以 (num,letter) 为列名进行输出：

```
highgo=#  SELECT * FROM (VALUES (1, 'one'), (2, 'two'), (3, 'three')) AS t (num,letter);
 num | letter 
-----+--------
   1 | one
   2 | two
   3 | three
(3 行记录)
```

在句法上，后面跟随着表达式列表的 VALUES 列表被视为等同于 `SELECT select_list FROM table_expression` ，并且可以出现在 SELECT 能出现的任何地方。例如，你可以把它用作 UNION 的一部分，或者附加一个 sort\_specification（ORDER BY、LIMIT、OFFSET）给它。VALUES 最常见的用途是作为一个 INSERT 命令的数据源，以及作为一个子查询。