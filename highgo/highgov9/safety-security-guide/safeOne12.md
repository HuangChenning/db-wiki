---
title: "数据脱敏"
book: "安全指南"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/safety/safeOne12.html"
tags:
  - highgo
  - highgo-v9
  - safety-security-guide
---

## 数据脱敏

数据脱敏，是指在保留数据原有格式的前提下，对某些敏感信息通过脱敏规则进行数据的变形或屏蔽，以防止未经授权的人员访问真实敏感数据的一种安全技术，从而实现敏感隐私数据的可靠保护。

数据脱敏主要分为静态脱敏和动态脱敏，静态数据脱敏采用”先脱敏-后分发”的方式，一般是将生产环境数据拷贝到测试或开发库中，导出后的数据已经改变了原始数据的内容，使得脱敏后的数据成为了测试开发源数据。而动态数据脱敏是与生产环境紧密关联的，访问敏感数据时实时地进行脱敏，主要用于直接访问生产数据的场景，在屏蔽敏感信息的同时也保证了源数据的一致性和有效性。

瀚高数据库主要提供动态数据脱敏功能。采用动态的改变来隐藏真实数据。通过给需要脱敏的每一个列定义一个函数来实现，返回脱敏函数处理后的数据给用户。数据脱敏只对用户数据做重编辑，不会对用户真实数据的传输、存储、非脱敏查询产生任何影响。

数据库安全员用户有权限打开脱敏开关，并创建、修改、删除、禁用、启用数据脱敏策略；关闭三权分立模块超级用户有权限打开脱敏开关，并创建、修改、删除、禁用、启用数据脱敏策略；

数据脱敏功能为V9.0.5版本新增功能。

## 数据脱敏的限制

瀚高数据库中对数据脱敏功能的运行做了以下限制：

1. 数据脱敏目前仅支持对普通表、分区表、继承表配置脱敏策略，脱敏用户查询到的结果是脱敏后的值；
2. 分区主表和每个分表、继承表都作为独立的表，需要单独创建脱敏策略。
3. 一个列上创建了脱敏策略后，不允许该列做任何修改操作；
4. 当 create table as 或 insert into  
	的数据来源于脱敏数据，则插入的数据为脱敏后的值，且无法还原。
5. 不支持DELETE中的查询子句带有数据脱敏；
6. 不支持MERGE INTO子句中带查询语句的数据脱敏。

## 数据脱敏插件

为使该模块生效，需要通过配置文件postgresql.conf  
中的shared\_preload\_libraries  
进行加载，给shared\_preload\_libraries参数追加hg\_redaction，随后重启服务器。然后登录数据库管理员创建扩展：

```
[highgo@node1 bin]$ ./psql highgo highgo

用户 highgo 的口令：

psql (14.20)

hgdb-client-V9.0.5

输入 "help" 来获取帮助信息.

highgo=# create extension hg_redaction;

CREATE EXTENSION
```

## 脱敏开关

瀚高数据库中对数据脱敏模块设置了开关。数据脱敏功能打开时，数据脱敏才会生效。数据脱敏功能关闭时，数据库不会发生数据动态脱敏动作。

hg\_redaction.enable为设置数据脱敏功能是否开启的总开关，取值为on和off，缺省为off。

on表示打开数据脱敏功能；

off表示关闭数据脱敏功能；

在会话中可以用SET的方式设置开关立即生效，也可以使用ALTER SYSTEM  
SET的方式，重载或重启数据库生效。

在瀚高数据库启动之前，修改postgresql.conf文件，将hg\_redaction.enable参数设置为on或off。

在瀚高数据库启动之后，通过SQL命令修改：

```
SET hg_redaction.enable=on;--立即生效

或
```
```
ALTER SYSTEM SET hg_redaction.enable=on;

SELECT pg_reload_conf();--重载生效
```

## 创建脱敏策略

支持通过使用 CREATE REDACTION POLICY  
的语法来创建脱敏策略。一张表上支持创建多个数据脱敏策略，但是每个列上只允许创建一次；支持在不同的表上创建同名的策略。

需要注意的是：如果给用户U1创建的脱敏策略，然后将U1用户重新命名成U2，那么U1的脱敏策略不会对U2生效。

创建脱敏策略的语法：

```
CREATE REDACTION POLICY <name> ON <schema.tbname>

[ FOR ( <expression>[,...] ) ]

ADD [COLUMN] <column_name>[,...] USING <funcname_clause>

[ WITH OPTIONS ( [ <redaction_option> ]

[, <redaction_option> ] )

]

[, ...]

[ENABLE | DISABLE]
```

参数说明

- name
	数据脱敏策略的名称
- schema.tbname
	需要建立脱敏策略的表名
- expression
	支持对特定session\_user，application，user，ip  
	的脱敏限制；支持同时设置多个条件，只要满足其中一个条件就脱敏。
	仅支持”=” 和”!=” 的表达形式；
- column\_name
	列名
- funcname\_clause
	函数名
- redaction\_option
	- SCOPE(query, top\_tlist, top\_tlist\_or\_error)
		query表示无论出现在查询中的什么位置，都会对列应用脱敏；缺省为query
		top\_tlist表示仅当列出现查询在顶部目标列中时，才对列应用脱敏；
		top\_tlist\_or\_error行为与top\_list相同，但当该列出现在查询中的其他任何地方会抛出一个错误。
		- EXCEPTION(none, equal)
		none 表示没有exception;
		equal 表示在等式查询中，脱敏列不脱敏。缺省为equal。
		创建脱敏策略后默认ENABLE启用状态。

## 修改脱敏策略

支持更改脱敏策略的相关信息，可以修改脱敏策略的名称，表达式，脱敏函数，增加/删除脱敏列和修改脱敏列属性，可以单独开启和关闭某一个数据脱敏策略。

修改脱敏策略的语法有如下几种：

方式一：

```
ALTER REDACTION POLICY <name> ON <schema.tbname> RENAME TO
<new_name>;
```

参数说明

- name
	数据脱敏策略的名称
- schema.tbname
	需要建立脱敏策略的表名
- new\_name
	数据脱敏策略的新名称

方式二：

```
ALTER REDACTION POLICY <name> ON <schema.tbname> FOR (
<expression> );
```

参数说明

- name
	数据脱敏策略的名称
- schema.tbname
	需要建立脱敏策略的表名
- expression
	支持对特定session\_user，application，user，ip  
	的脱敏限制；支持同时设置多个条件，只要满足其中一个条件就脱敏。
	仅支持”=” 和”!=” 的表达形式；

方式三：

```
ALTER REDACTION POLICY <name> ON <schema.tbname>

ADD [ COLUMN ] <column_name>[,...] USING <funcname_clause>

[ WITH OPTIONS ( [ <redaction_option> ]

[, <redaction_option> ] )

]

[,...];
```

参数说明

- name
	数据脱敏策略的名称
- schema.tbname
	需要建立脱敏策略的表名
- column\_name
	列名
- funcname\_clause
	函数名
- redaction\_option
	- SCOPE(query, top\_tlist, top\_tlist\_or\_error)
		query表示无论出现在查询中的什么位置，都会对列应用脱敏；缺省为query
		top\_tlist表示仅当列出现查询在顶部目标列中时，才对列应用脱敏；
		top\_tlist\_or\_error行为与top\_list相同，但当该列出现在查询中的其他任何地方会抛出一个错误。
		- EXCEPTION(none, equal)
		none 表示没有exception;
		equal 表示在等式查询中，脱敏列不脱敏。缺省为equal。

方式四：

```
ALTER REDACTION POLICY <name> ON <schema.tbname>

DROP [ COLUMN ] <column_name>;
```

参数说明

- name
	数据脱敏策略的名称
- schema.tbname
	需要建立脱敏策略的表名
- column\_name
	列名

方式五：

```
ALTER REDACTION POLICY <name> ON <schema.tbname>

MODIFY [ COLUMN ]

{

<column_name> [, ...]

[ USING <funcname_clause> ]

|

[ WITH OPTIONS ( [ <redaction_option> ]

[, <redaction_option> ] )

]

}

{, ...}
```

参数说明

- Name
	数据脱敏策略的名称
- schema.tbname
	需要建立脱敏策略的表名
- column\_name
	列名
- funcname\_clause
	函数名
- redaction\_option
	- SCOPE(query, top\_tlist, top\_tlist\_or\_error)

query表示无论出现在查询中的什么位置，都会对列应用脱敏；缺省为query

top\_tlist表示仅当列出现查询在顶部目标列中时，才对列应用脱敏；

top\_tlist\_or\_error行为与top\_list相同，但当该列出现在查询中的其他任何地方会抛出一个错误。

- EXCEPTION(none, equal)

none 表示没有exception;

equal 表示在等式查询中，脱敏列不脱敏。缺省为equal。

方式六：

```
ALTER REDACTION POLICY <name> ON <schema.tbname> [ENABLE |
DISABLE];
```

参数说明

- name
	数据脱敏策略的名称
- schema.tbname
	需要建立脱敏策略的表名

## 删除脱敏策略

删除数据脱敏策略后，数据脱敏策略相关信息将从表  
hg\_security.hg\_redaction\_policy和  
hg\_security.hg\_redaction\_column中一并删除。删除用户表时，如果用户表上有数据脱敏策略，那么该表上的脱敏策略将一并删除。

删除脱敏策略的语法：

```
DROP REDACTION POLICY [ IF EXISTS ] <name> ON <schema.tbname> [
CASCADE | RESTRICT ]
```

参数说明

- name
	数据脱敏策略的名称
- schema.tbname
	需要建立脱敏策略的表名

## 查看脱敏策略

提供hg\_security.hg\_redaction视图，用于查询已创建的脱敏策略，数据库安全员或超级用户有权限查看所有脱敏策略。

## 数据脱敏函数与特性

数据脱敏功能通过使用脱敏函数来实现，瀚高数据库支持完整脱敏、部分数据脱敏、数据脱敏、邮件数据脱敏和随机数据脱敏等多种脱敏函数。用户可结合对应的脱敏策略使用数据库脱敏函数。

| 函数 | 支持的数据类型 | 说明 |
| --- | --- | --- |
| hg\_security.redact\_all | BOOL,TIME,TIMETZ,INTERVAL,TIMESTAMP,TIMESTAMPTZ,TEXT,BPCHAR,VARCHAR,NAME, INT8,INT4,INT2,NUMRIC,FLOAT4,FLOAT8, MONEY，SECLABEL | ‘4880-9898-4545-2525’ 将会被脱敏为 ‘xxxxxxxxxxxxxxxxxxx’，安全标签的被脱敏为’s\*\*\*\*\*’ |
| hg\_security.redact\_bankcard | BPCHAR, VARCHAR, TEXT（ 注： 仅针对信用卡格式的文本类数据） | ‘4880-9898-4545-2525’ 将会被脱敏为 ‘xxxx-xxxx-xxxx-2525’， 该函数仅对后 4 位之前的数字进行脱敏。 |
| hg\_security.redact\_emailname | BPCHAR, VARCHAR, TEXT (注： 仅针对 email格式的文本类型数据) | ‘ [abcd@gmail.com](mailto:abcd@gmail.com) ‘ 将会被脱敏为‘ [xxxx@gmail.com](mailto:xxxx@gmail.com) ‘， 对出现第一个‘@’之前的文本进行脱敏 |
| hg\_security.redact\_emailfull | BPCHAR, VARCHAR, TEXT (注： 仅针对 email格式的文本类型数据) | ‘ [abcd@gmail.com](mailto:abcd@gmail.com) ‘ 将会被脱敏为‘ [xxxx@xxxxx.com](mailto:xxxx@xxxxx.com) ‘， 对出现最后一个’.’之前的文本（ 除‘@’符外） 进行脱敏 |
| hg\_security.redact\_digits | BPCHAR, VARCHAR, TEXT (注： 仅针对包含数字的文本类型数据) | ‘alex123alex’ 将会被脱敏为’alex000alex’， 仅对文本中的数字进行脱敏。 |
| hg\_security.redact\_shuffle | BPCHAR, VARCHAR, TEXT (注： 仅针对文本类型数据) | ‘hello word’ 将会被随机打乱顺序脱敏为 ‘hlwoeor dl’， 该函数通过字符乱序排列的方式实现， 属于弱脱敏函数， 语义较强的字符串不建议使用该函数脱敏。 |
| hg\_security.redact\_random | BPCHAR, VARCHAR, TEXT (注： 仅针对文本类型数据) | ‘hello word’ 将会被脱敏为’ad5f5ghdf5’， 将文本按字符随机脱敏 |
| hg\_security.redact\_idcard | BPCHAR,VARCHAR, TEXT(注： 仅针对身份证格式的文本类型数据) | 对身份证号进行脱敏130623202101010623’将被脱敏为’130623\*\*\*\*\*\*\* *0623’， 该函数保留身份证号的前六位和后四位，中间的号码用* 代替。 |
| hg\_security.redact\_name | BPCHAR, VARCHAR, TEXT (注： 仅针对姓名的文本类型数据) | 对姓名进行脱敏。不管名字是几个字， 保留第一个字， 后面两个\*表示。如“张三”被脱敏为“张 **”， “张三丰”被脱敏为“张** ”， “富兰克林”被脱敏为“富\*\*” |
| hg\_security.redact\_phone | BPCHAR, VARCHAR, TEXT (注： 仅针对电话号码的文本类型数据) | 对电话号码进行脱敏。适用于手机号和固话号。保留前三位和后四位， 对中间数字进行脱敏。如“13534556093” 脱敏为“135\* ***6093”“053*** \* *0980”。备注：中间有多少个字符显示多少个* 。 |
| hg\_security.redact\_cash | MONEY | 对货币类型进行脱敏处理，如“100.00” 会脱敏成“￥0.00”或“$0.00 |

## 数据脱敏的使用

一、启用数据脱敏功能

在数据库启动之前，修改配置文件postgresql.conf，给shared\_preload\_libraries参数追加hg\_redaction，随后启动数据库。

登录数据库管理员用户创建扩展

```
[highgo@node1 bin]$ ./psql highgo highgo

用户 highgo 的口令：

psql (14.20)

hgdb-client-V9.0.5

输入 "help" 来获取帮助信息.

highgo=# create extension hg_redaction;

CREATE EXTENSION

打开脱敏开关

highgo=# \c highgo syssso

用户 syssso 的口令：

hgdb-client-V9.0.5

您现在已经连接到数据库 "highgo",用户 "syssso".

highgo=> SET hg_redaction.enable=on;

SET
```

二、创建一个完整脱敏策略

```
登录highgo用户创建测试用户

highgo=> c highgo highgo

用户 highgo 的口令：

hgdb-client-V9.0.5

您现在已经连接到数据库 "highgo",用户 "highgo".

highgo=# create user u1 password 'highgo';

CREATE ROLE

highgo=# create user u2 password 'highgo';

CREATE ROLE

highgo=# create user u3 password 'highgo';

在用户u3下创建测试表，并赋予u1和u2用户select权限

highgo=# \c highgo u3

用户 u3 的口令：

hgdb-client-V9.0.5

您现在已经连接到数据库 "highgo",用户 "u3".

highgo=> create table test(id int, col1 varchar,info text);

CREATE TABLE

highgo=> insert into test values(1,'highgo','database');

INSERT 0 1

highgo=> insert into test values(2,'postgres','opensource');

INSERT 0 1

highgo=> grant select on test to u1,u2;

GRANT

登录安全员用户创建完整脱敏策略，仅对u1用户生效

highgo=> c highgo syssso

用户 syssso 的口令：

hgdb-client-V9.0.5

您现在已经连接到数据库 "highgo",用户 "syssso".

highgo=> create redaction policy p1 on test for(user='u1') add column
col1 using hg_security.redact_all;

CREATE REDACTION POLICY

登录u1用户查看test表中col1列数据已完全脱敏

highgo=> c highgo u1

用户 u1 的口令：

hgdb-client-V9.0.5

您现在已经连接到数据库 "highgo",用户 "u1".

highgo=> select * from test;

id | col1 | info

----+----------+------------

1 | xxxxxx | database

2 | xxxxxxxx | opensource

(2 行记录)

登录u2用户查看test表完整数据

highgo=> c highgo u2

用户 u2 的口令：

hgdb-client-V9.0.5

您现在已经连接到数据库 "highgo",用户 "u2".

highgo=> select * from test;

id | col1 | info

----+----------+------------

1 | highgo | database

2 | postgres | opensource

(2 行记录)
```

三、修改脱敏策略，将test表中info列进行随机脱敏显示

登录安全员用户修改脱敏策略

```
highgo=> c highgo syssso

用户 syssso 的口令：

hgdb-client-V9.0.5

您现在已经连接到数据库 "highgo",用户 "syssso".

highgo=> alter redaction policy p1 on test add column info using
hg_security.redact_random;

ALTER REDACTION POLICY

验证info列对u1用户脱敏，对u2用户正常显示

highgo=> c highgo u1

用户 u1 的口令：

hgdb-client-V9.0.5

您现在已经连接到数据库 "highgo",用户 "u1".

highgo=> select * from test;

id | col1 | info

----+----------+------------

1 | xxxxxx | cef1b1eb

2 | xxxxxxxx | 120342a72c

(2 行记录)

highgo=> c highgo u2

用户 u2 的口令：

hgdb-client-V9.0.5

您现在已经连接到数据库 "highgo",用户 "u2".

highgo=> select * from test;

id | col1 | info

----+----------+------------

1 | highgo | database

2 | postgres | opensource

(2 行记录)
```

四、创建test2表，在多个列上添加不同的脱敏规则

```
对test2表中的2列数据添加不同的脱敏规则

[highgo@node1 bin]$ ./psql highgo highgo

用户 highgo 的口令：

psql (14.20)

hgdb-client-V9.0.5

输入 "help" 来获取帮助信息.

highgo=# select * from test2;

name | phone | idcard | money

----------+-------------+--------------------+---------

富兰克林 | 15789177109 | 130623202101010623 | $500.00

(1 行记录)

highgo=# \c highgo syssso

用户 syssso 的口令：

hgdb-client-V9.0.5

您现在已经连接到数据库 "highgo",用户 "syssso".

highgo=> create redaction policy p2 on test2 add name using
hg_security.redact_name,add phone using hg_security.redact_phone;

CREATE REDACTION POLICY

highgo=> c highgo highgo

用户 highgo 的口令：

hgdb-client-V9.0.5

您现在已经连接到数据库 "highgo",用户 "highgo".

highgo=# select * from test2;

name | phone | idcard | money

------+-------------+--------------------+---------

富** | 157****7109 | 130623202101010623 | $500.00
```

2.删除脱敏策略

```
highgo=> drop redaction policy p2 on test2;

DROP REDACTION POLICY
```

五、创建脱敏策略，等式查询中脱敏列不脱敏

```
highgo=> c highgo highgo

用户 highgo 的口令：

hgdb-client-V9.0.5

您现在已经连接到数据库 "highgo",用户 "highgo".

highgo=# create table test3(id int, name text);

CREATE TABLE

highgo=# insert into test3 values(1, 'zhangsan');

INSERT 0 1

highgo=# \c highgo syssso

用户 syssso 的口令：

hgdb-client-V9.0.5

您现在已经连接到数据库 "highgo",用户 "syssso".

highgo=> create redaction policy p3 on test3 add column name using
hg_security.redact_all with options(scope query, exception equal);

CREATE REDACTION POLICY

highgo=> c highgo highgo

用户 highgo 的口令：

hgdb-client-V9.0.5

您现在已经连接到数据库 "highgo",用户 "highgo".

highgo=#

highgo=# select * from test3;

id | name

----+----------

1 | xxxxxxxx

(1 行记录)

----等式查询中name列不脱敏，能匹配到test3表里存的数据，所以有一条返回数据，返回为脱敏后的数据。

highgo=# select * from test3 where name = 'zhangsan';

id | name

----+----------

1 | xxxxxxxx

(1 行记录)

highgo=# \c highgo syssso

用户 syssso 的口令：

hgdb-client-V9.0.5

您现在已经连接到数据库 "highgo",用户 "syssso".

highgo=> drop redaction policy p3 on test3;

DROP REDACTION POLICY

highgo=> create redaction policy p4 on test3 add column name using
hg_security.redact_all with options(scope query, exception none);

CREATE REDACTION POLICY

highgo=> c highgo highgo

用户 highgo 的口令：

hgdb-client-V9.0.5

您现在已经连接到数据库 "highgo",用户 "highgo".

--无返回数据

highgo=# select * from test3 where name = 'zhangsan';

id | name

----+------

(0 行记录)

--有返回数据

highgo=# select * from test3 where name = 'xxxxxxxx';

id | name

----+----------

1 | xxxxxxxx

(1 行记录)

highgo=> c highgo syssso

用户 syssso 的口令：

hgdb-client-V9.0.5

您现在已经连接到数据库 "highgo",用户 "syssso".

highgo=>

highgo=> drop redaction policy p4 on test3;

DROP REDACTION POLICY
```

六、创建脱敏策略，top\_tlist

```
highgo=> c highgo highgo

用户 highgo 的口令：

hgdb-client-V9.0.5

您现在已经连接到数据库 "highgo",用户 "highgo".

highgo=# create table tb1(id int4 primary key,info text,name varchar);

highgo=#create table tb2(id int4,info text,name varchar);

highgo=#insert into tb1
values(1,'hgdb','highgo'),(2,'student','zhang'),(3,'fruit','apple');

highgo=#insert into tb2
values(1,'hgdb','highgo'),(22,'student','zhang'),(33,'fruit','apple');

highgo=#

highgo=# \c highgo syssso

用户 syssso 的口令：

hgdb-client-V9.0.5

您现在已经连接到数据库 "highgo",用户 "syssso".

highgo=> create redaction policy tb1_pol1 on tb1 add column id using
hg_security.redact_all with options (scope top_tlist);

CREATE REDACTION POLICY

--查询tb1表发现id列已被脱敏

highgo=> c highgo highgo

用户 highgo 的口令：

hgdb-client-V9.0.5

您现在已经连接到数据库 "highgo",用户 "highgo".

highgo=#

highgo=# select * from tb1;

id | info | name

----+---------+--------

0 | hgdb | highgo

0 | student | zhang

0 | fruit | apple

(3 行记录)

--redaction option为scope
toplist，仅当列出现查询在顶部目标列中时，才对列应用脱敏，出现在子查询中不会脱敏。

highgo=# SELECT id,name FROM tb2 WHERE id = (SELECT min(id) FROM tb1
WHERE name = 'highgo');

id | name

----+--------

1 | highgo

(1 行记录)
```

## 脱敏数据的导出导入

```
对表添加数据脱敏策略后，不会影响数据的导入导出操作。

1.u1用户登录数据库，查看test表

highgo=> c highgo u1

用户 u1 的口令：

hgdb-client-V9.0.5

您现在已经连接到数据库 "highgo",用户 "u1".

highgo=> select * from test;

id | col1 | info

----+----------+------------

1 | xxxxxx | 7ee15b47

2 | xxxxxxxx | 6a36652c3c

(2 行记录)

2.将test表数据指定输出到当前客户端

highgo=> copy test to stdout with csv;

1,highgo,database

2,postgres,opensource

3.使用highgo用户登录，将test表导出到csv文件

highgo=> c highgo highgo

用户 highgo 的口令：

hgdb-client-V9.0.5

您现在已经连接到数据库 "highgo",用户 "highgo".

highgo=# copy test to '/home/highgo/test' with csv;

COPY 2

4.查看导出的文件

[highgo@node1 ~]$ cat /home/highgo/test

1,highgo,database

2,postgres,opensource

5.highgo用户登录，将导出数据导入到test表

[highgo@node1 bin]$ ./psql highgo highgo

用户 highgo 的口令：

psql (14.20)

hgdb-client-V9.0.5

输入 "help" 来获取帮助信息.

highgo=# copy test from '/home/highgo/test' (FORMAT 'csv', DELIMITER
','); COPY 2

highgo=#

highgo=# select * from test;

id | col1 | info

----+----------+------------

1 | highgo | database

2 | postgres | opensource

1 | highgo | database

2 | postgres | opensource

(4 行记录)
```

## 脱敏数据的备份恢复

对表添加数据脱敏策略后，不会影响数据的备份和恢复操作。

```
1.备份已添加脱敏策略的test表

[highgo@node1 bin]$ ./pg_dump -f /home/highgo/testdump -Fc -t test
highgo

2.登录u3用户删除test表，注意：表对象删除后会同步删除脱敏策略。

[highgo@node1 bin]$ ./psql highgo u3

用户 u3 的口令：

psql (14.20)

hgdb-client-V9.0.5

输入 "help" 来获取帮助信息.

highgo=> drop table test;

DROP TABLE

3.执行恢复操作

[highgo@node1 bin]$ ./pg_restore -U u3 -d highgo
/home/highgo/testdump

4.登录u3用户检查数据是否恢复

[highgo@node1 bin]$ ./psql highgo u3

用户 u3 的口令：

psql (14.20)

hgdb-client-V9.0.5

输入 "help" 来获取帮助信息.

highgo=> dt

关联列表

架构模式 | 名称 | 类型 | 拥有者

----------+-------+--------+--------

public | test | 数据表 | u3

public | test2 | 数据表 | u3

(2 行记录)

highgo=> select * from test;

id | col1 | info

----+----------+------------

1 | highgo | database

2 | postgres | opensource

1 | highgo | database

2 | postgres | opensource

(4 行记录)

5.登录u1用户，查询test表

highgo=> c - highgo u1

无法解释主机名 "u1" 到地址: 未知的名称或服务

保留上一次连接

highgo=> c highgo u1

用户 u1 的口令：

hgdb-client-V9.0.5

您现在已经连接到数据库 "highgo",用户 "u1".

highgo=> select * from test;

id | col1 | info

----+----------+------------

1 | highgo | database

2 | postgres | opensource

1 | highgo | database

2 | postgres | opensource

(4 行记录)
```