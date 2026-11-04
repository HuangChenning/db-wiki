---
title: "MySQL :: MySQL 26.7 Reference Manual :: 28.3.3 The INFORMATION_SCHEMA APPLICABLE_ROLES Table"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/information-schema-applicable-roles-table.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

### 28.3.3 The INFORMATION\_SCHEMA APPLICABLE\_ROLES Table

The `APPLICABLE_ROLES` table provides information about the roles that are applicable for the current user.

The `APPLICABLE_ROLES` table has these columns:

- `USER`
	The user name part of the current user account.
- `HOST`
	The host name part of the current user account.
- `GRANTEE`
	The user name part of the account to which the role is granted.
- `GRANTEE_HOST`
	The host name part of the account to which the role is granted.
- `ROLE_NAME`
	The user name part of the granted role.
- `ROLE_HOST`
	The host name part of the granted role.
- `IS_GRANTABLE`
	`YES` or `NO`, depending on whether the role is grantable to other accounts.
- `IS_DEFAULT`
	`YES` or `NO`, depending on whether the role is a default role.
- `IS_MANDATORY`
	`YES` or `NO`, depending on whether the role is mandatory.