---
title: "MySQL :: MySQL 26.7 Reference Manual :: 28.3.23 The INFORMATION_SCHEMA ndb_transid_mysql_connection_map Table"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/information-schema-ndb-transid-mysql-connection-map-table.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

### 28.3.23 The INFORMATION\_SCHEMA ndb\_transid\_mysql\_connection\_map Table

The `ndb_transid_mysql_connection_map` table provides a mapping between `NDB` transactions, `NDB` transaction coordinators, and MySQL Servers attached to an NDB Cluster as API nodes. This information is used when populating the [`server_operations`](mysql-cluster-ndbinfo-server-operations.md) and [`server_transactions`](mysql-cluster-ndbinfo-server-transactions.md) tables of the [`ndbinfo`](mysql-cluster-ndbinfo.md) NDB Cluster information database.

| `INFORMATION_SCHEMA` Name | `SHOW` Name | Remarks |
| --- | --- | --- |
| `mysql_connection_id` |  | MySQL Server connection ID |
| `node_id` |  | Transaction coordinator node ID |
| `ndb_transid` |  | [`NDB`](mysql-cluster.md) transaction ID |

The `mysql_connection_id` is the same as the connection or session ID shown in the output of [`SHOW PROCESSLIST`](show-processlist.md).

There are no `SHOW` statements associated with this table.

This is a nonstandard table, specific to NDB Cluster. It is implemented as an `INFORMATION_SCHEMA` plugin; you can verify that it is supported by checking the output of [`SHOW PLUGINS`](show-plugins.md). If `ndb_transid_mysql_connection_map` support is enabled, the output from this statement includes a plugin having this name, of type `INFORMATION SCHEMA`, and having status `ACTIVE`, as shown here (using emphasized text):

```sql
mysql> SHOW PLUGINS;
+----------------------------------+--------+--------------------+---------+---------+
| Name                             | Status | Type               | Library | License |
+----------------------------------+--------+--------------------+---------+---------+
| binlog                           | ACTIVE | STORAGE ENGINE     | NULL    | GPL     |
| mysql_native_password            | ACTIVE | AUTHENTICATION     | NULL    | GPL     |
| sha256_password                  | ACTIVE | AUTHENTICATION     | NULL    | GPL     |
| caching_sha2_password            | ACTIVE | AUTHENTICATION     | NULL    | GPL     |
| daemon_keyring_proxy_plugin      | ACTIVE | DAEMON             | NULL    | GPL     |
| CSV                              | ACTIVE | STORAGE ENGINE     | NULL    | GPL     |
| MEMORY                           | ACTIVE | STORAGE ENGINE     | NULL    | GPL     |
| InnoDB                           | ACTIVE | STORAGE ENGINE     | NULL    | GPL     |
| INNODB_TRX                       | ACTIVE | INFORMATION SCHEMA | NULL    | GPL     |
| INNODB_CMP                       | ACTIVE | INFORMATION SCHEMA | NULL    | GPL     |

...

| INNODB_SESSION_TEMP_TABLESPACES  | ACTIVE | INFORMATION SCHEMA | NULL    | GPL     |
| MyISAM                           | ACTIVE | STORAGE ENGINE     | NULL    | GPL     |
| MRG_MYISAM                       | ACTIVE | STORAGE ENGINE     | NULL    | GPL     |
| PERFORMANCE_SCHEMA               | ACTIVE | STORAGE ENGINE     | NULL    | GPL     |
| TempTable                        | ACTIVE | STORAGE ENGINE     | NULL    | GPL     |
| ARCHIVE                          | ACTIVE | STORAGE ENGINE     | NULL    | GPL     |
| BLACKHOLE                        | ACTIVE | STORAGE ENGINE     | NULL    | GPL     |
| ndbcluster                       | ACTIVE | STORAGE ENGINE     | NULL    | GPL     |
| ndbinfo                          | ACTIVE | STORAGE ENGINE     | NULL    | GPL     |
| ndb_transid_mysql_connection_map | ACTIVE | INFORMATION SCHEMA | NULL    | GPL     |
| ngram                            | ACTIVE | FTPARSER           | NULL    | GPL     |
| mysqlx_cache_cleaner             | ACTIVE | AUDIT              | NULL    | GPL     |
| mysqlx                           | ACTIVE | DAEMON             | NULL    | GPL     |
+----------------------------------+--------+--------------------+---------+---------+
47 rows in set (0.01 sec)
```

The plugin is enabled by default. You can disable it (or force the server not to run unless the plugin starts) by starting the server with the [`--ndb-transid-mysql-connection-map`](mysql-cluster-options-variables.md) option. If the plugin is disabled, the status is shown by [`SHOW PLUGINS`](show-plugins.md) as `DISABLED`. The plugin cannot be enabled or disabled at runtime.

Although the names of this table and its columns are displayed using lowercase, you can use uppercase or lowercase when referring to them in SQL statements.

For this table to be created, the MySQL Server must be a binary supplied with the NDB Cluster distribution, or one built from the NDB Cluster sources with [`NDB`](mysql-cluster.md) storage engine support enabled. It is not available in the standard MySQL 26.7 Server.