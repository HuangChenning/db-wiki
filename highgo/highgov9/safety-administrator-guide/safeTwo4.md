---
title: "数据库角色"
book: "管理员指南"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/safety/safeTwo4.html"
tags:
  - highgo
  - highgo-v9
  - safety-administrator-guide
---

## 数据库角色

## 数据库角色

数据库角色在概念上已经完全独立于操作系统用户。事实上可能维护一个对应关系会比较方便，但是这并非必需。数据库角色在一个数据库集群安装范围内是全局的（而不是独立数据库内）。要创建一个角色，可使用CREATE ROLE SQL 命令：

---

CREATE ROLE name;

---

name遵循 SQL 标识符的规则：或是不包含特殊字符，或是用双引号包围（实际上，经常给这个命令加上其它选项，例如LOGIN。更多细节可见下文）。要删除一个已存在的角色，使用DROP ROLE命令：

---

DROP ROLE name;

---

为了方便，createuser和dropuser程序被提供作为这些 SQL 命令的包装器，它们可以从shell 命令行调用：

createuser name

dropuser name

查看已存在的角色，可以查询pg\_roles系统表，例如：

SELECT rolname FROM pg\_roles;

psql程序的\\du元命令也可以用来列出已存在的角色。

为了引导数据库系统，一个刚刚初始化好的系统会包含一个预定义角色。这个角色一般是一个”superuser”。为了创建更多角色，你首先必须以初始角色的身份连接。

每一个数据库连接都是使用某个特定角色名建立的，并且这个角色决定初始化权限。通过客户端连接数据库要求使用特定的格式。例如，psql命令使用-U行选项来指定要用哪个角色连接。很多应用将当前操作系统用户（包括createuser和psql）设定为默认的数据库用户。因此在角色和操作系统用户之间维护一个名字对应关系通常是很方便的。

通过客户端的认证方式来决定客户端哪些用户能够连接数据库，这些在第三章中有解释（因此，一个客户端不止限于以匹配其操作系统用户的角色连接，就像一个人的登录名不需要匹配他的真实名字一样）。因为角色身份决定一个已连接客户端可用的权限集合，在设置一个多用户环境时要小心地配置权限。

## 角色属性

一个数据库角色可以有一些属性，它们定义角色的权限并且与客户端认证系统交互。

1. login privilege

只有具有LOGIN属性的角色才能连接到数据库。带有LOGIN属性的角色可以被认为是一个”数据库用户”。创建带有登录权限的角色，语法如下：

CREATE ROLE name LOGIN;

CREATE USER name;

（CREATE USER和CREATE ROLE等效，除了CREATE USER默认假定有LOGIN，而CREATE ROLE没有）。

2. superuser status

数据库超级用户会绕开所有权限检查，除了登入权限。这是一个危险的权限并且应该小心使用，最好用一个不是超级用户的角色来完成大部分工作。要创建一个新数据库超级用户，必须用超级用户来执行，如下：

CREATE ROLE *name* SUPERUSER

3. database creation

一个角色必须被显式给予create database的权限（除了超级用户，因为它们会绕开所有权限检查）。要创建一个有create database权限的角色，如下：

CREATE ROLE *name* CREATEDB;

4. role creation

一个角色具有创建更多角色的权限必须显式授于create role的权限（除了超级用户，因为它们会绕开所有权限检查）。要创建这样一个角色，使用

CREATE ROLE name CREATEROLE;

一个带有CREATEROLE权限的角色也可以修改和删除其他角色，还可以授予或回收角色中的成员关系。然而，要创建、修改、删除或修改一个超级用户角色的成员关系，需要以超级用户的身份操作。CREATEROLE属性没有做这个的权限。

5. initiating replication

一个角色必须被显式授于流复制初始化权限（除了超级用户，因为它们会绕开所有权限检查）。一个流复制的角色必须也具有LOGIN权限。要创建这样一个角色，使用

CREATE ROLE name REPLICATION LOGIN;

6. password

当客户端认证方法要求用户在连接数据库时提供口令。password、md5认证方法需要使用口令。数据库口令与操作系统口令分开。在角色创建时指定口令：

CREATE ROLE *name* PASSWORD ' *string* ';

对已创建的角色可以用ALTER ROLE修改其属性。CREATE ROLE和ALTER ROLE命令的更多细节见相关章节

| 提示： |
| --- |
| 一个好习惯是创建一个具有CREATEDB和CREATEROLE权限的角色，而不是创建一个超级用户，用这个角色来完成对数据库和角色的日常管理。这种方法避免了在非必要时作为超级用户操作的风险。 |

对于第2章中描述的服务器配置设置，一个角色也可以设置特定的默认值。例如，如果想在连接时禁用索引扫描（提示：不是好方法），可以使用：

ALTER ROLE *myname* SET enable\_indexscan TO off;

保存设置（但是不会立刻生效）。在这个角色的后续连接时被执行SET enable\_indexscan TO off。你也可以在会话期间改变该设置，它将只是作为默认值。要移除角色的默认设置，使用

ALTER ROLE *rolename* RESET *varname*;

注意：没有LOGIN权限的角色的默认值是毫无意义的，因为它们从不会被调用。

## 角色成员关系

把用户分组便于权限管理：那样，可以将组作为一个整体，将权限进行授予与回收。在瀚高数据库中通过创建一个组角色来实现，并且然后将在该组角色中的成员关系授予给单独的用户角色。

要建立一个组角色，首先创建该角色：

CEATE ROLE name;

通常组角色不需要有LOGIN属性，不过如果你想也可以设置它。

一旦组角色存在，你可以使用GRANT和REVOKE命令增加和移除成员：

GRANT group\_role TO role1,...;

REVOKE group\_role FROM role1,...;

你也可以为其他组角色授予成员关系（因为组角色和非组角色之间其实没有任何区别）。数据库将不会让你设置闭环的成员关系。另外，不允许把一个角色中的成员关系授予给PUBLIC。

组角色的成员可以有两种方式使用角色的权限。第一，一个组的每一个成员可以显式通过SET ROLE来临时”成为”组角色。在这种状态中，数据库会话可以访问组角色而不是原始登录角色的权限，并且任何被创建的数据库对象被认为属于组角色而不是登录角色。第二，有INHERIT属性的成员角色自动地具有它们所属角色的权限，包括任何组角色继承得到的权限。如下操作：

CREATE ROLE joe LOGIN INHERIT;

CREATE ROLE admin NOINHERIT;

CREATE ROLE wheel NOINHERIT;

GRANT admin TO joe;

GRANT wheel TO admin;

角色joe连接数据库后，立即拥有直接授予给joe的权限，外加任何授予给admin的权限，因为joe”继承了” admin的权限。然而，授予给wheel的权限不可用，因为即使joe是wheel的一个间接成员，但是该成员关系是通过带NOINHERIT属性的admin得到的。执行：

SET ROLE admin;

之后，该会话将只拥有授予给admin的权限，但是没有授予给joe的权限，再执行：

SET ROLE wheel;

之后，该会话将只拥有授予给wheel的权限，但是没有授予给joe或admin的权限。初始的权限状态可以使用下面命令之一恢复：

SET ROLE joe;

SET ROLE NONE;

RESET ROLE;

| 注意： |
| --- |
| SET ROLE命令总是允许选择原始登录角色的直接或间接组角色。因此，在上面的例子中，在成为wheel之前不必先成为admin。 |

| **注意：** |
| --- |
| 在 SQL 标准中，用户和角色之间的区别很清楚，并且用户不会自动继承权限而角色会继承。这种行为在瀚高数据库中也可以实现：为要用作 SQL 角色的角色给予INHERIT属性，而为要用作 SQL 用户的角色给予NOINHERIT属性。瀚高数据库默认给所有的角色INHERIT属性。 |

角色属性LOGIN、SUPERUSER、CREATEDB和CREATEROLE是一种特殊权限，但是它们从来不会像数据库对象上的普通权限那样被继承。要使用这些属性，可以通过SET ROLE到一个有这些属性的角色。上述例子，我们可以授予CREATEDB和CREATEROLE给admin角色，joe角色连接的会话不会立即生效，执行SET ROLE admin之后才有CREATEDB和CREATEROLE的权限。

删除组角色，使用DROP ROLE：

DROP ROLE name;

> 任何在该组角色中的成员关系会被自动回收（但是成员自身角色不会受到影响）。

## 删除角色

由于角色可以拥有本身数据库对象和访问其他对象的特权。使用DROP ROLE删除角色前需要删除角色下的对象和被授权供其他角色使用的对象，同时必须回收所有授予该角色的权限。

对象的属主可以使用ALTER命令修改，例如：

ALTER TABLE bobs\_table OWNER TO alice;

此外，REASSIGN OWNED命令可以被用来把要被删除的角色的属主转移给另一个角色。由于REASSIGN OWNED不能访问其他数据库对象，它需要在每一个包含该角色所拥有对象的数据库中运行该命令（注意第一个这样的 REASSIGN OWNED将更改任何在数据库间共享的该角色的属主，即数据库或者表空间）。

一旦有用的对象被转移给新的属主，剩下的对象就可以用DROP OWNED命令删除。由于这个命令不能访问其他数据库中的对象，有必要在每一个包含该角色所拥有对象的数据库中运行该命令。DROP OWNED不能删除数据库或者表空间，因为数据库或表空间不能转移给新属主，需要手工删除。

DROP OWNED也会注意移除不属于目标角色的对象授予给目标角色的任何权限。因为REASSIGN OWNED不会触碰这类对象，一般需要执行REASSIGN OWNED和 DROP OWNED（按照这个顺序！）以完全地移除要被删除对象的依赖对象。

总之，移除曾经有对象的角色的方法为：

REASSIGN OWNED BY doomed\_role TO successor\_role;

DROP OWNED BY doomed\_role;

\-- 在每一个数据库中重复上述命令

DROP ROLE doomed\_role;

如果所有的属主对象没有被转移给了同一个后继拥有者，最好手工处理异常然后执行上述步骤直到结束。

如果有依赖对象存在时执行DROP ROLE，会提示哪些对象需要被重新分配或者删除。

## 默认角色

瀚高数据库提供了一组默认角色，它们提供对特定的、通常需要的、需要特权的功能和信息的访问。同环境下，管理员可以把这些角色GRANT其他用户或者角色，让这些用户能够访问指定的功能和信息。

表 4.1中描述了默认的角色。注意由于额外功能的增加，每一种默认角色相关的权限可能会在未来被改变。管理员应该关注手册中这方面的变化。

| 角色 | 允许的访问 |
| --- | --- |
| pg\_read\_all\_settings | 读取所有配置变量，甚至是那些通常只对超级用户可见的变量。 |
| pg\_read\_all\_stats | 读取所有的pg\_stat\_\*视图并且使用与扩展相关的各种统计信息，甚至是那些通常只对超级用户可见的信息。 |
| pg\_stat\_scan\_tables | 执行可能会在表上取得ACCESS SHARE锁的监控函数（可能会持锁很长时间）。 |
| pg\_monitor | 读取/执行各种不同的监控视图和函数。这角色是pg\_read\_all\_settings，pg\_read\_all\_stats和pg\_stat\_scan\_tables的成员。 |
| pg\_signal\_backend | 发信号到其他后端亿取消查询或中止它的会话。 |
| pg\_read\_server\_files | 允许使用COPY以及其他文件访问函数从服务器上该数据库可访问的任意位置读取文件。 |
| pg\_write\_server\_files | 允许使用COPY以及其他文件访问函数在服务器上该数据库可访问的任意位置中写入文件。 |
| pg\_execute\_server\_program | 允许用运行该数据库的用户执行数据库服务器上的程序来配合COPY和其他允许执行服务器端程序的函数。 |

: 表 4.1 默认角色

pg\_monitor、pg\_read\_all\_settings、pg\_read\_all\_stats和pg\_stat\_scan\_tables角色的目的在于让管理员更简单的监控数据库服务器。它们授予一组常用的特权，这些特权允许角色读取各种有用的配置设置、统计信息以及通常仅限于超级用户的其他系统信息。

pg\_signal\_backend角色是让管理员启用可信任，发送信号给其他后台角色，但是不是超级用户。当前，此角色允许发送信号以取消其他后台的查询或终止会话。不过授予此角色的用户不能向属于超级用户的后台发送信号。

pg\_read\_server\_files、pg\_write\_server\_files以及pg\_execute\_server\_program角色的目的是允许管理员有一些可信，这些角色来访问文件以及以运行数据库的用户在数据库服务器上运行程序，但不是超级用户。 由于这些角色能够访问服务器文件系统上的任何文件，因此在直接访问文件时它们会绕过任何数据库级别的权限检查并且它们可以被用来得到超级用户级别的访问，因此在把这些角色授予给用户时应当特别小心。

在授予这些角色时应当非常小心，以确保它们只被用在需要的地方，并且要理解这些角色会授予对特权信息的访问。

管理员可以用GRANT命令把对这些角色的访问权限授予给用户，例如：

GRANT pg\_signal\_backend TO admin\_user;