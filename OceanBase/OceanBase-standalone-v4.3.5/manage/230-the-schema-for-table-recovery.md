---
title: "表级恢复的 Schema 恢复说明"
book: "管理数据库"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006123822.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 表级恢复的 Schema 恢复说明

#### 注意

Oracle 模式下，如果存在重复的 `PRIMARY KEY` 约束名，则会导致整个表恢复失败。

#### 说明

如果约束名为用户自定义，并且在目标租户下已存在，则不恢复。
