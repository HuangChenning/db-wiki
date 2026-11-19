---
title: "重命名租户"
book: "管理数据库"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000002701891.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 重命名租户

创建租户后，`sys` 租户可以更改普通租户的名称。

当前，OceanBase 数据库仅支持修改普通租户的名称。

## 操作步骤

1.  使用 `root` 用户登录集群的 `sys` 租户。

2.  重命名普通租户。

    语句如下：

    ``` sql
    ALTER TENANT old_tenant_name RENAME GLOBAL_NAME TO new_tenant_name;
    ```

    将租户 `tenant1` 的租户名修改为 `tenant2` 的示例如下：

    ```
    obclient> ALTER TENANT tenant1 RENAME GLOBAL_NAME TO tenant2;
    ```

## 相关文档

更多 `ALTER TENANT` 语句的信息，请参见 [ALTER TENANT](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001501955)。
