---
title: DBA_HIST_SGA_TARGET_ADVICE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4040.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_SGA_TARGET_ADVICE` provides historical information about the `SGA_TARGET` initialization parameter.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `SGA_SIZE` | `NUMBER` | `NOT NULL` | Size of the SGA |
| `SGA_SIZE_FACTOR` | `NUMBER` | `NOT NULL` | Ratio between the `SGA_SIZE` and the current size of the SGA |
| `ESTD_DB_TIME` | `NUMBER` | `NOT NULL` | Estimated DB\_TIME for this SGA\_SIZE |
| `ESTD_PHYSICAL_READS` | `NUMBER` |  | Estimated number of physical reads |