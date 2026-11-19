---
title: "升级仲裁服务"
book: "OceanBase 升级"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002016130.html"
tags:
  - oceanbase
  - distributed
  - oceanbase-version-upgrade
---

# 升级仲裁服务

#### 注意

OceanBase 集群支持 V4.3.0 Beta 版本升级到 V4.3.1 Beta 版本。暂不支持 V4.2.x 系列或更低版本升级到 V4.3.1 Beta 版本，随着版本演进，后续会增加 V4.2.x 版本到 V4.3.x 版本的升级路径支持。

#### 说明

可以使用系统租户查询视图 [oceanbase.DBA_OB_ARBITRATION_SERVICE](../ref-system-views/15700-o-dba_ob_arbitration_service-of-sys-tenant.md) 检查本 OceanBase 集群是否关联仲裁服务。

#### 注意

如果升级路径中有多个 barrier 版本，按照顺序依次进行安装和升级 barrier 版本，直到成功升级最后的 barrier 版本再安装目标版本的 RPM 包。

#### 说明

再次启动仲裁 server 进程时不需要指定启动参数，因为之前的启动参数已经写到参数文件里了。
