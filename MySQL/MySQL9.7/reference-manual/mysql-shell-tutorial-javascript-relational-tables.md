---
title: "22.3.4 Relational Tables"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/mysql-shell-tutorial-javascript-relational-tables.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

### 22.3.4 Relational Tables

You can also use X DevAPI to work with relational tables. In MySQL, each relational table is associated with a particular storage engine. The examples in this section use [`InnoDB`](innodb-storage-engine.md) tables in the `world_x` schema.

#### Confirm the Schema

To show the schema that is assigned to the `db` global variable, issue `db`.

```
mysql-js> db
<Schema:world_x>
```

If the returned value is not `Schema:world_x`, set the `db` variable as follows:

```
mysql-js> \use world_x
Schema \`world_x\` accessible through db.
```

#### Show All Tables

To display all relational tables in the `world_x` schema, use the `getTables()` method on the `db` object.

```
mysql-js> db.getTables()
{
    "city": <Table:city>,
    "country": <Table:country>,
    "countrylanguage": <Table:countrylanguage>
}
```

#### Basic Table Operations

Basic operations scoped by tables include:

| Operation form | Description |
| --- | --- |
| ``db.*`name`*.insert()`` | The [insert()](mysql-shell-tutorial-javascript-table-insert.md) method inserts one or more records into the named table. |
| ``db.*`name`*.select()`` | The [select()](mysql-shell-tutorial-javascript-table-select.md) method returns some or all records in the named table. |
| ``db.*`name`*.update()`` | The [update()](mysql-shell-tutorial-javascript-table-update.md) method updates records in the named table. |
| ``db.*`name`*.delete()`` | The [delete()](mysql-shell-tutorial-javascript-table-delete.md) method deletes one or more records from the named table. |

#### Related Information

- See [Working with Relational Tables](https://docs.oracle.com/cd/E17952_01/x-devapi-userguide-en/devapi-users-working-with-relational-tables.html) for more information.
- [CRUD EBNF Definitions](https://docs.oracle.com/cd/E17952_01/x-devapi-userguide-en/mysql-x-crud-ebnf-definitions.html) provides a complete list of operations.
- See [Section 22.3.2, “Download and Import world\_x Database”](mysql-shell-tutorial-javascript-download.md) for instructions on setting up the `world_x` schema sample.