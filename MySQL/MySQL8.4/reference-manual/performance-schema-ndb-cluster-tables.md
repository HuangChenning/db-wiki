---
title: "29.12.12 Performance Schema NDB Cluster Tables"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/performance-schema-ndb-cluster-tables.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

### 29.12.12 Performance Schema NDB Cluster Tables

The following table shows all Performance Schema tables relating to the [`NDBCLUSTER`](mysql-cluster.md) storage engine.

**Table 29.3 Performance Schema NDB Tables**

| Table Name | Description |
| --- | --- |
| [`ndb_sync_excluded_objects`](performance-schema-ndb-sync-excluded-objects-table.md) | NDB objects which cannot be synchronized |
| [`ndb_sync_pending_objects`](performance-schema-ndb-sync-pending-objects-table.md) | NDB objects waiting for synchronization |

Automatic synchronization in [`NDB`](mysql-cluster.md) attempts to detect and synchronize automatically all mismatches in metadata between the NDB Cluster's internal dictionary and the MySQL Server's datadictionary. This is done by default in the background at regular intervals as determined by the [`ndb_metadata_check_interval`](mysql-cluster-options-variables.md) system variable, unless disabled using [`ndb_metadata_check`](mysql-cluster-options-variables.md) or overridden by setting [`ndb_metadata_sync`](mysql-cluster-options-variables.md).

Information about the current state of automatic synchronization is exposed by a MySQL server acting as an SQL node in an NDB Cluster in these two Performance Schema tables:

- [`ndb_sync_pending_objects`](performance-schema-ndb-sync-pending-objects-table.md): Displays information about [`NDB`](mysql-cluster.md) database objects for which mismatches have been detected between the `NDB` dictionary and the MySQL data dictionary. When attempting to synchronize such objects, [`NDB`](mysql-cluster.md) removes the object from the queue awaiting synchronization, and from this table, and tries to reconcile the mismatch. If synchronization of the object fails due to a temporary error, it is picked up and added back to the queue (and to this table) the next time `NDB` performs mismatch detection; if the attempts fails due a permanent error, the object is added to the [`ndb_sync_excluded_objects`](performance-schema-ndb-sync-excluded-objects-table.md) table.
- [`ndb_sync_excluded_objects`](performance-schema-ndb-sync-excluded-objects-table.md): Shows information about [`NDB`](mysql-cluster.md) database objects for which automatic synchronization has failed due to permanent errors resulting from mismatches which cannot be reconciled without manual intervention; these objects are blocklisted and not considered again for mismatch detection until this has been done.

The [`ndb_sync_pending_objects`](performance-schema-ndb-sync-pending-objects-table.md) and [`ndb_sync_excluded_objects`](performance-schema-ndb-sync-excluded-objects-table.md) tables are present only if MySQL has support enabled for the [`NDBCLUSTER`](mysql-cluster.md) storage engine.

These tables are described in more detail in the following two sections.