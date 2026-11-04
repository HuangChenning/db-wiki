---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/lob_signature_enable.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.179 LOB\_SIGNATURE\_ENABLE

`LOB_SIGNATURE_ENABLE` is used to enable or disable the LOB locator signature feature.

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `false` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Range of values | `true \| false` |
| Basic | No |
| Oracle RAC | Multiple instances must have the same value. |

You can secure your LOBs by enabling the LOB locator signature feature. A LOB locator is a pointer to the location of a large object (LOB) value. If the `LOB_SIGNATURE_ENABLED` initialization parameter is set to `true`, then when you create a LOB, Oracle Database automatically assigns a signature to the LOB locator. When Oracle Database receives a request from a client, it uses the signature to determine if any tampering with the LOB locator has occurred.

When this parameter is set to `true`, you also have the option of further securing your LOBs by encrypting your LOB locator signature keys.

See Also:

[Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DBSEG-GUID-8F585EBE-611D-4717-AD9F-CAC10A19B7E1) for more information on LOB locator signatures and encrypting LOB locator signature keys