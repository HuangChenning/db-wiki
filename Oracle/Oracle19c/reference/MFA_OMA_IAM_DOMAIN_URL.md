---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/MFA_OMA_IAM_DOMAIN_URL.html
tags:
  - oracle
  - 19c
  - reference
---

## 1.212 MFA\_OMA\_IAM\_DOMAIN\_URL

`MFA_OMA_IAM_DOMAIN_URL` specifies the OCI IAM domain URL for multi-factor authentication using Oracle Mobile Authenticator (OMA) push notifications.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `MFA_OMA_IAM_DOMAIN_URL =` `string` |
| Default value | None |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Basic | No |
| Oracle RAC | Multiple instances can have different values. |

This parameter is configured at the PDB level. Setting this parameter allows users in a PDB to be registered for multi-factor authentication using OMA push notifications.

Set this parameter to a valid OCI IAM domain URL. For example:

```
ALTER SYSTEM SET MFA_OMA_IAM_DOMAIN_URL =
   "https://idcs-cbcb9aaca84945e78466ab5b2e576360.identity.oraclecloud.com";
```

Note:

This parameter is available starting with Oracle Database 19c, Release Update 19.28.

See Also:

[Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/refrn&id=DBSEG-GUID-10E4F568-0FA3-4F82-99AA-14FB2947469C) for more information about this parameter