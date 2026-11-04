---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/CONTROL_MANAGEMENT_PACK_ACCESS.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.56 CONTROL\_MANAGEMENT\_PACK\_ACCESS

`CONTROL_MANAGEMENT_PACK_ACCESS` specifies which of the Server Manageability Packs should be active.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `CONTROL_MANAGEMENT_PACK_ACCESS = { NONE \| DIAGNOSTIC \| DIAGNOSTIC+TUNING }` |
| Default value | Enterprise Edition: `DIAGNOSTIC+TUNING`  All other editions: `NONE` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Basic | No |

The following packs are available:

- The `DIAGNOSTIC` pack includes AWR, ADDM, and so on.
- The `TUNING` pack includes SQL Tuning Advisor, SQLAccess Advisor, and so on.
	A license for `DIAGNOSTIC` is required for enabling the `TUNING` pack.

Values

- `NONE`
	Both packs are not available.
- `DIAGNOSTIC`
	Only the `DIAGNOSTIC` pack is available.
- `DIAGNOSTIC+TUNING`
	Both packs are available. This is the default.

See Also:

[Oracle Database Licensing Information User Manual](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DBLIC159)