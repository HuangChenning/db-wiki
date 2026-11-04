---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/LOG_ARCHIVE_DEST_STATE_n.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.186 LOG\_ARCHIVE\_DEST\_STATE\_n

The `LOG_ARCHIVE_DEST_STATE_` `n` parameters (where `n` = 1, 2, 3,... 31) specify the availability state of the corresponding destination.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `LOG_ARCHIVE_DEST_STATE_[1 \| 2 \| 3 \| 4 \| 5 \| 6 \| 7 \| 8 \| 9 \| 10 \| 11 \| 12 \| 13 \| 14 \| 15 \| 16 \| 17 \| 18 \| 19 \| 20 \| 21 \| 22 \| 23 \| 24 \| 25 \| 26 \| 27 \| 28 \| 29 \| 30 \| 31] = { enable \| defer \| alternate \| reset }` |
| Default value | `enable` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Basic | Yes |

The parameter suffix (1 through 31) specifies one of the corresponding `LOG_ARCHIVE_DEST_` `n` destination parameters.

Values

- `enable`
	Specifies that a valid log archive destination can be used for a subsequent archiving operation (automatic or manual). This is the default.
- `defer`
	Specifies that valid destination information and attributes are preserved, but the destination is excluded from archiving operations until reenabled.
- `alternate`
	Specifies that a log archive destination is not enabled but will become enabled if communications to another destination fail.
- `reset`
	Functions the same as `defer`, but clears any error messages for the destination if it had previously failed.

The `LOG_ARCHIVE_DEST_STATE_` `n` parameters have no effect on the `ENABLE` state for the `LOG_ARCHIVE_DEST` or `LOG_ARCHIVE_DUPLEX_DEST` parameters.

The `V$ARCHIVE_DEST` dynamic performance view shows values in use for the current session. The `DEST_ID` column of that view corresponds to the archive destination suffix `n`.

See Also:

- [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=SBYDB5028) for more information about this parameter
- " [V$ARCHIVE\_DEST](V-ARCHIVE_DEST.md) "