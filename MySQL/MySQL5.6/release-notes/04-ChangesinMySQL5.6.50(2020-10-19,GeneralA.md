---
title: "Changes in MySQL 5.6.50 (2020-10-19, General Availability)"
book: MySQL 5.6 Release Notes
version: "5.6"
source: "MySQL/MySQL5.6/sources/mysql-5.6-relnotes-en.pdf#page=4"
tags:
  - mysql
  - mysql-5.6
  - release-notes
---

- Functionality Added or Changed
- Bugs Fixed

> Functionality Added or Changed

- `LOCK TABLES` privilege checking for views was improved. (Bug #31304432, WL #14092)

> Bugs Fixed

- InnoDB: In session started with `START TRANSACTION WITH CONSISTENT SNAPSHOT`, a range query

returned a truncated result. The end range flag was not reset at the beginning of the index read resulting in an aborted read and missing rows. (Bug #30950714, Bug #98642)References: This issue is a regression of: Bug #23481444.

- In bootstrapping mode, certain multiple-statement transactions could cause unexpected server behavior.

(Bug #31650096)

## MySQL 5.6 Release Notes

- Assigning `CONCAT('')` or `CONCAT_WS('')` to a variable set the variable to `NULL`, not the empty string.

(Bug #31320716, Bug #99485, Bug #31413167, Bug #99722)

- `ORDER BY` queries were not executed correctly when `sort_buffer_size` and `max_sort_length`

were set to values which caused the internal limit on the maximum number of keys allowed per sort buffer to be set to 0. (Bug #30175483)

- The internal method `Field_tiny::pack()` did not always perform bounds checking as expected.

(Bug #29948029)References: See also: Bug #31591391.

- A large number of nested arguments in full-text search query caused an error. (Bug #29929684)
- An assertion could be raised when the SQL layer passed incorrect information to `InnoDB` about the type

of operation to be performed on a temporary table. (Bug #22503696)
