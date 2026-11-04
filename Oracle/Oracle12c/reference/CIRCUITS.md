---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/CIRCUITS.html
tags:
  - oracle
  - 12c
  - reference
---

`CIRCUITS` specifies the total number of virtual circuits that are available for inbound and outbound network sessions.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `4294967295` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Basic | No |

It is one of several parameters that contribute to the total SGA requirements of an instance.

You should not specify a value for this parameter unless you want to limit the number of virtual circuits.

See Also:

- [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=CNCPT7776) for more information on memory structures
- [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=CNCPT008) for more information on processes