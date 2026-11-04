---
title: Distributed Queries
book: SQL Language Reference
doc_id: E41084-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41084/queries010.htm
tags:
  - oracle
  - 11g
  - sql-language-reference
---

The Oracle distributed database management system architecture lets you access data in remote databases using Oracle Net and an Oracle Database server. You can identify a remote table, view, or materialized view by appending @ `dblink` to the end of its name. The `dblink` must be a complete or partial name for a database link to the database containing the remote table, view, or materialized view.

See Also:

- ["References to Objects in Remote Databases"](sql_elements009.md) for more information on referring to database links
- [Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/toc.htm) for information on accessing remote databases

Restrictions on Distributed Queries Distributed queries are currently subject to the restriction that all tables locked by a `FOR` `UPDATE` clause and all tables with `LONG` columns selected by the query must be located on the same database. In addition, Oracle Database currently does not support distributed queries that select user-defined types or object `REF` data types on remote tables.