---
title: PATH
book: SQL Language Reference
doc_id: E96310-37
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/PATH.html
tags:
  - oracle
  - 19c
  - sql-language-reference
---

## Syntax

![path](img/path.gif)

> ```
> PATH(correlation_integer)
> ```
>
> [Copyright ©](https://docs.oracle.com/pls/topic/lookup?ctx=en/legal&id=cpyr) 2026,1996, Oracle and/or its affiliates.


[Description of the illustration path.eps](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/img_text/path.html)

## Purpose

`PATH` is an ancillary function used only with the `UNDER_PATH` and `EQUALS_PATH` conditions. It returns the relative path that leads to the resource specified in the parent condition.

The *correlation\_integer* can be any `NUMBER` integer and is used to correlate this ancillary function with its primary condition. Values less than 1 are treated as 1.

**See Also:**

- [EQUALS\_PATH Condition](XML-Conditions.md) and [UNDER\_PATH Condition](XML-Conditions.md)
- in [*Oracle Database Globalization Support Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/sqlrf&id=NLSPG-GUID-AFCE41ED-775B-4A00-AF38-C436776AE0C5) for the collation derivation rules, which define the collation assigned to the character return value of `PATH`

## Examples

Refer to the related function [DEPTH](DEPTH.md) for an example using both of these ancillary functions of the `EQUALS_PATH` and `UNDER_PATH` conditions.