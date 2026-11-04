---
title: DBWR_IO_SLAVES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams073.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `0` |
| Modifiable | No |
| Range of values | 0 to operating system-dependent |
| Basic | No |

`DBWR_IO_SLAVES` is relevant only on systems with only one database writer process (`DBW0`). It specifies the number of I/O server processes used by the `DBW0` process. The `DBW0` process and its server processes always write to disk. By default, the value is `0` and I/O server processes are not used.

If you set `DBWR_IO_SLAVES` to a nonzero value, the number of I/O server processes used by the `ARCH` and `LGWR` processes is set to `4`. However, the number of I/O server processes used by Recovery Manager is set to `4` only if asynchronous I/O is disabled (either your platform does not support asynchronous I/O or `disk_asynch_io` is set to `false`).

Typically, I/O server processes are used to simulate asynchronous I/O on platforms that do not support asynchronous I/O or that implement it inefficiently. However, you can use I/O server processes even when asynchronous I/O is being used. In that case the I/O server processes will use asynchronous I/O.

I/O server processes are also useful in database environments with very large I/O throughput, even if asynchronous I/O is enabled.

See Also:

["BACKUP\_TAPE\_IO\_SLAVES"](initparams021.md)