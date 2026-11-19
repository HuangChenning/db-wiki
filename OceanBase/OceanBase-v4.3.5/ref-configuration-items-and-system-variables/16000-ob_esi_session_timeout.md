---
title: ob_esi_session_timeout
book: "配置项和系统变量"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002015693.html"
tags:
  - oceanbase
  - distributed
  - ref-configuration-items-and-system-variables
---

# ob_esi_session_timeout

<main id="notice" type='explain'>
<h4>说明</h4>
<p>由于 V4.x 版本对物理备份恢复功能进行了架构的优化调整，该配置项对应的功能在 V4.x 版本中不再支持，从 V4.0.0 版本开始删除。</p>
</main>

## 功能描述

`ob_esi_session_timeout` 用于设置 obesi 进程持有活动会话资源的超时时间。

## 属性说明

| **属性** | **描述** |
| --- | --- |
| 参数类型 | Time |
| 默认值 | 1m |
| 取值范围 | [10s, 30m] |
| 是否重启 OBServer 节点生效 | 否 |
