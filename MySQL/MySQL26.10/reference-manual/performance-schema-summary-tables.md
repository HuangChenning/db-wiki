---
title: "MySQL :: MySQL 26.10 Reference Manual :: 29.12.20 Performance Schema Summary Tables"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/performance-schema-summary-tables.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 29.12.20 Performance Schema Summary Tables

Summary tables provide aggregated information for terminated events over time. The tables in this group summarize event data in different ways.

Each summary table has grouping columns that determine how to group the data to be aggregated, and summary columns that contain the aggregated values. Tables that summarize events in similar ways often have similar sets of summary columns and differ only in the grouping columns used to determine how events are aggregated.

Summary tables can be truncated with [`TRUNCATE TABLE`](truncate-table.md). Generally, the effect is to reset the summary columns to 0 or `NULL`, not to remove rows. This enables you to clear collected values and restart aggregation. That might be useful, for example, after you have made a runtime configuration change. Exceptions to this truncation behavior are noted in individual summary table sections.

#### Wait Event Summaries

**Table 29.5 Performance Schema Wait Event Summary Tables**

| Table Name | Description |
| --- | --- |
| [`events_waits_summary_by_account_by_event_name`](performance-schema-wait-summary-tables.md) | Wait events per account and event name |
| [`events_waits_summary_by_host_by_event_name`](performance-schema-wait-summary-tables.md) | Wait events per host name and event name |
| [`events_waits_summary_by_instance`](performance-schema-wait-summary-tables.md) | Wait events per instance |
| [`events_waits_summary_by_thread_by_event_name`](performance-schema-wait-summary-tables.md) | Wait events per thread and event name |
| [`events_waits_summary_by_user_by_event_name`](performance-schema-wait-summary-tables.md) | Wait events per user name and event name |
| [`events_waits_summary_global_by_event_name`](performance-schema-wait-summary-tables.md) | Wait events per event name |

#### Stage Summaries

**Table 29.6 Performance Schema Stage Event Summary Tables**

| Table Name | Description |
| --- | --- |
| [`events_stages_summary_by_account_by_event_name`](performance-schema-stage-summary-tables.md) | Stage events per account and event name |
| [`events_stages_summary_by_host_by_event_name`](performance-schema-stage-summary-tables.md) | Stage events per host name and event name |
| [`events_stages_summary_by_thread_by_event_name`](performance-schema-stage-summary-tables.md) | Stage waits per thread and event name |
| [`events_stages_summary_by_user_by_event_name`](performance-schema-stage-summary-tables.md) | Stage events per user name and event name |
| [`events_stages_summary_global_by_event_name`](performance-schema-stage-summary-tables.md) | Stage waits per event name |

#### Statement Summaries

**Table 29.7 Performance Schema Statement Event Summary Tables**

| Table Name | Description |
| --- | --- |
| [`events_statements_histogram_by_digest`](performance-schema-statement-histogram-summary-tables.md) | Statement histograms per schema and digest value |
| [`events_statements_histogram_global`](performance-schema-statement-histogram-summary-tables.md) | Statement histogram summarized globally |
| [`events_statements_summary_by_account_by_event_name`](performance-schema-statement-summary-tables.md) | Statement events per account and event name |
| [`events_statements_summary_by_digest`](performance-schema-statement-summary-tables.md) | Statement events per schema and digest value |
| [`events_statements_summary_by_host_by_event_name`](performance-schema-statement-summary-tables.md) | Statement events per host name and event name |
| [`events_statements_summary_by_program`](performance-schema-statement-summary-tables.md) | Statement events per stored program |
| [`events_statements_summary_by_thread_by_event_name`](performance-schema-statement-summary-tables.md) | Statement events per thread and event name |
| [`events_statements_summary_by_user_by_event_name`](performance-schema-statement-summary-tables.md) | Statement events per user name and event name |
| [`events_statements_summary_global_by_event_name`](performance-schema-statement-summary-tables.md) | Statement events per event name |
| [`prepared_statements_instances`](performance-schema-prepared-statements-instances-table.md) | Prepared statement instances and statistics |

#### Transaction Summaries

**Table 29.8 Performance Schema Transaction Event Summary Tables**

| Table Name | Description |
| --- | --- |
| [`events_transactions_summary_by_account_by_event_name`](performance-schema-transaction-summary-tables.md) | Transaction events per account and event name |
| [`events_transactions_summary_by_host_by_event_name`](performance-schema-transaction-summary-tables.md) | Transaction events per host name and event name |
| [`events_transactions_summary_by_thread_by_event_name`](performance-schema-transaction-summary-tables.md) | Transaction events per thread and event name |
| [`events_transactions_summary_by_user_by_event_name`](performance-schema-transaction-summary-tables.md) | Transaction events per user name and event name |
| [`events_transactions_summary_global_by_event_name`](performance-schema-transaction-summary-tables.md) | Transaction events per event name |

#### Object Wait Summaries

**Table 29.9 Performance Schema Object Event Summary Tables**

| Table Name | Description |
| --- | --- |
| [`objects_summary_global_by_type`](performance-schema-objects-summary-global-by-type-table.md) | Object summaries |

#### File I/O Summaries

**Table 29.10 Performance Schema File I/O Event Summary Tables**

| Table Name | Description |
| --- | --- |
| [`file_summary_by_event_name`](performance-schema-file-summary-tables.md) | File events per event name |
| [`file_summary_by_instance`](performance-schema-file-summary-tables.md) | File events per file instance |

#### Table I/O and Lock Wait Summaries

**Table 29.11 Performance Schema Table I/O and Lock Wait Event Summary Tables**

| Table Name | Description |
| --- | --- |
| [`table_io_waits_summary_by_index_usage`](performance-schema-table-wait-summary-tables.md) | Table I/O waits per index |
| [`table_io_waits_summary_by_table`](performance-schema-table-wait-summary-tables.md) | Table I/O waits per table |
| [`table_lock_waits_summary_by_table`](performance-schema-table-wait-summary-tables.md) | Table lock waits per table |

#### Socket Summaries

**Table 29.12 Performance Schema Socket Event Summary Tables**

| Table Name | Description |
| --- | --- |
| [`socket_summary_by_event_name`](performance-schema-socket-summary-tables.md) | Socket waits and I/O per event name |
| [`socket_summary_by_instance`](performance-schema-socket-summary-tables.md) | Socket waits and I/O per instance |

#### Memory Summaries

**Table 29.13 Performance Schema Memory Operation Summary Tables**

| Table Name | Description |
| --- | --- |
| [`memory_summary_by_account_by_event_name`](performance-schema-memory-summary-tables.md) | Memory operations per account and event name |
| [`memory_summary_by_host_by_event_name`](performance-schema-memory-summary-tables.md) | Memory operations per host and event name |
| [`memory_summary_by_thread_by_event_name`](performance-schema-memory-summary-tables.md) | Memory operations per thread and event name |
| [`memory_summary_by_user_by_event_name`](performance-schema-memory-summary-tables.md) | Memory operations per user and event name |
| [`memory_summary_global_by_event_name`](performance-schema-memory-summary-tables.md) | Memory operations globally per event name |

#### Error Summaries

**Table 29.14 Performance Schema Error Summary Tables**

| Table Name | Description |
| --- | --- |
| [`events_errors_summary_by_account_by_error`](performance-schema-error-summary-tables.md) | Errors per account and error code |
| [`events_errors_summary_by_host_by_error`](performance-schema-error-summary-tables.md) | Errors per host and error code |
| [`events_errors_summary_by_thread_by_error`](performance-schema-error-summary-tables.md) | Errors per thread and error code |
| [`events_errors_summary_by_user_by_error`](performance-schema-error-summary-tables.md) | Errors per user and error code |
| [`events_errors_summary_global_by_error`](performance-schema-error-summary-tables.md) | Errors per error code |

#### Status Variable Summaries

**Table 29.15 Performance Schema Error Status Variable Summary Tables**

| Table Name | Description |
| --- | --- |
| [`status_by_account`](performance-schema-status-variable-summary-tables.md) | Session status variables per account |
| [`status_by_host`](performance-schema-status-variable-summary-tables.md) | Session status variables per host name |
| [`status_by_user`](performance-schema-status-variable-summary-tables.md) | Session status variables per user name |