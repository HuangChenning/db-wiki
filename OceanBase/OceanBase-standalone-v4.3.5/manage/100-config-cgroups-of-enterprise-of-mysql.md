---
title: "配置 cgroup"
book: "管理数据库"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003578211.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 配置 cgroup

#### 注意

- cgroup 系统目录的配置操作可以在 OceanBase 数据库软件安装前进行，也可以在 OceanBase 数据库软件安装后进行。本文档以 OceanBase 数据库软件已安装的前提下为例，提供 cgroup 系统目录的配置操作指导。
- 配置 cgroup 系统目录时需要 `root` 用户权限。

#### 说明

如果已经存在 `/sys/fs/cgroup` 目录，则可忽略该步骤。

#### 说明

如果已经存在 `/sys/fs/cgroup/cpu` 目录且目录为空，则可忽略该步骤。
