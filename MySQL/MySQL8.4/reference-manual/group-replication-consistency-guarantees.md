---
title: "20.5.3 Transaction Consistency Guarantees"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/group-replication-consistency-guarantees.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

### 20.5.3 Transaction Consistency Guarantees

One of the major implications of a distributed system such as Group Replication is the consistency guarantees that it provides as a group. In other words, the consistency of the global synchronization of transactions distributed across the members of the group. This section describes how Group Replication handles consistency guarantees depending on the events that occur in a group, and how to best configure your group's consistency guarantees.