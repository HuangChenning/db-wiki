---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/FAL_SERVER.html
tags:
  - oracle
  - 12c
  - reference
---

`FAL_SERVER` specifies the FAL (fetch archive log) server for a standby database.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `FAL_SERVER = ` `string` |
| Default value | There is no default value. |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Basic | No |

The value is an Oracle Net service name, which is assumed to be configured properly on the standby database system to point to the desired FAL server.

See Also:

[Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=SBYDB4876) for more information about FAL server