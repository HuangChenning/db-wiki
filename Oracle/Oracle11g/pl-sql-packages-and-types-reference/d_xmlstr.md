---
title: DBMS_XMLSTORE
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_xmlstr.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 178 DBMS\_XMLSTORE

`DBMS_XMLSTORE` provides the ability to store XML data in relational tables.

See Also:

[Oracle XML DB Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e23094/toc.htm)

This chapter contains the following sections:

- Using DBMS\_XMLSTORE
- Summary of DBMS\_XMLSTORE Subprograms

---

## Using DBMS\_XMLSTORE

- Security Model
- Types

---

### Security Model

Owned by `XDB`, the `DBMS_XMLSTORE` package must be created by `SYS` or `XDB`. The `EXECUTE` privilege is granted to `PUBLIC`. Subprograms in this package are executed using the privileges of the current user.

---

### Types

Table 178-1 Types of DBMS\_XMLSTORE

| Type | Description |
| --- | --- |
| `ctxType` | The type of the query context handle. This is the return type of NEWCONTEXT. |

---

## Summary of DBMS\_XMLSTORE Subprograms

Table 178-2 DBMS\_XMLSTORE Package Subprograms

| Method | Description |
| --- | --- |
| CLEARKEYCOLUMNLIST | Clears the key column list. |
| CLEARUPDATECOLUMNLIST | Clears the update column list. |
| CLOSECONTEXT | It closes/deallocates a particular save context. |
| DELETEXML | Deletes records specified by data from the XML document, from the table specified at the context creation time. |
| INSERTXML | Inserts the XML document into the table specified at the context creation time. |
| NEWCONTEXT | Creates a save context, and returns the context handle. |
| SETKEYCOLUMN | This method adds a column to the key column list. |
| SETROWTAG | Names the tag used in the XML document., to enclose the XML elements corresponding to the database. |
| SETUPDATECOLUMN | Adds a column to the "update column list". |
| UPDATEXML | Updates the table given the XML document. |

---

### CLEARKEYCOLUMNLIST

Clears the key column list.

Syntax

```
PROCEDURE clearKeyColumnList(
   ctxHdl IN ctxType);
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |

---

### CLEARUPDATECOLUMNLIST

Clears the update column list.

Syntax

```
PROCEDURE clearUpdateColumnList(
   ctxHdl IN ctxType);
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |

---

### CLOSECONTEXT

Closes/deallocates a particular save context.

Syntax

```
PROCEDURE closeContext(
   ctxHdl IN ctxType);
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |

---

### DELETEXML

Deletes records specified by data from the XML document from the table specified at the context creation time, and returns the number of rows deleted.

| Syntax | Description |
| --- | --- |
| `FUNCTION deleteXML(`  `   ctxHdl IN ctxPType,`  `   xDoc IN VARCHAR2)`  `RETURN NUMBER;` | Uses a `VARCHAR2` type for the `xDoc` parameter. |
| `FUNCTION deleteXML(`  `   ctxHdl IN ctxType,`  `   xDoc IN CLOB)`  `RETURN NUMBER;` | Uses a `CLOB` type for the `xDoc` parameter. |
| `FUNCTION deleteXML(`  `   ctxHdl IN ctxType,`  `   xDoc IN XMLType)`  `RETURN NUMBER;` | Uses an `XMLType` type for the `xDoc` parameter. |

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |
| `xDoc` | `(IN)` | String containing the XML document. |

---

### INSERTXML

Inserts the XML document into the table specified at the context creation time, and returns the number of rows inserted.

Note that if a user passes an XML file for insertXML to `DBMS_XMLSTORE` which contains extra elements (ones that do not match up to any columns in the table), Oracle will try to insert into those columns unless SETUPDATECOLUMN is used. The use of setUpdateColumn is optional only if the elements in the XML file match up to the columns in the table.

| Syntax | Description |
| --- | --- |
| `FUNCTION insertXML(`  `   ctxHdl IN ctxType,`  `   xDoc IN VARCHAR2)`  `RETURN NUMBER;` | Passes in the `xDoc` parameter as a `VARCHAR2`. |
| `FUNCTION insertXML(`  `   ctxHdl IN ctxType,`  `   xDoc IN CLOB)`  `RETURN NUMBER;` | Passes in the `xDoc` parameter as a `CLOB`. |
| `FUNCTION insertXML(`  `   ctxHdl IN ctxType,`  `   xDoc IN XMLType)`  `RETURN NUMBER;` | Passes in the `xDoc` parameter as an `XMLType`. |

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |
| `xDoc` | `(IN)` | String containing the XML document. |

---

### NEWCONTEXT

Creates a save context, and returns the context handle.

Syntax

```
FUNCTION newContext(
   targetTable IN VARCHAR2)
RETURN ctxType;
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `targetTable` | `(IN)` | The target table into which to load the XML document. |

---

### SETKEYCOLUMN

This method adds a column to the "key column list". The value for the column cannot be `NULL`. In case of update or delete, the columns in the key column list make up the `WHERE` clause of the statement. The key columns list must be specified before updates can complete; this is optional for delete operations

Syntax

```
PROCEDURE setKeyColumn( 
   ctxHdl IN ctxType,
   colName IN VARCHAR2);
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |
| `colName` | `(IN)` | Column to be added to the key column list; cannot be `NULL`. |

---

### SETROWTAG

Names the tag used in the XML document, to enclose the XML elements corresponding to databse records.

Syntax

```
PROCEDURE setRowTag(
   ctxHdl IN ctxType,
   tag IN VARCHAR2);
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |
| `tag` | `(IN)` | Tag name. |

---

### SETUPDATECOLUMN

Adds a column to the update column list. In case of insert, the default is to insert values to all the columns in the table; on the other hand, in case of updates, the default is to only update the columns corresponding to the tags present in the `ROW` element of the XML document. When the update column list is specified, the columns making up this list alone will get updated or inserted into.

Note that if a user passes an XML file for INSERTXML to `DBMS_XMLSTORE` which contains extra elements (ones that do not match up to any columns in the table), Oracle will try to insert into those columns unless setUpdateColumn is used. The use of setUpdateColumn is optional only if the elements in the XML file match up to the columns in the table.

Syntax

```
PROCEDURE setUpdateColumn( 
   ctxHdl IN ctxType,
   colName IN VARCHAR2);
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |
| `colName` | `(IN)` | Column to be added to the update column list. |

---

### UPDATEXML

Updates the table specified at the context creation time with data from the XML document, and returns the number of rows updated. The options are described in the following table.

| Syntax | Description |
| --- | --- |
| `FUNCTION updateXML(`  `   ctxHdl IN ctxType,`  `   xDoc IN VARCHAR2)`  `RETURN NUMBER;` | Passes in the `xDoc` parameter as a `VARCHAR2`. |
| `FUNCTION updateXML(`  `   ctxHdl IN ctxType,`  `   xDoc IN CLOB)`  `RETURN NUMBER;` | Passes in the `xDoc` parameter as a `CLOB`. |
| `FUNCTION updateXML(`  `   ctxHdl IN ctxType,`  `   xDoc IN XMLType)`  `RETURN NUMBER;` | Passes in the `xDoc` parameter as a `XMLType`. |

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |
| `xDoc` | `(IN)` | String containing the XML document. |