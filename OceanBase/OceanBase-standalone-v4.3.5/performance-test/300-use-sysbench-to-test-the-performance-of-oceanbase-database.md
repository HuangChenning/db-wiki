---
title: "OceanBase 集中式数据库 Sysbench 测试"
book: "性能测试"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003577318.html"
tags:
  - oceanbase
  - standalone
  - performance-test
---

# OceanBase 集中式数据库 Sysbench 测试

#### 说明

为了提升用户体验和易用性，让每一个开发者在使用数据库时都能获得较好的性能，OceanBase 数据库在 V4.0.0 版本之后，做了大量的优化工作。本性能测试方法仅基于基础参数进行调优，让开发者获得较好的数据库性能体验。

#### 注意

当使用的 OBClient 版本大于等于 2.2.0 时，会默认开启 ob20 协议以及全链路追踪的能力，在 Sysbench 测试中会影响性能，建议通过设置环境变量手动关闭：`export ENABLE_PROTOCOL_OB20=0`。

#### 注意

- 上文的租户规格可根据自身数据库的硬件配置进行动态调整。
- 部署集群时，建议不要使用 `obd cluster autodeploy` 命令，该命令为了保证稳定性，不会最大化资源利用率（例如不会使用所有内存），建议使用交互式部署或者 `obd cluster deploy` 部署。

#### 说明

在 Sysbench 测试中，部署 Sysbench 和 obd 的机器有一定的灵活性，根据 OBServer 总核数的不同分为以下三种情况：

- 当 OBServer 总核数小于等于 47 核时，该机器仅需要 8 核 64G 即可。
- 当 OBServer 总核数在 48 核和 72 核之间时，该机器需要 16 核 128G。
- 当 OBServer 总核数大于等于 73 核时，该机器需要 32 核 128G。
