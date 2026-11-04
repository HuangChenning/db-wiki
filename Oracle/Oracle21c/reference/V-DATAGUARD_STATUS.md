---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-DATAGUARD_STATUS.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.163 V$DATAGUARD\_STATUS

`V$DATAGUARD_STATUS` displays messages recently written to the alert log or server process trace files that concern physical standby databases or redo transport services for all standby database types.

| Column | Datatype | Description |
| --- | --- | --- |
| `FACILITY` | `VARCHAR2(24)` | Facility that encountered the event:  - `Crash Recovery` - `Log Transport Services` - `Log Apply Services` - `Role Management Services` - `Remote File Server` - `Fetch Archive Log` - `Data Guard` - `Network Services` |
| `SEVERITY` | `VARCHAR2(13)` | Severity of the event:  - `Informational` - Informational message - `Warning` - Warning message - `Error` - Indicates the process has failed - `Fatal` - `Control` - An expected change in state such as the start or completion of an archival, log recovery, or switchover operation |
| `DEST_ID` | `NUMBER` | Destination ID number to which the event pertains. If the event does not pertain to a particular destination, then the value is `0`. |
| `MESSAGE_NUM` | `NUMBER` | A chronologically increasing number giving each event a unique number |
| `ERROR_CODE` | `NUMBER` | Error ID pertaining to the event |
| `CALLOUT` | `VARCHAR2(3)` | Reserved for future use |
| `TIMESTAMP` | `DATE` | Message date |
| `MESSAGE` | `VARCHAR2(256)` | A text message describing the event |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |