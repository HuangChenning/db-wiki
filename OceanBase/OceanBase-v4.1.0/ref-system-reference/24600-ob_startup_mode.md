---
title: ob_startup_mode
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001702133.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# ob_startup_mode

`ob_startup_mode` 用于设置 OBServer 节点的启动模式，仅支持在第一次启动时修改。

<main id="notice" type='explain'>
  <h4>说明</h4>
  <p>该配置项从 V4.1.0 版本开始引入。</p>
</main>

| **属性** | **描述** |
| --- | --- |
| 参数类型 | 字符串类型 |
| 默认值 | normal |
| 取值范围 |<ul><li> normal 表示以正常模式启动  </li><li> arbitration 表示以仲裁模式启动 </li></ul>|
| 是否重启 OBServer 节点生效 | 否 |
