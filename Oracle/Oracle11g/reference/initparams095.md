---
title: FIXED_DATE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams095.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `FIXED_DATE = [YYYY-MM-DD-HH24:MI:SS` (or the default Oracle date format) `\| NONE`\] |
| Default value | There is no default value. |
| Modifiable | `ALTER SYSTEM` |
| Basic | No |

`FIXED_DATE` enables you to set a constant date that `SYSDATE` will always return instead of the current date. To undo a fixed date setting, specify `FIXED_DATE=NONE`. This parameter is useful primarily for testing. The value can be in the format shown above or in the default Oracle date format, without a time.