---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-HM_CHECK.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.277 V$HM\_CHECK

`V$HM_CHECK` displays information about all the checks registered with Health Monitor. Each check is uniquely identified by a name or an ID.

| Column | Datatype | Description |
| --- | --- | --- |
| `ID` | `NUMBER` | Health check ID |
| `NAME` | `VARCHAR2(64)` | Health check name |
| `NAME_NLS` | `VARCHAR2(1024)` | Internationalized names of the health checks |
| `CLSID` | `NUMBER` | Class ID to which this check belongs |
| `CLS_NAME` | `VARCHAR2(15)` | Class name of the check:  - `GENERIC` - `PERSISTENT_DATA` |
| `FLAGS` | `NUMBER` | Reserved for internal use |
| `INTERNAL_CHECK` | `VARCHAR2(1)` | Internal check |
| `OFFLINE_CAPABLE` | `VARCHAR2(1)` | Ability to run when database is not open yet (Y or N) |
| `DESCRIPTION` | `VARCHAR2(1024)` | Description of what the check does |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |