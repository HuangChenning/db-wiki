---
title: "租户内存写满"
book: "管理数据库"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077581.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 租户内存写满

#### 注意

截止 OceanBase V3.2 版本，修改 `resource unit` 配置仅 CPU、Memory 配置是实际生效的，其他 IO 参数例如磁盘、iops 等都暂时无效，默认即可。

#### 注意

该参数调大的代价为 CPU 使用率升高，请根据具体情况决定是否开启。
