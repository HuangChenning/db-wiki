---
title: "MySQL :: MySQL 26.10 Reference Manual :: 7.5.11 Health Monitor Component"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/health-monitor-component.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 7.5.11 Health Monitor Component

The Health Monitor component monitors host resources used by MySQL. The Health Monitor provides the following kinds of resource information:

- Health samples for the monitored filesystem, host memory, and MySQL process memory.
- Current and historical CPU, storage-device, memory, and MySQL process statistics.
- Disk metrics and disk-usage forecasts.

Important

Health Monitor is fully supported on Linux platforms and partially supported on MacOS. It is not currently supported on Windows platforms.

MacOS supports basic filesystem monitoring, host memory and CPU measurements. Disk forecasting is not supported on MacOS.

- Purpose: Monitor host resources and, when configured to do so, protect the server from disk exhaustion.
- URN: `file://component_health_monitor`

For installation instructions, see [Section 7.5.1, “Installing and Uninstalling Components”](component-loading.md).

To confirm installation, run the following to list all the available system variables:

```sql
SHOW GLOBAL VARIABLES LIKE 'health_monitor.%';
```

Disk and memory health tables are sampled according to their respective sample-rate variables. Their maximum number of rows is the retention interval divided by the sample interval. When a sampled table reaches its maximum size, the oldest rows are discarded.

All Health Monitor system variables are global and dynamic. Changing a collector setting can restart the affected collector, but does not restart the MySQL server.

For example:

```sql
SET GLOBAL health_monitor.memory_sample_rate = 120;
SET PERSIST health_monitor.disk_fallback_enable = ON;
```

Changing these variables requires the [`SYSTEM_VARIABLES_ADMIN`](privileges-provided.md) privilege.

Each collector can be started or stopped independently. For example:

```sql
SET GLOBAL health_monitor.disk_running = ON;
SET GLOBAL health_monitor.memory_running = ON;
SET GLOBAL health_monitor.system_running = ON;
```

To stop a collector, set the variable to `OFF`.