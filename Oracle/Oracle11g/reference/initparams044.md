---
title: CURSOR_SHARING
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams044.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `CURSOR_SHARING = { EXACT \| FORCE }` |
| Default value | `EXACT` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Basic | No |

`CURSOR_SHARING` determines what kind of SQL statements can share the same cursors.

Values:

- `FORCE`
	Allows the creation of a new cursor if sharing an existing cursor, or if the cursor plan is not optimal.
- `EXACT`
	Only allows statements with identical text to share the same cursor.

See Also:

[Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/memory.htm#PFGRF94345) before setting the `CURSOR_SHARING` parameter to learn about the performance implications