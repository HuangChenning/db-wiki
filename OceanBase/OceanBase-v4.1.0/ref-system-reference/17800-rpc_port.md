---
title: rpc_port
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001699356.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# rpc_port

`rpc_port` 用于设置远程访问的协议端口号。

<main id="notice" type='explain'>
  <h4>说明</h4>
  <p>从 V3.2.4 版本开始默认值由 2500 调整为 2882。</p>
</main>


|      **属性**      |     **描述**      |
|------------------|-----------------|
| 参数类型             | 整型              |
| 默认值              | 2882            |
| 取值范围             | \[1025, 65535\] |
| 是否重启 OBServer 节点生效 | 否               |
