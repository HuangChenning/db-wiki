---
title: "17.6.3 Group Replication and Virtual Private Networks (VPNs)"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/group-replication-virtual-private-networks-vpn.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 17.6.3 Group Replication and Virtual Private Networks (VPNs)

There is nothing preventing Group Replication from operating over a virtual private network. At its core, it just relies on an IPv4 socket to establish connections between servers for the purpose of propagating messages between them.