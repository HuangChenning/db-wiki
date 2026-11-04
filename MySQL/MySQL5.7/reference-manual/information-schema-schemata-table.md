---
title: "24.3.22 The INFORMATION_SCHEMA SCHEMATA Table"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/information-schema-schemata-table.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 24.3.22 The INFORMATION\_SCHEMA SCHEMATA Table

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

Schema names are also available from the [`SHOW       DATABASES`](show-databases.md) statement. See [Section 13.7.5.14, “SHOW DATABASES Statement”](show-databases.md). The following statements are equivalent:

```
SELECT SCHEMA_NAME AS \`Database\`
  FROM INFORMATION_SCHEMA.SCHEMATA
  [WHERE SCHEMA_NAME LIKE 'wild']

SHOW DATABASES
  [LIKE 'wild']
```

You see only those databases for which you have some kind of privilege, unless you have the global [`SHOW       DATABASES`](show-databases.md) privilege.

Caution

Because a global privilege is considered a privilege for all databases, *any* global privilege enables a user to see all database names with [`SHOW         DATABASES`](show-databases.md) or by examining the `INFORMATION_SCHEMA` `SCHEMATA` table.