---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/DBMS_GOLDENGATE_ADM.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 82 DBMS\_GOLDENGATE\_ADM

The `DBMS_GOLDENGATE_ADM` package provides subprograms to configure and manage Oracle GoldenGate conflict detection and resolution.

This chapter contains the following topics:

- Using DBMS\_GOLDENGATE\_ADM
- Summary of DBMS\_GOLDENGATE\_ADM Subprograms

### 82.1 Using DBMS\_GOLDENGATE\_ADM

This section contains topics which relate to using the `DBMS_GOLDENGATE_ADM` package.

- DBMS\_GOLDENGATE\_ADM Overview
- DBMS\_GOLDENGATE\_ADM Security Model

#### 82.1.1 DBMS\_GOLDENGATE\_ADM Overview

The `DBMS_GOLDENGATE_ADM` package provides interfaces to configure automatic conflict detection and resolution in an Oracle GoldenGate configuration that replicates tables between Oracle databases.

When more than one replica of a table allows changes to the table, a conflict can occur when a change is made to the same row in two different databases at nearly the same time. Oracle GoldenGate replicates changes using row logical change records (LCRs). It detects a conflict by comparing the old values in the row LCR with the current values of the corresponding table row identified by the key columns. If any column value does not match, then there is a conflict. After a conflict is detected, Oracle GoldenGate can resolve the conflict by overwriting values in the row with some values from the row LCR, ignoring the values in the row LCR, or computing a delta to update the row values.

XStream inbound servers and outbound servers can be used in an XStream configuration in a multitenant container database (CDB). A CDB is an Oracle database that includes zero, one, or many user-created pluggable databases (PDBs).

Note:

Using XStream requires purchasing a license for the Oracle GoldenGate product.

See Also:

- [Oracle Database XStream Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=XSTRM-GUID-F0C097D4-C197-4BC8-ACD0-B005325B78F8)
- [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=CNCPT89233) for more information about CDBs and PDBs

#### 82.1.2 DBMS\_GOLDENGATE\_ADM Security Model

Security on this package can be controlled either by granting `EXECUTE` on this package to selected users or roles or by granting `EXECUTE_CATALOG_ROLE` to selected users or roles.

If subprograms in the package are run from within a stored procedure, then the user who runs the subprograms must be granted `EXECUTE` privilege on the package directly. It cannot be granted through a role.

An Oracle GoldenGate administrator must be configured at each Oracle database in the table’s replication environment, and Oracle GoldenGate must be configured to replicate the table at each Oracle database. You can configure an Oracle GoldenGate administrator using the `GRANT_ADMIN_PRIVILEGE` procedure in the `DBMS_GOLDENGATE_ADM` package.

See Also:

The Oracle GoldenGate documentation for more information about Oracle GoldenGate replication and configuring an Oracle GoldenGate administrator

### 82.2 Summary of DBMS\_GOLDENGATE\_ADM Subprograms

Table 82-1 DBMS\_GOLDENGATE\_ADM Package Subprograms

| Subprogram | Description |
| --- | --- |
| ADD\_AUTO\_CDR Procedure | Configures Oracle GoldenGate automatic conflict detection and resolution for a table |
| ADD\_AUTO\_CDR\_COLUMN\_GROUP Procedure | Adds a column group and configures Oracle GoldenGate automatic conflict detection and resolution for the column group |
| ADD\_AUTO\_CDR\_DELTA\_RES Procedure | Configures Oracle GoldenGate automatic conflict detection and delta resolution for the column |
| ALTER\_AUTO\_CDR Procedure | Alters the Oracle GoldenGate automatic conflict detection and resolution for a table |
| ALTER\_AUTO\_CDR\_COLUMN\_GROUP Procedure | Alters a column group for Oracle GoldenGate automatic conflict detection and resolution |
| DELETE\_PROCREP\_EXCLUSION\_OBJ Procedure | Deletes a database object from the exclusion list for Oracle GoldenGate procedural replication |
| GG\_PROCEDURE\_REPLICATION\_ON Function | Returns 1 if Oracle GoldenGate procedural replication is enabled and returns 0 if it is disabled |
| INSERT\_PROCREP\_EXCLUSION\_OBJ Procedure | Inserts a database object into the exclusion list for Oracle GoldenGate procedural replication |
| PURGE\_TOMBSTONES Procedure | Purges rows that were deleted before the specified timestamp from the tombstone table |
| REMOVE\_AUTO\_CDR Procedure | Removes Oracle GoldenGate automatic conflict detection and resolution for a table |
| REMOVE\_AUTO\_CDR\_COLUMN\_GROUP Procedure | Removes a column group that was configured for Oracle GoldenGate automatic conflict detection and resolution |
| REMOVE\_AUTO\_CDR\_DELTA\_RES Procedure | Removes Oracle GoldenGate automatic conflict detection and delta resolution for the column |

Note:

All procedures commit unless specified otherwise.

#### 82.2.1 ADD\_AUTO\_CDR Procedure

This procedure configures Oracle GoldenGate automatic conflict detection and resolution for a table.

The conflict detection and resolution configured by this procedure is based on the timestamp of the changes. The procedure adds one or more hidden columns of `TIMESTAMP` type to the table, and each hidden column is counted against the limit of 1,000 columns for each table.

The procedure automatically places the columns in the table into a default column group and into an unconditional supplemental log group, excluding nonscalar columns. To create column groups that include a subset of the columns in the table, use the `ADD_AUTO_CDR_COLUMN_GROUP` procedure in this package.

This procedure is overloaded. One version of this procedure contains the `additional_options` parameter, and the other does not.

Syntax

```
DBMS_GOLDENGATE_ADM.ADD_AUTO_CDR(
   schema_name             IN VARCHAR2,
   table_name              IN VARCHAR2,
   resolution_granularity  IN VARCHAR2 DEFAULT 'ROW',
   existing_data_timestamp IN TIMESTAMP WITH TIME ZONE DEFAULT 'SYSTIMESTAMP',
   tombstone_deletes       IN BOOLEAN DEFAULT TRUE,
   fetchcols               IN BOOLEAN DEFAULT TRUE,
   record_conflicts        IN BOOLEAN DEFAULT TRUE,
   use_custom_handlers     IN BINARY_INTEGER DEFAULT 0);
```
```
DBMS_GOLDENGATE_ADM.ADD_AUTO_CDR(
   schema_name             IN VARCHAR2,
   table_name              IN VARCHAR2,
   resolution_granularity  IN VARCHAR2 DEFAULT 'ROW',
   existing_data_timestamp IN TIMESTAMP WITH TIME ZONE DEFAULT 'SYSTIMESTAMP',
   tombstone_deletes       IN BOOLEAN DEFAULT TRUE,
   fetchcols               IN BOOLEAN DEFAULT TRUE,
   record_conflicts        IN BOOLEAN DEFAULT TRUE,
   use_custom_handlers     IN BINARY_INTEGER DEFAULT 0,
   additional_options      IN BINARY_INTEGER);
```

Parameters

Table 82-2 ADD\_AUTO\_CDR Procedure Parameters

| Parameter | Description |
| --- | --- |
| `schema_name` | The name of the table’s schema. |
| `table_name` | The name of the table. |
| `resolution_granularity` | `ROW`, the default, adds one hidden `TIMESTAMP` column for the row and one hidden `TIMESTAMP` column for each LOB column.  `COLUMN` adds one hidden `TIMESTAMP` column for each column in the table. |
| `existing_data_timestamp` | Timestamp to assign to existing rows.  If `NULL`, then the current system timestamp is used. If a time is specified, and the operating system time zone is not a valid Oracle time zone, then Oracle uses UTC as the default value. |
| `tombstone_deletes` | `TRUE`, the default, tracks deleted rows in a tombstone table. Tracking deleted rows might be required to detect and resolve some conflicts, but tracking deleted rows requires additional database resources.  `FALSE` does not track deleted rows in a tombstone table. |
| `fetchcols` | `TRUE`, the default, fetches the value of LOBs during conflict detection and resolution. Fetching LOBs can be an expensive operation.  `FALSE` does not fetch the value of LOBs during conflict detection and resolution. |
| `record_conflicts` | `TRUE`, the default, records the conflict in the `DBA_APPLY_ERROR` and `DBA_APPLY_ERROR_MESSAGES` views.  `FALSE` does not record the conflict. |
| `use_custom_handlers` | `0,` the default, indicates that automatic conflict handlers are used.  `1` indicates that automatic conflict handlers are not used and that a custom error handler must be specified using the `SET_DML_HANDLER` procedure in the `DBMS_APPLY_ADM` package. |
| `additional_options` | `0` indicates `NONE.` You can also use the `DBMS_GOLDENGATE_ADM.DBMS_GOLDENGATE_ADM.ADDITIONAL_OPTIONS_NONE` constant.  `1` indicates `EARLIEST_TIMESTAMP_RESOLUTION.` In earliest timestamp resolution, the earliest timestamp is used for conflict resolution instead of the latest timestamp. You can also use the `DBMS_GOLDENGATE_ADM.ADDITIONAL_OPTIONS_EARLIEST_TIMESTAMP` constant.  `2` indicates `DELETE_ALWAYS_WINS.` In delete always wins, when there is a conflict between a delete operation and another operation, the delete operation succeeds and the other operation is discarded. You can also use the `DBMS_GOLDENGATE_ADM.ADDITIONAL_OPTIONS_DELETE_ALWAYS_WINS` constant.  `4` indicates `IGNORE_GLOBAL_SITE_PRIORITY.` In ignore global site priority, the locally defined resolution is used for the table even if global site priority is set in the Oracle GoldenGate replicat file. You can also use the `DBMS_GOLDENGATE_ADM.ADDITIONAL_OPTIONS_IGNORE_GLOBAL_SITE_PRIORITY` constant.  `8` indicates `ADD_KEY_VERSION.` Use this option to add a version number with `TIMESTAMP` data type to handle delete conflicts. You can also use the `DBMS_GOLDENGATE_ADM.ADDITIONAL_OPTIONS_ADD_KEY_VERSION` constant.  Add the options together to use more than one option. For example, to use earliest timestamp resolution and delete always wins, use `3.` |

Example

The following example illustrates how to use bitmask:

```
SQL> EXECUTE dbms_goldengate_adm.add_auto_cdr('scott','table1',
   additional_options =>
   dbms_goldengate_adm.additional_options_delete_always_wins +
      dbms_goldengate_adm.additional_options_add_key_version,
    record_conflicts => TRUE);
```

#### 82.2.2 ADD\_AUTO\_CDR\_COLUMN\_GROUP Procedure

This procedure adds a column group to a table that is configured for Oracle GoldenGate automatic conflict detection and resolution.

For a table that has been configured for timestamp conflict detection and resolution, this procedure adds a column group that includes a specified subset of columns in the table. Any columns in the table that are not part of a column group remain in the default column group for the table.

When you add a column group to a table, conflict detection and resolution is performed on the columns in the column group separately from the other columns in the table. Column groups enable different databases to update different columns in the same row at nearly the same time without causing a conflict.

For example, a replicated table that contains employee information might have a salary column and a bonus column as well as other columns that identify the employee and a location column for the employees office number. Assume that one department in the company updates its database to change the employee's salary while another department updates its database to change the employee's location. If the salary and bonus columns are in a column group, these changes are applied to the replicated table in each database without requiring conflict resolution.

The procedure automatically places the columns in the column group into an unconditional supplemental log group, excluding nonscalar columns.

Before this procedure can be run on a table, the `DBMS_GOLDENGATE_ADM.ADD_AUTO_CDR` procedure must be run in the table with `ROW` specified for the `resolution_granularity` parameter.

Syntax

```
DBMS_GOLDENGATE_ADM.ADD_AUTO_CDR_COLUMN_GROUP(
   schema_name             IN VARCHAR2,
   table_name              IN VARCHAR2,
   column_list             IN VARCHAR2,
   column_group_name       IN VARCHAR2 DEFAULT NULL,
   existing_data_timestamp IN TIMESTAMP WITH TIME ZONE DEFAULT NULL);
```

Parameters

Table 82-3 ADD\_AUTO\_CDR\_COLUMN\_GROUP Procedure Parameters

| Parameter | Description |
| --- | --- |
| `schema_name` | The name of the table’s schema. |
| `table_name` | The name of the table. |
| `column_list` | Group of columns for which the conflict detection and resolution is configured.  Specify the columns in a comma-separated list.  The same column cannot be in more than one column group. Also, the same column cannot be in a column group and specified in a delta resolution. |
| `column_group_name` | The name of the column group.  If `NULL`, the column group name is system generated. |
| `existing_data_timestamp` | The time value for the added `TIMESTAMP` columns for existing table data. |

#### 82.2.3 ADD\_AUTO\_CDR\_DELTA\_RES Procedure

This procedure configures Oracle GoldenGate automatic conflict detection and delta resolution for the column.

The resolution method does not depend on a timestamp or an extra resolution column. With delta conflict resolution, the conflict is resolved by adding the difference between the new and old values in the LCR to the value in the table. For example, if a bank balance is updated at two sites concurrently, then the converged value accounts for all debits and credits. This resolution method is generally used for financial data such as an account balance.

The procedure automatically places the column into an unconditional supplemental log group.

Before this procedure can be run on a table, the `DBMS_GOLDENGATE_ADM.ADD_AUTO_CDR` procedure must be run in the table with `ROW` specified for the `resolution_granularity` parameter.

Syntax

```
DBMS_GOLDENGATE_ADM.ADD_AUTO_CDR_DELTA_RES(
   schema_name IN VARCHAR2,
   table_name  IN VARCHAR2,
   column_name IN VARCHAR2);
```

Parameters

Table 82-4 ADD\_AUTO\_CDR\_DELTA\_RES Procedure Parameters

| Parameter | Description |
| --- | --- |
| `schema_name` | The name of the table’s schema. |
| `table_name` | The name of the table. |
| `column_name` | The name of the column.  The specified column must be a `NUMBER` or `FLOAT` data type column.  The same column cannot be in a column group. |

#### 82.2.4 ALTER\_AUTO\_CDR Procedure

This procedure alters the Oracle GoldenGate automatic conflict detection and resolution for a table.

This procedure is overloaded. One version of this procedure contains the `additional_options` parameter, and the other does not.

Syntax

```
DBMS_GOLDENGATE_ADM.ALTER_AUTO_CDR(
   schema_name             IN VARCHAR2,
   table_name              IN VARCHAR2,
   tombstone_deletes       IN BOOLEAN DEFAULT TRUE,
   fetchcols               IN BOOLEAN DEFAULT TRUE,
   record_conflicts        IN BOOLEAN DEFAULT TRUE,
   use_custom_handlers     IN BINARY_INTEGER DEFAULT 0);
```
```
DBMS_GOLDENGATE_ADM.ALTER_AUTO_CDR(
   schema_name             IN VARCHAR2,
   table_name              IN VARCHAR2,
   tombstone_deletes       IN BOOLEAN DEFAULT TRUE,
   fetchcols               IN BOOLEAN DEFAULT TRUE,
   record_conflicts        IN BOOLEAN DEFAULT TRUE,
   use_custom_handlers     IN BINARY_INTEGER DEFAULT 0,
   additional_options      IN BINARY_INTEGER);
```

Parameters

Table 82-5 ALTER\_AUTO\_CDR Procedure Parameters

| Parameter | Description |
| --- | --- |
| `schema_name` | The name of the table’s schema. |
| `table_name` | The name of the table. |
| `tombstone_deletes` | `TRUE` tracks deleted rows in a tombstone table. Tracking deleted rows might be required to detect and resolve some conflicts, but tracking deleted rows requires additional database resources.  `FALSE` does not track deleted rows in a tombstone table.  `NULL` retains the current setting for the parameter. |
| `fetchcols` | `TRUE` fetches the value of nonscalar columns during conflict detection and resolution.  `FALSE` does not fetch the value of nonscalar columns during conflict detection and resolution.  `NULL` retains the current setting for the parameter. |
| `record_conflicts` | `TRUE` records the conflict.  `FALSE` does not record the conflict.  `NULL` retains the current setting for the parameter. |
| `use_custom_handlers` | `0,` default, indicates that automatic conflict handlers are used.  `1` indicates that automatic conflict handlers are not used and that a custom error handler must be specified using the `SET_DML_HANDLER` procedure in the `DBMS_APPLY_ADM` package.  `NULL`, the default, retains the current setting for the parameter. |
| `additional_options ` | A bit mask that indicates which of six types of actions to follow:  - `0` - no changes are made from any previous settings. You can also use the `DBMS_GOLDENGATE_ADM.ADDITIONAL_OPTIONS_NONE` constant. - `1` - sets earliest timestamp, but clears all other options/bits. You can also use the `DBMS_GOLDENGATE_ADM.EARLIEST_TIMESTAMP_RESOLUTION` constant. - `2` - sets delete always wins, but clears all other options/bits. You can also use the `DBMS_GOLDENGATE_ADM.ADDITIONAL_OPTIONS_DELETE_ALWAYS_WINS` constant. - `4` - indicates `IGNORE_GLOBAL_SITE_PRIORITY`. When you specify this option, then use local site resolution configuration for the table, even if the global site priority is set in the Oracle GoldenGate replicat file. You can also use the `DBMS_GOLDENGATE_ADM.ADDITIONAL_OPTIONS_IGNORE_GLOBAL_SITE_PRIORITY` constant. - `8` - indicates `ADD_KEY_VERSION`. Use this option to add a version number with `TIMESTAMP` data type to handle delete conflicts. You can also use the `DBMS_GOLDENGATE_ADM.ADDITIONAL_OPTIONS_ADD_KEY_VERSION` constant. - `16` - clears all. You can also use the `DBMS_GOLDENGATE_ADM.ADDITIONAL_OPTIONS_CLEAR_OPTIONS` constant.  Note:  - Any combination of `1`,`2`, `4`, and `8` are possible. - Any combination that include `1` or `2` will implicitly set `8`.  You can add the options together to use more than one option.  For example:  If the previously used option was `DELETE_ALWAYS_WINS`, then when you specify a value of `1` for `additional_options`, `EARLIEST_TIMESTAMP_RESOLUTION` and `16` means clear all options. As a result, there are no additional options set. |

#### 82.2.5 ALTER\_AUTO\_CDR\_COLUMN\_GROUP Procedure

This procedure alters a column group for Oracle GoldenGate automatic conflict detection and resolution.

Syntax

```
DBMS_GOLDENGATE_ADM.ALTER_AUTO_CDR_COLUMN_GROUP(
   schema_name        IN VARCHAR2,
   table_name         IN VARCHAR2,
   column_group_name  IN VARCHAR2,
   add_column_list    IN VARCHAR2,
   remove_column_list IN VARCHAR2);
```

Parameters

Table 82-6 ALTER\_AUTO\_CDR\_COLUMN\_GROUP Procedure Parameters

| Parameter | Description |
| --- | --- |
| `schema_name` | The name of the table’s schema. |
| `table_name` | The name of the table. |
| `column_group_name` | The name of the column group. |
| `add_column_list` | A comma-separated list of columns to add to the column group. |
| `remove_column_list` | A comma-separated list of columns to remove from the column group. |

#### 82.2.6 DELETE\_PROCREP\_EXCLUSION\_OBJ Procedure

This procedure deletes a database object from the exclusion list for Oracle GoldenGate procedural replication.

When a database object is on the exclusion list for Oracle GoldenGate procedural replication, execution of subprogram in the package is not replicated if the subprogram operates on the excluded object. For example, if `hr.employees` is an excluded database object for the `DBMS_REDEFINITION` package, then an execution of the `DBMS_REDEFINITION.START_REDEF_TABLE` procedure on the `hr.employees` table is not replicated.

Caution:

Run the `DELETE_PROCREP_EXCLUSION_OBJ` procedure only under the direction of Oracle Support.

Syntax

```
DBMS_GOLDENGATE_ADM.DELETE_PROCREP_EXCLUSION_OBJ(
   package_owner     IN VARCHAR2 DEFAULT NULL,
   package_name      IN VARCHAR2 DEFAULT NULL,
   object_owner      IN VARCHAR2 DEFAULT NULL,
   object_name       IN VARCHAR2 DEFAULT NULL);
```

Parameters

Table 82-7 DELETE\_PROCREP\_EXCLUSION\_OBJ Procedure Parameters

| Parameter | Description |
| --- | --- |
| `package_owner` | The owner of the package. |
| `package_name` | The name of the package. |
| `object_owner` | The owner of the object. |
| `object_name` | The name of the object. |

#### 82.2.7 GG\_PROCEDURE\_REPLICATION\_ON Function

This function returns 1 if Oracle GoldenGate procedural replication is enabled and returns 0 if it is disabled.

Syntax

```
DBMS_GOLDENGATE_ADM.GG_PROCEDURE_REPLICATION_ON
RETURN NUMBER;
```

#### 82.2.8 INSERT\_PROCREP\_EXCLUSION\_OBJ Procedure

This procedure inserts a database object into the exclusion list for Oracle GoldenGate procedural replication.

When a database object is on the exclusion list for Oracle GoldenGate procedural replication, execution of subprogram in the package is not replicated if the subprogram operates on the excluded object. For example, if `hr.employees` is an excluded database object for the `DBMS_REDEFINITION` package, then an execution of the `DBMS_REDEFINITION.START_REDEF_TABLE` procedure on the `hr.employees` table is not replicated.

Caution:

Run the `INSERT_PROCREP_EXCLUSION_OBJ` procedure only under the direction of Oracle Support.

Syntax

```
DBMS_GOLDENGATE_ADM.INSERT_PROCREP_EXCLUSION_OBJ(
   package_owner     IN VARCHAR2 DEFAULT NULL,
   package_name      IN VARCHAR2 DEFAULT NULL,
   object_owner      IN VARCHAR2 DEFAULT NULL,
   object_name       IN VARCHAR2 DEFAULT NULL);
```

Parameters

Table 82-8 INSERT\_PROCREP\_EXCLUSION\_OBJ Procedure Parameters

| Parameter | Description |
| --- | --- |
| `package_owner` | The owner of the package. |
| `package_name` | The name of the package. |
| `object_owner` | The owner of the object. |
| `object_name` | The name of the object. |

#### 82.2.9 PURGE\_TOMBSTONES Procedure

This procedure purges rows that were deleted before the specified timestamp from the tombstone table.

Syntax

```
DBMS_GOLDENGATE_ADM.PURGE_TOMBSTONES(
   purge_timestamp IN TIMESTAMP WITH TIME ZONE);
```

Parameters

Table 82-9 PURGE\_TOMBSTONES Procedure Parameters

| Parameter | Description |
| --- | --- |
| `purge_timestamp` | The timestamp before which records are purged. |

#### 82.2.10 REMOVE\_AUTO\_CDR Procedure

This procedure removes Oracle GoldenGate automatic conflict detection and resolution for a table.

Syntax

```
DBMS_GOLDENGATE_ADM.REMOVE_AUTO_CDR(
   schema_name             IN VARCHAR2,
   table_name              IN VARCHAR2);
```

Parameters

Table 82-10 REMOVE\_AUTO\_CDR Procedure Parameters

| Parameter | Description |
| --- | --- |
| `schema_name` | The name of the table’s schema. |
| `table_name` | The name of the table. |

#### 82.2.11 REMOVE\_AUTO\_CDR\_COLUMN\_GROUP Procedure

This procedure removes a column group that was configured for Oracle GoldenGate automatic conflict detection and resolution.

Syntax

```
DBMS_GOLDENGATE_ADM.REMOVE_AUTO_CDR_COLUMN_GROUP(
   schema_name             IN VARCHAR2,
   table_name              IN VARCHAR2,
   column_group_name       IN VARCHAR2);
```

Parameters

Table 82-11 REMOVE\_AUTO\_CDR\_COLUMN\_GROUP Procedure Parameters

| Parameter | Description |
| --- | --- |
| `schema_name` | The name of the table’s schema. |
| `table_name` | The name of the table. |
| `column_group_name` | The name of the column group. |

#### 82.2.12 REMOVE\_AUTO\_CDR\_DELTA\_RES Procedure

This procedure removes Oracle GoldenGate automatic conflict detection and delta resolution for the column.

Syntax

```
DBMS_GOLDENGATE_ADM.REMOVE_AUTO_CDR_DELTA_RES(
   schema_name IN VARCHAR2,
   table_name  IN VARCHAR2,
   column_name IN VARCHAR2);
```

Parameters

Table 82-12 REMOVE\_AUTO\_CDR\_DELTA\_RES Procedure Parameters

| Parameter | Description |
| --- | --- |
| `schema_name` | The name of the table’s schema. |
| `table_name` | The name of the table. |
| `column_name` | The name of the column. |