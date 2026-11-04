---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DST_UPGRADE_INSERT_CONV.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.118 DST\_UPGRADE\_INSERT\_CONV

`DST_UPGRADE_INSERT_CONV` specifies whether internal operators will be allocated on top of `TIMESTAMP WITH TIME ZONE` (TSTZ) columns of tables which have not been upgraded during the upgrade window of daylight saving time patching for `TIMESTAMP WITH TIME ZONE` data.

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `true` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Range of values | `true \| false` |
| Basic | No |

Values

- `true`
	Internal operators will be allocated on top of TSTZ columns of tables which have not been upgraded. This is the default.
- `false`
	Internal operators will not be allocated on top of TSTZ columns of tables which have not been upgraded.

When DST\_UPGRADE\_INSERT\_CONV is set to true during the upgrade window of the daylight saving time patching process:

- `SELECT` queries on tables with TSTZ data which have not been upgraded will use internal operators on top of TSTZ columns to present TSTZ data as if they were recorded using the new time zone translation rules.
- DML on tables with TSTZ data which have not been upgraded will use internal operators on top of TSTZ columns to ensure that the TSTZ data is recorded using the old time zone translation rules in order to be consistent with the existing TSTZ data in the same tables.

Note:

Oracle strongly recommends that this parameter is set to `true` throughout the upgrade window of the daylight saving time patching process. This parameter reduces the performance impact since indexes on TSTZ columns will be disabled whenever internal operators are allocated. If the parameter is set to `false`, then indexes will be used and this may affect performance of queries against TSTZ data during the DST upgrade window. Turning off this parameter during the upgrade window may corrupt data on disk when DMLs occur for tables with TSTZ data which have not yet been upgraded.

See Also:

[Oracle Database Globalization Support Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=NLSPG759) for more information about this parameter