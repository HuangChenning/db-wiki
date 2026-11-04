---
title: PLSCOPE_SETTINGS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams194.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `PLSCOPE_SETTINGS = IDENTIFIERS:{ NONE \| ALL }` |
| Default value | `IDENTIFIERS:NONE` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Basic | No |

`PLSCOPE_SETTINGS` controls the compile time collection, cross reference, and storage of PL/SQL source code identifier data.

Values:

- `IDENTIFIERS:NONE`
	Disables collection of identifier data. This is the default.
- `IDENTIFIERS:ALL`
	Enables the collection of all source code identifier data.

`PLSCOPE_SETTINGS` can be set on a session, system, or per-library unit (`ALTER COMPILE`) basis. The current setting of `PLSCOPE_SETTINGS` for any library unit can be attained by querying the `*_PLSQL_OBJECT_SETTINGS` views. Any identifier data collected by setting this parameter can be accessed using the `*_IDENTIFIERS` views.