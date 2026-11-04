---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/CURSOR_SHARING.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.64 CURSOR\_SHARING

`CURSOR_SHARING` determines what kind of SQL statements can share the same cursors.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `CURSOR_SHARING = { EXACT \| FORCE }` |
| Default value | `EXACT` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Basic | No |

Values

- `FORCE`
	Allows the creation of a new cursor if sharing an existing cursor, or if the cursor plan is not optimal.
- `EXACT`
	Only allows statements with identical text to share the same cursor.

See Also:

[Oracle Database SQL Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=TGSQL848) before setting the `CURSOR_SHARING` parameter to learn about the performance implications