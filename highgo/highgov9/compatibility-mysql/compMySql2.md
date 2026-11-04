---
title: "数据类型"
book: "MySQL兼容性"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/compatibility/compMySql2.html"
tags:
  - highgo
  - highgo-v9
  - compatibility-mysql
---

## 数据类型

## 数值类型

### 整数

| 类型 | 字节 | 最小值 | 最小值(无符号) | 最大值 | 最大值(无符号) |
| --- | --- | --- | --- | --- | --- |
| TINYINT | 2 | \-128 | 0 | 127 | 255 |
| SMALLINT | 2 | \-32768 | 0 | 32767 | 65535 |
| MEDIUMINT | 4 | \-8388608 | 0 | 8388607 | 16777215 |
| INT | 4 | \-2147483648 | 0 | 2147483647 | 4294967295 |
| BIGINT | 8 | \-2^63^ | 0 | 2^63^-1 | 2^64^-1 |

#### 语法

TINYINT\[(M)\] \[UNSIGNED\] \[ZEROFILL\]

SMALLINT\[(M)\] \[UNSIGNED\] \[ZEROFILL\]

MEDIUMINT\[(M)\] \[UNSIGNED\] \[ZEROFILL\]

INT\[(M)\] \[UNSIGNED\] \[ZEROFILL\]

BIGINT\[(M)\] \[UNSIGNED\] \[ZEROFILL\]

#### 参数

M

表示最大显示宽度。显示宽度与类型可以存储的值的范围无关。最大值为255。

UNSIGNED

标识了此数据类型为无符号类型。

ZEROFILL

如果为数值列指定了ZEROFILL，会自动向该列添加UNSIGNED属性。

#### 示例

create table t1(c1 tinyint);

insert into t1 values(-128);

create table t2(c1 smallint);

insert into t2 values(0);

create table t3(c1 mediumint);

insert into t3 values(8388607);

create table t4(c1 integer);

insert into t4 values(-2147483648);

create table t5(c1 bigint);

insert into t5 values(9223372036854775807);

### 浮点数

FLOAT

单精度浮点数，允许的值范围是-3.402823466E+38到-1.175494351E-38，0，以及1.175494351E-38到3.402823466E+38。这些是基于IEEE标准的理论限制。实际范围可能会稍微小一些，具体取决于硬件或操作系统。

DOUBLE

双精度浮点数。允许的值范围是 -1.7976931348623157E+308到 -2.2250738585072014E-308，0，以及2.2250738585072014E-308到1.7976931348623157E+308。这些是基于IEEE标准的理论限制。实际范围可能会稍微小一些，具体取决于硬件或操作系统。

REAL

如果启用了REAL\_AS\_FLOAT模式，REAL是FLOAT的同义词；如果没有启用REAL\_AS\_FLOAT模式，REAL是DOUBLE的同义词。

#### 语法

FLOAT\[(M,D)\]

FLOAT(p)

DOUBLE\[(M,D)\]

DOUBLE PRECISION\[(M,D)\]

REAL\[(M,D)\]

#### 参数

M

可以存储的数字的总位数，最大值为255。

D

小数点后面的数字位数。最大值为30。

如果省略M和D，则值会按照硬件允许的限制存储。单精度浮动点数的精度大约为7位小数，双精度浮动点数的精度大约为 15 位小数。

p

表示位数的精度。仅使用此值来确定结果数据类型是使用FLOAT还是DOUBLE。如果p的值在0到24之间，数据类型将变为FLOAT，且没有M或D值。如果p的值在25到53之间，数据类型将变为DOUBLE，且没有M或D值。结果列的范围单精度FLOAT或双精度DOUBLE数据类型相同。

#### 示例

##float

set sql\_mode='REAL\_AS\_FLOAT';

create table t1(c1 float(1,0));

INSERT INTO t1 (c1) VALUES (3.14);

create table t2(c1 real);

INSERT INTO t2 (c1) VALUES (7.89);

##double

set sql\_mode='';

create table t3(c1 double(255,30));

INSERT INTO t3 (c1) VALUES (1.6180339887);

create table t4(c1 real);

INSERT INTO t4 (c1) VALUES (1.414);

### BIT类型

BIT数据类型是一种位值类型，用于存储位值。指定位值可以使用b'value'表示法，value是使用0和1表示的一个二进制值。例如，b'111'和b'10000000'分别表示7和128。

BIT类型从V9.0.5开始支持。

#### 语法

BIT\[(M)\]

#### 参数

M

M表示每个值的位数，范围从1到64。如果省略M，则默认值为1。

如果将小于M位长的值分配给BIT(M)列，该值会在左侧填充零。例如，将b'101'分配给BIT(6)列，实际上等同于分配b'000101'。

#### 示例

create table t1(c1 bit);

INSERT INTO t1 (c1) VALUES (B'1');

create table t2(c1 bit(6));

INSERT INTO t2 (c1) VALUES (B'1101');

## 字符类型

### CHAR

一种固定长度的字符串，在存储时始终用空格右填充到指定长度。

支持 sql\_mode 包含 PAD\_CHAR\_TO\_FULL\_LENGTH 的情况，以及cast(‘aaa’ as char)。

#### 语法

CHAR\[(M)\]

#### 参数

M

基于PG的char类型，增加了对char(0)的支持。M代表列的长度（以字符为单位），默认为1。

#### 示例

create table type\_c (c char(1));

insert into type\_c values('a');

### VARCHAR

一个可变长度的字符串。

#### 语法

VARCHAR(M)

NCHAR VARCHAR(M)

#### 参数

M

基于PG的varchar类型，增加了对varchar(0)的支持。M代表列的长度（以字符为单位），默认为1。

#### 示例

create table type\_vc (vc varchar);

insert into type\_vc values('a');

create table type\_nvc (vc nchar varchar(6));

insert into type\_nvc values('abcd');

create table type\_vc0 (vc varchar(0));

insert into type\_vc0 values('');

### TEXT

文本数据类型，用于存储大量文本数据。可以使用不同的变体，如TINYTEXT、TEXT、MEDIUMTEXT、LONGTEXT，它们的最大长度逐渐增加：

TINYTEXT：255（2^8^ − 1）个字符

TEXT：65,535 (2^16^ − 1) 个字符

MEDIUMTEXT：16,777,215 (2^24^ − 1)个字符

LONGTEXT：1GB个字符

#### 语法

TEXT\[(M)\]

TINYTEXT

MEDIUMTEXT

LONGTEXT

#### 参数

M

基于PG的text类型，增加了对text(M)的支持。表示文本列的最大长度，通常不需要指定，因为 TEXT 类型本身已经有最大长度限制。

#### 示例

##text

CREATE TABLE TextTest (t text);

INSERT INTO TextTest VALUES('This is a text test.');

##tinytext

CREATE TABLE TinyTextTest (

id INT PRIMARY KEY,

short\_description TINYTEXT

);

INSERT INTO TinyTextTest (id, short\_description) VALUES (1, 'This is a  
short text.');

##mediumtext

CREATE TABLE MediumTextTest (

id INT PRIMARY KEY,

medium\_description MEDIUMTEXT

);

INSERT INTO MediumTextTest (id, medium\_description) VALUES (1, 'This is  
a medium-length text.');

##longtext

CREATE TABLE LongTextTest (

id INT PRIMARY KEY,

long\_description LONGTEXT

);

INSERT INTO LongTextTest (id, long\_description) VALUES (1, 'This is a  
long text.');

## 二进制类型

### BINARY

#### 描述

BINARY类型类似于CHAR类型，但存储的是二进制字节字符串，而不是非二进制字符字符串。BINARY是定长的二进制类型，可选的长度M表示列的字节长度，最大长度为255，如果省略，M默认值为1。

#### 示例

create table tb(c binary(5));

INSERT INTO tb (c) VALUES('a\\0\\0');

### VARBINARY

#### 描述

VARBINARY类型类似于VARCHAR类型，但存储的是二进制字节字符串，而不是非二进制字符字符串。VARBINARY是变长的二进制类型，M表示列的最大长度，以字节为单位，最大长度为65532。

#### 示例

create table tvb(c varbinary(10));

INSERT INTO tvb (c) VALUES ('1234567890');

### BLOB

#### 描述

BLOB  
是一种二进制大对象，可以存储可变量的数据。四种BLOB类型分别是TINYBLOB、BLOB、MEDIUMBLOB和LONGBLOB。它们的区别仅在于它们能存储的最大值长度：

TINYBLOB：255（2^8^ − 1）字节

BLOB：65,535 (2^16^ − 1) 字节

MEDIUMBLOB：16,777,215 (2^24^ − 1) 字节

LONGBLOB：1GB 字节

#### 示例

create table test\_blob (c BLOB);

INSERT INTO test\_blob (c) VALUES (X'48656C6C6F');

create table test\_tinyblob (c TINYBLOB);

INSERT INTO test\_tinyblob (c) VALUES (X'01');

create table test\_mediumblob (c MEDIUMBLOB);

INSERT INTO test\_mediumblob (c) VALUES (X'1234567890ABCDEF');

create table test\_longblob (c LONGBLOB);

INSERT INTO test\_longblob (c) VALUES (X'ABCDEF1234567890');

## ENUM类型

ENUM是一种字符串对象，其值从在表创建时的列定义中显式列出的允许值列表、NULL或特殊的空值（''）中选择。ENUM的值在内部表示为整数。

ENUM类型从V9.0.5开始支持。

### 语法

ENUM('value1','value2',...)

### 参数

'value1','value2',...

允许值的列表。

### 示例

CREATE TABLE shirts (

name VARCHAR(40),

size ENUM('x-small', 'small', 'medium', 'large', 'x-large')

);

INSERT INTO shirts (name, size) VALUES ('Polo', 'large');

## 时间日期类型

### DATE

#### 描述

DATE是一个日期。支持的范围是 '1000-01-01' 到 '9999-12-31'。以 ‘YYYY-MM-DD' 格式显示DATE值，但允许使用字符串或数字将值赋给DATE列。

#### 示例

CREATE TABLE td1 (d DATE);

INSERT INTO td1 (d) VALUES ('2025-11-18');

### TIME

#### 描述

TIME\[(fsp)\]是一个时间。范围是 '-838:59:59.000000' 到 ‘838:59:59.000000'。以 'hh:mm:ss\[.fraction\]' 格式显示TIME值，但允许使用字符串或数字将值赋给TIME列。fsp值的范围从0到6，用于指定小数秒的精度。值为0表示没有小数部分。如果省略，则默认精度为0。

#### 示例

CREATE TABLE tt1 (t TIME(3));

INSERT INTO tt1 (t) VALUES ('12:30:45.123');

### DATETIME

#### 描述

DATETIME\[(fsp)\]是日期和时间的组合。支持的范围是 '1000-01-01 00:00:00.000000' 到 '9999-12-31 23:59:59.499999'。以 'YYYY-MM-DD hh:mm:ss\[.fraction\]'  
格式显示DATETIME值，但允许使用字符串或数字将值赋给DATETIME列。fsp值的范围从0到6，用于指定小数秒的精度。值为0表示没有小数部分。如果省略，则默认精度为0。

#### 示例

CREATE TABLE tdt1 (dt DATETIME(6));

INSERT INTO tdt1 (dt) VALUES ('2025-11-18 12:30:45');

### TIMESTAMP

#### 描述

TIMESTAMP\[(fsp)\]是一个时间戳。范围为 '1970-01-01 00:00:01.000000' UTC 到 '2038-01-19 03:14:07.499999' UTC。TIMESTAMP值以自纪元（'1970-01-01 00:00:00' UTC）以来的秒数存储。TIMESTAMP无法表示值'1970-01-01 00:00:00'，因为这等同于纪元后的0秒，而值0被保留用于表示 '0000-00-00 00:00:00'，即”零”时间戳值。fsp值的范围从0到6，用于指定小数秒的精度。值为0表示没有小数部分。如果省略，则默认精度为0。

#### 示例

CREATE TABLE tts1 (ts TIMESTAMP(0));

INSERT INTO tts1 (ts) VALUES ('2025-11-18 12:30:45');

### YEAR

#### 描述

YEAR是一个1字节类型，用于表示年份值。它可以声明为YEAR，默认为4个字符的显示宽度，或者等效地声明为YEAR(4)，并显式指定显示宽度。YEAR\[(4)\]是四位数格式的年份。以YYYY格式显示YEAR值，但允许使用字符串或数字为YEAR列赋值。值的显示范围为1901到2155，或者0000。