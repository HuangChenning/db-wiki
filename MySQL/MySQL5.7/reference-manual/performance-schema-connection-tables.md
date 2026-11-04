---
title: "25.12.8 Performance Schema Connection Tables"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/performance-schema-connection-tables.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 25.12.8 Performance Schema Connection Tables

When a client connects to the MySQL server, it does so under a particular user name and from a particular host. The Performance Schema provides statistics about these connections, tracking them per account (user and host combination) as well as separately per user name and host name, using these tables:

The meaning of “account” in the connection tables is similar to its meaning in the MySQL grant tables in the `mysql` system database, in the sense that the term refers to a combination of user and host values. They differ in that, for grant tables, the host part of an account can be a pattern, whereas for Performance Schema tables, the host value is always a specific nonpattern host name.

Each connection table has `CURRENT_CONNECTIONS` and `TOTAL_CONNECTIONS` columns to track the current and total number of connections per “tracking value” on which its statistics are based. The tables differ in what they use for the tracking value. The [`accounts`](performance-schema-accounts-table.md) table has `USER` and `HOST` columns to track connections per user and host combination. The [`users`](performance-schema-users-table.md) and [`hosts`](performance-schema-hosts-table.md) tables have a `USER` and `HOST` column, respectively, to track connections per user name and host name.

The Performance Schema also counts internal threads and threads for user sessions that failed to authenticate, using rows with `USER` and `HOST` column values of `NULL`.

Suppose that clients named `user1` and `user2` each connect one time from `hosta` and `hostb`. The Performance Schema tracks the connections as follows:

- The [`accounts`](performance-schema-accounts-table.md) table has four rows, for the `user1` / `hosta`, `user1` / `hostb`, `user2` / `hosta`, and `user2` / `hostb` account values, each row counting one connection per account.
- The [`hosts`](performance-schema-hosts-table.md) table has two rows, for `hosta` and `hostb`, each row counting two connections per host name.
- The [`users`](performance-schema-users-table.md) table has two rows, for `user1` and `user2`, each row counting two connections per user name.

When a client connects, the Performance Schema determines which row in each connection table applies, using the tracking value appropriate to each table. If there is no such row, one is added. Then the Performance Schema increments by one the `CURRENT_CONNECTIONS` and `TOTAL_CONNECTIONS` columns in that row.

When a client disconnects, the Performance Schema decrements by one the `CURRENT_CONNECTIONS` column in the row and leaves the `TOTAL_CONNECTIONS` column unchanged.

[`TRUNCATE TABLE`](truncate-table.md) is permitted for connection tables. It has these effects:

- Rows are removed for accounts, hosts, or users that have no current connections (rows with `CURRENT_CONNECTIONS             = 0`).
- Nonremoved rows are reset to count only current connections: For rows with `CURRENT_CONNECTIONS > 0`, `TOTAL_CONNECTIONS` is reset to `CURRENT_CONNECTIONS`.
- Summary tables that depend on the connection table are implicitly truncated, as described later in this section.

The Performance Schema maintains summary tables that aggregate connection statistics for various event types by account, host, or user. These tables have `_summary_by_account`, `_summary_by_host`, or `_summary_by_user` in the name. To identify them, use this query:

```
mysql> SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES
       WHERE TABLE_SCHEMA = 'performance_schema'
       AND TABLE_NAME REGEXP '_summary_by_(account|host|user)'
       ORDER BY TABLE_NAME;
+------------------------------------------------------+
| TABLE_NAME                                           |
+------------------------------------------------------+
| events_stages_summary_by_account_by_event_name       |
| events_stages_summary_by_host_by_event_name          |
| events_stages_summary_by_user_by_event_name          |
| events_statements_summary_by_account_by_event_name   |
| events_statements_summary_by_host_by_event_name      |
| events_statements_summary_by_user_by_event_name      |
| events_transactions_summary_by_account_by_event_name |
| events_transactions_summary_by_host_by_event_name    |
| events_transactions_summary_by_user_by_event_name    |
| events_waits_summary_by_account_by_event_name        |
| events_waits_summary_by_host_by_event_name           |
| events_waits_summary_by_user_by_event_name           |
| memory_summary_by_account_by_event_name              |
| memory_summary_by_host_by_event_name                 |
| memory_summary_by_user_by_event_name                 |
+------------------------------------------------------+
```

For details about individual connection summary tables, consult the section that describes tables for the summarized event type:

- Wait event summaries: [Section 25.12.15.1, “Wait Event Summary Tables”](performance-schema-wait-summary-tables.md)
- Stage event summaries: [Section 25.12.15.2, “Stage Summary Tables”](performance-schema-stage-summary-tables.md)
- Statement event summaries: [Section 25.12.15.3, “Statement Summary Tables”](performance-schema-statement-summary-tables.md)
- Transaction event summaries: [Section 25.12.15.4, “Transaction Summary Tables”](performance-schema-transaction-summary-tables.md)
- Memory event summaries: [Section 25.12.15.9, “Memory Summary Tables”](performance-schema-memory-summary-tables.md)

[`TRUNCATE TABLE`](truncate-table.md) is permitted for connection summary tables. It removes rows for accounts, hosts, or users with no connections, and resets the summary columns to zero for the remaining rows. In addition, each summary table that is aggregated by account, host, user, or thread is implicitly truncated by truncation of the connection table on which it depends. The following table describes the relationship between connection table truncation and implicitly truncated tables.

**Table 25.2 Implicit Effects of Connection Table Truncation**

| Truncated Connection Table | Implicitly Truncated Summary Tables |
| --- | --- |
| `accounts` | Tables with names containing `_summary_by_account`, `_summary_by_thread` |
| `hosts` | Tables with names containing `_summary_by_account`, `_summary_by_host`, `_summary_by_thread` |
| `users` | Tables with names containing `_summary_by_account`, `_summary_by_user`, `_summary_by_thread` |

Truncating a `_summary_global` summary table also implicitly truncates its corresponding connection and thread summary tables. For example, truncating [`events_waits_summary_global_by_event_name`](performance-schema-wait-summary-tables.md) implicitly truncates the wait event summary tables that are aggregated by account, host, user, or thread.