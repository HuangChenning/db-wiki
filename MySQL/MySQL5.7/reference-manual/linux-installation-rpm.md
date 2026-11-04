---
title: "2.5.5 Installing MySQL on Linux Using RPM Packages from Oracle"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/linux-installation-rpm.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 2.5.5 Installing MySQL on Linux Using RPM Packages from Oracle

The recommended way to install MySQL on RPM-based Linux distributions is by using the RPM packages provided by Oracle. There are two sources for obtaining them, for the Community Edition of MySQL:

- From the MySQL software repositories:
	- The MySQL Yum repository (see [Section 2.5.1, “Installing MySQL on Linux Using the MySQL Yum Repository”](linux-installation-yum-repo.md) for details).
	- The MySQL SLES repository (see [Section 2.5.4, “Installing MySQL on Linux Using the MySQL SLES Repository”](linux-installation-sles-repo.md) for details).
- From the [Download MySQL Community Server](https://dev.mysql.com/downloads/mysql/) page in the [MySQL Developer Zone](https://dev.mysql.com/).

Note

RPM distributions of MySQL are also provided by other vendors. Be aware that they may differ from those built by Oracle in features, capabilities, and conventions (including communication setup), and that the installation instructions in this manual do not necessarily apply to them. The vendor's instructions should be consulted instead.

If you have such a third-party distribution of MySQL running on your system and now want to migrate to Oracle's distribution using the RPM packages downloaded from the MySQL Developer Zone, see Compatibility with RPM Packages from Other Vendors below. The preferred method of migration, however, is to use the [MySQL Yum repository](linux-installation-yum-repo.md) or [MySQL SLES repository](linux-installation-sles-repo.md).

RPM packages for MySQL are listed in the following tables:

**Table 2.9 RPM Packages for MySQL Community Edition**

| Package Name | Summary |
| --- | --- |
| `mysql-community-server` | Database server and related tools |
| `mysql-community-client` | MySQL client applications and tools |
| `mysql-community-common` | Common files for server and client libraries |
| `mysql-community-devel` | Development header files and libraries for MySQL database client applications |
| `mysql-community-libs` | Shared libraries for MySQL database client applications |
| `mysql-community-libs-compat` | Shared compatibility libraries for previous MySQL installations |
| `mysql-community-embedded` | MySQL embedded library |
| `mysql-community-embedded-devel` | Development header files and libraries for MySQL as an embeddable library |
| `mysql-community-test` | Test suite for the MySQL server |

**Table 2.10 RPM Packages for the MySQL Enterprise Edition**

| Package Name | Summary |
| --- | --- |
| `mysql-commercial-server` | Database server and related tools |
| `mysql-commercial-client` | MySQL client applications and tools |
| `mysql-commercial-common` | Common files for server and client libraries |
| `mysql-commercial-devel` | Development header files and libraries for MySQL database client applications |
| `mysql-commercial-libs` | Shared libraries for MySQL database client applications |
| `mysql-commercial-libs-compat` | Shared compatibility libraries for previous MySQL installations |
| `mysql-commercial-embedded` | MySQL embedded library |
| `mysql-commercial-embedded-devel` | Development header files and libraries for MySQL as an embeddable library |
| `mysql-commercial-test` | Test suite for the MySQL server |

The full names for the RPMs have the following syntax:

```
packagename-version-distribution-arch.rpm
```

The *`distribution`* and *`arch`* values indicate the Linux distribution and the processor type for which the package was built. See the table below for lists of the distribution identifiers:

**Table 2.11 MySQL Linux RPM Package Distribution Identifiers**

| distribution Value | Intended Use |
| --- | --- |
| el *`{version}`* where *`{version}`* is the major Enterprise Linux version, such as `el8` | EL6 (8.0), EL7, EL8, EL9, and EL10-based platforms (for example, the corresponding versions of Oracle Linux, Red Hat Enterprise Linux, and CentOS) |
| `sles12` | SUSE Linux Enterprise Server 12 |

To see all files in an RPM package (for example, `mysql-community-server`), use the following command:

```
$> rpm -qpl mysql-community-server-version-distribution-arch.rpm
```

*The discussion in the rest of this section applies only to an installation process using the RPM packages directly downloaded from Oracle, instead of through a MySQL repository.*

Dependency relationships exist among some of the packages. If you plan to install many of the packages, you may wish to download the RPM bundle **tar** file instead, which contains all the RPM packages listed above, so that you need not download them separately.

In most cases, you need to install the `mysql-community-server`, `mysql-community-client`, `mysql-community-libs`, `mysql-community-common`, and `mysql-community-libs-compat` packages to get a functional, standard MySQL installation. To perform such a standard, basic installation, go to the folder that contains all those packages (and, preferably, no other RPM packages with similar names), and issue the following command for platforms *other than* Red Hat Enterprise Linux/Oracle Linux/CentOS:

```
$> sudo yum install mysql-community-{server,client,common,libs}-*
```

Replace **yum** with **zypper** for SLES.

For Red Hat Enterprise Linux/Oracle Linux/CentOS systems:

```
$> sudo yum install mysql-community-{server,client,common,libs}-* mysql-5.*­
```

While it is much preferable to use a high-level package management tool like **yum** to install the packages, users who prefer direct **rpm** commands can replace the **yum install** command with the **rpm -Uvh** command; however, using **rpm -Uvh** instead makes the installation process more prone to failure, due to potential dependency issues the installation process might run into.

To install only the client programs, you can skip `mysql-community-server` in your list of packages to install; issue the following command for platforms *other than* Red Hat Enterprise Linux/Oracle Linux/CentOS:

```
$> sudo yum install mysql-community-{client,common,libs}-*
```

Replace **yum** with **zypper** for SLES.

For Red Hat Enterprise Linux/Oracle Linux/CentOS systems:

```
$> sudo yum install mysql-community-{client,common,libs}-* mysql-5.*
```

A standard installation of MySQL using the RPM packages result in files and resources created under the system directories, shown in the following table.

**Table 2.12 MySQL Installation Layout for Linux RPM Packages from the MySQL Developer Zone**

| Files or Resources | Location |
| --- | --- |
| Client programs and scripts | `/usr/bin` |
| [**mysqld**](mysqld.md) server | `/usr/sbin` |
| Configuration file | `/etc/my.cnf` |
| Data directory | `/var/lib/mysql` |
| Error log file | For RHEL, Oracle Linux, CentOS or Fedora platforms: `/var/log/mysqld.log`  For SLES: `/var/log/mysql/mysqld.log` |
| Value of [`secure_file_priv`](server-system-variables.md) | `/var/lib/mysql-files` |
| System V init script | For RHEL, Oracle Linux, CentOS or Fedora platforms: `/etc/init.d/mysqld`  For SLES: `/etc/init.d/mysql` |
| Systemd service | For RHEL, Oracle Linux, CentOS or Fedora platforms: `mysqld`  For SLES: `mysql` |
| Pid file | ` /var/run/mysql/mysqld.pid` |
| Socket | `/var/lib/mysql/mysql.sock` |
| Keyring directory | `/var/lib/mysql-keyring` |
| Unix manual pages | `/usr/share/man` |
| Include (header) files | `/usr/include/mysql` |
| Libraries | `/usr/lib/mysql` |
| Miscellaneous support files (for example, error messages, and character set files) | `/usr/share/mysql` |

The installation also creates a user named `mysql` and a group named `mysql` on the system.

Notes

- The `mysql` user is created using the `-r` and `-s /bin/false` options of the `useradd` command, so that it does not have login permissions to your server host (see [Creating the mysql User and Group](https://dev.mysql.com/doc/mysql-secure-deployment-guide/5.7/en/secure-deployment-install.html#secure-deployment-mysql-user) for details). To switch to the `mysql` user on your OS, use the `--shell=/bin/bash` option for the `su` command:
	```
	su - mysql --shell=/bin/bash
	```
- Installation of previous versions of MySQL using older packages might have created a configuration file named `/usr/my.cnf`. It is highly recommended that you examine the contents of the file and migrate the desired settings inside to the file `/etc/my.cnf` file, then remove `/usr/my.cnf`.

MySQL is not automatically started at the end of the installation process. For Red Hat Enterprise Linux, Oracle Linux, CentOS, and Fedora systems, use the following command to start MySQL:

```
$> sudo service mysqld start
```

For SLES systems, the command is the same, but the service name is different:

```
$> sudo service mysql start
```

If the operating system is systemd enabled, standard **service** commands such as **stop**, **start**, **status** and **restart** should be used to manage the MySQL server service. The `mysqld` service is enabled by default, and it starts at system reboot. Notice that certain things might work differently on systemd platforms: for example, changing the location of the data directory might cause issues. See [Section 2.5.10, “Managing MySQL Server with systemd”](using-systemd.md) for additional information.

During an upgrade installation using RPM and DEB packages, if the MySQL server is running when the upgrade occurs then the MySQL server is stopped, the upgrade occurs, and the MySQL server is restarted. One exception: if the edition also changes during an upgrade (such as community to commercial, or vice-versa), then MySQL server is not restarted.

At the initial start up of the server, the following happens, given that the data directory of the server is empty:

- The server is initialized.
- An SSL certificate and key files are generated in the data directory.
- [`validate_password`](validate-password.md) is installed and enabled.
- A superuser account `'root'@'localhost'` is created. A password for the superuser is set and stored in the error log file. To reveal it, use the following command for RHEL, Oracle Linux, CentOS, and Fedora systems:
	```
	$> sudo grep 'temporary password' /var/log/mysqld.log
	```
	Use the following command for SLES systems:
	```
	$> sudo grep 'temporary password' /var/log/mysql/mysqld.log
	```
	The next step is to log in with the generated, temporary password and set a custom password for the superuser account:

```
$> mysql -uroot -p
```
```
mysql> ALTER USER 'root'@'localhost' IDENTIFIED BY 'MyNewPass4!';
```

Note

[`validate_password`](validate-password.md) is installed by default. The default password policy implemented by `validate_password` requires that passwords contain at least one uppercase letter, one lowercase letter, one digit, and one special character, and that the total password length is at least 8 characters.

If something goes wrong during installation, you might find debug information in the error log file `/var/log/mysqld.log`.

For some Linux distributions, it might be necessary to increase the limit on number of file descriptors available to [**mysqld**](mysqld.md). See [Section B.3.2.16, “File Not Found and Similar Errors”](not-enough-file-handles.md)

**Compatibility with RPM Packages from Other Vendors.** If you have installed packages for MySQL from your Linux distribution's local software repository, it is much preferable to install the new, directly-downloaded packages from Oracle using the package management system of your platform (**yum**, **dnf**, or **zypper**), as described above. The command replaces old packages with new ones to ensure compatibility of old applications with the new installation; for example, the old `mysql-libs` package is replaced with the `mysql-community-libs-compat` package, which provides a replacement-compatible client library for applications that were using your older MySQL installation. If there was an older version of `mysql-community-libs-compat` on the system, it also gets replaced.

If you have installed third-party packages for MySQL that are NOT from your Linux distribution's local software repository (for example, packages directly downloaded from a vendor other than Oracle), you should uninstall all those packages before installing the new, directly-downloaded packages from Oracle. This is because conflicts may arise between those vendor's RPM packages and Oracle's: for example, a vendor's convention about which files belong with the server and which belong with the client library may differ from that used for Oracle packages. Attempts to install an Oracle RPM may then result in messages saying that files in the RPM to be installed conflict with files from an installed package.

**Installing Client Libraries from Multiple MySQL Versions.** It is possible to install multiple client library versions, such as for the case that you want to maintain compatibility with older applications linked against previous libraries. To install an older client library, use the `--oldpackage` option with **rpm**. For example, to install `mysql-community-libs-5.5` on an EL6 system that has `libmysqlclient.20` from MySQL 5.7, use a command like this:

```
$> rpm --oldpackage -ivh mysql-community-libs-5.5.50-2.el6.x86_64.rpm
```

**Debug Package.** A special variant of MySQL Server compiled with the [debug package](dbug-package.md) has been included in the server RPM packages. It performs debugging and memory allocation checks and produces a trace file when the server is running. To use that debug version, start MySQL with `/usr/sbin/mysqld-debug`, instead of starting it as a service or with `/usr/sbin/mysqld`. See [Section 5.8.3, “The DBUG Package”](dbug-package.md) for the debug options you can use.

Note

The default plugin directory for debug builds changed from `/usr/lib64/mysql/plugin` to `/usr/lib64/mysql/plugin/debug` in 5.7.21. Previously, it was necessary to change [`plugin_dir`](server-system-variables.md) to `/usr/lib64/mysql/plugin/debug` for debug builds.

**Rebuilding RPMs from source SRPMs.** Source code SRPM packages for MySQL are available for download. They can be used as-is to rebuild the MySQL RPMs with the standard **rpmbuild** tool chain.

**`root` passwords for pre-GA releases.** For MySQL 5.7.4 and 5.7.5, the initial random `root` password is written to the `.mysql_secret` file in the directory named by the `HOME` environment variable. When trying to access the file, bear in mind that depending on operating system, using a command such as **sudo** may cause the value of `HOME` to refer to the home directory of the `root` system user. `.mysql_secret` is created with mode 600 to be accessible only to the system user for whom it is created. Before MySQL 5.7.4, the accounts (including `root`) created in the MySQL grant tables for an RPM installation initially have no passwords; after starting the server, you should assign passwords to them using the instructions in [Section 2.9, “Postinstallation Setup and Testing”](postinstallation.md)."