---
title: "4.安全审计"
book: "HGDB 安全管理手册"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/develop/security_audit.html"
tags:
  - highgo
  - highgo-v45
  - develop-security-management
---

## 4\. 安全审计

仅安全版提供该功能。

瀚高数据库提供安全审计模块，通过对用户访问数据库的行为进行记录、分析和告警，来帮助用户事后生成合规报告、事故追根溯源，以进一步提高数据安全。

安全审计模块会对特定操作进行审计，并记录审计日志，每一条审计产生的数据称为一条审计记录。使用审计管理员syssao可自定义需要审计的用户及操作，此过程称为审计（策略）配置；其中的“操作”（如CREATE TABLE）称为审计事件（或审计策略）。

当用户对比较重要的审计事件（如DROP TABLE）进行审计配置后，可通过创建审计分析规则，为该配置进行审计告警。用户可以自行配置需要审计的事件及其风险等级，当发生审计事件的时候，不同的风险等级对应着不同的处理。

审计相关的所有操作均需使用syssao用户完成。

## 4.1. 审计配置

想要对用户某行为进行审计，首先需要打开审计功能，然后再进行审计策略配置。

### 4.1.1. 审计参数配置

下文列出了所有审计相关的参数配置。使用审计管理员查看和配置审计参数。要想使用审计功能，必须确保hg\_audit参数值为on。

查看审计参数：

select show\_audit\_param();

修改审计参数：（审计参数修改后均需重启生效）

select set\_audit\_param(‘参数名称’,’要修改的参数值’);

审计参数说明：

- hg\_audit：审计总开关，默认为on。
- hg\_audit\_analyze：审计分析开关，on表示需要检查用户配置的审计事件风险等级，并根据风险等级进行处理，off表示只记录审计记录，而不处理风险等级，默认为off。
- hg\_audit\_alarm:审计告警方式，当前只支持email方式，即当需要进行审计告警时，发送邮件到hg\_audit\_alarm\_email所配置的邮箱。
- hg\_audit\_alarm\_email：审计告警邮箱。
- hg\_audit\_logsize：生成的审计文件大小，可配置的范围为16MB~1GB；默认为16MB。
- hg\_audit\_keep\_days：hgaudit目录下的审计记录文件所保存的时间(以天为单位)，若超过这个时间，相关文件将会被删除。
- hg\_audit\_file\_archive\_mode：审计自动归档模式的开关，on表示打开审计文件自动归档，审计归档进程扫描hgaudit/audit\_archive\_ready下的ready文件，把相应的审计日志文件归档到hg\_audit\_file\_archive\_dest指定的路径下。默认为off。
- hg\_audit\_file\_archive\_dest：审计归档路径，只支持绝对路径。设定的路径必须存在且数据库运行用户对其有写权限。

### 4.1.2. 审计策略配置

审计管理员可以对审计事件进行配置，可以配置语句审计与对象审计。

#### 4.1.2.1. 语句审计

配置语句审计的语法为：

> audit statement\_opts by username|all \[whenever \[not\] successful\]- statement\_opts：语句审计事件列表（支持的语句见支持的审计语句）
> 
> 支持指定多个语句类型，用逗号分隔；如果对所有语句进行审计，则使用all，此时，对每一种语句记录一条审计配置项；该参数不能为空。
> 
> - username：要审计的用户名称。指定all表示所有用户。支持指定多个用户，用户间用逗号分隔。为每个用户记录一条审计配置项。
> - whenever \[not\] successful：审计模式。whenever successful表示只对成功的事件进行审计。whenever not successful表示只对失败的事件进行审计。不指定表示不论成功失败均进行审计。

查看已配置的语句审计：

> highgo=> audit create table by all whenever successful;AUDIT
> 
> highgo=> select \* from hgaudit\_statement;
> 
> confid | userid | auditevent | auditmode | risklevel
> 
> ——–+——–+————–+————+———–
> 
> 16384 | 0 | CREATE TABLE | SUCCESSFUL | 0
> 
> (1 row)

删除已配置的语句审计策略，语法分两种:

> 1）noaudit statement\_opts by username|all \[whenever \[not\] successful\] \[cascade\]2）noaudit statement confid \[cascade\]
> 
> cascade表示，如果该审计配置项配置了审计分析规则，则连同审计分析规则一同删除。

#### 4.1.2.2. 对象审计

配置对象审计的语法为：

> audit object\_opts on objtype \[schema.\]objname\[.colname\] by username|all \[whenever \[not\] successful\]- object\_opts：要审计的操作类型，不能省略。支持指定多个操作类型，用逗号分隔；如果对该对象的所有操作审计，则使用all；此时，对每一种操作类型记录一条审计配置项。（支持的语句见12.6）
> 
> - objtype：要审计的对象的类型，必填项；支持table、view、column、sequence、function、procedure；不支持同时指定多个。
> - schema：对象所在的模式。如不指定，按照search\_path的定义搜索。
> - objname：对象名称。必填项。
> - colname：列名。表示对该列进行审计。仅当objtype为column时才需要指定，若不指定，表示对表的所有列进行审计。

查看已配置的对象审计：

审计记录生成的时候，对每个对象都生成一条记录。

> select \* from hgaudit\_object;confid | objecttype | objectid | clumnid | userid | auditevent | auditmode | risklevel
> 
> ——–+————+———-+———+——–+————+————+———–
> 
> 16388 | TABLE | 16385 | 0 | 9999 | INSERT | SUCCESSFUL | 0
> 
> (1 row)

删除已配置的对象审计策略，语法也分两种：

> 1）noaudit object\_opts on objtype \[schema.\]objname\[.colname\] by username|all \[whenever \[not\] successful\] \[cascade\]
> 
> 2）noaudit object confid \[cascade\]
> 
> cascade表示，如果该审计配置项配置了审计分析规则，则连同审计分析规则一同删除。

## 4.2. 审计记录

审计模块生成的审计日志会存放在数据目录下的hgaudit文件夹下。通过设置参数hg\_audit\_logsize可自定义审计文件的大小，当审计日志达到指定大小后，会自动新建一个新的审计日志继续存放审计记录。审计日志的文件名称以新建该文件的日期和时间命名。如hgaudit-2019-11-21-122103.log。

审计日志支持自动归档。可通过设置审计参数hg\_audit\_file\_archive\_mode和hg\_audit\_file\_archive\_dest使用审计日志的自动归档功能。

为避免庞大的审计日志占用过多的存储资源，瀚高数据库提供审计日志定期删除的功能。使用参数hg\_audit\_keep\_days进行配置。

审计记录包含以下信息：

| log\_time | 记录时间 |
| --- | --- |
| log\_time | 记录时间 |
| risklevel | 风险等级 |
| audittype | 审计类型：包含system(系统审计事件)，statement(语句审计事件)，object(对象审计事件)，mandatory(强制审计事件) |
| oper\_opts | 审计语句类型（支持的语句见12.6） |
| username | 用户名 |
| rolename | 角色名 |
| dbname | 数据库名称 |
| objtype | 对象类型 |
| schemaname | 模式名称 |
| objectname | 对象名称 |
| colname | 列名称 |
| privlevel | 权限等级：包含SYSTEM，DATABASE，SCHEMAOBJECT，INSTACE |
| procpid | 进程id |
| session\_start\_time | 会话开始时间 |
| action\_start\_time | 操作开始时间 |
| tansaction\_id | 事务id |
| client\_mac | 客户端mac |
| client\_ip | 客户端ip |
| client\_port | 客户端port |
| application\_name | 客户端应用 |
| server\_mac | 服务器mac |
| server\_ip | 服务器ip |
| server\_port | 服务器port |
| command | sql命令 |
| affect\_rows | 命令影响的行数 |
| return\_row | 命令返回行数 |
| duration | 命令持续时间 |
| result | 命令执行结果（成功或失败） |
| risklevel | 风险等级 |
| audittype | 审计类型：包含system(系统审计事件)，statement(语句审计事件)，object(对象审计事件)，mandatory(强制审计事件) |
| oper\_opts | 审计语句类型（支持的语句见支持的审计语句） |
| username | 用户名 |
| dbname | 数据库名称 |
| objtype | 对象类型 |
| schemaname | 模式名称 |
| objectname | 对象名称 |
| colname | 列名称 |
| privlevel | 权限等级：包含SYSTEM，DATABASE，SCHEMAOBJECT，INSTACE |
| procpid | 进程id |
| session\_start\_time | 会话开始时间 |
| action\_start\_time | 操作开始时间 |
| tansaction\_id | 事务id |
| client\_ip | 客户端ip |
| client\_port | 客户端port |
| application\_name | 客户端应用 |
| server\_ip | 服务器ip |
| server\_port | 服务器port |
| command | sql命令 |
| affect\_rows | 命令影响的行数 |
| return\_row | 命令返回行数 |
| duration | 命令持续时间 |
| result | 命令执行结果（成功或失败） |

审计日志是一个二进制文件。要想查看审计记录，需要将审计日志的内容导入到数据库表中。

### 4.2.1. 审计导入工具

审计管理员可以通过审计导入工具hgaudit\_imp把指定的审计文件导入public.hg\_t\_audit\_log表中，审计管理员可以查看该表。

hgaudit\_imp支持的选项有：

- \-f：指定需要导入的审计日志的文件，支持指定多个文件，多个文件用逗号分隔。支持指定绝对路径和相对路径，相对路径相对于审计日志文件路径$PGDATA/data/hgaudit。如不指定-f，则表示当前归档目录及审计日志目录下的审计记录。未写完的审计日志也支持导入。
- \-d：指定需要导入的数据库。
- \-h：指定要连接数据库IP（该参数在HGDB-SEE V4.5.3及以后的版本中支持）
- \-p：指定数据库的port（该参数在HGDB-SEE V4.5.3及以后的版本中支持）
- \-P：syssao用户的密码

示例：

1）导入审计日志：

hgaudit\_imp -p 5879 -d highgo -f hgaudit-2022-05-20-022624.log

2）回车后需要输入syssao用户的密码

3）执行完毕后，使用syssao用户登录数据库查看审计记录：

select \* from hg\_t\_audit\_log;

## 4.3. 审计分析规则

审计策略配置完成后，可通过创建审计分析规则，为某审计策略指定风险等级。不同的风险等级会有不同的告警行为。例如，将所有用户的drop table事件设置为低风险等级。当highgo用户成功执行drop table语句后，将触发低风险事件对应的告警行为（邮件告警）。如果不创建审计分析规则，则不会触发任何告警行为。

目前支持3种风险等级，分别对应如下行为：

- 低风险（1）：按照配置的告警方式告警(目前只支持邮箱的方式)
- 中风险（2）：违例进程终止。终止当前操作，但是用户连接仍存在。同时进行告警。
- 高风险（3）：服务取消。终止当前操作，断开用户连接，退出登录。同时进行告警。

### 4.3.1. 审计分析规则配置

使用该功能需要打开审计分析的开关，将审计参数hg\_audit\_analyze设置为on。

添加审计分析规则的语法：

|add\_actionaudit\_rule(rulename,audittype,auditevent,risklevel) - rulename：规则名称，必填项，唯一。

> - audittype：审计类型，可取值statement、object；必填项。
> - auditevent： 审计事件：填写confid；必填项。
> - risklevel ：风险等级：1、2、3分别代表低风险、中风险、高风险；必填项，默认为1

修改一个审计规则的语法：

alter\_actionaudit\_rule(rulename,risklevel)

删除一个审计规则的语法：

drop\_actionaudit\_rule(rulename)

示例：

> 1）配置一个审计策略audit create table by all;
> 
> 2）查看审计策略配置
> 
> select \* from hgaudit\_statement;
> 
> confid | userid | auditevent | auditmode | risklevel
> 
> ——–+——–+————–+—————-+———–
> 
> 24661 | 0 | CREATE TABLE | NOT SUCCESSFUL | 0
> 
> 24662 | 0 | CREATE TABLE | SUCCESSFUL | 0
> 
> (2 rows)
> 
> 3）为上述审计策略创建一个审计分析规则，风险等级为1
> 
> select add\_actionaudit\_rule(‘test’,’statement’,’24662’,’1’);
> 
> 4）查看审计分析规则
> 
> select \* from hg\_t\_sys\_auditanalyze\_rule;
> 
> rulename | audittype | auditevent | risklevel
> 
> ———-+———–+————+———–
> 
> test | \\x01 | 24662 | 1
> 
> (1 row)
> 
> 5）修改上述审计策略的风险等级为2
> 
> select alter\_actionaudit\_rule(‘test’,’2’);
> 
> 6）查看审计分析规则，risklevel列变为2
> 
> select \* from hg\_t\_sys\_auditanalyze\_rule;
> 
> rulename | audittype | auditevent | risklevel
> 
> ———-+———–+————+———–
> 
> test | \\x01 | 24662 | 2
> 
> (1 row)
> 
> 7）删除审计分析规则
> 
> select drop\_actionaudit\_rule(‘test’);
> 
> 8）查看审计分析规则，上述规则已被删除
> 
> select \* from hg\_t\_sys\_auditanalyze\_rule;
> 
> rulename | audittype | auditevent | risklevel
> 
> ———-+———–+————+———–
> 
> (0 rows)

### 4.3.2. 审计告警

用户可以通过参数hg\_audit\_alarm和hg\_audit\_alarm\_email来配置告警方式。当前只支持email方式。当hg\_audit\_analyze为on，hg\_audit\_alarm为email,且hg\_audit\_alarm\_email为有效邮箱时，告警方式即为向邮箱hg\_audit\_alarm\_email发送告警邮件,并向系统日志中输出warning。若只有hg\_audit\_analyze为on，其他两个参数未配置或无效，则只向系统日志中输出warning。

## 4.4. 特殊的审计事件

除了用户自定义配置的审计事件，系统中还定义了两种类型的特殊审计事件mandatory(强制审计事件)和system(系统审计事件)。

强制审计事件是指一定会被审计的事件，无论审计功能是否开启。该类型的事件目前只包含一个：审计总开关hg\_audit的修改。

系统审计事件不需要用户配置，只要hg\_audit为on就会审计，包括如下几种操作：

- 数据库启动
- 数据库停止
- 用户登陆
- 用户登出
- reload配置文件

## 4.5. 支持的审计语句

> CREATE ROLE
> 
> CREATE DOMAIN
> 
> CREATE PROCEDURE
> 
> CREATE INDEX
> 
> CREATE SCHEMA
> 
> CREATE SEQUENCE
> 
> CREATE TABLE
> 
> CREATE TABLE AS
> 
> CREATE TRIGGER
> 
> CREATE USER
> 
> CREATE VIEW
> 
> CREATE EXTENSION
> 
> CREATE DATABASE
> 
> ALTER ROLE
> 
> ALTER DOMAIN
> 
> ALTER PROCEDURE
> 
> ALTER INDEX
> 
> ALTER SYSTEM
> 
> ALTER SCHEMA
> 
> ALTER SEQUENCE
> 
> ALTER TABLE
> 
> ALTER TRIGGER
> 
> ALTER USER
> 
> ALTER VIEW
> 
> ALTER EXTENSION
> 
> ALTER DATABASE
> 
> DROP DOMAIN
> 
> DROP PROCEDURE
> 
> DROP ROLE
> 
> DROP INDEX
> 
> DROP SCHEMA
> 
> DROP SEQUENCE
> 
> DROP TABLE
> 
> DROP TRIGGER
> 
> DROP USER
> 
> DROP VIEW
> 
> DROP DATABASE
> 
> DROP EXTENSION
> 
> SELECT
> 
> SELECT INTO
> 
> INSERT
> 
> UPDATE
> 
> DELETE
> 
> GRANT
> 
> REVOKE