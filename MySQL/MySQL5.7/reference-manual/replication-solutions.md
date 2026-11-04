---
title: "16.3 Replication Solutions"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/replication-solutions.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

Replication can be used in many different environments for a range of purposes. This section provides general notes and advice on using replication for specific solution types.

For information on using replication in a backup environment, including notes on the setup, backup procedure, and files to back up, see [Section 16.3.1, “Using Replication for Backups”](replication-solutions-backups.md).

For advice and tips on using different storage engines on the source and replicas, see [Section 16.3.3, “Using Replication with Different Source and Replica Storage Engines”](replication-solutions-diffengines.md).

Using replication as a scale-out solution requires some changes in the logic and operation of applications that use the solution. See [Section 16.3.4, “Using Replication for Scale-Out”](replication-solutions-scaleout.md).

For performance or data distribution reasons, you may want to replicate different databases to different replicas. See [Section 16.3.5, “Replicating Different Databases to Different Replicas”](replication-solutions-partitioning.md)

As the number of replicas increases, the load on the source can increase and lead to reduced performance (because of the need to replicate the binary log to each replica). For tips on improving your replication performance, including using a single secondary server as a replication source server, see [Section 16.3.6, “Improving Replication Performance”](replication-solutions-performance.md).

For guidance on switching sources, or converting replicas into sources as part of an emergency failover solution, see [Section 16.3.7, “Switching Sources During Failover”](replication-solutions-switch.md).

To secure your replication communication, you can encrypt the communication channel. For step-by-step instructions, see [Section 16.3.8, “Setting Up Replication to Use Encrypted Connections”](replication-encrypted-connections.md).