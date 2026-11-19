---
title: "修改合并配置"
book: "系统管理"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077802.html"
tags:
  - oceanbase
  - standalone
  - ref-system-management
---

# 修改合并配置

#### 说明

您也可以在表创建后，通过 `ALTER TABLE table_name SET PROGRESSIVE_MERGE_NUM=0;` 语句修改表的合并行为。

#### 注意

集群级配置项需要在 `sys` 租户下设置。
