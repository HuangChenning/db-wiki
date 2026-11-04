---
title: DBMS_MEMOPTIMIZE_ADMIN
book: PL/SQL Packages and Types Reference
doc_id: E96430-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/DBMS_MEMOPTIMIZE_ADMIN.html
tags:
  - oracle
  - 19c
  - pl-sql-packages-and-types-reference
---

The `DBMS_MEMOPTIMIZE_ADMIN` package provides the interface for flushing the Memoptimized Rowstore data buffered in the large pool to disk.

This chapter contains the following topics:

- DBMS\_MEMOPTIMIZE\_ADMIN Overview
- Summary of DBMS\_MEMOPTIMIZE\_ADMIN Subprograms

### DBMS\_MEMOPTIMIZE\_ADMIN Overview

The `DBMS_MEMOPTIMIZE_ADMIN` package provides the interface for flushing the Memoptimized Rowstore data that is buffered in the large pool to disk.

The Memoptimized Rowstore provides the following functionality:

- Fast Ingest
	Fast ingest optimizes the processing of high-frequency, single-row data inserts. Fast ingest uses the large pool in the SGA for buffering the inserts before writing them to disk.
- Fast Lookup
	Fast lookup enables fast retrieval of data for high-frequency queries. Fast lookup uses a separate memory area in the SGA called the *memoptimize pool* for buffering the data queried from tables.

The `DBMS_MEMOPTIMIZE_ADMIN` package provides the following operation related to fast ingest of the Memoptimized Rowstore:

- Flush fast ingest data from the large pool to disk for all sessions.

### Summary of DBMS\_MEMOPTIMIZE\_ADMIN Subprograms

This table lists the `DBMS_MEMOPTIMIZE_ADMIN` subprograms and briefly describes them.

Table 1 DBMS\_MEMOPTIMIZE\_ADMIN Package Subprograms

| Procedure | Description |
| --- | --- |
| WRITES\_FLUSH Procedure | Flushes all the fast ingest data of the Memoptimize Rowstore from the large pool to disk for all the sessions. |

### WRITES\_FLUSH Procedure

This procedure flushes all the fast ingest data of the Memoptimized Rowstore from the large pool to disk for all the sessions.

**Syntax**

```md
DBMS_MEMOPTIMIZE_ADMIN.WRITES_FLUSH;
```