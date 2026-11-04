---
title: "GRANT 授权"
book: "数据控制DCL"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/guide/guide_seven_text2.html"
tags:
  - highgo
  - highgo-v9
  - guide-dcl
---

## GRANT 授权

使用highgo用户登录数据库输入 \\h alter user 可以查看有哪些权限

登录highgo用户  
alter user postgres WITH superuser; 授予超级管理员权限

```sql
highgo=# alter user postgres WITH superuser; 
ALTER ROLE
highgo=# \du 
                             角色列表
 角色名称 |                    属性                    | 成员属于 
----------+--------------------------------------------+----------
 highgo   | 超级用户, 建立角色, 建立 DB, 复制, 绕过RLS | {}
 postgres | 超级用户                                   | {}

highgo=#
```

– 授予用户postgres登录权限

```sql
ALTER USER postgres WITH LOGIN;   --可以省略创建新建用户都有数据库登录权限
```

– 授予postgres用户连接到 highgo 数据库的权限

```sql
GRANT CONNECT ON DATABASE highgo TO postgres ;
```

– 授予postgres用户对公共模式的使用权限（默认模式） \\c gwy\_nonce

```sql
GRANT USAGE ON SCHEMA public TO postgres ;
```

– 授予对txdatacenter用户public模式下所有表的查询权限

```sql
GRANT SELECT ON ALL TABLES IN SCHEMA public TO txdatacenter;
```

– 对未来创建得表也有只读权限

```sql
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO txdatacenter;
```

如果是其他模式还得加入一句

```sql
grant all on SCHEMA yncbdb to yncbdb;
```

对未来得表也有查询权限

```sql
ALTER DEFAULT PRIVILEGES IN SCHEMA yncbdb GRANT SELECT ON TABLES TO yncbdb;
```

– 修改用户默认模式

在修改之前执行这个

先在执行这个

```sql
ALTER USER nccyncbdb SET search_path TO yncbdb,public;
ALTER USER nccyncbdb RESET search_path;
```

在执行这个刷新一下

```sql
ALTER USER nccyncbdb SET search_path TO public;
```

在次执行这个

```sql
ALTER USER nccyncbdb SET search_path TO yncbdb,public;
ALTER USER nccyncbdb RESET search_path;
```

授予插入权限

```sql
GRANT INSERT ON ALL TABLES IN SCHEMA yncbdb TO yncbdb;
```