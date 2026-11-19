---
title: ob_create_table_strict_mode
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-0000000002183543.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# ob_create_table_strict_mode

ob_create_table_strict_mode 
================================================

`ob_create_table_strict_mode` 是动态变量，用于设置建表的严格模式。

<main id="notice" type='explain'>
  <h4>说明</h4>
  <p>从 V4.0.0 版本开始弃用。</p>
</main>



| **属性** |                                                                                   **描述**                                                                                    |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 参数类型   | bool                                                                                                                                                                        |
| 默认值    | 0                                                                                                                                                                           |
| 取值范围   | </li><li> 1：表示会严格按照 Locality 建立副本，任何副本建立失败，则建表失败。   </li><li> 0：表示全类型副本至少有 1 个，Paxos 成员组副本达到多数，则建表成功。    |
| 生效范围   | </li><li> Global   </li><li> Session                                                                     |
