---
title: "生成租户主密钥（Oracle 模式）"
book: "管理数据库"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005375454.html"
tags:
  - oceanbase
  - distributed
  - manage
---

# 生成租户主密钥（Oracle 模式）

#### 功能适用性

OceanBase 数据库社区版暂不支持租户主密钥相关功能。

#### 注意

配置项 `tde_method` 一旦设置为非 `none` 值，就不能再修改。

配置项 `tde_method` 中的 `obcloud` 选项从 V4.3.5 BP2 版本开始引入。

#### 注意

仅当租户上所有 OBServer 节点上的配置项 tde_method 的值均为 obcloud，该语句才能执行成功。
