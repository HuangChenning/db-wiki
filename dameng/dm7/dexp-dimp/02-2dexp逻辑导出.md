---
title: "2 dexp逻辑导出"
book: "DM7 dexp和dimp使用手册"
version: "DM7"
source: "temp/doc/special/DM7°ïÖúÎÄµµ.chm#~htm/dexp和dimp使用手册.htm"
tags:
  - dameng
  - dm7
  - dexp-dimp
---

`dexp`工具可以对本地或者远程数据库进行数据库级、用户级、模式级和表级的逻辑备份。备份的内容非常灵活，可以选择是否备份索引、数据行和权限，是否忽略各种约束（外键约束、非空约束、唯一约束等），在备份前还可以选择生成日志文件，记录备份的过程以供查看。

## 2.1 使用dexp工具

`dexp`工具需要从命令行启动。在`cmd`命令行工具中找到`dexp`所在安装目录`/dmdbms/bin`，输入`dexp`和参数后回车。参数在下一节详细介绍。

语法如下：

```
dexp PARAMETER= { PARAMETER= }
```

`PARAMETER`：`dexp`参数。多个参数之间排列顺序无影响，参数之间使用空格间隔。

``：参数取值。

例如，将用户名和密码均为`SYSDBA`，`IP`地址为`192.168.0.248`，端口号为8888的数据库采用`FULL`方式完全导出。`/user/data`为数字证书路径。导出文件名为`db_str.dmp`，导出的日志文件名为`db_str.log`，导出文件的路径为`/mnt/dexp/data`。

```
./dexp USERID=SYSDBA/SYSDBA@192.168.0.248:8888#/user/data FILE=db_str.dmp DIRECTORY=/mnt/dexp/data LOG=db_str.log FULL=Y
```

## 2.2 dexp参数一览表

本节提拱`dexp`的参数一览表，供用户快速参考。

表`2.1 dexp`参数一览表

| 参数 | 含义 | 备注 |
| --- | --- | --- |
| USERID | 用户名/口令@主机名:端口号#证书路径。 例如： SYSDBA/SYSDBA@server:5236#ssl_path@ssl_pwd | 必选。其中主机名、端口号和证书路径为可选项 |
| FILE | 明确指定导出文件名称 | 可选。如果缺省该参数，则导出文件名为dexp.dmp |
| DIRECTORY | 导出文件所在目录 | 可选 |
| FULL | 导出整个数据库(N) | 可选，四者中选其一。缺省为SCHEMA |
| OWNER | 用户名列表，导出一个或多个用户所拥有的所有对象 |  |
| SCHEMAS | 模式列表，导出一个或多个模式下的所有对象 |  |
| TABLES | 表名列表，导出一个或多个指定的表或表分区 |  |
| QUERY | 用于指定对导出表的数据进行过滤的条件。 | 可选 |
| PARALLEL | 用于指定导出的过程中所使用的线程数目 | 可选 |
| TABLE_PARALLEL | 用于指定导出每张表所使用的线程数,在MPP模式下会转换成单线程 | 可选 |
| TABLE_POOL | 用于设置导出过程中存储表的缓冲区个数 | 可选 |
| EXCLUDE | 1. 导出内容中忽略指定的对象。对象有CONSTRAINTS、INDEXES、ROWS、TRIGGERS、GRANTS和TABLESPACE。 比如：EXCLUDE= (CONSTRAINTS,INDEXES) 2. 忽略指定的表，使用TABLES:INFO格式，如果使用表级导出方式导出，则使用TABLES:INFO格式的EXCLUDE无效。例如：EXCLUDE= TABLES：'table1','table2' | 可选 |
| INCLUDE | 导出内容中包含指定的对象 例如：INCLUDE=(CONSTRAINTS,INDEXES) 或者INCLUDE=TABLES:'table1','table2' | 可选 |
| CONSTRAINTS | 导出约束 (Y) | 可选。 此处单独设置与和EXCLUDE/INCLUDE中批量设置功能一样。设置一个即可 |
| TABLESPACE | 导出的对象定义是否包含表空间(Y) |  |
| GRANTS | 导出权限 (N) |  |
| INDEXES | 导出索引 (Y) |  |
| TRIGGERS | 导出触发器（Y） |  |
| ROWS | 导出数据行 (Y) |  |
| LOG | 明确指定日志文件名称 | 可选，如果缺省该参数，则导出文件名为dexp.log |
| NOLOGFILE | 不使用日志文件(N) | 可选 |
| NOLOG | 屏幕上不显示日志信息(N) | 可选 |
| LOG_WRITE | 日志信息实时写入文件 (N) | 可选 |
| DUMMY | 交互信息处理: 打印(P), 所有交互都按YES处理(Y),NO(N)。默认为NO，不打印交互信息。 | 可选 |
| PARFILE | 参数文件名，如果dexp的参数很多，可以存成参数文件 | 可选 |
| FEEDBACK | 每 x 行显示进度 (0) | 可选 |
| COMPRESS | 是否压缩导出数据文件(N) | 可选 |
| ENCRYPT | 导出数据是否加密 (N) | 可选， 和ENCRYPT同时使用 |
| ENCRYPT_PASSWORD | 导出数据的加密密钥 |  |
| ENCRYPT_NAME | 导出数据的加密算法 | 可选。 和ENCRYPT、ENCRYPT_PASSWORD同时使用。缺省为CYT_ID_RC4 |
| FILESIZE | 用于指定单个导出文件大小的上限。可以按字节[B]、K[B]、M[B]、G[B]的方式指定大小 | 可选 |
| DROP | 导出后删除原表，但不级联删除 (N) | 可选 |
| DESCRIBE | 导出数据文件的描述信息，记录在数据文件中 | 可选 |
| LOCAL | MPP环境下使用MPP_LOCAL方式登录(N) | 可选 |
| HELP | 显示帮助信息 | 可选 |

> 每个参数含义后面的括号内为(N)则表示该参数缺省为否，为(Y)则表示为是，虽然参数大部分为可选参数，但后台这些参数都会传到服务器，此时参数的值就是缺省值。

## 2.3 dexp参数详解

本节详细介绍`dexp`的各个参数。

### 2.3.1特殊参数

特殊参数中介绍了必选参数的和最常用的可选参数。

#### 2.3.1.1 USERID

`USERID`用于连接服务器。必选参数。

语法如下：

```
USER/PWD@SERVER:PORT#SSLPATH@SSLPWD
```

`USER/PWD`：用户名和密码，必写。

`SERVER:PORT`：服务器`IP`地址和端口号。缺省情况下默认为本地服务器和端口号`LOCALHOST:5236`。当服务器为本机时，`SERVER:PORT` 可直接写`LOCALHOST`。例如：`192.168.0.248:8888`。

`SSLPATH@SSLPWD`：通信加密的`SSL`数字证书路径和密码，缺省为不使用加密。数字证书路径由用户自己创建，将相应的证书需放入该文件夹中。其中服务器证书必须与 `dmserver` 目录同级，客户端目录可以任意设置。

当连接其他服务器时，`SERVER:PORT`需写上`IP`地址和`PORTNUM`。

> PWD密码中带有特殊字符（/,@.:等），需要外加三层双引号（""" """）进行转义。

`PWD`密码中带有特殊字符的具体转义处理规则：

登录时，密码中含有`/,@.:`等特殊字符时，密码需要外加三层双引号（`""" """`）进行转义。下面使用一个例子进行解析。例如：密码为`aaa/aaa`，首先，`dexp`要求对含有特殊字符的密码内部进行转义（外加一层双引号），写成`"aaa/aaa"`。其次，要将转义后的内容作为一个整体传给`dexp`（外加一层双引号），写成`""aaa/aaa""`。最后，整个内容需要作为一个整体传给操作系统（外加一层双引号），因此写成`"""aaa/aaa"""`。

例如，使用上面的规则举例，密码为`SYSDBA/,@.:`，端口号为5236的本地服务器，`USERID`可写成如下所示：

```
./dexp USERID=SYSDBA/"""SYSDBA/,@.:"""@LOCALHOST:PORT
```

#### 2.3.1.2 FILE

`FILE`用于明确指定导出的文件（可以包含路径），可以包含多个文件，用逗号分隔。可选参数，如果不选用`FILE`参数（来明确指定导出文件名称），那么默认导出文件名称为`dexp.dmp`。

语法如下：

```
FILE=<文件>
```

例如，设置`FILE=db_str.dmp`，导出文件名为`db_str.dmp`。

```
./dexp USERID=SYSDBA/SYSDBA FILE=db_str.dmp LOG=db_str.log FULL=Y DIRECTORY=/mnt/data/dexp
```

例如，`FILE`指定的文件也可以包含路径，设置`FILE=/mnt/db_str.dmp`。

```
./dexp USERID=SYSDBA/SYSDBA FILE=/mnt/db_str.dmp LOG=db_str.log FULL=Y
```

> 如果FILE指定的文件包含生成路径，则忽略DIRECTORY中的路径； 如果FILE没有指定路径时，使用DIRECTORY中指定的路径； 如果FILE和DIRECTORY都没有指定路径，则使用系统当前路径。

文件也可以在生成过程中自动扩展成多个。首先，文件名需要包含通配符`%U`，用于作为自动扩充文件的文件名模板。`%U`表示为2个字符宽度的数字，由系统自动生成，起始为01。其次，使用`FILESIZE`参数来指定文件的大小。

例如，设置`FILE=db_str%U.dmp`，导出文件名为`db_str%U.dmp`。同时使用`%U`对文件进行扩展，使用`FIZESIZE=128m`指定文件大小。

```
./dexp USERID=SYSDBA/SYSDBA FILE=db_str%U.dmp LOG=db_str.log FULL=Y DIRECTORY=/mnt/data/dexp FILESIZE=128m
```

#### 2.3.1.3 LOG

`LOG`用于明确指定导出的日志文件名称（可以包含路径），可以包含多个文件，用逗号分隔。可选参数。如果不选用`LOG`参数（来明确指定日志文件名称），那么默认导出日志文件名称为`dexp.log`。

语法如下：

`LOG=<`文件名>

例如，指定日志文件名为`db_str.log`。

```
./dexp USERID=SYSDBA/SYSDBA FILE=db_str.dmp LOG=db_str.log FULL=Y DIRECTORY=/mnt/data/dexp
```

文件也可以在生成过程中自动扩展成多个。首先，文件名需要包含通配符`%U`，用于作为自动扩充文件的文件名模板。`%U`表示为2个字符宽度的数字，由系统自动生成，起始为01。其次，使用`FILESIZE`参数来指定文件的大小。

例如，指定日志文件名为`db_str%U.log`。同时使用`%U`对文件进行扩展，使用`FIZESIZE=128m`指定文件大小。

```
./dexp USERID=SYSDBA/SYSDBA FILE=db_str.dmp LOG=db_str%U.log FULL=Y DIRECTORY=/mnt/data/dexp FILESIZE=128m
```

> 如果LOG指定的文件包含生成路径，则忽略DIRECTORY中的路径； 如果LOG没有指定路径时，使用DIRECTORY中指定的路径； 如果LOG和DIRECTORY都没有指定路径，则使用系统当前路径。

`LOG`文件记载了导出对象的统计信息。供用户查看导出内容。

`LOG`内容具体介绍如下：

1.如果导出级别为`TABLES`，那么日志信息包含一张或多张表的索引、权限、数据行数。

2.如果导出级别为`SCHEMAS`，那么日志信息只包含一个或多个模式中的对象统计信息，每个模式下的内容具体有：

- 导出`SEQUENCE`、`VIEW`、`COMMENT`、`PROCEDURE`、`SYNONYM`、`DBLINK`、`TRIGGER`、`PACKAGE`、`OBJECT`、`CLASS_BODY`和`DOMAIN`等对象的个数和名称，以及对象的权限。
- 依次导出表的索引、权限、数据行数。
3. 如果导出级别为`OWNER`，那么日志内容包含一个或多个用户所拥有的所有模式中的对象统计信息，每个模式下的内容和导出级别为`SCHEMAS`时一样。
4. 如果导出级别为`FULL`，那么日志内容除了包含所有模式中的对象信息，还包括系统包和系统视图。

和`LOG`有关的参数还有`NOLOGFILE`、`NOLOG`和`LOG_WRITE`。`NOLOGFILE=Y`用于设置不使用日志文件。`NOLOG=Y`用于设置不在屏幕上显示日志信息。`LOG_WRITE=Y`用于设置日志的实时打印（到日志文件）功能。

#### 2.3.1.4 DIRECTORY

`DIRECTORY`用于指定导出文件及日志文件生成的路径。可选参数，缺省为导出到`dexp`所在路径。

语法如下：

```
DIRECTORY=
```

``：导出文件和日志文件生成的路径。

如果`FILE`和`LOG`参数指定的文件包含生成路径，则`FILE`和`LOG`参数中指定的路径将替代`DIRECTORY`所指定的路径；如果`FILE`和`LOG`参数指定的文件未包含路径信息，则文件将被生成到`DIRECTORY`指定的目录下；如果都没有指定路径，程序将根据当前的运行环境来设置相应的导出路径，一般为当前路径。

例如，没有指定路径，使用当前路径。

```
./dexp USERID=SYSDBA/SYSDBA FILE=db_str.dmp LOG=db_str.log FULL=Y
```

例如，指定路径`/mnt/data/dexp`。

```
./dexp USERID=SYSDBA/SYSDBA FILE=db_str.dmp LOG=db_str.log FULL=Y DIRECTORY=/mnt/data/dexp
```

> FILE和LOG中指定的路径，优先级高于DIRECTORY中指定的路径。 当FILE和LOG不指定路径时，才使用DIRECTORY指定的路径。 如果都没有指定路径，则使用系统当前路径。

#### 2.3.1.5 四种级别的导出方式

针对数据库对象，有`FULL`、`OWNER`、`SCHEMAS`、`TABLES`四种导出方式可供选择。一次导出只能指定一种方式。可选参数，缺省为`SCHEMA`。

##### 2.3.1.5.1 FULL

`FULL`方式导出整个数据库。

语法如下：

```
FULL=Y
```

例如，设置`FULL=Y`，导出整个数据库，导出数据库文件和日志文件放在路径`/mnt/data/dexp`下。

```
./dexp USERID=SYSDBA/SYSDBA FILE=db_str.dmp LOG=db_str.log FULL=Y DIRECTORY=/mnt/data/dexp
```

##### 2.3.1.5.2 OWNER

`OWNER`方式导出一个或多个用户拥有的所有对象。

语法如下：

`OWNER=<`用户名`>{,<`用户名`>}`

例如，设置`OWNER=USER01`，导出用户`USER01`所拥有的对象全部导出。

```
./dexp USERID=SYSDBA/SYSDBA FILE=db_str.dmp LOG=db_str.log OWNER=USER01 DIRECTORY=/mnt/data/dexp
```

##### 2.3.1.5.3 SCHEMAS

`SCHEMAS`方式的导出一个或多个模式下的所有对象。

语法如下：

`SCHEMAS=<`模式名`>{,<`模式名`>}`

例如，设置`SCHEMAS=USER01`，导出模式`USER01`模式下的所有对象。

```
./dexp USERID=SYSDBA/SYSDBA FILE=db_str.dmp LOG=db_str.log SCHEMAS=USER01 DIRECTORY=/mnt/data/dexp
```

> 一般情况下，OWNER与SCHEMAS导入导出是相同的。 但是用户可以包含多个模式，在这种情况下SCHEMAS的导入导出是OWNER导入导出的一个子集。

##### 2.3.1.5.4 TABLES

`TABLES`方式导出和导入一个或多个指定的表或表分区。导出所有数据行、约束、索引等信息。

语法如下：

```
TABLES=<表名>{,<表名>}
```

例如，设置`TABLES=table1,table2`，导出`table1,table2`两张表的所有数据和信息。

```
./dexp USERID=SYSDBA/SYSDBA FILE=db_str.dmp LOG=db_str.log TABLES=table1,table2 DIRECTORY=/mnt/data/dexp
```

和`TABLES`导出有关的参数还有`QUERY`、`EXCLUDE`和`INCLUDE`，都是用来设置过滤条件的。

##### 2.3.1.5.5 OWNER、SCHEMAS、TABLES的书写规定

1. 用户名、模式名和表名的书写规定
- 对于输入的用户名、模式名和表名，工具都会自动转换为大写。

例如：输入的命令`TABLES=t1`，那么实际处理的表是`T1`。

- 对于小写的用户名、模式名和表名，为了不转换为大写，需要转义。

转义步骤如下：><span lang=EN-US style='font-family:"Courier New";mso-hansi-font-family:Calibri'><span style='mso-element:field-begin'> <!第一步，><!><!如果想输入小写的名字不被转成大写，`dexp`要求将名称使用双引号扩起来。例如：名称为`tab1`，要写成`"tab1"`。><span lang=EN-US style='font-family:"Courier New";mso-hansi-font-family:Calibri'><span style='mso-element:field-begin'> <!第二步，><!另外，操作系统要求将传入的名称使用双引号括起来作为一个整体，同时要求内层的双引号还需要被转义。所以最终写成`"\"tab1\""`。

例如，表名为小写`tabname`，语句中应该写为`"\"tabname\""`。

```
./dexp USERID=SYSDBA/SYSDBA FILE=db_str.dmp LOG=db_str.log TABLES="\"tabname\""
```

- 如果含有特殊字符(双引号、单引号、空格、逗号等)的用户名、模式名和表名需要转义。具体规则如下：

转义步骤如下：第一步， `dexp`要求对含有特殊字符的对象名称需要使用双引号括起来，同时特殊字符需要被转义（使用双引号"）。例如:表名为`tab1"`，需写成`"tab1"""`； 第二步，另外，操作系统要求将传入的名称使用双引号括起来作为一个整体，同时要求内层的双引号和特殊字符还需要被转义。所以最终写成：`"\"tab1\"\"\""`。

例如，表名为小写`tabname"`，语句中应该写为`"\"tabname\"\"\""`。

```
./dexp USERID=SYSDBA/SYSDBA@192.168.0.248:8888 FILE=db_str.dmp LOG=db_str.log TABLES="\"tabname\"\"\""
```

2.如何转义双引号

`1) dexp`和`dimp`要求使用双引号"对双引号内的双引号转义。

`2) WINDOWS`命令行，使用双引号"或者反斜杠\对双引号内的双引号转义。

`3) LINUX`命令行，使用反斜杠\对双引号内的双引号转义。

### 2.3.2普通参数

普通参数中介绍了具有一些专门用途的可选参数。

#### 2.3.2.1 QUERY

`QUERY`用于指定过滤条件来对表数据进行导出。可选参数。

语法如下：

```
QUERY=""
```

``：过滤条件。更详细了解请参考《`DM_SQL`》的`。

例如，导出`OTHER.READER`表中满足`"WHERE AGE=19"`条件的数据。

```
./dexp USERID=SYSDBA/SYSDBA FILE=db_str.dmp LOG=db_str.log TABLES=OTHER.READER QUERY="WHERE AGE=19"
```

#### 2.3.2.2 PARALLEL

`PARALLEL`用于指定导出的过程中所使用的线程数目。可选参数，缺省为单线程。如果`CPU`核心数为N的话，那一般来说`PARALLEL`为N或者`N+1`最合适。

语法如下：

```
PARALLEL=
```

``：线程数。整数类型，取值范围：1-100。

例如，设置`PARALLEL=2`时则线程数为2。

```
./dexp USERID=SYSDBA/SYSDBA FILE=db_str.dmp LOG=db_str.log FULL=Y DIRECTORY=/mnt/data/dexp PARALLEL=2
```

#### 2.3.2.3 TABLE_PARALLEL

`TABLE_PARALLEL`用于指定导出每张表所使用的线程数。可选参数，缺省为单线程。如果`CPU`核数为N的话，那一般来说`TABLE_PARALLEL`为N或者`N+1`最合适。在`MPP`模式下会转换成单线程。

语法如下：

```
TABLE_PARALLEL=
```

``：线程数。整数类型，取值范围1-50。

例如，设置`TABLE_PARALLEL=3`时则线程数为3。

```
./dexp USERID=SYSDBA/SYSDBA FILE=db_str.dmp LOG=db_str.log FULL=Y DIRECTORY=/mnt/data/dexp TABLE_PARALLEL=3
```

#### 2.3.2.4 TABLE_POOL

`TABLE_POOL`用于设置导出过程中存储表数据的缓冲区个数。可选参数。

语法如下：

```
TABLE_POOL=
```

``：存储表数据的缓冲区个数。缺省值为1。整数类型，取值范围：1-20。

> TABLE_PARALLEL 固定的情况下，导出时间随着TABLE_POOL个数的增加而减少。当TABLE_POOL稍大于TABLE_PARALLEL时结果为最优。

例如，设置`TABLE_POOL=3`时。

```
./dexp USERID=SYSDBA/SYSDBA FILE=db_str.dmp LOG=db_str.log FULL=Y DIRECTORY=/mnt/data/dexp TABLE_POOL=3
```

#### 2.3.2.5 EXCLUDE

`EXCLUDE`用来批量设置导出时忽略的对象种类。可选参数。

语法如下：

`EXCLUDE=(<`对象种类名`>{,<`对象种类名`>})`

或者

```
EXCLUDE=TABLES:'<表名>'{,'<表名>'}
```

<对象种类名>：包括`CONSTRAINTS`、`INDEXES`、`ROWS`、`TRIGGERS`、`GRANTS`。

> 如果导出方式为TABLES表级导出时， 则“EXCLUDE=TABLES:'<表名>'{,'<表名>'}”方式将不起作用。

例如，设置`EXCLUDE=(CONSTRAINTS)`，将当前用户下的`table1`、`table2`的对象信息导出时不导出约束。

```
./dexp SYSDBA/SYSDBA FILE=/mnt/data/db_str.dmp LOG=db_str.log TABLES=table1,table2 EXCLUDE=(CONSTRAINTS)
```

#### 2.3.2.6 INCLUDE

`INCLUDE`用来批量设置导出时包含的对象种类。可选参数。

语法如下：

`INCLUDE=(<`对象种类名`>{,<`对象种类名`>})`

或者

```
INCLUDE=TABLES:'<表名>'{,'<表名>'}
<对象种类名>：CONSTRAINTS、INDEXES、ROWS、TRIGGERS或GRANTS。
```

例如，设置`INCLUDE=(CONSTRAINTS`、`INDECES)`，指明将当前用户下的`table1`的对象只导出约束和索引信息。

```
./dexp USERID=SYSDBA/SYSDBA FILE=db_str.dmp LOG=db_str.log TABLES=table1 DIRECTORY=/mnt/data/dexp INCLUDE=(CONSTRAINTS、INDECES)
```

#### 2.3.2.7 CONSTRAINTS、TABLESPACE、GRANTS、INDEXES、TRIGGERS、ROWS

这些参数用来指定某类对象是否被导出。类别分别为约束、表空间、权限、索引、触发器和数据。

语法如下：

```
CONSTRAINTS=N/Y
TABLESPACE=N/Y
GRANTS=Y/N
INDEXS=N/Y
TRIGGERSS=N/Y
ROWS=N/Y
```

`CONSTRAINTS=N`：设置不导出约束。可选参数。缺省该参数为Y，导出约束。

`TABLESPACE=N`：设置导出的对象定义中不包含表空间。可选参数。缺省该参数为Y，包含表空间。

`GRANTS=Y`：设置导出权限。可选参数。缺省该参数为N，不导出权限。

`INDEXES=N`：设置不导出索引。可选参数。缺省该参数为Y，导出索引。

`TRIGGERS=N`：设置不导出触发器。可选参数。缺省该参数为Y，导出触发器。

`ROWS=N`：设置不导出数据。可选参数。缺省该参数为Y，导出数据。

例如，设置`ROWS=N`不导出表中的数据。

```
./dexp USERID=SYSDBA/SYSDBA FILE=db_str.dmp NOLOGFILE=Y FULL=Y DIRECTORY=/mnt/data/dexp ROWS=N
```

> 此处，对象（CONSTRAINTS、TABLESPACE、GRANTS、INDEXES、TRIGGERS、ROWS）分别单独设置，和EXCLUDE/INCLUDE中批量设置功能一样。设置一个即可。 如果单独设置和批量设置同时出现时，那么以最后出现的那个为准。

#### 2.3.2.8 NOLOGFILE

`NOLOGFILE`用于设置是否使用日志文件。可选参数。

语法如下：

```
NOLOGFILE=Y/N
```

Y：不使用。

N或缺省参数：使用。

> 一旦设置NOLOGFILE=Y不使用日志文件。此时即使存在LOG参数，LOG参数也为无效。

例如，设置`NOLOGFILE=Y`，不使用日志文件。

```
./dexp USERID=SYSDBA/SYSDBA FILE=db_str.dmp NOLOGFILE=Y FULL=Y DIRECTORY=/mnt/data/dexp
```

#### 2.3.2.9 NOLOG

`NOLOG`设置屏幕上是否显示日志信息。可选参数。

语法如下：

```
NOLOG=Y/N
```

Y：不显示。

N或缺省参数：显示。

例如，设置`NOLOG=Y`屏幕不显示日志信息。

```
./dexp USERID=SYSDBA/SYSDBA FILE=db_str.dmp NOLOG=Y FULL=Y DIRECTORY=/mnt/data/dexp
```

#### 2.3.2.10 LOG_WRITE

`LOG_WRITE`用于日志信息实时写入日志文件。可选参数。

语法如下：

```
LOG_WRITE=Y/N
```

Y：一边将日志内容打印到屏幕上，一边将日志内容写入日志文件。

N或缺省参数：日志内容先在屏幕上全部打印完毕再写入日志文件。

#### 2.3.2.11 DUMMY

`DUMMY`用于设置交互信息处理。可选参数，缺省使用P打印交互信息。

语法如下：

```
DUMMY=P/Y/N
```

P：打印交互信息，默认方式。

Y：不打印交互信息，所有交互都按`YES`处理。

N：不打印交互信息，所有交互都按`NO`处理。

#### 2.3.2.12 PARFILE

`PARFILE`用于将常用的参数设置保存到文件中，然后使用参数文件`PARFILE`进行导出、导入操作。可选参数。

语法如下：

```
PARFILE=
```

``：`PARFILE`文件的绝对路径。

```
例如，设置PARFILE=/mnt/data/dexp/para.txt。
./dexp USERID=SYSDBA/SYSDBA PARFILE=/mnt/data/dexp/para.txt
```

其中，参数文件`/mnt/data/dexp/para.txt`的内容如下：

```
FILE=db_str.dmp
LOG=db_str.log
TABLES=table1
DIRECTORY=/mnt/data/dexp
```

#### 2.3.2.13 FEEDBACK

`FEEDBACK`用来指明在导出数据的过程中每间隔多少行打印一次进度信息。可选参数。

当参数缺省时，默认为0，只打印导出表的总行数。

语法如下：

```
FEEDBACK=
```

``：行数。

例如，将整个数据库导出到文件`dexp.dmp`中，并且在导出的过程中每隔100行打印一次进度信息。

```
./dexp SYSDBA/SYSDBA FULL=Y FILE=dexp.dmp DIRECTORY=/mnt/data/dexp FEEDBACK=100
```

#### 2.3.2.14 COMPRESS

`COMPRESS`指定是否压缩导出文件。可选参数。缺省为不压缩。

语法如下：

```
COMPRESS=Y/N
```

Y：压缩。

N或缺省参数：不压缩

#### 2.3.2.15 ENCRYPT、ENCRYPT_PASSWORD、ENCRYPT_NAME

这三个参数用来设置导出文件加密。可选参数。

语法如下：

```
ENCRYPT=Y
ENCRYPT_PASSWORD=<加密密钥>
ENCRYPT_NAME=<加密算法>
```

`ENCRYPT=Y`：设置导出文件加密。如果设置`ENCRYPT=Y`，那么默认`COMPRESS=Y`，先压缩后加密。

`ENCRYPT_PASSWORD=<`加密密钥>：设置加密密钥。

`ENCRYPT_NAME=<`加密算法>：设置加密算法。缺省为`RC4`。

> 加密算法： DES_ECB 、DES_CBC 、DES_CFB、DES_OFB、DESEDE_ECB、DESEDE_CBC 、DESEDE_CFB、DESEDE_OFB 、AES128_ECB 、 AES128_CBC 、AES128_CFB 、AES128_OFB 、AES192_ECB 、AES192_CBC 、AES192_CFB 、AES192_OFB 、AES256_ECB 、 AES256_CBC 、AES256_CFB 、AES256_OFB 、RC4

例如，设置导出文件加密，密钥`abcdefg`，加密算法为`DES_CBC`。

```
./dexp SYSDBA/SYSDBA DIRECTORY=/mnt/data/dexp FILE=dk15.dmp LOG=db_str15.log
ENCRYPT=Y ENCRYPT_PASSWORD=abcdefg ENCRYPT_NAME=DES_CBC FULL=Y
```

> ENCRYPT、ENCRYPT_PASSWORD、ENCRYPT_NAME需一起使用。其中ENCRYPT_NAME可以缺省（ 缺省值RC4）。

#### 2.3.2.16 FILESIZE

`FILESIZE`用于指定单个导出文件（`FILE`）大小或日志文件（`LOG`）大小的上限。可以按字节`[B]`、`K[B]`、`M[B]`、`G[B]`的方式指定大小。可选参数。

使用`FILESIZE`参数时，`FILE`（或`LOG`）必须使用`%U`对名称进行自动扩展。否则导出第一个文件之后将报错。如果`FILE`（或`LOG`）不使用`%U`对名称进行自动扩展，那么即使设置了`FILESIZE`也不起作用。`FILE`和`LOG`同时使用`%U`时，`FILESIZE`参数只需指定一次。

语法如下：

```
FILESIZE=
```

``：单个导出文件上限。整数类型，取值范围：`128M-`系统最大值。

以下示例表示以`FULL`方式导出实例，每个导出文件大小为`128m`，文件名以`data01.dmp`自动扩展，存储位置为`/mnt/data/dexp`目录。

```
./dexp USERID=SYSDBA/SYSDBA DIRECTORY=/mnt/data/dexp FILE=data%u.dmp LOG=data%u.log FILESIZE=128m FULL=Y
```

> dexp执行过程中可能遇到单个文件过大的问题。解决办法是通过FILESIZE 参数来设置单个导出文件上限，导出文件名称按照FILE参数中描述的使用%u来自动扩展。这样在按照FILESIZE大小导出到第一个文件之后，会自动生成下一个导出文件。

#### 2.3.2.17 DROP

`DROP`用于设置导出后是否删除原表。可选参数。

语法如下：

```
DROP=Y/N
```

`Y:` 导出后删除原表，但不级联删除。

N或缺省参数: 导出后不删除原表。

#### 2.3.2.18 DESCRIBE

`DESCRIBE`用于设置是否导出数据文件的描述信息，记录在数据文件中。可选参数。

语法如下：

```
DESCRIBE=Y/N
```

`Y:` 导出数据文件的描述信息，记录在数据文件中

N或缺省参数: 导出的数据文件中没有备注信息。

#### 2.3.2.19 LOCAL

`LOCAL`只用于在`MPP`环境下，是否使用`LOCAL`方式登录，缺省为不使用。可选参数。

语法如下：

```
LOCAL=Y/N
```

`Y:`表示用户在登录时为`LOCAL`本地登录方式，即只登录指定的节点，操作数据也只是本节点的数据。

`N:`表示不使用，为`GLOBOL`全局登录方式，即操作数据是所有节点上相关数据。

#### 2.3.2.20 HELP

输入`dexp HELP` 即可查看帮助信息。

语法如下：

```
HELP
```

例如，使用`HELP`查看帮助信息。

```
./dexp HELP
```

`HELP`信息会逐个显示所有参数的大致信息，供用户快速参考。
