---
title: "17、流复制备端错误40001"
book: "数据库使用类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/question/streams.html"
tags:
  - highgo
  - highgo-v45
  - faq-database-usage
---

## 流复制备端错误40001

## 1、问题描述

HGDB流复制备端多次报错如下：

```
2017-10-12 08:52:02.898 CST,"partyeducation","party_build_education",8639,"10.243.32.23:35889
",59deb5bc.21bf,2,"SELECT",2017-10-12 08:22:20 CST,33/645609,0,错误,40001,"由于与恢复操作冲突，正在取消语句命令","用户查询可能需要看到而必须被删除的行版本号",,,,,"select statistics0_.item_id as col_0_0_, statistics0_.user_id as col_1_0_, sum(statistics0_.statistics_value) as col_2_0_ from tf_f_statistics statistics0_ where (statistics0_.user_id in ($1 , $2 , $3 , $4 , $5 , $6 , $7 , $8 , $9 , $10 , $11 , $12)) and (statistics0_.item_id in ($13 , $14)) and statistics0_.DEL_FLAG='0' group by statistics0_.user_id , statistics0_.item_id",,,"PostgreSQL JDBC Driver"
```

当出现该报错信息时流复制备机查询业务无法访问（每次约3-5秒无法访问）。

## 2、问题原因

流复制备端在读取某业务表时，主端将该部分数据删除，进而导致备端查询报错。

> vacuum\_defer\_cleanup\_age (integer)  
> 指定VACUUM和HOT更新在清除死亡行版本之前，应该推迟多久（以事务数量计）。默认值是零个事务，表示死亡行版本将被尽可能快地清除，即当它们不再对任何打开的事务可见时尽快清除。在一个支持热后备服务器的主服务器上，你可能希望把这个参数设置为一个非零值，如第 26.5 节中所述。这允许后备机上的查询有更多时间来完成而不会由于先前的行清除产生冲突。但是，由于该值是用在主服务器上发生的写事务的数目衡量的，很难预测对后备机查询可用的附加时间到底是多少。这个参数只能在postgresql.conf文件中或在服务器命令行上设置。

你也可以考虑设置后备服务器上的hot\_standby\_feedback作为使用这个参数的一种替代方案。

这无法阻止已经达到old\_snapshot\_threshold 所指定年龄的死亡行被清除。

## 3、解决方案

在流复制备端修改如下参数：

```
highgo=# alter system set hot_standby_feedback = on;

ALTER SYSTEM
```

执行pg\_ctl reload后使修改参数生效：

```
[highgo@localhost ~]$ pg_ctl reload

server signaled
```