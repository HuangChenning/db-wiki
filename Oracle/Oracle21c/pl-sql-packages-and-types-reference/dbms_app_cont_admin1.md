---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/dbms_app_cont_admin1.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 20 DBMS\_APP\_CONT\_ADMIN

This package provides a collection dba level admin operations in relation to Application Continuity.

This chapter contains the following topics:

- DBMS\_APP\_CONT\_ADMIN Security Model
- Summary of DBMS\_APP\_CONT\_ADMIN Subprograms

### 20.1 DBMS\_APP\_CONT\_ADMIN Security Model

Applications must have the `EXECUTE` privilege on the `DBMS_APP_CONT_ADMIN` package.

### 20.2 Summary of DBMS\_APP\_CONT\_ADMIN Subprograms

This topic lists the `DBMS_APP_CONT_ADMIN` subprograms in alphabetical order and briefly describes them.

Table 20-1 DBMS\_APP\_CONT\_ADMIN Package Subprograms

| Subprogram | Description |
| --- | --- |
| ACCHK\_PURGE Procedure | This procedure purges all previously collected ACCHK information. |
| ACCHK\_SET Procedure | This procedure enables or disables data collection for acchk protection for your application when using Application Continuity or Transparent Application Continuity. The `DISABLE_TIME` parameter is used to extend the runtime. Default is `10` minutes. |
| ADD\_SQL\_CONNECTION\_TEST Procedure | This procedure adds a new connection test that is used during draining sessions before planned maintenance begins. |
| DELETE\_SQL\_CONNECTION\_TEST Procedure | This procedure deletes a connection test that is no longer needed for planned draining. Removing a test applies immediately to all RAC instances where the PDB is open. |
| DISABLE\_CONNECTION\_TEST Procedure | This procedure disables usage of a connection test during draining of sessions. |
| ENABLE\_CONNECTION\_TEST Procedure | This procedure enables usage of a connection test for draining database sessions before planned maintenance. Enabling a test applies immediately to all RAC instances where the PDB is open. |
|  |  |

#### 20.2.1 ACCHK\_PURGE Procedure

This procedure purges all previously collected ACCHK information.

- You should call `ACCHK_PURGE` before `ACCHK_SET`, which loads the filters.
- `ACCHK_PURGE` is set at the PDB level.

Syntax

```
DBMS_APP_CONT_ADMIN.ACCHK_PURGE (
   start_time IN DATE    DEFAULT NULL,
   end_time   IN DATE    DEFAULT NULL,
   purge_all  IN BOOLEAN DEFAULT FALSE);
```

Parameters

Table 20-2 ACCHK\_PURGE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `start_time` | The start time from which you want to purge the ACCHK information. |
| `end_time` | The end time till when you want to purge the ACCHK information. |
| `purge_all` | This parameter is used to delete all ACCHK information. - `TRUE` - enables deletion of all ACCHK information. - `FALSE` - disables deletion of all ACCHK information. When this parameter is set to `FALSE`, then only the specified ACCHK information is deleted. |

Examples

The following examples illustrate how to purge all ACCHK information:
```
SQL> execute dbms_app_cont_admin.acchk_purge(purge_all => TRUE);
```

#### 20.2.2 ACCHK\_SET Procedure

This procedure enables or disables data collection for `acchk` protection reports for your application when using Application Continuity or Transparent Application Continuity.

Enabling or disabling data collection applies to the level connected, that is, a CDB or a PDB.
- `acchk` is enabled/disabled at your CDB if connected to the container.
- `acchk` is enabled/disabled at your PDB only when connected to the PDB.

Data collection applies to new sessions only.

Once enabled, data is collected for the workload run under this service. You can then view this data in the `ACCHK_REPORT` s and can also be mined in the `ACCHK` views.

Syntax

```
DBMS_APP_CONT_ADMIN.ACCHK_SET (
   enabled                  IN BOOLEAN,
   disable_time_in_seconds  DEFAULT 600);
```

Parameters

Table 20-3 ACCHK\_SET Procedure Parameters

| Parameter | Description |
| --- | --- |
| `enabled` | This parameter is used to enable or disable data collection at a CDB or PDB level. - `TRUE` -enables data collection at this level. - `FALSE` -explicitly disables data collection. |
| `disable_time_in_seconds` | Optional parameter used to disable `ACCHK` tracing automatically in a given number of seconds.  The maximum value that you can specify is 3600 seconds.  The default value is 600 seconds. |

Usage Notes

- This procedure is owned by `SYS` at `CDB$ROOT` or PDB level, or by `SYS` when not multitenant
- The `acchk` activation is enabled across all instances of RAC supporting that service.
- Enabling is persistent to allow for failover and restart tests, that is, implementation uses `ALTER SESSION SET EVENTS ….. SCOPE=BOTH`. The enable is per database. For Data Guard, enable and disable must be at each database.

Examples

Application Continuity Protection Check is not enabled by default. Follow this procedure to enable or disable `ACCHK` and generate reports to check protection level for the applications.

1. Grant read access to the users, who will run the Application Continuity Protection Check report and views, using the `ACCHK_READ` role:
	```
	GRANT ACCHK_READ TO USER;
	```
2. Enable Application Continuity tracing for your applications using the `dbms_app_cont_admin.acchk_set(true)` procedure:
	```
	SQL> execute dbms_app_cont_admin.acchk_set(true);
	```
	By default, `ACCHK` is disabled automatically after 600 seconds. You can specify a lower number to reduce the auto disable time. For example, to disable `ACCHK` after 300 seconds:
	```
	SQL> dbms_app_cont_admin.acchk_set(true,300);
	```
	The `dbms_app_cont_admin.acchk_set(true)` procedure enables Application Continuity tracing at the database level to which you are connected. If you are connected at the CDB level, then tracing is enabled for the CDB, and if you are connected at the PDB level, then tracing is enabled for the PDB.
	Note:
	Set the `COMPATIBLE` parameter to 12.2.0 or greater. If the `COMPATIBLE` parameter was previously set to a lower value, then the `ACCHK_SET` procedure creates the ACCHK views and roles when you run the procedure for the first time after updating the `COMPATIBLE` parameter.
3. To disable Application Continuity tracing for new sessions in your applications:
	```
	SQL> execute dbms_app_cont_admin.acchk_set(false);
	```
	Note:
	The tracing will not be disabled for the current sessions until the sessions are terminated.

#### 20.2.3 ADD\_SQL\_CONNECTION\_TEST Procedure

This procedure adds a new connection test that is used during draining sessions before planned maintenance begins. Use this procedure when the SQL connection test is not covered by standard tests. The test is enabled when added. If the optional service name qualifier is provided, the test only applies only to that service name.

Syntax

```
DBMS_APP_CONT_ADMIN.ADD_SQL_CONNECTION_TEST (
   connection_test          IN VARCHAR2
   service_name             IN VARCHAR2   DEFAULT NULL);
```

Parameters

Table 20-4 ADD\_SQL\_CONNECTION\_TEST Procedure Parameters

| Parameter | Description |
| --- | --- |
| `CONNECTION_TEST` | The SQL text used to test and drain connections. |
| `SERVICE_NAME` | Optional service name qualifier. |

Usage Notes

The `ADD_SQL_CONNECTION_TEST Procedure` adds a connection test for the purpose of draining sessions before planned maintenance begins. The connection test is used by the application to test connections that are marked for draining. Sessions are set for draining at stop and relocate operations for services or PDBs. When set the RDBMS closes the connection while draining so the application sees no errors during planned maintenance. You can enter as many CONNECTION TESTs as needed. They are used only during planned maintenance. The tests apply to all RAC instances.

Check online documentation for latest updates on service qualifier availability.

Added connection can be viewed by querying the view `DBA_CONNECTION_TESTS`.

This procedure is owned by `SYS` and is granted to users for execution at `CDB$ROOT` or `PDB` levels, or when not multitenant, at dictionary level.

#### 20.2.4 DELETE\_SQL\_CONNECTION\_TEST Procedure

This procedure deletes a connection test that is no longer needed for planned draining. Removing a test applies immediately to all RAC instances where the PDB is open.

Syntax

```
DBMS_APP_CONT_ADMIN.DELETE_SQL_CONNECTION_TEST (
   connection_test          IN VARCHAR2
   service_name             IN VARCHAR2   DEFAULT NULL);
```

Parameters

Table 20-5 DELETE\_SQL\_CONNECTION\_TEST Procedure Parameters

| Parameter | Description |
| --- | --- |
| `CONNECTION_TEST` | The SQL text used to test and drain connections. |
| `SERVICE_NAME` | Optional service name qualifier.  If the optional `SERVICE_NAME` qualifier is provided, only the test for that service name is deleted. |

Usage Notes

If you are not certain if a test should be deleted, you can disable the test using `DISABLE_CONNECTION_TEST` Procedure. Only custom SQL tests can be deleted. Predefined tests cannot be deleted. Check for latest updates on service qualifier availability.

This procedure is owned by `SYS` at `CDB$ROOT` or `PDB` level, or `SYS` for when not multitenant.

Connection tests and their status can be checked by querying the view `DBA_CONNECTION_TESTS`.

#### 20.2.5 DISABLE\_CONNECTION\_TEST Procedure

This procedure disables usage of a connection test during draining of sessions. Disabling a test applies immediately to all RAC instances where the PDB is open.

Syntax

```
DBMS_APP_CONT_ADMIN.DISABLE_CONNECTION_TEST (
   connection_test_type     IN VARCHAR2,
   connection_test          IN VARCHAR2,
   service_name             IN VARCHAR2   DEFAULT NULL);
```

Parameters

Table 20-6 DISABLE\_CONNECTION\_TEST Procedure Parameters

| Parameter | Description |
| --- | --- |
| `CONNECTION_TEST_TYPE` | The permitted values are:  - `DBMS_APP_CONT_ADMIN.SQL_TEST` - `DBMS_APP_CONT_ADMIN.PING_TEST` - `DBMS_APP_CONT_ADMIN.ENDREQUEST_TEST` |
| `CONNECTION_TEST` | The SQL text used to test and drain connections.  This parameter is allowed only if the value of `CONNECTION_TEST_TYPE` is `SQL_TEST`. |
| `SERVICE_NAME` | Optional service name qualifier. If the optional service name qualifier is provided, only the test for that service name is enabled. A disable at service name level takes precedence over an enable at `PDB` level. That is the `PDB` can be enabled, and the service disabled. |

Usage Notes

This procedure is owned by `SYS` and is granted to users for execution at `CDB$ROOT` or `PDB` levels, or when not multitenant, at dictionary level.

Connection tests and their status can be checked by querying the view `DBA_CONNECTION_TESTS`.

#### 20.2.6 ENABLE\_CONNECTION\_TEST Procedure

This procedure enables usage of a connection test for draining database sessions before planned maintenance. Enabling a test applies immediately to all RAC instances where the PDB is open.

Syntax

```
DBMS_APP_CONT_ADMIN.ENABLE_CONNECTION_TEST (
   connection_test_type     IN VARCHAR2,
   connection_test          IN VARCHAR2,
   service_name             IN VARCHAR2   DEFAULT NULL);
```

Parameters

Table 20-7 ENABLE\_CONNECTION\_TEST Procedure Parameters

| Parameter | Description |
| --- | --- |
| `CONNECTION_TEST_TYPE` | The connection type used when managing connection tests for draining before planned maintenance. See ADD, DELETE, ENABLE, DISABLE procedures for connection tests.  The permitted values are:  - `DBMS_APP_CONT_ADMIN.SQL_TEST` - `DBMS_APP_CONT_ADMIN.PING_TEST` - `DBMS_APP_CONT_ADMIN.ENDREQUEST_TEST` - `DBMS_APP_CONT_ADMIN.BEGINREQUEST_TEST` |
| `CONNECTION_TEST` | The SQL text used to test and drain connections at the RDBMS before planned maintenance starts.  This parameter is allowed only if the value of `CONNECTION_TEST_TYPE` is `SQL_TEST`. |
| `SERVICE_NAME` | Optional service name qualifier. If the optional service name qualifier is provided, only the test for that service name is enabled. An enable at service name level overrides any higher-level disables. That is, the PDB can be disabled, and the service enabled. |

Usage Notes

- This procedure is owned by `SYS` and is granted to users for execution at `CDB$ROOT` or `PDB` levels, or when not multitenant, at dictionary level
- `ENABLE_CONNECTION_TEST` enables a connection test for draining sessions during planned maintenance. The enable operation applies to all RAC instances where the `PDB` is open. It persists across database restarts.
- This procedure is owned by `SYS` and is granted to users for execution at `CDB$ROOT` or `PDB` levels, or when not multitenant, at dictionary level.