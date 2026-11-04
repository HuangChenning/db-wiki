---
title: DBMS_AUTO_TASK_IMMEDIATE
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_autotaskimmed.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 30 DBMS\_AUTO\_TASK\_IMMEDIATE

The `DBMS_AUTO_TASK_IMMEDIATE` package consists of one subprogram whose function is to initiate gathering of optimizer statistics without delay.

This chapter contains the following topics:

- Summary of DBMS\_AUTO\_TASK\_IMMEDIATE Subprograms

---

## Summary of DBMS\_AUTO\_TASK\_IMMEDIATE Subprograms

Table 30-1 DBMS\_AUTO\_TASK\_IMMEDIATE Subprograms

| Subprogram | Description |
| --- | --- |
| GATHER\_OPTIMIZER\_STATS Procedure | Initiates gathering of optimizer statistics without waiting for the start of a maintenance window |

---

### GATHER\_OPTIMIZER\_STATS Procedure

This procedure initiates gathering of optimizer statistics without waiting for the start of a maintenance window.

Syntax

```
DBMS_AUTO_TASK_IMMEDIATE.GATHER_OPTIMIZER_STATS;
```