---
title: "13.1.4 ALTER INSTANCE Statement"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/alter-instance.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 13.1.4 ALTER INSTANCE Statement

```
ALTER INSTANCE ROTATE INNODB MASTER KEY
```

`ALTER INSTANCE`, introduced in MySQL 5.7.11, defines actions applicable to a MySQL server instance. The statement supports these actions:

- `ALTER INSTANCE ROTATE INNODB MASTER KEY`
	This action rotates the master encryption key used for `InnoDB` tablespace encryption. Key rotation requires the [`SUPER`](privileges-provided.md) privilege. To perform this action, a keyring plugin must be installed and configured. For instructions, see [Section 6.4.4, “The MySQL Keyring”](keyring.md).
	`ALTER INSTANCE ROTATE INNODB MASTER KEY` supports concurrent DML. However, it cannot be run concurrently with [`CREATE TABLE ...           ENCRYPTION`](create-table.md) or [`ALTER TABLE ...           ENCRYPTION`](alter-table.md) operations, and locks are taken to prevent conflicts that could arise from concurrent execution of these statements. If one of the conflicting statements is running, it must complete before another can proceed.
	`ALTER INSTANCE` actions are written to the binary log so that they can be executed on replicated servers.
	For additional `ALTER INSTANCE ROTATE INNODB MASTER           KEY` usage information, see [Section 14.14, “InnoDB Data-at-Rest Encryption”](innodb-data-encryption.md). For information about keyring plugins, see [Section 6.4.4, “The MySQL Keyring”](keyring.md).