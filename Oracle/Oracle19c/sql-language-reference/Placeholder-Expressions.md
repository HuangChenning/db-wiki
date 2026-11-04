---
title: Placeholder Expressions
book: SQL Language Reference
doc_id: E96310-37
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/Placeholder-Expressions.html
tags:
  - oracle
  - 19c
  - sql-language-reference
---

A placeholder expression provides a location in a SQL statement for which a third-generation language bind variable will provide a value. You can specify the placeholder expression with an optional indicator variable. This form of expression can appear only in embedded SQL statements or SQL statements processed in an Oracle Call Interface (OCI) program.

## placeholder\_expression::=

![placeholder_expression](img/placeholder_expression.gif)

> ```
> :host_variable
>    [ [ INDICATOR ]
>      :indicator_variable
>    ]
> ```
>
> [Copyright ©](https://docs.oracle.com/pls/topic/lookup?ctx=en/legal&id=cpyr) 2026,1996, Oracle and/or its affiliates.


[Description of the illustration placeholder\_expression.eps](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/img_text/placeholder_expression.html)

Some valid placeholder expressions are:

```md
:employee_name INDICATOR :employee_name_indicator_var
:department_location
```

**See Also:** in [*Oracle Database Globalization Support Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/sqlrf&id=NLSPG-GUID-AFCE41ED-775B-4A00-AF38-C436776AE0C5) for the collation derivation rules for the placeholder expression with a character data type