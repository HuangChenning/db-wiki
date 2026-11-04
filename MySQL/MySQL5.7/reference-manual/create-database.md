---
title: "13.1.11 CREATE DATABASE Statement"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/create-database.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 13.1.11 CREATE DATABASE Statement

```
CREATE {DATABASE | SCHEMA} [IF NOT EXISTS] db_name
    [create_option] ...

create_option: [DEFAULT] {
    CHARACTER SET [=] charset_name
  | COLLATE [=] collation_name
}
```

`CREATE DATABASE` creates a database with the given name. To use this statement, you need the [`CREATE`](privileges-provided.md) privilege for the database. `CREATE       SCHEMA` is a synonym for `CREATE       DATABASE`.

An error occurs if the database exists and you did not specify `IF NOT EXISTS`.

`CREATE DATABASE` is not permitted within a session that has an active [`LOCK       TABLES`](lock-tables.md) statement.

Each *`create_option`* specifies a database characteristic. Database characteristics are stored in the `db.opt` file in the database directory. The `CHARACTER SET` option specifies the default database character set. The `COLLATE` option specifies the default database collation. For information about character set and collation names, see [Chapter 10, *Character Sets, Collations, Unicode*](charset.md).

To see the available character sets and collations, use the [`SHOW CHARACTER SET`](show-character-set.md) and [`SHOW COLLATION`](show-collation.md) statements, respectively. See [Section 13.7.5.3, “SHOW CHARACTER SET Statement”](show-character-set.md), and [Section 13.7.5.4, “SHOW COLLATION Statement”](show-collation.md).

A database in MySQL is implemented as a directory containing files that correspond to tables in the database. Because there are no tables in a database when it is initially created, the `CREATE DATABASE` statement creates only a directory under the MySQL data directory and the `db.opt` file. Rules for permissible database names are given in [Section 9.2, “Schema Object Names”](identifiers.md). If a database name contains special characters, the name for the database directory contains encoded versions of those characters as described in [Section 9.2.4, “Mapping of Identifiers to File Names”](identifier-mapping.md).

If you manually create a directory under the data directory (for example, with **mkdir**), the server considers it a database directory and it shows up in the output of [`SHOW DATABASES`](show-databases.md).

When you create a database, let the server manage the directory and the files in it. Manipulating database directories and files directly can cause inconsistencies and unexpected results.

MySQL has no limit on the number of databases. The underlying file system may have a limit on the number of directories.

You can also use the [**mysqladmin**](mysqladmin.md) program to create databases. See [Section 4.5.2, “mysqladmin — A MySQL Server Administration Program”](mysqladmin.md).