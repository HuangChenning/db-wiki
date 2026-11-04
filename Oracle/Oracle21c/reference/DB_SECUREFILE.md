---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DB_SECUREFILE.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.95 DB\_SECUREFILE

`DB_SECUREFILE` specifies whether to treat LOB files as SecureFiles.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `DB_SECUREFILE = { NEVER \| PERMITTED \| PREFERRED \| ALWAYS \| IGNORE }` |
| Default value | `PERMITTED if the COMPATIBLE initialization parameter is set to 11.2.0.1, 11.2.0.2, or 11.2.0.3, or PREFERRED if the COMPATIBLE initialization parameter is set to 12.0.0.0 or higher` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Basic | No |

Values

- `NEVER`
	Any LOBs that are specified as SecureFiles are created as BasicFiles LOBs. All SecureFiles-specific storage options and features (for example, compress, encrypt, deduplicate) will cause an exception. The BasicFiles LOB defaults will be used for storage options not specified.
- `PERMITTED`
	LOBs are allowed to be created as SecureFiles.
- `PREFERRED`
	All LOBs are created as SecureFiles unless `BASICFILE` is explicitly specified in the LOB storage clause or the tablespace is a Manual Segment Space Management tablespace. When `PREFERRED` is set, cases where `BASICFILE` would otherwise be inherited from the partition or column level LOB storage are ignored; the LOBs will be created as SecureFiles instead.
- `ALWAYS`
	Attempts to create all LOBs as SecureFiles LOBs but creates any LOBs not in an Automatic Segment Space Managed (ASSM) tablespace as BasicFiles LOBs, unless `SECUREFILE` is explicitly specified. Any BasicFiles LOB storage options that are specified will be ignored and the SecureFiles LOB defaults will be used for all storage options not specified.
- `IGNORE`
	The `SECUREFILE` keyword and all SecureFiles options are ignored.

If the `COMPATIBLE` initialization parameter is not set to `11.1.0` or higher, then LOBs are not treated as SecureFiles.

If there is a LOB column with two partitions (one that has a tablespace for which ASSM is enabled and one that has a tablespace for which ASSM is not enabled), then LOBs in the partition with the ASSM-enabled tablespace will be treated as SecureFiles and LOBs in the other partition will be treated as BasicFiles.

If an application is not certified with SecureFiles, the value of the `DB_SECUREFILE` initialization parameter can be set to `PERMITTED` to get the default behavior of Oracle Database 11g.

See Also:

[Oracle Database SecureFiles and Large Objects Developer's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADLOB-GUID-AD240DE1-392F-41EC-864D-2D892CF7D45A) for an example of setting this parameter using the `ALTER SYSTEM` statement