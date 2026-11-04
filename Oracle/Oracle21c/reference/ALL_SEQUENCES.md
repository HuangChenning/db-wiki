---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_SEQUENCES.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.72 ALL\_SEQUENCES

`ALL_SEQUENCES` describes all sequences accessible to the current user.

Related Views

- `DBA_SEQUENCES` describes all sequences in the database.
- `USER_SEQUENCES` describes all sequences owned by the current user. This view does not display the `SEQUENCE_OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SEQUENCE_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the sequence |
| `SEQUENCE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Sequence name |
| `MIN_VALUE` | `NUMBER` |  | Minimum value of the sequence |
| `MAX_VALUE` | `NUMBER` |  | Maximum value of the sequence |
| `INCREMENT_BY` | `NUMBER` | `NOT NULL` | Value by which sequence is incremented |
| `CYCLE_FLAG` | `VARCHAR2(1)` |  | Indicates whether the sequence wraps around on reaching the limit (`Y`) or not (`N`) |
| `ORDER_FLAG` | `VARCHAR2(1)` |  | Indicates whether sequence numbers are generated in order (`Y`) or not (`N`) |
| `CACHE_SIZE` | `NUMBER` | `NOT NULL` | Number of sequence numbers to cache |
| `LAST_NUMBER` | `NUMBER` | `NOT NULL` | Last sequence number written to disk. If a sequence uses caching, the number written to disk is the last number placed in the sequence cache. This number is likely to be greater than the last sequence number that was used.  For session sequences, the value in this column should be ignored. |
| `SCALE_FLAG` | `VARCHAR2(1)` |  | Indicates whether this is a scalable sequence (`Y`) or not (`N`) |
| `EXTEND_FLAG` | `VARCHAR2(1)` |  | Indicates whether this scalable sequence’s generated values extend beyond `MAX_VALUE` or `MIN_VALUE` (`Y`) or not (`N`) |
| `SHARDED_FLAG` | `VARCHAR2(1)` |  | Indicates whether this is a sharded sequence (`Y`) or not (`N`) |
| `SESSION_FLAG` | `VARCHAR2(1)` |  | Indicates whether sequence values are session private (`Y`) or not (`N`) |
| `KEEP_VALUE` | `VARCHAR2(1)` |  | Indicates whether sequence values are kept during replay after a failure (`Y`) or not (`N`) |

See Also:

- " [DBA\_SEQUENCES](DBA_SEQUENCES.md) "
- " [USER\_SEQUENCES](USER_SEQUENCES.md) "