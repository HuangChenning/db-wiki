---
title: DB_SECUREFILE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams068.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `DB_SECUREFILE = { NEVER \| PERMITTED \| ALWAYS \| IGNORE }` |
| Default value | `PERMITTED` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Basic | No |

`DB_SECUREFILE` specifies whether or not to treat LOB files as SecureFiles.

Values:

- `NEVER`
	Any LOBs that are specified as SecureFiles are created as BasicFile LOBs. All SecureFile-specific storage options and features (for example, compress, encrypt, deduplicate) will cause an exception. The BasicFile LOB defaults will be used for storage options not specified.
- `PERMITTED`
	LOBs are allowed to be created as SecureFiles.
- `ALWAYS`
	Attempts to create all LOBs as SecureFile LOBs but creates any LOBs not in an Automatic Segment Space Managed tablespace as BasicFile LOBs, unless `SECUREFILE` is explicitly specified. Any BasicFile LOB storage options that are specified will be ignored and the SecureFile defaults will be used for all storage options not specified.
- `IGNORE`
	The `SECUREFILE` keyword and all SecureFile options are ignored.

If the `COMPATIBLE` initialization parameter is not set to `11.1.0` or higher, then LOBs are not treated as SecureFiles.

If there is a LOB column with two partitions (one that has a tablespace for which ASSM is enabled and one that has a tablespace for which ASSM is not enabled), then LOBs in the partition with the ASSM-enabled tablespace will be treated as SecureFiles and LOBs in the other partition will be treated as BasicFile LOBs.