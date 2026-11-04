---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/DBMS_COMPRESSION.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 43 DBMS\_COMPRESSION

The `DBMS_COMPRESSION` package provides an interface to facilitate choosing the correct compression level for an application.

This chapter contains the following topics:

### 43.1 DBMS\_COMPRESSION Overview

The `DBMS_COMPRESSION` package gathers compression-related information within a database environment. This includes tools for estimating compressibility of a table for both partitioned and non-partitioned tables, and gathering row-level compression information on previously compressed tables. This gives the user with adequate information to make compression-related decision.

### 43.2 DBMS\_COMPRESSION Security Model

The `DBMS_COMPRESSSION` package is defined with `AUTHID CURRENT USER`, so it executes with the privileges of the current user.

### 43.3 DBMS\_COMPRESSION Constants

The `DBMS_COMPRESSION` package uses constants that can be used for specifying parameter values.

These constants are shown in the following table:

Table 43-1 DBMS\_COMPRESSION Constants - Compression Types

| Constant | Type | Value | Description |
| --- | --- | --- | --- |
| `COMP_NOCOMPRESS` | `NUMBER` | `1` | No compression |
| `COMP_ADVANCED` | `NUMBER` | `2` | Advanced row compression |
| `COMP_QUERY_HIGH` | `NUMBER` | `4` | High for query warehouse compression (Hybrid Columnar Compression) |
| `COMP_QUERY_LOW` | `NUMBER` | `8` | Low for query warehouse compression (Hybrid Columnar Compression) |
| `COMP_ARCHIVE_HIGH` | `NUMBER` | `16` | High archive compression (Hybrid Columnar Compression) |
| `COMP_ARCHIVE_LOW` | `NUMBER` | `32` | Low archive compression (Hybrid Columnar Compression) |
| `COMP_BLOCK` | `NUMBER` | `64` | Compressed block |
| `COMP_LOB_HIGH` | `NUMBER` | `128` | High compression level for LOB operations |
| `COMP_LOB_MEDIUM` | `NUMBER` | `256` | Medium compression level for LOB operations |
| `COMP_LOB_LOW` | `NUMBER` | `512` | Low compression level for LOB operations |
| `COMP_INDEX_ADVANCED_HIGH` | `NUMBER` | `1024` | High compression level for indexes |
| `COMP_INDEX_ADVANCED_LOW` | `NUMBER` | `2048` | Low compression level for indexes |
| `COMP_RATIO_LOB_MINROWS` | `NUMBER` | `1000` | Minimum required number of LOBs in the object for which LOB compression ratio is to be estimated |
| `COMP_BASIC` | `NUMBER` | `4096` | Basic table compression |
| `COMP_RATIO_LOB_MAXROWS` | `NUMBER` | `5000` | Maximum number of LOBs used to compute the LOB compression ratio |
| `COMP_INMEMORY_NOCOMPRESS` | `NUMBER` | `8192	` | In-Memory with no compression |
| `COMP_INMEMORY_DML` | `NUMBER` | `16384` | In-Memory compression level for DML |
| `COMP_INMEMORY_QUERY_LOW` | `NUMBER` | `32768` | In-Memory compression level optimized for query performance |
| `COMP_INMEMORY_QUERY_HIGH` | `NUMBER` | `65536` | In-Memory compression level optimized on query performance as well as space saving |
| `COMP_INMEMORY_CAPACITY_LOW` | `NUMBER` | `131072` | In-Memory low compression level optimizing for capacity |
| `COMP_INMEMORY_CAPACITY_HIGH` | `NUMBER` | `262144` | In-Memory high compression level optimizing for capacity |
| `COMP_RATIO_MINROWS` | `NUMBER` | `1000000` | Minimum required number of rows in the object for which HCC ratio is to be estimated |
| `COMP_RATIO_ALLROWS` | `NUMBER` | `-1` | To indicate the use of all the rows in the object to estimate HCC ratio |
| `OBJTYPE_TABLE` | `PLS_INTEGER` | `1` | Identifies the object whose compression ratio is estimated as of type table |
| `OBJTYPE_INDEX` | `PLS_INTEGER` | 2 | Identifies the object whose compression ratio is estimated as of type index |

Note:

Hybrid columnar compression is a feature of certain Oracle storage systems. See [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=CNCPT89198) for more information.

### 43.4 DBMS\_COMPRESSION Data Structures

The `DBMS_COMPRESSION` package defines a `RECORD` type and a `TABLE` type.

RECORD TYPES

COMPREC Record Type

TABLE TYPES

COMPRECLIST Table Type

#### 43.4.1 COMPREC Record Type

The COMPREC record type is a record for calculating an individual index compression ratio on a table.

Syntax

```
TYPE COMPREC IS RECORD(
  ownname           varchar2(255),
  objname           varchar2(255),
  blkcnt_cmp        PLS_INTEGER,
  blkcnt_uncmp      PLS_INTEGER,
  row_cmp           PLS_INTEGER,
  row_uncmp         PLS_INTEGER,
  cmp_ratio         NUMBER,
  objtype           PLS_INTEGER);
```

Fields

Table 43-2 COMPREC Attributes

| Field | Description |
| --- | --- |
| `ownname` | Schema of the object owner |
| `objname` | Name of the object |
| `blkcnt_cmp` | Number of blocks used by the compressed sample of the object |
| `blkcnt_uncmp` | Number of blocks used by the uncompressed sample of the object |
| `row_cmp` | Number of rows in a block in compressed sample of the object |
| `row_uncmp` | Number of rows in a block in uncompressed sample of the object |
| `cmp_ratio` | Compression ratio, `blkcnt_uncmp` divided by `blkcnt_cmp` |
| `objtype` | Type of the object |

#### 43.4.2 COMPRECLIST Table Type

COMPRECLIST is a table type of the COMPREC Record Type.

Syntax

```
TYPE compreclist IS TABLE OF comprec;
```

### 43.5 Summary of DBMS\_COMPRESSION Subprograms

The `DBMS_COMPRESSION` package uses the `GET_COMPRESSION_RATIO` Procedure and `GET_COMPRESSION_TYPE` Function subprograms.

Table 43-3 DBMS\_COMPRESSION Package Subprograms

| Subprogram | Description |
| --- | --- |
| GET\_COMPRESSION\_RATIO Procedure | Analyzes the compression ratio of a table, and gives information about compressibility of a table |
| GET\_COMPRESSION\_TYPE Function | Returns the compression type for a specified row |

#### 43.5.1 GET\_COMPRESSION\_RATIO Procedure

This procedure analyzes the compression ratio of a table or an index, and gives information about compressibility of the object. Various parameters can be provided by the user to selectively analyze different compression types.

Syntax

Get compression ratio for an object (table or index, default is table):

```
DBMS_COMPRESSION.GET_COMPRESSION_RATIO (
   scratchtbsname        IN     VARCHAR2, 
   ownname               IN     VARCHAR2, 
   objname               IN     VARCHAR2,
   subobjname            IN     VARCHAR2,
   comptype              IN     NUMBER,
   blkcnt_cmp            OUT    PLS_INTEGER,
   blkcnt_uncmp          OUT    PLS_INTEGER,
   row_cmp               OUT    PLS_INTEGER,
   row_uncmp             OUT    PLS_INTEGER,
   cmp_ratio             OUT    NUMBER,
   comptype_str          OUT    VARCHAR2,
   subset_numrows        IN     NUMBER  DEFAULT COMP_RATIO_MINROWS,
   objtype               IN     PLS_INTEGER DEFAULT OBJTYPE_TABLE);
```

Get compression ratio for LOBs:

```
DBMS_COMPRESSION.GET_COMPRESSION_RATIO (
   scratchtbsname        IN     VARCHAR2,
   tabowner              IN     VARCHAR2,
   tabname               IN     VARCHAR2,
   lobname               IN     VARCHAR2,
   partname              IN     VARCHAR2,
   comptype              IN     NUMBER,
   blkcnt_cmp            OUT    PLS_INTEGER,
   blkcnt_uncmp          OUT    PLS_INTEGER,
   lobcnt                OUT    PLS_INTEGER,
   cmp_ratio             OUT    NUMBER,
   comptype_str          OUT    VARCHAR2,
   subset_numrows        IN     number DEFAULT COMP_RATIO_LOB_MAXROWS);
```

Get compression ratio for all indexes on a table. The compression ratios are returned as a collection.

```
DBMS_COMPRESSION.GET_COMPRESSION_RATIO (
  scratchtbsname        IN     VARCHAR2,
  ownname               IN     VARCHAR2,
  tabname               IN     VARCHAR2,
  comptype              IN     NUMBER,
  index_cr              OUT    DBMS_COMPRESSION.COMPRECLIST,
  comptype_str          OUT    VARCHAR2,
  subset_numrows        IN     NUMBER DEFAULT COMP_RATIO_INDEX_MINROWS);
```

Parameters

Table 43-4 GET\_COMPRESSION\_RATIO Procedure Parameters

| Parameter | Description |
| --- | --- |
| `scratchtbsname` | Temporary scratch tablespace that can be used for analysis |
| `ownname` / `tabowner` | Schema of the table to analyze |
| `tabname` | Name of the table to analyze |
| `objname` | Name of the object |
| `subobjname` | Name of the partition or sub-partition of the object |
| `comptype` | Compression types for which analysis should be performed  When the object is an index, only the following compression types are valid: `COMP_INDEX_ADVANCED_HIGH` (value `1024`) and `COMP_INDEX_ADVANCED_LOW` (value `2048`).  Note: The following compression types cannot be specified in this parameter for any type of object: `COMP_BLOCK` (value `64`) and `COMP_BASIC` (value `4096`). |
| `blkcnt_cmp` | Number of blocks used by compressed sample of the table |
| `blkcnt_uncmp` | Number of blocks used by uncompressed sample of the table |
| `row_cmp` | Number of rows in a block in compressed sample of the table |
| `row_uncmp` | Number of rows in a block in uncompressed sample of the table |
| `cmp_ratio` | Compression ratio, `blkcnt_uncmp` divided by `blkcnt_cmp` |
| `comptype_str` | String describing the compression type |
| `subset_numrows` | Number of rows sampled to estimate compression ratio. |
| `objtype` | Type of the object, either `OBJTYPE_TABLE` or `OBJTYPE_INDEX` |
| `lobname` | Name of the LOB column |
| `partname` | In case of partitioned tables, the related partition name |
| `lobcnt` | Number of lobs actually sampled to estimate compression ratio |
| `index_cr` | List of indexes and their estimated compression ratios |

Examples

The following example shows how to estimate the compression ratio for advanced row compression:

```
SET SERVEROUTPUT ON
DECLARE
  1_blkcnt_cmp   PLS_INTEGER;
  1_blkcnt_uncmp PLS_INTEGER;
  1_row_cmp      PLS_INTEGER;
  1_row_uncmp    PLS_INTEGER;
  1_cmp_ratio    NUMBER;
  1_comptype_str VARCHAR2(32767);
BEGIN
   DBMS_COMPRESSION.GET_COMPRESSION_RATIO (
   scratchtbsname => 'USERS' ,
   ownname      => 'TEST' ,
   objname      => 'SALES' ,
   subobjname     =>  NULL ,
   comptype       =>  DBMS_COMPRESSION.COMP_ADVANCED,
   blkcnt_cmp     => 1_blkcnt_cmp,
   blkcnt_uncmp   => 1_blkcnt_uncmp,
   row_cmp      => 1_row_cmp,
   row_uncmp      => 1_row_uncmp,
   cmp_ratio      => 1_cmp_ratio,
   comptype_str   => 1_comptype_str,
   subset_numrows => DBMS_COMPRESSION.comp_ratio_minrows,
   objtype      => DBMS_COMPRESSION.objtype_table
  );
DBMS_OUTPUT.put_line( 'Number of blocks used by the compressed sample of the object    :  ' || 1_blkcnt_cmp);
DBMS_OUTPUT.put_line( 'Number of blocks used by the uncompressed sample of the object    :  ' || 1_blkcnt_uncmp);
DBMS_OUTPUT.put_line( 'Number of rows in a block in compressed sample of the object    :  ' || 1_row_cmp);
DBMS_OUTPUT.put_line( 'Number of rows in a block in uncompressed sample of the object    :  ' || 1_row_uncmp);
DBMS_OUTPUT.put_line( 'Estimated Compression Ratio of Sample                           :  ' || 1_cmp_ratio);
DBMS_OUTPUT.put_line( 'Compression Type                            :  ' || 1_comptype_str);
END;
/
```

Output of compression advisor estimate for advanced row compression (entire table):

```
Number of blocks used by the compressed sample of the object     : 165
Number of blocks used by the uncompressed sample of the object   : 629
Number of rows in a block in compressed sample of the object     : 599
Number of rows in a block in uncompressed sample of the object   : 157
Estimated Compression Ratio of Sample                     : 3.8
Compression Type                         : “Compress Advanced”
```

The following example shows how to estimate the compression ratio for advanced index compression (Low):

```
SET SERVEROUTPUT ON
DECLARE
  1_blkcnt_cmp       PLS_INTEGER;
  1_blkcnt_uncmp   PLS_INTEGER
  1_row_cmp       PLS_INTEGER;
  1_row_uncmp       PLS_INTEGER;
  1_cmp_ratio       NUMBER;
  1_comptype_str   VARCHAR2(32767);
BEGIN
   DBMS_COMPRESSION.GET_COMPRESSION_RATIO (
    scratchtbsname =>       'USERS' ,
    ownname       =>       'TEST' ,
    objname       =>       'SALES_IDX' ,
    subobjname     =>        NULL ,
    comptype       =>        DBMS_COMPRESSION.COMP_INDEX_ADVANCED_LOW,
    blkcnt_cmp     =>        1_blkcnt_cmp,
    blkcnt_uncmp   =>        1_blkcnt_uncmp,
    row_cmp       =>        1_row_cmp,
    row_uncmp      =>        1_row_uncmp,
    cmp_ratio      =>        1_cmp_ratio,
    comptype_str   =>        1_comptype_str,
    subset_numrows =>        DBMS_COMPRESSION.comp_ratio_minrows,
    objtype       =>        DBMS_COMPRESSION.objtype_index
   );
DBMS_OUTPUT.put_line( 'Number of blocks used by the compressed sample of the object   :  ' || 1_blkcnt_cmp);
DBMS_OUTPUT.put_line( 'Number of blocks used by the uncompressed sample of the object :  ' || 1_blkcnt_uncmp);
DBMS_OUTPUT.put_line( 'Number of rows in a block in compressed sample of the object   :  ' || 1_row_cmp);
DBMS_OUTPUT.put_line( 'Number of rows in a block in uncompressed sample of the object :  ' || 1_row_uncmp);
DBMS_OUTPUT.put_line( 'Estimated Compression Ratio of Sample                          :  ' || 1_cmp_ratio);
DBMS_OUTPUT.put_line( 'Compression Type                              :  ' || 1_comptype_str);
END;
/
```

Output of compression advisor estimate for advanced index compression (Low):

```
Number of blocks used by the compressed sample of the object     : 243
Number of blocks used by the uncompressed sample of the object   : 539
Number of rows in a block in compressed sample of the object     : 499
Number of rows in a block in uncompressed sample of the object   : 145
Estimated Compression Ratio of Sample                 : 2.2
Compression Type                         : “Compress Advanced Low”
```

The following example shows how to estimate the compression ratio for advanced LOB compression (Medium):

```
SET SERVEROUTPUT ON
DECLARE
  1_blkcnt_cmp     PLS_INTEGER;
  1_blkcnt_uncmp   PLS_INTEGER;
  1_row_cmp       PLS_INTEGER;
  1_lobcnt       PLS_INTEGER;
  1_cmp_ratio      NUMBER;
  1_comptype_str   VARCHAR2(32767);
BEGIN
   DBMS_COMPRESSION.GET_COMPRESSION_RATIO (
    scratchtbsname => 'USERS' ,
    tabowner       => 'TEST' ,
    tabname       => 'PARTS' ,
    lobname       =>  'PART_DESCRIPTION' ,
    partname       =>  NULL ,
    comptype       =>  DBMS_COMPRESSION.COMP_LOB_MEDIUM,
    blkcnt_cmp     => 1_blkcnt_cmp,
    blkcnt_uncmp   => 1_blkcnt_uncmp,
    row_cmp       => 1_row_cmp,
    lobcnt       => 1_lobcnt,
    cmp_ratio      => 1_cmp_ratio,
    comptype_str   => 1_comptype_str,
    subset_numrows => DBMS_COMPRESSION.comp_ratio_lob_maxrows
   );
DBMS_OUTPUT.put_line( 'Number of blocks used by the compressed sample of the object    :  ' || 1_blkcnt_cmp);
DBMS_OUTPUT.put_line( 'Number of blocks used by the uncompressed sample of the object  :  ' || 1_blkcnt_uncmp);
DBMS_OUTPUT.put_line( 'Number of rows in a block in compressed sample of the object    :  ' || 1_row_cmp);
DBMS_OUTPUT.put_line( 'Number of LOBS actually sampled                       :  ' || 1_lobcnt);
DBMS_OUTPUT.put_line( 'Estimated Compression Ratio of Sample                           :  ' || 1_cmp_ratio);
DBMS_OUTPUT.put_line( 'Compression Type                                                :  ' || 1_comptype_str);
END;
/
```

Output of compression advisor estimate for advanced LOB compression (Medium):

```
Number of blocks used by the compressed sample of the object   : 199
Number of blocks used by the uncompressed sample of the object : 389
Number of rows in a block in compressed sample of the object   : 293
Number of LOBS actually sampled                    : 55
Estimated Compression Ratio of Sample                   : 1.9
Compression Type                           : “Compress Medium”
```

Usage Notes

The procedure creates different tables in the scratch tablespace and runs analysis on these objects. It does not modify anything in the user-specified tables.

#### 43.5.2 GET\_COMPRESSION\_TYPE Function

This function returns the compression type for a specified row. If the row is chained, the function returns the compression type of the head piece only, and does not examine the intermediate or the tail piece since head pieces can be differently compressed.

Syntax

```
DBMS_COMPRESSION.GET_COMPRESSION_TYPE (
   ownname      IN    VARCHAR2, 
   tabname      IN    VARCHAR2, 
   row_id       IN    ROWID,
   subobjname   IN    VARCHAR2 DEFAULT NULL))
  RETURN NUMBER;
```

Parameters

Table 43-5 GET\_COMPRESSION\_TYPE Function Parameters

| Parameter | Description |
| --- | --- |
| `ownname` | Schema name of the table |
| `tabname` | Name of table |
| `rowid` | Rowid of the row |
| `subobjname` | Name of the table partition or subpartition |

Return Values

Flag to indicate the compression type (see Table 43-1).