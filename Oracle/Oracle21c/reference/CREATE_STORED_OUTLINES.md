---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/CREATE_STORED_OUTLINES.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.61 CREATE\_STORED\_OUTLINES

`CREATE_STORED_OUTLINES` determines whether Oracle automatically creates and stores an outline for each query submitted during the session.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `CREATE_STORED_OUTLINES = { true \| false \| ` `category_name` ` }` \[`NOOVERRIDE`\] |
| Default value | There is no default value. |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Basic | No |

Values

- `true`
	Enables automatic outline creation for subsequent queries in the same session. These outlines receive a unique system-generated name and are stored in the `DEFAULT` category. If a particular query already has an outline defined for it in the `DEFAULT` category, then that outline will remain and a new outline will not be created.
- `false`
	Disables automatic outline creation during the session. This is the default.
- `category_name`
	Enables the same behavior as `true` except that any outline created during the session is stored in the `category_name` category.
- `NOOVERRIDE`
	`NOOVERRIDE` specifies that this system setting will not override the setting for any session in which this parameter was explicitly set. If you do not specify `NOOVERRIDE`, then this setting takes effect in all sessions.

See Also:

[Oracle Database SQL Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=TGSQL680) for more information on setting this parameter