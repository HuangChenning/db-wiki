---
title: "V$MANAGED_STANDBY"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2050.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$MANAGED_STANDBY` displays current status information for some Oracle Database processes related to physical standby databases in the Data Guard environment. This view does not persist after an instance shutdown.

| Column | Datatype | Description |
| --- | --- | --- |
| `PROCESS` | `VARCHAR2(9)` | Type of the process whose information is being reported: - `RFS` - Remote file server - `MRP0` - Detached recovery server process - `MR(fg)` - Foreground recovery session - `ARCH` - Archiver process - `FGRD` - `LGWR` - `RFS(FAL)` - `RFS(NEXP)` - `LNS` - Network server process |
| `PID` | `NUMBER` | Operating system process identifier of the process |
| `STATUS` | `VARCHAR2(12)` | Current process status: - `UNUSED` - No active process - `ALLOCATED` - Process is active but not currently connected to a primary database - `CONNECTED` - Network connection established to a primary database - `ATTACHED` - Process is actively attached and communicating to a primary database - `IDLE` - Process is not performing any activities - `ERROR` - Process has failed - `OPENING` - Process is opening the archived redo log - `CLOSING` - Process has completed archival and is closing the archived redo log - `WRITING` - Process is actively writing redo data to the archived redo log - `RECEIVING` - Process is receiving network communication - `ANNOUNCING` - Process is announcing the existence of a potential dependent archived redo log - `REGISTERING` - Process is registering the existence of a completed dependent archived redo log - `WAIT_FOR_LOG` - Process is waiting for the archived redo log to be completed - `WAIT_FOR_GAP` - Process is waiting for the archive gap to be resolved - `APPLYING_LOG` - Process is actively applying the archived redo log to the standby database |
| `CLIENT_PROCESS` | `VARCHAR2(8)` | Identifies the corresponding primary database process: - `Archival` - Foreground (manual) archival process (SQL) - `ARCH` - Background `ARC` `n` process - `LGWR` - Background `LGWR` process |
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