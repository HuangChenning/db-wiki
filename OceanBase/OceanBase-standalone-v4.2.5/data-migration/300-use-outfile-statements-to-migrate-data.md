---
title: "使用 OUTFILE 语句导出数据"
book: "数据迁移"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000002701738.html"
tags:
  - oceanbase
  - standalone
  - data-migration
---

# 使用 OUTFILE 语句导出数据

#### 注意

客户端需要直连 OceanBase 数据库实例以做导入导出操作。

#### 说明

由于阿里云 OSS 有文件大小的限制，对于超过 5 GB 的文件，导出到 OSS 时会被拆分成多个文件，每个文件小于 5 GB。

#### 说明

`SELECT` 子句后面的所有列中，没有使用聚合函数的列，必须出现在 `GROUP BY` 子句后面。

#### 注意

由于安全原因，设置系统变量 `secure_file_priv` 时，只能通过本地 Socket 连接数据库执行修改该全局变量的 SQL 语句。更多信息，请参见 [secure_file_priv](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001502601)。
