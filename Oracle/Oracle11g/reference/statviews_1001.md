---
title: About Static Data Dictionary Views
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1001.htm
tags:
  - oracle
  - 11g
  - reference
---

Data dictionary tables are not directly accessible, but you can access information in them through data dictionary views. To list the data dictionary views available to you, query the view `DICTIONARY`.

Many data dictionary tables have three corresponding views:

- An `ALL_` view displays all the information accessible to the current user, including information from the current user's schema as well as information from objects in other schemas, if the current user has access to those objects by way of grants of privileges or roles.
- A `DBA_` view displays all relevant information in the entire database. `DBA_` views are intended only for administrators. They can be accessed only by users with the `SELECT ANY DICTIONARY` privilege. This privilege is assigned to the `DBA` role when the system is initially installed.
- A `USER_` view displays all the information from the schema of the current user. No special privileges are required to query these views.

The columns of the `ALL_`, `DBA_`, and `USER_` views corresponding to a single data dictionary table are usually nearly identical. Therefore, these views are described in full only once in this chapter, at their first occurrence alphabetically, and are listed without full descriptions at their other occurrences.

## Oracle Replication Views

A number of data dictionary views are relevant only if you are using Oracle Replication. Table 2-1 lists these views.

Table 2-1 Oracle Replication Data Dictionary Views

| ALL\_ Views | DBA\_ Views | USER\_ Views |
| --- | --- | --- |
| `ALL_REPCAT` | `DBA_REPCAT` | `USER_REPCAT` |
|  | `DBA_REPCAT_EXCEPTIONS` |  |
| `ALL_REPCAT_REFRESH_TEMPLATES` | `DBA_REPCAT_REFRESH_TEMPLATES` | `USER_REPCAT_REFRESH_TEMPLATES` |
| `ALL_REPCAT_TEMPLATE_OBJECTS` | `DBA_REPCAT_TEMPLATE_OBJECTS` | `USER_REPCAT_TEMPLATE_OBJECTS` |
| `ALL_REPCAT_TEMPLATE_PARMS` | `DBA_REPCAT_TEMPLATE_PARMS` | `USER_REPCAT_TEMPLATE_PARMS` |
| `ALL_REPCAT_TEMPLATE_SITES` | `DBA_REPCAT_TEMPLATE_SITES` | `USER_REPCAT_TEMPLATE_SITES` |
| `ALL_REPCAT_USER_AUTHORIZATIONS` | `DBA_REPCAT_USER_AUTHORIZATIONS` | `USER_REPCAT_USER_AUTHORIZATIONS` |
| `ALL_REPCAT_USER_PARM_VALUES` | `DBA_REPCAT_USER_PARM_VALUES` | `USER_REPCAT_USER_PARM_VALUES` |
| `ALL_REPCATLOG` | `DBA_REPCATLOG` | `USER_REPCATLOG` |
| `ALL_REPCOLUMN` | `DBA_REPCOLUMN` | `USER_REPCOLUMN` |
| `ALL_REPCOLUMN_GROUP` | `DBA_REPCOLUMN_GROUP` | `USER_REPCOLUMN_GROUP` |
| `ALL_REPCONFLICT` | `DBA_REPCONFLICT` | `USER_REPCONFLICT` |
| `ALL_REPDDL` | `DBA_REPDDL` | `USER_REPDDL` |
|  | `DBA_REPEXTENSIONS` |  |
| `ALL_REPFLAVOR_COLUMNS` | `DBA_REPFLAVOR_COLUMNS` | `USER_REPFLAVOR_COLUMNS` |
| `ALL_REPFLAVOR_OBJECTS` | `DBA_REPFLAVOR_OBJECTS` | `USER_REPFLAVOR_OBJECTS` |
| `ALL_REPFLAVORS` | `DBA_REPFLAVORS` | `USER_REPFLAVORS` |
| `ALL_REPGENERATED` | `DBA_REPGENERATED` | `USER_REPGENERATED` |
| `ALL_REPGENOBJECTS` | `DBA_REPGENOBJECTS` | `USER_REPGENOBJECTS` |
| `ALL_REPGROUP` | `DBA_REPGROUP` | `USER_REPGROUP` |
| `ALL_REPGROUP_PRIVILEGES` | `DBA_REPGROUP_PRIVILEGES` | `USER_REPGROUP_PRIVILEGES` |
| `ALL_REPGROUPED_COLUMN` | `DBA_REPGROUPED_COLUMN` | `USER_REPGROUPED_COLUMN` |
| `ALL_REPKEY_COLUMNS` | `DBA_REPKEY_COLUMNS` | `USER_REPKEY_COLUMNS` |
| `ALL_REPOBJECT` | `DBA_REPOBJECT` | `USER_REPOBJECT` |
| `ALL_REPPARAMETER_COLUMN` | `DBA_REPPARAMETER_COLUMN` | `USER_REPPARAMETER_COLUMN` |
| `ALL_REPPRIORITY` | `DBA_REPPRIORITY` | `USER_REPPRIORITY` |
| `ALL_REPPRIORITY_GROUP` | `DBA_REPPRIORITY_GROUP` | `USER_REPPRIORITY_GROUP` |
| `ALL_REPPROP` | `DBA_REPPROP` | `USER_REPPROP` |
| `ALL_REPRESOL_STATS_CONTROL` | `DBA_REPRESOL_STATS_CONTROL` | `USER_REPRESOL_STATS_CONTROL` |
| `ALL_REPRESOLUTION` | `DBA_REPRESOLUTION` | `USER_REPRESOLUTION` |
| `ALL_REPRESOLUTION_METHOD` | `DBA_REPRESOLUTION_METHOD` | `USER_REPRESOLUTION_METHOD` |
| `ALL_REPRESOLUTION_STATISTICS` | `DBA_REPRESOLUTION_STATISTICS` | `USER_REPRESOLUTION_STATISTICS` |
| `ALL_REPSCHEMA` | `DBA_REPSCHEMA` | `USER_REPSCHEMA` |
| `ALL_REPSITES` | `DBA_REPSITES` | `USER_REPSITES` |
|  | `DBA_REPSITES_NEW` |  |

The following are additional Oracle Replication data dictionary views:

  
`DEFCALL`  
`DEFCALLDEST`  
`DEFDEFAULTDEST`  
`DEFERRCOUNT`  
`DEFERROR`  
`DEFLOB`  
`DEFPROPAGATOR`  
`DEFSCHEDULE`  
`DEFTRAN`  
`DEFTRANDEST`  

See Also:

[Oracle Database Advanced Replication Management API Reference](https://docs.oracle.com/cd/E11882_01/server.112/e10707/toc.htm) for information about these views

## Oracle Workspace Manager Views

A number of data dictionary views are relevant only if you are using Oracle Workspace Manager. Table 2-2 lists these views.

Table 2-2 Oracle Workspace Manager Data Dictionary Views

| ALL\_ Views | DBA\_ Views | USER\_ Views |
| --- | --- | --- |
| [`ALL_MP_GRAPH_WORKSPACES`](https://docs.oracle.com/cd/E11882_01/appdev.112/e11826/long_views.htm#ADWSM03004) |  | [`USER_MP_GRAPH_WORKSPACES`](https://docs.oracle.com/cd/E11882_01/appdev.112/e11826/long_views.htm#ADWSM03121) |
| [`ALL_MP_PARENT_WORKSPACES`](https://docs.oracle.com/cd/E11882_01/appdev.112/e11826/long_views.htm#ADWSM03006) |  | [`USER_MP_PARENT_WORKSPACES`](https://docs.oracle.com/cd/E11882_01/appdev.112/e11826/long_views.htm#ADWSM03123) |
| [`ALL_REMOVED_WORKSPACES`](https://docs.oracle.com/cd/E11882_01/appdev.112/e11826/long_views.htm#ADWSM03007) |  | [`USER_REMOVED_WORKSPACES`](https://docs.oracle.com/cd/E11882_01/appdev.112/e11826/long_views.htm#ADWSM99101) |
| [`ALL_VERSION_HVIEW`](https://docs.oracle.com/cd/E11882_01/appdev.112/e11826/long_views.htm#ADWSM03010) |  |  |
| [`ALL_WM_CONS_COLUMNS`](https://docs.oracle.com/cd/E11882_01/appdev.112/e11826/long_views.htm#ADWSM03012) |  | [`USER_WM_CONS_COLUMNS`](https://docs.oracle.com/cd/E11882_01/appdev.112/e11826/long_views.htm#ADWSM03122) |
| [`ALL_WM_CONSTRAINTS`](https://docs.oracle.com/cd/E11882_01/appdev.112/e11826/long_views.htm#ADWSM03014) |  | [`USER_WM_CONSTRAINTS`](https://docs.oracle.com/cd/E11882_01/appdev.112/e11826/long_views.htm#ADWSM03124) |
| [`ALL_WM_IND_COLUMNS`](https://docs.oracle.com/cd/E11882_01/appdev.112/e11826/long_views.htm#ADWSM03016) |  | [`USER_WM_IND_COLUMNS`](https://docs.oracle.com/cd/E11882_01/appdev.112/e11826/long_views.htm#ADWSM03126) |
| [`ALL_WM_IND_EXPRESSIONS`](https://docs.oracle.com/cd/E11882_01/appdev.112/e11826/long_views.htm#ADWSM03018) |  | [`USER_WM_IND_EXPRESSIONS`](https://docs.oracle.com/cd/E11882_01/appdev.112/e11826/long_views.htm#ADWSM03128) |
| [`ALL_WM_LOCKED_TABLES`](https://docs.oracle.com/cd/E11882_01/appdev.112/e11826/long_views.htm#ADWSM03020) |  | [`USER_WM_LOCKED_TABLES`](https://docs.oracle.com/cd/E11882_01/appdev.112/e11826/long_views.htm#ADWSM03130) |
| [`ALL_WM_MODIFIED_TABLES`](https://docs.oracle.com/cd/E11882_01/appdev.112/e11826/long_views.htm#ADWSM03030) |  | [`USER_WM_MODIFIED_TABLES`](https://docs.oracle.com/cd/E11882_01/appdev.112/e11826/long_views.htm#ADWSM03140) |
|  |  | [`USER_WM_PRIVS`](https://docs.oracle.com/cd/E11882_01/appdev.112/e11826/long_views.htm#ADWSM03150) |
| [`ALL_WM_RIC_INFO`](https://docs.oracle.com/cd/E11882_01/appdev.112/e11826/long_views.htm#ADWSM03040) |  | [`USER_WM_RIC_INFO`](https://docs.oracle.com/cd/E11882_01/appdev.112/e11826/long_views.htm#ADWSM03160) |
|  | [`DBA_WM_SYS_PRIVS`](https://docs.oracle.com/cd/E11882_01/appdev.112/e11826/long_views.htm#ADWSM03105) |  |
| [`ALL_WM_TAB_TRIGGERS`](https://docs.oracle.com/cd/E11882_01/appdev.112/e11826/long_views.htm#ADWSM03050) |  | [`USER_WM_TAB_TRIGGERS`](https://docs.oracle.com/cd/E11882_01/appdev.112/e11826/long_views.htm#ADWSM03170) |
| [`ALL_WM_VERSIONED_TABLES`](https://docs.oracle.com/cd/E11882_01/appdev.112/e11826/long_views.htm#ADWSM03060) |  | [`USER_WM_VERSIONED_TABLES`](https://docs.oracle.com/cd/E11882_01/appdev.112/e11826/long_views.htm#ADWSM03180) |
| [`ALL_WM_VT_ERRORS`](https://docs.oracle.com/cd/E11882_01/appdev.112/e11826/long_views.htm#ADWSM03070) | [`DBA_WM_VT_ERRORS`](https://docs.oracle.com/cd/E11882_01/appdev.112/e11826/long_views.htm#ADWSM03107) | [`USER_WM_VT_ERRORS`](https://docs.oracle.com/cd/E11882_01/appdev.112/e11826/long_views.htm#ADWSM03190) |
| [`ALL_WORKSPACE_PRIVS`](https://docs.oracle.com/cd/E11882_01/appdev.112/e11826/long_views.htm#ADWSM03080) |  | [`USER_WORKSPACE_PRIVS`](https://docs.oracle.com/cd/E11882_01/appdev.112/e11826/long_views.htm#ADWSM03200) |
| [`ALL_WORKSPACE_SAVEPOINTS`](https://docs.oracle.com/cd/E11882_01/appdev.112/e11826/long_views.htm#ADWSM03090) |  | [`USER_WORKSPACE_SAVEPOINTS`](https://docs.oracle.com/cd/E11882_01/appdev.112/e11826/long_views.htm#ADWSM03210) |
|  | [`DBA_WORKSPACE_SESSIONS`](https://docs.oracle.com/cd/E11882_01/appdev.112/e11826/long_views.htm#ADWSM03110) |  |
| [`ALL_WORKSPACES`](https://docs.oracle.com/cd/E11882_01/appdev.112/e11826/long_views.htm#ADWSM03100) | [`DBA_WORKSPACES`](https://docs.oracle.com/cd/E11882_01/appdev.112/e11826/long_views.htm#ADWSM03115) | [`USER_WORKSPACES`](https://docs.oracle.com/cd/E11882_01/appdev.112/e11826/long_views.htm#ADWSM03220) |

The following are additional Oracle Workspace Manager data dictionary views:

  
[`ROLE_WM_PRIVS`](https://docs.oracle.com/cd/E11882_01/appdev.112/e11826/long_views.htm#ADWSM03120)  
[`WM_COMPRESS_BATCH_SIZES`](https://docs.oracle.com/cd/E11882_01/appdev.112/e11826/long_views.htm#ADWSM03233)  
[`WM_COMPRESSIBLE_TABLES`](https://docs.oracle.com/cd/E11882_01/appdev.112/e11826/long_views.htm#ADWSM03234)  
[`WM_EVENTS_INFO`](https://docs.oracle.com/cd/E11882_01/appdev.112/e11826/long_views.htm#ADWSM03235)  
[`WM_INSTALLATION`](https://docs.oracle.com/cd/E11882_01/appdev.112/e11826/long_views.htm#ADWSM03230)  
[`WM_REPLICATION_INFO`](https://docs.oracle.com/cd/E11882_01/appdev.112/e11826/long_views.htm#ADWSM03240)  

See Also:

[Oracle Database Workspace Manager Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e11826/long_views.htm#ADWSM030) for information about these views

## Recovery Catalog Views

The following data dictionary views are only available after you create an optional recovery catalog (which contains schemas containing information about backups) for use with Recovery Manager:

  
[`RC_ARCHIVED_LOG`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews002.htm#RCMRF163)  
[`RC_BACKUP_ARCHIVELOG_DETAILS`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews003.htm#RCMRF1924)  
[`RC_BACKUP_ARCHIVELOG_SUMMARY`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews004.htm#RCMRF1925)  
[`RC_BACKUP_CONTROLFILE`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews005.htm#RCMRF164)  
[`RC_BACKUP_CONTROLFILE_DETAILS`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews006.htm#RCMRF1926)  
[`RC_BACKUP_CONTROLFILE_SUMMARY`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews007.htm#RCMRF1927)  
[`RC_BACKUP_COPY_DETAILS`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews008.htm#RCMRF1928)  
[`RC_BACKUP_COPY_SUMMARY`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews009.htm#RCMRF1929)  
[`RC_BACKUP_CORRUPTION`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews010.htm#RCMRF165)  
[`RC_BACKUP_DATAFILE`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews011.htm#RCMRF1964)  
[`RC_BACKUP_DATAFILE_DETAILS`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews012.htm#RCMRF1930)  
[`RC_BACKUP_DATAFILE_SUMMARY`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews013.htm#RCMRF1931)  
[`RC_BACKUP_FILES`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews014.htm#RCMRF1670)  
[`RC_BACKUP_PIECE`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews015.htm#RCMRF167)  
[`RC_BACKUP_PIECE_DETAILS`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews016.htm#RCMRF1933)  
[`RC_BACKUP_REDOLOG`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews017.htm#RCMRF168)  
[`RC_BACKUP_SET`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews018.htm#RCMRF169)  
[`RC_BACKUP_SET_DETAILS`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews019.htm#RCMRF1934)  
[`RC_BACKUP_SET_SUMMARY`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews020.htm#RCMRF1935)  
[`RC_BACKUP_SPFILE`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews021.htm#RCMRF189)  
[`RC_BACKUP_SPFILE_DETAILS`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews022.htm#RCMRF1936)  
[`RC_BACKUP_SPFILE_SUMMARY`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews023.htm#RCMRF1937)  
[`RC_CHECKPOINT`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews024.htm#RCMRF170)  
[`RC_CONTROLFILE_COPY`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews025.htm#RCMRF171)  
[`RC_COPY_CORRUPTION`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews026.htm#RCMRF172)  
[`RC_DATABASE`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews027.htm#RCMRF173)  
[`RC_DATABASE_BLOCK_CORRUPTION`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews028.htm#RCMRF188)  
[`RC_DATABASE_INCARNATION`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews029.htm#RCMRF174)  
[`RC_DATAFILE`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews030.htm#RCMRF175)  
[`RC_DATAFILE_COPY`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews031.htm#RCMRF176)  
[`RC_LOG_HISTORY`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews032.htm#RCMRF177)  
[`RC_OFFLINE_RANGE`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews033.htm#RCMRF178)  
[`RC_PROXY_ARCHIVEDLOG`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews034.htm#RCMRF1938)  
[`RC_PROXY_ARCHIVELOG_DETAILS`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews035.htm#RCMRF1939)  
[`RC_PROXY_ARCHIVELOG_SUMMARY`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews036.htm#RCMRF1940)  
[`RC_PROXY_CONTROLFILE`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews037.htm#RCMRF179)  
[`RC_PROXY_COPY_DETAILS`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews038.htm#RCMRF1941)  
[`RC_PROXY_COPY_SUMMARY`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews039.htm#RCMRF1942)  
[`RC_PROXY_DATAFILE`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews040.htm#RCMRF180)  
[`RC_REDO_LOG`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews041.htm#RCMRF181)  
[`RC_REDO_THREAD`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews042.htm#RCMRF182)  
[`RC_RESTORE_POINT`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews043.htm#RCMRF202)  
[`RC_RESYNC`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews044.htm#RCMRF183)  
[`RC_RMAN_BACKUP_JOB_DETAILS`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews045.htm#RCMRF1943)  
[`RC_RMAN_BACKUP_SUBJOB_DETAILS`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews046.htm#RCMRF1944)  
[`RC_RMAN_BACKUP_TYPE`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews047.htm#RCMRF1945)  
[`RC_RMAN_CONFIGURATION`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews048.htm#RCMRF184)  
[`RC_RMAN_OUTPUT`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews049.htm#RCMRF1946)  
[`RC_RMAN_STATUS`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews050.htm#RCMRF381)  
[`RC_SITE`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews051.htm#RCMRF1953)  
[`RC_STORED_SCRIPT`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews052.htm#RCMRF185)  
[`RC_STORED_SCRIPT_LINE`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews053.htm#RCMRF186)  
[`RC_TABLESPACE`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews054.htm#RCMRF187)  
[`RC_TEMPFILE`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews055.htm#RCMRF1870)  
[`RC_UNUSABLE_BACKUPFILE_DETAILS`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews056.htm#RCMRF1947)

See Also:

[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews.htm#RCMRF003) for information about these views