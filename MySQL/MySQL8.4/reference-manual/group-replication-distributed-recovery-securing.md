---
title: "20.6.3 Securing Distributed Recovery Connections"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/group-replication-distributed-recovery-securing.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

### 20.6.3 Securing Distributed Recovery Connections

Important

When using the MySQL communication stack ([`group_replication_communication_stack=MYSQL`](group-replication-system-variables.md)) AND secure connections between members ([`group_replication_ssl_mode`](group-replication-system-variables.md) is not set to `DISABLED`), the security settings discussed in this section are applied not just to distributed recovery connections, but to group communications between members in general.

When a member joins the group, distributed recovery is carried out using a combination of a remote cloning operation, if available and appropriate, and an asynchronous replication connection. For a full description of distributed recovery, see [Section 20.5.4, “Distributed Recovery”](group-replication-distributed-recovery.md).

Group members offer their standard SQL client connection to joining members for distributed recovery, as specified by MySQL Server's [`hostname`](server-system-variables.md) and [`port`](server-system-variables.md) system variables, and may (also) advertise an alternative list of distributed recovery endpoints as dedicated client connections for joining members. For more details, see [Section 20.5.4.1, “Connections for Distributed Recovery”](group-replication-distributed-recovery-connections.md). Notice that such connections offered to a joining member for distributed recovery is *not* the same connections that are used by Group Replication for communication between online members when the XCom communication stack is used for group communications ([`group_replication_communication_stack=XCOM`](group-replication-system-variables.md)).

To secure distributed recovery connections in the group, ensure that user credentials for the replication user are properly secured, and use SSL for distributed recovery connections if possible.