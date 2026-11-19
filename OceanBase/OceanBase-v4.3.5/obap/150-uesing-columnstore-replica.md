---
title: "部署与使用列存副本"
book: OceanBase AP
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000006175762.html"
tags:
  - oceanbase
  - distributed
  - obap
---

# 部署与使用列存副本

#### 说明

访问 C 副本依赖**独立 ODP（ODP V4.3.2+）**与**弱读 + 列存路由**配置。版本基线与架构选型见 [典型 AP 架构部署指南](100-obap-parameter-config.md) 文首说明。

#### 说明

**C 副本不能替代仲裁（A）**。在 3 Zone 场景下，可直接配置 `F@zone1,F@zone2,C@zone3`，不要求必须新增第 4 个 Zone。

#### 说明

新增第 4 个 Zone 仅适用于希望将 C 副本放在独立 Zone 的场景；不是部署 C 副本的前置条件。若 3 Zone 拓扑已满足隔离诉求，可直接在现有 Zone 上配置 C 副本（如 `F@zone1,F@zone2,C@zone3`）。

#### 注意

`RESOURCE_POOL_LIST` 是**整表替换**语义：需要同时写出已有资源池与新增资源池。若只写 `('pool2')`，会将原有资源池解绑。
