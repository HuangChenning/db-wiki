---
title: "备份恢复性能调优"
book: "管理数据库"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003522260.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 备份恢复性能调优

#### 注意

跨租户导表会消耗大量的临时存储空间和内存资源，建议结合租户的资源情况合理调大。其中，临时存储空间的消耗是在重建索引阶段，如果表的数据量很大，可能会消耗大量的临时空间。临时空间消耗大可能导致出现查询失败，事务回滚、服务不可用等问题。
