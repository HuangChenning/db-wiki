---
title: Changing Parameter Values in a Parameter File
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams004.htm
tags:
  - oracle
  - 11g
  - reference
---

You change the value of a parameter in a parameter file in one of the following ways:

- In most cases, the new value takes effect the next time you start an instance of the database.
- By issuing an `ALTER SYSTEM SET ... SCOPE=SPFILE` statement to update a server parameter file
- By issuing an `ALTER SYSTEM RESET ... SCOPE=SPFILE` statement to remove a parameter from a server parameter file, causing the default value to take effect the next time you start an instance of the database.

## Parameters by Functional Category

The following list shows the initialization parameters by their functional category:

- ANSI Compliance
	[`BLANK_TRIMMING`](initparams023.md)
- Backup and Restore
	[`BACKUP_TAPE_IO_SLAVES`](initparams021.md)
	[`CLONEDB`](initparams027.md)
	[`RECYCLEBIN`](initparams208.md)
	[`TAPE_ASYNCH_IO`](initparams256.md)
- BFILEs
	[`SESSION_MAX_OPEN_FILES`](initparams233.md)
- Buffer Cache and I/O
	[`CLIENT_RESULT_CACHE_LAG`](initparams025.md)
	[`CLIENT_RESULT_CACHE_SIZE`](initparams026.md)
	[`DB_` `n` `K_CACHE_SIZE`](initparams046.md)
	[`DB_BLOCK_BUFFERS`](initparams047.md)
	[`DB_BLOCK_SIZE`](initparams050.md)
	[`DB_CACHE_ADVICE`](initparams051.md)
	[`DB_CACHE_SIZE`](initparams052.md)
	[`DB_FILE_MULTIBLOCK_READ_COUNT`](initparams056.md)
	[`DB_KEEP_CACHE_SIZE`](initparams062.md)
	[`DB_RECYCLE_CACHE_SIZE`](initparams067.md)
	[`DB_WRITER_PROCESSES`](initparams072.md)
	[`DBWR_IO_SLAVES`](initparams073.md)
	[`DISK_ASYNCH_IO`](initparams079.md)
	[`DNFS_BATCH_SIZE`](initparams083.md)
	[`FILESYSTEMIO_OPTIONS`](initparams094.md)
	[`READ_ONLY_OPEN_DELAYED`](initparams206.md)
	[`RESULT_CACHE_MAX_RESULT`](initparams219.md)
	[`RESULT_CACHE_MAX_SIZE`](initparams220.md)
	[`RESULT_CACHE_MODE`](initparams221.md)
	[`USE_INDIRECT_DATA_BUFFERS`](initparams269.md)
- Cursors and Library Cache
	[`CURSOR_BIND_CAPTURE_DESTINATION`](initparams043.md)
	[`CURSOR_SHARING`](initparams044.md)
	[`CURSOR_SPACE_FOR_TIME`](initparams045.md)
	[`OPEN_CURSORS`](initparams163.md)
	[`SESSION_CACHED_CURSORS`](initparams232.md)
- Database/Instance Identification
	[`DB_DOMAIN`](initparams055.md)
	[`DB_NAME`](initparams064.md)
	[`INSTANCE_NAME`](initparams105.md)
- Diagnostics and Statistics
	`AWR_SNAPSHOT_TIME_OFFSET`
	[`BACKGROUND_CORE_DUMP`](initparams019.md)
	[`BACKGROUND_DUMP_DEST`](initparams020.md)
	[`CORE_DUMP_DEST`](initparams039.md)
	[`DB_BLOCK_CHECKING`](initparams048.md)
	[`DB_BLOCK_CHECKSUM`](initparams049.md)
	[`DIAGNOSTIC_DEST`](initparams078.md)
	[`EVENT`](initparams087.md)
	[`MAX_DUMP_FILE_SIZE`](initparams139.md)
	[`SHADOW_CORE_DUMP`](initparams237.md)
	[`STATISTICS_LEVEL`](initparams254.md)
	[`TIMED_OS_STATISTICS`](initparams258.md)
	[`TIMED_STATISTICS`](initparams259.md)
	[`TRACE_ENABLED`](initparams260.md)
	[`TRACEFILE_IDENTIFIER`](initparams261.md)
	[`USER_DUMP_DEST`](initparams267.md)
- Distributed, Replication
	[`COMMIT_POINT_STRENGTH`](initparams032.md)
	[`DISTRIBUTED_LOCK_TIMEOUT`](initparams081.md)
	[`ENABLE_GOLDENGATE_REPLICATION`](initparams086.md)
	[`GLOBAL_NAMES`](initparams098.md)
	[`HS_AUTOREGISTER`](initparams102.md)
	[`OPEN_LINKS`](initparams164.md)
	[`OPEN_LINKS_PER_INSTANCE`](initparams165.md)
	[`REPLICATION_DEPENDENCY_TRACKING`](initparams215.md)
- File Locations, Names, and Sizes
	[`AUDIT_FILE_DEST`](initparams014.md)
	[`BACKGROUND_CORE_DUMP`](initparams019.md)
	[`BACKGROUND_DUMP_DEST`](initparams020.md)
	[`CONTROL_FILES`](initparams037.md)
	[`CORE_DUMP_DEST`](initparams039.md)
	[`DB_CREATE_FILE_DEST`](initparams053.md)
	[`DB_CREATE_ONLINE_LOG_DEST_` `n`](initparams054.md)
	[`DB_FILES`](initparams058.md)
	[`DB_RECOVERY_FILE_DEST`](initparams065.md)
	[`DB_RECOVERY_FILE_DEST_SIZE`](initparams066.md)
	[`FILE_MAPPING`](initparams092.md)
	[`IFILE`](initparams103.md)
	[`LOG_ARCHIVE_DEST_` `n`](initparams125.md)
	[`SPFILE`](initparams247.md)
- Globalization
	[`NLS_CALENDAR`](initparams144.md)
	[`NLS_COMP`](initparams145.md)
	[`NLS_CURRENCY`](initparams146.md)
	[`NLS_DATE_FORMAT`](initparams147.md)
	[`NLS_DATE_LANGUAGE`](initparams148.md)
	[`NLS_DUAL_CURRENCY`](initparams149.md)
	[`NLS_ISO_CURRENCY`](initparams150.md)
	[`NLS_LANGUAGE`](initparams151.md)
	[`NLS_LENGTH_SEMANTICS`](initparams152.md)
	[`NLS_NCHAR_CONV_EXCP`](initparams153.md)
	[`NLS_NUMERIC_CHARACTERS`](initparams154.md)
	[`NLS_SORT`](initparams155.md)
	[`NLS_TERRITORY`](initparams156.md)
	[`NLS_TIMESTAMP_FORMAT`](initparams157.md)
	[`NLS_TIMESTAMP_TZ_FORMAT`](initparams158.md)
- Java
	[`JAVA_JIT_ENABLED`](initparams108.md)
	[`JAVA_MAX_SESSIONSPACE_SIZE`](initparams109.md)
	[`JAVA_POOL_SIZE`](initparams110.md)
	[`JAVA_SOFT_SESSIONSPACE_LIMIT`](initparams111.md)
- Job Queues
	[`JOB_QUEUE_PROCESSES`](initparams112.md)
- License Limits
	[`LICENSE_MAX_SESSIONS`](initparams116.md)
	[`LICENSE_MAX_USERS`](initparams117.md)
	[`LICENSE_SESSIONS_WARNING`](initparams118.md)
- Memory
	[`MEMORY_MAX_TARGET`](initparams142.md)
	[`MEMORY_TARGET`](initparams143.md)
- Miscellaneous
	[`AQ_TM_PROCESSES`](initparams008.md)
	[`ASM_PREFERRED_READ_FAILURE_GROUPS`](initparams013.md)
	[`COMPATIBLE`](initparams035.md)
	[`FIXED_DATE`](initparams095.md)
	[`LDAP_DIRECTORY_SYSAUTH`](initparams115.md)
	[`XML_DB_EVENTS`](initparams272.md)
- Networking
	[`LOCAL_LISTENER`](initparams120.md)
	[`REMOTE_LISTENER`](initparams211.md)
	[`SERVICE_NAMES`](initparams231.md)
- Objects and LOBs
	[`OBJECT_CACHE_MAX_SIZE_PERCENT`](initparams160.md)
	[`OBJECT_CACHE_OPTIMAL_SIZE`](initparams161.md)
- OLAP
	[`OLAP_PAGE_POOL_SIZE`](initparams162.md)
- Optimizer
	[`OPTIMIZER_CAPTURE_SQL_PLAN_BASELINES`](initparams166.md)
	[`OPTIMIZER_DYNAMIC_SAMPLING`](initparams167.md)
	[`OPTIMIZER_FEATURES_ENABLE`](initparams168.md)
	[`OPTIMIZER_INDEX_CACHING`](initparams169.md)
	[`OPTIMIZER_INDEX_COST_ADJ`](initparams170.md)
	[`OPTIMIZER_MODE`](initparams171.md)
	[`OPTIMIZER_SECURE_VIEW_MERGING`](initparams172.md)
	[`OPTIMIZER_USE_PENDING_STATISTICS`](initparams174.md)
	[`OPTIMIZER_USE_SQL_PLAN_BASELINES`](initparams175.md)
	[`QUERY_REWRITE_ENABLED`](initparams203.md)
	[`QUERY_REWRITE_INTEGRITY`](initparams204.md)
	[`STAR_TRANSFORMATION_ENABLED`](initparams253.md)
- Parallel Execution
	[`PARALLEL_ADAPTIVE_MULTI_USER`](initparams178.md)
	[`PARALLEL_EXECUTION_MESSAGE_SIZE`](initparams182.md)
	[`PARALLEL_MAX_SERVERS`](initparams186.md)
	[`PARALLEL_MIN_PERCENT`](initparams187.md)
	[`PARALLEL_MIN_SERVERS`](initparams188.md)
	[`PARALLEL_THREADS_PER_CPU`](initparams191.md)
- PL/SQL
	[`PLSQL_V2_COMPATIBILITY`](initparams199.md)
	[`REMOTE_DEPENDENCIES_MODE`](initparams210.md)
	[`UTL_FILE_DIR`](initparams270.md)
- PL/SQL Compiler
	[`PERMIT_92_WRAP_FORMAT`](initparams192.md)
	[`PLSCOPE_SETTINGS`](initparams194.md)
	[`PLSQL_CCFLAGS`](initparams195.md)
	[`PLSQL_CODE_TYPE`](initparams196.md)
	[`PLSQL_DEBUG`](initparams197.md)
	[`PLSQL_OPTIMIZE_LEVEL`](initparams198.md)
	[`PLSQL_WARNINGS`](initparams200.md)
	[`NLS_LENGTH_SEMANTICS`](initparams152.md)
- SGA Memory
	[`DB_` `n` `K_CACHE_SIZE`](initparams046.md)
	[`DB_CACHE_SIZE`](initparams052.md)
	[`HI_SHARED_MEMORY_ADDRESS`](initparams101.md)
	[`JAVA_POOL_SIZE`](initparams110.md)
	[`LARGE_POOL_SIZE`](initparams113.md)
	[`LOCK_SGA`](initparams122.md)
	[`OLAP_PAGE_POOL_SIZE`](initparams162.md)
	[`PRE_PAGE_SGA`](initparams201.md)
	[`SGA_MAX_SIZE`](initparams235.md)
	[`SGA_TARGET`](initparams236.md)
	[`SHARED_MEMORY_ADDRESS`](initparams238.md)
	[`SHARED_POOL_RESERVED_SIZE`](initparams239.md)
	[`SHARED_POOL_SIZE`](initparams240.md)
	[`STREAMS_POOL_SIZE`](initparams255.md)
	[`USE_LARGE_PAGES`](initparams268.md)
- Oracle RAC
	[`ACTIVE_INSTANCE_COUNT`](initparams007.md)
	[`CLUSTER_DATABASE`](initparams028.md)
	[`CLUSTER_DATABASE_INSTANCES`](initparams029.md)
	[`CLUSTER_INTERCONNECTS`](initparams030.md)
	[`INSTANCE_NUMBER`](initparams106.md)
	[`PARALLEL_INSTANCE_GROUP`](initparams184.md)
	[`THREAD`](initparams257.md)
- Redo Logs, Archiving, and Recovery
	[`CONTROL_FILE_RECORD_KEEP_TIME`](initparams036.md)
	[`DB_CREATE_ONLINE_LOG_DEST_` `n`](initparams054.md)
	[`DB_RECOVERY_FILE_DEST`](initparams065.md)
	[`DB_RECOVERY_FILE_DEST_SIZE`](initparams066.md)
	[`DB_UNRECOVERABLE_SCN_TRACKING`](initparams071.md)
	[`FAST_START_MTTR_TARGET`](initparams090.md)
	[`LOG_BUFFER`](initparams133.md)
	[`LOG_CHECKPOINT_INTERVAL`](initparams134.md)
	[`LOG_CHECKPOINT_TIMEOUT`](initparams135.md)
	[`LOG_CHECKPOINTS_TO_ALERT`](initparams136.md)
	[`LOG_ARCHIVE_CONFIG`](initparams123.md)
	[`LOG_ARCHIVE_DEST_` `n`](initparams125.md)
	[`LOG_ARCHIVE_DEST_STATE_` `n`](initparams126.md)
	[`LOG_ARCHIVE_DUPLEX_DEST`](initparams127.md)
	[`LOG_ARCHIVE_FORMAT`](initparams128.md)
	[`LOG_ARCHIVE_MAX_PROCESSES`](initparams130.md)
	[`LOG_ARCHIVE_MIN_SUCCEED_DEST`](initparams131.md)
	[`LOG_ARCHIVE_TRACE`](initparams132.md)
	[`REDO_TRANSPORT_USER`](initparams209.md)
	[`RECOVERY_PARALLELISM`](initparams207.md)
- Resource Manager
	[`RESOURCE_LIMIT`](initparams216.md)
	[`RESOURCE_MANAGER_CPU_ALLOCATION`](initparams217.md)
	[`RESOURCE_MANAGER_PLAN`](initparams218.md)
- Security and Auditing
	[`AUDIT_FILE_DEST`](initparams014.md)
	[`AUDIT_SYS_OPERATIONS`](initparams015.md)
	[`AUDIT_SYSLOG_LEVEL`](initparams016.md)
	[`AUDIT_TRAIL`](initparams017.md)
	[`COMMIT_LOGGING`](initparams031.md)
	[`COMMIT_WAIT`](initparams033.md)
	[`O7_DICTIONARY_ACCESSIBILITY`](initparams159.md)
	[`OS_AUTHENT_PREFIX`](initparams176.md)
	[`OS_ROLES`](initparams177.md)
	[`RDBMS_SERVER_DN`](initparams205.md)
	[`REMOTE_LOGIN_PASSWORDFILE`](initparams212.md)
	[`REMOTE_OS_AUTHENT`](initparams213.md)
	[`REMOTE_OS_ROLES`](initparams214.md)
	[`SEC_CASE_SENSITIVE_LOGON`](initparams225.md)
	[`SEC_MAX_FAILED_LOGIN_ATTEMPTS`](initparams226.md)
	[`SEC_PROTOCOL_ERROR_FURTHER_ACTION`](initparams227.md)
	[`SEC_PROTOCOL_ERROR_TRACE_ACTION`](initparams228.md)
	[`SEC_RETURN_SERVER_RELEASE_BANNER`](initparams229.md)
	[`SQL92_SECURITY`](initparams249.md)
- Sessions and Processes
	[`CPU_COUNT`](initparams040.md)
	[`PROCESSES`](initparams202.md)
	[`SESSIONS`](initparams234.md)
- Shared Server Architecture
	[`CIRCUITS`](initparams024.md)
	[`DISPATCHERS`](initparams080.md)
	[`MAX_DISPATCHERS`](initparams138.md)
	[`MAX_SHARED_SERVERS`](initparams141.md)
	[`SHARED_SERVER_SESSIONS`](initparams241.md)
	[`SHARED_SERVERS`](initparams242.md)
- Standby Database
	[`ARCHIVE_LAG_TARGET`](initparams009.md)
	[`DB_FILE_NAME_CONVERT`](initparams057.md)
	[`DB_UNIQUE_NAME`](initparams070.md)
	[`DG_BROKER_CONFIG_FILE` `n`](initparams076.md)
	[`DG_BROKER_START`](initparams077.md)
	[`FAL_CLIENT`](initparams088.md)
	[`FAL_SERVER`](initparams089.md)
	[`LOG_FILE_NAME_CONVERT`](initparams137.md)
	[`STANDBY_FILE_MANAGEMENT`](initparams252.md)
- Temporary Sort Space
	[`BITMAP_MERGE_AREA_SIZE`](initparams022.md)
	[`CREATE_BITMAP_AREA_SIZE`](initparams041.md)
	[`HASH_AREA_SIZE`](initparams100.md)
	[`PGA_AGGREGATE_TARGET`](initparams193.md)
	[`SORT_AREA_RETAINED_SIZE`](initparams245.md)
	[`SORT_AREA_SIZE`](initparams246.md)
	[`WORKAREA_SIZE_POLICY`](initparams271.md)
- Transactions
	[`COMMIT_LOGGING`](initparams031.md)
	[`COMMIT_WAIT`](initparams033.md)
	[`DB_LOST_WRITE_PROTECT`](initparams063.md)
	[`DDL_LOCK_TIMEOUT`](initparams074.md)
	[`DML_LOCKS`](initparams082.md)
	[`FAST_START_PARALLEL_ROLLBACK`](initparams091.md)
	[`GLOBAL_TXN_PROCESSES`](initparams099.md)
	[`TRANSACTIONS`](initparams262.md)
- Undo Management
	[`RESUMABLE_TIMEOUT`](initparams223.md)
	[`ROLLBACK_SEGMENTS`](initparams224.md)
	[`TRANSACTIONS_PER_ROLLBACK_SEGMENT`](initparams263.md)
	[`UNDO_MANAGEMENT`](initparams264.md)
	[`UNDO_RETENTION`](initparams265.md)
	[`UNDO_TABLESPACE`](initparams266.md)

## Modifiable Parameters

Some initialization parameters can be modified using the `ALTER SESSION` or `ALTER SYSTEM` statements while an instance is running. Use the following syntax to modify initialization parameters:

```
ALTER SESSION SET parameter_name = value
ALTER SYSTEM SET parameter_name = value [DEFERRED]
```

Whenever a parameter is modified using the `ALTER SYSTEM` statement, the Oracle Database records the statement that modifies the parameter in the alert log.

The `ALTER SESSION` statement changes the value of the specified parameter for the duration of the session that invokes the statement. The value of the parameter does not change for other sessions in the instance. The value of the following initialization parameters can be changed with `ALTER SESSION`:

  
`ASM_POWER_LIMIT`  
`COMMIT_LOGGING`  
`COMMIT_WAIT`  
`COMMIT_WRITE`  
`CREATE_STORED_OUTLINES`  
`CURSOR_BIND_CAPTURE_DESTINATION`  
`CURSOR_SHARING`  
`DB_BLOCK_CHECKING`  
`DB_CREATE_FILE_DEST`  
`DB_CREATE_ONLINE_LOG_DEST_` `n`  
`DB_FILE_MULTIBLOCK_READ_COUNT`  
`DB_FILE_NAME_CONVERT`  
`DB_SECUREFILE`  
`DB_UNRECOVERABLE_SCN_TRACKING`  
`DDL_LOCK_TIMEOUT`  
`DEFERRED_SEGMENT_CREATION`  
`DST_UPGRADE_INSERT_CONV`  
`ENABLE_DDL_LOGGING`  
`GLOBAL_NAMES`  
`HASH_AREA_SIZE`  
`JAVA_JIT_ENABLED`  
`LOG_ARCHIVE_DEST_` `n`  
`LOG_ARCHIVE_DEST_STATE_` `n`  
`LOG_ARCHIVE_MIN_SUCCEED_DEST`  
`MAX_DUMP_FILE_SIZE`  
`NLS_CALENDAR`  
`NLS_COMP`  
`NLS_CURRENCY`  
`NLS_DATE_FORMAT`  
`NLS_DATE_LANGUAGE`  
`NLS_DUAL_CURRENCY`  
`NLS_ISO_CURRENCY`  
`NLS_LANGUAGE`  
`NLS_LENGTH_SEMANTICS`  
`NLS_NCHAR_CONV_EXCP`  
`NLS_NUMERIC_CHARACTERS`  
`NLS_SORT`  
`NLS_TERRITORY`  
`NLS_TIMESTAMP_FORMAT`  
`NLS_TIMESTAMP_TZ_FORMAT`  
`OBJECT_CACHE_MAX_SIZE_PERCENT`  
`OBJECT_CACHE_OPTIMAL_SIZE`  
`OLAP_PAGE_POOL_SIZE`  
`OPTIMIZER_CAPTURE_SQL_PLAN_BASELINES`  
`OPTIMIZER_DYNAMIC_SAMPLING`  
`OPTIMIZER_FEATURES_ENABLE`  
`OPTIMIZER_INDEX_CACHING`  
`OPTIMIZER_INDEX_COST_ADJ`  
`OPTIMIZER_MODE`  
`OPTIMIZER_USE_INVISIBLE_INDEXES`  
`OPTIMIZER_USE_PENDING_STATISTICS`  
`OPTIMIZER_USE_SQL_PLAN_BASELINES`  
`PARALLEL_DEGREE_LIMIT`  
`PARALLEL_DEGREE_POLICY`  
`PARALLEL_FORCE_LOCAL`  
`PARALLEL_INSTANCE_GROUP`  
`PARALLEL_IO_CAP_ENABLED`  
`PARALLEL_MIN_PERCENT`  
`PARALLEL_MIN_TIME_THRESHOLD`  
`PLSCOPE_SETTINGS`  
`PLSQL_CCFLAGS`  
`PLSQL_CODE_TYPE`  
`PLSQL_DEBUG`  
`PLSQL_OPTIMIZE_LEVEL`  
`PLSQL_V2_COMPATIBILITY`  
`PLSQL_WARNINGS`  
`QUERY_REWRITE_ENABLED`  
`QUERY_REWRITE_INTEGRITY`  
`RECYCLEBIN`  
`REMOTE_DEPENDENCIES_MODE`  
`RESULT_CACHE_MODE`  
`RESULT_CACHE_REMOTE_EXPIRATION`  
`RESUMABLE_TIMEOUT`  
`SESSION_CACHED_CURSORS`  
`SKIP_UNUSABLE_INDEXES`  
`SMTP_OUT_SERVER`  
`SORT_AREA_RETAINED_SIZE`  
`SORT_AREA_SIZE`  
`SQL_TRACE`  
`SQLTUNE_CATEGORY`  
`STAR_TRANSFORMATION_ENABLED`  
`STATISTICS_LEVEL`  
`TIMED_OS_STATISTICS`  
`TIMED_STATISTICS`  
`TRACEFILE_IDENTIFIER`  
`WORKAREA_SIZE_POLICY`  
`XML_DB_EVENTS`  

The `ALTER SYSTEM` statement without the `DEFERRED` keyword modifies the global value of the parameter for all sessions in the instance, for the duration of the instance (until the database is shut down). The value of the following initialization parameters can be changed with `ALTER SYSTEM`:

  
`AQ_TM_PROCESSES`  
`ARCHIVE_LAG_TARGET`  
`ASM_DISKGROUPS`  
`ASM_DISKSTRING`  
`ASM_POWER_LIMIT`  
`ASM_PREFERRED_READ_FAILURE_GROUPS`  
`AWR_SNAPSHOT_TIME_OFFSET`  
`BACKGROUND_DUMP_DEST`  
`CIRCUITS`  
`COMMIT_LOGGING`  
`COMMIT_WAIT`  
`COMMIT_WRITE`  
`CONTROL_FILE_RECORD_KEEP_TIME`  
`CONTROL_MANAGEMENT_PACK_ACCESS`  
`CORE_DUMP_DEST`  
`CPU_COUNT`  
`CREATE_STORED_OUTLINES`  
`CURSOR_BIND_CAPTURE_DESTINATION`  
`CURSOR_SHARING`  
`DB_` `n` `K_CACHE_SIZE`  
`DB_BLOCK_CHECKING`  
`DB_BLOCK_CHECKSUM`  
`DB_CACHE_ADVICE`  
`DB_CACHE_SIZE`  
`DB_CREATE_FILE_DEST`  
`DB_CREATE_ONLINE_LOG_DEST_` `n`  
`DB_FILE_MULTIBLOCK_READ_COUNT`  
`DB_FLASH_CACHE_SIZE`  
`DB_FLASHBACK_RETENTION_TARGET`  
`DB_KEEP_CACHE_SIZE`  
`DB_LOST_WRITE_PROTECT`  
`DB_RECOVERY_FILE_DEST`  
`DB_RECOVERY_FILE_DEST_SIZE`  
`DB_RECYCLE_CACHE_SIZE`  
`DB_SECUREFILE`  
`DB_UNRECOVERABLE_SCN_TRACKING`  
`DDL_LOCK_TIMEOUT`  
`DEFERRED_SEGMENT_CREATION`  
`DG_BROKER_CONFIG_FILE` `n`  
`DG_BROKER_START`  
`DIAGNOSTIC_DEST`  
`DISPATCHERS`  
`DST_UPGRADE_INSERT_CONV`  
`ENABLE_DDL_LOGGING`  
`ENABLE_GOLDENGATE_REPLICATION`  
`FAL_CLIENT`  
`FAL_SERVER`  
`FAST_START_MTTR_TARGET`  
`FAST_START_PARALLEL_ROLLBACK`  
`FILE_MAPPING`  
`FIXED_DATE`  
`GLOBAL_NAMES`  
`GLOBAL_TXN_PROCESSES`  
`HS_AUTOREGISTER`  
`JAVA_JIT_ENABLED`  
`JAVA_POOL_SIZE`  
`JOB_QUEUE_PROCESSES`  
`LARGE_POOL_SIZE`  
`LDAP_DIRECTORY_ACCESS`  
`LICENSE_MAX_SESSIONS`  
`LICENSE_MAX_USERS`  
`LICENSE_SESSIONS_WARNING`  
`LISTENER_NETWORKS`  
`LOCAL_LISTENER`  
`LOG_ARCHIVE_CONFIG`  
`LOG_ARCHIVE_DEST`  
`LOG_ARCHIVE_DEST_` `n`  
`LOG_ARCHIVE_DEST_STATE_` `n`  
`LOG_ARCHIVE_DUPLEX_DEST`  
`LOG_ARCHIVE_LOCAL_FIRST`  
`LOG_ARCHIVE_MAX_PROCESSES`  
`LOG_ARCHIVE_MIN_SUCCEED_DEST`  
`LOG_ARCHIVE_TRACE`  
`LOG_CHECKPOINT_INTERVAL`  
`LOG_CHECKPOINT_TIMEOUT`  
`LOG_CHECKPOINTS_TO_ALERT`  
`MAX_DISPATCHERS`  
`MAX_DUMP_FILE_SIZE`  
`MAX_SHARED_SERVERS`  
`MEMORY_TARGET`  
`NLS_LENGTH_SEMANTICS`  
`NLS_NCHAR_CONV_EXCP`  
`OPEN_CURSORS`  
`OPTIMIZER_CAPTURE_SQL_PLAN_BASELINES`  
`OPTIMIZER_DYNAMIC_SAMPLING`  
`OPTIMIZER_FEATURES_ENABLE`  
`OPTIMIZER_INDEX_CACHING`  
`OPTIMIZER_INDEX_COST_ADJ`  
`OPTIMIZER_MODE`  
`OPTIMIZER_SECURE_VIEW_MERGING`  
`OPTIMIZER_USE_INVISIBLE_INDEXES`  
`OPTIMIZER_USE_PENDING_STATISTICS`  
`OPTIMIZER_USE_SQL_PLAN_BASELINES`  
`PARALLEL_ADAPTIVE_MULTI_USER`  
`PARALLEL_DEGREE_LIMIT`  
`PARALLEL_DEGREE_POLICY`  
`PARALLEL_FORCE_LOCAL`  
`PARALLEL_INSTANCE_GROUP`  
`PARALLEL_IO_CAP_ENABLED`  
`PARALLEL_MAX_SERVERS`  
`PARALLEL_MIN_SERVERS`  
`PARALLEL_MIN_TIME_THRESHOLD`  
`PARALLEL_SERVERS_TARGET`  
`PARALLEL_THREADS_PER_CPU`  
`PGA_AGGREGATE_TARGET`  
`PLSCOPE_SETTINGS`  
`PLSQL_CCFLAGS`  
`PLSQL_CODE_TYPE`  
`PLSQL_DEBUG`  
`PLSQL_OPTIMIZE_LEVEL`  
`PLSQL_V2_COMPATIBILITY`  
`PLSQL_WARNINGS`  
`QUERY_REWRITE_ENABLED`  
`QUERY_REWRITE_INTEGRITY`  
`REDO_TRANSPORT_USER`  
`REMOTE_DEPENDENCIES_MODE`  
`REMOTE_LISTENER`  
`RESOURCE_LIMIT`  
`RESOURCE_MANAGER_CPU_ALLOCATION`  
`RESOURCE_MANAGER_PLAN`  
`RESULT_CACHE_MAX_RESULT`  
`RESULT_CACHE_MAX_SIZE`  
`RESULT_CACHE_MODE`  
`RESULT_CACHE_REMOTE_EXPIRATION`  
`RESUMABLE_TIMEOUT`  
`SEC_CASE_SENSITIVE_LOGON`  
`SEC_PROTOCOL_ERROR_FURTHER_ACTION`  
`SEC_PROTOCOL_ERROR_TRACE_ACTION`  
`SERVICE_NAMES`  
`SGA_TARGET`  
`SHARED_POOL_SIZE`  
`SHARED_SERVER_SESSIONS`  
`SHARED_SERVERS`  
`SKIP_UNUSABLE_INDEXES`  
`SMTP_OUT_SERVER`  
`SPFILE`  
`SQL_TRACE`  
`SQLTUNE_CATEGORY`  
`STANDBY_ARCHIVE_DEST`  
`STANDBY_FILE_MANAGEMENT`  
`STAR_TRANSFORMATION_ENABLED`  
`STATISTICS_LEVEL`  
`STREAMS_POOL_SIZE`  
`THREAD`  
`TIMED_OS_STATISTICS`  
`TIMED_STATISTICS`  
`TRACE_ENABLED`  
`UNDO_RETENTION`  
`UNDO_TABLESPACE`  
`USER_DUMP_DEST`  
`WORKAREA_SIZE_POLICY`  
`XML_DB_EVENTS`  

The `ALTER SYSTEM ... DEFERRED` statement does not modify the global value of the parameter for existing sessions, but the value will be modified for future sessions that connect to the database. The value of the following initialization parameters can be changed with `ALTER SYSTEM ... DEFERRED`:

  
`AUDIT_FILE_DEST`  
`BACKUP_TAPE_IO_SLAVES`  
`OBJECT_CACHE_MAX_SIZE_PERCENT`  
`OBJECT_CACHE_OPTIMAL_SIZE`  
`OLAP_PAGE_POOL_SIZE`  
`RECYCLEBIN`  
`SORT_AREA_RETAINED_SIZE`  
`SORT_AREA_SIZE`

## Displaying Current Parameter Values

To see the current settings for initialization parameters, use the following SQL\*Plus command:

```
SQL> SHOW PARAMETERS
```

This command displays all parameters in alphabetical order, along with their current values.

Enter the following text string to display all parameters having `BLOCK` in their names:

```
SQL> SHOW PARAMETERS BLOCK
```

You can use the `SPOOL` command to write the output to a file.

## Parameters You Should Not Specify in the Parameter File

You should not specify the following two types of parameters in your parameter files:

- Parameters that you never alter except when instructed to do so by Oracle to resolve a problem
- Derived parameters, which normally do not need altering because their values are calculated automatically by the Oracle database server

## When Parameters Are Set Incorrectly

Some parameters have a minimum setting below which an Oracle instance will not start. For other parameters, setting the value too low or too high may cause Oracle to perform badly, but it will still run. Also, Oracle may convert some values outside the acceptable range to usable levels.

If a parameter value is too low or too high, or you have reached the maximum for some resource, then Oracle returns an error. Frequently, you can wait a short while and retry the operation when the system is not as busy. If a message occurs repeatedly, then you should shut down the instance, adjust the relevant parameter, and restart the instance.