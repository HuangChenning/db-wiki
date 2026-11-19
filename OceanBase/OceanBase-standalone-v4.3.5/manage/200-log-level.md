---
title: "日志级别"
book: "管理数据库"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003577426.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 日志级别

#### 注意

本文介绍的查看和设置日志级别仅对普通日志文件（`election.log`、`observer.log`、`rootservice.log`）生效。对于 WARNING 日志文件（带有 \`.wf\` 后缀的日志文件），总是打印 WARN 及高于 WARN 日志级别的日志。

#### 注意

建议仅在 SQL 客户端登录不了 OceanBase 集群的情况下使用 `kill -41/kill -42` 调节日志级别。

#### 说明

如果使用 MySQL 的 C 客户端执行带 Hint 的 SQL 语句，需要使用 `-c` 选项登录，否则 MySQL 客户端会将 Hint 作为注释从用户 SQL 语句中去除，导致系统无法收到用户 Hint。
