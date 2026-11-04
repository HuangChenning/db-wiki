---
title: OPTIMIZER_USE_INVISIBLE_INDEXES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams173.htm
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
| Basic | No |

`OPTIMIZER_USE_INVISIBLE_INDEXES` enables or disables the use of invisible indexes.

Values:

- `true`
	Invisible indexes are treated as visible (normal) indexes.
- `false`
	Invisible indexes will not be considered by the optimizer but will still be maintained by DML operations.