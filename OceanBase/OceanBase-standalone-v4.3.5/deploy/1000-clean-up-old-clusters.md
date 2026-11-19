---
title: "清理旧环境"
book: "部署集中式版"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003577352.html"
tags:
  - oceanbase
  - standalone
  - deploy
---

# 清理旧环境

#### 注意

destroy 命令不可逆，会在停止 OBServer 进程的同时清除数据库文件。因此执行以下命令前，请先确认集中式数据库已经不再使用，并且需要备份的数据已经完成备份。

#### 注意

执行 `install_obd.sh` 不需要加 sudo 。
