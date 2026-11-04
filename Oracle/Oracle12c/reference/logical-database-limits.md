---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/logical-database-limits.html
tags:
  - oracle
  - 12c
  - reference
---

This table describes limit types and limit values for logical database items.

| Item | Type of Limit | Limit Value |
| --- | --- | --- |
| Columns | Maximum per table | 1000 |
| Columns | Maximum per index (or clustered index) | 32 |
| Columns | Maximum per bitmapped index | 30 |
| Constraints | Maximum per column | Unlimited  Oracle does not define a limit on the number of constraints per column. However, constraints are subject to the limit on the maximum number of constraints in the database. See the entry for " Constraints - Maximum per database " in this table. |
| Constraints | Maximum per database | 4,294,967,293 |
| Database users | Maximum per database | 4,294,967,293 |
| Dictionary-managed database objects | Maximum per database | 4,254,950,911 - overhead |
| Indexes | Maximum per table | Unlimited  Oracle does not define a limit on the number of indexes per table. However, indexes are subject to the limit on the maximum number of dictionary-managed database objects allowed per database. See the entry for " Dictionary-managed database objects " in this table. |
| Indexes | Total size of indexed column(s) | Approximately 75% of the database block size minus some overhead |
| Partitions | Maximum length of linear partitioning key | 4 KB - overhead |
| Partitions | Maximum number of columns in partition key | 16 columns |
| Partitions | Maximum number of partitions allowed per table or index | 1024K - 1 |
| Rows | Maximum number per table | Unlimited |
| Stored Packages | Maximum size | Approximately `6,000,000` lines of code.  See Also: [Oracle Database PL/SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=LNPLS018) for details |
| Subpartitions | Maximum number of subpartitions in a composite partitioned table | 1024K - 1 |
| Subqueries | Maximum levels of subqueries in a SQL statement | Unlimited in the `FROM` clause of the top-level query  `255` subqueries in the `WHERE` clause |
| System Change Numbers (SCNs) | Maximum | 2 <sup>63</sup> - 2 <sup>48</sup> = 9,223,090,561,878,065,152 SCNs |
| Tables | Maximum per clustered table | 32 tables |
| Tables | Maximum per database | Unlimited  Oracle does not define a limit on the number of tables per database. However, tables are subject to the limit on the maximum number of dictionary-managed database objects allowed per database. See the entry for " Dictionary-managed database objects " in this table. |
| Trigger Cascade Limit | Maximum value | Operating system-dependent, typically `32` |
| Users and Roles | Maximum | 2,147,483,638 |

Note:

The limit on how long a SQL statement can be depends on many factors, including database configuration, disk space, and memory

Note:

When an object instance exists in memory, there is no fixed limit on the number of attributes in the object. But the maximum total amount of memory consumed by an object instance is 4 GB. When an object instance is inserted into a table, the attributes are exploded into separate columns in the table, and the Oracle 1000-column limit applies.