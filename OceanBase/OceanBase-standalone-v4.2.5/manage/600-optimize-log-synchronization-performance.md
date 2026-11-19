---
title: "优化日志同步性能"
book: "管理数据库"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000002702060.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 优化日志同步性能

#### 注意

由于调大 `log_archive_concurrency` 和 `log_restore_concurrency` 两个配置项的默认值均会为日志归档和日志恢复分配更多的 CPU 和内存资源，可能对正常的数据库执行带来负面影响，故在未确定有明确的性能瓶颈并经过实际验证的情况下，不建议修改配置项 `log_archive_concurrency` 和 `log_restore_concurrency` 的默认值。

#### 注意

对于小规模租户（ CPU 为 2C、4C 的租户），建议使用默认值，不要调整该配置项的值。

#### 注意

对于小规模租户（CPU 为 2C、4C 的租户），建议使用默认值，不要调整该配置项的值。
