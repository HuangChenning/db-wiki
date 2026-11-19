---
title: "设置和查看审计规则"
book: "管理数据库"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077557.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 设置和查看审计规则

#### 说明

该功能从 V4.4.2 BP2 版本开始引入，仅适用于将审计记录写入磁盘文件的场景（`audit_trail` 为 `LOG`）。

#### 注意

使用该函数需拥有 `SUPER` 权限。

#### 注意

仅在 `audit_log_encryption` 配置项开启且此步骤执行成功后，归档生成的审计日志文件才会被加密存储。

#### 说明

使用该函数需拥有 `SUPER` 权限。
