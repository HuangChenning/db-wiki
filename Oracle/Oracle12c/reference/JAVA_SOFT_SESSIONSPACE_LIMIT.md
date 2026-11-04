---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/JAVA_SOFT_SESSIONSPACE_LIMIT.html
tags:
  - oracle
  - 12c
  - reference
---

`JAVA_SOFT_SESSIONSPACE_LIMIT` specifies (in bytes) a soft limit on Java memory usage in a session, as a means to warn you if a user's session-duration Java state is using too much memory.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `0` |
| Modifiable | No |
| Modifiable in a PDB | No |
| Range of values | 0 to 2 GB - 1 |
| Basic | No |

Java session space is the memory that holds Java state from one database call to another. When a user's session-duration Java state exceeds the size specified by `JAVA_SOFT_SESSIONSPACE_LIMIT`, Oracle generates a warning that goes into the trace files.

See Also:

- [Oracle Database Java Developer’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=JJDEV13316) for more information on this parameter
- " [JAVA\_MAX\_SESSIONSPACE\_SIZE](JAVA_MAX_SESSIONSPACE_SIZE.md) "