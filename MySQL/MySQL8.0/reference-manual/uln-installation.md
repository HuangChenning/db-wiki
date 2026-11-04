---
title: "2.6 Installing MySQL Using Unbreakable Linux Network (ULN)"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/uln-installation.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

Linux supports a number of different solutions for installing MySQL, covered in [Section 2.5, “Installing MySQL on Linux”](linux-installation.md). One of the methods, covered in this section, is installing from Oracle's Unbreakable Linux Network (ULN). You can find information about Oracle Linux and ULN under [http://linux.oracle.com/](http://linux.oracle.com/).

To use ULN, you need to obtain a ULN login and register the machine used for installation with ULN. This is described in detail in the [ULN FAQ](https://linux.oracle.com/uln_faq.html). The page also describes how to install and update packages.

Both Community and Commercial packages are supported, and each offers three MySQL channels:

- `Server`: MySQL Server
- `Connectors`: MySQL Connector/C++, MySQL Connector/J, MySQL Connector/ODBC, and MySQL Connector/Python.
- `Tools`: MySQL Router, MySQL Shell, and MySQL Workbench

The Community channels are available to all ULN users.

Accessing commercial MySQL ULN packages at oracle.linux.com requires you to provide a CSI with a valid commercial license for MySQL (Enterprise or Standard). As of this writing, valid purchases are 60944, 60945, 64911, and 64912. The appropriate CSI makes commercial MySQL subscription channels available in your ULN GUI interface.

Once MySQL has been installed using ULN, you can find information on starting and stopping the server, and more, at [Section 2.5.7, “Installing MySQL on Linux from the Native Software Repositories”](linux-installation-native.md), particularly under [Section 2.5.4, “Installing MySQL on Linux Using RPM Packages from Oracle”](linux-installation-rpm.md).

If you are changing your package source to use ULN and not changing which build of MySQL you are using, then back up your data, remove your existing binaries, and replace them with those from ULN. If a change of build is involved, we recommend the backup be a dump ([**mysqldump**](mysqldump.md) or [**mysqlpump**](mysqlpump.md) or from [MySQL Shell's backup utility](https://docs.oracle.com/cd/E17952_01/mysql-shell-8.0-en/mysql-shell-utilities-dump-instance-schema.html)) just in case you need to rebuild your data after the new binaries are in place. If this shift to ULN crosses a version boundary, consult this section before proceeding: [Chapter 3, *Upgrading MySQL*](upgrading.md).

Note

Oracle Linux 8 is supported as of MySQL 8.0.17, and the community Tools and Connectors channels were added with the MySQL 8.0.24 release.