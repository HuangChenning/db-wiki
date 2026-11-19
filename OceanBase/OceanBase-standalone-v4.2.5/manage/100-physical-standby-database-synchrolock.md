---
title: "物理备库同步过程中卡住"
book: "管理数据库"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000002701878.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 物理备库同步过程中卡住

#### 注意

视图 `V$OB_LS_LOG_RESTORE_STATUS` 仅展示了日志流 Leader 的同步状态信息，因此，如果备租户出现日志流无主的情况，无法通过该视图查看，需要排查无主问题。
