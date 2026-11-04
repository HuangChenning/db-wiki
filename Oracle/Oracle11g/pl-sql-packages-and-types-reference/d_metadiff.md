---
title: DBMS_METADATA_DIFF
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_metadiff.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 88 DBMS\_METADATA\_DIFF

The `DBMS_METADATA_DIFF` package contains the interfaces for comparing two metadata documents in SXML format.

See Also:

[Oracle Database Utilities](https://docs.oracle.com/cd/E11882_01/server.112/e22490/toc.htm) for more information and for examples of using the Metadata API

This chapter contains the following topics:

---

## Using DBMS\_METADATA\_DIFF

This section contains topics which relate to using the `DBMS_METADATA_DIFF` package.

---

### Overview

You can use the interfaces contained in the `DBMS_METADATA_DIFF` package to compare two metadata documents in SXML format. The result of the comparison is an SXML difference document. This document can be converted to other formats using the `DBMS_METADATA` submit interface and the `CONVERT` API.

---

### Security Model

The browsing interface of the `DBMS_METADATA_DIFF` package actually uses the `DBMS_METADATA` package to fetch the metadata to be compared. Therefore, the security model used for `DBMS_METADATA` also applies to `DBMS_METADATA_DIFF`. (Note, however, that `DBMS_METADATA_DIFF` does not support all object types.)

See Also:

[DBMS\_METADATA](d_metada.md) for information about the DBMS\_METADATA security model

---

## Browsing APIs for Fetching and Comparing Objects

These functions allow you to compare the metadata for two objects with a single call.

Syntax

```
DBMS_METADATA_DIFF.COMPARE_SXML(
object_type   IN VARCHAR2,
name1         IN VARCHAR2,
name2         IN VARCHAR2,
schema1       IN VARCHAR2 DEFAULT NULL,
schema2       IN VARCHAR2 DEFAULT NULL,
network_link1 IN VARCHAR2 DEFAULT NULL,
network_link2 IN VARCHAR2 DEFAULT NULL)
RETURN CLOB;

DBMS_METADATA_DIFF.COMPARE_ALTER(
object_type   IN VARCHAR2,
name1         IN VARCHAR2,
name2         IN VARCHAR2,
schema1       IN VARCHAR2 DEFAULT NULL,
schema2       IN VARCHAR2 DEFAULT NULL,
network_link1 IN VARCHAR2 DEFAULT NULL,
network_link2 IN VARCHAR2 DEFAULT NULL)
RETURN CLOB;

DBMS_METADATA_DIFF.COMPARE_ALTER_XML(
object_type   IN VARCHAR2,
name1         IN VARCHAR2,
name2         IN VARCHAR2,
schema1       IN VARCHAR2 DEFAULT NULL,
schema2       IN VARCHAR2 DEFAULT NULL,
network_link1 IN VARCHAR2 DEFAULT NULL,
network_link2 IN VARCHAR2 DEFAULT NULL)
RETURN CLOB;
```

Parameters

Table 88-1 COMPARE\_xxx Function Parameters

| Parameters | Description |
| --- | --- |
| `object_type` | The type of object to be compared. Valid type names are `CLUSTER`, `CONTEXT`, `DB_LINK`, `FGA_POLICY`, `INDEX`, `MATERIALIZED_VIEW`, `MATERIALIZED_VIEW_LOG`, `QUEUE`, `QUEUE_TABLE`, `RLS_CONTEXT`, `RLS_GROUP`, `RLS_POLICY`, `ROLE`, `SEQUENCE`, `SYNONYM`, `TABLE`, `TABLESPACE`, `TRIGGER`, `TYPE`, `TYPE_SPEC`, `TYPE_BODY`, `USER`, and `VIEW`. |
| `name1` | The name of the first object in the comparison. |
| `name2` | The name of the second object in the comparison. |
| `schema1` | The schema of the first object in the comparison. The default is the current user. |
| `schema2` | The schema of the second object in the comparison. The default is the value of `schema1`. |
| `network_link1` | The name of a database link to the database on which the first object resides. If NULL (the default), then the object is assumed to be in the database on which the caller is running. |
| `network_link2` | The name of a database link to the database on which the second object resides. The default is the value of `network_link1`. |

Return Values

`DBMS_METADATA_DIFF.COMPARE_xxx` returns the differences between two objects.

Exceptions

- `INVALID_ARGVAL`
	A `NULL` or invalid value was supplied for an input parameter. The error message text identifies the parameter.
- `OBJECT_NOT_FOUND`
	The specified object was not found in the database.

Usage Notes

These functions encapsulate calls to both `DBMS_METADATA` and `DBMS_METADATA_DIFF` functions and procedures to fetch the metadata for each of the two objects and compare them.

Which function you use depends on the comparison format you want:

- `COMPARE_SXML` returns an SXML difference document.
- `COMPARE_ALTER` returns a set of `ALTER` statements for making the first object like the second object.
- `COMPARE_ALTER_XML` returns an `ALTER_XML` document.

---

## Summary of DBMS\_METADATA\_DIFF Subprograms

The `DBMS_METADATA_DIFF` subprograms are used to:

- Specify the type of objects to be compared
- Specify the SXML documents to be compared
- Show the differences between the compared documents
- Clean up after the comparison

Table 88-2 provides a summary of `DBMS_METADATA_DIFF` subprograms.

Table 88-2 DBMS\_METADATA\_DIFF Package Subprograms

| Subprogram | Description |
| --- | --- |
| OPENC Function | Specifies the type of objects to be compared |
| ADD\_DOCUMENT Procedure | Specifies an SXML document to be compared |
| FETCH\_CLOB Functions and Procedures | Returns a CLOB showing the differences between the two documents specified by `ADD_DOCUMENT` |
| CLOSE Procedure | Invalidates the handle returned by `OPENC` and cleans up associated state |

---

### OPENC Function

This function specifies the type of objects to be compared. The return value is an opaque context handle.

Syntax

```
DBMS_METADATA_DIFF.OPENC (
object_type  IN VARCHAR2)
RETURN NUMBER;
```

Parameters

Table 88-3 OPENC Function Parameters

| Parameters | Description |
| --- | --- |
| `object_type` | The type of object to be compared. Valid type names are `CLUSTER`, `CONTEXT`, `DB_LINK`, `FGA_POLICY`, `INDEX`, `MATERIALIZED_VIEW`, `MATERIALIZED_VIEW_LOG`, `QUEUE`, `QUEUE_TABLE`, `RLS_CONTEXT`, `RLS_GROUP`, `RLS_POLICY`, `ROLE`, `SEQUENCE`, `SYNONYM`, `TABLE`, `TABLESPACE`, `TRIGGER`, `TYPE`, `TYPE_SPEC`, `TYPE_BODY`, `USER`, and `VIEW`. |

Return Values

The opaque handle that is returned is used as input to `ADD_DOCUMENT`, `FETCH_xxx` and `CLOSE`.

Exceptions

- `INVALID_ARGVAL`
	A `NULL` or invalid value was supplied for an input parameter. The error message text identifies the parameter.

---

### ADD\_DOCUMENT Procedure

This procedure specifies an SXML document to be compared.

Syntax

```
DBMS_METADATA_DIFF.ADD_DOCUMENT(
handle IN NUMBER, document IN sys.XMLType);

DBMS_METADATA_DIFF.ADD_DOCUMENT(
handle IN NUMBER, document IN CLOB);
```

Parameters

Table 88-4 CLOSE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `handle` | The handle returned from `OPENC` |
| `document` | A document to be compared. The document must be of the type specified in `OPENC`. |

Usage Notes

Because the comparison interface allows you to compare exactly two SXML documents, a program must call `ADD_DOCUMENT` exactly twice for each `OPENC` handle. In the comparison result, the document specified by the first call is document 1, and the document specified by the second call is document 2.

Exceptions

- `INVALID_ARGVAL`
	A `NULL` or invalid value was supplied for an input parameter. The error message text identifies the parameter.

---

### FETCH\_CLOB Functions and Procedures

The `FETCH_CLOB` functions and procedures return a CLOB showing the differences between the two documents specified by `ADD_DOCUMENT`.

Syntax

```
DBMS_METADATA_DIFF.FETCH_CLOB(
handle IN NUMBER)
RETURN CLOB;

DBMS_METADATA_DIFF.FETCH_CLOB(
```
```
handle IN  NUMBER, 
doc    IN  OUT NOCOPY CLOB);

DBMS_METADATA_DIFF.FETCH_CLOB(
handle IN  NUMBER, 
doc    IN  OUT NOCOPY CLOB 
diffs  OUT BOOLEAN);
```

Parameters

Table 88-5 CONVERT Subprogram Parameters

| Parameter | Description |
| --- | --- |
| `handle` | The handle returned from `OPENC`. |
| `doc` | A CLOB containing the differences between documents 1 and 2. |
| `diffs` | `TRUE` if the documents are different or `FALSE` if they are identical. |

Return Values

The differences between documents 1 and 2.

Exceptions

- `INVALID_ARGVAL`
	A `NULL` or invalid value was supplied for an input parameter. The error message text identifies the parameter.

---

### CLOSE Procedure

This procedure invalidates the handle returned by `OPENC` and cleans up associated state.

Syntax

```
DBMS_METADATA_DIFF.CLOSE(
handle IN NUMBER);
```

Parameters

Table 88-6 FETCH\_xxx Function Parameters

| Parameters | Description |
| --- | --- |
| `handle` | The handle returned from `OPENC` |

Exceptions

- `INVALID_ARGVAL`
	A `NULL` or invalid value was supplied for an input parameter. The error message text identifies the parameter.