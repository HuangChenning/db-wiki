---
title: LOG_ARCHIVE_DEST_STATE_n
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams126.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `LOG_ARCHIVE_DEST_STATE_[1 \| 2 \| 3 \| 4 \| 5 \| 6 \| 7 \| 8 \| 9 \| 10 \| 11 \| 12 \| 13 \| 14 \| 15 \| 16 \| 17 \| 18 \| 19 \| 20 \| 21 \| 22 \| 23 \| 24 \| 25 \| 26 \| 27 \| 28 \| 29 \| 30 \| 31] = { enable \| defer \| alternate }` |
| Default value | `enable` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Basic | Yes |

The `LOG_ARCHIVE_DEST_STATE_` `n` parameters (where `n` = 1, 2, 3,... 31) specify the availability state of the corresponding destination. The parameter suffix (1 through 31) specifies one of the corresponding `LOG_ARCHIVE_DEST_` `n` destination parameters.

Values:

- `enable`
	Specifies that a valid log archive destination can be used for a subsequent archiving operation (automatic or manual). This is the default.
- `defer`
	Specifies that valid destination information and attributes are preserved, but the destination is excluded from archiving operations until re-enabled.
- `alternate`
	Specifies that a log archive destination is not enabled but will become enabled if communications to another destination fail.

The `LOG_ARCHIVE_DEST_STATE_` `n` parameters have no effect on the `ENABLE` state for the `LOG_ARCHIVE_DEST` or `LOG_ARCHIVE_DUPLEX_DEST` parameters.

The `V$ARCHIVE_DEST` dynamic performance view shows values in use for the current session. The `DEST_ID` column of that view corresponds to the archive destination suffix `n`.

See Also:

- [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/toc.htm) and [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm) for more information and examples
- ["V$ARCHIVE\_DEST"](dynviews_1012.md)