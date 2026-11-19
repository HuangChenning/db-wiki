---
title: "规划磁盘"
book: "部署集中式版"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003577363.html"
tags:
  - oceanbase
  - standalone
  - deploy
---

# 规划磁盘

#### 说明

OceanBase 集中式数据库当前版本支持将 `slog` 从数据（data）盘中独立出来，即 `slog` 与数据文件无需在同一个磁盘上。更多有关 OceanBase 集中式数据库安装目录的信息，请参见 [OBServer 节点安装目录结构](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001500075)。

#### 说明

- 建议根目录不小于 50 GB。如果使用 LVM，建议创建时使用条带化参数。示例如下：`lvcreate -n data -L 3000G obvg --stripes=3 --stripesize=128`
- 建议在生产环境上数据盘与日志盘以及安装盘使用不同的磁盘，避免出现性能问题。
