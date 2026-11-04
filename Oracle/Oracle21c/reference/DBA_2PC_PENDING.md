---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_2PC_PENDING.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.2 DBA\_2PC\_PENDING

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `LOCAL_TRAN_ID` | `VARCHAR2(22)` | `NOT NULL` | String of form: n.n.n; n is a number |
| `GLOBAL_TRAN_ID` | `VARCHAR2(169)` |  | Globally unique transaction ID |
| `STATE` | `VARCHAR2(16)` | `NOT NULL` | Collecting, prepared, committed, forced commit, or forced rollback |
| `MIXED` | `VARCHAR2(3)` |  | `YES` indicates part of the transaction committed and part rolled back |
| `ADVICE` | `VARCHAR2(1)` |  | `C` for commit, `R` for rollback, else `NULL` |
| `TRAN_COMMENT` | `VARCHAR2(255)` |  | Text for commit work comment text |
| `FAIL_TIME` | `DATE` | `NOT NULL` | Value of `SYSDATE` when the row was inserted (transaction or system recovery) |
| `FORCE_TIME` | `DATE` |  | Time of manual force decision (null if not forced locally) |
| `RETRY_TIME` | `DATE` | `NOT NULL` | Time automatic recovery (`RECO`) last tried to recover the transaction |
| `OS_USER` | `VARCHAR2(64)` |  | Operating system-specific name for the end-user |
| `OS_TERMINAL` | `VARCHAR2(255)` |  | Operating system-specific name for the end-user terminal |
| `HOST` | `VARCHAR2(128)` |  | Name of the host system for the end-user |
| `DB_USER ` | `VARCHAR2(128)` |  | Oracle user name of the end-user at the topmost database |
| `COMMIT#` | `VARCHAR2(16)` |  | Global commit number for committed transactions |