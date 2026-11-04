---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/DBMS_MVIEW_STATS.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 120 DBMS\_MVIEW\_STATS

`DBMS_MVIEW_STATS` package provides an interface to manage the collection and retention of statistics for materialized view refresh operations.

See Also:

[Oracle Database Data Warehousing Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=DWHSG-GUID-6AD8879A-0BE5-466E-8D19-1D076C5DDFFB) for information about managing and using materialized view refresh statistics

This chapter contains the following topics:

### 120.1 DBMS\_MVIEW\_STATS Overview

You can use the procedures contained in the `DBMS_MVIEW_STATS` package to manage the collection and retention of statistics for materialized view refresh operations. This includes the level and granularity at which these statistics are collected and the duration for which they are retained in the database.

You can also set database level system defaults for the parameters that control statistics collection.

### 120.2 DBMS\_MVIEW\_STATS Security Model

Refer to the Usage Notes section in each subprogram for information about the privileges required to use the subprogram.

### 120.3 Summary of DBMS\_MVIEW\_STATS Subprograms

This table lists the `DBMS_MVIEW_STATS` subprograms and briefly describes them.

Table 120-1 DBMS\_MVIEW\_STATS Package Subprograms

| Subprogram | Description |
| --- | --- |
| PURGE\_REFRESH\_STATS Procedure | Purges the statistics of materialized view refresh operations that are older than the specified retention period. |
| SET\_MVREF\_STATS\_PARAMS Procedure | Sets the values of parameters that define the collection level and retention period for materialized view refresh statistics. You can set the values either at the database level or for individual materialized views. |
| SET\_SYSTEM\_DEFAULT Procedure | Sets the system default value of a refresh statistics parameter. The two refresh statistics parameters are collection level and the retention period. |

#### 120.3.1 PURGE\_REFRESH\_STATS Procedure

This procedure purges refresh statistics that are older than the specified retention period for the specified materialized views.

This procedure forces a purge of refresh statistics without altering the retention period defined for the specified materialized views.

Syntax

```
DBMS_MVIEW_STATS.PURGE_REFRESH_STATS (
        mv_list               IN     VARACHAR2,
        retention_period      IN     NUMBER);
```

Parameters

Table 120-2 PURGE\_REFRESH\_STATS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `mv_list` | The fully-qualified name of an existing materialized view in the form of `schema_name`.`mv_name`. Use a comma-separated list to specify multiple materialized views.  Specify `NULL` to purge materialized view refresh statistics for all materialized views in the database. |
| `retention_period` | The number of days for which refresh statistics must be preserved in the data dictionary. Statistics for materialized view refresh operations that are older than the retention period are purged from the data dictionary.  The retention period specified in this procedure overrides the retention period that may have been set previously either at the database level or for specified materialized views.  Specify `NULL` to use the purging policy defined by the automatic statistics purge. Specify –1 to purge all refresh statistics. |

Usage Notes

To invoke this procedure, you need either the `SYSDBA` privilege or privileges on every materialized view that is specified in `mv_list`.

#### 120.3.2 SET\_MVREF\_STATS\_PARAMS Procedure

This procedure sets the collection level and retention period for materialized view refresh statistics. You can set these properties either for individual materialized views or for all materialized views in the database.

Syntax

```
DBMS_MVIEW_STATS.SET_MVREF_STATS_PARAMS (
        mv_list            IN    VARACHAR2,
        collection_level   IN    VARCHAR2 DEFAULT NULL,
        retention_period   IN    NUMBER DEFAULT NULL);
```

Parameters

Table 120-3 SET\_MVREF\_STATS\_PARAMS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `mv_list` | The fully-qualified name of an existing materialized view in the form of `schema_name`.`mv_name`. Use a comma-separated list to specify multiple materialized views.  Specify `NULL` to set properties for all existing materialized views in the database. |
| `collection_level` | Specifies the level of detail used when collecting refresh statistics for the materialized views specified in `mv_list`.  Set one of the following values for `collection_level`:  - NONE: No materialized view refresh statistics are collected. - TYPICAL: Only basic refresh statistics are collected and stored for the materialized views specified in `mv_list`. - ADVANCED: Detailed refresh statistics are collected and stored for materialized view specified in `mv_list`.  If this parameter is set to `NULL`, then the system default value for `collection_level` (set using `SET_SYSTEM_DEFAULT`) is used. |
| `retention_period` | Specifies the retention period, in days, for the refresh statistics of the materialized views specified in `mv_list`. Statistics that are older than the retention period are automatically purged from the data dictionary.  Valid values are between 1 and 1365000.  If this parameter is set to `NULL`, then the system default value for `retention_period` (set using `SET_SYSTEM_DEAFULT`) is used.  Set `retention_period` to -1 to specify that refresh statistics for the materialized views in `mv_list` must never be purged. |

Usage Notes

To set the collection level or retention period of one or more materialized views, you must have privileges on those materialized views. To set the collection level or retention period for all materialized views in the database, you must have either the `SYSDBA` privilege or privileges on every materialized view in the database.

To set the system-level default values for statistics collection level and retention period, use the `SET_SYSTEM_DEAFULT` procedure.

Use the `DBA_MVREF_STATS_PARAMS` view to determine the currently-set retention period and collection level for materialized view statistics collection.

To disable refresh statistics collection for all materialized views in the database, use the following:

`DBMS_MVIEW_STATS.SET_MVREF_STATS_PARAMS (NULL, ‘NONE’, NULL);`

Note that the parameters set using `SET_MVREF_STATS_PARAMS` only affect materialized views that exist in the database at the time the procedure is run. Any new materialized views created after this procedure is run will use the system default values for `collection_level` and `retention_period`.

#### 120.3.3 SET\_SYSTEM\_DEFAULT Procedure

This procedure sets system-wide defaults that manage the collection and retention of materialized view refresh statistics. All newly-created materialized views use these defaults until the parameters are reset explicitly using the `SET_MVREF_STATS_PARAMS` procedure.

Syntax

```
DBMS_MVIEW_STATS.SET_SYSTEM_DEFAULT (
        parameter_name        IN   VARCHAR2,
        value             IN   VARCHAR2 DEFAULT NULL);
```

Parameters

Table 120-4 SET\_SYSTEM\_DEFAULT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `parameter_name` | The name of the materialized view refresh statistics parameter whose system default value is being set.  The parameters that can be set are:  - `COLLECTION_LEVEL`: Specifies the level of detail for collecting materialized view refresh statistics. - `RETENTION_PERIOD`: Specifies the duration, in days, for which refresh statistics are retained in the data dictionary |
| `value` | The value of the materialized view refresh statistics parameter.  The valid values for `COLLECTION_LEVEL` are:  - NONE: No refresh statistics are collected for the refresh operation. - TYPICAL: Only basic refresh statistics are collected for the refresh operation. This is the default setting. - ADVANCED: Detailed refresh statistics are collected for the refresh operation.  The valid values for `RETENTION_PERIOD` are:  - \-1 - Numbers between 1 and 1365000  The default value for `retention_period` is 31.  If you specify `NULL` for any of the parameters, then the system default setting for that parameter is used. |

Usage Notes

You must have `SYSDBA` privilege to invoke this procedure.

Use the `DBA_MVREF_STATS_SYS_DEFAULTS` view to display the current default settings for materialized view refresh statistics collection.