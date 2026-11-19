---
title: "索引性能优化"
book: "向量搜索"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000005411369.html"
tags:
  - oceanbase
  - standalone
  - ob-vector-search
---

# 索引性能优化

#### 注意

此功能从 V4.3.5 BP3 版本开始支持，目前仅支持 IVF 系列索引。

#### 注意

只有在任务的失败重试阶段，且执行 `ALTER SYSTEM CANCEL TASK` 命令的情况下，才能取消任务。如果后台任务卡在某一次执行阶段，无法通过此命令取消后台任务。
