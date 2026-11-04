---
title: OS_ROLES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams177.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `false` |
| Modifiable | No |
| Range of values | `true \| false` |

`OS_ROLES` determines whether Oracle or the operating system identifies and manages the roles of each username.

Values:

- `TRUE`
	The operating system completely manages the role grants for all database usernames. When a user attempts to create a session, the username's security domain is initialized using the roles identified by the operating system. A user can subsequently enable as many roles identified by the operating system as specified by the parameter `MAX_ENABLED_ROLES`.
	Revocation by Oracle of roles granted by the operating system is ignored, as are any roles previously granted by Oracle.
- `FALSE`
	Oracle identifies and manages the roles.

See Also:

- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm) and [Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/toc.htm) for more information on roles and on setting this parameter
- ["REMOTE\_OS\_ROLES"](initparams214.md)