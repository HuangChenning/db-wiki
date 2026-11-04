---
title: DBMS_XMLSAVE
book: PL/SQL Packages and Types Reference
doc_id: E96430-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/DBMS_XMLSAVE.html
tags:
  - oracle
  - 19c
  - pl-sql-packages-and-types-reference
---

**Note:**

With Oracle Database 18.1 Release, the `DBMS_XMLSAVE` package is deprecated. Use `DBMS_XMLSTORE` instead.

The `DBMS_XMLSAVE` package has been replaced with improved technology. While Oracle recommends you not to begin development using `DBMS_XMLSAVE`, Oracle continues to support this package for reasons of backward compatibility. Your existing applications using `DBMS_XMLSAVE` will continue to work.

This chapter contains the following topics:

**See Also:**

For more information on `DBMS_XMLSTORE`, see [DBMS\_XMLSTORE](DBMS_XMLSTORE.md)

[*Oracle XML DB Developer’s Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=ADXDB-GUID-8611495B-A091-4B11-9E65-E8AD20D50D97)

### DBMS\_XMLSAVE Security Model

Owned by `XDB`, the `DBMS_XMLSAVE` package must be created by `SYS` or `XDB`. The `EXECUTE` privilege is granted to `PUBLIC`

Subprograms in this package are executed using the privileges of the current user.

### DBMS\_XMLSAVE Constants

The DBMS\_XMLSAVE includes constants to use when specifying parameter values.

These constants are defined in the following table.

Table 1 Constants of DBMS\_XMLSAVE

| Constant | Description |
| --- | --- |
| `DEFAULT_ROWTAG` | The default tag name for the element corresponding to database records – ROW |
| `DEFAULT_DATE_FORMAT` | Default date mask:’MM/dd/yyyy HH:mm:ss’ |
| `MATCH_CASE` | Used to specify that when mapping XML elements to database entities; the XSU should be case sensitive. |
| `IGNORE_CASE` | Used to specify that when mapping XML elements to database. entities the XSU should be case insensitive. |

### Types

The `DBMS_XMLSAVE` subprograms use the `ctxType` Type.

Table 2 *Types of DBMS\_XMLSAVE*

| Type | Description |
| --- | --- |
| `ctxType` | The type of the query context handle. The type of the query context handle. This the return type of NEWCONTEXT. |

### Summary of DBMS\_XMLSAVE Subprograms

This table lists the `DBMS_XMLSAVE` subprograms and briefly describes them.

Table 3 DBMS\_XMLSAVE Package Subprograms

| Method | Description |
| --- | --- |
| CLEARKEYCOLUMNLIST | Clears the key column list. |
| CLEARUPDATECOLUMNLIST | Clears the update column list. |
| CLOSECONTEXT | It closes/deallocates a particular save context. |
| DELETEXML | Deletes records specified by data from the XML document, from the table specified at the context creation time. |
| GETEXCEPTIONCONTENT | Returns the thrown exception’s error code and error message. |
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

### CLEARKEYCOLUMNLIST

This procedure clears the key column list.

**Syntax**

```md
PROCEDURE clearKeyColumnList(
   ctxHdl IN ctxType);
```

**Parameters**

Table 4 CLEARKEYCOLUMNLIST Procedure Parameters

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |

### CLEARUPDATECOLUMNLIST

This procedure clears the update column list.

**Syntax**

```md
PROCEDURE clearUpdateColumnList(
   ctxHdl IN ctxType);
```

**Parameters**

Table 5 CLEARUPDATECOLUMNLIST Procedure Parameters

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |

### CLOSECONTEXT

This procedure closes/deallocates a particular save context.

**Syntax**

```md
PROCEDURE closeContext(
   ctxHdl IN ctxType);
```

**Parameters**

Table 6 CLOSECONTEXT Procedure Parameters

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |

### DELETEXML

The `DELETEXML` function deletes records specified by data from the XML document from the table specified at the context creation time, and returns the number of rows deleted.

**Syntax**

The options are described in the following table.

```md
FUNCTION deleteXML(
  ctxHdl IN ctxPType,
    xDoc IN VARCHAR2)
RETURN NUMBER;
```
```md
FUNCTION deleteXML(
  ctxHdl IN ctxType,
  xDoc IN CLOB)
RETURN NUMBER;
```

**Paramters**

Table 7 DELETEXML Function Parameters

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |
| `xDoc` | `(IN)` | String containing the XML document. |

### GETEXCEPTIONCONTENT

Through its arguments, this method returns the thrown exception’s error code and error message, SQL error code.

This is to get around the fact that the JVM throws an exception on top of whatever exception was raised, rendering PL/SQL unable to access the original exception.

**Syntax**

```md
PROCEDURE getExceptionContent(
   ctxHdl IN ctxType,
   errNo OUT NUMBER,
   errMsg OUT VARCHAR2);
```

**Parameters**

Table 8 GETEXCEPTIONCONTENT Procedure Parameters

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |
| `errNo` | `(IN)` | Error number. |
| `errMsg` | `(IN)` | Error message. |

### INSERTXML

Inserts the XML document into the table specified at the context creation time, and returns the number of rows inserted. The options are described in the following table.

**Syntax**

Table 9 INSERTXML Function Syntax

| Syntax | Description |
| --- | --- |
| ```md FUNCTION insertXML( ctxHdl IN ctxType, xDoc IN VARCHAR2) RETURN NUMBER; ``` | Passes in the `xDoc` parameter as a `VARCHAR2`. |
| ```md FUNCTION insertXML( ctxHdl IN ctxType, xDoc IN CLOB) RETURN NUMBER; ``` | Passes in the `xDoc` parameter as a `CLOB`. |

**Parameters**

Table 10 INSERTXML Function Parameters

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |
| `xDoc` | `(IN)` | String containing the XML document. |

### NEWCONTEXT

`NEWCONTEXT` creates a save context and returns the context handle.

**Syntax**

```md
FUNCTION newContext(
   targetTable IN VARCHAR2)
RETURN ctxType;
```

**Parameters**

Table 11 NEWCONTEXT Function Parameters

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `targetTable` | `(IN)` | The target table into which to load the XML document. |

### PROPAGATEORIGINALEXCEPTION

The `PROPAGATEORIGINALEXCEPTION` procedure tells the XSU that if an exception is raised, and is being thrown, the XSU should throw the very exception raised; rather then, wrapping it with an `OracleXMLSQLException`.

**Syntax**

```md
PROCEDURE propagateOriginalException(
   ctxHdl IN ctxType,
   flag IN BOOLEAN);
```

**Parameters**

Table 12 PROPAGATEORIGINALEXCEPTION Procedure Parameters

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |
| `flag` | `(IN)` | Propagate the original exception? 0= `FALSE`, 1= `TRUE`. |

### REMOVEXSLTPARAM

This procedure removes the value of a top-level stylesheet parameter.

**Syntax**

```md
PROCEDURE removeXSLTParam(
   ctxHdl IN ctxType,
   name IN VARCHAR2);
```

**Parameters**

Table 13 REMOVEXSLTPARAM Procedure Parameters

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |
| `name` | `(IN)` | Parameter name. |

### SETBATCHSIZE

This procedure changes the batch size used during DML operations.

When performing inserts, updates or deletes, it is better to batch the operations so that they get executed in one shot rather than as separate statements. The flip side is that more memory is needed to buffer all the bind values. Note that when batching is used, a commit occurs only after a batch is executed. So if one of the statement inside a batch fails, the whole batch is rolled back. This is a small price to pay considering the performance gain; nevertheless, if this behavior is unacceptable, then set the batch size to 1.

**Syntax**

```md
PROCEDURE setBatchSize(
   ctxHdl IN ctxType,
   batchSize IN NUMBER);
```

**Parameters**

Table 14 SETBATCHSIZE Procedure Parameters

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |
| `batchSize` | `(IN)` | Batch size. |

### SETCOMMITBATCH

This procedure sets the commit batch size.

The commit batch size refers to the number or records inserted after which a commit should follow. If `batchSize` is less than `1` or the session is in “auto-commit” mode, using the XSU does not make any explicit commits. By default, `commitBatch` is `0`.

**Syntax**

```md
PROCEDURE setCommitBatch(
   ctxHdl IN ctxType,
   batchSize IN NUMBER);
```

**Parameters**

Table 15 SETCOMMITBATCH Procedure Parameters

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |
| `batchSize` | `(IN)` | Commit batch size. |

### SETDATEFORMAT

This procedure sets the format of the generated dates in the XML document.

The syntax of the date format pattern, the date mask, should conform to the requirements of the class `java.text.SimpleDateFormat`. Setting the mask to `<code>null</code>` or an empty string unsets the date mask.

**Syntax**

```md
PROCEDURE setDateFormat(
   ctxHdl IN ctxType,
   mask IN VARCHAR2);
```

**Parameters**

Table 16 SETDATEFORMAT Procedure Parameters

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |
| `mask` | `(IN)` | Syntax of the date format pattern. |

### SETIGNORECASE

This function tells the XSU whether to ignore case when the XSU maps XML elements to database columns/attributes. This matching is based on the element names (XML tags).

**Syntax**

```md
PROCEDURE setIgnoreCase(
   ctxHdl IN ctxType,
   flag IN NUMBER);
```

**Parameters**

Table 17 SETIGNORECASE Procedure Parameters

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |
| `flag` | `(IN)` | Ignore tag case in the XML doc? 0= `FALSE`, 1= `TRUE`. |

### SETKEYCOLUMN

This method adds a column to the “key column list”.

The value for the column cannot be `NULL`. In case of update or delete, the columns in the key column list make up the `WHERE` clause of the statement. The key columns list must be specified before updates can complete; this is optional for delete operations.

**Syntax**

```md
PROCEDURE setKeyColumn(
   ctxHdl IN ctxType,
   colName IN VARCHAR2);
```

**Parameters**

Table 18 SETKEYCOLUMN Procedure Parameters

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |
| `colName` | `(IN)` | Column to be added to the key column list; cannot be `NULL`. |

### SETPRESERVEWHITESPACE

This procedure tells the XSU whether or not to preserve whitespace.

**Syntax**

```md
PROCEDURE setPreserveWhitespace(
   ctxHdl IN ctxType,
   flag IN BOOLEAN := true);
```

**Parameters**

Table 19 SETPRESERVEWHITESPACE Procedure Parameters

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |
| `flag` | `(IN)` | Should XSU preserve whitespace? |

### SETROWTAG

This procedure names the tag used in the XML document to enclose the XML elements corresponding to db. records.

**Syntax**

```md
PROCEDURE setRowTag(
   ctxHdl IN ctxType,
   tag IN VARCHAR2);
```

**Parameters**

Table 20 SETROWTAG Procedure Parameters

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |
| `tag` | `(IN)` | Tag name. |

### SETSQLTOXMLNAMEESCAPING

`SETSQLTOXMLNAMEESCAPING` turns on or off escaping of XML tags in the case that the SQL object name, which is mapped to a XML identifier, is not a valid XML identifier.

**Syntax**

```md
PROCEDURE setSQLToXMLNameEscaping(
   ctxHdl IN ctxType,
   flag IN BOOLEAN := true);
```

**Parameters**

Table 21 SETSQLTOXMLNAMEESCAPING Procedure Parameters

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |
| `flag` | `(IN)` | Turn on escaping? |

### SETUPDATECOLUMN

`SETUPDATECOLUMN` adds a column to the update column list.

In case of insert, the default is to insert values to all the columns in the table. In case of updates, the default is to only update the columns corresponding to the tags present in the ROW element of the XML document. When the update column list is specified, the columns making up this list alone will get updated or inserted into.

**Syntax**

```md
PROCEDURE setUpdateColumn(
   ctxHdl IN ctxType,
   colName IN VARCHAR2);
```

**Parameters**

Table 22 SETUPDATECOLUMN Procedure Parameters

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |
| `colName` | `(IN)` | Column to be added to the update column list. |

### SETXSLT

`SETXSLT` registers an XSL transform to be applied to the XML to be saved.

If a stylesheet was already registered, it gets replaced by the new one. To un-register the stylesheet, pass in null for the URI. The options are described in the following table.

**Syntax**

Table 23 SETXSLT Procedure Syntax

| Syntax | Description |
| --- | --- |
| ```md PROCEDURE setXSLT( ctxHdl IN ctxType, uri IN VARCHAR2, ref IN VARCHAR2 := null); ``` | Passes in the stylesheet through a URI. |
| ```md PROCEDURE setXSLT( ctxHdl IN ctxType, stylesheet IN CLOB, ref IN VARCHAR2 := null); ``` | Passes in the stylesheet through a `CLOB`. |

**Parameters**

Table 24 SETXSLT Procedure Parameters

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |
| `uri` | `(IN)` | URI to the stylesheet to register. |
| `ref` | `(IN)` | URL for include, import, and external entities. |
| `stylesheet` | `(IN)` | `CLOB` containing the stylesheet to register. |

### SETXSLTPARAM

`SETXSLTPARAM` sets the value of a top-level stylesheet parameter.

The parameter is expected to be a valid XPath expression; literal values would therefore have to be explicitly quoted.

**Syntax**

```md
PROCEDURE setXSLTParam(
   ctxHdl IN ctxType,
   name IN VARCHAR2,
   value IN VARCHAR2);
```

**Parameters**

Table 25 SETXSLTPARAM Procedure Parameters

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |
| `name` | `(IN)` | Parameter name. |
| `value` | `(IN)` | Parameter value as an XPath expression |

### UPDATEXML

Updates the table specified at the context creation time with data from the XML document, and returns the number of rows updated.

The options are described in the following table.

**Syntax**

```md
FUNCTION updateXML(
  ctxHdl IN ctxType,
  xDoc IN VARCHAR2)
RETURN NUMBER;
```
```md
FUNCTION updateXML(
  ctxHdl IN ctxType,
  xDoc IN CLOB)
RETURN NUMBER;
```

**Parameters**

Table 26 UPDATEXML Function Parameters

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |
| `xDoc` | `(IN)` | String containing the XML document. |