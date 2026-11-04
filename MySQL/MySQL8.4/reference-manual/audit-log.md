---
title: "8.4.5 MySQL Enterprise Audit"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/audit-log.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

### 8.4.5 MySQL Enterprise Audit

Note

MySQL Enterprise Audit is an extension included in MySQL Enterprise Edition, a commercial product. To learn more about commercial products, see [https://www.mysql.com/products/](https://www.mysql.com/products/).

MySQL Enterprise Edition includes MySQL Enterprise Audit, implemented using a server plugin named `audit_log`. MySQL Enterprise Audit uses the open MySQL Audit API to enable standard, policy-based monitoring, logging, and blocking of connection and query activity executed on specific MySQL servers. Designed to meet the Oracle audit specification, MySQL Enterprise Audit provides an out of box, easy to use auditing and compliance solution for applications that are governed by both internal and external regulatory guidelines.

When installed, the audit plugin enables MySQL Server to produce a log file containing an audit record of server activity. The log contents include when clients connect and disconnect, and what actions they perform while connected, such as which databases and tables they access. You can add statistics for the time and size of each query to detect outliers.

By default, MySQL Enterprise Audit uses tables in the `mysql` system database for persistent storage of filter and user account data. To use a different database, set the [`audit_log_database`](audit-log-reference.md) system variable at server startup.

After you install the audit plugin (see [Section 8.4.5.2, “Installing or Uninstalling MySQL Enterprise Audit”](audit-log-installation.md)), it writes an audit log file. By default, the file is named `audit.log` in the server data directory. To change the name of the file, set the [`audit_log_file`](audit-log-reference.md) system variable at server startup.

By default, audit log file contents are written in new-style XML format, without compression or encryption. To select the file format, set the [`audit_log_format`](audit-log-reference.md) system variable at server startup. For details on file format and contents, see [Section 8.4.5.4, “Audit Log File Formats”](audit-log-file-formats.md).

For more information about controlling how logging occurs, including audit log file naming and format selection, see [Section 8.4.5.5, “Configuring Audit Logging Characteristics”](audit-log-logging-configuration.md). To perform filtering of audited events, see [Section 8.4.5.7, “Audit Log Filtering”](audit-log-filtering.md). For descriptions of the parameters used to configure the audit log plugin, see [Audit Log Options and Variables](audit-log-reference.md).

If the audit log plugin is enabled, the Performance Schema (see [Chapter 29, *MySQL Performance Schema*](performance-schema.md)) has instrumentation for it. To identify the relevant instruments, use this query:

```
SELECT NAME FROM performance_schema.setup_instruments
WHERE NAME LIKE '%/alog/%';
```