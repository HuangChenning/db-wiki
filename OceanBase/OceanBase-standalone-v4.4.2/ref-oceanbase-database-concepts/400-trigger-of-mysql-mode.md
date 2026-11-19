---
title: "触发器"
book: "系统原理"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006078450.html"
tags:
  - oceanbase
  - standalone
  - ref-oceanbase-database-concepts
---

# 触发器

#### 注意

使用 `DELIMITER` 命令修改结束符后，待语句执行结束，请务必将结束符修改为默认符号分号（;）。

#### 说明

- 自 OceanBase 数据库 V4.1.0 BP4 版本起，MySQL 模式下已禁用临时表功能。

- 对于 V4.4.x 版本，自 V4.4.2 版本起，MySQL 模式下支持临时表功能。

- 触发器不能使用 `CALL` 语句调用将数据返回给客户端或使用动态 SQL 的存储过程，但是允许存储过程或者函数通过 `OUT` 或者 `IN OUT` 类型的参数将数据返回触发器。

- 触发器中不能使用开启或结束事务的语句段。例如，开始事务（`START TRANSACTION`）、提交事务（`COMMIT`）或回滚事务（`ROLLBACK`），但是可以回滚到一个保存点，即 Savepoint 是允许的，因为回滚到保存点不会结束事务。

- 外键不会激活触发器。

- 触发器中不允许返回值，因此触发器中不能有返回语句，如果需要立即停止一个触发器，则需要使用 `LEAVE` 语句。
