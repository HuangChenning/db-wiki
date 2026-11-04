---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/DBFS-Content-Interface-Types.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 288 DBFS Content Interface Types

DBFS Content Interface Types are public types that support the `DBMS_DBFS_CONTENT` interface.

This chapter contains the following topics:

### 288.1 DDBFS Content Interface Types Overview

The type definitions described in this chapter support the DBMS\_DBFS\_CONTENT interface in implementing metadata tables, packages, views, dependent application-side entities, and service-provider entities.

### 288.2 DBFS Content Interface Types Security Model

The user can access the content operational and administrative interfaces (packages, types, tables, and so on) with the `DBFS_ROLE`. This role can be granted to users as needed.

### 288.3 DBFS Content Interface Types —Data Structures

Types that support the DBMS\_DBFS\_CONTENT interface include both Object and Table types.

Object Types

- DBMS\_DBFS\_CONTENT\_CONTEXT\_T Object Type
- DBMS\_DBFS\_CONTENT\_LIST\_ITEM\_T Object Type
- DBMS\_DBFS\_CONTENT\_PROPERTY\_T Object Type

Table Types

- DBMS\_DBFS\_CONTENT\_LIST\_ITEMS\_T Table Type
- DBMS\_DBFS\_CONTENT\_PROPERTIES\_T Table Type
- DBMS\_DBFS\_CONTENT\_RAW\_T Table Type

#### 288.3.1 DBMS\_DBFS\_CONTENT\_CONTEXT\_T Object Type

This type describes the execution context for the providers. It provides the user performing the operation with the Access Control List, the owner of the item(s), a timestamp for doing `asof` queries, and whether or not the item(s) are `read_only`. This type can be used both as input, in the case of path item creation functions, and output, in the case of path item query, or both.

Syntax

```
CREATE OR REPLACE TYPE dbms_dbfs_content_context_t
    AUTHID DEFINER
AS OBJECT (
    principal     VARCHAR2(32),
    acl           VARCHAR2(1024),
    owner         VARCHAR2(32),
    asof          TIMESTAMP,
    read_only     INTEGER);
```

Fields

Table 288-1 DBMS\_DBFS\_CONTENT\_CONTEXT\_T Fields

| Field | Description |
| --- | --- |
| `principal` | File system user |
| `acl` | Access control list |
| `owner` | Path item owner |
| `asof` | Timestamp |
| `read_only` | Nonzero if the path item is read-only |

#### 288.3.2 DBMS\_DBFS\_CONTENT\_LIST\_ITEM\_T Object Type

This type describes a type to assist in listing the contents of a directory.

Syntax

```
CREATE OR REPLACE TYPE dbms_dbfs_content_list_item_t
    AUTHID DEFINER
AS OBJECT (
    path          VARCHAR2(1024),
    item_name     VARCHAR2(256),
    item_type     INTEGER);
```

Fields

Table 288-2 DBMS\_DBFS\_CONTENT\_LIST\_ITEM\_T Fields

| Field | Description |
| --- | --- |
| `path` | Path to the path item |
| `item_name` | Name of the path item |
| `item_type` | Type of path item. (See [Table 57-4](DBMS_DBFS_CONTENT.md) |

#### 288.3.3 DBMS\_DBFS\_CONTENT\_PROPERTY\_T Object Type

This type describes a single (`name`, `value`, `typecode`) property tuple. All properties (standard, optional, and user-defined) are described using such tuples.

The type is used by both the client-facing interfaces and by store providers for the `DBMS_DBFS_CONTENT` interface.

Syntax

```
CREATE OR REPLACE TYPE dbms_dbfs_content_property_t
    AUTHID DEFINER
AS OBJECT (
    propname     VARCHAR2(32),
    propvalue    VARCHAR2(1024),
    typecode     INTEGER);
```

Fields

Table 288-3 DBMS\_DBFS\_CONTENT\_PROPERTY\_T Fields

| Field | Description |
| --- | --- |
| `prop_name` | Name of property |
| `prop_value` | Value of property |
| `typecode` | Property type (See Constants in DBMS\_TYPES) |

#### 288.3.4 DBMS\_DBFS\_CONTENT\_LIST\_ITEMS\_T Table Type

This type is a variable-sized array of DBMS\_DBFS\_CONTENT\_LIST\_ITEM\_T Object Type. It is used by both the client-facing interfaces and by store providers for the DBMS\_DBFS\_CONTENT interface.

Syntax

```
CREATE OR REPLACE TYPE dbms_dbfs_content_list_items_t AS
    TABLE OF dbms_dbfs_content_list_item_t;
```

#### 288.3.5 DBMS\_DBFS\_CONTENT\_PROPERTIES\_T Table Type

This type is a variable-sized array of property tuples of DBMS\_DBFS\_CONTENT\_PROPERTY\_T Object Type. It is used by both the client-facing interfaces and by store providers for the `DBMS_DBFS_CONTENT` interface.

Syntax

```
CREATE OR REPLACE TYPE dbms_dbfs_content_properties_t AS
    TABLE OF dbms_dbfs_content_property_t;
```

#### 288.3.6 DBMS\_DBFS\_CONTENT\_RAW\_T Table Type

This type is an array of `RAW`. It is to enable `RAW` data transport for batch interfaces in the DBMS\_DBFS\_CONTENT interface.

Syntax

```
CREATE OR REPLACE TYPE dbms_dbfs_content_raw_t AS
    TABLE OF RAW(32767);
```