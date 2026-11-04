---
title: "MySQL :: MySQL 26.7 Reference Manual :: 1.4 What Is New in MySQL 26.7"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/mysql-nutshell.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

## 1.4 What Is New in MySQL 26.7

This section summarizes what has been added to, deprecated in, changed, and removed from MySQL 26.7 since MySQL 9.7. A companion section lists MySQL server options and variables that have been added, deprecated, or removed in MySQL 26.7; see [Section 1.5, “Server and Status Variables and Options Added, Deprecated, or Removed in MySQL 26.7”](added-deprecated-removed.md).

### Features Added or Changed in MySQL 26.7

The following features have been added to MySQL 26.7:

- **Calendar-based versioning and compatibility-lineage validation.** MySQL 26.7.0 is the first release to use the YY.M.P calendar-version format. The server now persists internal compatibility-lineage metadata in the data dictionary and uses it when validating subsequent direct upgrades. MySQL 9.7.x LTS is the only legacy release line that can enter the first calendar-versioned lineage. Innovation releases can upgrade within a lineage but cannot cross a lineage boundary, while an LTS release can enter the immediately following lineage. Direct downgrade policy remains limited to qualifying patch downgrades within the same LTS YY.M release line. See [Section 1.3, “MySQL Releases: Innovation and LTS”](mysql-releases.md), [Section 3.2, “Upgrade Paths”](upgrade-paths.md), and [Chapter 4, *Downgrading MySQL*](downgrading.md).
- **Clone version compatibility for calendar-versioned releases.** The clone plugin permits cloning between patch releases within the same MySQL server series. Between different series, cloning is permitted only from an LTS donor to the immediately following LTS recipient. Cross-series cloning involving an Innovation release, cloning to an older LTS series, and cloning that skips an LTS series are not supported. See [Section 7.6.6.3, “Cloning Remote Data”](clone-plugin-remote.md).
- **InnoDB `AUTO_INCREMENT` counter persistence.** InnoDB now persists `AUTO_INCREMENT` counters in batches. The new global, dynamic [`innodb_autoinc_preallocate`](innodb-parameters.md) system variable controls how many extra values are reserved when a counter is persisted. The default is 50. This reduces persistent metadata updates, but an unexpected server exit can cause unused reserved values to be skipped. Setting the variable to 0 disables extra preallocation. A graceful shutdown persists the actual counter value and does not introduce a preallocation gap.
- **Crash-safe undo tablespace creation and truncation.** InnoDB no longer creates local `undo_space_number_trunc.log` marker files for `CREATE UNDO TABLESPACE` or undo tablespace truncation operations. Instead, it records in-progress state in the undo tablespace file header and uses redo and DDL logging to recover interrupted operations. At startup, affected undo tablespaces are removed or recreated as necessary. For backward compatibility, marker files left by earlier server versions continue to be recognized, but no new marker files are created. An undo tablespace recorded in the data dictionary but not discovered in a known directory is recreated automatically. At least one active undo tablespace must remain available after initialization; if no undo tablespaces are found, server startup cannot continue. See [Section 17.6.3.4, “Undo Tablespaces”](innodb-undo-tablespaces.md).
- **Post-quantum cryptography for TLS.** For builds using OpenSSL 3.5 or later, MySQL TLSv1.3 connections support hybrid and pure post-quantum key-exchange groups and ML-DSA TLS handshake signature algorithms. PQC key exchange is preferred with classical fallback by default, and can be required independently for the main, administrative, asynchronous replication, Group Replication, and X Plugin connection channels. New client options and status variables provide configuration and monitoring support. See [Section 8.3.6, “Post-Quantum Cryptography”](post-quantum-crytpography-ssl.md).
- **Change Stream Applier.** The Change Stream Applier (CSA) is an optional replication applier designed to improve parallel transaction application and scalability. CSA is selected per channel using `APPLIER_VERSION = 2`. The `APPLIER_WORKER_COUNT` and `APPLIER_EVENT_MEMORY_LIMIT` options provide per-channel worker and event-memory configuration. CSA requires row-based replication with GTIDs. See [Section 19.2.4, “Change Stream Applier”](change-stream-applier.md).

### Features Deprecated in MySQL 26.7

The following features are deprecated in MySQL 26.7 and may be removed in a future series. Where alternatives are shown, applications should be updated to use them.

For applications that use features deprecated in MySQL 26.7 that have been removed in a later MySQL version, statements may fail when replicated from a MySQL 26.7 source to a replica running a later version, or may have different effects on source and replica. To avoid such problems, applications that use features deprecated in 26.7 should be revised to avoid them and use alternatives when possible.

- **SCRAM-SHA-1 authentication.** The `SCRAM-SHA-1` authentication method for SASL LDAP authentication is deprecated as of MySQL 9.5.0. Use `SCRAM-SHA-256` instead; this is also now the default value for [`authentication_ldap_sasl_auth_method_name`](pluggable-authentication-system-variables.md).
	See [Section 8.4.1.6, “LDAP Pluggable Authentication”](ldap-pluggable-authentication.md), for more information.

### Features Removed in MySQL 26.7

The following items are obsolete and have been removed in MySQL 26.7. Where alternatives are shown, applications should be updated to use them.

For MySQL 9.7 applications that use features removed in MySQL 26.7, statements may fail when replicated from a MySQL 9.7 source to a MySQL 26.7 replica, or may have different effects on source and replica. To avoid such problems, applications that use features removed in MySQL 26.7 should be revised to avoid them and use alternatives when possible.

- **Server system and status variables removed.** Server system and status variables removed in MySQL 26.7 are shown in the following list: