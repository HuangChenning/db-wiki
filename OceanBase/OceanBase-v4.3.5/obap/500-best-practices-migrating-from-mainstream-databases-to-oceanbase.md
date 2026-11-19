---
title: "主流 AP 数据库数据迁移至 OceanBase 最佳实践"
book: OceanBase AP
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005147874.html"
tags:
  - oceanbase
  - distributed
  - obap
---

# 主流 AP 数据库数据迁移至 OceanBase 最佳实践

#### 说明

请确保目标存储桶（Bucket）已正确配置访问权限，并验证网络连通性。

#### 说明

两种方式均支持 `direct(true)` 直写模式和并行度控制，可大幅提升导入性能。
