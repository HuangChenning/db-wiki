---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/DBMS_METADATA.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 112 DBMS\_METADATA

The `DBMS_METADATA` package provides a way for you to retrieve metadata from the database dictionary as XML or creation DDL and to submit the XML to re-create the object.

See Also:

[Oracle Database Utilities](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=SUTIL-GUID-D9B1300F-B21D-416E-8B9B-C542195EF249) for more information and for examples of using the `DBMS_METADATA` package.

This chapter contains the following topics:

### 112.1 DBMS\_METADATA Overview

You can use the `DBMS_METADATA` package to retrieve metadata and to submit XML.

Retrieving Metadata

If you are retrieving metadata, you can specify:

- The kind of object to be retrieved. This can be either a particular object type (such as a table, index, or procedure) or a heterogeneous collection of object types that form a logical unit (such as a database export or schema export).
- Optional selection criteria, such as owner or name.
- Parse items (attributes of the returned objects to be parsed and returned separately).
- Optional transformations on the output, implemented by XSLT (Extensible Stylesheet Language Transformation) scripts. By default the output is represented in XML, but you can specify transformations (into SQL DDL, for example), which are implemented by XSLT stylesheets stored in the database or externally.

`DBMS_METADATA` provides the following retrieval interfaces:

- For programmatic use: `OPEN,` `SET_FILTER,` `SET_COUNT,` `GET_QUERY,` `SET_PARSE_ITEM,` `ADD_TRANSFORM,` `SET_TRANSFORM_PARAM,SET_REMAP_PARAM,` `FETCH_xxx,` and `CLOSE` retrieve multiple objects.
- For use in SQL queries and for browsing: `GET_XML`, `GET_DDL` and `GET_SXML` return metadata for a single named object. The `GET_DEPENDENT_XML`, `GET_DEPENDENT_DDL`, `GET_GRANTED_XML`, and `GET_GRANTED_DDL` interfaces return metadata for one or more dependent or granted objects. These procedures do not support heterogeneous object types.

Submitting XML

If you are submitting XML, you specify:

- The type of object
- Optional transform parameters to modify the object (for example, changing the object's owner)
- Parse items (attributes of the submitted objects to be parsed and submitted separately)
- Whether to execute the operation or simply return the generated DDL

`DBMS_METADATA` provides a programmatic interface for submission of XML. It is comprised of the following procedures: `OPENW`, `ADD_TRANSFORM`, `SET_TRANSFORM_PARAM`, `SET_REMAP_PARAM`, `SET_PARSE_ITEM`, `CONVERT`, `PUT`, and `CLOSE`.

### 112.2 DBMS\_METADATA Security Model

The `DBMS_METADATA` package considers a privileged user to be one who is connected as user `SYS` or who has the `SELECT_CATALOG_ROLE` role.

The object views of the Oracle metadata model implement security as follows:

- Nonprivileged users can see the metadata of only their own objects.
- Nonprivileged users can also retrieve public synonyms, system privileges granted to them, and object privileges granted to them or by them to others. This also includes privileges granted to `PUBLIC`.
- If callers request objects they are not privileged to retrieve, no exception is raised; the object is simply not retrieved.
- If nonprivileged users are granted some form of access to an object in someone else's schema, they will be able to retrieve the grant specification through the Metadata API, but not the object's actual metadata.
- In stored procedures, functions, and definers-rights packages, roles (such as `SELECT_CATALOG_ROLE`) are disabled. Therefore, such a PL/SQL program can only fetch metadata for objects in its own schema. If you want to write a PL/SQL program that fetches metadata for objects in a different schema (based on the invoker's possession of `SELECT_CATALOG_ROLE`), you must make the program invokers-rights.
- For all objects that have passwords, except database links (for example, users and roles), the following rules apply:
	- A user who has the `SELECT_CATALOG_ROLE` can see all metadata for an object except the passwords for that object.
		- The `SYS` user, users who have the `EXP_FULL_DATABASE` role, and users who own an object can see all metadata for that object, including passwords.
- For database links the password is never displayed. For security reasons Oracle restricts visibility of the password value to `SYS` users who query the `link$.passwordx` column directly. Instead of the password, `DBMS_METADATA` returns the following invalid syntax:
	```
	IDENTIFIED BY VALUES ':1'
	```
	A user who knows the password of the database link can manually replace the `:1` with the password.

### 112.3 Rules and Limits

In an Oracle Shared Server (OSS) environment, the `DBMS_METADATA` package must disable session migration and connection pooling.

This results in any shared server process that is serving a session running the package to effectively become a default, dedicated server for the life of the session. You should ensure that sufficient shared servers are configured when the package is used and that the number of servers is not artificially limited by too small a value for the `MAX_SHARED_SERVERS` initialization parameter.

### 112.4 DBMS\_METADATA Data Structures - Object and Table Types

The `DBMS_METADATA` package defines, in the `SYS` schema, the `OBJECT` and `TABLE` types shown in this code.

```
CREATE TYPE sys.ku$_parsed_item AS OBJECT (
  item            VARCHAR2(30),
  value           VARCHAR2(4000),
  object_row      NUMBER )
/

CREATE PUBLIC SYNONYM ku$_parsed_item FOR sys.ku$_parsed_item;

CREATE TYPE sys.ku$_parsed_items IS TABLE OF sys.ku$_parsed_item
/

CREATE PUBLIC SYNONYM ku$_parsed_items FOR sys.ku$_parsed_items;

CREATE TYPE sys.ku$_ddl AS OBJECT (
   ddlText        CLOB,
parsedItems sys.ku$_parsed_items )
/

CREATE PUBLIC SYNONYM ku$_ddl FOR sys.ku$_ddl;

CREATE TYPE sys.ku$_ddls IS TABLE OF sys.ku$_ddl
/

CREATE PUBLIC SYNONYM ku$_ddls FOR sys.ku$_ddls;

CREATE TYPE sys.ku$_multi_ddl AS OBJECT (
   object_row     NUMBER,
   ddls           sys.ku$_ddls )
/

CREATE OR REPLACE PUBLIC SYNONYM ku$_multi_ddl FOR sys.ku$_multi_ddl;

CREATE TYPE sys.ku$_multi_ddls IS TABLE OF sys.ku$_multi_ddl;
/

CREATE OR REPLACE PUBLIC SYNONYM ku$_multi_ddls FOR
                          sys.ku$_multi_ddls;

CREATE TYPE sys.ku$_ErrorLine IS OBJECT (
   errorNumber    NUMBER,
   errorText      VARCHAR2(2000) )
/

CREATE PUBLIC SYNONYM ku$_ErrorLine FOR sys.ku$_ErrorLine;

CREATE TYPE sys.ku$_ErrorLines IS TABLE OF sys.ku$_ErrorLine
/
CREATE PUBLIC SYNONYM ku$ErrorLines FOR sys.ku$_ErrorLines;

CREATE TYPE sys.ku$_SubmitResult AS OBJECT (
   ddl          sys.ku$_ddl,
   errorLines   sys.ku$_ErrorLines );
/

CREATE TYPE sys.ku$_SubmitResults IS TABLE OF sys.ku$_SubmitResult
/

CREATE PUBLIC SYNONYM ku$_SubmitResults FOR sys.ku$_SubmitResults;
```

Note:

The maximum size of the `VARCHAR2`, `NVARCHAR2`, and `RAW` datatypes has been increased to 32 KB when the `COMPATIBLE` initialization parameter is set to 12.0 and the `MAX_STRING_SIZE` initialization parameter is set to `EXTENDED`. The `DBMS_METADATA` package supports this increased size unless the version of the metadata is earlier than Oracle Database 12c Release 1 (12.1).

### 112.5 DBMS\_METADATA Subprogram Groupings

The `DBMS_METADATA` subprograms retrieve objects from, and submit XML to, a database. Some subprograms are used for both activities, while others are used only for retrieval or only for submission.

- Table 112-1 provides a summary, in alphabetical order, of `DBMS_METADATA` subprograms used to retrieve multiple objects from a database.
- Table 112-2 provides a summary, in alphabetical order, of `DBMS_METADATA` subprograms used to submit XML metadata to a database.

#### 112.5.1 DBMS\_METADATA Subprograms for Retrieving Multiple Objects From the Database

`DBMS_METADATA` uses these subprograms used for retrieving multiple objects from the database.

Table 112-1 DBMS\_METADATA Subprograms for Retrieving Multiple Objects

| Subprogram | Description |
| --- | --- |
| ADD\_TRANSFORM Function | Specifies a transform that `FETCH_xxx` applies to the XML representation of the retrieved objects |
| CLOSE Procedure CLOSE Procedure | Invalidates the handle returned by `OPEN` and cleans up the associated state |
| FETCH\_xxx Functions and Procedures | Returns metadata for objects meeting the criteria established by `OPEN`, `SET_FILTER`, `SET_COUNT`, `ADD_TRANSFORM`, and so on |
| GET\_QUERY Function | Returns the text of the queries that are used by `FETCH_xxx` |
| GET\_xxx Functions | Fetches the metadata for a specified object as XML, SXML, or DDL, using only a single call |
| OPEN Function | Specifies the type of object to be retrieved, the version of its metadata, and the object model |
| SET\_COUNT Procedure | Specifies the maximum number of objects to be retrieved in a single `FETCH_xxx` call |
| SET\_FILTER Procedure | Specifies restrictions on the objects to be retrieved, for example, the object name or schema |
| SET\_PARSE\_ITEM Procedure | Enables output parsing by specifying an object attribute to be parsed and returned |
| SET\_TRANSFORM\_PARAM and SET\_REMAP\_PARAM Procedures | Specifies parameters to the XSLT stylesheets identified by `transform_handle` |

#### 112.5.2 DBMS\_METADATA Subprograms for Submitting XML to the Database

`DBMS_METADATA` uses these subprograms for submitting XML to the database.

Table 112-2 DBMS\_METADATA Subprograms for Submitting XML

| Subprogram | Description |
| --- | --- |
| ADD\_TRANSFORM Function | Specifies a transform for the XML documents |
| CLOSE Procedure CLOSE Procedure | Closes the context opened with `OPENW` |
| CONVERT Functions and Procedures | Converts an XML document to DDL |
| OPENW Function | Opens a write context |
| PUT Function | Submits an XML document to the database |
| SET\_PARSE\_ITEM Procedure | Specifies an object attribute to be parsed |
| SET\_TRANSFORM\_PARAM and SET\_REMAP\_PARAM Procedures | `SET_TRANSFORM_PARAM` specifies a parameter to a transform  `SET_REMAP_PARAM` specifies a remapping for a transform |

### 112.6 Summary of All DBMS\_METADATA Subprograms

This table lists the `DBMS_METADATA` subprograms and briefly describes them.

Table 112-3 DBMS\_METADATA Package Subprograms

| Subprogram | Description |
| --- | --- |
| ADD\_TRANSFORM Function | Specifies a transform that `FETCH_xxx` applies to the XML representation of the retrieved objects |
| CLOSE Procedure CLOSE Procedure | Invalidates the handle returned by `OPEN` and cleans up the associated state |
| CONVERT Functions and Procedures | Converts an XML document to DDL |
| FETCH\_xxx Functions and Procedures | Returns metadata for objects meeting the criteria established by `OPEN`, `SET_FILTER`, `SET_COUNT`, `ADD_TRANSFORM`, and so on |
| GET\_xxx Functions | Fetches the metadata for a specified object as XML, SXML, or DDL, using only a single call |
| GET\_QUERY Function | Returns the text of the queries that are used by `FETCH_xxx` |
| OPEN Function | Specifies the type of object to be retrieved, the version of its metadata, and the object model |
| OPENW Function | Opens a write context |
| PUT Function | Submits an XML document to the database |
| SET\_COUNT Procedure | Specifies the maximum number of objects to be retrieved in a single `FETCH_xxx` call |
| SET\_FILTER Procedure | Specifies restrictions on the objects to be retrieved, for example, the object name or schema |
| SET\_PARSE\_ITEM Procedure | Enables output parsing by specifying an object attribute to be parsed and returned |
| SET\_TRANSFORM\_PARAM and SET\_REMAP\_PARAM Procedures | Specifies parameters to the XSLT stylesheets identified by `transform_handle` |

#### 112.6.1 ADD\_TRANSFORM Function

The `DBMS_METADATA.ADD_TRANSFORM` function is used for both retrieval and submission.

- When this procedure is used to retrieve objects, it specifies a transform that `FETCH_xxx` applies to the XML representation of the retrieved objects.
- When used to submit objects, it specifies a transform that `CONVERT` or `PUT` applies to the XML representation of the submitted objects. It is possible to add more than one transform.
	See Also:
	- Subprograms for Retrieving Multiple Objects From the Database
	- Subprograms for Submitting XML to the Database
	- " SET\_TRANSFORM\_PARAM and SET\_REMAP\_PARAM Procedures " for information about how to modify and customize transform output

Syntax

```
DBMS_METADATA.ADD_TRANSFORM (
   handle       IN NUMBER,
   name         IN VARCHAR2,
   encoding     IN VARCHAR2 DEFAULT NULL,
   object_type  IN VARCHAR2 DEFAULT NULL)
 RETURN NUMBER;
```

Parameters

Table 112-4 ADD\_TRANSFORM Function Parameters

| Parameters | Description |
| --- | --- |
| `handle` | The handle returned from `OPEN` when this transform is used to retrieve objects. Or the handle returned from `OPENW` when this transform is used in the submission of XML metadata. |
| `name` | The name of the transform. The name can be an internal keyword like `DDL` to use internally stored stylesheets. If the name contains a colon, it is interpreted as `directory_object_name:file_name` of a user-supplied Extensible Stylesheet Language Transformation (XSLT) script.  Otherwise, name designates a transform implemented by `DBMS_METADATA`.  See Table 112-5 for descriptions of available transforms. |
| `encoding` | The name of the Globalization Support character set in which the stylesheet pointed to by name is encoded. This is only valid if name is a URL. If left NULL and the URL is external to the database, UTF-8 encoding is assumed. If left `NULL` and the URL is internal to the database (that is, it begins with `/oradb/`), then the encoding is assumed to be the database character set. |
| `object_type` | The definition of this parameter depends upon whether you are retrieving objects or submitting XML metadata.  1. When you use `ADD_TRANFORM` to retrieve objects, the following definition of object\_type applies: 	Designates the object type to which the transform applies. (Note that this is an object type name, not a path name.) By default the transform applies to the object type of the `OPEN` handle. When the `OPEN` handle designates a heterogeneous object type, the following behavior can occur: 	- if `object_type` is omitted, the transform applies to all object types within the heterogeneous collection 		- if `object_type` is specified, the transform only applies to that specific object type within the collection 		If you omit this parameter you can add the DDL transform to all objects in a heterogeneous collection with a single call. If you supply this parameter, you can add a transform for a specific object type. 2. When you use `ADD_TRANSFORM` in the submission of XML metadata, this parameter is the object type to which the transform applies. By default, it is the object type of the `OPENW` handle. Because the `OPENW` handle cannot designate a heterogeneous object type, the caller would normally leave this parameter `NULL` in the `ADD_TRANSFORM` calls. |

The following table describes the transforms available on the `ADD_TRANSFORM` function.

Because new transforms are occasionally added, you might want to query the `DBMS_METADATA_TRANSFORMS` view to see all valid Oracle-supplied transforms for specific object types.

Table 112-5 Transforms Available on ADD\_TRANSFORM Function

| Object Type | Transform Name | Input Doc Type | Output Doc Type | Description |
| --- | --- | --- | --- | --- |
| All | DDL | XML | DDL | Convert XML to SQL to create the object |
| All | MODIFY | XML | XML | Modify XML document according to transform parameters |
| Subset | SXML | XML | SXML | Convert XML to SXML |
| Subset | MODIFYSXML | SXML | SXML | Modify SXML document according to transform parameters |
| Subset | SXMLDDL | SXML | DDL | Convert SXML to DDL |
| Subset | ALTERXML | SXML difference document | ALTER\_XML | Generate ALTER\_XML from SXML difference document. (See the `DBMS_METADATA_DIFF` PL/SQL package for more information about SXML difference format.)  The following parameters are valid for the ALTERXML transform:  - `XPATH` - The `XPATH` of the object being altered - `NAME` - Name of the object being altered - `ALTERABLE` - Affirms that the object can be altered. If the object cannot be altered, a `NOT_ALTERABLE` element is inserted whose value indicates the reason. - `CLAUSE_TYPE` - The type of clause (for example, `ADD_COLUMN`) - `COLUMN_ATTRIBUTE` - The attribute being modified - `CONSTRAINT_TYPE` - The type of constraint (for example, `UNIQUE` or `PRIMARY`) |
| Subset | ALTERDDL | ALTER\_XML | ALTER\_DDL | Convert ALTER\_XML to ALTER\_DDL |

Return Values

The opaque handle that is returned is used as input to `SET_TRANSFORM_PARAM` and `SET_REMAP_PARAM`. Note that this handle is different from the handle returned by `OPEN` or `OPENW`; it refers to the transform, not the set of objects to be retrieved.

Usage Notes

- With no transforms added, objects are returned by default as XML documents. You call `ADD_TRANSFORM` to specify the XSLT stylesheets to be used to transform the returned XML documents.
- You can call `ADD_TRANSFORM` more than once to apply multiple transforms to XML documents. The transforms are applied in the order in which they were specified, the output of the first transform being used as input to the second, and so on.
- The output of a DDL transform is not an XML document. Therefore, no transform should be added after the DDL transform.
- Each transform expects a certain format XML document as input. If the input document is unspecified, metadata XML format is assumed.
- When the ALTERXML transform is used, parse items are returned in a `PARSE_LIST` element of the ALTER\_XML document. Each `PARSE_LIST_ITEM` element contains an `ITEM` and a `VALUE`. For example:
	```
	<PARSE_LIST>
	 <PARSE_LIST_ITEM>
	  <ITEM>XPATH</ITEM>
	  <VALUE>/sxml:TABLE/sxml:RELATIONAL_TABLE/sxml:COL_LIST/sxml:COL_LIST_ITEM[14]</VALUE>
	 </PARSE_LIST_ITEM>
	 <PARSE_LIST_ITEM>
	  <ITEM>NAME</ITEM>
	  <VALUE>Z1</VALUE>
	 </PARSE_LIST_ITEM>
	 <PARSE_LIST_ITEM>
	  <ITEM>CLAUSE_TYPE</ITEM>
	  <VALUE>ADD_COLUMN</VALUE>
	 </PARSE_LIST_ITEM>
	 <PARSE_LIST_ITEM>
	  <ITEM>COLUMN_ATTRIBUTE</ITEM>
	  <VALUE>NOT_NULL</VALUE>
	 </PARSE_LIST_ITEM>
	</PARSE_LIST>
	```

Exceptions

- `INVALID_ARGVAL`. A `NULL` or invalid value was supplied for an input parameter. The error message text identifies the parameter.
- `INVALID_OPERATION`. `ADD_TRANSFORM` was called after the first call to `FETCH_xxx` for the `OPEN` context. After the first call to `FETCH_xxx` is made, no further calls to `ADD_TRANSFORM` for the current `OPEN` context are permitted.
- `INCONSISTENT_ARGS`. The arguments are inconsistent. Possible inconsistencies include the following:
	- `encoding` is specified even though name is not a URL.
		- `object_type` is not part of the collection designated by handle.

#### 112.6.2 CLOSE Procedure

This procedure is used for both retrieval and submission. This procedure invalidates the handle returned by `OPEN` (or `OPENW`) and cleans up the associated state.

Syntax

```
DBMS_METADATA.CLOSE (
   handle  IN NUMBER);
```

Parameters

Table 112-6 CLOSE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `handle` | The handle returned from `OPEN` (or `OPENW`). |

Usage Notes

Note:

The following notes apply only to object retrieval

You can prematurely terminate the stream of objects established by `OPEN` or (`OPENW)`.

- If a call to `FETCH_xxx` returns `NULL,` indicating no more objects, a call to `CLOSE` is made transparently. In this case, you can still call `CLOSE` on the handle and not get an exception. (The call to `CLOSE` is not required.)
- If you know that only one specific object will be returned, you should explicitly call `CLOSE` after the single `FETCH_xxx` call to free resources held by the handle.

Exceptions

- `INVALID_ARGVAL`. The value for the `handle` parameter is `NULL` or invalid.

#### 112.6.3 CONVERT Functions and Procedures

The `DBMS_METADATA.CONVERT` functions and procedures transform input XML documents.

The `CONVERT` functions return creation DDL. The `CONVERT` procedures return either XML or DDL, depending on the specified transforms.

See Also:

- Subprograms for Submitting XML to the Database

Syntax

The `CONVERT` functions are as follows:

```
DBMS_METADATA.CONVERT (
   handle   IN NUMBER,
   document IN sys.XMLType)
 RETURN sys.ku$_multi_ddls;

DBMS_METADATA.CONVERT (
  handle   IN NUMBER,
  document IN CLOB)
 RETURN sys.ku$_multi_ddls;
```

The `CONVERT` procedures are as follows:

```
DBMS_METADATA.CONVERT (
  handle   IN NUMBER,
  document IN sys.XMLType,
  result   IN OUT NOCOPY CLOB);

DBMS_METADATA.CONVERT (
  handle   IN NUMBER,
  document IN CLOB,
  result   IN OUT NOCOPY CLOB);
```

Parameters

Table 112-7 CONVERT Subprogram Parameters

| Parameter | Description |
| --- | --- |
| `handle` | The handle returned from `OPENW` |
| `document` | The XML document containing object metadata of the type of the `OPENW` handle |
| result | The converted document |

Return Values

Either XML or DDL, depending on the specified transforms.

Usage Notes

You can think of `CONVERT` as the second half of `FETCH_xxx`, either `FETCH_DDL` (for the function variants) or `FETCH_CLOB` (for the procedure variants). There are two differences:

- `FETCH_xxx` gets its XML document from the database, but `CONVERT` gets its XML document from the caller
- `FETCH_DDL` returns its results in a `sys.ku$_ddls ` nested table, but `CONVERT` returns a `sys.ku$_multi_ddls` nested table

The transforms specified with `ADD_TRANSFORM` are applied in turn, and the result is returned to the caller. For the function variants, the DDL transform must be specified. If parse items were specified, they are returned in the `parsedItems` column. Parse items are ignored by the procedure variants.

The encoding of the XML document is embedded in its CLOB or XMLType representation. The version of the metadata is embedded in the XML. The generated DDL is valid for the database version specified in `OPENW`.

Exceptions

- `INVALID_ARGVAL`. A `NULL` or invalid value was supplied for an input parameter. The error message text identifies the parameter.
- `INCONSISTENT_OPERATION`. No transform was specified. The DDL transform was not specified (function variants only).
- `INCOMPATIBLE_DOCUMENT`. The version of the XML document is not compatible with this version of the software.

#### 112.6.4 FETCH\_xxx Functions and Procedures

These functions and procedures return metadata for objects meeting the criteria established by `OPEN`, `SET_FILTER`, `SET_COUNT`, `ADD_TRANSFORM`, and so on.

See " Usage Notes " for the variants.

Syntax

The `FETCH` functions are as follows:

```
DBMS_METADATA.FETCH_XML (
   handle  IN NUMBER) 
RETURN sys.XMLType;
```
```
DBMS_METADATA.FETCH_DDL (
   handle  IN NUMBER)
RETURN sys.ku$_ddls;

DBMS_METADATA.FETCH_CLOB (
   handle       IN NUMBER,
   cache_lob    IN BOOLEAN DEFAULT TRUE,
   lob_duration IN PLS INTEGER DEFAULT DBMS_LOB.SESSION)
RETURN CLOB;
```

The `FETCH` procedures are as follows:

```
DBMS_METADATA.FETCH_CLOB (
   handle  IN NUMBER,
   doc     IN OUT NOCOPY CLOB);

DBMS_METADATA.FETCH_XML_CLOB (
   handle  IN NUMBER,
   doc     IN OUT NOCOPY CLOB,
   parsed_items OUT sys.ku$_parsed_items,
   object_type_path OUT VARCHAR2);
```

Parameters

Table 112-8 FETCH\_xxx Function Parameters

| Parameters | Description |
| --- | --- |
| `handle` | The handle returned from `OPEN`. |
| `cache_lob` | `TRUE` =read LOB into buffer cache |
| `lob_duration` | The duration for the temporary LOB created by `FETCH_CLOB`, either `DBMS_LOB.SESSION` (the default) or `DBMS_LOB.CALL`. |
| `doc` | The metadata for the objects, or `NULL` if all objects have been returned. |
| `parsed_items` | A nested table containing the items specified by `SET_PARSE_ITEM`. If `SET_PARSE_ITEM` was not called, a NULL is returned. |
| `object_type_path` | For heterogeneous object types, this is the full path name of the object type for the objects returned by the call to `FETCH_XXX`. If `handle` designates a homogeneous object type, a NULL is returned. |

Return Values

The metadata for the objects or `NULL` if all objects have been returned.

Usage Notes

These functions and procedures return metadata for objects meeting the criteria established by the call to `OPEN` that returned the handle, and subsequent calls to `SET_FILTER`, `SET_COUNT`, `ADD_TRANSFORM`, and so on. Each call to `FETCH_xxx` returns the number of objects specified by `SET_COUNT` (or less, if fewer objects remain in the underlying cursor) until all objects have been returned. After the last object is returned, subsequent calls to `FETCH_xxx` return `NULL` and cause the stream created by `OPEN` to be transparently closed.

There are several different `FETCH_xxx` functions and procedures:

- The `FETCH_XML` function returns the XML metadata for an object as an `XMLType`. It assumes that if any transform has been specified, that transform will produce an XML document. In particular, it assumes that the DDL transform has not been specified.
- The `FETCH_DDL` function returns the DDL (to create the object) in a `sys.ku$_ddls` nested table. It assumes that the DDL transform has been specified. Each row of the `sys.ku$_ddls` nested table contains a single DDL statement in the `ddlText ` column; if requested, parsed items for the DDL statement will be returned in the `parsedItems` column. Multiple DDL statements may be returned under the following circumstances:
	- When you call `SET_COUNT` to specify a count greater than `1`
		- When an object is transformed into multiple DDL statements. For example, A `TYPE` object that has a DDL transform applied to it can be transformed into both `CREATE TYPE` and `CREATE TYPE BODY` statements. A `TABLE` object can be transformed into a `CREATE TABLE`, and one or more `ALTER TABLE` statements
- The `FETCH_CLOB` function simply returns the object, transformed or not, as a CLOB. By default, the CLOB is read into the buffer cache and has session duration, but these defaults can be overridden with the `cache_lob` and `lob_duration` parameters.
- The `FETCH_CLOB` procedure returns the objects by reference in an `IN` `OUT` `NOCOPY` parameter. This is faster than the function variant, which returns LOBs by value, a practice that involves an expensive LOB copy.
- The `FETCH_XML_CLOB` procedure returns the XML metadata for the objects as a CLOB in an `IN` `OUT` `NOCOPY` parameter. This helps to avoid LOB copies, which can consume a lot of resources. It also returns a nested table of parse items and the full path name of the object type of the returned objects.
- All LOBs returned by `FETCH_xxx` are temporary LOBs. You must free the LOB. If the LOB is supplied as an `IN` `OUT` `NOCOPY` parameter, you must also create the LOB.
- If `SET_PARSE_ITEM` was called, `FETCH_DDL` and `FETCH_XML_CLOB` return attributes of the object's metadata (or the DDL statement) in a `sys.ku$_parsed_items` nested table. For `FETCH_XML_CLOB`, the nested table is an `OUT` parameter. For `FETCH_DDL`, it is a column in the returned `sys.ku$_ddls` nested table. Each row of the nested table corresponds to an item specified by `SET_PARSE_ITEM` and contains the following columns:
	- `item` —the name of the attribute as specified in the `name` parameter to `SET_PARSE_ITEM.`
		- value—the attribute value, or `NULL` if the attribute is not present in the DDL statement.
		- `object-row` —a positive integer indicating the object to which the parse item applies. If multiple objects are returned by `FETCH_xxx`, (because `SET_COUNT` specified a count greater than 1) then `object_row` = `1` for all items for the first object, `2` for the second, and so on.
- The rows of the `  sys.ku$_parsed_items  ` nested table are ordered by ascending `object_row`, but otherwise the row order is undetermined. To find a particular parse item within an object row the caller must search the table for a match on `item`.
- In general there is no guarantee that a requested parse item will be returned. For example, the parse item may not apply to the object type or to the particular line of DDL, or the item's value may be `NULL`.
- If `SET_PARSE_ITEM` was not called, `NULL` is returned as the value of the parsed items nested table.
- It is expected that the same variant of `FETCH_xxx` will be called for all objects selected by `OPEN`. That is, programs will not intermix calls to `FETCH_XML`, `FETCH_DDL`, `FETCH_CLOB`, and so on using the same `OPEN` handle. The effect of calling different variants is undefined; it might do what you expect, but there are no guarantees.
- Every object fetched will be internally consistent with respect to on-going DDL (and the subsequent recursive DML) operations against the dictionary. In some cases, multiple queries may be issued, either because the object type is heterogeneous or for performance reasons (for example, one query for heap tables, one for index-organized tables). Consequently the `FETCH_xxx` calls may in fact be fetches from different underlying cursors (meaning that read consistency is not guaranteed).

Caution:

Do not run functions and procedures within a query, because they can fail when the handle is for an open context for a heterogeneous object.

Exceptions

Most exceptions raised during execution of the query are propagated to the caller. Also, the following exceptions may be raised:

- `INVALID_ARGVAL`. A `NULL` or invalid value was supplied for an input parameter. The error message text identifies the parameter.
- `INCONSISTENT_OPERATION`. Either `FETCH_XML` was called when the DDL transform had been specified, or `FETCH_DD` L was called when the DDL transform had not been specified.

#### 112.6.5 GET\_xxx Functions

`GET_xxx` functions let you fetch metadata for objects with a single call.

Syntax

```
DBMS_METADATA.GET_XML (
object_type     IN VARCHAR2,
name            IN VARCHAR2,
schema          IN VARCHAR2 DEFAULT NULL,
version         IN VARCHAR2 DEFAULT 'COMPATIBLE',
model           IN VARCHAR2 DEFAULT 'ORACLE',
transform       IN VARCHAR2 DEFAULT NULL)
RETURN CLOB;

DBMS_METADATA.GET_DDL (
object_type     IN VARCHAR2,
name            IN VARCHAR2,
schema          IN VARCHAR2 DEFAULT NULL,
version         IN VARCHAR2 DEFAULT 'COMPATIBLE',
model           IN VARCHAR2 DEFAULT 'ORACLE',
transform       IN VARCHAR2 DEFAULT 'DDL')
RETURN CLOB;

DBMS_METADATA.GET_SXML (
object_type     IN VARCHAR2,
name            IN VARCHAR2 DEFAULT NULL,
schema          IN VARCHAR2 DEFAULT NULL,
version         IN VARCHAR2 DEFAULT 'COMPATIBLE',
model           IN VARCHAR2 DEFAULT 'ORACLE',
transform       IN VARCHAR2 DEFAULT 'SXML')
RETURN CLOB;

DBMS_METADATA.GET_DEPENDENT_XML (
object_type        IN VARCHAR2,
base_object_name   IN VARCHAR2,
base_object_schema IN VARCHAR2 DEFAULT NULL,
version            IN VARCHAR2 DEFAULT 'COMPATIBLE',
model              IN VARCHAR2 DEFAULT 'ORACLE',
transform          IN VARCHAR2 DEFAULT NULL,
object_count       IN NUMBER   DEFAULT 10000)
RETURN CLOB;

DBMS_METADATA.GET_DEPENDENT_DDL (
object_type         IN VARCHAR2,
base_object_name    IN VARCHAR2,
base_object_schema  IN VARCHAR2 DEFAULT NULL,
version             IN VARCHAR2 DEFAULT 'COMPATIBLE',
model               IN VARCHAR2 DEFAULT 'ORACLE',
transform           IN VARCHAR2 DEFAULT 'DDL',
object_count        IN NUMBER   DEFAULT 10000)
RETURN CLOB;

DBMS_METADATA.GET_GRANTED_XML (
object_type     IN VARCHAR2,
grantee         IN VARCHAR2 DEFAULT NULL,
version         IN VARCHAR2 DEFAULT 'COMPATIBLE',
model           IN VARCHAR2 DEFAULT 'ORACLE',
transform       IN VARCHAR2 DEFAULT NULL,
object_count    IN NUMBER   DEFAULT 10000)
RETURN CLOB;

DBMS_METADATA.GET_GRANTED_DDL (
object_type     IN VARCHAR2,
grantee         IN VARCHAR2 DEFAULT NULL,
version         IN VARCHAR2 DEFAULT 'COMPATIBLE',
model           IN VARCHAR2 DEFAULT 'ORACLE',
transform       IN VARCHAR2 DEFAULT 'DDL',
object_count    IN NUMBER   DEFAULT 10000)
RETURN CLOB;
```

Parameters

Table 112-9 GET\_xxx Function Parameters

| Parameter | Description |
| --- | --- |
| `object_type` | The type of object to be retrieved. This parameter takes the same values as the `OPEN object_type` parameter, except that it cannot be a heterogeneous object type. The attributes of the object type must be appropriate to the function. That is, for `GET_xxx` it must be a named object. |
| `name` | The object name. It is used internally in a `NAME` filter. (If the name is longer than 30 characters, it will be used in a `LONGNAME` filter.) If this parameter is NULL, then no `NAME` or `LONGNAME` filter is specified. See Table 112-18 for a list of filters. |
| `schema` | The object schema. It is used internally in a `SCHEMA` filter. The default is the current user. |
| `version` | The version of metadata to be extracted. This parameter takes the same values as the `OPEN` version parameter. |
| `model` | The object model to use. This parameter takes the same values as the `OPEN` model parameter. |
| `transform` | The name of a transformation on the output. This parameter takes the same values as the `ADD_TRANSFORM` `name` parameter. For `GET_XML` this must not be `DDL`. |
| `base_object_name` | The base object name. It is used internally in a `BASE_OBJECT_NAME` filter. |
| `base_object_schema` | The base object schema. It is used internally in a `BASE_OBJECT_SCHEMA` filter. The default is the current user. |
| `grantee` | The grantee. It is used internally in a `GRANTEE` filter. The default is the current user. |
| `object_count` | The maximum number of objects to return. See SET\_COUNT Procedure. |

Return Values

The metadata for the specified object as XML or DDL.

Usage Notes

- These functions allow you to fetch metadata for objects with a single call. They encapsulate calls to `OPEN`, `SET_FILTER`, and so on. The function you use depends on the characteristics of the object type and on whether you want XML, SXML, or DDL.
	- `GET_xxx` is used to fetch named objects, especially schema objects (tables, views).
		- `GET_DEPENDENT_xxx` is used to fetch dependent objects (audits, object grants).
		- `GET_GRANTED_xxx` is used to fetch granted objects (system grants, role grants).
- For some object types you can use more than one function. For example, you can use `GET_xxx` to fetch an index by name, or `GET_DEPENDENT_xxx` to fetch the same index by specifying the table on which it is defined.
- `GET_xxx` only returns a single named object.
- For `GET_DEPENDENT_xxx` and `GET_GRANTED_xxx,` an arbitrary number of dependent or granted objects can match the input criteria. You can specify an object count when fetching these objects. (The default count of 10000 should be adequate in most cases.)
- If the DDL transform is specified, session-level transform parameters are inherited.
- If you invoke these functions from SQL\*Plus, you should set the `PAGESIZE` to 0 and set `LONG` to some large number to get complete, uninterrupted output.
- Currently, `GET_DDL` for a `USER` object does not return the `CONTAINER` clause.

Exceptions

- `INVALID_ARGVAL`. A `NULL` or invalid value was supplied for an input parameter. The error message text identifies the parameter.
- `OBJECT_NOT_FOUND`. The specified object was not found in the database.

Examples

Example: Fetch the XML Representation of SCOTT.EMP

To generate complete, uninterrupted output, set the `PAGESIZE` to 0 and set `LONG` to some large number, as shown, before executing your query.

```
SET LONG 2000000
SET PAGESIZE 0
SELECT DBMS_METADATA.GET_XML('TABLE','EMP','SCOTT')
FROM DUAL;
```

Example: Fetch the DDL for all Complete Tables in the Current Schema, Filter Out Nested Tables and Overflow Segments

This example fetches the DDL for all "complete" tables in the current schema, filtering out nested tables and overflow segments. The example uses `SET_TRANSFORM_PARAM` (with the handle value = `DBMS_METADATA.SESSION_TRANSFORM` meaning "for the current session") to specify that storage clauses are not to be returned in the SQL DDL. Afterwards, the example resets the session-level parameters to their defaults.

To generate complete, uninterrupted output, set the `PAGESIZE` to 0 and set `LONG` to some large number, as shown, before executing your query.

```
SET LONG 2000000
SET PAGESIZE 0
EXECUTE DBMS_METADATA.SET_TRANSFORM_PARAM(DBMS_METADATA.SESSION_TRANSFORM,'STORAGE',false);
SELECT DBMS_METADATA.GET_DDL('TABLE',u.table_name)
     FROM USER_ALL_TABLES u
     WHERE u.nested='NO' 
     AND (u.iot_type is null or u.iot_type='IOT');
EXECUTE DBMS_METADATA.SET_TRANSFORM_PARAM(DBMS_METADATA.SESSION_TRANSFORM,'DEFAULT');
```

Example: Fetch the DDL For All Object Grants On HR.EMPLOYEES

```
SELECT DBMS_METADATA.GET_DEPENDENT_DDL('OBJECT_GRANT',
    'EMPLOYEES','HR') FROM DUAL;
```

Example: Fetch the DDL For All System Grants Granted To SCOTT

```
SELECT DBMS_METADATA.GET_GRANTED_DDL('SYSTEM_GRANT','SCOTT')
    FROM DUAL;
```

#### 112.6.6 GET\_QUERY Function

This function returns the text of the queries that are used by `FETCH_xxx`. This function assists in debugging.

Syntax

```
DBMS_METADATA.GET_QUERY (
   handle  IN NUMBER)
 RETURN VARCHAR2;
```

Parameters

Table 112-10 GET\_QUERY Function Parameters

| Parameter | Description |
| --- | --- |
| `handle` | The handle returned from `OPEN`. It cannot be the handle for a heterogeneous object type. |

Return Values

The text of the queries that will be used by `FETCH_xxx.`

Exceptions

- `INVALID_ARGVAL`. A `NULL` or invalid value was supplied for the `handle ` parameter.

#### 112.6.7 OPEN Function

The `DBMS_METADATA.OPEN` function specifies the type of object to be retrieved, the version of its metadata, and the object model.

The return value is an opaque context handle for the set of objects to be used in subsequent calls.

Syntax

```
DBMS_METADATA.OPEN (
   object_type  IN VARCHAR2,
   version      IN VARCHAR2 DEFAULT 'COMPATIBLE',
   model        IN VARCHAR2 DEFAULT 'ORACLE', 
   network_link IN VARCHAR2 DEFAULT NULL)
 RETURN NUMBER;
```

Parameters

Table 112-11 Open Function Parameters

| Parameter | Description |
| --- | --- |
| `object_type` | The type of object to be retrieved. The table `DBMS_METADATA`: Object Types lists the valid type names and their meanings. These object types are supported for the `ORACLE` model of metadata (see `model` in this table).  The Attributes column in the `DBMS_METADATA`: Object Types table specifies some object type attributes:  - Schema objects, such as tables, belong to schemas. - Named objects have unique names (if they are schema objects, the name is unique to the schema). - Dependent objects, such as indexes, are defined with reference to a base schema object. - Granted objects are granted or assigned to a user or role and therefore have a named grantee. - Heterogeneous object types denote a collection of related objects of different types. See the table "Object Types Returned for the Heterogeneous Object Type" for a listing of object types returned for the heterogeneous object type.  These attributes are relevant when choosing object selection criteria. See " SET\_FILTER Procedure " for more information. |
| `version` | The version of metadata to be extracted. Database objects or attributes that are incompatible with the version will not be extracted. Legal values for this parameter are as follows:  `COMPATIBLE` (default)—the version of the metadata corresponds to the database compatibility level.  `LATEST` —the version of the metadata corresponds to the database version.  A specific database version. The value cannot be lower than 9.2.0. |
| `model` | Specifies which view to use, because the API can support multiple views on the metadata. Only the `ORACLE` model is supported. |
| `network_link` | The name of a database link to the database whose metadata is to be retrieved. If `NULL` (the default), then metadata is retrieved from the database on which the caller is running |

The table "DBMS\_METADATA: Object Types" provides the name, meaning, attributes, and notes for the `DBMS_METADATA` package object types. In the attributes column, `S` represents a schema object, `N` represents a named object, `D` represents a dependent object, `G` represents a granted object, and `H` represents a heterogeneous object.

Table 112-12 DBMS\_METADATA: Object Types

| Type Name | Meaning | Attributes | Notes |
| --- | --- | --- | --- |
| `AQ_QUEUE` | queues | `SND` | Dependent on table |
| `AQ_QUEUE_TABLE` | additional metadata for queue tables | `ND` | Dependent on table |
| `AQ_TRANSFORM` | transforms | `SN` | None |
| `ASSOCIATION` | associate statistics | `D` | None |
| `AUDIT` | audits of SQL statements | `DG` | Modeled as dependent, granted object. The base object name is the statement audit option name (for example, `ALTER` `SYSTEM`). There is no base object schema. The grantee is the user or proxy whose statements are audited. |
| `AUDIT_OBJ` | audits of schema objects | `D` | None |
| `CLUSTER` | clusters | `SN` | None |