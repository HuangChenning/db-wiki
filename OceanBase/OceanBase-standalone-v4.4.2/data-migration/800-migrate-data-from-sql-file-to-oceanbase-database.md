---
title: "从 SQL 文件导入数据到 OceanBase 数据库"
book: "数据迁移"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006076952.html"
tags:
  - oceanbase
  - standalone
  - data-migration
---

# 从 SQL 文件导入数据到 OceanBase 数据库

#### 注意

sys 租户账号和密码 为集群租户下用户的账号和密码 (账号请勿填入"@sys#集群")。

#### 说明

使用 OceanBase 物理节点的主机地址和端口导入数据时，无需指定 `-c` 选项。

#### 注意

- 导入表结构时，SQL 内容是 DDL，使用 `--ddl` 选项。要求 SQL 里不能有注释和 SET 开关语句等。
- SQL 文件的目录要在 `-f` 选项中的 `/data/TABLE` 下，例如：`/home/admin/test_sql/data/TABLE/test_tbl1-schema.sql`。
- SQL 文件的名称格式：`表名-schema.sql`。
- 导入数据时，需要指定 `--sys-user` 和 `--sys-password` 选项，obloader 获取表结构元数据信息。

#### 注意

- 导入表数据时，SQL 内容是 DML，使用 `--sql` 选项。SQL 文件中的内容仅包含 `INSERT` 语句，数据不换行。
- SQL 文件的目录要在 `-f` 选项中的 `data` 下，例如：`/home/admin/test_sql/data/test_tbl1.sql`。
- SQL 文件的名称格式：`表名.sql`。
- 数据库（Schema）下要存在 SQL 文件对应的表名。
