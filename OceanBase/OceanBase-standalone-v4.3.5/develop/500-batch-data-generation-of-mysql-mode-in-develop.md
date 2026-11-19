---
title: "批量生成测试数据"
book: "应用开发"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003577748.html"
tags:
  - oceanbase
  - standalone
  - develop
---

# 批量生成测试数据

#### 说明

- 该脚本将生成一个名为 `insert_test_sql_file_tbl1.sql` 的 SQL 文件，并在其中插入了 100,000 条用户记录。您可以根据需要修改 SQL 语句和循环生成的用户记录数量。
- 在进行大量数据插入时，请提前关注相关服务器的资源使用情况，避免由于资源使用情况而导致数据插入失败或性能下降的情况。

#### 说明

更多有关执行 SQL 脚本的信息，请参见 [从 SQL 文件导入数据到 OceanBase 数据库](../data-migration/800-migrate-data-from-sql-file-to-oceanbase-database.md)。

#### 注意

连接租户的用户需要拥有该数据库的 `CREATE`、`INSERT` 和 `SELECT` 权限。更多有关用户权限的信息，请参见 [MySQL 模式下的权限分类](../manage/100-permission-classification-of-mysql.md)。

#### 说明

在执行 SQL 脚本文件时，请使用绝对路径指定 SQL 脚本文件的路径。

#### 说明

您可以增加或减少输入参数的大小，来控制测试数据的数量。在调整参数大小时，需要考虑到数据库性能和存储空间的限制，避免生成过多的数据导致数据库崩溃或者存储空间不足。
