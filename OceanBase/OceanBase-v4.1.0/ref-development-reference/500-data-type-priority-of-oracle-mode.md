---
title: "数据类型优先级"
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001701385.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
---

# 数据类型优先级

OceanBase 使用数据类型优先级来确定隐式数据类型转换顺序。本节主要介绍数据类型的转换优先级。

OceanBase 数据库数据类型的转换优先级如下（由高到低的顺序）：

1. 日期时间和间隔数据类型

2. `BINARY_DOUBLE` 数据类型

3. `BINARY_FLOAT` 数据类型

4. `NUMBER` 数据类型

5. 字符数据类型

6. 所有其他内置数据类型
