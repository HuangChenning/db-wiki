---
title: "MySQL :: MySQL 26.7 Reference Manual :: 11.2.1 Identifier Length Limits"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/identifier-length.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

### 11.2.1 Identifier Length Limits

The following table describes the maximum length for each type of identifier.

| Identifier Type | Maximum Length (characters) |
| --- | --- |
| Database | 64 |
| Table | 64 |
| Column | 64 |
| Index | 64 |
| Constraint | 64 |
| Stored Program | 64 |
| View | 64 |
| Tablespace | 64 |
| Server | 64 |
| Log File Group | 64 |
| Alias | 256 (see exception following table) |
| Compound Statement Label | 16 |
| User-Defined Variable | 64 |
| Resource Group | 64 |

Aliases for column names in [`CREATE         VIEW`](create-view.md) statements are checked against the maximum column length of 64 characters (not the maximum alias length of 256 characters).

For constraint definitions that include no constraint name, the server internally generates a name derived from the associated table name. For example, internally generated foreign key and `CHECK` constraint names consist of the table name plus `_ibfk_` or `_chk_` and a number. If the table name is close to the length limit for constraint names, the additional characters required for the constraint name may cause that name to exceed the limit, resulting in an error.

Identifiers are stored using Unicode (UTF-8). This applies to identifiers in table definitions and to identifiers stored in the grant tables in the `mysql` database. The sizes of the identifier string columns in the grant tables are measured in characters. You can use multibyte characters without reducing the number of characters permitted for values stored in these columns.

Values such as user name and host names in MySQL account names are strings rather than identifiers. For information about the maximum length of such values as stored in grant tables, see [Grant Table Scope Column Properties](grant-tables.md).