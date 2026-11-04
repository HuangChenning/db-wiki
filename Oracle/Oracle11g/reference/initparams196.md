---
title: PLSQL_CODE_TYPE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams196.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `PLSQL_CODE_TYPE = { INTERPRETED \| NATIVE }` |
| Default value | `INTERPRETED` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |

`PLSQL_CODE_TYPE` specifies the compilation mode for PL/SQL library units.

Values:

- `INTERPRETED`
	PL/SQL library units will be compiled to PL/SQL bytecode format. Such modules are executed by the PL/SQL interpreter engine.
- `NATIVE`
	PL/SQL library units (with the possible exception of top-level anonymous PL/SQL blocks) will be compiled to native (machine) code. Such modules will be executed natively without incurring any interpreter overhead.

When the value of this parameter is changed, it has no effect on PL/SQL library units that have already been compiled. The value of this parameter is stored persistently with each library unit.

If a PL/SQL library unit is compiled native, all subsequent automatic recompilations of that library unit will use native compilation.