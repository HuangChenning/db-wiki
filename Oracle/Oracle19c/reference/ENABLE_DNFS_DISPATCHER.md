---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/ENABLE_DNFS_DISPATCHER.html
tags:
  - oracle
  - 19c
  - reference
---

## 1.118 ENABLE\_DNFS\_DISPATCHER

`ENABLE_DNFS_DISPATCHER` enables dispatcher support for the Oracle Direct NFS client.

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `false` |
| Modifiable | No |
| Modifiable in a PDB | No |
| Range of values | `true \| false` |
| Basic | No |
| Oracle RAC | All instances should use the same value. |

When this parameter is set to `true` in the initialization parameter file, dispatcher processes will be spawned for the Oracle Direct NFS client.

The number of dispatcher processes spawned is calculated as one-eighth of the value of the `CPU_COUNT` parameter.

See Also:

" [CPU\_COUNT](CPU_COUNT.md) "