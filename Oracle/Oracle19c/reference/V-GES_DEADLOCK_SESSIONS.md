---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/V-GES_DEADLOCK_SESSIONS.html
tags:
  - oracle
  - 19c
  - reference
---

## 7.247 V$GES\_DEADLOCK\_SESSIONS

`V$GES_DEADLOCK_SESSIONS` displays information about sessions waiting for global enqueue service deadlocks detected by the distributed lock manager. This is an Oracle Real Application Clusters view.

This view displays a maximum of 20 sessions per deadlock.

| Column | Datatype | Description |
| --- | --- | --- |
| `DID` | `VARCHAR2(30)` | Deadlock ID |
| `SID` | `NUMBER` | Waiting session ID |
| `SERIAL#` | `NUMBER` | Waiting session serial number |
| `INSTANCE` | `NUMBER` | Waiting session instance |
| `BLOCKER_SID` | `NUMBER` | Blocker session ID |
| `BLOCKER_SERIAL#` | `NUMBER` | Blocker session serial number |
| `BLOCKER_INSTANCE` | `NUMBER` | Blocker session instance |
| `OSUSER` | `VARCHAR2(128)` | Waiting OS user |
| `APP_NAME` | `VARCHAR2(64)` | Waiting application name |
| `BLOCKED_RES_NAME` | `VARCHAR2(64)` | Resource on which the waiting session is blocked |
| `REQUEST_LEVEL` | `VARCHAR2(16)` | Waiting session requested level |
| `BLOCKER_RES_NAME` | `VARCHAR2(64)` | Resource on which the blocker is blocked |
| `GRANT_LEVEL` | `VARCHAR2(16)` | Granted level of the blocker |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |