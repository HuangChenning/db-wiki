---
title: "使用 OceanBase 导数工具在 OceanBase 集群 MySQL 租户间迁移数据"
book: "数据迁移"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003577497.html"
tags:
  - oceanbase
  - standalone
  - data-migration
---

# 使用 OceanBase 导数工具在 OceanBase 集群 MySQL 租户间迁移数据

#### 说明

- 使用 OceanBase 物理节点的主机地址和端口导出数据时，无需指定 `-c` 选项。
- 有关 obdumper 命令行选项的详细信息，请参见 [命令行选项](https://www.oceanbase.com/docs/enterprise-oceanbase-dumper-loader-cn-10000000001142216)。

#### 说明

- 使用 OceanBase 物理节点的主机地址和端口导入数据时，无需指定 `-c` 选项。
- 有关 obloader 命令行选项的详细信息，请参见 [命令行选项](https://www.oceanbase.com/docs/enterprise-oceanbase-dumper-loader-cn-10000000001142221)。

#### 说明

`--sys-user` 选项用于连接 `sys` 租户下拥有特定权限的用户。导出时如果未指定 `--sys-user` 选项，默认指定的是 `--sys-user root`。
