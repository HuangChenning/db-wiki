---
title: SQL Language Reference
book: SQL Language Reference
doc_id: F31301-19
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqlrf/Null-Conditions.html
tags:
  - oracle
  - 21c
  - sql-language-reference
---

## Null Conditions

A `NULL` condition tests for nulls. This is the only condition that you should use to test for nulls.

null\_condition::=

![null_condition](img/null_condition.gif)

> ```
> expr IS [ NOT ] NULL
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2025, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


Table 6-9 lists the null conditions.

Table 6-9 Null Condition

| Type of Condition | Operation | Example |
| --- | --- | --- |
| ``` IS [NOT] NULL ``` | Tests for nulls.  See Also: [Nulls](Nulls.md) | ``` SELECT last_name   FROM employees   WHERE commission_pct   IS NULL   ORDER BY last_name; ``` |