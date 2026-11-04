---
title: "17.9.5 Distributed Recovery"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/group-replication-distributed-recovery.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 17.9.5 Distributed Recovery

This section describes the process through which a member joining a group catches up with the remaining servers in the group, called distributed recovery. Distributed recovery can be summarized as the process through which a server gets missing transactions from the group so that it can then join the group having processed the same set of transactions as the other group members.