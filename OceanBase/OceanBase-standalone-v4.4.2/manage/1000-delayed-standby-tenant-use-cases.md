---
title: "备库延迟应用案例"
book: "管理数据库"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006547426.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 备库延迟应用案例

#### 注意

在进行下面的操作时，必须先设置备库的同步终点（步骤 2）再取消备库的延迟（步骤 3），否则，取消延迟后备库会全速追赶，可能会追过误操作的位点。同时，在恢复配置时，必须先恢复备库的延迟配置（步骤 6）再解除恢复终点（步骤 7），避免日志瞬间追过。
