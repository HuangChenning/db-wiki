---
title: DBMS_XMLSAVE
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_xmlsav.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 176 DBMS\_XMLSAVE

`DBMS_XMLSAVE` provides XML to database-type functionality.

See Also:

[Oracle XML DB Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e23094/toc.htm)

This chapter contains the following topics:

- Using DBMS\_XMLSAVE
- Summary of DBMS\_XMLSAVE Subprograms

---

## Using DBMS\_XMLSAVE

---

### Security Model

Owned by `XDB`, the `DBMS_XMLSAVE` package must be created by `SYS` or `XDB`. The `EXECUTE` privilege is granted to `PUBLIC`. Subprograms in this package are executed using the privileges of the current user.

---

### Constants

Table 176-1 Constants of DBMS\_XMLSAVE

| Constant | Description |
| --- | --- |
| `DEFAULT_ROWTAG` | The default tag name for the element corresponding to database records -- ROW |
| `DEFAULT_DATE_FORMAT` | Default date mask:'MM/dd/yyyy HH:mm:ss' |
| `MATCH_CASE` | Used to specify that when mapping XML elements to database entities; the XSU should be case sensitive. |
| `IGNORE_CASE` | Used to specify that when mapping XML elements to database. entities the XSU should be case insensitive. |

---

### Types

Table 176-2 Types of DBMS\_XMLSAVE

| Type | Description |
| --- | --- |
| `ctxType` | The type of the query context handle. The type of the query context handle. This the return type of NEWCONTEXT. |

---

## Summary of DBMS\_XMLSAVE Subprograms

Table 176-3 DBMS\_XMLSAVE Package Subprograms

| Method | Description |
| --- | --- |
| CLEARKEYCOLUMNLIST | Clears the key column list. |
| CLEARUPDATECOLUMNLIST | Clears the update column list. |
| CLOSECONTEXT | It closes/deallocates a particular save context. |
| DELETEXML | Deletes records specified by data from the XML document, from the table specified at the context creation time. |
| GETEXCEPTIONCONTENT | Returns the thrown exception's error code and error message. |
| INSERTXML | Inserts the XML document into the table specified at the context creation time. |
| NEWCONTEXT | Creates a save context, and returns the context handle. |
| PROPAGATEORIGINALEXCEPTION | Tells the XSU that if an exception is raised, and is being thrown, the XSU should throw the very exception raised; rather then, wrapping it with an `OracleXMLSQLException`. |
| REMOVEXSLTPARAM | Removes the value of a top-level stylesheet parameter |
| SETBATCHSIZE | Changes the batch size used during DML operations. |
| SETCOMMITBATCH | Sets the commit batch size. |
| SETDATEFORMAT | Sets the format of the generated dates in the XML document. |
| SETIGNORECASE | The XSU does mapping of XML elements to database. |
| SETKEYCOLUMN | This methods adds a column to the key column list. |
| SETPRESERVEWHITESPACE | Tells the XSU whether to preserve whitespace or not. |
| SETROWTAG | Names the tag used in the XML document to enclose the XML elements corresponding to database. |
| SETSQLTOXMLNAMEESCAPING | This turns on or off escaping of XML tags in the case that the SQL object name, which is mapped to a XML identifier, is not a valid XML identifier. |
| SETUPDATECOLUMN | Adds a column to the update column list. |
| SETXSLT | Registers a XSL transform to be applied to the XML to be saved. |
| SETXSLTPARAM | Sets the value of a top-level stylesheet parameter. |
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

Deletes records specified by data from the XML document from the table specified at the context creation time, and returns the number of rows deleted. The options are described in the following table.

| Syntax | Description |
| --- | --- |
| `FUNCTION deleteXML(`  `   ctxHdl IN ctxPType,`  `   xDoc IN VARCHAR2)`  `RETURN NUMBER;` | Uses a `VARCHAR2` type for the `xDoc` parameter. |
| `FUNCTION deleteXML(`  `   ctxHdl IN ctxType,`  `   xDoc IN CLOB)`  `RETURN NUMBER;` | Uses a `CLOB` type for the `xDoc` parameter. |

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |
| `xDoc` | `(IN)` | String containing the XML document. |

---

### GETEXCEPTIONCONTENT

Through its arguments, this method returns the thrown exception's error code and error message, SQL error code. This is to get around the fact that the JVM throws an exception on top of whatever exception was raised; thus, rendering PL/SQL unable to access the original exception.

Syntax

```
PROCEDURE getExceptionContent(
   ctxHdl IN ctxType,
   errNo OUT NUMBER,
   errMsg OUT VARCHAR2);
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |
| `errNo` | `(IN)` | Error number. |
| `errMsg` | `(IN)` | Error message. |

---

### INSERTXML

Inserts the XML document into the table specified at the context creation time, and returns the number of rows inserted. The options are described in the following table.

| Syntax | Description |
| --- | --- |
| `FUNCTION insertXML(`  `   ctxHdl IN ctxType,`  `   xDoc IN VARCHAR2)`  `RETURN NUMBER;` | Passes in the `xDoc` parameter as a `VARCHAR2`. |
| `FUNCTION insertXML(`  `   ctxHdl IN ctxType,`  `   xDoc IN CLOB)`  `RETURN NUMBER;` | Passes in the `xDoc` parameter as a `CLOB`. |

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

### PROPAGATEORIGINALEXCEPTION

Tells the XSU that if an exception is raised, and is being thrown, the XSU should throw the very exception raised; rather then, wrapping it with an `OracleXMLSQLException`.

Syntax

```
PROCEDURE propagateOriginalException(
   ctxHdl IN ctxType,
   flag IN BOOLEAN);
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |
| `flag` | `(IN)` | Propagate the original exception? 0= `FALSE`, 1= `TRUE`. |

---

### REMOVEXSLTPARAM

Removes the value of a top-level stylesheet parameter.

Syntax

```
PROCEDURE removeXSLTParam(
   ctxHdl IN ctxType, 
   name IN VARCHAR2);
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |
| `name` | `(IN)` | Parameter name. |

---

### SETBATCHSIZE

Changes the batch size used during DML operations. When performing inserts, updates or deletes, it is better to batch the operations so that they get executed in one shot rather than as separate statements. The flip side is that more memory is needed to buffer all the bind values. Note that when batching is used, a commit occurs only after a batch is executed. So if one of the statement inside a batch fails, the whole batch is rolled back. This is a small price to pay considering the performance gain; nevertheless, if this behavior is unacceptable, then set the batch size to 1.

Syntax

```
PROCEDURE setBatchSize(
   ctxHdl IN ctxType,
   batchSize IN NUMBER);
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |
| `batchSize` | `(IN)` | Batch size. |

---

### SETCOMMITBATCH

Sets the commit batch size. The commit batch size refers to the number or records inserted after which a commit should follow. If `batchSize` is less than `1` or the session is in "auto-commit" mode, using the XSU does not make any explicit commits. By default, `commitBatch` is `0`.

Syntax

```
PROCEDURE setCommitBatch(
   ctxHdl IN ctxType,
   batchSize IN NUMBER);
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |
| `batchSize` | `(IN)` | Commit batch size. |

---

### SETDATEFORMAT

Sets the format of the generated dates in the XML document. The syntax of the date format patern, the date mask, should conform to the requirements of the class `java.text.SimpleDateFormat`. Setting the mask to `<code>null</code>` or an empty string unsets the date mask.

Syntax

```
PROCEDURE setDateFormat(
   ctxHdl IN ctxType,
   mask IN VARCHAR2);
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |
| `mask` | `(IN)` | Syntax of the date format pattern.. |

---

### SETIGNORECASE

The XSU does mapping of XML elements to db columns/attributes based on the element names (XML tags). This function tells the XSU to do this match case insensitive.

Syntax

```
PROCEDURE setIgnoreCase(
   ctxHdl IN ctxType,
   flag IN NUMBER);
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |
| `flag` | `(IN)` | Ignore tag case in the XML doc? 0= `FALSE`, 1= `TRUE`. |

---

### SETKEYCOLUMN

This method adds a column to the "key column list". The value for the column cannot be `NULL`. In case of update or delete, the columns in the key column list make up the `WHERE` clause of the statement. The key columns list must be specified before updates can complete; this is optional for delete operations.

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

### SETPRESERVEWHITESPACE

Tells the XSU whether or not to preserve whitespace.

Syntax

```
PROCEDURE setPreserveWhitespace(
   ctxHdl IN ctxType,
   flag IN BOOLEAN := true);
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |
| `flag` | `(IN)` | Should XSU preserve whitespace? |

---

### SETROWTAG

Names the tag used in the XML document to enclose the XML elements corresponding to db. records.

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

### SETSQLTOXMLNAMEESCAPING

Turns on or off escaping of XML tags in the case that the SQL object name, which is mapped to a XML identifier, is not a valid XML identifier.

Syntax

```
PROCEDURE setSQLToXMLNameEscaping(
   ctxHdl IN ctxType,
   flag IN BOOLEAN := true);
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |
| `flag` | `(IN)` | Turn on escaping? |

---

### SETUPDATECOLUMN

Adds a column to the update column list. In case of insert, the default is to insert values to all the columns in the table; on the other hand, in case of updates, the default is to only update the columns corresponding to the tags present in the ROW element of the XML document. When the update column list is specified, the columns making up this list alone will get updated or inserted into.

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

### SETXSLT

Registers an XSL transform to be applied to the XML to be saved. If a stylesheet was already registered, it gets replaced by the new one. To un-register the stylesheet, pass in null for the URI. The options are described in the following table.

| Syntax | Description |
| --- | --- |
| `PROCEDURE setXSLT(`  `   ctxHdl IN ctxType,`  `   uri IN VARCHAR2,`  `   ref IN VARCHAR2 := null);` | Passes in the stylesheet through a URI. |
| `PROCEDURE setXSLT(`  `   ctxHdl IN ctxType,`  `   stylesheet IN CLOB,`  `   ref IN VARCHAR2 := null);` | Passes in the stylesheet through a `CLOB`. |

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |
| `uri` | `(IN)` | URI to the stylesheet to register. |
| `ref` | `(IN)` | URL for include, import, and external entities. |
| `stylesheet` | `(IN)` | `CLOB` containing the stylesheet to register. |

---

### SETXSLTPARAM

Sets the value of a top-level stylesheet parameter. The parameter is expected to be a valid XPath expression; literal values would therefore have to be explicitly quoted.

Syntax

```
PROCEDURE setXSLTParam(
   ctxHdl IN ctxType,
   name IN VARCHAR2,
   value IN VARCHAR2);
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |
| `name` | `(IN)` | Parameter name. |
| `value` | `(IN)` | Parameter value as an XPath expression |

---

### UPDATEXML

Updates the table specified at the context creation time with data from the XML document, and returns the number of rows updated. The options are described in the following table.

| Syntax | Description |
| --- | --- |
| `FUNCTION updateXML(`  `   ctxHdl IN ctxType,`  `   xDoc IN VARCHAR2)`  `RETURN NUMBER;` | Passes in the `xDoc` parameter as a `VARCHAR2`. |
| `FUNCTION updateXML(`  `   ctxHdl IN ctxType,`  `   xDoc IN CLOB)`  `RETURN NUMBER;` | Passes in the `xDoc` parameter as a `CLOB`. |

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |
| `xDoc` | `(IN)` | String containing the XML document. |