---
title: EXISTS Condition
book: SQL Language Reference
doc_id: E41084-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41084/conditions012.htm
tags:
  - oracle
  - 11g
  - sql-language-reference
---

An `EXISTS` condition tests for existence of rows in a subquery.

  
[Description of the illustration ''exists\_condition.gif''](https://docs.oracle.com/cd/E11882_01/server.112/e41084/img_text/exists_condition.htm)  
  

Table 7-11 shows the `EXISTS` condition.

Table 7-11 EXISTS Condition

| Type of Condition | Operation | Example |
| --- | --- | --- |
| ``` EXISTS ``` | `TRUE` if a subquery returns at least one row. | ``` SELECT department_id   FROM departments d   WHERE EXISTS   (SELECT * FROM employees e     WHERE d.department_id      = e.department_id)    ORDER BY department_id; ``` |