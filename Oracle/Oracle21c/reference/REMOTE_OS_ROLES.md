---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/REMOTE_OS_ROLES.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.306 REMOTE\_OS\_ROLES

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

- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DBSEG99899) for more information on setting this parameter
- " [OS\_ROLES](OS_ROLES.md) "