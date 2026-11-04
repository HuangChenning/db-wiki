---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/OS_ROLES.html
tags:
  - oracle
  - 12c
  - reference
---

`OS_ROLES` determines whether Oracle or the operating system identifies and manages the roles of each username.

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `false` |
| Modifiable | No |
| Modifiable in a PDB | No |
| Range of values | `true \| false` |
| Basic | No |

Values

- `TRUE`
	The operating system completely manages the role grants for all database usernames. When a user attempts to create a session, the username's security domain is initialized using the roles identified by the operating system.
	Revocation by Oracle of roles granted by the operating system is ignored, as are any roles previously granted by Oracle.
- `FALSE`
	Oracle identifies and manages the roles.

See Also:

- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=ADMIN11240) and [Oracle Database Enterprise User Security Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=DBIMI240) for more information on roles and on setting this parameter
- " [REMOTE\_OS\_ROLES](REMOTE_OS_ROLES.md) "