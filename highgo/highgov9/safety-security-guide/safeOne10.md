---
title: "安全审计"
book: "安全指南"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/safety/safeOne10.html"
tags:
  - highgo
  - highgo-v9
  - safety-security-guide
---

## 安全审计

安全审计模块用于监视并记录对数据库服务器的各类操作行为，通过对网络数据的分析，实时、智能地解析对数据库服务器的各种操作，来帮助用户事后生成合规报告、事故追根溯源，以进一步提高数据安全。

数据库审计技术可以监控和审计用户对数据库对象的创建、修改和删除等操作，分析内容可以精确到SQL操作语句一级；还可以根据设置的规则，智能地判断出违规操作数据库的行为，并对违规行为进行记录、报警。瀚高数据库提供权限审计、用户审计、对象审计、语句审计、系统审计和强制审计六种审计维度，方便用户选择最适合的方式配置审计策略。

数据库审计员可自定义需要审计的用户及操作行为，此过程称为审计策略配置；其中的”操作”（如CREATE  
TABLE）称为审计事件（或审计策略）。安全审计模块会将特定操作记录审计日志，每一条审计产生的数据称为一条审计记录。

## 审计开关

瀚高数据库中对安全审计模块设置了开关。审计功能打开时，我们配置的审计策略才会生效。审计功能关闭时，数据库不会发生审计动作，也无法将审计配置应用到数据库中。

audit.enable为设置安全审计功能是否开启的总开关，取值为on和off，缺省为off。

on表示打开审计功能；

off表示关闭审计功能；

您可以通过以下几种方式打开或关闭审计开关，另外，其他安全审计相关参数也可参照如下方式修改。

在瀚高数据库启动之前，修改postgresql.conf文件，将audit.enable参数设置为on或off。

在瀚高数据库启动之后，通过SQL命令修改：

ALTER SYSTEM SET audit.enable=on;

重启服务生效

## 审计模式

瀚高数据库支持两种审计模式，分别为通用模式和专用模式。通过参数audit.privimode来实现，参数可选值为1，2。默认为1。1代表通用模式，表示数据库审计员有权限查看所有审计日志；2代表专用模式，表示数据库安全员有权对普通用户和数据库审计员的行为进行审计，数据库审计员有权对数据库安全员和数据库管理员的行为进行审计。

## 审计配置

想要对用户某行为进行审计，首先需要打开审计功能，然后再进行审计配置。

### 审计参数配置

下文列出了审计相关的参数，只有超级用户或数据库审计员有权限查看和配置审计参数。所有审计参数均为重启服务生效。

| 参数 | 子参数 | 参数含义 |
| --- | --- | --- |
| audit.enable |  | 安全审计总开关on：表示打开安全审计off：表示关闭安全审计（默认） |
| audit.privimode |  | 指定审计模式1：表示通用模式（默认）2：表示专用模式 |
| audit.retentionpolicy |  | 审计日志保留策略，按时间或空间保存日志。time：按照时间方式保存日志（默认）space：按照空间方式保存日志 |
|  | audit.retentiondays | 审计日志保存天数默认180天，超180天覆盖。audit.retentionpolicy=time时本参数生效 |
|  | audit.detectiontime | 定时任务检测时间，将超过时间的日志删除，默认为1天。audit.retentionpolicy=time时本参数生效 |
|  | audit.spacelimit | 最大允许使用空间。默认为磁盘空间，默认10G；audit.retentionpolicy=space时本参数生效。磁盘空间达到使用最大值，停止审计。 |
|  | audit.spacealarm | 空间使用超阀值告警，用于指定一个百分比，默认0.8，audit.retentionpolicy=space时本参数生效 |
| audit.archdir |  | 指定审计日志本地自动归档路径。 |
| audit.remote\_archdir |  | 指定审计日志远程自动归档路径。参数默认值为空，表示关闭远程归档。参数配置格式为：user@ip:/xxx/dir,如 [highgo@192.168.94,129:/tem/test](mailto:highgo@192.168.94,129:/tem/test) 启用远程归档，需要首先保证两台服务器建立互信。注：本参数为9.0.5版本新增参数。 |
| audit.systemopers |  | 系统审计开关off：表示不对系统审计事件进行审计；（默认）succ：表示只对成功的系统审计事件进行审计；fail：表示只对失败的系统审计事件进行审计；all：表示成功和失败皆审计。 |
| audit.sqlitedbpath |  | 配置sqilte数据库的路径默认路径：$PGDATA/pgaudit/sqlite/sqlite.db |
| audit.monitoring |  | 安全监测的开关可取值on、off，默认值为off注：本功能为V9.0.5版本新增功能。 |
| audit.mail |  | 阈值告警发送的邮件地址注：本功能为9.0.5版本新增功能。 |

### 审计策略配置

瀚高数据库提供权限审计、用户审计、对象审计、语句审计、系统审计和强制审计六种审计维度，数据库审计员可以选定某些维度对审计策略进行配置。需要注意的是，审计策略配置属于数据库级别的操作，即在当前库配置的审计策略只在当前库生效。

#### 语句审计

语句审计指在数据库管理系统范围内，对数据库拥有的结构或模式对象进行操作时引发的事件进行审计，这类结构或模式对象并不指具体的某个结构或模式对象，而是一类结构或模式对象的泛称。一般包括数据库管理系统提供的DDL、DML、DQL、DCL、TCL等语句引发的事件。

配置语句审计：

```
hg_security.pg_audit_stmt(stmt_opts,whenever)
```

参数说明：

- stmt\_opts
	声明对应语句审计事件，详见下表，支持一次配置多个审计事件，多个审计事件使用英文逗号,分隔。配置all表示增加所有语句类型的权限审计配置。
- whenever
	审计时机。successful表示只审计成功的，fail表示只审计失败的。all或者无参数值均表示无论成功还是失败都进行审计。

取消语句审计：

```
hg_security.pg_noaudit_stmt(stmt_opts,whenever)
```

或者

```
hg_security.pg_noaudit_stmt_byoid(confid)
```

参数说明：

- stmt\_opts,whenever
	参见配置语句审计。
- confid
	表示要取消审计的审计配置项。

语句审计事件选项：

| 语句审计stmt\_opts |  |  |
| --- | --- | --- |
| create domain | alter trigger | comment |
| create procedure | alter view | reset |
| create index | alter materialized view | set |
| create sequence | alter extension | truncate |
| create function | drop domain | copy to |
| create table | drop function | copy from |
| create table as | drop procedure | reindex |
| create tablespace | drop index | lock |
| create trigger | drop sequence | call |
| create view | drop table | begin |
| create materialized view | drop tablespace | commit |
| create extension | drop trigger | rollback |
| alter domain | drop view | savepoint |
| alter function | drop materialized view | roll back to |
| alter procedure | drop extension | release |
| alter index | select | start transaction |
| alter system | select into | grant |
| alter sequence | insert | revoke |
| alter table | update | rollback prepared |
| alter tablespace | delete | create resource group |
| alter resource group | drop resource group |  |

---

语句审计示例：

拥有syssao\_role角色的审计管理员登录数据库；

打开安全审计开关；

```
highgo=# alter system set audit.enable =on;

ALTER SYSTEM
```

配置语句审计策略：审计用户创建表、删除表的事件；

```
highgo=> select hg_security.pg_audit_stmt('create table,drop table','all');

pg_audit_stmt

---------------------------------------------

Successfully configured statement audit policy!
```

配置语句审计策略：审计用户修改系统设置的事件；

```
highgo=> select hg_security.pg_audit_stmt('alter system,set','all');

pg_audit_stmt

---------------------------------------------

Successfully configured statement audit policy!
```

取消语句审计策略：取消用户修改系统设置的审计事件；

```
highgo=>select hg_security.pg_noaudit_stmt('alter system,set','all');

pg_noaudit_stmt

---------------------------------------------

Successfully canceled statement audit policy!
```

#### 对象审计

对象审计发生在具体的对象上的DML等操作，在审计配置时需要指定对象名及其模式名，只有对已配置的对象执行正确的操作才会触发对象审计。另外，用户需要在已有数据库对象上创建对象审计策略。

配置对象审计：

```
hg_security.pg_audit_object(object_opts,object_type,objname,schname,whenever)
```

参数说明：

- object\_opts
	对应对象审计事件，详见下表。配置all表示增加所有语句类型的对象审计配置。
- object\_type
	对象的类型，可取值有table、view、column、sequence、procedure、function等。
- object\_name
	对象的名称。支持指定column名称，例如支持objname.colname的格式，指定colname，表示对该列进行审计仅当objtype为column时才需要指定，不指定时会报错。
- schname
	对象所属模式名称。
- whenever
	审计时机。successful表示只审计成功的，fail表示只审计失败的。all或者无参数值均表示无论成功还是失败都进行审计。

取消对象审计：

```
hg_security.pg_noaudit_object(object_opts,object_type,objname,schname,whenever)
```

或者

```
hg_security.pg_noaudit_object_byoid(confid)
```

参数说明：

- object\_opts,object\_type,objname,schemaname,whenever
	参见上条
- confid
	要取消审计的审计配置项

对象审计事件选项：

---

| 对象类型 | object\_opts |
| --- | --- |
| table | insert |
|  | update |
|  | delete |
|  | select |
|  | lock |
|  | alter |
|  | comment |
|  | truncate |
|  | alter index |
|  | drop index |
| view | insert |
|  | update |
|  | delete |
|  | select |
|  | comment |
| column | insert |
|  | update |
|  | select |
| sequence | select |
|  | comment |
|  | alter |
|  | drop |
| procedure | call |
|  | alter |
|  | drop |
| function | select |
|  | alter |
|  | drop |

对象审计示例：

```
highgo=> select
hg_security.pg_audit_object('insert','table','tb1','public','fail');

pg_audit_object

---------------------------------------------

Successfully configured object audit policy!

highgo=> select
hg_security.pg_audit_object('insert','column','tb1.name','public','fail');

pg_audit_object

---------------------------------------------

Successfully configured object audit policy!

(1 行记录)
```

查看审计策略

```
highgo=> select * from pg_audit_config;

取消对象审计策略

highgo=> select
hg_security.pg_noaudit_object_byoid(32867);--32867是confid

pg_noaudit_object_byoid

---------------------------------------------

Successfully canceled statement audit policy!

(1 行记录)
```

#### 权限审计

权限审计是指审计数据库对象涉及的创建、删除、修改等操作引发的事件。

配置权限审计：

```
hg_security.pg_audit_privilege(stmt_opts,whenever)
```

参数说明：

- stmt\_opts
	对应权限审计事件，详见下表。配置all表示增加所有语句类型的权限审计配置。
- whenever
	审计时机。successful表示只审计成功的，fail表示只审计失败的。all或者无参数值均表示无论成功还是失败都进行审计。

取消权限审计：

```
hg_security.pg_noaudit_privilege(stmt_opts,whenever)
```

或者

```
hg_security.pg_noaudit_privilege_byoid(confid)
```

参数说明：

- stmt\_opts,whenever
	参见上条
- confid
	要取消审计的审计配置项

权限审计事件选项：

---

| 权限审计stmt\_opts |  |
| --- | --- |
| role | create role |
|  | grant role |
|  | revoke role |
|  | drop role |
|  | alter role |
| user | create user |
|  | alter user |
|  | drop user |
| schema | create schema |
|  | alter schema |
|  | drop schema |
| database | create database |
|  | alter database |
|  | drop database |

权限审计示例：

配置权限审计策略

```
highgo=> select hg_security.pg_audit_privilege('grant role,alter
role','all');

pg_audit_privilege

---------------------------------------------

Successfully configured privilege audit policy!

(1 行记录)

highgo=> select hg_security.pg_audit_privilege('drop role,drop
user,drop database','all');

pg_audit_privilege

---------------------------------------------

Successfully configured privilege audit policy!

查看权限审计策略

highgo=> select * from pg_audit_config where audittype ='p';
```

#### 用户审计

用户审计是指数据库用户涉及的DDL、DML、DQL、DCL、TCL等操作行为引发的审计事件。

配置用户审计：

hg\_security.pg\_audit\_user(stmt\_opts,username,whenever)

参数说明：

- stmt\_opts
	对应语句审计事件，详见下表
- username
	要审计的用户
- whenever
	审计时机。successful表示只审计成功的，fail表示只审计失败的。all或者无参数值均表示无论成功还是失败都进行审计

所有用户审计配置：

hg\_security.pg\_audit\_all\_user(stmt\_opts,whenever)

参数说明：

- stmt\_opts
	对应语句审计事件，详见附录，配置all表示增加所有语句类型的用户审计配置。
- whenever
	审计时机。successful表示只审计成功的，fail表示只审计失败的。all或者无参数值均表示无论成功还是失败都进行审计。

取消用户审计：

取消用户审计配置：

```
hg_security.pg_noaudit_user(stmt_opts,username,whenever)
```

或者

```
hg_security.pg_noaudit_user_byoid(confid)
```

参数说明：

- stmt\_opts,username,whenever
	参见上条
- confid
	要取消审计的审计配置项

取消所有用户审计配置：

hg\_security.pg\_noaudit\_all\_user(stmt\_opts,whenever)

参数说明：

- stmt\_opts,whenever
	参见上条

用户审计事件选项：

---

| 用户审计stmt\_opts |  |  |
| --- | --- | --- |
| create domain | alter trigger | comment |
| create procedure | alter view | reset |
| create index | alter materialized view | set |
| create sequence | alter extension | truncate |
| create function | drop domain | copy to |
| create table | drop function | copy from |
| create table as | drop procedure | reindex |
| create tablespace | drop index | lock |
| create trigger | drop sequence | call |
| create view | drop table | begin |
| create materialized view | drop tablespace | commit |
| create extension | drop trigger | rollback |
| alter domain | drop view | savepoint |
| aler function | drop materialized view | rollback to |
| alter procedure | drop extension | release |
| alter index | select | start transaction |
| alter system | select into | grant |
| alter sequence | insert | revoke |
| alter table | update | rollback prepared |
| alter tablespace | delete | create resource group |
| alter resource group | drop resource group |  |

用户审计示例：

配置用户审计策略

```
highgo=> select hg_security.pg_audit_user('create domain,create
index,alter extension','u1','all');

pg_audit_user

---------------------------------------------

Successfully configured user audit policy!

(1 行记录)

highgo=> select hg_security.pg_audit_user('lock','u2','fail');

pg_audit_user

---------------------------------------------

Successfully configured user audit policy!

查看对象审计策略

highgo=> select * from pg_audit_config where audittype ='u';

confid | actionname | auditoroid | objoid | classoid | objtype |
audittype | auditmode | enable

--------+-----------------+------------+-----------+----------+---------+-----------+-----------+--------

32874 | CREATE DOMAIN | 12247 | 32792.0.0 | 0 | none | u | a | t

32875 | CREATE INDEX | 12247 | 32792.0.0 | 0 | none | u | a | t

32876 | ALTER EXTENSION | 12247 | 32792.0.0 | 0 | none | u | a |
t

32877 | LOCK | 12247 | 32793.0.0 | 0 | none | u | f | t

(4 行记录)
```

#### 系统审计

系统审计是指审计数据库系统行为如数据库启动、数据库停止、数据库登入登出、数据库配置文件重载等操作引发的审计事件。系统审计不支持自定义审计事件配置。瀚高数据库提供audit.systemopers系统审计开关，有off、succ、fail、all四种选项。

off：表示不对系统审计事件进行审计；

succ：表示只对成功的系统审计事件进行审计；

fail：表示只对失败的系统审计事件进行审计；

all：表示成功和失败的系统审计事件皆审计。

| 操作类型 | sys\_opts |
| --- | --- |
| 数据库启动 | start |
| 数据库停止 | stop |
| 数据库登入 | login |
| 数据库登出 | logout |
| 数据库配置文件重载 | reload |
| 数据库GUC参数的修改 | alter\_guc |
| 主备切换 | SWITCH OVER |
|  | FAILOVER |
| 打开文件失败 | OPEN FILE FAIL |
| 死锁 | DEAD LOCK |
| 流复制 | WALSENDER CONN |
|  | WALSENDER EXIT |
| 可信信道 | CHANNEL |
| 主备GUC同步 | HGHAC SYNC GUC |
| 连接数超限 | LOGIN |
| 日志磁盘满 | LOG DISK FULL |
| wal归档失败 | EXEC CMD FAIL |
| 审计磁盘空间满 | DISK FULL |
| 审计磁盘已达上限 | SPACE LIMIT |
| 审计磁盘使用告警 | SPACE ALARM |
| wal重放 | RECOVERY DATA |
| 会话锁定和会话解锁 | Lock\_current\_session/unlock\_current\_session |
| pgagent启动和关闭 | START/STOP PGAGENT |

#### 强制审计

强制审计指的是记录安全审计开关的启动和关闭两种行为引发的审计事件。当用户修改审计总开关audit.enable时，就会触发强制审计。强制审计事件不支持用户自定义。

### 查看审计策略

提供pg\_audit\_config系统表存储用户已配置的审计策略，超级用户或数据库审计员有权限查看所有审计策略。一个审计配置项对应系统表中的一条记录。当配置用户审计指定了多个用户名，则一个用户名形成一个审计配置项。

### 审计配置清空

提供hg\_security.pg\_clean\_audit\_config()函数，用于清空审计配置，超级用户或数据库审计员有权限做清空操作。

### 审计配置删除

提供hg\_security.pg\_delete\_audit\_config(confid)函数，confid表示审计配置项ID，用于删除审计配置，超级用户或数据库审计员有权限做删除操作。

## 审计记录

### 审计信息存储

瀚高数据库审计信息存储在审计表hg\_security.pg\_audit\_log中，对于审计事件无法保存到数据库表中的特殊的事件，当HGDB恢复正常运行后，通过外部表访问的方式来读取审计表hg\_security.sqlite\_audit\_log。

另外，当用户配置了语句审计alter table，同时配置了对象审计table  
alter，那么当用户触发该审计事件时，会在审计表hg\_security.pg\_audit\_log中产生2条审计记录，但是2条审计记录的审计类型是不同的。

### 审计记录查询

审计策略配置和审计日志查询都属于数据库级别的操作。数据库审计员或数据库安全员可以查看用户在当前库配置的审计策略或触发的审计记录。假如我们在testdb库中配置了用户审计策略”pg\_audit\_user(‘all’,’zhangsan’,’all’);”然后zhangsan用户在testdb库中做了一些操作。那么我们可以登录testdb这个库，查询hg\_security.pg\_audit\_log表，即可以看到zhangsan用户触发的审计操作。

审计记录包含以下信息：

---

| 列名 | 说明 |
| --- | --- |
| confid | 审计配置项OID |
| sessionoid | 会话ID |
| username | 用户/角色标识及所属组名称 |
| useroid | 用户/角色标识及所属组OID |
| audittime | 事件的日期和时间 |
| result | 事件结果 |
| namespacename | 数据库模式和对象名称 |
| namespaceid | 数据库模式和对象标识 |
| classid | 对象或用户所在系统表OID |
| objecttype | 对象类型 |
| audittype | 审计类型 |
| actionname | 操作类型 |
| clientmac | 客户端MAC地址 |
| clientip | 客户端IP |
| clientport | 客户端端口号 |
| clientname | 客户端名称 |
| clientappname | 客户端程序名称 |
| sqltext | 执行的命令 |
| errtext | 执行失败时的错误消息 |
| commandid | 事务相关ID |
| authmethod | 认证方式 |
| colname | 列名 |
| privlevel | 权限级别 |
| roleoid | 角色对象OID |
| rolename | 角色对象名称 |
| objectoid | 对象OID |
| objectname | 对象名称 |

---

### 查看审计日志所占磁盘情况

可以通过配置audit.spacelimit、audit.spacealarm参数来限制审计日志所占磁盘空间，分为如下3种情况：

当审计日志使用空间到达audit.spacealarm值时，产生审计告警；

当审计日志使用空间到达audit.spacelimit值时，产生审计告警，并暂停审计；

当审计日志的磁盘空间已满，产生审计告警，并暂停审计；

提供hg\_security.show\_audit\_diskinfo视图用于查看审计日志所占磁盘情况，视图信息如下

---

| disk\_size | disk\_used | disk\_used% | Space\_limit | Table\_used | Avail | Table\_used% | Alarm |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 磁盘大小 | 已使用磁盘空间 | 已使用磁盘百分比 | 审计日志允许使用大小 | 审计日志已使用空间大小 | 审计日志剩余可使用空间大小 | 使用百分比 | 告警值 |

### 管理审计记录

#### 审计记录保留策略

瀚高数据库支持审计日志所在的磁盘空间管理，审计日志保留策略可选时间和空间两个维度。使用方法详见9.3.1章节audit.retentionpolicy相关内容。

#### 清空、删除审计表

支持由数据库审计员用户清空、删除审计表，通过内置函数hg\_security.pg\_clean\_auditlog()实现审计表清空；通过内置函数hg\_security.pg\_delete\_auditlog(timestamp  
endtime)来实现审计表删除数据，其中参数endtime指定审计日志的时间，表示删除该时间点之前的审计日志。如果同时配置了保留策略那么审计保留策略优先，保留策略内的数据记录将不会被删除。

#### 审计日志归档

瀚高数据库管理系统V9.0.5之前的版本支持审计日志的本地自动归档和手动归档，V9.0.5及之后的版本新增支持审计日志的远程自动归档。

配置audit.archdir参数指定审计日志本地自动归档路径，即启用审计日志本地自动归档功能；配置audit.remote\_archdir参数即启用审计日志远程自动归档功能，审计日志将会定期备份至指定的远端服务目录中。参数使用情况详见”审计参数配置”章节。

当配置本地自动归档和远程自动归档后，系统将使用copy的方式整点执行归档操作，当前归档文件会循环覆盖前一个归档文件。

提供函数hg\_security.pg\_audit\_file\_archive()用于审计日志的手动归档，通用模式下数据库审计员执行该函数，表示将审计日志归档到audit.archdir配置的归档目录下；专用模式下数据库安全员和数据库审计员均可执行该函数，表示将对应被审计角色的审计日志归档到audit.archdir配置的归档目录下，如果未设置归档目录，则审计日志归档操作执行失败。

## 安全监测

安全监测指在基础审计功能的基础上，按照用户定义的规则实时的对数据库系统进行监测。

安全监测的监测目标是已配置的审计事件，当监测发现目标审计事件后，生成对应的安全事件；随后按照用户给出的规则判断此安全事件是否达到阈值，若达到阈值则根据此安全事件的等级进行不同的处理。

数据库审计员或超级用户有权限通过一系列SQL内置函数来创建、修改和删除监测规则。

安全监测功能是V9.0.5版本新增功能。

### 创建安全监测规则

安全监测规则需要在已有审计配置的基础上进行创建。

创建安全监测规则：

```
hg_security.pg_create_secmon_rule(rulename text,

audconfoid oid,

monmode text,

enabled boolean

)
```

参数说明：

- rulename
	规则名称，由用户自己定义
- audconfoid
	对应已存在的审计配置id
- monmode
	审计配置规则的监测模式
	可选值为successful、faild、all
	分别表示监测当前审计事件的成功、失败和所有的情况
	此处允许与当前审计事件的审计实际不一致
- enabled
	安全监测规则是否启动

返回值说明：

- returns oid
	返回所创建监测规则的id

### 修改安全监测规则

```
hg_security.pg_alter_secmon_rule(ruleoid oid,

rulename text,

monmode text,

enabled boolean

)
```

参数说明：

- ruleoid
	被修改监测规则的oid
- rulename
	规则名称
- monmode
	修改监测模式，无参数值表示保留原值
- enabled
	安全监测规则是否启动，无参数值表示保留原值

返回值说明：

- returns oid
	返回所修改监测规则的id

删除安全监测规则

hg\_security.pg\_drop\_secmon\_rule(ruleoid oid

)

参数说明：

- ruleoid
	所删除监测规则的oid

返回值说明：

- returns oid
	返回所删除监测规则的id

### 监测规则的存储

提供系统表pg\_secmon\_rule用于存储用户创建的安全监测规则。系统表里记录的内容包括规则名称，审计配置id，安全监测模式等信息。pg\_secmon\_rule表中记录的安全监测模式与之前的审计时机相同分别记为成功（”  
s “）、失败（” f “）和所有（” a “）。

### 监测历史的存储

提供普通表hg\_security.pg\_secmon\_history用于存储安全监测的历史记录，触发安全规则的审计事件均被记录到该表中。表中记录的内容包括规则oid、审计配置id、操作类型、会话id、安全事件发生的时间、命令、安全检测规则名称等信息。

## 安全监测阈值

数据库审计员或超级用户有权限设置安全监测规则的阈值，一旦触发安全阈值，数据库会采取不同的行为对用户进行告警。

安全监测阈值功能是V9.0.5版本新增功能。

### 阈值的配置形式

安全监测阈值分为3种形式，我们在创建一条安全监测阈值时，只能选择一种形式的阈值进行创建。

1. 最大值阈值

一段时间间隔内，发生同一安全事件的次数。

2. 序列阈值

一段时间间隔内，同一session连续发生一系列安全事件。

3. 一次性阈值

包括基线阈值（ALTER SYSTEM）、重要时刻、重要列。

### 阈值的等级

安全监测阈值分为4个等级，分别对应不同的数据库行为及采取的操作：

1级：服务器日志形式报警。

2级：服务器日志形式报警，邮件形式报警。

3级：服务器日志形式报警，邮件形式报警，结束对应SESSION。

4级：服务器日志形式报警，邮件形式报警，结束对应SESSION， 并且锁定用户。

### 创建安全监测阈值

```
hg_security.pg_create_secmon_threshold(thrname text,

secmonseq oidvector,

interval int,

maxtimes int,

basename text,

basevalue text,

starttime timestamptz,

endtime timestamptz,

columns int2vector,

level int,

enabled boolean

)
```

参数说明：

- thrname
	阈值名称，用户自己定义
- secmonseq
	对应一个或一组监测规则id，由逗号分隔。配置一组监测规则id代表序列形式的阈值。
- interval
	间隔时间（单位分钟）
- maxtimes
	间隔时间内发生安全事件的最大次数（>0），配置为序列阈值时要求最大次数只能设置为1。
- basename
	GUC参数名称，基线阈值目前只支持alter system
- basevalue
	GUC参数值，基线阈值目前只支持alter system
- starttime
	一次性阈值中重要时刻的起始时间
- endtime
	一次性阈值中重要时刻的起始时间
- columns
	重要列，审计配置为对象审计才可设置重要列。
- level
	阈值等级，用于设置触发阈值时的数据库后续处理方式。
- enabled
	阈值是否启动

返回值说明：

- returns oid
	返回所创建监测阈值的id

### 修改安全监测阈值

```
hg_security.pg_alter_secmon_threshold(throid oid,

thrname text,

interval int,

maxtimes int,

basename text,

basevalue text,

starttime timestamptz,

endtime timestamptz,

columns int2vector,

level int,

enabled boolean

)
```

参数说明：

- throid
	被修改阈值的id
- thrname
	阈值名称，用户自己定义
- interval
	间隔时间（单位分钟）
- maxtimes
	间隔时间内发生安全事件的最大次数（>0），配置为序列阈值时要求最大次数只能设置为1。
- basename
	GUC参数名称，基线阈值目前只支持alter system
- basevalue
	GUC参数值，基线阈值目前只支持alter system
- starttime
	一次性阈值中重要时刻的起始时间
- endtime
	一次性阈值中重要时刻的起始时间
- columns
	重要列，审计配置为对象审计才可设置重要列。
- level
	阈值等级，用于设置触发阈值时的数据库后续处理方式。
- enabled
	阈值是否启动

返回值说明：

- returns oid
	返回所修改监测阈值的id

### 删除安全监测阈值

```
hg_security.pg_drop_secmon_threshold(throid oid)
```

参数说明：

- throid
	被删除监测阈值的id

返回值说明：

- returns oid
	返回所删除监测阈值的id

### 阈值配置的存储

提供系统表pg\_secmon\_threshold用于存储用户创建的安全监测阈值。系统表里记录的内容包括阈值名称、监测规则id、触发安全监测阈值的时间、阈值等级等信息。

### 阈值历史记录的存储

提供表hg\_security.pg\_secmon\_thrhis用于存储已触发安全监测阈值的审计事件等信息。

### 清空安全监测规则及阈值配置

提供内置函数hg\_security.pg\_clean\_secmon\_config()用于清空所有安全监测配置和阈值配置。

### 清空安全监测历史及阈值检查结果

提供内置函数hg\_security.pg\_clean\_secmon\_history()用于清空所有安全监测历史和阈值检查结果。

## 安全监测及阈值配置方法

一次性阈值之重要时刻的监测示例

打开安全审计和安全监测开关，重启数据库生效

```
highgo=> alter system set audit.enable =on;

ALTER SYSTEM

highgo=> alter system set audit.monitoring =on;

ALTER SYSTEM

配置语句审计策略

highgo=> select * from hg_security.pg_audit_stmt('delete');

pg_audit_stmt

-------------------------------------------------

Successfully configured statement audit policy!

(1 行记录)
```

查看审计配置系统表，获取confid

```
highgo=> select confid from pg_audit_config where
actionname='DELETE';

confid

--------

32779

(1 行记录)
```

创建安全监测规则

```
highgo=> select * from
hg_security.pg_create_secmon_rule('rule1',32779,'successful',true);

pg_create_secmon_rule

-----------------------

32780

(1 行记录)
```

查看安全监测配置系统表，获取ruleoid

```
highgo=> select ruleoid from pg_secmon_rule where confid = 32779;

ruleoid

---------

32780

(1 行记录)
```

创建安全监测阈值

```
highgo=> select * from

hg_security.pg_create_secmon_threshold('thr1','{32780}',1,1,NULL,NULL,

'20251030 12:00:00','20251230 12:00:00',NULL,1,true);

pg_create_secmon_threshold

----------------------------

32782

(1 行记录)
```

查看安全监测阈值配置系统表

```
highgo=> select * from pg_secmon_threshold ;
```

触发重要时刻阈值

```
highgo=# create table tb1(id int);

CREATE TABLE

highgo=# insert into tb1 values(123),(456);

INSERT 0 2

highgo=# delete from tb1 where id =123;

DELETE 1
```

查看审计日志

```
highgo=> select * from hg_security.pg_audit_log;
```

查看安全监测历史

```
highgo=> select * from hg_security.pg_secmon_history;

audittime | ruleoid | confid | actionname | session | commandid |
rulename

-------------------------------+---------+--------+------------+---------+-----------+----------

2025-11-07 11:47:59.202252+08 | 32780 | 32779 | DELETE | 1015 | 0
| rule1

(1 行记录)
```

查看安全监测阈值历史

```
highgo=> select * from hg_security.pg_secmon_thrhis;
```

一次性阈值之基线阈值的监测示例

配置语句审计策略

```
highgo=> select * from hg_security.pg_audit_stmt('alter system');

pg_audit_stmt

-------------------------------------------------

Successfully configured statement audit policy!
```

(1 行记录)

查看审计配置系统表，获取confid

```
highgo=> select confid from pg_audit_config where actionname='ALTER
SYSTEM';

confid

--------

32786

(1 行记录)
```

创建安全监测规则

```
highgo=> select * from
hg_security.pg_create_secmon_rule('rule2',32786,'successful',true);

pg_create_secmon_rule

-----------------------

32787

(1 行记录)
```

查看安全监测配置系统表，获取ruleoid

```
highgo=> select ruleoid from pg_secmon_rule where confid = 32786;

ruleoid

---------

32787

(1 行记录)
```

创建安全监测阈值

```
highgo=> select * from

hg_security.pg_create_secmon_threshold('thr2','{32787
}',1,1,'audit.retentiondays','10',NULL,NULL,NULL,1,true);

pg_create_secmon_threshold

----------------------------

32788

(1 行记录)
```

查看安全监测阈值配置系统表

```
highgo=> select * from pg_secmon_threshold ;
```

触发基线阈值

```
highgo=> alter system set audit.retentiondays = 60;
```

查看审计日志

```
highgo=> select * from hg_security.pg_audit_log;
```

查看安全监测历史

```
highgo=> select * from hg_security.pg_secmon_history;
```

查看安全监测阈值历史

```
highgo=> select * from hg_security.pg_secmon_thrhis;
```

一次性阈值之重要列阈值的监测示例

配置对象审计策略

```
highgo=# create table tb2(id int);

highgo=> select * from
hg_security.pg_audit_object('select','column','tb2.id');
```

查看审计配置系统表，获取confid

```
highgo=> select confid from pg_audit_config where actionname='SELECT'
and objtype = 'column' ;

confid

--------

32792

(1 行记录)
```

创建安全监测规则

```
highgo=> select * from
hg_security.pg_create_secmon_rule('rule3',32792,'successful',true);
```

查看安全监测配置系统表，获取ruleoid

```
highgo=> select ruleoid from pg_secmon_rule where confid = 32792;

ruleoid

---------

32793

(1 行记录)
```

创建安全监测阈值

```
highgo=> select * from

hg_security.pg_create_secmon_threshold('thr3','{32793}',1,1,NULL,NULL,NULL,NULL,'1',1,true);

pg_create_secmon_threshold

----------------------------

32794

(1 行记录)
```

查看安全监测阈值配置系统表

```
highgo=> select * from pg_secmon_threshold ;
```

触发重要列阈值

```
highgo=# select id from tb2;
```

查看审计日志

```
highgo=> select * from hg_security.pg_audit_log;
```

查看安全监测历史

```
highgo=> select * from hg_security.pg_secmon_history;
```

查看安全监测阈值历史

```
highgo=> select * from hg_security.pg_secmon_thrhis;
```

最大值阈值的监测示例

配置权限审计策略

```
highgo=> select * from hg_security.pg_audit_privilege('create
role');

pg_audit_privilege

-------------------------------------------------

Successfully configured privilege audit policy!

(1 行记录)
```

查看审计配置系统表，获取confid

```
highgo=> select confid from pg_audit_config where actionname='CREATE
ROLE';

confid

--------

32796

(1 行记录)
```

创建安全监测规则

```
highgo=> select * from
hg_security.pg_create_secmon_rule('rule4',32796,'successful',true);

pg_create_secmon_rule

-----------------------

32797

(1 行记录)
```

查看安全监测配置系统表，获取ruleoid

```
highgo=> select ruleoid from pg_secmon_rule where confid = 32796;

ruleoid

---------

32797

(1 行记录)
```

创建安全监测阈值

```
highgo=> select * from

hg_security.pg_create_secmon_threshold('thr4','{32797}',30,3,NULL,NULL,NULL,NULL,NULL,1,true);

pg_create_secmon_threshold

----------------------------

32798

(1 行记录)
```

查看安全监测阈值配置系统表

```
highgo=> select * from pg_secmon_threshold;
```

触发最大值阈值

```
create role test1;

create role test2;

create role test3;
```

查看审计日志

```
highgo=> select * from hg_security.pg_audit_log;
```

查看安全监测历史

```
highgo=> select * from hg_security.pg_secmon_history;
```

查看安全监测阈值历史

```
highgo=> select * from hg_security.pg_secmon_thrhis;
```

序列阈值的监测示例

配置语句审计策略

```
highgo=> select * from hg_security.pg_audit_stmt('create table');

highgo=> select * from hg_security.pg_audit_stmt('insert');

highgo=> select * from hg_security.pg_audit_stmt('delete');
```

查看审计配置系统表，获取confid

```
highgo=> select confid from pg_audit_config where actionname='CREATE
TABLE';

highgo=> select confid from pg_audit_config where
actionname='INSERT';

highgo=> select confid from pg_audit_config where
actionname='DELETE';
```

创建安全监测规则

```
highgo=> select * from
hg_security.pg_create_secmon_rule('rule5',32802,'successful',true);

highgo=> select * from
hg_security.pg_create_secmon_rule('rule6',32803,'successful',true);

highgo=> select * from
hg_security.pg_create_secmon_rule('rule7',32779,'successful',true);
```

根据创建安全监测规则返回的ruleoid,创建安全监测阈值

```
highgo=> select * from

hg_security.pg_create_secmon_threshold('thr5','{32804,32805,32806}',20,1,NULL,NULL,NULL,NULL,NULL,1,true);
```

查看安全监测阈值配置系统表

```
highgo=> select * from pg_secmon_threshold ;
```

触发序列阈值

```
highgo=# create table test4 (id int);

highgo=# insert into test4 values(1);

highgo=# delete from test4;
```

查看审计日志

```
highgo=> select * from hg_security.pg_audit_log;
```

查看安全监测历史

```
highgo=> select * from hg_security.pg_secmon_history;
```

查看安全监测阈值历史

```
highgo=> select * from hg_security.pg_secmon_thrhis;
```