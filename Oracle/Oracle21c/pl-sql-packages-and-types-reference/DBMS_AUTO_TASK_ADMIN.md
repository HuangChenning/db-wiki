---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/DBMS_AUTO_TASK_ADMIN.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 35 DBMS\_AUTO\_TASK\_ADMIN

The `DBMS_AUTO_TASK_ADMIN` package provides an interface to `AUTOTASK` functionality. It is used by the DBA as well as Enterprise Manager to access the `AUTOTASK` controls. Enterprise Manager also uses the `AUTOTASK` Advisor.

See Also:

Oracle Database Administrator's Guide for more information about ["Configuring Automated Maintenance Task"](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADMIN12332)

This chapter contains the following sections:

### 35.1 DBMS\_AUTO\_TASK\_ADMIN Deprecated Subprograms

The DBMS\_AUTO\_TASK\_ADMIN OVERRIDE\_PRIORITY subprogram has been deprecated.

Note:

Oracle recommends that you do not use deprecated procedures in new applications. Support for deprecated features is for backward compatibility only.

- OVERRIDE\_PRIORITY Procedures

### 35.2 DBMS\_AUTO\_TASK\_ADMIN Security Model

`DBMS_AUTO_TASK_ADMIN` is a definer's rights package, and `EXECUTE` is automatically granted to `DBA`, `IMP_FULL_DATABASE` and `DATAPUMP_IMP_FULL_DATABASE`.

### 35.3 DBMS\_AUTO\_TASK\_ADMIN Constants

The `DBMS_AUTO_TASK_ADMIN` package defines several constants that can be used for specifying parameter values.

These constants shown in the following table:

Table 35-1 DBMS\_AUTO\_TASK\_ADMIN Constants

| Name | Type | Value | Description |
| --- | --- | --- | --- |
| `PRIORITY_MEDIUM` | `VARCHAR2` | `'MEDIUM'` | Task with this priority should be executed as time permits |
| `PRIORITY_HIGH` | `VARCHAR2` | `'HIGH'` | Task with this priority should be executed within the current Maintenance Window |
| `PRIORITY_URGENT` | `VARCHAR2` | `'URGENT'` | Task with this priority is to be executed at the earliest opportunity |

### 35.4 Summary of DBMS\_AUTO\_TASK\_ADMIN Subprograms

This table lists the `DBMS_AUTO_TASK_ADMIN` subprograms and briefly describes them.

Table 35-2 DBMS\_AUTO\_TASK\_ADMIN Package Subprograms

| Method | Description |
| --- | --- |
| DISABLE Procedures | Prevents `AUTOTASK` from executing any requests from a specified client or operation. |
| ENABLE Procedures | Allows a previously disabled client, operation, target type, or individual target to be enabled under `AUTOTASK` control |
| GET\_CLIENT\_ATTRIBUTES Procedure | Returns values of select client attributes |
| GET\_P1\_RESOURCES Procedure | Returns percent of resources allocated to each `AUTOTASK` High Priority Consumer Groups |
| OVERRIDE\_PRIORITY Procedures | Manually overrides task priority. |
| SET\_CLIENT\_SERVICE Procedure | Associates an `AUTOTASK` Client with a specified Service |
| SET\_P1\_RESOURCES Procedure | Sets percentage-based resource allocation for each High Priority Consumer Group used by `AUTOTASK` Clients |

#### 35.4.1 DISABLE Procedures

This procedure prevents `AUTOTASK` from executing any requests from a specified client or operation.

Syntax

Disables all `AUTOTASK` functionality.

```
DBMS_AUTO_TASK_ADMIN.DISABLE;
```

Disables all tasks for the client or operation.

```
DBMS_AUTO_TASK_ADMIN.DISABLE (
   client_name       IN    VARCHAR2,
   operation         IN    VARCHAR2,
   window_name       IN    VARCHAR2);
```

Parameters

Table 35-3 DISABLE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `client_name` | Name of the client, as found in `DBA_AUTOTASK_CLIENT` View |
| `operation` | Name of the operation as specified in `DBA_AUTOTASK_OPERATION` View |
| `window_name` | Optional name of the window in which client is to be disabled |

Usage Notes

- If `operation` and `window_name` are both `NULL`, the client is disabled.
- If `operation` is not `NULL`, `window_name` is ignored and the operation is disabled
- If `operation` is `NULL` and `window_name` is not `NULL`, the client is disabled in the specified window.
- `Auto STS Capture Task` is accepted.

#### 35.4.2 ENABLE Procedures

This procedure allows a previously disabled client, operation, target type, or individual target to be enabled under `AUTOTASK` control.

Specifying the `DEFERRED` option postpones the effect of the call until the start of the next maintenance window. If `IMMEDIATE` option is specified the effect of this call is immediate – as long as there is a currently open maintenance window.

Syntax

Re-enabling `AUTOTASK`. This version enables the specified client. Note that any explicitly disabled tasks or operations must be re-enabled individually.

```
DBMS_AUTO_TASK_ADMIN.ENABLE;
```

Re-enabling a client or operation.Note that any explicitly disabled tasks or operations must be re-enabled individually.

```
DBMS_AUTO_TASK_ADMIN.ENABLE (
   client_name       IN    VARCHAR2,
   operation         IN    VARCHAR2,
   window_name       IN    VARCHAR2);
```

Parameters

Table 35-4 ENABLE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `client_name` | Name of the client, as found in `DBA_AUTOTASK_CLIENT` View |
| `operation` | Name of the operation as specified in `DBA_AUTOTASK_OPERATION` View |
| `window_name` | Optional name of the window in which client is to be enabled |

Usage Notes

- If `operation` and `window_name` are both `NULL`, the client is enabled.
- If `operation` is not `NULL`, `window_name` is ignored and the specified operation is enabled
- If `operation` is `NULL` and `window_name` is not `NULL`, the client is enabled in the specified window.
- `Auto STS Capture Task` is accepted.

#### 35.4.3 GET\_CLIENT\_ATTRIBUTES Procedure

This procedure returns values of select client attributes.

Syntax

```
DBMS_AUTO_TASK_ADMIN.GET_CLIENT_ATTRIBUTES(
   client_name        IN    VARCHAR2,   service_name       OUT   VARCHAR2,   window_group       OUT   VARCHAR2);
```

Parameters

Table 35-5 GET\_CLIENT\_ATTRIBUTES Procedure Parameters

| Parameter | Description |
| --- | --- |
| `client_name` | Name of the client, as found in `DBA_AUTOTASK_CLIENT` View |
| `service_name` | Service name for client, may be `NULL` |
| `window_group` | Name of the window group in which the client is active |

#### 35.4.4 GET\_P1\_RESOURCES Procedure

This procedure returns percent of resources allocated to each `AUTOTASK` High Priority Consumer Group.

Syntax

```
DBMS_AUTO_TASK_ADMIN.GET_P1_RESOURCES(
   stats_group_pct     OUT   NUMBER,
   seg_group_pct       OUT   NUMBER,
   tune_group_pct      OUT   NUMBER,
   health_group_pct    OUT   NUMBER);
```

Parameters

Table 35-6 GET\_P1\_RESOURCES Procedure Parameters

| Parameter | Description |
| --- | --- |
| `stats_group_pct` | %resources for Statistics Gathering |
| `seq_group_pct` | %resources for Space Management |
| `tune_group_pct` | %resources for SQL Tuning |
| `health_group_pct` | %resources for Health Checks |

Usage Notes

Values will add up to 100%.

#### 35.4.5 OVERRIDE\_PRIORITY Procedures

This deprecated procedure is used to manually override task priority.

Note:

This subprogram is deprecated and becomes nonoperative with Oracle Database 12c.

This can be done at the client, operation or individual task level. This priority assignment is honored during the next maintenance window in which the named client is active. Specifically, setting the priority to `URGENT` causes a high priority job to be generated at the start of the maintenance window. Setting `priority` to `CLEAR` removes the override.

Syntax

Override Priority for a Client.

```
DBMS_AUTO_TASK_ADMIN.OVERRIDE_PRIORITY (
   client_name       IN    VARCHAR2,
   priority          IN    VARCHAR2);
```

Override Priority for an Operation.

```
DBMS_AUTO_TASK_ADMIN.OVERRIDE_PRIORITY (
   client_name       IN    VARCHAR2,
   operation         IN    VARCHAR2,
   priority          IN    VARCHAR2);
```

Override Priority for a Task.

```
DBMS_AUTO_TASK_ADMIN.OVERRIDE_PRIORITY (
   client_name       IN    VARCHAR2,
   operation         IN    VARCHAR2,
   task_target_type  IN    VARCHAR2,
   task_target_name  IN    VARCHAR2,
   priority          IN    VARCHAR2);
```

Parameters

Table 35-7 OVERRIDE\_PRIORITY Procedure Parameters

| Parameter | Description |
| --- | --- |
| `client_name` | Name of the client, as found in `DBA_AUTOTASK_CLIENT` View |
| `priority` | `URGENT`, `HIGH`, `MEDIUM` or `LOW` |
| `operation` | Name of the operation as specified in `DBA_AUTOTASK_OPERATION` View |
| `task_target_type` | Type of target to be affected, as found in V$ `AUTOTASK_TARGET_TYPE` View |
| `task_target_name` | Name of the specific target to be affected |

#### 35.4.6 SET\_CLIENT\_SERVICE Procedure

This procedure associates an `AUTOTASK` Client with a specified Service.

Syntax

```
DBMS_AUTO_TASK_ADMIN.SET_CLIENT_SERVICE(
   client_name        IN    VARCHAR2,
   service_name       IN   VARCHAR2);
```

Parameters

Table 35-8 SET\_CLIENT\_SERVICE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `client_name` | Name of the client, as found in `DBA_AUTOTASK_CLIENT` View |
| `service_name` | Service name for client, may be `NULL` |

Usage Notes

All work performed on behalf of the Client takes place only on instances where the service is enabled.

#### 35.4.7 SET\_P1\_RESOURCES Procedure

This procedure sets percentage-based resource allocation for each High Priority Consumer Group used by `AUTOTASK` Clients.

Syntax

```
DBMS_AUTO_TASK_ADMIN.SET_P1_RESOURCES(
   stats_group_pct     IN   NUMBER,
   seg_group_pct       IN   NUMBER,
   tune_group_pct      IN   NUMBER,
   health_group_pct    IN   NUMBER);
```

Parameters

Table 35-9 SET\_P1\_RESOURCES Procedure Parameters

| Parameter | Description |
| --- | --- |
| `stats_group_pct` | %resources for Statistics Gathering |
| `seq_group_pct` | %resources for Space Management |
| `tune_group_pct` | %resources for SQL Tuning |
| `health_group_pct` | %resources for Health Checks |

Usage Notes

Values must be integers in the range `0` to `100`, and must add up to `100` (percent), otherwise, an exception is raised.