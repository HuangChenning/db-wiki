---
title: "17.7.2 Group Replication Status Variables"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/group-replication-status-variables.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 17.7.2 Group Replication Status Variables

MySQL 5.7 supports one status variable providing information about Group Replication. This variable is described here:

- [`group_replication_primary_member`](server-status-variables.md)
	Shows the primary member's UUID when the group is operating in single-primary mode. If the group is operating in multi-primary mode, shows an empty string. See [Section 17.5.1.3, “Finding the Primary”](group-replication-find-primary.md).