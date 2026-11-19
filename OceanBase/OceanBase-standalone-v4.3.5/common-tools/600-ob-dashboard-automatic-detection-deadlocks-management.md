---
title: "管理死锁自动检测"
book: "常用工具"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000005411377.html"
tags:
  - oceanbase
  - standalone
  - common-tools
---

# 管理死锁自动检测

#### 说明

关闭死锁自动检测后，将不再进行自动死锁检测和解决死锁，请谨慎操作。

#### 说明

开启死锁自动检测后会自动检测并解决死锁，集群内所有租户将同步开启，本功能对集群有 2% 左右的性能损耗，请谨慎操作。
