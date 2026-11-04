---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/V-SECUREFILE_TIMER.html
tags:
  - oracle
  - 19c
  - reference
---

## 9.2 V$SECUREFILE\_TIMER

These timer values are collected per session.

| Column | Datatype | Description |
| --- | --- | --- |
| `NAME` | `VARCHAR2(50)` | Name of the function |
| `LAYER_ID` | `NUMBER` | ID of the layer that the function belongs to:  - `0` - Entire Subtree - `1` - Delta Updates - `2` - Write gather cache - `3` - Deduplication - `4` - Compression & Encryption - `5` - Inode - `6` - Space - `7` - Utilities - `8` - Row-Column Intersection |
| `OWNTIME` | `NUMBER` | Total time taken by the function |
| `MAXTIME` | `NUMBER` | Maximum time taken by a single call |
| `MINTIME` | `NUMBER` | Minimum time taken by a single call |
| `INVOCATIONS` | `NUMBER` | Number of times the function was invoked |
| `LAYER_NAME` | `VARCHAR2(50)` | Name of the layer to which the function belongs |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |