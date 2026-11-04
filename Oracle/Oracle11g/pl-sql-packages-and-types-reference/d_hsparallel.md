---
title: DBMS_HS_PARALLEL
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_hsparallel.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 74 DBMS\_HS\_PARALLEL

The `DBMS_HS_PARALLEL` PL/SQL package enables parallel processing for heterogeneous targets access. This package is designed to improve performance when retrieving data from a large foreign table.

This chapter discusses the following topics:

- Using DBMS\_HS\_PARALLEL
- Summary of DBMS\_HS\_PARALLEL Subprograms

---

## Using DBMS\_HS\_PARALLEL

`DBMS_HS_PARALLEL` is compiled with the authorization ID of `CURRENT_USER`, which uses invoker's rights. In other words, all procedures in this package are executed with the privileges of the calling user.

---

## Summary of DBMS\_HS\_PARALLEL Subprograms

Table 74-1 DBMS\_HS\_PARALLEL Package Subprograms

| Subprogram | Description |
| --- | --- |
| CREATE\_OR\_REPLACE\_VIEW | Creates (or replaces) a read-only view to be referenced for retrieving the data from a remote table in parallel. |
| CREATE\_TABLE\_TEMPLATE | Writes out a `CREATE TABLE` template based on information gathered from the remote table. You can use the information to add any optimal Oracle `CREATE TABLE` clauses. |
| DROP\_VIEW | Drops the view and internal objects created by the `CREATE_OR_REPLACE_VIEW` procedure. If the view has not already been created by the `CREATE_OR_REPLACE_VIEW` procedure, an error message is returned. |
| LOAD\_TABLE | Loads the data from a remote table to a local Oracle table in parallel. If the local Oracle table does not already exist, it is created automatically. |

---

### CREATE\_OR\_REPLACE\_VIEW

This procedure creates (or replaces) a read-only view to be referenced for retrieving the data from a remote table in parallel.

#### Syntax

```
CREATE_OR_REPLACE_VIEW (remote_table, database_link, oracle_view, parallel_degree)
```

#### Parameters

Table 74-2 CREATE\_OR\_REPLACE\_VIEW Parameter

| Parameter | Value | Description |
| --- | --- | --- |
| `remote_table` | `IN VARCHAR2 NOT NULL` | The name of the remote database table. It is specified as `[remote_schema_name.]remote_table_name`. |
| `database_link` | `IN VARCHAR2 NOT NULL` | The remote database link name. The call can only be applied to a heterogeneous services database link. |
| `oracle_view` | `IN VARCHAR2` | The name of the Oracle view. It is specified as `[schema_name.]oracle_view_name`. The default schema name is the current user. If the `oracle_view` parameter is not specified, the remote table name will be used as the view name. |
| `parallel_degree` | `IN NUMBER` | The number of parallel processes for the operation is computed based on the range-partition number if applicable, or the number of CPUs. The range of values is `2` to `16`. |

Usage Notes

- The specified Oracle view is created and future reference of this view utilizes internal database objects for parallel retrieval of remote non-Oracle table data. If the Oracle view already exists, the following Oracle error message is raised:
	```
	ORA-00955: name is already used by an existing object
	```
- This view is created as a read-only view. If you attempt to insert and update the view, the following Oracle error message is raised:
	```
	ORA-01733: virtual column not allowed here
	```
- If the remote table or the database link does not exist, one of the following Oracle error messages is raised:
	```
	ORA-00942: table or view does not exist
	or
	ORA-02019: connection description for remote database not found
	```
- You need the `CREATE VIEW`, `CREATE TABLE`, `CREATE TYPE`, `CREATE PACKAGE`, and `CREATE FUNCTION` privileges to execute the `CREATE_OR_REPLACE_VIEW` procedure.
- If you encounter either of the following Oracle error messages, increase the `PROCESSES` and `SESSIONS` parameter in the Oracle initialization parameter file:
	```
	ORA-12801: error signaled in parallel query server P003
	or
	ORA-00018: maximum number of session exceeded
	```
- Because the `CREATE_OR_REPLACE_VIEW` procedure creates some internal objects, use the `DROP_VIEW` procedure to drop the view and the internal objects. The SQL `DROP VIEW` statement only drops the view and not the internal objects.

---

### CREATE\_TABLE\_TEMPLATE

This procedure writes out a `CREATE TABLE` template based on information gathered from the remote table. You can use the information to add any optimal Oracle `CREATE TABLE` clauses.

#### Syntax

```
CREATE_TABLE_TEMPLATE (remote_table, database_link, oracle_table, create_table_template_string)
```

#### Parameters

Table 74-3 CREATE\_TABLE\_TEMPLATE Parameter

| Parameter | Value | Description |
| --- | --- | --- |
| `remote_table` | `IN VARCHAR2 NOT NULL` | The name of the remote database table. It is specified as `[remote_schema_name.]remote_table_name`. |
| `database_link` | `IN VARCHAR2 NOT NULL` | The remote database link name. The call can only be applied to a heterogeneous services database link. |
| `oracle_table` | `IN VARCHAR2` | The name of the local Oracle table the data will be loaded into. It is specified as `[schema_name.]oracle_table_name`. The default schema name is the current user. If the `oracle_table` parameter is not specified, the remote table name will be used as the local Oracle name. |
| `create_table_template_string` | `OUT VARCHAR2` | Contains the Oracle `CREATE TABLE` SQL template when the procedure is returned. |

---

### DROP\_VIEW

This procedure drops the view and internal objects created by the `CREATE_OR_REPLACE_VIEW` procedure. If the view has not already been created by the `CREATE_OR_REPLACE_VIEW` procedure, an error message is returned.

#### Syntax

```
DROP_VIEW (oracle_view)
```

#### Parameters

Table 74-4 DROP\_VIEW Parameter

| Parameter | Value | Description |
| --- | --- | --- |
| `oracle_view` | `IN VARCHAR2 NOT NULL` | The name of the Oracle view created by the `CREATE_OR_REPLACE_VIEW` procedure. If the view has not been created by the `CREATE_OR_REPLACE_VIEW` procedure, an error is returned. |

---

### LOAD\_TABLE

This procedure loads the data from a remote table to a local Oracle table in parallel. If the local Oracle table does not already exist, it is created automatically.

#### Syntax

```
LOAD_TABLE (remote_table, database_link, oracle_table, truncate, parallel_degree, row_count)
```

#### Parameters

Table 74-5 LOAD\_TABLE Parameters

| Parameter | Value | Description |
| --- | --- | --- |
| `remote_table` | `IN VARCHAR2 NOT NULL` | The name of the remote database table. It is specified as `[remote_schema_name.]remote_table_name` |
| `database_link` | `IN VARCHAR2 NOT NULL` | The remote database link name. The call can only be applied to a heterogeneous services database link. |
| `oracle_table` | `IN VARCHAR2` | The name of the local Oracle table the data will be loaded into. It is specified as `[schema_name.]oracle_table_name`. The default schema name is the current user. If the `oracle_table` parameter is not specified, the remote table name will be used as the local Oracle name. |
| `truncate` | `IN BOOLEAN` | Determines whether the Oracle table is truncated before the data is loaded. The value is either `TRUE` or `FALSE`. The default value is `TRUE` which means the Oracle table is truncated first. When set to `FALSE`, the Oracle table will not be truncated before the data is loaded. |
| `parallel_degree` | `IN NUMBER` | The number of parallel processes for the operation is computed based on the range-partition number if applicable, or the number of CPUs. The range of values is `2` to `16`. |
| `row_count` | `OUT NUMBER` | Contains the number of rows just added with the load table operation. |

Usage Notes

- This procedure only loads the remote table data into Oracle local table. It does not create a key, index, constraints or any other dependencies such as triggers. It is recommended that you create these dependencies after the table data is loaded as performance will improve greatly. You will need to decide whether to create the dependencies before or after the data is loaded based on your knowledge of the remote table data and dependencies.
- If the local table does not exist, the `LOAD_TABLE` procedure creates a simple (non-partitioned) local table based on the exact column matching of the remote table after which the data is inserted into the local table.
- If the remote table or the database link does not exist, an error message is returned.
- If the local table is incompatible with the remote table, an error message is returned.
- You need the `CREATE TABLE`, `CREATE TYPE`, `CREATE PACKAGE`, and `CREATE FUNCTION` privileges to execute the `LOAD_TABLE` procedure.
- If you encounter either of the following Oracle error messages, increase the `PROCESSES` and `SESSIONS` parameter in Oracle initialization parameter file:
	```
	ORA-12801: error signaled in parallel query server P003
	or
	ORA-00018: maximum number of session exceeded
	```
- One of the following is required for parallel processing:
	- The remote table is range partitioned.
		- Histogram information for a numeric column is available.
		- There is a numeric index or primary key.
- To drop the local table, use the `DROP TABLE` SQL statement.