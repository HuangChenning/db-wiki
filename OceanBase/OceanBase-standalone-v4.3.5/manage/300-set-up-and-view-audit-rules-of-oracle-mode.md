---
title: "设置和查看审计规则"
book: "管理数据库"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003577821.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 设置和查看审计规则

开启安全审计后，需要设置具体的安全审计规则来对用户的操作进行审计。

## 设置审计规则

使用 `ORAAUDITOR` 用户登录到 Oracle 租户。通过内置的审计管理用户 `ORAAUDITOR` 可以配置审计规则，包括：

- 语句审计：对特定的操作进行审计，不指定具体对象，可以指定对具体用户或对所有用户生效。
- 对象审计：对特定的对象上执行的特定操作进行审计，可以指定对具体用户或对所有用户生效。

审计规则是通过 DDL 语句 `audit/noaudit` 语句来配置，审计规则也是一种 schema 对象。

有关设置审计规则的详细信息，请参见 [AUDIT](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002017405)。

例如，对用户 `user1` 的表 `tbl1` 的所有 INSERT、UPDATE 和 DELETE 操作进行审计：

```
obclient> AUDIT INSERT,UPDATE,DELETE ON user1.tbl1;
```

## 查看审计规则

设置审计规则后，您可以通过一系列 Oracle 兼容的数据字典视图查看审计规则的信息。

[TABLE]

查看 `ALL_DEF_AUDIT_OPTS` 中的审计规则。示例如下：

```
obclient> SELECT * FROM SYS.ALL_DEF_AUDIT_OPTS;
```

## 相关文档

有关安全审计的更多相关操作，参见：

- [开启安全审计](200-audit-open-of-oracle-mode.md)
- [查看审计记录](500-audit-records-of-oracle-mode.md)
