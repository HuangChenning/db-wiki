---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/IDENTITY_PROVIDER_CONFIG.html
tags:
  - oracle
  - 19c
  - reference
---

## 1.143 IDENTITY\_PROVIDER\_CONFIG

Use `IDENTITY_PROVIDER_CONFIG` to configure the database to use Microsoft Azure Active Directory (Azure AD) as an external identity provider.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | ``` IDENTITY_PROVIDER_CONFIG = '{ "application_id_uri" : "string",    "tenant_id" : "string",    "app_id" : "string" }' ```  Where:  - The `application_id_uri` value is obtained from the registered application, to be mapped in the JWT "aud" (audience) claim. It must be domain qualified and start with "https://" to specify the OCI database to access. - The `tenant_id` value is obtained from the tenant configuration and is also available on the database application registration overview page. - The `app_id` value is obtained from the registered resource application and is also available on the database application registration overview page. |
| Default value | None |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Basic | No |
| Oracle RAC | The same value must be used on all instances. |

This parameter is effective only when the database is enabled to use Azure AD as an external identity provider, that is, when the `IDENTITY_PROVIDER_TYPE` initialization parameter is set to `AZURE_AD`. You must use this parameter to specify Azure AD configuration settings.

Example:

```
ALTER SYSTEM SET IDENTITY_PROVIDER_CONFIG =
  '{ "application_id_uri" : "https://example.com/pdb1",
     "tenant_id" : "111a1111-a11a-111a-111111111111a",
     "app_id" : "11aa1a1-aaaa-1111-1111-1111aa111111" }'
   SCOPE=BOTH;
```

Note:

Setting the value of this parameter is only one step in a series of steps for configuring the database to use Azure AD. Refer to [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/refrn&id=DBSEG-GUID-2712902B-DD07-4A61-B336-31C504781D0F) for the complete steps before you set this parameter.

Note:

This parameter is available starting with Oracle Database 19c, Release Update 19.16.

Note:

This parameter is not available to update directly for Oracle Autonomous Database Serverless.

See Also:

" [IDENTITY\_PROVIDER\_TYPE](IDENTITY_PROVIDER_TYPE.md) "