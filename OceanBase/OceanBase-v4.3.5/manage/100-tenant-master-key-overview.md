---
title: "租户主密钥概述"
book: "管理数据库"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005375452.html"
tags:
  - oceanbase
  - distributed
  - manage
---

# 租户主密钥概述

#### 功能适用性

OceanBase 数据库社区版暂不支持租户主密钥相关功能。

#### 注意

- 系统租户不能开启加密。
- 配置项 `tde_method` 一旦设置为非 `none` 值，就不能再修改。除非租户重建，否则无法切换为其他加密方式。
