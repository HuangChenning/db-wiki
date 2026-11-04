---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-MVREFRESH.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.87 V$MVREFRESH

`V$MVREFRESH` displays information about the materialized views currently being refreshed.

| Column | Datatype | Description |
| --- | --- | --- |
| `SID` | `NUMBER` | Session identifier |
| `SERIAL#` | `NUMBER` | Session serial number, which is used to uniquely identify a session's objects. Guarantees that session-level commands are applied to the correct session objects if the session ends with, and another session begins with, the same session ID. |
| `CURRMVOWNER` | `VARCHAR2(31)` | Owner of the materialized view currently being refreshed. The materialized view resides in this user's schema. |
| `CURRMVNAME` | `VARCHAR2(31)` | Name of the materialized view currently being refreshed |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |