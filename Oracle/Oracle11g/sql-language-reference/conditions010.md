---
title: Compound Conditions
book: SQL Language Reference
doc_id: E41084-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41084/conditions010.htm
tags:
  - oracle
  - 11g
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

["Logical Conditions"](conditions004.md) for more information about `NOT`, `AND`, and `OR` conditions