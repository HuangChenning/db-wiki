---
title: "ODP 路由最佳实践"
book: "路由"
version: master
source: "https://www.oceanbase.com/docs/common-best-practices-1000000001591716.html"
tags:
  - oceanbase
  - best-practices
  - route
---

# ODP 路由最佳实践

#### 说明

- 指定 IP 路由和指定 Zone 路由，是强制性的路由，不会区分是否强读，适用于不关心 Leader 位置，需要路由到指定节点的场景。
- 如果是交易支付等强读业务，希望路由到 Leader 的场景，需要确保强制路由配置项没有设置，避免产生大量远程路由、二次路由等问题。

#### 说明

- OceanBase 数据库有 Local 计划、Remote 计划和 Distributed 计划三种表路由。
- Local 计划、Remote 计划均为单分区的路由。ODP 的作用是尽量消除 Remote 计划，将路由尽可能的变为 Local 计划。
- 如果表路由类型为 Remote 计划的 SQL 过多，说明该 ODP 的路由可能存在问题，需要排查。

#### 说明

对于生产环境和测试环境，一般情况下，建议 `enable_cached_server` 设置为 `false`。

#### 说明

OceanBase 数据库 V4.1.0 版本开始支持分布式事务路由。

#### 说明

弱读的路由策略 LDC 路由和随机路由，同样适用于计算分区失败的强读路由请求。

#### 注意

设置之前，需确保没有设置过指定 IP 路由的配置。可通过 `show proxyconfig like 'target_db_server';` 命令进行检查。

#### 注意

设置之前，需确保没有设置过指定 IP 路由及指定 Zone 路由。可通过 `show proxyconfig like 'target_db_server';` 和 `show proxyconfig like 'proxy_primary_zone_name';` 命令进行检查。
