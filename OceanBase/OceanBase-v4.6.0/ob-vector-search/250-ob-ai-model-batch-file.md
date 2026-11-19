---
title: "AI 模型交互（Batch File）"
book: OceanBase AI
version: V4.6.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000006768679.html"
tags:
  - oceanbase
  - distributed
  - ob-vector-search
---

# AI 模型交互（Batch File）

#### 注意

本功能目前仅支持语义索引的后建索引方式。

#### 说明

已完成或失败的任务会在约 10 分钟后从 `DBA_OB_AI_BATCH_TASKS` 归档至 `DBA_OB_AI_BATCH_TASK_HISTORY`。如需长期追溯，请及时查询历史视图。
