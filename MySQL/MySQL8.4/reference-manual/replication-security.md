---
title: "19.3 Replication Security"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/replication-security.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

To protect against unauthorized access to data that is stored on and transferred between replication source servers and replicas, set up all the servers involved using the security measures that you would choose for any MySQL instance in your installation, as described in [Chapter 8, *Security*](security.md). In addition, for servers in a replication topology, consider implementing the following security measures:

- Set up sources and replicas to use encrypted connections to transfer the binary log, which protects this data in motion. Encryption for these connections must be activated using a [`CHANGE REPLICATION SOURCE TO`](change-replication-source-to.md) statement, in addition to setting up the servers to support encrypted network connections. See [Section 19.3.1, “Setting Up Replication to Use Encrypted Connections”](replication-encrypted-connections.md).
- Encrypt the binary log files and relay log files on sources and replicas, which protects this data at rest, and also any data in use in the binary log cache. Binary log encryption is activated using the [`binlog_encryption`](replication-options-binary-log.md) system variable. See [Section 19.3.2, “Encrypting Binary Log Files and Relay Log Files”](replication-binlog-encryption.md).
- Apply privilege checks to replication appliers, which help to secure replication channels against the unauthorized or accidental use of privileged or unwanted operations. Privilege checks are implemented by setting up a `PRIVILEGE_CHECKS_USER` account, which MySQL uses to verify that you have authorized each specific transaction for that channel. See [Section 19.3.3, “Replication Privilege Checks”](replication-privilege-checks.md).

For Group Replication, binary log encryption and privilege checks can be used as a security measure on replication group members. You should also consider encrypting the connections between group members, comprising group communication connections and distributed recovery connections, and applying IP address allowlisting to exclude untrusted hosts. For information on these security measures specific to Group Replication, see [Section 20.6, “Group Replication Security”](group-replication-security.md).