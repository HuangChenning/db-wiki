---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_AUTO_SEGADV_SUMMARY.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_AUTO_SEGADV_SUMMARY` provides a summary of the auto advisor task runs.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `AUTO_TASKID` | `NUMBER` | `NOT NULL` | Unique auto task ID |
| `SNAPID` | `NUMBER` |  | Maximum AWR snapid used to process the segments |
| `SEGMENTS_SELECTED` | `NUMBER` |  | Number of segments chosen for analysis |
| `SEGMENTS_PROCESSED` | `NUMBER` |  | Number of segments actually processed |
| `TABLESPACE_SELECTED` | `NUMBER` |  | Number of tablespaces chosen for analysis |
| `TABLESPACE_PROCESSED` | `NUMBER` |  | Number of tablespaces actually processed |
| `RECOMMENDATIONS_COUNT` | `NUMBER` |  | Number of recommendations generated |
| `START_TIME` | `TIMESTAMP(6)` |  | Time at which the auto task was started |
| `END_TIME` | `TIMESTAMP(6)` |  | Time at which the auto task ended |