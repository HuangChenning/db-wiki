---
title: "MySQL :: MySQL 26.10 Reference Manual :: 5.6.9 Using AUTO_INCREMENT"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/example-auto-increment.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 5.6.9 Using AUTO\_INCREMENT

The `AUTO_INCREMENT` attribute can be used to generate a unique identity for new rows:

```sql
CREATE TABLE animals (
     id MEDIUMINT NOT NULL AUTO_INCREMENT,
     name CHAR(30) NOT NULL,
     PRIMARY KEY (id)
);

INSERT INTO animals (name) VALUES
    ('dog'),('cat'),('penguin'),
    ('lax'),('whale'),('ostrich');

SELECT * FROM animals;
```

Which returns:

```svg
+----+---------+
| id | name    |
+----+---------+
|  1 | dog     |
|  2 | cat     |
|  3 | penguin |
|  4 | lax     |
|  5 | whale   |
|  6 | ostrich |
+----+---------+
```

No value was specified for the `AUTO_INCREMENT` column, so MySQL assigned sequence numbers automatically. You can also explicitly assign 0 to the column to generate sequence numbers, unless the [`NO_AUTO_VALUE_ON_ZERO`](sql-mode.md) SQL mode is enabled. For example:

```sql
INSERT INTO animals (id,name) VALUES(0,'groundhog');
```

If the column is declared `NOT NULL`, it is also possible to assign `NULL` to the column to generate sequence numbers. For example:

```sql
INSERT INTO animals (id,name) VALUES(NULL,'squirrel');
```

When you insert any other value into an `AUTO_INCREMENT` column, the column is set to that value and the sequence is reset so that the next automatically generated value follows sequentially from the largest column value. For example:

```sql
INSERT INTO animals (id,name) VALUES(100,'rabbit');
INSERT INTO animals (id,name) VALUES(NULL,'mouse');
SELECT * FROM animals;
+-----+-----------+
| id  | name      |
+-----+-----------+
|   1 | dog       |
|   2 | cat       |
|   3 | penguin   |
|   4 | lax       |
|   5 | whale     |
|   6 | ostrich   |
|   7 | groundhog |
|   8 | squirrel  |
| 100 | rabbit    |
| 101 | mouse     |
+-----+-----------+
```

Updating an existing `AUTO_INCREMENT` column value also resets the `AUTO_INCREMENT` sequence.

You can retrieve the most recent automatically generated `AUTO_INCREMENT` value with the [`LAST_INSERT_ID()`](information-functions.md) SQL function or the [`mysql_insert_id()`](https://dev.mysql.com/doc/c-api/26.10/en/mysql-insert-id.html) C API function. These functions are connection-specific, so their return values are not affected by another connection which is also performing inserts.

Use the smallest integer data type for the `AUTO_INCREMENT` column that is large enough to hold the maximum sequence value you require. When the column reaches the upper limit of the data type, the next attempt to generate a sequence number fails. Use the `UNSIGNED` attribute if possible to allow a greater range. For example, if you use [`TINYINT`](integer-types.md), the maximum permissible sequence number is 127. For [`TINYINT         UNSIGNED`](integer-types.md), the maximum is 255. See [Section 13.1.2, “Integer Types (Exact Value) - INTEGER, INT, SMALLINT, TINYINT, MEDIUMINT, BIGINT”](integer-types.md) for the ranges of all the integer types.

Note

For a multiple-row insert, [`LAST_INSERT_ID()`](information-functions.md) and [`mysql_insert_id()`](https://dev.mysql.com/doc/c-api/26.10/en/mysql-insert-id.html) actually return the `AUTO_INCREMENT` key from the *first* of the inserted rows. This enables multiple-row inserts to be reproduced correctly on other servers in a replication setup.

To start with an `AUTO_INCREMENT` value other than 1, set that value with [`CREATE         TABLE`](create-table.md) or [`ALTER TABLE`](alter-table.md), like this:

```sql
mysql> ALTER TABLE tbl AUTO_INCREMENT = 100;
```

#### InnoDB Notes

For information about `AUTO_INCREMENT` usage specific to `InnoDB`, see [Section 17.6.1.6, “AUTO\_INCREMENT Handling in InnoDB”](innodb-auto-increment-handling.md).

#### MyISAM Notes

- For `MyISAM` tables, you can specify `AUTO_INCREMENT` on a secondary column in a multiple-column index. In this case, the generated value for the `AUTO_INCREMENT` column is calculated as [``MAX(*`auto_increment_column`*)               + 1 WHERE               prefix=*`given-prefix`*``](aggregate-functions.md). This is useful when you want to put data into ordered groups.
	```sql
	CREATE TABLE animals (
	    grp ENUM('fish','mammal','bird') NOT NULL,
	    id MEDIUMINT NOT NULL AUTO_INCREMENT,
	    name CHAR(30) NOT NULL,
	    PRIMARY KEY (grp,id)
	) ENGINE=MyISAM;
	INSERT INTO animals (grp,name) VALUES
	    ('mammal','dog'),('mammal','cat'),
	    ('bird','penguin'),('fish','lax'),('mammal','whale'),
	    ('bird','ostrich');
	SELECT * FROM animals ORDER BY grp,id;
	```
	Which returns:
	```svg
	+--------+----+---------+
	| grp    | id | name    |
	+--------+----+---------+
	| fish   |  1 | lax     |
	| mammal |  1 | dog     |
	| mammal |  2 | cat     |
	| mammal |  3 | whale   |
	| bird   |  1 | penguin |
	| bird   |  2 | ostrich |
	+--------+----+---------+
	```
	In this case (when the `AUTO_INCREMENT` column is part of a multiple-column index), `AUTO_INCREMENT` values are reused if you delete the row with the biggest `AUTO_INCREMENT` value in any group. This happens even for `MyISAM` tables, for which `AUTO_INCREMENT` values normally are not reused.
- If the `AUTO_INCREMENT` column is part of multiple indexes, MySQL generates sequence values using the index that begins with the `AUTO_INCREMENT` column, if there is one. For example, if the `animals` table contained indexes `PRIMARY KEY (grp, id)` and `INDEX (id)`, MySQL would ignore the `PRIMARY KEY` for generating sequence values. As a result, the table would contain a single sequence, not a sequence per `grp` value.