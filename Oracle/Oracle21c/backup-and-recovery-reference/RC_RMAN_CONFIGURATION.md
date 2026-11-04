---
title: Backup and Recovery Reference
book: Database Backup and Recovery Reference
doc_id: F31837-09
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/rcmrf/RC_RMAN_CONFIGURATION.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-reference
---

This view lists information about RMAN persistent configuration settings. It corresponds to the `V$RMAN_CONFIGURATION` view.

| Column | Data Type | Description |
| --- | --- | --- |
| `DB_KEY` | `NUMBER` | The primary key for the target database corresponding to this configuration. Use this column to join with almost any other catalog view. |
| `CONF#` | `NUMBER` | A unique key identifying this configuration record within the target database that owns it. |
| `NAME` | `VARCHAR2(65)` | The type of configuration. All options of `CONFIGURE` command are valid types except:` CONFIGURE EXCLUDE`, (described in `RC_TABLESPACE`), `CONFIGURE AUXNAME` (described in `RC_DATAFILE`), and `CONFIGURE SNAPSHOT CONTROLFILE` (stored only in control file). |
| `VALUE` | `VARCHAR2(1025)` | The `CONFIGURE` command setting. For example: `RETENTION POLICY TO RECOVERY WINDOW OF 1 DAYS`. |
| `DB_UNIQUE_NAME` | `VARCHAR2(512)` | The `DB_UNIQUE_NAME` of the database incarnation to which this record belongs. All databases in a Data Guard environment share the same DBID but different `DB_UNIQUE_NAME` values. The value in this column is null when the database name is not known for a specific file. For example, rows for databases managed by versions of RMAN before Oracle Database 11g are null. |
| `SITE_KEY` | `NUMBER` | Primary key of the Data Guard database associated with this configuration. Each database in a Data Guard environment has a unique `SITE_KEY` value. You can use `SITE_KEY` in a join with the `RC_SITE` view to obtain the `DB_UNIQUE_NAME` of the database. |