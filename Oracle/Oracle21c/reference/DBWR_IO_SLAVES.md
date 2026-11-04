---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBWR_IO_SLAVES.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.103 DBWR\_IO\_SLAVES

`DBWR_IO_SLAVES` specifies the number of I/O server processes used by the `DBW0` process.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `0` |
| Modifiable | No |
| Modifiable in a PDB | No |
| Range of values | 0 to operating system-dependent |
| Basic | No |

`DBWR_IO_SLAVES` is relevant only on systems with only one database writer process (`DBW0`). The `DBW0` process and its server processes always write to disk. By default, the value is `0` and I/O server processes are not used.

If you set `DBWR_IO_SLAVES` to a nonzero value, the number of I/O server processes used by the `ARCH` and `LGWR` processes is set to `4`. However, the number of I/O server processes used by Recovery Manager is set to `4` only if asynchronous I/O is disabled (either your platform does not support asynchronous I/O or `disk_asynch_io` is set to `false`).

Typically, I/O server processes are used to simulate asynchronous I/O on platforms that do not support asynchronous I/O or that implement it inefficiently. However, you can use I/O server processes even when asynchronous I/O is being used. In that case the I/O server processes will use asynchronous I/O.

I/O server processes are also useful in database environments with very large I/O throughput, even if asynchronous I/O is enabled.

See Also:

- " [BACKUP\_TAPE\_IO\_SLAVES](BACKUP_TAPE_IO_SLAVES.md) "
- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=TGDBA-GUID-01C9C892-4C0B-4524-82B3-146D1C191BDD) for more information about this parameter