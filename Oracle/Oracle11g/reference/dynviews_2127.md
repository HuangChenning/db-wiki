---
title: "V$RECOVERY_LOG"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2127.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$RECOVERY_LOG` lists information about archived logs that are needed to complete media recovery. This information is derived from the log history view, `V$LOG_HISTORY`.

`V$RECOVERY_LOG` contains useful information only for the Oracle process doing the recovery. When Recovery Manager directs a server process to perform recovery, only Recovery Manager is able to view the relevant information in this view. `V$RECOVERY_LOG` will be empty to all other Oracle users.

| Column | Datatype | Description |
| --- | --- | --- |
| `THREAD#` | `NUMBER` | Thread number of the archived log |
| `SEQUENCE#` | `NUMBER` | Sequence number of the archived log |
| `TIME` | `DATE` | Time of the first entry (lowest SCN) in the log |
| `ARCHIVE_NAME` | `VARCHAR2(513)` | Name of the file when archived, using the naming convention specified by the `LOG_ARCHIVE_FORMAT` initialization parameter  See Also: ["LOG\_ARCHIVE\_FORMAT"](initparams128.md) |

See Also:

["V$LOG\_HISTORY"](dynviews_2032.md) and [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/toc.htm)