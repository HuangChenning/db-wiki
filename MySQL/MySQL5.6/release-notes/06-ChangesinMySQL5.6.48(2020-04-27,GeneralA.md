---
title: "Changes in MySQL 5.6.48 (2020-04-27, General Availability)"
book: MySQL 5.6 Release Notes
version: "5.6"
source: "MySQL/MySQL5.6/sources/mysql-5.6-relnotes-en.pdf#page=6"
tags:
  - mysql
  - mysql-5.6
  - release-notes
---

> Bugs Fixed

- InnoDB: A tablespace import operation that failed due to the source and destination tables being defined

with different `DATA DIRECTORY` clauses reported an insufficiently descriptive schema mismatch error.

Moreover, if a `.cfg` file was not present, the same operation would raise an assertion failure. A more informative error message is now reported in both cases before the import operation is terminated due to the data directory mismatch. (Bug #30190199, Bug #30190227, Bug #20644698, Bug #76142)

- InnoDB: Updating certain `InnoDB` system variables that take string values raised invalid read errors

during Valgrind testing. (Bug #29717909, Bug #95215)

- Replication: In the event of an unplanned disconnection of a replication slave from the master, the

reference to the master's dump thread might not be removed from the list of registered slaves, in which case statements that accessed the list of slaves would fail. The issue has now been fixed. (Bug#29915479)

- Replication: With the settings `binlog_format=MIXED`, `tx_isolation=READ-COMMITTED`, and

`binlog_row_image=FULL`, an `INSERT ... SELECT` query involving a transactional storage engine omitted any columns with a null value from the row image written to the binary log. This happened because when processing `INSERT ... SELECT` statements, the columns were marked for inserts before the binary logging format was selected. The issue has now been fixed. (Bug #29110804, Bug#93423)

- The Event Scheduler had a memory leak. (Bug #30628268)
- Under certain circumstances, a memcached command could result in reading an uninitialized memory

buffer, causing a failure. (Bug #30592346)

- `CONCAT()` and `CONCAT_WS()` could produce incorrect results in rare cases due to incorrect substring

handling. (Bug #30350206, Bug #96950)

- Scheduling of events could be disturbed by removing events. (Bug #30301356, Bug #96849)

## MySQL 5.6 Release Notes

- Client programs could load authentication plugins from outside the plugin library. (Bug #30191834, Bug

#30644258)

- A query with a `WHERE` clause whose predicate contained a numeric value in scientific notation was not

handled correctly.

In addition, attempting to insert a particular integer specified as a string caused a server exit when the string-to-integer conversion was not successful. (Bug #29723340, Bug #30441969)

- The client library could dereference a null pointer while fetching result set metadata from the server.

(Bug #29597896, Bug #30689251)
