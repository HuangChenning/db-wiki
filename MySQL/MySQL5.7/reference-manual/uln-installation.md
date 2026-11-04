---
title: "2.6 Installing MySQL Using Unbreakable Linux Network (ULN)"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/uln-installation.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

Linux supports a number of different solutions for installing MySQL, covered in [Section 2.5, “Installing MySQL on Linux”](linux-installation.md). One of the methods, covered in this section, is installing from Oracle's Unbreakable Linux Network (ULN). You can find information about Oracle Linux and ULN under [http://linux.oracle.com/](http://linux.oracle.com/).

To use ULN, you need to obtain a ULN login and register the machine used for installation with ULN. This is described in detail in the [ULN FAQ](https://linux.oracle.com/uln_faq.html). The page also describes how to install and update packages. The MySQL packages are in the “MySQL for Oracle Linux 6” and “MySQL for Oracle Linux 7” channels for your system architecture on ULN.

Note

ULN provides MySQL 5.7 for Oracle Linux 6 and Oracle Linux 7. Alternatively, Oracle Linux 8 supports MySQL 8.0. In addition, Enterprise packages are available as of MySQL 8.0.21.

Once MySQL has been installed using ULN, you can find information on starting and stopping the server, and more, in [this section](linux-installation-native.md), particularly under [Section 2.5.5, “Installing MySQL on Linux Using RPM Packages from Oracle”](linux-installation-rpm.md).

If you are changing your package source to use ULN and not changing which build of MySQL you are using, then back up your data, remove your existing binaries, and replace them with those from ULN. If a change of build is involved, we recommend the backup be a dump ([**mysqldump**](mysqldump.md) or [**mysqlpump**](mysqlpump.md) or from [MySQL Shell's backup utility](https://docs.oracle.com/cd/E17952_01/mysql-shell-8.0-en/mysql-shell-utilities-dump-instance-schema.html)) just in case you need to rebuild your data after the new binaries are in place. If this shift to ULN crosses a version boundary, consult this section before proceeding: [Section 2.10, “Upgrading MySQL”](upgrading.md).