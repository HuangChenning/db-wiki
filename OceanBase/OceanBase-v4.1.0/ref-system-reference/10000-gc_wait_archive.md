---
title: gc_wait_archive
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-0000000002178104.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# gc_wait_archive

gc_wait_archive 
====================================

`gc_wait_archive` 用于设置分区 GC 时是否需要等待分区上所有日志归档完成。

<main id="notice" type='explain'>
  <h4>说明</h4>
  <p>从 V4.0.0 版本开始弃用。</p>
</main>

|      **属性**      |                                                 **描述**                                                 |
|------------------|--------------------------------------------------------------------------------------------------------|
| 参数类型             | 布尔类型                                                                                                   |
| 默认值              | True                                                                                                   |
| 取值范围             | </li><li> False   </li><li> True    |
| 是否重启 OBServer 节点生效 | 否                                                                                                      |
