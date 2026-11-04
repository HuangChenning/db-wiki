---
title: "LIMIT和OFFSET"
book: "数据查询"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/sql/LIMIT_OFFSET.html"
tags:
  - highgo
  - highgo-v45
  - sql-data-query
---

## LIMIT 和 OFFSET

LIMIT 和 OFFSET 允许你只检索查询产生的行的一部分。如果给出了一个 LIMIT 限制计数，那么会返回数量不超过该限制的行，LIMIT ALL 的效果和省略 LIMIT 子句一样，就像是 LIMIT 带有 NULL 参数一样，返回全部查询结果。OFFSET 说明在开始返回行之前忽略多少行，OFFSET 0 的效果和省略 OFFSET 子句是一样的，即不忽略任何行。如果 OFFSET 和 LIMIT 都出现了，那么在返回 LIMIT 个行之前要先忽略 OFFSET 个行。

在使用 LIMIT 时，用一个 ORDER BY 子句把结果行约束成一个唯一的顺序是很重要的，否则你将拿到一个不确定的查询结果。

下面是 LIMIT 和 OFFSET 的一个小例子：

```sql
highgo=# SELECT a+b AS sum,c FROM table1 ORDER BY sum LIMIT 1 OFFSET 1;
 sum | c 
-----+---
   5 | 4
(1 行记录)
```