---
title: "删除触发器"
book: "触发器"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/sql/delete_t.html"
tags:
  - highgo
  - highgo-v45
  - sql-triggers
---

## 删除触发器

触发器的删除可以用 `DROP TRIGGER` 、 `DROP FUNCTION` 将触发器和触发器函数分开删除，也可以通过 `CASCADE` 删除触发器函数来将两者一起删除。

```sql
DROP TRIGGER trigger_name ON table_name;
```

例如删除上面创建的触发器：

```sql
highgo=# DROP TRIGGER tg1_newname ON products;
DROP TRIGGER
highgo=# DROP FUNCTION products_insert_trigger_func();
DROP FUNCTION

highgo=# DROP FUNCTION products_insert_trigger_func() CASCADE;
注意：递归删除 触发器 tg1 在表 products
DROP FUNCTION
```