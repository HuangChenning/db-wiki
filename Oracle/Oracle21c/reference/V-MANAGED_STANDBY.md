---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-MANAGED_STANDBY.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.65 V$MANAGED\_STANDBY

`V$MANAGED_STANDBY` displays current status information for some Oracle Database processes related to physical standby databases in the Data Guard environment. This view does not persist after an instance shutdown.

| Column | Datatype | Description |
| --- | --- | --- |
| `PROCESS` | `VARCHAR2(9)` | Type of the process whose information is being reported:  - `RFS` - Remote file server - `MRP0` - Detached recovery server process - `MR(fg)` - Foreground recovery session - `ARCH` - Archiver process - `DGRD` - Generic Oracle Data Guard process - `FGRD` - `LGWR` - `RFS(FAL)` - `RFS(NEXP)` - `LNS` - ASYNC Redo Transport process |
| `PID` | `VARCHAR2(24)` | Operating system process identifier of the process |
| `STATUS` | `VARCHAR2(12)` | Current process status:  - `ALLOCATED` - Process is active but not currently connected to a primary database - `ANNOUNCING` - Process is announcing the existence of a potential dependent archived redo log - `APPLYING_LOG` - Process is actively applying the archived redo log to the standby database - `ATTACHED` - Process is actively attached and communicating to a primary database - `CLOSING` - Process has completed archival and is closing the archived redo log - `CONNECTED` - Network connection established to a primary database - `ERROR` - Process has failed - `IDLE` - Process is not performing any activities - `OPENING` - Process is opening the archived redo log - `RECEIVING` - Process is receiving network communication - `REGISTERING` - Process is registering the existence of a completed dependent archived redo log - `UNUSED` - No active process - `WAIT_FOR_GAP` - Process is waiting for the archive gap to be resolved - `WAIT_FOR_LOG` - Process is waiting for the archived redo log to be completed - `WRITING` - Process is actively writing redo data to the archived redo log |
| `CLIENT_PROCESS` | `VARCHAR2(8)` | Identifies the corresponding primary database process:  - `Archival` - Foreground (manual) archival process (SQL) - `ARCH` - Background `ARC` `n` process - `LGWR` - Background `LGWR` process |
| `CLIENT_PID` | `VARCHAR2(40)` | Operating system process identifier of the client process |
| `CLIENT_DBID` | `VARCHAR2(40)` | Database identifier of the primary database |
| `GROUP#` | `VARCHAR2(40)` | Standby redo log group |
| `RESETLOG_ID` | `NUMBER` | Resetlogs identifier of the archived redo log |
| `THREAD#` | `NUMBER` | Archived redo log thread number |
| `SEQUENCE#` | `NUMBER` | Archived redo log sequence number |
| `BLOCK#` | `NUMBER` | Last processed archived redo log block number |
| `BLOCKS` | `NUMBER` | Count (in 512-byte blocks) of the last write to a redo log, or for a recovery process, the expected final read count |
| `DELAY_MINS` | `NUMBER` | Archived redo log delay interval in minutes |
| `KNOWN_AGENTS` | `NUMBER` | Total number of standby database agents processing an archived redo log |
| `ACTIVE_AGENTS` | `NUMBER` | Number of standby database agents actively processing an archived redo log |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

Note:

This view is deprecated in Oracle Database 12c Release 2 (12.2.0.1) and may be desupported in a future release. The `V$DATAGUARD_PROCESS` view should be used, instead.

See Also:

" [V$DATAGUARD\_PROCESS](V-DATAGUARD_PROCESS.md) "