---
title: "使用 OUTFILE 语句导出数据"
book: "数据迁移"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077162.html"
tags:
  - oceanbase
  - standalone
  - data-migration
---

# 使用 OUTFILE 语句导出数据

#### 注意

客户端需要直连 OceanBase 数据库实例以做导入导出操作。

#### 说明

对于 OceanBase 数据库 V4.3.2 版本，从 V4.3.2 BP1 版本开始支持控制导出数据的分区方式。

#### 注意

- 当数据按分区导出数据时，要求 `SINGLE = FALSE`，即允许导出多文件。
- 当前按分区导出数据仅支持导入到 OSS 上。

#### 说明

`SELECT` 子句后面的所有列中，没有使用聚合函数的列，必须出现在 `GROUP BY` 子句后面。

#### 说明

- 对于 OceanBase 数据库 V4.3.5 版本，`SELECT INTO` 从 V4.3.5 BP2 版本开始适配 S3 和基于 S3 协议的对象存储作为数据导出的目的端。
- 由于阿里云 OSS 有文件大小的限制，对于超过 5 GB 的文件，导出到 OSS 时会被拆分成多个文件，每个文件小于 5 GB。

#### 注意

当并行度大于 1 且 `SINGLE = FALSE` 时，可以导出到多个文件，达到并行读并行写和提高导出速度的效果。

#### 说明

- `BUFFER_SIZE` 用于导出性能调优，当机器内存充足且希望提高导出效率时，可设置一个较大的值（例如 4 MB），当机器内存不足时，可设置一个较小的值（例如 4 KB。设置为 0 时，表示单个线程中所有分区都使用一块公共内存）。
- 对于 OceanBase 数据库 V4.3.2 版本，从 V4.3.2 BP1 版本开始支持 `BUFFER_SIZE` 参数。

#### 注意

由于安全原因，设置系统变量 `secure_file_priv` 时，只能通过本地 Unix Socket 连接数据库执行修改该全局变量的 SQL 语句。更多信息，请参见 [secure_file_priv](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002015981)。

#### 注意

由于安全原因，设置系统变量 `secure_file_priv` 时，只能通过本地 Unix Socket 连接数据库执行修改该全局变量的 SQL 语句。更多信息，请参见 [secure_file_priv](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002015981)。

#### 注意

由于安全原因，设置系统变量 `secure_file_priv` 时，只能通过本地 Unix Socket 连接数据库执行修改该全局变量的 SQL 语句。更多信息，请参见 [secure_file_priv](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002015981)。

#### 注意

由于安全原因，设置系统变量 `secure_file_priv` 时，只能通过本地 Unix Socket 连接数据库执行修改该全局变量的 SQL 语句。更多信息，请参见 [secure_file_priv](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002015981)。

#### 注意

由于安全原因，设置系统变量 `secure_file_priv` 时，只能通过本地 Unix Socket 连接数据库执行修改该全局变量的 SQL 语句。更多信息，请参见 [secure_file_priv](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002015981)。

#### 注意

由于安全原因，设置系统变量 `secure_file_priv` 时，只能通过本地 Unix Socket 连接数据库执行修改该全局变量的 SQL 语句。更多信息，请参见 [secure_file_priv](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002015981)。
