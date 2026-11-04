---
title: "3 DIsql环境变量设置"
book: "DM7 DIsql使用手册"
version: "DM7"
source: "temp/doc/special/DM7°ïÖúÎÄµµ.chm#~htm/DIsql使用手册.htm"
tags:
  - dameng
  - dm7
  - disql
---

使用`SET`命令可以对当前`DIsql`的环境变量进行设置。并通过`SHOW`命令来查看当前系统中环境变量的设置情况。

## 3.1 DIsql环境变量

`DIsql`中的系统环境变量，汇总如下：

表`3.1 DIsql`命令的快速参考

| 变量名称 | 属性 | 用途 |
| --- | --- | --- |
| AUTO[COMMIT] |  | 设置自动提交 |
| DEFINE |  | 定义本地变量 |
| ECHO |  | 显示脚本中正在执行的SQL语句 |
| FEED[BACK] | <6（默认值）\|n \|ON \|OFF> | 显示当前SQL语句查询或修改的行数 |
| HEA[DING] |  | 显示列标题 |
| LINESHOW |  | 显示行号 |
| NEWP[AGE] | <1（默认值）\|n \|NONE> | 设置页与页之间的分隔 |
| PAGES[IZE] | <14（默认值）\|n> | 设置一页有多少行数 |
| TIMING |  | 显示每个SQL语句花费的执行时间 |
| VER |  | 列出环境变量被替换前、 后的控制命令文本 |
| LONG | <800(默认值)\|n> | 设置大字段类型显示的最大字节数 |
| LINESIZE |  | 设置屏幕上一行显示宽度 |
| SERVEROUT[PUT] | <ON \| OFF(默认值)> [SIZE <20000(默认值)\|n>] [FOR[MAT] <WRA[PPED] \| WOR[D_WRAPPED](默认值) \| TRU[NCATED]>] | 在块中有打印信息时， 是否打印，以及打印的格式 |
| SCREENBUFSIZE | <DEFAULT(20K) \| n> | 设置屏幕缓冲区的长度 |
| CHAR_CODE | <GBK \| UTF8 \| DEFAULT (默认值，操作系统的编码方式)> | 设置SQL语句的编码方式 |
| CURSOR | <STATIC \| FORWARDONLY (默认值)\| DEFAULT> | 设置DPI语句句柄中游标的类型 |
| AUTOTRACE | <OFF \| NL \| INDEX \| ON \| TRACE> | 设置执行计划和统计信息的跟踪 |
| DESCRIBE | [DEPTH <1(默认值) \| n \| ALL>] [LINE[NUM] ] [INDENT ] | 设置DESCRIBE的显示方式 |
| TRIMS[POOL] | <OFF\| ON> | 设置spool文件中每行的结尾空格 |
| LOBCOMPLETE | <OFF\| ON> | 设置大字段数据是否从服务器全部取出 |
| COLSEP | COLSEP [text] | 设置列之间的分割符 |

## 3.2 SET命令用法

`SET`命令用于设置`DIsql`系统环境变量。

语法如下：

```
SET { }
```

``：变量名称，参考`3.1`节。

``：属性。

可以同时`SET`多个环境变量，如：`Set heading on timing on`。一旦`SET`之后某个环境变量出错，那么该变量之后的将不再起作用。

## 3.3 使用SET命令设置环境变量详解

本节详细介绍如何使用`SET`命令对环境变量进行设置。

### 3.3.1 AUTO[COMMIT]

设置当前`session`是否对修改的数据进行自动提交。

语法如下：

```
SET AUTO[COMMIT]
```

`ON`：表示打开自动提交，所有执行的`SQL`语句的事务将自动进行提交。

`OFF`：表示关闭自动提交，所有执行的`SQL`语句的事务将由用户显式提交，为默认设置。

### 3.3.2 DEFINE

是否使用`DEFINE`定义本地变量。

语法如下：

`SET DEFINE`

c：表示打开`DEFINE`功能，同时定义前缀变量符号，c为定义的前缀符号。

`ON`：表示打开`DEFINE`功能，使用默认前缀符号&。

`OFF`：表示不使用`DEFINE`功能。

示例如下，打开`DEFINE`功能，并设置#为变量前缀。

```
SQL> SET DEFINE #
SQL> SELECT #A FROM DUAL;
```

输入 A的值`:1`

```
原值 1:SELECT #A FROM DUAL;
新值 1:SELECT 1 FROM DUAL;
```

行号 1

```
---------- -----------
1 1
```

已用时间`: 0.178(`毫秒`).` 执行号`:722.`

### 3.3.3 ECHO

在用`START`命令执行一个`SQL`脚本时，是否显示脚本中正在执行的`SQL`语句。

语法如下：

```
SET ECHO
```

### 3.3.4 FEED[BACK]

是否显示当前`SQL`语句查询或修改的总行数。

语法如下：

```
SET FEED[BACK] <6（默认值）|n|ON|OFF>
```

n：表示结果大于n行时，才显示结果的总行数。

`ON`：打开显示开关，使用默认值6。

`OFF`：关闭显示开关。

示例如下：

```
图3.1 FEEK[BACK]用法
```

### 3.3.5 HEA[DING]

是否显示列标题。

语法如下：

```
SET HEA[DING]
```

当`set heading off`时，在每页的上面不显示列标题，而是以空白行代替。

示例如下：

```
图3.2HEA[DING]用法
```

### 3.3.6 LINESHOW

`lineshow`设置是否显示行号。

语法如下：

```
SET LINESHOW;
```

默认为每行输出打印行号。

例如：

```
图3.3 LINESHOW用法
```

### 3.3.7 NEWP[AGE]

设置页与页之间的分隔。

语法如下：

```
SET NEWP[AGE] <1（默认值）|n|NONE>
```

当`set newpage 0` 时，在每页的开头有一个换号符。

当`set newpage n` 时，在页和页之间隔着n个空行。

当`set newpage none` 时，在页和页之间没有任何间隔。

### 3.3.8 PAGES[IZE]

设置一页有多少行数。

语法如下：

```
SET PAGES[IZE] <14（默认值）|n>
```

如果设为0，则所有的输出内容为一页并且不显示列标题。默认值为14。

### 3.3.9 TIMING

显示每个`SQL`语句花费的执行时间。

语法如下：

```
SET TIMING
```

### 3.3.10 VER

`VER` 是否列出环境变量被替换前、后的控制命令文本。默认值为`ON`，表示列出命令文本。

语法如下：

```
SET VER < ON（默认值）|OFF>
```

示例如下：

```
SQL> SET VERIFY OFF
SQL> SELECT &A FROM DUAL;
```

输入 A的值`:3`

行号 3

```
---------- -----------
1 3
```

已用时间`: 0.558(`毫秒`).` 执行号`:733.`

```
SQL> SET VERIFY ON
SQL> SELECT &A FROM DUAL;
```

输入 A的值`:3`

```
原值 1:SELECT &A FROM DUAL;
新值 1:SELECT 3 FROM DUAL;
```

行号 3

```
---------- -----------
1 3
```

已用时间`: 0.127(`毫秒`).` 执行号`:734.`

### 3.3.11 LONG

设置`BLOB`、`CLOB`、`CHAR`、`VARCHAR`、`BINARY`、`VARBINARY`、`CLASS`等类型一列能显示的最大字节数。

语法如下：

```
SET LONG <800(默认值)|n>
```

### 3.3.12 LINESIZE

设置屏幕上一行显示宽度。

语法如下：

```
SET LINESIZE
```

### 3.3.13 SERVEROUT[PUT]

在块中有打印信息时，是否打印，以及打印的格式。设置之后，可以使用`DBMS_OUTPUT`包打印(认为`DBMS_OUTPUT`包已经创建)。

语法如下：

```
SET SERVEROUT[PUT] [SIZE <20000(默认值)|n>]
[FOR[MAT] <WRA[PPED] | WOR[D_WRAPPED](默认值) | TRU[NCATED]>]
```

`ON/OFF`：是否打印。

`SIZE`：打印的最大长度。

`WORD_WRAPPED`：按照单词分隔。

`TRUNCATED`：单词被截断。

`FORMAT`：按照服务器返回的显示，不做格式化。

示例如下，对比两个结果，不难发现，第二个结果中的单词被截断。

```
SQL> SET SERVEROUTPUT ON FORMAT WORD_WRAPPED
SQL> SET LINESIZE 20
SQL> BEGIN
DBMS_OUTPUT.PUT_LINE('If there is nothing left to do');
DBMS_OUTPUT.PUT_LINE('shall we continue with plan B?');
END;
/
If there is nothing
left to do
shall we continue with
plan B?
```

`PL/SQL` 过程已成功完成

已用时间`: 1.140(`毫秒`).` 执行号`:729.`

```
SQL> SET SERVEROUTPUT ON FORMAT TRUNCATED
SQL> SET LINESIZE 20
SQL> BEGIN
2 DBMS_OUTPUT.PUT_LINE('If there is nothing left to do');
3 DBMS_OUTPUT.PUT_LINE('shall we continue with plan B?');
4 END;
5 /
If there is nothing
shall we continue wi
```

`PL/SQL` 过程已成功完成

已用时间`: 0.330(`毫秒`).` 执行号`:731.`

### 3.3.14 SCREENBUFSIZE

设置屏幕缓冲区的长度。用来存储屏幕上显示的内容。

语法如下：

```
SET SCREENBUFSIZE
```

### 3.3.15 CHAR_CODE

设置`SQL`语句的编码方式。

语法如下：

`SET CHAR_CODE `

### 3.3.16 CURSOR

设置`DPI`语句句柄中游标的类型。

语法如下：

```
SET CURSOR <STATIC | FORWARDONLY (默认值)| DEFAULT>
```

### 3.3.17 AUTOTRACE

设置执行计划和统计信息的跟踪。

语法如下：

```
SET AUTOTRACE
```

当 `SET AUTOTRACE OFF`时，停止`AUTOTRACE`功能，常规执行语句。

当 `SET AUTOTRACE NL`时，开启`AUTOTRACE`功能，不执行语句，如果执行计划中有嵌套循环操作，那么打印`NL`操作符的内容。

当 `SET AUTOTRACE INDEX(`或者`ON)`时，开启`AUTOTRACE`功能，不执行语句，如果有表扫描，那么打印执行计划中表扫描的方式、表名和索引。

当 `SET AUTOTRACE TRACE`时，开启`AUTOTRACE`功能，执行语句，打印执行计划。此功能与服务器`EXPLAIN`语句的区别在于，`EXPLAIN`只生成执行计划，并不会真正执行`SQL`语句，因此产生的执行计划有可能不准。而`TRACE`获得的执行计划，是服务器实际执行的计划。

### 3.3.18 DESCRIBE

设置`DESCRIBE`对象结构信息的显示方式。

语法如下：

```
SET DESCRIBE [DEPTH <1(默认值) | n | ALL>] [LINE[NUM] ] [INDENT ]
```

`DEPTH`：结构信息显示至第N层，默认只显示第1层。范围是`1-40`。当设置为`ALL`时，`DEPTH`为40。

`LINENUM`：是否显示对象行号，成员显示父亲的行号。

`INDENT`：当对象的类型是复合类型时，是否通过缩进的方式显示成员信息。

### 3.3.19 TRIMS[POOL]

设置`TRIMS[POOL]`，和`SPOOL`功能结合使用。

语法如下：

```
SET TRIMS[POOL] <OFF(默认值) | ON>
```

对于`SPOOL`文件，是否去除输出每行的结尾空格，缺省为`OFF`。

### 3.3.20 LOBCOMPLETE

设置`LOBCOMPLETE`，是否从服务器中全部取出大字段数据。

语法如下：

```
SET LOBCOMPLETE <OFF(默认值) | ON>
```

对于大字段数据，是否从服务器全部取出，防止死锁的发生；与显示长度不同，即便是全部取出，也可以只显示一部分。

### 3.3.21 COLSEP

设置列之间的分割符。

语法如下：

```
SET colsep [text]
```

如果`text`包含空格或标点符号，请用单引号扩起来。默认为一个空格。

## 3.4 使用SHOW命令查看环境变量

通过使用`SHOW`命令，用户就可以快速而方便的了解到`DIsql`环境的当前环境变量设置。

`SHOW`可以显示一个或多个变量。显示多个变量时中间加空格，当其中某一变量出错之后，后面的仍会继续显示。

语法如下：

```
SHOW {}
:环境变量。
```

示例如下，显示`heading`和`timing`两个变量：

```
SQL> SHOW HEADING TIMING
HEADING ON.
TIMING ON
```
