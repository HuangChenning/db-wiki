---
title: "创建 Catalog"
book: "数据库对象管理"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077707.html"
tags:
  - oceanbase
  - standalone
  - ref-database-object-management
---

# 创建 Catalog

#### 注意

创建 HMS Catalog 前，如果 HMS 预期访问底层存储的文件数据在 HDFS 上，则需要完成 Java SDK 环境部署。有关配置 JAVA SDK 环境的详细信息，参见 [部署 OceanBase 数据库 JAVA SDK 环境](../deploy/800-deploy-the-ob-java-sdk-environment.md)。

#### 说明

复杂类型当前版本仅支持了 `Parquet` 格式的 `ARRAY` 类型。

#### 说明

适用于未开启 Kerberos 权限认证的集群，但相关 HDFS 路径需要特定用户才能访问的场景。

#### 说明

`CONFIGS` 中的 `dfs.data.transfer.protection` 必须与 HDFS 集群配置一致。

#### 说明

未启用 Kerberos，但 HDFS 为高可用（HA）模式，无需设置 `PRINCIPAL`、`KEYTAB` 和 `KRB5CONF` 参数。
