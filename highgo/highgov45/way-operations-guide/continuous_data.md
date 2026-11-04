---
title: "15、在HGDB中生成连续时间数据"
book: "运维指导类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/way/continuous_data.html"
tags:
  - highgo
  - highgo-v45
  - way-operations-guide
---

## 在HGDB中生成连续时间数据

## 1、文档用途

本文介绍了如何使用函数generate\_series产生连续的时间数据。

## 2、详细信息

在一些业务场景下，有时需要数据库产生连续时间的数据。HGDB中，可以通过函数generate\_series批量产生数据。

下面是按月、天、小时产生数据的示例。

按月产生连续数据

```
highgo=# SELECT to_char( T, 'yyyy-mm' ) AS TIME 

FROM generate_series(to_timestamp('2020-01', 'yyyy-mm'), to_timestamp('2020-10', 'yyyy-mm'), '1 months') AS T;

  time   

---------

 2020-01

 2020-02

 2020-03

 2020-04

 2020-05

 2020-06

 2020-07

 2020-08

 2020-09

 2020-10

(10 rows)
```

按天产生连续数据

```
highgo=# SELECT to_char( T, 'yyyy-mm-dd' ) AS TIME 

highgo-# FROM generate_series(to_timestamp('2020-01-01', 'yyyy-mm-dd'), to_timestamp('2020-01-03', 'yyyy-mm-dd'), '1 days') AS T;

    time    

------------

 2020-01-01

 2020-01-02

 2020-01-03

(3 rows)
```

按小时产生连续数据

highgo=# SELECT to\_char( t, ‘yyyy-mm-dd hh24:mi:ss’ ) AS TIME

```
highgo-# FROM generate_series ( to_timestamp( '2020-01-01 00:00:00', 'yyyy-mm-dd hh24:mi:ss' ), to_timestamp( '2020-01-02 00:00:00', 'yyyy-mm-dd hh24:mi:ss' ), '1 hours' ) AS t;

        time         

---------------------

 2020-01-01 00:00:00

 2020-01-01 01:00:00

 2020-01-01 02:00:00

 2020-01-01 03:00:00

 2020-01-01 04:00:00

 2020-01-01 05:00:00

 2020-01-01 06:00:00

 2020-01-01 07:00:00

 2020-01-01 08:00:00

 2020-01-01 09:00:00

 2020-01-01 10:00:00

 2020-01-01 11:00:00

 2020-01-01 12:00:00

 2020-01-01 13:00:00

 2020-01-01 14:00:00

 2020-01-01 15:00:00

 2020-01-01 16:00:00

 2020-01-01 17:00:00

 2020-01-01 18:00:00

 2020-01-01 19:00:00

 2020-01-01 20:00:00

 2020-01-01 21:00:00

 2020-01-01 22:00:00

 2020-01-01 23:00:00

 2020-01-02 00:00:00

(25 rows)
```

根据上面的语句还可以产生按分钟、按秒的语句，写法如下

```
--按分钟产生连续时间数据

SELECT to_char( t, 'yyyy-mm-dd hh24:mi:ss' ) AS TIME 

FROM generate_series ( to_timestamp( '2020-01-01 00:00:00', 'yyyy-mm-dd hh24:mi:ss' ), to_timestamp( '2020-01-02 00:00:00', 'yyyy-mm-dd hh24:mi:ss' ), '1 minutes' ) AS t;

--按秒产生连续时间数据

SELECT to_char( t, 'yyyy-mm-dd hh24:mi:ss' ) AS TIME 

FROM generate_series ( to_timestamp( '2020-01-01 00:00:00', 'yyyy-mm-dd hh24:mi:ss' ), to_timestamp( '2020-01-02 00:00:00', 'yyyy-mm-dd hh24:mi:ss' ), '1 seconds' ) AS t;
```

如果需要产生间隔的时间数据，只需要修改generate\_series的第三个参数，如果需要间隔一小时的时间数据，将“1 hours”修改为“2 hours”即可。

根据上面的例子，可以产生当月1号到当前时间的所有时间数据，如下：

```
highgo=# SELECT to_char(tt,'yyyy-mm-dd') as TIME FROM generate_series(date_trunc('month',now()), now(), '1 days') AS tt;

    time    

------------

 2020-05-01

 2020-05-02

 2020-05-03

 2020-05-04

 2020-05-05

 2020-05-06

 2020-05-07

 2020-05-08

 2020-05-09

 2020-05-10

 2020-05-11

 2020-05-12

 2020-05-13

 2020-05-14

 2020-05-15

 2020-05-16

 2020-05-17

 2020-05-18

 2020-05-19

 2020-05-20

 2020-05-21

 2020-05-22

 2020-05-23

 2020-05-24

 2020-05-25

(25 rows)
```

根据需要，可以将上述语句修改为按小时、分钟、秒等时间精度产生数据，与前面修改方法相同。