---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/REMOTE_OS_ROLES.html
tags:
  - oracle
  - 12c
  - reference
---

`REMOTE_OS_ROLES` specifies whether operating system roles are allowed for remote clients.

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `false` |
| Modifiable | No |
| Modifiable in a PDB | No |
| Range of values | `true \| false` |
| Basic | No |

The default value, `false`, causes Oracle to identify and manage roles for remote clients.

See Also:

- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=DBSEG99899) for more information on setting this parameter
- " [OS\_ROLES](OS_ROLES.md) "