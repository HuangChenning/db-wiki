---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_AUTO_MV_REFRESH_HISTORY.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.186 DBA\_AUTO\_MV\_REFRESH\_HISTORY

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `MVIEW_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the materialized view |
| `MVIEW_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the materialized view |
| `SWAT_MM_START_TIME` | `DATE` |  | Date and time of the maintenance invocation |
| `REFRESH_START_TIME` | `DATE` |  | Date and time the refresh started |
| `REFRESH_END_TIME` | `DATE` |  | Date and time the refresh ended |
| `ELAPSED_REFRESH_TIME` | `NUMBER` |  | Duration of the refresh (in seconds) |
| `STATUS` | `NUMBER` |  | Status of the refresh. Possible values:  - `0` - The refresh is in-progress - `1` - The refresh completed successfully - `2` - An error occurred during the refresh. Refer to the value of the `ERROR` column for more information. - `3` - The refresh was terminated |
| `ERROR` | `NUMBER` |  | If an error occurred during the refresh, this column displays the error number, which corresponds to error code `ORA-` `number`. Otherwise, the value of this column is `0`. |

Note:

This view is available starting with Oracle Database 21c.