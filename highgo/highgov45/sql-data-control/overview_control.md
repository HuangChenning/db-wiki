---
title: "概况"
book: "数据控制"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/sql/overview_control.html"
tags:
  - highgo
  - highgo-v45
  - sql-data-control
---

## 数据控制

数据控制是指设置或者更改数据库用户或角色权限，本节主要介绍有关数据库权限的分配及撤销。

对象（表、视图、模式等）的所有者通常是执行创建语句的角色，对于大部分类型的对象，初始状态下只有所有者（或者超级用户）能够对该对象做任何事情，为了允许其他角色使用它，必须分配权限。权限的分配或撤销通常也只有对象所有者可以进行操作。

权限：SELECT、INSERT、UPDATE、DELETE、TRUNCATE、REFERENCES、TRIGGER、CREATE、CONNECT、TEMPORARY、EXECUTE、USAGE。

用 ALL 取代特定权限会把与对象类型相关的所有权限全部授权。

要分配权限，可以使用 GRANT 命令；要撤销权限，可以使用 REVOKE 命令。

例如给角色 joe 分配 accounts 表 UPDATE 的权限：

```sql
GRANT UPDATE ON accounts TO joe;
```

撤销角色 joe 对表 accounts 的 UPDATE 权限：

```sql
REVOKE UPDATE ON accounts FROM joe;
```

注意，这里不能从 sysdba 授权给普通用户，普通用户和普通用户之间是可以相互授权的。