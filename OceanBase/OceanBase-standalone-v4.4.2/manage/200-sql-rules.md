---
title: "SQL 规范"
book: "管理数据库"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077600.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# SQL 规范

#### 注意

数据量上限在几百上千条的配置表，一般用于定期缓存加载或者读取配置场景的表，允许全表扫描。

#### 注意

对唯一索引，该条为建议性质约束，业务需根据自己实际业务情况做选择，若无特殊业务场景，建议 UK 索引中所包含的所有列都设置非 NULL 约束，避免出现 UK 失效情况。
