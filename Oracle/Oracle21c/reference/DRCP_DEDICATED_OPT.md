---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DRCP_DEDICATED_OPT.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.117 DRCP\_DEDICATED\_OPT

Use `DRCP_DEDICATED_OPT` to enable or disable the use of dedicated optimization with Database Resident Connection Pooling (DRCP).

Dedicated optimization causes DRCP to behave like a dedicated server when the number of connections to the DRCP broker is less than the DRCP maximum size.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `DRCP_DEDICATED_OPT = { YES \| NO }` |
| Default value | `NO` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | Yes, according to the following guidelines:  - When the `ENABLE_PER_PDB_DRCP` initialization parameter is set to `true`, `DRCP_DEDICATED_OPT` can be modified only at the PDB level; it cannot be modified for the CDB root. - When the `ENABLE_PER_PDB_DRCP` initialization parameter is set to `false`, `DRCP_DEDICATED_OPT` can be modified only for the CDB root; it cannot be modified at the PDB level. |
| Basic | No |
| Oracle RAC | Different instances can use different values. |

When the value of this parameter is set to `YES`, the use of dedicated optimization with DRCP is enabled. When it is set to `NO`, the use of dedicated optimization with DRCP is disabled.

Note:

This parameter is available starting with Oracle Database release 19c, version 19.11.

See Also:

- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADMIN-GUID-82FF6896-F57E-41CF-89F7-755F3BC9C924) for more information about setting this parameter
- " [ENABLE\_PER\_PDB\_DRCP](ENABLE_PER_PDB_DRCP.md) "