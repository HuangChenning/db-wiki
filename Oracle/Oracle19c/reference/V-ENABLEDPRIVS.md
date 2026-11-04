---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/V-ENABLEDPRIVS.html
tags:
  - oracle
  - 19c
  - reference
---

## 7.201 V$ENABLEDPRIVS

`V$ENABLEDPRIVS` displays the system privileges that have been granted to the current user directly or through the currently enabled roles.

| Column | Datatype | Description |
| --- | --- | --- |
| `PRIV_NUMBER` | `NUMBER` | Numeric identifier of the system privilege  The matching privilege name for each `PRIV_NUMBER` can be found in the table `SYSTEM_PRIVILEGE_MAP`. |
| `SCOPE` | `VARCHAR2(11)` | Indicates the scope with which a privilege was granted. Possible values:  - `COMMON` - `APPLICATION` - `LOCAL` - `NULL` (if connected to a non-CDB ) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [SYSTEM\_PRIVILEGE\_MAP](SYSTEM_PRIVILEGE_MAP.md) "