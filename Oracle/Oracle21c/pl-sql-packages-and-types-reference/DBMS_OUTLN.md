---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/DBMS_OUTLN.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 125 DBMS\_OUTLN

The `DBMS_OUTLN` package, synonymous with `OUTLN_PKG`, contains the functional interface for subprograms associated with the management of stored outlines.

See Also:

For more information about using the `DBMS_OUTLN` package, see [Oracle Database SQL Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=TGSQL-GUID-F1C45056-F998-43E5-B362-83F88DA49E58).

Note:

Stored outlines will be desupported in a future release in favor of SQL plan management. In Oracle Database 11g Release 1 (11.1), stored outlines continue to function as in past releases. However, Oracle strongly recommends that you use SQL plan management for new applications. SQL plan management creates SQL plan baselines, which offer superior SQL performance and stability compared with stored outlines.If you have existing stored outlines, please consider migrating them to SQL plan baselines by using the [LOAD\_PLANS\_FROM\_CURSOR\_CACHE Functions](DBMS_SPM.md) or [LOAD\_PLANS\_FROM\_SQLSET Function](DBMS_SPM.md) of the `DBMS_SPM` package. When the migration is complete, you should disable or remove the stored outlines.

This chapter contains the following topics:

### 125.1 DBMS\_OUTLN Overview

A stored outline is the stored data that pertains to an execution plan for a given SQL statement. It enables the optimizer to repeatedly re-create execution plans that are equivalent to the plan originally generated along with the outline.The data stored in an outline consists, in part, of a set of hints that are used to achieve plan stability.

Stored outlines will be de-supported in a future release in favor of SQL plan management. As of 11g R1, stored outlines continue to function as in past releases, but Oracle strongly recommends that you use SQL plan management for new applications. SQL plan management creates SQL plan baselines, which offer superior SQL performance and stability compared with stored outlines.If you have existing stored outlines, please consider migrating them to SQL plan baselines by using the [LOAD\_PLANS\_FROM\_CURSOR\_CACHE Functions](DBMS_SPM.md) or the [LOAD\_PLANS\_FROM\_SQLSET Function](DBMS_SPM.md) of the [DBMS\_SPM](DBMS_SPM.md) package. When the migration is complete, you should disable or remove the stored outlines.

### 125.2 DBMS\_OUTLN Security Model

`DBMS_OUTLN` contains management procedures that should be available to appropriate users only. `EXECUTE` privilege is not extended to the general user community unless the DBA explicitly does so.

PL/SQL functions that are available for outline management purposes can be executed only by users with `EXECUTE` privilege on the procedure (or package).

### 125.3 Summary of DBMS\_OUTLN Subprograms

This table lists the `DBMS_OUTLN` subprograms and briefly describes them.

Table 125-1 DBMS\_OUTLN Package Subprograms

| Subprogram | Description |
| --- | --- |
| CLEAR\_USED Procedure | Clears the outline 'used' flag |
| CREATE\_OUTLINE Procedure | Generates outlines from the shared cursor identified by hash value and child number |
| DROP\_BY\_CAT Procedure | Drops outlines that belong to a specified category |
| DROP\_UNUSED Procedure | Drops outlines that have never been applied in the compilation of a SQL statement |
| EXACT\_TEXT\_SIGNATURES Procedure | Updates outline signatures to those that compute based on exact text matching |
| UPDATE\_BY\_CAT Procedure | Changes the category of outlines in one category to a new category |
| UPDATE\_SIGNATURES Procedure | Updates outline signatures to the current version's signature |

#### 125.3.1 CLEAR\_USED Procedure

This procedure clears the outline 'used' flag.

Syntax

```
DBMS_OUTLN.CLEAR_USED (
   name    IN    VARCHAR2);
```

Parameters

Table 125-2 CLEAR\_USED Procedure Parameters

| Parameter | Description |
| --- | --- |
| `name` | Name of the outline. |

#### 125.3.2 CREATE\_OUTLINE Procedure

This procedure generates an outline by reparsing the SQL statement from the shared cursor identified by hash value and child number.

Syntax

```
DBMS_OUTLN.CREATE_OUTLINE (
   hash_value    IN NUMBER,
   child_number  IN NUMBER,
   category      IN VARCHAR2 DEFAULT 'DEFAULT');
```

Parameters

Table 125-3 CREATE\_OUTLINE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `hash_value` | Hash value identifying the target shared cursor. |
| `child_number` | Child number of the target shared cursor. |
| `category` | Category in which to create outline (optional). |

#### 125.3.3 DROP\_BY\_CAT Procedure

This procedure drops outlines that belong to a particular category. While outlines are put into the `DEFAULT` category unless otherwise specified, users have the option of grouping their outlines into groups called categories.

Syntax

```
DBMS_OUTLN.DROP_BY_CAT (
   cat VARCHAR2);
```

Parameters

Table 125-4 DROP\_BY\_CAT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `cat` | Category of outlines to drop. |

Usage Notes

This procedure purges a category of outlines in a single call.

Examples

This example drops all outlines in the `DEFAULT` category:

```
DBMS_OUTLN.DROP_BY_CAT('DEFAULT');
```

#### 125.3.4 DROP\_UNUSED Procedure

This procedure drops outlines that have never been applied in the compilation of a SQL statement.

Syntax

```
DBMS_OUTLN.DROP_UNUSED;
```

Usage Notes

You can use `DROP_UNUSED` for outlines generated by an application for one-time use SQL statements created as a result of dynamic SQL. These outlines are never used and take up valuable disk space.

#### 125.3.5 EXACT\_TEXT\_SIGNATURES Procedure

This procedure updates outline signatures to those that compute based on exact text matching.

Syntax

```
DBMS_OUTLN.EXACT_TEXT_SIGNATURES;
```

Usage Notes

This procedure is relevant only for downgrading an outline to 8.1.6 or earlier.

#### 125.3.6 UPDATE\_BY\_CAT Procedure

This procedure changes the category of all outlines in one category to a new category.

Syntax

```
DBMS_OUTLN.UPDATE_BY_CAT (
   oldcat    VARCHAR2 default 'DEFAULT',
   newcat    VARCHAR2 default 'DEFAULT');
```

Parameters

Table 125-5 UPDATE\_BY\_CAT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `oldcat` | The current category of outlines. |
| `newcat` | The new category of outlines. |

#### 125.3.7 UPDATE\_SIGNATURES Procedure

This procedure updates outline signatures to the current version's signature.

Syntax

```
DBMS_OUTLN.UPDATE_SIGNATURES;
```

Usage Notes

You should execute this procedure if you have imported outlines generated in an earlier release to ensure that the signatures are compatible with the current release's computation algorithm.