---
title: "3 dimp逻辑导入"
book: "DM7 dexp和dimp使用手册"
version: "DM7"
source: "temp/doc/special/DM7°ïÖúÎÄµµ.chm#~htm/dexp和dimp使用手册.htm"
tags:
  - dameng
  - dm7
  - dexp-dimp
---

`dimp`逻辑导入工具利用`dexp`工具生成的备份文件对本地或远程的数据库进行联机逻辑还原。`dimp`导入是`dexp`导出的相反过程。还原的方式可以灵活选择，如是否忽略对象存在而导致的创建错误、是否导入约束、是否导入索引、导入时是否需要编译、是否生成日志等。

## 3.1 使用dimp工具

`dimp`工具需要从命令行启动。在`cmd`命令行工具中找到`dimp`所在安装目录`/dmdbms/bin`，输入`dimp`和参数后回车。参数在下一节详细介绍。

语法如下：

```
dimp PARAMETER=value { PARAMETER=value }
```

`PARAMETER`：`dimp`参数。多个参数之间排列顺序无影响，参数之间使用空格间隔。

`value`：参数取值。

例如，将逻辑备份导入到用户名和密码为`SYSDBA`，`IP`地址为`192.168.0.248`，端口号为8888的数据库采用`FULL`方式完全导出。导入文件名为`db_str.dmp`，导入的日志文件名为`db_str.log`，路径为`/mnt/data/dexp`。

```
./dimp USERID=SYSDBA/SYSDBA@192.168.0.248:8888 FILE=db_str.dmp DIRECTORY=/mnt/data/dexp LOG=db_str.log FULL=Y
```

## 3.2 dimp参数一览表

本节提拱`dimp`的参数一览表，供用户快速参考。

表`3.1 dimp`参数一览表

| 参数 | 含义 | 备注 |
| --- | --- | --- |
| USERID | 用户名/口令@主机名:端口号#证书路径 例如： SYSDBA/SYSDBA@server:5236#ssl_path@ssl_pwd | 必选。其中主机名、端口号和证书路径为可选项 |
| FILE | 输入文件，即dexp导出的文件 | 必选 |
| DIRECTORY | 导入文件所在目录 | 可选 |
| FULL | 导入整个数据库 (N) | 可选，四者中选其一。缺省为SCHEMA |
| OWNER | 导入指定的用户名下的模式 |  |
| SCHEMAS | 导入的模式列表 |  |
| TABLES | 表名列表，指定导入的tables名称 |  |
| PARALLEL | 用于指定导入的过程中所使用的线程数目 | 可选 |
| TABLE_PARALLEL | 用于指定导入的过程中每个表所使用的子线程数目 | 可选。在FAST_LOAD为Y时有效 |
| IGNORE | 忽略创建错误 (N)。如果表已经存在则向表中插入数据，否则报错表已经存在。 | 可选 |
| TABLE_EXISTS_ACTION | 需要的导入表在目标库中存在时采取的操作 [SKIP\| APPEND \| TRUNCATE \| REPLACE] | 可选 |
| FAST_LOAD | 是否使用dmfldr进行数据导入(N) | 可选 |
| FLDR_ORDER | 使用dmfldr是否需要严格按顺序来导数据(Y) | 可选 |
| COMMIT_ROWS | 批量提交的行数(5000) | 可选 |
| EXCLUDE | 忽略指定的对象 (CONSTRAINTS、INDEXES、ROWS、TRIGGERS、GRANTS)。格式 EXCLUDE=(CONSTRAINTS,INDEXES,ROWS,TRIGGERS,GRANTS) | 可选。例如 EXCLUDE=( CONSTRAINT) |
| GRANTS | 导入权限 (N) | 可选 |
| CONSTRAINTS | 导入约束 (Y) | 可选 |
| INDEXES | 导入索引 (Y) | 可选 |
| TRIGGERS | 导入触发器（Y） | 可选 |
| ROWS | 导入数据行 (Y) | 可选 |
| LOG | 日志文件 | 可选 |
| NOLOGFILE | 不使用日志文件(N) | 可选 |
| NOLOG | 屏幕上不显示日志信息(N) | 可选 |
| DUMMY | 交互信息处理: 打印(P)。取值Y/N。 Y：打印所有交互信息。N：不打印交互信息。 | 可选 |
| LOG_WRITE | 日志信息实时写入文件(N) | 可选 |
| PARFILE | 参数文件名，如果dimp的参数很多，可以存成参数文件 | 可选 |
| FEEDBACK | 显示每 x 行 (0) 的进度 | 可选 |
| COMPILE | 编译过程, 程序包和函数 (Y) | 可选 |
| INDEXFILE | 将表的索引/约束信息写入指定的文件 | 可选 |
| INDEXFIRST | 导入时先建索引(N) | 可选 |
| REMAP_SCHEMA | SOURCE_SCHEMA：TARGET_SCHEMA 将SOURCE_SCHEMA中的数据导入到TARGET_SCHEMA中 (N) | 可选 |
| ENCRYPT_PASSWORD | 数据的加密密钥 | 可选。和dexp中的ENCRYPT_PASSWORD设置的密钥一样 |
| ENCRYPT_NAME | 数据的加密算法的名称 | 可选。和dexp中的ENCRYPT_NAME设置的加密算法一样 |
| SHOW/ DESCRIBE | 只列出文件内容 (N) | 可选 |
| LOCAL | MPP环境下，是否使用LOCAL方式登录(N) | 可选 |
| TASK_THREAD_NUMBER | 设置dmfldr处理用户数据的线程数目 | 可选 |
| BUFFER_NODE_SIZE | 设置dmfldr读入文件缓冲区大小 | 可选 |
| TASK_SEND_NODE_NUMBER | 用于设置dmfldr发送节点个数[16,65535] | 可选 |
| LOB_NOT_FAST_LOAD | 如果一个表含有大字段，那么不使用dmfldr，因为dmfldr是一行一行提交的 | 可选 |
| PRIMARY_CONFLICT | 主键冲突的处理方式[IGNORE\|OVERWRITE],默认报错 | 可选 |
| HELP | 显示帮助信息 | 可选 |

## 3.3 dimp参数详解

### 3.3.1特殊参数

特殊参数中介绍了必选参数的和最常用的可选参数。

#### 3.3.1.1 USERID

`USERID`用于连接服务器，必选参数。用法请参考`dexp`中`USERID`。

#### 3.3.1.2 FILE

`FILE`用于指定明确导入`dexp`导出的文件（可以包含路径）。为必选参数。

语法如下：

```
FILE=<文件>
```

例如，之前导出的文件路径为：`FILE=/mnt/data/dexp/db_str.dmp`，那么导入文件可以写成如下所示：

```
./dimp USERID=SYSDBA/SYSDBA FILE=/mnt/data/dexp/db_str.dmp LOG=db_str.log DIRECTORY=/mnt/data/dimp
```

若`FILE`没有指定文件路径，则可在`DIRECTORY`中指定。

> 如果FILE指定的文件包含生成路径，则忽略DIRECTORY中的路径； 如果FILE没有指定路径时，使用DIRECTORY中指定的路径； 如果FILE和DIRECTORY都没有指定路径，则使用系统当前路径。

#### 3.3.1.3 LOG

`LOG`用于明确指定导入的日志文件名称（可以包含路径），可以包含多个文件，用逗号分隔。可选参数。如果不选用`LOG`参数（来明确指定日志文件名称），那么默认导出日志文件名称为`dimp.log`。

语法如下：

`LOG=<`文件名>

例如，指定日志文件名为`db_str.log`。

```
./dimp USERID=SYSDBA/SYSDBA FILE=/mnt/data/dexp/db_str.dmp LOG=db_str.log FULL=Y DIRECTORY=/mnt/data/dimp
```

> 如果LOG指定的文件包含生成路径，则忽略DIRECTORY中的路径； 如果LOG没有指定路径时，使用DIRECTORY中指定的路径； 如果LOG和DIRECTORY都没有指定路径，则使用系统当前路径。

`LOG`文件记载了导出对象的统计信息。供用户查看导出内容。详细的日志内容和`dexp LOG`中一样，请参考`dexp`的`LOG`。

和`LOG`有关的参数还有`NOLOGFILE`、`NOLOG`和`LOG_WRITE`。`NOLOGFILE=Y`用于设置不使用日志文件。`NOLOG=Y`用于设置不在屏幕上显示日志信息。`LOG_WRITE=Y`用于设置日志的实时打印（到日志文件）功能。

#### 3.3.1.4 DIRECTORY

`DIRECTORY`用于指定导入文件及日志文件生成的路径。可选参数，缺省为`dimp`所在路径。

语法如下：

```
DIRECTORY=
```

``：导入文件路径和日志文件生成的路径。

如果`FILE`和`LOG`参数指定的文件包含生成路径，则`FILE`和`LOG`参数中指定的路径将替代`DIRECTORY`所指定的路径；如果`FILE`和`LOG`参数指定的文件未包含路径信息，则导入文件路径和日志生成的文件路径都是`DIRECTORY`指定的路径；如果都没有指定路径，程序将根据当前的运行环境来设置相应的导出路径，一般为当前路径。

例如，没有指定路径，使用当前路径。

```
./dimp USERID=SYSDBA/SYSDBA FILE=db_str.dmp LOG=db_str.log FULL=Y
```

例如，指定`FILE`使用`/mnt/data/dexp`路径，`LOG`使用`/mnt/data/dimp`路径。

```
./dimp USERID=SYSDBA/SYSDBA FILE=/mnt/data/dexp db_str.dmp LOG=db_str.log FULL=Y DIRECTORY=/mnt/data/dimp
```

> FILE和LOG中指定的路径，优先级高于DIRECTORY中指定的路径。 当FILE和LOG不指定路径时，才使用DIRECTORY指定的路径。 如果都没有指定路径，则使用系统当前路径。

#### 3.3.1.5 四种级别的导入方式

针对数据库对象，有`FULL`、`OWNER`、`SCHEMAS`、`TABLES`四种导入方式可供选择。一次导出只能指定一种方式。可选参数，缺省为`SCHEMA`。

> 导入方式可以和导出方式不一致。 例如：当导出方式不为FULL时，导入时也可以指定为FULL方式，此时 的FULL会将导出文件包含的全部内容导入到指定的实例中。

##### 3.3.1.5.1 FULL

`FULL`方式导入整个数据库。

语法如下：

```
FULL=Y
```

例如，设置`FULL=Y`，导入整个数据库，导入的数据库文件在`/mnt/data/dexp`，即将生成的日志文件放在`/mnt/data/dimp`。

```
./dimp USERID=SYSDBA/SYSDBA FILE=/mnt/data/dexp/db_str.dmp LOG=db_str.log FULL=Y DIRECTORY=/mnt/data/dimp
```

##### 3.3.1.5.2 OWNER

`OWNER`方式导入一个或多个用户拥有的所有对象。

语法如下：

`OWNER=<`用户名`>{,<`用户名`>}`

例如，设置`OWNER=USER01`，导入用户`USER01`所拥有的对象全部导出。导入的数据库文件在`/mnt/data/dexp`，即将生成的日志文件放在`/mnt/data/dimp`。

```
./dimp USERID=SYSDBA/SYSDBA FILE=/mnt/data/dexp/db_str.dmp LOG=db_str.log OWNER=USER01 DIRECTORY=/mnt/data/dimp
```

##### 3.3.1.5.3 SCHEMAS

`SCHEMAS`方式的导入一个或多个模式下的所有对象。

语法如下：

`SCHEMAS=<`模式名`>{,<`模式名`>}`

例如，设置`SCHEMAS=USER01`，导入模式`USER01`模式下的所有对象。导入的数据库文件在`/mnt/data/dexp`，即将生成的日志文件放在`/mnt/data/dimp`。

```
./dimp USERID=SYSDBA/SYSDBA FILE=/mnt/data/dexp/db_str.dmp LOG=db_str.log SCHEMAS=USER01 DIRECTORY=/mnt/data/dimp
```

> 一般情况下，OWNER与SCHEMAS导入导出是相同的。 但是用户可以包含多个模式，在这种情况下SCHEMAS的导入导出是OWNER导入导出的一个子集。

##### 3.3.1.5.4 TABLES

`TABLES`方式导入一个或多个指定的表或表分区。导入所有数据行、约束、索引等信息。

语法如下：

```
TABLES=<表名>{,<表名>}
```

例如，设置`TABLES=table1,table2`，导入`table1,table2`两张表的所有数据和信息。导入的数据库文件在`/mnt/data/dexp`，即将生成的日志文件放在`/mnt/data/dimp`。

```
./dimp USERID=SYSDBA/SYSDBA FILE=/mnt/data/dexp/db_str.dmp LOG=db_str.log TABLES=table1,table2 DIRECTORY=/mnt/data/dimp
```

和`TABLES`导入有关的参数还有`EXCLUDE`，用来指定导入时过滤掉某类对象。

### 3.3.2普通参数

#### 3.3.2.1 PARALLEL

`PARALLEL`用于指定导入的过程中所使用的线程数目。可选参数，缺省为单线程。如果`CPU`核数为N的话，那一般来说`PARALLEL`为N或者`N+1`最合适。

语法如下：

```
PARALLEL=
```

``：线程数。整数类型，取值范围：1-100。

例如，设置`PARALLELl=2`时则线程数为2。

```
./dimp USERID=SYSDBA/SYSDBA FILE=/mnt/data/dexp/db_str.dmp LOG=db_str.log FULL=Y DIRECTORY=/mnt/data/dimp PARALLEL=2
```

#### 3.3.2.2 TABLE_PARALLEL

`TABLE_PARALLEL`在`FAST_LOAD`为Y时有效，用于指定导入每张表所使用的线程数。可选参数，缺省为单线程。如果`CPU`核数为N的话，那一般来说`TABLE_PARALLEL`为N或者`N+1`最合适。在`MPP`模式下会转换成单线程。

语法如下：

```
TABLE_PARALLEL=
```

``：线程数。整数类型，取值范围1-50。

例如，设置`TABLE_PARALLEL=3`时则线程数为3。

```
./dimp USERID=SYSDBA/SYSDBA FILE=/mnt/data/dexp/db_str.dmp LOG=db_str.log FULL=Y DIRECTORY=/mnt/data/dimp TABLE_PARALLEL=3
```

#### 3.3.2.3 IGNORE

`IGNORE`指定忽略创建表错误。可选参数。缺省为N，不忽略。

语法如下：

```
IGNORE=Y
```

`IGNORE=Y`：忽略导入时所产生的创建表错误并继续执行。当缺省或`IDNORE=N`时，不忽略导入时所产生的创建表错误，遇到错误即停止执行并报错。

#### 3.3.2.4 TABLE_EXISTS_ACTION

`TABLE_EXISTS_ACTION`用于要导入的表已经存在时的处理方式。默认为直接报错。

语法如下：

```
PRAIMARY_CONFLICT=[SKIP | APPEND | TRUNCATE | REPLACE]
```

`SKIP`：跳过此表。

`APPEND`：直接向现有表中导入数据

`TRUNCATE`：先删除现有表中的数据，再向表中导入数据

`REPLACE`：先删除现有表，再导数据

#### 3.3.2.5 FAST_LOAD

`FAST_LOAD`用于设置是否使用`dmfldr`进行数据导入，默认为N。

语法如下：

```
FAST_LOAD=Y/N
```

Y：是。

N：否。

> 当FAST_LOAD=Y时才可以设置TABLE_PARALLEL参数，否则TABLE_PARALLEL参数无效。

#### 3.3.2.6 FLDR_ORDER

`FAST_ORDER`用于设置使用`dmfldr`时，是否严格按导出顺序来导入数据。可选参数。

语法如下：

```
FAST_ORDER=Y/N
```

Y或缺省`FLDR_ORDER`参数：表示按照导出顺序来导入数据。

N：表示不按照导出顺序来导入，数据的创建为随机生成。

#### 3.3.2.7 COMMIT_ROWS

`COMMIT_ROWS`用于设置批量提交的行数，默认为5000行。用户可以根据实际情况调整每次提交的行数，以达到性能的最佳点。一般情况下可不设置。可选参数。

语法如下：

```
COMMIT_ROWS=
```

``：行数。整数类型。

#### 3.3.2.8 EXCLUDE

`EXCLUDE`用来批量设置导入时忽略的对象种类。可选参数。

语法如下：

`EXCLUDE=(<`对象种类名`>{,<`对象种类名`>})`

或者

```
EXCLUDE=TABLES:'<表名>'{,'<表名>'}
```

<对象种类名>：包括`CONSTRAINTS`、`INDEXES`、`ROWS`、`TRIGGERS`、`GRANTS`。

> 如果导入方式为TABLES表级导入时， 则“EXCLUDE=TABLES:'<表名>'{,'<表名>'}”方式将不起作用。

例如，设置`EXCLUDE=(CONSTRAINTS)`，将当前用户下的`table1`、`table2`的对象信息导入时不导入约束。

```
./dimp SYSDBA/SYSDBA FILE=/mnt/data/db_str.dmp LOG=db_str.log TABLES=table1,table2 EXCLUDE=(CONSTRAINTS) DIRECTORY=/mnt/data/dimp
```

#### 3.3.2.9 GRANTS、CONSTRAINTS、INDEXES、TRIGGERS、ROWS

这些参数用来指定某类对象是否被导入。类别分别为约束、表空间、权限、索引、触发器和数据。

```
GRANTS=Y
CONSTRAINTS=N
TABLESPACE=N
INDEXS=N
TRIGGERSS=N
ROWS=N
```

`GRANTS=Y`：设置导入权限。可选参数。缺省该参数为不导入权限。

`CONSTRAINTS=N`：设置不导入约束。可选参数。缺省该参数为导入约束。

`TABLESPACE=N`：设置导入的对象定义中不包含表空间。可选参数。缺省该参数为包含表空间。

`INDEXES=N`：设置不导入索引。可选参数。缺省该参数为导入索引。

`TRIGGERS=N`：设置不导入触发器。可选参数。缺省该参数为导入触发器。

`ROWS=N`：设置不导入数据。可选参数。缺省该参数为导入数据。

例如，设置`ROWS=N`不导入表中的数据。

```
./dimp USERID=SYSDBA/SYSDBA FILE=/mnt/data/dexp/db_str.dmp NOLOGFILE=Y FULL=Y DIRECTORY=/mnt/data/dimp ROWS=N
```

#### 3.3.2.10 NOLOGFILE

`NOLOGFILE`用于设置是否使用日志文件。可选参数。

语法如下：

```
NOLOGFILE=Y/N
```

Y：不使用日志文件。此时即使存在`LOG`参数，`LOG`参数也为无效。

N或参数缺省：使用日志文件。

例如，设置`NOLOGFILE=Y`，不使用日志文件。

```
./dimp USERID=SYSDBA/SYSDBA FILE=/mnt/data/dexp/db_str.dmp NOLOGFILE=Y FULL=Y
```

#### 3.3.2.11 NOLOG

`NOLOG`设置屏幕上是否显示日志信息。可选参数。默认为N，显示日志信息。

语法如下：

```
NOLOG=Y/N
```

Y：不显示。

N：显示。

例如，设置`NOLOG=Y`屏幕不显示日志信息。

```
./dimp USERID=SYSDBA/SYSDBA FILE=/mnt/data/dexp/db_str.dmp LOG=db_str.log NOLOG=Y FULL=Y DIRECTORY=/mnt/data/dimp
```

#### 3.3.2.12 LOG_WRITE

`LOG_WRITE`用于日志信息实时写入日志文件。可选参数。

语法如下：

```
LOG_WRITE=Y/N
```

Y：一边将日志内容打印到屏幕上，一边将日志内容写入日志文件。

N或缺省参数：日志内容先在屏幕上全部打印完毕再写入日志文件。

#### 3.3.2.13 DUMMY

`DUMMY`用于设置交互信息处理。可选参数，缺省使用P打印交互信息。

语法如下：

```
DUMMY=P/Y/N
```

P：打印交互信息，默认方式。

Y：不打印交互信息，所有交互都按`YES`处理。

N：不打印交互信息，所有交互都按`NO`处理。

#### 3.3.2.14 PARFILE

`PARFILE`用于将常用的参数设置保存到文件中，然后使用参数文件`PARFILE`进行导出、导入操作。可选参数。

语法如下：

```
PARFILE=
```

``：`PARFILE`文件的绝对路径。

```
例如，在dimp中使用PARFILE，设置路径PARFILE=/mnt/data/dimp/para.txt。
./dimp USERID=SYSDBA/SYSDBA PARFILE=/mnt/data/dimp/para.txt
```

其中，参数文件`/mnt/data/dimp/para.txt`的内容如下：

```
FILE=/mnt/data/dexp/db_str.dmp
LOG=db_str.log
TABLES=table1
DIRECTORY=/mnt/data/dimp
```

#### 3.3.2.15 FEEDBACK

`FEEDBACK`用来指明在导入数据的过程中每间隔多少行打印一次进度信息。可选参数。

当参数缺省时，默认值为0，只打印导入表的总行数。

语法如下：

```
FEEDBACK=
```

``：行数。

例如，将文件`dexp.dmp`中的对象和数据导入到数据库时，要求在导出的过程中每隔100行打印一次进度信息。

```
./dimp SYSDBA/SYSDBA FULL=Y FILE=/mnt/data/dexp/dexp.dmp LOG=db_str.log DIRECTORY=/mnt/data/dimp FEEDBACK=100
```

#### 3.3.2.16 COMPILE

如果导出时包含过程/函数，那么导入时会执行一个编译语句（`alter ...compile`）。`COMPILE`用于设置是否在导入时，对过程或函数执行编译。

编译相当于执行重建操作，用于检查过程或函数是否还有效。编译成功，说明对象是有效的；编译失败，说明对象不存在或发生改变，导致重建操作失败。编译失败，导入停止。

不编译就不检查有效性，直接导入。

语法如下：

```
COMPILE=N/Y
```

Y或缺省参数：执行。

N：不执行。

例如，导入的过程中含有函数`FUN_01`，那么导出过程中会自动执行如下语句：

```
alter function "SYSDBA"."FUN_01" compile;
```

如果不想编译，需要缺省参数或设置`COMPILE=N`。

#### 3.3.2.17 INDEXFILE

用于将表的索引/约束创建信息写入指定的文件。

语法如下：

```
INDEXFILE=<文件>
例如，设置INDEXFILE=f:\data\dimp.log。
./dimp USERID=SYSDBA/SYSDBA FILE=/mnt/data/dexp/db_str.dmp LOG=db_str.log FULL=Y INDEXFILE=/mnt/data/dimp/dimp.log
```

#### 3.3.2.18 INDEXFIRST

`INDEXFIRST`用于设置导入时是否先建索引。可选参数。

创建索引的过程是先遍历数据再创建索引树。数据量比较大时，应该选择`INDEXFIRST=Y`，先创建索引再导入数据，这样就避免创建索引之前遍历大量数据而耗费时间；数据量小时，可任意选择。

语法如下：

```
INDEXFIRST=Y/N
```

Y：是。

N或参数缺省：否。

#### 3.3.2.19 REMAP_SCHEMA

将源模式中的数据导入到目标模式中。如果目标模式不存在，先创建目标模式，再继续导入。可选参数。

语法如下：

```
：
：源模式。
```

``：目标模式。

例如，将`SYSDBA`模式中的数据导入到`PRERSON`模式中。

```
./dimp SYSDBA/SYSDBA FILE=/mnt/data/dexp/imp_exp.dmp DIRECTORY=/mnt/data/dimp FULL=Y REMAP_SCHEMA=SYSDBA:PERSON
```

#### 3.3.2.20 ENCRYPT_PASSWORD、ENCRYPT_NAME

如果数据文件是通过加密后得到的，在数据文件导入到数据库时，需要提供加密密钥和加密算法。同时，在1个小时内只能尝试10次导入解密。

语法如下：

```
ENCRYPT_PASSWORD=<加密密钥>
ENCRYPT_NAME=<加密算法>
```

<加密密钥>：与导出文件的加密密钥相同。

<加密算法>：与导出文件的加密算法相同。导出加密算法缺省的情况下，此处加密密码可不写。

例如，将`2.3.3.15`中导出的数据再导入进来。

```
./dimp SYSDBA/SYSDBA FILE=/mnt/data/dexp/dk15.dmp LOG=db_str19.log
FULL=Y DIRECTORY=/mnt/data/dimp ENCRYPT_PASSWORD=abcdefg ENCRYPT_NAME=DES_CBC
```

#### 3.3.2.21 SHOW/ DESCRIBE

`SHOW/DESCRIBE`用于设置是否打印`dexp`导出的数据文件的内容列表。可选参数。

语法如下：

```
SHOW=Y/N 或DESCRIBE=Y/N
```

Y：是。

N或缺省参数：否。

例如，想查看`/mnt/data/dexp/`中`db_str.dmp`文件的内容列表。

```
./dimp USERID=SYSDBA/SYSDBA FILE=/mnt/data/dexp/db_str.dmp SHOW=Y
```

打印结果为：

```
--------------------------------导出文件列表信息--------------------------------
```

共包含1个文件，文件如下：

```
./dimp USERID=SYSDBA/SYSDBA FILE=/mnt/data/dexp/db_str.dmp SHOW=Y
----------------------------------------------------------------------------
```

- 导出文件为 `FULL` 方式导出，共包含以下 7 个模式

模式`PERSON` 含有 4 个表，分别为：

```
ADDRESS ADDRESS_TYPE PERSON PERSON_TYPE
```

模式`PRODUCTION` 含有 7 个表，分别为：

```
PRODUCT_CATEGORY PRODUCT_SUBCATEGORY PRODUCT LOCATION PRODUCT_INVENTORY PRODUCT_
REVIEW PRODUCT_VENDOR
```

模式`PURCHASING` 含有 5 个表，分别为：

```
VENDOR VENDOR_ADDRESS VENDOR_PERSON PURCHASEORDER_HEADER PURCHASEORDER_DETAIL
```

模式`RESOURCES` 含有 4 个表，分别为：

```
DEPARTMENT EMPLOYEE EMPLOYEE_ADDRESS EMPLOYEE_DEPARTMENT
```

模式`SALES` 含有 5 个表，分别为：

```
CUSTOMER CUSTOMER_ADDRESS SALESPERSON SALESORDER_HEADER SALESORDER_DETAIL
```

模式`SYSDBA` 含有 1 个表，分别为：

```
TAB1
```

模式`OTHER` 含有 10 个表，分别为：

```
DEPARTMENT EMPSALARY ACCOUNT ACTIONS READER READERAUDIT DEPTTAB EMPTAB SALGRADE
COMPANYHOLIDAYS
```

#### 3.3.2.22 LOCAL

`LOCAL`只用于在`MPP`环境下，是否使用`LOCAL`方式登录，缺省为不使用。可选参数。

语法如下：

```
LOCAL=Y/N
```

Y：表示用户在登录时为`LOCAL`本地登录方式，即只登陆指定的节点，操作数据也只是本节点的数据。

N或缺省参数：表示不使用，为`GLOBOL`全局登录方式，即操作数据是所有节点上相关数据。

#### 3.3.2.23 TASK_THREAD_NUMBER

`TASK_THEAD_NUMBER`用于设置`dmfldr`处理用户数据的线程数目。可选参数，缺省值为`CPU`个数。但当`CPU`个数大于8时，默认值都被置为8。

语法如下：

```
TASK_THEAD_NUMBER=
```

``：线程数。取值范围：1-128。

#### 3.3.2.24 BUFFER_NODE_SIZE

`BUFFER_NODE_SIZE`用于设置`dmfldr`指定读取文件缓冲区页大小。可选参数，默认为10。

值越大，缓冲区的页数越多，每次可以读取的数据就越多，每次发送到服务器的数据也就越多，效率越高。但其大小受`dmfldr`客户端内存大小限制。

语法如下：

```
BUFFER_NODE_SIZE=
```

``：缓冲区页数。整数类型，取值范围：1-256。单位为M。

#### 3.3.2.25 TASK_SEND_NODE_NUMBER

`TASK_SEND_NODE_NUMBER`用于设置`dmfldr`发送节点个数。可选参数。

语法如下：

```
TASK_SEND_NODE_NUMBER=
```

`:`节点个数。整数类型，取值范围：`16-65535`。在系统内存够的情况下可以适当的设大数值以提升效率。缺省情况下，由程序自动计算。

#### 3.3.2.26 LOB_NOT_FAST_LOAD

`LOB_NOT_FAST_LOAD`用于设置当表中含有大字段时不使用`dmfldr`，而使用普通的`INSERT`进行插入，根据`COMMIT_ROWS`参数决定提交的行数。因为当表中有大字段的时候，`dmfldr`是一行一行提交表数据。

语法如下：

```
LOB_NOT_FAST_LOAD=Y
```

#### 3.3.2.27 PRIMARY_CONFLICT

`PPIMARY_CONFLICT`用于设置主键冲突的处理方式。可选参数，默认报错（`OVERWRITE`）。

语法如下：

```
PRAIMARY_CONFLICT=[IGNORE|OVERWRITE]
```

`IGNORE`：不处理主键的冲突。

`OVERWRITE`：报错处理。

#### 3.3.2.28 HELP

输入`dimp HELP` 即可查看帮助信息。

语法如下：

```
HELP
```

例如，使用`HELP`查看帮助信息。

```
./dimp HELP
```

`HELP`信息会逐个显示所有参数的大致信息，供用户快速参考。
