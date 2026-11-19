---
title: ob_esi_syslog_level
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-0000000002180040.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# ob_esi_syslog_level

`ob_esi_syslog_level` 用于设置 obesi 进程的当前日志记录级别。

<main id="notice" type='explain'>
  <h4>说明</h4>
  <p>从 V4.0.0 版本开始弃用。</p>
</main>

| **属性** | **描述** |
| --- | --- |
| 参数类型 | 字符串 |
| 默认值 | WDIAG |
| 取值范围 |  <ul><li>DEBUG   </li><li> TRACE   </li><li>WDIAG </li><li>EDIAG  </li><li> INFO   </li><li> WARN  </li><li> ERROR </li></ul> |
| 是否重启 OBServer 节点生效 | 否 |
