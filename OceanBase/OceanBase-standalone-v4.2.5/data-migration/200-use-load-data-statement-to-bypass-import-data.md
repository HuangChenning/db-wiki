---
title: "使用 LOAD DATA 语句旁路导入数据"
book: "数据迁移"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000002701742.html"
tags:
  - oceanbase
  - standalone
  - data-migration
---

# 使用 LOAD DATA 语句旁路导入数据

#### 注意

如果使用了此参数，`file_name` 必须是一个 OSS 的地址。

#### 说明

这里所指的 OSS 泛指对象存储 OSS（`oss://`）、COS（`cos://`）、S3（`s3://`） 等，下文同理。

#### 说明

对于 OceanBase 数据库 V4.2.5 版本，旁路导入从 V4.2.5 BP1 版本开始支持将 OceanBase 数据库 V1.4x/V3.x 版本的备份数据（V1.4x 是逻辑备份，V3.x 是物理备份）直接导入到 OceanBase 数据库 V4.x 版本中。

#### 说明

对于 OceanBase 数据库 V4.2.5 版本，旁路导入从 V4.2.5 BP4 版本开始支持将 OceanBase 数据库 V2.x 版本的备份数据（逻辑或物理备份）直接导入到 OceanBase 数据库 V4.x 版本中。

#### 说明

下面的示例是从服务器端文件导入数据的方法。OceanBase 数据库 `LOAD DATA` 语句旁路导入数据还支持加载本地文件（`LOCAL INFILE`）的方式。更多有关 `LOAD DATA LOCAL INFILE` 的示例信息，请参见 [使用 `LOAD DATA` 语句导入数据](200-use-the-load-command-to-load-the-csv-data-file-to-the-oceanbase-database.md)

#### 说明

OceanBase 数据库中的 `LOAD DATA` 语句仅支持加载 OBServer 节点本地的输入文件。因此，需要在导入之前将文件拷贝到某台 OBServer 上。

#### 注意

由于安全原因，设置系统变量 `secure_file_priv` 时，只能通过本地 Socket 连接数据库执行修改该全局变量的 SQL 语句。更多信息，请参见 [secure_file_priv](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001502601)。
