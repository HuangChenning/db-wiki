---
title: "向角色中添加权限"
book: "管理数据库"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006078388.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 向角色中添加权限

创建角色后，需要向角色中添加权限，以便用户通过角色来使用这些权限。

## 前提条件

向角色中添加权限时，当前用户必须拥有被授予的权限，并且拥有 `GRANT OPTION` 权限，才能授权成功。查看当前用户所拥有的权限的相关操作请参见 [查看用户权限](400-view-user-permissions-of-mysql-mode.md)。如果您没有相关权限，请联系管理员为您添加，为用户添加权限的相关操作请参见 [直接授予权限](200-authority-of-mysql-mode.md)。

## 操作示例

- 将 `ALTER SYSTEM` 权限授予角色 `role1`。

  ```
  obclient [oceanbase]> GRANT ALTER SYSTEM ON *.* TO role1;
  ```

- 将数据库 `dbtest` 下的所有对象的 `SELECT` 权限授予角色 `role1`。

  ```
  obclient [oceanbase]> GRANT SELECT ON dbtest.* TO role1;
  ```

  支持将一个或多个权限同时添加到多个角色中。

  ```
  obclient [oceanbase]> GRANT SELECT,UPDATE ON dbtest.* TO role1,role2;
  ```

- 将表 `test1.tbl1` 的 `SELECT` 对象权限授予角色 `role1`。

  ```
  obclient [oceanbase]> GRANT SELECT ON test1.tbl1 TO role1;
  ```

- 将表 `test1.tbl1` 的 `c1` 列的 `SELECT` 权限授予角色 `role1`。

  ```
  obclient [oceanbase]> GRANT SELECT(c1) ON test1.tbl1 TO role1;
  ```

## 相关文档

- 有关 `GRANT` 语句的详细说明，请参见 \[GRANT\](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005286446。

- 有关 MySQL 模式支持的所有权限，请参见 [MySQL 模式下的权限分类](https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006078044)。
