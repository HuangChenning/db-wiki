---
title: "开启安全审计"
book: "管理数据库"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077551.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 开启安全审计

#### 说明

审计日志加密功能从 V4.4.2 BP1 版本开始支持。

#### 说明

`AUDIT_LOG_FILTER_SET_FILTER` 是 `CREATE OR REPLACE` 语义，对已存在的对象执行 DDL 会覆盖。

#### 说明

查看 `general_sql_command` 支持的完整 SQL 类型，请参考文末相关文档。

#### 说明

`AUDIT_LOG_FILTER_SET_USER` 指定的 `user@host` 不要求是已存在的用户，可以写通配符或不存在的用户。当指定不存在的用户时，可以在登录审计的时候起作用。`user_name` 有以下限制：

- `user` 只支持对整个字段进行通配，即 `%`。
- 不支持指定 `host` 字段或 `test_%` 这种部分通配符的写法。若指定 `host` 或 `test_%`，则无法创建过滤器。

#### 说明

`AUDIT_LOG_FILTER_SET_USER` 是 `CREATE OR REPLACE` 语义，对已存在的对象执行 DDL 会覆盖。指定的 `filter_name` 不存在时，DDL 不生效但也不报错。
