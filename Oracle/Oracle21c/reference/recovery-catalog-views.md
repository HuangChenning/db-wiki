---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/recovery-catalog-views.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.10 Recovery Catalog Views

The following data dictionary views are only available after you create an optional recovery catalog (which contains schemas containing information about backups) for use with Recovery Manager:

- [`RC_ARCHIVED_LOG`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RCMRF163)
- [`RC_BACKUP_ARCHIVELOG_DETAILS`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RCMRF1924)
- [`RC_BACKUP_ARCHIVELOG_SUMMARY`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RCMRF1925)
- [`RC_BACKUP_CONTROLFILE`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RCMRF164)
- [`RC_BACKUP_CONTROLFILE_DETAILS`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RCMRF1926)
- [`RC_BACKUP_CONTROLFILE_SUMMARY`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RCMRF1927)
- [`RC_BACKUP_COPY_DETAILS`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RCMRF1928)
- [`RC_BACKUP_COPY_SUMMARY`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RCMRF1929)
- [`RC_BACKUP_CORRUPTION`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RCMRF165)
- [`RC_BACKUP_DATAFILE`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RCMRF1964)
- [`RC_BACKUP_DATAFILE_DETAILS`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RCMRF1930)
- [`RC_BACKUP_DATAFILE_SUMMARY`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RCMRF1931)
- [`RC_BACKUP_FILES`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RCMRF1670)
- [`RC_BACKUP_PIECE`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RCMRF167)
- [`RC_BACKUP_PIECE_DETAILS`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RCMRF1933)
- [`RC_BACKUP_REDOLOG`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RCMRF168)
- [`RC_BACKUP_SET`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RCMRF169)
- [`RC_BACKUP_SET_DETAILS`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RCMRF1934)
- [`RC_BACKUP_SET_SUMMARY`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RCMRF1935)
- [`RC_BACKUP_SPFILE`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RCMRF189)
- [`RC_BACKUP_SPFILE_DETAILS`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RCMRF1936)
- [`RC_BACKUP_SPFILE_SUMMARY`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RCMRF1937)
- [`RC_CHECKPOINT`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RCMRF170)
- [`RC_CONTROLFILE_COPY`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RCMRF171)
- [`RC_COPY_CORRUPTION`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RCMRF172)
- [`RC_DATABASE`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RCMRF173)
- [`RC_DATABASE_BLOCK_CORRUPTION`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RCMRF188)
- [`RC_DATABASE_INCARNATION`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RCMRF174)
- [`RC_DATAFILE`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RCMRF175)
- [`RC_DATAFILE_COPY`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RCMRF176)
- [`RC_LOG_HISTORY`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RCMRF177)
- [`RC_OFFLINE_RANGE`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RCMRF178)
- [`RC_PROXY_ARCHIVEDLOG`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RCMRF1938)
- [`RC_PROXY_ARCHIVELOG_DETAILS`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RCMRF1939)
- [`RC_PROXY_ARCHIVELOG_SUMMARY`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RCMRF1940)
- [`RC_PROXY_CONTROLFILE`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RCMRF179)
- [`RC_PROXY_COPY_DETAILS`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RCMRF1941)
- [`RC_PROXY_COPY_SUMMARY`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RCMRF1942)
- [`RC_PROXY_DATAFILE`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RCMRF180)
- [`RC_REDO_LOG`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RCMRF181)
- [`RC_REDO_THREAD`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RCMRF182)
- [`RC_RESTORE_POINT`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RCMRF202)
- [`RC_RESYNC`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RCMRF183)
- [`RC_RMAN_BACKUP_JOB_DETAILS`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RCMRF1943)
- [`RC_RMAN_BACKUP_SUBJOB_DETAILS`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RCMRF1944)
- [`RC_RMAN_BACKUP_TYPE`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RCMRF1945)
- [`RC_RMAN_CONFIGURATION`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RCMRF184)
- [`RC_RMAN_OUTPUT`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RCMRF1946)
- [`RC_RMAN_STATUS`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RCMRF381)
- [`RC_SITE`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RCMRF1953)
- [`RC_STORED_SCRIPT`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RCMRF185)
- [`RC_STORED_SCRIPT_LINE`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RCMRF186)
- [`RC_TABLESPACE`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RCMRF187)
- [`RC_TEMPFILE`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RCMRF1870)
- [`RC_UNUSABLE_BACKUPFILE_DETAILS`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RCMRF1947)

See Also:

[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RCMRF003) for information about these views