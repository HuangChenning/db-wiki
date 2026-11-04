---
title: "2.用户标识与认证"
book: "HGDB 安全管理手册"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/develop/user_identify.html"
tags:
  - highgo
  - highgo-v45
  - develop-security-management
---

## 2\. 用户标识与认证

瀚高数据库通过用户标识和认证为系统提供最外层的安全保护措施。在客户端访问数据库资源之前，服务器首先需要通过身份认证模块来验证用户的合法身份，从而在数据库系统的前后端之间建立安全的通信信道，防止非法用户连接数据库，保证只有合法的用户才能访问数据库资源。

## 2.1. 管理员简介

瀚高安全版数据库采用“三权分立”的安全机制。三权分立是对数据库系统管理员的权限实施分离，使系统中不存在超级管理员/超级用户和权限过高的角色和用户，降低安全隐患和风险。

“三权分立”机制将系统管理员划分为相互独立、相互制约的系统管理员（SYSDBA）、安全保密管理员（SYSSSO）和安全审计员（SYSSAO）三个管理员角色。系统管理员主要负责系统运行维护和生成用户身份标识符；安全保密管理员主要负责用户权限设定、安全策略配置管理；安全审计员主要负责对数据库所有用户操作行为审计的策略设置和审计记录的查询与分析。

在HGDB-SEE V4.5中，可通过参数hg\_sepofpowers关闭三权分立功能。该参数关闭后，将关闭数据库中的所有安全功能，安全版数据库即变成普通版数据库。参数的使用方法详见附录1 安全功能相关的参数说明

## 2.2. 创建用户

数据库使用过程中往往会根据需要创建多个普通用户。在“三权分立”的机制下，只能由系统管理员sysdba创建用户，其他用户无创建用户的权限。

使用CREATE USER命令创建用户。在瀚高数据库中， CREATE USER是 CREATE ROLE（创建角色）的一个别名。唯一的区别是CREATE USER中LOGIN 作为默认值，而CREATE ROLE的默认值是NOLOGIN。在使用上可以将用户和角色理解为同一概念。

创建用户时需要为用户指定口令用于登录时认证。具体的语法格式如下：（安全版和非安全版的语法略有差异）

> CREATE USER *user\_name* \[ \[ WITH \] *option* \[ … \] \]
> 
> 这里 *option* 可以是：
> 
> 　SUPERUSER | NOSUPERUSER
> 
> 　| CREATEDB | NOCREATEDB
> 
> 　| CREATEROLE | NOCREATEROLE
> 
> 　| INHERIT | NOINHERIT
> 
> 　| LOGIN | NOLOGIN
> 
> 　| REPLICATION | NOREPLICATION
> 
> 　| BYPASSRLS | NOBYPASSRLS
> 
> 　| CONNECTION LIMIT *connlimit*
> 
> 　| \[ ENCRYPTED \] PASSWORD ‘ *password* ‘ | PASSWORD NULL
> 
> 　| VALID UNTIL ‘ *timestamp* ‘
> 
> 　| IN ROLE *role\_name* \[, …\]
> 
> 　| IN GROUP *role\_name* \[, …\]
> 
> 　| ROLE *role\_name* \[, …\]
> 
> 　| ADMIN *role\_name* \[, …\]
> 
> 　| USER *role\_name* \[, …\]
> 
> 　| SYSID *uid*
> 
> ⁣⁣⁣⁣  
> ⁣⁣⁣⁣
> 
> 说明：
> 
> *user\_name* ：
> 
> 要创建的用户的名称，用户名必须以字母或下划线开头，后续字符可以是字母、数字、下划线或美元符号（$）。用户名中不能包含瀚高数据库的关键字和保留字。如需使用关键字、保留字或其他特殊字符，或者要以数字开头，需要使用双引号将用户名引起来，后续引用用户名时也需使用双引号。
> 
> ⁣⁣⁣⁣  
> SUPERUSER或NOSUPERUSER：（安全版不支持）
> 
> 该选项指定创建的用户是否为管理员用户。管理员用户可以越过数据库内的所有访问限制，因此其状态很危险，只应该在必要时使用。要创建一个新的超级用户，自己必须是一个超级用户。默认值是NOSUPERUSER。
> 
> ⁣⁣⁣⁣  
> CREATEDB或NOCREATEDB：（安全版不支持）
> 
> 该选项指定创建的用户/角色是否有创建数据库的权限。如果指定了CREATEDB，新创建的用户将被允许创建新的数据库。默认值是NOCREATEDB。
> 
> ⁣⁣⁣⁣  
> CREATEROLE或NOCREATEROLE：（安全版不支持）
> 
> 创建的用户是否有创建新用户/角色的权限（即执行CREATE ROLE）。如果指定CREATEROLE，创建的用户也可以修改和删除其他角色。默认值是NOCREATEROLE。
> 
> ⁣⁣⁣⁣  
> INHERIT或NOINHERIT：
> 
> 如果新的用户/角色是其他用户/角色的成员，该选项指定新用户是否从那些用户中“继承”权限，一个带有INHERIT属性的角色/用户能够自动使用已经被授予给其直接或间接父角色的任何数据库特权。默认值是INHERIT。
> 
> ⁣⁣⁣⁣  
> LOGIN或NOLOGIN
> 
> 该选项指定新创建的用户/角色是否有登录权限，也就是在客户端连接期间是否能使用该用户登录数据库系统。执行CREATE USER创建用户时默认值是LOGIN；使用CREATE ROLE创建角色时默认值是NOLOGIN。
> 
> ⁣⁣⁣⁣  
> REPLICATION或NOREPLICATION
> 
> 该选项指定新创建的用户/角色是否有复制权限。用户必须具有复制权限（或者成为一个超级用户）才能以复制模式（物理复制或者逻辑复制）连接到服务器以及创建或者删除复制槽。一个具有REPLICATION属性的角色是一个具有非常高特权的角色，应慎重使用。默认值是NOREPLICATION。
> 
> ⁣⁣⁣⁣  
> BYPASSRLS或NOBYPASSRLS
> 
> 该选项指定新创建的用户是否可以绕过每一条行级安全策略（RLS）。默认是NOBYPASSRLS。注意 pg\_dump 默认把row\_security设置为OFF， 以确保表的所有内容被转储出来。如果运行pg\_dump的用户不具备该权限，将会返回一个错误。被转储表的拥有者总是可以绕过 RLS。
> 
> ⁣⁣⁣⁣  
> CONNECTION LIMIT *connlimit*
> 
> 该选项指定该用户能建立多少并发连接。-1（默认值）表示无限制。注意这个限制仅针对于普通连接。预备事务和后台进程连接不受这一限制。
> 
> ⁣⁣⁣⁣  
> \[ ENCRYPTED \] PASSWORD ‘ *password* ’或PASSWORD NULL
> 
> 设置用户口令。口令总是以加密的方式存放在系统目录中。ENCRYPTED关键词没有实际效果，只是为了向后兼容性而存在。加密的方法由配置参数password\_encryption决定。如果当前的口令字符串已经是MD5加密或者SCRAM加密的格式，那么不管password\_encryption的值是什么，口令字符串还是原样存储（因为系统无法解密以不同格式加密的口令字符串）。这种方式允许在转储/恢复时重载加密的口令。
> 
> 安全版和企业版数据库中不支持PASSWORD NULL选项。
> 
> ⁣⁣⁣⁣  
> VALID UNTIL *‘timestamp’*
> 
> 该选项为用户口令设置一个有效期，在该时间点之后用户口令将会失效。
> 
> 在非安全版数据库中，如不指定，表示口令将一直有效。
> 
> 在安全版数据库中，如不指定，口令的有效期由安全参数hg\_idcheck. pwdvaliduntil决定。
> 
> ⁣⁣⁣⁣  
> IN ROLE *role\_name*
> 
> 该选项列出一个或多个现有角色。新的角色/用户将作为新成员加入这些角色中。
> 
> ⁣⁣⁣⁣  
> IN GROUP *role\_name*
> 
> 同IN ROLE，是为了向后兼容保留的。不建议使用。
> 
> ⁣⁣⁣⁣  
> ROLE *role\_name*
> 
> 该选项列出一个或者多个现有角色，这些角色会被自动加入到一个新角色中（可以理解为一个“组”）。
> 
> ⁣⁣⁣⁣  
> ADMIN *role\_name*
> 
> ADMIN子句与ROLE相似，区别是被指定的角色使用WITH ADMIN OPTION加入到新角色中，让它们能够把这个角色中的成员关系授予给其他人。
> 
> ⁣⁣⁣⁣  
> USER *role\_name*
> 
> 同ROLE，是为了向后兼容保留的。不建议使用。
> 
> ⁣⁣⁣⁣  
> SYSID *uid*
> 
> 该选项是为了向后兼容保留的，无实际功能。不建议使用。

示例：

创建一个口令有效期截止到2020年底的用户hg：

> CREATE USER hg PASSWORD ‘Hello@123’ VALID UNTIL ‘2021-01-01’;

## 2.3. 口令认证

该章节在企业版中是以插件形式存在，功能略有差异，暂不详细介绍。以下内容为安全版数据库的功能点。

使用指定用户登录数据库系统时，需要对用户的身份进行认证。瀚高数据库提供多种认证方式，其中口令认证最为常见。该章节主要讲述口令认证涉及的功能点。其他认证方式详见客户端认证。

安全版数据库为口令认证的身份鉴别方式提供了参数：hg\_idcheck.子参数名。子参数可以为以下几种。参数的详细信息可查看附录2。

enable：口令身份鉴别的总开关。该参数控制下述几个参数功能。

pwdlock：控制密码输入错误次数，超限后用户将被锁定。

pwdlocktime：控制密码连续错误次数超限被锁定的时间。

pwdvaliduntil：控制密码有效期

pwdpolicy：控制密码的复杂程度。

使用如下命令设置和查看口令认证相关的参数：

> #设置hg\_idcheck.enable参数值
> 
> select set\_secure\_param(‘hg\_idcheck.enable’,’off’);
> 
> #重启数据库（该参数重启生效）后查看参数值。该命令会查看所有安全参数的值
> 
> select show\_secure\_param();

### 2.3.1. 口令策略

为新用户指定口令时需要遵循一定的复杂度要求，也就是口令策略。

瀚高安全版数据库的口令策略与其他版本功能略有差异，暂不详细介绍。以下内容为安全版数据库的功能点。

在安全版中，口令策略受安全参数hg\_idcheck.pwdpolicy的影响。当该参数取值为highest时，策略最严格，要求如下。

1、数据库用户密码至少为8位，密码长度最大为1024位。

2、密码必须同时含有大小写字母。

3、密码必须含有数字。

4、密码必须含有特殊字符，特殊字符包括：!@#$%^&\*()

5、密码不能含有当前用户名字符串。

6、密码不能含有瀚高数据库保留字和关键字。

7、新密码不能使用前五次使用过的密码。

当hg\_idcheck.pwdpolicy取值为high时，只需要满足上述1、2、3、4。

当hg\_idcheck.pwdpolicy取值为medium时，只需要满足上述1、2、3，其中2中字母只区分大小写。

当hg\_idcheck.pwdpolicy取值为low时，表示密码不受限制。

使用如下命令设置和查看口令策略：

> #设置hg\_idcheck.pwdpolicy参数值
> 
> select set\_secure\_param(‘hg\_idcheck.pwdpolicy’,’medium’);
> 
> #查看参数值。该命令会查看所有安全参数的值
> 
> select show\_secure\_param();

### 2.3.2. 口令有效期

口令有效期与VALID UNTIL语句以及安全参数hg\_idcheck.pwdvaliduntil有关。hg\_idcheck.pwdvaliduntil参数的值在下次修改密码后才生效。举例说明：

1. 在2020年1月1日执行CREATE USER或者ALTER USER时指定VAILD UNTIL为‘2020-02-01’表示该用户的密码有效期到2020年2月1日，为期一个月；
2. 此时hg\_idcheck.pwdvaliduntil的参数值为默认值7天；
3. 同样在2020年1月1日，修改该用户的密码。修改之后新密码的有效期则变为了7天；
4. 可以执行ALTER USER命令修改VAILD UNTIL选项为一年，此时第3步中的新密码的有效期则变为了一年。
5. 若下次再进行密码修改，密码的有效期则是hg\_idcheck.pwdvaliduntil的参数值。

使用如下命令查看口令有效期：

> #查看用户口令到期时间
> 
> \\du+ *user\_name*
> 
> #或者
> 
> SELECT rolname,rolvaliduntil FROM pg\_roles WHERE rolname=’ *user\_name* ‘;
> 
> #查看hg\_idcheck.pwdvaliduntil参数值
> 
> select show\_secure\_param();

### 2.3.3. 用户锁定

用户使用md5、sm3或scram-sha-256认证方式从客户端登陆时，连续输错密码次数过多将锁定用户，默认允许密码连续输错的次数为5次。

已经被锁定的用户可以使用syssso用户解锁，解锁的方法是:

> select user\_unlock(‘ *user\_name* ‘);

管理员用户syssso自己是不会被锁定的。

密码输错多次用户被锁定后，默认24小时后自动解锁，用户可自行配置锁定时间，参考配置参数pwdlocktime。

## 2.4. 修改用户信息

为保证数据安全性，用户应定期修改口令，并使用highest级别的口令策略。可使用ALTER USER命令修改口令，除此之外还可使用该命令修改其他信息，如用户名。

ALTER USER的语法格式如下：

> ALTER USER *role\_specification* \[ WITH \] *option* \[ … \]
> 
> ⁣⁣⁣⁣  
> 其中 *option* 可以是：
> 
> 　SUPERUSER | NOSUPERUSER
> 
> 　| CREATEDB | NOCREATEDB
> 
> 　| CREATEROLE | NOCREATEROLE
> 
> 　| INHERIT | NOINHERIT
> 
> 　| LOGIN | NOLOGIN
> 
> 　| REPLICATION | NOREPLICATION
> 
> 　| BYPASSRLS | NOBYPASSRLS
> 
> 　| CONNECTION LIMIT *connlimit*
> 
> 　| \[ ENCRYPTED \] PASSWORD *‘password* ‘ | PASSWORD NULL
> 
> 　| VALID UNTIL ‘ *timestamp* ‘
> 
> ⁣⁣⁣⁣  
> ALTER USER *name* RENAME TO *new\_name*
> 
> ⁣⁣⁣⁣  
> ALTER USER { *role\_specification* | ALL } \[ IN DATABASE *database\_name* \] SET *configuration\_parameter* { TO | = } { value | DEFAULT }
> 
> ALTER USER { *role\_specification* | ALL } \[ IN DATABASE *database\_name* \] SET *configuration\_parameter* FROM CURRENT
> 
> ALTER USER { *role\_specification* | ALL } \[ IN DATABASE *database\_name* \] RESET configuration\_parameter
> 
> ALTER USER { *role\_specification* | ALL } \[ IN DATABASE *database\_name* \] RESET ALL
> 
> ⁣⁣⁣⁣  
> 其中 *role\_specification* 可以是：
> 
> 　 *role\_name*
> 
> 　| CURRENT\_USER
> 
> 　| SESSION\_USER
> 
> ⁣⁣⁣⁣  
> 说明：
> 
> SUPERUSER
> 
> NOSUPERUSER
> 
> CREATEDB
> 
> NOCREATEDB
> 
> CREATEROLE
> 
> NOCREATEROLE
> 
> INHERIT
> 
> NOINHERIT
> 
> LOGIN
> 
> NOLOGIN
> 
> REPLICATION
> 
> NOREPLICATION
> 
> BYPASSRLS
> 
> NOBYPASSRLS
> 
> CONNECTION LIMIT *connlimit*
> 
> \[ ENCRYPTED \] PASSWORD *‘password* ‘
> 
> PASSWORD NULL
> 
> VALID UNTIL ‘ *timestamp* ‘
> 
> 这些选项参考CREATE USER。
> 
> ⁣⁣⁣⁣  
> CURRENT\_USER：
> 
> 修改当前用户而不是一个显式指定的用户。
> 
> ⁣⁣⁣⁣  
> SESSION\_USER
> 
> 修改当前会话用户而不是一个显式指定的角色。
> 
> ⁣⁣⁣⁣  
> *new\_name* ：
> 
> 该角色的新名称。
> 
> ⁣⁣⁣⁣  
> *database\_name* ：
> 
> 要在其中设置该配置变量的数据库名称。
> 
> ⁣⁣⁣⁣  
> *configuration\_parameter* 和 *value* ：
> 
> 把这个角色的指定配置参数的会话默认值设置为给定值。如果 *value* 为DEFAULT，相关的变量设置会被移除，这样该用户将会在新会话中继承系统的默认设置。使用RESET ALL可清除所有用户相关的设置。SET FROM CURRENT可以把会话中该参数的当前值保存为用户相关的值。如果指定了 IN DATABASE，只会为给定的用户和数据库设置或者移除该配置参数。
> 
> ⁣⁣⁣⁣  
> 角色相关的变量设置只在登录时生效， SET ROLE以及 SET SESSION AUTHORIZATION不会处理角色相关的变量设置。
> 
> ⁣⁣⁣⁣  
> 关于允许的参数名称和值详见SET和服务器配置章节。

## 2.5. 删除用户

在安全版数据库中，使用sysdba用户删除普通用户。三个管理员用户是无法被删除的。

删除用户的命令为DROP USER语法格式如下：

> DROP USER \[ IF EXISTS \] name \[, …\]

其中name为要删除的用户的名称。

删除用户之前必须删除该用户拥有的所有对象并回收已经授予给该角色在其他对象上的权限。可使用REASSIGN OWNED和DROP OWNED 命令。