---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/DBMS_TYPES.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 190 DBMS\_TYPES

The `DBMS_TYPES` package consists of constants, which represent the built-in and user-defined types.

This chapter contains the following topics:

- Constants
- Exceptions

### 190.1 DBMS\_TYPES Constants

The `DBMS_TYPES` package defines several constants to use when specifying parameter values.

These constants are listed in following table.

Table 190-1 DBMS\_TYPES Constants

| Constant | Description |
| --- | --- |
| `NO_DATA` | Is only relevant if PieceWise is called, for a collection or any dataset. Denotes the end of collection/any dataset when all the elements have been accessed |
| `SUCCESS` | The operation succeeded |
| `TYPECODE_BDOUBLE` | A `NUMBER` type |
| `TYPECODE_BFILE` | A `BFILE` type |
| `TYPECODE_BFLOAT` | A `NUMBER` type |
| `TYPECODE_BLOB` | A `BLOB` type |
| `TYPECODE_CFILE` | A `CFILE` type |
| `TYPECODE_CHAR` | A `CHAR` type |
| `TYPECODE_CLOB` | A `CLOB` type |
| `TYPECODE_DATE` | A `DATE` type |
| `TYPECODE_INTERVAL_DS` | An `INTERVAL_DS` type |
| `TYPECODE_INTERVAL_YM` | A `INTERVAL_YM` type |
| `TYPECODE_MLSLABEL` | An `MLSLABEL` type |
| `TYPECODE_NAMEDCOLLECTION` | A named collection (`VARRAY` /nested table) type |
| `TYPECODE_NCHAR` | A `NCHAR` type |
| `TYPECODE_NCLOB` | A `NCLOB` type |
| `TYPECODE_NUMBER` | A `NUMBER` type |
| `TYPECODE_NVARCHAR2` | A `NVARCHAR2` type |
| `TYPECODE_OBJECT` | An `OBJECT` type |
| `TYPECODE_OPAQUE` | An `OPAQUE` type |
| `TYPECODE_RAW` | A `RAW` type |
| `TYPECODE_REF` | A `REF` type |
| `TYPECODE_TABLE` | A nested table collection type |
| `TYPECODE_TIMESTAMP` | A `TIMESTAMP` type |
| `TYPECODE_TIMESTAMP_LTZ` | A `TIMESTAMP_LTZ` type |
| `TYPECODE_TIMESTAMP_TZ` | A `TIMESTAMP_TZ` type |
| `TYPECODE_UROWID` | A `UROWID` type |
| `TYPECODE_VARCHAR2` | A `VARCHAR2` type |
| `TYPECODE_VARCHAR` | A `VARCHAR` type |
| `TYPECODE_VARRAY` | A `VARRAY` collection type |

### 190.2 DBMS\_TYPES Exceptions

`DBMS_TYPES` throws these exceptions.