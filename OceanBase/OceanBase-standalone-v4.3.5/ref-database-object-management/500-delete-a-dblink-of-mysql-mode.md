---
title: "删除 DBLink"
book: "数据库对象管理"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003577953.html"
tags:
  - oceanbase
  - standalone
  - ref-database-object-management
---

# 删除 DBLink

您可以删除不需要使用的 DBLink。

## 操作步骤

删除 DBLink 的语法如下：

``` sql
DROP DATABASE LINK [IF EXISTS] dblink_name;
```

语句使用说明：

- 执行该语句的用户需要具备 `DROP DATABASE LINK` 权限。为用户授权的相关操作请参见 [直接授予权限](../manage/200-authority-of-mysql-mode.md)。

- `IF EXISTS`：如果指定 `IF EXISTS`，即使待删除的 DBLink 不存在，也不会报错；如果不指定且待删除的 DBLink 不存在，则系统会报错。

- `dblink_name` 表示待删除的 DBLink 的名称。

示例如下：

``` sql
DROP DATABASE LINK IF EXISTS ob_dblink;
```

## 相关文档

更多 DBLink 相关的操作，请参见以下信息：

- [创建 DBLink](100-create-a-dblink-of-mysql-mode.md)

- [查看已创建的 DBLink](200-view-a-dblink-of-mysql-mode.md)

- [通过 DBLink 访问远端数据库](300-access-a-remote-database-by-ablink-of-mysql-mode.md)
