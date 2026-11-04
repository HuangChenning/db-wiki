---
title: "16.1.6 Replication and Binary Logging Options and Variables"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/replication-options.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 16.1.6 Replication and Binary Logging Options and Variables

The following sections contain information about [**mysqld**](mysqld.md) options and server variables that are used in replication and for controlling the binary log. Options and variables for use on sources and replicas are covered separately, as are options and variables relating to binary logging and global transaction identifiers (GTIDs). A set of quick-reference tables providing basic information about these options and variables is also included.

Of particular importance is the `server_id` system variable.

| Command-Line Format | `--server-id=#` |
| --- | --- |
| System Variable | `server_id` |
| Scope | Global |
| Dynamic | Yes |
| Type | Integer |
| Default Value | `0` |
| Minimum Value | `0` |
| Maximum Value | `4294967295` |

This variable specifies the server ID. In MySQL 5.7, `server_id` must be specified if binary logging is enabled, otherwise the server is not allowed to start.

`server_id` is set to 0 by default. On a replication source server and each replica, you *must* specify `server_id` to establish a unique replication ID in the range from 1 to 2 <sup>32</sup> − 1. “Unique”, means that each ID must be different from every other ID in use by any other source or replica in the replication topology. For additional information, see [Section 16.1.6.2, “Replication Source Options and Variables”](replication-options-source.md), and [Section 16.1.6.3, “Replica Server Options and Variables”](replication-options-replica.md).

If the server ID is set to 0, binary logging takes place, but a source with a server ID of 0 refuses any connections from replicas, and a replica with a server ID of 0 refuses to connect to a source. Note that although you can change the server ID dynamically to a nonzero value, doing so does not enable replication to start immediately. You must change the server ID and then restart the server to initialize the replica.

For more information, see [Section 16.1.2.5.1, “Setting the Replica Configuration”](replication-setup-replicas.md).

`server_uuid`

In MySQL 5.7, the server generates a true UUID in addition to the `server_id` value supplied by the user. This is available as the global, read-only `server_uuid` system variable.

Note

The presence of the `server_uuid` system variable in MySQL 5.7 does not change the requirement for setting a unique `server_id` value for each MySQL server as part of preparing and running MySQL replication, as described earlier in this section.

| System Variable | `server_uuid` |
| --- | --- |
| Scope | Global |
| Dynamic | No |
| Type | String |

When starting, the MySQL server automatically obtains a UUID as follows:

1. Attempt to read and use the UUID written in the file ``*`data_dir`*/auto.cnf`` (where *`data_dir`* is the server's data directory).
2. If ``*`data_dir`*/auto.cnf`` is not found, generate a new UUID and save it to this file, creating the file if necessary.

The `auto.cnf` file has a format similar to that used for `my.cnf` or `my.ini` files. In MySQL 5.7, `auto.cnf` has only a single `[auto]` section containing a single `server_uuid` setting and value; the file's contents appear similar to what is shown here:

```
[auto]
server_uuid=8a94f357-aab4-11df-86ab-c80aa9429562
```

Important

The `auto.cnf` file is automatically generated; do not attempt to write or modify this file.

When using MySQL replication, sources and replicas know each other's UUIDs. The value of a replica's UUID can be seen in the output of [`SHOW SLAVE HOSTS`](show-slave-hosts.md). Once [`START SLAVE`](start-slave.md) has been executed, the value of the source's UUID is available on the replica in the output of [`SHOW SLAVE STATUS`](show-slave-status.md).

Note

Issuing a [`STOP SLAVE`](stop-slave.md) or [`RESET SLAVE`](reset-slave.md) statement does *not* reset the source's UUID as used on the replica.

A server's `server_uuid` is also used in GTIDs for transactions originating on that server. For more information, see [Section 16.1.3, “Replication with Global Transaction Identifiers”](replication-gtids.md).

When starting, the replication I/O thread generates an error and aborts if its source's UUID is equal to its own unless the [`--replicate-same-server-id`](replication-options-replica.md) option has been set. In addition, the replication I/O thread generates a warning if either of the following is true:

- No source having the expected `server_uuid` exists.
- The source's `server_uuid` has changed, although no [`CHANGE MASTER         TO`](change-master-to.md) statement has ever been executed.