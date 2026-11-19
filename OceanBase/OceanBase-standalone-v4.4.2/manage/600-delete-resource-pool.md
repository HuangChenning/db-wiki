---
title: "删除资源池"
book: "管理数据库"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077593.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 删除资源池

本文介绍如何删除资源池。

## 前提条件

删除资源池前，请确认该资源池当前未被任何租户使用。如果资源池正在被租户使用，则需要将资源池释放后再删除资源池。

## 操作步骤

1.  使用 root 用户登录到集群的 sys 租户。

    ```
    obclient -h172.30.xx.xx -P2881 -uroot@sys -p**** -A
    ```

2.  进入 `oceanbase` 数据库。

    ```
    obclient [(none)]> USE oceanbase;
    ```

3.  通过 `DBA_OB_RESOURCE_POOLS` 视图，确认资源池的配置信息。其中 `TENANT_ID` 为 NULL，说明资源池未被分配，可以执行删除。

    以查询 `mq_pool_02` 的配置信息为例：

    ```
    obclient [oceanbase]> SELECT TENANT_ID,NAME FROM DBA_OB_RESOURCE_POOLS WHERE NAME = 'mq_pool_02';
    +-----------+------------+
    | tenant_id | name       |
    +-----------+------------+
    |      NULL | mq_pool_02 |
    +-----------+------------+
    1 row in set
    ```

    `DBA_OB_RESOURCE_POOLS` 视图的详细说明，参见 [DBA_OB_RESOURCE_POOLS](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005284630)。

4.  通过 `DROP RESOURCE POOL` 语句，删除资源池。

    以删除资源池 `mq_pool_02` 为例：

    ```
    obclient [oceanbase]> DROP RESOURCE POOL mq_pool_02;
    Query OK, 0 rows affected 
    ```

    `DROP RESOURCE POOL` 语句的详细说明，参见 [DROP RESOURCE POOL](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005283781)。

5.  查看 `DBA_OB_RESOURCE_POOLS` 视图，确认资源池删除成功。

    ```
    obclient [oceanbase]> SELECT * FROM DBA_OB_RESOURCE_POOLS WHERE NAME = 'mq_pool_02';
    Empty set
    ```

## 相关文档

- [新建资源池](200-manage-create-tenant.md)
