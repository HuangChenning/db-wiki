---
title: "删除资源规格"
book: "管理数据库"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000002702075.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 删除资源规格

本文介绍如何删除资源规格。

## 前提条件

删除资源规格前必须确保当前资源规格未被使用。如果资源规格正在被使用，则需要先将资源规格从资源池中移出后再删除资源规格。详细操作，参见 [修改资源池属性](900-modify-resource-pool-properties.md)。

## 操作步骤

1.  使用 root 用户登录到集群的 sys 租户。

    ```
    obclient -h172.30.xx.xx -P2881 -uroot@sys -p**** -A
    ```

2.  进入 `oceanbase` 数据库。

    ```
    obclient [(none)]> USE oceanbase;
    ```

3.  通过 `DBA_OB_UNIT_CONFIGS` 和 `DBA_OB_RESOURCE_POOLS` 视图，确认资源规格的使用信息。

    示例如下，如果查询结果的 `UNIT_NAME` 列中无该资源规格名称，则表示该资源规格未被指定给资源池；如果查询结果的 `UNIT_NAME` 列中有该资源规格名称，则表示资源规格已被指定给资源池。

    确认资源规格 `S2_unit_config` 已经不在使用中。

    ```
    obclient [oceanbase]> SELECT a.UNIT_CONFIG_ID, a.NAME AS UNIT_NAME, b.NAME AS POOL_NAME FROM oceanbase.DBA_OB_UNIT_CONFIGS a,oceanbase.DBA_OB_RESOURCE_POOLS b WHERE b.UNIT_CONFIG_ID=a.UNIT_CONFIG_ID;
    +----------------+-----------------+---------------+
    | UNIT_CONFIG_ID | UNIT_NAME       | POOL_NAME     |
    +----------------+-----------------+---------------+
    |              1 | sys_unit_config | sys_pool      |
    |           1001 | unit_mysql      | S2_unit_mysql |
    |           1002 | S1_unit_oral    | S1_pool_oral  |
    +----------------+-----------------+---------------+
    3 rows in set
    ```

    `DBA_OB_UNIT_CONFIGS` 视图的详细说明，参见 [DBA_OB_UNIT_CONFIGS](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001501083)。

    `DBA_OB_RESOURCE_POOLS` 视图的详细说明，参见 [DBA_OB_RESOURCE_POOLS](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001501334)。

4.  通过 `DROP RESOURCE UNIT` 语句，删除资源规格。

    以删除资源规格 `S2_unit_config` 为例：

    ```
    obclient [oceanbase]> DROP RESOURCE UNIT S2_unit_config;
    Query OK, 0 rows affected
    ```

    `DROP RESOURCE UNIT` 语句的详细说明，参见 [DROP RESOURCE UNIT](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001501967)。

5.  查看 `DBA_OB_UNIT_CONFIGS` 视图，确认资源规格删除成功。

    ```
    obclient [oceanbase]> SELECT * FROM DBA_OB_UNIT_CONFIGS WHERE NAME = 'S2_unit_config';
    Empty set
    ```

## 相关文档

- [修改资源池属性](900-modify-resource-pool-properties.md)
