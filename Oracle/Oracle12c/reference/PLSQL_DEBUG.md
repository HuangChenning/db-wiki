---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/PLSQL_DEBUG.html
tags:
  - oracle
  - 12c
  - reference
---

`PLSQL_DEBUG` specifies whether or not PL/SQL library units will be compiled for debugging.

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `false` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Range of values | `true \| false` |
| Basic | No |

Note:

The `PLSQL_DEBUG` parameter is deprecated. It is retained for backward compatibility only.

Values

- `true`
	PL/SQL library units will be compiled for debugging
- `false`
	PL/SQL library units will be compiled for normal execution

When `PLSQL_DEBUG` is set to `true`, PL/SQL library units are always compiled `INTERPRETED` in order to be debuggable.

When the value of this parameter is changed, it has no effect on PL/SQL library units that have already been compiled. The value of this parameter is stored persistently with each library unit.