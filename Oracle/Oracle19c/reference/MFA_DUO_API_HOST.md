---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/MFA_DUO_API_HOST.html
tags:
  - oracle
  - 19c
  - reference
---

## 1.211 MFA\_DUO\_API\_HOST

`MFA_DUO_API_HOST` specifies the host name of the Cisco Duo security API to be used for multi-factor authentication using Cisco Duo push notifications.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `MFA_DUO_API_HOST =` `string` |
| Default value | None |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Basic | No |
| Oracle RAC | Multiple instances can have different values. |

This parameter is configured at the PDB level. Setting this parameter allows users in a PDB to be registered for multi-factor authentication using Cisco Duo push notifications.

Set this parameter to a valid Duo API host. For example:

```
ALTER SYSTEM SET MFA_DUO_API_HOST = "api-855fd6a0.duosecurity.com";
```

Note:

This parameter is available starting with Oracle Database 19c, Release Update 19.28.

See Also:

[Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/refrn&id=DBSEG-GUID-10E4F568-0FA3-4F82-99AA-14FB2947469C) for more information about this parameter