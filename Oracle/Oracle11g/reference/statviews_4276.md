---
title: DBA_SQL_PATCHES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4276.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_SQL_PATCHES` displays the set of SQL patches.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the SQL patch |
| `CATEGORY` | `VARCHAR2(30)` | `NOT NULL` | Category of the SQL patch |
| `SIGNATURE` | `NUMBER` | `NOT NULL` | Unique identifier generated from normalized SQL text |
| `SQL_TEXT` | `CLOB` | `NOT NULL` | Un-normalized SQL text |
| `CREATED` | `TIMESTAMP(6)` | `NOT NULL` | Timestamp when the SQL patch was created |
| `LAST_MODIFIED` | `TIMESTAMP(6)` |  | Timestamp when the SQL patch was last modified |
| `DESCRIPTION` | `VARCHAR2(500)` |  | Text description provided for the SQL patch |
| `STATUS` | `VARCHAR2(8)` |  | Status of the SQL patch: |
| `FORCE_MATCHING` | `VARCHAR2(3)` |  | Indicates whether the signature is force matching (`YES`) or exact matching (`NO`) |
| `TASK_ID` | `NUMBER` |  | Advisor task ID that generated the SQL patch |
| `TASK_EXEC_NAME` | `VARCHAR2(30)` |  | Advisor execution name for the SQL patch |
| `TASK_OBJ_ID` | `NUMBER` |  | Advisor object ID for the SQL patch |
| `TASK_FND_ID` | `NUMBER` |  | Advisor finding ID for the SQL patch |
| `TASK_REC_ID` | `NUMBER` |  | Advisor recommendation ID for the SQL patch |