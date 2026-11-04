---
title: "组合查询"
book: "数据查询"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/sql/combine.html"
tags:
  - highgo
  - highgo-v45
  - sql-data-query
---

## 组合查询

两个查询的结果可以用集合操作的并、交、差进行组合。为了计算两个查询的并、交、差，这两个查询必须是“并操作兼容的”，也就意味着它们都返回同样数量的列， 并且对应的列有兼容的数据类型。

UNION 有效地把 query2 的结果附加到 query1 的结果上（并）；INTERSECT 返回那些同时存在于 query1 和 query2 的结果中的行（交）；EXCEPT 返回所有在 query1 的结果中但是不在 query2 的结果中的行（差）。

```sql
query1 UNION [ALL] query2
query1 INTERSECT [ALL] query2 
query1 EXCEPT [ALL] query2
```

query1 和 query2 都是可以使用以上所有特性的查询，如果不使用 `ALL` ，查询将删除结果中所有重复的行。集合操作也可以嵌套和级连，例如 `query1 UNION query2 UNION query3` 实际执行的是： `(query1 UNION query2) UNION query3 ` 。