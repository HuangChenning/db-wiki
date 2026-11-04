---
title: "3.5 Changes in MySQL 8.4"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/upgrading-from-previous-series.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

Before upgrading to MySQL 8.4, review the changes described in the following sections to identify those that apply to your current MySQL installation and applications.

In addition, you can consult the resources listed here:

- [Section 1.4, “What Is New in MySQL 8.4 since MySQL 8.0”](mysql-nutshell.md)
- [MySQL 8.4 Release Notes](https://docs.oracle.com/cd/E17952_01/mysql-8.4-relnotes-en/)

### Incompatible Changes in MySQL 8.4

This section contains information about incompatible changes in MySQL 8.4.

- **Spatial indexes.** When upgrading to MySQL 8.4.4 or later, it is recommended that you drop any spatial indexes beforehand, then re-create them after the upgrade is complete. Alternatively, you can drop and re-create such indexes immediately following the upgrade, but before making use of any of the tables in which they occur.
	For more information, see [Section 13.4.10, “Creating Spatial Indexes”](creating-spatial-indexes.md).
- **WAIT\_UNTIL\_SQL\_THREAD\_AFTER\_GTIDS() function removed.** The `WAIT_UNTIL_SQL_THREAD_AFTER_GTIDS()` SQL function, deprecated in MySQL 8.0 has been removed; attempting to invoke it now causes a syntax error. Use [`WAIT_FOR_EXECUTED_GTID_SET()`](gtid-functions.md) instead.
- **`authentication_fido` and `authentication_fido_client` no longer available on some platforms.** Due to upgrading the libfido2 library bundled with the server to version 1.13.0, which requires OpenSSL 1.1.1 or higher, the `authentication_fido` and `authentication_fido_client` authentication plugins are no longer available on Enterprise Linux 6, Enterprise Linux 7, Solaris 11, or SUSE Enterprise Linux 12.
- **NULL disallowed for command-line options.** Setting server variables equal to SQL `NULL` on the command line is not supported. In MySQL 8.4, setting any of these to `NULL` is specifically disallowed, and attempting to do is rejected with an error.
	The following variables are excepted from this restriction: [`admin_ssl_ca`](server-system-variables.md), [`admin_ssl_capath`](server-system-variables.md), [`admin_ssl_cert`](server-system-variables.md), [`admin_ssl_cipher`](server-system-variables.md), [`admin_tls_ciphersuites`](server-system-variables.md), [`admin_ssl_key`](server-system-variables.md), [`admin_ssl_crl`](server-system-variables.md), [`admin_ssl_crlpath`](server-system-variables.md), [`basedir`](server-system-variables.md), [`character_sets_dir`](server-system-variables.md), [`ft_stopword_file`](server-system-variables.md), [`group_replication_recovery_tls_ciphersuites`](group-replication-system-variables.md), [`init_file`](server-system-variables.md), [`lc_messages_dir`](server-system-variables.md), [`plugin_dir`](server-system-variables.md), [`relay_log`](replication-options-replica.md), [`relay_log_info_file`](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/replication-options-replica.html#sysvar_relay_log_info_file), [`replica_load_tmpdir`](replication-options-replica.md), [`ssl_ca`](server-system-variables.md), [`ssl_capath`](server-system-variables.md), [`ssl_cert`](server-system-variables.md), [`ssl_cipher`](server-system-variables.md), [`ssl_crl`](server-system-variables.md), [`ssl_crlpath`](server-system-variables.md), [`ssl_key`](server-system-variables.md), [`socket`](server-system-variables.md), [`tls_ciphersuites`](server-system-variables.md), and [`tmpdir`](server-system-variables.md).
	See also [Section 7.1.8, “Server System Variables”](server-system-variables.md).

For additional information about changes in MySQL 8.4, see [Section 1.4, “What Is New in MySQL 8.4 since MySQL 8.0”](mysql-nutshell.md).

### Changed Server Defaults

This section contains information about MySQL server system variables whose default values have changed in MySQL 8.4 as compared to MySQL 8.0.

| System Variable | Old Default | New Default |
| --- | --- | --- |
| *InnoDB changes* |  |  |
| [`innodb_adaptive_hash_index`](innodb-parameters.md) | `ON` | `OFF` |
| [`innodb_buffer_pool_in_core_file`](innodb-parameters.md) | `ON` | `OFF` |
| [`innodb_buffer_pool_instances`](innodb-parameters.md) | [`innodb_buffer_pool_size`](innodb-parameters.md) < 1GB: 1; otherwise: 8 | [`innodb_buffer_pool_size`](innodb-parameters.md) <= 1GB: 1; otherwise: [`MIN`](aggregate-functions.md) `(               0.5 *               (`[`innodb_buffer_pool_size`](innodb-parameters.md) `                /                ` [`innodb_buffer_pool_chunk_size`](innodb-parameters.md)``),               0.25 *               *`number_of_cpus`*)`` |
| [`innodb_change_buffering`](innodb-parameters.md) | `all` | `none` |
| [`innodb_doublewrite_files`](innodb-parameters.md) | [`innodb_buffer_pool_instances`](innodb-parameters.md) ` *               2` | 2 |
| [`innodb_doublewrite_pages`](innodb-parameters.md) | Value of [`innodb_write_io_threads`](innodb-parameters.md) | 128 |
| [`innodb_flush_method`](innodb-parameters.md) | `fsync` | `O_DIRECT` if supported, otherwise `fsync` |
| [`innodb_io_capacity`](innodb-parameters.md) | 200 | 10000 |
| [`innodb_io_capacity_max`](innodb-parameters.md) | `MIN(2 *               ` [`innodb_io_capacity`](innodb-parameters.md)`,               2000)` | `2 * innodb_io_capacity` |
| [`innodb_log_buffer_size`](innodb-parameters.md) | 16777216 | 67108864 |
| [`innodb_numa_interleave`](innodb-parameters.md) | `OFF` | `ON` |
| [`innodb_page_cleaners`](innodb-parameters.md) | 4 | Value of [`innodb_buffer_pool_instances`](innodb-parameters.md) |
| [`innodb_parallel_read_threads`](innodb-parameters.md) | 4 | ``MIN(*`number_of_cpus`* / 8, 4)`` |
| [`innodb_purge_threads`](innodb-parameters.md) | 4 | If number\_of\_cpus <= 16: 1; otherwise: 4 |
| [`innodb_use_fdatasync`](innodb-parameters.md) | `OFF` | `ON` |
| *Group Replication changes* |  |  |
| [`group_replication_consistency`](group-replication-system-variables.md) | `EVENTUAL` | `BEFORE_ON_PRIMARY_FAILOVER` |
| [`group_replication_exit_state_action`](group-replication-system-variables.md) | `READ_ONLY` | `OFFLINE_MODE` |
| *Temporary table changes* |  |  |
| [`temptable_max_mmap`](server-system-variables.md) | 1073741824 | 0 |
| [`temptable_max_ram`](server-system-variables.md) | 1073741824 | 3% of total memory within a range of 1-4 (GB) |
| [`temptable_use_mmap`](server-system-variables.md) | `ON` | `OFF` |

For more information about options or variables which have been added, see [Option and Variable Changes for MySQL 8.4](https://dev.mysql.com/doc/mysqld-version-reference/en/optvar-changes-8-4.html), in the *MySQL Server Version Reference*.

Although the new defaults are the best configuration choices for most use cases, there are special cases, as well as legacy reasons for using existing configuration choices. For example, some people prefer to upgrade to MySQL 8.4 with as few changes to their applications or operational environment as possible. We recommend to evaluate all the new defaults and use as many as you can.

The Performance Schema [`variables_info`](performance-schema-variables-info-table.md) table shows, for each system variable, the source from which it was most recently set, as well as its range of values. This provides SQL access to all there is to know about a system variable and its values.