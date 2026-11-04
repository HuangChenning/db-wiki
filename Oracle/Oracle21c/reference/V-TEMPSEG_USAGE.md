---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-TEMPSEG_USAGE.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.112 V$TEMPSEG\_USAGE

| Column | Datatype | Description |
| --- | --- | --- |
| `USERNAME` | `VARCHAR2(128)` | User who requested temporary space |
| `USER` | `VARCHAR2(128)` | This column is obsolete and maintained for backward compatibility. The value of this column is always equal to the value in `USERNAME`. |
| `SESSION_ADDR` | `RAW(4 \| 8)` | Session address |
| `SESSION_NUM` | `NUMBER` | Serial number of session |
| `SQLADDR` | `RAW(4 \| 8)` | Address of SQL statement |
| `SQLHASH` | `NUMBER` | Hash value of SQL statement |
| `SQL_ID` | `VARCHAR2(13)` | SQL identifier of SQL statement |
| `TABLESPACE` | `VARCHAR2(30)` | Tablespace in which space is allocated |
| `CONTENTS` | `VARCHAR2(9)` | Indicates whether tablespace is `TEMPORARY` or `PERMANENT` |
| `SEGTYPE` | `VARCHAR2(9)` | Type of sort segment:  - `SORT` - `HASH` - `DATA` - `INDEX` - `LOB_DATA` - `LOB_INDEX` |
| `SEGFILE#` | `NUMBER` | File number of initial extent |
| `SEGBLK#` | `NUMBER` | Block number of the initial extent |
| `EXTENTS` | `NUMBER` | Extents allocated to the sort |
| `BLOCKS` | `NUMBER` | Extents in blocks allocated to the sort |
| `SEGRFNO#` | `NUMBER` | Relative file number of initial extent |
| `TS#` | `NUMBER` | Tablespace number |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |
| `SQL_ID_TEMPSEG` | `VARCHAR2(13)` | SQL identifier of the SQL statement that created the temporary segment |