---
title: "查看用户信息"
book: "管理数据库"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000002702186.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 查看用户信息

用户创建成功后，可以通过视图 `ALL_USERS`、`DBA_USERS` 和 `USER_USERS` 查看相关信息。

## 操作步骤

1.  登录数据库的 Oracle 租户。

2.  执行以下命令，查看用户信息。

    - 查看当前用户的详细信息

      ```
      obclient [TEST2]> SELECT * FROM USER_USERS;
      ```

      查询结果如下：

      ```
      +----------+--------+----------------+-----------+-------------+--------------------+----------------------+-----------------------+-----------+-----------------------------+---------------+--------------------+--------+-------------------+-----------+-------------------+----------+-----------+----------------------+
      | USERNAME | USERID | ACCOUNT_STATUS | LOCK_DATE | EXPIRY_DATE | DEFAULT_TABLESPACE | TEMPORARY_TABLESPACE | LOCAL_TEMP_TABLESPACE | CREATED   | INITIAL_RSRC_CONSUMER_GROUP | EXTERNAL_NAME | PROXY_ONLY_CONNECT | COMMON | ORACLE_MAINTAINED | INHERITED | DEFAULT_COLLATION | IMPLICIT | ALL_SHARD | PASSWORD_CHANGE_DATE |
      +----------+--------+----------------+-----------+-------------+--------------------+----------------------+-----------------------+-----------+-----------------------------+---------------+--------------------+--------+-------------------+-----------+-------------------+----------+-----------+----------------------+
      | TEST2    | 500013 | OPEN           | NULL      | NULL        | NULL               | NULL                 | NULL                  | 27-MAR-25 | NULL                        | NULL          | N                  | NO     | N                 | NO        | USING_NLS_COMP    | NO       | NO        | 27-MAR-25            |
      +----------+--------+----------------+-----------+-------------+--------------------+----------------------+-----------------------+-----------+-----------------------------+---------------+--------------------+--------+-------------------+-----------+-------------------+----------+-----------+----------------------+
      1 row in set
      ```

      有关视图 `USER_USERS` 的详细说明，请参见 [USER_USERS](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001500840)。

    - 查看当前用户可见的所有用户

      ```
      obclient [TEST2]> SELECT * FROM ALL_USERS;
      ```

      查询结果如下：

      ```
      +------------+--------+-----------+--------+-------------------+-----------+-------------------+----------+-----------+
      | USERNAME   | USERID | CREATED   | COMMON | ORACLE_MAINTAINED | INHERITED | DEFAULT_COLLATION | IMPLICIT | ALL_SHARD |
      +------------+--------+-----------+--------+-------------------+-----------+-------------------+----------+-----------+
      | SYS        | 200003 | 26-MAR-25 | NO     | N                 | NO        | USING_NLS_COMP    | NO       | NO        |
      | LBACSYS    | 200004 | 26-MAR-25 | NO     | N                 | NO        | USING_NLS_COMP    | NO       | NO        |
      | ORAAUDITOR | 200005 | 26-MAR-25 | NO     | N                 | NO        | USING_NLS_COMP    | NO       | NO        |
      | USER1      | 500009 | 27-MAR-25 | NO     | N                 | NO        | USING_NLS_COMP    | NO       | NO        |
      | TEST2      | 500013 | 27-MAR-25 | NO     | N                 | NO        | USING_NLS_COMP    | NO       | NO        |
      +------------+--------+-----------+--------+-------------------+-----------+-------------------+----------+-----------+
      5 rows in set
      ```

      查询结果中：

      - `SYS`：系统内置的数据库管理员。
      - `LBACSYS`：系统内置的数据库安全管理员。
      - `ORAAUDITOR`：系统内置的数据库审计员。
      - `TEST1`、`TEST2` 为用户创建的自定义用户。

      有关视图 `ALL_USERS` 的详细说明，请参见 [ALL_USERS](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001501036)。

    - 管理员用户查看当前租户内所有用户的详细信息

      ```
      obclient [TEST2]> SELECT * FROM DBA_USERS;
      ```

      查询结果如下：

      ```
      +------------+--------+-------------------------------------------+----------------+-----------+-------------+--------------------+----------------------+-----------------------+-----------+---------+-----------------------------+---------------+-------------------+------------------+---------------------+--------------------+--------+------------+-------------------+-----------+-------------------+----------+-----------+----------------------+
      | USERNAME   | USERID | PASSWORD                                  | ACCOUNT_STATUS | LOCK_DATE | EXPIRY_DATE | DEFAULT_TABLESPACE | TEMPORARY_TABLESPACE | LOCAL_TEMP_TABLESPACE | CREATED   | PROFILE | INITIAL_RSRC_CONSUMER_GROUP | EXTERNAL_NAME | PASSWORD_VERSIONS | EDITIONS_ENABLED | AUTHENTICATION_TYPE | PROXY_ONLY_CONNECT | COMMON | LAST_LOGIN | ORACLE_MAINTAINED | INHERITED | DEFAULT_COLLATION | IMPLICIT | ALL_SHARD | PASSWORD_CHANGE_DATE |
      +------------+--------+-------------------------------------------+----------------+-----------+-------------+--------------------+----------------------+-----------------------+-----------+---------+-----------------------------+---------------+-------------------+------------------+---------------------+--------------------+--------+------------+-------------------+-----------+-------------------+----------+-----------+----------------------+
      | SYS        | 200003 | NULL                                      | OPEN           | NULL      | NULL        | NULL               | NULL                 | NULL                  | 26-MAR-25 | DEFAULT | NULL                        | NULL          | NULL              | N                | PASSWORD            | N                  | NO     | NULL       | N                 | NO        | USING_NLS_COMP    | NO       | NO        | 26-MAR-25            |
      | LBACSYS    | 200004 | ***************************************** | OPEN           | NULL      | NULL        | NULL               | NULL                 | NULL                  | 26-MAR-25 | DEFAULT | NULL                        | NULL          | NULL              | N                | PASSWORD            | N                  | NO     | NULL       | N                 | NO        | USING_NLS_COMP    | NO       | NO        | 27-MAR-25            |
      | ORAAUDITOR | 200005 | ***************************************** | LOCKED         | NULL      | NULL        | NULL               | NULL                 | NULL                  | 26-MAR-25 | DEFAULT | NULL                        | NULL          | NULL              | N                | PASSWORD            | N                  | NO     | NULL       | N                 | NO        | USING_NLS_COMP    | NO       | NO        | 26-MAR-25            |
      | USER1      | 500009 | ***************************************** | OPEN           | NULL      | NULL        | NULL               | NULL                 | NULL                  | 27-MAR-25 | DEFAULT | NULL                        | NULL          | NULL              | N                | PASSWORD            | N                  | NO     | NULL       | N                 | NO        | USING_NLS_COMP    | NO       | NO        | 27-MAR-25            |
      | TEST2      | 500013 | ***************************************** | OPEN           | NULL      | NULL        | NULL               | NULL                 | NULL                  | 27-MAR-25 | DEFAULT | NULL                        | NULL          | NULL              | N                | PASSWORD            | N                  | NO     | NULL       | N                 | NO        | USING_NLS_COMP    | NO       | NO        | 27-MAR-25            |
      +------------+--------+-------------------------------------------+----------------+-----------+-------------+--------------------+----------------------+-----------------------+-----------+---------+-----------------------------+---------------+-------------------+------------------+---------------------+--------------------+--------+------------+-------------------+-----------+-------------------+----------+-----------+----------------------+
      5 rows in set
      ```

      查询结果中：

      - `SYS`：系统内置的数据库管理员。

      - `LBACSYS`：系统内置的数据库安全管理员，默认为锁定状态，在使用前需要为该用户解除锁定。

      - `ORAAUDITOR`：系统内置的数据库审计员，默认为锁定状态，在使用前需要为该用户解除锁定。

      有关视图 `DBA_USERS` 的详细说明，请参见 [DBA_USERS](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001500960)。

## 相关文档

[用户和权限概述](100-user-and-permission-overview.md)
