---
title: "7.8.2 Running Multiple MySQL Instances on Windows"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/multiple-windows-servers.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 7.8.2 Running Multiple MySQL Instances on Windows

You can run multiple servers on Windows by starting them manually from the command line, each with appropriate operating parameters, or by installing several servers as Windows services and running them that way. General instructions for running MySQL from the command line or as a service are given in [Section 2.3, “Installing MySQL on Microsoft Windows”](windows-installation.md). The following sections describe how to start each server with different values for those options that must be unique per server, such as the data directory. These options are listed in [Section 7.8, “Running Multiple MySQL Instances on One Machine”](multiple-servers.md).