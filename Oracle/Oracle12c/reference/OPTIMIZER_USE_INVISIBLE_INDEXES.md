---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/OPTIMIZER_USE_INVISIBLE_INDEXES.html
tags:
  - oracle
  - 12c
  - reference
---

`OPTIMIZER_USE_INVISIBLE_INDEXES` enables or disables the use of invisible indexes.

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `false` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Range of values | `true \| false` |
| Basic | No |

Values

- `true`
	Invisible indexes are treated as visible (normal) indexes.
- `false`
	Invisible indexes will not be considered by the optimizer but will still be maintained by DML operations.