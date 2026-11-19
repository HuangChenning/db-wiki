---
title: "容量问题"
book: "管理数据库"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003577861.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 容量问题

#### 说明

关于 `V$OB_SQL_AUDIT` 的详细介绍，参见 [V\$OB_SQL_AUDIT(Oracle 模式)](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002014202) 和 [V\$OB_SQL_AUDIT(MySQL 模式)](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002015089)。

#### 说明

`cpu_quota_concurrency`用于设置租户的每个 CPU 配额所允许的最大并发数。详细信息，参见 [cpu_quota_concurrency](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002015547)。

#### 注意

当出现容量问题时，一般采用扩容的方式解决（或者是调大租户的 CPU 规格，或者是调大 `cpu_quota_concurrency`），工作线程增加后需要使用的内存资源也会增加，所以还需要同步调大租户的内存规格。
