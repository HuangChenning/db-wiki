---
title: DNFS_BATCH_SIZE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams083.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | 4096 |
| Modifiable | No |
| Range of values | 0 - 4096 |
| Basic | No |

`DNFS_BATCH_SIZE` controls the number of asynchronous I/O's that can be queued by an Oracle process when Direct NFS Client is enabled. In environments where the NFS server cannot handle a large number of outstanding asynchronous I/O requests, use this parameter to limit the number of I/O's issued by an Oracle foreground process. The recommended setting for this parameter is to start at 128 and increase or decrease it based on NFS server performance.

Note:

The `DNFS_BATCH_SIZE` initialization parameter is available starting with Oracle Database 11g Release 2 (11.2.0.4).

See Also:

[Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/os.htm#PFGRF94412) for additional information about the `DNFS_BATCH_SIZE` initialization parameter