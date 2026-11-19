---
title: "PostgreSQL 迁移至 OceanBase MySQL 兼容模式的最佳实践"
book: "数据迁移和导入"
version: master
source: "https://www.oceanbase.com/docs/common-best-practices-1000000004896482.html"
tags:
  - oceanbase
  - best-practices
  - migrations
---

# PostgreSQL 迁移至 OceanBase MySQL 兼容模式的最佳实践

#### 说明

原 PostgreSQL 业务中同一逻辑表按规则拆分为多张结构一致的物理表（如 \`table_0\`、\`table_1\`、...、\`table_n\`），迁移至 OceanBase MySQL 兼容模式时，将这些分表数据统一合并至单一目标表进行存储与管理。

#### 说明

上述评估结果仅用于展示 OMA 的评估能力和报告形式，非本案例真实生产数据。实际结果以用户自身数据库评估结果为准。

#### 说明

在 PostgreSQL 迁移至 OceanBase MySQL 兼容模式的过程中，部分数据类型会发生映射或语义上的调整，例如：`PostgreSQL BIGINT → OceanBase MySQL BIGINT`、`PostgreSQL BIGSERIAL → OceanBase MySQL BIGINT`（结合 AUTO_INCREMENT 实现自增语义）。此类映射通常不会影响数据存储范围，但可能对自增行为、默认值或应用侧依赖逻辑产生影响，需在迁移完成后进行验证。完整的数据类型映射关系及说明，请参考本文附录：PostgreSQL 与 OceanBase MySQL 兼容模式数据类型映射表。
