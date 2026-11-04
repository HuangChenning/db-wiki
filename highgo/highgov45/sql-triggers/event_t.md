---
title: "事件触发器"
book: "触发器"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/sql/event_t.html"
tags:
  - highgo
  - highgo-v45
  - sql-triggers
---

## 事件触发器

基于某个表或者视图数据变更的触发器被称为数据变更触发器（DML 触发器），基于数据库事件的触发器被称为事件触发器（DDL 触发器）。只要与一个事件触发器相关的事件在事件触发器所在的数据库中发生，该事件触发器就会被引发，当前支持的事件是 ddl\_command\_start、ddl\_command\_end、 table\_rewrite 和 sql\_drop。

ddl\_command\_start 事件在 `CREATE` 、 `ALTER` 、 `DROP` 、 `SECURITY LABEL` 、 `COMMENT` 、 `GRANT` 或者 `REVOKE` 命令的执行之前发生，相应的，ddl\_command\_end 事件在这些命令执行之后发生。table\_rewrite 事件在表被命令 `ALTER TABLE` 和 `ALTER TYPE` 的某些动作重写之前发生。sql\_drop 事件为任何删除数据库对象的操作在 ddl\_command\_end 事件触发器之前发生。

事件触发器在创建时也要先创建触发器函数再创建触发器，创建事件触发器的命令为 `CREATE EVENT TRIGGER` 。例如创建如下 `ddl_command_start` 事件触发器：

```sql
CREATE OR REPLACE FUNCTION event_trigger_demo() RETURNS event_trigger AS
$$
BEGIN
  IF (user != 'sysdba') THEN
    RAISE EXCEPTION 'command % is disabled', tg_tag;
  END IF;
END
$$
LANGUAGE plpgsql;

CREATE EVENT TRIGGER event_demo ON ddl_command_start
  EXECUTE FUNCTION event_trigger_demo();
```

上面的事件触发器限制了用户对数据库的 DDL 语句，如果不是 sysdba 用户，相关 `CREATE` 、 `DROP` 等操作都将被拒绝。例如 `\c highgo test` 切换 test 用户，CREATE 及 DROP 等命令都被拒绝。

```sql
highgo=> CREATE TABLE b(t int);
错误:  command CREATE TABLE is disabled

highgo=> DROP TABLE test1;
错误:  command DROP TABLE is disabled
```

事件触发器的重命名、禁用/启用、删除操作如下所示：

```sql
ALTER EVENT TRIGGER event_demo RENAME TO new_name;
ALTER EVENT TRIGGER new_name DISABLE;
ALTER EVENT TRIGGER new_name ENABLE;
DROP EVENT TRIGGER new_name;
```