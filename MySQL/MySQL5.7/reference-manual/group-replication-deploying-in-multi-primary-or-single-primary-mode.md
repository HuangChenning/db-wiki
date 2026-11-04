---
title: "17.5.1 Deploying in Multi-Primary or Single-Primary Mode"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/group-replication-deploying-in-multi-primary-or-single-primary-mode.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 17.5.1 Deploying in Multi-Primary or Single-Primary Mode

Group Replication operates in the following different modes:

The default mode is single-primary. It is not possible to have members of the group deployed in different modes, for example one configured in multi-primary mode while another one is in single-primary mode. To switch between modes, the group and not the server, needs to be restarted with a different operating configuration. Regardless of the deployed mode, Group Replication does not handle client-side fail-over, that must be handled by the application itself, a connector or a middleware framework such as a proxy or [MySQL Router 8.0](https://docs.oracle.com/cd/E17952_01/mysql-router-8.0-en/).

When deployed in multi-primary mode, statements are checked to ensure they are compatible with the mode. The following checks are made when Group Replication is deployed in multi-primary mode:

- If a transaction is executed under the SERIALIZABLE isolation level, then its commit fails when synchronizing itself with the group.
- If a transaction executes against a table that has foreign keys with cascading constraints, then the transaction fails to commit when synchronizing itself with the group.

These checks can be deactivated by setting the option [`group_replication_enforce_update_everywhere_checks`](group-replication-system-variables.md) to `FALSE`. When deploying in single-primary mode, this option *must* be set to `FALSE`.