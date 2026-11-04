---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/DBMS_CSX_ADMIN.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 48 DBMS\_CSX\_ADMIN

The `DBMS_CSX_ADMIN` package provides an interface to customize the setup when transporting a tablespace containing binary XML data.

The chapter contains the following topics:

### 48.1 DBMS\_CSX\_ADMIN Overview

This package can be used by DBAs to customize the setup when transporting a tablespace containing binary XML data. The use of the package is not required in order for a transportable tablespace job to run.

By default, all binary XML tables will use the default token table set, which will be replicated during transport on the target database. To avoid the cost of transporting a potentially large token table set, the DBA may opt for registering a new set of token tables for a given tablespace. The package provides routines for token table set registration and lookup.

### 48.2 DBMS\_CSX\_ADMIN Security Model

Owned by `XDB`, the `DBMS_CSX_ADMIN` package must be created by `SYS` or `XDB`. The `EXECUTE` privilege is granted to `SYS` or `XDB` or `DBA`. Subprograms in this package are executed using the privileges of the current user.

### 48.3 DBMS\_CSX\_ADMIN Constants

The `DBMS_CSX_ADMIN` package uses several constants.

These are described in the following table.

Table 48-1 DBMS\_CSX\_ADMIN Constants

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

### 48.4 Summary of DBMS\_CSX\_ADMIN Subprograms

This table lists and describes the `DBMS_CSX_ADMIN` Package subprograms.

Table 48-2 DBMS\_CSX\_ADMIN Package Subprograms

| Subprogram | Description |
| --- | --- |
| GETTOKENTABLEINFO Procedure & Function | Returns the GUID of the token table set where token mappings for this table |
| GETTOKENTABLEINFOBYTABLESPACE Procedure | Returns the GUID and the token table names for this tablespace |
| NAMESPACEIDTABLE Function | Returns default namespace-ID token table |
| PATHIDTABLE Function | Returns the default path-ID token table |
| QNAMEIDTABLE Function | Returns the default qname-ID token table. |

#### 48.4.1 GETTOKENTABLEINFO Procedure & Function

This procedure is overloaded. The specific forms of functionality are described along with the syntax declarations.

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

Table 48-3 GETTOKENTABLEINFO Procedure & Function Parameters

| Parameter | Description |
| --- | --- |
| `ownername` | Owner of the table |
| `tablename` | Name of the table |
| `guid` | GUID of the token table set used by the given table |
| `qnametable` | Name of the qname-ID table in the new set |
| `nmspctable` | Name of the namespace-ID table in the new set |
| `level` | `DEFAULT_LEVEL` if default token table set, `TBS_LEVEL` if same token table set is used by all tables in the same tablespace as the given table, `TAB_LEVEL` otherwise |
| `tabno` | Table object number |

#### 48.4.2 GETTOKENTABLEINFOBYTABLESPACE Procedure

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

Table 48-4 GETTOKENTABLEINFOBYTABLESPACE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `tsname` | Tablespace name |
| `tablespaceno` | Tablespace number |
| `guid` | GUID of the token table set associated with this tablespace (if any) |
| `qnametable` | Name of the qname-ID table |
| `nmspctable` | Name of the namespace-ID table |
| `isdefault` | `TRUE` if the token table is the default one |
| `containTokTab` | `TRUE` if the tablespace contains its own token table set |

#### 48.4.3 NAMESPACEIDTABLE Function

This procedure returns default namespace-ID token table.

Syntax

```
DBMS_CSX_ADMIN.NAMESPACEIDTABLE 
  RETURN VARCHAR2;
```

#### 48.4.4 PATHIDTABLE Function

This procedure returns the default path-ID token table. This is used for granting permissions on the default path-ID token table for a user before executing `EXPLAIN PLAN` for a query on an XML table with an XML index.

Syntax

```
DBMS_CSX_ADMIN.PATHIDTABLE 
  RETURN VARCHAR2;
```

#### 48.4.5 QNAMEIDTABLE Function

This procedure returns the default qname-ID token table.

Syntax

```
DBMS_CSX_ADMIN.QNAMEIDTABLE 
  RETURN VARCHAR2;
```