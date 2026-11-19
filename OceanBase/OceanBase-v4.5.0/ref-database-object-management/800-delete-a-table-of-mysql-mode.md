---
title: "删除表"
book: "数据库对象管理"
version: V4.5.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000004476739.html"
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

或者

```sql
obclient> DROP TABLE IF EXISTS test;
```

在删除表时，如果指定了 `IF EXISTS`，即使要删除的表不存在也不会报错；如果不指定 `IF EXISTS`，则会报错。

对于 `DROP TABLE` 操作：

* 当租户关闭回收站功能时，`DROP TABLE` 操作表示删除表。

* 当租户开启回收站功能时，`DROP TABLE` 操作表示删除的表会进入回收站。对于回收站中的表，后续您可以通过回收站功能进一步删除或恢复该表，回收站相关操作请参见 [恢复回收站对象](../../../../600.manage/400.high-availability/500.recyclebin-management/400.restore-the-recyclebin-objects.md)。

* 回收站开关由系统变量 `recyclebin` 控制，默认为关闭状态。
