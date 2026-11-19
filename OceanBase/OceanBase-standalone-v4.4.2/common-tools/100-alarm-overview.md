---
title: "告警概述"
book: "常用工具"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077505.html"
tags:
  - oceanbase
  - standalone
  - common-tools
---

# 告警概述

#### 说明

仅首次登录 **告警中心** 页面需输入 Alertmanager 地址、用户名、密码等信息。

#### 说明

目前 obshell Dashboard 不提供修改告警规则配置功能，不支持自定义类型的告警规则。您可以通过修改 Prometheus 的配置文件进行修改。

#### 说明

如果您使用的是 RPM 包部署方式，Prometheus 配置文件目录为默认的 `/usr/prometheus/prometheus.yaml`。

#### 说明

您需要将 `--user 用户名:密码` 替换为部署 Prometheus 使用的真实用户及密码，否则配置可能无法生效。
