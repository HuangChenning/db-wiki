---
title: backup_net_limit
book: "配置项和系统变量"
version: V4.5.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000004478964.html"
tags:
  - oceanbase
  - distributed
  - ref-configuration-items-and-system-variables
---

# backup_net_limit

<main id="notice" type='explain'>
<h4>说明</h4>
<P>由于 V4.x 版本对物理备份恢复功能进行了架构的优化调整，不再支持集群级备份，该配置项从 V4.0.0 版本开始删除。</P>
</main>

## 功能描述

`backup_net_limit` 用于设置集群备份的总带宽。

## 属性说明

|      **属性**      |  **描述**   |
|------------------|-----------|
| 参数类型             | Capacity     |
| 默认值              | 0M        |
| 取值范围             | \[0M, +∞) |
| 是否重启 OBServer 节点生效 | 否         |
