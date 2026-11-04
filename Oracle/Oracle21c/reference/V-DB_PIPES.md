---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-DB_PIPES.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.166 V$DB\_PIPES

`V$DB_PIPES` displays the pipes that are currently represented in the shared pool for this instance.

| Column | Datatype | Description |
| --- | --- | --- |
| `OWNERID` | `NUMBER` | Owner ID of the owner (if this is a private pipe), else NULL |
| `NAME` | `VARCHAR2(1000)` | Name of the pipe (for example, `SCOTT.PIPE`) |
| `TYPE` | `VARCHAR2(7)` | Type of the pipe:  - `PUBLIC` - `PRIVATE` |
| `PIPE_SIZE` | `NUMBER` | Amount of memory the pipe uses  Note: The value of this column may be larger than `maxpipesize` because of an internal algorithm. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |
| `CON_NAME` | `VARCHAR2(64)` | Container name of the object. The value of this column is `NULL` in non-CDBs. |