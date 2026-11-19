---
title: "使用 OceanBase 导数工具从 OceanBase 集群 MySQL 租户迁移数据到 Oracle 租户"
book: "数据迁移"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003577501.html"
tags:
  - oceanbase
  - standalone
  - data-migration
---

# 使用 OceanBase 导数工具从 OceanBase 集群 MySQL 租户迁移数据到 Oracle 租户

#### 说明

- 使用 OceanBase 物理节点的主机地址和端口导出数据时，无需指定 `-c` 选项。
- 有关 obdumper 命令行选项的详细信息，请参见 [命令行选项](https://www.oceanbase.com/docs/enterprise-oceanbase-dumper-loader-cn-10000000001142216)。

#### 说明

- 使用 OceanBase 物理节点的主机地址和端口导入数据时，无需指定 `-c` 选项。
- 有关 obloader 命令行选项的详细信息，请参见 [命令行选项](https://www.oceanbase.com/docs/enterprise-oceanbase-dumper-loader-cn-10000000001142222)。

#### 说明

`--sys-user` 选项用于连接 `sys` 租户下拥有特定权限的用户。导出时如果未指定 `--sys-user` 选项，默认指定的是 `--sys-user root`。

#### 注意

从 MySQL 租户里导出的 DDL 文件不符合 Oracle 租户的语法要求，所以从 MySQL 租户里导出的 DDL 文件先修改成符合 Oracle 租户的语法要求的 DDL 文件后，再导入 Oracle 租户中。

例如，从租户 `mysql001` 里导出的 DDL 文件，修改规则如下：

- 去掉 `if not exists` 关键字和单引号。
- 把数据类型修改为 Oracle 模式通用的数据类型：
  - 将 `int(11)` 改为 `number(11)`。
  - 将 `varchar(50)` 改为 `varchar2(50)`。
- 去掉默认字符序和字符集参数 `default charset=utf8mb4`、`default collate=utf8mb4_general_ci`。

有关 Oracle 模式数据类型的详细信息，请参见 [内建数据类型概述](https://www.oceanbase.com/docs/enterprise-oceanbase-database-cn-10000000000886657)。

#### 注意

- 需要将租户 `mysql001` 里的 Schema `test_data` 导出的目录 `/home/admin/test_migrate_data/csv_data/data/` 下的 `test_data` 名称修改为 `OBLOADER_USER01`。
- 将导出的 CSV 文件名中的表名中的英文字母改为大写。

示例语句如下：

`bash [root@xxx /home/admin/test_migrate_data/csv_data/data]# mv test_data OBLOADER_USER01 [root@xxx /home/admin/test_migrate_data/csv_data/data]# cd OBLOADER_USER01/TABLE [root@xxx /home/admin/test_migrate_data/csv_data/data/OBLOADER_USER01/TABLE]# ls test_tbl1.1.0.csv test_tbl2.1.0.csv [root@xxx /home/admin/test_migrate_data/csv_data/data/OBLOADER_USER01/TABLE]# mv test_tbl1.1.0.csv TEST_TBL1.1.0.csv [root@xxx /home/admin/test_migrate_data/csv_data/data/OBLOADER_USER01/TABLE]# mv test_tbl2.1.0.csv TEST_TBL2.1.0.csv <code></code>`
