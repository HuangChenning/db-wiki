---
title: CURSOR_BIND_CAPTURE_DESTINATION
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams043.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `CURSOR_BIND_CAPTURE_DESTINATION = { off \| memory \| memory+disk }` |
| Default value | `memory+disk` |
| Modifiable | `ALTER` `SESSION`, `ALTER` `SYSTEM` |
| Basic | No |

`CURSOR_BIND_CAPTURE_DESTINATION` determines the location at which bind variables that are captured from SQL cursors are available.

Values:

- `off`
	Bind variables are not captured from SQL cursors.
- `memory`
	Bind variables are captured from SQL cursors, and are available only in memory (`V$` views).
- `memory+disk`
	Bind variables are captured from SQL cursors, and are available in memory (`V$` views) and disk (Automatic Workload Repository tables, SQL Tuning Set tables, and so on).
	Note:
	This initialization parameter is available starting with Oracle Database 11g Release 2 (11.2.0.2).