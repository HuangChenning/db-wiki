---
title: "过程语言"
book: "服务器编程指南"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/reference/referenceTwo6.html"
tags:
  - highgo
  - highgo-v9
  - server-programming-guide
---

## 过程语言

## 安装过程语言

在每一个要使用过程语言的数据库中都必须”安装”相应的过程语言。不过安装在数据库template1中的过程语言会被后续创建的数据库自动继承，因为template1中与过程语言相关的项会被CREATE DATABASE复制。因此，数据库管理员可以决定在哪些数据库中可以使用哪些语言，并且按照选择让一些语言默认可用。

对于标准发布所提供的语言，只需要执行CREATE EXTENSION language\_name来把该语言安装在当前数据库中。 下文所述的手工过程主要是为了安装没有被包装成扩展的语言。

手工安装过程语言

安装一个过程语言到一个数据库中包括五个步骤，且必须由一个数据库超级用户来执行。在大部分情况下，所需的 SQL 命令应该被打包成一个”扩展”的安装脚本，这样可以用CREATE EXTENSION来执行它们。

1\. 用于语言处理器的共享对象必须被编译并安装到一个合适的库目录中。这和编译和安装常规的用户定义 C 函数一样， 参见 。通常，语言处理器将依赖于一个实际提供编程语言引擎的外部库，如果是这样，那些外部库也应该被安装。

2\. 处理器必须用下面的命令声明

CREATE FUNCTION handler\_function\_name()

RETURNS language\_handler

AS 'path-to-shared-object'

LANGUAGE C;

特殊的返回类型language\_handler告诉数据库系统，这个函数不返回已定义的SQL数据类型，并且不能直接在SQL语句中使用。

3\. (可选的) 可选地，语言处理器能提供一个”内联”处理器函数来执行用这种语言编写的匿名代码块（DO命令）。如果该语言提供了一个内联函数，用类似下面的命令声明它

CREATE FUNCTION inline\_function\_name(internal)

RETURNS void

AS 'path-to-shared-object'

LANGUAGE C;

4\. (可选的) 可选地，语言处理器能提供一个”验证器”函数用来检查一个函数定义的正确性而无需实际执行它。如果验证器函数存在，它将被CREATE FUNCTION调用。如果该语言提供了一个验证器函数，用类似下面的命令声明它CREATE FUNCTION validator\_function\_name(oid)

RETURNS void

AS 'path-to-shared-object'

LANGUAGE C STRICT;

5\. 最后，PL 必须用下面的命令声明

CREATE \[TRUSTED\] LANGUAGE language\_name

HANDLER handler\_function\_name

\[INLINE inline\_function\_name\]

\[VALIDATOR validator\_function\_name\];

可选的关键词TRUSTED指定，如果用户不具有访问数据的权限，该语言不会授予对数据的访问。可信的语言是为普通数据库用户（没有超级用户特权）设计的并且允许他们安全地创建函数和过程。由于 PL 函数是在数据库内部执行的，TRUSTED标志只应被给予不允许访问数据库服务器内部或文件系统的语言。语言 PL/pgSQL、 PL/Tcl以及 PL/Perl被认为是可信的，语言 PL/TclU、 PL/PerlU以及 PL/PythonU是被设计用来提供无限制功能的并且不应该被标记为可信。

例 10.1展示了手工安装过程如何安装语言PL/Perl。

例 10.1. PL/Perl的手工安装

下列命令告诉数据库服务器在哪里寻找用于PL/Perl语言调用处理器函数的共享对象：

CREATE FUNCTION plperl\_call\_handler() RETURNS language\_handler AS

'$libdir/plperl' LANGUAGE C;

PL/Perl有一个内联处理器函数和一个验证器函数，因此我们也要声明它们：

CREATE FUNCTION plperl\_inline\_handler(internal) RETURNS void AS

'$libdir/plperl' LANGUAGE C;

CREATE FUNCTION plperl\_validator(oid) RETURNS void AS

'$libdir/plperl' LANGUAGE C STRICT;

命令

CREATE TRUSTED LANGUAGE plperl

HANDLER plperl\_call\_handler

INLINE plperl\_inline\_handler

VALIDATOR plperl\_validator;

则定义了前面声明的函数会为语言属性为plperl的函数及过程所调用。

在一个默认的瀚高数据库安装中，用于PL/pgSQL语言的处理器会被编译并且安装到”library”目录，此外PL/pgSQL语言本身会被安装在所有的数据库中。如果配置了Tcl支持，用于PL/Tcl和PL/TclU的处理器会被编译并且安装到库目录中，但语言本身默认不会被安装在任何数据库中。同样地，PL/Perl和PL/PerlU处理器在配置了 Perl 支持时被编译和安装，并且PL/PythonU处理器在配置了 Python 支持时被安装，但是这些语言默认都不会被安装。