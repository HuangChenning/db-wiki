---
title: transaction_isolation
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-0000000002186366.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# transaction_isolation

transaction_isolation 用于设置事务的隔离级别。

| **属性**  |                            **描述**                            |
|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 参数类型    | varchar                                                      |
| 默认值     | READ-COMMITTED                                               |
| 取值范围    | <li> READ-COMMITTED   <li> REPEATABLE-READ   <li> SERIALIZABLE    |
| 生效范围    | <li> GLOBAL   <li> SESSION                                         |
| 是否参与序列化 | 是                                                            |
