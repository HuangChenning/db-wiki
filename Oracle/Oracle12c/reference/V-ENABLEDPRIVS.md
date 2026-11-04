---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-ENABLEDPRIVS.html
tags:
  - oracle
  - 12c
  - reference
---

`V$ENABLEDPRIVS` displays the system privileges that have been granted to the current user and the currently enabled roles. These privileges can be found in the table `SYSTEM_PRIVILEGE_MAP`.

| Column | Datatype | Description |
| --- | --- | --- |
| `PRIV_NUMBER` | `NUMBER` | Numeric identifier of the system privilege |
| `SCOPE` | `VARCHAR2(11)` | Indicates the scope with which a privilege was granted. Possible values:  - `COMMON` - `APPLICATION` - `LOCAL` - `NULL` (if connected to a non-CDB )  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [SYSTEM\_PRIVILEGE\_MAP](SYSTEM_PRIVILEGE_MAP.md) "