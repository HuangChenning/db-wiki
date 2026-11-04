---
title: "权限分立"
book: "安全指南"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/safety/safeOne2.html"
tags:
  - highgo
  - highgo-v9
  - safety-security-guide
---

## 权限分立

瀚高数据库支持”三权分立”的安全机制。数据库系统通过”三权分立”机制划分为三个相互独立且相互制约的管理员角色，分别是数据库管理员角色（sysdba\_role）、数据库安全员角色（syssso\_role）和数据库审计员角色（syssao\_role）。对数据库系统权限实施分离，使系统中不存在超级用户和权限过高的角色/用户。用户权限按需分配，遵循最小化原则，从而降低安全隐患和风险。数据库管理员主要负责数据库系统的管理与维护；数据库安全员主要负责安全策略配置管理；数据库审计员的主要职责包括设置数据库用户操作行为的审计策略，以及对审计记录进行查询和分析。

数据库初始化完成后，系统会自动创建数据库管理员（默认为初始化时所使用的用户），自动创建数据库安全员（syssso）和数据库审计员（syssao）。另外，瀚高数据库允许有多个管理员账户同时存在，即允许某管理员用户将某管理员角色授予普通用户。安全用户的初始化属性如下：

---

| 用户名称 | 初始化属性 | 管理员角色 |
| --- | --- | --- |
| highgo(实例级)(假设使用highgo进行初始化或license中指定初始化用户为highgo) | SUPERUSER CREATEROEL CREATEDB REPLICATION BYPASSRLS。 | 使用通用排序规则。sysdba\_role(实例级) |
| syssso(实例级) |  | syssso\_role(实例级) |
| syssao(实例级) |  | syssao\_role(实例级) |

---

注意

瀚高数据库管理系统V9.0.5之前的版本，本模块涉及的函数放在了public模式下；从瀚高数据库管理系统V9.0.5版本开始，将本模块涉及的函数均迁移到hg\_security模式下。如果您在public模式下查询不到相关对象，请您指定hg\_security模式再做查询。

## 权限分立开关

三权分立模块的开关se\_feature.mode说明参见下表：

---

| 参数名称 | 参数类型 | 参数说明 | 修改 |
| --- | --- | --- | --- |
| se\_feature.mode | bool | 三权分立功能的开关。默认为off | 未开启三权分立时，仅限超级用户修改；开启三权分立后仅限syssso\_role成员用户修改 |
| se\_feature.restricted\_dba | bool | 受限DBA开关，默认为off，开启后表示对数据库管理员实施更严格的权限管控，详见2.4章节。 | 未开启三权分立时，仅限超级用户修改；开启三权分立后仅限syssso\_role成员用户修改。仅在se\_feature.mode开启时可修改。 |

上述2个参数可由安全管理员在不同层级（如实例级、库级和会话级）进行调整。具体而言，实例级的修改通过  
ALTER SYSTEM SET xxx命令实现，而库级的修改则通过 ALTER DATABASE dbname  
SET  
xxx命令完成。需要注意的是，实例级的修改需要重启或重载数据库才能生效，而库级的修改则要求重新创建连接后才生效。对于会话级的修改，安全管理员可以通过执行函数set\_backend\_se\_param(oid,  
text, boolean) 为指定用户的OID修改其后台连接参数，并通过被修改连接调用  
check\_se\_param\_change() 函数接收更改结果，此过程无需断开连接。

会话级安全参数修改示例：

会话级修改三权开关的方式：

给当前登录用户为user1的会话开启三权开关：

查询当前user1用户的oid

```
highgo=> select current_user::regrole::oid;

current_user

---------------

17187

(1 行记录)
```

重新创建会话登录到syssso用户下修改三权开关：

```
highgo=>select
hg_security.set_backend_se_param(17187,'se_feature.mode','true');
```

再切换到user1用户登录的会话，接收参数修改：

highgo=>select hg\_security.check\_se\_param\_change();

权限分立功能关闭的情况下，数据库级修改安全参数示例：

库级修改三权开关的方式：

highgo(数据库初始化时的用户)用户登录：

```
[highgo@node1 bin]$ ./psql highgo highgo -p 5866
```

使用alter database命令修改安全参数：

```
highgo=# alter database highgo set se_feature.mode=on;
ALTER DATABASE
```

重新创建会话连接生效。

权限分立功能关闭的情况下，实例级修改安全参数示例：

实例级修改三权开关的方式：

highgo(数据库初始化时的用户)用户登录：

```
[highgo@node1 bin]$ ./psql highgo highgo -p 5866
```

使用alter system命令修改安全参数：

```
highgo=# alter system set se_feature.mode=on;
ALTER SYSTEM
```

重启数据库参数生效。

三权分立功能开启后，所有安全角色由该角色的管理员admin，通过grant/revoke进行成员管理。同一用户无法拥有两种或以上的安全角色；管理员用户之间无法通过SET  
ROLE、SET SESSION AUTHORIZATION的方式切换。

三权分立功能开启后，普通用户由拥有createrole属性的用户创建，  
普通用户无法拥有superuser，createrole和createdb属性。superuser，createrole和createdb属性仅可在授权sysdba\_role成员时自动添加到新成员用户中。

三权分立功能开启后，只有属于sysdba\_role角色的成员用户的superuser  
属性可以生效，即sysdba\_role成员内的超级用户，三权分立功能开启以后，和系统管理员权限一致；sysdba\_role成员外的超级用户，三权开启以后，作为普通用户处理；sysdba\_role成员用户，自动赋予超级用户属性；移除时，自动移除超级用户属性。

## 管理员角色介绍

瀚高数据库新增了三个管理员角色，分别为数据库管理员角色（sysdba\_role）、数据库安全员角色（syssso\_role）和数据库审计员角色（syssao\_role）。以下是各角色的职责与功能概述：

数据库管理员角色

每个数据库至少需要一位数据库管理员（DBA）来负责管理，该角色可以是一个人或一个团队。不同数据库系统的数据库管理员职责可能有所不同，但总体任务包括以下内容：

评估软硬件环境：确定数据库服务器所需的运行环境。

安装与升级服务：负责数据库服务的安装和版本升级。

数据库结构设计：规划数据库的整体架构。

性能监控与优化：实时监控数据库性能并进行优化。

备份与恢复计划：制定并实施数据备份及故障恢复策略。

数据库安全员角色

从数据安全的角度来看，大型数据库系统需要将权限分配给不同的角色，以实现职责分离，从而相互制约和监督，确保系统的整体安全性。数据库安全员的主要职责如下：

制定安全策略：通过配置安全策略，确认请求访问的用户或设备是否具有合法身份。通过验证用户提供的凭据（如用户名、密码、证书等），确保只有授权用户才能访问受保护的资源。

权限限制：安全管理员无法创建角色/用户，无CREATE DATABASE、CREATE  
ROLE权限，他们的主要职责是设计和维护安全机制；

特殊权限：在某些特定模式下，安全管理员可能具备查看部分审计日志的权限，具体细节请参见”安全审计”章节。

数据库审计员角色

假设某小型在线支付平台的一名员工滥用数据库访问权限，私自查询并出售客户个人信息（如姓名、联系方式和银行卡信息）。由于缺乏安全审计机制，这种行为在初期未被发现，直到客户投诉资金异常流动后才引起注意。为避免类似问题的发生，可以通过以下方式加强安全管理：制定安全策略：由数据库安全员制定安全策略，限制DBA或其他用户的访问权限；设置审计策略：在系统建设初期，由安全审计员（syssao  
或其创建的其他审计员）设置审计策略；分析审计记录：在需要时，安全审计员可以查看审计记录，及时发现并追踪非法操作。

结合案例可以看出，数据库审计员的主要职责包括：创建和管理审计员账户、配置审计策略，查看和分析审计记录，确保系统操作的合规性和透明性。

通过明确分工和职责分离，这三个角色共同保障了数据库的安全性、稳定性和可追溯性。

## 开启三权分立用户权限划分

| 对象名称 | 操作类型 | 系统管理员 | 安全管理员 | 审计管理员 | 普通用户 |
| --- | --- | --- | --- | --- | --- |
| 用户/角色 | create role/user | 1）可以创建用户/角色；2）创建用户/角色的属性无法包含superuser、createdb 、createrole等属性。特别说明：在三权开关关闭时授权出去的用户属性，三权开启后应按照安全角色的划分来判断是否生效3）in role/group子句以及role、admin、user子句后不能包含sysdba\_role、syssso\_role、syssao\_role等安全角色或属于以上安全角色的成员。 | 无法执行 | 无法执行 | 无法执行 |
|  | alter role/user | 1）可修改自身密码。2）无法修改属于sysdba\_role、syssso\_role、syssao\_role等安全角色的成员的属性。3）修改普通用户时无法设置superuser、createdb 、createrole等属性。 | 1）可修改自身密码，以及有效期限。2）可修改普通用户密码、可修改所有用户的有效期 | 1）可修改自身密码。 | 1）可修改自身密码。 |
|  | drop role/user | 1）无法删除属于安全角色的成员。但是可以在撤销安全角色后删除2）可以删除普通用户/角色。 | 无法删除用户/角色。 | 无法删除用户/角色。 | 无法删除用户/角色。 |
|  | grant/revoke role … to/from grantee | 1）当role为普通用户/角色，grantee为普通用户/角色时可执行授权/撤销。2）role 为syssso\_role或 syssao\_role成员时，无法执行，授权/撤销。3）当role 为 sysdba\_role成员时有该角色admin属性的用户，可将 sysdba\_role角色授权/撤销 给普通用户，但操作中不能包含admin option子句防止级联授权。4）授权sysdba\_role角色时若grantee包含syssso\_role或syssao\_role的成员，则无法授权。 | 1）无法授权/撤销普通用户/角色。2）有admin属性的syssso\_role成员，可将 syssso\_role角色授权给普通用户。授权时无法授予admin option防止级联授权。3）有admin属性的syssso\_role成员，可将 syssso\_role角色从现有成员中撤销。4）授权syssso\_role角色时若接受对象拥有其他成员，则无法授权。防止级联授权。 | 1）无法授权/撤销普通用户/角色。2）有admin属性的syssao\_role成员，可将 syssao\_role角色授权给普通用户。授权时无法授予admin option防止级联授权。3）有admin属性的syssao\_role成员，可将 syssao\_role角色从现有成员中撤销。4）授权sysao\_role角色时若接受对象拥有其他成员，则无法授权。防止级联授权。 | 1）无法授权/撤销普通用户/角色。 |
| 表空间 | create tablesapce … | 可以执行，但是带owner 子句owner 只能指定sysdba\_role的成员，否则创建失败。 | 无法执行 | 无法执行 | 无法执行 |
|  | alter tablespace | 可以执行，但是指定owner 子句时若对象为sysdba\_role成员外的用户；其余与原生PG一致。 | 无法执行 | 无法执行 | 无法执行 |
|  | grant/revoke …on tablespace to/from grantee… | 当grantee 包含syssso\_role或syssao\_role成员用户时，无法执行赋权/回收；当grantee 只包含sysdba\_role的成员或普通用户时可以执行赋权/回收，但是不能将with grant option属性给任何非sysdba\_role成员用户 | 无法执行 | 无法执行 | 无法执行 |
|  | drop tablespace | 对所有表空间权限有删除权限 | 无法执行 | 无法执行 | 无法执行 |
| 数据库 | create database | 可创建属主为自己的数据库，带owner 属性创建时仅指定为owner sysdba\_role成员。 | 无法执行 | 无法执行 | 无法执行 |
|  | alter database | 不能修改数据库属主为为sysdba\_role成员外的用户。 | 无法执行 | 无法执行 | 无法执行 |
|  | grant/revoke …on database to/from grantee… | 赋权/撤销的grantee 包含syssso\_role和syssao\_role成员时操作权限不能包含create权限；不能将with grant option属性给任何非属性给任何非sysdba\_role成员用户；其他与原生PG一致 | 无法执行 | 无法执行 | 无法执行 |
|  | drop database | 对所有数据库有删除权限 | 无法执行 | 无法执行 | 无法执行 |
| 模式 | create schema | 可以创建，但包含authorization子句时只可以指定sysdba\_role成员或为普通用户。 | 无权限 | 无权限 | 被赋权数据库权限后只可创建模式。 |
|  | alter schema | 只可修改属主为sysdba\_role成员和普通用户的模式的属性，可以修改owner为sysdba\_role成员及普通用户。 | 无权限 | 无权限 | 赋权数据库权限后只可修改属主为自己的模式的属性，不可以将属主修改为管理员用户或其他普通用户,特定普通用户除外。例如：u1组有两个成员u2、u3，则u1不可以将属主为自己的模式属主修改为u2；u2可以将属主为自己的模式属主修改为u1；但u2不可将属主为自己的模式属主修改为u3 |
|  | grant/revoke …on schema to/from grantee … | 对于属主为sysdba\_role成员的模式，可执行授权/撤销，其赋权/回收,当grantee是普通用户和sysdba\_role的成员时不受限制，当grantee为syssso\_role和syssao\_role时不能包含create权限。对于属于syssso\_role和syssao\_role成员的模式，无法执行授权/撤销。对于数普通用户的模式，可执行授权/撤销，当grantee是普通用户和sysdba\_role的成员时不受限制，当grantee为syssso\_role和syssao\_role时不能包含create权限。 | 无权限 | 无权限 | 可将属主为自己的模式的权限进行授权/撤销。当grantee是普通用户和sysdba\_role的成员时不受限制，当grantee为syssso\_role和syssao\_role时不能包含create权限。 |
|  | 使用模式 | 可使用属主为sysdba\_role成员的模式，普通用户的模式被授权过的模式及public模式 | 可使用属主为自己的模式，被授权过的模式及public模式 | 可使用属主为自己的模式，被授权过的模式及public模式 | 可使用属主为自己的模式，被授权过的模式及public模式 |
|  | drop schema | 可删除属主sysdba\_role成员和普通用户的模式（public模式不可删除） | 无权限 | 无权限 | 只可删除属主为自己的模式，有其他用户创建的对象时可使用级联删除 |
| 表 | create table | 只可在属主为自己的模式，被授权过的模式，其他sysdba\_role成员的模式，普通用户的模式和public模式下创建表。 | 无权限 | 无权限 | 只可在属主为自己的模式、已授权的模式和public模式下创建表 |
|  | 查询及使用表 | 可查询、使用属主为自己的表，其他sysdba\_role成员的表，普通用户的表，已授权的表 | 可查询、使用属主为自己的表，可查询、使用已授权的表 | 可查询、使用属主为自己的表，可查询、使用已授权的表 | 可以查询、使用属主为自己的及已被授权的表 |
|  | alter table | 只可修改属主为sysdba\_role成员和普通用户的表式的属性，可以将属主修改为sysdba\_role成员及普通用户 | 无权限 | 无权限 | 只可修改属主为自己的表的属性，只可修改属主为特定普通用户，例如：u1组有两个成员u2、u3，则u1不可以将属主为自己的表属主修改为u2；u2可以将属主为自己的表属主修改为u1；但u2不可将属主为自己的表属主修改为u3。不可以将属主修改为管理员用户或其他普通用户 |
|  | grant/revoke.. | 对属于sysdba\_role成员的表可执行赋权/撤销，其赋权/撤销对象只能是sysdba\_role成员和普通用户。对于属于syssso\_role和syssao\_role成员的表，无法执行授权/撤销。对普通用户的表，可执行授权/撤销，对象不能是syssso\_role和syssao\_role成员。 | 无权限 | 无权限 | 普通用户有权限将属主为自己的表给其他普通用户或sysdba\_role成员用户执行授权/撤销。 |
|  | drop table | 只可删除属主为sysdba\_role成员的表和普通用户的表。 | 无权限 | 无权限 | 只可删除属主为自己的表 |
| 索引 | create index | 只可在sysdba\_role成员和普通用户的表上创建索引 | 无权限 | 无权限 | 只可在属主为自己的表上创建索引 |
|  | alter index | 只可修改sysdba\_role成员和普通用户的索引 | 无权限 | 无权限 | 只可修改自己创建的索引 |
|  | drop index | 只可删除sysdba\_role成员和普通用户的索引 | 无权限 | 无权限 | 只可删除自己创建的索引 |
| 视图 | create view | 只可在属主为自己的模式，sysdba\_role成员的模式，被授权过的模式，普通用户的模式和public模式下创建视图 | 无权限 | 无权限 | 只可在属主为自己的模式、已授权的模式和public模式下创建视图 |
|  | alter view | 只可修改属主sysdba\_role成员和普通用户的视图的属性，属主可以修改为sysdba\_role成员和普通用户，不能修改为syssso\_role成员syssao\_role成员用户 | 无权限 | 无权限 | 参照表的修改规则 |
|  | drop view | 只可删除属主为sysdba\_role成员的视图和普通用户的视图。 | 无权限 | 无权限 | 只可删除属主为自己的视图 |
| 序列 | create sequence | 只可在属主为自己的模式，sysdba\_role成员的模式，被授权过的模式，普通用户的模式和public模式下创建序列 | 无权限 | 无权限 | 只可在属主为自己的模式、已授权的模式及public模式下创建序列 |
|  | alter sequence | 只可修改属主为sysdba\_role成员和普通用户的序列的属性。属主可以修改为sysdba\_role成员和普通用户，不能修改为syssso\_role成员syssao\_role成员用户 | 无权限 | 无权限 | 参照表的修改规则 |
|  | grant/revoke… on sequence | 对属于sysdba\_role成员的序列可执行赋权/撤销，其赋权/撤销对象只能是sysdba\_role成员和普通用户。对于属于syssso\_role和syssao\_role成员的序列，无法执行授权/撤销。对普通用户的序列，可执行授权/撤销，对象不能是syssso\_role和syssao\_role成员。 | 无权限 | 无权限 | 普通用户有权限将属主为自己的序列对其他普通用户或sysdba\_role成员用户执行授权/撤销 |
|  | 使用及查询序列 | 可查询、使用属主为自己的序列，其他sysdba\_role成员的序列，普通用户的序列，已授权的序列 | 无权限 | 无权限 | 只能使用及查询属主为自己及已授权的序列 |
|  | 删除序列 | 只可删除属主为sysdba\_role成员的序列和普通用户的序列。 | 无权限 | 无权限 | 只可删除属主为自己的序列 |
| 函数/存储过程 | create function | 只可在属主为自己的模式，sysdba\_role成员的模式，被授权过的模式，普通用户的模式和public模式下创建函数 | 无权限 | 无权限 | 只可在属主为自己的模式、已授权的模式及public模式下创建函数 |
|  | alter function | 只可修改属主为sysdba\_role成员和普通用户的函数的属性，owner to属性只可修改为sysdba\_role成员或普通用户 | 无权限 | 无权限 | 参照表的修改规则 |
|  | grant/revoke | 对属于sysdba\_role成员的函数可执行赋权/撤销，其赋权/撤销对象只能是sysdba\_role成员和普通用户。对于属于syssso\_role和syssao\_role成员的函数，无法执行授权/撤销。对普通用户的函数，可执行授权/撤销，对象不能是syssso\_role和syssao\_role成员。 | 无权限 | 无权限 | 普通用户有权限将属主为自己的函数对其他普通用户或sysdba\_role成员用户执行授权/撤销。 |
|  | 调用函数 | 可调用属主为自己的函数，sysdba\_role成员模式下的函数，普通用户的默认授权的public模式下的函数、系统模式下的函数，被显示授权的函数 | 只可调用属主为自己的函数和已授权的函数，public下的函数 | 只可调用属主为自己的函数和已授权的函数，public下的函数 | 只可调用属主为自己的函数和已授权的函数，public下的函数 |
|  | drop function | 只可删除属主为sysdba\_role成员和普通用户的函数 | 无权限 | 无权限 | 只可删除属主为自己的函数 |

开启三权分立和受限DBA用户权限划分

| 对象名称 | 操作类型 | 系统管理员 | 安全管理员 | 审计管理员 | 普通用户 |
| --- | --- | --- | --- | --- | --- |
| 用户/角色 | create role/user | 1）可以创建用户/角色；2）创建用户/角色的属性无法包含superuser、createdb 、createrole等属性。特别说明：在三权开关关闭时授权出去的用户属性，三权开启后应按照安全角色的划分来判断是否生效3）in role/group子句以及role、admin、user子句后不能包含sysdba\_role、syssso\_role、syssao\_role等安全角色或属于以上安全角色的成员。 | 无法执行 | 无法执行 | 无法执行 |
|  | alter role/user | 1）可修改自身密码。2）无法修改属于sysdba\_role、syssso\_role、syssao\_role等安全角色的成员的属性。3）修改普通用户时无法设置superuser、createdb 、createrole等属性。 | 1）可修改自身密码，以及有效期限。2）可修改普通用户密码、可修改所有用户的有效期 | 1）可修改自身密码。 | 1）可修改自身密码。 |
|  | drop role/user | 1）无法删除属于安全角色的成员。但是可以在撤销安全角色后删除2）可以删除普通用户/角色。 | 无法删除用户/角色。 | 无法删除用户/角色。 | 无法删除用户/角色。 |
|  | grant/revoke role … to/from grantee | 1）当role为普通用户/角色，grantee为普通用户/角色时可执行授权/撤销。2）role 为syssso\_role或 syssao\_role成员时，无法执行，授权/撤销。3）当role 为 sysdba\_role成员时有该角色admin属性的用户，可将 sysdba\_role角色授权/撤销 给普通用户，但操作中不能包含admin option子句防止级联授权。4）授权sysdba\_role角色时若grantee包含syssso\_role或syssao\_role的成员，则无法授权。 | 1）无法授权/撤销普通用户/角色。2）有admin属性的syssso\_role成员，可将 syssso\_role角色授权给普通用户。授权时无法授予admin option防止级联授权。3）有admin属性的syssso\_role成员，可将 syssso\_role角色从现有成员中撤销。4）授权syssso\_role角色时若接受对象拥有其他成员，则无法授权。防止级联授权。 | 1）无法授权/撤销普通用户/角色。2）有admin属性的syssao\_role成员，可将 syssao\_role角色授权给普通用户。授权时无法授予admin option防止级联授权。3）有admin属性的syssao\_role成员，可将 syssao\_role角色从现有成员中撤销。4）授权sysao\_role角色时若接受对象拥有其他成员，则无法授权。防止级联授权。 | 1）无法授权/撤销普通用户/角色。 |
| 表空间 | create tablesapce … | 可以执行，但是带owner 子句owner 只能指定sysdba\_role的成员，否则创建失败。 | 无法执行 | 无法执行 | 无法执行 |
|  | alter tablespace | 可以执行，但是指定owner 子句时若对象为sysdba\_role成员外的用户；其余与原生PG一致。 | 无法执行 | 无法执行 | 无法执行 |
|  | grant/revoke …on tablespace to/from grantee… | 当grantee包含syssso\_role或syssao\_role成员用户时，无法执行赋权/回收；当grantee 只包含sysdba\_role的成员或普通用户时可以执行赋权/回收，但是不能将with grant option属性给任何非sysdba\_role成员用户 | 无法执行 | 无法执行 | 无法执行 |
|  | drop tablespace | 对所有表空间权限有删除权限 | 无法执行 | 无法执行 | 无法执行 |
| 数据库 | create database | 可创建属主为自己的数据库，带owner 属性创建时仅指定为owner sysdba\_role成员。 | 无法执行 | 无法执行 | 无法执行 |
|  | alter database | 不能修改数据库属主为为sysdba\_role成员外的用户。 | 无法执行 | 无法执行 | 无法执行 |
|  | grant/revoke …on database to/from grantee… | 赋权/撤销的grantee 包含syssso\_role和syssao\_role成员时操作权限不能包含create权限；不能将with grant option属性给任何非属性给任何非sysdba\_role成员用户；其他与原生PG一致 | 无法执行 | 无法执行 | 无法执行 |
|  | drop database | 对所有数据库有删除权限 | 无法执行 | 无法执行 | 无法执行 |
| 模式 | create schema | 可以创建，但包含authorization子句时只可以指定sysdba\_role成员或为普通用户。 | 无权限 | 无权限 | 被赋权数据库权限后只可创建模式。 |
|  | alter schema | 只可修改属主为自己的模式的属性，可以修改owner为sysdba\_role成员。 | 无权限 | 无权限 | 赋权数据库权限后只可修改属主为自己的模式的属性，不可以将属主修改为管理员用户或其他普通用户,特定普通用户除外。例如：u1组有两个成员u2、u3，则u1不可以将属主为自己的模式属主修改为u2；u2可以将属主为自己的模式属主修改为u1；但u2不可将属主为自己的模式属主修改为u3 |
|  | grant/revoke …on schema to/from grantee … | 对于属主为自己的模式，当grantee为sysdba\_role成员时授权/撤销不受任何限制；当grantee为syssso\_role或syssao\_role成员时不能包含create权限；当grantee为普通用户时，无法执行授权/撤销。对于属主为普通用户的模式，可执行授权/撤销，其赋权/回收grantee只能是普通用户。 | 无权限 | 无权限 | 可将属主为自己的模式的权限进行授权/撤销。当grantee是普通用户和sysdba\_role的成员时不受限制，当grantee为syssso\_role和syssao\_role时不能包含create权限。 |
|  | 使用模式 | 可使用属主为自己的模式，被授权过的模式及public模式 | 可使用属主为自己的模式，被授权过的模式及public模式 | 可使用属主为自己的模式，被授权过的模式及public模式 | 可使用属主为自己的模式，被授权过的模式及public模式 |
|  | drop schema | 可删除属主为自己的模式（public模式不可删除） | 无权限 | 无权限 | 只可删除属主为自己的模式，有其他用户创建的对象时可使用级联删除 |
| 表 | create table | 只可在自己拥有的模式，被授权过的模式，public模式下创建表。 | 无权限 | 无权限 | 只可在属主为自己的模式、已授权的模式和public模式下创建表 |
|  | 查询及使用表 | 可查询、使用属主为自己的表，可查询、使用已授权的表 | 可查询、使用属主为自己的表，可查询、使用已授权的表 | 可查询、使用属主为自己的表，可查询、使用已授权的表 | 可以查询、使用自己创建的及已被授权的表 |
|  | alter table | 只可修改自己创建的表的属性，不可将自己的表的属主修改为sysdba\_role成员外的其他用户。 | 无权限 | 无权限 | 只可修改自己表的属性，只可修改属主为特定普通用户，例如：u1组有两个成员u2、u3，则u1不可以将属主为自己的表属主修改为u2；u2可以将属主为自己的表属主修改为u1；但u2不可将属主为自己的表属主修改为u3。不可以将属主修改为管理员用户或其他普通用户 |
|  | grant/revoke.. | 只能在自己的表上做赋权与回收，自己的表只能赋权给sysdba\_role成员 | 无权限 | 无权限 | 普通用户有权限将属主为自己的表给其他普通用户或sysdba\_role成员用户执行授权/撤销。 |
|  | drop table | 只可删除属主为自己的表。 | 无权限 | 无权限 | 只可删除属主为自己的表 |
| 索引 | create index | 只可在属主为自己的表上创建索引 | 无权限 | 无权限 | 只可在属主为自己的表上创建索引 |
|  | alter index | 只可修改自己创建的索引 | 无权限 | 无权限 | 只可修改自己创建的索引 |
|  | drop index | 只可删除自己创建的索引 | 无权限 | 无权限 | 只可删除自己创建的索引 |
| 视图 | create view | 只可在属主为自己的模式，被授权过的模式，和public模式下创建视图 | 无权限 | 无权限 | 只可在属主为自己的模式、已授权的模式和public模式下创建视图 |
|  | alter view | 只可修改属主为自己的视图的属性，属主只可以修改为sysdba\_role成员， | 无权限 | 无权限 | 参照表的修改规则 |
|  | drop view | 只可删除属主为自己的视图。 | 无权限 | 无权限 | 只可删除属主为自己的视图 |
| 序列 | create sequence | 只可在属主为自己的模式，被授权过的模式，和public模式下创建序列 | 无权限 | 无权限 | 只可在属主为自己的模式、已授权的模式及public模式下创建序列 |
|  | alter sequence | 只可修改属主为自己的序列的属性。属主只可以修改为sysdba\_role成员 | 无权限 | 无权限 | 参照表的修改规则 |
|  | grant/revoke… on sequence | 只能在属主为自己的的序列上做赋权与回收，自己的序列只能赋权给sysdba\_role成员 | 无权限 | 无权限 | 普通用户有权限将属主为自己的序列对其他普通用户或sysdba\_role成员用户执行授权/撤销 |
|  | 使用及查询序列 | 可查询、使用属主为自己的序列，已授权的序列 | 无权限 | 无权限 | 只能使用及查询属主为自己及已授权的序列 |
|  | 删除序列 | 只可删除属主为自己的序列。 | 无权限 | 无权限 | 只可删除属主为自己的序列 |
| 函数/存储过程 | create function | 只可在属主为自己的模式被授权过的模式和public模式下创建函数 | 无权限 | 无权限 | 只可在属主为自己的模式、已授权的模式及public模式下创建函数 |
|  | alter function | 只可修改属主为自己的函数的属性，owner to属性只可修改为sysdba\_role成员 | 无权限 | 无权限 | 参照表的修改规则 |
|  | grant/revoke | 对属于自己的函数可执行赋权/撤销，其赋权/撤销对象只能是sysdba\_role成员。对于属于syssso\_role、syssao\_role、普通用户成员的函数，无法执行授权/撤销。 | 无权限 | 无权限 | 普通用户有权限将属主为自己的函数对其他普通用户或sysdba\_role成员用户执行授权/撤销。 |
|  | 调用函数 | 可调用属主为自己的函数，默认授权的public模式下的函数、系统模式下的函数，被显示授权的函数 | 只可调用属主为自己的函数和已授权的函数，public下的函数 | 只可调用属主为自己的函数和已授权的函数，public下的函数 | 只可调用属主为自己的函数和已授权的函数，public下的函数 |
|  | drop function | 只可删除属主为自己的函数 | 无权限 | 无权限 | 只可删除属主为自己的函数 |