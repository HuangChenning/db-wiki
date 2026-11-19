---
title: "释放保存点"
book: "应用开发"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077953.html"
tags:
  - oceanbase
  - standalone
  - develop
---

# 释放保存点

#### 注意

当 `RELEASE SAVEPOINT` 语句执行成功后，被释放的保存点不能再回滚到指定的保存点以及 `RELEASE SAVEPOINT` 语句与指定的保存点之间的任何其他保存点。
