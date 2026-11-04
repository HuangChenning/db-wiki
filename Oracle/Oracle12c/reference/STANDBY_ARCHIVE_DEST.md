---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/STANDBY_ARCHIVE_DEST.html
tags:
  - oracle
  - 12c
  - reference
---

Use `STANDBY_ARCHIVE_DEST` to specify where archived logs received from a primary database are stored on a standby database. It is no longer necessary to set this parameter, because an appropriate location is automatically chosen.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `STANDBY_ARCHIVE_DEST = ` `filespec` |
| Default value | Operating system-specific |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Range of values | A valid path or device name other than `RAW` |
| Basic | No |

Note:

The `STANDBY_ARCHIVE_DEST` parameter is deprecated. It is retained for backward compatibility only.

See Also:

[Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=SBYDB00010) for more information about Oracle Data Guard