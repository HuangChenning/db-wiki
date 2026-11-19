---
title: log_transport_compress_all
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001699381.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# log_transport_compress_all

`log_transport_compress_all` 用于对日志传输是否使用压缩。

<main id="notice" type='explain'>
  <h4>说明</h4>
  <p>从 V4.1.0 版本开始引入。</p>
</main>

| **属性** | **描述** |
| --- | --- |
| 参数类型 | 布尔类型 |
| 默认值 | False |
| 取值范围 |<ul><li> False 指对日志传输不使用压缩  </li><li>  True 指对日志传输使用压缩</li></ul>|
| 是否重启 OBServer 节点生效 | 否 |
