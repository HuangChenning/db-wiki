---
title: "生成租户主密钥（Oracle 模式）"
book: "管理数据库"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006362360.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 生成租户主密钥（Oracle 模式）

#### 注意

配置项 `tde_method` 一旦设置为非 `none` 值，就不能再修改。

配置项 `tde_method` 中的 `obcloud` 选项从 V4.3.5 BP2 版本开始引入。

#### 注意

仅当租户上所有 OBServer 节点上的配置项 tde_method 的值均为 obcloud，该语句才能执行成功。
