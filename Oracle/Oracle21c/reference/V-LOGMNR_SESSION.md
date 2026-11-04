---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-LOGMNR_SESSION.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.57 V$LOGMNR\_SESSION

`V$LOGMNR_SESSION` displays information about active LogMiner persistent sessions.

(A LogMiner persistent session is created either by starting Data Guard SQL Apply on a logical standby database for the first time or by creating Replication capture.) Transient LogMiner sessions (those created as a result of querying the `V$LOGMNR_CONTENTS` view) do not show up in the `V$LOGMNR_SESSION` view. The statistics shown in this view correspond to snapshots of the system and are not cumulative in nature.

| Column | Datatype | Description |
| --- | --- | --- |
| `SESSION_ID` | `NUMBER` | Unique identifier for the LogMiner persistent session |
| `SESSION_NAME` | `VARCHAR2(32)` | Unique session name |
| `SESSION_STATE` | `VARCHAR2(9)` | Current state of the LogMiner persistent session:  - `READY` - Client has created the LogMiner persistent session and added the relevant archived redo log files, but has not loaded the initial LogMiner dictionary - `STARTED` - The LogMiner dictionary has been loaded - `ACTIVE` - The LogMiner persistent session is mining the redo stream - `DETACHED` - The LogMiner persistent session is not currently active, and it is in the process of becoming inactive - `DISCARDED` - Client is about to destroy the LogMiner persistent session |
| `DB_NAME` | `VARCHAR2(128)` | Global database name for the source database |
| `DB_ID` | `NUMBER` | Database identifier of the source database |
| `RESET_SCN` | `NUMBER` | System change number (SCN) when the session started |
| `RESET_TIMESTAMP` | `NUMBER` | Time of the `RESETLOG` s when the LogMiner persistent session started |
| `RESET_TIME` | `DATE` | The time when the session started |
| `NUM_PROCESS` | `NUMBER` | Number of processes allocated to this session |
| `CHUNK_SIZE` | `NUMBER` | Amount of memory allocated for this chunk |
| `START_SCN` | `NUMBER` | System change number (SCN) at start of the session |
| `END_SCN` | `NUMBER` | System change number (SCN) at end of the session |
| `SPILL_SCN` | `NUMBER` | In the event of a restart, redo records with an SCN lower than this will not be read from the archived redo log files |
| `PROCESSED_SCN` | `NUMBER` | The `BUILDER` process has successfully mined redo records up to this SCN |
| `PROCESSED_TIME` | `DATE` | The `BUILDER` process has successfully mined redo records up to this time |
| `PREPARED_SCN` | `NUMBER` | The `PREPARER` processes have successfully transformed all redo records below this SCN into logical change records (LCRs). However the LCRs may not have been grouped into transactions or merged in case they pertain to chained rows or LOB updates. |
| `READ_SCN` | `NUMBER` | The `READER` process has read all redo records below this SCN |
| `LOW_MARK_SCN` | `NUMBER` | LogMiner has delivered all transactions that committed below this SCN to the client |
| `CONSUMED_SCN` | `NUMBER` | Client has consumed and released all transactions that committed below this SCN. |
| `MAX_MEMORY_SIZE` | `NUMBER` | Maximum amount of shared memory (in bytes) that LogMiner is allowed to consume |
| `USED_MEMORY_SIZE` | `NUMBER` | Amount of shared memory (in bytes) actually consumed by LogMiner |
| `BUILDER_WORK_SIZE` | `NUMBER` | Amount of redo (in bytes) in the current work unit being processed by the BUILDER process. |
| `PREPARED_WORK_SIZE` | `NUMBER` | Amount of redo (in bytes) that has been prepared by LogMiner |
| `AVAILABLE_WORK_SIZE` | `NUMBER` | Amount of redo records (in bytes) that are ready, but are yet to be consumed by the client |
| `AVAILABLE_TXN` | `NUMBER` | Number of transaction chunks ready for consumption |
| `AVAILABLE_COMMITTED_TXN` | `NUMBER` | Number of committed transactions ready for consumption. This is less than, or equal to, `AVAILABLE_TXN`. |
| `DELIVERED_TXN` | `NUMBER` | Number of transaction chunks that the client currently has in its possession |
| `DELIVERED_COMMITTED_TXN` | `NUMBER` | Number of committed transaction chunks that the client is currently working on. This is less than, or equal to, the value of the `DELIVERED_TXN` column. |
| `PINNED_TXN` | `NUMBER` | Number of transactions pinned (the client is actively working on) |
| `PINNED_COMMITTED_TXN` | `NUMBER` | Number of committed transactions pinned (the client is actively working on) |
| `CHECKPOINT_INTERVAL` | `NUMBER` | Checkpoint interval |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [V$LOGMNR\_CONTENTS](V-LOGMNR_CONTENTS.md) "