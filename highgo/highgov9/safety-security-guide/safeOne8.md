---
title: "强制访问控制"
book: "安全指南"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/safety/safeOne8.html"
tags:
  - highgo
  - highgo-v9
  - safety-security-guide
---

## 强制访问控制

强制访问控制是根据客体的安全标记和安全规则限制用户对数据库对象进行某项操作的一种方法。在强制访问控制中，系统给主体和客体都分配一个特殊的安全标记，主体的安全标记反映了该主体可信的程度，客体的安全标记则与其包含信息的敏感度一致。主体是否可以对客体执行特定的操作取决于主体和客体的安全标记之间的支配关系。因此，强制访问控制可以控制系统中信息流动的轨迹，可以抵抗特洛伊木马的攻击，强制访问控制功能在一些对安全要求很高的数据库应用系统中是非常必要的。瀚高数据库利用安全标记来实现数据库的强制访问控制。

强制访问控制的级别分为表级、列级和行级。其中表级强制访问控制支持的对象有：表(TABLE)、视图(VIEW)、序列(SEQUENCE)，在表对象访问控制支持普通表、分区表，不支持外部表、系统表、临时表。

强制访问控制功能为V9.0.5版本新增功能。

## 强制访问控制开关

### 参数配置

---

| 参数 | 生效方式 | 参数说明 | 默认值 | 优先级 |
| --- | --- | --- | --- | --- |
| hg\_sysmac.global\_on | 重载生效 | 强制访问控制开关 | off | 1 |
| hg\_sysmac.global\_table\_level | 重载生效 | 表级控制开关 | off | 2 |
| hg\_sysmac.global\_column\_level | 重载生效 | 列安全开关 | off | 3 |
| hg\_sysmac.global\_row\_level | 重载生效 | 行安全开关 | on | 2 |

global\_on是强制访问控制模块的总开关，开关优先级为1，次开关开启后强制访问控制功能才会生效；global\_table\_level  
和  
global\_row\_level分别是表级控制的开关和行级控制的开关，优先级为2，只有在global\_on开关开启后才会生效，这两个开关即可以单独启用，也可以同时启用；global\_column\_level表示列级控制开关，此开关优先级为3，只有在  
global\_table\_level 开启时，global\_column\_level  
的设置才会生效。上述4个开关数据库管理员可通过ALTER SYSTEM  
SET的方式修改后，执行SELECT pg\_reload\_conf();命令进行重载参数生效。

### 控制级别说明

图8-1 强制访问控制级别说明

### 对指定表启用行安全控制

开启行安全开关global\_row\_level后，还需要数据库安全员或超级用户对单个表启用或禁用行级安全控制。

我们提供了hg\_security.apply\_row\_policy()函数，可针对单个表启用或禁用行级安全控制。

```
hg_security.apply_row_policy(tbl_oid oid,action text )
```

参数说明：

- tbl\_oid 指定表对象的oid

action  
行级安全策略的动作，可取值：apply、enable、disable、drop，分别对应应用（添加隐藏列，并打开行级安全控制）、启用（打开行级控制）、禁用和删除行级安全控制操作。

## 安全标记

要想实现强制访问控制，数据库安全员首先需要给主体和客体设置相应的安全标记。强制访问控制的主体一般指的是用户，强制访问控制的客体包括普通表、视图、序列、记录或字段等。

安全标记为特定格式的字符串，由安全密级和安全范围组成。安全密级为s0 ~~s15共16个级别，安全范围为c0~~ c1023共1024个类别。其中安全密级s0~s15为安全级别的递进关系，即s0密级最低，s15密级最高；而安全范围之间不是级别高低的关系而是包含与被包含的关系。

这样可根据需要，将保密等级分为绝密范围、机密范围、秘密范围、内部范围、公开范围、自定义范围（用户自定义）六种级别范围，syssso可以自行从s0~s15中挑选一部分与之对应。安全范围则可以进一步对权限进行细化，即只有当主体包含客体对应的类别时才能进行相应的操作。主体或客体可拥有多个安全范围并使用逗号分隔，如果多个安全范围是连续的则可设置第一个和最后一个安全范围中间使用句号分隔。例如安全标记”s0:c0.c1023”，表示安全密级为s0，安全范围为包含c0到c1023全部类别的集合。

安全标记的格式如下：

<安全密级>:\[<安全范围>{,<安全范围>}\]

### 设置安全标记

启用强制访问控制之后，主体及客体的安全标记默认为空，需要数据库安全员或超级用户对主体和客体设置安全标记。启用行级安全控制之后，行安全标记值默认继承自创建该条记录的用户的安全标记。

所有主体和客体的安全标记值按照”安全密级：安全类别”的方式设置和存储。数据库安全员或超级用户有权限设置、查看安全标记。

设置用户安全标记

```
hg_security.set_user_seclabel(user_oid oid, seclabel text)
```

参数说明：

- user\_oid
	指定用户的oid
- seclabel
	安全标记

设置表、视图、序列对象的安全标记

```
hg_security.set_table_seclabel(tbl_oid oid, seclabel text)
```

参数说明：

- tbl\_oid
	指定对象的oid
- seclabel
	安全标记

设置表中某列的安全标记

```
hg_security.set_column_seclabel(tbl_oid oid,column_no integer,seclabel text )
```

参数说明：

- tbl\_oid
	指定表对象的oid
- column\_no
	指定表的列
- seclabel
	安全标记

示例：

设置oid为32838的用户安全标记，安全密级为s5，包含所有安全范围：

```
highgo=> select * from
hg_security.set_user_seclabel(32838,'s5:c0.c1023');

set_user_seclabel

-------------------------------------------

set

(1 行记录)
```

将oid为32783的表的第1列安全标记设置为安全密级为s1,安全范围包含c0和c3：

```
highgo=> select * from hg_security.set_column_seclabel(32783, 1,
's1:c0,c3');

set_column_seclabel

-------------------------------------------

set

(1 行记录)
```

### 查看安全标记

```
hg_security.get_user_seclabel(user_oid oid)
```

参数说明：

- user\_oid 指定用户的oid

查看表、视图、序列对象的安全标记

```
hg_security.get_table_seclabel(tbl_oid oid)
```

参数说明：

- tbl\_oid 指定对象的oid

查看表中某列的安全标记

```
hg_security.get_column_seclabel(tbl_oid oid,column_no integer)
```

参数说明：

- tbl\_oid
	指定表对象的oid
- column\_no
	指定表的列

### 安全标记的支配关系

在比较安全标记时，若标记L1安全密级大于等于标记L2的安全密级且L1安全范围包含L2的范围，则称L1支配L2。例如安全标记”s1:c0,c1,c2”支配标记”s0:c0,c1”。若安全密级和安全范围全部相等则称这两个安全标记相等。其余情况算作不可比较。

图8-2安全标记比较规则

## 强制访问控制规则

强制访问控制范围限定在所定义的主体和客体中，粒度是表级、记录级或字段级；主体可以读/写具有相关权限的客体，不可以读/写其不具有相关权限的客体。主体依据上写下读的原则对客体进行相关操作。

### 读访问规则

强制访问控制的读访问规则为：

1. 用户的安全密级必须大于等于对象的安全密级；
2. 用户的标记必须包含对象所有的安全范围。

如果用户满足以上两个规则，即可以对对象进行读取。比较的先后顺序是安全密级，安全范围。

### 写访问规则

强制访问控制的读访问规则为：

1. 对象的安全密级必须大于等于用户的安全密级；
2. 对象的标记必须包含用户所有的安全范围。

如果用户满足以上两个规则，即可以对对象进行写操作。比较的先后顺序是安全密级，安全范围。

如果两个标记的安全范围不属于支配与被支配的关系，那么这两个标记为不可比较的状态。安全标记不可比较那么就意味着不允许用户在这个对象上做所有增、删、改、查操作。

### 普通表强制访问控制规则

当表对象上没有安全标记时，即无表安全标记，无行安全标记，无列安全标记，那么表对象遵循自主访问控制。

当一个无安全标记的用户，去访问已被安全标记的表时，我们认为无安全标记的用户敏感度低于被安全标记的表。他们仍然遵循上写下读原则，即无安全标记的用户可以向被安全标记的表中写入数据，而没有权限查询表中数据。

更详细的访问控制规则参考下表：

图8-3普通表强制访问控制规则

### 继承表/分区表强制访问控制规则

继承表和分区表相较于普通表的访问控制规则稍有差异。具体规则如下：

- 单独开启行级安全：
1. 应用行级安全控制
	(1) 可以分别给主表和子表应用行级安全（分区表需要先给主表应用）。
2. 打开行安全控制
	(1) 可以分别给主表和子表打开行级安全。
3. 关闭行安全控制
	(1) 可以分别给主表和子表关闭行级安全。
4. 删除行安全控制
	(1) 分区表：只能在主表删除行级安全，并且是将所有表的\_hg\_seclabel\_列（隐藏列，用于存储行安全标记）删除。
	(2) 继承表：如果只在子表或者父表应用了行级安全，只需要执行删除自己的行级安全；如果在父表和子表都应用了行级安全，需要先删除主表的行级安全，才能删除子表的行级安全。
	

图8-4继承表/分区表开启行级安全控制规则

- 开启表级安全列级安全：
1. 父表设置安全标签
	(1) 父表会受强制访问控制，子表不受强制访问控制。
2. 子表设置安全标签
	(1) delete/update/select操作：父表和子表都会受强制访问控制。
	(2) insert操作：父表不受强制访问控制，子表受强制访问控制。
3. 同时设置安全标记
	(1) delete/update/select操作：对父表进行操作时，需要同时遵循父表和子表的标记比较规则。
	(2) insert操作：只需遵循本表的标记比较规则。

图8-5继承表/分区表开启表级/列级安全控制规则

## 强制访问控制模块使用

### 开启表级强制访问控制示例

登录syssso数据库管理员用户

打开强访模块的总开关和表级安全开关

```
highgo=# \c highgo syssso

hgdb-client-V9.0.5

您现在已经连接到数据库 "highgo",用户 "syssso".

highgo=> alter system set hg_sysmac.global_on=on;

ALTER SYSTEM

highgo=> alter system set hg_sysmac.global_table_level=on;

ALTER SYSTEM

highgo=> select pg_reload_conf();

切换到highgo用户创建用户u1 u2

highgo=# \c highgo highgo

hgdb-client-V9.0.5

您现在已经连接到数据库 "highgo",用户 "highgo".

highgo=# create user u1 password 'highgo';

CREATE ROLE

highgo=# create user u2 password 'highgo';

CREATE ROLE

highgo=> \c highgo u1

hgdb-client-V9.0.5

您现在已经连接到数据库 "highgo",用户 "u1".

highgo=> create table t1 (id int);

CREATE TABLE

highgo=> insert into t1 values(1),(2),(3);

INSERT 0 3

highgo=> grant all on t1 to u2;

highgo=> \c - u2

hgdb-client-V9.0.5

您现在已经连接到数据库 "highgo",用户 "u2".

highgo=> create table t2(name text);

CREATE TABLE

highgo=> insert into t2 values('zhangsan'),('wangwu'),('lisi');

INSERT 0 3

highgo=> grant all on t2 to u1;

GRANT

分别给用户u1 u2表t1 t2设置安全标记

highgo=> \c highgo syssso

hgdb-client-V9.0.5

您现在已经连接到数据库 "highgo",用户 "syssso".

highgo=> select * from
hg_security.set_user_seclabel('u1'::regrole,'s1:c0.c1023');

set_user_seclabel

-----------------------------------

set

(1 行记录)

highgo=> select * from
hg_security.set_user_seclabel('u2'::regrole,'s2:c0.c1023');

set_user_seclabel

------------------------------------

set

(1 行记录)

highgo=> select * from
hg_security.set_table_seclabel('t1'::regclass,'s1:c0.c1023');

set_table_seclabel

------------------------------------

set

(1 行记录)

highgo=> select * from
hg_security.set_table_seclabel('t2'::regclass,'s2:c0.c1023');

set_table_seclabel

------------------------------------

set

(1 行记录)

验证u2用户可以读取安全标记等级低的表t1的数据，但无法写入t1

highgo=> \c - u2

hgdb-client-V9.0.5

您现在已经连接到数据库 "highgo",用户 "u2".

highgo=> select * from t1;

id

----

1

2

3

(3 行记录)

highgo=> insert into t1 values(4);

2025-11-21 17:59:17.044 CST [17213] 错误: permission deined: violate
insert rules on t1

2025-11-21 17:59:17.044 CST [17213] 语句: insert into t1 values(4);

错误: permission deined: violate insert rules on t1

验证u1用户可以写入安全标记等级高的表t1，但无法读取t1表的数据

highgo=> \c highgo u1

hgdb-client-V9.0.5

您现在已经连接到数据库 "highgo",用户 "u1".

highgo=>

highgo=> insert into t2 values('u1data');

INSERT 0 1

highgo=> select * from t2;

2025-11-21 18:03:01.785 CST [18672] 错误: permission deined: violate
select rules on t2

2025-11-21 18:03:01.785 CST [18672] 语句: select * from t2;

错误: permission deined: violate select rules on t2
```

### 开启表级和行级强制访问控制

查看全局行安全开关的状态

```
highgo=> \c highgo syssso

hgdb-client-V9.0.5

您现在已经连接到数据库 "highgo",用户 "syssso".

highgo=>

highgo=> show hg_sysmac.global_row_level;

hg_sysmac.global_row_level

-------------------------------------------------

on

(1 行记录)

对指定表t1 t2应用行安全

highgo=> select * from
hg_security.apply_row_policy('t1'::regclass,'apply');

apply_row_policy

-------------------------------------------------

set

(1 行记录)

highgo=> select * from
hg_security.apply_row_policy('t2'::regclass,'apply');

apply_row_policy

-------------------------------------------------

set

(1 行记录)

查询表t1 t2的安全标记

highgo=> select * from
hg_security.get_table_seclabel('t1'::regclass);

get_table_seclabel

-------------------------------------------------

s1:c0.c1023

(1 行记录)

highgo=> select * from
hg_security.get_table_seclabel('t2'::regclass);

get_table_seclabel

-------------------------------------------------

s2:c0.c1023

(1 行记录)

查看u1 u2用户的安全标记

highgo=> select * from hg_security.get_user_seclabel('u1'::regrole);

get_user_seclabel

-------------------------------------------------

s1:c0.c1023

(1 行记录)

highgo=>

highgo=> select * from hg_security.get_user_seclabel('u2'::regrole);

get_user_seclabel

-------------------------------------------------

s2:c0.c1023

(1 行记录)

u1用户向t2表插入数据

highgo=> insert into t2 values('u1data');

INSERT 0 1

u1用户查询t2表，因为表安全优先级高于行安全，u1用户安全级别低于t2表，所以u1还是无权限查看这个表。

highgo=> select * from t2;

2025-11-21 18:32:26.775 CST [25553] 错误: permission deined: violate
select rules on t2

2025-11-21 18:32:26.775 CST [25553] 语句: select * from t2;

错误: permission deined: violate select rules on t2

我们创建u3用户，安全标记为"s3:c0.c1023"

highgo=> \c highgo highgo

hgdb-client-V9.0.5

您现在已经连接到数据库 "highgo",用户 "highgo".

highgo=#

highgo=# create user u3 password 'highgo';

CREATE ROLE

highgo=# \c highgo syssso

hgdb-client-V9.0.5

您现在已经连接到数据库 "highgo",用户 "syssso".

highgo=> select * from
hg_security.set_user_seclabel('u3'::regrole,'s3:c0.c1023');

set_user_seclabel

-------------------------------------------------

set

(1 行记录)

highgo=> \c highgo u2

hgdb-client-V9.0.5

您现在已经连接到数据库 "highgo",用户 "u2".

highgo=> grant all on t2 to u3;

GRANT

u3用户访问t2表数据，因为u3安全标记等级高于t2表和t2表中的行安全标记，所以能访问t2表的所有行的数据

highgo=> \c highgo u3

hgdb-client-V9.0.5

您现在已经连接到数据库 "highgo",用户 "u3".

highgo=> select * from t2;

name

-------------------------------------------------

zhangsan

wangwu

lisi

u1data

(4 行记录)
```

### 开启表级和列级强制访问控制

```
开启列级访问控制开关

highgo=> c - syssso

hgdb-client-V9.0.5

您现在已经连接到数据库 "highgo",用户 "syssso".

highgo=> alter system set hg_sysmac.global_column_level=on;

ALTER SYSTEM

highgo=# select pg_reload_conf();

2025-11-21 19:57:53.285 CST [31388] 日志: 接收到 SIGHUP, 重载配置文件

pg_reload_conf

-------------------------------

t

(1 行记录)

创建用户及测试表

highgo=> \c - highgo

hgdb-client-V9.0.5

您现在已经连接到数据库 "highgo",用户 "highgo".

highgo=# create user u4 password 'highgo';

CREATE ROLE

highgo=# create user u5 password 'highgo';

CREATE ROLE

highgo=# \c highgo u4

hgdb-client-V9.0.5

您现在已经连接到数据库 "highgo",用户 "u4".

highgo=> create table t4 (id int,name varchar(20));

CREATE TABLE

highgo=> grant all on t4 to u5;

GRANT

安全员用户给用户/表/列设置安全标记，用户设置s1,表设置s1，列设置s3

highgo=> \c highgo syssso

hgdb-client-V9.0.5

您现在已经连接到数据库 "highgo",用户 "syssso".

highgo=> select hg_security.set_user_seclabel('u4'::regrole,
's1:c0,c1');

set_user_seclabel

-------------------------------------------------

set

(1 行记录)

highgo=> select hg_security.set_user_seclabel('u5'::regrole,
's0:c0,c1');

set_user_seclabel

-------------------------------------------------

set

(1 行记录)

highgo=> select hg_security.set_table_seclabel('t4'::regclass,
's1:c0,c1');

set_table_seclabel

-------------------------------------------------

set

(1 行记录)

highgo=> select hg_security.set_column_seclabel('t4'::regclass, 2,
's3:c0,c1');

set_column_seclabel

----------------------------------------

set

(1 行记录)

使用u4用户新增数据

highgo=> \c - u4

hgdb-client-V9.0.5

您现在已经连接到数据库 "highgo",用户 "u4".

highgo=>

highgo=> insert into t4 values(1,'zhangsan');

INSERT 0 1

highgo=> insert into t4 values(2);

INSERT 0 1

u5用户向安全级别高的表和列中插入数据成功

highgo=>\c - u5

hgdb-client-V9.0.5

您现在已经连接到数据库 "highgo",用户 "u5".

highgo=> insert into t4 values(2,'lisi');

INSERT 0 1

修改u5用户的安全级别高于表和列的安全级别

highgo=> \c - syssso

hgdb-client-V9.0.5

您现在已经连接到数据库 "highgo",用户 "syssso".

highgo=>

highgo=> select hg_security.set_user_seclabel('u5'::regrole,
's5:c0,c1');

set_user_seclabel

-------------------------------------------------

set

(1 行记录)

可以看到u5安全级别高于表和列时，可以访问表中的数据

highgo=> \c - u5

hgdb-client-V9.0.5

您现在已经连接到数据库 "highgo",用户 "u5".

highgo=>

highgo=> select * from t4;

id | name

-------+-----------------------------------------

1 | zhangsan

2 |

2 | lisi

(3 行记录)
```