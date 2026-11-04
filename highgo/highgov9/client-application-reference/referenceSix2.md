---
title: "客户端应用"
book: "客户端应用参考手册"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/reference/referenceSix2.html"
tags:
  - highgo
  - highgo-v9
  - client-application-reference
---

## 客户端应用

## clusterdb

clusterdb — 聚簇一个瀚高数据库

**命令**

clusterdb \[connection-option...\] \[ --verbose | -v \] \[ --table | -t table \]... \[dbname\]

clusterdb \[connection-option...\] \[ --verbose | -v \] --all | -a

**描述**

clusterdb是一个工具，它用来对一个瀚高数据库中的表进行重新聚簇。它会寻找之前已经被聚簇过的表，并且再次在最后使用过的同一个索引上对它们重新聚簇。没有被聚簇过的表将不会被影响。

clusterdb是 SQL 命令CLUSTER的一个包装器。在通过这个工具和其他方法访问服务器来聚簇数据库之间没有实质性的区别。

**选项**

clusterdb接受下列命令行参数：

\-a

\--all

聚簇所有数据库。

\[-d\] dbname

\[--dbname=\]dbname

指定要被聚簇的数据库名称。如果这个参数没有被指定并且-a（或--all）没有被使用，数据库名将从环境变量PGDATABASE中读出。如果该环境变量也没有被设置，指定给该连接的用户名将被用作数据库名。

\-e

\--echo

回显clusterdb生成并发送给服务器的命令。

\-q

\--quiet

不显示进度消息。

\-t table

\--table=table

只聚簇table。可以通过写多个-t开关来聚簇多个表。

\-v

\--verbose

在处理期间打印详细信息。

\-V

\--version

打印clusterdb版本并退出。

\-?

\--help

显示关于clusterdb命令行参数的帮助并退出。

clusterdb也接受下列命令行参数用于连接参数：

\-h host

\--host=host

指定运行服务所在机器的主机名。如果该值以一个斜线开始，它被用作 Unix 域套接字的目录。

\-p port

\--port=port

指定服务正在监听连接的 TCP 端口或本地 Unix 域套接字文件扩展。

\-U username

\--username=username

要作为哪个用户连接。

\--maintenance-db=dbname

指定要连接到来发现哪些其他数据库应该被聚簇的数据库名。如果没有指定，将使用highgo数据库。而如果它也不存在，将使用template1。

> **环境**

PGDATABASE

PGHOST

PGPORT

PGUSER

默认连接参数

PG\_COLOR

规定在诊断消息中是否使用颜色。可选的值为always、 auto、never。和其他数据库工具相似，这个工具也使用libpq（见开发手册）支持的环境变量。

**诊断**

在有困难时，可以在CLUSTER和psql中找潜在问题和错误消息的信息。数据库服务必须运行在目标主机上。同样，任何libpq前端库使用的默认连接设置和环境变量都将适用于此。

**示例**

要聚簇数据库test：

$ clusterdb test

要聚簇在数据库xyzzy中的一个表foo：

$ clusterdb --table foo xyzzy

**参见**

SQL命令cluster

## createdb

createdb — 创建一个新的瀚高数据库

**命令**

createdb \[connection-option...\] \[option...\] \[dbname \[description\]\]

**描述**

createdb创建一个新的瀚高数据库。

通常，执行这个命令的数据库用户将成为新数据库的所有者。但是，如果执行用户具有合适的权限，可以通过-O选项指定一个不同的所有者。

createdb是SQL命令CREATE DATABASE的一个包装器。在通过这个工具和其他方法访问服务来创建数据库之间没有实质性的区别。

**选项**

createdb接受下列命令行参数：

dbname

指定要被创建的数据库名。该名称必须在这个集簇中所有数据库中唯一。默认是创建一个与当前系统用户同名的数据库。

description

指定与新创建的数据库相关联的一段注释。

\-D tablespace

\--tablespace=tablespace

指定该数据库的默认表空间（这个名称被当做一个双引号引用的标识符处理）。

\-e

\--echo

回显createdb生成并发送到服务的命令。

\-E encoding

\--encoding=encoding

指定要在这个数据库中使用的字符编码模式。

\-l locale

\--locale=locale

指定要在这个数据库中使用的区域。这等效于同时指定--lc-collate和--lc-ctype。

\--lc-collate=locale

指定要在这个数据库中使用的 LC\_COLLATE 设置。

\--lc-ctype=locale

指定要在这个数据库中使用的 LC\_CTYPE 设置。

\-O owner

\--owner=owner

指定拥有这个新数据库的数据库用户（这个名称被当做一个双引号引用的标识符处理）。

\-T template

\--template=template

指定用于创建这个数据库的模板数据库（这个名称被当做一个双引号引用的标识符处理）。

\-V

\--version

打印createdb版本并退出。

\-?

\--help

显示关于createdb命令行参数的帮助并退出。

选项-D、-l、-E、 -O和 -T对应于底层 SQL 命令CREATE DATABASE的选项，关于这些选项的信息可见该命令的内容。

createdb也接受下列命令行参数用于连接参数：

\-h host

\--host=host

指定运行服务的机器的主机名。如果该值以一个斜线开始，它被用作 Unix 域套接字的目录。

\-p port

\--port=port

指定服务正在监听连接的 TCP 端口或本地 Unix 域套接字文件扩展。

\-U username

\--username=username

要作为哪个用户连接。

\--maintenance-db=dbname

指定要连接到来发现哪些其他数据库应该被聚簇的数据库名。如果没有指定，将使用highgo数据库。而如果它也不存在（或者如果它就是要创建新数据库的名称），将使用template1。

**环境**

PGDATABASE

如果被设置，就是要创建的数据库名，除非在命令行中覆盖。

PGHOST

PGPORT

PGUSER

默认连接参数。如果没有在命令行或PGDATABASE指定要创建的数据库名，PGUSER也决定要创建的数据库名。

PG\_COLOR

规定在诊断消息中是否使用颜色。可能的值为 always， auto，never。

和大部分其他数据库工具相似，这个工具也使用libpq（见开发手册）支持的环境变量。

**诊断**

在有困难时，可以在CREATE DATABASE和psql中找潜在问题和错误消息的信息。数据库服务必须运行在目标主机上。同样，任何libpq前端库使用的默认连接设置和环境变量都将适用于此。

**示例**

要使用默认数据库服务创建数据库demo：

$ createdb demo

要在主机eden、端口 5000 上使用template0 模板数据库创建数据库demo，这里是命令行命令和底层SQL命令：

$ createdb -p 5000 -h eden -T template0 -e demo

CREATE DATABASE demo TEMPLATE template0;

**参见**

dropdb 、SQL命令CREATE DATABASE

## createuser

createuser — 定义一个新的数据库用户账户

**命令**

createuser \[connection-option...\] \[option...\] \[username\]

**描述**

createuser创建一个新的瀚高数据库用户（或者更准确些，是一个角色）。

createuser是SQL命令CREATE ROLE的一个包装器。在通过这个工具和其他方法访问服务器来创建用户之间没有实质性的区别。

**选项**

createuser接受下列命令行参数：

> username

指定要被创建的数据库用户的名称。这个名称必须与这个数据库中所有现存角色不同。

\-c number

\--connection-limit=number

为该新用户设置一个最大连接数。默认值为不设任何限制。

\-d

\--createdb

新用户将被允许创建数据库。

\-D

\--no-createdb

新用户将不被允许创建数据库。这是默认值。

\-e

\--echo

回显createuser生成并发送给服务器的命令。

\-E

\--encrypted

此选项已过时，但为了实现向后兼容仍然接受。

\-g role

\--role=role

指定一个角色，这个角色将立即加入其中成为其成员。如果要把这个角色加入到多个角色中作为成员， 可以写多个-g开关。

\-i

\--inherit

新角色将自动继承把它作为成员的角色的特权。这是默认值。

\-I

\--no-inherit

新角色将不会自动继承把它作为成员的角色的特权。

\--interactive

如果在命令行没有指定用户名，提示要求用户名，并且在命令行没有指定选项 -d/-D、-r/-R、 -s/-S时也提示。

\-l

\--login

新用户将被允许登入（即，该用户名能被用作初始会话用户标识符）。这是默认值。

\-L

\--no-login

新用户将不被允许登入（一个没有登录特权的角色仍然可以作为管理数据库权限的方式而存在）。

\-P

\--pwprompt

如果给定，createuser将发出一个提示要求新用户的口令。如果你没有计划使用口令认证，这就不是必须的。

\-r

\--createrole

新用户将被允许创建新的角色（即，这个用户将具有CREATEROLE特权）。

\-R

\--no-createrole

新用户将不被允许创建新角色。这是默认值。

\-s

\--superuser

新用户将成为一个超级用户。

\-S

\--no-superuser

新用户将不会成为一个超级用户。这是默认值。

\-V

\--version

打印createuser版本并退出。

\--replication

新用户将具有REPLICATION特权，这在CREATE ROLE的文档中有更完整的描述。

\--no-replication

新用户将不具有REPLICATION特权，这在CREATE ROLE的文档中有更完整的描述。

\-?

\--help

显示有关createuser命令行参数的帮助并退出。

createuser也接受下列命令行参数作为连接参数：

\-h host

\--host=host

指定运行服务器的机器的主机名。如果该值以一个斜线开始，它被用作 Unix 域套接字的目录。

\-p port

\--port=port

指定服务器正在监听连接的 TCP 端口或本地 Unix 域套接字文件扩展。

\-U username

\--username=username

要作为哪个用户连接（不是要创建的用户名）。

**环境**

PGHOST

PGPORT

PGUSER

默认连接参数

PG\_COLOR

规定在诊断消息中是否使用颜色。可能的值为 always， auto，never。

和大部分其他数据库工具相似，这个工具也使用libpq（见开发手册）支持的环境变量。

**诊断**

在有困难时，可以在CREATE ROLE和psql中找潜在问题和错误消息的讨论。数据库服务器必须运行在目标主机上。同样，任何libpq前端库使用的默认连接设置和环境变量都将适用于此。

**示例**

要在默认数据库服务器上创建一个用户joe：

$ createuser joe

要在默认数据库服务器上创建一个用户joe并提示要求一些额外属性：

$ createuser --interactive joe

Shall the new role be a superuser? (y/n) n

Shall the new role be allowed to create databases? (y/n) n

Shall the new role be allowed to create more new roles? (y/n) n

要使用在主机eden、端口 5000 上的服务器创建同一个用户joe，并带有显式指定的属性，看看下面的命令：

$ createuser -h eden -p 5000 -S -D -R -e joe

CREATE ROLE joe NOSUPERUSER NOCREATEDB NOCREATEROLE INHERIT LOGIN;

要创建用户joe为一个超级用户并且立刻分配一个口令：

$ createuser -P -s -e joe

Enter password for new role: xyzzy

Enter it again: xyzzy

CREATE ROLE joe PASSWORD 'md5b5f5ba1a423792b526f799ae4eb3d59e' SUPERUSER

CREATEDB CREATEROLE INHERIT LOGIN;

在上面的例子中，在录入新口令时新口令并没有真正地被回显，但是为了清晰，我们特意把它列了出来。如你所见，该口令在被发送给客户端之前会被加密。

**参见**

dropuser, SQL命令CREATE ROLE

## dropdb

dropdb — 移除一个瀚高数据库

**命令**

dropdb \[connection-option...\] \[option...\] dbname

**描述**

dropdb毁掉一个现有的数据库。执行这个命令的用户必须是一个数据库超级用户或该数据库的拥有者。

dropdb是SQL命令DROP DATABASE的一个包装器。在通过这个工具和其他方法访问服务器来删除数据库之间没有实质性的区别。

**选项**

dropdb接受下列命令行参数：

> dbname

指定要被移除的数据库的名字。

\-e

> \--echo

回显dropdb生成并发送给服务器的命令。

\-i

> \--interactive

在做任何破坏性的工作之前发出一个验证提示。

\-V

> \--version

打印dropdb版本并退出。

> \--if-exists

如果数据库不存在也不抛出一个错误。在这种情况下会发出一个提醒。

> \-?
> 
> \--help

显示有关dropdb命令行参数的帮助并退出。

dropdb也接受下列命令行参数作为连接参数：

> \-h host
> 
> \--host=host

指定运行服务器的机器的主机名。如果该值以一个斜线开始，它被用作 Unix 域套接字的目录。

\-p port

\--port=port

指定服务器正在监听连接的 TCP 端口或本地 Unix 域套接字文件扩展。

> \-U username
> 
> \--username=username

要作为哪个用户连接。

\-w

\--no-password

从不发出一个口令提示。如果服务器要求口令认证并且没有其他方式提供口令（例如一个.pgpass文件），那儿连接尝试将失败。这个选项对于批处理任务和脚本有用，因为在其中没有一个用户来输入口令。

\-W

\--password

强制dropdb在连接到一个数据库之前提示要求一个口令。

这个选项不是必不可少的，因为如果服务器要求口令认证，dropdb将自动提示要求一个口令。但是，dropdb将浪费一次连接尝试来发现服务器想要一个口令。在某些情况下值得用-W来避免额外的连接尝试。

\--maintenance-db=dbname

指定要连接到来发现哪些其他数据库应该被删除的数据库名。如果没有指定，将使用highgo数据库。而如果它也不存在，将使用template1。

**环境**

> PGHOST
> 
> PGPORT
> 
> PGUSER

默认连接参数

> PG\_COLOR

规定在诊断消息中是否使用颜色。可能的值为always、 auto、never。

和大部分其他数据库工具相似，这个工具也使用libpq（见开发手册）支持的环境变量。

**诊断**

在有困难时，可以在DROP DATABASE和psql中找潜在问题和错误消息的讨论。数据库服务器必须运行在目标主机上。同样，任何libpq前端库使用的默认连接设置和环境变量都将适用于此。

**示例**

要在默认数据库服务器上毁掉数据库demo：

$ dropdb demo

要使用在主机eden、端口 5000 上的服务器中毁掉数据库demo，并带有验证和回显，看看下面的命令：

$ dropdb -p 5000 -h eden -i -e demo

Database "demo" will be permanently deleted.

Are you sure? (y/n) y

DROP DATABASE demo;

**参见**

createdb, SQL命令DROP DATABASE

## dropuser

dropuser — 移除一个瀚高数据库用户账户

**命令**

dropuser \[connection-option...\] \[option...\] \[username\]

**描述**

dropuser移除一个已有的瀚高数据库用户。只有超级用户以及具有CREATEROLE特权的用户能够移除用户（要移除一个超级用户，你必须自己是一个超级用户）。

dropuser是SQL命令DROP ROLE的一个包装器。在通过这个工具和其他方法访问服务器来删除用户之间没有实质性的区别。

**选项**

dropuser接受下列命令行参数：

username

指定要移除的数据库用户的名字。如果没有在命令行指定并且使用了-i/-- interactive选项，你将被提醒要求一个用户名。

\-e

\--echo

回显dropuser生成并发送给服务器的命令。

\-i

\--interactive

在实际移除该用户之前提示要求确认，并且在没有在命令行指定用户名提示要求一个用户名。

> \-V
> 
> \--version

打印dropuser版本并退出。

\--if-exists

如果用户不存在时不要抛出一个错误。在这种情况下将发出一个提示。

\-?

\--help

显示有关dropuser命令行参数的帮助并退出。

dropuser也接受下列命令行参数作为连接参数：

\-h host

\--host=host

指定运行服务器的机器的主机名。如果该值以一个斜线开始，它被用作 Unix 域套接字的目录。

> \-p port

\--port=port

指定服务器正在监听连接的 TCP 端口或本地 Unix 域套接字文件扩展。

\-U username

\--username=username

要作为哪个用户连接（不是要移除的用户名）。

\-w

\--no-password

从不发出一个口令提示。如果服务器要求口令认证并且没有其他方式提供口令（例如一个.pgpass文件），那儿连接尝试将失败。这个选项对于批处理任务和脚本有用，因为在其中没有一个用户来输入口令。

\-W

\--password

强制dropuser在连接到一个数据库之前提示要求一个口令。

这个选项不是必不可少的，因为如果服务器要求口令认证，dropuser将自动提示要求一个口令。但是，dropuser将浪费一次连接尝试来发现服务器想要一个口令。在某些情况下值得用-W来避免额外的连接尝试。

**环境**

> PGHOST
> 
> PGPORT
> 
> PGUSER

默认连接参数

> PG\_COLOR

规定在诊断消息中是否使用颜色。可能的值为always、 auto、never。

和大部分其他数据库工具相似，这个工具也使用libpq（见开发手册）支持的环境变量。

**诊断**

在有困难时，可以在DROP ROLE和psql中找潜在问题和错误消息的讨论。数据库服务器必须运行在目标主机上。同样，任何libpq前端库使用的默认连接设置和环境变量都将适用于此。

**示例**

要从默认数据库服务器移除用户joe：

$ dropuser joe

要使用在主机eden、端口 5000 上的服务器移除用户joe，并带有验证和回显，可使用下面的命令：

$ dropuser -p 5000 -h eden -i -e joe

Role "joe" will be permanently removed.

Are you sure? (y/n) y

DROP ROLE joe;

**参见**

createuser, SQL命令DROP ROLE

## pg\_amcheck

pg\_amcheck — 在一个或多个瀚高数据库中检查损坏

**命令：**

pg\_amcheck \[option...\] \[dbname\]

**描述：**

pg\_amcheck支持对一个或多个数据库运行 [amcheck](http://postgres.cn/docs/14/amcheck.html) 的损坏检查函数，并提供选项来选择要检查的模式、表和索引、要执行的检查类型以及是否并行执行检查，如果是，按并行数建立连接并使用。

当前仅支持表关系和btree索引。其他关系类型将自动跳过。

如果指定了dbname，则它应该是要检查的单个数据库的名称，并且不应该存在其他数据库选择选项。否则，如果存在任何数据库选择选项，将检查所有匹配的数据库。如果不存在此类选项，将选中默认数据库。数据库选择选项包括--all，--database和--exclude-database。它们还包括--relation，--exclude-relation， --table，--exclude-table，--index，和--exclude-index，但仅当这些选项与三段式模式一起使用时（例如，mydb\*.myschema\*.myrel\*）。最后，它们包括--schema和--exclude-schema 当这些选项与两段式模式一起使用时（例如mydb\*.myschema\*）。

dbname也可以是一个 [连接字符串](http://postgres.cn/docs/14/libpq-connect.html#LIBPQ-CONNSTRING) 。

**选项：**

以下命令行选项控制要检查的内容：

\-a

\--all

检查所有数据库，但通过--exclude-database排除的数据库除外。

\-d pattern

\--database=pattern

检查与指定的 [pattern](http://postgres.cn/docs/14/app-psql.html#APP-PSQL-PATTERNS) 匹配的数据库，但--exclude-database排除的数据库除外。可以多次指定此选项。

\-D pattern

\--exclude-database=pattern

排除与给定的 [pattern](http://postgres.cn/docs/14/app-psql.html#APP-PSQL-PATTERNS) 匹配的数据库。可以多次指定此选项。

\-i pattern

\--index=pattern

检查与指定的 [pattern](http://postgres.cn/docs/14/app-psql.html#APP-PSQL-PATTERNS) 匹配的索引，除非它们被排除在外。可以多次指定此选项。

这类似于--relation选项，只是它只适用于索引，而不适用于表。

\-I pattern

\--exclude-index=pattern

排除与指定的 [pattern](http://postgres.cn/docs/14/app-psql.html#APP-PSQL-PATTERNS) 匹配的索引。可以多次指定此选项。

这类似于--exclude-relation选项，只是它只适用于索引，而不适用于表。

\-r pattern

\--relation=pattern

检查与指定的 [pattern](http://postgres.cn/docs/14/app-psql.html#APP-PSQL-PATTERNS) 匹配的关系，除非它们被排除在外。可以多次指定此选项。

模式可能是非限定的，例如myrel\*，或者它们可能是模式限定的，如myschema\*.myrel\*或数据库限定和模式限定，例如mydb\*.myscheam\*.myrel\*。数据库限定模式将向要检查的数据库列表中添加匹配的数据库。

\-R pattern

\--exclude-relation=pattern

排除与指定的 [pattern](http://postgres.cn/docs/14/app-psql.html#APP-PSQL-PATTERNS) 匹配的关系。可以多次指定此选项。

As with --relation, the [pattern](http://postgres.cn/docs/14/app-psql.html#APP-PSQL-PATTERNS) may be unqualified, schema-qualified, or database- and schema-qualified. 与--relation一样， [pattern](http://postgres.cn/docs/14/app-psql.html#APP-PSQL-PATTERNS) 可以是非限定的、模式限定的或数据库和模式限定的。

\-s pattern

\--schema=pattern

检查模式中与指定的 [pattern](http://postgres.cn/docs/14/app-psql.html#APP-PSQL-PATTERNS) 匹配的表和索引，除非另有排除。可以多次指定此选项。

要仅选择与特定模式匹配的模式中的表，请考虑使用类似--table=SCHEMAPAT.\* --no-dependent-indexes。要仅选择索引，请考虑使用类似--index=SCHEMAPAT.\*的方法。

模式模式可以是数据库限定的。例如，你可以编写--schema=mydb\*.myschema\*在数据库中选择匹配 mydb\*的模式。

> \-S pattern
> 
> \--exclude-schema=pattern

排除模式中与指定的 [pattern](http://postgres.cn/docs/14/app-psql.html#APP-PSQL-PATTERNS) 匹配的表和索引。可以多次指定此选项。

与--schema一样，模式可以是数据库限定的。

> \-t pattern
> 
> \--table=pattern

检查与指定的 [pattern](http://postgres.cn/docs/14/app-psql.html#APP-PSQL-PATTERNS) 匹配的表，除非它们被排除在外。可以多次指定此选项。

这类似于--relation选项，只是它只适用于表，而不适用于索引。

\-T pattern

\--exclude-table=pattern

排除与指定的 [pattern](http://postgres.cn/docs/14/app-psql.html#APP-PSQL-PATTERNS) 匹配的表。可以多次指定此选项。

这类似于--exclude-relation选项，只是它只适用于表，而不适用于索引。

\--no-dependent-indexes

默认情况下，如果选中了一个表，则该表的任何btree索引也将被选中，即使它们没有被诸如--index或--relation之类的选项显式选择。此选项将抑制该行为。

\--no-dependent-toast

默认情况下，如果选中了一个表，则也将检查它的toast表（如果有），即使它没有通过诸如--table或--relation之类的选项显式选择。此选项将抑制该行为。

\--no-strict-names

默认情况下，如果--database，--table，--index，或--relation的参数不匹配任何对象，则这是一个致命错误。此选项将该错误降级为警告。

以下命令行选项用于控制表的检查：

\--exclude-toast-pointers

默认情况下，每当在表中遇到toast指针时，都会执行查找以确保它引用toast表中明显有效的条目。这些检查可能非常慢，可以使用此选项跳过这些检查。

\--on-error-stop

在发现损坏的表的第一页上报告所有损坏后，停止处理该表关系，并转到下一个表或索引。

请注意，索引检查总是在第一个损坏页之后停止。此选项仅与表关系相关。

\--skip=option

如果给定all-frozen，表损坏检查将跳过所有表中标记为全部冻结的页面。

如果给定了all-visible，则表损坏检查将跳过所有表中标记为所有可见的页面。

默认情况下，不跳过任何页面。这可以指定为none，但由于这是默认值，因此无需提及。

\--startblock=block

从指定的块号开始检查。如果正在检查的表关系的块数少于此数，则会发生错误。此选项不适用于索引，可能仅在检查单个表关系时有用。请参阅--endblock了解更多注意事项。

\--endblock=block

在指定的块号结束检查。如果正在检查的表关系的块数少于此数，则会发生错误。此选项不适用于索引，可能仅在检查单个表关系时有用。如果同时选中常规表和toast表，则此选项将同时适用于这两个表，但在验证toast指针时，仍然可以访问编号更高的toast块，除非使用--exclude-toast-pointers抑制。

以下命令行选项用来控制B树索引的检查：

\--heapallindexed

对于每个选中的索引，使用 [amcheck](http://postgres.cn/docs/14/amcheck.html) 's heapallindexed选项验证索引中是否存在作为索引元组的所有堆元组。

\--parent-check

对于检查的每个btree索引，使用 [amcheck](http://postgres.cn/docs/14/amcheck.html) 的bt\_index\_parent\_check函数，该函数在索引检查期间对父/子关系执行其他检查。

默认情况是使用amcheck的bt\_index\_check函数，但请注意，使用--rootdescend选项会隐式选择bt\_index\_parent\_check。

\--rootdescend

对于每个选中的索引，通过使用 [amcheck](http://postgres.cn/docs/14/amcheck.html) 's rootdescend选项从根页面对每个元组执行新搜索，在叶级重新查找元组。

使用此选项也会隐式选择--parent-check选项。

这种形式的验证最初是为了帮助开发btree索引功能而编写的。它在帮助检测实践中发生的损坏类型方面可能用处有限，甚至毫无用处。它还可能导致损坏检查花费相当长的时间，并消耗服务器上相当多的资源。

| **警告：** |
| --- |
| 当指定--parent-check选项或--rootdescend选项时，对B树索引执行的额外检查需要相对强的关系级锁。这些检查是唯一会阻止INSERT，UPDATE，和DELETE命令并发数据修改的检查。 |

以下命令行选项用来控制与服务器的连接：

> \-h hostname  
> \--host=hostname

指定运行服务器的计算机的主机名。如果该值以斜杠开头，它将用作Unix域套接字的目录。

> \-p port  
> \--port=port

指定服务器正在侦听连接的TCP端口或本地Unix域套接字文件扩展名。

> \-U  
> \--username=username

连接的用户名。

> \-w  
> \--no-password

永远不要发出密码提示。如果服务器需要密码身份验证，并且密码无法通过其他方式（如.pgpass文件，连接尝试将失败。在没有用户输入密码的批处理作业和脚本中，此选项非常有用。

> \-W  
> \--password

在连接到数据库之前，强制pg\_amcheck提示输入密码。

此选项从来都不是必需的，因为如果服务器要求密码身份验证，pg\_amcheck将自动提示输入密码。但是，pg\_amcheck将浪费一次连接尝试，以发现服务器需要密码。在某些情况下，键入-W以避免额外的连接尝试是值得的。

\--maintenance-db=dbname

指定用于发现要检查的数据库列表的数据库或 [连接字符串](http://postgres.cn/docs/14/libpq-connect.html#LIBPQ-CONNSTRING) 。如果既不使用--all也不使用任何包含数据库模式的选项，则不需要这种连接，并且该选项不起任何作用。否则，连接到正在检查的数据库时，也将使用此选项值中包含的数据库名称以外的任何连接字符串参数。如果省略此选项，则默认值为postgres，或如果失败，则为template1。

其它允许的选项：

> \-e  
> \--echo

回显发送到服务器的所有SQL。

> \-j num  
> \--jobs=num

使用num个到服务器的并发连接，或每个要检查的对象使用一个连接，以较小者为准。

默认情况是使用单个连接。

\-P

\--progress

显示进度信息。进度信息包括已完成检查的关系数以及这些关系的总大小。它还包括最终要检查的关系的总数，以及这些关系的估计大小。

\-v

\--verbose

打印更多消息。特别是，这将为每个正在检查的关系打印一条消息，并将增加服务器错误的详细程度。

\-V

\--version

打印pg\_amcheck版本并退出。

\--install-missing

\--install-missing=schema

安装检查数据库所需的任何缺少的扩展。如果尚未安装，每个扩展的对象将安装到给定的schema中，或者如果未指定则安装到pg\_catalog模式中。

目前，唯一需要的扩展是 [amcheck](http://postgres.cn/docs/14/amcheck.html) 。

\-?

\--help

显示有关pg\_amcheck命令行参数的帮助，然后退出。

## ecpg

ecpg — 嵌入式 SQL C 预处理器

**命令**

ecpg \[option...\] file...

**描述**

ecpg是用于 C 程序的嵌入式 SQL 预处理器。它通过将 SQL 调用替换为特殊函数调用把带有嵌入式 SQL 语句的 C 程序转换为普通 C 代码。输出文件可以被任何 C 编译器工具链处理。

ecpg将把命令行中给出的每一个输入文件转换为相应的 C 输出文件。输入文件更适宜于使用扩展名.pgc。该扩展名将被替换为.c来决定输出文件名。输出文件名也可以使用-o选项覆盖。

这个参考页没有描述嵌入式 SQL 语言。

**选项**

ecpg接受下列命令行参数：

> \-c

自动从 SQL 代码生成确定的 C 代码。当前，这对EXEC SQL TYPE起效。

> \-C mode

设置一个兼容性模式。mode可以是INFORMIX，INFORMIX\_SE或ORACLE。

> \-D symbol

定义一个 C 预处理器符号。

> \-i

分析系统也包括文件。

> \-I directory

指定一个额外的包括路径，用来寻找通过EXEC SQL INCLUDE包括的文件。默认值是.（当前目录）、$HGDB\_HOME/include、在编译时定义的包括目录（默认：$HGDB\_HOME/include）。

> \-o filename

指定ecpg应该将它的所有输出写到给定的filename。

> \-r option

选择运行时行为。option可以是下列之一：

> no\_indicator

不使用指示器而使用特殊值来表示空值。历史上曾有数据库使用这种方法。

> prepare

在使用所有语句之前准备它们。libecpg 将保持一个预备语句的缓冲并当语句再被执行时重用该语句。如果缓冲满了，libecpg 将释放最少使用的语句。

> questionmarks

为兼容性原因允许使用问号作为占位符。在很久以前这被用作默认值。

> \-t

打开事务的自动提交。在这种模式下，每一个 SQL 命令会被自动提交，除非它位于一个显式事务块中。在默认模式中，命令只有当EXEC SQL COMMIT被发出时才被提交。

> \-v

打印额外信息，包括版本和”包括”路径。

> \--version

打印ecpg版本并退出。

> \-?

\--help

显示关于ecpg命令行参数的帮助并退出。

**注释**

在编译预处理好的 C 代码文件时，编译器需要能够找到数据库包括目录中的ECPG头文件。因此，在调用编译器时，你可能必须使用-I选项（例如，-I $HGDB\_HOME/include）。

使用带有嵌入式 SQL 的 C 代码的程序必须被链接到libecpg库，例如使用链接器选项-L $HGDB\_HOME/lib -lecpg。

适合于安装的这些目录的值可以使用pg\_config找到。

**示例**

如果你有一个名为prog1.pgc的嵌入式 SQL C 源文件，你可以使用下列命令序列创建一个可执行程序：

ecpg prog1.pgc

cc -I /home/highgo/highgo/database/9.0/include -c prog1.c

cc -o prog1 prog1.o -L /home/highgo/highgo/database/9.0/lib -lecpg

## pg\_basebackup

pg\_basebackup — 获得一个数据库集簇的一个基础备份

**命令**

pg\_basebackup \[option...\]

**描述**

pg\_basebackup被用于获得一个正在运行的数据库集簇的基础备份。获得这些备份不会影响连接到该数据库的其他客户端，并且可以被用于时间点恢复以及用作一个日志传送或流复制后备服务器的开始点。

pg\_basebackup建立数据库集簇文件的一份二进制副本，同时保证系统进入和退出备份模式。备份总是从整个数据库集簇获得，不可能备份单个数据库或数据库对象。关于个体数据库备份，必须使用一个像pg\_dump的工具。

备份通过一个常规数据库连接，并且使用复制协议。该连接必须由一个超级用户或者一个具有REPLICATION权限的用户建立，并且pg\_hba.conf必须显式地允许该复制连接。该服务器还必须被配置，使max\_wal\_senders设置得足够高以留出至少一个会话用于备份以及一个用于WAL流（如果使用流）。

在同一时间可以有多个pg\_basebackup运行，但是从性能的角度来说最好只做一个备份并且复制结果。

pg\_basebackup不仅能从主控机也能从后备机创建一个基础备份。要从后备机获得一个备份，设置后备机让它能接受复制连接（也就是，设置max\_wal\_senders和hot\_standby，并且配置基于主机的认证）。你将也需要在主控机上启用full\_page\_writes。

注意在来自后备机的在线备份中有一些限制：

• 不会在被备份的数据库集簇中创建备份历史文件。

• 如果正在使用-X none，不保证备份所需的所有 WAL 文件在备份结束时被归档。

• 如果在在线备份期间后备机被提升为主控机，备份会失败。

• 备份所需的所有 WAL 记录必须包含足够的全页写，这要求你在主控机上启用full\_page\_writes并且不使用一个类似pg\_compresslog的工具以archive\_command从WAL 文件中移除全页写。

**选项**

下列命令行选项控制输出的位置和格式。

> \-D directory

\--pgdata=directory

将输出写到哪个目录。如果必要，pg\_basebackup将创建该目录及任何父目录。该目录可能已经存在，但是如果该目录已经存在并且非空就是一个错误。

当备份处于 tar 模式中并且目录被指定为-（破折号）时，tar 文件将被写到stdout。

\-F format

> \--format=format

为输出选择格式。format可以是下列之一：

> p
> 
> plain

把输出写成平面文件，使用和当前数据目录和表空间相同的布局。当集簇没有额外表空间时，整个数据库将被放在目标目录中。如果集簇包含额外的表空间，主数据目录将被放置在目标目录中，但是所有其他表空间将被放在它们位于服务器上的相同的绝对路径中。

这是默认格式。

t

> tar

将输出写成目标目录中的 tar 文件。主数据目录将被写入到一个名为base.tar的文件中，并且其他表空间将被以其 OID 命名。

如果值-（破折号）被指定为目标目录，tar 内容将被写到标准输出，适合于管道输出到其他程序，例如gzip。只有当集簇没有额外表空间并且没有使用WAL流时这才是可能的。

\-r rate

\--max-rate=rate

从该服务器传输数据的最大传输率。值的单位是千字节每秒。加上一个后缀M表示兆字节每秒。也接受后缀k，但是没有效果。合法的值在 32 千字节每秒到 1024 兆字节每秒之间。

其目标是限制在运行服务器上的pg\_basebackup产生的影响。

这个选项总是会影响数据目录的传输。如果收集方法是fetch时，只有 WAL 文件受到影响。

> \-R
> 
> \--write-recovery-conf

在输出目录中（或者当使用 tar 格式时再基础归档文件中）建立 standby.signal 并附加连接设置到postgresql.auto.conf 来简化设置一个后备服务器。postgresql.auto.conf文件将记录连接设置（如果有）以及pg\_basebackup所使用的复制槽，这样流复制后面就会使用相同的设置。

> \-T olddir=newdir
> 
> \--tablespace-mapping=olddir=newdir

在备份期间将目录olddir中的表空间重定位到newdir中。为使之有效，olddir必须正好匹配表空间所在的路径（但如果备份中没有包含olddir中的表空间也不是错误）。olddir和newdir必须是绝对路径。如果一个路径凑巧包含了一个=符号，可用反斜线对它转义。对于多个表空间可以多次使用这个选项。例子见下文。

如果以这种方法重定位一个表空间，主数据目录中的符号链接会被更新成指向新位置。因此新数据目录已经可以被一个所有表空间位于更新后位置的新服务器实例使用。

\--waldir=waldir

指定用于预写式日志目录的位置。waldir必须是绝对路径。只有当备份是平面文件模式时才能指定事务日志目录。

\-X method

\--wal-method=method

在备份中包括所需的预写式日志文件（WAL文件）。这包括所有在备份期间产生的预写式日志。除非指定了方法none，可以直接在提取出的目录中启动postmaster而无需参考日志归档，所以这样得到的是一种完整的独立备份。

支持下列收集预写式日志的方法：

> n
> 
> none

不要在备份中包括预写式日志。

> f
> 
> fetch

在备份末尾收集预写式日志文件。因此，有必要把wal\_keep\_segments参数设置得足够高，这样在备份末尾之前日志不会被移除。如果在要传输日志时它已经被轮转，备份将失败并且是不可用的。

如果使用tar格式，预写式日志文件将被写入到base.tar文件。

> s
> 
> stream

在备份被创建时流传送预写式日志。这将开启一个到服务器的第二连接并且在运行备份时并行开始流传输预写式日志。因此，它将使用最多两个由max\_wal\_senders参数配置的连接。只要客户端能保持接收预写式日志，使用这种模式不需要在主控机上保存额外的预写式日志。

如果使用tar格式，预写式日志文件被写入到一个单独的名为pg\_wal.tar的文件（如果服务器的版本超过10，该文件将被命名为pg\_wal.tar）。

这个值是默认值。

> \-z

\--gzip

启用对 tar 文件输出的 gzip 压缩，使用默认的压缩级别。只有使用 tar 格式时压缩才可用，并且会在所有tar文件名后面自动加上后缀.gz。

> \-Z level

\--compress=level

启用对 tar 文件输出的 gzip 压缩，并且制定压缩机别（0 到 9，0 是不压缩，9 是最佳压缩）。只有使用 tar 格式时压缩才可用，并且会在所有tar文件名后面自动加上后缀.gz。

下列命令行选项控制备份的生成和程序的运行。

> \-c fast|spread

\--checkpoint=fast|spread

将检查点模式设置为 fast（立刻）或 spread（默认）。

> \-C

\--create-slot

这个选项会导致在开始备份前创建一个由--slot选项指定名称的复制槽。如果槽已经存在则会发生错误。

\-l label

> \--label=label

为备份设置标签。如果没有指定，将使用一个默认值”pg\_basebackup base backup”。

> \-n

\--no-clean

默认情况下，当pg\_basebackup因为一个错误而中止时，它会把它意识到无法完成该工作之前已经创建的目录（例如数据目录和预写式日志目录）都移除。这个选项可以禁止这种清洗，因此可以用于调试。

注意不管哪一种方式都不会清除表空间目录。

> \-N

\--no-sync

默认情况下，pg\_basebackup将等待所有文件被安全地写到磁盘上。这个选项导致pg\_basebackup不做这种等待就返回，这样会更快一些，但是也意味着后续发生的操作系统崩溃可能会使得这个基础备份损坏。通常这个选项对测试比较有用，在创建生产安装时不应该使用。

> \-P

\--progress

启用进度报告。启用这个选项将在备份期间发表一个大致的进度报告。由于数据库可能在备份期间改变，这仅仅是一种近似并且可能不会刚好在100%结束。特别地，当 WAL 日志被包括在备份中时，总数据量无法预先估计，并且在这种情况中估计的目标尺寸会在它经过不带 WAL 的总估计后增加。

当这个选项被启用时，备份开始时会列举整个数据库的尺寸，并且接着回头开始发送实际的内容。这可能使备份需要多花一点点时间，并且它在发送第一个数据之前花费的时间更长。

> \-S slotname

\--slot=slotname

这个选项仅能与-X stream一起使用。它导致WAL流使用指定的复制槽。如果该基础备份的目的是被用作一台使用复制槽的流复制后备，则它应该使用与primary\_slot\_name中相同的复制槽名称。通过这种方式，可以确保服务器不会移除位于该基础备份结束与流复制开始之间产生的任何所需的WAL数据。

指定的复制槽必须已经存在，除非同时使用了选项-C。

如果这个选项没有被指定并且服务器支持临时复制槽（版本10以后），则会自动使用一个临时复制槽来进行WAL流。

> \-v

\--verbose

启用冗长模式。将在启动和关闭期间输出一些额外步骤，并且如果进度报告也被启用，还会显示当前正在被处理的确切文件名。

> \--no-slot

如果服务器支持临时复制槽，这个选项防止备份期间创建临时复制槽。在使用日志流时，如果没有用选项-S指定槽名称，则默认会创建临时复制槽。

这个选项的主要目的是允许在服务器没有空闲复制槽可用时制作基础备份。使用复制槽几乎总是最好的方式，因为它能防止备份期间所需的WAL被删除。

\--no-verify-checksums

如果在取基础备份的服务器上启用了校验码验证，则禁用校验码验证。默认情况下，校验码会被验证并且校验码失败将会导致一种非零的退出状态。不过，基础备份在这种情况下将不会被移除，就好像使用了--no-clean选项一样。校验和验证失败也将报告在pg\_stat\_database视图中。

下列命令行选项控制数据库连接参数。

> \-d connstr

\--dbname=connstr

以一个连接字符串的形式指定用于连接到服务器的参数。

为了和其他客户端应用一致，该选项被称为--dbname。但是因为pg\_basebackup并不连接到集簇中的任何特定数据库，连接字符串中的数据库名将被忽略。

> \-h host

\--host=host

指定运行服务器的机器的主机名。如果该值以一个斜线开始，它被用作 Unix 域套接字的目录。默认值取自PGHOST环境变量（如果设置），否则会尝试一个 Unix 域套接字连接。

> \-p port

\--port=port

指定服务器正在监听连接的 TCP 端口或本地 Unix 域套接字文件扩展。默认用PGPORT环境变量中的值（如果设置），或者一个编译在程序中的默认值。

> \-s interval

\--status-interval=interval

指定发送回服务器的状态包之间的秒数。这允许我们更容易地监控服务器的进度。一个零值完全禁用这种周期性的状态更新，不过当服务器需要时还是会有一个更新会被发送来避免超时导致的断开连接。默认值是 10 秒。

> \-U username

\--username=username

要作为哪个用户连接。

> \-w

\--no-password

从不发出一个口令提示。如果服务器要求口令认证并且没有其他方式提供口令（例如一个.pgpass文件），那儿连接尝试将失败。这个选项对于批处理任务和脚本有用，因为在其中没有一个用户来输入口令。

> \-W

\--password

强制pg\_basebackup在连接到一个数据库之前提示要求一个口令。

这个选项不是必不可少的，因为如果服务器要求口令认证，pg\_basebackup将自动提示要求一个口令。但是，pg\_basebackup将浪费一次连接尝试来发现服务器想要一个口令。在某些情况下值得用-W来避免额外的连接尝试。

其他选项也可用：

> \-V

\--version

打印pg\_basebackup版本并退出。

> \-?

\--help

显示有关pg\_basebackup命令行参数的帮助并退出。

**环境**

和大部分其他数据库工具相似，这个工具也使用libpq（见开发手册）支持的环境变量。

环境变量PG\_COLOR规定在诊断消息中是否使用颜色。可能的值为always、auto、never。

**注释**

在备份的开始时，需要向从中拿去备份的服务器写一个检查点。尤其在没有使用选项-- checkpoint=fast时，这可能需要一点时间，在其间pg\_basebackup看起来处于闲置状态。

备份将包括数据目录和表空间中的所有文件，包括配置文件以及由第三方放在该目录中的任何额外文件，不过由瀚高数据库管理的特定临时文件除外。但只有常规文件和目录会被拷贝，但用于表空间的符号链接会被保留。指向数据库已知的特定目录的符号链接被拷贝为空目录。其他符号链接和特殊设备文件会被跳过。

表空间默认将以普通格式备份到与它们在服务器上相同的路径中，除非使用了-- tablespace-mapping选项。如果没有这个选项并且表空间正在使用，在同一台服务器上进行普通格式的基础备份将无法工作，因为备份必须要写入到与原始表空间相同的目录位置。

在使用 tar 格式模式时，用户应负责在启动数据库服务前解压每一个 tar 文件。

如果有额外的表空间，用于它们的 tar 文件需要被解压到正确的位置。在这种情况下，服务器将根据包含在base.tar文件中的tablespace\_map文件的内容为那些表空间创建符号链接。

如果在源集簇上启用了组权限，在plain以及tar模式中pg\_basebackup将保留组权限。

**示例**

> 要创建服务器mydbserver的一个基础备份并将它存储在本地目录/home/highgo/highgo/database/8.0/data中：

$ pg\_basebackup -h mydbserver -D /home/highgo/highgo/database/8.0/data

要创建本地服务器的一个备份，为其中每一个表空间产生一个压缩过的 tar 文件，并且将它存储在目录backup中，在运行期间显示一个进度报告：

$ pg\_basebackup -D backup -Ft -z -P

要创建一个单一表空间本地数据库的备份并且使用bzip2压缩它：

$ pg\_basebackup -D - -Ft -X fetch | bzip2 > backup.tar.bz2

（如果在该数据库中有多个表空间，这个命令将失败）。

要创建一个本地数据库的备份，其中/opt/ts中的表空间被重定位到./backup/ts：

$ pg\_basebackup -D backup/data -T /opt/ts=$(pwd)/backup/ts

**参见**

pg\_dump

## pgbench

pgbench — 在数据库上运行一个基准测试

**命令**

pgbench -i \[option...\] \[dbname\]

pgbench \[option...\] \[dbname\]

**描述**

pgbench是一种在瀚高数据库上运行基准测试的简单程序。它可能在并发的数据库会话中一遍一遍地运行相同序列的 SQL 命令，并且计算平均事务率（每秒的事务数）。默认情况下，pgbench会测试一种基于 TPC-B 但是要更宽松的场景，其中在每个事务中涉及五个SELECT、UPDATE以及INSERT命令。但是，通过编写自己的事务脚本文件很容易用来测试其他情况。

pgbench的典型输出像这样：

> transaction type: <builtin: TPC-B (sort of)>
> 
> scaling factor: 10
> 
> query mode: simple
> 
> number of clients: 10
> 
> number of threads: 1
> 
> number of transactions per client: 1000
> 
> number of transactions actually processed: 10000/10000
> 
> tps = 85.184871 (including connections establishing)
> 
> tps = 85.296346 (excluding connections establishing)

前六行报告一些最重要的参数设置。接下来的行报告完成的事务数以及预期的事务数（后者就是客户端数量与每个客户端事务数的乘积），除非运行在完成之前失败，这些值应该是相等的（在-T模式中，只有实际的事务数会被打印出来）。最后两行报告每秒的事务数，分别代表包括和不包括开始数据库会话所花时间的情况。

默认的类 TPC-B 事务测试要求预先设置好特定的表。可以使用-i（初始化）选项调用pgbench来创建并且填充这些表（当你在测试一个自定义脚本时，你不需要这一步，但是需要按你自己的测试需要做一些设置工作）。初始化类似这样：

> pgbench -i \[ other-options \] dbname

其中dbname是要在其中进行测试的预先创建好的数据库的名称（你可能还需要-h、-p或-U选项来指定如何连接到数据库服务器）。

| 注意： |
| --- |
| pgbench -i会创建四个表pgbench\_accounts、 pgbench\_branches、pgbench\_history以及pgbench\_tellers，如果同名表已经存在会被先删除。如果你已经有同名表，一定注意要使用另一个数据库！ |

在默认的情况下”比例因子”为 1，这些表初始包含的行数为：

table # of rows

\---------------------------------

pgbench\_branches 1

pgbench\_tellers 10

pgbench\_accounts 100000

pgbench\_history 0

你可以使用-s（比例因子）选项增加行的数量。-F（填充因子）选项也可以在这里使用。

一旦你完成了必要的设置，你就可以用不包括-i的命令运行基准，也就是：

> pgbench \[ options \] dbname

在近乎所有的情况中，你将需要一些选项来做一次有用的测试。最重要的选项是-c（客户端数量）、-t（事务数量）、-T（时间限制）以及-f（指定一个自定义脚本文件）。完整的列表见下文。

**选项**

下面分成三个部分。数据库初始化期间使用的选项和运行基准时会使用不同的选项，但也有一些选项在两种情况下都使用。

- 初始化选项

pgbench接受下列命令行初始化参数：

> \-i

\--initialize

要求调用初始化模式。

\-I init\_steps

\--init-steps=init\_steps

只执行选出的一组普通初始化步骤。init\_steps指定要被执行的初始化步骤，每一个步骤使用一个字符代表。每一个步骤都以指定的顺序被调用。默认是dtgvp。可用的步骤是：

d（删除）

删除任何已有的pgbench表。

t（创建表）

创建标准pgbench场景使用的表，即pgbench\_accounts、pgbench\_branches、pgbench\_history以及pgbench\_tellers。

g（生成数据）

生成数据并且装入到标准的表中，替换掉已经存在的任何数据。

v（清理）

在标准的表上调用VACUUM。

p（创建主键）

在标准的表上创建主键索引。

f（创建外键）

在标准的表之间创建外键约束（注意这一步默认不会被执行）。

\-F fillfactor

> \--fillfactor=fillfactor

用给定的填充因子创建表pgbench\_accounts、pgbench\_tellers以及pgbench\_branches。

默认是100。

> \-n

\--no-vacuum

在初始化期间不执行清理（这个选项会抑制v初始化步骤，即便在-I中指定了该步骤）。

\-q

\--quiet

把记录切换到安静模式，只是每 5 秒产生一个进度消息。默认的记录会每 100000 行打印一个消息，这经常会在每秒钟输出很多行（特别是在好的硬件上）。

\-s scale\_factor

\--scale=scale\_factor

将生成的行数乘以比例因子。例如，-s 100将在pgbench\_accounts表中创建 10,000,000行。默认为 1。当比例为 20,000 或更高时，用来保存账号标识符的列（aid列）将切换到使用更大的整数（bigint），这样才能足以保存账号标识符。

\--foreign-keys

在标准的表之间创建外键约束（如果f在初始化步骤序列中不存在，这个选项会把它加入）。

\--index-tablespace=index\_tablespace

在指定的表空间而不是默认表空间中创建索引。

\--tablespace=tablespace

在指定的表空间而不是默认表空间中创建表。

\--unlogged-tables

把所有的表创建为非日志记录表而不是永久表。

- 基准选项

pgbench接受下列命令行基准参数：

\-b scriptname\[@weight\]

\--builtin=scriptname\[@weight\]

把指定的内建脚本加入到要执行的脚本列表中。@之后是一个可选的整数权重，它允许调节抽取该脚本的可能性。如果没有指定，它会被设置为 1。可用的内建脚本有：tpcb-like、simple-update和select-only。这里也接受内建名称无歧义的前缀缩写。如果用上特殊的名字list，将会显示内建脚本的列表并且立刻退出。

\-c clients

\--client=clients

模拟的客户端数量，也就是并发数据库会话数量。默认为 1。

\-C

\--connect

为每一个事务建立一个新连接，而不是只为每个客户端会话建立一个连接。这对于度量连接开销有用。

\-d

\--debug

打印调试输出。

\-D varname=value

\--define=varname=value

定义一个由自定义脚本（见下文）使用的变量。允许多个-D选项。

\-f filename\[@weight\]

\--file=filename\[@weight\]

把一个从filename读到的事务脚本加入到被执行的脚本列表中。@后面是一个可选的整数权重，它允许调节抽取该测试的可能性。详见下文。

\-j threads

\--jobs=threads

pgbench中的工作者线程数量。在多 CPU 机器上使用多于一个线程会有用。客户端会尽可能均匀地分布到可用的线程上。默认为 1。

\-l

\--log

把与每一个事务相关的信息写到一个日志文件中。详见下文。

\-L limit

\--latency-limit=limit

对持续超过limit毫秒的事务进行独立的计数和报告，这些事务被认为是迟到（late）了的事务。

在使用限流措施时（--rate=...），滞后于计划超过 limit毫秒并且因此没有希望满足延迟限制的事务根本不会被发送给服务器。这些事务被认为是被跳过（skipped）的事务，它们会被单独计数并且报告。

\-M querymode

\--protocol=querymode

要用来提交查询到服务器的协议：

• simple：使用简单查询协议。

• extended使用扩展查询协议。

• prepared：使用带预备语句的扩展查询语句。

在prepared模式中，pgbench重用从第二次查询迭代开始的语法分析结果，因此pgbench运行速度比其他模式快。

默认是简单查询协议。

\-n

\--no-vacuum

在运行测试前不进行清理。如果你在运行一个不包括标准的表pgbench\_accounts、 pgbench\_branches、pgbench\_history和 pgbench\_tellers的自定义测试场景时，这个选项是必需的。

\-N

\--skip-some-updates

运行内建的简单更新脚本。这是-b simple-update的简写。

\-P sec

\--progress=sec

每sec秒显示进度报告。该报告包括运行了多长时间、从上次报告以来的 tps 以及从上次报告以来事务延迟的平均值和标准偏差。如果低于限流值（-R），延迟会相对于事务预定的开始时间（而不是实际的事务开始时间）计算，因此其中也包括了平均调度延迟时间。

\-r

\--report-latencies

在基准结束后，报告平均的每个命令的每语句等待时间（从客户端的角度来说是执行时间）。详见下文。

\-R rate

\--rate=rate

按照指定的速率执行事务而不是尽可能快地执行（默认行为）。该速率以 tps（每秒事务数）形式给定。如果目标速率高于最大可能速率，则该速率限制不会影响结果。

该速率的目标是按照一条泊松分布的调度时间线开始事务。期望的开始时间表会基于客户端第一次开始的时间（而不是上一个事务结束的时 间）前移。这种方法意味着当事务超过它们的原定结束时间时，更迟的那些有机会再次追赶上来。

当限流措施被激活时，运行结束时报告的事务延迟是从预订的开始时间计算而来的，因此它包括每一个事务不得不等待前一个事务结束所花的时间。该等待时间被称作调度延迟时间，并且它的平均值和最大值也会被单独报告。关于实际事务开始时间的事务延迟（即在数据库中执行事务所花的时间）可以用报告的延迟减去调度延迟时间计算得到。

如果把--latency-limit和--rate一起使用， 当一个事务在前一个事务结束时已经超过了延迟限制时，它可能会滞后非常多，因为延迟是从计划的开始时间计算得来。这类事务不会被发送给服务器，而是一起被跳过并且被单独计数。

一个高的调度延迟时间表示系统无法用选定的客户端和线程数按照指定的速率处理事务。当平均的事务执行时间超过每个事务之间的调度间隔时，每一个后续事务将会落后更多，并且随着测试运行时间越长，调度延迟时间将持续增加。发生这种情况时，你将不得不降低指定的事务速率。

\-s scale\_factor

\--scale=scale\_factor

在pgbench的输出中报告指定的比例因子。对于内建测试，这并非必需；正确的比例因子将通过对pgbench\_branches表中的行计数来检测。不过，当只测试自定义基准（-f选项）时，比例因子将被报告为 1（除非使用了这个选项）。

\-S

\--select-only

执行内建的只有选择的脚本。是-b select-only简写形式。

\-t transactions

\--transactions=transactions

每个客户端运行的事务数量。默认为 10。

\-T seconds

\--time=seconds

运行测试这么多秒，而不是为每个客户端运行固定数量的事务。-t和-T是互斥的。

\-v

\--vacuum-all

在运行测试前清理所有四个标准的表。在没有用-n以及-v时， pgbench将清理pgbench\_tellers 和pgbench\_branches表，并且截pgbench\_history。

\--aggregate-interval=seconds

聚集区间的长度（单位是秒）。仅可以与-l选项一起使用。通过这个选项，日志会包含针对每个区间的概要数据，如下文所述。

\--log-prefix=prefix

设置--log创建的日志文件的文件名前缀。默认是pgbench\_log。

\--progress-timestamp

当显示进度（选项-P）时，使用一个时间戳（Unix 时间）取代从运行开始的秒数。单位是秒，在小数点后是毫秒精度。这可以有助于比较多种工具生成的日志。

\--random-seed=SEED

设置随机数生成器种子。为系统的随机数生成器提供种子，然后随机数生成器会产生一个初始生成器状态序列，每一个线程一个状态。SEED的值可以是：time（默认值，种子基于当前时间）、rand（使用一种强随机源，如果没有可用的源则失败）或者一个无符号十进制整数值。一个pgbench脚本中会显式（random...函数）地或者隐式地（如-- rate使用随机数生成器调度事务）调用随机数生成器。在被明确设置时，用作种子的值会显示在终端上。还可以通过环境变量PGBENCH\_RANDOM\_SEED提供用于SEED的值。为了确保所提供的种子影响所有可能的使用，把这个选项放在第一位或者使用环境变量。

明确地设置种子允许准确地再生一个pgbench运行，对随机数而言。因为随机状态是针对每个线程管理，这意味着如果每一个线程有一个客户端并且没有外部或者数据依赖，则对于一个相同的调用就会有完全相同的pgbench运行。从一种统计的角度来看，再生运行不是什么好主意，因为它能隐藏性能可变性或者不正当地改进性能，即通过命中前一次运行的相同页面来改进性能。不过，它也可以对调试起到很大帮助作用，例如重新运行一种导致错误的棘手用例。请善用。

\--sampling-rate=rate

采样率，在写入数据到日志时被用来减少日志产生的数量。如果给出这个选项，只有指定比例的事务被记录。1.0 表示所有事务都将被记录，0.05 表示只有 5% 的事务会被记录。

在处理日志文件时，记得要考虑这个采样率。例如，当计算TPS值时，你需要相应地乘以这个数字（例如，采样率是 0.01，你将只能得到实际TPS的 1/100）。

- 普通选项

pgbench接受下列命令行普通参数：

\-h hostname

\--host=hostname

数据库服务器的主机名

\-p port

\--port=port

数据库服务器的端口号

\-U login

\--username=login

要作为哪个用户连接

\-V

\--version

打印pgbench版本并退出。

\-?

\--help

显示有关pgbench命令行参数的信息，并且退出。

## pg\_config

pg\_config — 获取已安装的数据库的信息

**命令**

pg\_config \[option...\]

**描述**

pg\_config工具打印当前安装版本的数据库的配置参数。它的设计目的之一是便于想与数据库交互的软件包能够找到所需的头文件和库。

**选项**

要使用pg\_config，提供一个或多个下列选项：

\--bindir

打印用户可执行文件的位置。例如使用这个选项来寻找psql程序。这通常也是pg\_config程序所在的位置。

\--docdir

打印文档文件的位置。

\--htmldir

打印 HTML 文档文件的位置。

\--includedir

打印客户端接口的 C 头文件的位置。

\--pkgincludedir

打印其它 C 头文件的位置。

\--includedir-server

打印用于服务器编程的 C 头文件的位置。

\--libdir

打印对象代码库的位置。

\--pkglibdir

打印动态可载入模块的位置，或者服务器可能搜索它们的位置（其它架构独立数据文件可能也被安装在这个目录）。

\--localedir

打印区域支持文件的位置。

\--mandir

打印手册页的位置。

\--sharedir

打印架构独立支持文件的位置。

\--sysconfdir

打印系统范围配置文件的位置。

\--pgxs

打印扩展 makefile 的位置。

\--configure

打印当数据库被配置编译时给予configure脚本的选项。这可以被用来重新得到相同的配置，或者找出是哪个选项编译了一个二进制包（不过注意二进制包通常包含厂商相关的自定补丁）。

\--cc

打印用来编译数据库的CC变量值。这显示被使用的 C 编译器。

\--cppflags

打印用来编译数据库的CPPFLAGS变量值。这显示在预处理时需要的 C 编译器开关（典型的是-I开关）。

\--cflags

打印用来编译数据库的CFLAGS变量值。这显示被使用的 C 编译器开关。

\--cflags\_sl

打印用来编译数据库的CFLAGS\_SL变量值。这显示被用来编译共享库的额外 C 编译器开关。

\--ldflags

打印用来编译数据库的LDFLAGS变量值。这显示链接器开关。

\--ldflags\_ex

打印用来编译数据库的LDFLAGS\_EX变量值。这只显示被用来编译可执行程序的链接器开关。

\--ldflags\_sl

打印用来编译数据库的LDFLAGS\_SL变量值。这只显示被用来编译共享库的链接器开关。

\--libs

打印用来编译数据库的LIBS变量值。这通常包含用于链接到数据库中的外部库的-l开关。

\--version

打印数据库的版本。

\-?

\--help

显示有关pg\_config命令行参数的帮助并退出。

如果给定多于一个选项，将按照相同的顺序打印信息，每行一项。如果没有给定选项，将打印所有可用信息，并带有标签。

## pg\_dump

pg\_dump — 把瀚高数据库抽取为一个脚本文件或其他归档文件

**命令**

pg\_dump \[connection-option...\] \[option...\] \[dbname\]

**描述**

pg\_dump是一种用于备份瀚高数据库的工具。即使数据库正在被并发使用，它也能创建一致的备份。pg\_dump不阻塞其他用户访问数据库（读取或写入）。

pg\_dump只转储单个数据库。要备份一个集簇或者集簇中 对于所有数据库公共的全局对象（例如角色和表空间），应使用 pg\_dumpall。

转储可以被输出到脚本或归档文件格式。脚本转储是包含 SQL 命令的纯文本文件，它们可以用来重构数据库到它被转储时的状态。要从这样一个脚本恢复，需使用psql。脚本文件甚至可以被用来在其他机器和其他架构上重构数据库。在经过一些修改后，甚至可以在其他SQL数据库产品上重构数据库。

另一种可选的归档文件格式必须与pg\_restore配合使用来重建数据库。它们允许pg\_restore能选择恢复什么，或者甚至在恢复之前对条目重排序。归档文件格式被设计为在架构之间可移植。

当使用归档文件格式之一并与pg\_restore组合时，pg\_dump提供了一种灵活的归档和传输机制。pg\_dump可以被用来备份整个数据库，然后pg\_restore可以被用来检查归档并/或选择数据库的哪些部分要被恢复。最灵活的输出文件格式是”自定义”格式（-Fc）和”目录”格式（-Fd）。它们允许选择和重排序所有已归档项、支持并行恢复并且默认是压缩的。”目录”格式是唯一一种支持并行转储的格式。

当运行pg\_dump时，我们应该检查输出中有没有任何警告（打印在标准错误上），特别是要考虑到下面列出的限制。

**选项**

下列命令选项控制输出的内容和格式。

dbname

指定要被转储的数据库名。如果没有指定，将使用环境变量PGDATABASE。如果环境变量也没有设置，则使用指定给该连接的用户名。

\-a

\--data-only

只转储数据，而不转储模式（数据定义）。表数据、大对象和序列值都会被转储。

这个选项类似于指定--section=data。

\-b

\--blobs

在转储中包括大对象。这是当--schema、--table或--schema-only被指定时的默认行为。因此，只有在请求转储一个特定方案或者表的情况中，-b开关才对向转储中加入大对象有用。注意blobs是被考虑的数据，因此在使用--data-only时将被包括在内，但在使用--schema-only时则不会包括。

\-B

\--no-blobs

在转储中排除大对象。

当同时给定-b和-B时，行为是在数据被转储时输出大对象，请参考-b文档。

\-c

\--clean

在输出创建数据库对象的命令之前输出清除（删除）它们的命令（除非也指定了--if-exists，如果任何对象不存在于目的数据库中，恢复可能会产生一些伤害性的错误消息）。

这个选项只对纯文本格式有意义。对于归档格式，你可以在调用pg\_restore时指定该选项。

\-C

\--create

使得在输出的开始是一个创建数据库本身并且重新连接到被创建的数据库的命令（通过这种形式的一个脚本，在运行脚本之前你连接的是目标安装中的哪个数据库都没有关系）。如果也指定了--clean，脚本会在重新连接到目标数据库之前先删除它然后再重建。

通过--create，输出还会包括数据库的注释（如果有）以及与这个数据库相关的任何配置变量设置，也就是任何提到了这个数据库的ALTER DATABASE... SET...命令和ALTER ROLE... IN DATABASE... SET...命令。该数据库本身的访问特权也会被转储，除非指定有--no-acl。

这个选项只对纯文本格式有意义。对于归档格式，你可以在你调用pg\_restore时指定这个选项。

\-E encoding

\--encoding=encoding

以指定的字符集编码创建转储。在默认情况下，该转储会以该数据库的编码创建（另一种得到相同结果的方式是将PGCLIENTENCODING环境变量设置成想要的转储编码）。

\-f file

\--file=file

将输出发送到指定文件。对于基于输出格式的文件这个参数可以被忽略，在那种情况下将使用标准输出。不过对于目录输出格式必须给定这个参数，在目录输出格式中指定的是一个目录而不是一个文件。在这种情况中，该目录会由pg\_dump创建并且不需要以前就存在。

\-F format

\--format=format

选择输出的格式。format可以是下列之一：

p

plain

> 输出一个纯文本形式的SQL脚本文件（默认值）。

c

custom

> 输出一个适合于作为pg\_restore输入的自定义格式归档。和目录输出格式一起，这是最灵活的输出格式，它允许在恢复时手动选择和排序已归档的项。这种格式在默认情况还会被压缩。

d

directory

> 输出一个适合作为pg\_restore输入的目录格式归档。这将创建一个目录，其中每个被转储的表和大对象都有一个文件，外加一个所谓的目录文件，该文件以一种pg\_restore能读取的机器可读格式描述被转储的对象。一个目录格式归档能用标准Unix 工具操纵，例如一个未压缩归档中的文件可以使用gzip工具压缩。这种格式默认情况下是被压缩的并且也支持并行转储。

t

tar

> 输出一个适合于输入到pg\_restore中的tar格式归档。tar 格式可以兼容目录格式，抽取一个 tar 格式的归档会产生一个合法的目录格式归档。不过，tar 格式不支持压缩。还有，在使用 tar 格式时，表数据项的相对顺序不能在恢复过程中被更改。

\-j njobs

\--jobs=njobs

通过同时归档njobs个表来运行并行转储。这个选项缩减了转储的时间，但是它也增加了数据库服务器上的负载。你只能和目录输出格式一起使用这个选项，因为这是唯一一种让多个进程能在同一时间写其数据的输出格式。

pg\_dump将打开njobs + 1 个到该数据库的连接，因此确保你的max\_connections设置足够高以容纳所有的连接。

在运行一次并行转储时请求数据库对象上的排他锁可能导致转储失败。其原因是，pg\_dump主控进程会在工作者进程将要稍后转储的对象上请求共享锁，以便确保在转储运行时不会有人删除它们并让它们出错。如果另一个客户端接着请求一个表上的排他锁，那个锁将不会被授予但是会被排入队列等待主控进程的共享锁被释放。因此，任何其他对该表的访问将不会被授予或者将排在排他锁请求之后。这包括尝试转储该表的工作者进程。如果没有任何防范措施，这可能会是一种经典的死锁情况。要检测这种冲突，pg\_dump工作者进程使用NOWAIT选项请求另一个共享锁。如果该工作者进程没有被授予这个共享锁，其他某人必定已经在同时请求了一个排他锁并且没有办法继续转储，因此pg\_dump除了中止转储之外别无选择。

\-n pattern

\--schema=pattern

只转储匹配pattern的模式，这会选择模式本身以及它所包含的所有对象。当没有指定这个选项时，目标数据库中所有非系统模式都将被转储。多个模式可以通过书写多个-n开关来选择。另外，pattern参数可以被解释为一种根据psql's\\d命令所用的相同规则）编写的模式，这样多个模式也可以通过在该模式中书写通配字符来选择。在使用通配符时，如果需要阻止 shell 展开通配符需要小心引用该模式，见示例。

| 注意： |
| --- |
| 当-n被指定时，pg\_dump不会尝试转储所选模式可能依赖的任何其他数据库对象。因此，无法保证一次指定模式转储的结果能够仅凭其本身被成功地恢复到一个干净的数据库中。 |

| **注意：** |
| --- |
| 当-n被指定时，非模式对象（如二进制大对象）不会被转储。你可以使用--blobs开关将二进制大对象加回到该转储中。 |

\-N pattern

\--exclude-schema=pattern

不转储匹配pattern模式的任何模式。该模式被根据-n所用的相同规则被解释。-N可以被给定多次来排除匹配几个模式中任意一个的模式。

当-n和-N都被给定时，该行为是只转储匹配至少一个-n开关但是不匹配-N开关的模式。如果只有-N而没有-n，那么匹配-N的模式会被从一个正常转储中排除。

\-O

\--no-owner

不输出设置对象拥有关系来匹配原始数据库的命令。默认情况下，pg\_dump会发出ALTER OWNER或SET SESSION AUTHORIZATION语句来设置被创建的数据库对象的拥有关系。除非该脚本被一个超级用户（或是拥有脚本中所有对象的同一个用户）启动，这些语句都将会失败。要使一个脚本能够被任意用户恢复，但把所有对象的拥有关系都给这个用户，可指定-O。

这个选项只对纯文本格式有意义。对于归档格式，你可以在调用pg\_restore时指定该选项。

\-R

\--no-reconnect

这个选项已经废弃，但是为了向后兼容仍然能被接受。

\-s

\--schema-only

只转储对象定义（模式），而非数据。

这个选项是--data-only的逆选项。它和指定--section=pre-data --section=post-data相似，但是由于历史原因又不完全相同。（不要把这个选项和--schema选项混淆，后者在”schema”的使用上有不同的含义）。

要为数据库中表的一个子集排除表数据，见--exclude-table-data。

\-S username

\--superuser=username

指定要在禁用触发器时使用的超级用户的用户名。只有使用--disable-triggers时，这个选项才相关（通常，最好省去这个选项，而作为超级用户来启动结果脚本来取而代之）。

\-t pattern

\--table=pattern

只转储名字匹配pattern的表，”table”还可以包括视图、物化视图、序列和外部表。

通过写多个-t开关可以选择多个表。另外，pattern参数可以被解释为一种根据psql's \\d命令所用的相同规则编写的模式，这样多个表也可以通过在该模式中书写通配字符来选择。在使用通配符时，如果需要阻止 shell 展开通配符需要小心引用该模式，见示例。

当-t被使用时，-n和-N开关不会有效果，因为被-t选择的表将被转储而无视那些开关，并且非表对象将不会被转储。

| **注意：** |
| --- |
| 当-t被指定时，pg\_dump不会尝试转储所选表可能依赖的任何其他数据库对象。因此，无法保证一次指定表转储的结果能够仅凭其本身被成功地恢复到一个干净的数据库中。 |

\-T pattern

\--exclude-table=pattern

不转储匹配pattern模式的任何表。该模式被根据-t所用的相同规则被解释。-T可以被给定多次来排除匹配几个模式中任意一个的模式。

当-t和-T都被给定时，该行为是只转储匹配至少一个-t开关但是不匹配-T开关的表。如果只有-T而没有-t，那么匹配-T的表会被从一个正常转储中排除。

\-v

\--verbose

指定冗长模式。这将导致pg\_dump向标准错误输出详细的对象注释以及转储文件的开始/停止时间，还有进度消息。

\-V

\--version

pg\_dump版本并退出。

\-x

\--no-privileges

\--no-acl

防止转储访问特权（授予/收回命令）。

\-Z 0..9

\--compress=0..9

指定要使用的压缩级别。零意味着不压缩。对于自定义归档格式，这会指定个体表数据段的压缩，并且默认是进行中等级别的压缩。对于纯文本输出，设置一个非零压缩级别会导致整个输出文件被压缩，就好像它被gzip处理过一样，但是默认是不压缩。tar 归档格式当前完全不支持压缩。

\--binary-upgrade

这个选项用于就地升级功能。我们不推荐也不支持把它用于其他目的。这个选项在未来的发行中可能被改变而不做通知。

\--column-inserts

\--attribute-inserts

将数据转储为带有显式列名的INSERT命令（INSERT INTO table (column,...)VALUES...）。这将使得恢复过程非常慢，这主要用于使转储能够被载入到非瀚高数据库中。重新加载期间的任何错误都将导致有问题的INSERT相关的行将丢失，而不是整个表内容。

\--disable-dollar-quoting

这个选项禁止在函数体中使用美元符号引用，并且强制它们使用 SQL 标准字符串语法被引用。

\--disable-triggers

只有在创建一个只转储数据的转储时，这个选项才相关。它指示pg\_dump包括在数据被重新载入时能够临时禁用目标表上的触发器的命令。如果你在表上有引用完整性检查或其他触发器，并且你在数据重新载入期间不想调用它们，请使用这个选项。

当前，为--disable-triggers发出的命令必须作为超级用户来执行。因此，你还应当使用-S指定一个超级用户名，或者宁可作为一个超级用户启动结果脚本。

这个选项只对纯文本格式有意义。对于归档格式，你可以在调用pg\_restore时指定这个选项。

\--enable-row-security

只有在转储具有行安全性的表的内容时，这个选项才相关。默认情况下， pg\_dump将把row\_security设置为 off 来确保从该表中转储出所有的数据。如果用户不具有足够能绕过行安全性的特权，那么会抛出一个错误这个参数指示pg\_dump将 row\_security设置为 on，允许用户只转储该表中它们能够访问到的部分内容。

注意如果当前你使用了这个选项，你可能还想得到INSERT格式的转储，因为恢复期间的COPY FROM不支持行安全性。

\--exclude-table-data=pattern

不转储匹配pattern模式的任何表中的数据。该模式根据-t的相同规则被解释。-- exclude-table-data可以被给定多次来排除匹配多个模式的表。当你需要一个特定表的定义但不想要其中的数据时，这个选项就有用了。

要排除数据库中所有表的数据，见--schema-only。

\--extra-float-digits=ndigits

在转储浮点数据时使用规定的extra\_float\_digits值，而不是最大可用精度。以备份目的生成的常规转储不使用此选项。

\--if-exists

时间条件性命令（即增加一个IF EXISTS子句）来清除数据库和其他对象。 只有同时指定了--clean时，这个选项才可用。

\--inserts

将数据转储为INSERT命令（而不是COPY）。这将使得恢复非常慢，这主要用于使转储能够被载入到非瀚高数据库中。重新加载期间的任何错误都将导致有问题的INSERT相关的行将丢失，而不是整个表内容。注意如果你已经重新安排了列序，该恢复可能会一起失败。--column-inserts选项对于列序改变是安全的，但是会更慢。

\--load-via-partition-root

在为一个分区表转储数据时，让COPY语句或者INSERT语句把包含它的分区层次的根而不是分区自身作为目标。这导致在数据被装载时，会为每一个行重新确定合适的分区。如果在一台服务器上重新装载数据时会出现行并不是总是落入到和原始服务器上相同的分区中的情况，这个选项就很有用。例如，如果分区列是文本类型并且两个系统中用于排序分区列的排序规则有着不同的定义，就会发生这种情况。

在从用这个选项制作的归档恢复时，最好不要使用并行，因为pg\_restore将不能准确地知道一个给定的归档数据项将把数据装载到哪个分区中。这会导致效率不高，因为在并行任务时会有锁冲突，或者甚至可能由于在所有的相关数据被装载前建立了外键约束而导致重新装载失败。

\--lock-wait-timeout=timeout

在转储的开始从不等待共享表锁的获得。而是在指定的timeout内不能锁定一个表时失败。超时时长可以用SET statement\_timeout接受的任何格式指定。

\--no-comments

不转储注释。

\--no-publications

不转储publication。

\--no-security-labels

不转储安全标签。

\--no-subscriptions

不转储订阅。

\--no-sync

默认情况下，pg\_dump将等待所有文件被安全地写入磁盘。这个选项会让pg\_dump不等待直接返回，这样会更快，但是也意味着后续的一次操作系统崩溃会让该转储损坏。通常这个选项对测试有用，但是不应该在从生产安装中转储数据时使用。

\--no-synchronized-snapshots

这个选项允许对瀚高数据库最早版本的服务器运行pg\_dump -j，详见-j参数的文档。

\--no-tablespaces

不要输出选择表空间的命令。通过这个选项，在恢复期间所有的对象都会被创建在任何作为默认的表空间中。

这个选项只对纯文本格式有意义。对于归档格式，你可以在调用pg\_restore时指定该选项。

\--no-unlogged-table-data

不转储非日志记录表的内容。这个选项对于表定义（模式）是否被转储没有影响，它只会限制转储表数据。当从一个后备服务器转储时，在非日志记录表中的数据总是会被排除。

\--on-conflict-do-nothing

增加 ON CONFLICT DO NOTHING 到INSERT commands。 除非规定了 --inserts,--column-inserts 或--rows-per-insert ，否则此选项是无效的。

\--quote-all-identifiers 强制引用所有标识符。当从瀚高数据库主版本与pg\_dump不同的服务器上转储一个数据库时或者当输出准备载入到一个具有不同主版本的服务器时，推荐使用这个选项。默认情况下，pg\_dump只对在其主版本中是被保留词的标识符加上引号。在转储其他版本服务器时，这种默认行为有时会导致兼容性问题，因为那些版本可能具有些许不同的被保留词集合。使用--quote-all-identifiers能阻止这种问题，但代价是转储脚本更难阅读。

\--rows-per-insert=nrows

数据转储为INSERT命令（而不是COPY）。控制每个INSERT命令的最大行数。指定的值必须大于零。重新加载期间的任何错误都将导致有问题的INSERT相关的行将丢失，而不是整个表内容。

\--section=sectionname

只转储命名节。节的名称可以是pre-data、data或post-data。这个选项可以被指定多次来选择多个节。默认是转储所有节。

数据节包含真正的表数据、大对象内容和序列值。数据后项包括索引、触发器、规则和除了已验证检查约束之外的约束的定义。数据前项包括所有其他数据定义项。

\--serializable-deferrable

为转储使用一个可序列化事务，以保证所使用的快照与后来的数据库状态是一致的。但是这样做是在事务流中等待一个点，在该点上不能存在异常，这样就不会有转储失败或者导致其他事务带着serialization\_failure回滚的风险。

对于一个只为灾难恢复存在的转储，这个选项没什么益处。如果一个转储被用来在原始数据库持续被更新期间载入一份用于报表或其他只读负载的数据库拷贝时，这个选项就有所帮助。如果没有这个选项，转储可能会反映一个与最终提交事务的任何执行序列都不一致的状态。例如，如果使用了批处理技术，一个批处理在转储中可以显示为关闭，而其中的所有项都不出现。

如果 pg\_dump 被启动时没有读写事务在活动，则这个选项没有什么不同。如果有读写事务在活动，该转储的启动可能会被延迟一段不确定的时间。一旦开始运行，有没有这个开关的表现是相同的。

\--snapshot=snapshotname

在做一个数据库的转储时指定一个同步的快照。在需要把转储和一个逻辑复制槽或者一个并发会话同步时可以用上这个选项。

在并行转储的情况下，将使用这个选项指定的快照名而不是取一个新快照。

\--strict-names

要求每一个模式（-n/--schema）和表（-t/--table）限定符匹配要转储的数据库中至少一个模式/表。注意，如果没有找到有这样的模式/表限定符匹配，即便没有--strict-names，pg\_dump也将生成一个错误。

这个选项对-N/--exclude-schema、-T/--exclude-table或者--exclude-table-data没有效果。无法匹配任何对象的排除模式不会被当作错误。

\--use-set-session-authorization

输出 SQL-标准的SET SESSION AUTHORIZATION命令取代ALTER OWNER命令来确定对象的所有关系。这让该转储更加兼容标准，但是取决于该转储中对象的历史，该转储可能无法正常恢复。而且，一个使用SET SESSION AUTHORIZATION的转储将一定会要求超级用户特权来正确地恢复，而ALTER OWNER要求更少的特权。

\-?

\--help

显示有关pg\_dump命令行参数的帮助并退出。

下列命令行选项控制数据库连接参数。

\-d dbname

\--dbname=dbname

指定要连接到的数据库名。这等效于指定dbname为命令行上的第一个非选项参数。

如果这个参数包含一个=符号或者以一个合法的URI前缀开始，它将被视作一个conninfo字符串。

\-h host

\--host=host

指定服务器正在运行的机器的主机名。如果该值开始于一个斜线，它被用作一个 Unix域套接字的目录。默认是从PGHOST环境变量中取得（如果被设置），否则将尝试一次Unix 域套接字连接。

\-p port

\--port=port

指定服务器正在监听连接的 TCP 端口或本地 Unix 域套接字文件扩展名。默认是放在PGPORT环境变量中（如果被设置），否则使用编译在程序中的默认值。

\-U username

\--username=username

要作为哪个用户连接。

\--role=rolename

指定一个用来创建该转储的角色名。这个选项导致pg\_dump在连接到数据库后发出一个SET ROLE rolename命令。当已认证用户（由-U指定）缺少pg\_dump所需的特权但是能够切换到一个具有所需权利的角色时，这个选项很有用。一些安装有针对直接作为超级用户登录的策略，使用这个选项可以让转储在不违反该策略的前提下完成。

**环境**

PGDATABASE

PGHOST

PGOPTIONS

PGPORT

PGUSER

默认连接参数

PG\_COLOR

规定在诊断消息中是否使用颜色。可能的值为always、 auto、never。

**诊断**

pg\_dump在内部执行SELECT语句。如果你运行pg\_dump时出现问题，确定你能够从正在使用的数据库中选择信息，例如psql。此外，libpq前端-后端库所使用的任何默认连接设置和环境变量都将适用。

pg\_dump的数据库活动会被统计收集器正常地收集。如果不想这样，你可以通过PGOPTIONS或ALTER USER命令设置参数track\_counts为假。

**注释**

如果你的数据库集簇对于template1数据库有任何本地添加，要注意将pg\_dump的输出恢复到一个真正的空数据库。否则你很可能由于以增加对象的重复定义而得到错误。要创建一个不带任何本地添加的空数据库，从template0而不是template1复制它，例如：

CREATE DATABASE foo WITH TEMPLATE template0;

当一个只含数据的转储被选中并且使用了选项--disable-triggers时，pg\_dump在开始插入数据之前会发出命令禁用用户表上的触发器，并且接着在数据被插入之后发出命令重新启用它们。如果恢复中途被停止，系统目录可能会停留在一种错误状态。

pg\_dump产生的转储文件不包含优化器用来做出查询计划决定的统计信息。因此，在从一个转储文件恢复后运行ANALYZE来确保最优性能是明智的。

因为pg\_dump被用来传输数据到更新版本的数据库，pg\_dump的输出被认为可以载入到比pg\_dump版本更新的数据库服务器中。pg\_dump也能够从比其版本更旧的数据库服务器中转储。不过，pg\_dump无法从比起主版本号更新的数据库服务器中转储，它甚至将拒绝冒着创建一个非法转储的风险尝试。还有，不保证pg\_dump的输出能被载入到一个更旧主版本的服务器 — 即使该转储是从该版本的服务器中被取得也不行。将一个转储文件载入到一个更旧的服务器可能需要手工编辑该转储文件来移除旧服务器无法理解的语法。在跨版本的情况下，推荐使用--quote-all-identifiers选项，因为它可以避免因为不同版本间的保留词列表变化而发生问题。

在转储逻辑复制订阅时，pg\_dump将生成使用connect = false选项的CREATE SUBSCRIPTION命令，这样恢复订阅时不会建立远程连接来创建复制槽或者进行初始的表拷贝。通过这种方式，可以无需到远程服务器的网络访问就能恢复该转储。然后就需要用户以一种合适的方式

重新激活订阅。如果涉及到的主机已经改变，连接信息可能也必须被改变。在开启一次新的全表拷贝之前，截断目标表也可能是合适的。

**示例**

要把一个数据库mydb转储到一个 SQL 脚本文件：

$ pg\_dump mydb > db.sql

要把这样一个脚本重新载入到一个（新创建的）名为newdb的数据库中：

$ psql -d newdb -f db.sql

要转储一个数据库到一个自定义格式归档文件：

$ pg\_dump -Fc mydb > db.dump

要转储一个数据库到一个目录格式的归档：

$ pg\_dump -Fd mydb -f dumpdir

要用 5 个并行的工作者任务转储一个数据库到一个目录格式的归档：

$ pg\_dump -Fd mydb -j 5 -f dumpdir

要把一个归档文件重新载入到一个（新创建的）名为newdb的数据库：

$ pg\_restore -d newdb db.dump

把一个归档文件重新装载到同一个数据库（该归档正是从这个数据库中转储得来）中，丢掉那个数据库中的当前内容：

$ pg\_restore -d highgo --clean --create db.dump

要转储一个名为mytab的表：

$ pg\_dump -t mytab mydb > db.sql

要转储detroit模式中名称以emp开始的所有表，排除名为employee\_log的表：

$ pg\_dump -t 'detroit.emp\*' -T detroit.employee\_log mydb > db.sql

要转储名称以east或者west开始并且以gsm结束的所有模式，排除名称包含词test的任何模式：

$ pg\_dump -n 'east\*gsm' -n 'west\*gsm' -N '\*test\*' mydb > db.sql

同样，用正则表达式记号法来合并开关：

$ pg\_dump -n '(east|west)\*gsm' -N '\*test\*' mydb > db.sql

要转储除了名称以ts\_开头的表之外的所有数据库对象：

$ pg\_dump -T 'ts\_\*' mydb > db.sql

要在-t和相关开关中指定一个大写形式或混合大小写形式的名称，你需要双引用该名称，否则它会被折叠到小写形式（见模式（Pattern））。但是双引号对于 shell 是特殊的，所以反过来它们必须被引用。因此，要转储一个有混合大小写名称的表，你需要类似这样的东西：

$ pg\_dump -t "\\"MixedCaseName\\"" mydb > mytab.sql

**参见**

pg\_dumpall, pg\_restore, psql

## pg\_dumpall

pg\_dumpall — 将一个瀚高数据库集簇抽取到一个脚本文件中

**命令**

pg\_dumpall \[connection-option...\] \[option...\]

**描述**

pg\_dumpall工具可以一个集簇中所有的数据库写出到（”转储”）一个脚本文件。该脚本文件包含可以用作psql的输入SQL命令来恢复数据库。它会对集簇中的每个数据库调用pg\_dump来完成该工作。pg\_dumpall还转储对所有数据库公用的全局对象（pg\_dump不保存这些对象），也就是说数据库角色和表空间都会被转储。目前这包括适数据库用户和组、表空间以及适合所有数据库的访问权限等属性。

因为pg\_dumpall从所有数据库中读取表，所以你很可能需要以一个数据库超级用户的身份连接以便生成完整的转储。同样，你也需要超级用户特权执行保存下来的脚本，这样才能增加角色和组以及创建数据库。

SQL 脚本将被写出到标准输出。使用 -f/--file 选项或者 shell 操作符可以把它重定向到一个文件。

pg\_dumpall需要多次连接到数据库服务（每个数据库一次）。如果你使用口令认证，可能每次都会要求口令。这种情况下使用一个~/.pgpass会比较方便。

**选项**

下列命令行选项用于控制输出的内容和格式。

\-a

\--data-only

只转储数据，不转储模式（数据定义）。

\-c

\--clean

包括在重建数据库之前清除（移除）它们的 SQL 命令。角色和表空间的DROP命令也会被加入进来。

\-E encoding

\--encoding=encoding

用指定的字符集编码创建转储。默认情况下，转储使用数据库的编码创建（另一种得到相同结果的方法是设置PGCLIENTENCODING环境变量为想要的转储编码）。

\-f filename

\--file=filename

将输出发送到指定的文件中。如果省略，将使用标准输出。

\-g

\--globals-only

只转储全局对象（角色和表空间），而不转储数据库。

\-O

\--no-owner

不输出用于设置对象所有权以符合原始数据库的命令。默认情况下，pg\_dumpall发出ALTER OWNER或SET SESSION AUTHORIZATION语句来设置被创建的模式元素的所有权。除非脚本是由一个超级用户（或者是拥有脚本中所有对象的同一个用户）所运行，这些语句在脚本运行时会失败。要使得一个脚本能被任意用户恢复，但又不想给予该用户所有对象的所有权，可以指定-O。

\-r

\--roles-only

只转储角色，不转储数据库和表空间。

\-s

\--schema-only

只转储对象定义（模式），不转储数据。

\-S username

\--superuser=username

指定要在禁用触发器时使用的超级用户的用户名。只有使用--disable-triggers时，这个选项才相关（通常，最好省去这个选项，而作为超级用户来启动结果脚本来取而代之）。

\-t

\--tablespaces-only

只转储表空间，不转储数据库和角色。

\-v

\--verbose

指定细节模式。这将导致pg\_dumpall向标准错误输出详细的对象注释以及转储文件的开始/停止时间，还有进度消息。它也会启用pg\_dump中的细节输出。

\-V

\--version

打印pg\_dumpall版本并退出。

\-x

\--no-privileges

\--no-acl

防止转储访问特权（授予/收回命令）。

\--binary-upgrade

这个选项用于就地升级功能。我们不推荐也不支持把它用于其他目的。这个选项在未来的发行中可能被改变而不做通知。

\--column-inserts

\--attribute-inserts

将数据转储为带有显式列名的INSERT命令（INSERT INTO

table(column,...) VALUES...）。这将使得恢复过程非常慢，这主要用于使转储能够被载入到非 瀚高数据库数据库中。

\--disable-dollar-quoting

这个选项禁止在函数体中使用美元符号引用，并且强制它们使用 SQL 标准字符串语法被引用。

\--disable-triggers

只有在创建一个只转储数据的转储时，这个选项才相关。它指示pg\_dumpall包括在数据被重新载入时能够临时禁用目标表上的触发器的命令。如果你在表上有引用完整性检查或其他触发器，并且你在数据重新载入期间不想调用它们，请使用这个选项。

当前，为--disable-triggers发出的命令必须作为超级用户来执行。因此，你还应当使用-S指定一个超级用户名，或者宁可作为一个超级用户启动结果脚本。

\--extra-float-digits=ndigits

在转储浮点数据时使用extra\_float\_digits规定的值，而不是最大可用精度。备份目的进行的常规转储不使用此选项。

\--exclude-database=pattern

不要转储名字与 pattern 匹配的数据库。可以通过编写多个--exclude-database开关来排除多个模式。 pattern参数被解释为模式，根据psql的\\d命令使用的相同规则 (参见模式（Pattern）)，因此，通过在模式中编写通配符也可以排除多个数据库。 使用通配符时，请谨慎的引用模式，如果需要防止shell通配符扩展。

\--if-exists

时间条件性命令（即增加一个IF EXISTS子句）来清除数据库和其他对象。 只有同时指定了--clean时，这个选项才可用。

\--inserts

将数据转储为INSERT命令（而不是COPY）。这将使得恢复非常慢，这主要用于使转储能够被载入到非瀚高数据库中。注意如果你已经重新安排了列序，该恢复可能会一起失败。--column-inserts选项对于列序改变是安全的，但是会更慢。

\--load-via-partition-root

在为一个分区表转储数据时，让COPY语句或者INSERT语句把包含它的分区层次的根而不是分区自身作为目标。这导致在数据被装载时，会为每一个行重新确定合适的分区。如果在一台服务器上重新装载数据时会出现行并不是总是落入到和原始服务器上相同的分区中的情况，这个选项就很有用。例如，如果分区列是文本类型并且两个系统中用于排序分区列的排序规则有着不同的定义，就会发生这种情况。

\--lock-wait-timeout=timeout

在转储的开始从不等待共享表锁的获得。而是在指定的timeout内不能锁定一个表时失败。超时时长可以用SET statement\_timeout接受的任何格式指定（允许的值根据你从其转出的服务器版本变化，但是从 7.3 以来的所有版本都接受一个整数表示的毫秒数。如果从 7.3 以前的服务器转出，这个选项会被忽略。）。

\--no-comments

不转储注释。

\--no-publications

不转储publication。

\--no-role-passwords

不为角色转储口令。在恢复完后，角色的口令将是空口令，并且在设置口令之前口令认证都不会成功。由于指定这个选项时并不需要口令值，角色信息将从目录视图pg\_roles而不是pg\_authid中读出。因此，如果对pg\_authid的访问被某条安全性策略所限制，那么这个选项也会有所帮助。

\--no-security-labels

不转储安全标签。

\--no-subscriptions

不转储subscription。

\--no-sync

默认情况下，pg\_dumpall将等待所有文件被安全地写入到磁盘。这个选项会让pg\_dumpall不做这种等待而返回，这样会更快，但是意味着后续的操作系统崩溃可能留下被损坏的转储。通常来说，这个选项对测试有用，但不应该在从生产安装中转储数据时使用。

\--no-tablespaces

不要输出选择表空间的命令。通过这个选项，在恢复期间所有的对象都会被创建在任何作为默认的表空间中。

\--no-unlogged-table-data

不转储非日志记录表的内容。这个选项对于表定义（模式）是否被转储没有影响，它只会限制转储表数据。

\--on-conflict-do-nothing

添加ON CONFLICT DO NOTHING到INSERT命令。除非--inserts或--column-inserts也被规定，否则此选项不生效。

\--quote-all-identifiers

强制引用所有标识符。在从一个与pg\_dumpall主版本不同的数据库服务转储数据库时或者要将输出载入到一个不同主版本的服务器时，推荐使用这个选项。默认情况下，pg\_dumpall只会对为其主版本中保留词的标识符加上引号。在与其他版本的具有不同保留词集合的服务器交互时，这有时会导致兼容性问题。使用--quote-all-identifiers可以阻止这类问题，但是代价是转储脚本会更加难读。

\--rows-per-insert=nrows

将数据转储为INSERT命令（而不是COPY）。控制每个INSERT命令的最大行数。 指定的值必须是大于零的数。重新加载期间的任何错误都将导致仅丢失有问题的INSERT的行，而不是整个表内容。

\--use-set-session-authorization

输出 SQL-标准的SET SESSION AUTHORIZATION命令取代ALTER OWNER命令来确定对象的所有关系。这让该转储更加兼容标准，但是取决于该转储中对象的历史，该转储可能无法正常恢复。

\-?

\--help

显示有关pg\_dumpall命令行参数的帮助并退出。

下列命令行选项控制数据库连接参数。

\-d connstr

\--dbname=connstr

以一个连接字符串的形式，指定用来连接到服务器的参数。

这个选项被称为--dbname是为了和其他客户端应用一致，但是因为pg\_dumpall需要连接多个数据库，连接字符串中的数据库名将被忽略。使用-l选项指定一个数据库，该数据库被用于初始连接，这将转储全局对象并且发现需要转储哪些其他数据库。

\-h host

\--host=host

指定服务器正在运行的机器的主机名。如果该值开始于一个斜线，它被用作一个 Unix域套接字的目录。默认是从PGHOST环境变量中取得（如果被设置），否则将尝试一次Unix 域套接字连接。

\-l dbname

\--database=dbname

指定要连接到哪个数据库转储全局对象以及发现要转储哪些其他数据库。如果没有指定，将会使用highgo数据库，如果不存在，就使用 template1。

\-p port

\--port=port

指定服务器正在监听连接的 TCP 端口或本地 Unix 域套接字文件扩展名。默认是放在PGPORT环境变量中（如果被设置），否则使用编译在程序中的默认值。

\-U username

\--username=username

要作为哪个用户连接。

\-w

\--no-password

从不发出一个口令提示。如果服务器要求口令认证并且没有其他方式提供口令（例如一个.pgpass文件），那儿连接尝试将失败。这个选项对于批处理任务和脚本有用，因为在其中没有一个用户来输入口令。

\-W

\--password

强制pg\_dumpall在连接到一个数据库之前提示要求一个口令。

这个选项从来不是必须的，因为如果服务器要求口令认证，pg\_dumpall将自动提示要求一个口令。但是，pg\_dumpall将浪费一次连接尝试来发现服务器想要一个口令。在某些情况下，值得键入-W来避免额外的连接尝试。

注意对每个要被转储的数据库，口令提示都会再次出现。通常，最好设置一 个~/.pgpass文件来减少手工口令输入。

\--role=rolename

指定一个用来创建该转储的角色名。这个选项导致pg\_dump在连接到数据库后发出一个SET ROLE rolename命令。当已认证用户（由-U指定）缺少pg\_dump所需的特权但是能够切换到一个具有所需权利的角色时，这个选项很有用。一些安装有针对直接作为超级用户登录的策略，使用这个选项可以让转储在不违反该策略的前提下完成。

**环境**

> PGHOST
> 
> PGOPTIONS
> 
> PGPORT
> 
> PGUSER

默认连接参数

PG\_COLOR

规定在诊断消息中是否使用颜色。可能的值为always、 auto、never。

**注释**

因为pg\_dumpall在内部调用pg\_dump，所以， 一些诊断消息可以参考pg\_dump。

即使当用户的目的是把转储脚本恢复到一个空的集簇中，--clean选项也有用武之地。-- clean的使用让该脚本删除并且重建内建的highgo和template1数据库，确保这两个数据库保持与源集簇中相同的属性（例如locale和编码）。如果不用这个选项，这两个数据库将保持它们现有的数据库级属性以及任何已有的内容。

一旦恢复，建议在每个数据库上运行ANALYZE，这样优化器就可以得到有用的统计信息。你也可以运行vacuumdb -a -z来分析所有数据库。

不应该预期转储脚本运行到结束都不出错。特别是由于脚本将为源集簇中已有的每一个角色发出CREATE ROLE语句，对于bootstrap用户当然会得到一个”role already exists”错误，除非目标集簇用一个不同的bootstrap用户名完成的初始化。这种错误是无害的并且应该被忽略。--clean选项的使用很可能会产生额外的有关于不存在对象的无害错误消息，不过可以通过加上--if-exists减少这类错误消息。

pg\_dumpall要求所有需要的表空间目录在进行恢复之前就必须存在；否则，数据库创建就会由于在非默认位置创建数据库而失败。

**示例**

要转储所有数据库：

$ pg\_dumpall > db.out

要从这个文件重新载入数据库，你可以使用：

$ psql -f db.out highgo

这里你连接哪一个数据库并不重要，因为由pg\_dumpall创建的脚本将包含合适的命令来创建和连接到被保存的数据库。一个例外是，如果指定了--clean，则开始时必须连接到highgo数据库，该脚本将立即尝试删除其他数据库，并且这种动作对于已连接上的这个数据库将会失败。

**参见**

可能的错误情况请查看 pg\_dump 。

## pg\_isready

pg\_isready — 检查一个瀚高服务器的连接状态

**命令**

pg\_isready \[connection-option...\] \[option...\]

**描述**

pg\_isready是一个用来检查一个瀚高数据库服务器的连接状态的工具。其退出状态指定了连接检查的结果。

**选项**

\-d dbname

\--dbname=dbname

指定要连接的数据库名。

如果这个参数包含一个=记号或者以一个合法的URI前缀，它会被当作一个conninfo字符串。

\-h hostname

\--host=hostname

指定运行服务器的机器的主机名。如果该值以一个斜线开始，它被用作 Unix 域套接字的目录。

\-p port

\--port=port

指定服务器正在监听连接的 TCP 端口或本地 Unix 域套接字文件扩展。默认值取自PGPORT环境变量。如果环境变量没有设置，则默认值使用编译时指定的端口（通常是5866）。

\-q

\--quiet

不显示状态消息。当脚本编程时有用。

\-t seconds

\--timeout=seconds

尝试连接时，在返回服务器不响应之前等待的最大秒数。设置为 0 则禁用。默认值是 3秒。

\-U username

\--username=username

作为用户username连接数据库，而不是用默认用户。

\-V

\--version

打印pg\_isready版本并退出。

\-?

\--help

显示有关pg\_isready命令行参数的帮助并退出。

**退出状态**

如果服务器正常接受连接，pg\_isready返回0给 shell；如果服务器拒绝连接（例如处于启动阶段）则返回1；如果连接尝试没有被相应则返回2；如果没有尝试（例如由于非法参数）则返回3。

**环境**

和大部分其他数据库工具相似，pg\_isready也使用libpq（见开发手册）支持的环境变量。

环境变量PG\_COLOR规定在诊断消息中是否使用颜色。可能的值为always、auto、never。

**注释**

要获得服务器状态，不一定需要提供正确的用户名、口令或数据库名。不过，如果提供了不正确的值，服务器将会记录一次失败的连接尝试。

**示例**

标准用法：

$ pg\_isready

/tmp:5866 - accepting connections

$ echo $?

0

使用连接参数运行连接到处于启动中的数据库集簇：

$ pg\_isready -h localhost -p 5433

localhost:5433 - rejecting connections

$ echo $?

1

使用连接参数运行连接到无响应的数据库集簇：

$ pg\_isready -h someremotehost

someremotehost:5866 - no response

$ echo $?

2

## pg\_receivewal

pg\_receivewal — 以流的方式从一个瀚高数据库服务得到预写式日志

**命令**

pg\_receivewal \[option...\]

**描述**

pg\_receivewal被用来从一个运行着的瀚高数据库集簇以流的方式得到预写式日志。预写式日志会被使用流复制协议以流的方式传送，并且被写入到文件的一个本地目录。这个目录可以被用作归档位置来做一次使用时间点恢复的恢复。

当预写式日志在服务器上被产生时，pg\_receivewal实时以流的方式传输预写式日志，并且不像archive\_command那样等待段完成。由于这个原因，在使用pg\_receivewal时不必设置archive\_timeout。

与瀚高数据库后备服务器上的 WAL 接收进程不同，pg\_receivewal默认只在一个 WAL文件被关闭时才刷入 WAL 数据。要实时刷入 WAL 数据，必须指定选项--synchronous。

由于pg\_receivewal不应用于WAL，当synchronous\_commit 等于 remote\_apply时，你将不允许它成为同步备用。如果发生这样的情况，它将成为一个永远不能拉起的备用数据库，并且会导致事务提交阻塞。为了避免这种情况，你应该为synchronous\_standby\_names配置一个适当的值，或规定为pg\_receivewal 的application\_name 与它不匹配，或将synchronous\_commit的值更改为remote\_apply以外的内容。

预写式日志在一个常规数据库连接上被以流式传送，并且使用复制协议。连接必须由一个超级用户或一个具有REPLICATION权限的用户建立，并且pg\_hba.conf必须允许复制连接。服务器也必须被配置一个足够高的max\_wal\_senders来至少留出一个可用会话给流。

如果该连接丢失，或者它一开始就由于一个非致命错误而没有被建立，pg\_receivewal将无限期地重试连接并且尽可能重新建立流。为了避免这种行为，使用-n参数。

如果不出现致命错误，pg\_receivewal将一直运行直至被SIGINT信号（Control+C）终止。

**选项**

\-D directory

\--directory=directory

要把输出写到哪个目录。

这个参数是必需的。

\-E lsn

\--endpos=lsn

当接收到达指定的LSN时，自动停止复制并且以正常退出状态0退出。

如果有一个记录的LSN正好等于lsn，则该记录将会被处理。

\--if-not-exists

当指定--create-slot并且具有指定名称的槽已经存在时不要抛出错误。

\-n

\--no-loop

不要在连接错误上循环。相反，碰到一个错误时立刻退出。

\--no-sync

这个选项导致pg\_receivewal不强制WAL数据被刷回磁盘。这样会更快，但是也意味着接下来的操作系统崩溃会让WAL段损坏。通常，这个选项对于测试有用，但不应该在对生产部署进行WAL归档时使用。

这个选项与--synchronous不兼容。

\-s interval

\--status-interval=interval

指定发送回服务器的状态包之间的秒数。这允许我们更容易地监控服务器的进度。一个零值完全禁用这种周期性的状态更新，不过当服务器需要时还是会有一个更新 会被发送来避免超时导致的断开连接。默认值是 10 秒。

\-S slotname

\--slot=slotname

要求pg\_receivewal使用一个已有的复制槽。在使用这个选项时， pg\_receivewal将会报告给服务器一个刷写位置，指示每一个段是何时被同步到磁盘的，这样服务器可以在不需要该段时移除它。

当pg\_receivewal的复制客户端在服务器上被配置为一个同步后备时，那么使用一个复制槽将会向服务器报告刷写位置，但只在一个 WAL 文件被关闭时报告。因此，该配置将导致主服务器上的事务等待很长的时间并且无法令人满意地工作。要让这种配置工作正确，还必须制定选项--synchronous（见下文）。

\--synchronous

在 WAL 数据被收到后立即刷入到磁盘。还要在刷写后立即向服务器回送 一个状态包（不考虑--status-interval）。

如果pg\_receivewal的复制客户端在服务器 上被配置为一个同步后备，应该指定这个选项来确保向服务器发送及时的反馈。

\-v

\--verbose

启用冗长模式。

\-Z level

\--compress=level

启用预写式日志上的gzip压缩，并且指定压缩级别（0到9，0是不压缩而9是最大压缩）。所有的文件名后都将被追加后缀.gz。

下列命令行选项控制数据库连接参数。

\-d connstr

\--dbname=connstr

指定用于连接到服务器的参数为一个连接字符串。

为了和其他客户端应用一致，该选项被称为--dbname。但是因为pg\_receivewal并不连接到集簇中的任何特定数据库，连接字符串中的数据库名将被忽略。

\-h host

\--host=host

指定运行服务器的机器的主机名。如果该值以一个斜线开始，它被用作 Unix 域套接字的目录。默认值取自PGHOST环境变量（如果设置），否则会尝试一个 Unix 域套接字连接。

\-p port

\--port=port

指定服务器正在监听连接的 TCP 端口或本地 Unix 域套接字文件扩展。默认用PGPORT环境变量中的值（如果设置），或者一个编译在程序中的默认值。

\-U username

\--username=username

要作为哪个用户连接。

\--create-slot

用--slot中指定的名称创建一个新的物理复制槽， 然后退出。

\--drop-slot

删除--slot中指定的复制槽，然后退出。

其他选项也可用：

\-V

\--version

打印pg\_receivewal版本并退出。

\-?

\--help

显示有关pg\_receivewal命令行参数的帮助并退出。

**退出状态**

在被SIGINT信号终止（没有正常的方式结束它。因此这不是一种错误）时，pg\_receivewal将以状态0退出。对于致命错误或者其他信号，退出状态将不是零。

**环境**

和大部分其他瀚高数据库工具相似，这个工具也使用libpq（见开发手册）支持的环境变量。

环境变量PG\_COLOR规定在诊断消息中是否使用颜色。可能的值为always、auto、never。

**注释**

在使用pg\_receivewal替代 archive\_command作为主要的 WAL 备份方法时， 强烈建议使用复制槽。否则，服务器可能会在预写式日志文件被备份好之前重用 或者移除它们，因为没有任何信息（不管是来自 archive\_command或是复制槽）能够指示 WAL 流已经被归档到什么程度。不过要注意，如果接收者没有持续地取走 WAL 数据， 一个复制槽将会填满服务器的磁盘空间。

如果在源集簇上启用了组权限，pg\_receivewal将保留接收到的WAL文件上的组权限。

**示例**

要从位于mydbserver的服务器流式传送预写式日志并且将它存储在本地目录/home/highgo/highgo/database/0.0/archive：

$ pg\_receivewal -h mydbserver -D /home/highgo/highgo/database/9.0/archive

**参见**

pg\_basebackup

## pg\_recvlogical

pg\_recvlogical — 控制数据库逻辑解码流

**命令**

pg\_recvlogical \[option...\]

**描述**

pg\_recvlogical控制逻辑解码复制槽以及来自这种复制槽的流数据。

它会创建一个复制模式的连接，因此它受到和pg\_receivewal 相同的约束，还有逻辑复制的约束。

pg\_recvlogical与逻辑解码SQL接口的peek和get模式没有等效性。它在接收到数据以及干净地退出时，会惰性地发送数据的确认。为了检查一个槽上还未应用的待处理数据，可以使用pg\_logical\_slot\_peek\_changes。

**选项**

必须至少要指定下列选项之一来选择一个动作：

\--create-slot

为--dbname指定的数据库用--slot 指定的名称创建一个新的逻辑复制槽，使用 --plugin指定的输出插件。

\--drop-slot

删除名称由--slot指定的复制槽，然后退出。

\--start

从--slot指定的逻辑复制槽开始进行流式传送更改，一直继续到被一个信号终止。如果服务器端关机或者断开连接导致更改流结束，会进入一个循环一直重试，通过指定--no-loop可以防止这种情况下进入循环重试。 流格式由槽创建时指定的输出插件决定。

连接必须是连接到用于创建该槽的同一个数据库上。

\--create-slot和--start可以被一起指定。 --drop-slot不能和另一个动作组合在一起。

下面的命令行选项控制输出的位置和格式以及其他复制行为：

\-E lsn

\--endpos=lsn

在--start模式中，当接收过程到达指定的LSN时会自动地停止复制并且以正常的退出状态0退出。如果不处于--start模式时指定这个选项，则会发生错误。

如果有一个记录的LSN正好等于lsn，则该记录将被输出。

\--endpos不会察觉到事务边界并且可能会在一个事务中间截断输出。任何部分输出的事务都将不会被消费，并且在下一次从该槽中读取时将会重放该事务。单个的消息不会被截断。

\-f filename

\--file=filename

把接收到并且解码好的事务数据写入到一个文件。使用-可以写到stdout。

\-F interval\_seconds

\--fsync-interval=interval\_seconds

指定pg\_recvlogical发出 fsync()调用确保输出文件被安全地刷到磁盘的频度。

服务器将会偶尔要求客户端执行一次刷写并且把刷写位置报告给服务器。 这个设置可以在此之外更加频繁地执行刷写。指定间隔为0会完全禁止发出fsync() 调用，但是仍会报告进度给服务器。在这种情况下，发生崩溃会导致数据丢失。

\-I lsn

> \--startpos=lsn

在--start模式中，从给定的 LSN 开始复制。在其他模式中会忽略这个参数。

\--if-not-exists

当指定--create-slot并且具有指定名称 的槽已经存在时不要抛出错误。

\-n

\--no-loop

当服务器连接丢失时，不要在循环中重试，直接退出。

\-o name\[=value\]

\--option=name\[=value\]

如果指定了输出插件，把选项值value 传递给选项name。存在哪些选项以及它们的效果取决于使用的输出插件。

\-P plugin

\--plugin=plugin

在创建一个槽时使用指定的逻辑解码输出插件。如果该槽已经存在，这个选项没有效果。

\-s interval\_seconds

\--status-interval=interval\_seconds

这个选项和pg\_receivewal中的同名选项具有相同的效果。请参考那里的描述。

\-S slot\_name

\--slot=slot\_name

在--start模式中，使用名为slot\_name 的已有逻辑复制槽。在--create-slot模式中，使用这个名称 创建该槽。在--drop-slot模式中，删除这个名称指定的槽。

\-v

\--verbose

开启详细输出模式。

下列命令行选项控制数据库连接参数。

\-d database

\--dbname=database

要连接的数据库。这个选项的详细含义请见动作的描述。它可以是一个 libpq连接字符串。默认为用户名。

\-h hostname-or-ip

\--host=hostname-or-ip

指定服务器正在运行的机器的主机名。如果该值开始于一个斜线， 它被用作一个 Unix域套接字的目录。默认是从 PGHOST环境变量中取得（如果被设置）， 否则将尝试一次Unix 域套接字连接。

\-p port

\--port=port

指定服务器正在监听连接的 TCP 端口或本地 Unix 域套接字文件扩展名。 默认是放在PGPORT环境变量中（如果被设置）， 否则使用编译在程序中的默认值。

\-U user

\--username=user

要作为哪个用户连接。默认是用当前操作系统用户名。

\-V

\--version

打印pg\_recvlogical的版本并且退出。

\-?

\--help

显示关于pg\_recvlogical命令行参数的帮助，并且退出。

**环境**

和大部分其他数据库工具相似，这个工具也使用libpq（见开发手册）支持的环境变量。

环境变量PG\_COLOR规定在诊断消息中是否使用颜色。可能的值为always、auto、never。

**注释**

如果在源服务器上启用了组权限，pg\_recvlogical将会在接收到的WAL文件上保留组权限。

**参见**

pg\_receivewal

## pg\_restore

pg\_restore — 从一个由pg\_dump创建的归档文件恢复一个瀚高数据库

**命令**

pg\_restore \[connection-option...\] \[option...\] \[filename\]

**描述**

pg\_restore是一个用来从pg\_dump创建的非文本格式归档恢复数据库的工具。它将发出必要的命令把该数据库重建成它被保存时的状态。这些归档文件还允许pg\_restore选择恢复哪些内容或者在恢复前对恢复项重排序。这些归档文件被设计为可以在不同的架构之间迁移。

pg\_restore可以在两种模式下操作。如果指定了一个数据库名称，pg\_restore会连接那个数据库并且把归档内容直接恢复到该数据库中。否则，会创建一个脚本，其中包含着重建该数据库所必要的 SQL 命令，它会被写入到一个文件或者标准输出。这个脚本输出等效于pg\_dump的纯文本输出格式。因此，一些控制输出的选项与pg\_dump的选项类似。

显然，pg\_restore无法恢复不在归档文件中的信息。例如，如果归档使用”以INSERT命令转储数据”选项创建， pg\_restore将无法使用COPY语句装载数据。

**选项**

pg\_restore接受下列命令行参数。

filename

指定要被恢复的归档文件（对于一个目录格式的归档则是目录）的位置。如果没有指定，则使用标准输入。

\-a

\--data-only

只恢复数据，不恢复模式（数据定义）。如果在归档中存在，表数据、大对象和序列值会被恢复。这个选项类似于指定--section=data，但是由于历史原因两者不完全相同。

\-c

\--clean

在重新创建数据库对象之前清除（丢弃）它们（除非使用了--if-exists，如果有对象在目标数据库中不存在，这可能会生成一些无害的错误消息）。

\-C

\--create

在恢复一个数据库之前县创建它。如果还指定了--clean，在连接到目标数据库之前丢弃并且重建它。

如果使用--create，pg\_restore还会恢复数据库的注释（如果有）以及与其相关的配置变量设置，也就是任何提到过这个数据库的ALTER DATABASE... SET...和ALTER

ROLE... IN DATABASE... SET...命令。不管是否指定--no-acl，数据库本身的访问特权都会被恢复。

在使用这个选项时，-d提到的数据库只被用于发出初始的DROP DATABASE和CREATE DATABASE命令。所有要恢复到该数据库名中的数据都出现在归档中。

\-d dbname

\--dbname=dbname

连接到数据库dbname并且直接恢复到该数据库中。

\-e

\--exit-on-error

在发送 SQL 命令到该数据库期间如果碰到一个错误就退出。默认行为是继续并且在恢复结束时显示一个错误计数。

\-f filename

\--file=filename

为生成的脚本指定输出文件，或在与-l选项一起使用时为列表指定输出文件。为 stdout用 -。

\-F format

\--format=format

指定归档的格式。并不一定要指定该格式，因为pg\_restore将会自动决定格式。如果指定，可以是下列之一：

> c
> 
> custom
> 
> 归档是pg\_dump的自定义格式。
> 
> d
> 
> directory
> 
> 归档是一个目录归档。
> 
> t
> 
> tar
> 
> 归档是一个tar归档。
> 
> \-I index

\--index=index

> 只恢复提及的索引的定义。可以通过写多个-I开关指定多个索引。

\-j number-of-jobs

\--jobs=number-of-jobs

使用并发任务运行pg\_restore中最耗时的部分 — 载入数据、创建索引或者创建约束。

对于一个运行在多处理器机器上的服务器，这个选项能够大幅度减少恢复一个大型数据库的时间。

每一个任务是一个进程或者一个线程，这取决于操作系统，它们都使用一个独立的服务器连接。

这个选项的最佳值取决于服务器、客户端以及网络的硬件设置。因素包括 CPU 的核心数和磁盘设置。一个好的建议是服务器上 CPU 的核心数，但是更大的值在很多情况下也能导致更快的恢复时间。当然，过高的值会由于超负荷反而导致性能降低。

这个选项只支持自定义和目录归档格式。输入必须是一个常规文件或目录（例如，不能是一个管道）。当发出一个脚本而不是直接连接到数据库服务器时会忽略这个选项。还有，多任务不能和选项--single-transaction一起用。

\-l

\--list

列出归档的内容的表格。这个操作的输出能被用作-L选项的输入。注意如果把-n或-t这样的过滤开关与-l一起使用，它们将会限制列出的项。

\-L list-file

\--use-list=list-file

只恢复在list-file中列出的归档元素，并且按照它们出现在该文件中的顺序进行恢复。

注意如果把-n或-t这样的过滤开关与-L一起使用，它们将会进一步限制要恢复的项。

list-file通常是编辑一个-l操作的输出来创建。行可以被移动或者移除，并且也可以通过在行首放一个（;）将其注释掉。例子见下文。

\-n shcema

\--schema=schema

只恢复在被提及的模式中的对象。可以用多个-n开关来指定多个模式。这可以与-t选项组合在一起只恢复一个指定的表。

\-N schema

\--exclude-schema=schema

不恢复所提及方案中的对象。可以用多个-N开关指定多个要被排除的方案。如果对同一个方案名称同时给出了-n和-N，则-N会胜出并且该方案会被排除。

\-O

\--no-owner

不要输出将对象的所有权设置为与原始数据库匹配的命令。默认情况下，pg\_restore会发出ALTER OWNER或者SET SESSION AUTHORIZATION语句来设置已创建的模式对象的所有权。除非到该数据库的初始连接是一个超级用户（或者拥有脚本中所有对象的同一个用户）建立的，这些语句将会失败。通过-O，任何用户名都可以被用于初始连接，并且这个用户将会拥有所有被创建的对象。

\-P function-name(argtype \[,...\])

\--function=function-name(argtype \[,...\])

只恢复被提及的函数。要小心地拼写函数的名称和参数使它们正好就是出现在转储文件的内容表中的名称和参数。可以使用多个-P开关指定多个函数。

\-R

\--no-reconnect

这个选项已被废弃，但是出于向后兼容性的目的，系统仍然还接受它。

\-s

\--schema-only

只恢复归档中的模式（数据定义）不恢复数据。

这个选项是--data-only的逆选项。它与指定--section=pre-data --section=post-data相似，但是由于历史原因并不完全相同。（不要把这个选项和--schema选项弄混，后者把词”schema”用于一种不同的含义）。

\-S username

\--superuser=username

指定在禁用触发器时要用的超级用户名。只有使用--disable-triggers时这个选项才相关。

\-t table

\--table=table

只恢复所提及的表的定义和数据。出于这个目的，”table”包括视图、物化视图、序列和外部表。可以写上多个-t开关可以选择多个表。这个选项可以和-n选项结合在一起指定一个特定模式中的表。

| **注意：** |
| --- |
| 在指定-t时，pg\_restore不会尝试恢复所选表可能依赖的任何其他数据库对象。因此，无法确保能成功地把一个特定表恢复到一个干净的数据库中。 |

| **注意：** |
| --- |
| 这个标志的行为和pg\_dump的-t标志不一样。在pg\_restore中当前没有任 何通配符匹配的规定，也不能在其-t选项中包括模式的名称。而且，虽然 pg\_dump的-t标志也会转储选中表的附属对象（例如索引），但是pg\_restore的-t标志不包括这些附属对象。 |

\-T trigger

\--trigger=trigger

只恢复所提及的触发器。可以用多个-T开关指定多个触发器。

\-v

\--verbose

指定冗长模式。

\-V

\--version

打印该pg\_restore的版本并退出。

\-x

\--no-privileges

\--no-acl

阻止恢复访问特权（授予/收回命令）。

\-1

\--single-transaction

将恢复作为单一事务执行（即把发出的命令包裹在BEGIN/COMMIT中）。这可以确保要么所有命令完全成功，要么任何改变都不被应用。这个选项隐含了--exit-on-error。

\--disable-triggers

只有在执行一个只恢复数据的恢复时，这个选项才相关。它指示pg\_restore在装载数据时执行命令临时禁用目标表上的触发器。如果你在表上有参照完整性检查或者其他触发器并且你不希望在数据载入期间调用它们时，请使用这个选项。

目前，为--disable-triggers发出的命令必须以超级用户身份完成。因此你还应该用-S指定一个超级用户名，或者更好的方法是以一个超级用户运行pg\_restore。

\--enable-row-security

只有在恢复具有行安全性的表的内容时，这个选项才相关。默认情况下，pg\_restore将把row\_security设置为 off 来确保所有数据都被恢复到表中。 如果用户不拥有足够绕过行安全性的特权，那么会抛出一个错误。这个参数指示pg\_restore把row\_security设置为on允许用户尝试恢复启用了行安全性的表的内容。如果用户没有从转储向表中插入行的权限，这仍将失败。

注意当前这个选项还要求转储处于INSERT格式，因为COPY FROM不支持行安全性。

\--if-exists

使用条件命令（即增加一个IF EXISTS子句）删除数据库对象。只有指定了--clean时，这个选项才有效。

\--no-comments

即便归档中包含注释也不输出恢复注释的命令。

\--no-data-for-failed-tables

默认情况下，即便表的创建命令失败（例如因为表已经存在），表数据也会被恢复。通过这个选项，对这类表的数据会被跳过。如果目标数据库已经包含了想要的表内容，这种行为又很有有用。例如，数据库扩展（如PostGIS）的辅助表可能已经被载入到目标数据库中，指定这个选项就能阻止把重复的或者废弃的数据载入到这些表中。

只有当直接恢复到一个数据库中时这个选项才有效，在产生 SQL脚本输出时这个选项不会产生效果。

\--no-publications

即便归档中包含publication也不输出恢复publication的命令。

\--no-security-labels

不要输出恢复安全标签的命令，即使归档中包含安全标签。

\--no-subscriptions

即便归档中包含subscription也不输出恢复subscription的命令。

\--no-tablespaces

不输出命令选择表空间。通过这个选项，所有的对象都会被创建在恢复时的默认表空间中。

\--section=sectionname

只恢复提及的小节。小节的名称可以是pre-data、data或者post-data。可以把这个选项指定多次来选择多个小节。默认值是恢复所有小节。

数据小节包含实际的表数据以及大对象定义。Post-data 项由索引定义、触发器、规则和除已验证的检查约束之外的约束构成。Pre-data 项由所有其他数据定义项构成。

\--strict-names

要求每一个模式（-n/--schema）以及表（-t/--table）限定词匹配备份文件中至少一个模式/表。

\--use-set-session-authorization

输出 SQL 标准的SET SESSION AUTHORIZATION命令取代ALTER OWNER命令来决定对象拥有权。这会让转储更加兼容标准，但是依赖于转储中对象的历史，可能无法正确恢复。

\-?

\--help

显示有关pg\_restore命令行参数的帮助，并且退出。

pg\_restore也接受下列用于连接参数的命令行参数：

\-h host

\--host=host

指定服务器正在运行的机器的主机名。如果该值开始于一个斜线，它被用作一个 Unix域套接字的目录。默认是从PGHOST环境变量中取得（如果被设置），否则将尝试一次Unix 域套接字连接。

\-p port

\--port=port

指定服务器正在监听连接的 TCP 端口或本地 Unix 域套接字文件扩展名。默认是放在PGPORT环境变量中（如果被设置），否则使用编译在程序中的默认值。

\-U username

\--username=username

要作为哪个用户连接。

\--role=rolename

指定一个用来创建该转储的角色名。这个选项导致pg\_restore在连接到数据库后发出一个SET ROLE rolename命令。当已认证用户（由-U指定）缺少pg\_restore所需的特权但是能够切换到一个具有所需权利的角色时，这个选项很有用。一些安装有针对直接作为超级用户登录的策略，使用这个选项可以让转储在不违反该策略的前提下完成。

**环境**

> PGHOST
> 
> PGOPTIONS
> 
> PGPORT
> 
> PGUSER

默认连接参数

PG\_COLOR

规定在诊断消息中是否使用颜色。可能的值为always、 auto、never。 never.

**诊断**

当使用-d选项指定一个直接数据库连接时，pg\_restore在内部执行SELECT语句。如果你运行pg\_restore时出现问题，确定你能够从正在使用的数据库中选择信息，例如psql。此外，libpq前端-后端库所使用的任何默认连接设置和环境变量都将适用。

**注释**

如果你的数据库集簇对于template1数据库有任何本地添加，要注意将pg\_restore的输出载入到一个真正的空数据库。否则你很可能由于以增加对象的重复定义而得到错误。要创建一个不带任何本地添加的空数据库，从template0而不是template1复制它，例如：

CREATE DATABASE foo WITH TEMPLATE template0;

下面将详细介绍pg\_restore的局限性。

• 在恢复数据到一个已经存在的表中并且使用了选项--disable-triggers时，pg\_restore会在插入数据之前发出命令禁用用户表上的触发器，然后在完成数据插入后重新启用它们。

如果恢复在中途停止，可能会让系统目录处于错误的状态。

• pg\_restore不能有选择地恢复大对象，例如只恢复特定表的大对象。如果一个归档包含大对象，那么所有的大对象都会被恢复，如果通过-L、-t或者其他选项进行了排除，它们一个也不会被恢复。

一旦完成恢复，应该在每一个被恢复的表上运行ANALYZE，这样优化器能得到有用的统计信息。

**示例**

假设我们已经以自定义格式转储了一个叫做mydb的数据库：

$ pg\_dump -Fc mydb > db.dump

要删除该数据库并且从转储中重新创建它：

$ dropdb mydb

$ pg\_restore -C -d highgo db.dump

\-d开关中提到的数据库可以是任何已经存在于集簇中的数据库，pg\_restore只会用它来为mydb发出CREATE DATABASE命令。通过-C，数据总是会被恢复到出现在归档文件的数据库名中。

要把转储重新载入到一个名为newdb的新数据库中：

$ createdb -T template0 newdb

$ pg\_restore -d newdb db.dump

注意我们不使用-C，而是直接连接到要恢复到其中的数据库。还要注意我们是从template0而不是template1创建了该数据库，以保证它最初是空的。

要对数据库项重排序，首先需要转储归档的表内容：

$ pg\_restore -l db.dump > db.list

列表文件由一个头部和一些行组成，这些行每一个都用于一个项，例如：

;

; Archive created at Mon Sep 14 13:55:39 2009

; dbname: DBDEMOS

; TOC Entries: 81

; Compression: 9

; Dump Version: 1.10-0

; Format: CUSTOM

; Integer: 4 bytes

; Offset: 8 bytes

; Dumped from database version: 8.3.5

; Dumped by pg\_dump version: 8.3.8

;

;

; Selected TOC Entries:

;

3; 2615 2200 SCHEMA - public pasha

1861; 0 0 COMMENT - SCHEMA public pasha

1862; 0 0 ACL - public pasha

317; 1247 17715 TYPE public composite pasha

319; 1247 25899 DOMAIN public domain0 pasha

分号表示开始一段注释，行首的数字表明了分配给每个项的内部归档 ID。

文件中的行可以被注释掉、删除以及重排序。例如：

10; 145433 TABLE map\_resolutions highgo

;2; 145344 TABLE species highgo

;4; 145359 TABLE nt\_header highgo

6; 145402 TABLE species\_records highgo

;8; 145416 TABLE ss\_old highgo

把这样一个文件作为pg\_restore的输入将会只恢复项10和6，并且先恢复10再恢复6。

$ pg\_restore -L db.list db.dump

**参见**

pg\_dump, pg\_dumpall, psql

## pg\_verifybackup

pg\_verifybackup — 验证瀚高数据库基础备份的完整性。

**命令：**

pg\_verifybackup \[option...\]

**描述：**

pg\_verifybackup用于根据备份时服务器生成的backup\_manifest检查使用pg\_basebackup进行的数据库群集备份的完整性。备份必须以”普通”格式存储；”tar”格式的备份可以在解压缩后进行检查。

需要注意的是，由pg\_verifybackup执行的验证不包括也不可能包括运行中的服务器在尝试使用备份时执行的所有检查。 即使使用此工具，也应执行测试还原，并验证生成的数据库是否按预期工作，以及它们是否包含正确的数据。但是，pg\_verifybackup可以检测到由于存储问题或用户错误而经常出现的许多问题。

备份验证分四个阶段进行。首先，pg\_verifybackup读取backup\_manifest文件。如果该文件不存在、无法读取、格式不正确或无法根据其内部校验和进行验证，pg\_verifybackup 将以致命错误终止。

其次，pg\_verifybackup 将尝试验证当前存储在磁盘上的数据文件是否与服务器打算发送的数据文件完全相同，下面将介绍一些例外情况。 除了少数例外，额外和丢失的文件将被检测到。此步骤将忽略 postgresql.auto.conf、standby.signal 和 recovery.signal 的存在与否或对其的任何修改，因为预计这些文件可能是在备份过程中创建或修改的。它也不会抱怨目标目录中的 backup\_manifest 文件或 pg\_wal 中的任何内容，即使这些文件不会列在备份清单中。只检查文件；不验证目录的存在与否，除非间接验证：如果目录丢失，则它应该包含的任何文件也必然会丢失。

接下来，pg\_verifybackup将对所有文件进行校验和计算，将校验和与清单中的值进行比较，并对计算出的校验和与清单中存储的校验和不匹配的任何文件发出错误。对于在上一步中产生错误的任何文件，不执行此步骤，因为已知这些文件存在问题。在上一步中被忽略的文件在此步骤中也被忽略。

最后，pg\_verifybackup 将使用清单来验证恢复备份所需的预写式日志记录是否存在，并且它们可以被读取和解析。 backup\_manifest 包含有关需要哪些预写式日志记录的信息，并且 pg\_verifybackup 将使用该信息来调用 pg\_waldump 来解析这些预写式日志记录。 --quiet 标志将被使用，因此 pg\_waldump 只会报告错误，而不会产生任何其他输出。虽然这种级别的验证足以检测明显的问题，例如丢失的文件或内部校验和不匹配的问题，但它们还不足以检测尝试恢复时可能出现的所有问题。例如，此方法无法检测到产生具有正确校验和但指定无意义操作的预写式日志记录的服务器错误。

请注意，如果存在不需要恢复备份的额外 WAL 文件，则此工具不会检查它们，尽管可以为此使用单独的 pg\_waldump 调用。另请注意，WAL 验证是特定于版本的：您必须使用 pg\_verifybackup 的版本，因此是 pg\_waldump 的版本，它与正在检查的备份有关。 相比之下，数据文件完整性检查应适用于生成 backup\_manifest 文件的任何版本的服务器。

**选项：**

pg\_verifybackup 接受以下命令行参数：

\-e

\--exit-on-error

检测到备份问题后立即退出。 如果没有指定这个选项，pg\_verifybackup 将在检测到问题后继续检查备份，并将检测到的所有问题报告为错误。

\-i path

\--ignore=path

在将备份中实际存在的数据文件列表与 backup\_manifest 文件中列出的数据文件列表进行比较时，忽略指定的文件或目录，该文件或目录应表示为相对路径名。如果指定了目录，则此选项会影响以该位置为根的整个子树。 如果相对路径名与指定的路径名匹配，有关额外文件、丢失文件、文件大小差异或校验和不匹配的投诉将被抑制。 可以多次指定此选项。

\-m path

\--manifest-path=path

使用指定路径的清单文件，而不是位于备份目录根目录中的清单文件。

\-n

\--no-parse-wal

不要试图解析从该备份恢复所需的预写式日志数据。

\-q

\--quiet

成功验证备份后不要打印任何内容。

\-s

\--skip-checksums

不要验证数据文件校验和。但仍检查是否存在文件以及这些文件的大小。这样将会快得多，因为文件本身不需要读取。

\-w path

\--wal-directory=path

尝试解析存储在指定目录中的 WAL 文件，而不是 pg\_wal。 如果备份存储在与WAL存档不同的位置，则这可能很有用。

其他选项也可用：

\-V

\--version

打印 pg\_verifybackup 版本并退出。

\-?

\--help

显示有关pg\_verifybackup命令行参数的帮助，然后退出

**示例：**

要在 mydbserver 上创建服务器的基本备份并验证备份的完整性：

$ pg\_basebackup -h mydbserver -D /usr/local/pgsql/data

$ pg\_verifybackup /usr/local/pgsql/data

要在 mydbserver 上创建服务器的基本备份，请将清单移动到备份目录之外的某个位置，并验证备份：

$ pg\_basebackup -h mydbserver -D /usr/local/pgsql/backup1234

$ mv /usr/local/pgsql/backup1234/backup\_manifest /my/secure/location/backup\_manifest.1234

$ pg\_verifybackup -m /my/secure/location/backup\_manifest.1234 /usr/local/pgsql/backup1234

要在忽略手动添加到备份目录的文件的同时验证备份，并跳过校验和验证：

$ pg\_basebackup -h mydbserver -D /usr/local/pgsql/data

$ edit /usr/local/pgsql/data/note.to.self

$ pg\_verifybackup --ignore=note.to.self --skip-checksums /usr/local/pgsql/data

## psql

psql — 数据库的交互式终端

**命令**

psql \[option...\] \[dbname \[username\]\]

**描述**

psql是一个瀚高数据库的基于终端的前端。它让你能交互式地键入查询，把它们发送给数据库，并且查看查询结果。或者，输入可以来自于一个文件或者命令行参数。此外，psql还提供一些元命令和多种类似 shell 的特性来为编写脚本和自动化多种任务提供便利。

**选项**

\-a

\--echo-all

把所有非空输入行按照它们被读入的形式打印到标准输出（不适用于交互式行读取）。

这等效于把变量ECHO设置为 all。

\-A

\--no-align

切换到非对齐输出模式（默认输出模式是对齐的）。这等效于\\pset format unaligned。

\-b

\--echo-errors

把失败的 SQL 命令打印到标准错误输出。这等效于把变量ECHO设置为errors。

\-c command

\--command=command

指定psql执行一个给定的命令字符串command。这个选项可以重复多次并且以任何顺序与-f选项组合在一起。当-c或者-f被指定时，psql不会从标准输入读取命令，直到它处理完序列中所有的-c和-f选项之后终止。

command必须是一个服务器完全可解析的命令字符串（即不包含psql相关的特性）或者单个反斜线命令。因此不能在一个-c选项中混合SQL和psql元命令。要那样做，可以使用多个-c选项或者把字符串用管道输送到psql中，例如：

psql -c '\\x' -c 'SELECT \* FROM foo;'

> 或者

echo '\\x \\\\ SELECT \* FROM foo;' | psql

（\\\\是分隔符元命令）。

每一个被传递给-c的SQL命令字符串会被当做一个单独的请求发送给服务器。因此，即便该字符串包括多个SQL命令，服务器也会把它当做一个事务来执行，除非在该字符串中有显式的BEGIN/COMMIT命令把它划分成多个事务。此外，psql只会打印出该字符串中最后一个SQL命令的结果。这和从文件中读取同一字符串或者把同一字符串传给psql的标准输出时的行为不同，因为那两种情况下psql会独立地发送每一个SQL命令。

由于这种行为，把多于一个SQL命令放在-c字符串中通常会得到意料之外的结果。最好使用多个-c命令或者把多个命令输送给psql的标准输入，按照上文所说的使用echo或者通过一个 shell，例如：

psql <<EOF

\\x

SELECT \* FROM foo;

EOF

\--csv

切换到CSV（逗号分隔值）输出模式。 这相当于\\pset format csv。

\-d dbname

\--dbname=dbname

指定要连接的数据库的名称。这等效于指定dbname为命令行上的第一个非选项参数。

如果这个参数包含一个=符号或者以一个合法的URI前缀开始，它会被当作一个conninfo字符串。

\-e

\--echo-queries

也把发送到服务器的所有 SQL 命令复制到标准输出。这等效于把变量ECHO设置为queries。

\-E

\--echo-hidden

回显\\d以及其他反斜线命令生成的实际查询。可以用它来学习psql的内部操作。这等效于把变量ECHO\_HIDDEN设置为on。

\-f filename

\--file=filename

从文件filename而不是标准输入中读取命令。这个选项可以被重复多次，也可以以任意顺序与-c选项组合。当-c或者-f被指定时，psql不会从标准输入读取命令，直到它处理完序列中所有的-c和-f选项之后终止。除此以外，这个选项很大程度上等价于元命令\\i。

如果filename是-（连字符），那么会读取标准输入直到遇见一个 EOF 指示或者\\q元命令。这种方式可以用把自多个文件的输入组合成一种交互式输入。不过注意在这种情况下不会使用 Readline（很像指定了-n的情况）。

使用这个选项与psql < filename有细微的不同。通常，两种形式都可以做到我们所期望的，但是使用-f启用了一些好的特性，例如带有行号的错误消息。使用这个选项还有一丝机会可以降低启动开销。在另一方面，使用 shell输入重定向的变体（理论上）保证会得到与手工输入时相同的输出。

\-F separator

\--field-separator=separator

使用separator作为非对齐输出的域分隔符。这等效于\\pset fieldsep或者\\f。-h hostname

\--host=hostname

指定运行服务器的机器的主机名。如果这个值由一个斜线开始，它会被用作 Unix 域套接字的目录。

\-H

\--html

切换到HTML输出模式。这等效于\\pset format html或者\\H命令。

\-l

\--list

列出所有可用的数据库，然后退出。其他非连接选项会被忽略。这与元命令\\list类似。

在使用这个选项时，psql将连接到数据库highgo，除非在命令行上提及一个不同的数据（选项-d或非选项参数，可能是通过一个服务项，但不能通过一个环境变量）。

\-L filename

\--log-file=filename

除了把所有查询输出写到普通输出目标之外，还写到文件filename中。

\-n

\--no-readline

不使用Readline做行编辑并且不使用命令历史。在剪切和粘贴时，关掉 Tab 展开会有所帮助。

\-o filename

\--output=filename

把所有查询输出放到文件filename中。这等效于命令\\o。

\-p port

\--port=port

指定服务器用于监听连接的 TCP 端口或者本地 Unix 域套接字文件扩展。默认是PGPORT环境变量的值，如果没有设置，则默认为编译时指定的端口号（通常是5866）。

\-P assignment

\--pset=assignment

以\\pset的形式指定打印选项。注意，这里你必须用一个等号而不是空格来分隔名称和值。例如，要设置输出格式为LaTeX，应该写成-P format=

latex。

\-q

\--quiet

指定psql应该安静地工作。默认情况下，它会打印出欢迎消息以及多种输出。如果使用了这个选项，以上那些就都不会输出。在使用-c选项时，配合这个选项很有用。这等效于设置变量QUIET为on。

\-R separator

\--record-separator=separator

把separator用作非对齐输出的记录分隔符。这等效于\\pset recordsep命令。

\-s

\--single-step

运行在单步模式中。这意味着在每个命令被发送给数据库服务之前都会提示用户一个可以取消执行的选项。使用这个选项可以调试脚本。

\-S

\--single-line

运行在单行模式中，其中新行会终止一个 SQL 命令，就像分号的作用一样。

| **注意：** |
| --- |
| 这种模式被提供给那些坚持使用它的用户，但是并不一定要使用它。特别地，如果在一行中混合了SQL和元命令，那对于没有经验的用户来说，它们的执行顺序可能不总是那么清晰。 |

\-t

\--tuples-only

关闭打印列名和结果行计数页脚等。这等效于\\t或者\\pset tuples\_only命令。

\-T table\_options

\--table-attr=table\_options

指定要替换HTML table标签的选项。详见\\pset tableattr。

\-U username

\--username=username

作为用户username而不是默认用户连接到数据库（当然，你必须具有这样做的权限）。

> \-v assignment
> 
> \--set=assignment
> 
> \--variable=assignment

执行一次变量赋值，和\\set元命令相似。注意你必须在命令行上用等号分隔名字和值（如果有）。要重置一个变量，去掉等号就行。要把一个变量置为空值，使用等号但是去掉值。这些赋值在命令行处理期间被完成，因此反映连接状态的变量将在稍后被覆盖。

> \-V
> 
> \--version

打印psql版本并且退出。

> \-x
> 
> \--expanded

打开扩展表格式模式。这等效于\\x或者\\pset expanded命令。

> \-X,
> 
> \--no-psqlrc

不读取启动文件（要么是系统范围的psqlrc文件，要么是用户的~/.psqlrc文件）。

> \-z
> 
> \--field-separator-zero

设置非对齐输出的域分隔符为零字节。这等效于\\pset fieldsep\_zero。

> \-0
> 
> \--record-separator-zero

设置非对齐输出的记录分隔符为零字节。例如，这对与xargs -0配合有关。这等效于\\pset recordsep\_zero。

> \-1
> 
> \--single-transaction

这个选项只能被用于与一个或者多个-c以及/或者-f选项组合。它会让psql在第一个上述选项之前发出一条BEGIN命令并且在最后一个上述选项之后发出一条COMMIT命令，这样就把所有的命令都包裹在一个事务中。这个选项可以保证要么所有的命令都成功地完成，要么不应用任何更改。

如果命令本身包含BEGIN、COMMIT或者ROLLBACK，这个选项将不会得到想要的效果。还有，如果当个命令不能在一个事务块中执行，指定这个选项将导致整个事务失败。

> \-?

\--help\[=topic\]

显示有关psql的帮助并且退出。可选的topic参数（默认为options）选择要解释哪一部分的psql：commands描述psql的反斜线命令；options描述可以被传递给psql的命令行选项；而variables则显示有关psql配置变量的帮助。

**退出状态**

如果psql正常完成，它会向 shell 返回 0。如果它自身发生一个致命错误（例如内存用完、找不到文件），它会返回 1。如果到服务器的连接出问题并且事务不是交互式的，它会返回2。如果在脚本中发生错误，它会返回3并且变量ON\_ERROR\_STOP会被设置。

**用法**

- 连接到数据库

psql是一个常规瀚高数据库客户端应用。为了连接到数据库，你需要知道你的目标数据库的名称、主机名和该服务器的端口号，还有要作为哪个用户名连接。可以通过命令行选项告知psql这些参数，分别是-d、-h、-p以及-U。如果发现一个参数不属于任何选项，它将被解释。

为数据库名称（如果已经给出数据库名称，就解释为用户名）。并非所有这些选项都是必需的，它们都有可用的默认值。如果省略主机名，psql将通过一个 Unix 域套接字连接到本地主机上的服务器，或者通过 TCP/IP 连接到没有 Unix 域套接字的主机上的localhost。默认端口号是5866。默认的用户名是你的操作系统用户名，它也会是默认的数据库名。注意你不一定能连接到任意用户名下的任何数据库。

当默认值不是很符合实际时，可以把环境变量PGDATABASE、PGHOST、PGPORT以及PGUSER设置为适当的值。用一个~/.pgpass文件来避免定期输入密码也很方便。

另一种指定连接参数的方法是用一个conninfo字符串或者一个URI，它可以被用来替代数据库名。这种机制可以让我们对连接具有很广的控制权。例如：

$ psql "service=myservice sslmode=require"

用这种方式，你也可以把LDAP用于开发手册第一章中描述的连接参数查找。可用连接选项的更多信息请见开发手册第一章节的内容。

如果由于任何原因（例如权限不足、服务器没有在目标主机上运行等）导致连接无法建立，psql将返回一个错误并且终止。

如果标准输入和标准输出都是一个终端，那么psql会把客户端编码设置成”auto”，这会使psql从区域设置（Unix 系统上的LC\_CTYPE环境变量）中检测合适的客户端编码。如果这样不起作用，可以使用环境变量PGCLIENTENCODING覆盖客户端编码。

- 输入 SQL 命令

在正常操作时，psql会提供一个提示符，该提示符是psql当前连接到的数据库名称后面跟上字符串=>。例如： testdb=> 。

在提示符下，用户可以键入SQL命令。正常情况下，当碰到一个表示命令终结的分号时，输入的行会被发送给服务器。一行的结束并不表示命令的完结。因此，为了清晰，可以把命令散布在多个行上。如果命令被发送并且执行而不产生错误，该命令的结果将会显示在屏幕上。

如果不可信用户对还没有采用安全方案使用模式的一个而数据库拥有访问，通过从search\_path移除公共可写的方案来开始你的会话。人们可以在连接字符串中加入options=-csearch\_path=或者在其他SQL命令之前发出SELECT

pg\_catalog.set\_config('search\_path', '', false)。这种考虑并非专门针对psql，它适用于每一种执行任意SQL命令的接口。

只要执行命令，psql还会测试LISTEN和NOTIFY产生的异步通知。

虽然 C 风格的注释块会被传给服务器处理并且移除，psql会自己移除掉 SQL 标准的注释。

- 元命令

你输入到psql中的任何以未加引用的反斜线开始的东西都是一个psql元命令，它们由psql自行处理。这些命令让psql对管理和编写脚本更有用。元命令常常被称作斜线或者反斜线命令。

psql命令的格式是用反斜线后面直接跟上一个命令动词，然后是一些参数。参数与命令动词和其他参数之间用任意多个空白字符分隔开。

要在一个参数中包括空白，可以将它加上单引号。要在一个参数中包括一个单引号，则需要在文本中写上两个单引号。任何包含在单引号中的东西都服从与 C 语言中\\n（新行）、\\t（制表符）、\\b（退格）、\\r（回车）、\\f（换页）、\\digits（10 进制）以及\\xdigits（16 进制）类似的替换规则。单引号内文本中的其他任何字符（不管它是什么）前面的反斜线都没有实际意义（会被忽略）。

如果在一个参数中出现一个未加引号的冒号（:）后面跟着一个psql变量名，它会被该变量的值替换，如SQL中插入变量中所述。在其中描述的形

式:'variable\_name'和:"variable\_name"也有同样的效果。:{?variable\_name}语法允许测试一个变量是否被定义。它会被TRUE或FALSE替换。用一个反斜线转义该冒号可以防止它被替换。

在一个参数中，封闭在反引号（\`）中的文本会被当做一个传递给shell的命令行。该命令的输出（移除任何拖尾的新行）会替换反引号文本。在封闭在反引号的文本中，不会有特别的引号或者其他处理发生，:variable\_name的出现除外，其中variable\_name是一个会被其值替换的psql变量名。此外，Also, appearances of:'variable\_name'的出现会被替换为该变量的值，而值会被适当地加以引用以变成一个单一shell命令参数（后一种形式几乎总是优先，除非你非常确定变量中有什么）。因为回车和换行字符在所有的平台上都不能被安全地引用。

:'variable\_name'形式会打印一个错误消息并且在这类字符出现在值中时不替换该变量值。

有些命令把SQL标识符（例如一个表名）当作参数。这些参数遵循SQL的语法规则：无引号的字母被强制变为小写，而双引号（"）可以保护字母避免大小写转换并且允许在标识符中包含空白。在双引号内，成对的双引号会被缩减为结果名称中的单个双引号。例如，FOO"BAR"BAZ会被解释成fooBARbaz，而"A weird"" name"会变成A weird" name。

对参数的解析会在行尾或者碰到另一个未加引号的反斜线时停止。一个未加引号的反斜线被当做新元命令的开始。特殊的序列\\\\（两个反斜线）表示参数结束并且应继续解析SQL命令（如果还有）。使用这种方法，SQL命令和psql命令可以被自由地混合在一行中。但是无论在何种情况中，元命令的参数都无法跨越一行。

很多元命令作用在当前查询缓冲区上。这就是一个缓冲区而已，它保存任何已经被键入但是还没有发送到服务器执行的SQL命令文本。这将包括之前输入的行以及在该元命令同一行上出现在前面的任何文本。

可以使用下列元命令：

\\a

如果当前的表输出格式是非对齐的，则切换成对齐格式。如果不是非对齐格式，则设置成非对齐格式。保留这个命令是为了向后兼容性。更一般的方案请见\\pset。

\\c or \\connect \[ -reuse-previous=on|off \] \[ dbname \[ username \] \[ host \] \[ port

\] | conninfo \]

与一个数据库服务建立一个新连接。可以使用位置语法指定要使用的连接参数，或者使用开发手册第一章节中详细介绍的conninfo连接串。

在省略了数据库名、用户、主机或者端口的命令中，新的连接将会重用之前一个连接的值。默认情况下，前一个连接的值将会被重用，除非给出了一个conninfo串。给出第一个参数-reuse-previous=on或者-reuse-previous=off可以覆盖默认行为。当这个命令既没有指定一个参数也没有重用它时，将使用libpq的默认值。

把dbname、username、host或者port中的任何一个指定为-等价于省略该参数。

如果新连接成功地被建立，之前的连接会被关闭。如果连接尝试失败（错误的用户名、访问被拒绝等），只有在psql处于交互模式的情况下才会保留之前的连接。当执行一个非交互式脚本时出现连接尝试失败，处理将被立即停止，并且报出一个错误。这种区别一方面可以帮助用户发现打字错误，另一方面也可以作为一种安全机制防止脚本在错误的数据库上执行动作。

例子：

\=> \\c mydb myuser host.dom 6432

\=> \\c service=foo

\=> \\c "host=localhost port=5866 dbname=mydb connect\_timeout=10

sslmode=disable"

\\C \[ title \]

设置查询结果的任何表的标题，或者重置这类标题。这个命令等效于\\pset title title（这个命令的名称来自于”caption”，因为它之前只被用来在HTML表格中设置标题）。

\\cd \[ directory \]

把当前工作目录改为directory。如果不带参数，则切换到当前用户的主目录。

| 提示： |
| --- |
| 要打印当前的工作目录，可以使用\\! pwd。 |

\\conninfo

输出有关当前数据库连接的信息。

\\copy { table \[ ( column\_list ) \] | ( query ) } { from | to } { 'filename' | program

'command' | stdin | stdout | pstdin | pstdout } \[ \[ with \] ( option \[,...\] ) \]

执行一次前端拷贝。这个操作会运行一个SQL COPY命令，不过不是服务器读取或者写入指定的文件，而是由psql读写文件并且把数据从本地文件系统导向服务器。这意味着文件的可访问性和权限是本地用户的而非服务器上的，并且不需要 SQL 超级用户特权。

当program被指定时，command被psql执行并且传给command的数据或者从command传出的数据会在服务器和客户端之间流动。同样地，执行特权是本地用户的而非服务器上的，并且不需要 SQL 超级用户特权。

对于\\copy... from stdin，数据行从发出该命令的同一来源读取，一直到读到\\.或者数据流到达EOF。这个选项可以用来填充内嵌在一个 SQL 脚本文件中的表。对于\\copy... to stdout，输出被发送到与psql命令输出相同的位置，并且COPY count命令的状态不会被打印（因为它会被一个数据行搞乱）。要读/写psql的标准输入或者输出而不管当前命令的来源或者\\o选项，可以写from pstdin或者to pstdout。

这个命令的语法和SQL COPY命令类似。所有除开数据来源/目的地的选项都和COPY指定的一样。因此，\\copy元命令由特殊的解析规则。与大部分其他元命令不同，该行的所有剩余部分总是会被当做\\copy的参数，并且在参数中不会执行变量篡改以及反引号展开。

| 提示： |
| --- |
| 获得与\\copy... to相同结果的另一种方法是使用SQL COPY... TO STDOUT 命令并使用\\g filename或\\ g \|program 终止它。与 \\copy不同，此方法允许命令跨越多行; 此外，可以使用变量插值和反引号扩展。 |

| 提示： |
| --- |
| 这些操作不如带有文件或程序数据源或目标的SQL COPY命令有效， 因为所 有数据都必须通过客户端/服务器连接。 对于大量数据，SQL命令可能更可取。 |

\\copyright

显示数据库的版权以及发布条款。

\\crosstabview \[ colV \[ colH \[ colD \[ sortcolH \] \] \] \]

执行当前的查询缓冲区（像\\g那样）并且在一个交叉表格子中显示结果。该查询必须返回至少三列。由colV标识的输出列会成为垂直页眉并且colH所标识的输出列会成为水平页眉。colD标识显示在格子中的输出列。sortcolH标识用于水平页眉的可选的排序列。

每一个列说明可以是一个列编号（从1开始）或者一个列名。常用的 SQL 大小写折叠和引用规则适用于列名。如果省略，colV被当做列 1 并且colH被当做列 2。colH必须和colV不同。如果没有指定colD，那么在查询结果中必须正好有三列，并且colV和colH之外的那一列会被当做colD。

垂直页眉显示为最左边的列，它包含列colV中找到的值，值的顺序和查询结果中的顺序相同，但是重复值会被移除。

水平页眉显示为第一行，它包含列colH中找到的值，其中的重复值被移除。默认情况下，这些值会以查询结果中相同的顺序出现。但是如果给出了可选的sortcolH参数，它标识一个值必须为整数编号的列，并且来自colH的值 将会根据相应的sortcolH值排序后出现在水平页眉中。

在交叉表格子中，对于colH的每一个可区分的值x以及colV的每一个可区分的值y，位于交叉点(x,y)的单元包含colH值为x且colV值为y的查询结果行中colD列的值。如果没有这样的行，则该单元为空。如果有多个这样的行，则会报告一个错误。

\\d\[S+\] \[ pattern \]

对于每一个匹配pattern的关系（表、视图、物化视图、索引、序列或者外部表）或者组合类型，显示所有的列、它们的类型、表空间（如果非默认表空间）以及任何诸如NOT NULL或者默认值的特殊属性。相关的索引、约束、规则以及触发器也会被显示。对于外部表，还会显示相关的外部服务器（下文的模式（Pattern）中定义了”匹配模式”）。

对于某些类型的关系，\\d会为每一列显示额外的信息：对于序列会显示列值，对于索引显示被索引的表达式，对于外部表显示外部数据包装器选项。

命令形式\\d+是一样的，不过会显示更多信息：与该表的列相关的任何注释，表中是否存在 OID，如果关系是视图则显示视图定义，非默认的replica identity设置。

默认情况下只会显示用户创建的对象，提供一个模式或者S修饰符可以把系统对象包括在内。

| 注意： |
| --- |
| 如果使用\\d但不带有pattern参数，它等价于\\dtvmsE，后者将显示所有可见的表、视图、物化视图、序列和外部表的列表。这纯粹是一种便利措施。 |

\\da\[S\] \[ pattern \]

列出聚集函数，以及它们的返回类型和它们所操作的数据类型。如果指定了pattern，只显示名称匹配该模式的聚集。默认情况下只会显示用户创建的对象，提供一个模式或者S修饰符可以把系统对象包括在内。

\\dA\[+\] \[ pattern \]

列出访问方法。如果指定了pattern，只显示名称匹配该模式的访问方法。如果在命令名称后面追加+，则与访问方法相关的处理器函数和描述也会和访问方法本身一起被列出。

\\db\[+\] \[ pattern \]

列出表空间。如果指定了pattern，只显示名称匹配该模式的表空间。如果在命令名称后面追加+，则与表空间相关的选项、磁盘上的尺寸、权限以及描述也会和表空间本身一起被列出。

\\dc\[S+\] \[ pattern \]

列出字符集编码之间的转换。如果指定了pattern，只列出名称匹配该模式的转换。默认情况下只会显示用户创建的对象，提供一个模式或者S修饰符可以把系统对象包括在内。

如果在命令名称后面追加+，则每一个对象相关的描述也会被列出。

\\dC\[+\] \[ pattern \]

列出类型转换。如果指定了pattern，只列出源类型和目标类型匹配该模式的转换。如果在命令名称后面追加+，则每一个对象相关的描述也会被列出。

\\dd\[S\] \[ pattern \]

显示约束、操作符类、操作符族、规则以及触发器类型对象的描述。所有其他注释可以通过那些对象类型相应的反斜线命令查看。

\\dd显示匹配pattern的对象的描述，如果没有给出参数则显示合适类型的可见对象的描述。但是在任一种情况下都只列出具有描述的对象。默认情况下只会显示用户创建的对象，提供一个模式或者S修饰符可以把系统对象包括在内。

对象的描述可以用SQL命令COMMENT创建。

\\dD\[S+\] \[ pattern \]

列出域。如果指定了pattern，只有名称匹配该模式的域会被显示。默认情况下，只有用户创建的对象会被显示，可以提供一个模式或者S修饰符以包括系统对象。如果+被追加到命令名称上，每一个被列出的对象会带有其相关的权限和描述。

\\ddp \[ pattern \]

列出默认的访问特权设置。对那些默认特权设置已经被改变得与内建默认值不同的角色（以及模式，如果适用），为每一个角色（以及模式）显示一项。如果指定了pattern，只列出角色名称或者模式名称匹配该模式的项。

ALTER DEFAULT PRIVILEGES命令被用来设置默认访问特权。在第 5.7 节中解释了显示的特权的含义。

\\dE\[S+\] \[ pattern \]

\\di\[S+\] \[ pattern \]

\\dm\[S+\] \[ pattern \]

\\ds\[S+\] \[ pattern \]

\\dt\[S+\] \[ pattern \]

\\dv\[S+\] \[ pattern \]

在这一组命令中，字母E、i、m、s、t和v分别对应着外部表、索引、物化视图、序列、表和视图。你可以以任何顺序指定这些字母中的任意一个或者多个，这样可以得到这些类型的对象的列表。例如，\\dit会列出索引和表。如果在命令名称后面追加+，则每一个对象的物理尺寸以及相关的描述也会被列出。如果指定了pattern，只列出名称匹配该模式的对象。默认情况下只会显示用户创建的对象，提供一个模式或者S修饰符可以把系统对象包括在内。

\\des\[+\] \[ pattern \]

列出外部服务器（助记：”外部服务器”）。如果指定了pattern，只列出名称匹配该模式的那些服务器。如果使用了\\des+形式，将显示每个服务器的完整描述，包括该服务器的访问特权、类型、版本、选项和描述。

\\det\[+\] \[ pattern \]

列出外部表（助记：”外部表”）。如果指定了pattern，只列出表名称或者模式名称匹配该模式的项。如果使用了\\det+选项，一般选项和外部表描述也会被显示。

\\deu\[+\] \[ pattern \]

列出用户映射（助记：”外部用户”）。如果指定了pattern，只列出用户名匹配该模式的那些映射。如果使用了\\deu+形式，有关每个映射的额外信息也会被显示。

| 注意： |
| --- |
| \\deu+可能也会显示远程用户的用户名和口令，所以要小心不要把它们泄露出去。 |

\\dew\[+\] \[ pattern \]

列出外部数据包装器（助记：”外部包装器”）。如果指定了pattern，只列出名称匹配该模式的那些外部数据包装器。如果使用了\\dew+形式，外部数据包装器的访问特权、选项和描述也会被显示。

\\df\[anptwS+\] \[ pattern \]

列出函数，以及它们的结果数据类型、参数数据类型和函数类型，函数类型被分为”agg”（聚集）、”normal”、”procedure”、”trigger”以及”window”。如果要只显示指定类型的函数，可以在该命令上增加相应的字母a、n、p、t或者w。如果指定了pattern，只显示名称匹配该模式的函数。默认情况下只会显示用户创建的对象，提供一个模式或者S修饰符可以把系统对象包括在内。如果使用了\\df+形式，则有关每个函数的额外信息也会被显示，包括易失性、并行安全性、拥有者、安全性分类、访问特权、语言、源代码和描述。

| 提示： |
| --- |
| 如果要查找接收指定数据类型参数或者返回指定类型值的函数，可以使用分页器的搜索能力来滚动显示\\df输出。 |

\\dF\[+\] \[ pattern \]

列出文本搜索配置。如果指定了pattern，只显示名称匹配该模式的配置。如果使用了\\dF+形式，每种配置的完整描述也会被显示，包括底层的文本搜索解析器和用于每一种解析器记号类型的字典列表。

\\dFd\[+\] \[ pattern \]

列出文本搜索字典。如果指定了pattern，只显示名称匹配该模式的字典。如果使用了\\dFd+形式，有关每一种选中的字典的额外信息也会被显示，包括底层的文本搜索模板和选项值。

\\dFp\[+\] \[ pattern \]

列出文本搜索解析器。如果指定了pattern，只显示名称匹配该模式的解析器。如果使用了\\dFp+形式，每一种解析器的完整描述也会被显示，包括底层的函数和可识别的记号类型列表。

\\dFt\[+\] \[ pattern \]

列出文本搜索模板。如果指定了pattern，只显示名称匹配该模式的模板。如果使用了\\dFt+形式，每一种模板有关的额外信息也会被显示，包括底层的函数名称。

\\dg\[S+\] \[ pattern \]

列出数据库角色（因为”用户”和”组”的概念已经被统一成”角色”，这个命令现在等价于\\du）。默认情况下只会显示用户创建的角色，提供一个模式或者S修饰符可以把系统角色包括在内。如果指定了pattern，只列出名称匹配该模式的那些角色。如果使用了\\dg+形式，有关每种角色的额外信息也将被显示，当前这种形式会为角色增加显示注释。

\\dl

这是\\lo\_list的一个别名，它显示大对象的列表。

\\dL\[S+\] \[ pattern \]

列出过程语言。如果指定了pattern，只列出名称匹配该模式的语言。默认情况下只会显示用户创建的语言，提供一个模式或者S修饰符可以把系统对象包括在内。如果向命令名称追加+，则每一种语言会和它的调用处理器、验证器、访问特权以及它是否为系统对象一起列出。

\\dn\[S+\] \[ pattern \]

列出模式（名字空间）。如果指定了pattern，只列出名称匹配该模式的模式。默认情况下只会显示用户创建的对象，提供一个模式或者S修饰符可以把系统对象包括在内。如果向命令名称追加+，每个对象会与它相关的权限及描述（如果有）一起被列出。

\\do\[S+\] \[ pattern \]

列出操作符及其操作数和结果类型。如果指定了pattern，只列出名称匹配该模式的操作符。默认情况下只会显示用户创建的对象，提供一个模式或者S修饰符可以把系统对象包括在内。如果向命令名称追加+，有关每个操作符的额外信息也将被显示，当前只包括底层函数的名称。

\\dO\[S+\] \[ pattern \]

列出排序规则。如果指定了pattern，只列出名称匹配该模式的排序规则。默认情况下只会显示用户创建的对象，提供一个模式或者S修饰符可以把系统对象包括在内。如果向命令名称追加+，每个排序规则将和它相关的描述（如果有）一起被列出。注意只有可用于当前数据库编码的排序规则会被显示，因此在同一个安装下的不同数据库中执行此命令可能会得到不同的结果。

\\dp \[ pattern \]

列出表、视图和序列，包括与它们相关的访问特权。如果指定了pattern，只列出名称匹配该模式的表、视图以及序列。

GRANT和REVOKE命令被用来设置访问特权。

\\dP\[itn+\] \[ pattern \]

列出分区关系。如果指定了pattern，则仅列出名称与模式匹配的条目。 修改符t（表）和i（索引）可以追加到命令中，筛选要列出的关系类型。默认会列出分区表和索引。

如果用了修饰符n（”nested”）或指定了模式，则包括非根分区关系，并显示每个分区关系的父级的列。

如果+被附加到命令名中，那么还会显示每个关系分区的大小总和，以及关系的描述。

如果n与\_相结合，将显示两种大小：一种包含直接连接的叶分区的总大小，另一种显示所有分区的总大小，包括间接附加的子分区。

\\drds \[ role-pattern \[ database-pattern \] \]

列出已定义的配置设置。这些设置可以是针对角色的、针对数据库的或者同时针对两者的。role-pattern和database-pattern分别被用来选择要列出的角色和数据库。如果省略它们或者指定了\*，则会列出所有设置，分别会包括针对角色和针对数据库的设置。

ALTER ROLE以及ALTER DATABASE命令可以用来定义一个角色以及一个数据库的配置设置。

\\dRp\[+\] \[ pattern \]

列出复制的publication。如果指定有pattern，只有那些名称匹配该模式的publication会被列出。如果+被追加到命令的名称上，与每个publication相关的表也会被显示。

\\dRs\[+\] \[ pattern \]

列出复制的订阅。如果指定有pattern，只有那些名字匹配该模式的订阅才会被列出。如果+被追加到命令的名称上，订阅的额外属性会被显示。

\\dT\[S+\] \[ pattern \]

列出数据类型。如果指定了pattern，只列出名称匹配该模式的类型。如果向命令名称追加+，每一种类型、其内部名称和尺寸、允许的值（如果是一种enum类型）以及相关权限会被一同列出。默认情况下只会显示用户创建的对象，提供一个模式或者S修饰符可以把系统对象包括在内。

\\du\[S+\] \[ pattern \]

列出数据库角色（因为”用户”和”组”的概念已经被统一成”角色”，这个命令现在等价于\\dg）。默认情况下只会显示用户创建的角色，提供一个模式或者S修饰符可以把系统角色包括在内。如果指定了pattern，只列出名称匹配该模式的那些角色。如果使用了\\du+形式，有关每一种角色的额外信息也会被显示，当前只会多显示角色的注释。

\\dx\[+\] \[ pattern \]

列出已安装的扩展。如果指定了pattern，只列出名称匹配该模式的那些扩展。如果使用了\\dx+形式，所有属于每个匹配扩展的对象会被列出。

\\dy\[+\] \[ pattern \]

列出事件触发器。如果指定了pattern，只列出名称匹配该模式的事件触发器。如果在命令名称后面加上+，还会为每个列出的对象显示其相关的描述。

\\e或\\edit \[ filename \] \[ line\_number \]

如果指定了filename，则它是被编辑的文件，在编辑器退出后，该文件的内容会被拷贝到当前查询缓冲区中。如果没有给定filename，当前查询缓冲区会被拷贝到一个临时文件中，并且接着以相同的方式编辑。或者，如果当前查询缓冲区为空，则最近被执行的查询会被拷贝到一个临时文件并且以同样的方式编辑。

然后会根据psql的一般规则重新解析查询缓冲区的新内容，把整个缓冲区当作一个单一行来处理。任何完整的查询都会被立即执行，也就是说，如果查询缓冲区包含一个分号或者以一个分号结尾，则到分号处为止的所有东西都会被执行。剩下的东西会在查询缓冲区中等待，输入分号或者\\g会把它发送出去，输入\\r会通过清除查询缓冲区来取消它。把缓冲区当作单一行主要会影响元命令：缓冲区中在一个元命令之后的任何东西都将被当作该元命令的参数，即便元命令之后的内容跨越多行也是如此。（因此不能以这种方式来制作使用元命令的脚本。应该使用\\i。）

如果指定了一个行号，psql将会把游标（注意不是服务器端的游标）定位到文件或者查询缓冲区的指定行上。注意如果给出了一个全是数字的参数，psql就会假定它是行号而不是文件名。

| **提示：** |
| --- |
| 关于如何配置以及自定义编辑器，请见环境。 |

\\echo text \[... \]

把参数打印到标准输出，参数之间用一个空格分隔，最后加上一个新行。这可以用来在脚本的输出中间混入信息，例如：

\=> \\echo \`date\`

Tue Oct 26 21:40:57 CEST 1999

如果第一个参数是一个没有加引号的-n，则不会加上最后的新行。

| **提示：** |
| --- |
| 如果使用\\o命令来重定向查询的输出，你可能希望使用\\qecho来取代这个命令。 |

\\ef \[ function\_description \[ line\_number \] \]

这个命令会以一个CREATE OR REPLACE FUNCTION或CREATE OR REPLACE PROCEDURE命令的形式取出并且编辑指定函数或过程的定义。编辑的方式与\\edit完全相同。在编辑器退出后，更新过的命令将在查询缓冲区中等待，可以键入分号或者\\g把它发出，也可以用\\r取消之。

目标函数可以单独用名称或者用名称和参数（例如foo(integer, text)）来指定。如果有多于一个函数具有同样的名称，则必须给出参数的类型。

如果没有指定函数，将会给出一个空白的CREATE FUNCTION模板来编辑。

如果指定了一个行号，psql将把游标定位在该函数体的指定行上（注意函数体通常不是开始于文件的第一行）。

和大部分其他元命令不同，该行的整个剩余部分总是会被当作\\ef的参数，并且在参数中不会执行变量篡改以及反引号展开。

| 提示： |
| --- |
| 有关如何配置和自定义编辑器可见环境。 |

\\encoding \[ encoding \]

> 设置客户端字符集编码。如果没有参数，这个命令会显示当前的编码。

\\errverbose

最详细的程度重复最近的服务器错误消息，就好像VERBOSITY被设置为verbose且SHOW\_CONTEXT被设置为always。

\\ev \[ view\_name \[ line\_number \] \]

这个命令会以一个CREATE OR REPLACE VIEW的形式取出并且编辑指定函数的定义。编辑的方式与\\edit完全相同。在编辑器退出后，更新过的命令将在查询缓冲区中等待，可以键入分号或者\\g把它发出，也可以用\\r取消之。

如果没有指定函数，将会给出一个空白的CREATE VIEW模板来编辑。

如果指定了一个行号，psql将把游标定位在该视图定义的指定行上。

和大部分其他元命令不同，该行的整个剩余部分总是会被当作\\ev的参数，并且在参数中不会执行变量篡改以及反引号展开。

\\f \[ string \]

设置用于非对齐查询输出的域分隔符。默认值是竖线（|）。它等效于\\pset fieldsep。

\\g \[ filename \]

\\g \[ |command \]

把当前查询缓冲区发送给服务器执行。如果给出一个参数，查询的输出将被写到提到的文件或者用管道导向给定的shell命令，而不是按照惯常显示出来。只有该查询成功地返回零或更多个元组时才会写文件或命令，如果查询失败或者不是一个数据返回SQL命令，则不会写文件或者导向shell命令。

如果当前查询缓冲区为空，则重新执行最近一次被发送的查询。除了这种行为之外，没有参数的\\g实际上等效于一个分号。一个带有参数的\\g是\\o命令的一种”一次性”选择。

如果该参数以|开始，则该行的所有剩余部分总是会被当做要执行的command，并且在参数中不会执行变量篡改以及反引号展开。该行的剩余部分会被简单地按字面传给shell。

\\gdesc

显示当前查询缓冲区的结果的描述（即列名和数据类型）。查询不会被实际执行，不过，如果它含有某种类型的语法错误，该错误将被以通常的方式报出。

如果当前查询缓冲区为空，则会描述最近被发送的查询。

\\gexec

把当前查询缓冲区发送到服务器，然后该查询输出（如果有）中的每一行的每一列都当作一个要被执行的 SQL 语句。例如，要在my\_table的每一列上都创建一个索引：

\=> SELECT format('create index on my\_table(%I)', attname)

\-> FROM pg\_attribute

\-> WHERE attrelid = 'my\_table'::regclass AND attnum > 0

\-> ORDER BY attnum

\-> \\gexec

CREATE INDEX

CREATE INDEX

CREATE INDEX

CREATE INDEX

产生的查询会按照其所在行被返回的顺序执行，如果有多个列，则同一行中按照从左至右的顺序执行。NULL 域会被忽略。产生的查询会被原样发送给服务器处理，因此它们即不能是psql元命令，也不能包含psql变量引用。如果其中任何一个查询失败，剩余查询的执行将会继续，除非设置了ON\_ERROR\_STOP。每个查询的执行都遵照ECHO的处理（在使用\\gexec时，通常建议设置ECHO为all或者queries）。查询日志、单步模式、计时以及其他查询执行特性也适用于每一个生成的查询。

如果当前查询缓冲区为空，则会重新执行最近被发送的查询。

\\gset \[ prefix \]

把当前查询输入缓冲区发送给服务器并且将查询的输出存储在psql变量中（见变量）。

被执行的查询必须只返回一行。该行的每一列会被存储到一个单独的变量中，变量和该列的名字一样。例如：

\=> SELECT 'hello' AS var1, 10 AS var2

\-> \\gset

\=> \\echo:var1:var2

hello 10

如果指定了一个prefix，那么该字符串会被追加在该查询的输出列名称之前用来创建要使用的变量名：

\=> SELECT 'hello' AS var1, 10 AS var2

\-> \\gset result\_

\=> \\echo:result\_var1:result\_var2

hello 10

如果一个列的结果为 NULL，那么对应的变量会被重置而不是被设置。

如果查询失败或者没有返回一行，则不会有任何变量被更改。

如果当前查询缓冲区为空，则重新执行最近被发送的查询。

\\gx \[ filename \]

\\gx \[ |command \]

\\gx等效于\\g，但会为这个查询强制扩展的输出模式。请参考\\x。

\\h or \\help \[ command \]

给出指定SQL命令的语法帮助。如果没有指定command，则psql会列出可以显示语法帮助的所有命令。如果command是一个星号（\*），则会显示所有SQL命令的语法帮助。

与大部分其他元命令不同，该行的所有剩余部分总是会被当做\\help的参数，并且在参数中不会执行变量篡改以及反引号展开。

| 注意： |
| --- |
| 为了简化输入，由几个词构成的命令不需要被加上引号。因此，键入\\help alter table是可以的。 |

\\H or \\html

开启HTML查询输出格式。如果HTML格式已经开启，这会把它切换回默认的对齐文本格式。这个命令是为了兼容性和方便，有关设置其他输出选项请见\\pset。

\\i or \\include filename

从文件filename读取输入并且把它当作从键盘输入的命令来执行。

如果filename是-（连字符），那么会一直读取标准输入直到碰到一个 EOF 指示符或者\\q元命令。这可以用来把交互式输入与文件输入混杂。注意只有在最外层激活了readline 行为的情况下才将会使用 readline 行为。

| **注意：** |
| --- |
| 如果想在屏幕上看到被读入的行，必须把变量ECHO设置成all。 |

\\if expression

\\elif expression

\\else

\\endif

这一组命令实现可嵌套的条件块。条件块必须以一个\\if开始并且以一个\\endif结束。两者之间可能有任意数量的\\elif子句，后面也可能有选择地跟着一个单一的\\else子句。

一般查询以及其他类型的反斜线命令可以出现在这些命令之间构成条件块。

\\if和\\elif命令读取它们的参数并且将它们作为布尔表达式进行计算。如果表达式得到真则处理正常继续下去，否则会跳过下面的行直到到达一个匹配的\\elif、\\else或者\\endif。一旦一个\\if或者\\elif测试成功，同一个块中后面的\\elif命令的参数将不会被计算但会被当作为假。跟在一个\\else后面的行只有在先前的匹配的\\if或\\elif成功时才被处理。

就像任何其他反斜线命令参数一样，\\if或者\\elif命令的expression参数服从变量篡改以及反引号展开。然后会像一个on/off选项变量的值一样来计算它。因此，对下列项无歧义、大小写无关的匹配都是有效的值：true、false、1、0、on、off、yes、no。例如，t、T以及tR都将被认为是真。

无法被正确计算为真或假的表达式将产生一个警告并且被当做假。

正在被跳过的行还是会被正常地解析以标识查询和反斜线命令，但是查询不会被发送到服务器，并且非条件（\\if、\\elif、\\else、\\endif）反斜线命令会被忽略。条件命令会被检查以判断嵌套是否有效。被跳过的行中的变量引用不会被展开，并且也不会执行反引号展开。

一个给定条件块中的所有反斜线命令必须出现在相同的源文件中。如果在所有的本地\\if块被关闭之前，主输入文件或者一个\\include进来的文件上就达到了EOF，则psql将产生一个错误。

这里是一个例子：

\-- 检查数据库中两个单独记录的存在性并且把结果存在单独的psql变量中

SELECT

EXISTS(SELECT 1 FROM customer WHERE customer\_id = 123) as is\_customer,

EXISTS(SELECT 1 FROM employee WHERE employee\_id = 456) as is\_employee

\\gset

\\if:is\_customer

SELECT \* FROM customer WHERE customer\_id = 123;

\\elif:is\_employee

\\echo 'is not a customer but is an employee'

SELECT \* FROM employee WHERE employee\_id = 456;

\\else

\\if yes

\\echo 'not a customer or employee'

\\else

\\echo 'this will never print'

\\endif

\\endif

\\ir or \\include\_relative filename

\\ir命令类似于\\i，但是以不同的方式处理相对路径文件名。在交互模式中执行时，这两个命令的行为相同。不过，当被从脚本中调用时，\\ir相对于脚本所在的目录而不是根据当前工作目录来解释文件名。

\\l\[+\] or \\list\[+\] \[ pattern \]

列出服务器中的数据库并且显示它们的名称、拥有者、字符集编码以及访问特权。如果指定了pattern，则只列出名称匹配该模式的数据库。如果向命令名称追加+，则还会显示数据库的尺寸、默认表空间以及描述（尺寸信息只对当前用户能连接的数据库可用）。

\\lo\_export loid filename

从数据库中读取具有OID loid的大对象并且将它写入到filename。注意这和服务器函数lo\_export有微妙的不同，后者会以运行数据库服务器的用户权限来执行并且运行在服务器的文件系统上。

| **提示：** |
| --- |
| 使用\\lo\_list可以找出大对象的OID。 |

\\lo\_import filename \[ comment \]

把该文件存储到数据库大对象。可选地，它可以把给定的注释关联到该对象。例如：

foo=> \\lo\_import '/home/peter/pictures/photo.xcf' 'a picture of me'

lo\_import 152801

该响应表示该大对象得到的对象 ID 是 152801，未来可以用这个 ID 来访问这个新创建的大对象。为了便于阅读，推荐总是给每一个对象都关联人类可读的注释。OID 和注释都可以用\\lo\_list命令查看。

注意这个命令和服务器端的lo\_import有微妙的不同，因为它以本地文件系统上的本地用户的身份运行，而不是服务器用户和文件系统。

\\lo\_list

显示当前存储在数据库中的所有数据库大对象，同时显示它们的任何注释。

\\lo\_unlink loid

从数据库中删除OID为loid的大对象。

| **提示：** |
| --- |
| 使用\\lo\_list可以找出该大对象的OID。 |

\\o or \\out \[ filename \]

\\o or \\out \[ |command \]

安排把未来的查询结果保存到文件filename中或者用管道导向到 shell 命令command。如果没有指定参数，查询输出会被重置到标准输出。

如果该参数以|开始，则该行的所有剩余部分总是会被当做要执行的command，并且在参数中不会执行变量篡改以及反引号展开。该行的剩余部分会被简单地按字面传给shell。

“查询结果”包括从数据库服务器得到的所有表、命令响应和提示，还有查询数据库的各种反斜线命令（如\\d）的输出，但不包括错误消息。

| **提示：** |
| --- |
| 要在查询结果之间混入文本输出，可以使用\\qecho。 |

\\p or \\print

把当前查询缓冲区打印到标准输出。如果当前查询缓冲区为空，会打印最近被执行的查询。

\\password \[ username \]

更改指定用户（默认情况下是当前用户）的口令。这个命令会提示要求输入新口令、对口令加密然后把加密后的口令作为一个ALTER ROLE命令发送到服务器。这确保新口令不会以明文的形式出现在命令历史、服务器日志或者其他地方。

\\prompt \[ text \] name

提示用户提供一个文本用于分配给变量name。可以指定一个可选的提示字符串text（对于多个词组成的提示，把文本包裹在单引号中）。

默认情况下，\\prompt使用终端进行输入和输出。不过，如果使用了-f命令行开关，\\prompt会使用标准输入和标准输出。

\\pset \[ option \[ value \] \]

这个命令设置影响查询结果表输出的选项。option表示要设置哪个选项。value的语义取决于选中的选项。对于某些选项，如果省略value会导致该选项值被切换或者被重置，具体是哪些选项可见特定选项的描述。如果没有上面提到的那种行为，那么省略value只会导致当前设置被显示。

不带任何参数的\\pset显示所有打印选项的当前状态。

可调整的打印选项有：

- border

value必须是一个数字。通常，数字越大，表格就会有更多的边框和线条，但具体要看是哪一种格式。在HTML格式中，这会直接被转换成border=...属性。在大部分其他格式中，只有值 0（没有边框）、1（内部分隔线）和 2（表格边框）有意义，并且 2 以上的值会被视为与border = 2相同。latex和latex-longtable格式会额外地允许一个值 3 表示在数据行之间增加分隔线。

- columns

为wrapped格式设置目标宽度，还有扩展自动模式中决定输出是否足够多到需要分页器或者切换到垂直显示的宽度限制。零（默认）导致目标宽度由环境变量COLUMNS所控制，如果没有设置COLUMNS则使用检测到的屏幕宽度。此外，如果columns为零则wrapped格式只影响屏幕输出。如果columns为非零则文件和管道输出也会被包裹成该宽度。

- csv\_fieldsep

规定要用于CSV输出格式的字段分隔符。如果分隔符出现在字段的值中，则该字段遵循标准CSV规则在双引号中输出。默认值为逗号。

- expanded (or x)

如果value被指定，它必须是on或者off，它们分别会启用或者禁用扩展模式，也可以是auto。如果value被省略，则该命令会在开启和关闭设置之间切换。当扩展模式被启用时，查询结果被显示在两列中，第一列是列名而第二列是列值。如果在通常的”水平”模式中数据不适合屏幕，则可以用这种模式。在自动设置中，只要查询输出有多于一列并且比屏幕宽，就会使用扩展模式。否则，将使用常规模式。只有在对齐格式和 wrapped 格式中自动设置才有效。在其他格式中，它的行为总是像扩展模式被关闭一样。

- fieldsep

指定在非对齐输出格式中使用的域分隔符。用那种方式，用户可以创建 tab 分隔的输出，这种形式其他程序可能更喜欢。要设置 tab 为域分隔符，可以键入\\pset fieldsep '\\t'。默认的域分隔符是'|'（一个竖线）。

- fieldsep\_zero

把用在非对齐输出格式中的域分隔符设置为一个零字节。

- footer

如果value被指定，它必须是on或者off，它们分别会启用或者禁用表格页脚（(n rows)计数）的显示。如果value被省略，则该命令会切换页脚显示为打开或者关闭。

- format

设置输出格式为下列的一种： aligned, asciidoc, csv, html, latex, latex-longtable, troff-ms, unaligned, 或 wrapped。允许唯一的缩写。

aligned 格式是标准,人类可阅读的、良好格式化的文本输出；这是默认值。

unaligned格式把一个数据行的所有列都写在一行上，之间用当前活动的域分隔符分隔。这可用于生成意图由其他程序读取的输出，例如，tab 分隔或者逗号分隔格式。但是，如果字段分隔符出现在列的值中，则不专门处理该字符；因此CSV格式可能更适合此类目的。

csv 格式写入以逗号分隔的列值，应用引号规则描述在RFC 41801。此输出与服务器COPY命令的 CSV 格式兼容。 除非tuples\_only参数为on，否则将生成具有列名称的标头行。不打印标题和页脚。每行都由系统相关的行尾字符结束，该字符通常是类似Unix的系统的单一换行符（\\n）。除了逗号之外的\\pset csv\_fieldsep字段分隔符，还可以使用\\pset csv\_fieldsep选择。

wrapped格式和aligned相似，但是前者会把过宽的数据值分成多个行以便输出能够适合目标行的宽度。目标行的宽度由columns选项决定。注意psql将不会尝试对列头部标题进行换行，因此如果列头部需要的总宽度超过目标宽度，wrapped格式的行为就变得和aligned一样了。

The asciidoc, html,latex, latex-longtable, 和troff-ms 格式分别用相应的标记语言把要输出的表格放在文档中。不过它们的输出并不是完整的文档。这在HTML中也许不重要，但是在LaTeX中必须有完整的文档包装器。latex 格式使用 LaTeX的tabular环境。latex-longtable 格式需要 LaTeX、longtable 和 booktabs 包。

- linestyle

设置边框线的绘制样式为ascii、old-ascii或者unicode之一。允许不产生歧义的缩写（这意味着一个字母就足够了）。默认的设置是ascii。这个选项只影 响aligned以及wrapped输出格式。

ascii样式使用纯ASCII字符。数据中的新行使用一个+符号在右手边的空白处显示。当在wrapped格式中包裹两行中间没有新行字符的数据时，会在第一行右手边空白处显示一个点号（.），并且在下一行的左手边空白处也显示一个点号（.）。

old-ascii样式使用纯ASCII字符。数据中的新行使用:符号来代替左手边的列分隔符显示。在包裹两行中间没有新行字符的数据时，会用一个;符号取代左手边的列分隔符。

unicode样式使用 Unicode 的方框绘制字符。数据中的新行会使用一个回车符号显示在右手边的空白处。在包裹两行中间没有新行字符的数据时，会在第一行的右手边空白处显示一个省略号，并且在下一行的左手边空白处也显示一个省略号。

当border设置大于零时，linestyle选项也决定边框线用什么字符绘制。纯ASCII字符到处都可以使用，但是在识别 Unicode 字符的显示上使用 Unicode 字符会更好看。

- null

设置要用来替代空值被打印的字符串。默认是什么也不打印，对于一个空字符串这很容易弄错。例如，有人可能更想用\\pset null '(null)'。

- numericlocale

如果value被指定，它必须是on或者off，它们将分别启用或者禁用一个与区域相关的字符来分隔数字和左边的十进制标记。如果value被省略，该命令会在常规输出和区域相关的数字输出之间切换。

- pager

控制对查询和psql的帮助输出使用分页器程序。如果环境变量PSQL\_PAGER或PAGER被设置，输出会被用管道输送到指定的程序。否则将使用与平台相关的默认分页器程序（例如more）。

如果pager选项被设为off，则不会使用分页器程序。如果pager选项被设为on，则会在适当的时候使用分页器，即当输出到终端并且无法适合屏幕时就会使用分页器。pager选项也可以被设置为always，这会导致对所有的终端输出都是用分页器而不管输出是否适合屏幕。不带value的\\pset pager会切换分页器开、关状态。

- pager\_min\_lines

如果pager\_min\_lines被设置为一个大于页面高度的数字，在至少这么多输出行被显示之前都不会调用分页器程序。默认设置为 0。

- recordsep

指定用在非对齐输出格式中的记录（行）分隔符。

- recordsep\_zero

把用在非对齐输出格式中的记录分隔符设置为一个零字节。

- tableattr (or T)

在HTML格式中，这会指定要放在table标记内的属性。例如，这可能是cellpadding或者bgcolor。注意你可能不想在这里指定border，因为那由\\pset border负责。如果没有给出value，则表属性会被重置。

在latex-longtable格式中，这个选项控制每个包含左对齐数据类型的列的宽度比例。这个选项的值是一个由空格分隔的值列表，例如'0.2 0.2 0.6'。没有指定的输出列会使用最后一个指定的值。

- title (or C)

设置用于任何后续被打印表的表标题。这可以用来给输出加上描述性的标签。如果没有给出value，这个标题会被复原。

- tuples\_only (or t)

如果value被指定，它必须是on或者off，这个选项将启用或者禁用只显示元组的模式。如果value被省略，则该命令会在常规输出和只显示元组输出之间切换。常规输出包括列头、标题以及多种页脚之类的额外信息。在只显示元组的模式中，只会显示实际的表数据。

- unicode\_border\_linestyle

设置unicode线型的边框绘制风格为single或者double之一。

- unicode\_column\_linestyle

设置unicode线型的列绘制风格为single或者double之一。

- unicode\_header\_linestyle

设置unicode线型的页眉绘制风格为single或者double之一。

这些不同格式的外观可以在示例小节的图示中看到。

| **提示：** |
| --- |
| \\pset有多种快捷命令。请参见\\a、\\C、\\f、\\H、\\t、\\T以及\\x。 |

\\q or \\quit

退出psql程序。在一个脚本文件中，只有该脚本的执行会被终止。

\\qecho text \[... \]

这个命令和\\echo一样，不过输出将被写到\\o所设置的查询输出通道。

\\r or \\reset

重置（清除）查询缓冲区。

\\s \[ filename \]

打印psql的命令行历史到filename。如果省略filename，该历史会被写入到标准输出（如果适用则使用分页器）。如果编译psql时没有加上Readline支持，则这个命令不可用。

\\set \[ name \[ value \[... \] \] \]

设置psql变量name为value，如果给出了多于一个值，则把该变量的值设置为所有给出的值的串接。如果只给了一个参数，该变量会被设置为空字符串值。要重置一个变量，可以使用\\unset 命令。

不带任何参数的\\set显示所有当前设置的psql变量的名称和值。

合法的变量名可以包含字母、数字和下划线。详见下文的变量。变量名是大小写敏感的。

某些变量是特殊的，它们控制psql的行为或者会被自动设置以反映连接状态。这些变量在下文的变量中记录。

| **注意：** |
| --- |
| 这个命令和SQL命令SET无关。 |

\\setenv name \[ value \]

把环境变量name设置为value，如果没有提供value，则会重置该环境变量。例如：

testdb=> \\setenv PAGER less

testdb=> \\setenv LESS -imx4F

\\sf\[+\] function\_description

这个命令以一个CREATE OR REPLACE FUNCTION命令或者CREATE OR REPLACE PROCEDURE命令取出并且显示指定函数或者过程的定义。定义会被打印到当前的查询输出渠道，就像\\o所作的那样。

目标函数可以单独用名称指定，也可以用名称和参数指定，例如foo(integer, text)。

如果有多于一个函数具有相同的名字，则必须给出参数的类型。

如果向命令名称追加+，那么输出行会被编号，函数体的第一行会被编为 1。

与大部分其他元命令不同，该行的所有剩余部分总是会被当做\\sf的参数，并且在参数中不会执行变量篡改以及反引号展开。

\\sv\[+\] view\_name

这个命令以一个CREATE OR REPLACE VIEW命令取出并且显示指定视图的定义。定义会被打印到当前的查询输出渠道，就像\\o所作的那样。

如果在命令名称上追加+，那么输出行会从 1 开始编号。

与大部分其他元命令不同，该行的所有剩余部分总是会被当做\\sv的参数，并且在参数中不会执行变量篡改以及反引号展开。

\\t

切换输出列名标题和行计数页脚的显示。这个命令等效于\\pset tuples\_only，提供它只是为了使用方便而已。

\\T table\_options

指定在HTML输出格式中，要放在table标签内的属性。这个命令等效于\\pset tableattr table\_options。

\\timing \[ on | off \]

如果给出一个参数，这个参数用来打开或者关闭对每个SQL语句执行时长的显示。如果没有参数，则在打开和关闭之间切换。显示的数据以毫秒为单位，超过1秒的区间还会被显示为”分钟:秒”的格式，如果必要还会加上小时和日的字段。

\\unset name

重置（删除）psql变量name。

大部分控制psql行为的变量不能被重置，相反，\\unset命令会被解释为把它们设置为其默认值。请参考下文的变量。

\\w or \\write filename

\\w or \\write |command

把当前查询缓冲区写到文件filename或者用管道导出到 shell 命令command。如果当前查询缓冲区为空，则写最近被执行的查询。

如果参数以|开始，则该行的整个剩余部分会被当做要执行的command，并且在参数中不会执行变量篡改以及反引号展开。该行的剩余部分会被简单地按字面传递给shell。

\\watch \[ seconds \]

反复执行当前的查询缓冲区（就像\\g那样）直到被中止或者查询失败。两次执行之间等待指定的秒数（默认是 2 秒）。显示每个查询结果时带上一个由\\pset title字符串（如果有）、从查询开始起的时间以及延时间隔组成的页眉。

如果当前查询缓冲区为空，则会重新执行最近被发送的查询。

\\x \[ on | off | auto \]

设置或者切换扩展表格格式化模式。究其本身而言，这个命令等效于\\pset expanded。

\\z \[ pattern \]

列出表、视图和序列，以及它们相关的访问特权。如果指定了pattern，则只会列出名称匹配该模式的表、视图和序列。

这是\\dp（”display privileges”）的一个别名。

\\! \[ command \]

如果没有参数，就跳出到一个子shell，当子shell退出时psql会继续。如果有一个参数，则执行shell命令command。

与大部分其他元命令不同，该行的所有剩余部分总是会被当做\\!的参数，并且在参数中不会执行变量篡改以及反引号展开。该行的剩余部分会被简单地按字面传递给shell。

\\? \[ topic \]

显示帮助信息。可选的topic参数（默认是commands）选择解释psql的哪一部分：commands表示psql的反斜线命令；options表示可以传递给psql的命令行选项；而variables显示有关psql配置变量的帮助。

\\;

反斜线分号并非和前述命令相同的元命令，它只是会把一个分号加入到查询缓冲区且不会进一步执行。

通常，只要psql达到了命令结束的分号，它就将分发一个SQL命令给服务器，即使在当前行上还留有更多输入。因此，例如输入 select 1; select 2; select 3;将导致三个SQL命令被逐个发送给服务器，在继续到下一个命令前会显示每一个命令的结果。不过，被输入为\\;的分号将不会触发命令处理，这样在它之前的命令以及其后的命令实际上会被组合在一个请求中发送给服务器。例如

select 1\\; select 2\\; select 3;

会导致在到达非反斜线分号时用一个单一的请求把三个SQL命令发送给服务器。服务器会把这样一个请求当作单一的事务执行，除非该字符串中有显式的BEGIN/COMMIT命令把它划分成多个事务。psql对每个请求仅打印出它接收到的最后一个查询结果。在这个例子中，尽管所有三个SELECT确实都被执行了，但psql只会打印出3。

模式（Pattern）

很多\\d命令都可以用一个pattern参数来指定要被显示的对象名称。在最简单的情况下，模式正好就是该对象的准确名称。在模式中的字符通常会被变成小写形式（就像在 SQL 名称中那样），例如\\dt FOO将会显示名为foo的表。就像在 SQL 名称中那样，把模式放在双引号中可以阻止它被转换成小写形式。如果需要在一个模式中包括一个真正的双引号字符，则需要把它写成两个相邻的双引号，这同样是符合 SQL 引用标识符的规则。例如，\\dt "FOO""BAR"将显示名为FOO"BAR（不是foo"bar）的表。和普通的 SQL 名称规则不同，你不能只在模式的一部分周围放上双引号，例如\\dt FOO"FOO"BAR将会显示名为fooFOObar的表。

只要pattern参数被完全省略，\\d命令会显示在当前 schema 搜索路径中可见的全部对象—这等价于用\*作为模式（如果一个对象所在的 schema 位于搜索路径中并且没有同类且同名的对象出现在搜索路径中该 schema 之前的 schema 中，则说该对象是可见的。这表示可以直接用名称引用该对象，而不需要用 schema 来进行限定）。要查看数据库中所有的对象而不管它们的可见性，可以把\*.\*用作模式。

如果放在一个模式中，\*将匹配任意字符序列（包括空序列），而?会匹配任意的单个字符（这种记号方法就像 Unix shell 的文件名模式一样）。例如，\\dt int\*会显示名称以int开始的表。但是如果被放在双引号内，\*和?就会失去这些特殊含义而变成普通的字符。

包含一个点号（.）的模式被解释为一个 schema 名称模式后面跟上一个对象名称模式。例如，\\dt foo\*.\*bar\*会显示名称以foo开始的 schema 中所有名称包括bar的表。如果没有出现点号，那么模式将只匹配当前 schema 搜索路径中可见的对象。同样，双引号内的点号会失去其特殊含义并且变成普通的字符。

高级用户可以使用字符类等正则表达式记法，如\[0-9\]可以匹配任意数字。以下字符除外：.会按照上面所说的作为一种分隔符，\*会被翻译成正则表达式记号.\*，?会被翻译成.，而$则按字面意思匹配。根据需要，可以通过书写?、(R+|)、(R|)和R?来分别模拟模式字符.、R\*和R?。$不需要作为一个正则表达式字符，因为模式必须匹配整个名称，而不是像正则表达式的常规用法那样解释（换句话说，$会被自动地追加到模式上）。如果不希望该模式的匹配位置被固定，可以在开头或者结尾写上\*。注意在双引号内，所有的正则表达式特殊字符会失去其特殊含义并且按照其字面意思进行匹配。还有，在操作符名称模式中（即作为\\do的参数），正则表达式特殊字符也按照字面意思进行匹配。

**高级特性**

- 变量

psql提供了和普通 Unix 命令 shell 相似的变量替换特性。变量简单来说就是一对名称/值，其中值可以是任意长度的任意字符串。名称必须由字母（包括非拉丁字母）、数字和下划线构成。

要设置一个变量，可以使用psql的元命令\\set。例如，testdb=> \\set foo bar会设置foo为值bar。要检索该变量的内容，可以在名称前放一个分号，例如：

testdb=> \\echo:foo bar

这在常规 SQL 命令和元命令中均有效，下文的SQL 中插入变量中有更多细节。

如果调用\\set时没有第二个参数，该变量会被设置为一个空字符串值。要重置（即删除）一个变量，可以使用命令\\unset。要显示所有变量的值，在调用\\set时不带任何参数即可。

| **注意：** |
| --- |
| \\set的参数服从与其他命令相同的替换规则。因此可以构造有趣的引用，例如\\set:foo 'something'以及分别得到Perl或者PHP的”软链接”或者”可变变量”。不幸的是（或者幸运的是？），这些构造出来的东西并没有什么用处。在另一方面，\\set bar:foo是一种很好的拷贝变量的方法。 |

有一些变量会被psql特殊对待。它们表示特定的选项设置，运行时这类选项设置可以通过修改该变量的值来改变，或者在某些情况下它们表示psql的可更改的状态。按照惯例，所有被特殊对待的变量的名称由全部大写形式的 ASCII 字母（还有可能是数字和下划线）组成。为了确保未来最大的兼容性，最好避免把这类变量名用于自己的目的。

控制psql行为的变量通常不能被重置或者设置为无效值。允许\\unset命令，但它会被解释为将变量设置为它的默认值。没有第二参数的\\set命令会被解释为将变量设置为on（对于接受该值的控制变量），对不接受该值的变量则会拒绝这个命令。此外，接受值on和off的控制变量也能接受其他常见的布尔值拼写方式，例如true和false。

被特殊对待的变量是：

AUTOCOMMIT

在被设置为on（默认）时，每一个 SQL 命令在成功完成时会被自动提交。在这种模式中要推迟提交，必须输入一个BEGIN或者START TRANSACTION SQL 命令。当被设置为off或者被重置时，在显式发出COMMIT或者END之前，SQL 命令不会被提交。自动提交打开模式会为你发出一个隐式的BEGIN，这会发生在任何不在一个事务块中且本身即不是BEGIN及其他事务控制命令且不是无法在事务块中执行的命令（例如VACUUM）之前。

| **注意：** |
| --- |
| 在自动提交关闭模式中，必须通过ABORT或者ROLLBACK显式地放弃任何失 败的事务。还要记住，如果退出会话时没有提交，则所有的工作都会丢失。 |

| **注意：** |
| --- |
| 自动提交打开模式是瀚高数据库的传统行为，但是自动提交关闭模式更接 近于 SQL 的规范。如果更喜欢自动提交关闭模式，可以在系统级的psqlrc文件或者个人的~/.psqlrc文件中设置它。 |

COMP\_KEYWORD\_CASE

确定在补全一个 SQL 关键词时要使用的大小写形式。如果被设置为lower或者upper，补全后的词将分别是小写或者大写形式。如果被设置为preserve-lower或者preserve-upper（默认），补全后的词将会保持该词已输入部分的大小写形式，但是如果被补全的词还没有被输入，则它会被分别补全成小写或者大写形式。

DBNAME

当前已连接的数据库名称。每次连接到一个数据库时都会设置该变量（包括程序启动时），但是可以被更改或者重置。

ECHO

如果被设置为all，所有非空输入行会被按照读入它们的样子打印到标准输出（不适用于交互式读取的行）。要在程序开始时选择这种行为，可以使用开关-a。如果被设置为queries，psql会在发送每个查询给服务器时将它们打印到标准输出。选择这种行为的开关是-e。如果被设置为errors，那么只有失败的查询会被显示在标准错误输出上。这种行为的开关是-b。如果被重置或者设置为none（默认值）则不会显示任何查询。

ECHO\_HIDDEN

当这个变量被设置为on且一个反斜线命令查询数据库时，相应的查询会被先显示。如果把这个变量设置为值noexec，则对应的查询只会被显示而并不真正被发送给服务器执行。默认值是off。

ENCODING

当前的客户端字符集编码。每一次你连接到一个数据库（包括程序启动）时以及当你用\\encoding更改编码时，这个变量都会被设置，但它可以被更改或者重置。

ERROR

如果上一个SQL查询失败则为true，如果成功则是false。

FETCH\_COUNT

如果这个变量被设置为一个大于零的整数值，SELECT查询的结果会以一组一组的方式取出并且显示（而不是像默认的那样把整个结果集拿到以后再显示），每一组就会包括这么多个行。因此，这种方式只会使用有限的内存量，而不管整个结果集的大小。在启用这个特性时，通常会使用 100 到 1000 的设置。记住在使用这种特性时，一个查询可能会在已经显示了一些行之后失败。

| **注意：** |
| --- |
| 尽管可以把这种特性用于任何的输出格式，但是默认的aligned格式看起来会比较糟糕，因为每一组的FETCH\_COUNT个行将被单独格式化，这就会导致不同的行组的列宽不同。其他的输出格式会更好。 |

HIDE\_TABLEAM

如果此变量设置为true，则不显示表的访问方法的详细信息。这主要用于回归测试。

HISTCONTROL

如果这个变量被设置为ignorespace，则以一个空格开始的行不会被放入到历史列表中。如果被设置为值ignoredups，则匹配之前的历史行的行不会被放入。值ignoreboth组合了上述两种值。如果被重置或者被设置为none（默认值），所有在交互模式中被读入的行都会保存在历史列表中。

HISTFILE

该文件名将被用于存储历史列表。如果被重设，文件名将从PSQL\_HISTORY环境变量中取得。如果该环境变量也没有被设置，则默认值是~/.psql\_history，放在~/.psqlrc中将会导致psql为每一个数据库维护一个单独的历史。

HISTSIZE

存储在命令历史中的最大命令数（默认值是500）。如果被设置为一个负值，则不会应用限制。

HOST

当前连接到的数据库服务器端口。每次连接到一个数据库时都会设置该变量（包括程序启动时），但是可以被更改或者重置。

IGNOREEOF

如果被设置为1或者更小，向一个psql的交互式会话发送一个EOF字符（通常是Control+D）将会终止应用。如果设置为一个较大的数字值，则必须键入多个连续的EOF字符才能让交互式会话终止。如果该变量被设置为一个非数字值，则它会被解释为10。默认值为0。

LASTOID

最后被影响的 OID 的值，这可能会由INSERT或者\\lo\_import命令返回。这个变量只保证在下一个SQL命令被显示完之前有效。

LAST\_ERROR\_MESSAGE

LAST\_ERROR\_SQLSTATE

当前psql会话中最近一个失败查询的主错误消息和相关的SQLSTATE代码，如果在当前会话中没有发生错误，则是一个空字符串和00000。

ON\_ERROR\_ROLLBACK

当被设置为on时，如果事务块中的一个语句产生一个错误，该错误会被忽略并且该事务会继续。当被设置为interactive时，只在交互式会话中忽略这类错误，而读取脚本文件时则不会忽略错误。当被重置或者设置为off（默认值）时，事务块中产生错误的一个语句会中止整个事务。错误回滚模式的工作原理是在事务块的每个命令之前都为你发出一个隐式的SAVEPOINT，然后在该命令失败时回滚到该保存点。

ON\_ERROR\_STOP

默认情况下，出现一个错误后命令处理会继续下去。当这个变量被设置为on后，出现错误后命令处理会立即停止。在交互模式下，psql将会返回到命令提示符；否则，psql将会退出并且返回错误代码 3 来把这种情况与致命错误区分开来，致命错误会被报告为错误代码 1。在两种情况下，任何当前正在运行的脚本（顶层脚本以及任何它已经调用的其他脚本）将被立即中止。如果顶层命名字符串包含多个 SQL 命令，将在当前命令处停止处理。

PORT

当前连接到的数据库服务器端口。每次连接到一个数据库时都会设置该变量（包括程序启动时），但是可以被更改或者重置。

PROMPT1

PROMPT2

PROMPT3

这些变量指定psql发出的提示符的模样。见下文的提示符。

QUIET

把这个变量设置为on等效于命令行选项-q。在交互模式下可能用处不大。

ROW\_COUNT

上一个SQL查询返回的行数或者受影响的行数，如果该查询失败或者没有报告行计数则为0。

SERVER\_VERSION\_NAME

SERVER\_VERSION\_NUM

字符串形式的服务器版本号，以及数字形式的服务器版本号。每次你连接到一个数据库（包括程序启动）时，这些都会被设置，但可以被改变或者重设。

SHOW\_CONTEXT

这个变量可以被设置为值never、errors或者always来控制是否在来自服务器的消息中显示CONTEXT域。默认是errors（表示在错误消息中显示上下文，但在通知和警告消息中不显示）。 当VERBOSITY被设置为terse或sqlstate时，这个设置无效（另见\\errverbose，它可以用来得到刚遇到的错误的详细信息）。

SINGLELINE

设置这个变量为on等效于命令行选项-S。

SINGLESTEP

设置这个变量为on等效于命令选项-s。

SQLSTATE

与上一个SQL查询的失败相关的错误代码（见附录A），如果上一个查询成功则为00000。

USER

当前连接的数据库用户。每次连接到一个数据库时都会设置该变量（包括程序启动时），但是可以被更改或者重置。

VERBOSITY

这个变量可以被设置为值default、verbose、terse或者sqlstate来控制错误报告的详细程度（另见\\errverbose，在想得到之前的错误的详细版本时使用）。

VERSION

VERSION\_NAME

VERSION\_NUM

这些变量在程序启动时被设置以反映psql的版本，分别是一个详细的字符串、一个短字符串以及一个数字。它们可以被更改或重设。

- SQL 中插入变量

psql变量的一个关键特性是可以把它们替换（”插入”）到常规SQL语句中，也可以把它们作为元命令的参数。此外，psql还提供了功能来确保被用作 SQL 文字和标识符的变量值会被正确地引用。插入一个值而不需要加引用的语法是在变量名前面加上一个冒号（:）。例如，

testdb=> \\set foo 'my\_table'

testdb=> SELECT \* FROM:foo;

将查询表my\_table。注意这可能会不安全：该变量的值会被按字面拷贝，因此它可能包含不平衡的引号甚至反斜线命令。必须确保把它放在那里是有意义的。

当一个值被用作 SQL 文本或者标识符时，最安全的是把它加上引用。要引用一个变量的值作为 SQL 文本，可以把变量名称放在单引号中并且在引号前面写一个冒号。要引用作为SQL 标识符，则可以把变量名称放在双引号中并且在引号前面写一个冒号。这种结构可以正确地处理变量值中嵌入的引号和其他特殊字符。之前的例子用这种方法写会更安全：

testdb=> \\set foo 'my\_table'

testdb=> SELECT \* FROM:"foo";

在被引用的SQL文本和标识符中将不会执行变量插入。因此，一个诸如':foo'的结构不会从一个变量的值产生一个被引用的文本（即便能够也会不安全，因为无法正确地处理嵌入在值中的引号）。

使用这种机制的一个例子是把一个文件的内容拷贝到一个表列中。首先把该文件载入到一个变量，然后把该变量的值作为一个被引用的字符串插入：

testdb=> \\set content \`cat my\_file.txt\`

testdb=> INSERT INTO my\_table VALUES (:'content');

（注意如果my\_file.txt包含 NUL 字节，这样也不行。psql不支持在变量值中嵌入 NUL 字节）。

因为冒号可以合法地出现在 SQL 命令中，一次明显的插入尝试（即:name、:'name'或者:"name"）不会被替换，除非所提及的变量就是当前被设置的。在任何情况下，可以用一个反斜线对冒号进行转义以避免它被替换。

:{?name}特殊语法根据该变量存在与否返回TRUE或者FALSE，并且因此总是会被替换，除非分号被反斜线转义。

变量的冒号语法对嵌入式查询语言（例如ECPG）来说是标准的SQL。用于数组切片和类型造型的冒号语法是瀚高数据库扩展，它有时可能会与标准用法冲突。把一个变量值转义成 SQL文本或者标识符的冒号引用语法是一种psql扩展。

- 提示符

psql发出的提示符可以根据用户的喜好自定义。PROMPT1、PROMPT2和PROMPT3这三个变量包含了描述提示符外观的字符串和特殊转义序列。Prompt 1 是当psql等待新命令时发出的常规提示符。Prompt 2 是在命令输入时需要更多输入时发出的提示符，例如因为当命令没有被分号终止或者引用没有被关闭时就会发出这个提示符。在运行一个SQL COPY FROM STDIN命令并且需要在终端上输入一个行值时，会发出 Prompt 3。

被选中的提示符变量会被原样打印，除非碰到一个百分号（%）。百分号的下一个字符会被特定的其他文本替换。预定义好的替换有：

%M

数据库服务器的完整主机名（带有域名），或者当该连接是建立在一个 Unix 域套接字上时则是\[local\]，或者当 Unix 域套接字不在编译在系统内的默认位置上时则是\[local:/dir/name\]。

%m

数据库服务器的主机名称（在第一个点处截断），或者当连接建立在一个 Unix 域套接字上时是\[local\]。

%>

数据库服务器正在监听的端口号。

%n

数据库会话的用户名（在数据库会话期间，这个值可能会因为命令SET SESSION AUTHORIZATION的结果而改变）。

%/

当前数据库的名称。

%~

和%/类似，但是如果数据库是默认数据库时输出是~（波浪线）。

%#

如果会话用户时一个数据库超级用户，则是#，否则是一个>（在数据库会话期间，这个值可能会因为命令SET SESSION AUTHORIZATION的结果而改变）。

%p

当前连接到的后端的进程 ID。

%R

在提示符1下通常是=，但如果会话位于一个条件块的一个非活动分支中则是@，如果会话处于单行模式中则是^，如果会话从数据库断开连接（\\connect失败时会发生这种情况）则是!。在提示符 2 中，根据为什么psql期待更多的输入，%R会被一个相应的字符替换：如果命令还没有被终止是-，如果有一个未完的/\*... \*/注释则是\*，如果有一个未完的被引用字符串则是一个单引号，如果有一个未完的被引用标识符则是一个双引号，如果有一个未完的美元引用字符串则是一个美元符号，如果有一个还没有被配对的左圆括号则是(。在提示符 3 中%R不会产生任何东西。

%x

事务状态：当不在事务块中时是一个空字符串，在一个事务块中时是\*，在一个失败的事务块中时是!，当事务状态是未判定时（例如因为没有连接）为?。

%l

当前语句中的行号，从1开始。%digits 带有指定的八进制码的字符会被替换。

%:name:

psql变量name的值。详见变量。

%\`command\` command的输出，类似于平常的”反引号”替换。

%\[... %\]

提示符可以包含终端控制字符，例如改变提示符文本的颜色、背景或者风格以及更改终端窗口标题的控制字符。为了让Readline的行编辑特性正确工作，这些不可打印的控制字符必须被包裹在%\[和%\]之间以指定它们是不可见的。在提示附中可以出现多个这样的标识对。例如：

testdb=> \\set PROMPT1 '%\[%033\[1;33;40m%\]%n@%/%R%\[%033\[0m%\]%# '

会导致一个在兼容 VT100 的彩色终端上的粗体（1;）的、黑底黄字（33;40）的提示符。

要在你的提示符中插入一个百分号，可以写成%%。提示符 1 和 2 的默认提示是'%/%R%# '，提示符 3 的提示是'>> '。

- 命令行编辑

为了方便的行编辑和检索，psql支持Readline库。psql退出时命令历史会被自动保存，而当psql启动时命令历史会被重新载入。psql也支持 tab 补全，不过补全逻辑绝不是一个SQL解析器。tab 补全产生的查询也可能会受其他 SQL 命令干扰，例如SET TRANSACTION ISOLATION LEVEL。如果出于某种原因不想用 tab 键补全，可以把下面的代码放在主目录下的名为.inputrc文件中关闭该特性：

$if psql

set disable-completion on

$endif

（这不是psql特性而是Readline的特性。进一步的细节请阅读它的文档。）

**环境**

COLUMNS

如果\\pset columns为零，这个环境变量控制用于wrapped格式的宽度以及用来确定是否输出需要用到分页器或者切换到扩展自动模式中的垂直格式的宽度。

PGDATABASE

PGHOST

PGPORT

PGUSER

默认连接参数（见开发手册第一章节内容）。

PG\_COLOR

规定在诊断消息中是否使用颜色。可能的值为always、 auto、never。

PSQL\_EDITOR

EDITOR

VISUAL

\\e、\\ef以及\\ev命令所使用的编辑器。会按照列出的顺序检查这些变量，第一个被设置的将被使用。如果都没有被设置，默认是使用Unix系统上的vi。

PSQL\_EDITOR\_LINENUMBER\_ARG

当\\e、\\ef或者\\ev带有一个行号参数时，这个变量指定用于传递起始行号给用户编辑器的命令行参数。对于Emacs或者vi之类的编辑器，这个变量是一个加号。如果需要在选项名称和行号之间有空格，可以在该变量的值中包括一个结尾的空格。例如：

PSQL\_EDITOR\_LINENUMBER\_ARG='+'

PSQL\_EDITOR\_LINENUMBER\_ARG='--line '

在 Unix 系统上默认是+（对应于默认编辑器vi，且对很多其他常见编辑器可用）。

PSQL\_HISTORY

命令历史文件的替代位置。波浪线（~）扩展会被执行。

PSQL\_PAGER

PAGER

如果一个查询的结果在屏幕上放不下，它们会通过这个命令分页显示。典型的值是more或less。通过把PSQL\_PAGER或PAGER设置为空字符串可以禁用分页器的使用，调整\\pset命令与分页器相关的选项也能达到同样的效果。会按照列出的顺序检查这些变量，第一个被设置的将被使用。如果都没有被设置，则大部分平台上默认使用more，但在Cygwin上使用less。

PSQLRC

用户的.psqlrc文件的替代位置。波浪线（~）扩展会被执行。

SHELL

被\\!命令执行的命令。

TMPDIR

存储临时文件的目录。默认是/tmp。

和大部分其他瀚高工具一样，这个工具也使用libpq所支持的环境变量（见开发手册）。

**文件**

psqlrc and ~/.psqlrc

如果没有-X选项，在连接到数据库后但在接收正常的命令之前，psql会尝试依次从系统级的启动文件（psqlrc）和用户的个人启动文件（~/.psqlrc）中读取并且执行命令。这些文件可以被用来设置客户端或者服务器，通常是一些\\set和SET命令。

系统级的启动文件是psqlrc，它应该在安装好的数据库的”系统配置”目录中，最可靠的定位方法是运行pg\_config --sysconfdir。默认情况下，这个目录将是../etc/ （相对于包含数据库可执行文件的目录）。可以通过PGSYSCONFDIR环境变量显式地设置这个目录的名称。

用户个人的启动文件是.psqlrc，它应该在调用用户的主目录中。用户启动文件的位置可以通过PSQLRC环境变量设置。

系统级和用户个人的启动文件都可以弄成是针对特定psql版本的，方法是在文件名后面加上一个横线以及数据库的主、次版本号。版本最为匹配的文件会优先于不那么匹配的文件读入。

.psql\_history

命令行历史被存储在文件~/.psql\_history中。

历史文件的位置可以通过HISTFILE psql变量或者PSQL\_HISTORY环境变量明确的设置。

**注解**

• psql和具有相同主版本或者更老的主版本服务器最为匹配。如果服务器的版本比psql本身要高，则反斜线命令尤其容易失败。不过，\\d家族的反斜线命令应该可以和版本 7.4 之后的服务器一起使用，但服务器的版本不必比psql本身新。运行 SQL 命令并且显示查询结果的一般功能应该也能和具有更新主版本的服务器一起使用，但是并非在所有的情况下都能保证如此。

如果你想用psql连接到多个具有不同主版本的服务器，推荐使用最新版本的psql。或者，你可以为每一个主版本保留一份psql拷贝，并且针对相应的服务器使用匹配的版本。但实际上，这种额外的麻烦是不必要的。

**给用户的注解**

psql是一个”控制台应用”。在psql中使用 8 位字符时要特别注意。如果psql检测到一个有问题的控制台代码页，它将会在启动时警告你。要更改控制台代码页，有两件事是必要的：

• 输入cmd.exe /c chcp 1252可以设置代码页（1252 是适用于德语的一个代码页，请在这里替换成你的值）。如果正在使用 Cygwin，可以把这个命令放在/etc/profile中。

• 把控制台字体设置为Lucida Console，因为栅格字体无法与 ANSI 代码页一起使用。

**示例**

第一个例子展示了如何如何跨越多行输入一个命令。注意提示符的改变：

testdb=> CREATE TABLE my\_table (

testdb(> first integer not null default 0,

testdb(> second text)

testdb->;

CREATE TABLE

现在再看看表定义：

testdb=> \\d my\_table

Table "public.my\_table"

Column | Type | Collation | Nullable | Default

\--------+---------+-----------+----------+---------

first | integer | | not null | 0

second | text | | |

现在我们把提示符改一改：

testdb=> \\set PROMPT1 '%n@%m %~%R%# '

peter@localhost testdb=>

假定已经用数据填充了这个表并且想看看其中的数据：

peter@localhost testdb=> SELECT \* FROM my\_table;

first | second

\-------+--------

1 | one

2 | two

3 | three

4 | four

(4 rows)

你可以用\\pset命令以不同的方式显示表：

peter@localhost testdb=> \\pset border 2

Border style is 2.

peter@localhost testdb=> SELECT \* FROM my\_table;

+-------+--------+

| first | second |

+-------+--------+

| 1 | one |

| 2 | two |

| 3 | three |

| 4 | four |

+-------+--------+

(4 rows)

peter@localhost testdb=> \\pset border 0

Border style is 0.

peter@localhost testdb=> SELECT \* FROM my\_table;

first second

\----- ------

1 one

2 two

3 three

4 four

(4 rows)

peter@localhost testdb=> \\pset border 1

Border style is 1.

peter@localhost testdb=> \\pset format csv

Output format is csv.

peter@localhost testdb=> \\pset tuples\_only

Tuples only is on.

peter@localhost testdb=> SELECT second, first FROM my\_table;

one,1

two,2

three,3

four,4

peter@localhost testdb=> \\pset format unaligned

Output format is unaligned.

peter@localhost testdb=> \\pset fieldsep '\\t'

Field separator is " ".

peter@localhost testdb=> SELECT second, first FROM my\_table;

one 1

two 2

three 3

four 4

或者使用短命令：

peter@localhost testdb=> \\a \\t \\x

Output format is aligned.

Tuples only is off.

Expanded display is on.

peter@localhost testdb=> SELECT \* FROM my\_table;

\-\[ RECORD 1 \]-

first | 1

second | one

\-\[ RECORD 2 \]-

first | 2

second | two

\-\[ RECORD 3 \]-

first | 3

second | three

\-\[ RECORD 4 \]-

first | 4

second | four

如果需要，可以用\\crosstabview命令以交叉表的形式显示查询结果：

testdb=> SELECT first, second, first > 2 AS gt2 FROM my\_table;

first | second | gt2

\-------+--------+-----

1 | one | f

2 | two | f

3 | three | t

4 | four | t

(4 rows)

testdb=> \\crosstabview first second

first | one | two | three | four

\-------+-----+-----+-------+------

1 | f | | |

2 | | f | |

3 | | | t |

4 | | | | t

(4 rows)

这第二个例子展示了表的”乘法”（连接），行按照序号降序排序且列按照独立的、升序的方式排序。

testdb=> SELECT t1.first as "A", t2.first+100 AS "B", t1.first\*(t2.first+100) as

"AxB",

testdb(> row\_number() over(order by t2.first) AS ord

testdb(> FROM my\_table t1 CROSS JOIN my\_table t2 ORDER BY 1 DESC

testdb(> \\crosstabview "A" "B" "AxB" ord

A | 101 | 102 | 103 | 104

\---+-----+-----+-----+-----

4 | 404 | 408 | 412 | 416

3 | 303 | 306 | 309 | 312

2 | 202 | 204 | 206 | 208

1 | 101 | 102 | 103 | 104

(4 rows)

## reindexdb

reindexdb — 重建数据库索引

**命令**

reindexdb \[connection-option...\] \[option...\] \[ --schema | -S schema \]... \[ --

table | -t table \]... \[ --index | -i index \]... \[dbname\]

reindexdb \[connection-option...\] \[option...\] --all | -a

reindexdb \[connection-option...\] \[option...\] --system | -s \[dbname\]

**描述**

reindexdb是用于重建一个数据库中索引的工具。

reindexdb是 SQL 命令REINDEX的一个包装器。在通过这个工具和其他方法访问服务器来重索引数据库之间没有实质性的区别。

**选项**

reindexdb接受下列命令行参数：

\-a

\--all

重索引所有数据库。

\--concurrently

使用 CONCURRENTLY 选项。更多信息参见 REINDEX。

\[-d\] dbname

\[--dbname=\]dbname

指定要被重索引的数据库名。如果这没有被指定并且没有使用-a（或--all），数据库名可以从环境变量PGDATABASE中被读出。如果环境变量也没被设置，为该连接指定的用户名将被用作数据库名。

\-e

\--echo

回显reindexdb生成并发送到服务器的命令。

\-i index

\--index=index

只是重建index。可以通过写多个-i开关来重建多个索引。

\-q

\--quiet

不显示进度消息。

\-s

\--system

索引数据库的系统目录。

\-S schema

\--schema=schema

只对schema重建索引。 通过写多个-S开关可以指定多个要重建索引的模式。

\-t table

\--table=table

只索引table。可以通过写多个-t开关来重索引多个表。

\-v

\--verbose

在处理时打印详细信息。

\-V

\--version

打印reindexdb版本并退出。

\-?

\--help

显示有关reindexdb命令行参数的帮助并退出。

reindexdb也接受下列命令行参数用于连接参数：

\-h host

\--host=host

指定运行服务器的机器的主机名。如果该值以一个斜线开始，它被用作 Unix 域套接字的目录。

\-p port

\--port=port

指定服务器正在监听连接的 TCP 端口或本地 Unix 域套接字文件扩展。

\-U username

\--username=username

要作为哪个用户连接。

\--maintenance-db=dbname

指定要连接到来发现哪些其他数据库应该被重索引的数据库名。如果没有指定，将使用highgo数据库。而如果它也不存在，将使用template1。

**环境**

> PGDATABASE
> 
> PGHOST
> 
> PGPORT
> 
> PGUSER

默认连接参数

PG\_COLOR

规定在诊断消息中是否使用颜色。可能的值为always、 auto、never。

**诊断**

在有困难时，可以在REINDEX和psql中找潜在问题和错误消息的讨论。数据库服务器必须运行在目标主机上。同样，任何libpq前端库使用的默认连接设置和环境变量都将适用于此。

**注释**

reindexdb可能需要多次连接到数据库服务，每一次都会询问一个口令。在这种情况下使用一个~/.pgpass文件会更方便。

**示例**

要重索引数据库test：

$ reindexdb test

要重索引名为abcd的数据库中的表foo和索引bar：

$ reindexdb --table foo --index bar abcd

**参见**

SQL命令REINDEX

## vacuumdb

vacuumdb — 对一个瀚高数据库进行垃圾收集和分析

**命令**

vacuumdb \[connection-option...\] \[option...\] \[ --table | -t table \[( column

\[,...\] )\] \]... \[dbname\]

vacuumdb \[connection-option...\] \[option...\] --all | -a

**描述**

vacuumdb是用于清理数据库的工具。vacuumdb也将产生由数据库查询优化器所使用的内部统计信息。

vacuumdb是 SQL 命令VACUUM的一个包装器。在通过这个工具和其他方法访问服务器来清理和分析数据库之间没有实质性的区别。

**选项**

vacuumdb接受下列命令行参数：

\-a

\--all

清理所有数据库。

\[-d\] dbname

\[--dbname=\]dbname

指定要被清理或分析的数据库名。如果没有被指定并且没有使用-a（或--all），数据库名将从环境变量PGDATABASE中读出。如果环境变量也没有设置，指定给该连接的用户名将用作数据库名。

\--disable-page-skipping

根据可见性地图的内容禁用跳过页面。

\--echo

回显vacuumdb生成并发送给服务器的命令。

\-f

\--full

执行”完全”清理。

\-F

\--freeze

强有力地”冻结”元组。

\-j njobs

\--jobs=njobs

通过同时运行njobs 个命令来并行执行清理或者分析命令。这个选项会减少处理的时间， 但是它也会增加数据库服务器的负载。

vacuumdb将开启 njobs个到数据库的连接，因此请确认你的max\_connections 设置足够高以容纳所有的连接。

注意如果某些系统目录被并行处理，使用这种模式加上 -f（FULL）选项可能会导致死锁失败。

\--min-mxid-age mxid\_age

仅在multixact ID 年龄至少为mxid\_age的表上执行清空或分析命令。 此设置对于确定要处理的表的优先级比较有用，以防止multixact ID 回绕。

对于此选项的用途，关系的multixact ID年龄是主关系及其关联的TOAST表的年龄中最大的，如果存在的话。 由于vacuumdb发出的命令在需要时还将处理TOAST表的关系，它无需单独考虑。

\--min-xid-age xid\_age

仅在事务ID 年龄至少为xid\_age的表上执行清空或分析命令。 此设置对于确定要处理的表的优先级比较有用，以防止事务ID 回绕。

对于此选项的用途，关系的事务ID年龄是主关系及其关联的TOAST表的年龄中最大的，如果存在的话。由于vacuumdb发出的命令在需要时还将处理TOAST表的关系，它无需单独考虑。

\-q

\--quiet

不显示进度消息。

\--skip-locked

跳过无法立即锁定以进行处理的关系。

\-t table \[ (column \[,...\]) \]

\--table=table \[ (column \[,...\]) \]

只清理或分析table。列名只能和--analyze或--analyze-only选项一起被指定。通过写多个-t开关可以清理多个表。

| 提示： |
| --- |
| 如果你指定列，你可能必须转义来自 shell 的括号（见下面的例子）。 |

\-v

\--verbose

在处理期间打印详细信息。

\-V

\--version

打印vacuumdb版本并退出。

\-z

\--analyze

也计算优化器使用的统计信息。

\-Z

\--analyze-only

只计算优化器使用的统计信息（不清理）。

\--analyze-in-stages

与--analyze-only相似，只计算优化器使用的统计信息（不做清理）。使用不同的配置设置运行分析的几个（目前是 3个）阶段以更快地产生可用的统计信息。

这个选项对分析一个刚从转储恢复或者通过pg\_upgrade得到 的数据库有用。这个选项将尝试尽可能快地创建一些统计信息来让该数据库可用，然后在后续的阶段中产生完整的统计信息。

\-?

\--help

显示有关vacuumdb命令行参数的帮助并退出。

vacuumdb也接受下列命令行参数用于连接参数：

\-h host

\--host=host

指定运行服务器的机器的主机名。如果该值以一个斜线开始，它被用作 Unix 域套接字的目录。

\-p port

\--port=port

指定服务器正在监听连接的 TCP 端口或本地 Unix 域套接字文件扩展。

\-U username

\--username=username

要作为哪个用户连接。

\--maintenance-db=dbname

指定要连接到来发现哪些其他数据库应该被清理的数据库名。如果没有指定，将使用highgo数据库。而如果它也不存在，将使用template1。

**环境**

> PGDATABASE
> 
> PGHOST
> 
> PGPORT
> 
> PGUSER

默认连接参数

> PG\_COLOR

规定在诊断消息中是否使用颜色。可能的值为always、 auto、never。

和大部分其他数据库工具相似，这个工具也使用libpq支持的环境变量。

**诊断**

在有困难时，可以在VACUUM和psql中找潜在问题和错误消息的讨论。数据库服务器必须运行在目标主机上。同样，任何libpq前端库使用的默认连接设置和环境变量都将适用于此。

**注释**

vacuumdb可能需要多次连接到数据库，每次都询问一个口令。在这种情况下有一个~/.pgpass文件会很方便。

**示例**

要清理数据库test：

$ vacuumdb test

要清理和为优化器分析一个名为bigdb的数据库：

$ vacuumdb --analyze bigdb

要清理在名为xyzzy的数据库中的一个表foo，并且为优化器分析该表的bar列：

$ vacuumdb --analyze --verbose --table 'foo(bar)' xyzzy

**参见**

SQL命令VACUUM