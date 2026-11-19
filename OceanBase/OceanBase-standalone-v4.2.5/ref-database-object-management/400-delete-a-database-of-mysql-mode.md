---
title: "删除数据库"
book: "数据库对象管理"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003150282.html"
tags:
  - oceanbase
  - standalone
  - ref-database-object-management
---

# 删除数据库

本节主要介绍 MySQL 模式中数据库的删除语句及操作方法。

## 前提条件

请确认当前用户拥有 `DROP` 权限。查看当前拥有的权限的操作请参见 [查看用户权限](../manage/400-view-user-permissions-of-mysql-mode.md)。如果您没有 `DROP` 权限，请联系管理员为您添加，为用户添加权限的相关操作请参见 [直接授予权限](../manage/200-authority-of-mysql-mode.md)。

## 操作步骤

1.  用户登录集群的 MySQL 租户。

2.  使用 `DROP DATABASE` 语句删除数据库。

    示例如下：

    ```
    obclient> DROP DATABASE my_db;    
    ```

## 后续操作

如果误删数据库，可以通过回收站功能进行恢复，前提是需要开启回收站功能，相关操作请参见 [恢复回收站对象](../manage/400-restore-the-recyclebin-objects.md)。

## 相关文档

更多 `DROP DATABASE` 语句相关的语法说明请参见 [DROP DATABASE](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001503261)。
