---
title: DBMS_COMPRESSION
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_compress.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 36 DBMS\_COMPRESSION

The `DBMS_COMPRESSION` package provides an interface to facilitate choosing the correct compression level for an application.

See Also:

- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/tables.htm#ADMIN11630)
- [Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/tablecls.htm#CNCPT1132)
- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_7002.htm#SQLRF54484)
- [Oracle Database 2 Day + Data Warehousing Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25555/tdpdw_perform.htm#TDPDW12080)
- [Oracle Database Data Warehousing Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25554/basicmv.htm#DWHSG00833)
- [Oracle Database VLDB and Partitioning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25523/part_avail.htm#VLDBG00404)
- [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/toc.htm)

This chapter contains the following topics:

- Using DBMS\_COMPRESSION
	- Overview
		- Security Model
		- Constants
		- Views
- Summary of DBMS\_COMPRESSION Subprograms

---

## Using DBMS\_COMPRESSION

---

### Overview

The `DBMS_COMPRESSION` package gathers compression-related information within a database environment. This includes tools for estimating compressibility of a table for both partitioned and non-partitioned tables, and gathering row-level compression information on previously compressed tables. This gives the user with adequate information to make compression-related decision.

---

### Security Model

The `DBMS_COMPRESSSION` package is owned by user `SYS`, and must be created by `SYS`. The execution privilege is granted to `PUBLIC`. Subprograms in this package are executed using the privileges of the current user.

---

### Constants

The `DBMS_COMPRESSION` package uses the constants shown in Table 36-1, "DBMS\_COMPRESSION Constants - Compression Types" e:

Table 36-1 DBMS\_COMPRESSION Constants - Compression Types

| Constant | Type | Value | Description |
| --- | --- | --- | --- |
| `COMP_NOCOMPRESS` | `NUMBER` | `1` | No compression |
| `COMP_FOR_OLTP` | `NUMBER` | `2` | OLTP compression |
| `COMP_FOR_QUERY_HIGH` | `NUMBER` | `4` | High compression level for query operations |
| `COMP_FOR_QUERY_LOW` | `NUMBER` | `8` | Low compression level for query operations |
| `COMP_FOR_ARCHIVE_HIGH` | `NUMBER` | `16` | High compression level for archive operations |
| `COMP_FOR_ARCHIVE_LOW` | `NUMBER` | `32` | Low compression level for archive operations |
| `COMP_BLOCK` | `NUMBER` | `64` | Compression |
| `COMP_RATIO_MINROWS` | `NUMBER` | `1000000` | Minimum required number of rows in the object for which HCC ratio is to be estimated |
| `COMP_RATIO_ALLROWS` | `NUMBER` | `-1` | To indicate the use of all the rows in the object to estimate HCC ratio |

Note:

Hybrid columnar compression is a feature of certain Oracle storage systems. See [Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/tablecls.htm#CNCPT89198) for more information.

---

### Views

The `DBMS_COMPRESSION` package uses views described in the [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/toc.htm). The twenty catalog views that contain a `COMPRESS_FOR` or `DEF_COMPRESS_FOR` will have a list of valid displayed values to be one of the following:

- `BASIC`
- `OLTP`
- `QUERY` `LOW`
- `QUERY` `HIGH`
- `ARCHIVE` `LOW`
- `ARCHIVE` `HIGH`

The affected views are:

- [`ALL_ALL_TABLES`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1003.htm#REFRN20003)
- [`ALL_OBJECT_TABLES`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1157.htm#REFRN20145)
- [`ALL_PART_TABLES`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2006.htm#REFRN20159)
- [`ALL_TABLES`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2117.htm#REFRN20286)
- [`ALL_TAB_PARTITIONS`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2108.htm#REFRN20281)
- [`ALL_TAB_SUBPARTITIONS`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2116.htm#REFRN20285)
- [`DBA_ALL_TABLES`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3045.htm#REFRN23003)
- [`DBA_OBJECT_TABLES`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4157.htm#REFRN23145)
- [`DBA_PART_TABLES`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4177.htm#REFRN23159)
- [`DBA_TABLES`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5056.htm#REFRN23286)
- [`DBA_TAB_PARTITIONS`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5049.htm#REFRN23281)
- [`DBA_TAB_SUBPARTITIONS`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5055.htm#REFRN23285)
- [`DBA_TABLESPACES`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5060.htm#REFRN23287)
- [`USER_OBJECT_TABLES`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5375.htm#REFRN26145)
- [`USER_PART_TABLES`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5392.htm#REFRN26159)
- [`USER_TABLES`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5490.htm#REFRN26286)
- [`USER_TAB_PARTITIONS`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5481.htm#REFRN26281)
- [`USER_TABLESPACES`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5491.htm#REFRN26287)

---

## Summary of DBMS\_COMPRESSION Subprograms

Table 36-2 DBMS\_COMPRESSION Package Subprograms

| Subprogram | Description |
| --- | --- |
| GET\_COMPRESSION\_RATIO Procedure | Analyzes the compression ratio of a table, and gives information about compressibility of a table |
| GET\_COMPRESSION\_TYPE Function | Returns the compression type for a specified row |

---

### GET\_COMPRESSION\_RATIO Procedure

This procedure analyzes the compression ratio of a table, and gives information about compressibility of a table. Various parameters can be provided by the user to selectively analyze different compression types.

Syntax

```
DBMS_COMPRESSION.GET_COMPRESSION_RATIO (
   scratchtbsname        IN     VARCHAR2,
   ownname               IN     VARCHAR2,
   tabname               IN     VARCHAR2,
   partname              IN     VARCHAR2,
   comptype              IN     NUMBER,
   blkcnt_cmp            OUT    PLS_INTEGER,
   blkcnt_uncmp          OUT    PLS_INTEGER,
   row_cmp               OUT    PLS_INTEGER,
   row_uncmp             OUT    PLS_INTEGER,
   cmp_ratio             OUT    NUMBER,
   comptype_str          OUT    VARCHAR2,   subset_numrows        IN     NUMBER DEFAULT COMP_RATIO_MINROWS);
```

Parameters

Table 36-3 GET\_COMPRESSION\_RATIO Procedure Parameters

| Parameter | Description |
| --- | --- |
| `scratchtbsname` | Temporary scratch tablespace that can be used for analysis |
| `ownname` | Schema of the table to analyze |
| `tabname` | Name of the table to analyze |
| `partname` | In case of partitioned tables, the related partition name |
| `comptype` | Compression types for which analysis should be performed |
| `blkcnt_cmp` | Number of blocks used by compressed sample of the table |
| `blkcnt_uncmp` | Number of blocks used by uncompressed sample of the table |
| `row_cmp` | Number of rows in a block in compressed sample of the table |
| `row_uncmp` | Number of rows in a block in uncompressed sample of the table |
| `cmp_ratio` | Compression ratio, `blkcnt_uncmp` divided by `blkcnt_cmp` |
| `comptype_str` | String describing the compression type |
| `subset_numrows` | Number of rows sampled to estimate compression ratio. |

Usage Notes

The procedure creates different tables in the scratch tablespace and runs analysis on these objects. It does not modify anything in the user-specified tables.

---

### GET\_COMPRESSION\_TYPE Function

This function returns the compression type for a specified row. If the row is chained, the function returns the compression type of the head piece only, and does not examine the intermediate or the tail piece since head pieces can be differently compressed.

Syntax

```
DBMS_COMPRESSION.GET_COMPRESSION_TYPE (
   ownname    IN    VARCHAR2, 
   tabname    IN    VARCHAR2, 
   row_id     IN    ROWID)
  RETURN NUMBER;
```

Parameters

Table 36-4 GET\_COMPRESSION\_TYPE Function Parameters

| Parameter | Description |
| --- | --- |
| `ownname` | Schema name of the table |
| `tabname` | Name of table |
| `rowid` | Rowid of the row |

Return Values

Flag to indicate the compression type (see DBMS\_COMPRESSION Constants - Compression Types).