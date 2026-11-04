---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/DBMS_AUTO_REPORT.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 34 DBMS\_AUTO\_REPORT

The `DBMS_AUTO_REPORT` package provides an interface to view SQL Monitoring and Real-time Automatic Database Diagnostic Monitor (ADDM) data that has been captured into Automatic Workload Repository (AWR). It also provides subprograms to control the behavior of how these data are captured to AWR.

See Also:

[Oracle Database SQL Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=TGSQL94607) for more information about reporting database operations

This chapter contains the following topics:

### 34.1 DBMS\_AUTO\_REPORT Overview

This package provides an interface to view SQL Monitoring and Real-time ADDM data that has been captured into AWR. It also provides subprograms to control the behavior of how these data are captured to AWR.Captured data are stored in AWR and exposed via 2 views: `DBA_HIST_REPORTS` and `DBA_HIST_REPORTS_DETAILS`.

### 34.2 DBMS\_AUTO\_REPORT Security Model

This package is available to `PUBLIC` and performs its own security checking.

### 34.3 Summary of DBMS\_AUTO\_REPORT Subprograms

This table describes the parameters of the `DBMS_AUTO_REPORT` package subprograms.

Table 34-1 DBMS\_AUTO\_REPORT Package Subprograms

| Subprogram | Description |
| --- | --- |
| FINISH\_REPORT\_CAPTURE Procedure | Ends the complete capture of SQL monitor data that was started with the START\_REPORT\_CAPTURE Procedure. |
| REPORT\_REPOSITORY\_DETAIL Function | Obtains the stored report for a given report ID |
| REPORT\_REPOSITORY\_DETAIL\_XML Function | Obtains the stored XML report for a given report ID |
| REPORT\_REPOSITORY\_LIST\_XML Function | Obtains an XML report of the list of SQL Monitor and Real-time ADDM data captured in AWR |
| START\_REPORT\_CAPTURE Procedure | Captures SQL monitor data of any newly monitored SQLs every minute since the last run of the capture cycle, and stores it in AWR. |

#### 34.3.1 FINISH\_REPORT\_CAPTURE Procedure

This procedure ends the complete capture of SQL monitor data that was started with the `START_REPORT_CAPTURE` procedure.

After calling this subprogram, capture of data continues every minute except that it is not captured for all active SQLs but only for those deemed important, namely the top 5 SQLs (by elapsed time, or elapsed time\*DOP in case of PQ) whose monitoring has completed.

Syntax

```
DBMS_AUTO_REPORT.FINISH_REPORT_CAPTURE;
```

#### 34.3.2 REPORT\_REPOSITORY\_DETAIL Function

This procedure obtains the stored report for a given report ID in the specified format such as XML or HTML.

Syntax

```
DBMS_AUTO_REPORT.REPORT_REPOSITORY_DETAIL (
   rid              IN NUMBER    DEFAULT NULL,
   type             IN VARCHAR2  DEFAULT 'XML',
   base_path        IN VARCHAR2  DEFAULT NULL)
 RETURNS CLOB
```

Parameters

Table 34-2 REPORT\_REPOSITORY\_DETAIL Function Parameters

| Parameter | Description |
| --- | --- |
| `rid` | ID of the stored report which returned by the function |
| `type` | Desired format of the report. Values can be `'XML'`, `'TEXT'`, ' `HTML'`, `'EM'` or ` 'ACTIVE'`. The last two options generate a report in the same format called active HTML. Default value is `'XML'`. |
| `base_path` | Unused/Non-operative |

Return Values

The persisted report for the given record ID

#### 34.3.3 REPORT\_REPOSITORY\_DETAIL\_XML Function

This procedure obtains the stored XML report for a given report ID.

Syntax

```
DBMS_AUTO_REPORT.REPORT_REPOSITORY_DETAIL_XML (
   rid              IN NUMBER    DEFAULT NULL,
   base_path        IN VARCHAR2  DEFAULT NULL)
 RETURNS XMLTYPE
```

Parameters

Table 34-3 REPORT\_REPOSITORY\_DETAIL\_XML Function Parameters

| Parameter | Description |
| --- | --- |
| `rid` | ID of the stored report which returned by the function |
| `base_path` | Unused/Non-operative |

Return Values

The persisted XML report for the given record ID

#### 34.3.4 REPORT\_REPOSITORY\_LIST\_XML Function

This procedure obtains an XML report of the list of SQL Monitor and Real-time ADDM data captured in AWR.

The input parameters can be used to select and restrict which captured data will be included in the list report. All parameters are optional.

Syntax

```
DBMS_AUTO_REPORT.REPORT_REPOSITORY_LIST_XML (
    active_since              IN DATE     DEFAULT NULL,
    active_upto               IN DATE     DEFAULT NULL,
    snapshot_id               IN NUMBER   DEFAULT NULL,
    dbid                      IN NUMBER   DEFAULT NULL,
    inst_id                   IN NUMBER   DEFAULT NULL,
    con_dbid                  IN NUMBER   DEFAULT NULL,
    session_id                IN NUMBER   DEFAULT NULL,
    session_serial            IN NUMBER   DEFAULT NULL,
    component_name            IN VARCHAR2 DEFAULT NULL,
    key1                      IN VARCHAR2 DEFAULT NULL,
    key2                      IN VARCHAR2 DEFAULT NULL,
    key3                      IN VARCHAR2 DEFAULT NULL,
    report_level              IN VARCHAR2 DEFAULT 'TYPICAL',
    base_path                 IN VARCHAR2 DEFAULT NULL)
RETURNS XMLTYPE
```

Parameters

Table 34-4 REPORT\_REPOSITORY\_LIST\_XML Function Parameters

| Parameter | Description |
| --- | --- |
| `active_since` | Start of a time range used to select data. When a time range is specified, only those data are included in the list that were active during the time range. When no value is specified the time range is chosen as the last 24 hours ending at the current system time. |
| `active_upto` | Same as `active_since` except that it is the end of the time range |
| `snapshot_id` | If a value is specified, only those data captured during the specified snapshot ID are included in the list report. If no value is specified, no filtering is performed on snapshot ID. |
| `dbid` | If a value is specified, only those data captured for the specified database ID are included in the list report. If no value is specified, no filtering is performed on database ID |
| `inst_id` | If a value is specified, only those data captured on the specified instance number are included in the list report. If no value is specified, no filtering is performed on the instance ID. |
| `con_dbid` | If a value is specified, only those data captured on the specified container DBID are included in the list report. If no value is specified, no filtering is performed on the container DBID. |
| `session_id` | If a value is specified, only those data captured for the specified session ID are included in the list report. If no value is specified, no filtering is performed on session ID. |
| `session_serial` | If a value is specified, only those data captured for the specified session are included in the list report. If no value is specified, no filtering is performed on session serial number. This parameter should be used in conjunction with the `session_id` parameter. |
| `component_name` | Can be `'sqlmonitor'` for SQL Monitor data or `'rtaddm'` for Real-time ADDM data. If a value is specified then data pertaining only to the specified component will be included in the list report. If no value is specified, no filtering is performed. |
| `key1` | Key value relevant to a component. For SQL Monitor, `key1` is the SQL ID of the captured SQL statement. If a value is specified, only those data having specified value for `key1` are included, else no filtering is performed on `key1`. |
| `key2` | Key value relevant to a component. For SQL Monitor, `key2` is the SQL execution ID of the captured SQL statement. If a value is specified, only those data having specified value for `key2` are included, else no filtering is performed on `key2`. |
| `key3` | Key value relevant to a component. For SQL Monitor, `key3` is the SQL execution start time of the captured SQL statement. If a value is specified, then only those data having specified value for `key3` are included, else no filtering is performed on `key3`. |
| `report_level` | Currently only `'TYPICAL'` is used |
| `base_path` | Unused/Non-operative |

#### 34.3.5 START\_REPORT\_CAPTURE Procedure

This procedure captures SQL monitor data of any newly monitored SQLs every minute since the last run of the capture cycle, and stores it in AWR.

Every capture cycle attempts to capture data for SQLs that are not currently executing or queued. This is a complete capture since data of all newly monitored SQLs is captured. It continues to run every minute until it is explicitly ended with the FINISH\_REPORT\_CAPTURE Procedure. In the case of a RAC system, the capture will start on each node of the cluster.

Syntax

```
DBMS_AUTO_REPORT.START_REPORT_CAPTURE;
```