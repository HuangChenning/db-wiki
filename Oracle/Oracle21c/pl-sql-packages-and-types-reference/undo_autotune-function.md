---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/undo_autotune-function.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 192.1.7 UNDO\_AUTOTUNE Function

This function finds out whether the auto-tuning of undo retention is enabled for the current undo tablespace.

Syntax

```
DBMS_UNDO_ADV.UNDO_AUTOTUNE(
     chk OUT BOOLEAN)
RETURN BOOLEAN;
```

Parameters

Table 192-8 UNDO\_AUTOTUNE Function Parameters

| Parameter | Description |
| --- | --- |
| `chk` | `TRUE` if auto-tuning of undo retention is enabled, `FALSE` otherwise. |