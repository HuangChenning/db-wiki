---
title: "使用 obd 升级 OceanBase 数据库"
book: "OceanBase 升级"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002016131.html"
tags:
  - oceanbase
  - distributed
  - oceanbase-version-upgrade
---

# 使用 obd 升级 OceanBase 数据库

#### 说明

- 待升级集群租户存在备租户的情况下，您需先升级备租户所在集群，或执行 switchover 进行主备切换。

- obd 支持升级企业版和社区版 OceanBase 集群，本节以升级社区版 OceanBase 集群为例介绍升级 OceanBase 集群的操作。

#### 说明

仅在升级目标版本为 V4.0.x、V4.1.x 和 V4.2.0 BETA 版本时需执行该步骤。

#### 注意

您需使用部署 OceanBase 数据库时所用的主机账号（比如 admin）安装 all-in-one 安装包。

#### 说明

仅在升级目标版本为 V4.0.x、V4.1.x 和 V4.2.0 BETA 版本时需执行该步骤。
