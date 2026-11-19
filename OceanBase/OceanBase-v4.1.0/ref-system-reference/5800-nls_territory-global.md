---
title: nls_territory
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-0000000002183533.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# nls_territory

`nls_territory` 表示数据库国际化支持中的当前地域，与 nls_language 结合使用。

  <main id="notice" type='explain'>
    <h4>说明</h4>
    <p>该变量不支持修改。</p>
  </main>

| **属性**  |                                                   **描述**                                                   |
|---------|------------------------------------------------------------------------------------------------------------|
| 参数类型    | varchar                 |
| 默认值     | AMERICA                 |
| 取值范围    | N/A                     |
| 生效范围    | <li> Global   <li> Session    |
| 是否参与序列化 | 是                       |
