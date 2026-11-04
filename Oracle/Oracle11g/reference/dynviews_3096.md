---
title: "V$SYSTEM_FIX_CONTROL"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3096.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$SYSTEM_FIX_CONTROL` displays information about Fix Control (enabled/disabled) at the system level.

| Column | Datatype | Description |
| --- | --- | --- |
| `BUGNO` | `NUMBER` | Bug number (as fix control identifier) |
| `VALUE` | `NUMBER` | Current value set for the fix control |
| `SQL_FEATURE` | `VARCHAR2(64)` | Feature control ID |
| `DESCRIPTION` | `VARCHAR2(64)` | Description of the fix control |
| `OPTIMIZER_FEATURE_ENABLE` | `VARCHAR2(25)` | Version on (and after) which the fix is enabled by default |
| `EVENT` | `NUMBER` | Event formerly used to control this fix |
| `IS_DEFAULT` | `NUMBER` | Indicates whether the current value is the same as the default (`1`) or not (`0`) |