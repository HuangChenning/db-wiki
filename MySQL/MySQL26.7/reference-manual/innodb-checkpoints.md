---
title: "MySQL :: MySQL 26.7 Reference Manual :: 17.11.3 InnoDB Checkpoints"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/innodb-checkpoints.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

### 17.11.3 InnoDB Checkpoints

Making your [log files](glossary.md) very large may reduce disk I/O during [checkpointing](glossary.md). It often makes sense to set the total size of the log files as large as the buffer pool or even larger.

#### How Checkpoint Processing Works

`InnoDB` implements a [checkpoint](glossary.md) mechanism known as [fuzzy checkpointing](glossary.md). `InnoDB` flushes modified database pages from the buffer pool in small batches. There is no need to flush the buffer pool in one single batch, which would disrupt processing of user SQL statements during the checkpointing process.

During [crash recovery](glossary.md), `InnoDB` looks for a checkpoint label written to the log files. It knows that all modifications to the database before the label are present in the disk image of the database. Then `InnoDB` scans the log files forward from the checkpoint, applying the logged modifications to the database.