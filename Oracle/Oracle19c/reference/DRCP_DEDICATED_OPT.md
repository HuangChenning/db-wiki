---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/DRCP_DEDICATED_OPT.html
tags:
  - oracle
  - 19c
  - reference
---

## 1.114 DRCP\_DEDICATED\_OPT

Use `DRCP_DEDICATED_OPT` to enable or disable the use of dedicated optimization with Database Resident Connection Pooling (DRCP).

Dedicated optimization makes DRCP behave like a dedicated server when the number of connections to the DRCP broker is less than the DRCP maximum size.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `DRCP_DEDICATED_OPT = { YES \| NO }` |
| Default value | `YES` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Basic | No |
| Oracle RAC | Different instances can use different values. |

When the value of this parameter is set to `YES`, the use of dedicated optimization with DRCP is enabled. When it is set to `NO`, the use of dedicated optimization with DRCP is disabled.

Note:

This parameter is available starting with Oracle Database 19c, Release Update 19.11.

See Also:

[Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/refrn&id=ADMIN-GUID-82FF6896-F57E-41CF-89F7-755F3BC9C924) for more information about setting this parameter