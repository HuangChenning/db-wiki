---
title: "REVOKE 取消授权"
book: "数据控制DCL"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/guide/guide_seven_text3.html"
tags:
  - highgo
  - highgo-v9
  - guide-dcl
---

## REVOKE 取消授权

### 基本语法

```
REVOKE [GRANT OPTION FOR] privilege_type(s)
ON object_type object_name
FROM { user | role | PUBLIC } [, ...]
[CASCADE | RESTRICT];
```
- \*\* `privilege_type` \*\*：要撤销的权限类型（如 `SELECT` 、 `INSERT` 、 `UPDATE` 、 `DELETE` 、 `ALL PRIVILEGES` 等）。
- \*\* `object_type` \*\*：对象类型（如 `TABLE` 、 `VIEW` 、 `SEQUENCE` 、 `FUNCTION` 、 `DATABASE` 等）。
- \*\* `CASCADE` \*\*：自动撤销被 revoke 对象授予其他用户的权限（慎用）。

### 常见应用场景

\\h REVOKE USAGE 查看

```sql
命令：       REVOKE
描述：       移除存取权限
语法：
REVOKE [ GRANT OPTION FOR ]
    { { SELECT | INSERT | UPDATE | DELETE | TRUNCATE | REFERENCES | TRIGGER }
    [, ...] | ALL [ PRIVILEGES ] }
    ON { [ TABLE ] 表名 [, ...]
         | ALL TABLES IN SCHEMA 模式名称 [, ...] }
    FROM role_specification [, ...]
    [ GRANTED BY role_specification ]
    [ CASCADE | RESTRICT ]

REVOKE [ GRANT OPTION FOR ]
    { { SELECT | INSERT | UPDATE | REFERENCES } ( 列名称 [, ...] )
    [, ...] | ALL [ PRIVILEGES ] ( 列名称 [, ...] ) }
    ON [ TABLE ] 表名 [, ...]
    FROM role_specification [, ...]
    [ GRANTED BY role_specification ]
    [ CASCADE | RESTRICT ]

REVOKE [ GRANT OPTION FOR ]
    { { USAGE | SELECT | UPDATE }
    [, ...] | ALL [ PRIVILEGES ] }
    ON { SEQUENCE 序列名称 [, ...]
         | ALL SEQUENCES IN SCHEMA 模式名称 [, ...] }
    FROM role_specification [, ...]
    [ GRANTED BY role_specification ]
    [ CASCADE | RESTRICT ]

REVOKE [ GRANT OPTION FOR ]
    { { CREATE | CONNECT | TEMPORARY | TEMP } [, ...] | ALL [ PRIVILEGES ] }
    ON DATABASE 数据库名称 [, ...]
    FROM role_specification [, ...]
    [ GRANTED BY role_specification ]
    [ CASCADE | RESTRICT ]

REVOKE [ GRANT OPTION FOR ]
    { USAGE | ALL [ PRIVILEGES ] }
    ON DOMAIN 域_名称 [, ...]
    FROM role_specification [, ...]
    [ GRANTED BY role_specification ]
    [ CASCADE | RESTRICT ]

REVOKE [ GRANT OPTION FOR ]
    { USAGE | ALL [ PRIVILEGES ] }
    ON FOREIGN DATA WRAPPER 外部数据封装器的名称 [, ...]
```

#### 取消数据库权限

```sql
-- 取消用户iho登录权限
alter user iho with nologin;
```

#### 取消用户连接模式所有表权限

```sql
-- 取消用户hgtest对模式public的所有表访问权限
REVOKE SELECT ON ALL TABLES IN SCHEMA public from hgtest;
```

#### 取消用户超级权限得用alter

```sql
ALTER ROLE username NOSUPERUSER;
```