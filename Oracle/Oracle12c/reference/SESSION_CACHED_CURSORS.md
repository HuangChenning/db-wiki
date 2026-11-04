---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/SESSION_CACHED_CURSORS.html
tags:
  - oracle
  - 12c
  - reference
---

`SESSION_CACHED_CURSORS` specifies the number of session cursors to cache.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `50` |
| Modifiable | `ALTER SESSION, ALTER SYSTEM ... DEFERRED` |
| Modifiable in a PDB | Yes |
| Range of values | 0 to operating system-dependent |
| Basic | No |
| Oracle RAC | Multiple instances can have different values. |

Repeated parse calls of the same SQL (including recursive SQL) or PL/SQL statement cause the session cursor for that statement to be moved into the session cursor cache. Oracle uses a least recently used algorithm to remove entries in the session cursor cache to make room for new entries when needed.

See Also:

[Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=TGDBA598) for information about enabling the session cursor cache