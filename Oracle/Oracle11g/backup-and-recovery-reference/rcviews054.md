---
title: RC_TABLESPACE
book: Backup and Recovery Reference
doc_id: E10643-09
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews054.htm
tags:
  - oracle
  - 11g
  - backup-and-recovery-reference
---

This view lists all tablespaces registered in the recovery catalog, all dropped tablespaces, and tablespaces that belong to old incarnations. It corresponds to the `V$TABLESPACE` view. The current value is shown for tablespace attributes.

| Column | Data Type | Description |
| --- | --- | --- |
| `DB_KEY` | `NUMBER` | The primary key for the target database. Use this column to join with almost any other catalog view. |
| `DBINC_KEY` | `NUMBER` | The primary key for the incarnation of the target database. Use this column to join with `RC_DATABASE_INCARNATION`. |
| `DB_NAME` | `VARCHAR2(8)` | The `DB_NAME` of the database incarnation to which this record belongs. |
| `TS#` | `NUMBER` | The tablespace ID in the target database. The `TS#` may exist multiple times in the same incarnation if the tablespace is dropped and re-created. |
| `NAME` | `VARCHAR2(30)` | The tablespace name. The name may exist multiple times in the same incarnation if the tablespace is dropped and re-created. |
| `CREATION_CHANGE#` | `NUMBER` | The creation SCN (from the first data file). |
| `CREATION_TIME` | `DATE` | The creation time of the tablespace. `NULL` for offline tablespaces after creating the control file. |
| `DROP_CHANGE#` | `NUMBER` | The SCN recorded when the tablespace was dropped. If a new tablespace with the same `TS#` is discovered, then the `DROP_CHANGE#` is set to `CREATION_CHANGE#` for the tablespace; otherwise, the value is set to `RC_CHECKPOINT.CKP_SCN`. |
| `DROP_TIME` | `DATE` | The date when the tablespace was dropped. |
| `INCLUDED_IN_DATABASE_BACKUP` | `VARCHAR2(3)` | Indicates whether this tablespace is included in whole database backups: `YES` or `NO`. The `YES` value occurs only if `CONFIGURE EXCLUDE` was run on the tablespace that owns this data file. |
| `BIGFILE` | `VARCHAR2(3)` | Indicates whether this tablespace is a tablespace created with the `BIGFILE` option. |
| `TEMPORARY` | `VARCHAR2(3)` | `YES` if tablespace is a locally managed temporary tablespace. Otherwise, `NO`. |
| `ENCRYPT_IN_BACKUP` | `VARCHAR2(3)` | Possible values are: - `ON`. Encryption is turned `ON` at tablespace level - `OFF`. Encryption is turned `OFF` at tablespace level - `NULL`. Encryption is neither explicitly turned on or off at tablespace level (default or when `CLEARED`) |