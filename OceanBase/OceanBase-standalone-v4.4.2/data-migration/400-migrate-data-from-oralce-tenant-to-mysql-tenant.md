---
title: "使用 OceanBase 导数工具从 OceanBase 集群 Oracle 租户迁移数据到 MySQL 租户"
book: "数据迁移"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077154.html"
tags:
  - oceanbase
  - standalone
  - data-migration
---

# 使用 OceanBase 导数工具从 OceanBase 集群 Oracle 租户迁移数据到 MySQL 租户

#### 说明

- 使用 OceanBase 物理节点的主机地址和端口导出数据时，无需指定 `-c` 选项。
- 有关 obdumper 命令行选项的详细信息，请参见 [命令行选项](https://www.oceanbase.com/docs/enterprise-oceanbase-dumper-loader-cn-10000000001142216)。

#### 说明

- 使用 OceanBase 物理节点的主机地址和端口导入数据时，无需指定 `-c` 选项。
- 有关 obloader 命令行选项的详细信息，请参见 [命令行选项](https://www.oceanbase.com/docs/enterprise-oceanbase-dumper-loader-cn-10000000001142222)。

#### 说明

`--sys-user` 选项用于连接 `sys` 租户下拥有特定权限的用户。导出时如果未指定 `--sys-user` 选项，默认指定的是 `--sys-user root`。

#### 注意

从 Oracle 租户里导出的 DDL 文件不符合 MySQL 租户的语法要求，所以从 Oracle 租户里导出的 DDL 文件先修改成符合 MySQL 租户的语法要求的 DDL 文件后，再导入 MySQL 租户中。

例如，从租户 `oracle001` 里导出的 DDL 文件，修改规则如下：

- 把数据类型修改为 MySQL 模式通用的数据类型：
  - 将 `NUMBER(11,0)` 改为 `int(11)`。
  - 将 `VARCHAR2(20 BYTE)` 改为 `varchar(20)`。
- 去掉 `CONSTRAINT "TEST_TBL1_OBPK_1672051192536124"` 参数。
- 去所有掉双引号。

有关 MySQL 模式数据类型的详细信息，请参见 [数据类型概述](https://www.oceanbase.com/docs/enterprise-oceanbase-database-cn-10000000000886185)。

#### 注意

- 需要将租户 `oracle001` 里的 Schema `OBDUMPER_USER01` 导出的目录 `/home/admin/test_migrate_data/csv_data/data/` 下的 `OBDUMPER_USER01` 名称修改为 `test_data`。

- 将导出的 CSV 文件名中的表名中的英文字母改为小写。

  示例语句如下：

  ``` bash

      [root@xxx /home/admin/test_migrate_data/csv_data/data]# mv OBDUMPER_USER01 test_data
      [root@xxx /home/admin/test_migrate_data/csv_data/data]# cd test_data/TABLE
      [root@xxx /home/admin/test_migrate_data/csv_data/data/test_data/TABLE]# ls
      TEST_TBL1.1.0.csv  TEST_TBL2.1.0.csv
      [root@xxx /home/admin/test_migrate_data/csv_data/data/test_data/TABLE]# mv TEST_TBL1.1.0.csv test_tbl1.1.0.csv
      [root@xxx /home/admin/test_migrate_data/csv_data/data/test_data/TABLE]# mv TEST_TBL2.1.0.csv test_tbl2.1.0.csv
      
  ```
