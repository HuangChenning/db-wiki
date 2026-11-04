---
title: "V$TEMPSEG_USAGE"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3107.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$TEMPSEG_USAGE` describes temporary segment usage.

| Column | Datatype | Description |
| --- | --- | --- |
| `USERNAME` | `VARCHAR2(30)` | User who requested temporary space |
| `USER` | `VARCHAR2(30)` | This column is obsolete and maintained for backward compatibility. The value of this column is always equal to the value in `USERNAME`. |
| `SESSION_ADDR` | `RAW(4 \| 8)` | Session address |
| `SESSION_NUM` | `NUMBER` | Serial number of session |
| `SQLADDR` | `RAW(4 \| 8)` | Address of SQL statement |
| `SQLHASH` | `NUMBER` | Hash value of SQL statement |
| `SQL_ID` | `VARCHAR2(13)` | SQL identifier of SQL statement |
| `TABLESPACE` | `VARCHAR2(31)` | Tablespace in which space is allocated |
| `CONTENTS` | `VARCHAR2(9)` | Indicates whether tablespace is `TEMPORARY` or `PERMANENT` |
| `SEGTYPE` | `VARCHAR2(9)` | Type of sort segment: |
| `SEGFILE#` | `NUMBER` | File number of initial extent |
| `SEGBLK#` | `NUMBER` | Block number of the initial extent |
| `EXTENTS` | `NUMBER` | Extents allocated to the sort |
| `BLOCKS` | `NUMBER` | Extents in blocks allocated to the sort |
| `SEGRFNO#` | `NUMBER` | Relative file number of initial extent |