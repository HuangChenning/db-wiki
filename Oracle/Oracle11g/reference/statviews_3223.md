---
title: DBA_HIST_EVENT_NAME
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3223.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_EVENT_NAME` displays information about wait events. This view contains a snapshot of `V$EVENT_NAME`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID |
| `EVENT_ID` | `NUMBER` | `NOT NULL` | Identifier of the wait event |
| `EVENT_NAME` | `VARCHAR2(64)` | `NOT NULL` | Name of the wait event |
| `PARAMETER1` | `VARCHAR2(64)` |  | Description of the first parameter for the wait event |
| `PARAMETER2` | `VARCHAR2(64)` |  | Description of the second parameter for the wait event |
| `PARAMETER3` | `VARCHAR2(64)` |  | Description of the third parameter for the wait event |
| `WAIT_CLASS_ID` | `NUMBER` |  | Identifier of the class of the wait event |
| `WAIT_CLASS` | `VARCHAR2(64)` |  | Name of the class of the wait event |