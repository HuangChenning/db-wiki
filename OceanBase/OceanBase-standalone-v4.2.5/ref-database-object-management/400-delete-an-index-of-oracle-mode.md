---
title: "删除索引"
book: "数据库对象管理"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003150376.html"
tags:
  - oceanbase
  - standalone
  - ref-database-object-management
---

# 删除索引

当索引过多时，维护开销会增大，您可以根据需要删除不必要的索引。

删除索引的语法格式如下：

``` sql
DROP INDEX index_name;
```

删除表的索引的示例如下：

``` sql
obclient> DROP INDEX t3_ind2;
Query OK, 0 rows affected (0.02 sec)
```
