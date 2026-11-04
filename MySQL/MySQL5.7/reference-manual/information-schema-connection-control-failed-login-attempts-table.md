---
title: "24.6.2 The INFORMATION_SCHEMA CONNECTION_CONTROL_FAILED_LOGIN_ATTEMPTS Table"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/information-schema-connection-control-failed-login-attempts-table.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

Skip to Main Content

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 24.6.2 The INFORMATION\_SCHEMA CONNECTION\_CONTROL\_FAILED\_LOGIN\_ATTEMPTS Table

This table provides information about the current number of consecutive failed connection attempts per account (user/host combination). The table was added in MySQL 5.7.17.

`CONNECTION_CONTROL_FAILED_LOGIN_ATTEMPTS` has these columns:

- `USERHOST`
	The user/host combination indicating an account that has failed connection attempts, in ``'*`user_name`*'@'*`host_name`*'`` format.
- `FAILED_ATTEMPTS`
	The current number of consecutive failed connection attempts for the `USERHOST` value. This counts all failed attempts, regardless of whether they were delayed. The number of attempts for which the server added a delay to its response is the difference between the `FAILED_ATTEMPTS` value and the [`connection_control_failed_connections_threshold`](connection-control-plugin-variables.md) system variable value.

#### Notes

- The `CONNECTION_CONTROL_FAILED_LOGIN_ATTEMPTS` plugin must be activated for this table to be available, and the `CONNECTION_CONTROL` plugin must be activated or the table contents are always empty. See [Section 6.4.2, “Connection Control Plugins”](connection-control-plugin.md).
- The table contains rows only for accounts that have had one or more consecutive failed connection attempts without a subsequent successful attempt. When an account connects successfully, its failed-connection count is reset to zero and the server removes any row corresponding to the account.
- Assigning a value to the [`connection_control_failed_connections_threshold`](connection-control-plugin-variables.md) system variable at runtime resets all accumulated failed-connection counters to zero, which causes the table to become empty.

[MySQL Documentation Library](https://docs.oracle.com/cd/E17952_01/index.html "Go to MySQL Doc Library")