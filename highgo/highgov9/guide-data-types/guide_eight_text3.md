---
title: "货币类型"
book: "数据类型"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/guide/guide_eight_text3.html"
tags:
  - highgo
  - highgo-v9
  - guide-data-types
---

## 货币类型

money 类型存储固定小数精度的货币数字，小数的精度由数据库的 lc\_monetary 设置决定，表中展示的范围假设有两个小数位。money 类型可以接受的输入格式很多，包括整数和浮点数文字，以及常用的货币格式，如’$1,000.00’。 输出通常是最后一种形式，但和区域相关。

| 名字 | 存储尺寸 | 描述 | 范围 |
| --- | --- | --- | --- |
| money | 8 bytes | 货币额 | 92233720368547758.08 to +92233720368547758.07 |

由于这种数据类型的输出是区域敏感的，因此将money 数据装入到一个具 有不同 lc\_monetary 设置的数据库是不起作用的。为了避免这种问题，在恢复一 个转储到一个新数据库中之前，应确保新数据库的 lc\_monetary 设置和被转储数 据库的相同或者具有等效值。

数据类型 numeric 、int 和 bigint 的值可以被造型成 money 。从数据类型 real 和 double precision 的转换可以通过先造型成 numeric 来实现，例如：

```sql
SELECT ' 12.34'::float8::numeric::money;
```

但是，我们不推荐这样做。浮点数不应该被用来处理货币，因为浮点数可能 会有圆整错误。