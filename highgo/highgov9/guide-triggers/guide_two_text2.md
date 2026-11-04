---
title: "创建触发器"
book: "触发器"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/guide/guide_two_text2.html"
tags:
  - highgo
  - highgo-v9
  - guide-triggers
---

## 创建触发器

HGDB 中触发器必须结合触发器函数来使用，需要先用 `CREATE FUNCTION` 创建触发器函数，再用 `CREATE TRIGGER` 创建触发器。触发器函数必须声明为无参，且返回 trigger 类型，一个触发器函数可用于多个触发器。有关 `CREATE FUNCTION` 的用法将在下一节介绍。

```sql
CREATE TRIGGER trigger_name [BEFORE|AFTER|INSTEAD OF] event_name ON table_name
[
 -- 触发器逻辑....
];
```

event\_name 可以是在所提到的表 table\_name 上的 `INSERT` 、 `DELETE` 和 `UPDATE` 数据库操作，在表名后指定 `FOR EACH ROW` 即为行级触发器。

下面来创建一个完整的触发器：

```sql
CREATE OR REPLACE FUNCTION public.log_booksusers_delete()
 RETURNS trigger
 LANGUAGE plpgsql
AS $function$
begin
  insert into  table_change_log(log_id, table_name, operation_type, user_name, row_data)
  values (nextval('seq_table_change_log'),
  'customers',
  'DELETE',
  USER,
  'ID: ' ||  OLD.user_id || ', Name: ' ||  OLD.book_id);
end;
$function$
;

可以通过OLD或者NEW获取上一条删除的数据与下一条新增的数据

在创建一个
CREATE TRIGGER log_booksusers_delete after delete on "BOOKSUSERS" 
for each row 
EXECUTE FUNCTION log_booksusers_delete(); 来调用函数
```