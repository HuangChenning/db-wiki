---
title: cluster_id
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001702087.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# cluster_id

cluster_id 
===============================

`cluster_id` 用于设置本 OceanBase 集群的 ID。

  <main id="notice" type='explain'>
    <h4>说明</h4>
    <p>该配置项仅支持在部署集群时设置，集群生效后，无法修改。</p>
  </main>


|      **属性**      |      **描述**       |
|------------------|-------------------|
| 参数类型             | 整型                |
| 默认值              | 0                 |
| 取值范围             | \[1, 4294901759\] |
| 是否重启 OBServer 节点生效 | 否                 |
