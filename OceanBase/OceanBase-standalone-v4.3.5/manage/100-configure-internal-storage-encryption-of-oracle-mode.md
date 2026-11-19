---
title: "为新创建的表设置透明加密"
book: "管理数据库"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006362364.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 为新创建的表设置透明加密

本节主要介绍如何创建加密表空间来对新创建的表实现数据透明加密。

OceanBase 数据库的加密在形式上尽量兼容 Oracle 数据库，数据的加密单位为表空间（Tablespace）。OceanBase 数据库并非一个多数据文件的数据库系统，表空间是为了兼容而设计的概念，可以简单理解为表空间是一组表的集合。

本节以在加密表空间 `sectest_ts1` 上创建表 `t1` 为例，提供透明加密的操作指导。

## 前提条件

在配置透明加密之前，需要先生成租户主密钥。请参见 [生成租户主密钥（Oracle 模式）](300-configure-tenant-master-key-oracle.md)。

## 创建加密表空间

租户主密钥生成完成后，即可创建加密表空间。

1.  管理员用户登录到集群的 Oracle 租户。

2.  创建表空间并指定加密算法。

    可以指定加密算法 `aes-256`、`aes-128`、`aes-192`、`sm4-cbc`、`aes-128-gcm`、`aes-192-gcm`、`aes-256-gcm`、`sm4-gcm`。

    示例如下：

    ``` sql
    CREATE TABLESPACE sectest_ts1 ENCRYPTION USING 'aes-256';
    ```

## 在加密的表空间中创建新表

1.  普通用户登录到 Oracle 租户。

2.  创建表并指定表空间。

    ``` sql
    CREATE TABLE t1 (id1 int, id2 int) TABLESPACE sectest_ts1;
    ```

    创建后，该表对应的任何事务都需要加密。

3.  确认表空间内的表是否标记为加密。

    执行以下语句，查看 `encryptionalg` 是否为之前设置的 `aes-256`。

    ``` sql
    SELECT table_name,encryptionalg,encrypted FROM V$OB_ENCRYPTED_TABLES;
    +------------+---------------+-----------+
    | TABLE_NAME | ENCRYPTIONALG | ENCRYPTED |
    +------------+---------------+-----------+
    | T1         | aes-256       | YES       |
    +------------+---------------+-----------+
    1 row in set
    ```

    `encryptionalg` 为 `aes-256`，且 `encrypted` 为 `YES` 则表示表加密配置成功。

    更多视图 `V$OB_ENCRYPTED_TABLES` 的字段及说明信息，参见 [V\$OB_ENCRYPTED_TABLES](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002014084)。

## 相关文档

- [为已有表设置透明加密](200-set-storage-encryption-for-existing-tables-of-oracle-mode.md)
- [解除加密](300-unencrypt-of-oracle-mode.md)
