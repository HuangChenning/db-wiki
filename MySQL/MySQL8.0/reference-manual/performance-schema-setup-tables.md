---
title: "29.12.2 Performance Schema Setup Tables"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/performance-schema-setup-tables.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 29.12.2 Performance Schema Setup Tables

The setup tables provide information about the current instrumentation and enable the monitoring configuration to be changed. For this reason, some columns in these tables can be changed if you have the [`UPDATE`](privileges-provided.md) privilege.

The use of tables rather than individual variables for setup information provides a high degree of flexibility in modifying Performance Schema configuration. For example, you can use a single statement with standard SQL syntax to make multiple simultaneous configuration changes.

These setup tables are available:

- [`setup_actors`](performance-schema-setup-actors-table.md): How to initialize monitoring for new foreground threads
- [`setup_consumers`](performance-schema-setup-consumers-table.md): The destinations to which event information can be sent and stored
- [`setup_instruments`](performance-schema-setup-instruments-table.md): The classes of instrumented objects for which events can be collected
- [`setup_objects`](performance-schema-setup-objects-table.md): Which objects should be monitored
- [`setup_threads`](performance-schema-setup-threads-table.md): Instrumented thread names and attributes