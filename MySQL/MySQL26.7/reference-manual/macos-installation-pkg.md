---
title: "MySQL :: MySQL 26.7 Reference Manual :: 2.4.2 Installing MySQL on macOS Using Native Packages"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/macos-installation-pkg.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

### 2.4.2 Installing MySQL on macOS Using Native Packages

The package is located inside a disk image (`.dmg`) file that you first need to mount by double-clicking its icon in the Finder. It should then mount the image and display its contents.

Note

Before proceeding with the installation, be sure to stop all running MySQL server instances by using either the MySQL Manager Application (on macOS Server), the preference pane, or [**mysqladmin shutdown**](mysqladmin.md) on the command line.

To install MySQL using the package installer:

1. Download the disk image (`.dmg`) file (the community version is available [here](https://dev.mysql.com/downloads/mysql/)) that contains the MySQL package installer. Double-click the file to mount the disk image and see its contents.
	Double-click the MySQL installer package from the disk. It is named according to the version of MySQL you have downloaded. For example, for MySQL server 26.7.0 it might be named ``mysql-26.7.0-macos-*`10.13-x86_64`*.pkg``.
2. The initial wizard introduction screen references the MySQL server version to install. Click Continue to begin the installation.
	The MySQL community edition shows a copy of the relevant GNU General Public License. Click Continue and then Agree to continue.
3. From the Installation Type page you can either click Install to execute the installation wizard using all defaults, click Customize to alter which components to install (MySQL server, MySQL Test, Preference Pane, Launchd Support -- all but MySQL Test are enabled by default).
	Note
	Although the Change Install Location option is visible, the installation location cannot be changed.
	**Figure 2.5 MySQL Package Installer Wizard: Customize**
	![Customize shows three package name options: MySQL Server, MySQL Test, Preference Pane, and Launchd Support. All three options are checked.](img/mac-installer-installation-type-customize.png)
4. Click Install to install MySQL Server. The installation process ends here if upgrading a current MySQL Server installation, otherwise follow the wizard's additional configuration steps for your new MySQL Server installation.
5. After a successful new MySQL Server installation, complete the configuration by defining the root password and enabling (or disabling) the MySQL server at startup.
6. Define a password for the root user, and also toggle whether MySQL Server should start after the configuration step is complete.
7. Summary is the final step and references a successful and complete MySQL Server installation. Close the wizard.

MySQL server is now installed. If you chose to not start MySQL, then use either launchctl from the command line or start MySQL by clicking "Start" using the MySQL preference pane. For additional information, see [Section 2.4.3, “Installing and Using the MySQL Launch Daemon”](macos-installation-launchd.md), and [Section 2.4.4, “Installing and Using the MySQL Preference Pane”](macos-installation-prefpane.md). Use the MySQL Preference Pane or launchd to configure MySQL to automatically start at bootup.

When installing using the package installer, the files are installed into a directory within `/usr/local` matching the name of the installation version and platform. For example, the installer file ``mysql-26.7.0-*`macos10.15-x86_64.dmg`*`` installs MySQL into `/usr/local/mysql-26.7.0-macos10.15-x86_64/       ` with a symlink to `/usr/local/mysql`. The following table shows the layout of this MySQL installation directory.

Note

The macOS installation process does not create nor install a sample `my.cnf` MySQL configuration file.

**Table 2.8 MySQL Installation Layout on macOS**

| Directory | Contents of Directory |
| --- | --- |
| `bin` | [**mysqld**](mysqld.md) server, client and utility programs |
| `data` | Log files, databases, where `/usr/local/mysql/data/mysqld.local.err` is the default error log |
| `docs` | Helper documents, like the Release Notes and build information |
| `include` | Include (header) files |
| `lib` | Libraries |
| `man` | Unix manual pages |
| `mysql-test` | MySQL test suite ('MySQL Test' is disabled by default during the installation process when using the installer package (DMG)) |
| `share` | Miscellaneous support files, including error messages, `dictionary.txt`, and rewriter SQL |
| `support-files` | Support scripts, such as `mysqld_multi.server`, `mysql.server`, and `mysql-log-rotate`. |
| `/tmp/mysql.sock` | Location of the MySQL Unix socket |