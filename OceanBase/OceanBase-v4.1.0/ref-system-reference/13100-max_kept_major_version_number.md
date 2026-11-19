---
title: max_kept_major_version_number
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-0000000002168953.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# max_kept_major_version_number

max_kept_major_version_number 
==================================================

`max_kept_major_version_number` 用于设置数据保留的冻结版本数量。

<main id="notice" type='explain'>
  <h4>说明</h4>
  <p>从 V4.0.0 版本开始弃用。</p>
</main>

|      **属性**      |  **描述**   |
|------------------|-----------|
| 参数类型             | 整型        |
| 默认值              | 2         |
| 取值范围             | \[1, 16\] |
| 是否重启 OBServer 节点生效 | 否         |
