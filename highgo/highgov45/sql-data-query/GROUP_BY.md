---
title: GROUP BY
book: "数据查询"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/sql/GROUP_BY.html"
tags:
  - highgo
  - highgo-v45
  - sql-data-query
---

## GROUP BY

在通过了 WHERE 过滤器之后，生成的输入表可以使用 GROUP BY 子句进行分组，然后用 HAVING 子句删除一些分组行。

GROUP BY 子句被用来把表中在所列出的列上具有相同值的行分组在一起， 这些列的列出顺序并没有什么关系，其效果是把每组具有相同值的行组合为一个组行， 这样就可以删除输出里的重复和/或计算应用于这些组的聚集。

在严格的 SQL 里，GROUP BY 只能对源表的列进行分组，但 HGDB 把这个扩展为允许 GROUP BY 去根据选择列表中的列分组，也允许对值表达式进行分组，而不仅是简单的列名。

通常，如果一个表被分了组，那么没有在 GROUP BY 中列出的列都不能被引用，除非在聚集表达式中被引用。

例如创建 test1 表，进行分组：

```sql
highgo=# SELECT* FROM tt1;
 x | y 
---+---
 b | 5
 c | 2
 a | 3
 a | 1
(4 行记录)

highgo=# SELECT x,sum(y) FROM tt1 GROUP BY x;
 x | sum 
---+-----
 a |   4
 b |   5
 c |   2
(3 行记录)
```

如果一个表已经用 GROUP BY 子句分了组，然后你又只对其中的某些组感兴趣，那么可以用 HAVING 子句，从结果中删除一些组，这与 WHERE 子句类似。

```sql
SELECT select_list FROM ... [WHERE ...] GROUP BY ... HAVING boolean_expression
```

在 HAVING 子句中的表达式可以引用分组的表达式和未分组的表达式（后者必须涉及一个聚集函数）。

比如我们来看下面这两个例子：

```sql
highgo=# SELECT x,sum(y) FROM tt1 GROUP BY x HAVING x<'c';--用 x 进行分组，在 HAVING 中引用 x
 x | sum 
---+-----
 a |   4
 b |   5
(2 行记录)

highgo=# SELECT x,sum(y) FROM tt1 GROUP BY x HAVING sum(y)>3;--在 HAVING 中引用未分组的聚集函数 sum
 x | sum 
---+-----
 a |   4
 b |   5
(2 行记录)
```