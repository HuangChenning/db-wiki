---
title: "22.3.3 Documents and Collections"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/mysql-shell-tutorial-javascript-documents-collections.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

### 22.3.3 Documents and Collections

When you are using MySQL as a Document Store, collections are containers within a schema that you can create, list, and drop. Collections contain JSON documents that you can add, find, update, and remove.

The examples in this section use the `countryinfo` collection in the `world_x` schema. For instructions on setting up the `world_x` schema, see [Section 22.3.2, “Download and Import world\_x Database”](mysql-shell-tutorial-javascript-download.md).

#### Documents

In MySQL, documents are represented as JSON objects. Internally, they are stored in an efficient binary format that enables fast lookups and updates.

- Simple document format for JavaScript:
	```
	{field1: "value", field2 : 10, "field 3": null}
	```

An array of documents consists of a set of documents separated by commas and enclosed within `[` and `]` characters.

- Simple array of documents for JavaScript:
	```
	[{"Name": "Aruba", "Code:": "ABW"}, {"Name": "Angola", "Code:": "AGO"}]
	```

MySQL supports the following JavaScript value types in JSON documents:

- numbers (integer and floating point)
- strings
- boolean (False and True)
- null
- arrays of more JSON values
- nested (or embedded) objects of more JSON values

#### Collections

Collections are containers for documents that share a purpose and possibly share one or more indexes. Each collection has a unique name and exists within a single schema.

The term schema is equivalent to a database, which means a group of database objects as opposed to a relational schema, used to enforce structure and constraints over data. A schema does not enforce conformity on the documents in a collection.

In this quick-start guide:

- Basic objects include:
	| Object form | Description |
	| --- | --- |
	| `db` | `db` is a global variable assigned to the current active schema. When you want to run operations against the schema, for example to retrieve a collection, you use methods available for the `db` variable. |
	| `db.getCollections()` | [db.getCollections()](mysql-shell-tutorial-javascript-collections-operations.md) returns a list of collections in the schema. Use the list to get references to collection objects, iterate over them, and so on. |
- Basic operations scoped by collections include:
	| Operation form | Description |
	| --- | --- |
	| ``db.*`name`*.add()`` | The [add()](mysql-shell-tutorial-javascript-collections-add.md) method inserts one document or a list of documents into the named collection. |
	| ``db.*`name`*.find()`` | The [find()](mysql-shell-tutorial-javascript-documents-find.md) method returns some or all documents in the named collection. |
	| ``db.*`name`*.modify()`` | The [modify()](mysql-shell-tutorial-javascript-documents-modify.md) method updates documents in the named collection. |
	| ``db.*`name`*.remove()`` | The [remove()](mysql-shell-tutorial-javascript-documents-remove.md) method deletes one document or a list of documents from the named collection. |

#### Related Information

- See [Working with Collections](https://docs.oracle.com/cd/E17952_01/x-devapi-userguide-en/devapi-users-working-with-collections.html) for a general overview.
- [CRUD EBNF Definitions](https://docs.oracle.com/cd/E17952_01/x-devapi-userguide-en/mysql-x-crud-ebnf-definitions.html) provides a complete list of operations.