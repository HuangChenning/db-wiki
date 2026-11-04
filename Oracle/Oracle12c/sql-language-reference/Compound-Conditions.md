---
title: SQL Language Reference
book: SQL Language Reference
doc_id: E83703-08
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/sqlrf/Compound-Conditions.html
tags:
  - oracle
  - 12c
  - sql-language-reference
---

A compound condition specifies a combination of other conditions.

compound\_condition::=

![compound_condition](img/compound_condition.gif)

> ```
> { (condition)
> | NOT condition
> | condition { AND | OR } condition
> }
> ```


See Also:

[Logical Conditions](Logical-Conditions.md) for more information about `NOT`, `AND`, and `OR` conditions