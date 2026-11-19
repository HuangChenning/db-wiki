---
title: "配置 sysctl.conf"
book: "部署集中式版"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006076968.html"
tags:
  - oceanbase
  - standalone
  - deploy
---

# 配置 sysctl.conf

#### 说明

您必须在每台部署 OceanBase 节点的机器上执行此操作。

#### 注意

- `max_map_count` 配置不合理的情况下，可能会导致严重的内存泄露。
- 至少需要给 core 文件的目录预留和 OBServer 配置的 memory_limit 同等大小的磁盘空间，同时应避免影响到数据目录和日志目录的可用空间。
