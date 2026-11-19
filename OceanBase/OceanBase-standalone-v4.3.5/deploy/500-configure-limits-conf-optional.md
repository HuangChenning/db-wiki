---
title: "配置 limits.conf"
book: "部署集中式版"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003577356.html"
tags:
  - oceanbase
  - standalone
  - deploy
---

# 配置 limits.conf

#### 说明

您必须在每台部署 OceanBase 节点的机器上执行此操作。

#### 说明

- 您需查看 `/etc/security/limits.d/20-nproc.conf` 文件中是否存在 nproc 的配置，若存在需同步修改该文件中 nproc 的值。
- limits.conf 的配置仅对新登录的会话生效（如新打开的终端、SSH 连接或新启动的进程）。当前已存在的会话或进程不会自动继承新配置，需要重新登录或重启相关服务。
