---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/FIXED_DATE.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.137 FIXED\_DATE

`FIXED_DATE` enables you to set a constant date that `SYSDATE` will always return instead of the current date.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `FIXED_DATE =` \[ `YYYY-MM-DD-HH24:MI:SS` (or the default Oracle date format) `\| NONE` \] |
| Default value | There is no default value. |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Basic | No |

To undo a fixed date setting, specify `FIXED_DATE=NONE`. This parameter is useful primarily for testing. The value can be in the format shown above or in the default Oracle date format, without a time.