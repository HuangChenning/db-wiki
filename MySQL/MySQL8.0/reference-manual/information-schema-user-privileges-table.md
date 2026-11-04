---
title: "28.3.47 The INFORMATION_SCHEMA USER_PRIVILEGES Table"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/information-schema-user-privileges-table.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 28.3.47 The INFORMATION\_SCHEMA USER\_PRIVILEGES Table

The `USER_PRIVILEGES` table provides information about global privileges. It takes its values from the `mysql.user` system table.

The `USER_PRIVILEGES` table has these columns:

- `GRANTEE`
	The name of the account to which the privilege is granted, in ``'*`user_name`*'@'*`host_name`*'`` format.
- `TABLE_CATALOG`
	The name of the catalog. This value is always `def`.
- `PRIVILEGE_TYPE`
	The privilege granted. The value can be any privilege that can be granted at the global level; see [Section 15.7.1.6, “GRANT Statement”](grant.md). Each row lists a single privilege, so there is one row per global privilege held by the grantee.
- `IS_GRANTABLE`
	`YES` if the user has the [`GRANT OPTION`](privileges-provided.md) privilege, `NO` otherwise. The output does not list [`GRANT OPTION`](privileges-provided.md) as a separate row with `PRIVILEGE_TYPE='GRANT OPTION'`.

#### Notes

- `USER_PRIVILEGES` is a nonstandard `INFORMATION_SCHEMA` table.

The following statements are *not* equivalent:

```
SELECT ... FROM INFORMATION_SCHEMA.USER_PRIVILEGES

SHOW GRANTS ...
```