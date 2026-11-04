---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-GES_DEADLOCKS.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.256 V$GES\_DEADLOCKS

`V$GES_DEADLOCKS` displays information about global enqueue service deadlocks detected by the distributed lock manager. This is an Oracle Real Application Clusters view.

This view displays the 20 most recent deadlocks.

| Column | Datatype | Description |
| --- | --- | --- |
| `DID` | `VARCHAR2(30)` | Deadlock ID |
| `DD_TIME` | `DATE` | Deadlock timestamp |
| `NUMBER_OF_SESSIONS` | `NUMBER` | Number of sessions involved in the deadlock |
| `MASTER_INSTANCE` | `NUMBER` | Master instance of the resource |
| `VICTIM_INSTANCE` | `NUMBER` | Victim instance |
| `VICTIM_PID` | `VARCHAR2(24)` | OS process ID of the victim |
| `VICTIM_RESNM` | `VARCHAR2(64)` | Resource involved in the deadlock |
| `VICTIM_SID` | `NUMBER` | Session ID of the victim |
| `VICTIM_SERIAL#` | `NUMBER` | Session serial number of the victim |
| `VICTIM_REQ_LEVEL` | `VARCHAR2(16)` | Level of the lock being requested by the victim |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |