---
title: "2.7 Installing MySQL on Solaris"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/solaris-installation.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

Note

MySQL 5.7 supports Solaris 11 (Update 3 and later).

MySQL on Solaris is available in a number of different formats.

- For information on installing using the native Solaris PKG format, see [Section 2.7.1, “Installing MySQL on Solaris Using a Solaris PKG”](solaris-installation-pkg.md).
- To use a standard `tar` binary installation, use the notes provided in [Section 2.2, “Installing MySQL on Unix/Linux Using Generic Binaries”](binary-installation.md). Check the notes and hints at the end of this section for Solaris specific notes that you may need before or after installation.

Important

The installation packages have a dependency on the Oracle Developer Studio 12.5 Runtime Libraries, which must be installed before you run the MySQL installation package. See the download options for Oracle Developer Studio [here](http://www.oracle.com/technetwork/server-storage/developerstudio/downloads/index.html). The installation package enables you to install the runtime libraries only instead of the full Oracle Developer Studio; see instructions in [Installing Only the Runtime Libraries on Oracle Solaris 11](https://docs.oracle.com/cd/E60778_01/html/E60743/gozsu.html).

To obtain a binary MySQL distribution for Solaris in tarball or PKG format, [https://dev.mysql.com/downloads/mysql/5.7.html](https://dev.mysql.com/downloads/mysql/5.7.html).

Additional notes to be aware of when installing and using MySQL on Solaris:

- If you want to use MySQL with the `mysql` user and group, use the **groupadd** and **useradd** commands:
	```
	groupadd mysql
	useradd -g mysql -s /bin/false mysql
	```
- If you install MySQL using a binary tarball distribution on Solaris, because the Solaris **tar** cannot handle long file names, use GNU **tar** (**gtar**) to unpack the distribution. If you do not have GNU **tar** on your system, install it with the following command:
	```
	pkg install archiver/gnu-tar
	```
- You should mount any file systems on which you intend to store `InnoDB` files with the `forcedirectio` option. (By default mounting is done without this option.) Failing to do so causes a significant drop in performance when using the `InnoDB` storage engine on this platform.
- If you would like MySQL to start automatically, you can copy `support-files/mysql.server` to `/etc/init.d` and create a symbolic link to it named `/etc/rc3.d/S99mysql.server`.
- If too many processes try to connect very rapidly to [**mysqld**](mysqld.md), you should see this error in the MySQL log:
	```
	Error in accept: Protocol error
	```
	You might try starting the server with the [`--back_log=50`](server-system-variables.md) option as a workaround for this.
- To configure the generation of core files on Solaris you should use the **coreadm** command. Because of the security implications of generating a core on a `setuid()` application, by default, Solaris does not support core files on `setuid()` programs. However, you can modify this behavior using **coreadm**. If you enable `setuid()` core files for the current user, they are generated using mode 600, and are owned by the superuser.