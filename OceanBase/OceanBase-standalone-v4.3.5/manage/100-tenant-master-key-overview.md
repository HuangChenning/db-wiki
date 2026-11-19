---
title: "租户主密钥概述"
book: "管理数据库"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006362358.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 租户主密钥概述

#### 注意

- 系统租户不能开启加密。
- 配置项 `tde_method` 一旦设置为非 `none` 值，就不能再修改。除非租户重建，否则无法切换为其他加密方式。
