---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/USER_JOINGROUPS.html
tags:
  - oracle
  - 12c
  - reference
---

`USER_JOINGROUPS` describes join groups belonging to the user. A join group is a user-created object that consists of two or more columns that can be meaningfully joined. The maximum number of columns that can be included in a join group is 255. The `USER_JOINGROUPS` columns (except for `JOINGROUP_OWNER`) are the same as those in `DBA_JOINGROUPS`.

In certain queries, join groups enable the database to eliminate the performance overhead of decompressing and hashing column values. Join groups require an In-Memory column store (IM column store).

Note:

This view is available starting with Oracle Database 12c Release 2 (12.2.0.1).

See Also:

- " [DBA\_JOINGROUPS](DBA_JOINGROUPS.md) "
- [Oracle Database In-Memory Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=INMEM-GUID-3E5491C4-B345-4A8E-8B1B-8DC150C8A797) for an introduction to join groups
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=SQLRF-GUID-87CA7034-4F80-4D46-8EE1-5CC865C2D676) for information about creating a join group using the `CREATE INMEMORY JOIN GROUP` statement