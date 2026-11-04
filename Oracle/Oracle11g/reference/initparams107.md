---
title: INSTANCE_TYPE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams107.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `INSTANCE_TYPE = { RDBMS \| ASM }` |
| Default value | `RDBMS` |
| Modifiable | No |
| Basic | No |
| Oracle RAC | Multiple instances must have the same value. |

`INSTANCE_TYPE` specifies whether the instance is a database instance or an Automatic Storage Management instance.

Values:

- `RDBMS`
	The instance is a database instance.
- `ASM`
	The instance is an Automatic Storage Management instance.