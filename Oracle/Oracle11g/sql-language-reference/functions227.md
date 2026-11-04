---
title: USER
book: SQL Language Reference
doc_id: E41084-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41084/functions227.htm
tags:
  - oracle
  - 11g
  - sql-language-reference
---

Syntax

  
[Description of the illustration ''user.gif''](https://docs.oracle.com/cd/E11882_01/server.112/e41084/img_text/user.htm)  
  

Purpose

`USER` returns the name of the session user (the user who logged on) with the data type `VARCHAR2`. Oracle Database compares values of this function with blank-padded comparison semantics.

In a distributed SQL statement, the `UID` and `USER` functions together identify the user on your local database. You cannot use these functions in the condition of a `CHECK` constraint.

Examples

The following example returns the current user and the user's UID:

```
SELECT USER, UID FROM DUAL;
```