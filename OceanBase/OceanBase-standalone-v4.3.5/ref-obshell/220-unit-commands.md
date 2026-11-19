---
title: "obshell 资源规格命令组"
book: obshell
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003975907.html"
tags:
  - oceanbase
  - standalone
  - ref-obshell
---

# obshell 资源规格命令组

本文介绍 obshell 的资源规格命令组，资源规格命令组可用于管理 OceanBase 集群中的资源规格，该命令组要求 OceanBase 集群已经被初始化。

您可通过在命令中配置 `-h`/`--help` 选项查看命令的帮助信息；当任务执行报错时，也可配置 `-v`/`--verbose` 选项查看命令的详细执行过程。

## obshell unit create

使用该命令可以为集群创建新的资源规格。

```
${home_path}/bin/obshell unit create <unit_config_name> -m -c [--min_cpu] [--log_disk_size] [--min_iops] [--max_iops]

# example
/home/admin/oceanbase/bin/obshell unit create unit_1 -m 5G -c 2
```

`home_path` 为 OceanBase 数据库的安装目录，obshell 默认在 OceanBase 数据库安装目录的 `bin` 目录下。`unit_config_name` 需配置为待创建的资源规格名称。

命令的选项说明见下表：

[TABLE]

## obshell unit show

使用该命令可以查询资源规格。

```
${home_path}/bin/obshell unit show [unit_config_name]

# example
/home/admin/oceanbase/bin/obshell unit show
```

`home_path` 为 OceanBase 数据库的安装目录，obshell 默认在 OceanBase 数据库安装目录的 `bin` 目录下。`unit_config_name` 需配置为待查询的资源规格名称，未配置的情况下，默认展示集群中所有 unit 资源规格。

## obshell unit drop

使用该命令可以删除指定的未被使用的资源规格。

```
${home_path}/bin/obshell unit drop <unit_config_name> [-y]

# example
/home/admin/oceanbase/bin/obshell unit drop unit_1
```

`home_path` 为 OceanBase 数据库的安装目录，obshell 默认在 OceanBase 数据库安装目录的 `bin` 目录下。`unit_config_name` 需配置为待删除的资源规格名称。

可通过配置 `-y`/`--yes` 控制是否取消二次确认，该选项无需传值，配置即表示取消二次确认。
