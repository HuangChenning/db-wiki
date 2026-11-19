---
title: nls_date_language
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-0000000002183515.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# nls_date_language

`nls_date_language` 表示数据库国际化支持中的日期默认语言。用于 TO_DATE 和 TO_CHAR 输入或返回的日期、月份、上下午、公元前后等信息。

  <main id="notice" type='explain'>
    <h4>说明</h4>
    <p>该变量不支持修改。</p>
  </main>

| **属性**  |                                                   **描述**                                                   |
|---------|------------------------------------------------------------------------------------------------------------|
| 参数类型    | varchar                 |
| 默认值     | AMERICAN                |
| 取值范围    | N/A                     |
| 生效范围    | <li> Global   <li> Session    |
| 是否参与序列化 | 是                       |
