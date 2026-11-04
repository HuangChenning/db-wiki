---
title: DEPTH
book: SQL Language Reference
doc_id: E96310-37
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/DEPTH.html
tags:
  - oracle
  - 19c
  - sql-language-reference
---

## Syntax

![depth](img/depth.gif)

> ```
> DEPTH(correlation_integer)
> ```
>
> [Copyright ©](https://docs.oracle.com/pls/topic/lookup?ctx=en/legal&id=cpyr) 2026,1996, Oracle and/or its affiliates.


[Description of the illustration depth.eps](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/img_text/depth.html)

## Purpose

`DEPTH` is an ancillary function used only with the `UNDER_PATH` and `EQUALS_PATH` conditions. It returns the number of levels in the path specified by the `UNDER_PATH` condition with the same correlation variable.

The *correlation\_integer* can be any `NUMBER` integer. Use it to correlate this ancillary function with its primary condition if the statement contains multiple primary conditions. Values less than 1 are treated as 1.

**See Also:** [EQUALS\_PATH Condition](XML-Conditions.md), [UNDER\_PATH Condition](XML-Conditions.md), and the related function [PATH](PATH.md)

## Examples

The `EQUALS_PATH` and `UNDER_PATH` conditions can take two ancillary functions, `DEPTH` and `PATH`. The following example shows the use of both ancillary functions. The example assumes the existence of the XMLSchema `warehouses.xsd` (created in [Using XML in SQL Statements](Using-XML-in-SQL-Statements.md)).

```md
SELECT PATH(1), DEPTH(2)
  FROM RESOURCE_VIEW
  WHERE UNDER_PATH(res, '/sys/schemas/OE', 1)=1
    AND UNDER_PATH(res, '/sys/schemas/OE', 2)=1;

PATH(1)                          DEPTH(2)
-------------------------------- --------
. . .
www.example.com                         1
www.example.com/xwarehouses.xsd         2
. . .
```