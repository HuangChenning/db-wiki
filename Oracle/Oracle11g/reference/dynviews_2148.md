---
title: "V$RMAN_OUTPUT"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2148.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$RMAN_OUTPUT` displays messages reported by RMAN. This is an in-memory view and is not recorded in the controlfile. The view can hold 32768 rows.

| Column | Datatype | Description |
| --- | --- | --- |
| `SID` | `NUMBER` | Session ID of the session which is running this RMAN operation |
| `RECID` | `NUMBER` | Record ID of the corresponding `V$RMAN_STATUS` row |
| `STAMP` | `NUMBER` | Timestamp of the corresponding `V$RMAN_STATUS` row |
| `SESSION_RECID` | `NUMBER` | Record ID of the session (corresponding `V$RMAN_STATUS` row with `ROW_LEVEL` = `0`) |
| `SESSION_STAMP` | `NUMBER` | Timestamp of the session (corresponding `V$RMAN_STATUS` row with `ROW_LEVEL` = `0`) |
| `OUTPUT` | `VARCHAR2(129)` | Output text reported by RMAN |
| `RMAN_STATUS_RECID` | `NUMBER` | Owning `V$RMAN_STATUS` record ID |
| `RMAN_STATUS_STAMP` | `NUMBER` | Owning `V$RMAN_STATUS` record stamp |
| `SESSION_KEY` | `NUMBER` | Session identifier |