---
title: "MySQL :: MySQL 26.10 Reference Manual :: 19.1 Configuring Replication"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/replication-configuration.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

## 19.1 Configuring Replication

This section describes how to configure the different types of replication available in MySQL and includes the setup and configuration required for a replication environment, including step-by-step instructions for creating a new replication environment. The major components of this section are:

- For a guide to setting up two or more servers for replication using binary log file positions, [Section 19.1.2, “Setting Up Binary Log File Position Based Replication”](replication-howto.md), deals with the configuration of the servers and provides methods for copying data between the source and replicas.
- For a guide to setting up two or more servers for replication using GTID transactions, [Section 19.1.3, “Replication with Global Transaction Identifiers”](replication-gtids.md), deals with the configuration of the servers.
- Events in the binary log are recorded using a number of formats. These are referred to as statement-based replication (SBR) or row-based replication (RBR). A third type, mixed-format replication (MIXED), uses SBR or RBR replication automatically to take advantage of the benefits of both SBR and RBR formats when appropriate. The different formats are discussed in [Section 19.2.1, “Replication Formats”](replication-formats.md).
- Detailed information on the different configuration options and variables that apply to replication is provided in [Section 19.1.6, “Replication and Binary Logging Options and Variables”](replication-options.md).
- Once started, the replication process should require little administration or monitoring. However, for advice on common tasks that you may want to execute, see [Section 19.1.7, “Common Replication Administration Tasks”](replication-administration.md).