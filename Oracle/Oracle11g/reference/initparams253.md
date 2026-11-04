---
title: STAR_TRANSFORMATION_ENABLED
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams253.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `STAR_TRANSFORMATION_ENABLED = { FALSE \| TRUE \| TEMP_DISABLE }` |
| Default value | `FALSE` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Basic | Yes |

`STAR_TRANSFORMATION_ENABLED` determines whether a cost-based query transformation will be applied to star queries.

Values:

- `FALSE`
	The transformation will not be applied.
- `TRUE`
	The optimizer will consider performing a cost-based query transformation on the star query.
- `TEMP_DISABLE`
	The optimizer will consider performing a cost-based query transformation on the star query but will not use temporary tables in the star transformation.

See Also:

- [Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/toc.htm) for information on star queries
- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/toc.htm) for information on enabling star query