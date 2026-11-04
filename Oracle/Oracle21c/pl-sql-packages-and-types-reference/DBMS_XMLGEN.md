---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/DBMS_XMLGEN.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 211 DBMS\_XMLGEN

The `DBMS_XMLGEN` package converts the results of a SQL query to a canonical XML format.

The package takes an arbitrary SQL query as input, converts it to XML format, and returns the result as a `CLOB`. This package is similar to the `DBMS_XMLQUERY` package, except that it is written in C and compiled into the kernel. This package can only be run on the database.

This chapter contains the following topic:

- Security Model
- Summary of DBMS\_XMLGEN Subprograms

See Also:

[Oracle XML DB Developer's Guide, f](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADXDB) or more information on XML support and on examples of using `DBMS_XMLGEN`

### 211.1 DBMS\_XMLGEN Security Model

Owned by `XDB`, the `DBMS_XMLGEN` package must be created by `SYS` or `XDB`. The `EXECUTE` privilege is granted to `PUBLIC`. Subprograms in this package are executed using the privileges of the current user.

### 211.2 Summary of DBMS\_XMLGEN Subprograms

This table lists the DBMS\_XMLGEN subprograms and briefly describes them.

Table 211-1 Summary of DBMS\_XMLGEN Package Subprograms

| Subprogram | Description |
| --- | --- |
| CLOSECONTEXT Procedure | Closes the context and releases all resources |
| CONVERT Functions | Converts the XML into the escaped or unescaped XML equivalent |
| GETNUMROWSPROCESSED Function | Gets the number of SQL rows that were processed in the last call to GETXML Functions |
| GETXML Functions | Gets the XML document |
| GETXMLTYPE Functions | Gets the XML document and returns it as `XMLType` |
| NEWCONTEXT Functions | Creates a new context handle |
| NEWCONTEXTFROMHIERARCHY Function | Obtains a handle to use in the GETXML Functions and other functions to get a hierarchical XML with recursive elements from the result |
| RESTARTQUERY Procedure | Restarts the query to start fetching from the beginning |
| SETCONVERTSPECIALCHARS Procedure | Sets whether special characters such as `$,` which are non-XML characters, should be converted or not to their escaped representation |
| SETMAXROWS Procedure | Sets the maximum number of rows to be fetched each time |
| SETNULLHANDLING Procedure | Sets `NULL` handling options |
| SETROWSETTAG Procedure | Sets the name of the element enclosing the entire result |
| SETROWTAG Procedure | Sets the name of the element enclosing each row of the result |
| SETSKIPROWS Procedure | Sets the number of rows to skip every time before generating the XML. |
| USEITEMTAGSFORCOLL Procedure | Forces the use of the collection column name appended with the tag ` _ITEM` for collection elements |
| USENULLATTRIBUTEINDICATOR Procedure | Specifies whether to use an XML attribute to indicate `NULL` ness, or to do it by omitting the inclusion of the particular entity in the XML document. |

#### 211.2.1 CLOSECONTEXT Procedure

This procedure closes a given context and releases all resources associated with it, including the SQL cursor and bind and define buffers. After this call, the handle cannot be used for a subsequent function call.

Syntax

```
DBMS_XMLGEN.CLOSECONTEXT (
   ctx  IN ctxHandle);
```

Parameters

Table 211-2 CLOSECONTEXT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ctx` | The context handle to close. |

#### 211.2.2 CONVERT Functions

This function converts the XML data into the escaped or unescapes XML equivalent, and returns XML `CLOB` data in encoded or decoded format. There are several version of the function.

Syntax

Uses `XMLDATA` in string form (`VARCHAR2`):

```
DBMS_XMLGEN.CONVERT (
   xmlData IN VARCHAR2,
   flag    IN NUMBER := ENTITY_ENCODE)
RETURN VARCHAR2;
```

Uses `XMLDATA` in `CLOB` form:

```
DBMS_XMLGEN.CONVERT (
   xmlData IN CLOB,
   flag    IN NUMBER := ENTITY_ENCODE)
 RETURN CLOB;
```

Parameters

Table 211-3 CONVERT Function Parameters

| Parameter | Description |
| --- | --- |
| `xmlData` | The XML `CLOB` data to be encoded or decoded. |
| `flag` | The flag setting; `ENTITY_ENCODE` (default) for encode, and `ENTITY_DECODE` for decode. |

Usage Notes

This function escapes the XML data if the `ENTITY_ENCODE` is specified. For example, the escaped form of the character `<` is `&lt;`. Unescaping is the reverse transformation.

#### 211.2.3 GETNUMROWSPROCESSED Function

This function retrieves the number of SQL rows processed when generating the XML using the GETXML Functions call. This count does not include the number of rows skipped before generating the XML.

Note that GETXML Functions always generates an XML document, even if there are no rows present.

Syntax

```
DBMS_XMLGEN.GETNUMROWSPROCESSED (
   ctx     IN    ctxHandle)
RETURN NUMBER;
```

Parameters

Table 211-4 GETNUMROWSPROCESSED Function Parameters

| Parameter | Description |
| --- | --- |
| `ctx` | The context handle obtained from the NEWCONTEXT Functions call. |

Usage Notes

This function is used to determine the terminating condition if calling GETXML Functions in a loop.

#### 211.2.4 GETXML Functions

This function gets the XML document. The function is overloaded.

Syntax

Gets the XML document by fetching the maximum number of rows specified. It appends the XML document to the `CLOB` passed in. Use this version of GETXML Functions to avoid any extra `CLOB` copies and to reuse the same `CLOB` for subsequent calls. Because of the `CLOB` reuse, this GETXML Functions call is potentially more efficient:

```
DBMS_XMLGEN.GETXML (
   ctx          IN ctxHandle, 
   tmpclob      IN OUT NCOPY CLOB,
   dtdOrSchema  IN number := NONE)
 RETURN BOOLEAN;
```

Generates the XML document and returns it as a temporary `CLOB`. The temporary `CLOB` obtained from this function must be freed using the `DBMS_LOB.FREETEMPORARY` call:

```
DBMS_XMLGEN.GETXML (
   ctx          IN ctxHandle,
   dtdOrSchema  IN number := NONE)
 RETURN CLOB;
```

Converts the results from the SQL query string to XML format, and returns the XML as a temporary `CLOB`, which must be subsequently freed using the `DBMS_LOB.FREETEMPORARY` call:

```
DBMS_XMLGEN.GETXML (
   sqlQuery     IN VARCHAR2,
   dtdOrSchema  IN number := NONE)
 RETURN CLOB;
```

Parameters

Table 211-5 GETXML Function Parameters

| Parameter | Description |
| --- | --- |
| ``` ctx ``` | The context handle obtained from the `newContext` call. |
| ``` tmpclob ``` | The `CLOB` to which the XML document is appended. |
| `sqlQuery` | The SQL query string. |
| `dtdOrSchema` | Generate a DTD or a schema? Only `NONE` is supported. |

Usage Notes

When the rows indicated by the SETSKIPROWS Procedure call are skipped, the maximum number of rows as specified by the SETMAXROWS Procedure call (or the entire result if not specified) is fetched and converted to XML. Use the GETNUMROWSPROCESSED Function to check if any rows were retrieved.

#### 211.2.5 GETXMLTYPE Functions

This function gets the XML document and returns it as an `XMLTYPE`. `XMLTYPE` operations can be performed on the results. This function is overloaded.

Syntax

Generates the XML document and returns it as a `sys.XMLType:`

```
DBMS_XMLGEN.GETXMLTYPE (
   ctx           IN ctxhandle,
   dtdOrSchema   IN number := NONE)
 RETURN sys.XMLType;
```

Converts the results from the SQL query string to XML format, and returns the XML as a `sys.XMLType`:

```
DBMS_XMLGEN.GETXMLTYPE (
   sqlQuery     IN VARCHAR2,
   dtdOrSchema  IN number := NONE)
 RETURN sys.XMLType
```

Parameters

Table 211-6 GETXMLTYPE Function Parameters

| Parameter | Description |
| --- | --- |
| `ctx` | The context handle obtained from the `newContext` call. |
| `sqlQuery` | The SQL query string. |
| `dtdOrSchema` | Generate a DTD or a schema? Only `NONE` is supported. |

#### 211.2.6 NEWCONTEXT Functions

This function generates and returns a new context handle.

This context handle is used in GETXML Functions and other functions to get XML back from the result. There are several version of the function.

Syntax

Generates a new context handle from a query:

```
DBMS_XMLGEN.NEWCONTEXT ( 
      query     IN VARCHAR2) 
 RETURN ctxHandle;
```

Generates a new context handle from a query string in the form of a PL/SQL ref cursor:

```
DBMS_XMLGEN.NEWCONTEXT (
   queryString  IN SYS_REFCURSOR)
 RETURN ctxHandle;
```

Parameters

Table 211-7 NEWCONTEXT Function Parameters

| Parameter | Description |
| --- | --- |
| `query` | The query, in the form of a `VARCHAR`, the result of which must be converted to XML. |
| `queryString` | The query string in the form of a PL/SQL ref cursor, the result of which must be converted to XML. |

#### 211.2.7 NEWCONTEXTFROMHIERARCHY Function

This function obtains a handle to use in the GETXML Functions and other functions to get a hierarchical XML with recursive elements from the result.

Syntax

```
DBMS_XMLGEN.NEWCONTEXTFROMHIERARCHY ( 
   queryString IN VARCHAR2) 
 RETURN ctxHandle;
```

Parameters

Table 211-8 NEWCONTEXTFROMHIERARCHY Function Parameters

| Parameter | Description |
| --- | --- |
| `queryString` | The query string, the result of which must be converted to XML. The query is a hierarchical query typically formed using a `CONNECT` `BY` clause, and the result must have the same property as the result set generated by a `CONNECT` `BY` query. The result set must have only two columns, the level number and an XML value. The level number is used to determine the hierarchical position of the XML value within the result XML document. |

#### 211.2.8 RESTARTQUERY Procedure

This procedure restarts the query and generates the XML from the first row.

It can be used to start executing the query again, without having to create a new context.

Syntax

```
DBMS_XMLGEN.RESTARTQUERY (
ctx  IN ctxHandle);
```

Parameters

Table 211-9 RESTARTQUERY Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ctx` | The context handle corresponding to the current query. |

#### 211.2.9 SETCONVERTSPECIALCHARS Procedure

This procedure sets whether or not special characters in the XML data must be converted into their escaped XML equivalent. For example, the `<` sign is converted to `&lt;`.

The default is to perform conversions.

This function improves performance of XML processing when the input data cannot contain any special characters such as `<`, `>`, `",'`, which must be escaped. It is expensive to scan the character data to replace the special characters, particularly if it involves a lot of data.

Syntax

```
DBMS_XMLGEN.SETCONVERTSPECIALCHARS (
ctx   IN ctxHandle,
conv  IN BOOLEAN);
```

Parameters

Table 211-10 SETCONVERTSPECIALCHARS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ctx` | The context handle obtained from one of the NEWCONTEXT Functions call. |
| `conv` | `TRUE` indicates that conversion is needed. |

#### 211.2.10 SETMAXROWS Procedure

This procedure sets the maximum number of rows to fetch from the SQL query result for every invocation of the GETXML Functions call.

It is used when generating paginated results. For example, when generating a page of XML or HTML data, restrict the number of rows converted to XML or HTML by setting the `maxrows` parameter.

Syntax

```
DBMS_XMLGEN.SETMAXROWS (
ctx      IN ctxHandle,
maxRows  IN NUMBER);
```

Parameters

Table 211-11 SETMAXROWS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ctx` | The context handle corresponding to the query executed. |
| `maxRows` | The maximum number of rows to get for each call to GETXML Functions |

#### 211.2.11 SETNULLHANDLING Procedure

This procedure sets `NULL` handling options, handled through the `flag` parameter setting.

Syntax

```
DBMS_XMLGEN.SETNULLHANDLING(
ctx  IN ctx,
flag IN NUMBER);
```

Parameters

Table 211-12 SETNULLHANDLING Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ctx` | The context handle corresponding to the query executed. |
| `flag` | The `NULL` handling option set.  - `DROP_NULLS CONSTANT NUMBER:= 0;` (Default) Leaves out the tag for `NULL` elements. - `NULL_ATTR CONSTANT NUMBER:= 1`; Sets `xsi:nil="true"`. - `EMPTY_TAG CONSTANT NUMBER:= 2; `Sets, for example, `<foo/>`. |

#### 211.2.12 SETROWSETTAG Procedure

This procedure sets the name of the root element of the document. The default name is `ROWSET.`

Syntax

```
DBMS_XMLGEN.SETROWSETTAG ( 
ctx            IN ctxHandle,  
rowSetTagName  IN VARCHAR2);
```

Parameters

Table 211-13 SETROWSETTAG Procedure Parameters

| Parameter | Description |
| --- | --- |
| ctx | The context handle obtained from the NEWCONTEXT Functions call. |
| rowSetTagName | The name of the document element. Passing `NULL` indicates that you do not want the `ROWSET` element present. |

Usage Notes

The user can set the `rowSetTag` to `NULL` to suppress the printing of this element. However, an error is produced if both the row and the rowset are `NULL` and there is more than one column or row in the output. This is because the generated XML would not have a top-level enclosing tag, and so would be invalid.

#### 211.2.13 SETROWTAG Procedure

This procedure sets the name of the element separating all the rows. The default name is `ROW.`

Syntax

```
DBMS_XMLGEN.SETROWTAG (
ctx         IN ctxHandle,
rowTagName  IN VARCHAR2);
```

Parameters

Table 211-14 SETROWTAG Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ctx` | The context handle obtained from the NEWCONTEXT Functions call. |
| `rowTagName` | The name of the `ROW` element. Passing `NULL` indicates that you do not want the `ROW` element present. |

Usage Notes

The user can set the name of the element to `NULL` to suppress the `ROW` element itself. However, an error is produced if both the row and the rowset are `NULL` and there is more than one column or row in the output. This is because the generated XML would not have a top-level enclosing tag, and so would be invalid.

#### 211.2.14 SETSKIPROWS Procedure

This procedure skips a given number of rows before generating the XML output for every call to the GETXML Functions. It is used when generating paginated results for stateless Web pages using this utility.

For example, when generating the first page of XML or HTML data, set `skiprows` to zero. For the next set, set the `skiprows` to the number of rows obtained in the first case. See GETNUMROWSPROCESSED Function.

Syntax

```
DBMS_XMLGEN.SETSKIPROWS (
ctx       IN ctxHandle,
skipRows  IN NUMBER);
```

Parameters

Table 211-15 SETSKIPROWS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ctx` | The context handle corresponding to the query executed. |
| `skipRows` | The number of rows to skip for each call to `getXML.` |

#### 211.2.15 USEITEMTAGSFORCOLL Procedure

This procedure overrides the default name of the collection elements. The default name for collection elements is the type name itself.

Syntax

```
DBMS_XMLGEN.USEITEMTAGSFORCOLL (
   ctx  IN ctxHandle);
```

Parameters

Table 211-16 USEITEMTAGSFORCOLL Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ctx` | The context handle. |

Usage Notes

Using this procedure, you can override the default to use the name of the column with the `_ITEM` tag appended to it. If there is a collection of `NUMBER`, the default tag name for the collection elements is `NUMBER`.

#### 211.2.16 USENULLATTRIBUTEINDICATOR Procedure

This procedure specifies whether to use an XML attribute to indicate `NULL`, or to do it by omitting the inclusion of the particular entity in the XML document.

It is used as a shortcut for the SETNULLHANDLING Procedure`.`

Syntax

```
DBMS_XMLGEN.USENULLATTRIBUTEINDICATOR(
ctx       IN   ctxType,
attrind   IN   BOOLEAN := TRUE);
```

Parameters

Table 211-17 USENULLATTRIBUTEINDICATOR Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ctx` | Context handle. |
| `attrind` | Use attribute to indicate `NULL`? |