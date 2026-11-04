---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/DBMS_PART.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 128 DBMS\_PART

The `DBMS_PART` package provides an interface for maintenance and management operations on partitioned objects.

This chapter contains the following topics:

### 128.1 DBMS\_PART Security Model

`DBMS_PART` is an invoker's rights package, running with the privileges of the user.

### 128.2 DBMS\_PART Operational Notes

The following operational notes apply to DBMS\_PART.

- `DBMS_PART` ignores all the errors that it runs into during the cleanup process.
- To display the message `PL/SQL procedure executed successfully` requires at least one cleanup operation to be successful.

### 128.3 Summary of DBMS\_PART Subprograms

This table briefly describes the subprograms of `DBMS_PART` package.

Table 128-1 DBMS\_PART Package Subprograms

| Subprogram | Description |
| --- | --- |
| CLEANUP\_GIDX Procedure | Gathers the list of global indexes where optimized asynchronous index maintenance has taken place to clean up entries pointing to data segments that no longer exist |
| CLEANUP\_GIDX\_JOB Procedure |  |
| CLEANUP\_ONLINE\_OP Procedure | Cleans up failed online move operations |

#### 128.3.1 CLEANUP\_GIDX Procedure

As a consequence of prior partition maintenance operations with asynchronous global index maintenance, global indexes can contain entries pointing to data segments that no longer exist. These stale index rows will not cause any correctness issues or corruptions during any operation on the table or index, whether these are queries, DMLs, DDLs or analyze. This procedure will identify and cleanup these global indexes to ensure efficiency in terms of storage and performance.

Syntax

```
DBMS_PART.CLEANUP_GIDX (
   schema_name_in    IN   VARCHAR2 DEFAULT NULL,
   table_name_in     IN   VARCHAR2 DEFAULT NULL,
   parallel          IN   VARCHAR2 DEFAULT NULL,
   options           IN   VARCHAR2 DEFAULT NULL);
```

Parameters

Table 128-2 CLEANUP\_GIDX Function Parameters

| Parameter | Description |
| --- | --- |
| `schema_name_in` | Non- `NULL` processes only indexes on tables in the given schema |
| `table_name_in` | Non- `NULL` processes only indexes on the given table in the given schema (`schema_name_in` must be non- `NULL` if `table_name_in` is non- `NULL`) |
| `parallel` | The parallel degree to use for the `ALTER INDEX` DDLs. |
| `options` | The following options are supported: - `CLEANUP_ORPHANS`: implies that 'cleanup only' mechanism is used. - `COALESCE`: implies that 'coalesce cleanup' mechanism is used. |

#### 128.3.2 CLEANUP\_GIDX\_JOB Procedure

This procedure will identify and cleanup these global indexes to ensure efficiency in terms of storage and performance.

Syntax

```
DBMS_PART.CLEANUP_GIDX_JOB (
   parallel          IN   VARCHAR2 DEFAULT NULL,
   options           IN   VARCHAR2 DEFAULT NULL);
```

Parameters

Table 128-3 CLEANUP\_GIDX\_JOB Function Parameters

| Parameter | Description |
| --- | --- |
| `parallel` | The parallel degree to use for the `ALTER INDEX` DDLs. |
| `options` | The following options are supported: - `CLEANUP_ORPHANS`: implies that 'cleanup only' mechanism is used. - `COALESCE`: implies that coalesce cleanup mechanism is used. |

#### 128.3.3 CLEANUP\_ONLINE\_OP Procedure

There are many possible points of failure when performing `ALTER TABLE ... MOVE PARTITION ... ONLINE` operations. This procedure pro-actively cleans up such failed online move operations instead of waiting for the background process (`SMON`) to do so.

Syntax

```
DBMS_PART.CLEANUP_ONLINE_OP (
   schema_name       IN   VARCHAR2 DEFAULT NULL,
   table_name        IN   VARCHAR2 DEFAULT NULL, 
   partition_name    IN   VARCHAR2 DEFAULT NULL);
```

Parameters

Table 128-4 CLEANUP\_ONLINE\_OP Function Parameters

| Parameter | Description |
| --- | --- |
| `schema_name` | Name of schema |
| `table_name` | Name of schema |
| `partition_name` | Name of partition |

Usage Notes

- If `schema_name`, `table_name` and `partition_name` are specified, this cleans up the failed online move operation for the specified partition.
- If `schema_name` and `table_name` are specified, this cleans up all failed online move operations for all the partitions of the specified table.
- If only `schema_name` is specified, this cleans up all failed online move operations in the schema.
- If no arguments are provided, we cleans up all the failed online move operations in the system.
- All other cases raise `ORA-20000` to inform the user of invalid inputs as arguments.