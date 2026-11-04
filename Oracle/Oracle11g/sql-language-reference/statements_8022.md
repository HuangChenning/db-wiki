---
title: DROP MATERIALIZED VIEW LOG
book: SQL Language Reference
doc_id: E41084-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_8022.htm
tags:
  - oracle
  - 11g
  - sql-language-reference
---

Purpose

Use the `DROP` `MATERIALIZED` `VIEW` `LOG` statement to remove a materialized view log from the database.

Note:

The keyword `SNAPSHOT` is supported in place of `MATERIALIZED` `VIEW` for backward compatibility.

See Also:

- [CREATE MATERIALIZED VIEW](statements_6002.md) and [ALTER MATERIALIZED VIEW](statements_2002.md) for more information on materialized views
- [CREATE MATERIALIZED VIEW LOG](statements_6003.md) for information on materialized view logs
- [Oracle Database Advanced Replication](https://docs.oracle.com/cd/E11882_01/server.112/e10706/repmview.htm#REPLN003) for information on materialized views in a replication environment
- [Oracle Database Data Warehousing Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25554/basicmv.htm#DWHSG008) for information on materialized views in a data warehousing environment

Prerequisites

To drop a materialized view log, you must have the privileges needed to drop a table.

See Also:

[DROP TABLE](statements_9003.md)

Syntax

drop\_materialized\_view\_log::=

![drop_materialized_view_log](img/drop_materialized_view_log.gif)

> ```
> DROP MATERIALIZED VIEW LOG ON [ schema. ] table ;
> ```
  

Semantics

schema

Specify the schema containing the materialized view log and its master table. If you omit `schema`, then Oracle Database assumes the materialized view log and master table are in your own schema.

table

Specify the name of the master table associated with the materialized view log to be dropped.

After you drop a materialized view log, some materialized views based on the materialized view log master table can no longer be fast refreshed. These materialized views include rowid materialized views, primary key materialized views, and subquery materialized views.

See Also:

[Oracle Database Data Warehousing Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25554/basicmv.htm#DWHSG008) for a description of these types of materialized views

Examples

Dropping a Materialized View Log: Example The following statement drops the materialized view log on the `oe.customers` master table:

```
DROP MATERIALIZED VIEW LOG ON customers;
```