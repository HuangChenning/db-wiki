---
title: "配置时钟源"
book: "部署集中式版"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003577358.html"
tags:
  - oceanbase
  - standalone
  - deploy
---

# 配置时钟源

#### 说明

- 本文基于 x86 架构的 CentOS Linux 7.9 镜像环境提供操作指导，其余环境可能略有不同，请以实际环境为准。

- OceanBase 自 V4.0.0 起支持动态修改时钟，修改的间隔在 2s 以内时不会对数据正确性和集群稳定运行带来影响。

- 若部署 OCP 的节点和 OceanBase 集中式数据库不在一个节点时，也需为 OCP 的节点与 OceanBase 集中式数据库节点做时钟源同步，防止使用过程中因时钟偏差引发 OCP 操作异常。

#### 注意

NTP 服务端服务启动后，您需要等待 5 分钟再开启 NTP 客户端服务。否则系统会提示 "no server suitable for synchronization found"。
