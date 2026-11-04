---
title: "操作符"
book: "Oracle兼容性"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/compatibility/compOracle20.html"
tags:
  - highgo
  - highgo-v9
  - compatibility-oracle
---

## 操作符

## Like

LIKE运算符是用来检查列中的值是否与指定的模式匹配，即通过指定的模式来查询数据。

1）expression

该表达式是一个列名称或一个表达式，要针对该模式 (pattern) 进行测试。

2）pattern

pattern要在expression中搜索的字符串。pattern包括以下通配符：

%（百分比）匹配零个或多个字符的任何字符串。

\_（下划线）匹配任何单个字符。

3）escape\_characters

escape\_characters是出现在通配符前面的字符，用于指定通配符应解释为常规字符，而不是通配符。

escape\_character如果指定，则必须是一个字符，并且没有默认值。

如果表达式匹配模式，LIKE运算符返回true。 否则返回false。

如果指定了运算NOT符，则会否定LIKE运算符的结果。

在where子句中使用like关键字来达到模糊查询的效果；在Where子句中，可以对datetime、char、varchar字段类型的列用Like关键字配合通配符来实现模糊查询。

示例：

日期类型：

create table tb1(col date);

insert into tb1 values(‘20121212’);

insert into tb1 values(‘3030\\12\\12’);

alter session set NLS\_DATE\_FORMAT=’YYYY-MM-DD’;

highgo=# select \* from tb1 where to\_char(tb1.col,’yyyy\\MM\\dd’) like ‘1999\\%’;

col

\-———–

1999-10-01

(1 row)

highgo=# select \* from tb1 where col like ‘1999\_\_\_ *\_* ‘;

col

\-———–

1999-10-01

字符串类型：

highgo=# create table test(id int,name varchar2(40));

CREATE TABLE

highgo=#

highgo=# insert into test values(1,’my name is highgo\_database’);

INSERT 0 1

highgo=# SELECT name FROM test WHERE name like ‘%highgo\\\_database%’ escape ‘\\‘;

name

\-————————

my name is highgo\_database

(1 row)

highgo=# SELECT name FROM test WHERE name like ‘%highgo\_database%’ escape ‘\\‘;

name

\-————————

my name is highgo\_database

(1 row)

highgo=# SELECT name FROM test WHERE name like ‘%highgo\_%’;

name

\-————————

my name is highgo\_database

(1 row)

## 索引操作符

首先在需要使用操作符的数据库中创建插件：

postgres=# CREATE EXTENSION ora\_btree\_gist;

CREATE EXTENSION

postgres=# CREATE EXTENSION ora\_btree\_gin;

CREATE EXTENSION

### GIST

支持在兼容类型如number、varchar2、binary\_float、binary\_double、timestamp、date、timestamp with time zone、timestamp with local timezone、interval year to month、interval day to second上使用gist索引时相关操作符的使用。

在对应的列上创建gist索引，执行如下语句：

CREATE INDEX gist\_index ON table USING gist (columnname );

创建完成该列的gist索引后，支持下述类型对应操作符处理。

#### NUMBER类型

| **操作符** | **左数据类型** | **右数据类型** |
| --- | --- | --- |
| < | number | number |
| <= | number | number |
| \= | number | number |
| \>= | number | number |
| \> | number | number |
| <> | number | number |

#### VARCHAR2类型

| **操作符** | **左数据类型** | **右数据类型** |
| --- | --- | --- |
| < | varchar2 | varchar2 |
| <= | varchar2 | varchar2 |
| \= | varchar2 | varchar2 |
| \>= | varchar2 | varchar2 |
| \> | varchar2 | varchar2 |
| <> | varchar2 | varchar2 |

#### BINARY\_FLOAT类型

| **操作符** | **左数据类型** | **右数据类型** |
| --- | --- | --- |
| < | binary\_float | binary\_float |
| <= | binary\_float | binary\_float |
| \= | binary\_float | binary\_float |
| \>= | binary\_float | binary\_float |
| \> | binary\_float | binary\_float |
| <> | binary\_float | binary\_float |
| <-> | binary\_float | binary\_float |

#### BINARY\_DOUBLE类型

| **操作符** | **左数据类型** | **右数据类型** |
| --- | --- | --- |
| < | binary\_double | binary\_double |
| <= | binary\_double | binary\_double |
| \= | binary\_double | binary\_double |
| \>= | binary\_double | binary\_double |
| \> | binary\_double | binary\_double |
| <> | binary\_double | binary\_double |
| <-> | binary\_double | binary\_double |

#### DATE类型

| **操作符** | **左数据类型** | **右数据类型** |
| --- | --- | --- |
| < | date | date |
| <= | date | date |
| \= | date | date |
| \>= | date | date |
| \> | date | date |
| <> | date | date |
| <-> | date | date |

#### TIMESTAMP类型

|  |  |  |
| --- | --- | --- |
| **操作符** | **左数据类型** | **右数据类型** |
| < | timestamp | timestamp |
| <= | timestamp | timestamp |
| \= | timestamp | timestamp |
| \>= | timestamp | timestamp |
| \> | timestamp | timestamp |
| <> | timestamp | timestamp |
| <-> | timestamp | timestamp |

#### TIMESTAMP WITH TIME ZONE类型

| **操作符** | **左数据类型** | **右数据类型** |
| --- | --- | --- |
| < | timestamp with time zone | timestamp with time zone |
| <= | timestamp with time zone | timestamp with time zone |
| \= | timestamp with time zone | timestamp with time zone |
| \>= | timestamp with time zone | timestamp with time zone |
| \> | timestamp with time zone | timestamp with time zone |
| <> | timestamp with time zone | timestamp with time zone |
| <-> | timestamp with time zone | timestamp with time zone |

#### TIMESTAMP WITH LOCAL TIME ZONE类型

| **操作符** | **左数据类型** | **右数据类型** |
| --- | --- | --- |
| < | timestamp with local time zone | timestamp with local time zone |
| <= | timestamp with local time zone | timestamp with local time zone |
| \= | timestamp with local time zone | timestamp with local time zone |
| \>= | timestamp with local time zone | timestamp with local time zone |
| \> | timestamp with local time zone | timestamp with local time zone |
| <> | timestamp with local time zone | timestamp with local time zone |
| <-> | timestamp with local time zone | timestamp with local time zone |

#### INTERVAL YEAR TO MONTH类型

| **操作符** | **左数据类型** | **右数据类型** |
| --- | --- | --- |
| < | interval year to month | interval year to month |
| <= | interval year to month | interval year to month |
| \= | interval year to month | interval year to month |
| \>= | interval year to month | interval year to month |
| \> | interval year to month | interval year to month |
| <> | interval year to month | interval year to month |
| <-> | interval year to month | interval year to month |

#### INTERVAL DAY TO SECOND类型

| **操作符** | **左数据类型** | **右数据类型** |
| --- | --- | --- |
| < | interval day to second | interval day to second |
| <= | interval day to second | interval day to second |
| \= | interval day to second | interval day to second |
| \>= | interval day to second | interval day to second |
| \> | interval day to second | interval day to second |
| <> | interval day to second | interval day to second |
| <-> | interval day to second | interval day to second |

### GIN

支持在兼容类型如number、varchar2、binary\_float、binary\_double、timestamp、date、timestamp with time zone、timestamp with local timezone上使用gin索引时相关操作符的使用。

在对应的列上创建gist索引，执行如下语句：

CREATE INDEX gin\_index ON table USING gist (columnname );

创建完成该列的gin索引后，支持下述类型对应操作符处理。

#### NUMBER类型

| **操作符** | **左数据类型** | **右数据类型** |
| --- | --- | --- |
| < | number | number |
| <= | number | number |
| \= | number | number |
| \>= | number | number |
| \> | number | number |

#### VARCHAR2类型

| **操作符** | **左数据类型** | **右数据类型** |
| --- | --- | --- |
| < | varchar2 | varchar2 |
| <= | varchar2 | varchar2 |
| \= | varchar2 | varchar2 |
| \>= | varchar2 | varchar2 |
| \> | varchar2 | varchar2 |

#### BINARY\_FLOAT类型

| **操作符** | **左数据类型** | **右数据类型** |
| --- | --- | --- |
| < | binary\_float | binary\_float |
| <= | binary\_float | binary\_float |
| \= | binary\_float | binary\_float |
| \>= | binary\_float | binary\_float |
| \> | binary\_float | binary\_float |

#### BINARY\_DOUBLE类型

| **操作符** | **左数据类型** | **右数据类型** |
| --- | --- | --- |
| < | binary\_double | binary\_double |
| <= | binary\_double | binary\_double |
| \= | binary\_double | binary\_double |
| \>= | binary\_double | binary\_double |
| \> | binary\_double | binary\_double |

#### DATE类型

| **操作符** | **左数据类型** | **右数据类型** |
| --- | --- | --- |
| < | date | date |
| <= | date | date |
| \= | date | date |
| \>= | date | date |
| \> | date | date |

#### TIMESTAMP类型

| **操作符** | **左数据类型** | **右数据类型** |
| --- | --- | --- |
| < | timestamp | timestamp |
| <= | timestamp | timestamp |
| \= | timestamp | timestamp |
| \>= | timestamp | timestamp |
| \> | timestamp | timestamp |

#### TIMESTAMP WITH TIME ZONE类型

| **操作符** | **左数据类型** | **右数据类型** |
| --- | --- | --- |
| < | timestamp with time zone | timestamp with time zone |
| <= | timestamp with time zone | timestamp with time zone |
| \= | timestamp with time zone | timestamp with time zone |
| \>= | timestamp with time zone | timestamp with time zone |
| \> | timestamp with time zone | timestamp with time zone |

#### TIMESTAMP WITH LOCAL TIME ZONE类型

| **操作符** | **左数据类型** | **右数据类型** |
| --- | --- | --- |
| < | timestamp with local time zone | timestamp with local time zone |
| <= | timestamp with local time zone | timestamp with local time zone |
| \= | timestamp with local time zone | timestamp with local time zone |
| \>= | timestamp with local time zone | timestamp with local time zone |
| \> | timestamp with local time zone | timestamp with local time zone |

## (+)操作符

### 说明

(+) 操作符是用于执行外连接的一种旧式语法。其主要作用是指示在连接多个表时，哪些列需要匹配，以及如何处理不匹配的情况。

具体来说，(+) 操作符用在WHERE子句中，以表示OUTER JOIN。通常，(+) 操作符被放置在WHERE子句中的某个表的列与另一个表的列进行比较的条件中，以指示执行外连接。如果某列带有 (+) 操作符，并且没有与之匹配的行，则会填充 NULL 值。

语法如下所示：

语法除支持语法图中=号以外，还支持=、>=、<=、<>、>、<、运算表达式(如：t1.col(+)+1 = t2.col)、between and等表达式，在where子句中的子链接中使用(+)操作符，但是子链接中使用(+)操作符的表不能引用外部的表。

### 示例

create table t1 (i int, j int);

insert into t1 values (1,2);

insert into t1 values (2,2);

insert into t1 values (3,1);

insert into t1 values (null, null);

create table t2 as select \* from t1;

create table t3 as select \* from t1;

create table t4 as select \* from t1;

create table t5 as select \* from t1;

\--simple testcase

select \* from t1, t2 where t1.i = t2.i(+);

\--multi AND testcase

select \* from t1,t2,t3,t4,t5 where t1.i(+)+t2.i = t3.i and t4.i(+)= t2.i + t5.i;

\--like testcase

select \* from t1, t2 where t1.i like t2.j(+);

\--between and

select \* from t1, t2 where t1.i between t2.i(+) and t2.j(+);

\--IS (NOT) NULL testcase

select \* from t1, t2, t3 where t1.i = t2.i(+) and t3.i(+) is not null;