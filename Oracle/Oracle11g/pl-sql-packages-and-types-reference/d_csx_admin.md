---
title: DBMS_CSX_ADMIN
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_csx_admin.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 40 DBMS\_CSX\_ADMIN

The `DBMS_CSX_ADMIN` package provides an interface to customize the setup when transporting a tablespace containing binary XML data.

The chapter contains the following topics:

- Using DBMS\_CSX\_ADMIN
- Summary of DBMS\_CSX\_ADMIN

---

## Using DBMS\_CSX\_ADMIN

---

### Overview

This package can be used by DBAs to customize the setup when transporting a tablespace containing binary XML data. The use of the package is not required in order for a transportable tablespace job to run.

By default, all binary XML tables will use the default token table set, which will be replicated during transport on the target database. To avoid the cost of transporting a potentially large token table set, the DBA may opt for registering a new set of token tables for a given tablespace. The package provides routines for token table set registration and lookup.

---

### Security Model

Owned by `XDB`, the `DBMS_CSX_ADMIN` package must be created by `SYS` or `XDB`. The `EXECUTE` privilege is granted to `SYS` or `XDB` or `DBA`. Subprograms in this package are executed using the privileges of the current user.

---

### Constants

The `DBMS_CSX_ADMIN` package uses the constants shown in Table 40-1:

Table 40-1 DBMS\_CSX\_ADMIN Constants

| Name | Type | Value | Description |
| --- | --- | --- | --- |
| `DEFAULT_LEVEL` | `BINARY_INTEGER` | `0` | Default token table |
| `TAB_LEVEL` | `BINARY_INTEGER` | `1` | Token table set associated with tables, not tablespaces |
| `TBS_LEVEL` | `BINARY_INTEGER` | `2` | Token table set associated with a tablespace |
| `NO_CREATE` | `BINARY_INTEGER` | `0` | Token tables already exist, associate them with the given table/tablespace |
| `NO_INDEXES` | `BINARY_INTEGER` | `1` | Do not create indexes on the new set of token tables |
| `WITH_INDEXES` | `BINARY_INTEGER` | `2` | Create indexes on the token tables |
| `DEFAULT_TOKS` | `BINARY_INTEGER` | `0` | Prepopulate the token tables with default token mappings |
| `NO_DEFAULT_TOKS` | `BINARY_INTEGER` | `1` | Do not prepopulate the token tables with default token mappings |

---

### Examples

Example 1: Register a New Set of Token Tables for the Tablespace

To prepare a tablespace CSXTS for export, the DBA can register a new set of token tables for the tablespace with the following PL/SQL:

```
DECLARE
  tsno   number;
  stmt   varchar2(2000);
BEGIN
  stmt := 'SELECT ts# FROM ts$ WHERE (name = ''' || 'CSXTS' || ''')';
  EXECUTE IMMEDIATE stmt into tsno;
  DBMS_CSX_ADMIN.REGISTERTOKENTABLESET(
    tstabno     =>  tsno, 
    guid        =>  NULL,
    flags       =>  DBMS_CSX_ADMIN.TBS_LEVEL, 
    tocreate    =>  DBMS_CSX_ADMIN.WITH_INDEXES,
    defaulttoks =>  DBMS_CSX_ADMIN.DEFAULT_TOKS);
  COMMIT;
END;
/
```

In this example, the new token tables are indexed, populated with default token mappings, and associated with all tables in the `CSXTS` tablespace. All subsequent loads of binary XML data in `CSXTS` will make use of the new set of token tables. The advantage is that no loading of binary XML data in other tablespaces will affect the size of the token tables used by `CSXTS` and exported during a tablespace export of `CSXTS`. This setup is suited to the case in which the tablespace does not yet contain binary XML data.

Example 2: Copying the Default Token Tables in a New Set

If binary XML data already exists in the tablespace to be exported, the DBA has the option of copying the default token tables in a new set.

```
DECLARE
  tsno   number;
  stmt   varchar2(2000);
  qntab  varchar2(34);
  nmtab  varchar2(34);
  pttab  varchar2(34);
BEGIN
  stmt := 'select ts# from ts$ where (name = ''' || 'CSXTS' || ''')';
  EXECUTE IMMEDIATE stmt INTO tsno;
  DBMS_CSX_ADMIN.COPYDEFAULTTOKENTABLESET(
    tstabno => tsno, qntab, nmtab, pttatb);
  COMMIT;
END;
/
```

This setup is suited to the case in which the DBA wishes to optimize the export of a tablespace that already contains binary XML data, and does not have associated a token table set. After cloning the default token table set, all subsequent loads of binary XML data in `CSXTS` will make use of the new set of token tables.

---

## Summary of DBMS\_CSX\_ADMIN

Table 40-2 DBMS\_CSX\_ADMIN Package Subprograms

| Subprogram | Description |
| --- | --- |
| COPYDEFAULTTOKENTABLESET Procedure | Creates a new token table set associated with a given tablespace, and populates the token tables with the token mappings from the default token tables |
| GETTOKENTABLEINFO Procedure & Function | Returns the GUID of the token table set where token mappings for this table |
| GETTOKENTABLEINFOBYTABLESPACE Procedure | Returns the GUID and the token table names for this tablespace |
| NAMESPACEIDTABLE Function | Returns default namespace-ID token table |
| PATHIDTABLE Function | Returns the default path-ID token table |
| QNAMEIDTABLE Function | Returns the default qname-ID token table. |
| REGISTERTOKENTABLESET Procedure | Registers a new token table set, creates (if required) the token tables (with the corresponding indexes) |

---

### COPYDEFAULTTOKENTABLESET Procedure

This procedure creates a new token table set associated with a given tablespace, and populates the token tables with the token mappings from the default token tables.

Syntax

```
DBMS_CSX_ADMIN.COPYDEFAULTTOKENTABLESET  (
   tsno         IN    NUMBER,
   qnametable   OUT   VARCHAR2,
   nmspctable   OUT   VARCHAR2,
   pttable      OUT   VARCHAR2);
```

Parameters

Table 40-3 COPYDEFAULTTOKENTABLESET Procedure Parameters

| Parameter | Description |
| --- | --- |
| `tsno` | Tablespace number the new set of token tables will be associated with |
| `qnametable` | Name of the qname-ID table in the new set |
| `nmspctable` | Name of the namespace-ID table in the new set |
| `pttable` | Name of the path-id table in the new set |

---

### GETTOKENTABLEINFO Procedure & Function

Given the table name and the owner, the first overload of the procedure returns the globally unique identifier (GUID) of the token table set where token mappings for this table can be found. The procedure returns also the names of the token tables, and whether the token table set is the default one.

Given the object number of a table, the second overload of the procedure returns the GUID of the token table set used by the table, and whether this is the default token table set.

Syntax

```
DBMS_CSX_ADMIN.GETTOKENTABLEINFO  (
   ownername      IN   VARCHAR2,
   tablename      IN   VARCHAR2,
   guid           OUT  RAW,
   qnametable     OUT  VARCHAR2,
   nmspctable     OUT  VARCHAR2,
   level          OUT  NUMBER,
   tabno          OUT  NUMBER);
```
```
DBMS_CSX_ADMIN.GETTOKENTABLEINFO  (
   tabno          IN   NUMBER,
   guid           OUT  RAW);
 RETURN BOOLEAN;
```

Parameters

Table 40-4 GETTOKENTABLEINFO Procedure & Function Parameters

| Parameter | Description |
| --- | --- |
| `ownername` | Owner of the table |
| `tablename` | Name of the table |
| `guid` | GUID of the token table set used by the given table |
| `qnametable` | Name of the qname-ID table in the new set |
| `nmspctable` | Name of the namespace-ID table in the new set |
| `level` | `DEFAULT_LEVEL` if default token table set, `TBS_LEVEL` if same token table set is used by all tables in the same tablespace as the given table, `TAB_LEVEL` otherwise |
| `tabno` | Table object number |

---

### GETTOKENTABLEINFOBYTABLESPACE Procedure

Given a tablespace number, this procedure returns the GUID and the token table names for this tablespace.

Syntax

```
DBMS_CSX_ADMIN.GETTOKENTABLEINFOBYTABLESPACE  (
   tsname          IN   VARCHAR2,
   tablespaceno    IN   NUMBER,
   guid            OUT  RAW,
   qnametable      OUT  VARCHAR2,
   nmspctable      OUT  VARCHAR2,
   isdefault       OUT  BOOLEAN,
   containTokTab   OUT  BOOLEAN);
```

Parameters

Table 40-5 GETTOKENTABLEINFOBYTABLESPACE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `tsname` | Tablespace name |
| `tablespaceno` | Tablespace number |
| `guid` | GUID of the token table set associated with this tablespace (if any) |
| `qnametable` | Name of the qname-ID table |
| `nmspctable` | Name of the namespace-ID table |
| `isdefault` | `TRUE` if the token table is the default one |
| `containTokTab` | `TRUE` if the tablespace contains its own token table set |

---

### NAMESPACEIDTABLE Function

This procedure returns default namespace-ID token table.

Syntax

```
DBMS_CSX_ADMIN.NAMESPACEIDTABLE 
  RETURN VARCHAR2;
```

---

### PATHIDTABLE Function

This procedure returns the default path-ID token table. This is used for granting permissions on the default path-ID token table for a user before executing `EXPLAIN` `PLAN` for a query on an XML table with an XML index.

Syntax

```
DBMS_CSX_ADMIN.PATHIDTABLE 
  RETURN VARCHAR2;
```

---

### QNAMEIDTABLE Function

This procedure returns the default qname-ID token table.

Syntax

```
DBMS_CSX_ADMIN.QNAMEIDTABLE 
  RETURN VARCHAR2;
```

---

### REGISTERTOKENTABLESET Procedure

This procedure registers a new token table set, creates (if required) the token tables (with the corresponding indexes).

Syntax

```
DBMS_CSX_ADMIN.REGISTERTOKENTABLESET  (
   tstabno      IN  NUMBER  DEFAULT NULL,
   guid         IN  RAW     DEFAULT NULL, 
   flags        IN  NUMBER  DEFAULT TBS_LEVEL,
   tocreate     IN  NUMBER  DEFAULT WITH_INDEXES,
   defaulttoks  IN  NUMBER  DEFAULT DEFAULT_TOKS);
```

Parameters

Table 40-6 REGISTERTOKENTABLESET Procedure Parameters

| Parameter | Description |
| --- | --- |
| `tstabno` | Tablespace/table number of the tablespace/table using the set of token table we register |
| `guid` | GUID of the token table set. If `NULL`, a new identifier is created, provided the user is `SYS`. |
| `flags` | `TAB_LEVEL` for table level, `TBS_LEVEL` for tablespace level |
| `tocreate` | Possible values:  - `NO_CREATE` if no token tables are created - `NO_INDEXES` if token tables are created, but no indexes - `WITH_INDEXES` if token tables and corresponding indexes are created |
| `defaulttoks` | If `DEFAULT_TOKS`, insert default token mappings |