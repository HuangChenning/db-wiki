---
title: "MySQL :: MySQL 26.10 Reference Manual :: 1.5 Server and Status Variables and Options Added, Deprecated, or Removed in\n    MySQL 26.10"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/added-deprecated-removed.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

## 1.5 Server and Status Variables and Options Added, Deprecated, or Removed in MySQL 26.10

This section lists server variables, status variables, and options that were added for the first time, have been deprecated, or have been removed in MySQL 26.10.

### Options and Variables Introduced in MySQL 26.10

The following system variables, status variables, and server options have been added in MySQL 26.10.

- `disk_forecaster_run_mode`: Current Disk Forecaster mode. Added in MySQL 26.10.0.
- `disk_forecaster_test_state`: Current state of disk forecasting test or simulation. Added in MySQL 26.10.0.
- `health_monitor.disk_fallback_enable`: Enable disk collection.. Added in MySQL 26.10.0.
- `health_monitor.disk_fallback_force`: Permit termination of blocking foreground sessions during fencing. Added in MySQL 26.10.0.
- `health_monitor.disk_forecast_report_interval`: Disk forecast metric interval in seconds. Added in MySQL 26.10.0.
- `health_monitor.disk_forecast_run_mode`: Disk Forecaster operating mode. Added in MySQL 26.10.0.
- `health_monitor.disk_forecast_running`: Enable disk metric collection and forecasting. Added in MySQL 26.10.0.
- `health_monitor.disk_forecast_sample_interval`: Disk forecast metric interval in seconds. Added in MySQL 26.10.0.
- `health_monitor.disk_forecast_test_filename`: Input file selected for TEST mode. Added in MySQL 26.10.0.
- `health_monitor.disk_low_space_critical_level`: Critical low space threshold in MiB for immediate fencing when fencing is enabled. Added in MySQL 26.10.0.
- `health_monitor.disk_low_space_duration`: Seconds below the low space threshold before fencing. Added in MySQL 26.10.0.
- `health_monitor.disk_low_space_level`: Seconds below the low space threshold before fencing. Added in MySQL 26.10.0.
- `health_monitor.disk_low_space_percent`: Low space threshold as a percentage of filesystem capacity, used with the fixed threshold. Added in MySQL 26.10.0.
- `health_monitor.disk_monitored`: Path on the filesystem to monitor. Empty selects the data directory filesystem. Added in MySQL 26.10.0.
- `health_monitor.disk_recovery_enable`: Enable automatic recovery from Health Monitor fencing. Added in MySQL 26.10.0.
- `health_monitor.disk_recovery_increment`: Delay in seconds added after each recovery cycle. Added in MySQL 26.10.0.
- `health_monitor.disk_recovery_level`: Free space percentage above the reserve required to start recovery. Added in MySQL 26.10.0.
- `health_monitor.disk_recovery_max_cycles`: Maximum number of automatic recovery cycles within the recovery window. Added in MySQL 26.10.0.
- `health_monitor.disk_recovery_time_1`: Seconds above the recovery level before clearing Health Monitor-owned OFFLINE\_MODE. Added in MySQL 26.10.0.
- `health_monitor.disk_recovery_time_2`: Additional seconds above the recovery level before clearing Health Monitor-owned SUPER\_READ\_ONLY. Added in MySQL 26.10.0.
- `health_monitor.disk_recovery_window`: Window in seconds used to reset the recovery cycle count. Added in MySQL 26.10.0.
- `health_monitor.disk_retention`: Disk sample retention in seconds. Added in MySQL 26.10.0.
- `health_monitor.disk_running`: Enable disk collection.. Added in MySQL 26.10.0.
- `health_monitor.disk_sample_rate`: Disk sample interval in seconds. Added in MySQL 26.10.0.
- `health_monitor.disk_usage_warning_level_1`: First warning level as a percentage above reserved free space. Added in MySQL 26.10.0.
- `health_monitor.disk_usage_warning_level_2`: Second warning level as a percentage above reserved free space. Added in MySQL 26.10.0.
- `health_monitor.disk_usage_warning_level_3`: Third warning level as a percentage above reserved free space. Added in MySQL 26.10.0.
- `health_monitor.memory_report_definition`: Valid report definition of up to 65,535 bytes Reserved for future development. Added in MySQL 26.10.0.
- `health_monitor.memory_reporting`: Enable triggered memory reports. Added in MySQL 26.10.0.
- `health_monitor.memory_retention`: Memory sample retention in seconds. Added in MySQL 26.10.0.
- `health_monitor.memory_running`: Enable host and MySQL process memory collection. Added in MySQL 26.10.0.
- `health_monitor.memory_sample_rate`: Memory sample interval in seconds. Added in MySQL 26.10.0.
- `health_monitor.memory_usage_warning_level_1`: First memory warning level in MiB. Added in MySQL 26.10.0.
- `health_monitor.memory_usage_warning_level_2`: Second memory warning level in MiB. Added in MySQL 26.10.0.
- `health_monitor.memory_usage_warning_level_3`: Third memory warning level in MiB. Added in MySQL 26.10.0.
- `health_monitor.periodic_report_definition`: Valid report definition of up to 65,535 bytes Reserved for future development. Added in MySQL 26.10.0.
- `health_monitor.periodic_reporting`: Valid report definition of up to 65,535 bytes Reserved for future development. Added in MySQL 26.10.0.
- `health_monitor.status_interval`: Shared status message interval in multiples of each collector's sample interval. Added in MySQL 26.10.0.
- `health_monitor.system_cpu_stats_history`: Enable CPU history rows. Added in MySQL 26.10.0.
- `health_monitor.system_disk_stats_history`: Enable disk history rows when disk statistics are available. Added in MySQL 26.10.0.
- `health_monitor.system_memory_stats_history`: Enable system memory history rows. Added in MySQL 26.10.0.
- `health_monitor.system_process_stats_history`: Enable MySQL process history rows. Added in MySQL 26.10.0.
- `health_monitor.system_retention`: System statistics retention in seconds. Added in MySQL 26.10.0.
- `health_monitor.system_running`: Enable CPU, disk, memory and MySQL process statistics collection. Added in MySQL 26.10.0.
- `health_monitor.system_sample_rate`: System statistics sample interval in seconds. Added in MySQL 26.10.0.
- `mysql_rest_service.current_http_port`: Port bound by the active HTTP listener. Added in MySQL 26.10.0.
- `mysql_rest_service.current_io_worker_threads`: Resolved active IO worker-thread count. Added in MySQL 26.10.0.
- `mysql_rest_service.current_tls_cert`: Certificate path loaded by the active TLS context. Added in MySQL 26.10.0.
- `mysql_rest_service.current_tls_cipher`: Active TLS 1.2 cipher-list policy. Added in MySQL 26.10.0.
- `mysql_rest_service.current_tls_key`: Key path loaded by the active TLS context. Added in MySQL 26.10.0.
- `mysql_rest_service.http_max_connections`: The HTTP connection limit. Added in MySQL 26.10.0.
- `mysql_rest_service.http_max_request_body_size`: The request body size limit. Added in MySQL 26.10.0.
- `mysql_rest_service.http_max_response_body_size`: The response body size limit. Added in MySQL 26.10.0.
- `mysql_rest_service.http_port`: HTTPS port bound by the active HTTP listener. Added in MySQL 26.10.0.
- `mysql_rest_service.io_worker_threads`: The I/O worker count. Added in MySQL 26.10.0.
- `mysql_rest_service.ssl_cert`: Specifies path to public key certificate file. Added in MySQL 26.10.0.
- `mysql_rest_service.ssl_cipher`: Permissible ciphers for SSL encryption. Added in MySQL 26.10.0.
- `mysql_rest_service.ssl_key`: Specifies path to private key file. Added in MySQL 26.10.0.
- `mysql_rest_service.state`: State of the MRS stack. Added in MySQL 26.10.0.
- `offline_mode_disk_full`: ON if the Health Monitor set OFFLINE\_MODE=ON for low disk space. Added in MySQL 26.10.0.
- `option_tracker_usage:Health           Monitor`: Total number of times a Health Monitor table is accessed by SQL query. MySQL Enterprise Edition only.. Added in MySQL 26.10.0.
- `recovery_cycles`: Number of fence and recovery cycles in the active recovery window. Added in MySQL 26.10.0.
- `super_read_only_disk_full`: ON if the Health Monitor set SUPER\_READ\_ONLY=ON for low disk space. Added in MySQL 26.10.0.
- `version_with_update`: Return a string that indicates the four-part MySQL server version. Added in MySQL 26.10.0.

### Options and Variables Deprecated in MySQL 26.10

No system variables, status variables, or server options have been deprecated in MySQL 26.10.

### Options and Variables Removed in MySQL 26.10

No system variables, status variables, or options have been removed in MySQL 26.10.