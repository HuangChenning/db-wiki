---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/PLSQL_CODE_TYPE.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.286 PLSQL\_CODE\_TYPE

`PLSQL_CODE_TYPE` specifies the compilation mode for PL/SQL library units.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `PLSQL_CODE_TYPE = { INTERPRETED \| NATIVE }` |
| Default value | `INTERPRETED` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Basic | No |

Values

- `INTERPRETED`
	PL/SQL library units will be compiled to PL/SQL bytecode format. Such modules are executed by the PL/SQL interpreter engine.
- `NATIVE`
	PL/SQL library units (with the possible exception of top-level anonymous PL/SQL blocks) will be compiled to native (machine) code. Such modules will be executed natively without incurring any interpreter overhead.

When the value of this parameter is changed, it has no effect on PL/SQL library units that have already been compiled. The value of this parameter is stored persistently with each library unit.

If a PL/SQL library unit is compiled native, all subsequent automatic recompilations of that library unit will use native compilation.

See Also:

[Oracle Database PL/SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=LNPLS188) for more information about this parameter