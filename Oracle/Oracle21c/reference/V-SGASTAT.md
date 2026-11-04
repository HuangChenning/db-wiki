---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-SGASTAT.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.38 V$SGASTAT

`V$SGASTAT` displays detailed information on the system global area (SGA).

| Column | Datatype | Description |
| --- | --- | --- |
| `POOL` | `VARCHAR2(14)` | Designates the pool in which the memory in `NAME` resides:  - `in-memory pool` - Memory is allocated from the In-Memory pool - `java pool` - Memory is allocated from the Java pool - `large pool` - Memory is allocated from the large pool - `numa pool` - Memory is allocated from the NUMA pool - `shared pool` - Memory is allocated from the shared pool - `streams pool` - Memory is allocated from the Streams pool |
| `NAME` | `VARCHAR2(26)` | SGA component name |
| `BYTES` | `NUMBER` | Memory size (in bytes) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |