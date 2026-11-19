---
title: debug_sync_timeout
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001702097.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# debug_sync_timeout

debug_sync_timeout 
=======================================

debug_sync_timeout 用于打开 debug sync 调试开关，并设置其超时时间。


|      **属性**      |  **描述**  |
|------------------|----------|
| 参数类型             | 时间类型     |
| 默认值              | 0        |
| 取值范围             | \[0, +∞) |
| 是否重启 OBServer 节点生效 | 否        |


  <main id="notice" type='explain'>
    <h4>说明</h4>
    <p>debug_sync_timeout 的值为 0 时，表示关闭 debug sync 调试。</p>
  </main>
