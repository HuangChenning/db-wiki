---
title: "数据备份失败"
book: "管理数据库"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000002701876.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 数据备份失败

#### 注意

如果在 `observer.log` 中 `grep` 不到相关日志，可能是因为 `observer.log` 切了文件，可以执行 `grep 'YB42C0A80C44-0005F637014C8DE6-0-0' observer.log.*`。

#### 注意

如果在 `observer.log` 中 `grep` 不到相关日志，可能是因为 `observer.log` 切了文件，可以 `grep 'YFA40BA2D90B-005FA487348F363-0-0' observer.log.*`。

#### 注意

如果在 `rootservice.log` 中 `grep` 不到相关日志，可能是因为 `rootservice.log` 切了文件，可以 `grep 'YFA40BA2D90B-005FA487348F363-0-0' rootservice.log.*`。
