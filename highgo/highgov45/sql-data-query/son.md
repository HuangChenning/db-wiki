---
title: "子查询"
book: "数据查询"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/sql/son.html"
tags:
  - highgo
  - highgo-v45
  - sql-data-query
---

## 子查询

子查询指定了一个派生表，它必须被包围在圆括弧里并且必须被赋予一个表别名。一个子查询也可以是一个 VALUES 列表。

例如用 SELECT 和 VALUES 来表示两个子查询：

```sql
FROM (SELECT * FROM table1) AS alias_name

FROM (VALUES ('anne', 'smith'), ('bob', 'jones'), ('joe', 'blow')) AS names(first, last)
```