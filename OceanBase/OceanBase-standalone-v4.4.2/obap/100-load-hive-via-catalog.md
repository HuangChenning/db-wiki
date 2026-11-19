---
title: "通过 Catalog 加载 Hive 表"
book: OceanBase AP
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077315.html"
tags:
  - oceanbase
  - standalone
  - obap
---

# 通过 Catalog 加载 Hive 表

#### 注意

HMS Catalog 的 `CREATE EXTERNAL CATALOG ... TYPE = 'HMS'` 语法见本文；完整 SQL 参考以 [CREATE EXTERNAL CATALOG](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005286499) 当前版本是否已收录为准。需 **V4.4.1 及以上**、**MySQL 模式**。

#### 说明

若 HMS 版本为 3.1.3 及以上，且表注册在非默认 Catalog 中，需通过 `HMS_CATALOG_NAME` 指定目标 Catalog 名称。访问默认 Catalog 时，可设置为 `hive`，也可省略该参数（默认为空，由 HMS 侧默认行为决定）。

#### 注意

该配置位于 Hadoop 服务端（`$HADOOP_HOME/etc/hadoop/hdfs-site.xml`），OceanBase 不直接读取此文件，而是通过自身的 Catalog 和 Location 配置来适配该模式。

#### 说明

- `CONFIGS` 中的 `dfs.data.transfer.protection` 参数用于指定 HDFS 数据传输通道的安全级别（如 `authentication`、`integrity`、`privacy` 或 `null`）。

&nbsp;

- 该值必须与 Hadoop 集群 `hdfs-site.xml` 中配置的 `dfs.data.transfer.protection` 完全一致，否则在读取数据时可能因安全策略不匹配而失败。

&nbsp;

- 建议从 Hadoop 管理员处确认该配置项的实际值，或直接查看 HDFS 集群的 `hdfs-site.xml` 文件。

#### 说明

- 所有 OBServer 节点需部署相同的 keytab 和 krb5.conf。

&nbsp;

- 若遇 “Unknown Host” 错误，请在 /etc/hosts 添加 HDFS 节点映射。
