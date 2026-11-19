---
title: "使用 obd 升级 OceanBase 集中式数据库"
book: "升级集中式版"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006076921.html"
tags:
  - oceanbase
  - standalone
  - upgade
---

# 使用 obd 升级 OceanBase 集中式数据库

#### 注意

如果是从 V4.2.5 BP3~BP6 或者 V4.3.5 BP3~BP5 版本升级到 V4.4.2 BP1 版本，还需要准备对应的 barrier 版本（V4.2.5 BP7 或者 V4.3.5 BP6）的安装包。

#### 注意

不要和之前部署的目录在一起，避免新旧安装包混合在一起。

#### 注意

执行 `bash bin/uninstall_obd.sh` 不需要加 sudo 。

#### 注意

此步骤仅为 V4.2.5 BP3~BP6 或者 V4.3.5 BP3~BP5 版本升级到 V4.4.2 BP1 版本时需要。
