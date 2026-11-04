---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DATA_GUARD_SYNC_LATENCY.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.68 DATA\_GUARD\_SYNC\_LATENCY

`DATA_GUARD_SYNC_LATENCY` controls how many seconds the Log Writer (LGWR) process waits beyond the response of the first in a series of Oracle Data Guard SYNC redo transport mode connections.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `0` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Range of values | `0` to the number of seconds specified by the `NET_TIMEOUT` attribute for the `LOG_ARCHIVE_DEST_n` parameter |
| Basic | No |
| Oracle RAC | The same value must be used on all instances. |

The default value is `0`, which means that the LGWR will wait up to the number of seconds specified by the `NET_TIMEOUT` attribute of the `LOG_ARCHIVE_DEST_n` parameter for each SYNC standby destination.

For example, in an Oracle Data Guard configuration that has two standbys which receive redo in SYNC mode, you would define `LOG_ARCHIVE_DEST_2` and `LOG_ARCHIVE_DEST_3` to use SYNC transport with `DATA_GUARD_SYNC_LATENCY` set to a value of 2 seconds. When redo needs to be sent to the standbys, it is sent to both the `LOG_ARCHIVE_DEST_2` and `LOG_ARCHIVE_DEST_3` connections in parallel and the LGWR will wait for acknowledgement. If `LOG_ARCHIVE_DEST_2` responds with its message acknowledging that the redo has been received first, the LGWR will not wait for `LOG_ARCHIVE_DEST_3` to respond for more than 2 extra seconds (`DATA_GUARD_SYNC_LATENCY`). If `LOG_ARCHIVE_DEST_3` does not respond within those 2 seconds the LGWR disconnects from `LOG_ARCHIVE_DEST_3`, putting it into the error state. Redo continues to be sent to `LOG_ARCHIVE_DEST_2` as usual. After the duration of the `REOPEN` attribute for `LOG_ARCHIVE_DEST_3` has elapsed, the LGWR reconnects to `LOG_ARCHIVE_DEST_3` and redo transfer continues. In this manner, the maximum impact of having the second SYNC standby would be restricted to 2 seconds more than having only one SYNC standby, while allowing the Oracle Data Guard configuration to maintain the desired protection level.

LGWR will never wait longer than the value of the `NET_TIMEOUT` attribute of the `LOG_ARCHIVE_DEST_n` parameter, regardless of the value of `DATA_GUARD_SYNC_LATENCY`.

See Also:

" [LOG\_ARCHIVE\_DEST\_n](LOG_ARCHIVE_DEST_n.md) "