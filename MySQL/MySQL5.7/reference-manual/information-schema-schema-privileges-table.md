---
title: "24.3.23 The INFORMATION_SCHEMA SCHEMA_PRIVILEGES Table"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/information-schema-schema-privileges-table.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 24.3.23 The INFORMATION\_SCHEMA SCHEMA\_PRIVILEGES Table

The `SCHEMA_PRIVILEGES` table provides information about schema (database) privileges. It takes its values from the `mysql.db` system table.

The `SCHEMA_PRIVILEGES` table has these columns:

- `GRANTEE`
	The name of the account to which the privilege is granted, in ``'*`user_name`*'@'*`host_name`*'`` format.
- `TABLE_CATALOG`
	The name of the catalog to which the schema belongs. This value is always `def`.
- `TABLE_SCHEMA`
	The name of the schema.
- `PRIVILEGE_TYPE`
	The privilege granted. The value can be any privilege that can be granted at the schema level; see [Section 13.7.1.4, “GRANT Statement”](grant.md). Each row lists a single privilege, so there is one row per schema privilege held by the grantee.
- `IS_GRANTABLE`
	`YES` if the user has the [`GRANT OPTION`](privileges-provided.md) privilege, `NO` otherwise. The output does not list [`GRANT OPTION`](privileges-provided.md) as a separate row with `PRIVILEGE_TYPE='GRANT OPTION'`.

#### Notes

- `SCHEMA_PRIVILEGES` is a nonstandard `INFORMATION_SCHEMA` table.

The following statements are *not* equivalent:

```
SELECT ... FROM INFORMATION_SCHEMA.SCHEMA_PRIVILEGES

SHOW GRANTS ...
```