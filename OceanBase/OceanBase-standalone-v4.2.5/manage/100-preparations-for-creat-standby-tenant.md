---
title: "创建备租户前准备"
book: "管理数据库"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000002702067.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 创建备租户前准备

#### 注意

- 选择好备租户的源端后，在创建备租户前，建议为该备租户对应的源端租户（主租户或另一个备租户）开启日志归档。这是因为，如果源端租户未开启日志归档，当备租户落后于源端租户而源端租户的日志又已经回收时，就会导致备租户的日志同步卡住。如果源端租户在创建备租户前已开启日志归档，则出现该情况时，备租户可以自动从源端租户的归档日志中补齐这部分数据。
- 为源端租户开启日志归档的详细操作，请参见 [开启归档模式](300-open-the-log-archive-mode.md)。
- 如果因未开启源端租户的日志归档，出现了备租户日志同步卡住的现象，请参考 [物理备库同步过程中卡住](100-physical-standby-database-synchrolock.md) 中的 **问题三：备库日志同步状态异常** 进行排查。
