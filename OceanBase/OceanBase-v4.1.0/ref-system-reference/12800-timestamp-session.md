---
title: timestamp
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-0000000002186431.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# timestamp

TIMESTAMP 是时间戳，单位为秒，该变量影响 `select now(6)`的结果。

| **属性** |       **描述**       |
|--------|--------------------|
| 参数类型   | numeric            |
| 默认值    | 0                  |
| 取值范围   | \[0, 253402272000) |
| 生效范围   | SESSION            |
