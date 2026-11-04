---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_BLOCKERS.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.209 DBA\_BLOCKERS

`DBA_BLOCKERS` displays a session if it is not waiting for a locked object but is holding a lock on an object for which another session is waiting.

In an Oracle RAC environment, this only applies if the blocker is on the same instance.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `HOLDING_SESSION` | `NUMBER` |  | Session holding a lock |
| `CON_ID` | `NUMBER` |  | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire multitenant container database (CDB). This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |