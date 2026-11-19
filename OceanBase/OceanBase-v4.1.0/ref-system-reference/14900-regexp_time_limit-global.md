---
title: regexp_time_limit
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-0000000002186406.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# regexp_time_limit

`regexp_time_limit` 用于正则表达式匹配操作的时间限制，默认单位为毫秒。

<main id="notice" type='explain'>
  <h4>说明</h4>
  <p>从 V4.1.0 版本开始引入。</p>
</main>

| **属性**      |      **描述**                            |
|---------------|------------------------------------------|
| 参数类型      | int                                       |
| 默认值        | 32                                        |
| 取值范围      | \[0, 2147483647]                          |
| 生效范围      | Global                                    |
|是否参与序列化 |否                                          |
