---
title: DBMS_APP_CONT_ADMIN
book: PL/SQL Packages and Types Reference
doc_id: E96430-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/dbms_app_cont_admin1.html
tags:
  - oracle
  - 19c
  - pl-sql-packages-and-types-reference
---

This package provides a collection dba level admin operations in relation to Application Continuity.

### DBMS\_APP\_CONT\_ADMIN Security Model

Applications must have the `EXECUTE` privilege on the `DBMS_APP_CONT_ADMIN` package.

### Summary of DBMS\_APP\_CONT\_ADMIN Subprograms

This topic lists the `DBMS_APP_CONT_ADMIN` subprograms in alphabetical order and briefly describes them.

Table 1 DBMS\_APP\_CONT\_ADMIN Package Subprograms

| Subprogram | Description |
| --- | --- |
| ACCHK\_PURGE Procedure | This procedure purges all previously collected ACCHK information. |
| ACCHK\_SET Procedure | This procedure enables or disables data collection for acchk protection for your application when using Application Continuity or Transparent Application Continuity. The \`DISABLE\_TIME\` parameter is used to extend the runtime. Default is \`10\` minutes. |
| ADD\_SQL\_CONNECTION\_TEST Procedure | This procedure adds a new connection test that is used during draining sessions before planned maintenance begins. |
| CHECK\_REPLAY\_RULES Procedure | This procedure shows replay rules for the specified or the current service and returns the replayable targets as a bitmap in targets argument. |
| DELETE\_SQL\_CONNECTION\_TEST Procedure | This procedure deletes a connection test that is no longer needed for planned draining. Removing a test applies immediately to all RAC instances where the PDB is open. |
| DISABLE\_CONNECTION\_TEST Procedure | This procedure disables usage of a connection test during draining of sessions. |
| ENABLE\_CONNECTION\_TEST Procedure | This procedure enables usage of a connection test for draining database sessions before planned maintenance. Enabling a test applies immediately to all RAC instances where the PDB is open. |
| RESET\_REPLAY\_RULES Procedure | This procedure resets replay rules for the specified or the current service. |
| SET\_REPLAY\_RULES Procedure | This procedure sets replay rules for the specified or the current service. |

### ACCHK\_PURGE Procedure

This procedure purges all previously collected ACCHK information.

- You should call `ACCHK_PURGE` before `ACCHK_SET`, which loads the filters.
- `ACCHK_PURGE` is set at the PDB level.

**Syntax**

```md
DBMS_APP_CONT_ADMIN.ACCHK_PURGE (
   start_time IN DATE    DEFAULT NULL,
   end_time   IN DATE    DEFAULT NULL,
   purge_all  IN BOOLEAN DEFAULT FALSE);
```

**Parameters**

Table 2 ACCHK\_PURGE Procedure

| Parameter | Description |
| --- | --- |
| `start_time` | The start time from which you want to purge the ACCHK information. |
| `end_time` | The end time till when you want to purge the ACCHK information. |
| `purge_all` | This parameter is used to delete all ACCHK information. \`TRUE\` enables deletion of all ACCHK information; \`FALSE\` disables deletion of all ACCHK information. When this parameter is set to \`FALSE\`, then only the specified ACCHK information is deleted. |

**Examples**

The following examples illustrate how to purge all ACCHK information:

```md
SQL> execute dbms_app_cont_admin.acchk_purge(purge_all => TRUE);
```

### ACCHK\_SET Procedure

This procedure enables or disables data collection for `acchk` protection reports for your application when using Application Continuity or Transparent Application Continuity. The `DISABLE_TIME` parameter is used to extend the runtime. Default value is `10` minutes.

Enabling or disabling data collection applies to the level connected, that is, a CDB or a PDB.

- `acchk` is enabled/disabled at your CDB if connected to the container.
- `acchk` is enabled/disabled at your PDB only when connected to the PDB.

Data collection applies to new sessions only.

Once enabled, data is collected for the workload run under this service. You can then view this data in the `ACCHK_REPORT` s and can also be mined in the `ACCHK` views.

**Syntax**

```md
DBMS_APP_CONT_ADMIN.ACCHK_SET (
   enabled                  IN BOOLEAN,
   disable_time_in_seconds  DEFAULT 600);
```

**Parameters**

Table 3 ACCHK\_SET Procedure Parameters

| Parameter | Description |
| --- | --- |
| `enabled` | This parameter is used to enable or disable data collection at a CDB or PDB level. \`TRUE\` enables data collection at this level; \`FALSE\` explicitly disables data collection. |
| `disable_time_in_seconds` | Optional parameter used to disable `ACCHK` tracing automatically in a given number of seconds. The maximum value that you can specify is 3600 seconds. The default value is 600 seconds. |

**Usage Notes**

- This procedure is owned by `SYS` at `CDB$ROOT` or PDB level, or by `SYS` when not multitenant
- The `acchk` activation is enabled across all instances of RAC supporting that service.
- Enabling is persistent to allow for failover and restart tests, that is, implementation uses `ALTER SESSION SET EVENTS ..... SCOPE=BOTH`. The enable is per database. For Data Guard, enable and disable must be at each database.

**Examples**

Application Continuity Protection Check is not enabled by default. Follow this procedure to enable or disable `ACCHK` and generate reports to check protection level for the applications.

1. Grant read access to the users, who will run the Application Continuity Protection Check report and views, using the `ACCHK_READ` role:
	```md
	GRANT ACCHK_READ TO USER;
	```
2. Enable Application Continuity tracing for your applications using the `dbms_app_cont_admin.acchk_set(true)` procedure:
	```md
	SQL> execute dbms_app_cont_admin.acchk_set(true);
	```
	By default, `ACCHK` is disabled automatically after 600 seconds. You can specify a lower number to reduce the auto disable time. For example, to disable `ACCHK` after 300 seconds:
	```md
	SQL> dbms_app_cont_admin.acchk_set(true,300);
	```
	The `dbms_app_cont_admin.acchk_set(true)` procedure enables Application Continuity tracing at the database level to which you are connected. If you are connected at the CDB level, then tracing is enabled for the CDB, and if you are connected at the PDB level, then tracing is enabled for the PDB.
	**Note:** Set the `COMPATIBLE` parameter to 12.2.0 or greater.
3. To disable Application Continuity tracing for new sessions in your applications:
	```md
	SQL> execute dbms_app_cont_admin.acchk_set(false);
	```
	**Note:** The tracing will not be disabled for the current sessions until the sessions are terminated.

### ADD\_SQL\_CONNECTION\_TEST Procedure

This procedure adds a new connection test that is used during draining sessions before planned maintenance begins. Use this procedure when the SQL connection test is not covered by standard tests. The test is enabled when added. If the optional service name qualifier is provided, the test only applies only to that service name.

**Syntax**

```md
DBMS_APP_CONT_ADMIN.ADD_SQL_CONNECTION_TEST (
   connection_test          IN VARCHAR2
   service_name             IN VARCHAR2   DEFAULT NULL);
```

**Parameters**

Table 4 ADD\_SQL\_CONNECTION\_TEST Procedure Parameters

| Parameter | Description |
| --- | --- |
| `CONNECTION_TEST` | The SQL text used to test and drain connections. |
| `SERVICE_NAME` | Optional service name qualifier. |

**Usage Notes**

The `ADD_SQL_CONNECTION_TEST Procedure` adds a connection test for the purpose of draining sessions before planned maintenance begins. The connection test is used by the application to test connections that are marked for draining. Sessions are set for draining at stop and relocate operations for services or PDBs. When set the RDBMS closes the connection while draining so the application sees no errors during planned maintenance. You can enter as many CONNECTION TESTs as needed. They are used only during planned maintenance. The tests apply to all RAC instances.

Check online documentation for latest updates on service qualifier availability.

Added connection can be viewed by querying the view `DBA_CONNECTION_TESTS`.

This procedure is owned by `SYS` and is granted to users for execution at `CDB$ROOT` or `PDB` levels, or when not multitenant, at dictionary level.

### CHECK\_REPLAY\_RULES Procedure

This procedure shows replay rules for the specified or the current service and returns the replayable targets as a bitmap in targets argument.

**Syntax**

```md
DBMS_APP_CONT_ADMIN.CHECK_REPLAY_RULES (
 service_name  IN  VARCHAR2        DEFAULT NULL
 targets       OUT BINARY_INTEGER);
```

**Parameters**

Table 5 CHECK\_REPLAY\_RULES Procedure

| Parameter | Description |
| --- | --- |
| `service_name` | Optional service name qualifier. If the optional `SERVICE_NAME` qualifier is not provided, then replay rules are displayed for the current service. |
| `targets` | The replayable targets in a bitmap. You can use \`BITAND\` function to test if any one of these targets is replayable. \`dbms\_app\_cont\_admin.side\_effects\`, \`dbms\_app\_cont\_admin.autonomous\_transactions\`, and \`dbms\_app\_cont\_admin.database\_links\`. |

### DELETE\_SQL\_CONNECTION\_TEST Procedure

This procedure deletes a connection test that is no longer needed for planned draining. Removing a test applies immediately to all RAC instances where the PDB is open.

**Syntax**

```md
DBMS_APP_CONT_ADMIN.DELETE_SQL_CONNECTION_TEST (
   connection_test          IN VARCHAR2
   service_name             IN VARCHAR2   DEFAULT NULL);
```

**Parameters**

Table 6 DELETE\_SQL\_CONNECTION\_TEST Procedure Parameters

| Parameter | Description |
| --- | --- |
| `CONNECTION_TEST` | The SQL text used to test and drain connections. |
| `SERVICE_NAME` | Optional service name qualifier. If the optional `SERVICE_NAME` qualifier is provided, only the test for that service name is deleted. |

**Usage Notes**

If you are not certain if a test should be deleted, you can disable the test using `DISABLE_CONNECTION_TEST` Procedure. Only custom SQL tests can be deleted. Predefined tests cannot be deleted. Check for latest updates on service qualifier availability.

This procedure is owned by `SYS` at `CDB$ROOT` or `PDB` level, or `SYS` for when not multitenant.

Connection tests and their status can be checked by querying the view `DBA_CONNECTION_TESTS`.

### DISABLE\_CONNECTION\_TEST Procedure

This procedure disables usage of a connection test during draining of sessions. Disabling a test applies immediately to all RAC instances where the PDB is open.

**Syntax**

```md
DBMS_APP_CONT_ADMIN.DISABLE_CONNECTION_TEST (
   connection_test_type     IN VARCHAR2,
   connection_test          IN VARCHAR2,
   service_name             IN VARCHAR2   DEFAULT NULL);
```

**Parameters**

Table 7 DISABLE\_CONNECTION\_TEST Procedure Parameters

| Parameter | Description |
| --- | --- |
| `CONNECTION_TEST_TYPE` | The permitted values are `DBMS_APP_CONT_ADMIN.SQL_TEST`, `DBMS_APP_CONT_ADMIN.PING_TEST`, and `DBMS_APP_CONT_ADMIN.ENDREQUEST_TEST`. |
| `CONNECTION_TEST` | The SQL text used to test and drain connections. This parameter is allowed only if the value of `CONNECTION_TEST_TYPE` is `SQL_TEST`. |
| `SERVICE_NAME` | Optional service name qualifier. If the optional service name qualifier is provided, only the test for that service name is enabled. A disable at service name level takes precedence over an enable at `PDB` level. That is the `PDB` can be enabled, and the service disabled. |

**Usage Notes**

This procedure is owned by `SYS` and is granted to users for execution at `CDB$ROOT` or `PDB` levels, or when not multitenant, at dictionary level.

Connection tests and their status can be checked by querying the view `DBA_CONNECTION_TESTS`.

### ENABLE\_CONNECTION\_TEST Procedure

This procedure enables usage of a connection test for draining database sessions before planned maintenance. Enabling a test applies immediately to all RAC instances where the PDB is open.

**Syntax**

```md
DBMS_APP_CONT_ADMIN.ENABLE_CONNECTION_TEST (
   connection_test_type     IN VARCHAR2,
   connection_test          IN VARCHAR2,
   service_name             IN VARCHAR2   DEFAULT NULL);
```

**Parameters**

Table 8 ENABLE\_CONNECTION\_TEST Procedure Parameters

| Parameter | Description |
| --- | --- |
| `CONNECTION_TEST_TYPE` | The connection type used when managing connection tests for draining before planned maintenance. See ADD, DELETE, ENABLE, DISABLE procedures for connection tests. The permitted values are `DBMS_APP_CONT_ADMIN.SQL_TEST`, `DBMS_APP_CONT_ADMIN.PING_TEST`, and `DBMS_APP_CONT_ADMIN.ENDREQUEST_TEST`. |
| `CONNECTION_TEST` | The SQL text used to test and drain connections at the RDBMS before planned maintenance starts. This parameter is allowed only if the value of `CONNECTION_TEST_TYPE` is `SQL_TEST`. |
| `SERVICE_NAME` | Optional service name qualifier. If the optional service name qualifier is provided, only the test for that service name is enabled. An enable at service name level overrides any higher-level disables. That is, the PDB can be disabled, and the service enabled. |

**Usage Notes**

- This procedure is owned by `SYS` and is granted to users for execution at `CDB$ROOT` or `PDB` levels, or when not multitenant, at dictionary level
- `ENABLE_CONNECTION_TEST` enables a connection test for draining sessions during planned maintenance. The enable operation applies to all RAC instances where the `PDB` is open. It persists across database restarts.
- This procedure is owned by `SYS` and is granted to users for execution at `CDB$ROOT` or `PDB` levels, or when not multitenant, at dictionary level.

### RESET\_REPLAY\_RULES Procedure

This procedure resets replay rules for the specified or the current service.

**Note:**

- When resetting an AC service (`FAILOVER_TYPE = TRANSACTION`), if targets is not specified, then all targets become replayable, meaning allowing all side effects to be replayed (default).
- When resetting a TAC service (`FAILOVER_TYPE = AUTO`), if targets is not specified, all targets become un-replayable, meaning not allowing any side effect to be replayed (default).

**Syntax**

```md
DBMS_APP_CONT_ADMIN.RESET_REPLAY_RULES (
 service_name  IN  VARCHAR2        DEFAULT NULL
 targets       IN  BINARY_INTEGER  DEFAULT NULL);
```

**Parameters**

Table 9 RESET\_REPLAY\_RULES Procedure

| Parameter | Description |
| --- | --- |
| `service_name` | Optional service name qualifier. If the optional `SERVICE_NAME` qualifier is not provided, then replay rules are reset for the current service. |
| `targets` | Targets for the replay rule. The permitted values are \`dbms\_app\_cont\_admin.side\_effects\`, \`dbms\_app\_cont\_admin.autonomous\_transactions\`, and \`dbms\_app\_cont\_admin.database\_links\`. If multiple targets are required, then pass them as \`bit or\` of individual targets, such as: \`dbms\_app\_cont.side\_effects + dbms\_app\_cont.autonomous\_transactions\`. |

### SET\_REPLAY\_RULES Procedure

This procedure sets replay rules for the specified or the current service.

The replay rules are used by Application Continuity to determine whether side effects can be replayed or not.

**Syntax**

```md
DBMS_APP_CONT_ADMIN.SET_REPLAY_RULES (
 service_name  IN  VARCHAR2        DEFAULT NULL
 replayable    IN  BOOLEAN,
 targets       IN  BINARY_INTEGER);
```

**Parameters**

Table 10 SET\_REPLAY\_RULES Procedure

| Parameter | Description |
| --- | --- |
| `service_name` | Optional service name qualifier. If the optional `SERVICE_NAME` qualifier is not provided, then replay rules are set for the current service. |
| `replayable` | `TRUE` or `FALSE`, depending on whether the rule is replayable or not. |
| `targets` | Target effects on which this rule is applied. The permitted values are \`dbms\_app\_cont\_admin.side\_effects\`, \`dbms\_app\_cont\_admin.autonomous\_transactions\`, and \`dbms\_app\_cont\_admin.database\_links\`. If multiple targets are required, then pass them as \`bit or\` of individual targets, such as: \`dbms\_app\_cont.side\_effects + dbms\_app\_cont.autonomous\_transactions\`. |