---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DNFS_BATCH_SIZE.html
tags:
  - oracle
  - 12c
  - reference
---

`DNFS_BATCH_SIZE` controls the number of asynchronous I/O's that can be queued by an Oracle process when Direct NFS Client is enabled.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `4096` |
| Modifiable | No |
| Modifiable in a PDB | No |
| Range of values | 0 - 4096 |
| Basic | No |

In environments where the NFS server cannot handle a large number of outstanding asynchronous I/O requests, use this parameter to limit the number of I/O's issued by an Oracle foreground process. The recommended setting for this parameter is to start at 128 and increase or decrease it based on NFS server performance.

See Also:

[Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=TGDBA95342) for additional information about the `DNFS_BATCH_SIZE` initialization parameter