---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/DBMS_REFRESH.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 145 DBMS\_REFRESH

The `DBMS_REFRESH` package enables you to create groups of materialized views that can be refreshed together to a transactionally consistent point in time. These groups are called refresh groups.

This chapter contains the following topics:

- DBMS\_REFRESH Overview
- DBMS\_REFRESH Security Model

### 145.1 DBMS\_REFRESH Overview

When it is important for materialized views to be transactionally consistent with each other, you can organize them into refresh groups.

By refreshing the refresh group, you can ensure that the data in all of the materialized views in the refresh group correspond to the same transactionally consistent point in time. A materialized view in a refresh group still can be refreshed individually, but doing so nullifies the benefits of the refresh group because refreshing the materialized view individually does not refresh the other materialized views in the refresh group

### 145.2 DBMS\_REFRESH Security Model

Users must have the `EXECUTE` privilege to run the procedures of `DBMS_REFRESH` package.

### 145.3 Summary of DBMS\_REFRESH Subprograms

This table lists the `DBMS_REFRESH` subprograms and briefly describes them.

Table 145-1 DBMS\_REFRESH Package Subprograms

| Subprogram | Description |
| --- | --- |
| ADD Procedure | Adds materialized views to a refresh group |
| CHANGE Procedure | Changes the refresh interval for a refresh group |
| DESTROY Procedure | Removes all of the materialized views from a refresh group and deletes the refresh group |
| MAKE Procedure | Specifies the members of a refresh group and the time interval used to determine when to refresh the members of this group |
| REFRESH Procedure | Manually refreshes a refresh group |
| SUBTRACT Procedure | Removes materialized views from a refresh group |

#### 145.3.1 ADD Procedure

This procedure adds materialized views to a refresh group.

Syntax

```
DBMS_REFRESH.ADD (
   name     IN VARCHAR2,
   { list   IN VARCHAR2, 
   | tab    IN DBMS_UTILITY.UNCL_ARRAY, }
   lax      IN BOOLEAN := FALSE);
```

Note:

This procedure is overloaded. The `list` and `tab` parameters are mutually exclusive.

Parameters

Table 145-2 ADD Procedure Parameters

| Parameter | Description |
| --- | --- |
| `name` | Name of the refresh group to which you want to add members, specified as `[schema_name.]refresh_group_name`. If the schema is not specified, then the current user is the default. |
| `list` | Comma-delimited list of materialized views that you want to add to the refresh group. Synonyms are not supported.  Each materialized view is specified as `[schema_name.]materialized_view_name`. If the schema is not specified, then the refresh group owner is the default. |
| `tab` | Instead of a comma-delimited list, you can supply a PL/SQL associative array of type `DBMS_UTILITY.UNCL_ARRAY`, where each element is the name of a materialized view. The first materialized view should be in position 1. The last position must be `NULL`.  Each materialized view is specified as `[schema_name.]materialized_view_name`. If the schema is not specified, then the refresh group owner is the default. |
| `lax` | A materialized view can belong to only one refresh group at a time. If you are moving a materialized view from one group to another, then you must set the `lax` flag to `TRUE` to succeed. Oracle then automatically removes the materialized view from the other refresh group and updates its refresh interval to be that of its new group. Otherwise, the call to `ADD` generates an error message. |

#### 145.3.2 CHANGE Procedure

This procedure changes the refresh interval for a refresh group.

Syntax

```
DBMS_REFRESH.CHANGE (
   name                  IN VARCHAR2,
   next_date             IN DATE           := NULL,
   interval              IN VARCHAR2       := NULL,
   implicit_destroy      IN BOOLEAN        := NULL,
   rollback_seg          IN VARCHAR2       := NULL,
   push_deferred_rpc     IN BOOLEAN        := NULL,
   refresh_after_errors  IN BOOLEAN        := NULL,
   purge_option          IN BINARY_INTEGER := NULL,
   parallelism           IN BINARY_INTEGER := NULL,
   heap_size             IN BINARY_INTEGER := NULL);
```

Parameters

Table 145-3 CHANGE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `name` | Name of the refresh group for which you want to alter the refresh interval. |
| `next_date` | Next date that you want a refresh to occur. By default, this date remains unchanged. |
| `interval` | Function used to calculate the next time to refresh the materialized views in the refresh group. This interval is evaluated immediately before the refresh. Thus, select an interval that is greater than the time it takes to perform a refresh. By default, the interval remains unchanged. |
| `implicit_destroy` | Allows you to reset the value of the `implicit_destroy` flag. If this flag is set, then Oracle automatically deletes the group if it no longer contains any members. By default, this flag remains unchanged. |
| `rollback_seg` | Allows you to change the rollback segment used. By default, the rollback segment remains unchanged. To reset this parameter to use the default rollback segment, specify `NULL`, including the quotes. Specifying `NULL` without quotes indicates that you do not want to change the rollback segment currently being used. |
| `push_deferred_rpc` | Starting with Oracle Database 12c Release 2 (12.2), this parameter is ignored. |
| `refresh_after_errors` | Starting with Oracle Database 12c Release 2 (12.2), this parameter is ignored. |
| `purge_option` | Starting with Oracle Database 12c Release 2 (12.2), this parameter is ignored. |
| `parallelism` | - 0 specifies serial propagation. - n > 1 specifies parallel propagation with n parallel processes. - 1 specifies parallel propagation using only one parallel process. |
| `heap_size` | Maximum number of transactions to be examined simultaneously for parallel propagation scheduling. Oracle automatically calculates the default setting for optimal performance.  Note:  Do not set this parameter unless directed to do so by Oracle Support Services. |

#### 145.3.3 DESTROY Procedure

This procedure removes all of the materialized views from a refresh group and delete the refresh group.

Syntax

```
DBMS_REFRESH.DESTROY (
   name   IN   VARCHAR2);
```

Parameters

Table 145-4 DESTROY Procedure Parameters

| Parameter | Description |
| --- | --- |
| `name` | Name of the refresh group that you want to destroy. |

#### 145.3.4 MAKE Procedure

This procedure specifies the members of a refresh group and the time interval used to determine when to refresh the members of this group.

Syntax

```
DBMS_REFRESH.MAKE (
   name                  IN    VARCHAR2
   { list                IN    VARCHAR2,
   | tab                 IN    DBMS_UTILITY.UNCL_ARRAY,}
   next_date             IN    DATE,
   interval              IN    VARCHAR2,
   implicit_destroy      IN    BOOLEAN         := FALSE,
   lax                   IN    BOOLEAN         := FALSE,
   job                   IN    BINARY_INTEGER  := 0,
   rollback_seg          IN    VARCHAR2        := NULL,
   push_deferred_rpc     IN    BOOLEAN         := TRUE,
   refresh_after_errors  IN    BOOLEAN         := FALSE
   purge_option          IN    BINARY_INTEGER  := NULL,
   parallelism           IN    BINARY_INTEGER  := NULL,
   heap_size             IN    BINARY_INTEGER  := NULL
   job_name              IN    VARCHAR2        := NULL,
   auto_commit           IN    BOOLEAN         := NULL);
```

Note:

This procedure is overloaded. The `list` and `tab` parameters are mutually exclusive.

Parameters

Table 145-5 MAKE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `name` | Unique name used to identify the refresh group, specified as `[schema_name.]refresh_group_name`. If the schema is not specified, then the current user is the default. Refresh groups must follow the same naming conventions as tables. |
| `list` | Comma-delimited list of materialized views that you want to refresh. Synonyms are not supported. These materialized views can be located in different schemas and have different master tables or master materialized views. However, all of the listed materialized views must be in your current database.  Each materialized view is specified as `[schema_name.]materialized_view_name`. If the schema is not specified, then the refresh group owner is the default. |
| `tab` | Instead of a comma-delimited list, you can supply a PL/SQL associative array of names of materialized views that you want to refresh using the data type `DBMS_UTILITY.UNCL_ARRAY`. If the table contains the names of n materialized views, then the first materialized view should be in position 1 and the n + 1 position should be set to `NULL`.  Each materialized view is specified as `[schema_name.]materialized_view_name`. If the schema is not specified, then the refresh group owner is the default. |
| `next_date` | Next date that you want a refresh to occur. |
| `interval` | Function used to calculate the next time to refresh the materialized views in the group. This field is used with the `next_date` value.  For example, if you specify `NEXT_DAY(SYSDATE+1, "MONDAY")` as your interval, and if your `next_date` evaluates to Monday, then Oracle refreshes the materialized views every Monday. This interval is evaluated immediately before the refresh. Thus, select an interval that is greater than the time it takes to perform a refresh. |
| `implicit_destroy` | Set this to `TRUE` to delete the refresh group automatically when it no longer contains any members. Oracle checks this flag only when you call the `SUBTRACT` procedure. That is, setting this flag still enables you to create an empty refresh group. |
| `lax` | A materialized view can belong to only one refresh group at a time. If you are moving a materialized view from an existing group to a new refresh group, then you must set this to `TRUE` to succeed. Oracle then automatically removes the materialized view from the other refresh group and updates its refresh interval to be that of its new group. Otherwise, the call to `MAKE` generates an error message. |
| `job` | Needed by the Import utility. Use the default value, 0. |
| `rollback_seg` | Name of the rollback segment to use while refreshing materialized views. The default, `NULL`, uses the default rollback segment. |
| `push_deferred_rpc` | Starting with Oracle Database 12c Release 2 (12.2), this parameter is ignored. |
| `refresh_after_errors` | Starting with Oracle Database 12c Release 2 (12.2), this parameter is ignored. |
| `purge_option` | Starting with Oracle Database 12c Release 2 (12.2), this parameter is ignored. |
| `parallelism` | - 0 specifies serial propagation. - n > 1 specifies parallel propagation with n parallel processes. - 1 specifies parallel propagation using only one parallel process. |
| `heap_size` | Maximum number of transactions to be examined simultaneously for parallel propagation scheduling. Oracle automatically calculates the default setting for optimal performance.  Note:  Do not set this parameter unless directed to do so by Oracle Support Services. |
| `job_name` | This parameter is needed by the import utility. User should use the default value, `NULL`. |
| `auto_commit` | Supported values are `NULL`, `TRUE`, and `FALSE`.  - `NULL` —allows the user to continue using `DBMS_JOB`. - `TRUE` —commit statement will be automatically issued after the job of the refresh group are created by `DBMS_REFRESH.MAKE`. - `FALSE` —user must issue a commit statement to finish the transaction after calling `DBMS_REFRESH.MAKE`.  The default value is `NULL`. |

Usage Notes

Import utility and export utility need `CREATE JOB` privilege if `DBMS_SCHEDULER` jobs are used.

#### 145.3.5 REFRESH Procedure

This procedure manually refreshes a refresh group.

Syntax

```
DBMS_REFRESH.REFRESH (
   name   IN    VARCHAR2);
```

Parameters

Table 145-6 REFRESH Procedure Parameters

| Parameter | Description |
| --- | --- |
| `name` | Name of the refresh group that you want to refresh manually. |

#### 145.3.6 SUBTRACT Procedure

This procedure removes materialized views from a refresh group.

Syntax

```
DBMS_REFRESH.SUBTRACT (
   name      IN    VARCHAR2,
   { list    IN    VARCHAR2,
   | tab     IN    DBMS_UTILITY.UNCL_ARRAY, }
   lax       IN    BOOLEAN := FALSE);
```

Note:

This procedure is overloaded. The `list` and `tab` parameters are mutually exclusive.

Parameters

Table 145-7 SUBTRACT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `name` | Name of the refresh group from which you want to remove members, specified as `[schema_name.]refresh_group_name`. If the schema is not specified, then the current user is the default. |
| `list` | Comma-delimited list of materialized views that you want to remove from the refresh group. (Synonyms are not supported.) These materialized views can be located in different schemas and have different master tables or master materialized views. However, all of the listed materialized views must be in your current database.  Each materialized view is specified as `[schema_name.]materialized_view_name`. If the schema is not specified, then the refresh group owner is the default. |
| `tab` | Instead of a comma-delimited list, you can supply a PL/SQL associative array of type `DBMS_UTILITY.UNCL_ARRAY`, where each element is the name of a materialized view. The first materialized view should be in position 1. The last position must be `NULL`.  Each materialized view is specified as `[schema_name.]materialized_view_name`. If the schema is not specified, then the refresh group owner is the default. |
| `lax` | Set this to `FALSE` if you want Oracle to generate an error message if the materialized view you are attempting to remove is not a member of the refresh group. |