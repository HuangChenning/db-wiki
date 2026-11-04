---
title: "Chapter 2 Installing MySQL Enterprise Backup"
book: "MySQL Enterprise Backup User's Guide (Version 9.7.0)"
version: "9.7"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/9.7/en/installing.html"
tags:
  - mysql
  - mysql-9.7
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 9.7.0)

Install MySQL Enterprise Backup on each database server whose contents you intend to back up. Typically, you perform all backup and restore operations locally, by running **mysqlbackup** on the same server as the MySQL instance.

MySQL Enterprise Backup is packaged as either an archive file (`.tgz`, archived with `tar` and compressed with `gzip`) or as a platform-specific installer.

## Installing on Unix and Linux Systems

For all Linux and Unix systems, the product is available as a `.tgz` file. Unpack this file as follows:

```
tar xvzf package.tgz
```

**mysqlbackup** is unpacked into a subdirectory. You can either copy them into a system directory (preserving their execute permission bits), or add to your `$PATH` setting the directory where you unpacked it.

For certain Linux distributions, the product is also available as an RPM archive. When you install the RPM using the command ``sudo rpm -i     *`package_name`*.rpm``, the **mysqlbackup** client is installed in the directory `/usr/bin/mysqlbackup`.

Installation packages for Debian and Ubuntu platforms are also available. Install the package with the following command ``sudo dpkg -i     *`package_name`*.deb``.

## Installing on Windows Systems

The product can be installed together with other MySQL products with the MySQL Installer for Windows. It can also be installed separately with either an individual `.msi` installer or `.zip` file.

When installing with a `.msi` installer, specify the installation location, preferably under the same directory where other MySQL products have been installed. Choose the option Include directory in Windows PATH, so that you can run **mysqlbackup** from any directory.

When installing with a `.zip` file, simply unzip the file and put `mysqlbackup.exe` at the desired installation location. You can add that location to the `%PATH%` variable, so that you can run the **mysqlbackup** client from any directory.

Verify the installation by selecting the menu item Start > Programs > MySQL Enterprise Backup 9.7 > MySQL Enterprise Backup Command Line. The menu item displays version information and opens a command prompt for running the **mysqlbackup** command.