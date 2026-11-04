---
title: "MySQL :: MySQL 26.7 Reference Manual :: 28.3.37 The INFORMATION_SCHEMA SCHEMATA Table"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/information-schema-schemata-table.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

### 28.3.37 The INFORMATION\_SCHEMA SCHEMATA Table

A schema is a database, so the `SCHEMATA` table provides information about databases.

The `SCHEMATA` table has these columns:

- `CATALOG_NAME`
	The name of the catalog to which the schema belongs. This value is always `def`.
- `SCHEMA_NAME`
	The name of the schema.
- `DEFAULT_CHARACTER_SET_NAME`
	The schema default character set.
- `DEFAULT_COLLATION_NAME`
	The schema default collation.
- `SQL_PATH`
	This value is always `NULL`.
- `DEFAULT_ENCRYPTION`
	The schema default encryption.

Schema names are also available from the [`SHOW       DATABASES`](show-databases.md) statement. See [Section 15.7.7.17, “SHOW DATABASES Statement”](show-databases.md). The following statements are equivalent:

```sql
SELECT SCHEMA_NAME AS \`Database\`
  FROM INFORMATION_SCHEMA.SCHEMATA
  [WHERE SCHEMA_NAME LIKE 'wild']

SHOW DATABASES
  [LIKE 'wild']
```

You see only those databases for which you have some kind of privilege, unless you have the global [`SHOW       DATABASES`](show-databases.md) privilege.

Caution

Because any static global privilege is considered a privilege for all databases, any static global privilege enables a user to see all database names with [`SHOW         DATABASES`](show-databases.md) or by examining the `SCHEMATA` table of `INFORMATION_SCHEMA`, except databases that have been restricted at the database level by partial revokes.

#### Notes

- The [`SCHEMATA_EXTENSIONS`](information-schema-schemata-extensions-table.md) table augments the `SCHEMATA` table with information about schema options.