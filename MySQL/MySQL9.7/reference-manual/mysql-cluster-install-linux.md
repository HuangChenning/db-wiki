---
title: "25.3.1 Installation of NDB Cluster on Linux"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/mysql-cluster-install-linux.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

### 25.3.1 Installation of NDB Cluster on Linux

This section covers installation methods for NDB Cluster on Linux and other Unix-like operating systems. While the next few sections refer to a Linux operating system, the instructions and procedures given there should be easily adaptable to other supported Unix-like platforms. For manual installation and setup instructions specific to Windows systems, see [Section 25.3.2, “Installing NDB Cluster on Windows”](mysql-cluster-install-windows.md).

Each NDB Cluster host computer must have the correct executable programs installed. A host running an SQL node must have installed on it a MySQL Server binary ([**mysqld**](mysqld.md)). Management nodes require the management server daemon ([**ndb\_mgmd**](mysql-cluster-programs-ndb-mgmd.md)); data nodes require the data node daemon ([**ndbd**](mysql-cluster-programs-ndbd.md) or [**ndbmtd**](mysql-cluster-programs-ndbmtd.md)). It is not necessary to install the MySQL Server binary on management node hosts and data node hosts. It is recommended that you also install the management client ([**ndb\_mgm**](mysql-cluster-programs-ndb-mgm.md)) on the management server host.

Installation of NDB Cluster on Linux can be done using precompiled binaries from Oracle (downloaded as a.tar.gz archive), with RPM packages (also available from Oracle), or from source code. All three of these installation methods are described in the section that follow.

Regardless of the method used, it is still necessary following installation of the NDB Cluster binaries to create configuration files for all cluster nodes, before you can start the cluster. See [Section 25.3.3, “Initial Configuration of NDB Cluster”](mysql-cluster-install-configuration.md).