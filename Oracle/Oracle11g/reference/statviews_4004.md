---
title: DBA_HIST_LATCH_NAME
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4004.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_LATCH_NAME` displays information about decoded latch names for the latches shown in `DBA_HIST_LATCH`. This view contains a snapshot of `V$LATCHNAME`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID |
| `LATCH_HASH` | `NUMBER` | `NOT NULL` | Latch hash |
| `LATCH_NAME` | `VARCHAR2(64)` | `NOT NULL` | Latch name |