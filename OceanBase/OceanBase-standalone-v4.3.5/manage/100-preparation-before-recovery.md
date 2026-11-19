---
title: "恢复前准备"
book: "管理数据库"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003577565.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 恢复前准备

在执行恢复操作前，您需要创建待恢复的租户所需的资源。

## 注意事项

在进行恢复操作前，请务必确认待恢复的备份数据的版本。通常，除了本版本内的恢复，恢复支持的其他备份数据版本与 OceanBase 集群的升级路径一致。在当前版本中，需要重点注意以下事项：

- 暂不支持恢复 V4.2.x 版本的备份数据，后续会有兼容的 LTS 版本支持恢复 V4.2.5 的备份数据。

- 不支持恢复 V4.3.0（含）~ V4.3.2（含）版本的备份数据。

## 恢复前准备

1.  使用 `root` 用户登录集群的 `sys` 租户。

2.  创建 Unit（资源单元）。

    示例如下：

    ```
    obclient [(none)]> CREATE RESOURCE UNIT box_16c96g MAX_CPU 16, MEMORY_SIZE = '5G', MAX_IOPS 10240, MIN_IOPS=10240;
    ```

    创建资源单元的详细操作及说明请参见 [创建租户](200-manage-create-tenant.md)。

3.  创建 Resource Pool（资源池）。

    创建待恢复的租户的资源池时，建议尽量与源租户保持同构，即建议待恢复的租户的资源池中 `unit_num` 的个数与源租户相同。

    示例如下：

    ```
    obclient [(none)]> CREATE RESOURCE POOL restore_pool unit = 'box_16c96g', unit_num = 1, zone_list = ('zone1');
    ```

    创源资源池的详细操作及说明请参见 [创建租户](200-manage-create-tenant.md)。

## 后续操作

[执行物理恢复](200-initiate-the-tenant-restore.md)
