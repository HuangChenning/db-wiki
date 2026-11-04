---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALLOW_GROUP_ACCESS_TO_SGA.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.11 ALLOW\_GROUP\_ACCESS\_TO\_SGA

`ALLOW_GROUP_ACCESS_TO_SGA` controls `group` access to shared memory on UNIX platforms.

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `false` |
| Modifiable | No |
| Modifiable in a PDB | No |
| Range of values | `true \| false` |
| Basic | No |
| Oracle RAC | The same value must be used on all instances. |

The default value is `false`, which means that database shared memory is created with `owner` access only. In Oracle Database releases prior to Oracle Database 12c Release 2 (12.2.0.1), database shared memory was created with `owner` and `group` access.

When this parameter is set to `true`, database shared memory is created with `owner` and `group` access. This behavior grants permissions to DBAs to manage shared memory outside the database, but also allows DBAs to read and write to shared memory, which may not be desirable for certain installations.