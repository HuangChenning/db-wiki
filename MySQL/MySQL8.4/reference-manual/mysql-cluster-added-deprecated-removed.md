---
title: "25.2.5 Options, Variables, and Parameters Added, Deprecated or Removed in NDB 8.4"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/mysql-cluster-added-deprecated-removed.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

### 25.2.5 Options, Variables, and Parameters Added, Deprecated or Removed in NDB 8.4

The next few sections contain information about `NDB` node configuration parameters and NDB-specific [**mysqld**](mysqld.md) options and variables that have been added to, deprecated in, or removed from NDB 8.4 since NDB 8.0.

#### Parameters Introduced in NDB 8.4

The following node configuration parameters have been added in NDB 8.4.

- `ApiFailureHandlingTimeout`: Maximum time for API node failure handling before escalating. 0 means no time limit; minimum usable value is 10. Added in NDB 8.4.5.
- `RequireCertificate`: Node is required to find key and certificate in TLS search path. Added in NDB 8.3.0.
- `RequireLinkTls`: Read-only; is set to true if either endpoint of this connection requires TLS. Added in NDB 8.3.0.
- `RequireTls`: Client connection must authenticate with TLS before being used otherwise. Added in NDB 8.3.0.
- `RequireTls`: Require TLS-authenticated secure connections. Added in NDB 8.3.0.

#### Parameters Deprecated in NDB 8.4

No node configuration parameters have been deprecated in NDB 8.4.

#### Parameters Removed in NDB 8.4

No node configuration parameters have been removed in NDB 8.4.

#### Options and Variables Introduced in NDB 8.4

The following system variables, status variables, and server options have been added in NDB 8.4.

- `Ndb_schema_participant_count`: Number of MySQL servers participating in NDB schema change distribution. Added in NDB 8.4.5.
- `ndb-mgm-tls`: Whether TLS connection requirements are strict or relaxed. Added in NDB 8.3.0-ndb-8.3.0.
- `ndb-tls-search-path`: Directories to search for NDB TLS CAs and private keys. Added in NDB 8.3.0-ndb-8.3.0.
- `ndb_log_cache_size`: Set size of transaction cache used for recording NDB binary log. Added in NDB 8.4.3-ndb-8.4.3.

#### Options and Variables Deprecated in NDB 8.4

No system variables, status variables, or server options have been deprecated in NDB 8.4.

#### Options and Variables Removed in NDB 8.4

No system variables, status variables, or options have been removed in NDB 8.4.