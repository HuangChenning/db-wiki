---
title: Null Conditions
book: SQL Language Reference
doc_id: E41084-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41084/conditions008.htm
tags:
  - oracle
  - 11g
  - sql-language-reference
---

A `NULL` condition tests for nulls. This is the only condition that you should use to test for nulls.

null\_condition::=

![null_condition](img/null_condition.gif)

> ```
> expr IS [ NOT ] NULL
> ```
  
  

Table 7-9 lists the null conditions.

Table 7-9 Null Condition

| Type of Condition | Operation | Example |
| --- | --- | --- |
| ``` IS [NOT] NULL ``` | Tests for nulls.  See Also: ["Nulls"](sql_elements005.md) | ``` SELECT last_name   FROM employees   WHERE commission_pct   IS NULL   ORDER BY last_name; ``` |