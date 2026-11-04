---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-BLOCK_CHANGE_TRACKING.html
tags:
  - oracle
  - 12c
  - reference
---

`V$BLOCK_CHANGE_TRACKING` displays the status of block change tracking for the database.

| Column | Datatype | Description |
| --- | --- | --- |
| `STATUS` | `VARCHAR2(10)` | Status of block change tracking in the database:  - `DISABLED` - Block change tracking is disabled - `TRANSITION` - Block change tracking is in the process of transitioning between the enabled and disabled states. The `TRANSITION` state should usually never be observed, because it only exists while enabling or disabling block change tracking. This state might be observed if the instance crashed while enabling or disabling block change tracking, in which case it will be cleaned up automatically the next time that the database is opened. - `ENABLED` - Block change tracking is enabled |
| `FILENAME` | `VARCHAR2(513)` | Name of the block change tracking file for the database |
| `BYTES` | `NUMBER` | Size of the block change tracking file (in bytes) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

[Oracle Database Backup and Recovery User’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=BRADV8125) for information on setting up block change tracking