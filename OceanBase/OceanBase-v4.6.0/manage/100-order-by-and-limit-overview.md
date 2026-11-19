---
title: "排序和 limit 优化概述"
book: "管理数据库"
version: V4.6.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005685817.html"
tags:
  - oceanbase
  - distributed
  - manage
---

# 排序和 limit 优化概述

order by + limit 是常见的业务查询场景，用于获取排序后的一定行数的结果集。为获取这些结果集，最终生成的的查询计划可能仅需要从相关表上读取很少的数据，得到一个执行效率高的计划，也可能需要读取相关表的全部数据经过一定运算后仅返回需要的结果行，相比前者这一般是个效率较差的计划。在这种场景的调优中，需要理解产生这两种计划的原因并通过一些优化方法获得效率较高的计划。
