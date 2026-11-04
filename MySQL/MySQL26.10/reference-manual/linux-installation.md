---
title: "MySQL :: MySQL 26.10 Reference Manual :: 2.5 Installing MySQL on Linux"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/linux-installation.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

## 2.5 Installing MySQL on Linux

Linux supports a number of different solutions for installing MySQL. We recommend that you use one of the distributions from Oracle, for which several methods for installation are available:

**Table 2.9 Linux Installation Methods and Information**

| Type | Setup Method | Additional Information |
| --- | --- | --- |
| Apt | Enable the [MySQL Apt repository](https://dev.mysql.com/downloads/repo/apt/) | [Documentation](linux-installation-apt-repo.md) |
| Yum | Enable the [MySQL Yum repository](https://dev.mysql.com/downloads/repo/yum/) | [Documentation](linux-installation-yum-repo.md) |
| Zypper | Enable the [MySQL SLES repository](https://dev.mysql.com/downloads/repo/suse/) | [Documentation](linux-installation-sles-repo.md) |
| RPM | [Download](https://dev.mysql.com/downloads/mysql/) a specific package | [Documentation](linux-installation-rpm.md) |
| DEB | [Download](https://dev.mysql.com/downloads/mysql/) a specific package | [Documentation](linux-installation-debian.md) |
| Generic | [Download](https://dev.mysql.com/downloads/mysql/) a generic package | [Documentation](binary-installation.md) |
| Source | Compile from [source](https://dev.mysql.com/downloads/mysql/) | [Documentation](source-installation.md) |
| Docker | Use the [Oracle Container Registry](https://container-registry.oracle.com/). You can also use [My Oracle Support](https://support.oracle.com/) for the MySQL Enterprise Edition. | [Documentation](linux-installation-docker.md) |
| Oracle Unbreakable Linux Network | Use ULN channels | [Documentation](uln-installation.md) |

As an alternative, you can use the package manager on your system to automatically download and install MySQL with packages from the native software repositories of your Linux distribution. These native packages are often several versions behind the currently available release. You are also normally unable to install innovation releases, since these are not usually made available in the native repositories. For more information on using the native package installers, see [Section 2.5.7, “Installing MySQL on Linux from the Native Software Repositories”](linux-installation-native.md).

Note

For many Linux installations, you want to set up MySQL to be started automatically when your machine starts. Many of the native package installations perform this operation for you, but for source, binary and RPM solutions you may need to set this up separately. The required script, [**mysql.server**](mysql-server.md), can be found in the `support-files` directory under the MySQL installation directory or in a MySQL source tree. You can install it as `/etc/init.d/mysql` for automatic MySQL startup and shutdown. See [Section 6.3.3, “mysql.server — MySQL Server Startup Script”](mysql-server.md).