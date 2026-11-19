---
title: partition_table_check_interval
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-0000000002180048.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# partition_table_check_interval

partition_table_check_interval 
===================================================

`partition_table_check_interval` 用于设置 OBServer 从分区表中删除不存在的副本的时间间隔。

<main id="notice" type='explain'>
  <h4>说明</h4>
  <p>从 V4.0.0 版本开始弃用。</p>
</main>


|      **属性**      |    **描述**    |
|------------------|--------------|
| 参数类型             | 时间类型         |
| 默认值              | 30m，表示 30 分钟 |
| 取值范围             | \[1m, +∞)    |
| 是否重启 OBServer 节点生效 | 否            |
