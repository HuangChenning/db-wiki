---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-HS_AGENT.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.283 V$HS\_AGENT

`V$HS_AGENT` displays the set of HS agents currently running on a given host. There is one row per agent process.

| Column | Datatype | Description |
| --- | --- | --- |
| `AGENT_ID` | `NUMBER` | Oracle Net session identifier used for connections to the agent (the identifier used in the `LISTENER.ORA` file) |
| `MACHINE` | `VARCHAR2(64)` | Operating system machine name |
| `PROCESS` | `VARCHAR2(9)` | Operating system process identifier of the agent |
| `PROGRAM` | `VARCHAR2(48)` | Program name of the agent |
| `OSUSER` | `VARCHAR2(128)` | Operating system user |
| `STARTTIME` | `DATE` | Starting time |
| `AGENT_TYPE` | `NUMBER` | Type of the agent |
| `FDS_CLASS_ID` | `NUMBER` | ID of the Foreign Data Store class |
| `FDS_INST_ID` | `NUMBER` | Instance name of the Foreign Data Store |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |