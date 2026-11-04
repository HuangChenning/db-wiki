---
title: "29.12 Performance Schema Table Descriptions"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/performance-schema-table-descriptions.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

Tables in the `performance_schema` database can be grouped as follows:

- Setup tables. These tables are used to configure and display monitoring characteristics.
- Current events tables. The [`events_waits_current`](performance-schema-events-waits-current-table.md) table contains the most recent event for each thread. Other similar tables contain current events at different levels of the event hierarchy: [`events_stages_current`](performance-schema-events-stages-current-table.md) for stage events, [`events_statements_current`](performance-schema-events-statements-current-table.md) for statement events, and [`events_transactions_current`](performance-schema-events-transactions-current-table.md) for transaction events.
- History tables. These tables have the same structure as the current events tables, but contain more rows. For example, for wait events, [`events_waits_history`](performance-schema-events-waits-history-table.md) table contains the most recent 10 events per thread. [`events_waits_history_long`](performance-schema-events-waits-history-long-table.md) contains the most recent 10,000 events. Other similar tables exist for stage, statement, and transaction histories.
	To change the sizes of the history tables, set the appropriate system variables at server startup. For example, to set the sizes of the wait event history tables, set [`performance_schema_events_waits_history_size`](performance-schema-system-variables.md) and [`performance_schema_events_waits_history_long_size`](performance-schema-system-variables.md).
- Summary tables. These tables contain information aggregated over groups of events, including those that have been discarded from the history tables.
- Instance tables. These tables document what types of objects are instrumented. An instrumented object, when used by the server, produces an event. These tables provide event names and explanatory notes or status information.
- Miscellaneous tables. These do not fall into any of the other table groups.