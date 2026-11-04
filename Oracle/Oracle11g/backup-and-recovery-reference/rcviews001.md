---
title: Summary of RMAN Recovery Catalog Views
book: Backup and Recovery Reference
doc_id: E10643-09
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews001.htm
tags:
  - oracle
  - 11g
  - backup-and-recovery-reference
---

The following table provides a functional summary of RMAN recovery catalog views.

Table 5-1 Recovery Catalog Views

| Recovery Catalog View | Corresponding V$ View | Catalog View Describes... |
| --- | --- | --- |
| `RC_ARCHIVED_LOG` | [`V$ARCHIVED_LOG`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1016.htm#REFRN30011) | Archived and unarchived redo log files |
| `RC_BACKUP_ARCHIVELOG_DETAILS` | [`V$BACKUP_ARCHIVELOG_DETAILS`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1045.htm#REFRN30362) | Details about archived redo log backups for Enterprise Manager |
| `RC_BACKUP_ARCHIVELOG_SUMMARY` | [`V$BACKUP_ARCHIVELOG_SUMMARY`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1046.htm#REFRN30363) | Summary of information about archived redo log backups for Enterprise Manager |
| `RC_BACKUP_CONTROLFILE` | [`V$BACKUP_DATAFILE`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1053.htm#REFRN30020) | Control files backed up in backup sets |
| `RC_BACKUP_CONTROLFILE_DETAILS` | [`V$BACKUP_CONTROLFILE_DETAILS`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1048.htm#REFRN30364) | Details about control file backups for Enterprise Manager |
| `RC_BACKUP_CONTROLFILE_SUMMARY` | [`V$BACKUP_CONTROLFILE_SUMMARY`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1049.htm#REFRN30365) | Summary of information about control file backups for Enterprise Manager |
| `RC_BACKUP_COPY_DETAILS` | [`V$BACKUP_COPY_DETAILS`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1050.htm#REFRN30366) | Details about data file image copy backups for Enterprise Manager |
| `RC_BACKUP_COPY_SUMMARY` | [`V$BACKUP_COPY_SUMMARY`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1051.htm#REFRN30367) | Summary of information about data file image copy backups for Enterprise Manager |
| `RC_BACKUP_CORRUPTION` | [`V$BACKUP_CORRUPTION`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1052.htm#REFRN30019) | Corrupt block ranges in data file backups |
| `RC_BACKUP_DATAFILE` | [`V$BACKUP_DATAFILE`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1053.htm#REFRN30020) | Data files in backup sets |
| `RC_BACKUP_DATAFILE_DETAILS` | [`V$BACKUP_DATAFILE_DETAILS`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1054.htm#REFRN30368) | Details about data file backups for Enterprise Manager |
| `RC_BACKUP_DATAFILE_SUMMARY` | [`V$BACKUP_DATAFILE_SUMMARY`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1055.htm#REFRN30369) | Summary of information about data file backups for Enterprise Manager |
| `RC_BACKUP_FILES` | [`V$BACKUP_FILES`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1057.htm#REFRN30022) | RMAN backups and copies known to the repository. |
| `RC_BACKUP_PIECE` | [`V$BACKUP_PIECE`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1058.htm#REFRN30023) | Backup pieces |
| `RC_BACKUP_PIECE_DETAILS` | [`V$BACKUP_PIECE_DETAILS`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1059.htm#REFRN30370) | Details about backup pieces for Enterprise Manager |
| `RC_BACKUP_REDOLOG` | [`V$BACKUP_REDOLOG`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1060.htm#REFRN30024) | Archived redo log files in backup sets |
| `RC_BACKUP_SET` | [`V$BACKUP_SET`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1061.htm#REFRN30025) | Backup sets for all incarnations of databases registered in the catalog |
| `RC_BACKUP_SET_DETAILS` | [`V$BACKUP_SET_DETAILS`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1062.htm#REFRN30371) | Details about backup sets for Enterprise Manager |
| `RC_BACKUP_SET_SUMMARY` | [`V$BACKUP_SET_SUMMARY`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1063.htm#REFRN30372) | Summary of information about backup sets for Enterprise Manager |
| `RC_BACKUP_SPFILE` | [`V$BACKUP_SPFILE`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1064.htm#REFRN30026) | Server parameter files in backups |
| `RC_BACKUP_SPFILE_DETAILS` | [`V$BACKUP_SPFILE_DETAILS`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1065.htm#REFRN30373) | Details about server parameter file backups for Enterprise Manager |
| `RC_BACKUP_SPFILE_SUMMARY` | [`V$BACKUP_SPFILE_SUMMARY`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1066.htm#REFRN30374) | Summary of information about server parameter file backups for Enterprise Manager |
| `RC_CHECKPOINT` | n/a | Deprecated in favor of [RC\_RESYNC](rcviews044.md) |
| `RC_CONTROLFILE_COPY` | [`V$DATAFILE_COPY`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1101.htm#REFRN30051) | Control file copies on disk |
| `RC_COPY_CORRUPTION` | [`V$COPY_CORRUPTION`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1089.htm#REFRN30045) | Corrupt block ranges in data file copies |
| `RC_DATABASE` | [`V$DATABASE`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1097.htm#REFRN30047) | Databases registered in the recovery catalog |
| `RC_DATABASE_BLOCK_CORRUPTION` | [`V$DATABASE_BLOCK_CORRUPTION`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1098.htm#REFRN30048) | Database blocks marked as corrupted in the most recent RMAN backup or copy |
| `RC_DATABASE_INCARNATION` | [`V$DATABASE_INCARNATION`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1099.htm#REFRN30049) | Database incarnations registered in the recovery catalog |
| `RC_DATAFILE` | [`V$DATAFILE`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1100.htm#REFRN30050) | Data files registered in the recovery catalog |
| `RC_DATAFILE_COPY` | [`V$DATAFILE_COPY`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1101.htm#REFRN30051) | Data file copies on disk |
| `RC_LOG_HISTORY` | [`V$LOG_HISTORY`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2032.htm#REFRN30128) | Online redo log history indicating when log switches occurred |
| `RC_OFFLINE_RANGE` | [`V$OFFLINE_RANGE`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2082.htm#REFRN30165) | Offline ranges for data files |
| `RC_PROXY_ARCHIVEDLOG` | [`V$PROXY_ARCHIVEDLOG`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2105.htm#REFRN30187) | Archived log backups taken with the proxy copy functionality |
| `RC_PROXY_ARCHIVELOG_DETAILS` | [`V$PROXY_ARCHIVELOG_DETAILS`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2106.htm#REFRN30386) | Details about proxy archived redo log files for Enterprise Manager |
| `RC_PROXY_ARCHIVELOG_SUMMARY` | [`V$PROXY_ARCHIVELOG_SUMMARY`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2107.htm#REFRN30387) | Summary of information about proxy archived redo log files for Enterprise Manager |
| `RC_PROXY_CONTROLFILE` | [`V$PROXY_DATAFILE`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2110.htm#REFRN30188) | Control file backups taken with the proxy copy functionality |
| `RC_PROXY_COPY_DETAILS` | [`V$PROXY_COPY_DETAILS`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2108.htm#REFRN30388) | Details about data file proxy copies for Enterprise Manager |
| `RC_PROXY_COPY_SUMMARY` | [`V$PROXY_COPY_SUMMARY`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2109.htm#REFRN30389) | Summary of information about data file proxy copies for Enterprise Manager |
| `RC_PROXY_DATAFILE` | [`V$PROXY_DATAFILE`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2110.htm#REFRN30188) | Data file backups that were taken using the proxy copy functionality |
| `RC_REDO_LOG` | [`V$LOG`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2031.htm#REFRN30127) and [`V$LOGFILE`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2033.htm#REFRN30129) | Online redo logs for all incarnations of the database since the last catalog resynchronization |
| `RC_REDO_THREAD` | [`V$THREAD`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3109.htm#REFRN30288) | All redo threads for all incarnations of the database since the last catalog resynchronization |
| `RC_RESTORE_POINT` | [`V$RESTORE_POINT`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2137.htm#REFRN30390) | All restore points for all incarnations of the database since the last catalog resynchronization |
| `RC_RESYNC` | n/a | Recovery catalog resynchronizations |
| `RC_RMAN_BACKUP_JOB_DETAILS` | [`V$RMAN_BACKUP_JOB_DETAILS`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2142.htm#REFRN30391) | Details about backup jobs for Enterprise Manager |
| `RC_RMAN_BACKUP_SUBJOB_DETAILS` | [`V$RMAN_BACKUP_SUBJOB_DETAILS`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2143.htm#REFRN30392) | Details about backup subjobs for Enterprise Manager |
| `RC_RMAN_BACKUP_TYPE` | [`V$RMAN_BACKUP_TYPE`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2144.htm#REFRN30411) | Used internally by Enterprise Manager |
| `RC_RMAN_CONFIGURATION` | [`V$RMAN_CONFIGURATION`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2146.htm#REFRN30208) | RMAN configuration settings |
| `RC_RMAN_OUTPUT` | [`V$RMAN_OUTPUT`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2148.htm#REFRN30305) | Output from RMAN commands for use in Enterprise Manager |
| `RC_RMAN_STATUS` | [`V$RMAN_STATUS`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2149.htm#REFRN30306) | Historical status information about RMAN operations. |
| `RC_SITE` | n/a | Databases in a Data Guard environment |
| `RC_STORED_SCRIPT` | n/a | Names of scripts stored in the recovery catalog |
| `RC_STORED_SCRIPT_LINE` | n/a | Contents of the scripts stored in the recovery catalog |
| `RC_TABLESPACE` | [`V$TABLESPACE`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3100.htm#REFRN30277) | All tablespaces registered in the recovery catalog, all dropped tablespaces, and tablespaces that belong to old incarnations |
| `RC_TEMPFILE` | [`V$TEMPFILE`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3105.htm#REFRN30283) | All temp files registered in the recovery catalog |
| `RC_UNUSABLE_BACKUPFILE_DETAILS` | [`V$UNUSABLE_BACKUPFILE_DETAILS`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3119.htm#REFRN30398) | Unusable backup files registered in the recovery catalog |