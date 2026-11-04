---
title: "V$SESS_IO"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3014.htm
tags:
  - oracle
  - 11g
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