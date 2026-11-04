---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/PKCS11_LIBRARY_LOCATION.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.283 PKCS11\_LIBRARY\_LOCATION

`PKCS11_LIBRARY_LOCATION` specifies the PKCS#11 library location for Transparent Data Encryption (TDE).

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `PKCS11_LIBRARY_LOCATION = 'library_location'` |
| Default value | None |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Basic | No |
| Oracle RAC | The same value must be used on all instances. |

For `library_location`, specify the full operating system path to the PKCS#11 library. For example:

```
ALTER SYSTEM SET PKCS11_LIBRARY_LOCATION =
    '/opt/oracle/extapi/64/pkcs11/okv/21.8/liborapkcs.so';
```

Note:

This parameter is available starting with Oracle Database 21c.

See Also:

" [V$PKCS11\_PATH](V-PKCS11_PATH.md) "