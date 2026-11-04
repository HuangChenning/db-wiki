---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-ENABLEDPRIVS.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.196 V$ENABLEDPRIVS

`V$ENABLEDPRIVS` displays the system privileges that have been granted to the current user directly or through the currently enabled roles.

| Column | Datatype | Description |
| --- | --- | --- |
| `PRIV_NUMBER` | `NUMBER` | Numeric identifier of the system privilege  The matching privilege name for each `PRIV_NUMBER` can be found in the table `SYSTEM_PRIVILEGE_MAP`. |
| `SCOPE` | `VARCHAR2(11)` | Indicates the scope with which a privilege was granted. Possible values:  - `COMMON` - `APPLICATION` - `LOCAL` |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [SYSTEM\_PRIVILEGE\_MAP](SYSTEM_PRIVILEGE_MAP.md) "