---
title: "6、查询瀚高数据库的创建时间"
book: "运维指导类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/way/create_time.html"
tags:
  - highgo
  - highgo-v45
  - way-operations-guide
---

## 查询瀚高数据库的创建时间

瀚高数据库可以通过控制文件的”Database system identifier”值来反推数据库的创建时间，方法如下:

## 方法1、通过pg\_controldata查询出system identifier的值，通过to\_timestamp函数将字符串转换为时间格式

```
[highgo@host ~]$ pg_controldata | grep "system identifier"                
Database system identifier:           6940441653725889375     

[highgo@host ~]$ psql highgo highgo                
psql (HighGo Database 6 Release 6.0.2-64-bit Production)                
PSQL: Release HighGo Database 6 Release 6.0.2-64-bit Production                
Type "help" for help.                
highgo=# select to_timestamp(6940441653725889375 >> 32);                
      to_timestamp                      
------------------------
 2021-03-17 10:18:17+08                
(1 row)
```

## 方法2、瀚高数据库提供函数pg\_control\_system可以直接查询出system identifier

```
highgo=# select to_timestamp(system_identifier >> 32) from pg_control_system();                
      to_timestamp                      
------------------------
 2021-03-17 10:18:17+08                
(1 row)
```