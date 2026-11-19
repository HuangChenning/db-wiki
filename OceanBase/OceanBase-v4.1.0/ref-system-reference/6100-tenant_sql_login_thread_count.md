---
title: tenant_sql_login_thread_count
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001699384.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# tenant_sql_login_thread_count

`tenant_sql_login_thread_count` 用于设置 MySQL 租户登录的线程个数，即 `mysql_queue` 线程的个数，默认值为 0 表示取 `unit_min_cpu` 的值。

<main id="notice" type='explain'>
  <h4>说明</h4>
  <p>从 V4.1.0 版本开始引入。</p>
</main>

| **属性** | **描述** |
| --- | --- |
| 参数类型 | 整型 |
| 默认值 | 0 |
| 取值范围 | \[0, 32] |
| 是否重启 OBSever 节点生效 | 否 |
