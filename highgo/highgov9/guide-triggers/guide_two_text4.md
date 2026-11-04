---
title: "删除触发器"
book: "触发器"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/guide/guide_two_text4.html"
tags:
  - highgo
  - highgo-v9
  - guide-triggers
---

## 删除触发器

触发器的删除可以用 `DROP TRIGGER` 、 `DROP FUNCTION` 将触发器和触发器函数分开删除，也可以通过 `CASCADE` 删除触发器函数来将两者一起删除。

```sql
DROP TRIGGER trigger_name ON table_name;
```

例如删除上面创建的触发器：

```sql
highgo=# DROP TRIGGER log_booksusers_delete ON table_change_log;
DROP TRIGGER
highgo=# DROP FUNCTION log_booksusers_delete();
DROP FUNCTION

highgo=# DROP FUNCTION log_booksusers_delete() CASCADE;
注意：递归删除 触发器 log_booksusers_delete 在表 table_change_log
DROP FUNCTION
```