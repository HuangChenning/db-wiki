---
title: "管理触发器"
book: "触发器"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/sql/control_t.html"
tags:
  - highgo
  - highgo-v45
  - sql-triggers
---

## 管理触发器

可以通过 `ALTER` 来实现对触发器的管理。

1. 修改触发器名称
```sql
ALTER TRIGGER name ON table_name RENAME TO new_name;
```
2. 启用和禁用触发器
```sql
ALTER TABLE table_name {ENABLE|DISABLE} TRIGGER {trigger_name | ALL | USER}
```

例如将前面创建的 tg1 触发器重命名为 tg1\_newname 并将之禁用：

```sql
ALTER TRIGGER tg1 ON products RENAME to tg1_newname;
ALTER TABLE products DISABLE T tg1_newname;
```