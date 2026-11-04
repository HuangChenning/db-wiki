---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/TDE_KEY_CACHE.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.360 TDE\_KEY\_CACHE

Use `TDE_KEY_CACHE` to enable or disable sharing of Transparent Data Encryption (TDE) master encryption keys across Oracle processes.

Note:

This parameter is available only for databases in Oracle Cloud Infrastructure (OCI) that use the OCI Key Management Service (KMS) for TDE key management.

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `false` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Range of values | `true \| false` |
| Basic | No |
| Oracle RAC | The same value must be used on all instances. |

Values:

- `true`
	Enables sharing of TDE master encryption keys across Oracle processes
- `false`
	Disables sharing of TDE master encryption keys across Oracle processes

Note:

This parameter is available starting with Oracle Database 21c.

See Also:

- [Oracle Database Advanced Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ASOAG-GUID-4C0941AC-C684-43D0-B3E7-25D168C98FFB) for more information about setting the TDE master encryption key in a hardware keystore in united mode
- [Oracle Database Advanced Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ASOAG-GUID-749AECD4-9DBB-4D1E-A526-B3AC5659A653) for more information about setting the TDE master encryption key in a hardware keystore in isolated mode