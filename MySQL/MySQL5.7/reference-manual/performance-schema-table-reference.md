---
title: "25.12.1 Performance Schema Table Reference"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/performance-schema-table-reference.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 25.12.1 Performance Schema Table Reference

The following table summarizes all available Performance Schema tables. For greater detail, see the individual table descriptions.

**Table 25.1 Performance Schema Tables**

| Table Name | Description | Deprecated |
| --- | --- | --- |
| [`accounts`](performance-schema-accounts-table.md) | Connection statistics per client account |  |
| [`cond_instances`](performance-schema-cond-instances-table.md) | Synchronization object instances |  |
| [`events_stages_current`](performance-schema-events-stages-current-table.md) | Current stage events |  |
| [`events_stages_history`](performance-schema-events-stages-history-table.md) | Most recent stage events per thread |  |
| [`events_stages_history_long`](performance-schema-events-stages-history-long-table.md) | Most recent stage events overall |  |
| [`events_stages_summary_by_account_by_event_name`](performance-schema-stage-summary-tables.md) | Stage events per account and event name |  |
| [`events_stages_summary_by_host_by_event_name`](performance-schema-stage-summary-tables.md) | Stage events per host name and event name |  |
| [`events_stages_summary_by_thread_by_event_name`](performance-schema-stage-summary-tables.md) | Stage waits per thread and event name |  |
| [`events_stages_summary_by_user_by_event_name`](performance-schema-stage-summary-tables.md) | Stage events per user name and event name |  |
| [`events_stages_summary_global_by_event_name`](performance-schema-stage-summary-tables.md) | Stage waits per event name |  |
| [`events_statements_current`](performance-schema-events-statements-current-table.md) | Current statement events |  |
| [`events_statements_history`](performance-schema-events-statements-history-table.md) | Most recent statement events per thread |  |
| [`events_statements_history_long`](performance-schema-events-statements-history-long-table.md) | Most recent statement events overall |  |
| [`events_statements_summary_by_account_by_event_name`](performance-schema-statement-summary-tables.md) | Statement events per account and event name |  |
| [`events_statements_summary_by_digest`](performance-schema-statement-summary-tables.md) | Statement events per schema and digest value |  |
| [`events_statements_summary_by_host_by_event_name`](performance-schema-statement-summary-tables.md) | Statement events per host name and event name |  |
| [`events_statements_summary_by_program`](performance-schema-statement-summary-tables.md) | Statement events per stored program |  |
| [`events_statements_summary_by_thread_by_event_name`](performance-schema-statement-summary-tables.md) | Statement events per thread and event name |  |
| [`events_statements_summary_by_user_by_event_name`](performance-schema-statement-summary-tables.md) | Statement events per user name and event name |  |
| [`events_statements_summary_global_by_event_name`](performance-schema-statement-summary-tables.md) | Statement events per event name |  |
| [`events_transactions_current`](performance-schema-events-transactions-current-table.md) | Current transaction events |  |
| [`events_transactions_history`](performance-schema-events-transactions-history-table.md) | Most recent transaction events per thread |  |
| [`events_transactions_history_long`](performance-schema-events-transactions-history-long-table.md) | Most recent transaction events overall |  |
| [`events_transactions_summary_by_account_by_event_name`](performance-schema-transaction-summary-tables.md) | Transaction events per account and event name |  |
| [`events_transactions_summary_by_host_by_event_name`](performance-schema-transaction-summary-tables.md) | Transaction events per host name and event name |  |
| [`events_transactions_summary_by_thread_by_event_name`](performance-schema-transaction-summary-tables.md) | Transaction events per thread and event name |  |
| [`events_transactions_summary_by_user_by_event_name`](performance-schema-transaction-summary-tables.md) | Transaction events per user name and event name |  |
| [`events_transactions_summary_global_by_event_name`](performance-schema-transaction-summary-tables.md) | Transaction events per event name |  |
| [`events_waits_current`](performance-schema-events-waits-current-table.md) | Current wait events |  |
| [`events_waits_history`](performance-schema-events-waits-history-table.md) | Most recent wait events per thread |  |
| [`events_waits_history_long`](performance-schema-events-waits-history-long-table.md) | Most recent wait events overall |  |
| [`events_waits_summary_by_account_by_event_name`](performance-schema-wait-summary-tables.md) | Wait events per account and event name |  |
| [`events_waits_summary_by_host_by_event_name`](performance-schema-wait-summary-tables.md) | Wait events per host name and event name |  |
| [`events_waits_summary_by_instance`](performance-schema-wait-summary-tables.md) | Wait events per instance |  |
| [`events_waits_summary_by_thread_by_event_name`](performance-schema-wait-summary-tables.md) | Wait events per thread and event name |  |
| [`events_waits_summary_by_user_by_event_name`](performance-schema-wait-summary-tables.md) | Wait events per user name and event name |  |
| [`events_waits_summary_global_by_event_name`](performance-schema-wait-summary-tables.md) | Wait events per event name |  |
| [`file_instances`](performance-schema-file-instances-table.md) | File instances |  |
| [`file_summary_by_event_name`](performance-schema-file-summary-tables.md) | File events per event name |  |
| [`file_summary_by_instance`](performance-schema-file-summary-tables.md) | File events per file instance |  |
| [`global_status`](performance-schema-status-variable-tables.md) | Global status variables |  |
| [`global_variables`](performance-schema-system-variable-tables.md) | Global system variables |  |
| [`host_cache`](performance-schema-host-cache-table.md) | Information from internal host cache |  |
| [`hosts`](performance-schema-hosts-table.md) | Connection statistics per client host name |  |
| [`memory_summary_by_account_by_event_name`](performance-schema-memory-summary-tables.md) | Memory operations per account and event name |  |
| [`memory_summary_by_host_by_event_name`](performance-schema-memory-summary-tables.md) | Memory operations per host and event name |  |
| [`memory_summary_by_thread_by_event_name`](performance-schema-memory-summary-tables.md) | Memory operations per thread and event name |  |
| [`memory_summary_by_user_by_event_name`](performance-schema-memory-summary-tables.md) | Memory operations per user and event name |  |
| [`memory_summary_global_by_event_name`](performance-schema-memory-summary-tables.md) | Memory operations globally per event name |  |
| [`metadata_locks`](performance-schema-metadata-locks-table.md) | Metadata locks and lock requests |  |
| [`mutex_instances`](performance-schema-mutex-instances-table.md) | Mutex synchronization object instances |  |
| [`objects_summary_global_by_type`](performance-schema-objects-summary-global-by-type-table.md) | Object summaries |  |
| [`performance_timers`](performance-schema-performance-timers-table.md) | Which event timers are available |  |
| [`prepared_statements_instances`](performance-schema-prepared-statements-instances-table.md) | Prepared statement instances and statistics |  |
| [`replication_applier_configuration`](performance-schema-replication-applier-configuration-table.md) | Configuration parameters for replication applier on replica |  |
| [`replication_applier_status`](performance-schema-replication-applier-status-table.md) | Current status of replication applier on replica |  |
| [`replication_applier_status_by_coordinator`](performance-schema-replication-applier-status-by-coordinator-table.md) | SQL or coordinator thread applier status |  |
| [`replication_applier_status_by_worker`](performance-schema-replication-applier-status-by-worker-table.md) | Worker thread applier status |  |
| [`replication_connection_configuration`](performance-schema-replication-connection-configuration-table.md) | Configuration parameters for connecting to source |  |
| [`replication_connection_status`](performance-schema-replication-connection-status-table.md) | Current status of connection to source |  |
| [`replication_group_member_stats`](performance-schema-replication-group-member-stats-table.md) | Replication group member statistics |  |
| [`replication_group_members`](performance-schema-replication-group-members-table.md) | Replication group member network and status |  |
| [`rwlock_instances`](performance-schema-rwlock-instances-table.md) | Lock synchronization object instances |  |
| [`session_account_connect_attrs`](performance-schema-session-account-connect-attrs-table.md) | Connection attributes per for current session |  |
| [`session_connect_attrs`](performance-schema-session-connect-attrs-table.md) | Connection attributes for all sessions |  |
| [`session_status`](performance-schema-status-variable-tables.md) | Status variables for current session |  |
| [`session_variables`](performance-schema-system-variable-tables.md) | System variables for current session |  |
| [`setup_actors`](performance-schema-setup-actors-table.md) | How to initialize monitoring for new foreground threads |  |
| [`setup_consumers`](performance-schema-setup-consumers-table.md) | Consumers for which event information can be stored |  |
| [`setup_instruments`](performance-schema-setup-instruments-table.md) | Classes of instrumented objects for which events can be collected |  |
| [`setup_objects`](performance-schema-setup-objects-table.md) | Which objects should be monitored |  |
| [`setup_timers`](performance-schema-setup-timers-table.md) | Currently selected event timers | Yes |
| [`socket_instances`](performance-schema-socket-instances-table.md) | Active connection instances |  |
| [`socket_summary_by_event_name`](performance-schema-socket-summary-tables.md) | Socket waits and I/O per event name |  |
| [`socket_summary_by_instance`](performance-schema-socket-summary-tables.md) | Socket waits and I/O per instance |  |
| [`status_by_account`](performance-schema-status-variable-summary-tables.md) | Session status variables per account |  |
| [`status_by_host`](performance-schema-status-variable-summary-tables.md) | Session status variables per host name |  |
| [`status_by_thread`](performance-schema-status-variable-tables.md) | Session status variables per session |  |
| [`status_by_user`](performance-schema-status-variable-summary-tables.md) | Session status variables per user name |  |
| [`table_handles`](performance-schema-table-handles-table.md) | Table locks and lock requests |  |
| [`table_io_waits_summary_by_index_usage`](performance-schema-table-wait-summary-tables.md) | Table I/O waits per index |  |
| [`table_io_waits_summary_by_table`](performance-schema-table-wait-summary-tables.md) | Table I/O waits per table |  |
| [`table_lock_waits_summary_by_table`](performance-schema-table-wait-summary-tables.md) | Table lock waits per table |  |
| [`threads`](performance-schema-threads-table.md) | Information about server threads |  |
| [`user_variables_by_thread`](performance-schema-user-variable-tables.md) | User-defined variables per thread |  |
| [`users`](performance-schema-users-table.md) | Connection statistics per client user name |  |
| [`variables_by_thread`](performance-schema-system-variable-tables.md) | Session system variables per session |  |