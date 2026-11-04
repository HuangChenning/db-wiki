---
title: PLSQL_DEBUG
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams197.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `false` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Range of values | `true \| false` |

Note:

The `PLSQL_DEBUG` parameter is deprecated. It is retained for backward compatibility only.

`PLSQL_DEBUG` specifies whether or not PL/SQL library units will be compiled for debugging.

Values:

- `true`
	PL/SQL library units will be compiled for debugging
- `false`
	PL/SQL library units will be compiled for normal execution

When `PLSQL_DEBUG` is set to `true`, PL/SQL library units are always compiled `INTERPRETED` in order to be debuggable.

When the value of this parameter is changed, it has no effect on PL/SQL library units that have already been compiled. The value of this parameter is stored persistently with each library unit.