---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/FILESYSTEMIO_OPTIONS.html
tags:
  - oracle
  - 12c
  - reference
---

`FILESYSTEMIO_OPTIONS` specifies I/O operations for file system files.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `FILESYSTEMIO_OPTIONS = { none \| setall \| directIO \| asynch }` |
| Default value | Varies by database version and operating system. |
| Modifiable | No |
| Modifiable in a PDB | No |
| Basic | No |

See Also:

[Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=TGDBA94383) for information about setting this parameter before running I/O calibration