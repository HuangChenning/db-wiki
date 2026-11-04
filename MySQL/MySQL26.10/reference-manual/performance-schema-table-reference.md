---
title: "MySQL :: MySQL 26.10 Reference Manual :: 29.12.1 Performance Schema Table Reference"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/performance-schema-table-reference.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 29.12.1 Performance Schema Table Reference

The following table summarizes all available Performance Schema tables. For greater detail, see the individual table descriptions.

**Table 29.1 Performance Schema Tables**

| Table Name | Description |
| --- | --- |
| [`accounts`](performance-schema-accounts-table.md) | Connection statistics per client account |
| [`binary_log_transaction_compression_stats`](performance-schema-binary-log-transaction-compression-stats-table.md) | Binary log transaction compression |
| [`clone_progress`](performance-schema-clone-progress-table.md) | Clone operation progress |
| [`clone_status`](performance-schema-clone-status-table.md) | Clone operation status |
| [`component_scheduler_tasks`](performance-schema-component-scheduler-tasks-table.md) | Status of scheduled tasks |
| [`cond_instances`](performance-schema-cond-instances-table.md) | Synchronization object instances |
| [`connection_control_failed_login_attempts`](performance-schema-connection-control-failed-login-attempts-table.md) | Current number of consecutive failed connection attempts per account |
| [`data_lock_waits`](performance-schema-data-lock-waits-table.md) | Data lock wait relationships |
| [`data_locks`](performance-schema-data-locks-table.md) | Data locks held and requested |
| [`disk_forecast`](performance-schema-disk-forecast-table.md) | Lists the forecasted disk usage samples and state |
| [`disk_forecast_summary`](performance-schema-disk-forecast-summary-table.md) | Lists the current disk forecast summary |
| [`disk_metric`](performance-schema-disk-metric-table.md) | Lists the disk metrics used for forecasting |
| [`error_log`](performance-schema-error-log-table.md) | Server error log recent entries |
| [`events_errors_summary_by_account_by_error`](performance-schema-error-summary-tables.md) | Errors per account and error code |
| [`events_errors_summary_by_host_by_error`](performance-schema-error-summary-tables.md) | Errors per host and error code |
| [`events_errors_summary_by_thread_by_error`](performance-schema-error-summary-tables.md) | Errors per thread and error code |
| [`events_errors_summary_by_user_by_error`](performance-schema-error-summary-tables.md) | Errors per user and error code |
| [`events_errors_summary_global_by_error`](performance-schema-error-summary-tables.md) | Errors per error code |
| [`events_stages_current`](performance-schema-events-stages-current-table.md) | Current stage events |
| [`events_stages_history`](performance-schema-events-stages-history-table.md) | Most recent stage events per thread |
| [`events_stages_history_long`](performance-schema-events-stages-history-long-table.md) | Most recent stage events overall |
| [`events_stages_summary_by_account_by_event_name`](performance-schema-stage-summary-tables.md) | Stage events per account and event name |
| [`events_stages_summary_by_host_by_event_name`](performance-schema-stage-summary-tables.md) | Stage events per host name and event name |
| [`events_stages_summary_by_thread_by_event_name`](performance-schema-stage-summary-tables.md) | Stage waits per thread and event name |
| [`events_stages_summary_by_user_by_event_name`](performance-schema-stage-summary-tables.md) | Stage events per user name and event name |
| [`events_stages_summary_global_by_event_name`](performance-schema-stage-summary-tables.md) | Stage waits per event name |
| [`events_statements_current`](performance-schema-events-statements-current-table.md) | Current statement events |
| [`events_statements_histogram_by_digest`](performance-schema-statement-histogram-summary-tables.md) | Statement histograms per schema and digest value |
| [`events_statements_histogram_global`](performance-schema-statement-histogram-summary-tables.md) | Statement histogram summarized globally |
| [`events_statements_history`](performance-schema-events-statements-history-table.md) | Most recent statement events per thread |
| [`events_statements_history_long`](performance-schema-events-statements-history-long-table.md) | Most recent statement events overall |
| [`events_statements_summary_by_account_by_event_name`](performance-schema-statement-summary-tables.md) | Statement events per account and event name |
| [`events_statements_summary_by_digest`](performance-schema-statement-summary-tables.md) | Statement events per schema and digest value |
| [`events_statements_summary_by_host_by_event_name`](performance-schema-statement-summary-tables.md) | Statement events per host name and event name |
| [`events_statements_summary_by_program`](performance-schema-statement-summary-tables.md) | Statement events per stored program |
| [`events_statements_summary_by_thread_by_event_name`](performance-schema-statement-summary-tables.md) | Statement events per thread and event name |
| [`events_statements_summary_by_user_by_event_name`](performance-schema-statement-summary-tables.md) | Statement events per user name and event name |
| [`events_statements_summary_global_by_event_name`](performance-schema-statement-summary-tables.md) | Statement events per event name |
| [`events_transactions_current`](performance-schema-events-transactions-current-table.md) | Current transaction events |
| [`events_transactions_history`](performance-schema-events-transactions-history-table.md) | Most recent transaction events per thread |
| [`events_transactions_history_long`](performance-schema-events-transactions-history-long-table.md) | Most recent transaction events overall |
| [`events_transactions_summary_by_account_by_event_name`](performance-schema-transaction-summary-tables.md) | Transaction events per account and event name |
| [`events_transactions_summary_by_host_by_event_name`](performance-schema-transaction-summary-tables.md) | Transaction events per host name and event name |
| [`events_transactions_summary_by_thread_by_event_name`](performance-schema-transaction-summary-tables.md) | Transaction events per thread and event name |
| [`events_transactions_summary_by_user_by_event_name`](performance-schema-transaction-summary-tables.md) | Transaction events per user name and event name |
| [`events_transactions_summary_global_by_event_name`](performance-schema-transaction-summary-tables.md) | Transaction events per event name |
| [`events_waits_current`](performance-schema-events-waits-current-table.md) | Current wait events |
| [`events_waits_history`](performance-schema-events-waits-history-table.md) | Most recent wait events per thread |
| [`events_waits_history_long`](performance-schema-events-waits-history-long-table.md) | Most recent wait events overall |
| [`events_waits_summary_by_account_by_event_name`](performance-schema-wait-summary-tables.md) | Wait events per account and event name |
| [`events_waits_summary_by_host_by_event_name`](performance-schema-wait-summary-tables.md) | Wait events per host name and event name |
| [`events_waits_summary_by_instance`](performance-schema-wait-summary-tables.md) | Wait events per instance |
| [`events_waits_summary_by_thread_by_event_name`](performance-schema-wait-summary-tables.md) | Wait events per thread and event name |
| [`events_waits_summary_by_user_by_event_name`](performance-schema-wait-summary-tables.md) | Wait events per user name and event name |
| [`events_waits_summary_global_by_event_name`](performance-schema-wait-summary-tables.md) | Wait events per event name |
| [`file_instances`](performance-schema-file-instances-table.md) | File instances |
| [`file_summary_by_event_name`](performance-schema-file-summary-tables.md) | File events per event name |
| [`file_summary_by_instance`](performance-schema-file-summary-tables.md) | File events per file instance |
| [`firewall_group_allowlist`](performance-schema-firewall-group-allowlist-table.md) | Firewall in-memory data for group profile allowlists |
| [`firewall_groups`](performance-schema-firewall-groups-table.md) | Firewall in-memory data for group profiles |
| [`firewall_membership`](performance-schema-firewall-membership-table.md) | Firewall in-memory data for group profile members |
| [`global_status`](performance-schema-status-variable-tables.md) | Global status variables |
| [`global_variable_attributes`](performance-schema-global-variable-attributes-table.md) | Attribute-value pairs assigned to global variables |
| [`global_variables`](performance-schema-system-variable-tables.md) | Global system variables |
| [`health_block_device`](performance-schema-health-block-device-table.md) | Lists the monitored block device state |
| [`health_process_memory`](performance-schema-health-process-memory-table.md) | Lists the MySQL process memory samples |
| [`health_system_memory`](performance-schema-health-system-memory-table.md) | Lists the system memory samples |
| [`host_cache`](performance-schema-host-cache-table.md) | Information from internal host cache |
| [`hosts`](performance-schema-hosts-table.md) | Connection statistics per client host name |
| [`keyring_component_status`](performance-schema-keyring-component-status-table.md) | Status information for installed keyring component |
| [`keyring_keys`](performance-schema-keyring-keys-table.md) | Metadata for keyring keys |
| [`log_status`](performance-schema-log-status-table.md) | Information about server logs for backup purposes |
| [`memory_summary_by_account_by_event_name`](performance-schema-memory-summary-tables.md) | Memory operations per account and event name |
| [`memory_summary_by_host_by_event_name`](performance-schema-memory-summary-tables.md) | Memory operations per host and event name |
| [`memory_summary_by_thread_by_event_name`](performance-schema-memory-summary-tables.md) | Memory operations per thread and event name |
| [`memory_summary_by_user_by_event_name`](performance-schema-memory-summary-tables.md) | Memory operations per user and event name |
| [`memory_summary_global_by_event_name`](performance-schema-memory-summary-tables.md) | Memory operations globally per event name |
| [`metadata_locks`](performance-schema-metadata-locks-table.md) | Metadata locks and lock requests |
| [`mutex_instances`](performance-schema-mutex-instances-table.md) | Mutex synchronization object instances |
| [`mysql_option`](performance-schema-mysql-option-table.md) | Features known to Option tracker in MySQL server, components, and plugins |
| [`ndb_replication_applier_status`](performance-schema-ndb-replication-applier-status-table.md) | NDB replication applier status information for each replication channel |
| [`ndb_sync_excluded_objects`](performance-schema-ndb-sync-excluded-objects-table.md) | NDB objects which cannot be synchronized |
| [`ndb_sync_pending_objects`](performance-schema-ndb-sync-pending-objects-table.md) | NDB objects waiting for synchronization |
| [`objects_summary_global_by_type`](performance-schema-objects-summary-global-by-type-table.md) | Object summaries |
| [`performance_timers`](performance-schema-performance-timers-table.md) | Which event timers are available |
| [`persisted_variables`](performance-schema-system-variable-tables.md) | Contents of mysqld-auto.cnf file |
| [`prepared_statements_instances`](performance-schema-prepared-statements-instances-table.md) | Prepared statement instances and statistics |
| [`processlist`](performance-schema-processlist-table.md) | Process list information |
| [`replication_applier_configuration`](performance-schema-replication-applier-configuration-table.md) | Configuration parameters for replication applier on replica |
| [`replication_applier_filters`](performance-schema-replication-applier-filters-table.md) | Channel-specific replication filters on current replica |
| [`replication_applier_global_filters`](performance-schema-replication-applier-global-filters-table.md) | Global replication filters on current replica |
| [`replication_applier_status`](performance-schema-replication-applier-status-table.md) | Current status of replication applier on replica |
| [`replication_applier_status_by_coordinator`](performance-schema-replication-applier-status-by-coordinator-table.md) | SQL or coordinator thread applier status |
| [`replication_applier_status_by_worker`](performance-schema-replication-applier-status-by-worker-table.md) | Worker thread applier status |
| [`replication_asynchronous_connection_failover`](performance-schema-replication-asynchronous-connection-failover-table.md) | Source lists for asynchronous connection failover mechanism |
| [`replication_asynchronous_connection_failover_managed`](performance-schema-replication-asynchronous-connection-failover-managed-table.md) | Managed source lists for asynchronous connection failover mechanism |
| [`replication_connection_configuration`](performance-schema-replication-connection-configuration-table.md) | Configuration parameters for connecting to source |
| [`replication_connection_status`](performance-schema-replication-connection-status-table.md) | Current status of connection to source |
| [`replication_group_communication_information`](performance-schema-replication-group-communication-information-table.md) | Replication group configuration options |
| [`replication_group_configuration_version`](performance-schema-replication-group-configuration-version-table.md) | Version of the member actions configuration for replication group members |
| [`replication_group_member_actions`](performance-schema-replication-group-member-actions-table.md) | Member actions that are included in the member actions configuration for replication group members |
| [`replication_group_member_stats`](performance-schema-replication-group-member-stats-table.md) | Replication group member statistics |
| [`replication_group_members`](performance-schema-replication-group-members-table.md) | Replication group member network and status |
| [`rwlock_instances`](performance-schema-rwlock-instances-table.md) | Lock synchronization object instances |
| [`session_account_connect_attrs`](performance-schema-session-account-connect-attrs-table.md) | Connection attributes per for current session |
| [`session_connect_attrs`](performance-schema-session-connect-attrs-table.md) | Connection attributes for all sessions |
| [`session_status`](performance-schema-status-variable-tables.md) | Status variables for current session |
| [`session_variables`](performance-schema-system-variable-tables.md) | System variables for current session |
| [`setup_actors`](performance-schema-setup-actors-table.md) | How to initialize monitoring for new foreground threads |
| [`setup_consumers`](performance-schema-setup-consumers-table.md) | Consumers for which event information can be stored |
| [`setup_instruments`](performance-schema-setup-instruments-table.md) | Classes of instrumented objects for which events can be collected |
| [`setup_loggers`](performance-schema-setup-loggers-table.md) | Lists the registered loggers and their logging level |
| [`setup_meters`](performance-schema-setup-meters-table.md) | Lists the registered meters and their frequency |
| [`setup_metrics`](performance-schema-setup-metrics-table.md) | Lists the available metrics |
| [`setup_objects`](performance-schema-setup-objects-table.md) | Which objects should be monitored |
| [`setup_threads`](performance-schema-setup-threads-table.md) | Instrumented thread names and attributes |
| [`socket_instances`](performance-schema-socket-instances-table.md) | Active connection instances |
| [`socket_summary_by_event_name`](performance-schema-socket-summary-tables.md) | Socket waits and I/O per event name |
| [`socket_summary_by_instance`](performance-schema-socket-summary-tables.md) | Socket waits and I/O per instance |
| [`status_by_account`](performance-schema-status-variable-summary-tables.md) | Session status variables per account |
| [`status_by_host`](performance-schema-status-variable-summary-tables.md) | Session status variables per host name |
| [`status_by_thread`](performance-schema-status-variable-tables.md) | Session status variables per session |
| [`status_by_user`](performance-schema-status-variable-summary-tables.md) | Session status variables per user name |
| [`system_cpu_stats`](performance-schema-system-cpu-stats-table.md) | Lists the current CPU statistics |
| [`system_cpu_stats_history`](performance-schema-system-cpu-stats-history-table.md) | Lists the historical CPU statistics |
| [`system_disk_stats`](performance-schema-system-disk-stats-table.md) | Lists the current disk statistics |
| [`system_disk_stats_history`](performance-schema-system-disk-stats-history-table.md) | Lists the historical disk statistics |
| [`system_memory_stats`](performance-schema-system-memory-stats-table.md) | Lists the current system memory statistics |
| [`system_memory_stats_history`](performance-schema-system-memory-stats-history-table.md) | Lists the historical system memory statistics |
| [`system_process_stats`](performance-schema-system-process-stats-table.md) | Lists the current MySQL process statistics |
| [`system_process_stats_history`](performance-schema-system-process-stats-history-table.md) | Lists the historical MySQL process statistics |
| [`table_handles`](performance-schema-table-handles-table.md) | Table locks and lock requests |
| [`table_io_waits_summary_by_index_usage`](performance-schema-table-wait-summary-tables.md) | Table I/O waits per index |
| [`table_io_waits_summary_by_table`](performance-schema-table-wait-summary-tables.md) | Table I/O waits per table |
| [`table_lock_waits_summary_by_table`](performance-schema-table-wait-summary-tables.md) | Table lock waits per table |
| [`threads`](performance-schema-threads-table.md) | Information about server threads |
| [`tls_channel_status`](performance-schema-tls-channel-status-table.md) | TLS status for each connection interface |
| [`tp_thread_group_state`](performance-schema-tp-thread-group-state-table.md) | Thread pool thread group states |
| [`tp_thread_group_stats`](performance-schema-tp-thread-group-stats-table.md) | Thread pool thread group statistics |
| [`tp_thread_state`](performance-schema-tp-thread-state-table.md) | Thread pool thread information |
| [`user_defined_functions`](performance-schema-user-defined-functions-table.md) | Registered loadable functions |
| [`user_variables_by_thread`](performance-schema-user-variable-tables.md) | User-defined variables per thread |
| [`users`](performance-schema-users-table.md) | Connection statistics per client user name |
| [`variables_by_thread`](performance-schema-system-variable-tables.md) | Session system variables per session |
| [`variables_info`](performance-schema-system-variable-tables.md) | How system variables were most recently set |
| [`variables_metadata`](performance-schema-system-variable-tables.md) | System variable metadata, including scope, type, range, and description |