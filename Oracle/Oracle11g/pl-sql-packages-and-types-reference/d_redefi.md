---
title: DBMS_REDEFINITION
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_redefi.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 110 DBMS\_REDEFINITION

The `DBMS_REDEFINITION` package provides an interface to perform an online redefinition of tables.

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/tables.htm#ADMIN01514) for more information about online redefinition of tables

This chapter contains the following topics:

- Using DBMS\_REDEFINITION
- Summary of DBMS\_REDEFINITION Subprograms

---

## Using DBMS\_REDEFINITION

---

### Overview

To achieve online redefinition, incrementally maintainable local materialized views are used. These logs keep track of the changes to the master tables and are used by the materialized views during refresh synchronization.

---

### Security Model

Subprograms in the `DBMS_REDEFINTION` package are run with invokers' rights (with the privileges of the current user). There are two modes:

- In `USER` mode, the user who has the `CREATE TABLE` and `CREATE MVIEW` privileges may redefine a table residing in his own schema.
- In `FULL` mode, the user who has the `ANY` privilege may redefine tables in any schema.

---

### Constants

The `DBMS_REDEFINITION` package uses the constants shown in Table 110-1, "DBMS\_REDEFINITION Constants":

Table 110-1 DBMS\_REDEFINITION Constants

| Constant | Type | Value | Description |
| --- | --- | --- | --- |
| `CONS_CONSTRAINT` | `PLS_INTEGER` | `3` | Used to specify that dependent object type is a constraint |
| `CONS_INDEX` | `PLS_INTEGER` | `2` | Used to specify that dependent object type is a index |
| `CONS_MVLOG` | `PLS_INTEGER` | `10` | Used to (un)register a materialized view log, as a dependent object of the table, through the REGISTER\_DEPENDENT\_OBJECT Procedure and the UNREGISTER\_DEPENDENT\_OBJECT Procedure. |
| `CONS_ORIG_PARAMS` | `PLS_INTEGER` | `1` | Used to specify that indexes should be cloned with their original storage parameters |
| `CONS_TRIGGER` | `PLS_INTEGER` | `4` | Used to specify that dependent object type is a trigger |
| `CONS_USE_PK` | `BINARY_INTEGER` | `1` | Used to indicate that the redefinition should be done using primary keys or pseudo-primary keys (unique keys with all component columns having not- `NULL` constraints) |
| `CONS_USE_ROWID` | `BINARY_INTEGER` | `2` | Used to indicate that the redefinition should be done using rowids |

---

### Operational Notes

- `CONS_USE_PK` and `CONS_USE_ROWID` are constants used as input to the "options\_flag" parameter in both the START\_REDEF\_TABLE Procedure and CAN\_REDEF\_TABLE Procedure. `CONS_USE_ROWID` is used to indicate that the redefinition should be done using rowids while `CONS_USE_PK` implies that the redefinition should be done using primary keys or pseudo-primary keys (which are unique keys with all component columns having `NOT` `NULL` constraints).
- `CONS_INDEX`, `CONS_MVLOG`,`CONS_TRIGGER` and `CONS_CONSTRAINT` are used to specify the type of the dependent object being (un)registered in REGISTER\_DEPENDENT\_OBJECT Procedure and UNREGISTER\_DEPENDENT\_OBJECT Procedure (parameter " `dep_type` ").
	`CONS_INDEX` ==> dependent object is of type `INDEX`
	`CONS_TRIGGER` ==> dependent object is of type `TRIGGER`
	`CONS_CONSTRAINT` ==> dependent object type is of type `CONSTRAINT`
	`CONS_MVLOG` ==> dependent object is of type `MATERIALIZED` `VIEW` `LOG`
- `CONS_ORIG_PARAMS` as used as input to the " `copy_indexes` " parameter in COPY\_TABLE\_DEPENDENTS Procedure. Using this parameter implies that the indexes on the original table be copied onto the interim table using the same storage parameters as that of the original index.

---

### Rules and Limits

For information about various rules and limits that apply to implementation of this package, see the [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/tables.htm#ADMIN01510).

---

## Summary of DBMS\_REDEFINITION Subprograms

Table 110-2 DBMS\_REDEFINITION Package Subprograms

| Subprogram | Description |
| --- | --- |
| ABORT\_REDEF\_TABLE Procedure | Cleans up errors that occur during the redefinition process and removes all temporary objects created by the reorganization process |
| CAN\_REDEF\_TABLE Procedure | Determines if a given table can be redefined online |
| COPY\_TABLE\_DEPENDENTS Procedure | Copies the dependent objects of the original table onto the interim table |
| FINISH\_REDEF\_TABLE Procedure | Completes the redefinition process. |
| REGISTER\_DEPENDENT\_OBJECT Procedure | Registers a dependent object (index, trigger, constraint or materialized view log) on the table being redefined and the corresponding dependent object on the interim table |
| START\_REDEF\_TABLE Procedure | Initiates the redefinition process |
| SYNC\_INTERIM\_TABLE Procedure | Keeps the interim table synchronized with the original table |
| UNREGISTER\_DEPENDENT\_OBJECT Procedure | Unregisters a dependent object (index, trigger, constraint or materialized view log) on the table being redefined and the corresponding dependent object on the interim table |

---

### ABORT\_REDEF\_TABLE Procedure

This procedure cleans up errors that occur during the redefinition process. This procedure can also be used to terminate the redefinition process any time after the START\_REDEF\_TABLE Procedure has been called and before the FINISH\_REDEF\_TABLE Procedure is called. This process will remove the temporary objects that are created by the redefinition process such as materialized view logs.

Syntax

```
DBMS_REDEFINITION.ABORT_REDEF_TABLE (
   uname       IN VARCHAR2,
   orig_table  IN VARCHAR2,
   int_table   IN VARCHAR2,
  part_name    IN  VARCHAR2 := NULL);
```

Parameters

Table 110-3 ABORT\_REDEF\_TABLE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `uname` | Schema name of the tables |
| `orig_table` | Name of the table to be redefined |
| `int_table` | Name of the interim table |
| `part_name` | Name of the partition being redefined. If redefining only a single partition of a table, specify the partition name in this parameter. `NULL` implies the entire table is being redefined. |

---

### CAN\_REDEF\_TABLE Procedure

This procedure determines if a given table can be redefined online. This is the first step of the online redefinition process. If the table is not a candidate for online redefinition, an error message is raised.

Syntax

```
DBMS_REDEFINITION.CAN_REDEF_TABLE (
   uname         IN  VARCHAR2,
   tname        IN  VARCHAR2,
   options_flag  IN  PLS_INTEGER := 1,
   part_name     IN  VARCHAR2 := NULL);
```

Parameters

Table 110-4 CAN\_REDEF\_TABLE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `uname` | Schema name of the table |
| `tname` | Name of the table to be re-organized |
| `options_flag` | Indicates the type of redefinition method to use.  - If `dbms_redefinition.cons_use_pk`, the redefinition is done using primary keys or pseudo-primary keys (unique keys with all component columns having `NOT` `NULL` constraints). The default method of redefinition is using primary keys. - If `dbms_redefinition.cons_use_rowid`, the redefinition is done using rowids. |
| `part_name` | Name of the partition being redefined. If redefining only a single partition of a table, specify the partition name in this parameter. `NULL` implies the entire table is being redefined. |

Exceptions

If the table is not a candidate for online redefinition, an error message is raised.

---

### COPY\_TABLE\_DEPENDENTS Procedure

This procedure clones the dependent objects of the table being redefined onto the interim table and registers the dependent objects. This procedure does not clone the already registered dependent objects.

This subprogram is used to clone the dependent objects like grants, triggers, constraints and privileges from the table being redefined to the interim table (which represents the post-redefinition table).

Syntax

```
DBMS_REDEFINITION.COPY_TABLE_DEPENDENTS(
   uname                    IN  VARCHAR2,
   orig_table               IN  VARCHAR2,
   int_table                IN  VARCHAR2,
   copy_indexes             IN  PLS_INTEGER := 1,
   copy_triggers            IN  BOOLEAN     := TRUE,
   copy_constraints         IN  BOOLEAN     := TRUE,
   copy_privileges          IN  BOOLEAN     := TRUE,
   ignore_errors            IN  BOOLEAN     := FALSE,
   num_errors               OUT PLS_INTEGER,
   copy_statistics          IN  BOOLEAN     := FALSE, 
   copy_mvlog               IN  BOOLEAN     := FALSE);
```

Parameters

Table 110-5 COPY\_TABLE\_DEPENDENTS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `uname` | Schema name of the tables |
| `orig_table` | Name of the table being redefined |
| `int_table` | Name of the interim table |
| `copy_indexes` | Flag indicating whether to copy the indexes  - `0` - do not copy any index - `dbms_redefinition`.`cons_orig_params` – copy the indexes using the physical parameters of the source indexes |
| `copy_triggers` | `TRUE` = clone triggers, `FALSE` = do nothing |
| `copy_constraints` | `TRUE` = clone constraints, `FALSE` = do nothing. If compatibility setting is 10.2 or higher, then clone `CHECK` and `NOT` `NULL` constraints |
| `copy_privileges` | `TRUE` = clone privileges, `FALSE` = do nothing |
| `ignore_errors` | `TRUE` = if an error occurs while cloning a particular dependent object, then skip that object and continue cloning other dependent objects. `FALSE` = that the cloning process should stop upon encountering an error. |
| `num_errors` | Number of errors that occurred while cloning dependent objects |
| `copy_statistics` | `TRUE` = copy statistics, `FALSE` = do nothing |
| `copy_mvlog` | `TRUE` = copy materialized view log, `FALSE` = do nothing |

Usage Notes

- The user must check the column `num_errors` before proceeding to ensure that no errors occurred during the cloning of the objects.
- In case of an error, the user should fix the cause of the error and call the COPY\_TABLE\_DEPENDENTS Procedure again to clone the dependent object. Alternatively the user can manually clone the dependent object and then register the manually cloned dependent object using the REGISTER\_DEPENDENT\_OBJECT Procedure.
- All cloned referential constraints involving the interim tables will be created disabled (they will be automatically enabled after the redefinition) and all triggers on interim tables will not fire till the redefinition is completed. After the redefinition is complete, the cloned objects will be renamed to the corresponding pre-redefinition names of the objects (from which they were cloned from).
- It is the user's responsibility that the cloned dependent objects are unaffected by the redefinition. All the triggers will be cloned and it is the user's responsibility that the cloned triggers are unaffected by the redefinition.

---

### FINISH\_REDEF\_TABLE Procedure

This procedure completes the redefinition process. Before this step, you can create new indexes, triggers, grants, and constraints on the interim table. The referential constraints involving the interim table must be disabled. After completing this step, the original table is redefined with the attributes and data of the interim table. The original table is locked briefly during this procedure.

Syntax

```
DBMS_REDEFINITION.FINISH_REDEF_TABLE (
   uname       IN VARCHAR2,
   orig_table  IN VARCHAR2,
   int_table   IN VARCHAR2,
   part_name   IN  VARCHAR2 := NULL);
```

Parameters

Table 110-6 FINISH\_REDEF\_TABLE Procedure Parameters

| Parameters | Description |
| --- | --- |
| `uname` | Schema name of the tables |
| `orig_table` | Name of the table to be redefined |
| `int_table` | Name of the interim table |
| `part_name` | Name of the partition being redefined. If redefining only a single partition of a table, specify the partition name in this parameter. `NULL` implies the entire table is being redefined. |

---

### REGISTER\_DEPENDENT\_OBJECT Procedure

This procedure registers a dependent object (index, trigger, constraint or materialized view log) on the table being redefined and the corresponding dependent object on the interim table.

This can be used to have the same object on each table but with different attributes. For example: for an index, the storage and tablespace attributes could be different but the columns indexed remain the same

Syntax

```
DBMS_REDEFINITION.REGISTER_DEPENDENT_OBJECT(
   uname             IN VARCHAR2,
   orig_table        IN VARCHAR2,
   int_table         IN VARCHAR2,
   dep_type          IN  PLS_INTEGER,
   dep_owner         IN VARCHAR2,
   dep_orig_name     IN VARCHAR2,
   dep_int_name      IN  VARCHAR2);
```

Parameters

Table 110-7 REGISTER\_DEPENDENT\_OBJECT Procedure Parameters

| Parameters | Description |
| --- | --- |
| `uname` | Schema name of the tables |
| `orig_table` | Name of the table to be redefined |
| `int_table` | Name of the interim table |
| `dep_type` | Type of the dependent object (see Constants and Operational Notes) |
| `dep_owner` | Owner of the dependent object |
| `dep_orig_name` | Name of the original dependent object |
| `dep_int_name` | Name of the interim dependent object |

Usage Notes

- Attempting to register an already registered object will raise an error.
- Registering a dependent object will automatically remove that object from `DBA_REDEFINITION_ERRORS` if an entry exists for that object.

---

### START\_REDEF\_TABLE Procedure

Prior to calling this procedure, you must manually create an empty interim table (in the same schema as the table to be redefined) with the desired attributes of the post-redefinition table, and then call this procedure to initiate the redefinition.

Syntax

```
DBMS_REDEFINITION.START_REDEF_TABLE (
   uname          IN VARCHAR2,
   orig_table     IN VARCHAR2,
   int_table      IN VARCHAR2,
   col_mapping    IN VARCHAR2 := NULL,
   options_flag   IN BINARY_INTEGER := 1,
   orderby_cols   IN VARCHAR2 := NULL,
   part_name     IN  VARCHAR2 := NULL);
```

Parameters

Table 110-8 START\_REDEF\_TABLE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `uname` | Schema name of the tables |
| `orig_table` | Name of the table to be redefined |
| `int_table` | Name of the interim table |
| `col_mapping` | Mapping information from the columns in the original table to the columns in the interim table. (This is similar to the column list on the `SELECT` clause of a query.) If `NULL,` all the columns in the original table are selected and have the same name after redefinition. |
| `options_flag` | Indicates the type of redefinition method to use:  - If `dbms_redefinition.cons_use_pk`, the redefinition is done using primary keys or pseudo-primary keys (unique keys with all component columns having `NOT` `NULL` constraints). The default method of redefinition is using primary keys. - If `dbms_redefinition.cons_use_rowid`, the redefinition is done using rowids. |
| `orderby_cols` | This optional parameter accepts the list of columns (along with the optional keyword(s) ascending/descending) with which to order by the rows during the initial instantiation of the interim table (the order by is only done for the initial instantiation and not for subsequent synchronizations) |
| `part_name` | Name of the partition being redefined. If redefining only a single partition of a table, specify the partition name in this parameter. `NULL` implies the entire table is being redefined. |

---

### SYNC\_INTERIM\_TABLE Procedure

This procedure keeps the interim table synchronized with the original table.

Syntax

```
DBMS_REDEFINITION.SYNC_INTERIM_TABLE (
   uname          IN  VARCHAR2,
   orig_table     IN  VARCHAR2,
   int_table      IN  VARCHAR2,
   part_name      IN  VARCHAR2 := NULL);
```

Parameters

Table 110-9 SYNC\_INTERIM\_TABLE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `uname` | Schema name of the table |
| `orig_table` | Name of the table to be redefined |
| `int_table` | Name of the interim table |
| `part_name` | Name of the partition being redefined. If redefining only a single partition of a table, specify the partition name in this parameter. `NULL` implies the entire table is being redefined. |

Usage Notes

- This step is useful in minimizing the amount of synchronization needed to be done by the FINISH\_REDEF\_TABLE Procedure before completing the online redefinition.
- This procedure can be called between long running operations (such as `CREATE` `INDEX`) on the interim table to sync it up with the data in the original table and speed up subsequent operations.

---

### UNREGISTER\_DEPENDENT\_OBJECT Procedure

This procedure unregisters a dependent object (index, trigger, constraint or materialized view log) on the table being redefined and the corresponding dependent object on the interim table.

Syntax

```
DBMS_REDEFINITION.UNREGISTER_DEPEPENDENT_OBJECT(
   uname              IN VARCHAR2,
   orig_table        IN VARCHAR2,
   int_table         IN VARCHAR2,
   dep_type          IN PLS_INTEGER,
   dep_owner         IN VARCHAR2,
   dep_orig_name     IN VARCHAR2,
   dep_int_name      IN  VARCHAR2);
```

Parameters

Table 110-10 UNREGISTER\_DEPENDENT\_OBJECT Procedure Parameters

| Parameters | Description |
| --- | --- |
| `uname` | Schema name of the tables |
| `orig_table` | Name of the table to be redefined |
| `int_table` | Name of the interim table |
| `dep_type` | Type of the dependent object |
| `dep_owner` | Owner of the dependent object |
| `dep_orig_name` | Name of the original dependent object |
| `dep_int_name` | Name of the interim dependent object |