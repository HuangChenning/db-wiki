---
title: "3.1 Before You Begin"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/upgrade-before-you-begin.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

Review the information in this section before upgrading. Perform any recommended actions.

- Understand what may occur during an upgrade. See [Section 3.4, “What the MySQL Upgrade Process Upgrades”](upgrading-what-is-upgraded.md).
- Protect your data by creating a backup. The backup should include the `mysql` system database, which contains the MySQL data dictionary tables and system tables. See [Section 9.2, “Database Backup Methods”](backup-methods.md).
	Important
	Downgrade from MySQL 8.0 to MySQL 5.7, or from a MySQL 8.0 release to a previous MySQL 8.0 release, is not supported. The only supported alternative is to restore a backup taken *before* upgrading. It is therefore imperative that you back up your data before starting the upgrade process.
- Review [Section 3.2, “Upgrade Paths”](upgrade-paths.md) to ensure that your intended upgrade path is supported.
- Review [Section 3.5, “Changes in MySQL 8.0”](upgrading-from-previous-series.md) for changes that you should be aware of before upgrading. Some changes may require action.
- Review [Section 1.3, “What Is New in MySQL 8.0”](mysql-nutshell.md) for deprecated and removed features. An upgrade may require changes with respect to those features if you use any of them.
- Review [Section 1.4, “Server and Status Variables and Options Added, Deprecated, or Removed in MySQL 8.0”](added-deprecated-removed.md). If you use deprecated or removed variables, an upgrade may require configuration changes.
- Review the [Release Notes](https://docs.oracle.com/cd/E17952_01/mysql-8.0-relnotes-en/) for information about fixes, changes, and new features.
- If you use replication, review [Section 19.5.3, “Upgrading a Replication Topology”](replication-upgrade.md).
- Review [Section 3.3, “Upgrade Best Practices”](upgrade-best-practices.md) and plan accordingly.
- Upgrade procedures vary by platform and how the initial installation was performed. Use the procedure that applies to your current MySQL installation:
	- For binary and package-based installations on non-Windows platforms, refer to [Section 3.7, “Upgrading MySQL Binary or Package-based Installations on Unix/Linux”](upgrade-binary-package.md).
		Note
		For supported Linux distributions, the preferred method for upgrading package-based installations is to use the MySQL software repositories (MySQL Yum Repository, MySQL APT Repository, and MySQL SLES Repository).
	- For installations on an Enterprise Linux platform or Fedora using the MySQL Yum Repository, refer to [Section 3.8, “Upgrading MySQL with the MySQL Yum Repository”](updating-yum-repo.md).
	- For installations on Ubuntu using the MySQL APT repository, refer to [Section 3.9, “Upgrading MySQL with the MySQL APT Repository”](updating-apt-repo.md).
	- For installations on SLES using the MySQL SLES repository, refer to [Section 3.10, “Upgrading MySQL with the MySQL SLES Repository”](updating-sles-repo.md).
	- For installations performed using Docker, refer to [Section 3.12, “Upgrading a Docker Installation of MySQL”](upgrade-docker-mysql.md).
	- For installations on Windows, refer to [Section 3.11, “Upgrading MySQL on Windows”](windows-upgrading.md).
- If your MySQL installation contains a large amount of data that might take a long time to convert after an in-place upgrade, it may be useful to create a test instance for assessing the conversions that are required and the work involved to perform them. To create a test instance, make a copy of your MySQL instance that contains the `mysql` database and other databases without the data. Run the upgrade procedure on the test instance to assess the work involved to perform the actual data conversion.
- Rebuilding and reinstalling MySQL language interfaces is recommended when you install or upgrade to a new release of MySQL. This applies to MySQL interfaces such as PHP `mysql` extensions and the Perl `DBD::mysql` module.