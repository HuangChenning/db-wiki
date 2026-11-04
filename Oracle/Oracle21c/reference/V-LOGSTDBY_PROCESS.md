---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-LOGSTDBY_PROCESS.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.60 V$LOGSTDBY\_PROCESS

`V$LOGSTDBY_PROCESS` displays dynamic information about what is happening to the Data Guard log apply services.

This view is helpful when diagnosing performance problems during the logical application of archived redo logs to the standby database, and it can be helpful for other problems. This view is for logical standby databases only.

| Column | Datatype | Description |
| --- | --- | --- |
| `SID` | `NUMBER` | Session id of the associated session. This matches the `SID` column of the corresponding row in the `V$SESSION` view. |
| `SERIAL#` | `NUMBER` | Serial number of the associated session. Together, (`SID`,`SERIAL#`) uniquely identify the session in the current database instance. |
| `LOGSTDBY_ID` | `NUMBER` | Parallel query worker ID |
| `SPID` | `VARCHAR2(24)` | This corresponds to the `SPID` value of the row corresponding to this process in the `V$PROCESS` view |
| `TYPE` | `VARCHAR2(128)` | Role that the process plays in the context of SQL Apply:  - `COORDINATOR` - `APPLIER` - `ANALYZER` - `READER` - `PREPARER` - `BUILDER` |
| `STATUS_CODE` | `NUMBER` | Operation code identifying the current action of the process:  - `16111` - SQL Apply process is initializing - `16112` - SQL Apply process is cleaning up as apply and mining processes are stopping based on a user command - `16116` - SQL Apply process is idle - `16117` - SQL Apply process is busy and is not waiting on any interesting event - `16110` - `APPLIER` process has invoked a user-provided stored procedure in order to inspect a DDL statement prior to it being processed - `16113` - `APPLIER` process is applying DML changes to some user object or to a sequence - `16114` - `APPLIER` process is applying a DDL change - `16115` - `COORDINATOR` process is loading the LogMiner dictionary from the redo stream - `16243` - `BUILDER` process is paging out memory to free up space in lcr cache - `16240` - `READER` process idle waiting for additional logfile to be available - `16241` - `READER` process is idle waiting for the logfile to fill the log sequence gap - `16242` - `READER` process is processing a logfile |
| `STATUS` | `VARCHAR2(256)` | Description of the current action of the process |
| `HIGH_SCN` | `NUMBER` | Identifies the highest redo record/LCR processed by this process |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |