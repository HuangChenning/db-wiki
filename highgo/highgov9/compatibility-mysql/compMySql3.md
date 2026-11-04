---
title: "语法"
book: "MySQL兼容性"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/compatibility/compMySql3.html"
tags:
  - highgo
  - highgo-v9
  - compatibility-mysql
---

## 语法

## USE

### 描述

切换当前会话的默认schema，用于后续的语句。指定的schema必须存在，否则报错。指定的schema会一直作为默认模式，直到会话结束或另一个USE语句被执行。

### 示例

USE highgo;

## CREATE

### CREATE TABLE

#### 描述

CREATE TABLE用于创建一个具有指定名称的表。

CREATE TABLE语法从V9.0.5开始支持。

#### 示例

CREATE TABLE t1 (

id INT NOT NULL AUTO\_INCREMENT,

PRIMARY KEY (id),

Name VARCHAR(50)

) COMMENT 'some comments here';

CREATE TABLE t2(

id INT,

Name VARCHAR(50),

INDEX idx\_name(name)

);

CREATE TABLE t3(

c CHAR(20) CHARSET utf8 COLLATE utf8\_bin

);

### CREATE INDEX

#### 描述

CREATE INDEX用于为已存在的表添加索引。

CREATE INDEX语法从V9.0.5开始支持。

#### 示例

\## 创建一张表

CREATE TABLE IF NOT EXISTS test\_table (

id INT,

col1 VARCHAR(50),

col2 INT,

col3 VARCHAR(100)

);

\## 为该表添加一个单列普通索引

CREATE INDEX idx\_test ON test\_table (col1);

\## 查看索引信息

SHOW INDEX FROM test\_table WHERE Key\_name = 'idx\_test';

## INSERT

### 描述

INSERT 用于向现有表中插入新行。

### 示例

CREATE TABLE users (

id INT AUTO\_INCREMENT PRIMARY KEY,

name VARCHAR(100)

);

INSERT INTO users (name) VALUES ('Alice'),('Bob');

## DELETE

### 描述

DELETE语句用于从表中删除行，包括单表删除和多表删除。

### 示例

##单表删除

CREATE TABLE users (

id INT AUTO\_INCREMENT PRIMARY KEY,

name VARCHAR(100)

);

INSERT INTO users (name) VALUES ('Alice'),('Bob');

DELETE FROM users WHERE name = 'Bob';

##多表删除

CREATE TABLE td1(a int);

CREATE TABLE td2(a int,b varchar(20));

INSERT INTO td1(a) VALUES (1),(2),(3),(4),(5);

INSERT INTO td2(a,b) VALUES  
(1,'a'),(2,'b'),(3,'c'),(4,'d'),(6,'f');

DELETE FROM a1,a2 USING td1 AS a1, td2 AS a2 WHERE a1.a = a2.a;

## UPDATE

### 描述

UPDATE语句用于更新表中的行，包括单表更新和多表更新。对于单表更新，UPDATE语句用新值更新指定表中现有行的列。对于多表更新，UPDATE更新指定的每个表中满足条件的行。

### 示例

##单表更新

CREATE TABLE tu ( a INTEGER, b INTEGER, c INTEGER, d INTEGER);

INSERT INTO tu (a,b,c,d) VALUES (1, 1, 1, 4), (2, 2, 2, 5), (2, 3, 4,  
7), (3, 3, 3, 9), (4, 4, 4, 0), (5, 5, 5, 1), (5, 6, 7, 3), (5, 7, 9,  
9);

UPDATE tu SET c = 72 WHERE a = 2 ORDER BY b ASC LIMIT 1;

##多表更新

create table t1(a int,b int);

create table t2(c int,d int);

insert into t1 values(1,2),(2,3);

insert into t2 values(1,2),(2,3);

update t1,t2 set t1.a = t2.d,t2.c = 12

where t1.a = t2.c;

## REPLACE

### 描述

REPLACE的工作方式与INSERT几乎完全相同，不同之处在于，如果表中的旧行与PRIMARY KEY或UNIQUE索引的新行具有相同的值，则在插入新行之前会删除旧行。REPLACE 只有在表中有主键或唯一索引时才有意义。否则，它就等同于 INSERT，因为没有索引可以用来判断新行是否与已有行重复。

### 示例

CREATE TABLE tr\_with\_primary\_key (

id INT PRIMARY KEY,

name VARCHAR(50)

);

INSERT INTO tr\_with\_primary\_key (id, name) VALUES (1, 'Alice');

REPLACE INTO tr\_with\_primary\_key (id, name) VALUES (1, 'Bob');

CREATE TABLE tr\_with\_unique\_index (

id INT,

name VARCHAR(50),

UNIQUE (id)

);

INSERT INTO tr\_with\_unique\_index (id, name) VALUES (1, 'Alice');

REPLACE INTO tr\_with\_unique\_index (id, name) VALUES (2, 'Bob');

## SELECT

### 描述

SELECT用于从一个或多个表中检索选定的行，也可以用于检索不引用任何表的计算结果。在没有引用任何表的情况下，可以指定DUAL作为虚拟表名。

SELECT语法从V9.0.5开始支持。

### 示例

SELECT 1+1;

SELECT 1+1 FROM dual;

select \* from tr\_with\_unique\_index;

## SHOW

### SHOW CHARACTER SET

#### 描述

SHOW CHARACTER SET（SHOW CHARSET）语句显示所有可用的字符集。

#### 示例

SHOW CHARACTER SET LIKE 'latin%';

### SHOW COLLATION

#### 描述

SHOW  
COLLATION语句列出服务器支持的排序规则，默认情况下列出所有可用的排序规则。

#### 示例

SHOW COLLATION WHERE Charset = 'latin1';

### SHOW CREATE DATABASE

#### 描述

显示创建数据库时的CREATE DATABASE语句。SHOW CREATE SCHEMA是SHOW CREATE DATABASE的同义词。

如果SHOW语句包含IF NOT EXISTS子句，输出中也会包含该子句，而与原本的CREATE DATABASE语句是否包含IF NOT EXISTS子句无关。

SHOW CREATE DATABASE根据系统变量sql\_quote\_show\_create的值来确定是否使用引号来引用数据库名。

SHOW CREATE DATABASE语法从V9.0.5开始支持。

#### 示例

SHOW CREATE DATABASE highgo;

SHOW CREATE SCHEMA highgo;

SHOW CREATE DATABASE IF NOT EXISTS highgo;

### SHOW DATABASES

#### 描述

列出服务器主机上的数据库。SHOW SCHEMAS是SHOW DATABASES的同义词。

SHOW DATABASE语法从V9.0.5开始支持。

#### 示例

SHOW DATABASES;

SHOW SCHEMAS;

### SHOW TRIGGERS

#### 描述

列出当前为数据库中的表（默认数据库，除非给定了FROM子句）定义的触发器。LIKE子句表示要匹配的表名，而不是触发器名。

SHOW TRIGGERS语法从V9.0.5开始支持。

#### 示例

SHOW TRIGGERS like 'ins\_sum';

### SHOW CREATE TABLE

#### 描述

显示创建指定表的CREATE TABLE语句。此语句也适用于视图，与SHOW CREATE VIEW效果相同。

SHOW CREATE TABLE根据sql\_quote\_show\_create选项的值确定是否使用引号来引用表和列的名称。

SHOW CREATE TABLE语法从V9.0.5开始支持。

#### 示例

SHOW CREATE TABLE sales;

SHOW CREATE TABLE vsales; ##vsales是一个视图

### SHOW CREATE VIEW

#### 描述

显示创建指定视图的CREATE VIEW语句。

SHOW CREATE VIEW语法从V9.0.5开始支持。

#### 示例

SHOW CREATE VIEW vsales;

### SHOW COLUMNS

#### 描述

显示给定表中列的信息，也适用于视图。

SHOW COLUMNS语法从V9.0.5开始支持。

#### 示例

SHOW COLUMNS FROM sales;

SHOW COLUMNS FROM vsales; ##vsales是一个视图

### SHOW TABLES

#### 描述

列出指定数据库中的非临时表和视图。

SHOW TABLES语法从V9.0.5开始支持。

#### 示例

SHOW FULL TABLES LIKE 'my%';

### SHOW TABLE STATUS

#### 描述

列出每个非临时表的详细信息。

SHOW TABLE STATUS语法从V9.0.5开始支持。

#### 示例

SHOW TABLE STATUS;

### SHOW INDEX

#### 描述

返回表的索引信息。

SHOW INDEX语法从V9.0.5开始支持。

#### 示例

SHOW INDEX FROM tr\_with\_unique\_index;

### SHOW VARIABLES

#### 描述

显示MySQL兼容相关的系统变量的值。

SHOW VARIABLES语法从V9.0.5开始支持。

#### 示例

SHOW GLOBAL VARIABLES LIKE 'mysql%';

## DESCRIBE | DESC

### 描述

显示给定表中列的信息，也适用于视图。

在表结构查询的语境中，DESC是DESCRIBE的缩写。

DESCRIBE是SHOW COLUMNS的快捷方式。DESCRIBE tbl\_name显示表中所有列的信息，如果提供了列名，会显示指定列的信息；如果提供了模式字符串，仅显示列名与字符串匹配的列的信息。

DESCRIBE | DESC语法从V9.0.5开始支持。

### 示例

DESCRIBE tr\_with\_unique\_index;

DESC tr\_with\_unique\_index id;

## RENAME

### RENAME USER

#### 描述

对一个或多个用户进行重命名。

执行RENAME USER进行多个重命名操作时，如果其中某个用户名重命名失败，则之前重命名操作回滚，后面的重命名操作不执行。

RENAME USER语法从V9.0.5开始支持。

#### 示例

RENAME USER u1 to u2;

RENAME USER u1 to u2, u2 to u3;

### RENAME TABLE

#### 描述

将一个或者多个数据表进行重命名。可以使用RENAME TABLE将数据表从一个数据库移动到另一个数据库（schema）。

当执行RENAME TABLE进行多个重命名操作时，如果其中某个表名重命名失败，则整条RENAME TABLE所有的重命名表名操作都会失败，之前的重命名操作都会回滚，后面的重命名操作不会执行。

RENAME TABLE语法从V9.0.5开始支持。

#### 示例

RENAME TABLE test to testr;

RENAME TABLE t to t1, t1 to t2;

RENAME TABLE highgo.td1 to mysql.td1;

## ALTER

### ALTER TABLE RENAME

#### 描述

ALTER TABLE命令RENAME选项支持修改表名和索引名。

该语法从V9.0.5开始支持。

#### 示例

ALTER TABLE t2 RENAME TO t3;

ALTER TABLE t3 RENAME AS t4;

ALTER TABLE tr\_with\_unique\_index RENAME INDEX  
tr\_with\_unique\_index\_id\_key TO my\_new\_unique\_index;

## SET

### 描述

SET语法用于变量赋值，可以为影响服务器或客户端操作的不同类型的变量赋值：

- 用户定义的变量；
- 存储过程和函数参数，以及存储程序局部变量；
- 系统变量，包括全局系统变量和会话系统变量。其中，对GLOBAL关键字和 @@GLOBAL. 限定符目前仅做语法支持。

另外，在建立连接之后，客户端可以更改当前会话的字符集和排序规则系统变量。这些变量可以通过SET语句单独更改，但有两个更便捷的语句可以将与连接相关的字符集系统变量作为一组进行更改，这就是SET CHARACTER SET和SET NAMES。目前SET CHARACTER SET和SET NAMES均仅支持语法，暂不实现功能。

瀚高数据库管理系统V9.0使用mysql.at\_or\_atat参数控制是否启用自定义变量功能。

SET语法从V9.0.5开始支持。

### 示例

SET GLOBAL lower\_case\_table\_names = 0;

SET CHARACTER SET 'gb18030';

SET NAMES 'utf8';

SET mysql.at\_or\_atat = on;

SET @name = 43;

SET @a = @a + 1;

SET @@GLOBAL.lower\_case\_table\_names = 0;

## DO

### 描述

DO语句执行表达式，但不返回任何结果。表达式包括一般表达式和函数等。

在大多数情况下，DO是SELECT expr,...的简写形式。因为DO只执行表达式，所以不能在所有情况下替代SELECT语句（例如引用表的操作），但是DO语句都可以用SELECT语句替代。

瀚高数据库管理系统V9.0使用mysql.use\_mysql\_do参数控制选择执行MySQL的DO语法或者PG的DO语法。