---
title: "使用 INSERT INTO SELECT 语句旁路导入数据"
book: "数据迁移"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000002701740.html"
tags:
  - oceanbase
  - standalone
  - data-migration
---

# 使用 INSERT INTO SELECT 语句旁路导入数据

#### 说明

一般情况下，`enable_parallel_dml` Hint 和 `parallel` Hint 必须配合使用才能开启并行 DML。不过，当目标表的 Schema 上指定了表级别的并行度时，仅需指定 `enable_parallel_dml` Hint。
