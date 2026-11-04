---
title: "12、如何开关数据库告警日志及修改日志级别"
book: "运维指导类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/way/alarm.html"
tags:
  - highgo
  - highgo-v45
  - way-operations-guide
---

## 如何开关数据库告警日志及修改日志级别

## 1、文档用途

本文旨在介绍如何开启和关闭数据库告警日志及修改日志级别。

## 2、详细信息

先提供一份通用告警日志参数设置：

打开数据库参数文件$PGDATA/postgresql.auto.conf，在文件末尾追加如下内容：

```
logging_collector = on

log_destination = 'csvlog'

log_directory = 'hgdb_log'

log_filename = 'highgodb_%d.log'

log_rotation_age = '1d'

log_rotation_size = 0

log_truncate_on_rotation = on

log_min_messages = 'WARNING'

log_statement = 'ddl'
```

然后重启数据库(确保非业务时段执行)。

```
pg_ctl restart
```

这样配置后，将会达到如下配置目标：

1. 开启数据库告警日志记录；
2. 产生的日志文件位于data目录下的hgdb\_log中；
3. 日志文件格式为csv；
4. 文件名以highgodb为前缀；
5. 日志大小无上限，按日保留，循环覆盖；
6. 消息级别在warning及以上的进行记录，sql语句在error级别及以上的被记录；
7. 所有ddl语句被记录。

### 2.1 开启和关闭数据库告警日志的方法

#### (1) 查询数据库告警日志是否开启

连接数据库执行show logging\_collector;

返回结果是on则代表开启。off代表关闭。

#### (2) 开启数据库告警日志方法

打开数据库参数文件$PGDATA/postgresql.auto.conf，在文件末尾追加如下内容：

```
logging_collector = on

log_directory = 'hgdb_log'
```

然后重启数据库(确保非业务时段执行)。

```
pg_ctl restart
```

#### (3) 关闭数据库告警日志方法

打开数据库参数文件$PGDATA/postgresql.auto.conf，在文件末尾追加如下内容：

```
logging_collector = off
```

然后重启数据库(确保非业务时段执行)。

```
pg_ctl restart
```

### 2.2.修改告警日志级别

#### (1)查询告警日志级别

连接数据库执行

```
show log_min_messages;

show log_statement;
```

#### (2)修改告警日志级别

##### 1) log\_min\_messages

控制哪些消息级别被写入到服务器日志。有效值是DEBUG5、DEBUG4、DEBUG3、DEBUG2、DEBUG1、INFO、NOTICE、WARNING、ERROR、LOG、FATAL和 PANIC。每个级别都包括其后的所有级别。级别越靠后，被记录的消息越少。

级别介绍：

DEBUG1..DEBUG5：极端情况下提供连续的更详细的信息。

INFO：提供用户隐式要求的信息，例如来自VACUUM VERBOSE的输出。

NOTICE：提供可能对用户有用的信息，例如长标识符截断提示。

WARNING：提供可能出现的问题的警告，例如在一个事务块外COMMIT。

ERROR：报告一个导致当前命令中断的错误。

LOG：报告管理员一般需要的信息，例如检查点活动。

FATAL：报告一个导致当前会话中断的错误。

PANIC：报告一个导致所有数据库会话中断的错误。

##### 2) log\_statement

控制哪些SQL语句被记录。有效值是none(off)、ddl、mod和all（所有语句）。ddl记录所有数据定义语句，例如CREATE、ALTER和 DROP语句。mod记录所有ddl语句，外加数据修改语句例如INSERT, UPDATE、DELETE、TRUNCATE, 和COPY FROM。all记录包括select在内的所有语句。