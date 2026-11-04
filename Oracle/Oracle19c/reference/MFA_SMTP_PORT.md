---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/MFA_SMTP_PORT.html
tags:
  - oracle
  - 19c
  - reference
---

## 1.216 MFA\_SMTP\_PORT

`MFA_SMTP_PORT` specifies the SMTP port for emails sent to users when configuring multi-factor authentication using Oracle Mobile Authenticator (OMA) or Cicco Duo push notifications.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | 587 |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Range of values | 25 to 587 |
| Basic | No |
| Oracle RAC | Multiple instances can have different values. |

This parameter is configured at the PDB level. When adding OMA or Duo as an additional authentication method for a user in a PDB, the user is sent an email with instructions on how to register a device. This parameter specifies the SMTP port for those emails.

Set this parameter to to a valid SMTP port. For example:

```
ALTER SYSTEM SET MFA_SMTP_PORT = 587;
```

Note:

This parameter is available starting with Oracle Database 19c, Release Update 19.28.

See Also:

[Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/refrn&id=DBSEG-GUID-10E4F568-0FA3-4F82-99AA-14FB2947469C) for more information about this parameter