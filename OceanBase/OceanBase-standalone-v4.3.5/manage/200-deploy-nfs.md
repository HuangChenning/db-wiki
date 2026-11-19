---
title: "部署 NFS"
book: "管理数据库"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003577389.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 部署 NFS

#### 注意

如果您使用的是 NFS 硬件设备，则可跳过本操作，直接部署 NFS 客户端。

#### 注意

- 在挂载 NFS 3/4 时，必须保证备份挂载环境的参数中包含示例中建议的参数。
- Docker 环境需要在宿主机上挂载 NFS，然后映射到 Docker 里面。如果 Docker 内部直接挂载 NFS，可能会出现客户端 Hang 住的场景。
