---
title: cursor_sharing
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-0000000002186422.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# cursor_sharing

`cursor_sharing` 用于判断处理 SQL 时是否进行参数化。

<main id="notice" type='explain'>
  <h4>说明</h4>
  <p>从 V4.0.0 版本开始引入。</p>
</main>

|    属性    |                                                                       描述                                                                        |
|----------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| 参数类型     | enum                                                         |
| 默认值      | FORCE                                                        |
| 取值范围     | <li> FORCE：表示处理 SQL 时，必须要进行参数化   <li> EXACT：表示处理 SQL 时，不需要进行参数化    |
| 生效范围     | <li> Global   <li> Session                                         |
| 是否参与序列化  | 否                                                            |
| 是否影响计划生成 | 否                                                            |
| 是否可以为空   | 否                                                            |
| 是否可修改    | 是                                                            |
