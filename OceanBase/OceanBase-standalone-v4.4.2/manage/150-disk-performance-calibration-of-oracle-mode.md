---
title: "磁盘性能校准"
book: "管理数据库"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006078067.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 磁盘性能校准

#### 说明

在当前版本中，CPU 和 IOPS 资源隔离均不再强依赖磁盘性能校准操作。

#### 说明

指定磁盘校准信息时，如果当前没有相关磁盘的压测数据，您可以使用 FIO 工具执行一次性能压测来获取当前磁盘的性能数据，有关 FIO 工具的详细介绍及使用，请参见 [FIO 工具官网](https://fio.readthedocs.io/en/latest/index.html)。
