---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DRCP_CONNECTION_LIMIT.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.116 DRCP\_CONNECTION\_LIMIT

`DRCP_CONNECTION_LIMIT` specifies the maximum number of Database Resident Connection Pooling (DRCP) connections for a PDB.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | In `CDB$ROOT`: `0` (unlimited)  In a PDB:  - If a persistent value for `SESSIONS` was explicitly set for the PDB (`ALTER` `SYSTEM` `SET` `SESSIONS` `=` `n` `SCOPE={SPFILE\|BOTH}`), and the PDB was subsequently restarted, then the default value is (10 \* `SESSIONS`). - Otherwise, the PDB inherits the value for this parameter from `CDB$ROOT`. |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Range of values | `0` to operating system-dependent  A value of `0` specifies that there is no limit on the number of DRCP connections. |
| Basic | No |
| Oracle RAC | Different instances can use different values. |

`DRCP_CONNECTION_LIMIT` is a PDB-inherited parameter. The value of this parameter in `CDB$ROOT` is not a CDB-wide limit. It is the default value for each PDB.

Note:

This parameter is available starting with Oracle Database 21c.