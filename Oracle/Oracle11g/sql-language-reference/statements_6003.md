---
title: CREATE MATERIALIZED VIEW LOG
book: SQL Language Reference
doc_id: E41084-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_6003.htm
tags:
  - oracle
  - 11g
  - sql-language-reference
---

Purpose

Use the `CREATE` `MATERIALIZED` `VIEW` `LOG` statement to create a materialized view log, which is a table associated with the master table of a materialized view.

Note:

The keyword `SNAPSHOT` is supported in place of `MATERIALIZED` `VIEW` for backward compatibility.

When DML changes are made to master table data, Oracle Database stores rows describing those changes in the materialized view log and then uses the materialized view log to refresh materialized views based on the master table. This process is called incremental or fast refresh. Without a materialized view log, Oracle Database must reexecute the materialized view query to refresh the materialized view. This process is called a complete refresh. Usually, a fast refresh takes less time than a complete refresh.

A materialized view log is located in the master database in the same schema as the master table. A master table can have only one materialized view log defined on it. Oracle Database can use this materialized view log to perform fast refreshes for all fast-refreshable materialized views based on the master table.

To fast refresh a materialized join view, you must create a materialized view log for each of the tables referenced by the materialized view.

There are two types of materialized view logs: timestamp-based materialized view logs and commit SCN-based materialized view logs. Timestamp-based materialized view logs use timestamps and require some setup operations when preparing to refresh the materialized view. Commit SCN-based materialized view logs use commit SCN data rather than timestamps, which removes the need for the setup operations and thus can improve the speed of the materialized view refresh. If you specify the `COMMIT` `SCN` clause, then a commit SCN-based materialized view log is created. Otherwise, a time-stamp based materialized view log is created.

Note that only new materialized view logs can take advantage of `COMMIT` `SCN`. Existing materialized view logs cannot be altered to add `COMMIT` `SCN` unless they are dropped and recreated. Refer to [Oracle Database Data Warehousing Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25554/refresh.htm#DWHSG0319) for more information.

See Also:

- [CREATE MATERIALIZED VIEW](statements_6002.md), [ALTER MATERIALIZED VIEW](statements_2002.md), [Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/schemaob.htm#CNCPT411), [Oracle Database Data Warehousing Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25554/basicmv.htm#DWHSG008), and [Oracle Database Advanced Replication](https://docs.oracle.com/cd/E11882_01/server.112/e10706/repmview.htm#REPLN003) for information on materialized views in general
- [ALTER MATERIALIZED VIEW LOG](statements_2003.md) for information on modifying a materialized view log
- [DROP MATERIALIZED VIEW LOG](statements_8022.md) for information on dropping a materialized view log
- [Oracle Database Utilities](https://docs.oracle.com/cd/E11882_01/server.112/e22490/ldr_concepts.htm#SUTIL003) for information on using direct loader logs

Prerequisites

The privileges required to create a materialized view log directly relate to the privileges necessary to create the underlying objects associated with a materialized view log.

- If you own the master table, then you can create an associated materialized view log if you have the `CREATE` `TABLE` privilege.
- If you are creating a materialized view log for a table in another user's schema, then you must have the `CREATE` `ANY` `TABLE` and `COMMENT` `ANY` `TABLE` system privileges, as well as either the `SELECT` object privilege on the master table or the `SELECT` `ANY` `TABLE` system privilege.

In either case, the owner of the materialized view log must have sufficient quota in the tablespace intended to hold the materialized view log or must have the `UNLIMITED` `TABLESPACE` system privilege.

See Also:

[Oracle Database Data Warehousing Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25554/basicmv.htm#DWHSG008) for more information about the prerequisites for creating a materialized view log

Syntax

create\_materialized\_vw\_log::=

![create_materialized_vw_log](img/create_materialized_vw_log.gif)

> ```
> CREATE MATERIALIZED VIEW LOG ON [ schema. ] table
>   [ physical_attributes_clause
>   | TABLESPACE tablespace
>   | logging_clause
>   | { CACHE | NOCACHE }
>   ]...
>   [ parallel_clause ]
>   [ table_partitioning_clauses ]
>   [ WITH [ { OBJECT ID
>          | PRIMARY KEY
>          | ROWID
>          | SEQUENCE
>          | COMMIT SCN
>          }
>            [ { , OBJECT ID
>              | , PRIMARY KEY
>              | , ROWID
>              | , SEQUENCE
>              | , COMMIT SCN
>              }
>            ]... ]
>     (column [, column ]...)
>     [ new_values_clause ]
>   ] [ mv_log_purge_clause ] 
> ;
> ```
  
  

([physical\_attributes\_clause::=](statements_6002.md), logging\_clause::=, parallel\_clause::=, [table\_partitioning\_clauses::=](statements_7002.md) (in `CREATE` `TABLE`), new\_values\_clause::=, mv\_log\_purge\_clause::=.)

physical\_attributes\_clause::=

![physical_attributes_clause](img/physical_attributes_clause.gif)

> ```
> [ { PCTFREE integer
>   | PCTUSED integer
>   | INITRANS integer
>   | storage_clause
>   }...
> ]
> ```
  
  

([storage\_clause::=](clauses009.md))

logging\_clause::=

![logging_clause](img/logging_clause.gif)

> ```
> { LOGGING | NOLOGGING |  FILESYSTEM_LIKE_LOGGING }
> ```
  
  

parallel\_clause::=

![parallel_clause](img/parallel_clause.gif)

> ```
> { NOPARALLEL | PARALLEL [ integer ] }
> ```
  
  

new\_values\_clause::=

![new_values_clause](img/new_values_clause.gif)

> ```
> { INCLUDING | EXCLUDING } NEW VALUES
> ```
  
  

mv\_log\_purge\_clause::=

![mv_log_purge_clause](img/mv_log_purge_clause.gif)

> ```
> PURGE { IMMEDIATE [ SYNCHRONOUS | ASYNCHRONOUS ]
>       | START WITH datetime_expr [ NEXT datetime_expr 
>                                  | REPEAT INTERVAL interval_expr 
>                                  ]
>       | [ START WITH datetime_expr ] { NEXT datetime_expr 
>                                      | REPEAT INTERVAL interval_expr 
>                                      }
>       }
> ```
  

Semantics

schema

Specify the schema containing the materialized view log master table. If you omit `schema`, then Oracle Database assumes the master table is contained in your own schema. Oracle Database creates the materialized view log in the schema of its master table. You cannot create a materialized view log for a table in the schema of the user `SYS`.

table

Specify the name of the master table for which the materialized view log is to be created. Oracle Database encrypts any columns in the materialized view log that are encrypted in the master table, using the same encryption algorithm.

Restrictions on Master Tables of Materialized View Logs The following restrictions apply to master tables of materialized view logs:

- You cannot create a materialized view log for a temporary table or for a view.
- You cannot create a materialized view log for a master table with a virtual column.

See Also:

"Creating a Materialized View Log: Examples"

physical\_attributes\_clause

Use the `physical_attributes_clause` to define physical and storage characteristics for the materialized view log.

See Also:

[physical\_attributes\_clause](clauses007.md) and [storage\_clause](clauses007.md) for a complete description these clauses, including default values

TABLESPACE Clause

Specify the tablespace in which the materialized view log is to be created. If you omit this clause, then the database creates the materialized view log in the default tablespace of the schema of the materialized view log.

logging\_clause

Specify either `LOGGING` or `NOLOGGING` to establish the logging characteristics for the materialized view log. The default is the logging characteristic of the tablespace in which the materialized view log resides.

See Also:

[logging\_clause](clauses005.md) for a full description of this clause

CACHE | NOCACHE

For data that will be accessed frequently, `CACHE` specifies that the blocks retrieved for this log are placed at the most recently used end of the least recently used (LRU) list in the buffer cache when a full table scan is performed. This attribute is useful for small lookup tables.

`NOCACHE` specifies that the blocks are placed at the least recently used end of the LRU list. The default is `NOCACHE`.

Note:

`NOCACHE` has no effect on materialized view logs for which you specify `KEEP` in the `storage_clause`.

See Also:

[CREATE TABLE](statements_7002.md) for information about specifying `CACHE` or `NOCACHE`

parallel\_clause

The `parallel_clause` lets you indicate whether parallel operations will be supported for the materialized view log.

For complete information on this clause, refer to [parallel\_clause](statements_7002.md) in the documentation on `CREATE` `TABLE`.

table\_partitioning\_clauses

Use the `table_partitioning_clauses` to indicate that the materialized view log is partitioned on specified ranges of values or on a hash function. Partitioning of materialized view logs is the same as partitioning of tables.

See Also:

[table\_partitioning\_clauses](statements_7002.md) in the `CREATE TABLE` documentation

WITH Clause

Use the `WITH` clause to indicate whether the materialized view log should record the primary key, rowid, object ID, or a combination of these row identifiers when rows in the master are changed. You can also use this clause to add a sequence to the materialized view log to provide additional ordering information for its records.

This clause also specifies whether the materialized view log records additional columns that might be referenced as filter columns, which are non-primary-key columns referenced by subquery materialized views, or join columns, which are non-primary-key columns that define a join in the subquery `WHERE` clause.

If you omit this clause, or if you specify the clause without `PRIMARY` `KEY`, `ROWID`, or `OBJECT` `ID`, then the database stores primary key values by default. However, the database does not store primary key values implicitly if you specify only `OBJECT` `ID` or `ROWID` at create time. A primary key log, created either explicitly or by default, performs additional checking on the primary key constraint.

OBJECT ID Specify `OBJECT` `ID` to indicate that the system-generated or user-defined object identifier of every modified row should be recorded in the materialized view log.

Restriction on OBJECT ID You can specify `OBJECT` `ID` only when creating a log on an object table, and you cannot specify it for storage tables.

PRIMARY KEY Specify `PRIMARY` `KEY` to indicate that the primary key of all rows changed should be recorded in the materialized view log.

ROWID Specify `ROWID` to indicate that the rowid of all rows changed should be recorded in the materialized view log.

SEQUENCE Specify `SEQUENCE` to indicate that a sequence value providing additional ordering information should be recorded in the materialized view log. Sequence numbers are necessary to support fast refresh after some update scenarios.

See Also:

[Oracle Database Data Warehousing Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25554/basicmv.htm#DWHSG008) for more information on the use of sequence numbers in materialized view logs and for examples that use this clause

COMMIT SCN

Without the `COMMIT` `SCN` clause, the materialized view log is based on timestamps and requires some setup operations when preparing to refresh the materialized view. Specify `COMMIT` `SCN` to instruct the database to use commit SCN data rather than timestamps. This setting removes the need for the setup operations and thus can improve the speed of the materialized view refresh.

You can create the following types of local materialized views (including both `ON` `COMMIT` and `ON` `DEMAND`) on master tables with commit SCN-based materialized view logs:

- Materialized aggregate views, including materialized aggregate views on a single table
- Materialized join views
- Primary-key-based and rowid-based single table materialized views
- `UNION` `ALL` materialized views, where each `UNION` `ALL` branch is one of the above materialized view types

You cannot create remote materialized views on master tables with commit SCN-based materialized view logs.

Restrictions on COMMIT SCN The following restrictions apply to `COMMIT` `SCN`:

- Use of `COMMIT` `SCN` on a table with one or more LOB columns is not supported and causes `ORA-32421`.
- Creating a materialized view on master tables with different types of materialized view logs (that is, a master table with timestamp-based materialized view logs and a master table with commit SCN-based materialized view logs) is not supported and causes `ORA-32414`.

column Specify the columns whose values you want to be recorded in the materialized view log for all rows that are changed. Typically these columns are filter columns and join columns.

Restrictions on the WITH Clause This clause is subject to the following restrictions:

- You can specify only one `PRIMARY` `KEY`, one `ROWID`, one `OBJECT` `ID`, one `SEQUENCE`, and one column list for each materialized view log.
- Primary key columns are implicitly recorded in the materialized view log. Therefore, you cannot specify any of the following combinations if `column` contains one of the primary key columns:
	```
	WITH ... PRIMARY KEY ... (column)
	WITH ... (column) ... PRIMARY KEY
	WITH (column)
	```

See Also:

- [CREATE MATERIALIZED VIEW](statements_6002.md) for information on explicit and implicit inclusion of materialized view log values
- [Oracle Database Advanced Replication](https://docs.oracle.com/cd/E11882_01/server.112/e10706/repplan.htm#REPLN006) for more information about filter columns and join columns
- "Specifying Filter Columns for Materialized View Logs: Example" and "Specifying Join Columns for Materialized View Logs: Example"

NEW VALUES Clause

The `NEW` `VALUES` clause lets you determine whether Oracle Database saves both old and new values for update DML operations in the materialized view log.

See Also:

"Including New Values in Materialized View Logs: Example"

INCLUDING Specify `INCLUDING` to save both new and old values in the log. If this log is for a table on which you have a single-table materialized aggregate view, and if you want the materialized view to be eligible for fast refresh, then you must specify `INCLUDING`.

EXCLUDING Specify `EXCLUDING` to disable the recording of new values in the log. This is the default. You can use this clause to avoid the overhead of recording new values. Do not use this clause if you have a fast-refreshable single-table materialized aggregate view defined on the master table.

mv\_log\_purge\_clause

Use this clause to specify the purge time for the materialized view log.

- `IMMEDIATE` `SYNCHRONOUS`: the materialized view log is purged immediately after refresh. This is the default.
- `IMMEDIATE` `ASYNCHRONOUS`: the materialized view log is purged in a separate Oracle Scheduler job after the refresh operation.
- `START` `WITH`, `NEXT`, and `REPEAT` `INTERVAL` set up a scheduled purge that is independent of the materialized view refresh and is initiated during `CREATE` or `ALTER` `MATERIALIZED` `VIEW` `LOG` statement. This is very similar to scheduled refresh syntax in a `CREATE` or `ALTER` `MATERIALIZED` `VIEW` statement:
	- The `START` `WITH` datetime expression specifies when the purge starts.
		- The `NEXT` datetime expression computes the next run time for the purge.
	If you specify `REPEAT` `INTERVAL`, then the next run time will be: `SYSDATE +` `interval_expr`.
	A `CREATE` `MATERIALIZED` `VIEW` `LOG` statement with a scheduled purge creates an Oracle Scheduler job to perform log purge. The job calls the `DBMS_SNAPSHOT`.`PURGE_LOG` procedure to purge the materialized view logs. This process allows you to amortize the purging costs over several materialized view refreshes.

Restriction on mv\_log\_purge\_clause This clause is not valid for materialized view logs on temporary tables.

See Also:

[Oracle Database Data Warehousing Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25554/basicmv.htm#DWHSG8211) for more information on purging materialized view logs

Examples

Creating a Materialized View Log: Examples The following statement creates a materialized view log on the `oe.customers` table that specifies physical and storage characteristics:

```
CREATE MATERIALIZED VIEW LOG ON customers 
   PCTFREE 5 
   TABLESPACE example 
   STORAGE (INITIAL 10K);
```

The materialized view log on `customers` supports fast refresh for primary key materialized views only.

The following statement creates another version of the materialized view log with the `ROWID` clause, which enables fast refresh for more types of materialized views:

```
CREATE MATERIALIZED VIEW LOG ON customers WITH PRIMARY KEY, ROWID;
```

This materialized view log on `customers` makes fast refresh possible for rowid materialized views and for materialized join views. To provide for fast refresh of materialized aggregate views, you must also specify the `SEQUENCE` and `INCLUDING` `NEW` `VALUES` clauses, as shown in the example that follows.

Specify a Purge Repeat Interval for a Materialized View Log: Example The following statement creates a materialized view log on the `oe.orders` table. The contents of the log will be purged once every five days, beginning five days after the creation date of the materialized view log:

```
CREATE MATERIALIZED VIEW LOG ON orders
  PCTFREE 5
  TABLESPACE example
  STORAGE (INITIAL 10K)
  PURGE REPEAT INTERVAL '5' DAY;
```

Specifying Filter Columns for Materialized View Logs: Example The following statement creates a materialized view log on the `sh.sales` table and is used in ["Creating Materialized Aggregate Views: Example"](statements_6002.md). It specifies as filter columns all of the columns of the table referenced in that materialized view.

```
CREATE MATERIALIZED VIEW LOG ON sales 
   WITH ROWID, SEQUENCE(amount_sold, time_id, prod_id)
   INCLUDING NEW VALUES;
```

Specifying Join Columns for Materialized View Logs: Example The following statement creates a materialized view log on the `order_items` table of the sample `oe` schema. The log records primary keys and `product_id`, which is used as a join column in ["Creating a Fast Refreshable Materialized View: Example"](statements_6002.md).

```
CREATE MATERIALIZED VIEW LOG ON order_items WITH (product_id);
```

Including New Values in Materialized View Logs: Example The following example creates a materialized view log on the `oe.product_information` table that specifies `INCLUDING` `NEW` `VALUES`:

```
CREATE MATERIALIZED VIEW LOG ON product_information 
   WITH ROWID, SEQUENCE (list_price, min_price, category_id), PRIMARY KEY
   INCLUDING NEW VALUES;
```

You could create the following materialized aggregate view to use the `product_information` log:

```
CREATE MATERIALIZED VIEW products_mv 
   REFRESH FAST ON COMMIT
   AS SELECT SUM(list_price - min_price), category_id
         FROM product_information 
         GROUP BY category_id;
```

This materialized view is eligible for fast refresh because the log defined on its master table includes both old and new values.