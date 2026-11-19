---
title: identity
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-0000000002183476.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# identity

identity 和变量 last_insert_id 是同义词，可以通过 `select @@identity` 查询。

| **属性** |           **描述**            |
|--------|-----------------------------|
| 参数类型   | uint                        |
| 默认值    | 0                           |
| 取值范围   | \[0, 18446744073709551615\] |
| 生效范围   | SESSION                     |
