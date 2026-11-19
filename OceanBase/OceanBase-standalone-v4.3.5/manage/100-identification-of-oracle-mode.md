---
title: "身份鉴别"
book: "管理数据库"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003577813.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 身份鉴别

身份标识与鉴别功能用于对登录数据库访问数据的用户进行身份验证，确认该用户是否能够与某一个数据库用户进行关联，并根据关联的数据库用户的权限，对该用户在数据库中的数据访问活动进行安全控制。本文主要介绍 Oracle 模式的身份鉴别功能。

Oracle 模式下，OceanBase 用户鉴权是指为 OceanBase 用户名和密码鉴定，以便识别用户的身份以及用户的所能访问的功能、资源等。在 OceanBase 数据库中，所有的用户都需要使用正确的用户名和密码来登录，以此来保护数据库的安全。

## 示例

Oracle 模式中，用户名称在租户内是唯一的，不同租户的用户可以同名，所以通过 `用户名@租户名` 的形式在系统全局唯一确定一个用户。

1.  使用 `SYS` 用户登录集群的 Oracle 租户。

    ```
    obclient -usys@oracle -h10.xxx.xxx.1 - P2881 -P*******
    ```

2.  执行以下命令，创建用户 `u1`。

    ```
    obclient> CREATE USER u1 IDENTIFIED BY ******;
    Query OK, 0 rows affected (0.064 sec)
    ```

3.  执行以下命令，授予用户 `u1` 连接数据库的权限。

    ```
    obclient>GRANT CREATE SESSION TO u1;
    Query OK, 0 rows affected (0.045 sec)
    ```

4.  使用 `u1` 用户登录集群。

    ```
    $obclient -h10.xxx.xxx.1 -P2881 -uu1@oracle001 -p****** -A
    Welcome to the OceanBase.  Commands end with ; or \g.
    Your OceanBase connection id is 3221544104
    Server version: OceanBase 4.3.5.3 (r203000012025070417-cfc8beb57ee771f20efa9bb39aaf4c26adbcd7a2) (Built Jul  4 2025 17:55:25)

    Copyright (c) 2000, 2018, OceanBase and/or its affiliates. All rights reserved.

    Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

    obclient(uu1@oracle001)[SYS]>
    ```
