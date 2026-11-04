---
title: SQL Language Reference
book: SQL Language Reference
doc_id: E83703-08
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/sqlrf/Null-Conditions.html
tags:
  - oracle
  - 12c
  - sql-language-reference
---

A `NULL` condition tests for nulls. This is the only condition that you should use to test for nulls.

null\_condition::=

![null_condition](img/null_condition.gif)

> ```
> expr IS [ NOT ] NULL
> ```


Table 6-9 lists the null conditions.

Table 6-9 Null Condition

| Type of Condition | Operation | Example |
| --- | --- | --- |
| ``` IS [NOT] NULL ``` | Tests for nulls.  See Also: [Nulls](Nulls.md) | ``` SELECT last_name   FROM employees   WHERE commission_pct   IS NULL   ORDER BY last_name; ``` |