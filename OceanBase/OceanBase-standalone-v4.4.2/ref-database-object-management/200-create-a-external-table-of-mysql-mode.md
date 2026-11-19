---
title: "创建和查询外表"
book: "数据库对象管理"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006078151.html"
tags:
  - oceanbase
  - standalone
  - ref-database-object-management
---

# 创建和查询外表

#### 说明

未显式指定 `API_MODE` 时默认使用 `tunnel_api`，适用于公网或 OB 与 MaxCompute 不在同一 VPC 的场景。若 OB 与 MaxCompute 同地域 VPC 且已开通 Storage API，可设置 `API_MODE = 'storage_api'` 与 `SPLIT = 'byte'` 以提升吞吐；参数说明参见 [ODPS 外部表](../obap/200-odps-external-table.md) 与 [CREATE EXTERNAL TABLE](%5B../../../../../620.obap/400.data-lake/200.data-lake-integration/300.odps/200.odps-external-table.md%5D(https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005286424)) 中的 `properties_type_options`。
