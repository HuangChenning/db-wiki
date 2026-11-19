---
title: "数据库对象类型"
book: "系统原理"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003578342.html"
tags:
  - oceanbase
  - standalone
  - ref-oceanbase-database-concepts
---

# 数据库对象类型

数据库对象（即 Schema 对象）属于某一个 Schema。Schema 为数据库对象的集合，一个用户有一个缺省的 Schema，其 Schema 名称就等于用户名。用户还可以访问和使用其他的 Schema。如果访问一个 Schema 中的对象时，没有指明该对象属于哪一个 Schema，系统就会自动给对象加上缺省的 Schema 名称。

有关 OceanBase 数据库 Oracle 模式下的数据库对象的详细信息如下表所示。

[TABLE]
