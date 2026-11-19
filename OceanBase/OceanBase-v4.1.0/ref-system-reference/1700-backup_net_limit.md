---
title: backup_net_limit
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-0000000002168963.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# backup_net_limit

backup_net_limit
=====================================

`backup_net_limit` 用于设置集群备份的总带宽。

<main id="notice" type='explain'>
  <h4>说明</h4>
  <p>从 V4.0.0 版本开始弃用。</p>
</main>

|      **属性**      |  **描述**   |
|------------------|-----------|
| 参数类型             | 容量单位      |
| 默认值              | 0M        |
| 取值范围             | \[0M, +∞) |
| 是否重启 OBServer 节点生效 | 否         |
