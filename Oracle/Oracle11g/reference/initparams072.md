---
title: DB_WRITER_PROCESSES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams072.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | 1 or `CPU_COUNT` / 8, whichever is greater. If the number of processor groups is less than 36 but greater than the number of DB writer processes, then the number of DB writer processes is adjusted to be a multiple of the number of processor groups. If the number of DB writer processes is greater than or equal to the number of processor groups, then there is no adjustment. |
| Modifiable | No |
| Range of values | 1 to 36 |
| Basic | No |

`DB_WRITER_PROCESSES` specifies the initial number of database writer processes (DBW0,... DBW9 and DBWa,... DBWz) for an instance. This parameter is useful for systems that modify data heavily.

See Also:

- [Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/toc.htm) for more information on the database writer processes
- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/toc.htm) for information on setting this parameter