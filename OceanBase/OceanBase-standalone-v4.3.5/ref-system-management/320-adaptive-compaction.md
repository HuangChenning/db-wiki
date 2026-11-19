---
title: "自适应合并"
book: "系统管理"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003578052.html"
tags:
  - oceanbase
  - standalone
  - ref-system-management
---

# 自适应合并

#### 注意

由于自适应合并调度任务的执行会占用部分系统资源，为了减少系统资源的占用，您可以通过将租户级隐藏配置项 `_enable_adaptive_compaction` 的值修改为 `False` 来关闭除 extreme 模式表以外的其他自适应合并的调度。
