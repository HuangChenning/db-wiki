---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/release-changes.html
tags:
  - oracle
  - 19c
  - reference
---

## Changes in This Release for Oracle Database Reference

This preface lists changes in Oracle Database Reference:

### Changes in Oracle Database 19c, Release Update 19.29

The following initialization parameter is new in Oracle Database 19c, Release Update 19.29:

- [HEARTBEAT\_BATCH\_SIZE](HEARTBEAT_BATCH_SIZE.md)

### Changes in Oracle Database 19c, Release Update 19.28

The following initialization parameters are new in Oracle Database 19c, Release Update 19.28:

- [MFA\_DUO\_API\_HOST](MFA_DUO_API_HOST.md)
- [MFA\_OMA\_IAM\_DOMAIN\_URL](MFA_OMA_IAM_DOMAIN_URL.md)
- [MFA\_SENDER\_EMAIL\_DISPLAYNAME](MFA_SENDER_EMAIL_DISPLAYNAME.md)
- [MFA\_SENDER\_EMAIL\_ID](MFA_SENDER_EMAIL_ID.md)
- [MFA\_SMTP\_HOST](MFA_SMTP_HOST.md)
- [MFA\_SMTP\_PORT](MFA_SMTP_PORT.md)

The following static data dictionary views are new in Oracle Database 19c, Release Update 19.28:

- [ALL\_ANNOTATION\_VALUES](ALL_ANNOTATION_VALUES.md), [DBA\_ANNOTATION\_VALUES](DBA_ANNOTATION_VALUES.md), and [USER\_ANNOTATION\_VALUES](USER_ANNOTATION_VALUES.md)
- [ALL\_ANNOTATIONS](ALL_ANNOTATIONS.md), [DBA\_ANNOTATIONS](DBA_ANNOTATIONS.md), and [USER\_ANNOTATIONS](USER_ANNOTATIONS.md)
- [ALL\_ANNOTATIONS\_USAGE](ALL_ANNOTATIONS_USAGE.md), [DBA\_ANNOTATIONS\_USAGE](DBA_ANNOTATIONS_USAGE.md), and [USER\_ANNOTATIONS\_USAGE](USER_ANNOTATIONS_USAGE.md)
- [DBA\_HIST\_SNAPSHOT\_DETAILS](DBA_HIST_SNAPSHOT_DETAILS.md)

### Changes in Oracle Database 19c, Release Update 19.26

The following initialization parameter is changed in Oracle Database 19c, Release Update 19.26:

- A new `AUTO` setting is available for the [DB\_LOST\_WRITE\_PROTECT](DB_LOST_WRITE_PROTECT.md) parameter and it is the default setting.

### Changes in Oracle Database 19c, Release Update 19.23

The following initialization parameter is new in Oracle Database 19c, Release Update 19.23:

- [SESSION\_EXIT\_ON\_PACKAGE\_STATE\_ERROR](SESSION_EXIT_ON_PACKAGE_STATE_ERROR.md)

### Changes in Oracle Database 19c, Release Update 19.22

The following initialization parameter is new in Oracle Database 19c, Release Update 19.22:

- [OGG\_ONLINE\_DDL](OGG_ONLINE_DDL.md)

The following initialization parameter is changed in Oracle Database 19c, Release Update 19.22:

- The [PRE\_PAGE\_SGA](PRE_PAGE_SGA.md) initialization parameter is deprecated. The value of [PRE\_PAGE\_SGA](PRE_PAGE_SGA.md) is always set to `TRUE` on Exadata systems. Any attempt to set this parameter to `FALSE` on an Exadata system will not take effect.

### Changes in Oracle Database 19c, Release Update 19.21

The following initialization parameter is new in Oracle Database 19c, Release Update 19.21:

- [MAIN\_WORKLOAD\_TYPE](MAIN_WORKLOAD_TYPE.md)

### Changes in Oracle Database 19c, Release Update 19.13

New AE Analytic Views

Oracle Database 19c, Release Update 19.13, introduces `AE` ("all edition") analytic views. Each new `AE` analytic view corresponds to an existing non- `AE` analytic view. `AE` views have the same columns as their non- `AE` counterparts, plus a column that displays the name of the application edition where the editioned object is defined.

The following table lists the new `AE` analytic views, divided into three categories: analytic view views, attribute dimension views, and hierarchy views. For brevity, only the `ALL_` views are listed. The corresponding `DBA_` and `USER_` views are also available and are documented in this guide.

| Analytic View Views | Attribute Dimension Views | Hierarchy Views |
| --- | --- | --- |
| [ALL\_ANALYTIC\_VIEW\_ATTR\_CLS\_AE](ALL_ANALYTIC_VIEW_ATTR_CLS_AE.md)   [ALL\_ANALYTIC\_VIEW\_BAS\_MEAS\_AE](ALL_ANALYTIC_VIEW_BAS_MEAS_AE.md)   [ALL\_ANALYTIC\_VIEW\_CLASS\_AE](ALL_ANALYTIC_VIEW_CLASS_AE.md)   [ALL\_ANALYTIC\_VIEW\_CLC\_MEAS\_AE](ALL_ANALYTIC_VIEW_CLC_MEAS_AE.md)   [ALL\_ANALYTIC\_VIEW\_COLUMNS\_AE](ALL_ANALYTIC_VIEW_COLUMNS_AE.md)   [ALL\_ANALYTIC\_VIEW\_DIM\_CLS\_AE](ALL_ANALYTIC_VIEW_DIM_CLS_AE.md)   [ALL\_ANALYTIC\_VIEW\_DIMS\_AE](ALL_ANALYTIC_VIEW_DIMS_AE.md)   [ALL\_ANALYTIC\_VIEW\_HIER\_CLS\_AE](ALL_ANALYTIC_VIEW_HIER_CLS_AE.md)   [ALL\_ANALYTIC\_VIEW\_HIERS\_AE](ALL_ANALYTIC_VIEW_HIERS_AE.md)   [ALL\_ANALYTIC\_VIEW\_KEYS\_AE](ALL_ANALYTIC_VIEW_KEYS_AE.md)   [ALL\_ANALYTIC\_VIEW\_LEVELS\_AE](ALL_ANALYTIC_VIEW_LEVELS_AE.md)   [ALL\_ANALYTIC\_VIEW\_LVL\_CLS\_AE](ALL_ANALYTIC_VIEW_LVL_CLS_AE.md)   [ALL\_ANALYTIC\_VIEW\_LVLGRPS\_AE](ALL_ANALYTIC_VIEW_LVLGRPS_AE.md)   [ALL\_ANALYTIC\_VIEW\_MEAS\_CLS\_AE](ALL_ANALYTIC_VIEW_MEAS_CLS_AE.md)   [ALL\_ANALYTIC\_VIEWS\_AE](ALL_ANALYTIC_VIEWS_AE.md) | [ALL\_ATTRIBUTE\_DIM\_ATTR\_CLS\_AE](ALL_ATTRIBUTE_DIM_ATTR_CLS_AE.md)   [ALL\_ATTRIBUTE\_DIM\_ATTRS\_AE](ALL_ATTRIBUTE_DIM_ATTRS_AE.md)   [ALL\_ATTRIBUTE\_DIM\_CLASS\_AE](ALL_ATTRIBUTE_DIM_CLASS_AE.md)   [ALL\_ATTRIBUTE\_DIM\_JN\_PTHS\_AE](ALL_ATTRIBUTE_DIM_JN_PTHS_AE.md)   [ALL\_ATTRIBUTE\_DIM\_KEYS\_AE](ALL_ATTRIBUTE_DIM_KEYS_AE.md)   [ALL\_ATTRIBUTE\_DIM\_LEVELS\_AE](ALL_ATTRIBUTE_DIM_LEVELS_AE.md)   [ALL\_ATTRIBUTE\_DIM\_LVL\_ATRS\_AE](ALL_ATTRIBUTE_DIM_LVL_ATRS_AE.md)   [ALL\_ATTRIBUTE\_DIM\_LVL\_CLS\_AE](ALL_ATTRIBUTE_DIM_LVL_CLS_AE.md)   [ALL\_ATTRIBUTE\_DIM\_ORD\_ATRS\_AE](ALL_ATTRIBUTE_DIM_ORD_ATRS_AE.md)   [ALL\_ATTRIBUTE\_DIM\_TABLES\_AE](ALL_ATTRIBUTE_DIM_TABLES_AE.md)   [ALL\_ATTRIBUTE\_DIMENSIONS\_AE](ALL_ATTRIBUTE_DIMENSIONS_AE.md) | [ALL\_HIER\_CLASS\_AE](ALL_HIER_CLASS_AE.md)   [ALL\_HIER\_COLUMNS\_AE](ALL_HIER_COLUMNS_AE.md)   [ALL\_HIER\_HIER\_ATTR\_CLASS\_AE](ALL_HIER_HIER_ATTR_CLASS_AE.md)   [ALL\_HIER\_HIER\_ATTRIBUTES\_AE](ALL_HIER_HIER_ATTRIBUTES_AE.md)   [ALL\_HIER\_JOIN\_PATHS\_AE](ALL_HIER_JOIN_PATHS_AE.md)   [ALL\_HIER\_LEVEL\_ID\_ATTRS\_AE](ALL_HIER_LEVEL_ID_ATTRS_AE.md)   [ALL\_HIER\_LEVELS\_AE](ALL_HIER_LEVELS_AE.md)   [ALL\_HIERARCHIES\_AE](ALL_HIERARCHIES_AE.md) |

### Changes in Oracle Database 19c, Release Update 19.11

The following initialization parameter is new in Oracle Database 19c, Release Update 19.11:

- [DRCP\_DEDICATED\_OPT](DRCP_DEDICATED_OPT.md)

The following static data dictionary views are new in Oracle Database 19c, Release Update 19.11:

- [DBA\_ACCHK\_EVENTS](DBA_ACCHK_EVENTS.md)
- [DBA\_ACCHK\_EVENTS\_SUMMARY](DBA_ACCHK_EVENTS_SUMMARY.md)
- [DBA\_ACCHK\_STATISTICS](DBA_ACCHK_STATISTICS.md)
- [DBA\_ACCHK\_STATISTICS\_SUMMARY](DBA_ACCHK_STATISTICS_SUMMARY.md)
- [ALL\_IMMUTABLE\_TABLES](ALL_IMMUTABLE_TABLES.md), [DBA\_IMMUTABLE\_TABLES](DBA_IMMUTABLE_TABLES.md), and [USER\_IMMUTABLE\_TABLES](USER_IMMUTABLE_TABLES.md)

### Changes in Oracle Database 19c, Release Update 19.10

The following initialization parameters are new in Oracle Database 19c, Release Update 19.10:

- [BLOCKCHAIN\_TABLE\_MAX\_NO\_DROP](BLOCKCHAIN_TABLE_MAX_NO_DROP.md)
- [CONTAINER\_DATA](CONTAINER_DATA.md)
- [MAX\_AUTH\_SERVERS](MAX_AUTH_SERVERS.md)
- [MIN\_AUTH\_SERVERS](MIN_AUTH_SERVERS.md)
- [OPTIMIZER\_REAL\_TIME\_STATISTICS](OPTIMIZER_REAL_TIME_STATISTICS.md)

The following static data dictionary views are new in Oracle Database 19c, Release Update 19.10:

- [ALL\_BLOCKCHAIN\_TABLES](ALL_BLOCKCHAIN_TABLES.md), [DBA\_BLOCKCHAIN\_TABLES](DBA_BLOCKCHAIN_TABLES.md), and [USER\_BLOCKCHAIN\_TABLES](USER_BLOCKCHAIN_TABLES.md)
- [ALL\_CERTIFICATES](ALL_CERTIFICATES.md), [DBA\_CERTIFICATES](DBA_CERTIFICATES.md), and [USER\_CERTIFICATES](USER_CERTIFICATES.md)
- [DBA\_LOGMNR\_DICTIONARY\_BUILDLOG](DBA_LOGMNR_DICTIONARY_BUILDLOG.md)

### Changes in Oracle Database 19c, Release Update 19.6

The following initialization parameter is new in Oracle Database 19c, Release Update 19.6:

- [OPTIMIZER\_SESSION\_TYPE](OPTIMIZER_SESSION_TYPE.md)

### Changes in Oracle Database 19c, Release Update 19.4

The following initialization parameter is new in Oracle Database 19c, Release Update 19.4:

- [IGNORE\_SESSION\_SET\_PARAM\_ERRORS](IGNORE_SESSION_SET_PARAM_ERRORS.md)

### Changes in Oracle Database 19c

This section lists changes in Oracle Database Reference for Oracle Database 19c.

See [Oracle Database New Features Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/refrn&id=NEWFT) for a complete list of new features for this release.

#### New Features

This section lists new features in this manual for Oracle Database 19c.

The following changes to initialization parameters are new in Oracle Database 19c:

- On Linux platforms only, Oracle recommends against explicitly setting values for `MEMORY_TARGET` and `MEMORY_MAX_TARGET` in the initialization parameter file at the time of instance startup. Doing so may result in suboptimal small page allocation in the SGA. Furthermore, if the `USE_LARGE_PAGES` parameter is set to `ONLY` and you attempt to set values for `MEMORY_TARGET` and `MEMORY_MAX_TARGET`, the instance will fail to start.
	See [MEMORY\_TARGET](MEMORY_TARGET.md), [MEMORY\_MAX\_TARGET](MEMORY_MAX_TARGET.md), and [USE\_LARGE\_PAGES](USE_LARGE_PAGES.md).

The following initialization parameters are new in Oracle Database 19c:

- [ADG\_REDIRECT\_DML](ADG_REDIRECT_DML.md)
- [ALLOW\_ROWID\_COLUMN\_TYPE](ALLOW_ROWID_COLUMN_TYPE.md)
- [CLIENT\_STATISTICS\_LEVEL](CLIENT_STATISTICS_LEVEL.md)
- [CPU\_MIN\_COUNT](CPU_MIN_COUNT.md)
- [DATA\_GUARD\_MAX\_IO\_TIME](DATA_GUARD_MAX_IO_TIME.md)
- [DATA\_GUARD\_MAX\_LONGIO\_TIME](DATA_GUARD_MAX_LONGIO_TIME.md)
- [ENABLE\_IMC\_WITH\_MIRA](ENABLE_IMC_WITH_MIRA.md)
- [LOB\_SIGNATURE\_ENABLE](lob_signature_enable.md)
- [MAX\_DATAPUMP\_PARALLEL\_PER\_JOB](MAX_DATAPUMP_PARALLEL_PER_JOB.md)
- [MAX\_IDLE\_BLOCKER\_TIME](MAX_IDLE_BLOCKER_TIME.md)
- [OPTIMIZER\_CAPTURE\_SQL\_QUARANTINE](OPTIMIZER_CAPTURE_SQL_QUARANTINE.md)
- [OPTIMIZER\_USE\_SQL\_QUARANTINE](OPTIMIZER_USE_SQL_QUARANTINE.md)
- [UNIFIED\_AUDIT\_COMMON\_SYSTEMLOG](UNIFIED_AUDIT_COMMON_SYSTEMLOG.md)

Note:

See [Initialization Parameters](initialization-parameters.md) for more information about these initialization parameters.

The following static data dictionary views are new in Oracle Database 19c:

- [ALL\_TRIGGERS\_AE](ALL_TRIGGERS_AE.md), [DBA\_TRIGGERS\_AE](DBA_TRIGGERS_AE.md), and [USER\_TRIGGERS\_AE](USER_TRIGGERS_AE.md)
- [DBA\_AUTO\_INDEX\_CONFIG](DBA_AUTO_INDEX_CONFIG.md)
- [DBA\_AUTO\_STAT\_EXECUTIONS](DBA_AUTO_STAT_EXECUTIONS.md)
- [DBA\_PDB\_SNAPSHOTFILE](DBA_PDB_SNAPSHOTFILE.md)
- [DBA\_RAT\_CAPTURE\_SCHEMA\_INFO](DBA_RAT_CAPTURE_SCHEMA_INFO.md)
- [DBA\_REGISTRY\_BACKPORTS](DBA_REGISTRY_BACKPORTS.md)
- [DBA\_SQL\_QUARANTINE](DBA_SQL_QUARANTINE.md)

Note:

[Static Data Dictionary Views](static-data-dictionary-views.md) for more information about these static data dictionary views

The following dynamic performance views are new in Oracle Database 19c:

- GV$AQ\_PARTITION\_STATS and [V$AQ\_PARTITION\_STATS](V-AQ_PARTITION_STATS.md)
- GV$ASM\_ACFSAUTORESIZE and [V$ASM\_ACFSAUTORESIZE](V-ASM_ACFSAUTORESIZE.md)
- GV$MEMOPTIMIZE\_WRITE\_AREA and [V$MEMOPTIMIZE\_WRITE\_AREA](V-MEMOPTIMIZE_WRITE_AREA.md)
- GV$SHARED\_SERVER\_STAT and [V$SHARED\_SERVER\_STAT](V-SHARED_SERVER_STAT.md)
- GV$SQL\_TESTCASES and [V$SQL\_TESTCASES](V-SQL_TESTCASES.md)

Note:

[GV$ Views](about-dynamic-performance-views.md) and [Dynamic Performance Views](dynamic-performance-views.md) for more information about these dynamic performance views

#### Deprecated Features

The following features are deprecated in Oracle Database 19c, and may be desupported in a future release:

- The [CLUSTER\_DATABASE\_INSTANCES](CLUSTER_DATABASE_INSTANCES.md) initialization parameter
- The [PRE\_PAGE\_SGA](PRE_PAGE_SGA.md) initialization parameter (starting with Oracle Database 19c, Release Update 19.22)
- The [SERVICE\_NAMES](SERVICE_NAMES.md) initialization parameter

#### Desupported Features

The following features are desupported in Oracle Database 19c:

- The `MAX_CONNECTIONS` attribute of the `LOG_ARCHIVE_DEST_n` initialization parameter, for Oracle Data Guard redo transport
- The `EXAFUSION_ENABLED` initialization parameter
- The `O7_DICTIONARY_ACCESSIBILITY` initialization parameter
- Oracle Streams is desupported. As a result, the following views are desupported:
	- `ALL_STREAMS_COLUMNS`
		- `ALL_STREAMS_MESSAGE_RULES`
		- `ALL_STREAMS_RULES`
		- `ALL_STREAMS_UNSUPPORTED`
		- `DBA_STREAMS_ADMINISTRATOR`
		- `DBA_STREAMS_COLUMNS`
		- `DBA_STREAMS_MESSAGE_RULES`
		- `DBA_STREAMS_RULES`
		- `DBA_STREAMS_SPLIT_MERGE`
		- `DBA_STREAMS_SPLIT_MERGE_HIST`
		- `DBA_STREAMS_STMTS`
		- `DBA_STREAMS_STMT_HANDLERS`
		- `DBA_STREAMS_TRANSFORMATIONS`
		- `DBA_STREAMS_UNSUPPORTED`
		- `V$STREAMS_CAPTURE`
		- `V$STREAMS_MESSAGE_TRACKING`
		- `V$STREAMS_TRANSACTION`
- Extended Datatype Support (EDS) is desupported. As a result, the following views are desupported:

See Also:

[Oracle Database Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/refrn&id=UPGRD60000)