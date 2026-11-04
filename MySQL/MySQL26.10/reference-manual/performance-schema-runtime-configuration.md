---
title: "MySQL :: MySQL 26.10 Reference Manual :: 29.4 Performance Schema Runtime Configuration"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/performance-schema-runtime-configuration.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

## 29.4 Performance Schema Runtime Configuration

Specific Performance Schema features can be enabled at runtime to control which types of event collection occur.

Performance Schema setup tables contain information about monitoring configuration:

```sql
mysql> SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES
       WHERE TABLE_SCHEMA = 'performance_schema'
       AND TABLE_NAME LIKE 'setup%';
+-------------------+
| TABLE_NAME        |
+-------------------+
| setup_actors      |
| setup_consumers   |
| setup_instruments |
| setup_objects     |
| setup_threads     |
+-------------------+
```

You can examine the contents of these tables to obtain information about Performance Schema monitoring characteristics. If you have the [`UPDATE`](privileges-provided.md) privilege, you can change Performance Schema operation by modifying setup tables to affect how monitoring occurs. For additional details about these tables, see [Section 29.12.2, “Performance Schema Setup Tables”](performance-schema-setup-tables.md).

The [`setup_instruments`](performance-schema-setup-instruments-table.md) and [`setup_consumers`](performance-schema-setup-consumers-table.md) tables list the instruments for which events can be collected and the types of consumers for which event information actually is collected, respectively. Other setup tables enable further modification of the monitoring configuration. [Section 29.4.2, “Performance Schema Event Filtering”](performance-schema-filtering.md), discusses how you can modify these tables to affect event collection.

If there are Performance Schema configuration changes that must be made at runtime using SQL statements and you would like these changes to take effect each time the server starts, put the statements in a file and start the server with the [`init_file`](server-system-variables.md) system variable set to name the file. This strategy can also be useful if you have multiple monitoring configurations, each tailored to produce a different kind of monitoring, such as casual server health monitoring, incident investigation, application behavior troubleshooting, and so forth. Put the statements for each monitoring configuration into their own file and specify the appropriate file as the [`init_file`](server-system-variables.md) value when you start the server.