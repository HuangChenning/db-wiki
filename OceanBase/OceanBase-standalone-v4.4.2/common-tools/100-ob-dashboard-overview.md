---
title: obshell Dashboard
book: "常用工具"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077116.html"
tags:
  - oceanbase
  - standalone
  - common-tools
---

# obshell Dashboard

obshell Dashboard 是 obshell 提供的基于 Web 的交互式管理页面，专为 OceanBase 集群和租户资源的管理而设计。它提供了关键资源和性能指标的监控功能，帮助用户高效管理 OceanBase 集群。

obshell Dashboard 服务完全集成在 obshell 进程中，用户可以通过访问任何部署了 obshell 的服务地址来管理 OceanBase 集群。这种设计不仅简化了管理流程，还确保了极低的资源开销，为用户提供简单易用的管控体验。

## 特性介绍

obshell Dashboard 目前支持集中式版 OceanBase 集群管理的以下特性：

- 集群管理：查看 [集群信息](200-ob-dashboard-cluster-overview.md)，包含状态信息、资源消耗、拓扑结构等核心信息，以及 [管理集群](100-ob-dashboard-cluster-management.md)、[管理参数](500-ob-dashboard-parameter.md) 等功能。

- 租户管理：管理集群下的租户及租户中的数据库、用户和参数，具体介绍可参见 [租户管理](100-ob-dashboard-tenant.md) 章节。

- 备份恢复：支持租户级备份能力。具体介绍可参加 [备份恢复](100-tenant-backup-and-recovery-overview.md) 章节。

- 性能监控：展示了集群维度和租户维度的性能数据，集群维度包含数据库和主机两个方面的性能数据，租户维度包含性能与 SQL、事务、存储与缓存三个方面的性能数据，具体介绍可参见 [性能监控](420-Performance-monitoring.md) 。

- 告警中心：obshell Dashboard 提供了告警能力，可通过告警中心查看告警事件、设置告警屏蔽和告警规则，以便及时响应和处理异常情况，确保系统稳定运行，具体介绍可参加 [告警中心](100-alarm-overview.md) 章节。

- 软件包管理：上传软件包，升级 obshell 和 OceanBase 集中式数据库均需保证已上传目标版本的软件包。具体操作可参见 [软件包管理](600-ob-dashboard-package.md)。

## 登录与退出

自 obshell V4.3.0.0 起支持通过图形化界面交互式管理集群，在成功安装 obshell 后，使用 obshell 节点 IP 和 obshell 端口即可访问 obshell Dashboard（obshell 交互式管理页面）。访问时默认使用 sys 租户下的 root 用户登录，密码为部署 OceanBase 集群时设置的 root@sys 用户密码，若 root@sys 密码为空，可直接单击 **登录** 按钮登陆。

登录 obshell Dashboard 控制台后，光标悬停在页面右上角 ![用户](img/3ced0d1f9225189a.png) 图标处，单击出现的 **退出登录**，在弹出的窗口单击 **确定** 即可退出登录。

## 查看版本

登录 obshell Dashboard 控制台后，单击页面右上角 **帮助** \> **关于 obshell Dashboard**，即可查看 obshell Dashboard 的版本。
