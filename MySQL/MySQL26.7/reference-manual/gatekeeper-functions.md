---
title: "MySQL :: MySQL 26.7 Reference Manual :: 14.23 Gatekeeper Functions"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/gatekeeper-functions.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

## 14.23 Gatekeeper Functions

Masking policies require the following gatekeeper functions:

- ``CURRENT_USER_IN(*`user_list`*)``:
	Arguments:
	- A single STRING argument containing comma-separated authorization IDs. For example, `'admin@%,guest'` or `` '`user`@`localhost`,admin` ``. When used in a `CREATE MASKING POLICY` gatekeeper function, the argument must be a string literal. Dynamic expressions, such as column references, are not allowed and raise an error.
	Return Value: Boolean.
	Examples:
	- `SELECT CURRENT_USER_IN('admin');`: returns true if the current user is `admin@%`.
	- `SELECT               CURRENT_USER_IN('user@localhost');`: returns true if the current user is and exact host match with `user@localhost`.
- ``CURRENT_ROLE_IN(*`role_list`*)``:
	Arguments:
	- A single STRING argument containing comma-separated authorization IDs. When used in a `CREATE MASKING               POLICY` gatekeeper function, the argument must be a string literal. Dynamic expressions, such as column references, are not allowed and raise an error.
		Returns true if any of the active roles matches any in the supplied list, and false if no match exists.
	Return Value: Boolean.
	Examples, assuming existence of `role1` and `role2`:
	- `SELECT CURRENT_ROLE_IN('role1');`: returns true because `role1` is active.
	- `SELECT               CURRENT_ROLE_IN('admin@%,role2');`: returns true because `role2` is active.