---
title: "升级概述"
book: "OceanBase 升级"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002016127.html"
tags:
  - oceanbase
  - distributed
  - oceanbase-version-upgrade
---

# 升级概述

#### 注意

OceanBase 数据库暂不支持 V4.2.x 系列或更低版本升级到 V4.3.x 版本。

#### 注意

如果 OceanBase 集群关联了仲裁服务，那么在进行 OceanBase 集群版本升级时，需要确保先升级仲裁服务版本，然后再升级 OceanBase 集群版本。仲裁服务版本升级的详细信息，请参见 [升级仲裁服务](200-arbitration-services-version-upgrade.md)。\
可以使用系统租户查询视图 [oceanbase.DBA_OB_ARBITRATION_SERVICE](../ref-system-views/15700-o-dba_ob_arbitration_service-of-sys-tenant.md) 检查本 OceanBase 集群是否关联仲裁服务。

#### 说明

OceanBase 数据库自以下版本开始对 AVX 指令集的强制依赖策略已调整：

- 对于 V4.3.5 版本，从 V4.3.5 BP4 版本开始不再强制要求 AVX 指令集支持。
- 对于 V4.2.5 版本，从 V4.2.5 BP6 版本开始不再强制要求 AVX 指令集支持。
- 对于 V4.4.0 版本，从 V4.4.1 版本开始不再强制要求 AVX 指令集支持。

#### 说明

- 本文升级路径图仅作为参考，如需了解更多版本的升级路径，可以参考 `oceanbase_upgrade_dep.yml` 文件，该文件记录了 OceanBase 的版本升级拓扑图。
- 解压目标版本的 OceanBase RPM 包后，会在存放 RPM 包的目录下生成 `home` 和 `use` 两个目录。升级相关脚本和 `oceanbase_upgrade_dep.yml` 文件存放 `home/admin/oceanbase/etc` 目录下。

使用 `oceanbase_upgrade_dep.yml` 文件确认升级路径的详细信息，参见 [升级 OceanBase 集群](300-start-upgrade.md) 中的 **步骤二：确认升级流程** 章节。
