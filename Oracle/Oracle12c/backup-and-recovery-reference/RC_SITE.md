---
title: Database Backup and Recovery Reference
book: Database Backup and Recovery Reference
doc_id: E85640-04
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/rcmrf/RC_SITE.html
tags:
  - oracle
  - 12c
  - backup-and-recovery-reference
---

This view lists information about all databases in a Data Guard environment that are known to the recovery catalog.

You can use this view to obtain the `DB_UNIQUE_NAME` value for views which do not have this column.

| Column | Data Type | Description |
| --- | --- | --- |
| `SITE_KEY` | `NUMBER` | The unique key of this database. You can join the `RC_SITE.SITE_KEY` column with the `RC_SITE` column of other views to determine which `DB_UNIQUE_NAME` is associated with a backup. |
| `DB_KEY` | `NUMBER` | The primary key for this database in the recovery catalog. Use this column to join with almost any other catalog view. |
| `DATABASE_ROLE` | `VARCHAR2(7)` | The role of the database in the Data Guard environment. |
| `CF_CREATE_TIME` | `DATE` | The creation date of the control file. |
| `DB_UNIQUE_NAME` | `VARCHAR2(30)` | The `DB_UNIQUE_NAME` of the database. All databases in a Data Guard environment share the same DBID but different `DB_UNIQUE_NAME` values. |