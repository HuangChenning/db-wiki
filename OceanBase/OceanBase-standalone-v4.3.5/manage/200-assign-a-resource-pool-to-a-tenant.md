---
title: "将资源池分配给租户"
book: "管理数据库"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003577845.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 将资源池分配给租户

资源池创建成功后，您可以在创建租户时将资源池分配给租户，也可以在修改资源池列表时，将未使用的资源池分配给租户。

## 创建租户时分配资源池

创建租户时，您可以将未使用的资源池分配给租户，SQL 语句示例如下：

``` sql
obclient>  CREATE TENANT IF NOT EXISTS test_tenant charset='utf8mb4',primary_zone='zone1', resource_pool_list=('pool1');
```

其中：

- 每个资源池仅能绑定给一个租户，每个租户可以拥有多个资源池。
- 租户在 Zone 内被分配的所有资源总量为：Unit 规格 \* Unit 数量。

创建租户的更多信息请参见 [创建租户](200-manage-create-tenant.md)。
