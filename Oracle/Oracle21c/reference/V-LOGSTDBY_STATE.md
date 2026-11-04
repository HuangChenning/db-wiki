---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-LOGSTDBY_STATE.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.62 V$LOGSTDBY\_STATE

`V$LOGSTDBY_STATE` provides consolidated information from `V$LOGSTDBY` and `V$LOGSTDBY_STATS` about the running state of Logical Standby.

| Column | Datatype | Description |
| --- | --- | --- |
| `PRIMARY_DBID` | `NUMBER` | Database ID (DBID) of the primary database |
| `PRIMARY_CON_DBID` | `NUMBER` | This column indicates the DBID of the source database or source PDB corresponding to the database (or CDB) from which this column is queried.For a non-CDB and the root of a CDB, this column matches the `PRIMARY_DBID` column.For a maintained PDB, this column indicates the DBID for the corresponding PDB at the source.For a skipped PDB or a local PDB, this column would be `NULL`. |
| `SESSION_ID` | `NUMBER` | LogMiner session ID allocated to SQL Apply. |
| `REALTIME_APPLY` | `VARCHAR2(64)` | `Y` indicates that SQL Apply is running in real-time apply mode. If a standby redo log is configured, SQL Apply applies changes as they are written to the standby redo log files. `N` indicates that SQL Apply applies changes as each archived redo log file is received. |
| `STATE` | `VARCHAR2(64)` | - `INITIALIZING`: LogMiner session has been created and coordinator has attached to it - `LOADING DICTIONARY`: SQL Apply is loading the LogMiner dictionary - `WAITING ON GAP`: SQL Apply is waiting for a log file to be sent from the primary database - `APPLYING`: SQL Apply is actively mining or applying transactions - `WAITING FOR DICTIONARY LOGS`: SQL Apply is waiting for the archived logs containing the LogMiner dictionary to be shipped from the primary database - `IDLE`: SQL Apply has applied all changes available at the logical standby, and is caught up with the primary database |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

- " [V$LOGSTDBY](V-LOGSTDBY.md) "
- " [V$LOGSTDBY\_STATS](V-LOGSTDBY_STATS.md) "