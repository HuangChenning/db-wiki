---
title: "集群信息"
book: "组件 & 工具"
version: V4.5.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000004479363.html"
tags:
  - oceanbase
  - distributed
  - ref-components-and-tools
---

# 集群信息

登录 obshell Dashboard 后，系统默认进入 **集群管理** 页面。**集群管理** 页面展示了当前登录用户下的集群概览信息，包括：**基本信息**、**OBServer 统计**、**租户统计**、**租户合并时间 Top3**、**资源水位**、**租户资源使用 Top3** 和 **拓扑结构**。同时支持进行参数管理、启停集群、启停 Zone、启停 OBServer、升级集群版本、升级 obshell 和管理死锁自动检测操作。

本文仅介绍 **集群管理** 页面的展示信息情况，其他需操作的步骤介绍可参见 [集群管理](./300.ob-dashboard-cluster/100.ob-dashboard-cluster-management.md)。

## 基本信息

**基本信息** 模块展示了集群名、集群状态以及集群的 OceanBase 版本号。

![基本信息](img/74d75fbe02d85845.png)

## OBServer 统计

您可在 **OBServer 统计** 模块查看集群中 OBServer 节点的运行状态，方便您及时对状态异常的 OBServer 节点进行运维管理。

![OBServer 统计](img/40ce1db6f402281b.png)

## 租户统计

您可在 **租户统计** 模块查看集群中租户的运行状态，方便您及时对状态异常的租户进行运维管理。单击运行状态后方的数字，页面将跳转至 **租户管理** 页面。

![租户统计](img/7342cbf36de1a362.png)

## 租户合并时间 Top3

**租户合并时间 Top3** 区域展示了按最近一次合并时间进行排序的 3 个租户。合并操作（Major freeze）是将动静态数据做归并，会比较费时。当转储产生的增量数据积累到一定程度时，通过合并操作实现大版本的合并。

![合并时间](img/c9f8f833b6e2d4f3.png)

## 资源水位

**资源水位** 区域展示了集群的 **CPU**、**内存** 和 **数据盘** 的总量、已分配、消耗比和剩余情况，将光标悬停于资源饼图部分会展示详细情况。当光标悬停于模块右上角 **···** 时，可查看集群名称和部署模式信息。

![资源水位](img/f221750afa16598e.png)


## 租户资源使用 Top3

为您展示 **CPU 消耗比**、**内存消耗比** 和 **数据量** 前 3 的 OceanBase 租户数据。

![资源使用](img/1e801d1075bcf4ce.png)

## 拓扑结构

您可在 **拓扑结构** 区域中查看集群下 Zone 的名称、所属 Region、OBServer 数量、Root Server、状态，单击 **状态** 后的 <span style="vertical-align: middle;"><img src="https://obbusiness-private.oss-cn-shanghai.aliyuncs.com/doc/img/observer-enterprise/V4.3.5/700.reference/1500.Components-and-Tools/100.obshell/500.icon/100.ob-dashboard-tenant-02.png" alt="筛选" style="height: 20px;"></span> 图标，可按照 Zone 的状态筛选 Zone。支持对 Zone 进行启停操作，操作详见 [管理 Zone](300.ob-dashboard-cluster/200.ob-dashboard-zone-management.md)。单击 Zone 名称前的 <span style="vertical-align: middle;"><img src="https://obbusiness-private.oss-cn-shanghai.aliyuncs.com/doc/img/observer-enterprise/V4.3.5/700.reference/1500.Components-and-Tools/100.obshell/500.icon/200.ob-dashboard-cluster-overview-01.png" alt="展开" style="height: 20px;"></span>，可查看该 Zone 下的 OBServer 详情，包括 **IP**、**SQL 端口**、**RPC 端口**、**硬件架构**、**数据盘路径**、**日志盘路径**、**资源水位** 和 **状态**，支持对 Zone 内的 OBServer 节点服务和进程进行启停操作，操作详见 [管理 OBServer 节点](300.ob-dashboard-cluster/300.ob-dashboard-observer-management.md)。

![拓扑结构](img/726a97d07340df3b.png)
