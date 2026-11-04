---
title: "21.7.1 NDB Cluster Replication: Abbreviations and Symbols"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/mysql-cluster-replication-abbreviations.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 21.7.1 NDB Cluster Replication: Abbreviations and Symbols

Throughout this section, we use the following abbreviations or symbols for referring to the source and replica clusters, and to processes and commands run on the clusters or cluster nodes:

**Table 21.63 Abbreviations used throughout this section referring to source and replica clusters, and to processes and commands run on cluster nodes**

| Symbol or Abbreviation | Description (Refers to...) |
| --- | --- |
| *`S`* | The cluster serving as the (primary) replication source |
| *`R`* | The cluster acting as the (primary) replica |
| ``shell*`S`*>`` | Shell command to be issued on the source cluster |
| ``mysql*`S`*>`` | MySQL client command issued on a single MySQL server running as an SQL node on the source cluster |
| ``mysql*`S*`*>`` | MySQL client command to be issued on all SQL nodes participating in the replication source cluster |
| ``shell*`R`*>`` | Shell command to be issued on the replica cluster |
| ``mysql*`R`*>`` | MySQL client command issued on a single MySQL server running as an SQL node on the replica cluster |
| ``mysql*`R*`*>`` | MySQL client command to be issued on all SQL nodes participating in the replica cluster |
| *`C`* | Primary replication channel |
| *`C'`* | Secondary replication channel |
| *`S'`* | Secondary replication source |
| *`R'`* | Secondary replica |