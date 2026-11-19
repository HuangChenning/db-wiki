---
title: "SQL 监控概述"
book: "管理数据库"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077617.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# SQL 监控概述

前面讨论的都是系统监控，使用者根据特定的监控信息，对系统（集群、租户、会话）的健康状况作出判断。实际运维中，另一类非常重要的监控手段是 SQL 监控，即根据特定 SQL 的多次执行或特定执行中收集的监控信息对系统的性能问题进行诊断。

SQL 相关的监控信息，记录 SQL 在执行过程中的资源消耗，这些信息通常在一条 SQL 执行的前后，通过收集监控项和等待事件的统计信息，并计算差值来获得。除此之外，SQL 监控还包含 SQL 文本、SQL 计划、执行反馈等信息，这些信息在诊断一个具体的 SQL 问题时会非常有帮助。

下图展示了一个可能的 SQL 问题诊断路径：

![SQL 诊断](img/3a64303491295fba.jpg)

OceanBase 数据库提供了多种视图用于 SQL 诊断，主要视图如下：

| 视图 | 展示内容 |
|----|----|
| [GV\$OB_SQL_AUDIT](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005284886) | SQL 统计信息。 |
| [GV\$OB_PLAN_CACHE_PLAN_STAT](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005284863) | 执行计划统计信息。 |
| [GV\$OB_PLAN_CACHE_PLAN_EXPLAIN](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005284976) | 执行计划详细信息。 |
| [DBA_OB_OUTLINES](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005284144) | 普通 Outline 信息。 |
| [DBA_OB_CONCURRENT_LIMIT_SQL](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005284103) | 限流 Outline 信息。 |
| [GV\$OB_PLAN_CACHE_STAT](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005283855) | Plan Cache 统计信息。 |
| [GV\$SQL_PLAN_MONITOR](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005284990) | SQL 算子级统计信息。 |
| [GV\$SESSION_EVENT](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005284908) | 会话级等待统计。 |
| [GV\$OB_TRANSACTION_PARTICIPANTS](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005284864) | 活跃事务的参与者信息。 |
| [DBA_INDEX_USAGE](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005285160) | 用于展示索引使用数据信息。 |
