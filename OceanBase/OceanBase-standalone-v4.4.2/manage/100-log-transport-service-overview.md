---
title: "日志传输服务概述"
book: "管理数据库"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077530.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 日志传输服务概述

#### 说明

对于基于网络的物理备库，建议主库开启归档模式，否则，备库可能会有断流的风险。例如，以下场景可能会导致断流：

- 主库的日志盘容量不够大时，备库落后场景下可能会同步不到对应的日志。
