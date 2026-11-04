---
title: "17.21.2 Troubleshooting Recovery Failures"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/innodb-troubleshooting-recovery.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 17.21.2 Troubleshooting Recovery Failures

From MySQL 8.0.26, checkpoints and advancing the checkpoint LSN are not permitted until redo log recovery is complete and data dictionary dynamic metadata (`srv_dict_metadata`) is transferred to data dictionary table (`dict_table_t`) objects. Should the redo log run out of space during recovery or after recovery (but before data dictionary dynamic metadata is transferred to data dictionary table objects) as a result of this change, an [`innodb_force_recovery`](innodb-parameters.md) restart may be required, starting with at least the `SRV_FORCE_NO_IBUF_MERGE` setting or, in case that fails, the `SRV_FORCE_NO_LOG_REDO` setting. If an [`innodb_force_recovery`](innodb-parameters.md) restart fails in this scenario, recovery from backup may be necessary. (Bug #32200595)