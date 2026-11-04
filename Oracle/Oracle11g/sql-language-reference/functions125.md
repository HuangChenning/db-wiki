---
title: PATH
book: SQL Language Reference
doc_id: E41084-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41084/functions125.htm
tags:
  - oracle
  - 11g
  - sql-language-reference
---

Syntax

  
[Description of the illustration ''path.gif''](https://docs.oracle.com/cd/E11882_01/server.112/e41084/img_text/path.htm)  
  

Purpose

`PATH` is an ancillary function used only with the `UNDER_PATH` and `EQUALS_PATH` conditions. It returns the relative path that leads to the resource specified in the parent condition.

The `correlation_integer` can be any `NUMBER` integer and is used to correlate this ancillary function with its primary condition. Values less than 1 are treated as 1.

See Also:

[EQUALS\_PATH Condition](conditions009.md) and [UNDER\_PATH Condition](conditions009.md)

Examples

Refer to the related function [DEPTH](functions053.md) for an example using both of these ancillary functions of the `EQUALS_PATH` and `UNDER_PATH` conditions.