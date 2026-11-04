---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/dbms_blocker_resolver1.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 85 DBMS\_HANG\_MANAGER

The DBMS\_HANG\_MANAGER package provides a method of changing some Hang Manager configuration parameters.

This chapter contains the following topics:

### 85.1 DBMS\_HANG\_MANAGER Overview

The DBMS\_HANG\_MANAGER package provides a method of changing some Hang Manager configuration parameters.

Hang Manager is always enabled on all databases, Automatic Storage Management (ASM) disk groups, and single instance systems (when not using Oracle RAC). Hang resolution is enabled on all instances by default except for single instance systems (when not using Oracle RAC) where it is disabled and cannot be enabled at this time.

Note:

The `DBMS_HANG_MANAGER` package is intended for use by database administrators (DBA) only. It is not intended for use by application developers.

### 85.2 DBMS\_HANG\_MANAGER Security Model

DBMS\_HANG\_MANAGER can only be run as the `SYS` user.

### 85.3 DBMS\_HANG\_MANAGER Constants

The table in this topic lists DBMS\_HANG\_MANAGER package constants.

Table 85-1 DBMS\_HANG\_MANAGER Constants

| Name | Type | Value | Description |
| --- | --- | --- | --- |
| `RESOLUTION_SCOPE` | `VARCHAR2` | `resolution scope` | Resolution scope parameter name |
| `SENSITIVITY` | `VARCHAR2` | `sensitivity` | Sensitivity parameter name |
| `BASE_FILE_SIZE_LIMIT` | `VARCHAR2` | `base file size limit` | Base file size limit parameter name. The default value of this parameter is `100 MB.` |
| `BASE_FILE_SET_COUNT` | `VARCHAR2` | `base file set count` | Base file set count parameter name. The default value is `5` trace files in the circular trace file set. |
| `LWS_FILE_SIZE_LIMIT` | `VARCHAR2` | `long waiting session file size limit` | Long waiting session file size limit parameter name. The default value of this parameter is `100 MB.` |
| `LWS_FILE_SET_COUNT` | `VARCHAR2` | `long waiting session set count` | Long waiting session set count parameter name. The default value is `5` trace files in the circular trace file set. |
| `RESOLUTION_SCOPE_PROCESS` | `VARCHAR2` | `PROCESS` | Enables only session and/or process termination |
| `RESOLUTION_SCOPE_INSTANCE` | `VARCHAR2` | `INSTANCE` | Enables session, process, and instance termination. The latter is used in specific scenarios. The default value is `INSTANCE`. |
| `SENSITIVITY_NORMAL` | `VARCHAR2` | `NORMAL` | Sets various Hang Manager intervals to their default values. The default value is `NORMAL`. |
| `SENSITIVITY_HIGH` | `VARCHAR2` | `HIGH` | Sets the various Hang Manager intervals to half of their default values |

### 85.4 DBMS\_HANG\_MANAGER Exceptions

The table in this topic lists the exceptions raised by the DBMS\_HANG\_MANAGER package.

Table 85-2 DBMS\_HANG\_MANAGER Package Exceptions

| Exception | Error Code | Description |
| --- | --- | --- |
| `ERRNUM_INPUT_ERROR` | `-32706` | Invalid user input |
| `ERRNUM_INTERNAL_ERROR` | `-32707` | Database experienced an error setting a parameter |
| `ERRNUM_UNSUPPORTED_ERROR` | `-32708` | Operation is not supported on this instance type |

### 85.5 Summary of DBMS\_HANG\_MANAGER Subprograms

The `DBMS_HANG_MANAGER` package includes the `SET` procedure subprogram.

Table 85-3 DBMS\_HANG\_MANAGER Package Subprograms

| Subprogram | Description |
| --- | --- |
| SET Procedure | Sets the specified parameter to the specified value |

#### 85.5.1 SET Procedure

This procedure sets the specified parameters to specified values.

Syntax

```
DBMS_HANG_MANAGER.SET (
   pname   IN  VARCHAR2,
   pvalue  IN  VARCHAR2);
```

Parameters

Table 85-4 SET Procedure Parameters

| Parameter | Description |
| --- | --- |
| `pname` | Contains the parameter name that needs to be modified |
| `pvalue` | Contains the new value for the parameter name specified in `pname` |