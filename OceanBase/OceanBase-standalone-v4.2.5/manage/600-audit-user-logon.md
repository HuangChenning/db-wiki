---
title: "审计用户登录"
book: "管理数据库"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000002702019.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 审计用户登录

审计功能可以对用户的登录操作进行审计。

## 审计指定用户的登录

以 `ORAAUDITOR` 用户登录，设置审计用户 `aud` 登录。

```
obclient> AUDIT SESSION BY user1;
```

## 审计所有用户的登录

以 `ORAAUDITOR` 用户登录，设置审计所有用户登录。

```
obclient> AUDIT SESSION;
```

## 查看审计记录

查看 `DBA_AUDIT_TRAIL` 中的审计记录。

```
obclient> SELECT USERNAME,USERHOST,TIMESTAMP,SQL_TEXT FROM SYS.DBA_AUDIT_TRAIL;
+----------+----------------+-----------+----------+
| USERNAME | USERHOST       | TIMESTAMP | SQL_TEXT |
+----------+----------------+-----------+----------+
| USER1    | xx.xx.xx.xx    | 27-MAR-25 | CONNECT  |
+----------+----------------+-----------+----------+
1 row in set
```

## 相关文档

有关安全审计的更多相关操作，参见：

- [开启审计](200-audit-open.md)
- [设置和查看审计规则](300-set-up-and-view-audit-rules.md)
- [查看审计记录](500-audit-records.md)
- [审计用户操作](700-audit-user-operations.md)
- [审计指定数据库对象](800-audit-a-specified-database-object.md)
