---
title: SET PASSWORD
book: "SQL 参考"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002017044.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# SET PASSWORD

## 描述

该语句用于修改 OceanBase 数据库当前登录用户或其他用户的密码。

## 语法

```sql
SET PASSWORD [FOR user] = password_option;

password_option: {
PASSWORD('authstring')
|'hashstring'
}
```

## 参数解释

|  **参数**  |                                                                       **描述**                                                                        |
|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| FOR user | 如果没有 `FOR user` 子句，表示修改当前用户的密码。任何成功登录的用户都可以修改当前用户的密码。 如果有 `FOR user` 子句，表示修改指定用户的密码。必须拥有全局（MySQL 库）的 `CREATE USER` 权限，才可以修改指定用户的密码。 |
|password|默认 `password` 为明文传输, 会在内核做一次编码。|

## 示例

* 修改当前用户的密码。

  ```sql
  obclient> SET PASSWORD = PASSWORD('**1***');
  Query OK, 0 rows affected
  ```

* 修改 `sqluser01` 用户的密码。

  ```sql
  obclient> SET PASSWORD FOR sqluser01 = PASSWORD('**2***');
  Query OK, 0 rows affected
  ```
