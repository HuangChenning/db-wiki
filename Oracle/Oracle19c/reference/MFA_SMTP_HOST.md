---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/MFA_SMTP_HOST.html
tags:
  - oracle
  - 19c
  - reference
---

## 1.215 MFA\_SMTP\_HOST

`MFA_SMTP_HOST` specifies the SMTP host for emails sent to users when configuring multi-factor authentication using Oracle Mobile Authenticator (OMA) or Cisco Duo push notifications.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `MFA_SMTP_HOST =` `string` |
| Default value | None |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Basic | No |
| Oracle RAC | Multiple instances can have different values. |

This parameter is configured at the PDB level. When adding OMA or Duo as an additional authentication method for a user in a PDB, the user is sent an email with instructions on how to register a device. This parameter specifies the SMTP host name for those emails.

Set this parameter to a valid SMTP host name. For example:

```
ALTER SYSTEM SET MFA_SMTP_HOST =
   "smtp.email.us-sanjose-1.oci.oraclecloud.com";
```

Note:

This parameter is available starting with Oracle Database 19c, Release Update 19.28.

See Also:

[Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/refrn&id=DBSEG-GUID-10E4F568-0FA3-4F82-99AA-14FB2947469C) for more information about this parameter