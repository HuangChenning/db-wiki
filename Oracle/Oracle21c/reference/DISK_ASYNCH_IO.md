---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DISK_ASYNCH_IO.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.111 DISK\_ASYNCH\_IO

`DISK_ASYNCH_IO` controls whether I/O to datafiles, control files, and logfiles is asynchronous (that is, whether parallel server processes can overlap I/O requests with CPU processing during table scans).

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `true` |
| Modifiable | No |
| Modifiable in a PDB | No |
| Range of values | `true \| false` |
| Basic | No |

If your platform supports asynchronous I/O to disk, Oracle recommends that you leave this parameter set to its default value. However, if the asynchronous I/O implementation is not stable, you can set this parameter to `false` to disable asynchronous I/O. If your platform does not support asynchronous I/O to disk, this parameter has no effect.

If you set `DISK_ASYNCH_IO` to `false`, then you can increase `DB_WRITER_PROCESSES` or use `DBWR_IO_SLAVES` to simulate asynchronous I/O.

See Also:

- " [DB\_WRITER\_PROCESSES](DB_WRITER_PROCESSES.md) "
- " [DBWR\_IO\_SLAVES](DBWR_IO_SLAVES.md) "
- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=TGDBA-GUID-01C9C892-4C0B-4524-82B3-146D1C191BDD) for more information