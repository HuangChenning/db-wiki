---
title: "V$LOGSTDBY_STATE"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2047.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$LOGSTDBY_STATE` provides consolidated information from `V$LOGSTDBY` and `V$LOGSTDBY_STATS` about the running state of Logical Standby.

| Column | Datatype | Description |
| --- | --- | --- |
| `PRIMARY_DBID` | `NUMBER` | Database ID (DBID) of the primary database |
| `SESSION_ID` | `NUMBER` | LogMiner session ID allocated to SQL Apply. |
| `REALTIME_APPLY` | `VARCHAR2(64)` | `Y` indicates that SQL Apply is running in real-time apply mode. If a standby redo log is configured, SQL Apply applies changes as they are written to the standby redo log files. `N` indicates that SQL Apply applies changes as each archived redo log file is received. |
| `STATE` | `VARCHAR2(64)` | - `INITIALIZING`: LogMiner session has been created and coordinator has attached to it - `LOADING DICTIONARY`: SQL Apply is loading the LogMiner dictionary - `WAITING ON GAP`: SQL Apply is waiting for a log file to be sent from the primary database - `APPLYING`: SQL Apply is actively mining or applying transactions - `WAITING FOR DICTIONARY LOGS`: SQL Apply is waiting for the archived logs containing the LogMiner dictionary to be shipped from the primary database - `IDLE`: SQL Apply has applied all changes available at the logical standby, and is caught up with the primary database |