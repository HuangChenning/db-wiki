---
title: dblink
book: "数据库使用类"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/question/questionTwo1.html"
tags:
  - highgo
  - highgo-v9
  - faq-database-usage
---

#### 定义

Database Link (DBLink) 是数据库提供的一种跨数据库访问机制，允许用户在一个数据库中访问另一个数据库的对象（如表、视图、存储过程等），就像访问本地数据库一样。

核心特性：

- 透明访问远程数据库对象
- 支持 SELECT、INSERT、UPDATE、DELETE 等 DML 操作
- 支持公共(Public)和私有(Private)两种类型

#### 环境准备

- 安装瀚高V9版本数据库，本次使用hgdb-ee-9.0.1.000-build2412161753-68eb8a3-linux.x86\_64-RC.tar
- oracle版本使用Oracle Database 11g Enterprise Edition Release 11.2.0.1.0 - 64bit Production
- 创建扩展oracle\_fdw、oracle\_fdw
```sql
psql highgo highgo -p 5866
create database animal;
create database water;
psql animal system -p 1521
create user manager password 'Hello@1234';
create schema manager authorization manager;
psql water system -p 1521
create user watersuer password 'Hello1234';
create schema watersuer authorization watersuer;
```

#### 准备测试数据

```sql
psql animal manager -p 1521
create table dog(id serial,name varchar2(10));
insert into dog(name) values('大黄');
insert into dog(name) values('小黑');

psql water wateruser -p 1521
create table worker(id serial,name varchar2(10));
INSERT INTO worker(name) values('大壮'),('小壮');
select * FROM worker;
```

#### 赋权

```sql
grant create database link to public;
```

> 1. 将创建database的权限赋予普通用户（或public）

#### 基本语法

```sql
create database  link blink1 connect to dbName 
identified by dbPassword 
using '(DESCRIPTION =(ADDRESS =(PROTOCOL = TCP)(HOST = 192.168.1.106)(PORT = 1521))(CONNECT_DATA =(server = dedicated)(SERVICE_NAME = orcl)))';
with '***fdw';

--blink1 ： 表示dblink名字
--dbName ：表示 远程数据库的用户
--dbPassword：表示 远程数据库的密码
--HOST ： 表示远程数据库IP
--PORT ： 表示远程数据库端口
--SERVICE_NAME ： 远程数据库的实例名
--with :    使用的fdw（oracle_fdw/postgres_fdw）
```

#### 查看已有DBLink

```sql
select * from dba_db_links;
select * from ivorysql_dblink;
```

#### 用例

##### HG\_TO\_ORACLE

```sql
create public database link water_to_oracle 
connect to wateruser identified by "Hello1234" 
using '(description=(address=(protocol=tcp)(host=192.168.239.152)(port=1521))(connect_data=(server = dedicated)(service_name=orcl)))' 
with 'oracle_fdw';
```

###### 查看dblink

```sql
INSERT INTO NEWPRODUCTS@water_to_oracle values(1,'alibaba','shuopping');
DELETE FROM NEWPRODUCTS@water_to_oracle WHERE product_id = 1666;
UPDATE NEWPRODUCTS@water_to_oracle SET product_name = 'baidu' WHERE product_id = 1666;
SELECT * FROM NEWPRODUCTS@water_to_oracle;
```

###### 简化访问

```sql
CREATE VIEW newproducts AS SELECT * FROM NEWPRODUCTS@water_to_oracle;
SELECT * FROM newproducts;
```

##### HG\_TO\_HG

```sql
create public database link wateruser_to_manager 
connect to manager identified by "Hello@1234" 
using '(description=(address=(protocol=tcp)(host=192.168.239.130)(port=1521))
    (connect_data=(server = dedicated)(service_name=animal)))' 
with 'postgres_fdw';
```

###### 查询修改数据

```sql
SELECT * FROM dog@wateruser_to_manager;
SELECT * FROM manager.dog@wateruser_to_manager;
INSERT INTO manager.dog@wateruser_to_manager values(3,'大白');
DELETE FROM manager.dog@wateruser_to_manager WHERE id = 3;
UPDATE manager.dog@wateruser_to_manager SET name='大白' WHERE id = 2;
```

###### 删除dblink

```sql
drop public database link water_to_oracle;
drop public database link wateruser_to_manager;
```