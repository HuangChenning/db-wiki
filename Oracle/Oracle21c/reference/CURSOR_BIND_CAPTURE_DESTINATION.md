---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/CURSOR_BIND_CAPTURE_DESTINATION.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.62 CURSOR\_BIND\_CAPTURE\_DESTINATION

`CURSOR_BIND_CAPTURE_DESTINATION` determines the location at which bind variables that are captured from SQL cursors are available.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `CURSOR_BIND_CAPTURE_DESTINATION = { off \| memory \| memory+disk }` |
| Default value | `memory+disk` |
| Modifiable | `ALTER` `SESSION`, `ALTER` `SYSTEM` |
| Modifiable in a PDB | Yes |
| Basic | No |

Values

- `off`
	Bind variables are not captured from SQL cursors.
- `memory`
	Bind variables are captured from SQL cursors, and are available only in memory (`V$` views).
- `memory+disk`
	Bind variables are captured from SQL cursors, and are available in memory (`V$` views) and disk (Automatic Workload Repository tables, SQL Tuning Set tables, and so on).
	When you specify this value with a SQL `ALTER SESSION` or `ALTER SYSTEM` statement, enclose the value in single quotes or double quotes. For example:
	```
	ALTER SESSION SET CURSOR_BIND_CAPTURE_DESTINATION = 'memory+disk';
	ALTER SYSTEM SET CURSOR_BIND_CAPTURE_DESTINATION = "memory+disk";
	```