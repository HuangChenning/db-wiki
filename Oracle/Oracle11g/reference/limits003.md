---
title: Logical Database Limits
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/limits003.htm
tags:
  - oracle
  - 11g
  - reference
---

| Item | Type of Limit | Limit Value |
| --- | --- | --- |
| Indexes | Maximum per table | Unlimited |
| Indexes | Total size of indexed column | 75% of the database block size minus some overhead |
| Columns | Per table | 1000 columns maximum |
| Columns | Per index (or clustered index) | 32 columns maximum |
| Columns | Per bitmapped index | 30 columns maximum |
| Constraints | Maximum per column | Unlimited |
| Subqueries | Maximum levels of subqueries in a SQL statement | Unlimited in the `FROM` clause of the top-level query  `255` subqueries in the `WHERE` clause |
| Partitions | Maximum length of linear partitioning key | `4` KB - overhead |
| Partitions | Maximum number of columns in partition key | 16 columns |
| Partitions | Maximum number of partitions allowed per table or index | 1024K - 1 |
| Subpartitions | Maximum number of subpartitions in a composite partitioned table | 1024K - 1 |
| Rows | Maximum number per table | Unlimited |
| System Change Numbers (SCNs) | Maximum | 281,474,976,710,656, which is 281 trillion SCNs |
| Stored Packages | Maximum size | Approximately `6,000,000` lines of code.  See Also: [Oracle Database PL/SQL Language Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/limits.htm#LNPLS018) for details |
| Trigger Cascade Limit | Maximum value | Operating system-dependent, typically `32` |
| Users and Roles | Maximum | `2,147,483,638` |
| Tables | Maximum per clustered table | 32 tables |
| Tables | Maximum per database | Unlimited |

Note:

The limit on how long a SQL statement can be depends on many factors, including database configuration, disk space, and memory

Note:

When an object instance exists in memory, there is no fixed limit on the number of attributes in the object. But the maximum total amount of memory consumed by an object instance is 4 GB.When an object instance is inserted into a table, the attributes are exploded into separate columns in the table, and the Oracle 1000-column limit applies.