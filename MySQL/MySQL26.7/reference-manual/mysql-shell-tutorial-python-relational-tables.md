---
title: "MySQL :: MySQL 26.7 Reference Manual :: 22.4.4 Relational Tables"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/mysql-shell-tutorial-python-relational-tables.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

### 22.4.4 Relational Tables

You can also use X DevAPI to work with relational tables. In MySQL, each relational table is associated with a particular storage engine. The examples in this section use [`InnoDB`](innodb-storage-engine.md) tables in the `world_x` schema.

#### Confirm the Schema

To show the schema that is assigned to the `db` global variable, issue `db`.

```svg
mysql-py> db
<Schema:world_x>
```

If the returned value is not `Schema:world_x`, set the `db` variable as follows:

```svg
mysql-py> \use world_x
Schema \`world_x\` accessible through db.
```

#### Show All Tables

To display all relational tables in the `world_x` schema, use the `get_tables()` method on the `db` object.

```svg
mysql-py> db.get_tables()
[
    <Table:city>,
    <Table:country>,
    <Table:countrylanguage>
]
```

#### Basic Table Operations

Basic operations scoped by tables include:

| Operation form | Description |
| --- | --- |
| ``db.*`name`*.insert()`` | The [insert()](mysql-shell-tutorial-python-table-insert.md) method inserts one or more records into the named table. |
| ``db.*`name`*.select()`` | The [select()](mysql-shell-tutorial-python-table-select.md) method returns some or all records in the named table. |
| ``db.*`name`*.update()`` | The [update()](mysql-shell-tutorial-python-table-update.md) method updates records in the named table. |
| ``db.*`name`*.delete()`` | The [delete()](mysql-shell-tutorial-python-table-delete.md) method deletes one or more records from the named table. |

#### Related Information

- See [Working with Relational Tables](https://dev.mysql.com/doc/x-devapi-userguide/en/devapi-users-working-with-relational-tables.html) for more information.
- [CRUD EBNF Definitions](https://dev.mysql.com/doc/x-devapi-userguide/en/mysql-x-crud-ebnf-definitions.html) provides a complete list of operations.
- See [Section 22.4.2, “Download and Import world\_x Database”](mysql-shell-tutorial-python-download.md) for instructions on setting up the `world_x` schema sample.