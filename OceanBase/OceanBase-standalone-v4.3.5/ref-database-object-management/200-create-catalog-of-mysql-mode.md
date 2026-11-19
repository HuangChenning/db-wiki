---
title: "创建 Catalog"
book: "数据库对象管理"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006123846.html"
tags:
  - oceanbase
  - standalone
  - ref-database-object-management
---

# 创建 Catalog

本文将向您介绍如何使用 SQL 语句创建 External Catalog。

## 权限要求

创建 External Catalog，需要当前用户拥有 `CREATE CATALOG` 权限。有关 OceanBase 数据库权限的详细介绍，参见 [MySQL 模式下的权限分类](../manage/100-permission-classification-of-mysql.md)。

## 语法

创建 External Catalog 的 SQL 语句格式如下：

``` sql
CREATE EXTERNAL CATALOG [IF NOT EXISTS] external_catalog_name
    PROPERTIES [=] (properties_type_options);

properties_type_options:
    odps_type_list

odps_type_list:
    TYPE = 'ODPS',
    [ACCESSTYPE = 'accesstype_string',]
    ACCESSID = 'string',
    ACCESSKEY = 'string',
    STSTOKEN = 'string',
    ENDPOINT = 'string',
    TUNNEL_ENDPOINT = 'string',
    PROJECT_NAME = 'string',
    [QUOTA_NAME = 'string',]
    [COMPRESSION = 'compression_string',]
    REGION = 'string'

accesstype_string:
    aliyun
    | sts
    | app

compression_string:
    zlib
    | zstd
    | lz4
    | odps_lz4
```

**参数说明：**

- `IF NOT EXISTS`：可选项，如果指定该子句，即使要创建的外部数据目录在当前租户中已存在，也不会报错，系统会提示一条 Warning 信息；如果不指定，则会报错。
- `external_catalog_name`：表示要创建的外部数据目录的名称。
- `PROPERTIES [=] (properties_type_options)`：用于指定外部数据目录类型的相关属性选项。
- `odps_type_list`：表示 ODPS 类型外部数据目录（ODPS Catalog）的相关属性列表。

有关创建 External Catalog 语法的详细参数说明信息，参见 [CREATE EXTERNAL CATALOG](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002977502)。

## 创建 ODPS 类型的 External Catalog

外表读写 MaxCompute 数据时，取值为 `ODPS`。

通过 `CREATE EXTERNAL CATALOG` 创建与 MaxCompute（ODPS）的连接，实现直接查询 ODPS 表数据，无需手动创建映射表。Catalog 下对象为只读；向 MaxCompute 写入数据请使用 [ODPS 外部表](../obap/200-odps-external-table.md)。

**示例如下：**

```
obclient> CREATE EXTERNAL CATALOG test_odps_catalog
    PROPERTIES = (
        TYPE = 'ODPS',
        ACCESSID = '$odps_accessid',
        ACCESSKEY = '$odps_accesskey',
        ENDPOINT = '$odps_endpoint',
        TUNNEL_ENDPOINT = 'http://xxx.maxcompute.aliyun.com',
        PROJECT_NAME = 'mysqltest_regression_sqlqa',
        QUOTA_NAME = '',
        COMPRESSION_CODE = ''
    );
```

## 相关文档

- [Catalog 概述](100-catalog-overview-of-mysql-mode.md)
- [查看 Catalog](300-view-catalog-of-mysql-mode.md)
- [删除 Catalog](400-delete-catalog-of-mysql-mode.md)
- [CREATE EXTERNAL CATALOG](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002977502)
