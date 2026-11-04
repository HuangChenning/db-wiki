---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/DBMS_XMLINDEX.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 212 DBMS\_XMLINDEX

The `DBMS_XMLINDEX` package provides an interface to implement asynchronous indexing.

This chapter contains the following topics:

See Also:

Oracle XML DB Developer's Guide for more information about ["XMLIndex"](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADXDB0500)

### 212.1 DBMS\_XMLINDEX Overview

`DBMS_XMLINDEX` provides a mechanism for asynchronous index maintenance.

Asynchronous Index Maintenance

The basic XMLIndex is maintained on every DML operation. However, given the computing costs, in many cases the availability of stale result is adequate. In such situations, it is desirable to defer index updates to a more convenient time, for example when the load on the database is low. `DBMS_XMLINDEX` provides this mechanism.

### 212.2 DBMS\_XMLINDEX Security Model

Owned by `XDB`, the `DBMS_XMLINDEX` package must be created by `SYS` or `XDB`. The `EXECUTE` privilege is granted to `PUBLIC`.

Subprograms in this package are executed using the privileges of the current user.

### 212.3 Summary of DBMS\_XMLINDEX Subprograms

This table lists the `DBMS_XMLINDEX` subprograms and briefly describes them.

Table 212-1 DBMS\_XMLINDEX Package Subprograms

| Subprogram | Description |
| --- | --- |
| CREATEDATEINDEX Procedure | Creates a secondary index for date values in the `VALUE` column of a `PATH` `TABLE` which is the storage table of an `XMLIndex` |
| CREATENUMBERINDEX Procedure | Creates a secondary index for number values in the `VALUE` column of a `PATH` `TABLE` which is the storage table of an `XMLIndex` |
| DROPPARAMETER Procedure | Drops the `XMLIndex` parameter string that is associated with a given parameter identifier. |
| MODIFYPARAMETER Procedure | Modifies the `XMLIndex` parameter string that is associated with a given parameter name |
| PROCESS\_PENDING Procedure | Processes pending rows for a `NONBLOCKING` `ALTER` `INDEX` `OPERATION` on an `XMLIndex` |
| REGISTERPARAMETER Procedure | Registers a parameter string and `XMLIndex` parameter string pair in XDB |
| SYNCINDEX Procedure | Synchronizes the index manually |

#### 212.3.1 CREATEDATEINDEX Procedure

This procedure creates a secondary index for date values in the `VALUE` column of a `PATH` `TABLE` which is the storage table of an `XMLIndex`. The second form of the procedure allows for the `date_index_clause` to be set to an empty string.

Syntax

```
DBMS_XMLINDEX.CREATEDATEINDEX  (
   xml_index_schema   IN   VARCHAR2,
   xml_index_name     IN   VARCHAR2,
   date_index_name    IN   VARCHAR2,
   xmltypename        IN   VARCHAR2,
   date_index_clause  IN   VARCHAR2);

DBMS_XMLINDEX.CREATEDATEINDEX  (
   xml_index_schema   IN   VARCHAR2
   xml_index_name     IN   VARCHAR2,
   date_index_name    IN   VARCHAR2,
   xmltypename        IN   VARCHAR2);
```

Parameters

Table 212-2 CREATEDATEINDEX Procedure Parameters

| Parameter | Description |
| --- | --- |
| `xml_index_schema` | Name of the owner of the `XMLIndex` |
| `xml_index_name` | Name of the `XMLIndex` |
| `date_index_name` | Name of the secondary index to be created for date values in the `VALUE` column of the `PATH` `TABLE` of `XMLIndex` named `xml_index_name` and owned by `xml_index_schema` |
| `xmltypename` | The type to which values in the `VALUE` column of the path table are to be cast. Acceptable values are the following strings: `DATETIME`, `TIME`, `DATE`, `GDAY`, `GMONTH`, `GYEAR`, `GYEARMONTH`, `GMONTHDAY`. |
| `date_index_clause` | Storage clause to be applied to the date index during its creation. This is a string argument appended to the `CREATE` `INDEX` statement for creating the date index |

#### 212.3.2 CREATENUMBERINDEX Procedure

This procedure creates a secondary index for number values in the `VALUE` column of a `PATH` `TABLE` which is the storage table of an `XMLIndex`.

Syntax

```
DBMS_XMLINDEX.CREATENUMBERINDEX (
   xml_index_schema   IN   VARCHAR2,
   xml_index_name     IN   VARCHAR2,
   num_index_name     IN   VARCHAR2,
   num_index_clause   IN   VARCHAR2,
   xmltypename        IN   VARCHAR2);
```

Parameters

Table 212-3 CREATENUMBERINDEX Procedure Parameters

| Parameter | Description |
| --- | --- |
| `xml_index_schema` | Name of the owner of the `XMLIndex` |
| `xml_index_name` | Name of the `XMLIndex` |
| `num_index_name` | Name of the secondary index to be created for number values in the `VALUE` column of the `PATH` `TABLE` of `XMLIndex` named `xml_index_name` and owned by `xml_index_schema` |
| `num_index_clause` | Storage clause to be applied to the number index during its creation. This is a string argument appended to the `CREATE` `INDEX` statement for creating the number index. |
| `xmltypename` | The type to which values in the `VALUE` column of the path table are to be cast. Acceptable values are the following strings: `FLOAT`, `DOUBLE`, `DECIMAL`, `INTEGER`, `NONPOSITIVEINTEGER`, `NEGATIVEINTEGER`, `LONG`, `INT`, `SHORT`, `BYTE`, `NONNEGATIVEINTEGER`, `UNSIGNEDLONG`, `UNSIGNEDINT`, `UNSIGNEDSHORT`, `UNSIGNEDBYTE`, `POSITIVEINTEGER`. |

#### 212.3.3 DROPPARAMETER Procedure

This procedure drops the `XMLIndex` parameter string that is associated with a given parameter identifier.

Syntax

```
DBMS_XMLINDEX.DROPPARAMETER (
   name        IN      VARCHAR2);
```

Parameters

Table 212-4 DROPPARAMETER Procedure Parameters

| Parameter | Description |
| --- | --- |
| `name` | Identifier for parameter string |

Examples

```
DBMS_XMLINDEX.DROPPARAMETER ( 
   'myIndexParam');
```

#### 212.3.4 MODIFYPARAMETER Procedure

This procedure modifies the `XMLIndex` parameter string that is associated with a given parameter identifier.

Syntax

```
DBMS_XMLINDEX.MODIFYPARAMETER (
   name        IN      VARCHAR2, 
   parameter   IN      CLOB);
```

Parameters

Table 212-5 MODIFYPARAMETER Procedure Parameters

| Parameter | Description |
| --- | --- |
| `name` | Identifier for parameter string |
| `parameter` | `XMLIndex` parameter clause that can appear in a `CREATE` `INDEX` or an `ALTER` `INDEX` statement |

Examples

```
DBMS_XMLINDEX.MODIFYPARAMETER ( 
   'myIndexParam', 
   'PATH TABLE po_ptab 
    PATH ID INDEX po_pidx 
    ORDER KEY INDEX po_oidx 
    VALUE INDEX po_vidx');
```

#### 212.3.5 PROCESS\_PENDING Procedure

This procedure processes executes DMLs required to complete a `NONBLOCKING ALTER INDEX ADD_GROUP/ADD_COLUMN` operation on an `XMLIndex`.

Syntax

```
DBMS_XMLINDEX.PROCESS_PENDING (
   xml_index_schema    IN     VARCHAR2,
   xml_index_name      IN     VARCHAR2,
   pending_row_count   OUT    BINARY_INTEGER,
   error_row_count     OUT    BINARY_INTEGER);
```

Parameters

Table 212-6 PROCESS\_PENDING Procedure Parameters

| Parameter | Description |
| --- | --- |
| `xml_index_schema` | Name of the owner of the `XMLIndex` |
| `xml_index_name` | Name of the `XMLIndex` to be altered using `NONBLOCKING` `ALTER` `INDEX` `OPERATION` |
| `pending_row_count` | Number of pending rows to be processed |
| `error_row_count` | Number of rows for which indexing may have failed because of an error |

Usage Notes

- This procedure will iteratively attempt to index all necessary rows in small batches while skipping rows that are locked and rows for which index maintenance fails with an error. Therefore, it may have to be executed multiple times for an XMLIndex until all pending rows are processed. Once all pending rows are processed, user can complete the `NONBLOCKING` `ALTER` `INDEX` `OPERATION`.
- If it is not possible process all the pending rows after multiple trials, the user will have to manually triage the locking or error issues by examining unprocessed rows in `SYS_AIXSXI_######_PENDINGTAB` and errors in `SYS_AIXSXI_#####_ERRORTAB`.. Keeping track of rows and the errors is useful in triaging issues.

Examples

```
EXEC DBMS_XMLINDEX.PROCESS_PENDING(
   'SCOTT', 'PO_XMLINDEX_IX', out_param1, out_param2);
```

#### 212.3.6 REGISTERPARAMETER Procedure

This procedure registers a parameter identifier and `XMLIndex` parameter string pair in XDB.

Syntax

```
DBMS_XMLINDEX.REGISTERPARAMETER (
   name        IN      VARCHAR2, 
   parameter   IN      CLOB);
```

Parameters

Table 212-7 REGISTERPARAMETER Procedure Parameters

| Parameter | Description |
| --- | --- |
| `name` | Identifier for parameter string |
| `parameter` | `XMLIndex` parameter clause that can appear in a `CREATE` `INDEX` or an `ALTER` `INDEX` statement |

Examples

```
DBMS_XMLINDEX.REGISTERPARAMETER ( 
   'myIndexParam', 
   'PATH TABLE po_ptab 
    PATH ID INDEX po_pidx 
    ORDER KEY INDEX po_oidx 
    VALUE INDEX po_vidx 
    PATHS(NAMESPACE MAPPING(xmlns:p="http://www.example.com/IPO")) 
    GROUP MASTERGROUP XMLTABLE PO_TAB 
    (''/p:PurchaseOrder'' 
        COLUMNS 
           REFERENCE VARCHAR2(30) PATH ''p:Reference'', 
           REQUESTOR VARCHAR2(30) PATH ''p:Requestor'' ) 
    GROUP ITEMGROUP XMLTABLE ITEMGROUP_TAB     
    (''/p:PurchaseOrder/p:LineItems/p:LineItem'' 
        COLUMNS 
           LINENUMBER NUMBER(38) PATH ''@p:ItemNumber'', 
           QUANTITY NUMBER(38) PATH ''@p:Quantity'', 
           DESCRIPTION VARCHAR2(256) PATH ''p:Description'''));
```

#### 212.3.7 SYNCINDEX Procedure

This function synchronizes an asynchronously maintained XMLIndex.

It applies to the XMLIndex changes that are logged in the pending table, and brings the path table up-to-date with the base `XMLTYPE` column.

Syntax

```
DBMS_XMLINDEX.SYNCINDEX (
   xml_index_schema      IN VARCHAR2,
   xml_index_name        IN VARCHAR2,
   partition_name        IN VARCHAR2 DEFAULT NULL,
   reindex               IN BOOLEAN DEFAULT FALSE);
```

Parameters

Table 212-8 SYNCINDEX Procedure Parameters

| Parameter | Description |
| --- | --- |
| `xml_index_schema` | Name of the owner of the XMLIndex |
| `xml_schema_name` | Name of the XMLIndex |
| `partition_name` | \[Currently not supported\] |
| `reindex` | Default is `FALSE`. If set to `TRUE`, this drops the secondary indexes and recreates them later so that they can be bulk-loaded. |

Examples

```
EXEC DBMS_XMLINDEX.SYNCINDEX('USER1', 'SS_TAB_XMLI', REINDEX=>TRUE);
```