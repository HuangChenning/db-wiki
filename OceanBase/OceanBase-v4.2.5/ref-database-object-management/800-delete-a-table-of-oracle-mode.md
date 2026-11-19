---
title: "删除表"
book: "数据库对象管理"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001501834.html"
tags:
  - oceanbase
  - distributed
  - ref-database-object-management
---

# 删除表

当一个表不再使用时，可以使用 `DROP TABLE` 语句将其删除。

删除表的示例如下：

```sql
obclient> DROP TABLE test;
```

对于 `DROP TABLE` 操作：

* 当租户关闭回收站功能时，`DROP TABLE` 操作表示删除表。回收站开关由系统变量 `recyclebin` 控制，默认为关闭状态。

* 当租户开启回收站功能时，`DROP TABLE` 操作表示删除的表会进入回收站。对于回收站中的表，后续您可以通过回收站功能进一步删除或恢复该表，回收站相关操作请参见 [恢复回收站对象](../../../../600.manage/400.high-availability/500.recyclebin-management/400.restore-the-recyclebin-objects.md)。
