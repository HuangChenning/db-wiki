---
title: "计划缓存的缺点和解决方案"
book: "管理数据库"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006078088.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 计划缓存的缺点和解决方案

#### 注意

在使用 `target_stmt` 时，严格要求 `stmt` 与 `target_stmt` 在去掉 Hint 后完全匹配。

#### 说明

对于 V4.4.2 版本，从 V4.4.2 BP3 版本开始引入 `BINDING_RULE` 子句。

#### 注意

- 当 `MAP` 左侧为 `db.table` 形式时，右侧 `pattern` 必须拆成两组引号：`'db_pattern'.'table_pattern'`。
- 同一 `BINDING_RULE` 内，变量必须先定义后引用，同名变量在所有引用处取值必须一致。
