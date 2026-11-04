---
title: Placeholder Expressions
book: SQL Language Reference
doc_id: E41084-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41084/expressions012.htm
tags:
  - oracle
  - 11g
  - sql-language-reference
---

A placeholder expression provides a location in a SQL statement for which a third-generation language bind variable will provide a value. You can specify the placeholder expression with an optional indicator variable. This form of expression can appear only in embedded SQL statements or SQL statements processed in an Oracle Call Interface (OCI) program.

placeholder\_expression::=

![placeholder_expression](img/placeholder_expression.gif)

> ```
> :host_variable
>    [ [ INDICATOR ]
>      :indicator_variable
>    ]
> ```
  
  

Some valid placeholder expressions are:

```
:employee_name INDICATOR :employee_name_indicator_var
:department_location
```