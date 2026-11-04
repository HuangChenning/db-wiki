---
title: "2.8.1 Source Installation Methods"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/source-installation-methods.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

### 2.8.1 Source Installation Methods

There are two methods for installing MySQL from source:

- Use a standard MySQL source distribution. To obtain a standard distribution, see [Section 2.1.3, “How to Get MySQL”](getting-mysql.md). For instructions on building from a standard distribution, see [Section 2.8.4, “Installing MySQL Using a Standard Source Distribution”](installing-source-distribution.md).
	Standard distributions are available as compressed **tar** files, Zip archives, or RPM packages. Distribution files have names of the form ``mysql-*`VERSION`*.tar.gz``, ``mysql-*`VERSION`*.zip``, or ``mysql-*`VERSION`*.rpm``, where *`VERSION`* is a number like `9.7.0`. File names for source distributions can be distinguished from those for precompiled binary distributions in that source distribution names are generic and include no platform name, whereas binary distribution names include a platform name indicating the type of system for which the distribution is intended (for example, `pc-linux-i686` or `winx64`).
- Use a MySQL development tree. For information on building from one of the development trees, see [Section 2.8.5, “Installing MySQL Using a Development Source Tree”](installing-development-tree.md).