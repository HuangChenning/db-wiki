---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/STAR_TRANSFORMATION_ENABLED.html
tags:
  - oracle
  - 12c
  - reference
---

`STAR_TRANSFORMATION_ENABLED` determines whether a cost-based query transformation will be applied to star queries.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `STAR_TRANSFORMATION_ENABLED = { FALSE \| TRUE \| TEMP_DISABLE }` |
| Default value | `FALSE` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Basic | Yes |

Values

- `FALSE`
	The transformation will not be applied.
- `TRUE`
	The optimizer will consider performing a cost-based query transformation on the star query.
- `TEMP_DISABLE`
	The optimizer will consider performing a cost-based query transformation on the star query but will not use temporary tables in the star transformation.

See Also:

- [Oracle Database SQL Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=TGSQL252) for information on enabling star queries