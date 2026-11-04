---
title: "MySQL :: MySQL 26.10 Reference Manual :: 1.3 MySQL Releases: Innovation and LTS"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/mysql-releases.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

## 1.3 MySQL Releases: Innovation and LTS

The MySQL release model is divided into two main tracks: LTS (Long-Term Support) and Innovation. All LTS and Innovation releases include bug and security fixes, and are considered production-grade quality.

### MySQL Version Numbers

MySQL 9.7 was the final release line using the sequential versioning model. Subsequent MySQL Innovation and LTS releases use calendar versioning in the YY.M.P format:

- YY: the two-digit release year
- M: the release month
- P: the patch or maintenance release number, starting at 0.

MySQL 26.7.0, representing the July 2026 release, is the first valid calendar-versioned MySQL release. MySQL 26.7.1 is a patch release in the same 26.7 release line. When a release is designated as an LTS release, its YY.M release base remains fixed throughout the support lifecycle, and subsequent maintenance releases increment the P component.

A calendar version does not determine whether a release is an Innovation or LTS release. Release maturity remains an explicit property of each release.

### Calendar-Version Compatibility Lineages

A calendar version identifies when a release was produced. It does not, by itself, identify which direct server upgrades are supported. Each calendar-versioned release contains release metadata that assigns it to a compatibility lineage anchored by an LTS release base.

All Innovation releases before an LTS release, and the LTS release that closes that sequence, belong to the same compatibility lineage. The first Innovation release after that LTS release begins the next lineage, which is anchored by the new LTS release base.

The following direct-upgrade rules apply:

- An Innovation release can upgrade to a later release in the same compatibility lineage, including the LTS release that closes the lineage.
- An Innovation release cannot upgrade across a compatibility-lineage boundary.
- An LTS release can upgrade within its own release line or into the immediately following compatibility lineage.
- An LTS release cannot skip a compatibility lineage.
- Only the final sequentially versioned LTS line, MySQL 9.7.x LTS, can upgrade directly into the first calendar-versioned compatibility lineage. That lineage is anchored by MySQL 9.7.0.

### MySQL LTS Releases

- `Audience`: If your environment requires a stable set of features and a longer support period.
- `Behavior`: These releases only contain necessary fixes to reduce the risks associated with changes in the database software's behavior. There are no removals within an LTS release. Features can be removed (and added) only in the first LTS release (such as 8.4.0 LTS) but not later.
- `Support`: An LTS series follows the [Oracle Lifetime Support](https://www.oracle.com/support/lifetime-support/software.html) Policy, which includes 5 years of premier support and 3 years of extended support.

### MySQL Innovation Releases

- `Audience`: If you want access to the latest features, improvements, and changes. These releases are ideal for developers and DBAs working in fast-paced development environments with high levels of automated tests and modern continuous integration techniques for faster upgrade cycles.
- `Behavior`: Apart from new features in innovation releases, behavior changes are also expected as code is refactored, deprecated functionality is removed, and when MySQL is modified to behave more in line with SQL Standards. This will not happen within an LTS release.
	Behavior changes can have a big impact, especially when dealing with anything application-related, such as SQL syntax, new reserved words, query execution, and query performance. Behavior changes might require application changes which can involve considerable effort to migrate. We intend to provide the necessary tools and configuration settings to make these transitions easier.
- `Support`: Innovation releases are supported until the next Innovation release.

### MySQL Portfolio

MySQL Server and MySQL NDB Cluster have both Innovation and LTS releases.

MySQL Connectors, MySQL Shell, MySQL Router, MySQL Operator for Kubernetes, have one release using the latest version number but remain compatible with all supported MySQL Server versions. For example, MySQL Connector/Python 26.7.0 is compatible with supported MySQL Server 8.4, 9.7, and 26.7 releases.

When a major version line advances (for example, 26.7), these products will follow the new major version while continuing to support the then-current Innovation and LTS releases of MySQL Server and MySQL NDB Cluster.

### Installing, Upgrading, and Downgrading

Having two tracks affects how MySQL is installed, upgraded, and downgraded. Typically you choose one particular track and all upgrades progress accordingly.

When using the official MySQL repository, the desired track is defined in the repository configuration. For example, with [Yum](linux-installation-yum-repo.md) choose `mysql-innovation-community` to install and upgrade Innovation releases or `mysql-9.7-lts-community` to install and upgrade MySQL 9.7.x releases.

**LTS Notes**

Functionality remains the same and data format does not change in an [LTS series](glossary.md), therefore in-place upgrades and downgrades are possible within the LTS series. For example, MySQL 8.4.0 can be upgraded to a later MySQL 8.4.x release. Additional upgrade and downgrade methods are available, such as [the clone plugin](clone-plugin.md).

Upgrading to the next [LTS series](glossary.md) is supported, such as 8.4.x LTS to 9.7.x LTS, while skipping an LTS series is not supported. For example, you cannot skip from 8.4.x LTS directly to 28.4.x LTS.

**Innovation Notes**

For releases that use sequential versioning, an Innovation installation upgrades to a more recent release in the same Innovation series. For example, MySQL 9.1.0 Innovation can upgrade to MySQL 9.2.0.

With sequential versioning, you cannot directly upgrade between Innovation series of different major versions, such as from 8.3.0 to 9.0.0. Instead, first upgrade to the intervening LTS series and then upgrade to the following Innovation series. For example, upgrading from 8.3.0 to 8.4.0, and then from 8.4.0 to 9.0.0, is a valid upgrade path. Calendar-versioned releases instead use the compatibility-lineage rules described in Calendar-Version Compatibility Lineages.

To help make the transition easier, the official MySQL repository treats the first LTS release as both LTS and Innovation, so for example with the Innovation track enabled in your local repository configuration, MySQL 8.3.0 upgrades to 8.4.0, and later to 9.0.0.

Innovation release downgrades require a logical dump and load.

**Additional Information and Examples**

For additional information and specific example supported scenarios, see [Section 3.2, “Upgrade Paths”](upgrade-paths.md) or [Chapter 4, *Downgrading MySQL*](downgrading.md). They describe available options to perform in-place updates (that replace binaries with the latest packages), a logical dump and load (such as using [**mysqldump**](mysqldump.md) or [MySQL Shell's dump utilities](https://dev.mysql.com/doc/mysql-shell/26.10/en/mysql-shell-utilities-dump-instance-schema.html)), cloning data with the [clone plugin](clone-plugin.md), and [asynchronous replication](replication-upgrade.md) for servers in a replication topology.