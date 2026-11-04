---
title: SQL Language Reference
book: SQL Language Reference
doc_id: F31301-19
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqlrf/Compound-Conditions.html
tags:
  - oracle
  - 21c
  - sql-language-reference
---

## Compound Conditions

A compound condition specifies a combination of other conditions.

compound\_condition::=

![compound_condition](img/compound_condition.gif)

> ```
> { (condition)
> | NOT condition
> | condition { AND | OR } condition
> }
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2025, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


See Also:

[Logical Conditions](Logical-Conditions.md) for more information about `NOT`, `AND`, and `OR` conditions