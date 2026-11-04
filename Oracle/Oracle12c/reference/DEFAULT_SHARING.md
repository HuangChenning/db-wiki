---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DEFAULT_SHARING.html
tags:
  - oracle
  - 12c
  - reference
---

`DEFAULT_SHARING` sets the value of the sharing clause in statements creating objects in an application root.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `DEFAULT_SHARING = { NONE \| METADATA \| DATA \| EXTENDED DATA }` |
| Default value | For types of objects that support sharing, `METADATA` is the default.  For types of objects that do not support sharing, `NONE` is the default. |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Basic | No |
| Oracle RAC | All instances must have the same value |

Specifying `SHARING=` in the create DDL overrides the value of the `DEFAULT_SHARING` parameter.

Note:

This initialization parameter is available starting with Oracle Database 12c Release 2 (12.2.0.1).

Example

Issuing the following `ALTER SYSTEM` statement in an application root sets the default value of the sharing clause to `NONE` in the server parameter file for the application root:

```
ALTER SYSTEM SET DEFAULT_SHARING = NONE SCOPE = SPFILE;
```