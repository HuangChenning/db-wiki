---
title: "3 dmfldr实战"
book: "DM7 dmfldr使用手册"
version: "DM7"
source: "temp/doc/special/DM7°ïÖúÎÄµµ.chm#~htm/dmfldr使用手册.htm"
tags:
  - dameng
  - dm7
  - dmfldr
---

在上一章简单了解了`dmfldr`的各参数含义后，本章介绍如何通过设置不同参数值使用`dmfldr`进行不同情况的数据装载。并介绍了如何通过设置参数提高`dmfldr`的性能以及使用限制。

> 本章中皆以在Linux操作系统下进行操作为例，在Windows操作 系统下目录分隔符与单引号转义的处理有些许区别，不再赘述

## 3.1 dmfldr控制文件

控制文件`CONTROL`是启动`dmfldr`必须要指定的参数，用于指定数据文件中数据的格式。在数据载入时，`dmfldr`根据控制文件指定的格式来解析数据文件；导出数据时，`dmfldr`也会根据控制文件指定的列分隔符、行分隔符等生成数据文件。

控制文件中还可以指定其他`dmfldr`参数值。

`dmfldr`控制文件的语法如下所示：

```
[OPTIONS(
=
……
)]
LOAD [DATA]
INFILE [LIST] [] [, []]
[BADFILE ]
[APPEND|REPLACE|INSERT]
INTO TABLE [.]
[FIELDS ]
[]
::=参数
::=值
::=文件地址
```

` ::=`含文件列表文件地址

```
::=STR [X] ‘’
::=模式名
::=表名
::=<单字节字符>
::=({ ,})
::= [] [] [] [][][]
::=列名
::=FILLER||NULL
::=position(p1:p2)
::=DATE FORMAT ‘<时间日期格式串>’
::= TERMINATED [BY]
::= WHITESPACE|<单字节字符>
::= [OPTIONALLY] ENCLOSE [BY] <单字节字符>
::= CONSTANT "<常量>"
::= "函数名称()"
```

对于上述控制文件语法，需要说明的是：

- `dmfldr`在处理数据文件中换行符时`windows`默认为`0x0D0A(\r\n)`，非`windows`默认为`0x0A(\n)`，用户应该根据现有的数据文件中的换行符做相应的调整。对应选项为``，若指定的``值为二进制的字符串值需要指明`[X]`选项，``值不再需要以`0x`开头。若没有指明`[X]`选项，则``值为指定的字符串；
- 关于列分隔符，用户应当指定`FIELDS`或者`coldef_option`中的至少一种；
- 关于`LIST`选项，`INFILE`使用`LIST`选项时，表明实际的数据文件路径存储在`INFILE`指定的文件中，该文件可以存储多个实际的数据文件路径，使用逗号或者换行分割；
- 关于`OPTIONS`选项，该选项支持命令行参数中除`userid`，`control`，`help`以外的所有参数的指定，每个参数值对使用空格或者换行分割。对于`option`中出现的参数，在`dmfldr`的指定执行参数中也出现的，`dmfldr`会选择`option`中对应参数的值执行；
- 关于`property_option`选项，`FILLER`：跳过处理数据文件中指定列的值；`position(p1,p2)`：从数据文件中每行数据的第`p1`个字节到第`p2`个字节为该列值，包含边界`p1,p2`；`NULL`：指定的值为`NULL`，忽略数据文件中的值。`property_option`参数仅对导入有效；
- 关于`fun_option`选项，目前只支持`trim()`函数。

例：一个`dmfldr`控制文件的例子

```
OPTIONS
(
SKIP = 0
ROWS = 50000
DIRECT = TRUE
INDEX_OPTION = 2
)
LOAD DATA
INFILE '/opt/data/test1.txt' STR X '0D0A'
BADFILE '/opt/data/test1.bad'
INTO TABLE test1
FIELDS '|'
(
F1,
F2 DATE FORMAT 'YYYY-MM-DD',
F3 NULL,
F4 TERMINATED BY WHITESPACE ENCLOSE BY '(',
F5 CONSTANT "test",
F6 "trim()"
)
LOAD DATA
INFILE '/opt/data/test2.txt' STR X '0D0A'
BADFILE '/opt/data/test2.bad'
INTO TABLE test2
FIELDS '|'
(
C1 TERMINATED BY ' ',
C2,
C3 DATE FORMAT 'yyyy-mm-dd'
)
```

在这个例子中：

- `OPTIONS`选项中定义了`SKIP`、`ROWS`、`DIRECT`和`INDEX_OPTION`参数
- 有两个`LOAD`选项，表明有一次装载同时处理两个表，在每个`LOAD`选项中：
- 指定了数据文件和数据文件的换行符，还指定了`BADFILE`文件
- 指定了操作的数据库基表、列分隔符以及列定义

## 3.2 指定数据文件

当`dmfldr`工作在`IN`模式时，从数据文件中读取数据并载入数据库；当工作在`OUT`模式时，从数据库中将指定数据导出到数据文件。

数据文件通常为文本文件，列与列之间由列分隔符隔开，行与行之间由行分隔符隔开。数据文件中的列分隔符和行分隔符由用户指定，并在控制文件中设置为与数据文件中的一致。

### 3.2.1 在控制文件中指定数据文件

可以在控制文件的`LOAD`节点中指定数据文件。

例如：

`1)` 建表`TEST`

```
DROP TABLE TEST;
CREATE TABLE TEST(C1 INT,C2 INT,C3 DATE);
```

`2)` 编辑数据文件`test.txt`，存放路径为`/opt/data/test.txt`，文件内容如下

```
1 1|2015-11-06
2 2|2015-11-05
3 3|2015-11_04
```

`3)` 编辑控制文件`test.ctrl`，存放路径为`/opt/data/test.ctrl`，内容如下：

```
LOAD DATA
INFILE '/opt/data/test.txt'
INTO TABLE test
FIELDS '|'
(
C1 TERMINATED BY ' ',
C2,
C3 DATE FORMAT 'yyyy-mm-dd'
)
```

`4)` 使用`dmfldr`进行数据载入

```
./dmfldr userid=SYSDBA/SYSDBA@localhost:5236 control=\'/opt/data/test.ctrl\'
```

### 3.2.2 使用DATA参数指定数据文件

也可以使用`DATA`参数指定`dmfldr`的数据文件，数据文件路径的优先选择顺序为先控制文件，后参数选项。如果控制文件中数据文件路径指定为‘*’，在命令行通过`DATA`参数指定数据文件路径，`DATA`所指定的文件路径会替换‘*’。

例如：

`1)` 建表`TEST`

```
DROP TABLE TEST;
CREATE TABLE TEST(C1 INT,C2 INT,C3 DATE);
```

`2)` 编辑数据文件`test.txt`，存放路径为`/opt/data/test.txt`，文件内容如下

```
1 1|2015-11-06
2 2|2015-11-05
3 3|2015-11_04
```

`3)` 编辑控制文件`test.ctrl`，存放路径为`/opt/data/test.ctrl`，内容如下：

```
LOAD DATA
INFILE *
INTO TABLE test
FIELDS '|'
(
C1 TERMINATED BY ' ',
C2,
C3 DATE FORMAT 'yyyy-mm-dd'
)
```

`4)` 使用`dmfldr`进行数据载入

```
./dmfldr userid=SYSDBA/SYSDBA@localhost:5236 control=\'/opt/data/test.ctrl\' data=\'/opt/data/test.txt \'
```

## 3.3 数据转换

`dmfldr`使用的数据文件都是文本格式的，其中的列值都是以字符串的方式保存在数据文件中。要想将这些数据载入数据库表中，需要将字符串转换成数据库表各列对应的数据类型。`dmfldr`支持所有`DM`数据库支持的列定义类型，包括字符串、数值、时间日期、时间日期间隔、大字段类型等。

若数据文件的编码方式与`DM`数据库服务器的编码方式不一样，`dmfldr`还需要进行字符编码的转换。`dmfldr`支持`UTF8`和`GBK`编码之间的相互转换。

在数据类型和编码转换过程中如果出现错误，`dmfldr`会跳过该行继续后面的工作，并记录错误行到`BADFILE`指定的文件。常见的出错的情况有以下几种：

- 编码转换失败
- 目标列为字符串类型时，数据长度大于列定义长度
- 目标列为数值类型时，数据包含非法字符或者转换后超出该数值的范围
- 目标列为日期类型时，`dmfldr`默认按`yyyy-mm-dd hh:ss:mm`的格式解析，如果数据不是这样的格式，需要指定对应列的时间日期`fmt`格式而未指定

## 3.4 错误数据文件

`dmfldr`错误数据的文件路径由`BADFILE`参数设置，默认的错误文件名为`fldr.bad`。用户也可以通过设置控制文件中的`OPTION`选项来指定错误数据文件的路径，同时也可以在控制文件的`LOAD`节点中指定错误数据文件的路径。错误数据文件路径最终值的优先选择顺序为`LOAD`节点选项，`OPTION`选项，参数选项。用户可以同时对三种设置方式中的一个或多个设置，但最终的值只取一个。`BADFILE`仅作用于`dmfldr`的工作`MODE`为`IN`的情况下，`MODE`为`OUT`时无效。

当导入的数据文件中存在错误数据，而错误数在允许的最大错误数范围内时，`dmfldr`会将出错的数据记录到错误数据文件中。文件记录的信息为执行程序、时间、目标表、数据文件中存在格式错误的行数据以及转换出错的行数据。

允许的最大容错个数由`ERRORS`选项设置，默认为100。当`dmfldr`在数据载入过程中出现的错误个数超过了`ERRORS`所设置的数目，`dmfldr`会停止载入，当前时间点的所有正确数据将会被提交到`DM7`数据库服务器。如果载入过程中不允许出现错误则可以将`ERRORS`设置为0；如果允许所有的错误出现，则可以将`ERRORS`设置为一个非常大的数。`ERRORS`所统计的错误包含在数据转换和数据插入过程中所产生的数据错误。

例如：

`1)` 建表`TEST`

```
DROP TABLE TEST;
CREATE TABLE TEST(C1 INT,C2 INT,C3 DATE);
```

`2)` 编辑数据文件`test.txt`，存放路径为`/opt/data/test.txt`，文件内容如下

```
1 1|2015-11-06
2 2|2015-11-05
3 3|2015-11_04
4 4|aaaa-bbb-ccc
```

`3)` 编辑控制文件`test.ctrl`，存放路径为`/opt/data/test.ctrl`，内容如下：

```
LOAD DATA
INFILE '/opt/data/test.txt'
INTO TABLE test
FIELDS '|'
(
C1,
C2 TERMINATED BY ' ',
C3 DATE FORMAT 'yyyy-mm-dd'
)
```

`4)` 使用`dmfldr`进行数据载入

```
./dmfldr userid=SYSDBA/SYSDBA@localhost:5236 control=\'/opt/data/test.ctrl\' badfile=\'/opt/data/test.bad\'
```

`5)` 查看错误数据文件`/opt/data/test.bad`，其内容如下

```
dmfldr: 2015-11-09 16:56:52 SYSDBA->TEST 4|4 aaaa-bbb-ccc
```

## 3.5 大字段数据处理

`dmfldr`支持对`DM`数据库的大字段类型数据的载入和导出，`DM`数据库支持的大字段数据类型有`TEXT`、`LONGVARCHAR`、`IMAGE`、`LONGVARBINARY`、`BLOB`以及`CLOB`。

### 3.5.1 大字段数据的导出

当`dmfldr`工作在导出模式即`MODE`为`OUT`时，`dmfldr`生成大字段对应的数据文件名由`LOB_FILE_NAME`指定，若未指定默认为`dmfldr.lob`，文件存放于`LOB_DIRECTORY`指定的目录，如果未指定`LOB_DIRECTORY`则存放于指定的导出数据文件同一目录。

例如：

`1)` 建表`TEST`

```
DROP TABLE TEST;
CREATE TABLE TEST(C1 INT,C2 BLOB,C3 CLOB);
```

`2)` 插入数据

```
INSERT INTO TEST VALUES(1,0XAB121032DE,'abcdefg');
INSERT INTO TEST VALUES(2,0XAB121032DE,'abcdefg');
COMMIT;
```

`3)` 编辑控制文件`test.ctrl`，存放路径为`/opt/data/test.ctrl`，内容如下：

```
LOAD DATA
INFILE '/opt/data/test.txt'
INTO TABLE test
FIELDS '|'
(
C1,
C2,
C3
)
```

`4)` 使用`dmfldr`进行导出数据

```
./dmfldr userid=SYSDBA/SYSDBA@localhost:5236 control=\'/opt/data/test.ctrl\' LOB_DIRECTORY=\'/opt/data/\' mode=\'out\'
```

在这个例子中，指定了`LOB_DIRECTORY`，而没有指定`LOB_FILE_NAME`，导出的大字段数据文件将存放在`LOB_DIRECTORY`指定的`/opt/data`目录，文件名为`dmfldr.lob`。

### 3.5.2 DIRECT为TRUE时大字段数据的载入

当`MODE`为`IN`且`DIRECT`为`TRUE`时，此时数据载入若涉及到大字段对象，需要用户指定大字段数据文件，且用户必须先把相关文件传送到服务器本地目录，然后使用`LOB_DIRECTORY`指明存放目录。

大字段数据文件在数据文件中指定，可以是任意格式的文件。在数据文件中，大字段以“文件名：起始偏移：长度”的形式记录在数据文件中。指定的文件名无效时，`dmfldr`会报错，装载失败。对于`CLOB`类型字段，当指定的偏移、长度范围内带有不完整字符时，`dmfldr`将装载失败。

例如：

`1)` 建表`TEST`

```
DROP TABLE TEST;
CREATE TABLE TEST(C1 INT,C2 BLOB,C3 CLOB);
```

`2)` 编辑数据文件`test.txt`，存放路径为`/opt/data/test.txt`，文件内容如下

```
1|testblob.txt:1:10|testclob.txt:1:10
2|testblob.txt:10:20|testclob.txt:10:20
3|testblob.txt:20:30|testclob.txt:20:30
```

其中，`testblob.txt`、`testclob.txt`为文本文件，长度大于30字节，存放路径为`/opt/data`。

`3)` 编辑控制文件`test.ctrl`，存放路径为`/opt/data/test.ctrl`，内容如下：

```
LOAD DATA
INFILE '/opt/data/test.txt'
INTO TABLE test
FIELDS '|'
(
C1,
C2,
C3
)
```

`4)` 使用`dmfldr`进行导入数据

```
./dmfldr userid=SYSDBA/SYSDBA@localhost:5236 control=\'/opt/data/test.ctrl\' LOB_DIRECTORY=\'/opt/data/\'
```

### 3.5.3 DIRECT为FALSE时大字段数据的载入

当`MODE`为`IN`且`DIRECT`为`FALSE`时，数据文件中大字段列数据即字段内容。`BLOB_TYPE`参数指定`BLOB`列内容为十六进制或者字符串：

- `BLOB_TYPE`为`HEX_CHAR`时，数据文件中`BLOB`列当作为十六进制内容；
- `BLOB_TYPE`为`HEX`时，数据文件中`BLOB`列为字符串形式内容，导入后会转换为十六进制。

`BLOB_TYPE`参数只对`DIRECT`为`FALSE`时有效，默认为`HEX_CHAR`。

例1：

`1)` 建表`TEST`

```
DROP TABLE TEST;
CREATE TABLE TEST(C1 INT,C2 BLOB,C3 CLOB);
```

`2)` 编辑数据文件`test.txt`，存放路径为`/opt/data/test.txt`，文件内容如下

```
1|0x12d3c8a7|abcdefg
2|0x12a4cbac|hijlkmn
3|0x22d3c8b3|adefhjd
```

`3)` 编辑控制文件`test.ctrl`，存放路径为`/opt/data/test.ctrl`，内容如下：

```
LOAD DATA
INFILE '/opt/data/test.txt'
INTO TABLE test
FIELDS '|'
(
C1,
C2,
C3
)
```

`4)` 使用`dmfldr`进行导入数据，`BLOB_TYPE`为`HEX_CHAR`

```
./dmfldr userid=SYSDBA/SYSDBA@localhost:5236 control=\'/opt/data/test.ctrl\' direct=false blob_type=\'hex_char\'
```

`5)` 查询表数据

```
SELECT * FROM TEST;
行号 C1 C2 C3
---------- ----------- ---------- -------
1 1 0x12D3C8A7 abcdefg
2 2 0x12A4CBAC hijlkmn
3 3 0x22D3C8B3 adefhjd
```

例2：

步骤`1)`、`2)`、`3)`同例1

`4)` 使用`dmfldr`进行导入数据，`BLOB_TYPE`为`HEX`

```
./dmfldr userid=SYSDBA/SYSDBA@localhost:5236 control=\'/opt/data/test.ctrl\' direct=false blob_type=\'hex\'
```

`5)` 查询表数据

```
select * from test;
行号 C1 C2 C3
---------- ----------- ---------------------- -------
1 1 0x30783132643363386137 abcdefg
2 2 0x30783132613463626163 hijlkmn
3 3 0x30783232643363386233 adefhjd
```

## 3.6 日志文件及日志信息

`dmfldr`的日志文件路径由`LOG`参数设置，默认日志文件名为`fldr.log`。文件记录了装载过程中的装载信息和错误信息以及统计信息。用户也可以通过设置控制文件中的`OPTION`选项来指定日志路径。如果参数及`OPTION`中同时指定了日志路径则其将以`OPTION`中指定的路径为最终路径。

例如：

`1)` 建表`TEST`

```
DROP TABLE TEST;
CREATE TABLE TEST(C1 INT,C2 INT,C3 DATE);
```

`2)` 编辑数据文件`test.txt`，存放路径为`/opt/data/test.txt`，文件内容如下

```
1|1 2015-11-06
2|2 2015-11-05
3|3 2015-11_04
```

`3)` 编辑控制文件`test.ctrl`，存放路径为`/opt/data/test.ctrl`，内容如下：

```
LOAD DATA
INFILE '/opt/data/test.txt'
INTO TABLE test
FIELDS '|'
(
C1,
C2 TERMINATED BY ' ',
C3 DATE FORMAT 'yyyy-mm-dd'
)
```

`4)` 使用`dmfldr`进行数据载入

```
./dmfldr userid=SYSDBA/SYSDBA@localhost:5236 control=\'/opt/data/test.ctrl\' log=\'/opt/data/test.log\'
```

`5)` 查看日志文件`/opt/data/test.log`，其内容如下

```
dmfldr: 2015-11-20 14:48:41 dmfldr:
Copyright (c) 2011, 2015, Dameng. All rights reserved.
```

控制文件：

加载行数:全部

每次提交服务器行数`:50000`

跳过行数`:0`

允许错误数`:100`

是否直接加载`:Yes`

是否插入自增列`:No`

数据是否已按照聚集索引排序`:No`

字符集`:GBK`

```
dmfldr: 2015-11-20 14:48:41
```

数据文件共1个:

```
/opt/data/test.txt
```

错误文件`:fldr.bad`

目标表`:TEST`

列名 终止 包装数据类型

```
C1 | CHARACTER
C2 WHT CHARACTER
C3 | yyyy-mm-dd
dmfldr: 2015-11-20 14:48:41
```

目标表`:TEST`

3 行加载成功。

由于数据格式错误`,0`行 丢弃。

由于数据错误`,0`行 没有加载。

跳过的逻辑记录总数`:0`

读取的逻辑记录总数`:3`

拒绝的逻辑记录总数`:0`

```
用时:40.831(ms)
```

## 3.7 自增列装载

自增列是比较特殊的列，为了保证数据库中自增列列值的正确性，用户在进行数据载入时需要特别注意。`dmfldr`提供了`SET_IDENTITY`参数对数据载入时自增列的处理进行设置。

如果指定`SET_IDENTITY`选项值为`TRUE`，则`dmfldr`将把从数据文件中读取的自增列值作为目标值插入数据库表中，用户应当保证每一行的自增列的值符合自增列的规则，否则将造成数据混乱；如果`SET_IDENTITY`选项值设置为`FALSE`，则`dmfldr`将忽略数据文件中对应自增列的值，服务器将根据自增列定义和表中已有数据自动生成自增列的值插入每一行的对应列。`SET_IDENTITY`默认为`FALSE`。

用户也可以通过设置控制文件中的`OPTION`选项来设置`SET_IDENTITY`的值，参数值的优先选择顺序为先`OPTION`选项，后参数选项。

此参数为可选参数，作用于`MODE`为`IN`的情况下，当`MODE`为`OUT`时无效。

例1：

`1)` 建表`TEST`，并插入两行数据

```
DROP TABLE TEST;
CREATE TABLE TEST(C1 INT IDENTITY(1,1),C2 VARCHAR);
INSERT INTO TEST(C2) VALUES('AAA');
INSERT INTO TEST(C2) VALUES('BBB');
COMMIT;
```

此时表`TEST`中的数据为：

行号 `C1 C2`

```
---------- ----------- ---
1 1 AAA
2 2 BBB
```

`2)` 编辑数据文件`test.txt`，存放路径为`/opt/data/test.txt`，文件内容如下

```
2|aaa
3|bbb
4|ccc
```

`3)` 编辑控制文件`test.ctrl`，存放路径为`/opt/data/test.ctrl`，内容如下：

```
LOAD DATA
INFILE '/opt/data/test.txt'
INTO TABLE test
FIELDS '|'
(
C1,
C2
)
```

`4)` 使用`dmfldr`进行数据载入

```
./dmfldr userid=SYSDBA/SYSDBA@localhost:5236 control=\'/opt/data/test.ctrl\' set_identity=false
```

`5)` 查看表`TEST`的数据

```
SELECT * FROM TEST;
```

行号 `C1 C2`

```
---------- ----------- ---
1 1 AAA
2 2 BBB
3 3 aaa
4 4 bbb
5 5 ccc
```

在这个例子中，表`TEST`中已有两行数据，由于`SET_IDENTITY`置为`FALSE`，因此在数据载入时`dmfldr`根据`C1`列的定义和表中已有数据，为`C1`列重新插入合适的值。

我们再看看如果将`SET_IDENTITY`置为`TURE`结果会怎样。

例2：

重复例1的`1)`、`2)`、3）步骤

`4)` 使用`dmfldr`进行数据载入

```
./dmfldr userid=SYSDBA/SYSDBA@localhost:5236 control=\'/opt/data/test.ctrl\' set_identity=true
```

`5)` 查看表`TEST`的数据

```
SELECT * FROM TEST;
```

行号 `C1 C2`

```
---------- ----------- ---
1 1 AAA
2 2 BBB
3 2 aaa
4 3 bbb
5 4 ccc
```

## 3.8 数据排序

`SORTED`参数用来设置数据是否已经按照聚集索引排序，默认为`FALSE`。

如果设置为`TRUE`，则用户必须保证数据已按照聚集索引排序完成，并且如果表中存在数据，需要插入的数据索引值要比表中数据的索引值大，服务器在做插入操作时顺序进行插入。若数据并未按照索引排序，则`dmfldr`会报错，装载失败。

如果设置为`FALSE`，则服务器对于每条记录进行定位插入。

用户也可以通过设置控制文件中的`OPTION`选项来设置`SORTED`的值。`SORTED`参数值的优先选择顺序为`OPTION`选项，参数选项。此参数为可选参数，作用于`MODE`为`IN`且`DIRECT`为`TRUE`的情况下，对于其他情况此参数无效。

在数据量大，并且确定数据已按照聚集索引排序完成的情况下，将`SORTED`参数设置为`TRUE`，可以提升装载性能。

例如：

`1)` 建表`TEST`

```
DROP TABLE TEST;
CREATE TABLE TEST(C1 INT CLUSTER PRIMARY KEY,C2 VARCHAR);
```

`2)` 编辑数据文件`test.txt`，存放路径为`/opt/data/test.txt`，文件内容如下

```
2|aaa
3|bbb
4|ccc
5|ddd
1|zzz
```

`3)` 编辑控制文件`test.ctrl`，存放路径为`/opt/data/test.ctrl`，内容如下：

```
LOAD DATA
INFILE '/opt/data/test.txt'
INTO TABLE test
FIELDS '|'
(
C1,
C2
)
```

`4)` 使用`dmfldr`进行数据载入

```
./dmfldr userid=SYSDBA/SYSDBA@localhost:5236 control=\'/opt/data/test.ctrl\' sorted=true
```

由于本例中数据文件中的数据并没有按照`C1`列排序，`dmfldr`将会报错。

不能使用`NOSORT`选项，数据非有序

## 3.9 空值处理

`dmfldr`通过设置`NULL_MODE`参数来处理空值。

- 设置为`TRUE`，载入时`NULL`字符串处理为`NULL`，载出时空值处理为`NULL`字符串
- 设置为`FALSE`，载入时`NULL`字符串处理为字符串，载出时空值处理为空串

例1：

`1)` 建表`TEST`

```
DROP TABLE TEST;
CREATE TABLE TEST(C1 INT,C2 VARCHAR);
```

`2)` 编辑数据文件`test.txt`，存放路径为`/opt/data/test.txt`，文件内容如下

```
1|aaa
2|NULL
3|null
```

`3)` 编辑控制文件`test.ctrl`，存放路径为`/opt/data/test.ctrl`，内容如下：

```
LOAD DATA
INFILE '/opt/data/test.txt'
INTO TABLE test
FIELDS '|'
(
C1,
C2
)
```

`4)` 使用`dmfldr`进行数据载入

```
./dmfldr userid=SYSDBA/SYSDBA@localhost:5236 control=\'/opt/data/test.ctrl\' null_mode=true
```

`5)` 查看表`TEST`的数据，数据文件中`C2`列的“`NULL`”和“`null`”字符串都被处理为空值

```
SELECT C1, IFNULL(C2, 'NULL VALUE') FROM TEST;
行号 C1 IFNULL(C2,'NULLVALUE')
---------- ----------- ----------------------
1 1 aaa
2 2 NULL VALUE
3 3 NULL VALUE
```

例2：

步骤`1)`、`2)`、`3)`与例1相同

`4)` 使用`dmfldr`进行数据载入

```
./dmfldr userid=SYSDBA/SYSDBA@localhost:5236 control=\'/opt/data/test.ctrl\' null_mode=false
```

`5)` 查看表`TEST`的数据，数据文件中`C2`列的“`NULL`”和“`null`”字符串直接被作为字符串值插入表中

```
SELECT C1, IFNULL(C2, 'NULL VALUE') FROM TEST;
行号 C1 IFNULL(C2,'NULLVALUE')
---------- ----------- ----------------------
1 1 aaa
2 2 NULL
3 3 null
```

## 3.10 类类型装载

`dmfldr`支持对`CLASS`类型数据的装载。`CLASS`类型装载和`LOB`类型一样，载入时需要指定`LOB_DIRECTORY`，另外需要指定`ENABLE_CLASS_TYPE`为`TRUE`；导出时，默认导出目录和数据文件所在目录一致，导出类类型形成的大字段文件默认为`dmfldr.lob`，导出目录和大字段文件可通过`LOB_DIRECTORY`和`LOB_FILE_NAME`参数设置。

> CLASS类型大字段数据文件无法通过手动创建，只有从表中导出到大字段文件中，并使用数据文件CLASS字段对应的偏移、字长进行导入。

例如：

`1)` 建表`TEST`

数据准备，创建类`mycls`的类头与类体，之后创建表`TEST`，其`C2`列类型为`mycls`类类型，并向`TEST`中插入两行数据。

`--`类头创建

```
CREATE CLASS mycls
AS
TYPE rec_type IS RECORD (c1 INT, c2 INT); --类型声明
```

`id INT; --`成员变量

```
r rec_type; --成员变量
FUNCTION f1(a INT, b INT) RETURN rec_type; --成员函数
FUNCTION mycls(id INT , r_c1 INT, r_c2 INT) RETURN mycls; --用户自定义构造函数
END;
/
```

`--`类体创建

```
CREATE OR REPLACE CLASS BODY mycls
AS
FUNCTION f1(a INT, b INT) RETURN rec_type
AS
BEGIN
r.c1 = a;
r.c2 = b;
RETURN r;
END;
FUNCTION mycls(id INT, r_c1 INT, r_c2 INT) RETURN mycls
AS
BEGIN
```

`this.id = id; --`可以使用`this.`来访问自身的成员

```
r.c1 = r_c1; --this也可以省略
r.c2 = r_c2;
RETURN this; --使用return this 返回本对象
END;
END;
/
--建表TEST
DROP TABLE TEST;
CREATE TABLE TEST(C1 INT,C2 mycls);
```

`--`插入数据：

```
INSERT INTO TEST VALUES(1,mycls(1,1,1));
INSERT INTO TEST VALUES(2,mycls(2,2,2));
COMMIT;
```

`2)` 编辑控制文件`test.ctrl`，存放路径为`/opt/data/test.ctrl`，内容如下：

```
LOAD DATA
INFILE '/opt/data/test.txt'
INTO TABLE test
FIELDS '|'
(
C1,
C2
)
```

`3)` 使用`dmfldr`进行数据导出

```
./dmfldr userid=SYSDBA/SYSDBA@localhost:5236 control=\'/opt/data/test.ctrl\' mode=\'out\' lob_directory=\'/opt/data\'
```

`4)` 在指定的`LOB_DIRECTORY`目录会生成大字段文件`dmfldr.lob`，在指定的数据文件路径生成的数据文件内容如下：

```
1|dmfldr.lob:0:70
2|dmfldr.lob:70:70
```

`5)` 创建一张新表`TEST2`，表的两列都为`mycls`类类型

```
CREATE TABLE TEST2(C1 MYCLS,C2 MYCLS);
```

`6)` 编辑数据文件`test2.txt`，存放路径为`/opt/data/test2.txt`，文件内容如下：

```
dmfldr.lob:70:70|dmfldr.lob:0:70
dmfldr.lob:0:70|dmfldr.lob:70:70
```

`7)` 编辑控制文件`test2.ctrl`，存放路径为`/opt/data/test2.ctrl`，内容如下：

```
LOAD DATA
INFILE '/opt/data/test2.txt'
INTO TABLE test2
FIELDS '|'
(
C1,
C2
)
```

`8)` 使用`dmfldr`进行数据导入

```
./dmfldr userid=SYSDBA/SYSDBA@localhost:5236 control=\'/opt/data/test2.ctrl\'
lob_directory=\'/opt/data/\' enable_class_type=true
```

`9)` 查看表`TEST2`的数据

行号 `C1 C2`

```
---------- ----------------------------- -----------------------------
1 SYSDBA.MYCLS(2,REC_TYPE(2,2)) SYSDBA.MYCLS(1,REC_TYPE(1,1))
2 SYSDBA.MYCLS(1,REC_TYPE(1,1)) SYSDBA.MYCLS(2,REC_TYPE(2,2))
```

## 3.11 个性化设置

用户通过设置`dmfldr`的`SKIP`、`LOAD`、`ROWS`参数，可以根据自己的需求调整装载的起始行、装载最大行数以及每次提交的行数。

`SKIP`参数用来设置跳过数据文件起始的逻辑行数，整形数值。默认的跳过起始行数为0行。如果用户指定了多个文件，且起始文件中的行数不足`SKIP`所指定的行数，则`dmfldr`工具会扫描下一个文件直至累加的行数等于`SKIP`所设置的行数或者所有文件都已扫描结束。

`LOAD`参数用来设置装载的最大行数，整形数值。默认的最大装载行数为数据文件中的所有行数。`LOAD`指定的值是包括`SKIP`指定的跳过的行数。

`ROWS`参数用来设置每次提交的行数，整形数值。默认的提交行数为50000行。提交行数的值表示提交到服务器的行数，并不一定代表按照数据文件中的数据顺序的行数。用户可以根据实际情况调整每次提交的行数，以达到性能的最佳点。`ROWS`参数作用于`MODE`为`IN`的情况下，当`MODE`为`OUT`时无效。

例如：

`1)` 建表`TEST`

```
DROP TABLE TEST;
CREATE TABLE TEST(C1 INT, C2 VARCHAR);
```

`2)` 编辑数据文件`test.txt`，存放路径为`/opt/data/test.txt`，文件内容如下

```
1|aaa
2|bbb
3|ccc
4|ddd
5|eee
6|fff
7|ggg
8|hhh
9|iii
10|jjj
```

`3)` 编辑控制文件`test.ctrl`，存放路径为`/opt/data/test.ctrl`，内容如下：

```
LOAD DATA
INFILE '/opt/data/test.txt'
INTO TABLE test
FIELDS '|'
(
C1,
C2
)
```

`4)` 使用`dmfldr`进行数据载入

```
./dmfldr userid=SYSDBA/SYSDBA@localhost:5236 control=\'/opt/data/test.ctrl\' skip=3 load=5
```

`5)` 查看表`TEST`的数据，载入时跳过了数据文件的前3行数据，且只载入了5条数据。

```
SELECT * FROM TEST;
```

行号 `C1 C2`

```
---------- ----------- ---
1 4 ddd
2 5 eee
3 6 fff
4 7 ggg
5 8 hhh
```

## 3.12 MPP本地分发

`MPP_CLIENT`参数用来设置在`DM MPP`环境下使用`dmfldr`进行数据装载时的数据分发方式。

当`DM`数据库服务器环境为单站点时此参数无效。当服务器环境为`MPP`环境时，若`MPP_CLIENT`为`TRUE`，`dmfldr`采用客户端分发模式；若`MPP_CLIENT`为`FALSE`，则采用本地分发模式。

客户端分发模式下，数据在`dmfldr`客户端分发好后直接往指定站点发送数据。

本地分发模式下，导入时，`dmfldr`直接将数据发送到连接的站点，数据最终在连接的站点；导出时，`dmfldr`只导出连接站点的数据。

`MPP`环境下要配置`dmmal.ini`文件中的`MAL_INST_HOST`和`MAL_INST_PORT`参数。

例如：

当前`DM`数据库服务器环境为`MPP`环境，两个节点，`SEQNO`号分别为0、1。使用`dmfldr`采用本地分发方式进行数据装载，连接的节点为`SEQNO`为0的节点。

`1)` 建表`TEST`

```
DROP TABLE TEST;
CREATE TABLE TEST(C1 INT, C2 INT);
```

`2)` 编辑数据文件`test.txt`，存放路径为`/opt/data/test.txt`，文件内容如下

```
1|1
2|2
3|3
4|4
5|5
6|6
7|7
8|8
9|9
10|10
```

`3)` 编辑控制文件`test.ctrl`，存放路径为`/opt/data/test.ctrl`，内容如下：

```
LOAD DATA
INFILE '/opt/data/test.txt'
INTO TABLE test
FIELDS '|'
(
C1,
C2
)
```

`4)` 使用`dmfldr`进行数据载入

```
./dmfldr userid=SYSDBA/SYSDBA@localhost:5236 control=\'/opt/data/test.ctrl\' mpp_client=false
```

`5)` 查询`SEQNO`为0的节点上`TEST`表的数据

```
SELECT * FROM TEST WHERE SF_GET_EP_SEQNO(ROWID)=0;
```

行号 `C1 C2`

```
---------- ----------- -----------
1 1 1
2 2 2
3 3 3
4 4 4
5 5 5
6 6 6
7 7 7
8 8 8
9 9 9
10 10 10
```

`6)` 查询`SEQNO`为1的节点上`TEST`表的数据

```
SELECT * FROM TEST WHERE SF_GET_EP_SEQNO(ROWID)=0;
```

未选定行

## 3.13 提升dmfldr性能

用户在使用`dmfldr`时根据系统和数据的具体情况对一些参数进行调整，可以获得更好的性能，这些参数包括：

- `BUFFER_NODE_SIZE`

`BUFFER_NODE_SIZE`设置读取文件缓冲区页大小，值越大，缓冲区的页越大，每次读取的数据就越多，每次发送到服务器的数据也就越多，效率越高。但其大小受`dmfldr`客户端内存大小限制。

- `READ_ROWS`

在某些情况下，`BUFFER_NODE_SIZE`读入的数据行数很大，而后续操作处理不了这么大的行数，此时可以用`READ_ROWS`来限制处理的行数。`dmfldr`取`READ_ROWS`和`BUFFER_NODE_SIZE`中较小的值作为一次处理的行数。

- `SEND_NODE_NUMBER`

指定`dmfldr`在数据载入时发送节点的个数，默认由系统计算一个初始值。若在数据载入时发现发送节点不够用，系统会动态增加分配。在系统内存足够的情况下，可以适当设大`SEND_NODE_NUMBER`值，提升`dmfldr`载入性能。

- `TASK_THREAD_NUMBER`

指定`dmfldr`在数据载入时处理用户数据的线程数目。默认情况下，`dmfldr`将该参数值设为系统`CPU`的个数，但当`CPU`个数大于8时，默认值都被置为8。在`dmfldr`客户端所在机器`CPU`大于8环境中，提高`TASK_THREAD_NUMBER`值可以提升`dmfldr`装载性能。

- `BLDR_NUM`

水平分区表装载时，指定服务器`BLDR`的最大个数，默认为100。

服务器的`BLDR`保存水平分区子表相关信息，`BLDR_NUM`的设置也就指定了服务器能同时载入的水平分区子表的个数。若`BLDR_NUM`设置太大，当水平分区子表数过多时，可能会导致服务器内存不足。当载入时实际需要的`BLDR`个数超出`BLDR_NUM`设置时，会淘汰指定子表的`BLDR`，并替换为新的子表`BLDR`。

- `BDTA_SIZE`

`BDTA`（`Batch DaTA`）的大小，默认为5000。

`BDTA`代表`DM7`数据库批量数据处理机制中一个批量，在内存、`CPU`允许的条件下，增大`BDTA_SIZE`能加快装载速度；在网络是装载性能瓶颈时，增大`BADT_SIZE`影响不大。

- `INDEX_OPTION`

索引的设置选项，默认为1。`INDEX_OPTION`的可选项有1和2。

1代表服务器装载数据时先不刷新二级索引，而是将新数据按照索引预先排序，在装载完成后，再将排好序的数据插入索引。如果在数据载入前，目标表中已有较多数据，建议`INDEX_OPTION`置为1。

2代表服务器在快速装载过程中不刷新二级索引数据，只在装载完成时重建所有二级索引。如果在数据载入前，目标表中没有数据或数据量较小，建议`INDEX_OPTION`置为2。

## 3.14 dmfldr使用限制

`dmfldr`的使用存在以下一些限制：

- 不支持向临时表、外部表装载数据
- 不支持向系统表装载数据
- 不支持向带有位图索引的表装载数据
- 不支持向带有函数索引的表装载数据
- 不支持向带有全文索引的表装载数据
- 不支持单独对表垂直分区子表装载数据
- 不支持向`DCP`代理装载数据
- `dmfldr`装载时，对约束进行检查，对各种约束的处理机制如下表所示

表`3.1 dmfldr`的约束检查机制

| 约束 | 数据不满足时 | 数据插入与否 | 约束是否有效 |
| --- | --- | --- | --- |
| 非空约束(NOT NULL) | 报错 | 不插入 | 有效 |
| 聚集索引(CLUSTER PRIMARY KEY) | 报错 | 不插入 | 有效 |
| 唯一约束(UNIQUE， PRIMARY KEY) | 报错 | 插入 | 失效 |
| 引用约束(FOREIGN KEY) | 不报错 | 插入 | 有效 |
| CHECK约束(CHECK) | 不报错 | 插入 | 有效 |
