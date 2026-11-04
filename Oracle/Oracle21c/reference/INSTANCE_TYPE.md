---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/INSTANCE_TYPE.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.166 INSTANCE\_TYPE

`INSTANCE_TYPE` specifies whether the instance is a database instance, an Oracle Automatic Storage Management (Oracle ASM) instance, or an Oracle ASM Proxy instance.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `INSTANCE_TYPE = { RDBMS \| ASM \| ASMPROXY }` |
| Default value | `RDBMS` |
| Modifiable | No |
| Modifiable in a PDB | No |
| Basic | No |
| Oracle RAC | Multiple instances must have the same value. |

Values

- `RDBMS`
	The instance is a database instance.
- `ASM`
	The instance is an Oracle ASM instance.
- `ASMPROXY`
	The instance is an Oracle ASM proxy instance.

See Also:

[Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=OSTMG-GUID-DE759521-9CF3-45D9-9123-7159C9ED4D30) for information about managing Oracle Flex ASM