---
title: "15.6.1 BEGIN ... END Compound Statement"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/begin-end.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 15.6.1 BEGIN... END Compound Statement

```
[begin_label:] BEGIN
    [statement_list]
END [end_label]
```

`BEGIN ... END` syntax is used for writing compound statements, which can appear within stored programs (stored procedures and functions, triggers, and events). A compound statement can contain multiple statements, enclosed by the `BEGIN` and `END` keywords. *`statement_list`* represents a list of one or more statements, each terminated by a semicolon (`;`) statement delimiter. The *`statement_list`* itself is optional, so the empty compound statement (`BEGIN END`) is legal.

`BEGIN ... END` blocks can be nested.

Use of multiple statements requires that a client is able to send statement strings containing the `;` statement delimiter. In the [**mysql**](mysql.md) command-line client, this is handled with the `delimiter` command. Changing the `;` end-of-statement delimiter (for example, to `//`) permit `;` to be used in a program body. For an example, see [Section 27.1, “Defining Stored Programs”](stored-programs-defining.md).

A `BEGIN ...       END` block can be labeled. See [Section 15.6.2, “Statement Labels”](statement-labels.md).

The optional `[NOT] ATOMIC` clause is not supported. This means that no transactional savepoint is set at the start of the instruction block and the `BEGIN` clause used in this context has no effect on the current transaction.

Note

Within all stored programs, the parser treats [`BEGIN [WORK]`](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/commit.html "15.3.1 START TRANSACTION, COMMIT, and ROLLBACK Statements") as the beginning of a `BEGIN ...         END` block. To begin a transaction in this context, use [`START         TRANSACTION`](commit.md) instead.