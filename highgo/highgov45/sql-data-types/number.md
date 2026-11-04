---
title: "数字类型"
book: "数据类型"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/sql/number.html"
tags:
  - highgo
  - highgo-v45
  - sql-data-types
---

## 数字类型

HGDB 有着丰富的本地数据类型可用，用户也可以使用 `CREATE TYPE` 命令为 HGDB 增加新的数据类型。

数字类型由 2、4 或 8 字节的整数以及 4 或 8 字节的浮点数和可选精度小数组成。下表列出了数字类型的所有可用类型。

| 名字 | 存储尺寸 | 描述 | 范围 |
| --- | --- | --- | --- |
| smallint | 2字节 | 小范围整数 | \-32768 to +32767 |
| integer | 4字节 | 整数的典型选择 | \-2147483648 to +2147483647 |
| bigint | 8字节 | 大范围整数 | \-9223372036854775808 to +9223372036854775807 |
| decimal | 可变 | 用户指定精度，精确 | 最高小数点前 131072 位，以及小数点后16383 位 |
| numeric(precision,scale) | 可变 | 用户指定精度，精确 | 最高小数点前 131072位，以及小数点后16383 位 |
| real | 4字节 | 可变精度，不精确 | 6 位十进制精度 |
| double precision | 8字节 | 可变精度，不精确 | 15 位十进制精度 |
| smallserial | 2字节 | 自动增加的小整数 | 1 到 32767 |
| serial | 4字节 | 自动增加的整数 | 1 到 2147483647 |
| bigserial | 8字节 | 自动增加的大整数 | 1 到9223372036854775807 |

### 整数类型

smallint、integer、bigint。常用的类型是 integer，一般只有在磁盘空间紧张的时候才用 smallint 类型，只有在 integer 范围不够的时候才用 bigint 类型。

### 任意精度数字

numeric(precision,scale)、decimal、real、double precision。numeric 的 precision 是数中有效位的位数，包括小数点两边的数字，scale 是小数部分的位数。numeric 建议用于货币金额和其他要求计算准确的数量。类型 decimal 和 numeric 是等效的，在圆整时，numeric 类型会圆整到远离零的整数，而大部分情况下 real 和 double precision 类型会圆整到最近的偶数。

### 浮点类型

real、double precision 是不精确的、变精度的数字类型。

### 序数类型

smallserial、serial、bigserial。可以用序数类型为表创建一个自增列。类型名 serial 和 serial4 是等效的，两个都创建 integer 列。类型名 bigserial 和 serial8 是等效的，它们创建一个 bigint 列。如果预计使用的标识符数目超过 2^31 个，那么建议使用 bigserial。类型名 smallserial 和 serial2 也以相同方式工作，它们创建一个 smallint 列。

例如用 numeric 创建一个属性 info 在表 table\_num 中：

```sql
CREATE TABLE table_num (info_1 numeric(4,3),info_2 numeric(5,4));
INSERT INTO table_num VALUES (1.234,2.34);
SELECT* FROM table_num;
```

查询结果如下：

```
info_1 | info_2 
--------+--------
  1.234 | 2.3400
(1 行记录)
```