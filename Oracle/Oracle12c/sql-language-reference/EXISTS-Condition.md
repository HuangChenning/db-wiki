---
title: SQL Language Reference
book: SQL Language Reference
doc_id: E83703-08
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/sqlrf/EXISTS-Condition.html
tags:
  - oracle
  - 12c
  - sql-language-reference
---

An `EXISTS` condition tests for existence of rows in a subquery.

![exists_condition](img/exists_condition.gif)

> ```
> EXISTS (subquery)
> ```


Table 6-11 shows the `EXISTS` condition.

Table 6-11 EXISTS Condition

| Type of Condition | Operation | Example |
| --- | --- | --- |
| ``` EXISTS ``` | `TRUE` if a subquery returns at least one row. | ``` SELECT department_id   FROM departments d   WHERE EXISTS   (SELECT * FROM employees e     WHERE d.department_id      = e.department_id)    ORDER BY department_id; ``` |