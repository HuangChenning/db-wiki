---
title: "升级 OceanBase 集群"
book: "OceanBase 升级"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002016129.html"
tags:
  - oceanbase
  - distributed
  - oceanbase-version-upgrade
---

# 升级 OceanBase 集群

#### 注意

OceanBase 数据库暂不支持 V4.2.x 系列或更低版本升级到 V4.3.x 版本。

#### 注意

如果 OceanBase 集群关联了仲裁服务，那么在进行 OceanBase 集群版本升级时，需要确保先升级仲裁服务版本，然后再升级 OceanBase 集群版本。仲裁服务版本升级的详细信息，请参见 [升级仲裁服务](200-arbitration-services-version-upgrade.md)。\
可以使用系统租户查询视图 [oceanbase.DBA_OB_ARBITRATION_SERVICE](../ref-system-views/15700-o-dba_ob_arbitration_service-of-sys-tenant.md) 检查本 OceanBase 集群是否关联仲裁服务。更多升级注意信息，请参见 [升级概述](100-upgrade-overview.md)。

#### 注意

在下面步骤执行升级脚本时，指定的 `-u` 参数必须是 `sys` 租户有读写及 `SUPER` 权限的用户。

#### 说明

解压 RPM 包完成后，会在存放 RPM 包的目录下生成 `home` 和 `use` 两个目录。升级相关脚本和 `oceanbase_upgrade_dep.yml` 文件存放 `home/admin/oceanbase/etc` 目录下。

#### 注意

如果升级序列中存在 barrier 版本，那么您还需获取升级路径中所有 barrier 版本的 OceanBase RPM 包。

#### 注意

如果 OceanBase 集群当前版本和目标版本之间存在 barrier 版本，那么 OceanBase 集群应该先升级到 barrier 版本，然后再从 barrier 版本升级到目标版本。

#### 注意

- 如果在您的升级路径中存在 barrier 版本，请先安装相应的 barrier 版本的 RPM 包。等待集群成功升级到 barrier 版本后，再安装目标版本的 RPM 包。
- 如果升级路径中有多个 barrier 版本，按照顺序依次进行安装和升级 barrier 版本，直到集群成功升级最后的 barrier 版本再安装目标版本的 RPM 包。

#### 说明

升级相关脚本和 `oceanbase_upgrade_dep.yml` 文件存放 `/home/admin/oceanbase/etc` 目录下。目录 `/home/admin/oceanbase/etc` 为 OceanBase 数据库的默认安装目录。

#### 注意

单机或单副本 OceanBase 数据库升级无需停止 Zone（`STOP ZONE`）。

#### 说明

再次启动 observer 进程时不需要指定启动参数，因为之前的启动参数已经写到参数文件里了。

#### 注意

在执行升级脚本 `upgrade_post.py` 时，若出现错误，其原因很可能是 RS 切主过。建议通过以下步骤进行排查与修复：

1.  可以执行 `SELECT * FROM oceanbase.DBA_OB_TENANT_JOBS WHERE job_type = 'upgrade_all' ORDER BY job_id DESC LIMIT 1;` 验证升级任务状态。若 `JOB_STATUS` 显示为 `inprogress`，且 `MODIFY_TIME` 为最近时间（与当前时间间隔较短），则可以手动执行一下 `ALTER SYSTEM RUN UPGRADE JOB 'UPGRADE_ALL';` 命令解决这个问题。
2.  重新执行升级脚本。
