---
title: "常量"
book: "MySQL兼容性"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/compatibility/compMySql8.html"
tags:
  - highgo
  - highgo-v9
  - compatibility-mysql
---

## 常量

## 十六进制常量

### 描述

十六进制常量的表示可以使用0xval或X'val'形式，其中val包含十六进制数字（0..9,a..f,A..F），字母大小写不敏感。前缀0x必须小写，不能写成0X。前缀X的大小写不敏感。

当使用0xval表示时，val长度任意，可为奇数，也可为偶数。当val长度为奇数时，将其视为具有额外的前导零，如0xaaa等效于0x0aaa。当使用X'val'表示时，val长度必须为偶数。

十六进制常量从V9.0.5开始支持。

### 示例

合法语法：

0x1

0x12

0xaa

0xAA

0xAa

x’12’

X’12’

非法语法：

0xg

0X12

x’1’

x’0g’

非法语法，如0X12，将被识别为列名。

## 二进制常量

### 描述

二进制常量使用b'val' 或0bval语法书写。val是一个由0和1组成的二进制值。

val长度任意，可为奇数，也可为偶数。当val长度为奇数时，将其视为具有额外的前导零，例如0b111等效于0b0111。

前导的b字母大小写无关，但前导的0b是区分大小写的，不能写成0B。

二进制常量从V9.0.5开始支持。

### 示例

合法语法：

b'01'

B'01'

0b01

非法语法：

b'2'

0B01

非法语法，如0X12，将被识别为列名。