---
title: "MySQL :: MySQL 26.10 Reference Manual :: 12.9.3 The utf8 Character Set (Deprecated alias)"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/charset-unicode-utf8.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 12.9.3 The utf8 Character Set (Deprecated alias)

`utf8` is a deprecated alias whose interpretation in SQL statements is controlled by the \`INTERPRET\_UTF8\_AS\_UTF8MB4\` SQL mode. When the server stores or reports a resolved character set or collation, it uses the canonical \`utf8mb3\` or \`utf8mb4\` name rather than \`utf8\`. For more information, see [Section 12.9.1, “The utf8mb4 Character Set (4-Byte UTF-8 Unicode Encoding)”](charset-unicode-utf8mb4.md) and [Section 12.9.2, “The utf8mb3 Character Set (3-Byte UTF-8 Unicode Encoding)”](charset-unicode-utf8mb3.md).

The alias mapping is as follows:

**Table 12.3 utf8 Alias Mapping INTERPRET\_UTF8\_AS\_UTF8MB4**

| SQL mode | utf8 | utf8\_xxx |
| --- | --- | --- |
| [`INTERPRET_UTF8_AS_UTF8MB4`](sql-mode.md) not enabled (default) | `utf8mb3` | `utf8mb3_xxx` |
| [`INTERPRET_UTF8_AS_UTF8MB4`](sql-mode.md) enabled | `utf8mb4` | `utf8mb4_xxx` |

Character set and collation names are not case-sensitive. For example, \`UTF8\`, \`Utf8\`, and \`utf8\` are interpreted identically. The mapping applies to character set and collation names in DDL and DML statements. DDL stores the resolved canonical names, which are displayed by \`SHOW CREATE\` statements. \`EXPLAIN\` reflects names resolved while processing DML statements. For example:

```sql
SET SESSION sql_mode = '';
CREATE TABLE t1 (c VARCHAR(10))
  CHARACTER SET utf8 COLLATE utf8_bin;
SHOW CREATE TABLE t1;

SET SESSION sql_mode = 'INTERPRET_UTF8_AS_UTF8MB4';
CREATE TABLE t2 (c VARCHAR(10))
  CHARACTER SET utf8 COLLATE utf8_bin;
SHOW CREATE TABLE t2;
```

`t1` uses `utf8mb3` and utf8mb3\_bin; while t2 uses `utf8mb4` and `utf8mb4_bin`.

All `utf8mb3` collations have a corresponding `utf8mb4` collation except `utf8mb3_general_mysql500_ci` and `utf8mb3_tolower_ci`. Consequently, `utf8_general_mysql500_ci` and `utf8_tolower_ci` are rejected when [`INTERPRET_UTF8_AS_UTF8MB4`](sql-mode.md) is enabled. Specify the corresponding `utf8mb3` name explicitly to use either collation. For generated columns, aliases are resolved to explicit character set and collation names when the table is created.

[`INTERPRET_UTF8_AS_UTF8MB4`](sql-mode.md) does not affect the following:

- For MySQL client program options, [`--default-character-set=utf8`](mysql-command-options.md) always selects utf8mb3.
- For external character set definitions read from `Index.xml`, `utf8` continues to map to `utf8mb3`.
- Server startup options require explicit names. [`--default-character-set=utf8`](mysql-command-options.md), [`--default-character-set=utf8`](mysql-command-options.md), and [`--collation-server=utf8_xxx`](server-system-variables.md) are rejected. Use explicit `utf8mb3`, `utf8mb4`, `utf8mb3_xxx`, or `utf8mb4_xxx` names instead.

To avoid behavior that depends on the SQL mode, it is recommended to specify `utf8mb3` or `utf8mb4` explicitly.

Note

The recommended character set for MySQL is `utf8mb4`. All new applications should use `utf8mb4`.

The `utf8mb3` character set is deprecated. `utf8mb3` remains supported for the lifetimes of the MySQL 8.4.x LTS release series.

Expect `utf8mb3` to be removed in a future major release of MySQL.

Since changing character sets can be a complex and time-consuming task, you should begin to prepare for this change now by using `utf8mb4` for new applications. For guidance in converting existing applications which use utfmb3, see [Section 12.9.8, “Converting Between 3-Byte and 4-Byte Unicode Character Sets”](charset-unicode-conversion.md).