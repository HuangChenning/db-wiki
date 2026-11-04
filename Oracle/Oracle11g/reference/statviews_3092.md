---
title: DBA_AUTOTASK_WINDOW_HISTORY
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3092.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_AUTOTASK_WINDOW_HISTORY` displays historical information for automated maintenance task windows.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `WINDOW_NAME` | `VARCHAR2(65)` |  | Name of the maintenance window |
| `WINDOW_START_TIME` | `TIMESTAMP(6) WITH TIME ZONE` |  | Window start time |
| `WINDOW_END_TIME` | `TIMESTAMP(6) WITH TIME ZONE` |  | Window end time |