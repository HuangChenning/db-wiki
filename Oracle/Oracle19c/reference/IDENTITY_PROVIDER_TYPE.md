---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/IDENTITY_PROVIDER_TYPE.html
tags:
  - oracle
  - 19c
  - reference
---

## 1.144 IDENTITY\_PROVIDER\_TYPE

`IDENTITY_PROVIDER_TYPE` specifies an external identity provider for the database.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `IDENTITY_PROVIDER_TYPE = { AZURE_AD \| OCI_IAM \| NONE }` |
| Default value | `NONE` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Basic | No |
| Oracle RAC | The same value must be used on all instances. |

Values:

- `AZURE_AD` - Enables the database to use Microsoft Azure Active Directory (Azure AD) as an external identity provider.
	When you specify this value, you must also specify configuration settings for Azure AD by setting the `IDENTITY_PROVIDER_CONFIG` initialization parameter.
- `OCI_IAM` - Enables the database to use Oracle Cloud Infrastructure Identity and Access Management (OCI IAM) as an external identity provider.
	When you specify this value, there is no need to specify configuration settings with the `IDENTITY_PROVIDER_CONFIG` initialization parameter.
- `NONE` - The database will not use Azure AD or OCI IAM as an external identity provider.

Note:

Setting the value of this parameter is only one step in a series of steps for configuring an external identity provider for the database. Refer to Oracle Database Security Guide for the complete set of steps for configuring [Azure AD](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/refrn&id=DBSEG-GUID-2712902B-DD07-4A61-B336-31C504781D0F) or [OCI IAM](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/refrn&id=DBSEG-GUID-466A8800-5AF1-4202-BAFF-5AE727D242E8) before you set this parameter value.

Note:

This parameter is available starting with Oracle Database 19c, Release Update 19.16.

Note:

This parameter is not available to update directly for Oracle Autonomous Database Serverless.

See Also:

" [IDENTITY\_PROVIDER\_CONFIG](IDENTITY_PROVIDER_CONFIG.md) "