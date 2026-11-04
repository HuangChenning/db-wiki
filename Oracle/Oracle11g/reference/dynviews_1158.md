---
title: "V$GES_CONVERT_REMOTE"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1158.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$GES_CONVERT_REMOTE` displays values for remote GES enqueue conversions. This view records average convert times, count information, and timed statistics for global enqueue requests.

| Column | Datatype | Description |
| --- | --- | --- |
| `INST_ID` | `NUMBER` | ID of the instance |
| `CONVERT_TYPE` | `VARCHAR2(16)` | Conversion type: - `NULL -> SS` - NULL mode to subshared mode - `NULL -> SX` - NULL mode to shared exclusive mode - `NULL -> S` - NULL mode to shared mode - `NULL -> SSX` - NULL mode to subshared exclusive mode - `NULL -> X` - NULL mode to exclusive mode - `SS -> SX` - Subshared mode to shared exclusive mode - `SS -> S` - Subshared mode to shared mode - `SS -> SSX` - Subshared mode to subshared exclusive mode - `SS -> X` - Subshared mode to exclusive mode - `SX -> S` - Shared exclusive mode to shared mode - `SX -> SSX` - Shared exclusive mode to subshared exclusive mode - `SX -> X` - Shared exclusive mode to exclusive mode - `S -> SX` - Shared mode to shared exclusive mode - `S -> SSX` - Shared mode to subshared exclusive mode - `S -> X` - Shared mode to exclusive mode - `SSX -> X` - Sub-shared exclusive mode to exclusive mode |
| `AVERAGE_CONVERT_TIME` | `NUMBER` | Average conversion time for each type of lock operation (in hundredths of a second) |
| `CONVERT_COUNT` | `NUMBER` | Number of operations |