---
title: "为新创建的表设置透明加密"
book: "管理数据库"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006362362.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 为新创建的表设置透明加密

本节主要介绍如何创建加密表空间来对新创建的表实现透明加密。

OceanBase 数据库的数据加密单位为表空间（Tablespace）。OceanBase 数据库并非一个多数据文件的数据库系统，表空间是为了兼容而设计的概念，可以简单理解为表空间是一组表的集合。

本节以在加密表空间 `sectest_ts1` 上创建表 `t1` 为例，提供透明加密的操作指导。

## 使用限制

- 系统租户不能开启加密。
- 租户配置透明加密后，除非租户重建，否则无法再切换为其他加密模式。

## 前提条件

在配置透明加密之前，需要先生成租户主密钥。请参见 [生成租户主密钥（MySQL 模式）](200-configure-tenant-master-key-mysql.md)。

## 创建加密表空间

租户主密钥生成完成后，即可创建加密表空间。

1.  管理员用户登录到集群的 MySQL 租户。

2.  创建表空间并指定加密算法。

    可以指定加密算法 `aes-256`、`aes-128`、`aes-192`、`sm4-cbc`、`aes-128-gcm`、`aes-192-gcm`、`aes-256-gcm`、`sm4-gcm`，如果使用 `'y'`，则表示默认使用 aes-256。

    示例如下：

    ``` sql
    CREATE TABLESPACE sectest_ts1 encryption = 'y'; 
    ```

## 在加密的表空间中创建新表

1.  普通用户登录到数据库的 MySQL 租户。

2.  进入对应的数据库后，创建表并指定表空间。

    ``` sql
    CREATE TABLE t1 (id1 int, id2 int) TABLESPACE sectest_ts1;
    ```

    创建后，该表对应的任何事务都需要加密。

3.  确认表空间内的表是否标记为加密。

    执行以下语句，查看 `encryptionalg` 是否为之前设置的 `aes-256`。

    ``` sql
    SELECT table_name,encryptionalg,encrypted FROM oceanbase.V$OB_ENCRYPTED_TABLES;
    +------------+---------------+-----------+
    | table_name | encryptionalg | encrypted |
    +------------+---------------+-----------+
    | t1         | aes-256       | YES       |
    +------------+---------------+-----------+
    1 row in set
    ```

    `encryptionalg` 为 `aes-256`，且 `encrypted` 为 `YES` 则表示表加密配置成功。

    更多视图 `V$OB_ENCRYPTED_TABLES` 的字段及说明信息，参见 [V\$OB_ENCRYPTED_TABLES](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002015164)。

## 相关文档

- [为已有表设置透明加密](200-set-storage-encryption-for-existing-tables-of-mysql-mode.md)
- [解除加密](300-unencrypt-of-mysql-mode.md)
