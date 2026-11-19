---
title: "事务隔离级别概述"
book: "系统原理"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006078156.html"
tags:
  - oceanbase
  - standalone
  - ref-oceanbase-database-concepts
---

# 事务隔离级别概述

#### 注意

串行化隔离级别下，开启事务后，会保留事务快照，事务提交后快照才会回收。因此，串行化隔离级别下，需要注意及时提交事务，否则可能遇到磁盘占用变大或者读取越来越慢的问题。
