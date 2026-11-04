---
title: RC_DATABASE
book: Backup and Recovery Reference
doc_id: E10643-09
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews027.htm
tags:
  - oracle
  - 11g
  - backup-and-recovery-reference
---

This view gives information about the databases registered in the recovery catalog. It corresponds to the `V$DATABASE` view.

| Column | Data Type | Description |
| --- | --- | --- |
| `DB_KEY` | `NUMBER` | The primary key for the database. Use this column to join with almost any other catalog view. |
| `DBINC_KEY` | `NUMBER` | The primary key for the current incarnation. Use this column to join with `RC_DATABASE_INCARNATION`. |
| `DBID` | `NUMBER` | Unique identifier for the database obtained from `V$DATABASE`. |
| `NAME` | `VARCHAR2(8)` | The `DB_NAME` of the database for the current incarnation. |
| `RESETLOGS_CHANGE#` | `NUMBER` | The SCN of the `RESETLOGS` of the current database incarnation. |
| `RESETLOGS_TIME` | `DATE` | The timestamp of the `RESETLOGS` of the current database incarnation. |