---
title: "数字函数"
book: "常用内置函数"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/guide/guide_one_text8.html"
tags:
  - highgo
  - highgo-v9
  - guide-built-in-functions
---

## 数学函数

HGDB 为内建的数据类型提供了大量的函数，psql 命令 `\df` 可以用于显示所有可用的函数和操作符的列表。

### 数学函数

| 函数 | 返回类型 | 描述 | 例子 | 结果 |
| --- | --- | --- | --- | --- |
| abs(x) | （和输入相同） | 绝对值 | abs(-17.4) | 17.4 |
| cbrt(dp) | dp | 立方根 | cbrt(8.0) | 2 |
| ceil(dp or numeric) | （和输入相同） | 不小于参数的 最近的整数 | ceil(-42.8) | \-42 |
| ceiling(dp or numeric) | （和输入相同） | 不小于参数的 最近的整数 （ceil的别名） | ceil(-95.3) | \-95 |
| degrees(dp) | dp | 把弧度转为角度 | degrees(0.5) | 28.64788975 654116 |
| div(y numeric,x numeric) | numeric | y/x 的整数商 | div(9,4) | 2 |
| exp(dp or numeric) | （和输入相同） | 指数 | exp(1.0) | 2.71828182 84590452 |
| floor(dp or numeric) | （和输入相同） | 不大于参数的 最近的整数 | floor(-42.8) | \-43 |
| ln(dp or numeric) | （和输入相同） | 自然对数 | ln(2.0) | 0.693147180 5599453 |
| log(dp or numeric) | （和输入相同） | 以10为底的对数 | log(100.0) | 2.00000000 00000000 |
| log10(dp or numeric) | （和输入相同） | 以10为底的对数 | log10(100.0) | 2.000000000 0000000 |
| log(b numeric, x numeric) | numeric | 以 b 为底的对数 | log(2.0,64.0) | 6.00000000 00000000 |
| mod(y, x) | （和参数类型相同） | y/x 的余数 | mod(9,4) | 1 |
| pi() | dp | ”π“的常数 | pi() | 3.14159265 3589793 |
| power(a dp, b dp) | dp | 求 a 的 b 次幂 | power(9.0,3.0) | 729.0000000 000000000 |
| power(a numeric, b numeric) | numeric | 求 a 的 b 次幂 | power(9.0,3.0) | 729.0000000 000000000 |
| radians(dp) | dp | 把角度转为弧度 | radians(45.0) | 0.78539816 33974483 |
| round(dp or numeric) | （和输入相同） | 圆整为最接近的整数 | round(42.4) | 42 |
| round(v numeric, s int) | numeric | 圆整为 s 位小数数字 | round(42.4382,2) | 42.44 |
| scale(numeric) | integer | 参数的精度 （小数点后的位数） | scale(8.41) | 2 |
| sign(dp or numeric) | （和输入相同） | 参数的符号（-1，0，+1） | sign(-8.4) | \-1 |
| sqrt(dp or numeric) | （和输入相同） | 平方根 | sqrt(2.0) | 1.4142135 62373095 |
| trunc(dp or numeric) | （和输入相同） | 截断（向零靠近） | trunc(42.8) | 42 |
| trunc(v numeric, s int) | numeric | 截断为 s 位小数位置的数字 | trunc(42.4382,2) | 42.43 |
| width\_bucket (op dp, b1 dp, b2 dp, count int) | int | 返回一个桶号，这个桶是在一个柱状图中 operand 将被分配的那个桶，该柱状图有 count 个散布在范围 b1 到 b2 上的等宽桶。对于超过该范围的输入，将返回0或者 count+1 | width\_bucket (5.35,0.024, 10.06,5) | 3 |
| width\_bucket (op numeric, b1 numeric, b2 numeric, count int) | int | 返回一个桶号，这个桶是在一个柱状图中 operand 将被分配的那个桶，该柱状图有 count 个散布在范围 b1 到 b2 上的等宽桶。对于超过该范围的输入，将返回0或者 count+1 | width\_bucket (5.35,0.024, 10.06,5) | 3 |
| width\_bucket (operand anyelement, thresholds anyarray) | int | 返回一个桶号，这个桶是在给定数组中 operand 将被分配的桶，该数组列出了桶的下界。对于一个低于第一个下界的输入返回0。thresholds 数组必须被排好序，最小的排在最前面，否则将会得到意想不到的结果 | width\_bucket (now(), array\[‘yesterday’, ‘today’, ‘tomorrow’\]::timestamptz\[ \]) | 2 |

### 随机函数

| 函数 | 返回类型 | 描述 |
| --- | --- | --- |
| random() | dp | 范围 0.0 <= x < 1.0 中 的随机值 |
| setseed(dp) | void | 为后续的 random()调用 设置种子（值为于 -1.0 和 1.0 之间，包括边界值） |

### 三角函数

| 函数（弧度） | 函数（角度） | 描述 |
| --- | --- | --- |
| acos(x) | acosd(x) | 反余弦 |
| asin(x) | asind(x) | 反正弦 |
| atan(x) | atand(x) | 反正切 |
| atan2(y, x) | atan2d(y, x) | y/x 的反正切 |
| cos(x) | cosd(x) | 余弦 |
| cot(x) | cotd(x) | 余切 |
| sin(x) | sind(x) | 正弦 |
| tan(x) | tand(x) | 正切 |

### 双曲函数

| 函数 | 描述 | 举例 | 结果 |
| --- | --- | --- | --- |
| sinh(x) | 双曲正弦 | sinh(0) | 0 |
| cosh(x) | 双曲余弦 | cosh(0) | 1 |
| tanh(x) | 双曲切线 | tanh(0) | 0 |
| asinh(x) | 反双曲正弦 | asinh(0) | 0 |
| acosh(x) | 反双曲余弦 | acosh(1) | 0 |
| atanh(x) | 反双曲切线 | atanh(0) | 0 |