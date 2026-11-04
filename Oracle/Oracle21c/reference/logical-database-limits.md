---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/logical-database-limits.html
tags:
  - oracle
  - 21c
  - reference
---

## A.3 Logical Database Limits

This table describes limit types and limit values for logical database items.

| Item | Type of Limit | Limit Value |
| --- | --- | --- |
| Columns | Maximum per table | 1000 |
| Columns | Maximum per index (or clustered index) | 32 |
| Columns | Maximum per bitmapped index | 30 |
| Constraints | Maximum per column | Not defined  Oracle does not define a limit on the number of constraints per column. However, constraints are subject to the limit on the maximum number of constraints in the database. See the entry for " Constraints - Maximum per database " in this table. |
| Constraints | Maximum per database | 4,294,967,293  Constraints are numbered internally from 1 to 4,294,967,294. The internal number is incremented each time a constraint is created, and numbers are never recycled. One number is always consumed by a special internal user called `_NEXT_CONSTRAINT`, which represents the next available number for a new constraint. Therefore, the maximum number of constraints that can be created during the lifetime of a database is 4,294,967,293.  You can view constraint numbers by querying the `CON#` column of the `SYS.CON$` table.  If your database has reached the constraint limit and you would like to create more constraints, contact Oracle Support. |
| Dictionary-managed database objects | Maximum per database | 4,254,950,911 - overhead  - The value of 4,254,950,911 is derived as follows: The data type used for object identifiers can store a maximum value of 4,294,967,294. However, approximately 40 million of these values are reserved at the high end for other purposes, which results in a maximum object identifier value of 4,254,950,911. - Overhead includes the following: 	- Multiple object identifiers for one database object 		Database objects consume one object identifier at the time of creation. This identifier is displayed in both the `OBJECT_ID` and `DATA_OBJECT_ID` columns of the [ALL\_OBJECTS](ALL_OBJECTS.md) view. Over the lifetime of an object, the value of `OBJECT_ID` remains unchanged, but the value of `DATA_OBJECT_ID` changes when the object is altered, for example, with a DDL statement or a table truncation. Therefore, one object can consume more than one object identifier over its lifetime. 		- Object identifiers for lightweight jobs 		Lightweight jobs consume object identifiers, even though they are not permanent objects. Therefore, if many lightweight jobs are running in the database, the number of objects that can be created in the database is dependent upon the remaining pool of identifiers. |
| Indexes | Maximum per table | Not defined  Oracle does not define a limit on the number of indexes per table. However, indexes are subject to the limit on the maximum number of dictionary-managed database objects allowed per database. See the entry for " Dictionary-managed database objects " in this table. |
| Indexes | Total size of indexed column(s) | Approximately 75% of the database block size minus some overhead |
| Partitions | Maximum length of linear partitioning key | 4 KB - overhead |
| Partitions | Maximum number of columns in partition key | 16 columns |
| Partitions | Maximum number of partitions allowed per table or index | 1024K - 1 |
| Rows | Maximum number per table | Not defined |
| Stored Packages | Maximum size | Approximately `6,000,000` lines of code.  See Also: [Oracle Database PL/SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=LNPLS018) for details |
| Subpartitions | Maximum number of subpartitions in a composite partitioned table | 1024K - 1 |
| Subqueries | Maximum levels of subqueries in a SQL statement | `255` subqueries in the `WHERE` clause  A limit is not defined for subqueries in the `FROM` clause of the top-level query. |
| System Change Numbers (SCNs) | Maximum | 2 <sup>63</sup> - 2 <sup>48</sup> = 9,223,090,561,878,065,152 SCNs |
| Tables | Maximum per clustered table | 32 tables |
| Tables | Maximum per database | Not defined  Oracle does not define a limit on the number of tables per database. However, tables are subject to the limit on the maximum number of dictionary-managed database objects allowed per database. See the entry for " Dictionary-managed database objects " in this table. |
| Temporary Tablespaces | Maximum used per session | 16 |
| Users and Roles | Maximum | 2,147,483,638  Users and roles are numbered internally from 0 to 2,147,483,638. The internal number is incremented each time a user or role is created, and numbers are never recycled. One number is always consumed by a special internal user called `_NEXT_USER`, which represents the next available number for a new user or role. Therefore, the maximum number of users and roles that can be created during the lifetime of a database is 2,147,483,638.  You can view user and role numbers by querying the `USER#` column of the `SYS.USER$` table. |

Note:

The limit on how long a SQL statement can be depends on many factors, including database configuration, disk space, and memory

Note:

When an object instance exists in memory, there is no fixed limit on the number of attributes in the object. But the maximum total amount of memory consumed by an object instance is 4 GB. When an object instance is inserted into a table, the attributes are exploded into separate columns in the table, and the Oracle 1000-column limit applies.