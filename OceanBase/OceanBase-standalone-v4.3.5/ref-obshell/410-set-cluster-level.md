---
title: "设置集群级配置"
book: obshell
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003975944.html"
tags:
  - oceanbase
  - standalone
  - ref-obshell
---

# 设置集群级配置

#### 说明

设置集群级配置时采取全量覆盖策略，即原有配置将被新配置完全替代。

#### 说明

自 obshell V4.2.4.0 起，配置 rootPwd 参数无需加密。使用之前版本的 obshell 调用该 API 时仍需对 rootPwd 参数进行加密，详细介绍可参见 [API 混合加密](20-api-hybrid-encryption.md)。
