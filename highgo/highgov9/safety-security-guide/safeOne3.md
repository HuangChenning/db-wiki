---
title: "用户标识与鉴别"
book: "安全指南"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/safety/safeOne3.html"
tags:
  - highgo
  - highgo-v9
  - safety-security-guide
---

## 用户标识与鉴别

瀚高数据库通过用户标识和认证为系统提供最外层的安全保护措施。在客户端访问数据库资源之前，服务器首先需要通过身份认证模块来验证用户的合法身份，从而在数据库系统的前后端之间建立安全的通信信道，禁止非法用户连接数据库，保证只有合法的用户才能访问数据库资源。

## 如何创建用户

数据库使用过程中往往会根据需要创建多个普通用户。在”权限分立”的机制下，只能由拥有数据库管理员角色的用户创建用户，其他用户无创建用户的权限。

使用CREATE USER命令创建用户。在瀚高数据库中，CREATE USER是CREATE  
ROLE（创建角色）的一个别名。唯一的区别是CREATE  
USER中LOGIN作为默认值，而CREATE  
ROLE的默认值是NOLOGIN。在使用上可以将用户和角色理解为同一概念。

创建用户时需要为用户指定口令用于登录时认证。具体的语法格式如下：

```
CREATE USER user_name [[WITH]option[...]]
```

这里option可以是：

```
SUPERUSER|NOSUPERUSER

|CREATEDB|NOCREATEDB

|CREATEROLE|NOCREATEROLE

|INHERIT|NOINHERIT

|LOGIN|NOLOGIN

|REPLICATION|NOREPLICATION

|BYPASSRLS|NOBYPASSRLS

|CONNECTION LIMIT connlimit

|[ENCRYPTED] PASSWORD 'password' |PASSWORDNULL

|VALID UNTIL 'timestamp'

|IN ROLE role_name[,...]

|IN GROUP role_name[,...]

|ROLE role_name[,...]

|ADMIN role_name[,...]

|USER role_name[,...]

|SYSID uid
```

说明：

user\_name：

要创建的用户的名称，用户名必须以字母或下划线开头，后续字符可以是字母、数字、下划线或美元符号（$）。用户名中不能包含瀚高数据库的关键字和保留字。如需使用关键字、保留字或其他特殊字符，或者要以数字开头，需要使用双引号将用户名引起来，后续引用用户名时也需使用双引号。

SUPERUSER或NOSUPERUSER：

该选项指定创建的用户是否为管理员用户。管理员用户可以越过数据库内的所有访问限制，因此其状态很危险，只应该在必要时使用。要创建一个新的超级用户，自己必须是一个超级用户。默认值是NOSUPERUSER。

CREATEDB或NOCREATEDB：

该选项指定创建的用户/角色是否有创建数据库的权限。如果指定了CREATEDB，新创建的用户将被允许创建新的数据库。默认值是NOCREATEDB。

CREATEROLE或NOCREATEROLE：

创建的用户是否有创建新用户/角色的权限（即执行CREATEROLE）。如果指定CREATEROLE，创建的用户也可以修改和删除其他角色。默认值是NOCREATEROLE。

INHERIT或NOINHERIT：

如果新的用户/角色是其他用户/角色的成员，该选项指定新用户是否从那些用户中”继承”权限，一个带有INHERIT属性的角色/用户能够自动使用已经被授予给其直接或间接父角色的任何数据库特权。默认值是INHERIT。

LOGIN或NOLOGIN

该选项指定新创建的用户/角色是否有登录权限，也就是在客户端连接期间是否能使用该用户登录数据库系统。执行CREATEUSER创建用户时默认值是LOGIN；使用CREATEROLE创建角色时默认值是NOLOGIN。

REPLICATION或NOREPLICATION

该选项指定新创建的用户/角色是否有复制权限。用户必须具有复制权限（或者成为一个超级用户）才能以复制模式（物理复制或者逻辑复制）连接到服务器以及创建或者删除复制槽。一个具有REPLICATION属性的角色是一个具有非常高特权的角色，应慎重使用。默认值是NOREPLICATION。

BYPASSRLS或NOBYPASSRLS

该选项指定新创建的用户是否可以绕过每一条行级安全策略（RLS）。默认是NOBYPASSRLS。注意pg\_dump默认把row\_security设置为OFF，以确保表的所有内容被转储出来。如果运行pg\_dump的用户不具备该权限，将会返回一个错误。被转储表的拥有者总是可以绕过RLS。

CONNECTION LIMIT connlimit：

该选项指定该用户能建立多少并发连接。-1（默认值）表示无限制。注意这个限制仅针对于普通连接。预备事务和后台进程连接不受这一限制。

\[ENCRYPTED\]PASSWORD ‘password’或 PASSWORD NULL

设置用户口令。口令总是以加密的方式存放在系统目录中。ENCRYPTED关键词没有实际效果，只是为了向后兼容性而存在。加密的方法由配置参数password\_encryption决定。如果当前的口令字符串已经是MD5加密或者SCRAM加密的格式，那么不管password\_encryption的值是什么，口令字符串还是原样存储（因为系统无法解密以不同格式加密的口令字符串）。这种方式允许在转储/恢复时重载加密的口令。

VALID UNTIL 'timestamp'

该选项为用户口令设置一个有效期，在该时间点之后用户口令将会失效。

INROLE role\_name

该选项列出一个或多个现有角色。新的角色/用户将作为新成员加入这些角色中。

INGROUP role\_name

同INROLE，是为了向后兼容保留的。不建议使用。

ROLErole\_name

该选项列出一个或者多个现有角色，这些角色会被自动加入到一个新角色中（可以理解为一个”组”）。

ADMIN role\_name

ADMIN子句与ROLE相似，区别是被指定的角色使用WITHADMINOPTION加入到新角色中，让它们能够把这个角色中的成员关系授予给其他人。

USER role\_name

同ROLE，是为了向后兼容保留的。不建议使用。

SYSID uid

该选项是为了向后兼容保留的，无实际功能。不建议使用。

需要注意的是，在权限分立模块开启时，CREATE  
USER语法不支持带有SUPERUSER、CREATEDB、CREATEROLE属性。

示例：

创建一个口令有效期截止到2020年底的用户hg：

```
CREATE USER hg PASSWORD 'Hello@123' VALID UNTIL '2026-01-01';
```

## 用户身份鉴别策略

瀚高数据库提供身份鉴别模块，提供数据库用户的口令复杂度检查策略、口令的有效期限设置、用户异常登录锁定、用户登录信息显示等安全策略的管理机制。在开启三权分立的情况下数据库安全员有权限设置身份鉴别策略，在三权分立模块关闭的情况下超级用户有权限设置身份鉴别策略。

注意

瀚高数据库管理系统V9.0.5之前的版本，本模块涉及的表、函数、视图放在了public模式下；从瀚高数据库管理系统V9.0.5版本开始，将本模块涉及的表、函数、视图均迁移到了hg\_security模式下。如果您在public模式下查询不到相关对象，请您指定hg\_security模式再做查询。

### 规则检查开关

瀚高数据库通过加载credcheck插件，来提供用户名/密码规则检查、密码重复使用、用户锁定、身份验证延迟功能等模块。规则检查总开关credcheck.enable，当开关打开后我们配置的规则检查才会生效，否则不生效。另外，credcheck.enable  
参数仅支持超级用户或者安全管理员用户通过ALTER SYSTEM SET方式设置。

---

| 规则检查参数 | 类型/生效方式 | 描述 | 默认值 | 最小值 | 最大值 |
| --- | --- | --- | --- | --- | --- |
| credcheck.enable | on\|off/重载 | 规则检查等功能总开关 | off |  |  |

---

### 用户名/密码规则设置

瀚高数据库提供灵活的规则配置方式，支持用户自由定义用户名命名规则和密码复杂度规则。由数据库安全管理员或超级管理员对用户名命名规则、口令的最小长度，所包含的数字、英文字母、特殊符号等检查内容进行设置后，在创建和修改用户时，自动对用户名和口令进行相关方面的检查。如果用户名称或口令不满足指定的条件，那么创建用户将不成功。

用户名/密码规则检查发生在创建用户并设置密码时。假如您创建了一个用户A并设置了一个简单的密码，然后通过修改参数设置了较复杂的密码规则并生效，那么用户A仍然可以登录，不受当前复杂密码规则的限制。再次创建用户B，则B用户的密码规则需要遵循当前设置的密码规则。

用户名规则和密码复杂度规则配置参数如下：

| 检查项 | 类型/生效方式 | 描述 | 默认值 | 最小值 | 最大值 |
| --- | --- | --- | --- | --- | --- |
| credcheck.username\_min\_length | 用户名/立即 | 用户名的最小长度 | 1 | 1 | 2147483647注意：瀚高数据库允许的用户名最大长度为63字节。超出部分截断或报错。 |
| credcheck.username\_min\_special | 用户名/立即 | 特殊字符的最小数量 | 0 | 0 | 2147483647 |
| credcheck.username\_min\_digit | 用户名/立即 | 最小数字位数 | 0 | 0 | 2147483647 |
| credcheck.username\_min\_upper | 用户名/立即 | 最小大写数 | 0 | 0 | 2147483647 |
| credcheck.username\_min\_lower | 用户名/立即 | 最小小写数 | 0 | 0 | 2147483647 |
| credcheck.username\_min\_repeat | 用户名/立即 | 连续字符可重复的最大次数 | 0 | 0 | 2147483647 |
| credcheck.username\_contain\_password | 用户名/立即 | 用户名不应包含密码 | on |  |  |
| credcheck.username\_contain | 用户名/立即 | 用户名应包含以下字符之一 | “” |  |  |
| credcheck.username\_not\_contain | 用户名/立即 | 用户名不应包含以下字符之一 | “” |  |  |
| credcheck.username\_ignore\_case | 用户名/立即 | 在执行上述检查时忽略大小写 | on |  |  |
| credcheck.password\_min\_length | 密码/立即 | 密码的最小长度 | 1 | 1 | 2147483647 |
| credcheck.password\_min\_special | 密码/立即 | 特殊字符的最小数量 | 0 | 0 | 2147483647 |
| credcheck.password\_min\_digit | 密码/立即 | 密码中的数字最小位数 | 0 | 0 | 2147483647 |
| credcheck.password\_min\_upper | 密码/立即 | 最小大写字符数 | 0 | 0 | 2147483647 |
| credcheck.password\_min\_lower | 密码/立即 | 最小小写字符数 | 0 | 0 | 2147483647 |
| credcheck.password\_min\_repeat | 密码/立即 | 连续字符可重复的最大次数 | 0 | 0 | 2147483647 |
| credcheck.password\_contain\_username | 密码/立即 | 密码不应包含password | on |  |  |
| credcheck.password\_contain | 密码/立即 | password应包含以下字符 | “” |  |  |
| credcheck.password\_not\_contain | 密码/立即 | 密码不应包含这些字符 | “” |  |  |
| credcheck.password\_ignore\_case | 密码/立即 | 在执行上述检查时忽略大小写 | on |  |  |
| credcheck.whitelist | 密码/立即 | 要从密码策略检查中排除的用户名列表，以逗号分隔 | “” |  |  |
| credcheck.password\_valid\_until | 密码/立即 | 有效期最小天数。当该参数设置后，在执行CREATE ROLE/USER、ALTER ROLE/USER语句中要求强制使用VALID UNTIL子句，且具有最少天数，0为不限制 | 0 | 0 | 2147483647 |
| credcheck.password\_valid\_max | 密码/立即 | 有效期最大天数。当该参数设置后，在执行CREATE ROLE/USER、ALTER ROLE/USER语句中要求强制使用VALID UNTIL子句，最大天数，0为不限制 | 0 | 0 | 2147483647 |
| credcheck.password\_force\_set | 密码/立即 | 强制在CREATE USER语句中设置密码 | off |  |  |

除大写字母、小写字母、数字外的所有字符(包括中文等)都被视为特殊字符，如：  
!, ", #, $, %, &, ', (, ), \*, +,,, -,., /,:,;, <, =, >,?, @,  
\[, \\, \], ^, \_, \`{, |, }, ~

用户名密码规则设置示例：

highgo用户登录并启用身份鉴别规则检查开关，设置用户名最小长度为2，密码最小长度为5，包含特殊字符的数量最少为2，用户的有效期范围为最大10天最小5天。

```
highgo=# \c highgo highgo

hgdb-client-V9.0.5

您现在已经连接到数据库 "highgo",用户 "highgo".

highgo=#

highgo=# alter system set credcheck.enable =on;

ALTER SYSTEM

highgo=# select pg_reload_conf();

2025-11-13 16:59:33.093 CST [18539] 日志: 接收到 SIGHUP, 重载配置文件

pg_reload_conf

------------------------------------

t

(1 行记录)

highgo=# 2025-11-13 16:59:33.095 CST [18539] 日志: 参数
"credcheck.enable"被改为"on"

highgo=# set credcheck.username_min_length=2;

SET

highgo=# set credcheck.password_min_length =5;

SET

highgo=# set credcheck.password_min_special=2;

SET

highgo=# set credcheck.password_valid_until =5;

SET

highgo=# set credcheck.password_valid_max =10;

SET

highgo=# select now();

now

------------------------------------------------------

2025-11-13 17:01:42.419382+08

(1 行记录)

highgo=# create user u1 valid until '2025-11-23';

CREATE ROLE

highgo=# create user u2 password 'hgo!@' valid until '2025-11-23';

CREATE ROLE
```

### 密码重用

瀚高数据库提供密码重用限制功能，即设置新密码时，不可以与指定次数内以及指定时间段内的历史密码相同。

重复使用密码的限制如下：

---

| 检查 | 类型/生效方式 | 描述 | 默认值 | 最小值 | 最大值 |
| --- | --- | --- | --- | --- | --- |
| credcheck.password\_reuse\_history | 次数/立即 | 不可重复使用的最近次数，0为不限制 | 0 | 0 | 100 |
| credcheck.password\_reuse\_interval | 天数/立即 | 不可重复使用的最少天数，0为不限制 | 0 | 0 | 730 |
| credcheck.history\_max\_size | 缓存/重启 | 所有用户历史密码记录缓存条数最大值，如果记录条数超过此值则覆盖 | 65535 | 1 | 2,097,151 |
| credcheck.encrypted\_password\_allowed | 开关/立即 | 是否可以设置密文密码 | off |  |  |

所有用户历史密码记录到hg\_security.pg\_password\_history视图中，查询方式如下：

```
SELECT rolename, password_hash FROM hg_security.pg_password_history;
```

支持安全管理员清空历史密码记录集函数为hg\_security.pg\_password\_history\_reset，用户名参数为可选，不指定用户则清空所有用户历史密码记录：

```
SELECT hg_security.pg_password_history_reset('username');

SELECT hg_security.pg_password_history_reset();
```

密码重用示例：

将密码重用次数设置为2，修改用户时再次使用相同的密码则报错：

```
highgo=# set credcheck.password_reuse_history=2;

highgo=# create user u3 password 'highgo@!' valid until
'2025-11-23';

CREATE ROLE

highgo=# alter user u3 password 'highgo@!';

2025-11-13 17:08:22.886 CST [20612] 错误: Cannot use this credential
following the password reuse policy

错误: Cannot use this credential following the password reuse policy

highgo=# alter user u3 password 'hello@!!';

ALTER ROLE
```

查看所有用户历史密码：

```
highgo=# SELECT rolename,password_hash FROM
hg_security.pg_password_history; rolename | password_hash

----------------------------------------------------------------

u3 | cb9b10ed54a980225ffc2a702c3ccf2aa2ec523e91026a01bcde7cfa5218dc8a

u3 | 2b9a78f12b1fcf35a2f90b3fdbb4e280e140b674ff8db8a021309e1805a64060

(2 行记录)
```

### 用户锁定

瀚高数据库提供用户锁定功能，即用户在连续输入错误密码指定次数之后被锁定，被锁定用户可被超级用户或安全管理员解锁或者锁定时间达到解锁时长后自动解除锁定。

连续输入错误密码的用户锁定限制如下：

| 检查 | 类型/生效方式 | 描述 | 默认值 | 最小值 | 最大值 |
| --- | --- | --- | --- | --- | --- |
| credcheck.max\_auth\_failure | 次数/重载 | 连续输入错误密码最大次数，0为不限制。注意：输错一次计数递增1。开启SSL功能则每次递增0.5 | 0 | 0 | 64 |
| credcheck.reset\_superuser | 开关/重载 | 连续输入错误密码最大次数是否排除限制管理员，默认不排除。即reset\_superuser=off表示受密码次数限制。 | off |  |  |
| credcheck.auth\_failure\_cache\_size | 缓存/重启 | 用户输错密码则产生一条记录，再次输错密码则累加计数不新增记录，输入正确密码则删除记录，所有用户产生的所有记录条数，默认值为1024，超出则覆盖 | 1024 | 1 | 2,097,151 |
| credcheck.reset\_time\_min | 时间/重载 | 自动解锁时间(有效单位：”min”,”h”,”d”，默认值”min”) | 1d | 0 | 2,097,151 |

支持超级用户或安全管理员解除已锁定的用户，调用函数pg\_banned\_role\_reset()，不带参数时解锁所有被锁定用户，带参数时解锁指定用户，示例如下：

```
解锁所有用户：select hg_security.pg_banned_role_reset();
解锁指定用户：select hg_security.pg_banned_role_reset('username');
```

auth\_failure\_cache\_size对应产生的缓存记录信息被记录到视图pg\_banned\_role，查询示例如下：

highgo用户登录，查询已锁定的用户

```
highgo=# \c highgo highgo

hgdb-client-V9.0.5

您现在已经连接到数据库 highgo",用户 "highgo".

highgo=# select * from hg_security.pg_banned_role ;
```

解锁用户u1

```
highgo=# select * from hg_security.pg_banned_role_reset('u1');
```

解锁所有用户

```
highgo=# select * from hg_security.pg_banned_role_reset();
```

登录失败信息保存在内存中不被永久保存，数据库重启后登录失败信息丢失用户锁定失效。

### 身份验证延迟

瀚高数据库提供用户身份验证延迟功能，当用户输入错误密码后，身份验证流程暂停指定时间。

| 检查 | 类型/生效方式 | 描述 | 默认值 | 最小值 | 最大值 |
| --- | --- | --- | --- | --- | --- |
| credcheck.auth\_delay\_ms | 时间/重载 | 认证失败后休眠时间(有效单位：”ms”,”s”,”min”，默认值”ms”) | 0 | 0 | 2147483 |

### 显示登录信息

用户登录成功后显示用户登录信息，登录信息显示内容包括用户名、IP地址、上次登录状态、当前时间、用户有效期时间(上次登录状态正确显示依赖于用户连续输入错误密码参数max\_auth\_failure的设置，用户锁定功能关闭则不显示)。

| 检查 | 类型/生效方式 | 描述 | 默认值 | 最小值 | 最大值 |
| --- | --- | --- | --- | --- | --- |
| credcheck.login\_msg\_display | 开关/立即 | 是否显示登录信息on\|off | on |  |  |

示例：

```
[highgo@node1 bin]$ ./psql highgo highgo
```

信息:

```
------------------------------------------------

Login User : highgo

Login Address : [local]

Last Login Status :

Current Time : 2025-11-13 17:29:38+08

User Valid Until :

-----------------------------------------------

psql (14.20)

hgdb-client-V9.0.5

输入 "help" 来获取帮助信息.

highgo=# show credcheck.login_msg_display;

credcheck.login_msg_display

-----------------------------------------------

on

(1 行记录)
```

### 密码过期告警

用户密码过期前72小时内，用户通过psql登录时会收到用户密码即将过期的告警通知。同时，提供密码过期告警查询接口：user\_expiration\_info()，您可以选择指定用户名也可以不指定用户名，不指定用户名时查询所有用户临过期（72小时内）信息；

用户密码过期后，可以通过安全管理员对用户密码有效期进行修改。但是需要注意的是，修改用户密码有效期时需要结合password\_valid\_until、password\_valid\_max参数值来设定，用户密码有效期需要设置在这两参数设置的最小及最大值区间范围内。

### 参数设置说明

瀚高数据库中，所有涉及时间设置的参数都有一个最小时间单位。当设置为较大的时间单位并且包含小数时，系统会根据四舍五入的规则将小数部分取整到下一级时间单位。例如：

如果设置的时间单位是小时（h），并且包含小数部分（如 1.21  
h），系统会将该值换算成分钟（min）并进行四舍五入取整。1.21 h等于 73  
分钟，因此 1.21 小时会被取整为 73 分钟。

同样，如果设置的时间单位是分钟（min），并且包含小数部分（如 1.21  
分钟），系统会将该值换算成秒（s）并进行四舍五入取整。1.21 分钟等于 73  
秒，因此 1.21 分钟会被取整为 73 秒。

所有涉及到四舍五入的GUC参数均遵循银行家舍入规则，银行家四舍五入规则（又称”就近偶数舍入法”或”Round  
Half to Even”）是一种用于减少累计舍入偏差的方法，其规则如下：

首先，根据通常的规则对数值进行四舍五入处理。如果尾数（或舍弃的位数）小于  
0.5，则该数值舍入为较低的整数；如果大于 0.5，则舍入为较高的整数。

当数值的尾数正好为 0.5  
时，不再一味地向上舍入，而是将结果舍入到最接近的偶数。例如：

2.5 舍入结果为 2（因为 2 是偶数）；

3.5 舍入结果为 4（因为 4 是偶数）。

## 用户会话管理

本模块提供用户锁定和解锁其拥有的交互式会话的能力。在一定的时间内用户如果一直不活动，用户可以发起对当前交互式会话的锁定操作。锁定会话后将会阻塞当前会话连接，结束其继续执行相关操作，锁定会话是一个重要的管理与安全机制。

本功能为V9.0.5版本新增功能。

### 锁定会话

手动锁定会话

提供内置函数lock\_current\_session()，用户执行该函数将手动锁定当前会话。会话锁定后，执行psql端的简单查询会告警返回，提示用户应该先执行解锁操作。

超时自动锁定会话

新增GUC参数hg\_session\_locking\_timeout，单位为毫秒，当会话空闲时间超过参数设定的值时，系统将执行自动锁定会话操作，该参数需要重启生效，数据库安全员或超级用户有权限设置该参数。

特别注意，自动锁定会话参数hg\_session\_locking\_timeout设置的值要小于超时断开会话连接参数idle\_sesssion\_timout，否则在启动或重启数据库时会报错。

### 解锁会话

提供内置函数unlock\_current\_session()，用户执行该函数后将手动解锁当前会话。

示例：

登录u1用户并执行锁定会话操作

```
highgo=# \c - u1
```

用户 u1 的口令：

```
highgo=> select lock_current_session();

lock_current_session

-----------------------------------------------

lock current session successfully

(1 行记录)
```

锁定会话后，不允许用户做任何操作

```
highgo=> select now();

WARNING: current session is locked, please unlock first
```

解除当前会话锁定

```
highgo=> select unlock_current_session();

unlock_current_session
-----------------------------------------------
unlock current session successfully

(1 行记录)
```

### 查看会话信息

提供pg\_stat\_activity系统视图将每个服务器进程显示为一行，用于实时监控数据库中所有活跃会话（连接）的状态和当前正在执行的操作。

另外，提供hg\_security.hg\_stat\_session视图作为pg\_stat\_activity的补充，支持对客户端MAC地址、客户操作系统信息、等待时间统计信息等信息的统计。

pg\_stat\_activity视图：

| 列 | 类型 | 描述 |
| --- | --- | --- |
| datid | oid | 这个后端连接到的数据库的OID |
| datname | name | 这个后端连接到的数据库的名称 |
| pid | datname | name |
| usesysid | oid | 登录到这个后端的用户的OID |
| usename | name | 登录到这个后端的用户的名称 |
| application\_name | text | 连接到这个后端的应用的名称 |
| client\_addr | inet | 连接到这个后端的客户端的IP 地址。如果这个域为空，它表示客户端通过服务器机器上的一个 Unix 套接字连接或者这是一个内部进程（如 自动清理）。 |
| client\_hostname | text | 已连接的客户端的主机名，由client\_addr的反向DNS查找报告。这个域将只对IP连接非空，并且只有log\_hostname被启用时才会非空。注意：该字段的显示要依赖客户端和服务器的配置，即log\_hostname参数设置为on，客户端登录方式为tcp/ip（非本地），且服务端网络环境支持通过IP地址获取到客户端的hostname |
| client\_port | integer | 客户端用以和这个后端通信的TCP端口号，如果使用Unix 套接字则为-1 |
| backend\_start | timestamp with time zone | 这个进程被启动的时间。对客户端后端来说就是客户端连接到服务器的时间。 |
| xact\_start | timestamp with time zone | 这个进程的当前事务被启动的时间，如果没有活动事务则为空。如果当前查询是它的第一个事务，这一列等于query\_start。 |
| query\_start | timestamp with time zone | 当前活动查询被开始的时间，如果state不是active，这个域为上一个查询被开始的时间 |
| state\_change | timestamp with time zone | state上一次被改变的时间 |
| wait\_event\_type | text | 后端正在等待的事件类型，如果不存在则为NULL。可能的值有： LWLock：后端正在等待一个轻量级锁。每一个这样的锁保护着共享内存中的一个特殊数据结构。wait\_event将含有一个标识该轻量级锁目的的名称（一些锁具有特定的名称，其他是一组具有类似目的的锁中的一部分）。Lock：后端正在等待一个重量级锁。重量级锁，也称为锁管理器锁或者简单锁，主要保护SQL可见的对象，例如表。不过它们也被用于确保特定内部操作的互斥，例如关系扩展。wait\_event将标识等待的锁的类型。BufferPin：服务器进程正在等待访问一个数据缓冲区，而此时没有其他进程正在检查该缓冲区。如果另一个进程持有一个最终从要访问的缓冲区中读取数据的打开的游标，缓冲区pin等待可能会被拖延。Activity：服务器进程处于闲置状态。这被用于在其主处理循环中等待活动的系统进程。wait\_event将标识特定的等待点。 Extension：服务器进程正在一个扩展模块中等待活动。这一个分类被用于要跟踪自定义等待点的模块。Client：服务器进程正在一个套接字上等待来自用户应用的某种活动，并且该服务器预期某种与其内部处理无关的事情发生。wait\_event将标识特定的等待点。IPC：服务器进程正在等待来自服务器中另一个进程的某种活动。wait\_event将标识特定的等待点。 Timeout：服务器进程正在等待一次超时发生。wait\_event将标识特定的等待点。 IO：服务器进程正在等待一次IO完成。wait\_event将标识特定的等待点。 |
| wait\_event | text | 如果后端当前正在等待，则是等待事件的名称，否则为NULL。详见表12.4。 |
| state | text | 这个后端的当前总体状态。可能的值是： active：后端正在执行一个查询。 idle：后端正在等待一个新的客户端命令。 idle in transaction：后端在一个事务中，但是当前没有正在执行一个查询。 idle in transaction (aborted)：这个状态与idle in transaction相似，不过在该事务中的一个语句导致了一个错误。 fastpath function call：后端正在执行一个fast- path函数。 disabled：如果在这个后端中track\_activities被禁用，则报告这个状态。 |
| backend\_xid | xid | 这个后端的顶层事务标识符（如果存在）。 |
| backend\_xmin | xid | 当前后端的xmin范围。 |
| query | text | 这个后端最近查询的文本。如果state为active，这个域显示当前正在执行的查询。在所有其他状态下，它显示上一个被执行的查询。默认情况下，查询文本会被截断至1024个字符，这个值可以通过参数track\_activity\_query\_size更改。 |
| backend\_type | text | 当前后端的类型。可能的类型是 autovacuum launcher, autovacuum worker, logical replication launcher, logical replication worker,parallel worker, background writer, client backend,checkpointer, startup,walreceiver, walsender以及walwriter。除此以外，由扩展注册的后台Worker可能有额外的类型。 |

hg\_security.hg\_stat\_session视图

| 列 | 类型 | 来源 | 描述 |
| --- | --- | --- | --- |
| datid | OID | pg\_stat\_activity | 会话所连接的数据库OID。 |
| datename | name | pg\_database | 会话所连接的数据库名称（由 datid关联 pg\_database得到）。 |
| pid | integer | pg\_stat\_activity | 会话的进程ID。 |
| sid | OID | pg\_stat\_activity\_ext | 会话ID |
| idle\_time | text | pg\_stat\_activity\_ext | 空闲总时长，新增GUC开关count\_idle\_busy\_time，仅当其打开时，会统计该值，否则为0。开关默认不开启，仅超级用户可通过alter system命令设置，需要重启。 |
| busy\_time | text | pg\_stat\_activity\_ext | 忙总时长，仅当count\_idle\_busy\_time打开时统计，否则为0 |
| trans\_info | text | pg\_stat\_activity\_ext | 事务状态 |
| tid | OID | pg\_stat\_activity\_ext | 事务ID |
| proto | text | pg\_stat\_activity\_ext | 协议名，固定值“TCP/IP” |
| def\_schema | text | pg\_stat\_activity\_ext | 固定值：”$user”, public |
| type | int4 | pg\_stat\_activity\_ext | 客户端类型，1表示psql，0表示jdbc或其它 |
| is\_share | bool | pg\_stat\_activity\_ext | 端口连接方式，true表示共享，false表示不共享 |
| is\_locked | bool | pg\_stat\_activity\_ext | 会话是否锁定，true表示锁定，false不锁定 |
| usesysid | OID | pg\_stat\_activity | 登录该会话的用户的OID。 |
| rolename | name | pg\_authid | 登录该会话的用户名（由 usesysid关联 pg\_authid得到）。 |
| application | text | pg\_stat\_activity | 客户端应用程序的名称，由客户端在连接时通过 application\_name参数设置。 |
| client\_osname | text | pg\_stat\_activity\_ext | 客户端操作系统的名称。 |
| client\_addr | inet | pg\_stat\_activity\_ext | 客户端的IP地址。 |
| client\_hostname | text | pg\_stat\_activity\_ext | 客户端的主机名。注意：该字段的显示要依赖客户端和服务器的配置，即log\_hostname参数设置为on，客户端登录方式为tcp/ip（非本地），且服务端网络环境支持通过IP地址获取到客户端的hostname |
| client\_port | integer | pg\_stat\_activity\_ext | 客户端用于与后端通信的TCP端口号。 |
| client\_uid | OID | pg\_stat\_activity | 客户端操作系统中发起连接用户的用户ID（UID）。 |
| client\_pid | integer | pg\_stat\_activity | 客户端应用程序的进程ID（PID）。 |
| client\_mac | macaddr | pg\_stat\_activity | 客户端的MAC地址（物理地址）。通常只在本地网络连接且系统支持时才能获取。 |
| backend\_start | timestamptz | pg\_stat\_activity | 该进程启动的时间（即客户端连接到服务器的时间）。 |
| xact\_start | timestamptz | pg\_stat\_activity | 当前事务开始的时间。如果当前未在事务中，则为NULL。 |
| query\_start | timestamptz | pg\_stat\_activity | 当前正在执行的查询开始的时间 |
| state\_change | timestamptz | pg\_stat\_activity | 会话状态（state）最后一次改变的时间。 |
| wait\_event\_type | text | pg\_stat\_activity | 等待事件的类型。如果会话当前正在等待某事，则此字段显示等待的类型（如 Lock, LWLock, BufferPin等），否则为NULL。 |
| wait\_event | text | pg\_stat\_activity | 等待事件的名称。与 wait\_event\_type配合使用，指明具体等待什么（如某个锁的名称）。 |
| state | text | pg\_stat\_activity | 会话的当前总体状态。取值：active（活动idle）, idle（空闲）idle in transaction（事务中空闲）, idle in transaction (aborted)（事务中空闲-已终止）, fastpath function call（快速路径函数调用）, disabled（禁用，track\_activities关闭）。 |
| backend\_xid | xid | pg\_stat\_activity | 此会话的顶级事务ID（如果存在）。 |
| backend\_xmin | xid | pg\_stat\_activity | 此会话的最早活跃事务ID（xmin），用于判断元组可见性。 |
| query | text | pg\_stat\_activity | 该会话最近正在执行的查询语句。如果state不是active，则显示的是上一条执行完毕的查询。 |
| backend\_type | text | pg\_stat\_activity | 后端进程的类型。取值：client backend（客户端后台进程）, autovacuum worker（自动清理工作进程）, walsender（WAL发送进程）。 |

### 查看连接信息

提供hg\_security.hg\_db\_connection\_info视图,用户可从该视图获取到数据库连接信息。

| 列 | 类型 | 来源 | 描述 |
| --- | --- | --- | --- |
| datid | OID | pg\_d提供hg\_security.hg\_db\_connection\_info视图,用户可从该视图获取到数据库连接信息。atabase.oid | 数据库的对象标识符（OID） |
| datname | name | pg\_database.datname | 数据库的名称 |
| connect\_nums | bigint | 聚合函数 count() | 连接到该数据库的会话数量 |
| proto | text | hg\_stat\_session.proto | 连接使用的协议类型 |
| type | text | 聚合函数 hg\_group\_concat(type) | 所有连接的客户端类型列表，1表示psql，0表示jdbc或其它，用换行符分隔 |
| connect\_name | text | 聚合函数 hg\_group\_concat(application\_name) | 所有连接的应用程序名称列表，用换行符分隔 |
| usesysid | text | 聚合函数 hg\_group\_concat(usesysid) | 所有连接的用户OID列表 |
| usename | text | 聚合函数 hg\_group\_concat(usename) | 所有连接的用户名列表 |
| state | text | 聚合函数 hg\_group\_concat(state) | 所有会话的状态列表 |
| excute\_content | text | 聚合函数 hg\_group\_concat(query) | 所有连接正在执行或最后执行的查询列表，用换行符分隔 |