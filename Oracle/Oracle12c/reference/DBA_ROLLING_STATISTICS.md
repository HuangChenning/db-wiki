---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_ROLLING_STATISTICS.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_ROLLING_STATISTICS` provides a list of rolling operation statistics.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `NAME` | `VARCHAR2(256)` |  | Name of the statistic. Possible values:  - `DBMS_ROLLING execution time` - `logical to primary switchover finish time` - `primary services offline for` - `primary to logical switchover start time` - `rolling upgrade finish time` - `rolling upgrade start time` - `time for former primary to fully recover upgrade redo` - `time for former primary to start upgrade redo recovery` - `total time former primary in physical role` - `transient logical creation finish time` - `transient logical creation start time` - `transient logical protection finish time` - `transient logical protection start time` - `user upgrade time` |
| `VALUE` | `VARCHAR2(256)` |  | Value of the statistic |
| `UPDATE_TIME` | `TIMESTAMP(6)` |  | Time of last update |

See Also:

[Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=SBYDB5214) for more information about rolling operations.