---
title: "5、如何禁止数据库执行drop table的操作"
book: "日常使用类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/way/droptable.html"
tags:
  - highgo
  - highgo-v45
  - way-daily-use
---

## 如何禁止数据库执行drop table的操作

本文档旨在介绍如何在数据库中通过事件触发器禁止用户执行drop table的操作。

## 1、创建触发器函数：

```
CREATE OR REPLACE FUNCTION abort_DROP_TABLE()
RETURNS event_trigger
LANGUAGE plpgsql
AS $$
BEGIN
  if tg_tag = 'DROP TABLE' THEN
    RAISE EXCEPTION 'command % is disabled', tg_tag;
  END if;
END;
$$;
```

## 2、创建事件触发器：

```
CREATE EVENT TRIGGER abort_drop_table on ddl_command_start EXECUTE FUNCTION abort_DROP_TABLE();
```

## 3、尝试执行drop table 命令报错：

```
highgo=# drop table hgjob_test0305 ;
2021-04-02 10:37:48.575 CST [4665] ERROR: command DROP TABLE is disabled
2021-04-02 10:37:48.575 CST [4665] CONTEXT: PL/pgSQL function abort_drop_table() line 4 at RAISE
2021-04-02 10:37:48.575 CST [4665] STATEMENT: drop table hgjob_test0305 ;
ERROR: command DROP TABLE is disabled
CONTEXT: PL/pgSQL function abort_drop_table() line 4 at RAISE
```