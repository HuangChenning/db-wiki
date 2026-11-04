---
title: "创建触发器"
book: "触发器"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/sql/create_t.html"
tags:
  - highgo
  - highgo-v45
  - sql-triggers
---

## 创建触发器

HGDB 中触发器必须结合触发器函数来使用，需要先用 `CREATE FUNCTION` 创建触发器函数，再用 `CREATE TRIGGER` 创建触发器。触发器函数必须声明为无参，且返回 trigger 类型，一个触发器函数可用于多个触发器。有关 `CREATE FUNCTION` 的用法将在下一节介绍。

触发器的创建语句如下：

```sql
CREATE TRIGGER trigger_name [BEFORE|AFTER|INSTEAD OF] event_name ON table_name
[
 -- 触发器逻辑....
];
```

event\_name 可以是在所提到的表 table\_name 上的 `INSERT` 、 `DELETE` 和 `UPDATE` 数据库操作，在表名后指定 `FOR EACH ROW` 即为行级触发器。

下面来创建一个完整的触发器：

```sql
highgo=# CREATE OR REPLACE FUNCTION products_insert_trigger_func() RETURNS TRIGGER AS $$
DECLARE 
BEGIN
    RAISE NOTICE 'the function products_insert_trigger_func has been invoked';  --抛出提示
    RETURN null;
END
$$
LANGUAGE plpgsql;           --创建触发器函数
CREATE FUNCTION         

highgo=# CREATE TRIGGER tg1 AFTER INSERT ON products FOR EACH ROW EXECUTE PROCEDURE products_insert_trigger_func();   --创建触发器，定义在 INSERT 之后的行级触发器
CREATE TRIGGER

highgo=# INSERT INTO products VALUES(3,'c',3);   --触发
注意:  the function products_insert_trigger_func has been invoked
INSERT 0 1
```

`RAISE` 可用于报告信息和抛出错误，有关 `RAISE` 的用法将在下节介绍。