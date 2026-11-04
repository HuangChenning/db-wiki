---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DB_BLOCK_CHECKSUM.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.74 DB\_BLOCK\_CHECKSUM

`DB_BLOCK_CHECKSUM` determines whether `DBW` `n` and the direct loader will calculate a checksum (a number calculated from all the bytes stored in the block) and store it in the cache header of every data block when writing it to disk.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `DB_BLOCK_CHECKSUM = { OFF \| FALSE \| TYPICAL \| TRUE \| FULL }` |
| Default value | `TYPICAL` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Basic | No |

Checksums are verified when a block is read - only if this parameter is `TYPICAL` or `FULL` and the last write of the block stored a checksum. In `FULL` mode, Oracle also verifies the checksum before a change application from update/delete statements and recomputes it after the change is applied. In addition, Oracle gives every log block a checksum before writing it to the current log.

Most of the log block checksum is done by the generating foreground processes, while the LGWR or the LGWR worker processes (LGnn processes) perform the rest of the work, for better CPU and cache efficiency.

If this parameter is set to `OFF`, `DBW` `n` calculates checksums only for the `SYSTEM` tablespace, but not for user tablespaces. In addition, no log checksum is performed when this parameter is set to `OFF`.

Checksums allow Oracle to detect corruption caused by underlying disks, storage systems, or I/O systems. If set to `FULL`, `DB_BLOCK_CHECKSUM` also catches in-memory corruptions and stops them from making it to the disk. Turning on this feature in `TYPICAL` mode causes only an additional 1% to 2% overhead. In the `FULL` mode it causes 4% to 5% overhead. Oracle recommends that you set `DB_BLOCK_CHECKSUM` to `TYPICAL`.

For backward compatibility the use of `TRUE` (implying `TYPICAL`) and `FALSE` (implying `OFF`) values is preserved.

See Also:

[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RCMRF90307) for more information about this parameter