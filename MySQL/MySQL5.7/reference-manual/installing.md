---
title: "Chapter 2 Installing and Upgrading MySQL"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/installing.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

This chapter describes how to obtain and install MySQL. A summary of the procedure follows and later sections provide the details. If you plan to upgrade an existing version of MySQL to a newer version rather than install MySQL for the first time, see [Section 2.10, “Upgrading MySQL”](upgrading.md), for information about upgrade procedures and about issues that you should consider before upgrading.

If you are interested in migrating to MySQL from another database system, see [Section A.8, “MySQL 5.7 FAQ: Migration”](faqs-migration.md), which contains answers to some common questions concerning migration issues.

Installation of MySQL generally follows the steps outlined here:

1. **Determine whether MySQL runs and is supported on your platform.**
	Please note that not all platforms are equally suitable for running MySQL, and that not all platforms on which MySQL is known to run are officially supported by Oracle Corporation. For information about those platforms that are officially supported, see [https://www.mysql.com/support/supportedplatforms/database.html](https://www.mysql.com/support/supportedplatforms/database.html) on the MySQL website.
2. **Choose which distribution to install.**
	Several versions of MySQL are available, and most are available in several distribution formats. You can choose from pre-packaged distributions containing binary (precompiled) programs or source code. When in doubt, use a binary distribution. Oracle also provides access to the MySQL source code for those who want to see recent developments and test new code. To determine which version and type of distribution you should use, see [Section 2.1.2, “Which MySQL Version and Distribution to Install”](which-version.md).
3. **Download the distribution that you want to install.**
	For instructions, see [Section 2.1.3, “How to Get MySQL”](getting-mysql.md). To verify the integrity of the distribution, use the instructions in [Section 2.1.4, “Verifying Package Integrity Using MD5 Checksums or GnuPG”](verifying-package-integrity.md).
4. **Install the distribution.**
	To install MySQL from a binary distribution, use the instructions in [Section 2.2, “Installing MySQL on Unix/Linux Using Generic Binaries”](binary-installation.md). Alternatively, use the [Secure Deployment Guide](https://dev.mysql.com/doc/mysql-secure-deployment-guide/5.7/en/), which provides procedures for deploying a generic binary distribution of MySQL Enterprise Edition Server with features for managing the security of your MySQL installation.
	To install MySQL from a source distribution or from the current development source tree, use the instructions in [Section 2.8, “Installing MySQL from Source”](source-installation.md).
5. **Perform any necessary postinstallation setup.**
	After installing MySQL, see [Section 2.9, “Postinstallation Setup and Testing”](postinstallation.md) for information about making sure the MySQL server is working properly. Also refer to the information provided in [Section 2.9.4, “Securing the Initial MySQL Account”](default-privileges.md). This section describes how to secure the initial MySQL `root` user account, *which has no password* until you assign one. The section applies whether you install MySQL using a binary or source distribution.
6. If you want to run the MySQL benchmark scripts, Perl support for MySQL must be available. See [Section 2.12, “Perl Installation Notes”](perl-support.md).

Instructions for installing MySQL on different platforms and environments is available on a platform by platform basis:

- **Unix, Linux**
	For instructions on installing MySQL on most Linux and Unix platforms using a generic binary (for example, a `.tar.gz` package), see [Section 2.2, “Installing MySQL on Unix/Linux Using Generic Binaries”](binary-installation.md).
	For information on building MySQL entirely from the source code distributions or the source code repositories, see [Section 2.8, “Installing MySQL from Source”](source-installation.md)
	For specific platform help on installation, configuration, and building from source see the corresponding platform section:
	- Linux, including notes on distribution specific methods, see [Section 2.5, “Installing MySQL on Linux”](linux-installation.md).
	- Solaris, including PKG and IPS formats, see [Section 2.7, “Installing MySQL on Solaris”](solaris-installation.md).
	- IBM AIX, see [Section 2.7, “Installing MySQL on Solaris”](solaris-installation.md).
- **Microsoft Windows**
	For instructions on installing MySQL on Microsoft Windows, using either the MySQL Installer or Zipped binary, see [Section 2.3, “Installing MySQL on Microsoft Windows”](windows-installation.md).
	For details and instructions on building MySQL from source code using Microsoft Visual Studio, see [Section 2.8, “Installing MySQL from Source”](source-installation.md).
- **macOS**
	For installation on macOS, including using both the binary package and native PKG formats, see [Section 2.4, “Installing MySQL on macOS”](macos-installation.md).
	For information on making use of an macOS Launch Daemon to automatically start and stop MySQL, see [Section 2.4.3, “Installing a MySQL Launch Daemon”](macos-installation-launchd.md).
	For information on the MySQL Preference Pane, see [Section 2.4.4, “Installing and Using the MySQL Preference Pane”](macos-installation-prefpane.md).