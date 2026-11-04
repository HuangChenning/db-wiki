---
title: "同义词"
book: "Oracle兼容性"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/compatibility/compOracle31.html"
tags:
  - highgo
  - highgo-v9
  - compatibility-oracle
---

## 同义词

同义词（synonym） 是数据库对象的一个别名。它本质上是一个指向另一个数据库对象（如表、视图、序列、存储过程、函数、包，甚至是另一个同义词）的名称映射，具有以下作用：

● 简化对象访问：隐藏复杂对象名或路径；

● 位置透明性：屏蔽对象物理位置变化；

● 权限隔离：通过别名控制访问权限。

同义词分为公有同义词和私有同义词两种。其中公有同义词为所有用户所有，数据库中的每个用户都可以访问它；私有同义词为特定用户所有，仅在该用户下可见。用户可通过ALL\_SYNONYMS、DBA\_SYNONYMS和USER\_SYNONYMS视图查看创建的同义词。

**说明：**

该功能在V9.0.5及以后的版本中支持。

## 创建同义词

### 说明

支持为以下对象创建同义词：

● 表

● 视图和物化视图

● 其他同义词

● 序列

● PL/iSQL存储过程

● PL/iSQL函数

● PL/iSQL包

● 自定义类型（通过CREATE TYPE创建的类型）

**语法：**

$$
.\Oracle兼容性手册-images\media\image126.jpg
$$

**参数说明：**

| 参数 | 说明 |
| --- | --- |
| OR REPLACE | 覆盖现有同义词定义（若存在），或创建新的同义词（若不存在）；如果没有指定OR REPLACE， 而存在同名的同义词，创建报错。注意: 私有同义词不会通过OR REPLACE替换为公共同义词，反之公共同义词不会通过OR REPLACE替换为私有同义词。 |
| EDITIONABLE\|NONEDITIONABLE | 指定对象是editionable还是noneditionable。对于私有同义词，默认值是EDITIONABLE。对于公共同义词，默认值是NONEDITIONABLE。（仅语法支持） |
| PUBLIC | 创建公共同义词（所有用户可访问），否则为私有同义词（如果没有指定模式，创建在当前模式下）。公共同义词创建在PUBLIC模式下。 |
| schema | 指定同义词的所属schema，如果没有指定模式，默认为当前schema。如果创建的是公共同义词，不能指定schema。 |
| synonym | 同义词的名称。 |
| SHARING | 此子句仅在应用程序根中创建同义词时应用。创建同义词后，不能更改同义词的该属性。（仅语法支持） |
| schema.object | 目标对象的schema和名称。支持表、视图、物化视图、其他同义词、序列、PL/iSQL存储过程、PL/iSQL函数、PL/iSQL包、通过CREATE TYPE创建的自定义类型。 |
| dblink | 通过数据库链接引用远程对象的dblink名称。如果省略dblink，假定该对象位于本地数据库上。 |

### 限制和差异

**目前同义词的使用有如下限制：**

● 可以为一个不存在的对象创建同义词，但是在使用同义词时会报错。

● 不能对具有任何表依赖或类型依赖的同义词使用OR REPLACE子句。

● 在创建公共同义词时，不能指定模式名也不能引用dblink对象。

● 不建议创建与现有模式同名的公共同义词。

● 公共同义词可以和系统对象同名。但是查找优先级是先查找系统对象名，然后是公共同义词。

● 私有同义词不能和同一模式中其他私有同义词同名，但不同模式下可以有同名的私有同义词。私有同义词和公共同义词可以同名。私有同义词可以和其他对象同名。

● 如果当前用户对指定的对象没有权限，执行CREATE SYNONYM也是成功的，在引用同义词时会因为权限问题报错，如果进行了对象授权操作后，在引用同义词不会报错。

**目前V9与oracle中的同义词具有以下差异：**

● 如果目标对象被更改或删除， Oracle同义词将失效，可以通过查询ALL\_、DBA\_和USER\_OBJECTS数据字典视图的STATUS列来确定同义词是否有效。但是在V9数据库中暂时不支持同义词的STATUS列状态，但是可以通过直接引用同义词体现出来，您可以这么认为：引用同义词时，如果目标对象被更改或删除，直接报错。

● V9私有同义词可以其他对象同名，但是Oracle私有同义词不可以其他对象同名。这属于pg和Oracle差异，Oracle中即使不同类型对象（比如函数、表等对象），也不能同名。但是pg设计中没有这样的限制，相同类型对象不允许重名，但是不同类型对象可以重名。

### 示例

**示例1：创建同名的同义词**

```sql
create table test1(id int); 
create table test2(id int); 
create table test3(id int); 
insert into test1 values(1);
insert into test2 values(2);
insert into test3 values(3);
 
--同义词不能和当前模式下引用对象同名
create synonym test1 for test1;  --报错：ERROR:  cannot create a synonym with same as object
create synonym test_syn for test2;
create public synonym test_syn for test3;

--私有和公共同义词同名了，先查找私有同义词。
select *from test_syn;   --查询的是私有同义词，输出结果是2

--公共同义词可以和当前模式下对象同名，查找优先级是先查找对象，然后是公共同义词
create public synonym test1 for test2;
SQL> select *from test1;
  ID
----------
    1
```

**示例2：创建私有同义词指向本地表t1**

```sql
--1. 管理员登录创建新用户
CREATE USER u1;
ALTER USER u1 PASSWORD 'highgo';

--2. 创建同义词。通过同义词查找表t1。
--使用u1用户登录
CREATE TABLE t1(id int, name varchar(20));
--创建同义词
CREATE OR REPLACE SYNONYM SYN1 FOR t1; 
SELECT * FROM SYN1;
```

**示例3：创建公共同义词指向本地表t2**

```sql
--1. 管理员登录创建新用户
CREATE USER u1;
ALTER USER u1 PASSWORD 'highgo';

--2. 创建同义词。通过同义词查找表t1。
--使用u1用户登录
CREATE TABLE t2(id int, name varchar(20));

--创建同义词
CREATE OR REPLACE PUBLIC SYNONYM SYN2 FOR t2; 
SELECT * FROM SYN2;
```

示例4：跨schema，引用模式s1下的表

```sql
CREATE SCHEMA s1;
CREATE TABLE s1.t3(id int, name varchar(20));
CREATE SYNONYM syn3 FOR s1.t3;
```

## 引用同义词

同义词的使用方式和对象的使用方式完全相同。如果当前用户对指定的对象没有权限，执行CREATE SYNONYM也是成功的。只要赋予对象权限，就可以使用其他用户的私有同义词。支持在指定的DML和DDL语句中引用同义词。

### DML语句中引用同义词

支持在以下DML语句中引用同义词：

● SELECT

● INSERT

● UPDATE

● DELETE

● FLASHBACK TABLE

● EXPLAIN

● LOCK TABLE

● MERGE

● CALL

#### 示例

**示例1：SELECT、INSERT、UPDATE、DELETE语句中引用同义词**

```sql
CREATE TABLE t1(id int, name varchar(20));
CREATE OR REPLACE SYNONYM syn1 FOR t1;
INSERT INTO syn1 VALUES(1, 'a');
INSERT INTO syn1 VALUES(2, 'b');
UPDATE syn1 SET id = 3 WHERE id = 1;
DELETE syn1 WHERE id = 2;
SELECT * FROM syn1;
DROP SYNONYM syn1;
DROP TABLE t1;
```

**示例2：FLASHBACK TABLE、EXPLAIN语句中引用同义词**

```sql
CREATE TABLE t1(id int, name varchar(20));
CREATE OR REPLACE SYNONYM syn1 FOR t1;
FLASHBACK TABLE syn1
 TO TIMESTAMP (SYSTIMESTAMP - INTERVAL '1' minute);

EXPLAIN SELECT * FROM syn1;
```

**示例3：LOCK TABLE语句中引用同义词**

```sql
CREATE TABLE t1(id int, name varchar(20));
CREATE OR REPLACE SYNONYM syn1 FOR t1;
BEGIN WORK;
LOCK TABLE syn1 IN SHARE MODE NOWAIT;
INSERT INTO syn1 VALUES(0, 'new');
COMMIT WORK;
SELECT * FROM syn1
DROP SYNONYM syn1;
DROP TABLE t1;
```

**示例4：MERGE语句中引用同义词**

```sql
CREATE TABLE people_source ( 
 person_id  INTEGER NOT NULL PRIMARY KEY, 
 first_name VARCHAR(20) NOT NULL, 
 last_name  VARCHAR(20) NOT NULL, 
 title    VARCHAR(10) NOT NULL 
);

CREATE TABLE people_target ( 
 person_id  INTEGER NOT NULL PRIMARY KEY, 
 first_name VARCHAR(20) NOT NULL, 
 last_name  VARCHAR(20) NOT NULL, 
 title    VARCHAR(10) NOT NULL 
);

INSERT INTO people_target VALUES (1, 'John', 'Smith', 'Mr');
INSERT INTO people_target VALUES (2, 'alice', 'jones', 'Mrs');
INSERT INTO people_target VALUES (3, 'tony', 'james', 'Mr');
INSERT INTO people_source VALUES (2, 'Alice', 'Jones', 'Mrs.');
INSERT INTO people_source VALUES (3, 'Jane', 'Doe', 'Miss');
INSERT INTO people_source VALUES (4, 'Dave', 'Brown', 'Mr');
 
CREATE OR REPLACE SYNONYM syn1 FOR people_source;
CREATE OR REPLACE SYNONYM syn2 FOR people_target;

MERGE INTO syn2 pt 
USING syn1 ps
ON (pt.person_id = ps.person_id)
WHEN MATCHED THEN UPDATE
  SET pt.first_name = ps.first_name,
    pt.last_name = ps.last_name,
    pt.title = ps.title;
DROP SYNONYM syn1;
DROP SYNONYM syn2;
DROP TABLE people_source;
DROP TABLE people_target;
```

**示例5：CALL语句中引用同义词**

```sql
CREATE TABLE tab(a int);
CREATE OR REPLACE PROCEDURE insert_data(a int) AS
BEGIN
  INSERT INTO tab VALUES (a);
END;

CREATE OR REPLACE SYNONYM synprod FOR insert_data;
CALL synprod(3);
DROP PROCEDURE insert_data;
DROP SYNONYM synprod;
DROP TABLE tab;
```

### DDL语句中引用同义词

支持在以下DDL语句中引用同义词：

● GRANT

● REVOKE

● COMMENT

#### 示例

**示例1：GRANT、REVOKE语句中引用同义词**

```sql
CREATE TABLE tab(id int, name varchar(20));
CREATE SYNONYM syntab FOR tab;
GRANT SELECT ON syntab TO u1;
REVOKE SELECT ON syntab FROM u1;
```

**示例2：COMMENT语句中引用同义词**

```sql
CREATE TABLE tab(id int, name varchar(20));
CREATE SYNONYM syntab FOR tab;
COMMENT ON TABLE syntab IS 'Employee data';
```

### 查找同义词规则

解析对象的顺序，首先是查看模式内是否存在该对象，然后再查看模式内的私有同义词，最后才是公共同义词。

例如，用户OE和SH在他们的模式下都有一个表customer，管理员为OE模式下的customer表创建了一个公共同义词customer\_syn，管理员为SH模式下的customer表创建了一个私有同义词customer\_syn，如果用户SH查询：SELECT COUNT(*) FROM customer，则此时返回的结果为SH.CUSTOMER下的行数，而在非SH模式下查询：SELECT COUNT(*) FROM customer返回的结果为 OE.CUSTOMER表的行数。

如果对象、私有同义词、公共同义词这三者都重名了，查找顺序也是：先找对象，然后找模式内私有同义词，然后是公共同义词。

如果私有同义词与系统对象同名，在不加模式名前缀调用时，系统函数优先级比私有同义词高、系统包和系统过程的优先级比私有同义词低。

#### 示例

**示例1：对象、私有同义词、公共同义词三者都重名**

```sql
create table test1(id int); 
create table test2(id int); 
create table test3(id int); 
insert into test1 values(1);
insert into test2 values(2);
insert into test3 values(3);

create synonym test1 for test2;
create public synonym test1 for test3;

select *from test1;   --查询的是对象，输出结果是1
SQL> select *from test1;
  ID
----------
    1
```

**示例2：系统函数和同义词重名**

```sql
SELECT ABS(1) FROM DUAL;  --返回结果1

--创建一个函数f1
CREATE FUNCTION f1(a int) RETURN NUMBER AS
BEGIN
RETURN a + 1;
END;

--创建和系统函数abs同名的同义词
CREATE SYNONYM abs FOR f1;

--创建和系统函数同名的同义词后，返回结果是1  
SELECT ABS(1) FROM DUAL;
```

### 同义词成环检测

在数据库中，同义词成环（Synonym Circular Reference）是指多个同义词（Synonym）之间通过互相引用形成循环依赖链。

当尝试访问这类同义词时，会因为无法解析到最终的实际对象（如表、视图等）而抛出错误。

#### 示例

```sql
--创建 SYN_A，指向 SYN_B
CREATE SYNONYM SYN_A FOR SYN_B;
 
-- 创建 SYN_B，指向 SYN_A
CREATE SYNONYM SYN_B FOR SYN_A;

--引用同义词的时候才会报错： looping chain of synonyms
SELECT * FROM SYN_A;
```

## 更改同义词

### 说明

使用ALTER SYNONYM 修改现有同义词。主要功能是重新编译同义词。当同义词所引用的对象（如表、视图等）发生结构变化（如添加或删除列、删除对象）时，可以使用 ALTER SYNONYM 重新编译同义词。

**ALTER SYNONYM语法：**

$$
.\Oracle兼容性手册-images\media\img127.jpg
$$

**参数说明：**

| 参数 | 说明 |
| --- | --- |
| PUBLIC | 如果是公共同义词，则指定PUBLIC。不能使用此子句将公共同义词更改为私有同义词，反之亦然。 |
| schema | 同义词所属schema，如果省略schema，假定同义词在当前模式下。 |
| synonym | 指定要更改的同义词的名称。 |
| EDITIONABLE \| NONEDITIONABLE | 使用这些子句指定同义词是EDITIONABLE还是NONEDITIONABLE （仅语法支持） |
| COMPILE | 使用此子句编译同义词。 |

### 限制

**目前更改同义词有以下限制：**

● 要执行更改同义词命令，您必须是同义词的所有者，并对同义词所在的 schema 具有 USAGE 特权。

● 不能为公共同义词指定EDITIONABLE或NONEDITIONABLE子句。

### 示例

```sql
drop table tab;
create table tab(a int, b int);
create synonym syntab for tab;
create public synonym syntab2 for tab;

alter table tab drop column b;
alter synonym syntab COMPILE;
alter public synonym syntab2 COMPILE;
```

## 删除同义词

### 说明

使用DROP SYNONYM 删除数据库中的同义词，或者通过删除和重新创建同义词来更改同义词的定义。可删除私有同义词或公共同义词。

DROP SYNONYM 是管理同义词生命周期的关键操作，需谨慎处理公共同义词和依赖关系。强制删除（FORCE）适用于清理无效别名，确保数据库对象整洁性。

DROP SYNONYM 语法：

$$
.\Oracle兼容性手册-images\media\img128.jpg
$$

**参数说明：**

| 参数 | 说明 |
| --- | --- |
| PUBLIC | 删除公共同义词（必须与创建时的声明一致）。 |
| schema | 指定包含同义词的模式，如果省略schema，假定同义词在当前模式下。 |
| synonym | 指定要删除的同义词名字。 |
| FORCE | 强制删除同义词，即使有表或用户自定义类型依赖同义词。不建议指定FORCE来删除有对象依赖的自定义类型同义词。 |

### 限制

**目前删除同义词有以下限制：**

● 要执行删除同义词命令，您必须是同义词的所有者，并对同义词所在的 schema 具有 USAGE 特权。

● 删除公共同义词时，必须指定PUBLIC关键字。如果指定了PUBLIC，则不能指定模式。

### 示例

```sql
drop table tab;
create table tab(a int, b int);
create synonym syntab for tab;
create public synonym syntab2 for tab;
drop synonym syntab;
drop public synonym syntab2;
```

## 同义词系统视图

用户可通过ALL\_SYNONYMS、DBA\_SYNONYMS和USER\_SYNONYMS视图查看创建的同义词。

### 示例

**示例1：查看all\_synonyms**

```sql
drop table tab;
drop public synonym syntab2;
drop synonym syntab ;
create table tab(a int, b int);
create synonym syntab for tab;
create public synonym syntab2 for tab;
 
--执行下面视图查询，返回两行结果，可以查询到私有同义词和公共同义词
SELECT * FROM all_synonyms WHERE SYNONYM_NAME = 'syntab' OR SYNONYM_NAME = 'syntab2';
```

**示例2：查看dba\_synonyms**

```sql
--执行下面视图查询，返回两行结果，可以查询到私有同义词和公共同义词
select * from dba_synonyms where SYNONYM_NAME = 'syntab' OR SYNONYM_NAME = 'syntab2';
```

**示例3：查看user\_synonyms**

```sql
--执行下面视图查询，返回一行结果，可以查看私有同义词，查不到公共同义词
select * from user_synonyms where SYNONYM_NAME = 'syntab'  OR SYNONYM_NAME = 'syntab2';
```