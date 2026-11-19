---
title: "横向派生表"
book: "SQL 参考"
version: V4.5.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000004479761.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# 横向派生表

横向派生表（Lateral Derived Table）是一种特殊类型的派生表，它使用 `LATERAL` 关键字可以用来指定一个派生表，使其能够引用同一个 `FROM` 子句中先前定义的其他表或派生表的字段。这使得派生表中的子查询可以依赖于在同一 `FROM` 子句中定义的表，从而访问这些表的列值。

横向派生表的主要特点是它们可以引用在它们之前在 `FROM` 子句中定义的表的列，普通派生表不具备这种能力。

## 示例

```sql
SELECT *
FROM A, LATERAL (SELECT * FROM B WHERE B.col1 = A.col1) AS derived_table;
```

## 相关文档

更多有关横向派生表的使用信息，请参见 [横向派生表](../../../../../300.develop/200.application-development-of-oracle-mode/500.read-data-of-oracle-mode/200.multi-table-join-query-of-oracle-mode/600.lateral-derived-tables-of-oracle-develop.md)。
