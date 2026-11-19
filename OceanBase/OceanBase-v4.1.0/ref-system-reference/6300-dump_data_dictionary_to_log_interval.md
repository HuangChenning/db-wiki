---
title: dump_data_dictionary_to_log_interval
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001699386.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# dump_data_dictionary_to_log_interval

`dump_data_dictionary_to_log_interval` 用于控制租户数据字典持久化的周期。

<main id="notice" type='explain'>
  <h4>说明</h4>
  <p>从 V4.1.0 版本开始引入。</p>
</main>

| **属性** | **描述** |
| --- | --- |
| 参数类型 | 时间类型 |
| 默认值 | 24H |
| 取值范围 | (0s, +∞) |
| 是否重启 OBSever 节点生效 | 否 |

**示例**

```sql
ALTER SYSTEM SET dump_data_dictionary_to_log_interval = 24H;
```
