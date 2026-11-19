---
title: "执行按表恢复"
book: "管理数据库"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000002701905.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 执行按表恢复

#### 注意

- **物理恢复辅助租户执行阶段**，可以通过调整 [ha_high_thread_score](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001502002) 配置项来动态调整恢复的并行度，调整后立即生效。其中，辅助租户名可以通过表级恢复的任务进度表 [CDB_OB_RECOVER_TABLE_JOBS](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001501136) 查看。具体调整请参见[物理恢复](200-initiate-the-tenant-restore.md)
- **跨租户导表阶段**，你可以通过调整目标租户的 `recover_table_concurrency` 或 `recover_table_dop` 配置项来动态调整多表/单表恢复的并行度，调整后立即生效。

#### 注意

- 表数据恢复成功即表示表恢复成功，允许索引、约束或其他关联的 Schema 恢复失败。
- 按表恢复结束后，建议还原 `ddl_thread_score`、`recover_table_concurrency` 和 `recover_table_dop` 配置项设置。如果不恢复，则后续的表级恢复都会按照设置的并行参数执行。
