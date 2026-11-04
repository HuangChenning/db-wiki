---
title: DBMS_XMLQUERY
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_xmlque.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 175 DBMS\_XMLQUERY

`DBMS_XMLQUERY` provides database-to- `XMLType` functionality. Whenever possible, use `DBMS_XMLGEN`, a built-in package in C, instead of `DBMS_XMLQUERY`.

See Also:

[Oracle XML DB Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e23094/toc.htm)

This chapter contains the following topics:

- Using DBMS\_XMLQUERY
- Summary of DBMS\_XMLQUERY Subprograms

---

## Using DBMS\_XMLQUERY

- Security Model
- Constants
- Types

---

### Security Model

Owned by `XDB`, the `DBMS_XMLQUERY` package must be created by `SYS` or `XDB`. The `EXECUTE` privilege is granted to `PUBLIC`. Subprograms in this package are executed using the privileges of the current user.

---

### Constants

Table 175-1 Constants of DBMS\_XMLQUERY

| Constant | Description |
| --- | --- |
| `DB_ENCODING` | Used to signal that the DB character encoding is to be used. |
| `DEFAULT_ROWSETTAG` | The tag name for the element enclosing the XML generated from the result set (that is, for most cases the root node tag name) -- `ROWSET`. |
| `DEFAULT_ERRORTAG` | The default tag to enclose raised errors -- `ERROR`. |
| `DEFAULT_ROWIDATTR` | The default name for the cardinality attribute of XML elements corresponding to `db.records` -- `NUM` |
| `DEFAULT_ROWTAG` | The default tag name for the element corresponding to `db. records` -- `ROW` |
| `DEFAULT_DATE_FORMAT` | Default date mask `--'MM/dd/yyyy HH:mm:ss'` |
| `ALL_ROWS` | Indicates that all rows are needed in the output. |
| `NONE` | Used to specifies that the output should not contain any XML metadata (for example, no DTD). |
| `DTD` | Used to specify that the generation of the DTD is desired. |
| `SCHEMA` | Used to specify that the generation of the XML Schema is desired. |
| `LOWER_CASE` | Use lower case tag names. |
| `UPPER_CASE` | Use upper case tag names. |

---

### Types

Table 175-2 Types of DBMS\_XMLQUERY

| Type | Description |
| --- | --- |
| `ctxType` | The type of the query context handle. This is the return type of NEWCONTEXT |

---

## Summary of DBMS\_XMLQUERY Subprograms

Table 175-3 DBMS\_XMLQUERY Package Subprograms

| Method | Description |
| --- | --- |
| CLOSECONTEXT | Closes or deallocates a particular query context. |
| GETDTD | Generates the DTD. |
| GETEXCEPTIONCONTENT | Returns the thrown exception's error code and error message. |
| GETNUMROWSPROCESSED | Returns the number of rows processed for the query. |
| GETVERSION | Prints the version of the XSU in use. |
| GETXML | Generates the XML document. |
| NEWCONTEXT | Creates a query context and it returns the context handle. |
| PROPAGATEORIGINALEXCEPTION | Tells the XSU that if an exception is raised, and is being thrown, the XSU should throw the very exception raised; rather then, wrapping it with an `OracleXMLSQLException`. |
| REMOVEXSLTPARAM | Removes a particular top-level stylesheet parameter. |
| SETBINDVALUE | Sets a value for a particular bind name. |
| SETCOLLIDATTRNAME | Sets the name of the id attribute of the collection element's separator tag. |
| SETDATAHEADER | Sets the XML data header. |
| SETDATEFORMAT | Sets the format of the generated dates in the XML document. |
| SETENCODINGTAG | Sets the encoding processing instruction in the XML document. |
| SETERRORTAG | Sets the tag to be used to enclose the XML error documents. |
| SETMAXROWS | Sets the maximum number of rows to be converted to XML. |
| SETMETAHEADER | Sets the XML meta header. |
| SETRAISEEXCEPTION | Tells the XSU to throw the raised exceptions. |
| SETRAISENOROWSEXCEPTION | Tells the XSU to throw or not to throw an `OracleXMLNoRowsException` in the case when for one reason or another, the XML document generated is empty. |
| SETROWIDATTRNAME | Sets the name of the id attribute of the row enclosing tag. |
| SETROWIDATTRVALUE | Specifies the scalar column whose value is to be assigned to the id attribute of the row enclosing tag. |
| SETROWSETTAG | Sets the tag to be used to enclose the XML dataset. |
| SETROWTAG | Sets the tag to be used to enclose the XML element. |
| SETSKIPROWS | Sets the number of rows to skip. |
| SETSQLTOXMLNAMEESCAPING | This turns on or off escaping of XML tags in the case that the SQL object name, which is mapped to a XML identifier, is not a valid XML identifier. |
| SETSTYLESHEETHEADER | Sets the stylesheet header. |
| SETTAGCASE | Specified the case of the generated XML tags. |
| SETXSLT | Registers a stylesheet to be applied to generated XML. |
| SETXSLTPARAM | Sets the value of a top-level stylesheet parameter. |
| USENULLATTRIBUTEINDICATOR | Specifies weather to use an XML attribute to indicate `NULL` ness. |
| USETYPEFORCOLLELEMTAG | Tells the XSU to use the collection element's type name as the collection element tag name. |

---

### CLOSECONTEXT

Closes or deallocates a particular query context

Syntax

```
PROCEDURE CLOSECONTEXT(
ctxHdl IN ctxType);
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |

---

### GETDTD

Generates and returns the DTD based on the SQL query used to initialize the context. The options are described in the following table.

| Syntax | Description |
| --- | --- |
| `FUNCTION GETDTD(`  `   ctxHdl IN ctxType,`  `   withVer IN BOOLEAN := false)`  `RETURN CLOB;` | Function that generates the DTD based on the SQL query used to initialize the context. |
| `PROCEDURE GETDTD(`  `   ctxHdl IN ctxType,`  `   xDoc IN CLOB,`  `   withVer IN BOOLEAN := false);` | Procedure that generates the DTD based on the SQL query used to initialize the context; specifies the output `CLOB` for XML document result. |

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |
| `withVer` | `(IN)` | Generate the version information? `TRUE` for yes`.` |
| `xDoc` | `(IN)` | `CLOB` into which to write the generated XML document. |

---

### GETEXCEPTIONCONTENT

Returns the thrown exception's SQL error code and error message through the procedure's `OUT` parameters. This procedure is a work around the JVM functionality that obscures the original exception by its own exception, rendering PL/SQL unable to access the original exception content.

Syntax

```
PROCEDURE GETEXCEPTIONCONTENT(
ctxHdl IN ctxType,
errNo OUT NUMBER,
errMsg OUT VARCHAR2);
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |
| `errNo` | `(OUT)` | Error number. |
| `errMsg` | `(OUT)` | Error message. |

---

### GETNUMROWSPROCESSED

Return the number of rows processed for the query.

Syntax

```
FUNCTION GETNUMROWSPROCESSED(
ctxHdl IN ctxType)
RETURN NUMBER;
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |

---

### GETVERSION

Prints the version of the XSU in use.

Syntax

```
PROCEDURE GETVERSION();
```

---

### GETXML

Creates the new context, executes the query, gets the XML back and closes the context. This is a convenience function. The context doesn't have to be explicitly opened or closed. The options are described in the following table.

| Syntax | Description |
| --- | --- |
| `FUNCTION GETXML(`  `   sqlQuery IN VARCHAR2,`  `   metaType IN NUMBER := NONE)`  `RETURN CLOB;` | This function uses a SQL query in string form. |
| `FUNCTION GETXML(`  `   sqlQuery IN CLOB,`  `   metaType IN NUMBER := NONE)`  `RETURN CLOB;` | This function uses a SQL query in `CLOB` form. |
| `FUNCTION GETXML(`  `   ctxHdl IN ctxType,`  `   metaType IN NUMBER := NONE)`  `RETURN CLOB;` | This function generates the XML document based on a SQL query used to initialize the context. |
| `PROCEDURE GETXML(`  `   ctxHdl IN ctxType,`  `   xDoc IN CLOB,`  `   metaType IN NUMBER := NONE);` | This procedure generates the XML document based on the SQL query used to initialize the context. |

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |
| `metaType` | `(IN)` | XML metadata type (`NONE`, `DTD`, or `SCHEMA`). |
| `sqlQuery` | `(IN)` | SQL query. |
| `xDoc` | `(IN)` | `CLOB` into which to write the generated XML document. |

---

### NEWCONTEXT

Creates a query context and it returns the context handle. The options are described in the following table.

| Syntax | Description |
| --- | --- |
| `FUNCTION NEWCONTEXT(`  `   sqlQuery IN VARCHAR2)`  `RETURN ctxType;` | Creates a query context from a string. |
| `FUNCTION NEWCONTEXT(`  `   sqlQuery IN CLOB)`  `RETURN ctxType;` | Creates a query context from a `CLOB`. |

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `sqlQuery` | `(IN)` | SQL query, the results of which to convert to XML. |

---

### PROPAGATEORIGINALEXCEPTION

Specifies whether to throw every original exception raised or to wrap it in an `OracleXMLSQLException`.

Syntax

```
PROCEDURE PROPAGATEORIGINALEXCEPTION(
ctxHdl IN ctxType,
flag IN BOOLEAN);
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |
| `flag` | `(IN)` | `TRUE` if want to propagate original exception, `FALSE` to wrap in `OracleXMLException.` |

---

### REMOVEXSLTPARAM

Removes the value of a top-level stylesheet parameter. If no stylesheet is registered, this method is not operational.

Syntax

```
PROCEDURE REMOVEXSLTPARAM(
ctxHdl IN ctxType,
name IN VARCHAR2);
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |
| `name` | `(IN)` | Name of the top level stylesheet parameter. |

---

### SETBINDVALUE

Sets a value for a particular bind name.

Syntax

```
PROCEDURE SETBINDVALUE(
ctxHdl IN ctxType,
bindName IN VARCHAR2,
bindValue IN VARCHAR2);
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |
| `bindName` | `(IN)` | Bind name. |
| `bindValue` | `(IN)` | Bind value. |

---

### SETCOLLIDATTRNAME

Sets the name of the id attribute of the collection element's separator tag. Passing `NULL` or an empty string for the tag causes the row id attribute to be omitted.

Syntax

```
PROCEDURE SETCOLLIDATTRNAME(
ctxHdl IN ctxType,
attrName IN VARCHAR2);
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |
| `attrName` | `(IN)` | Attribute name. |

---

### SETDATAHEADER

Sets the XML data header. The data header is an XML entity that is appended at the beginning of the query-generated XML entity, the `rowset`. The two entities are enclosed by the `docTag` argument. The last data header specified is used. Passing in `NULL` for the `header` parameter unsets the data header.

Syntax

```
PROCEDURE SETDATAHEADER(
ctxHdl IN ctxType,
header IN CLOB := null,
tag IN VARCHAR2 := null);
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |
| `header` | `(IN)` | Header. |
| `tag` | `(IN)` | Tag used to enclose the data header and the rowset. |

---

### SETDATEFORMAT

Sets the format of the generated dates in the XML document. The syntax of the date format pattern, the date mask, should conform to the requirements of the `java.text.SimpleDateFormat` class. Setting the mask to `NULL` or an empty string sets the default mask -- `DEFAULT_DATE_FORMAT`.

Syntax

```
PROCEDURE SETDATEFORMAT(
ctxHdl IN ctxType,
mask IN VARCHAR2);
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |
| `mask` | `(IN)` | The date mask. |

---

### SETENCODINGTAG

Sets the encoding processing instruction in the XML document.

Syntax

```
PROCEDURE SETENCODINGTAG(
ctxHdl IN ctxType,
enc IN VARCHAR2 := DB_ENCODING);
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |
| `enc` | `(IN)` | The encoding to use. |

---

### SETERRORTAG

Sets the tag to be used to enclose the XML error documents.

Syntax

```
PROCEDURE SETERRORTAG(
ctxHdl IN ctxType,
tag IN VARCHAR2);
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |
| `tag` | `(IN)` | Tag name. |

---

### SETMAXROWS

Sets the maximum number of rows to be converted to XML. By default, there is no set maximum.

Syntax

```
PROCEDURE SETMAXROWS (
ctxHdl IN ctxType,
rows IN NUMBER);
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |
| `rows` | `(IN)` | Maximum number of rows to generate. |

---

### SETMETAHEADER

Sets the XML meta header. When set, the header is inserted at the beginning of the metadata part (DTD or XMLSchema) of each XML document generated by this object. The last meta header specified is used. Passing in `NULL` for the `header` parameter unsets the meta header.

Syntax

```
PROCEDURE SETMETAHEADER(
ctxHdl IN ctxType, 
header IN CLOB := null);
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |
| `Header` | `(IN)` | Header. |

---

### SETRAISEEXCEPTION

Specifies whether to throw raised exceptions. If this call isn't made or if `FALSE` is passed to the `flag` argument, the XSU catches the SQL exceptions and generates an XML document from the exception message.

Syntax

```
PROCEDURE SETRAISEEXCEPTION(
ctxHdl IN ctxType,
flag IN BOOLEAN:=true);
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |
| `flag` | `(IN)` | Throw raised exceptions? `TRUE` for yes, otherwise `FALSE.` |

---

### SETRAISENOROWSEXCEPTION

Specifies whether to throw an `OracleXMLNoRowsException` when the generated XML document is empty. By default, the exception is not thrown.

Syntax

```
PROCEDURE SETRAISENOROWSEXCEPTION(
ctxHdl IN ctxType,
flag IN BOOLEAN:=false);
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |
| `flag` | `(IN)` | Throws an `OracleXMLNoRowsException` if set to `TRUE`. |

---

### SETROWIDATTRNAME

Sets the name of the id attribute of the row enclosing tag. Passing `NULL` or an empty string for the tag causes the row id attribute to be omitted.

Syntax

```
PROCEDURE SETROWIDATTRNAME(
ctxHdl IN ctxType,
attrName IN VARCHAR2);
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |
| `attrName` | `(IN)` | Attribute name. |

---

### SETROWIDATTRVALUE

Specifies the scalar column whose value is to be assigned to the id attribute of the row enclosing tag. Passing `NULL` or an empty string for the `colName` assigns the row count value (0, 1, 2 and so on) to the row id attribute.

Syntax

```
PROCEDURE SETROWIDATTRVALUE(
ctxHdl IN ctxType,
colName IN VARCHAR2);
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |
| `colName` | `(IN)` | Column whose value is to be assigned to the row id attribute. |

---

### SETROWSETTAG

Sets the tag to be used to enclose the XML dataset.

Syntax

```
PROCEDURE SETROWSETTAG(
ctxHdl IN ctxType,
tag IN VARCHAR2);
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |
| `tag` | `(IN)` | Tag name. |

---

### SETROWTAG

Sets the tag to be used to enclose the XML element corresponding to a `db.record`.

Syntax

```
PROCEDURE SETROWTAG(
ctxHdl IN ctxType,
tag IN VARCHAR2);
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |
| `tag` | `(IN)` | Tag name. |

---

### SETSKIPROWS

Sets the number of rows to skip. By default, 0 rows are skipped.

Syntax

```
PROCEDURE SETSKIPROWS(
ctxHdl IN ctxType,
rows IN NUMBER);
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |
| `rows` | `(IN)` | Maximum number of rows to skip. |

---

### SETSQLTOXMLNAMEESCAPING

This turns on or off escaping of XML tags in the case that the SQL object name, which is mapped to a XML identifier, is not a valid XML identifier.

Syntax

```
PROCEDURE SETSQLTOXMLNAMEESCAPING(
ctxHdl IN ctxType,
flag IN BOOLEAN := true);
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |
| `flag` | `(IN)` | Turn on escaping? `TRUE` for yes, otherwise `FALSE.` |

---

### SETSTYLESHEETHEADER

Sets the stylesheet header (the stylesheet processing instructions) in the generated XML document. Passing `NULL` for the `uri` argument will unset the stylesheet header and the stylesheet type.

Syntax

```
PROCEDURE SETSTYLESHEETHEADER(
ctxHdl IN ctxType,
uri IN VARCHAR2,
type IN VARCHAR2 := 'text/xsl');
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |
| `uri` | `(IN)` | Stylesheet URI. |
| `type` | `(IN)` | Stylesheet type; defaults to " `text/xsl` ". |

---

### SETTAGCASE

Specifies the case of the generated XML tags.

Syntax

```
PROCEDURE SETTAGCASE(
ctxHdl IN ctxType,
tCase IN NUMBER);
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |
| `tCase` | `(IN)` | The tag's case: - 0 for as are - 1 for lower case - 2 for upper case |

---

### SETXSLT

Registers a stylesheet to be applied to generated XML. If a stylesheet was already registered, it is replaced by the new one. The options are described in the following table. Passing `NULL` for the `uri` argument or an empty string for the `stylesheet` argument will unset the stylesheet header and type.

| Syntax | Description |
| --- | --- |
| `PROCEDURE SETXSLT(`  `   ctxHdl IN ctxType,`  `   uri IN VARCHAR2,`  `   ref IN VARCHAR2 := null);` | To un-register the stylesheet pass in a null for the uri. |
| `PROCEDURE SETXSLT(`  `   ctxHdl IN ctxType,`  `   stylesheet CLOB,`  `   ref IN VARCHAR2 := null);` | To un-register the stylesheet pass in a null or an empty string for the stylesheet. |

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |
| `uri` | `(IN)` | Stylesheet URI. |
| `stylesheet` | `(IN)` | Stylesheet. |
| `ref` | `(IN)` | URL to include, imported and external entities. |

---

### SETXSLTPARAM

Sets the value of a top-level stylesheet parameter. The parameter value is expected to be a valid XPath expression; the string literal values would therefore have to be quoted explicitly. If no stylesheet is registered, this method is not operational.

Syntax

```
PROCEDURE SETXSLTPARAM(
ctxHdl IN ctxType,
name IN VARCHAR2,
value IN VARCHAR2);
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |
| `name` | `(IN)` | Name of the top level stylesheet parameter. |
| `value` | `(IN)` | Value to be assigned to the stylesheet parameter. |

---

### USENULLATTRIBUTEINDICATOR

Specifies whether to use an XML attribute to indicate `NULL` ness, or to do this by omitting the particular entity in the XML document.

Syntax

```
PROCEDURE SETNULLATTRIBUTEINDICATOR(
ctxHdl IN ctxType, 
flag IN BOOLEAN);
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |
| `flag` | `(IN)` | Sets attribute to `NULL` if `TRUE`, omits from XML document if `FALSE`. |

---

### USETYPEFORCOLLELEMTAG

Specifies whether to use the collection element's type name as its element tag name. By default, the tag name for elements of a collection is the collection's tag name followed by `_item`.

Syntax

```
PROCEDURE USETYPEFORCOLLELEMTAG(
ctxHdl IN ctxType,
flag IN BOOLEAN := true);
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `ctxHdl` | `(IN)` | Context handle. |
| `flag` | `(IN)` | Turn on use of the type name? |