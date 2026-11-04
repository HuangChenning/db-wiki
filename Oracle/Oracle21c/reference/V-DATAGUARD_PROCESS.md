---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-DATAGUARD_PROCESS.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.161 V$DATAGUARD\_PROCESS

`V$DATAGUARD_PROCESS` displays one row for each Oracle Data Guard process that is currently running.

| Column | Datatype | Description |
| --- | --- | --- |
| `NAME` | `VARCHAR2(5)` | Name of the process whose information is being reported. Some of the possible values include:  - ARCn - Archiver process - DTS - Data transport process - FAL - File/announce process - LGWR - Log Writer Process - MRP0 - Detached recovery server process - NSSn - SYNC Redo Transport process - ORA - Foreground process - RFS - Remote file server - RMI - Remote message process - TMON - Redo Transport Process monitor - TTnn - Redo Transport Worker Process |
| `PID` | `VARCHAR2(24)` | Operating system process identifier of the process |
| `TYPE` | `VARCHAR2(3)` | Indicates which Oracle subsystem created the process. Possible values:  - KSB - KSV - NET - UNK |
| `ROLE` | `VARCHAR2(25)` | Role of the process. Possible values:  - test - async ORL multi - async ORL single - async SRL multi - async SRL single - log writer - sync - archive redo - archive local - archive gap - RFS async - RFS sync - RFS archive - RFS gap - RFS SMON - data transport - data receive - redo transport monitor - heartbeat redo informer - process kill - post role transition - gap manager - update TMI - RFS ping - FAL gap - FAL announce - failover - switchover - remote failover - remote switchover - redo transport timer - announce request - managed recovery PSBY BG - managed recovery PSBY FG - controlfile update - broker monitor - broker worker - broker net slave - broker instance slave - fast-start failover ping - recovery coordinator - recovery logmerger - recovery apply slave - recovery sending slave - recovery receiving slave - redo transport test - temporary - datafile pre-create - redo log management - managed recovery DGPDB BG - managed recovery DGPDB FG - Compress ORL master - Compress ORL worker - Compress SRL master - Compress SRL worker - UNKNOWN |
| `PROC_TIME` | `TIMESTAMP(0)` | Timestamp of when the process started or registered for inclusion in this fixed view |
| `TASK_TIME` | `TIMESTAMP(0)` | Timestamp of when the first task of the process was requested |
| `TASK_DONE` | `VARCHAR2(1)` | Indicates whether the task performed by the process is done (`Y`) or not (`N`) |
| `ACTION` | `VARCHAR2(12)` | Current action of the process. Possible values can include:  - `ANNOUNCING` - `APPLYING_LOG` - `ATTACHED` - `CLOSING` - `CONNECTED` - `ERROR` - `IDLE` - `OPENING` - `PROCESSING` - `RECEIVING` - `REGISTERING` - `STARTING` - `TERMINATING` - `UNKNOWN` - `UNUSED` - `WAIT_FOR_GAP` - `WAIT_FOR_LOG` - `WRITING` |
| `CLIENT_PID` | `NUMBER` | For RFS and DTS processes, the PID of the process communicating with this process |
| `CLIENT_ROLE` | `VARCHAR2(16)` | For RFS and DTS processes, the role of the process communicating with this process.  Possible values can include:  - none - async ORL multi - async ORL single - async SRL multi - async SRL single - log writer - sync - archive redo - archive gap - data transport - gap manager - failover - switchover - announce request - managed recovery - recovery - UNKNOWN |
| `GROUP#` | `NUMBER` | Group number of the log that the process is operating upon |
| `RESETLOG_ID` | `NUMBER` | Resetlog ID (branch) of the log that the process is operating upon |
| `THREAD#` | `NUMBER` | Thread number that the process is operating upon |
| `SEQUENCE#` | `NUMBER` | Sequence number that the process is operating upon |
| `BLOCK#` | `NUMBER` | Starting block number that the process is operating upon |
| `BLOCK_COUNT` | `NUMBER` | Number of blocks that the process is operating upon |
| `DELAY_MINS` | `NUMBER` | Archived redo log delay interval in minutes |
| `DEST_ID` | `NUMBER` | Destination ID that the process is currently operating upon |
| `DEST_MASK` | `NUMBER` | Mask of all destination IDs that the process will operate upon, where:  - Bit 0 is LOG\_ARCHIVE\_DEST1 - Bit 1 is LOG\_ARCHIVE\_DEST2 - Bit 2 is LOG\_ARCHIVE\_DEST3  and so on. |
| `TENANT_KEY` | `NUMBER` | Unique identifier assigned to each customer in the Oracle Cloud  If the database is not in the cloud, then the value of this column is `0`.  The combination of `TENANT_KEY` and `DBID` can be used to uniquely identify a database. |
| ` DBID` | `NUMBER` | Database ID of the redo that the process is operating upon |
| `DGID` | `NUMBER` | Data Guard ID that the process must communicate with |
| `INSTANCE` | `NUMBER` | Instance number that the process must communicate with at the specified DGID |
| `STOP_STATE` | `VARCHAR2(7)` | Indicates the method by which the process has been requested to stop:  - NOW - Requested to stop immediately and exit - SOON - Requested to stop on next log and exit - COMMIT - Requested to write remaining redo and exit - N/A - No request to stop |
| `APPLY` | `NUMBER` | SCN at which the database has applied redo |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

Note:

Oracle recommends that you use this view instead of `V$MANAGED_STANDBY`.