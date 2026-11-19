---
title: "监控概述"
book: "管理数据库"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003577409.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 监控概述

#### 说明

- 监控指标的数据来源于 OceanBase 数据库的视图，但日常工作中应该尽量使用可视化的外部监控系统，可以更加方便的分析监控指标的变化趋势，提高效率。
- 由于 `GV$` 视图和 `V$` 视图的同质性，下文不再特殊区分，将根据具体场景选择合适的视图。
