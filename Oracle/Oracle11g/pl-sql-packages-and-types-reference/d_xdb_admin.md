---
title: DBMS_XDB_ADMIN
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_xdb_admin.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 165 DBMS\_XDB\_ADMIN

The `DBMS_XDB_ADMIN` package provides an interface to manage the Oracle XML DB repository.

See Also:

[Oracle XML DB Developer's Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=ADXDB6017) for information about the Oracle XML DB Repository

This chapter contains the following topics:

- Using DBMS\_XDB\_ADMIN
- Summary of DBMS\_XDB\_ADMIN Subprograms

---

## Using DBMS\_XDB\_ADMIN

- Deprecated Subprograms
- Security Model

---

### Deprecated Subprograms

Note:

Oracle recommends that you do not use deprecated procedures in new applications. Support for deprecated features is for backward compatibility only and may be terminated in future releases.

The following subprograms are deprecated with Oracle Database 11g:

---

### Security Model

Owned by `XDB`, the `DBMS_XDB_ADMIN` package must be created by `SYS` or `XDB`. The `EXECUTE` privilege is granted to `SYS` or `XDB` or `DBA`. Subprograms in this package are executed using the privileges of the current user.

---

## Summary of DBMS\_XDB\_ADMIN Subprograms

This table lists the package subprograms in alphabetical order.

Table 165-1 DBMS\_XDB\_ADM Package Subprograms

| Subprogram | Description |
| --- | --- |
| CREATEREPOSITORYXMLINDEX Procedure | \[Deprecated\] Creates an XMLIndex on the XML DB repository |
| DROPREPOSITORYXMLINDEX Procedure | \[Deprecated\] Drops the XMLIndex on the XML DB repository |
| MOVEXDB\_TABLESPACE Procedure | Moves the XDB (user) to the specified tablespace |
| REBUILDHIERARCHICALINDEX Procedure | Rebuilds the hierarchical index after import or export operations |
| XMLINDEXADDPATH Procedure | \[Deprecated\] Takes a path in XML DB repository as an input and index all the resources under this given path |
| XMLINDEXREMOVEPATH Procedure | \[Deprecated\] Removes the index for the given path |

---

### CREATEREPOSITORYXMLINDEX Procedure

Note:

This procedure is deprecated in Release 11g.

This procedure creates an XMLIndex on the XML DB repository.

Syntax

```
DBMS_XDB_ADMIN.CREATEREPOSITORYXMLINDEX;
```

---

### DROPREPOSITORYXMLINDEX Procedure

Note:

This procedure is deprecated in Release 11g.

This procedure drops the XMLIndex on the XML DB repository.

Syntax

```
DBMS_XDB_ADMIN.DROPREPOSITORYXMLINDEX;
```

---

### MOVEXDB\_TABLESPACE Procedure

This procedure moves the XDB (user) to the specified tablespace.

Syntax

```
DBMS_XDB.MOVEXDB_TABLESPACE(
   new_tablespace   IN  VARCHAR2);
```

Parameters

Table 165-2 MOVEXDB\_TABLESPACE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `new_tablespace` | Name of the tablespace to where the XDB is moved |

Usage Notes

- This operation waits for all concurrent XDB sessions to exit.
- If `MOVEXDB_TABLESPACE` fails, the user should restart the database before issuing any further command.Failure to do so will result into unexpected behavior from the database.

---

### REBUILDHIERARCHICALINDEX Procedure

This procedure rebuilds the hierarchical index after import or export operations. This is necessary because data cannot be exported from index tables.

Syntax

```
DBMS_XDB.REBUILDHIERARCHICALINDEX;
```

---

### XMLINDEXADDPATH Procedure

Note:

This procedure is deprecated in Release 11g.

This procedure adds to the repository xmlindex the resource identified by path (when `recurse` is `FALSE`) or adds to the repository xmlindex the sub-tree of resources rooted at path (when `recurse` is `TRUE`). The default value for `recurse` is `TRUE`.

Syntax

```
DBMS_XDB_ADMIN.XMLINDEXADDPATH(
   path         IN  VARCHAR2, 
   recurse      IN  BOOLEAN);
```

Parameters

Table 165-3 XMLINDEXADDPATH Procedure Parameters

| Parameter | Description |
| --- | --- |
| `path` | Path to a resource |
| `recurse` | `TRUE` or `FALSE` |

---

### XMLINDEXREMOVEPATH Procedure

Note:

This procedure is deprecated in Release 11g.

This procedure removes from the repository xmlindex the resource identified by path (when `recurse` is `FALSE`) or removes from the repository xmlindex the sub-tree of resources rooted at path (when `recurse` is `TRUE`). The default value for `recurse` is `TRUE`.

Syntax

```
DBMS_XDB_ADMIN.XMLINDEXREMOVEPATH(
   path              IN  VARCHAR2, 
   isrecursive       IN  BOOLEAN);
```

Parameters

Table 165-4 XMLINDEXREMOVEPATH Procedure Parameters

| Parameter | Description |
| --- | --- |
| `path` | Path to a resource |
| `recurse` | `TRUE` or `FALSE` |