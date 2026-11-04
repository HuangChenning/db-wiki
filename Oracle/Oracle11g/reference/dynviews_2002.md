---
title: "V$INSTANCE"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2002.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$INSTANCE` displays the state of the current instance.

| Column | Datatype | Description |
| --- | --- | --- |
| `INSTANCE_NUMBER` | `NUMBER` | Instance number used for instance registration (corresponds to the `INSTANCE_NUMBER` initialization parameter)  See Also: ["INSTANCE\_NUMBER"](initparams106.md) |
| `INSTANCE_NAME` | `VARCHAR2(16)` | Name of the instance |
| `HOST_NAME` | `VARCHAR2(64)` | Name of the host machine |
| `VERSION` | `VARCHAR2(17)` | Database version |
| `STARTUP_TIME` | `DATE` | Time when the instance was started |
| `STATUS` | `VARCHAR2(12)` | Status of the instance: - `STARTED` - After `STARTUP NOMOUNT` - `MOUNTED` - After `STARTUP MOUNT` or `ALTER DATABASE CLOSE` - `OPEN` - After `STARTUP` or `ALTER DATABASE OPEN` - `OPEN MIGRATE` - After `ALTER DATABASE OPEN { UPGRADE \| DOWNGRADE }` |
| `PARALLEL` | `VARCHAR2(3)` | Indicates whether the instance is mounted in cluster database mode (`YES`) or not (`NO`) |
| `THREAD#` | `NUMBER` | Redo thread opened by the instance |
| `ARCHIVER` | `VARCHAR2(7)` | Automatic archiving status: - `STOPPED` - `STARTED` - `FAILED` - Archiver failed to archive a log last time but will try again within 5 minutes |
| `LOG_SWITCH_WAIT` | `VARCHAR2(15)` | Event that log switching is waiting for: - `ARCHIVE LOG` - `CLEAR LOG` - `CHECKPOINT` - NULL - `ALTER SYSTEM SWITCH LOGFILE` is hung but there is room in the current online redo log |
| `LOGINS` | `VARCHAR2(10)` | Indicates whether the instance is in unrestricted mode, allowing logins by all users (`ALLOWED`, or in restricted mode, allowing logins by database administrators only (`RESTRICTED`) |
| `SHUTDOWN_PENDING` | `VARCHAR2(3)` | Indicates whether a shutdown is pending (`YES`) or not (`NO`) |
| `DATABASE_STATUS` | `VARCHAR2(17)` | Status of the database: - `ACTIVE` - `SUSPENDED` - `INSTANCE RECOVERY` |
| `INSTANCE_ROLE` | `VARCHAR2(18)` | Indicates whether the instance is an active instance (`PRIMARY_INSTANCE`) or an inactive secondary instance (`SECONDARY_INSTANCE`), or `UNKNOWN` if the instance has been started but not mounted |
| `ACTIVE_STATE` | `VARCHAR2(9)` | Quiesce state of the instance: - `NORMAL` - Database is in a normal state. - `QUIESCING` - `ALTER SYSTEM QUIESCE RESTRICTED` has been issued: no new user transactions, queries, or PL/SQL statements are processed in this instance. User transactions, queries, or PL/SQL statements issued before the `ALTER SYSTEM QUIESCE RESTRICTED` statement are unaffected. DBA transactions, queries, or PL/SQL statements are also unaffected. - `QUIESCED` - `ALTER SYSTEM QUIESCE RESTRICTED` has been issued: no user transactions, queries, or PL/SQL statements are processed. DBA transactions, queries, or PL/SQL statements are unaffected. User transactions, queries, or PL/ SQL statements issued after the `ALTER SYSTEM QUIESCE RESTRICTED` statement are not processed.  A single `ALTER SYSTEM QUIESCE RESTRICTED` statement quiesces all instances in an Oracle RAC environment. After this statement has been issued, some instances may enter into a quiesced state before other instances; the system is quiesced when all instances enter the quiesced state. |
| `BLOCKED` | `VARCHAR2(3)` | Indicates whether all services are blocked (`YES`) or not (`NO`) |