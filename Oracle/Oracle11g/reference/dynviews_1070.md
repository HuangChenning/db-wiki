---
title: "V$BLOCK_CHANGE_TRACKING"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1070.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$BLOCK_CHANGE_TRACKING` displays the status of block change tracking for the database.

| Column | Datatype | Description |
| --- | --- | --- |
| `STATUS` | `VARCHAR2(10)` | Status of block change tracking in the database: - `DISABLED` - Block change tracking is disabled - `TRANSITION` - Block change tracking is in the process of transitioning between the enabled and disabled states. The `TRANSITION` state should usually never be observed, because it only exists while enabling or disabling block change tracking. This state might be observed if the instance crashed while enabling or disabling block change tracking, in which case it will be cleaned up automatically the next time that the database is opened. - `ENABLED` - Block change tracking is enabled |
| `FILENAME` | `VARCHAR2(513)` | Name of the block change tracking file for the database |
| `BYTES` | `NUMBER` | Size of the block change tracking file (in bytes) |

See Also:

[Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/toc.htm) for information on setting up block change tracking