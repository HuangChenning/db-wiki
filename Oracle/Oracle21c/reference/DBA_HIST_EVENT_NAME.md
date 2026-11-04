---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_EVENT_NAME.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.403 DBA\_HIST\_EVENT\_NAME

This view contains a snapshot of `V$EVENT_NAME`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID |
| `EVENT_ID` | `NUMBER` | `NOT NULL` | Identifier of the wait event |
| `EVENT_NAME` | `VARCHAR2(64)` | `NOT NULL` | Name of the wait event |
| `PARAMETER1` | `VARCHAR2(64)` |  | Description of the first parameter for the wait event |
| `PARAMETER2` | `VARCHAR2(64)` |  | Description of the second parameter for the wait event |
| `PARAMETER3` | `VARCHAR2(64)` |  | Description of the third parameter for the wait event |
| `WAIT_CLASS_ID` | `NUMBER` |  | Identifier of the class of the wait event |
| `WAIT_CLASS` | `VARCHAR2(64)` |  | Name of the class of the wait event |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [V$EVENT\_NAME](V-EVENT_NAME.md) "