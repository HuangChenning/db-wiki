---
title: "1.5 Server and Status Variables and Options Added, Deprecated, or Removed in MySQL 9.7"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/added-deprecated-removed.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

This section lists server variables, status variables, and options that were added for the first time, have been deprecated, or have been removed in MySQL 9.7.

### Options and Variables Introduced in MySQL 9.7

The following system variables, status variables, and server options have been added in MySQL 9.7.

- `audit_log.filter_recovery_mode`: Controls the recovery mode of the server if. Added in MySQL 9.7.0.
- `audit_log.rotate_on_time`: Close and reopen audit log file based on elapsed time since current file was created. Added in MySQL 9.7.0.
- `audit_log_filter_recovery_mode`: Controls the recovery mode of the server if. Added in MySQL 9.7.0.
- `caching_sha2_password_enforce_storage_format`: Enforces storage format for. Added in MySQL 9.7.0.
- `caching_sha2_password_storage_format`: Storage format for. Added in MySQL 9.7.0.
- `enable_cascade_triggers`: Specifies handling of foreign keys by the server runtime or the InnoDB engine. Added in MySQL 9.7.0.
- `object_policy_flush_interval_seconds`: Enables refreshing of object policy cache for secondaries and replicas. Added in MySQL 9.7.0.
- `replica_allow_higher_version_source`: Controls whether asynchronous replication is allowed from a higher-version source server.. Added in MySQL 9.7.0.

### Options and Variables Deprecated in MySQL 9.7

The following system variables, status variables, and options have been deprecated in MySQL 9.7.

- `enable_cascade_triggers`: Specifies handling of foreign keys by the server runtime or the InnoDB engine. Deprecated in MySQL 9.7.0.

### Options and Variables Removed in MySQL 9.7

No system variables, status variables, or options have been removed in MySQL 9.7.