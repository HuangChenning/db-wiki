---
title: About Dynamic Performance Views
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1001.htm
tags:
  - oracle
  - 11g
  - reference
---

Oracle contains a set of underlying views that are maintained by the database server and accessible to the database administrator user `SYS`. These views are called dynamic performance views because they are continuously updated while a database is open and in use, and their contents relate primarily to performance.

Although these views appear to be regular database tables, they are not. These views provide data on internal disk structures and memory structures. You can select from these views, but you can never update or alter them.

Note:

- You can query the dynamic performance views to extract information from them. However, only simple queries are supported. If sorts, joins, `GROUP BY` clauses and the like are needed, then you should copy the information from each `V$` view into a table (for example, using a `CREATE TABLE ... AS SELECT` statement), and then query from those tables.
- Because the information in the `V$` views is dynamic, read consistency is not guaranteed for `SELECT` operations on these views.

The `catalog.sql` script contains definitions of the views and public synonyms for the dynamic performance views. You must run `catalog.sql` to create these views and synonyms. After installation, only user `SYS` or anyone with `SYSDBA` role has access to the dynamic performance tables. See [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/create.htm#ADMIN11082) for more information about running `catalog.sql`.

## V$ Views

The actual dynamic performance views are identified by the prefix `V_$`. Public synonyms for these views have the prefix `V$`. Database administrators and other users should access only the `V$` objects, not the `V_$` objects.

The dynamic performance views are used by Oracle Enterprise Manager, which is the primary interface for accessing information about system performance. After an instance is started, the `V$` views that read from memory are accessible. Views that read data from disk require that the database be mounted, and some require that the database be open.

## GV$ Views

For almost every `V$` view described in this chapter, Oracle has a corresponding `GV$` (global `V$`) view. In Real Application Clusters, querying a `GV$` view retrieves the `V$` view information from all qualified instances. In addition to the `V$` information, each `GV$` view contains an extra column named `INST_ID` of datatype `NUMBER`. The `INST_ID` column displays the instance number from which the associated `V$` view information was obtained. The `INST_ID` column can be used as a filter to retrieve `V$` information from a subset of available instances. For example, the following query retrieves the information from the `V$LOCK` view on instances 2 and 5:

```
SQL> SELECT * FROM GV$LOCK WHERE INST_ID = 2 OR INST_ID = 5;
```

See Also:

Oracle Real Application Clusters Installation and Configuration Guide for your operating system