---
title: "29.4.3 Event Pre-Filtering"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/performance-schema-pre-filtering.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 29.4.3 Event Pre-Filtering

Pre-filtering is done by the Performance Schema and has a global effect that applies to all users. Pre-filtering can be applied to either the producer or consumer stage of event processing:

- To configure pre-filtering at the producer stage, several tables can be used:
	- [`setup_instruments`](performance-schema-setup-instruments-table.md) indicates which instruments are available. An instrument disabled in this table produces no events regardless of the contents of the other production-related setup tables. An instrument enabled in this table is permitted to produce events, subject to the contents of the other tables.
	- [`setup_objects`](performance-schema-setup-objects-table.md) controls whether the Performance Schema monitors particular table and stored program objects.
	- [`threads`](performance-schema-threads-table.md) indicates whether monitoring is enabled for each server thread.
	- [`setup_actors`](performance-schema-setup-actors-table.md) determines the initial monitoring state for new foreground threads.
- To configure pre-filtering at the consumer stage, modify the [`setup_consumers`](performance-schema-setup-consumers-table.md) table. This determines the destinations to which events are sent. [`setup_consumers`](performance-schema-setup-consumers-table.md) also implicitly affects event production. If a given event is not sent to any destination (that is, it is never consumed), the Performance Schema does not produce it.

Modifications to any of these tables affect monitoring immediately, with the exception that modifications to the [`setup_actors`](performance-schema-setup-actors-table.md) table affect only foreground threads created subsequent to the modification, not existing threads.

When you change the monitoring configuration, the Performance Schema does not flush the history tables. Events already collected remain in the current-events and history tables until displaced by newer events. If you disable instruments, you might need to wait a while before events for them are displaced by newer events of interest. Alternatively, use [`TRUNCATE TABLE`](truncate-table.md) to empty the history tables.

After making instrumentation changes, you might want to truncate the summary tables. Generally, the effect is to reset the summary columns to 0 or `NULL`, not to remove rows. This enables you to clear collected values and restart aggregation. That might be useful, for example, after you have made a runtime configuration change. Exceptions to this truncation behavior are noted in individual summary table sections.

The following sections describe how to use specific tables to control Performance Schema pre-filtering.