---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/STAR_TRANSFORMATION_ENABLED.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.354 STAR\_TRANSFORMATION\_ENABLED

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

- [Oracle Database SQL Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=TGSQL252) for information on enabling star queries