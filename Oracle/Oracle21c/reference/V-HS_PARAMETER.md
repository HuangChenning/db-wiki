---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-HS_PARAMETER.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.284 V$HS\_PARAMETER

`V$HS_PARAMETER` describes the initialization parameters in use by the server and agent.

| Column | Datatype | Description |
| --- | --- | --- |
| `HS_SESSION_ID` | `NUMBER` | Unique HS session identifier (maps to the `HS_SESSION_ID` column of `V$HS_SESSION`) |
| `PARAMETER` | `VARCHAR2(128)` | Name of the parameter |
| `VALUE` | `VARCHAR2(64)` | Value of the parameter |
| `SOURCE` | `VARCHAR2(1)` | Indicates whether the parameter was defined in the agent (`A`) or server (`S`) |
| `ENV` | `VARCHAR2(1)` | Indicates whether the parameter was set as an environment variable in the agent (`T`) or elsewhere (`F`) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |