---
title: "V$GCSPFMASTER_INFO"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1155.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$GCSPFMASTER_INFO` describes the current and previous master instances and the number of re-masterings of Global Cache Service resources belonging to files mapped to instances.

| Column | Datatype | Description |
| --- | --- | --- |
| `FILE_ID` | `NUMBER` | File number |
| `DATA_OBJECT_ID` | `NUMBER` | Data object ID |
| `GC_MASTERING_POLICY` | `VARCHAR2(11)` | Data object type.  The possible values are `Affinity` or `Read mostly.` |
| `CURRENT_MASTER` | `NUMBER` | Master instance of this file |
| `PREVIOUS_MASTER` | `NUMBER` | Previous master instance of this file |
| `REMASTER_CNT` | `NUMBER` | Number of times this has been remastered |