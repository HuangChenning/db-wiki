---
title: "内置数据类型"
book: "Oracle兼容性"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/compatibility/compOracle5.html"
tags:
  - highgo
  - highgo-v9
  - compatibility-oracle
---

## 内置数据类型

瀚高数据库管理系统V9.0提供如下多种兼容数据类型，内容如下：

| **数据类型分类** | **数据类型** | **说明** |
| --- | --- | --- |
| 日期时间类型 | DATE |  |
|  | TIMESTAMP(p) |  |
|  | TIMESTAMP WITH TIME ZONE |  |
|  | TIMESTAMP WITH LOCAL TIME ZONE |  |
|  |  |  |
| 时间间隔类型 | INTERVAL YEAR(p) TO MONTH |  |
|  | INTERVAL DAY(p) TO SECOND(s) |  |
|  |  |  |
| 数值类型 | NUMBER | 无限制 |
|  | BINARY\_FLOAT | 6 位十进制数字精度 |
|  | BINARY\_DOUBLE | 15 位十进制数字精度 |
|  |  |  |
| 字符类型 | CHAR(n) | 支持最大长度32767 |
|  | VARCHAR2(n) | 支持最大长度32767 |
|  |  |  |
| 长类型 | CLOB | 支持最大1GB |
|  | NCLOB | 支持最大1GB |
|  | LONG | 支持最大1GB |
|  | BLOB | 支持最大1GB |
|  | RAW | 支持最大2000字节 |
|  | LONG RAW | 支持最大1GB |

## 示例

主要展示创建带有不同数据类型字段的测试表，插入对应类型数据并进行查询。

### Date

本示例展示创建带有Date类型字段的表，插入数据后进行查询。

代码示例：

ALTER SESSION set nls\_date\_format =’YYYY-MM-DD HH24.MI.SS.FF’;

create table date\_tb1(dt date);

insert into date\_tb1 values(‘2022-08-19 11.11.11’);

select \* from date\_tb1;

### TIMESTAMP

本示例展示创建带有Timestamp类型字段的表，修改nls\_timestamp\_format参数值，插入数据后进行查询。

代码示例：

alter session set nls\_timestamp\_format=’DD-MON-YY HH24.MI.SS.FF’;

create table timestp\_tb(timestp timestamp);

insert into timestp\_tb values(‘19-AUG-22 11.11.11’);

select \* from timestp\_tb;

### TIMESTAMP WITH TIME ZONE

本示例展示创建带有Timestamp with time zone类型字段的表，修改nls\_timestamp\_tz\_format参数值，插入数据后进行查询。

代码示例：

alter session set nls\_timestamp\_tz\_format=’DD-MON-YY HH24.MI.SS.FF TZH:TZM’;

create table timestpwtz\_tb(timestpwtz timestamp with time zone);

insert into timestpwtz\_tb VALUES(‘19-AUG-22 11.11.11’);

select \* from timestpwtz\_tb;

### TIMESTAMP WITH LOCAL TIME ZONE

本示例展示创建带有Timestamp with local time zone类型字段的表，修改nls\_timestamp\_format参数值，插入数据后进行查询。

代码示例：

alter session set nls\_timestamp\_format=’DD-MON-YY HH24.MI.SS.FF’;

create table timestpwltz\_tb(timestpwltz\_clo timestamp with local time zone);

insert into timestpwltz\_tb VALUES(‘19-AUG-22 11.11.11’);

select \* from timestpwltz\_tb;

### INTERVAL YEAR TO MONTH

本示例展示创建带有interval year to month类型字段的表，插入数据后并进行查询。

代码示例：

create table inytom\_tb(ytom\_clo interval year to month);

insert into inytom\_tb values(interval ‘ + 2 -1’ year to month);

select \* from inytom\_tb;

### INTERVAL DAY TO SECOND

本示例展示创建带有interval day to second类型字段的表，插入数据后并进行查询。

代码示例：

create table indtos\_tb(dtos\_clo interval day to second);

insert into indtos\_tb values(interval ‘ 2 07:16:23’ day to second);

select \* from indtos\_tb;

### NUMBER

本示例展示创建带有number类型字段的表，插入数据后并进行查询。

代码示例：

create table num\_tb(num\_clo NUMBER(\*));

insert into num\_tb values(1E-130);

select \* from num\_tb;

### BINARY\_FLOAT

本示例展示创建带有binary\_float类型字段的表，插入数据后并进行查询。

create table binaryf\_tb(binaryf\_clo binary\_float);

insert into binaryf\_tb values (‘34.84’);

select \* from binaryf\_tb;

### BINARY\_DOUBLE

本示例展示创建带有binary\_double类型字段的表，插入数据后并进行查询。

create table binaryd\_tb(binaryf\_clo binary\_double);

insert into binaryd\_tb values (‘34.84’);

select \* from binaryd\_tb;

### CHAR

本示例展示创建带有char类型字段的表，修改nls\_length\_semantics参数值，插入数据后并进行查询。

alter session set nls\_length\_semantics = char;

create table character\_tb(char\_c char(6), char\_b varchar2(6 byte), char\_v varchar(6));

insert into character\_tb values(‘中文测试数据’, ‘123456’, ‘成功’);

select \* from character\_tb;

### VARCHAR2

本示例展示创建带有varchar2类型字段的表，插入数据后并进行查询。

create table varchar2\_tb(char\_clo varchar2(2000));

insert into varchar2\_tb values(‘This is a char test!’);

select \* from varchar2\_tb;

### 其他类型

CLOB、NCLOB、LONG、BLOB、RAW、LONG RAW等类型操作需要结合管理工具使用。