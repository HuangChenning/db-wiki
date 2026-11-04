---
title: "数字类型"
book: "数据类型"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/guide/guide_eight_text7.html"
tags:
  - highgo
  - highgo-v9
  - guide-data-types
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

类型 smallint 、integer 和 bigint 存储各种范围的全部是数字的数，常用的类型是 integer，因为它提供了在范围、存储空间和性能之间的最佳平 衡。一般只有在磁盘空间紧张的时候才使用 smallint 类型，SQL 只声明了整数类型 integer（或 int）、smallint 和 bigint 。类型 int2、int4 和 int8 都是扩展

### 任意精度类型

numeric(precision,scale)、decimal、real、double precision。numeric 的 precision 是数中有效位的位数，包括小数点两边的数字，scale 是小数部分的位数。numeric 建议用于货币金额和其他要求计算准确的数量。类型 decimal 和 numeric 是等效的，在圆整时，numeric 类型会圆整到远离零的整数，而大部分情况下 real 和 double precision 类型会圆整到最近的偶数。

### 浮点类型

数据类型 real 和 double precision 是不精确的、变精度的数字类型。 如果你要求准确的存储和计算（例如计算货币金额），应使用 numeric 类 型。

### 序数类型

smallserial 、serial 和 bigserial 类型不是真正的类型，它们只是为了创建唯一 标识符列而存在的方便符号（类似其它一些数据库中支持的AUTO\_INCREMENT 属性），例如

```sql
CREATE TABLE tablename (
colname SERIAL
);
等价于以下语句：
CREATE SEQUENCE tablename_colname_seq AS integer;
CREATE TABLE tablename (
colname integer NOT NULL DEFAULT nextval('tablename_colname_seq') );
```

**注意：**

因为 smallserial、serial 和 bigserial 是用序列实现的，所以即使没有删除过行， 在出现在列中的序列值可能有“空洞”或者间隙。如果一个从序列中分配的 值被用在一行中，即使该行最终没有被成功地插入到表中，该值也被“用掉” 了。例如，当插入事务回滚时就会发生这种情况。