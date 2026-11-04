---
title: "管理触发器"
book: "触发器"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/guide/guide_two_text3.html"
tags:
  - highgo
  - highgo-v9
  - guide-triggers
---

## 管理触发器

可以通过 `ALTER` 来实现对触发器的管理。

1. 修改触发器名称
```sql
ALTER TRIGGER name ON table_name RENAME TO new_name;
```
1. 启用和禁用触发器
```sql
ALTER TABLE table_name {ENABLE|DISABLE} TRIGGER {trigger_name | ALL | USER}
```

例如将前面创建的 log\_booksusers\_delete触发器重命名为 log\_booksusers\_delete\_copy并将之禁用：

```sql
ALTER TRIGGER log_booksusers_delete ON table_change_log RENAME to log_booksusers_delete_copy;
ALTER TABLE table_change_log DISABLE T log_booksusers_delete_copy;
```