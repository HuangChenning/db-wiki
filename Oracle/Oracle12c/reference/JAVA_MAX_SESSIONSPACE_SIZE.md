---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/JAVA_MAX_SESSIONSPACE_SIZE.html
tags:
  - oracle
  - 12c
  - reference
---

`JAVA_MAX_SESSIONSPACE_SIZE` specifies (in bytes) the maximum amount of session space made available to a Java program executing in the server.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `0` |
| Modifiable | No |
| Modifiable in a PDB | No |
| Range of values | 0 to 2 GB - 1 |
| Basic | No |

Java session space is the memory that holds Java state from one database call to another. When a user's session-duration Java state attempts to exceed the amount specified by `JAVA_MAX_SESSIONSPACE_SIZE`, the Java virtual machine kills the session with an out-of-memory failure.

See Also:

- [Oracle Database Java Developer’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=JJDEV13316) for more information about this parameter
- " [JAVA\_SOFT\_SESSIONSPACE\_LIMIT](JAVA_SOFT_SESSIONSPACE_LIMIT.md) "