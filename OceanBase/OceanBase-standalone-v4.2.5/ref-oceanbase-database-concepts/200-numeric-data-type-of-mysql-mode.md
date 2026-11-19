---
title: "数值类型"
book: "系统原理"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003150145.html"
tags:
  - oceanbase
  - standalone
  - ref-oceanbase-database-concepts
---

# 数值类型

#### 注意

浮点类型的精度只是 IEEE 标准中规定的理论值，实际情况可能因硬件或操作系统限制略有不同。

#### 说明

- `FLOAT(M,D)` 是 MySQL 的过时语法，不建议用户使用。
- 由于 `FLOAT` 是单精度浮点数，其最大有效精度不会超过 7 位，当输入的有效精度大于 7 时，只有前 7 位有效数字得到保证，超过部分的数值无法保证。MySQL 也存在这种问题，如果用户需要精确查找，建议用户使用 `DECIMAL` 类型。

#### 说明

- `DOUBLE[(M,D)]` 是 MySQL 的过时语法，不建议用户使用。由于`DOUBLE` 是双精度浮点数，其最大有效精度不会超过 15 位，当输入的有效精度大于 15 时，只有前 15 位有效数字得到保证，超过部分的数值无法保证。MySQL 也存在这种问题，如果用户需要精确查找，建议使用 `DECIMAL` 类型。
- OceanBase 数据库中，`D` 的值只支持 0，当设置为非 0 时，会报错"Feature not supportted"。

#### 说明

`DOUBLE PRECISION [(M,D)] ` 是 MySQL 的过时语法，不建议用户使用。如果用户需要精确查找，建议使用 `DECIMAL` 类型。
