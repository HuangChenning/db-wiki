---
title: CREATE_STORED_OUTLINES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams042.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `CREATE_STORED_OUTLINES = { true \| false \|` `category_name` `}` \[`NOOVERRIDE`\] |
| Default value | There is no default value. |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Basic | No |

`CREATE_STORED_OUTLINES` determines whether Oracle automatically creates and stores an outline for each query submitted during the session.

Values:

- `true`
	Enables automatic outline creation for subsequent queries in the same session. These outlines receive a unique system-generated name and are stored in the `DEFAULT` category. If a particular query already has an outline defined for it in the `DEFAULT` category, then that outline will remain and a new outline will not be created.
- `false`
	Disables automatic outline creation during the session. This is the default.
- `category_name`
	Enables the same behavior as `true` except that any outline created during the session is stored in the `category_name` category.
- `NOOVERRIDE`
	`NOOVERRIDE` specifies that this system setting will not override the setting for any session in which this parameter was explicitly set. If you do not specify `NOOVERRIDE`, then this setting takes effect in all sessions.

See Also:

[Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/toc.htm) for more information on setting this parameter