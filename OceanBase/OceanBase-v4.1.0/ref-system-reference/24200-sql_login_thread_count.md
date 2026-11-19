---
title: sql_login_thread_count
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001702129.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# sql_login_thread_count

`sql_login_thread_count` 用于设置处理 SQL 登录请求的线程数量。

<main id="notice" type='explain'>
  <h4>说明</h4>
  <p>从 V3.2.4 版本开始引入。</p>
</main>

| **属性** | **描述** |
| --- | --- |
| 参数类型 | 整型 |
| 默认值 | 0 |
| 取值范围 | [0, 32] |
| 是否重启 OBServer 节点生效 | 否 |
