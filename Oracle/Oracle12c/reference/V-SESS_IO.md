---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-SESS_IO.html
tags:
  - oracle
  - 12c
  - reference
---

`V$SESS_IO` displays I/O statistics for each user session.

| Column | Datatype | Description |
| --- | --- | --- |
| `SID` | `NUMBER` | Session identifier |
| `BLOCK_GETS` | `NUMBER` | Block gets for this session |
| `CONSISTENT_GETS` | `NUMBER` | Consistent gets for this session |
| `PHYSICAL_READS` | `NUMBER` | Physical reads for this session |
| `BLOCK_CHANGES` | `NUMBER` | Block changes for this session |
| `CONSISTENT_CHANGES` | `NUMBER` | Consistent changes for this session |
| `OPTIMIZED_PHYSICAL_READS` | `NUMBER` | Number of physical reads from Database Smart Flash Cache for this session |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |