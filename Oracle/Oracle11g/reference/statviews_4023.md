---
title: DBA_HIST_PGASTAT
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4023.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_PGASTAT` displays historical PGA memory usage statistics as well as statistics about the automatic PGA memory manager when it is enabled. This view contains snapshots of `V$PGASTAT`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `NAME` | `VARCHAR2(64)` | `NOT NULL` | Name of the statistic: - `aggregate PGA auto target` - `aggregate PGA target parameter` - `bytes processed` - `cache hit percentage` - `extra bytes read/written` - `global memory bound` - `max processes count` - `maximum PGA allocated` - `maximum PGA used for auto workareas` - `maximum PGA used for manual workareas` - `over allocation count` - `PGA memory freed back to OS` - `process count` - `recompute count (total)` - `total freeable PGA memory` - `total PGA allocated` - `total PGA inuse` - `total PGA used for auto workareas` - `total PGA used for manual workareas`  See Also: `V$PGASTAT` for descriptions of the statistics |
| `VALUE` | `NUMBER` |  | Statistic value |