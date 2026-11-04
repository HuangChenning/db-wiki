---
title: "23、将瀚高数据库表内数据导出csv格式"
book: "日常使用类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/way/import_csv.html"
tags:
  - highgo
  - highgo-v45
  - way-daily-use
---

## 将瀚高数据库表内数据导出csv格式

copy命令同\\copy命令语法上相同，区别在于copy必须使用能够超级用户使用,copy.. to file 中的文件都是数据库服务器所在的服务器上的文件，而\\copy 一般用户即可执行且\\copy 保存或者读取的文件是在客户端所在的服务器，本文主要以copy命令作为介绍重点，使用copy命令将表内数据倒为csv格式文件即为excel格式。

## 1、copy命令语法

COPY { 表名 \[ ( 列名称 \[, …\] ) \] | ( 查询 ) }

```
TO { '文件名' | PROGRAM '命令' | STDOUT }
[ [ WITH ] ( 选项 [, ...] ) ]
```

选项可以是下列内容之一:

```
FORMAT 格式_名称
FREEZE [ 布尔 ]
DELIMITER '分隔字符'
NULL '空字符串'
HEADER [ 布尔 ]
QUOTE '引用字符'
ESCAPE '转义字符'
FORCE_QUOTE { ( 列名称 [, ...] ) | * }
FORCE_NOT_NULL ( 列名称 [, ...] )
FORCE_NULL ( 列名称 [, ...] )
ENCODING 'encoding_name(编码名)'
```

## 2、使用介绍

①查看现有表数据

```
highgo=# select * from test;
 user_id |   user_name   | age | gender |                    remark                    
---------+---------------+-----+--------+----------------------------------------------
       1 | Jackie Chan   |  45 | male   | "police story","project A","rush hour"
       3 | Brigitte Li   |  46 | female | 
       4 | Maggie Cheung |  39 | female | 
       5 | Jet Li        |  41 | male   | "Fist of Legend","Once Upon a Time in China"
       2 | Gong Li       |  38 | female | "Farewell My Concubine","Lifetimes Living
(5 行记录)
```

②带列名导出，默认情况下使用，作为分隔符

```
highgo=# copy test to '/tmp/test1.csv' with csv header;
COPY 5
highgo=# \! cat /tmp/test1.csv
user_id,user_name,age,gender,remark
1,Jackie Chan,45,male,"""police story"",""project A"",""rush hour"""
3,Brigitte Li,46,female,
4,Maggie Cheung,39,female,
5,Jet Li,41,male,"""Fist of Legend"",""Once Upon a Time in China"""
2,Gong Li,38,female,"""Farewell My Concubine"",""Lifetimes Living"
```

③带列名导出，指定使用|作为分隔符

```
highgo=# copy test to '/tmp/test1.csv' with csv header DELIMITER '|';
COPY 5
highgo=# \! cat /tmp/test1.csv
user_id|user_name|age|gender|remark
1|Jackie Chan|45|male|"""police story"",""project A"",""rush hour"""
3|Brigitte Li|46|female|
4|Maggie Cheung|39|female|
5|Jet Li|41|male|"""Fist of Legend"",""Once Upon a Time in China"""
2|Gong Li|38|female|"""Farewell My Concubine"",""Lifetimes Living"
```

④带列名导出，将空字符替换为指定值导出

```
highgo=# copy test to '/tmp/test1.csv' with csv header null 'to be supplemented';
COPY 5
highgo=# \! cat /tmp/test1.csv
user_id,user_name,age,gender,remark
1,Jackie Chan,45,male,"""police story"",""project A"",""rush hour"""
3,Brigitte Li,46,female,to be supplemented
4,Maggie Cheung,39,female,to be supplemented
5,Jet Li,41,male,"""Fist of Legend"",""Once Upon a Time in China"""
2,Gong Li,38,female,"""Farewell My Concubine"",""Lifetimes Living"
```