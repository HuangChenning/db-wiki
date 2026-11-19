---
title: arbitration_timeout
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001699379.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# arbitration_timeout

`arbitration_timeout` 用于设置触发自动降级的超时时间。

<main id="notice" type='explain'>
  <h4>说明</h4>
  <p>从 V4.1.0 版本开始引入。</p>
</main>

| **属性** | **描述** |
| --- | --- |
| 参数类型 | 时间类型 |
| 默认值 | 5s |
| 取值范围 | \[3s, +∞) |
| 是否重启 OBSever 节点生效 | 否 |

**示例**

```sql
ALTER SYSTEM SET arbitration_timeout='30s';
```
