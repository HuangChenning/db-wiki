---
title: "闪回查询和闪回表"
book: "Oracle兼容性"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/compatibility/compOracle30.html"
tags:
  - highgo
  - highgo-v9
  - compatibility-oracle
---

## 闪回查询和闪回表

闪回查询和闪回表功能，能够使用户在秒级时间内恢复误操作前的数据，提升数据库的容错能力和数据恢复效率。具体功能包括：

- 基于时间戳的闪回查询功能，允许用户查询指定历史时刻的数据。
- 闪回表功能，允许用户将表恢复到指定时间点的状态。允许用户将表恢复到DROP/TRUNCATE操作前的状态。

闪回查询和闪回表到某时间点的功能需要获取事务与时间的对应关系，因此需要提前开启数据库参数track\_commit\_timestamp。

闪回查询和闪回表到某时间点的功能依赖于历史数据的保留，因此需要合理设置vacuum\_defer\_cleanup\_age等参数，以确保有足够的历史数据可供恢复。

说明：

该功能在V9.0.5及以后的版本中支持。

## 闪回查询

使用该功能需要提前开启数据库自带参数track\_commit\_timestamp，设置参数vacuum\_defer\_cleanup\_age（设置保留旧元组的事务数量）到合适值。

语法：

SELECT \[ \* | expression \] \[ FROM from\_item \[AS OF time\_expr \] \]

说明：

- time\_expr可以为timestamptz常量字符串，或返回结果为timestamptz类型的表达式。

示例1：使用常量

SELECT \* FROM foo AS OF ‘2025-02-10 12:00:00+08’;

\-- 创建表并插入数据

CREATE TABLE test\_employees (id NUMBER, name VARCHAR2(50), salary  
NUMBER);

INSERT INTO test\_employees VALUES (1, '张三', 5000);

\-- 查看现在的时间

SELECT TO\_CHAR(SYSTIMESTAMP, 'YYYY-MM-DD HH24:MI:SS') FROM DUAL;

to\_char

\---------------------

2025-09-02 10:22:03

(1 行记录)

\-- 更新数据

UPDATE test\_employees SET salary = 6000 WHERE id = 1;

\-- 使用闪回查询，查看update之前的数据

SELECT \* FROM test\_employees

AS OF ' 2025-09-02 10:22:03'

WHERE id = 1;

示例2：使用表达式

\-- 上述闪回查询语句可改写为表达式格式

SELECT \* FROM test\_employees

AS OF NOW() - INTERVAL '12' minute;

## 闪回表

闪回表功能支持将表恢复到指定的时间点，支持将表恢复到DROP操作之前的状态，支持将表恢复到TRUNCATE操作之前的状态。后两者需要依赖数据库的回收站功能。回收站功能可通过设置 ivorysql.enable\_recycle\_bin 启用和关闭。

通过系统表pg\_recyclebin可查看回收对象的相关信息。

### 闪回表数据到指定时间点

使用该功能需要提前开启数据库自带参数track\_commit\_timestamp，设置参数vacuum\_defer\_cleanup\_age（设置保留旧元组的事务数量）到合适值。

语法：

FLASHBACK TABLE table\_name TO TIMESTAMP time\_expr;

示例：

\-- 打开回收站

alter session set ivorysql.enable\_recycle\_bin to on;

\-- 创建表并插入数据

drop table test\_employees;

CREATE TABLE test\_employees (id NUMBER, name VARCHAR2(50), salary  
NUMBER);

INSERT INTO test\_employees VALUES (1, '张三', 5000);

\-- 查看现在的时间

SELECT TO\_CHAR(SYSTIMESTAMP, 'YYYY-MM-DD HH24:MI:SS') FROM DUAL;

to\_char

\---------------------

2025-09-02 10:40:52

(1 行记录)

\-- 更新数据

UPDATE test\_employees SET salary = 6000 WHERE id = 1;

\-- 闪回表到update之前的时间

FLASHBACK TABLE test\_employees TO TIMESTAMP '2025-09-02 10:40:52';

### 闪回表到DROP操作前

使用该功能可以将表闪回到DROP操作前。如果在当前 SCHEMA  
下已经存在同名的表，则闪回失败，需要使用 RENAME TO  
选项指定一个新的表名。

需要开启参数ivorysql.enable\_recycle\_bin。

语法：

FLASHBACK TABLE table\_name TO BEFORE DROP \[RENAME TO new\_tablename\];

示例：

\-- 打开回收站

alter session set ivorysql.enable\_recycle\_bin to on;

\-- 创建表并插入数据

drop table test\_employees;

CREATE TABLE test\_employees (id NUMBER, name VARCHAR2(50), salary  
NUMBER);

INSERT INTO test\_employees VALUES (1, '张三', 5000);

\-- 删除表

DROP TABLE test\_employees;

\-- 查看表数据

select \* from test\_employees;

\-- 报错如下，表不存在：

ERROR: relation "test\_employees" does not exist

\-- 将表闪回到删除前的状态

FLASHBACK TABLE test\_employees TO BEFORE DROP;

\-- 再次查看表数据

select \* from test\_employees;

### 闪回表到TRUNCATE操作前

使用该功能需要开启参数ivorysql.enable\_recycle\_bin。

语法：

FLASHBACK TABLE table\_name TO BEFORE TRUNCATE;

示例：

\-- 打开回收站

alter session set ivorysql.enable\_recycle\_bin to on;

\-- 创建表并插入数据

drop table test\_employees;

CREATE TABLE test\_employees (id NUMBER, name VARCHAR2(50), salary  
NUMBER);

INSERT INTO test\_employees VALUES (1, '张三', 5000);

\-- truncate表

TRUNCATE TABLE test\_employees;

\-- 查看表，无数据

highgo=# select \* from test\_employees;

id | name | salary

\----+------+--------

(0 行记录)

\-- 执行闪回

FLASHBACK TABLE test\_employees TO BEFORE TRUNCATE;

\-- 再次查看表，可查看到数据

select \* from test\_employees;

### PURGE清理回收站

当参数ivorysql.enable\_recycle\_bin设置为ON（默认OFF），将为该数据库开启回收站功能。回收站是一个逻辑容器，用于存储被DROP或TRUNCATE的表及其相关对象（toast表、索引）。当用户执行DROP TABLE命令时，表并没有被立即删除，而是被重命名并移动到回收站中。当用户执行FLASHBACK TABLE... TO BEFORE DROP或者FLASHBACK TABLE... TO BEFORE TRUNCATE时，实际上是从回收站中将对象还原。如果回收站被清理，执行上述操作将失败。

为了释放回收站占用的存储资源，可使用PURGE命令清理回收站。

语法：

PURGE \[RECYCLEBIN | TABLE table\_name\];

说明：

- 执行PURGE TABLE  
	table\_name，可清除指定表关联的对象，每次执行清理对应表最旧的一个版本的垃圾数据；
- 执行PURGE RECYCLEBIN，可清空对应数据库的整个回收站；
- table\_name必须是表的原始名称；
- 需使用超级用户或者具有sysdba\_role角色的用户执行PURGE  
	RECYCLEBIN命令。

示例：

PURGE TABLE test\_employees;

PURGE RECYCLEBIN;

DROP TABLE test\_employees PURGE;

### 使用限制

闪回表功能具有以下使用限制：

- 闪回表到DROP操作之前仅支持restrict模式的操作，回收对象也仅支持表本身及依赖于它的toast表、索引。
- 闪回表到TRUNCATE操作之前仅支持restrict模式的操作，回收对象也仅支持表本身和依赖于它的toast表。不支持对trigger的处理，不支持重置sequence的情况。