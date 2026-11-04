---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-SESSION_FIX_CONTROL.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.22 V$SESSION\_FIX\_CONTROL

`V$SESSION_FIX_CONTROL` displays information about Fix Control (enabled/disabled) for the current session.

| Column | Datatype | Description |
| --- | --- | --- |
| `SESSION_ID` | `NUMBER` | Session identifier (can be used to join this view with `V$SESSION`) |
| `BUGNO` | `NUMBER` | Bug number (as fix control identifier) |
| `VALUE` | `NUMBER` | Current value set for the fix control |
| `SQL_FEATURE` | `VARCHAR2(64)` | Feature control ID |
| `DESCRIPTION` | `VARCHAR2(64)` | Description of the fix control |
| `OPTIMIZER_FEATURE_ENABLE` | `VARCHAR2(25)` | Version on (and after) which the fix is enabled by default |
| `EVENT` | `NUMBER` | Event formerly used to control the fix |
| `IS_DEFAULT` | `NUMBER` | Indicates whether the current value is the same as the default (`1`) or not (`0`) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |