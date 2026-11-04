---
title: CONTROL_MANAGEMENT_PACK_ACCESS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams038.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `CONTROL_MANAGEMENT_PACK_ACCESS = { NONE \| DIAGNOSTIC \| DIAGNOSTIC+TUNING }` |
| Default value | Enterprise Edition: `DIAGNOSTIC+TUNING`  All other editions: `NONE` |
| Modifiable | `ALTER SYSTEM` |
| Basic | No |

`CONTROL_MANAGEMENT_PACK_ACCESS` specifies which of the Server Manageability Packs should be active. The following packs are available:

- The `DIAGNOSTIC` pack includes AWR, ADDM, and so on.
- The `TUNING` pack includes SQL Tuning Advisor, SQLAccess Advisor, and so on.
	A license for `DIAGNOSTIC` is required for enabling the `TUNING` pack.

Values:

- `NONE`
	Both packs are not available.
- `DIAGNOSTIC`
	Only the `DIAGNOSTIC` pack is available.
- `DIAGNOSTIC+TUNING`
	Both packs are available. This is the default.

See Also:

[Oracle Database Licensing Information](https://docs.oracle.com/cd/E11882_01/license.112/e47877/toc.htm)