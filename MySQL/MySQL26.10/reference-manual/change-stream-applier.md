---
title: "MySQL :: MySQL 26.10 Reference Manual :: 19.2.4 Change Stream Applier"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/change-stream-applier.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 19.2.4 Change Stream Applier

MySQL provides the following implementations for applying transactions on a replica:

- Applier version 1 is the existing Multi-Threaded Applier (MTA).
- Applier version 2 is the Change Stream Applier (CSA), introduced in MySQL 26.7.0.

The applier implementation is selected separately for each replication channel using the `APPLIER_VERSION` option of `CHANGE REPLICATION SOURCE TO`. Version 1 is the default for a new channel.

The CSA uses a scheduler and a channel-specific pool of worker sessions. It determines transaction dependencies from the `last_committed` and `sequence_number` values recorded in GTID events. Transactions whose dependencies are satisfied can be applied in parallel.

If [`replica_preserve_commit_order`](replication-options-replica.md) is enabled, the apply and commit phases are scheduled separately. A transaction that has finished applying waits for its turn to register for commit, but the worker that applied it can process another ready transaction instead of waiting. The commit order manager preserves the order in which transactions were committed on the source.

CSA workers can read transaction events from the relay log in parallel and release event memory as events are consumed. Relay log files can be marked for purging concurrently when they have been completely read and all transactions that use them have been applied successfully.