---
title: UID
book: SQL Language Reference
doc_id: E41084-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41084/functions223.htm
tags:
  - oracle
  - 11g
  - sql-language-reference
---

Syntax

  
[Description of the illustration ''uid.gif''](https://docs.oracle.com/cd/E11882_01/server.112/e41084/img_text/uid.htm)  
  

Purpose

`UID` returns an integer that uniquely identifies the session user (the user who logged on).

Examples

The following example returns the UID of the current user:

```
SELECT UID FROM DUAL;
```