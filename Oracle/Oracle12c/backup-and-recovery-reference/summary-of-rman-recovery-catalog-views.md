---
title: Database Backup and Recovery Reference
book: Database Backup and Recovery Reference
doc_id: E85640-04
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/rcmrf/summary-of-rman-recovery-catalog-views.html
tags:
  - oracle
  - 12c
  - backup-and-recovery-reference
---

RMAN recovery catalog views store information about backups of all databases that are registered with the recovery catalog.

The following table provides a functional summary of RMAN recovery catalog views.

Note:

The data type of some recovery catalog view columns is listed as `VARCHAR2(4000)`. This length for `VARCHAR2` columns is applicable when the initialization parameter `VARCHAR2_MAX_SIZE` is set to LEGACY. If you set the value of `VARCHAR2_MAX_SIZE` to 32767, the columns with data type listed as `VARCHAR2(4000)` will be `VARCHAR2(32767)`.

Table 5-1 Recovery Catalog Views

| Recovery Catalog View | Corresponding V$ View | Catalog View Description |
| --- | --- | --- |
| `RC_ARCHIVED_LOG` | [`V$ARCHIVED_LOG`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/rcmrf&id=REFRN30011) | Archived and unarchived redo log files |
| `RC_BACKUP_ARCHIVELOG_DETAILS` | [`V$BACKUP_ARCHIVELOG_DETAILS`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/rcmrf&id=REFRN30362) | Details about archived redo log backups for Enterprise Manager |
| `RC_BACKUP_ARCHIVELOG_SUMMARY` | [`V$BACKUP_ARCHIVELOG_SUMMARY`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/rcmrf&id=REFRN30363) | Summary of information about archived redo log backups for Enterprise Manager |
| `RC_BACKUP_CONTROLFILE` | [`V$BACKUP_DATAFILE`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/rcmrf&id=REFRN30020) | Control files backed up in backup sets |
| `RC_BACKUP_CONTROLFILE_DETAILS` | [`V$BACKUP_CONTROLFILE_DETAILS`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/rcmrf&id=REFRN30364) | Details about control file backups for Enterprise Manager |
| `RC_BACKUP_CONTROLFILE_SUMMARY` | [`V$BACKUP_CONTROLFILE_SUMMARY`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/rcmrf&id=REFRN30365) | Summary of information about control file backups for Enterprise Manager |
| `RC_BACKUP_COPY_DETAILS` | [`V$BACKUP_COPY_DETAILS`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/rcmrf&id=REFRN30366) | Details about data file image copy backups for Enterprise Manager |
| `RC_BACKUP_COPY_SUMMARY` | [`V$BACKUP_COPY_SUMMARY`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/rcmrf&id=REFRN30367) | Summary of information about data file image copy backups for Enterprise Manager |
| `RC_BACKUP_CORRUPTION` | [`V$BACKUP_CORRUPTION`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/rcmrf&id=REFRN30019) | Corrupt block ranges in data file backups |
| `RC_BACKUP_DATAFILE` | [`V$BACKUP_DATAFILE`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/rcmrf&id=REFRN30020) | Data files in backup sets |
| `RC_BACKUP_DATAFILE_DETAILS` | [`V$BACKUP_DATAFILE_DETAILS`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/rcmrf&id=REFRN30368) | Details about data file backups for Enterprise Manager |
| `RC_BACKUP_DATAFILE_SUMMARY` | [`V$BACKUP_DATAFILE_SUMMARY`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/rcmrf&id=REFRN30369) | Summary of information about data file backups for Enterprise Manager |
| `RC_BACKUP_FILES` | [`V$BACKUP_FILES`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/rcmrf&id=REFRN30022) | RMAN backups and copies known to the repository. |
| `RC_BACKUP_PIECE` | [`V$BACKUP_PIECE`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/rcmrf&id=REFRN30023) | Backup pieces |
| `RC_BACKUP_PIECE_DETAILS` | [`V$BACKUP_PIECE_DETAILS`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/rcmrf&id=REFRN30370) | Details about backup pieces for Enterprise Manager |
| `RC_BACKUP_REDOLOG` | [`V$BACKUP_REDOLOG`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/rcmrf&id=REFRN30024) | Archived redo log files in backup sets |
| `RC_BACKUP_SET` | [`V$BACKUP_SET`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/rcmrf&id=REFRN30025) | Backup sets for all incarnations of databases registered in the catalog |
| `RC_BACKUP_SET_DETAILS` | [`V$BACKUP_SET_DETAILS`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/rcmrf&id=REFRN30371) | Details about backup sets for Enterprise Manager |
| `RC_BACKUP_SET_SUMMARY` | [`V$BACKUP_SET_SUMMARY`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/rcmrf&id=REFRN30372) | Summary of information about backup sets for Enterprise Manager |
| `RC_BACKUP_SPFILE` | [`V$BACKUP_SPFILE`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/rcmrf&id=REFRN30026) | Server parameter files in backups |
| `RC_BACKUP_SPFILE_DETAILS` | [`V$BACKUP_SPFILE_DETAILS`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/rcmrf&id=REFRN30373) | Details about server parameter file backups for Enterprise Manager |
| `RC_BACKUP_SPFILE_SUMMARY` | [`V$BACKUP_SPFILE_SUMMARY`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/rcmrf&id=REFRN30374) | Summary of information about server parameter file backups for Enterprise Manager |
| `RC_CHECKPOINT` | n/a | Deprecated in favor of [RC\_RESYNC](RC_RESYNC.md) |
| `RC_CONTROLFILE_COPY` | [`V$DATAFILE_COPY`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/rcmrf&id=REFRN30051) | Control file copies on disk |
| `RC_COPY_CORRUPTION` | [`V$COPY_CORRUPTION`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/rcmrf&id=REFRN30045) | Corrupt block ranges in data file copies |
| `RC_DATABASE` | [`V$DATABASE`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/rcmrf&id=REFRN30047) | Databases registered in the recovery catalog |
| `RC_DATABASE_BLOCK_CORRUPTION` | [`V$DATABASE_BLOCK_CORRUPTION`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/rcmrf&id=REFRN30048) | Database blocks marked as corrupted in the most recent RMAN backup or copy |
| `RC_DATABASE_INCARNATION` | [`V$DATABASE_INCARNATION`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/rcmrf&id=REFRN30049) | Database incarnations registered in the recovery catalog |
| `RC_DATAFILE` | [`V$DATAFILE`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/rcmrf&id=REFRN30050) | Data files registered in the recovery catalog |
| `RC_DATAFILE_COPY` | [`V$DATAFILE_COPY`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/rcmrf&id=REFRN30051) | Data file copies on disk |
| `RC_DISK_RESTORE_RANGE` | `V$DISK_RESTORE_RANGE` | Details about the restore range of the database for backup data stored on disk |
| `RC_LOG_HISTORY` | [`V$LOG_HISTORY`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/rcmrf&id=REFRN30128) | Online redo log history indicating when log switches occurred |
| `RC_OFFLINE_RANGE` | [`V$OFFLINE_RANGE`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/rcmrf&id=REFRN30165) | Offline ranges for data files |
| `RC_PDBS` | [`V$PDBS`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/rcmrf&id=REFRN30652) | Pluggable databases (PDBs) registered in the recovery catalog |
| `RC_PLUGGABLE_DATABASE_INC` | `V$PDB_INCARNATION` | PDB incarnations registered in the recovery catalog |
| `RC_PROXY_ARCHIVEDLOG` | [`V$PROXY_ARCHIVEDLOG`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/rcmrf&id=REFRN30187) | Archived log backups taken with the proxy copy functionality |
| `RC_PROXY_ARCHIVELOG_DETAILS` | [`V$PROXY_ARCHIVELOG_DETAILS`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/rcmrf&id=REFRN30386) | Details about proxy archived redo log files for Enterprise Manager |
| `RC_PROXY_ARCHIVELOG_SUMMARY` | [`V$PROXY_ARCHIVELOG_SUMMARY`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/rcmrf&id=REFRN30387) | Summary of information about proxy archived redo log files for Enterprise Manager |
| `RC_PROXY_CONTROLFILE` | [`V$PROXY_DATAFILE`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/rcmrf&id=REFRN30188) | Control file backups taken with the proxy copy functionality |
| `RC_PROXY_COPY_DETAILS` | [`V$PROXY_COPY_DETAILS`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/rcmrf&id=REFRN30388) | Details about data file proxy copies for Enterprise Manager |
| `RC_PROXY_COPY_SUMMARY` | [`V$PROXY_COPY_SUMMARY`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/rcmrf&id=REFRN30389) | Summary of information about data file proxy copies for Enterprise Manager |
| `RC_PROXY_DATAFILE` | [`V$PROXY_DATAFILE`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/rcmrf&id=REFRN30188) | Data file backups that were taken using the proxy copy functionality |
| `RC_REDO_LOG` | [`V$LOG`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/rcmrf&id=REFRN30127) and [`V$LOGFILE`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/rcmrf&id=REFRN30129) | Online redo logs for all incarnations of the database since the last catalog resynchronization |
| `RC_REDO_THREAD` | [`V$THREAD`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/rcmrf&id=REFRN30288) | All redo threads for all incarnations of the database since the last catalog resynchronization |
| `RC_RESTORE_POINT` | [`V$RESTORE_POINT`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/rcmrf&id=REFRN30390) | All restore points for all incarnations of the database since the last catalog resynchronization |
| `RC_RESTORE_RANGE` | `V$RESTORE_RANGE` | Details about the restore range of databases registered in the recovery catalog |
| `RC_RESYNC` | n/a | Recovery catalog resynchronizations |
| `RC_RMAN_BACKUP_JOB_DETAILS` | [`V$RMAN_BACKUP_JOB_DETAILS`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/rcmrf&id=REFRN30391) | Details about backup jobs for Enterprise Manager |
| `RC_RMAN_BACKUP_SUBJOB_DETAILS` | [`V$RMAN_BACKUP_SUBJOB_DETAILS`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/rcmrf&id=REFRN30392) | Details about backup subjobs for Enterprise Manager |
| `RC_RMAN_BACKUP_TYPE` | [`V$RMAN_BACKUP_TYPE`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/rcmrf&id=REFRN30411) | Used internally by Enterprise Manager |
| `RC_RMAN_CONFIGURATION` | [`V$RMAN_CONFIGURATION`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/rcmrf&id=REFRN30208) | RMAN configuration settings |
| `RC_RMAN_OUTPUT` | [`V$RMAN_OUTPUT`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/rcmrf&id=REFRN30305) | Output from RMAN commands for use in Enterprise Manager |
| `RC_RMAN_STATUS` | [`V$RMAN_STATUS`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/rcmrf&id=REFRN30306) | Historical status information about RMAN operations. |
| `RC_SBT_RESTORE_RANGE` | `V$SBT_RESTORE_RANGE` | Details about the restore range of the database for backup data stored on tape |
| `RC_SITE` | n/a | Databases in a Data Guard environment |
| `RC_STORED_SCRIPT` | n/a | Names of scripts stored in the recovery catalog |
| `RC_STORED_SCRIPT_LINE` | n/a | Contents of the scripts stored in the recovery catalog |
| `RC_TABLESPACE` | [`V$TABLESPACE`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/rcmrf&id=REFRN30277) | All tablespaces registered in the recovery catalog, all dropped tablespaces, and tablespaces that belong to old incarnations |
| `RC_TEMPFILE` | [`V$TEMPFILE`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/rcmrf&id=REFRN30283) | All temp files registered in the recovery catalog |
| `RC_UNUSABLE_BACKUPFILE_DETAILS` | [`V$UNUSABLE_BACKUPFILE_DETAILS`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/rcmrf&id=REFRN30398) | Unusable backup files registered in the recovery catalog |