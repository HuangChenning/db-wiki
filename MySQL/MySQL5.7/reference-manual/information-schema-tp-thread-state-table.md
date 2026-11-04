---
title: "24.5.4 The INFORMATION_SCHEMA TP_THREAD_STATE Table"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/information-schema-tp-thread-state-table.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 24.5.4 The INFORMATION\_SCHEMA TP\_THREAD\_STATE Table

The `TP_THREAD_STATE` table has one row per thread created by the thread pool to handle connections.

The `TP_THREAD_STATE` table has these columns:

- `TP_GROUP_ID`
	The thread group ID.
- `TP_THREAD_NUMBER`
	The ID of the thread within its thread group. `TP_GROUP_ID` and `TP_THREAD_NUMBER` together provide a unique key within the table.
- `PROCESS_COUNT`
	The 10ms interval in which the statement that uses this thread is currently executing. 0 means no statement is executing, 1 means it is in the first 10ms, and so forth.
- `WAIT_TYPE`
	The type of wait for the thread. `NULL` means the thread is not blocked. Otherwise, the thread is blocked by a call to `thd_wait_begin()` and the value specifies the type of wait. The ``*`xxx`*_WAIT`` columns of the [`TP_THREAD_GROUP_STATS`](information-schema-tp-thread-group-stats-table.md) table accumulate counts for each wait type.
	The `WAIT_TYPE` value is a string that describes the type of wait, as shown in the following table.
	**Table 24.8 TP\_THREAD\_STATE Table WAIT\_TYPE Values**
	| Wait Type | Meaning |
	| --- | --- |
	| `THD_WAIT_SLEEP` | Waiting for sleep |
	| `THD_WAIT_DISKIO` | Waiting for Disk IO |
	| `THD_WAIT_ROW_LOCK` | Waiting for row lock |
	| `THD_WAIT_GLOBAL_LOCK` | Waiting for global lock |
	| `THD_WAIT_META_DATA_LOCK` | Waiting for metadata lock |
	| `THD_WAIT_TABLE_LOCK` | Waiting for table lock |
	| `THD_WAIT_USER_LOCK` | Waiting for user lock |
	| `THD_WAIT_BINLOG` | Waiting for binlog |
	| `THD_WAIT_GROUP_COMMIT` | Waiting for group commit |
	| `THD_WAIT_SYNC` | Waiting for fsync |