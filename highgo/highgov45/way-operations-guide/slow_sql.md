---
title: "16、HGDB如何查询慢SQL"
book: "运维指导类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/way/slow_sql.html"
tags:
  - highgo
  - highgo-v45
  - way-operations-guide
---

## HGDB如何查询慢SQL

## 1、设置数据库获取所有的SQL语句

修改配置文件postgresql.conf，设置以下参数

```
#开启日志记录
logging_collector = on
#设置日志输出格式，格式有stderr（默认）, csvlog , syslog
log_destination = 'csvlog’
#设置日志存放位置，下面设置表示日志存放在$PGDATA下hgdb_log日志中
log_directory = 'hgdb_log’
#设置日志截断
log_truncate_on_rotation = on
#设置日志的名称
log_filename = 'highgodb_%d.log’
#设置跟踪的SQL语句级别，级别包含none（默认，只记录出错信息）, ddl, mod, all
log_statement = all
#记录执行超过以下时间的SQL语句，单位毫秒
log_min_duration_statement = 5000
```

## 2、创建存储日志的表

使用psql或其他数据库客户端连接到瀚高数据库，执行以下建表语句。

```
CREATE TABLE hgdb_log
( log_timetimestamp(3) with time zone,
 user_nametext,
 database_nametext,
 process_idinteger,
 connection_fromtext,
 session_idtext,
 session_line_num bigint,
 command_tagtext,
 session_start_timetimestamp with time zone,
 virtual_transaction_idtext,
 transaction_id bigint,
 error_severitytext,
 sql_state_codetext,
 message text,
 detail text,
 hint text,
 internal_querytext,
 internal_query_posinteger,
 context text,
 query text,
 query_posinteger,
 location text,
 application_nametext,
 PRIMARY KEY (session_id, session_line_num)
);
```

## 3、将日志导入到表中

使用psql或其他数据库客户端连接到瀚高数据库，执行以下语句导入日志到表中。

```
--黑色字体部分修改为日志文件的绝对路径
COPY hgdb_log FROM '**/opt/HighGo4.3.4.7-see/data/hgdb_log/highgodb_20.csv**' WITH csv;
```

## 4、查询慢SQL

导入表中后，由于SQL语句的执行时间、SQL语句等信息均存放在message列中，在编写分析SQL时，需要使用字符处理函数分离相关信息，以下示例为按SQL执行时间由长到短进行排列。

```
--按执行时间由长到短排序
select log_time,database_name,user_name,application_name,substr(message, 7,8),message from hgdblog where message like '%执行时间%' order by substr(message, 7,8) desc
```