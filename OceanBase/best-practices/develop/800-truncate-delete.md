---
title: "OceanBase 数据库批量数据清理策略最佳实践"
book: "开发"
version: master
source: "https://www.oceanbase.com/docs/common-best-practices-1000000003039638.html"
tags:
  - oceanbase
  - best-practices
  - develop
---

# OceanBase 数据库批量数据清理策略最佳实践

#### 说明

OceanBase 4.x 版本起，`TRUNCATE TABLE` 支持并行执行，显著提升批量清表效率。3.x 及更早版本建议采用并发 `DELETE` 并分批提交。

#### 说明

只有支持并行的 DDL 执行过程中才能并行。如果您插入了串行 DDL，则整体 DDL 执行将转为串行。因此，在 TRUNCATE TABLE 执行过程中最好仅包含支持并行的 DDL。如果有其他 DDL，您需要查看是否支持并行。

#### 注意

- DELETE 操作会产生 undo 日志，需确保有足够的 undo 空间。
- 对关联表的清理需考虑引用完整性约束。
- 定期执行 ANALYZE TABLE 维护统计信息。

#### 说明

以上测试结果仅为特定环境下的示例，实际效果需结合您的业务环境和系统配置进行评估。
