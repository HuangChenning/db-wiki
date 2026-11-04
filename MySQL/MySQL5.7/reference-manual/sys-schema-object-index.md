---
title: "26.4.1 sys Schema Object Index"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/sys-schema-object-index.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 26.4.1 sys Schema Object Index

The following tables list [`sys`](sys-schema.md) schema objects and provide a short description of each one.

**Table 26.1 sys Schema Tables and Triggers**

| Table or Trigger Name | Description |
| --- | --- |
| [`sys_config`](sys-sys-config.md) | sys schema configuration options table |
| [`sys_config_insert_set_user`](sys-sys-config-insert-set-user.md) | sys\_config insert trigger |
| [`sys_config_update_set_user`](sys-sys-config-update-set-user.md) | sys\_config update trigger |

**Table 26.2 sys Schema Views**

| View Name | Description | Deprecated |
| --- | --- | --- |
| [`host_summary`, `x$host_summary`](sys-host-summary.md) | Statement activity, file I/O, and connections, grouped by host |  |
| [`host_summary_by_file_io`, `x$host_summary_by_file_io`](sys-host-summary-by-file-io.md) | File I/O, grouped by host |  |
| [`host_summary_by_file_io_type`, `x$host_summary_by_file_io_type`](sys-host-summary-by-file-io-type.md) | File I/O, grouped by host and event type |  |
| [`host_summary_by_stages`, `x$host_summary_by_stages`](sys-host-summary-by-stages.md) | Statement stages, grouped by host |  |
| [`host_summary_by_statement_latency`, `x$host_summary_by_statement_latency`](sys-host-summary-by-statement-latency.md) | Statement statistics, grouped by host |  |
| [`host_summary_by_statement_type`, `x$host_summary_by_statement_type`](sys-host-summary-by-statement-type.md) | Statements executed, grouped by host and statement |  |
| [`innodb_buffer_stats_by_schema`, `x$innodb_buffer_stats_by_schema`](sys-innodb-buffer-stats-by-schema.md) | InnoDB buffer information, grouped by schema |  |
| [`innodb_buffer_stats_by_table`, `x$innodb_buffer_stats_by_table`](sys-innodb-buffer-stats-by-table.md) | InnoDB buffer information, grouped by schema and table |  |
| [`innodb_lock_waits`, `x$innodb_lock_waits`](sys-innodb-lock-waits.md) | InnoDB lock information |  |
| [`io_by_thread_by_latency`, `x$io_by_thread_by_latency`](sys-io-by-thread-by-latency.md) | I/O consumers, grouped by thread |  |
| [`io_global_by_file_by_bytes`, `x$io_global_by_file_by_bytes`](sys-io-global-by-file-by-bytes.md) | Global I/O consumers, grouped by file and bytes |  |
| [`io_global_by_file_by_latency`, `x$io_global_by_file_by_latency`](sys-io-global-by-file-by-latency.md) | Global I/O consumers, grouped by file and latency |  |
| [`io_global_by_wait_by_bytes`, `x$io_global_by_wait_by_bytes`](sys-io-global-by-wait-by-bytes.md) | Global I/O consumers, grouped by bytes |  |
| [`io_global_by_wait_by_latency`, `x$io_global_by_wait_by_latency`](sys-io-global-by-wait-by-latency.md) | Global I/O consumers, grouped by latency |  |
| [`latest_file_io`, `x$latest_file_io`](sys-latest-file-io.md) | Most recent I/O, grouped by file and thread |  |
| [`memory_by_host_by_current_bytes`, `x$memory_by_host_by_current_bytes`](sys-memory-by-host-by-current-bytes.md) | Memory use, grouped by host |  |
| [`memory_by_thread_by_current_bytes`, `x$memory_by_thread_by_current_bytes`](sys-memory-by-thread-by-current-bytes.md) | Memory use, grouped by thread |  |
| [`memory_by_user_by_current_bytes`, `x$memory_by_user_by_current_bytes`](sys-memory-by-user-by-current-bytes.md) | Memory use, grouped by user |  |
| [`memory_global_by_current_bytes`, `x$memory_global_by_current_bytes`](sys-memory-global-by-current-bytes.md) | Memory use, grouped by allocation type |  |
| [`memory_global_total`, `x$memory_global_total`](sys-memory-global-total.md) | Total memory use |  |
| [`metrics`](sys-metrics.md) | Server metrics |  |
| [`processlist`, `x$processlist`](sys-processlist.md) | Processlist information |  |
| [`ps_check_lost_instrumentation`](sys-ps-check-lost-instrumentation.md) | Variables that have lost instruments |  |
| [`schema_auto_increment_columns`](sys-schema-auto-increment-columns.md) | AUTO\_INCREMENT column information |  |
| [`schema_index_statistics`, `x$schema_index_statistics`](sys-schema-index-statistics.md) | Index statistics |  |
| [`schema_object_overview`](sys-schema-object-overview.md) | Types of objects within each schema |  |
| [`schema_redundant_indexes`](sys-schema-redundant-indexes.md) | Duplicate or redundant indexes |  |
| [`schema_table_lock_waits`, `x$schema_table_lock_waits`](sys-schema-table-lock-waits.md) | Sessions waiting for metadata locks |  |
| [`schema_table_statistics`, `x$schema_table_statistics`](sys-schema-table-statistics.md) | Table statistics |  |
| [`schema_table_statistics_with_buffer`, `x$schema_table_statistics_with_buffer`](sys-schema-table-statistics-with-buffer.md) | Table statistics, including InnoDB buffer pool statistics |  |
| [`schema_tables_with_full_table_scans`, `x$schema_tables_with_full_table_scans`](sys-schema-tables-with-full-table-scans.md) | Tables being accessed with full scans |  |
| [`schema_unused_indexes`](sys-schema-unused-indexes.md) | Indexes not in active use |  |
| [`session`, `x$session`](sys-session.md) | Processlist information for user sessions |  |
| [`session_ssl_status`](sys-session-ssl-status.md) | Connection SSL information |  |
| [`statement_analysis`, `x$statement_analysis`](sys-statement-analysis.md) | Statement aggregate statistics |  |
| [`statements_with_errors_or_warnings`, `x$statements_with_errors_or_warnings`](sys-statements-with-errors-or-warnings.md) | Statements that have produced errors or warnings |  |
| [`statements_with_full_table_scans`, `x$statements_with_full_table_scans`](sys-statements-with-full-table-scans.md) | Statements that have done full table scans |  |
| [`statements_with_runtimes_in_95th_percentile`, `x$statements_with_runtimes_in_95th_percentile`](sys-statements-with-runtimes-in-95th-percentile.md) | Statements with highest average runtime |  |
| [`statements_with_sorting`, `x$statements_with_sorting`](sys-statements-with-sorting.md) | Statements that performed sorts |  |
| [`statements_with_temp_tables`, `x$statements_with_temp_tables`](sys-statements-with-temp-tables.md) | Statements that used temporary tables |  |
| [`user_summary`, `x$user_summary`](sys-user-summary.md) | User statement and connection activity |  |
| [`user_summary_by_file_io`, `x$user_summary_by_file_io`](sys-user-summary-by-file-io.md) | File I/O, grouped by user |  |
| [`user_summary_by_file_io_type`, `x$user_summary_by_file_io_type`](sys-user-summary-by-file-io-type.md) | File I/O, grouped by user and event |  |
| [`user_summary_by_stages`, `x$user_summary_by_stages`](sys-user-summary-by-stages.md) | Stage events, grouped by user |  |
| [`user_summary_by_statement_latency`, `x$user_summary_by_statement_latency`](sys-user-summary-by-statement-latency.md) | Statement statistics, grouped by user |  |
| [`user_summary_by_statement_type`, `x$user_summary_by_statement_type`](sys-user-summary-by-statement-type.md) | Statements executed, grouped by user and statement |  |
| [`version`](sys-version.md) | Current sys schema and MySQL server versions | Yes |
| [`wait_classes_global_by_avg_latency`, `x$wait_classes_global_by_avg_latency`](sys-wait-classes-global-by-avg-latency.md) | Wait class average latency, grouped by event class |  |
| [`wait_classes_global_by_latency`, `x$wait_classes_global_by_latency`](sys-wait-classes-global-by-latency.md) | Wait class total latency, grouped by event class |  |
| [`waits_by_host_by_latency`, `x$waits_by_host_by_latency`](sys-waits-by-host-by-latency.md) | Wait events, grouped by host and event |  |
| [`waits_by_user_by_latency`, `x$waits_by_user_by_latency`](sys-waits-by-user-by-latency.md) | Wait events, grouped by user and event |  |
| [`waits_global_by_latency`, `x$waits_global_by_latency`](sys-waits-global-by-latency.md) | Wait events, grouped by event |  |
| [`x$ps_digest_95th_percentile_by_avg_us`](sys-statements-with-runtimes-in-95th-percentile.md) | Helper view for 95th-percentile views |  |
| [`x$ps_digest_avg_latency_distribution`](sys-statements-with-runtimes-in-95th-percentile.md) | Helper view for 95th-percentile views |  |
| [`x$ps_schema_table_statistics_io`](sys-schema-table-statistics.md) | Helper view for table-statistics views |  |
| [`x$schema_flattened_keys`](sys-schema-redundant-indexes.md) | Helper view for schema\_redundant\_indexes |  |

**Table 26.3 sys Schema Stored Procedures**

| Procedure Name | Description |
| --- | --- |
| [`create_synonym_db()`](sys-create-synonym-db.md) | Create synonym for schema |
| [`diagnostics()`](sys-diagnostics.md) | Collect system diagnostic information |
| [`execute_prepared_stmt()`](sys-execute-prepared-stmt.md) | Execute prepared statement |
| [`ps_setup_disable_background_threads()`](sys-ps-setup-disable-background-threads.md) | Disable background thread instrumentation |
| [`ps_setup_disable_consumer()`](sys-ps-setup-disable-consumer.md) | Disable consumers |
| [`ps_setup_disable_instrument()`](sys-ps-setup-disable-instrument.md) | Disable instruments |
| [`ps_setup_disable_thread()`](sys-ps-setup-disable-thread.md) | Disable instrumentation for thread |
| [`ps_setup_enable_background_threads()`](sys-ps-setup-enable-background-threads.md) | Enable background thread instrumentation |
| [`ps_setup_enable_consumer()`](sys-ps-setup-enable-consumer.md) | Enable consumers |
| [`ps_setup_enable_instrument()`](sys-ps-setup-enable-instrument.md) | Enable instruments |
| [`ps_setup_enable_thread()`](sys-ps-setup-enable-thread.md) | Enable instrumentation for thread |
| [`ps_setup_reload_saved()`](sys-ps-setup-reload-saved.md) | Reload saved Performance Schema configuration |
| [`ps_setup_reset_to_default()`](sys-ps-setup-reset-to-default.md) | Reset saved Performance Schema configuration |
| [`ps_setup_save()`](sys-ps-setup-save.md) | Save Performance Schema configuration |
| [`ps_setup_show_disabled()`](sys-ps-setup-show-disabled.md) | Display disabled Performance Schema configuration |
| [`ps_setup_show_disabled_consumers()`](sys-ps-setup-show-disabled-consumers.md) | Display disabled Performance Schema consumers |
| [`ps_setup_show_disabled_instruments()`](sys-ps-setup-show-disabled-instruments.md) | Display disabled Performance Schema instruments |
| [`ps_setup_show_enabled()`](sys-ps-setup-show-enabled.md) | Display enabled Performance Schema configuration |
| [`ps_setup_show_enabled_consumers()`](sys-ps-setup-show-enabled-consumers.md) | Display enabled Performance Schema consumers |
| [`ps_setup_show_enabled_instruments()`](sys-ps-setup-show-enabled-instruments.md) | Display enabled Performance Schema instruments |
| [`ps_statement_avg_latency_histogram()`](sys-ps-statement-avg-latency-histogram.md) | Display statement latency histogram |
| [`ps_trace_statement_digest()`](sys-ps-trace-statement-digest.md) | Trace Performance Schema instrumentation for digest |
| [`ps_trace_thread()`](sys-ps-trace-thread.md) | Dump Performance Schema data for thread |
| [`ps_truncate_all_tables()`](sys-ps-truncate-all-tables.md) | Truncate Performance Schema summary tables |
| [`statement_performance_analyzer()`](sys-statement-performance-analyzer.md) | Report of statements running on server |
| [`table_exists()`](sys-table-exists.md) | Whether a table exists |

**Table 26.4 sys Schema Stored Functions**

| Function Name | Description |
| --- | --- |
| [`extract_schema_from_file_name()`](sys-extract-schema-from-file-name.md) | Extract schema name part of file name |
| [`extract_table_from_file_name()`](sys-extract-table-from-file-name.md) | Extract table name part of file name |
| [`format_bytes()`](sys-format-bytes.md) | Convert byte count to value with units |
| [`format_path()`](sys-format-path.md) | Replace directories in path name with symbolic system variable names |
| [`format_statement()`](sys-format-statement.md) | Truncate long statement to fixed length |
| [`format_time()`](sys-format-time.md) | Convert picoseconds time to value with units |
| [`list_add()`](sys-list-add.md) | Add item to list |
| [`list_drop()`](sys-list-drop.md) | Remove item from list |
| [`ps_is_account_enabled()`](sys-ps-is-account-enabled.md) | Whether Performance Schema instrumentation for account is enabled |
| [`ps_is_consumer_enabled()`](sys-ps-is-consumer-enabled.md) | Whether Performance Schema consumer is enabled |
| [`ps_is_instrument_default_enabled()`](sys-ps-is-instrument-default-enabled.md) | Whether Performance Schema instrument is enabled by default |
| [`ps_is_instrument_default_timed()`](sys-ps-is-instrument-default-timed.md) | Whether Performance Schema instrument is timed by default |
| [`ps_is_thread_instrumented()`](sys-ps-is-thread-instrumented.md) | Whether Performance Schema instrumentation for connection ID is enabled |
| [`ps_thread_account()`](sys-ps-thread-account.md) | Account associated with Performance Schema thread ID |
| [`ps_thread_id()`](sys-ps-thread-id.md) | Performance Schema thread ID associated with connection ID |
| [`ps_thread_stack()`](sys-ps-thread-stack.md) | Event information for connection ID |
| [`ps_thread_trx_info()`](sys-ps-thread-trx-info.md) | Transaction information for thread ID |
| [`quote_identifier()`](sys-quote-identifier.md) | Quote string as identifier |
| [`sys_get_config()`](sys-sys-get-config.md) | sys schema configuration option value |
| [`version_major()`](sys-version-major.md) | MySQL server major version number |
| [`version_minor()`](sys-version-minor.md) | MySQL server minor version number |
| [`version_patch()`](sys-version-patch.md) | MySQL server patch release version number |