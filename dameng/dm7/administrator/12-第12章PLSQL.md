---
title: "第12章 PL/SQL"
book: "DM7系统管理员手册"
version: "DM7"
source: "temp/doc/DM7系统管理员手册.pdf#page=113"
tags:
  - dameng
  - dm7
  - administrator
---

## 第12章 PL/SQL

## 12.1 PL/SQL 概述

`PL/SQL`是达梦数据库对标准`SQL`语言的扩展，叫做过程化`SQL`语言。在`PL/SQL`程序中，包括一整套的数据类型、条件结构、循环结构和异常处理结构等，`PL/SQL`可以执行`SQL`语句，`SQL`语句中也可以使用`PL/SQL`函数。

### 12.1.1  PL/SQL 优点

与`SQL`相比，`PL/SQL`体现了模块化的程序设计思想，具体优点如下：

1. `PL/SQL` 是一种高性能的基于事务处理的语言，能运行在`DM` 环境中，支持所有数

据处理命令。通过使用`PL/SQL`程序单元处理`SQL`的数据定义和数据控制元素；

2. `PL/SQL` 支持所有`SQL` 数据类型和所有`SQL` 函数，同时支持所有`DM` 对象类型；
3. `PL/SQL` 块可以被命名和存储在`DM` 数据库中，同时也能被其他的`PL/SQL` 程序或

`SQL`命令调用，任何客户/服务器工具都能访问`PL/SQL`程序，具有很好的可重用性；

4. 可以使用`DM` 的管理工具`Manager` 管理存储在服务器中的`PL/SQL` 程序的安全性。

可以授权或撤销数据库其他用户访问`PL/SQL`程序的能力；

5. `PL/SQL` 代码可以使用任何`ASCII` 文本编辑器编写，所以对任何达梦数据库能够运

行的操作系统都是非常便利的；

6. 对于`SQL`，`DM` 服务器必须处理每一条`SQL` 语句，在网络环境下这就意味着每一个

独立的调用都必须被`DM`服务器处理，占用大量的服务器时间，容易导致网络拥挤，而`PL/SQL`是以整个语句块被服务器处理，降低了网络拥挤，同时可以大大提高访问数据库的效率。

### 12.1.2  PL/SQL 语句块

`PL/SQL`语言的基本程序单元是语句块，主要的块形式有函数、过程和匿名块。每个语句块由关键字`DECLARE`、`BEGIN`、`EXCEPTION`和`END`划分为说明部分、执行部分和异常处理部分。其中执行部分是必须的，说明和异常处理部分可以省略。语句块可以嵌套，它可以出现在任何其他语句可以出现的位置，格式如下：

```
DECLARE
```

变量声明部分

```
BEGIN
```

可执行部分

```
EXCEPTION
```

异常处理部分

```
END
```

其中变量声明部分用来定义变量、类型、游标、子程序、异常等。被声明的元素在本块范围内有效，这一部分在`PL/SQL`块中是可选的。

可执行部分是`PL/SQL`块的主体，它包含了`PL/SQL`块的可执行代码，是必不可少的部

103

## 第12 章 PL/SQL

分，`PL/SQL`块的主要功能体现在这一部分。

异常处理部分用于处理`PL/SQL`块在执行过程中发生的错误。如果块执行正常，则块正常结束，否则从出现错误的语句开始，转至异常处理部分开始执行，即进行异常处理，这部分在`PL/SQL`块中也是可选的。

最简单的`PL/SQL`块仅包含由`BEGIN`和`END`限定的可执行部分。例如：

```
BEGIN
PRINT 'HELLO WORLD';
END;
```

`PL/SQL`块的代码可以直接在`“SQL>”`提示符下输入。输入结束后，执行命令`“/”`即可使该`PL/SQL`块开始执行。

## 12.2 PL/SQL 变量

变量的定义必须放在`PL/SQL`块的变量声明部分，变量定义有两种格式，分别为：

```
变量名[CONSTANT]  类型 [NOT NULL] [DEFAULT 默认值]
变量名[CONSTANT]  类型 [NOT NULL] [:=初始值]
```

变量名要遵守一定的命名规则。变量名必须以字母开头，包含数字、字母、下划线以及$、#符号，长度不能超过128 字符，并且不能与达梦数据库的关键字相同，变量名与大小写是无关的。

变量在定义时可以指定默认值或初始值，在`PL/SQL`块的运行过程中也可以对其赋值。

赋值语句有两种方式：

（1）直接赋值语句

变量名`:=`表达式或`SET`变量名=表达式

（2）通过`SQL SELECT INTO`或`FETCH INTO`给变量赋值

`SELECT <`表达式`>{,<`表达式`>} [INTO <`主变量名`>{,<`主变量名`>}] FROM <`表引用`>{,<`表引用`>} …;`或

```
FETCH [NEXT|PREV|FIRST|LAST|ABSOLUTE N|RELATIVE N]<游标名> [INTO<主变量名>{,<
```

主变量名`>}];`

注：`FETCH`中的N，起始值为0。

常量与变量相似，但常量的值在程序内部不能改变，常量的值在定义时赋予，它的声明方式与变量相似，但必须包含关键字`CONSTANT`。

如果需要打印输出变量的值，则要调用`PRINT`语句，如果数据类型不一致，则系统会自动将它转换为`VARCHAR`类型输出。除了变量的声明外，变量的赋值、输出等操作都要放在`PL/SQL`块的可执行部分。

下面是一个变量声明和赋值的例子。

```
CREATE TABLE STUDENT(NAME VARCHAR(30) , AGE INT, SNO INT PRIMARY KEY);
INSERT INTO STUDENT VALUES('ZHANGSAN', 18, 10010);
INSERT INTO STUDENT VALUES('LISI', 20, 10011);
CREATE OR REPLACE PROCEDURE PROC AS
C1 CHAR(20) DEFAULT 'ABC';                 --默认值
C2 CONSTANT VARCHAR:= 'HELLO WORLD!';    --常量
C3 INT NOT NULL := 1;                       --约束
C4 INT;
NAME1 VARCHAR;
SNO1 INT;
CURSOR_1 CURSOR;
BEGIN
```

104

## 第12 章 PL/SQL

```
OPEN CURSOR_1 FOR SELECT SNO FROM STUDENT;
SET C3 = 10;
C4 := C3 * 100;
SELECT NAME INTO NAME1 FROM STUDENT WHERE SNO = 10010;
FETCH ABSOLUTE 1 CURSOR_1 INTO SNO1;
CLOSE CURSOR_1;
PRINT C1; PRINT C2; PRINT C3; PRINT C4;
PRINT NAME1||' '||SNO1;
END;
```

运行结果：

```
ABC
HELLO WORLD!
10
1000
ZHANGSAN 10011
```

## 12.3 PL/SQL 数据类型和操作符

在`PL/SQL`块中可以定义变量和数据类型，同时`PL/SQL`有一系列操作符，这使得`PL/SQL`块对数据的处理更加灵活。

### 12.3.1  SQL 数据类型

`PL/SQL`支持所有的`SQL`数据类型，其中包括：字符数据类型、多媒体数据类型、精确数值数据类型、近似数值数据类型、一般日期时间数据类型、时间间隔数据类型，如表`12.1`所示：

表`12.1 PL/SQL`支持的数据类型列表类型名类型描述CHAR(N) 固定串长度为N的字符串，N<=8188 VARCHAR(N) 最大字符串长度为N的可变长度字符串，N<=8188 IMAGE 影像数据类型，可变长度的二进制数据，最大长度为2G-1 TEXT 文本数据类型，可变长度的字符数据，最大长度为2G-1 BLOB 二进制大对象，可变长度的二进制数据，最大长度为2G-1 CLOB 字符串大对象，可变长度的字符数据，最大长度为2G-1 BFILE 操作系统文件大对象，作为二进制文件处理，只读BIT 单个二进制位数据BOOL 在数据库中用1、0 进行存储，1 表示TRUE，0 表示FALSE BINARY(N) 固定长度为N的二进制数据，N<=8188 VARBINARY(N) 最大长度为N的可变长度二进制数据，N<=8188 TINYINT 精度为3，刻度为0 的有符号精确数字，取值范围-128…127 SMALLINT 精度为5，刻度为0 的有符号精确数字，取值范围-32,768…32,767 BYTE 与TINYINT 相似，精度为3，刻度为0 INTEGER/INT 精度为10，刻度为0 的有符号精确数字，取值范围-2[31]…2[31]-1 PLS_INTEGER 与INTEGER 相同BIGINT 精度为19，刻度为0 的有符号精确数字值，取值范围-2[63]…2[63]-1 105

## 第12 章 PL/SQL

DECIMAL(P,S) 精度为P，刻度为S的有符号精确数字值，1≤P≤38，S≤P DEC(P,S) 与DECIMAL 相同NUMERIC(P,S) 精度为P，刻度为S的有符号精确数字值，1≤P≤38，S≤P二进制精度为24 的有符号近似数字值，取值范围0 或者绝对值为：

REAL 10[-38]…10[38]二进制精度为53 的有符号近似数字值，取值范围0 或者绝对值为：

FLOAT 10[-308]…10[308]二进制精度为53 的有符号近似数字值，取值范围0 或者绝对值为：

DOUBLE 10[-308]…10[308]DATE 日期数据类型，年月日字段，格式与GREGORIAN（罗马）日历一致TIME(P) 时间数据类型，时分秒字段，精度P指定了秒的精度TIMESTAMP(P) 时间戳数据类型，年月日时分秒字段，精度P指定了秒的精度年间隔，即两个日期之间的年数字，P为时间间隔的首项字段精度(后INTERVAL YEAR(P)面简称为：首精度)INTERVAL MONTH(P) 月间隔，即两个日期之间的月数字，P为时间间隔的首精度INTERVAL DAY(P) 日间隔，即为两个日期/时间之间的日数字，P为时间间隔的首精度INTERVA L HOUR(P) 时间隔，即为两个日期/时间之间的时数字，P为时间间隔的首精度INTERVAL MINUTE(P) 分间隔，即为两个日期/时间之间的分数字，P为时间间隔的首精度秒间隔，即为两个日期/时间之间的秒数字，P为时间间隔的首精度，INTERVAL SECOND(P,Q)Q为时间间隔秒精度INTERVAL YEAR(P) TO 年月间隔，即两个日期之间的年月数字，P为时间间隔的首精度MONTH日时间隔，即为两个日期/时间之间的日时数字，P为时间间隔的首精INTERVAL DAY(P) TO HOUR度日时分间隔，即为两个日期/时间之间的日时分数字，P为时间间隔的INTERVAL DAY(P) TO MINUTE首精度INTERVAL DAY(P)TO 日时分秒间隔，即为两个日期/时间之间的日时分秒数字，P为时间间SECOND(Q) 隔的首精度，Q为时间间隔秒精度INTERVALL HOUR(P) TO 时分间隔，即为两个日期/时间之间的时分数字，P为时间间隔的首精MINUTE 度INTERVAL HOUR(P) TO 时分秒间隔，即为两个日期/时间之间的时分秒数字，P为时间间隔的SECOND(Q) 首精度，Q为时间间隔秒精度INTERVAL MINUTE(P) TO 分秒间隔，即为两个日期/时间之间的分秒间隔，P为时间间隔的首精SECOND(Q) 度，Q为时间间隔秒精度

`PL/SQL`除了支持表`12.1`中所示的`SQL`数据类型外，为了方便用户使用，`DM`扩展提供了`%TYPE`、`%ROWTYPE`、记录类型、数组类型、索引表类型和类类型。

### 12.3.2  %TYPE 和%ROWTYPE

在许多情况下，存储过程变量可以被用来处理存储在数据库表中的数据。在这种情况下，变量应该拥有与表列相同的类型。例如表`T(ID INT, NAME VARCHAR(30))`中有个字段`NAME`类型为`VARCHAR(30)`。对应的在存储过程中，我们可以声明一个变量： `DECLARE``V_NAME VARCHAR(30);`但是如果T中的`NAME`字段定义发生了变化，比如变为`VARCHAR(100)`。那么存储过程中的变量`V_NAME`也要做相应修改为`DECLARE V_NAME``VARCHAR(100);`如果您有很多的变量以及存储过程代码，这种处理可能是十分耗时和容易出错的。

106

## 第12 章 PL/SQL

为了解决上述问题，`DM`提供了`%TYPE`类型。`%TYPE`可以附加在表列或者另外一个变量上，并返回其类型。例如：`DECLARE V_NAME T.NAME % TYPE;`通过使用`%TYPE`，`V_NAME`将拥有T表的`NAME`列所拥有的类型；如果表T的`NAME`列类型定义发生变化，`V_NAME`的类型也随之自动发生变化，而不需要用户手动修改。

下面给出一个`%TYPE`类型的使用例子。

```
CREATE TABLE T(ID INT, NAME VARCHAR(30));
INSERT INTO T VALUES(1, 'ZHANGSAN');
CREATE OR REPLACE PROCEDURE PROC AS
DECLARE
V1 T.NAME %TYPE;
C1 CURSOR;
BEGIN
OPEN C1 FOR SELECT NAME FROM T WHERE ID = 1;
FETCH C1 INTO V1;
PRINT V1;
CLOSE C1;
END;
```

与`%TYPE`类似，`%ROWTYPE`将返回一个基于表定义的运算类型，它将一个记录声明为具有相同类型的数据库行。例如：`DECLARE V_TREC T % ROWTYPE;`将定义一个记录，该记录中的字段将与表T中的列相对应。`V_TREC`变量会拥有下面这样的结构：`(ID INT, NAME``VARCHAR(30))`，与`%TYPE`类似，如果表定义改变了，那么`%ROWTYPE`定义的变量也会随之改变。

下面是一个`%ROWTYPE`类型的使用例子。

```
CREATE OR REPLACE PROCEDURE PROC AS
DECLARE
V1 T % ROWTYPE;
C1 CURSOR;
BEGIN
OPEN C1 FOR SELECT * FROM T WHERE ID = 1;
FETCH C1 INTO V1;
PRINT V1.ID; PRINT V1.NAME;
CLOSE C1;
END;
```

### 12.3.3  记录类型

记录类型类似于C语句的结构。记录类型提供了处理分离，但又作为一个整体单元的相关变量的一种机制。例如： `DECLARE V_ID INT; V_NAME VARCHAR(30);`这两个变量在逻辑上是相互关联的，因为它们对应T表中的相同字段。如果为这些变量声明一个记录类型，那么它们之间的关系就十分明显了。定义记录类型的语法如下：

`TYPE`记录类型名`IS RECORD`(记录字段名1 数据类型`, [`记录字段名2 数据类型`, ……]);`

记录类型可以单独对记录中的字段赋值，也可以将一个记录直接赋值给另外一个记录。

可以使用点标记引用一个记录中的字段（记录名.字段名），如果要进行记录赋值，那么这两个记录必须是相同类型的，或者记录类型中字段的数据类型是相同的。

在下面的例子中，可以看到记录类型单独字段赋值和记录直接给另外一个记录赋值。

```
DECLARE TYPE T_REC IS RECORD( ID INT, NAME VARCHAR(30));
```

107

## 第12 章 PL/SQL

```
V_REC1 T_REC;
V_REC2 T_REC;
BEGIN
V_REC1.ID := 100;
V_REC1.NAME:= '雷锋';
V_REC2 := V_REC1;
PRINT V_REC1.ID;PRINT V_REC1.NAME;
PRINT V_REC2.ID;PRINT V_REC2.NAME;
END;
```

下面的例子则显示了记录类型不同，但记录类型中字段的数据类型相同时的赋值。

```
DECLARE
TYPE T_REC IS RECORD( ID INT, NAME VARCHAR(30));
TYPE T_REC_NEW IS RECORD( ID INT, NAME VARCHAR(30));
V_REC1 T_REC;
V_REC2 T_REC_NEW;
BEGIN
V_REC1.ID := 100; V_REC1.NAME:= '雷锋';
V_REC2 := V_REC1;
PRINT V_REC2.ID;
PRINT V_REC2.NAME;
END;
```

### 12.3.4  数组类型

数组数据类型包括静态数组类型和动态数组类型。静态数组的长度是预先定义好的，在整个程序中，一旦给定大小后就无法改变。而动态数组则不然，它可以随程序需要而重新指定大小。动态数组的内存空间是从堆（`HEAP`）上分配（即动态分配）的，通过执行代码为其分配存储空间。当程序执行到这些语句时，才为其分配，程序员自己负责释放内存。需要注意的是，`DM`中数组下标的起始值为1。静态数组的语法格式为：

`TYPE`数组名`IS ARRAY`数据类型 [常量表达式, 常量表达式`, …];`或`TYPE`数组名`IS ARRAY (`常量表达式`) OF`数据类型;

变量名数组名 [常量表达式, 常量表达式`, …];`

下面给出一个静态数组使用的例子。

```
DECLARE
TYPE ARR IS ARRAY INT[3];  --TYPE 定义数组类型
TYPE ARR2 IS ARRAY INT[2,3];    --TYPE 定义数组类型
```

`A ARR;` `--`用自己定义的数组类型申明数组`B ARR2;` `--`多维数组

```
BEGIN
FOR I IN 1..3 LOOP  --TYPE 定义的数组
A[I] := I * 10;
PRINT A[I];
END LOOP;
FOR I IN 1..2 LOOP
FOR J IN 1..3 LOOP
B[I][J] := I * 10 + J;
```

108

## 第12 章 PL/SQL

```
PRINT B[I][J];
END LOOP;
END LOOP;
END;
```

动态数组与静态数组的用法类似，区别只在于动态数组没有指定下标，需要动态分配空间。动态数组的语法格式为：

`TYPE`数组名`IS ARRAY`数据类型`[,…];`或`TYPE`数组名`IS TABLE OF`数据类型;

变量名数组名`[,…];`

多维动态数组分配空间的语法为：

数组名`:= NEW`数据类型[常量表达式`,…];`

或者可以使用如下语法对多维数组的某一维度进行空间分配：

数组名`:= NEW`数据类型[常量表达式`][];`

下面是一个动态数组使用的例子

```
DECLARE
TYPE ARR IS ARRAY INT[];
A ARR;
BEGIN
A := NEW INT[3];  --动态分配空间
FOR I IN 1..3 LOOP
A[I] := I * 10;
PRINT A[I];
END LOOP;
```

`PRINT ARRAYLEN(A); --`函数`ARRAYLEN`用于求取数组的长度

```
END;
```

### 12.3.5  操作符

`PL/SQL`支持的操作符包括：算术操作符、关系操作符、比较操作符、逻辑操作符，如表`12.2`所示。

表`12.2 PL/SQL`支持的操作符列表操作符类型操作符对应操作算术操作符 + 加

-  减

/ 除* 乘关系操作符 < 小于操作符<= 小于或等于操作符> 大于操作符>= 大于或等于操作符= 等于操作符!= 不等于操作符<> 不等于操作符:= 赋值操作符比较操作符 IS NULL 如果操作数为NULL 返回TRUE LIKE 比较字符串值BETWEEN 验证值是否在范围之内109

## 第12 章 PL/SQL

IN 验证操作数在设定的一系列值中逻辑操作符 AND 两个条件都必须满足OR 只要满足两个条件中的一个NOT 取反

## 12.4 PL/SQL 流控制

`PL/SQL`提供了丰富的流控制语句，用于对程序的执行流程进行控制。通过流控制语句，我们可以编写更复杂的`PL/SQL`块。流控制语句分为两类，即条件判断语句和循环语句。

### 12.4.1  IF 语句

`IF`语句是基于布尔条件的语句序列，以实现条件分支控制结构。最简单的`IF`语句格式为：

```
IF 条件 THEN
```

代码

```
END IF;
```

如果条件成立，则执行`THEN`后面的语句，否则跳过`THEN`到`END IF`之间的语句，执行`END IF`后面的语句。如果需要在条件不成立时执行另外的代码，格式如下：

```
IF 条件 THEN
```

代码1

```
ELSE
```

代码2

```
END IF
```

即当条件成立时执行代码1，条件不成立时执行代码2。

`IF`可以嵌套，可以在`IF`或`IF ..ELSE`语句中使用`IF`或`IF..ELSE`语句。条件表达式中的因子可以是布尔类型的参数、变量、也可以是条件谓词，控制语句中支持的条件谓词有：比较谓词、`BETWEEN`、`IN`、`LIKE`、和`IS NULL`。含`BETWEEN`谓词的条件表达式。

下面是一个`IF..THEN..ELSE`语句的例子

```
CREATE OR REPLACE PROCEDURE P_CONDITION(A INT) AS
BEGIN
IF A BETWEEN -5 AND 5 THEN
PRINT 'TRUE';
ELSE
PRINT 'FALSE';
END IF;
END;
```

更复杂的`IF`语句要先后判断多个条件，格式如下：

```
IF 条件1 THEN
```

代码1

```
ELSEIF 条件2 THEN
```

代码2

```
…
ELSE
```

代码N

```
END IF
```

110

## 第12 章 PL/SQL

在执行上面的`IF`语句时，首先判断条件1，当条件1 成立时执行代码1，否则继续判断条件2，条件成立则执行代码2，否则继续判断下面的条件。如果前面的条件都不成立，则执行`ELSE`后面的代码N。

### 12.4.2  LOOP 语句

循环控制的基本形式是`LOOP`语句，`LOOP`和`END LOOP`之间的语句将无限次的执行。

`LOOP`语句的基本格式如下：

```
LOOP
```

循环体

```
END LOOP
```

`LOOP`和`END LOOP`之间的语句无限次的执行显然是不行的，那么在使用`LOOP`语句时必须使用`EXIT`或`EXIT WHEN`语句结束`LOOP`循环。`EXIT`语句使循环结束，一般与`IF`语句相结合使用。`EXIT WHEN`指定一个条件，当条件满足时退出循环。

下面是一个`LOOP`循环语句的例子。

```
DECLARE X INT;
BEGIN
X:=100;
LOOP
X:=X+100;
IF X>1000 THEN
PRINT X;
EXIT;
END IF;
END LOOP;
END;
```

### 12.4.3  WHILE 语句

`WHILE..LOOP`循环语句在每次循环开始以前，先计算搜索条件，若该条件为`TRUE`，语句序列被执行一次，然后控制重新回到循环顶部。若搜索条件为`FALSE`，则结束循环。

`WHILE`语句的格式如下：

```
WHILE 条件 LOOP
```

循环体

```
END LOOP
```

在循环内部，也可以通过`EXIT WHEN`、`EXIT`、`CONTINUE WHEN`、`CONTINUE`来控制循环的执行流程，如下面的例子所示。

```
CREATE OR REPLACE PROCEDURE PROC(A INT) AS
DECLARE I INT:=0;
BEGIN
WHILE 1 LOOP
I = I + 1;
EXIT WHEN I > A;
END LOOP;
PRINT I;
END;
```

111

## 第12 章 PL/SQL

### 12.4.4  FOR 语句

`LOOP`和`WHILE`循环的循环次数都是不确定的，`FOR`循环的循环次数是固定的，循环变量是一个隐式声明的变量，循环变量从起始值开始，每执行一次循环，循环变量自动加1 或者减1，直到与终止值相等时，循环结束。如果使用`REVERSE`，则按照相反的顺序取集合中的元素，即先取最后一个元素，然后依次取前面的元素，直到第一个元素。`FOR`语句的格式如下：

`FOR`循环变量`IN[REVERSE]`起始值…终止值`LOOP`循环体

```
END LOOP
```

`FOR`语句中的循环变量不需要定义，也不需要显式地将集合中元素赋值给它，但只能在`FOR`循环内使用。循环变量可与当前语句块内的参数或变量同名，这时该同名的参数或变量在`FOR`语句的范围内将被屏蔽。`FOR`语句也可以通过`EXIT WHEN`、`EXIT`、`CONTINUE WHEN`、`CONTINUE`来控制循环的执行流程，如下面例子所示。

```
DECLARE I INT:=0;
BEGIN
FOR I IN 1..5 LOOP
```

`PRINT I;` `--`循环变量I，语句块定义的变量I被屏蔽了

```
EXIT WHEN I = 3;
END LOOP;
PRINT I;              --语句块定义的变量I
END;
```

运行结果：`1 2 3 0`

### 12.4.5  EXIT 语句

`EXIT`语句与循环语句一起使用，用于终止其所在循环语句的执行，将控制转移到该循环语句外的下一个语句继续执行。`EXIT`还可以和条件表达式结合起来使用，当条件满足时才会退出。`EXIT`格式如下：

```
EXIT [LABEL]
```

`[WHEN <`条件表达式`>]`

`EXIT`语句必须出现在一个循环语句中，否则编译器将报错。

### 12.4.6  GOTO 语句

`GOTO`语句无条件地跳转到一个标签`LABEL`所指的位置，`LABEL`在其作用域中必须是唯一的。`GOTO`语句将控制权交给带有标号的语句或语句块。格式如下:

```
GOTO <LABEL>
```

但是`GOTO`语句有一些缺点，因为在一个`PL/SQL`语句块中可能会定义很多变量，如果从某一个位置直接跳转到另一个地方，会引起不同部位的变量共享现象，导致程序不易读懂和维护，所以一般情况下不要使用`GOTO`语句来从嵌套很深的循环中直接跳到外面去。为了保证`GOTO`语句的使用不会引起程序的混乱，对`GOTO`语句的使用有下列限制:

1. `GOTO` 语句不能跳入一个`IF` 语句、循环语句或下层语句块中；
2. `GOTO` 语句不能从一个异常处理器跳回当前块，但可以跳转到包含当前块的上层语

句块。

112

## 第12 章 PL/SQL

### 12.4.7  NULL 语句

`NULL`语句的语法为:

```
NULL
```

该语句不做任何事情，只是用于保证语法的正确性，或增加程序的可读性。例如：

```
CREATE OR REPLACE PROCEDURE PROC(SCORE INT) AS
BEGIN
IF SCORE = 100 THEN
PRINT 'YOUR ARE WONDERFUL! ';
ELSE
NULL;
END IF;
END;
```

## 12.5 PL/SQL 访问数据库

编写`PL/SQL`块的目的主要是对数据进行访问，因此，在`PL/SQL`块中可以包含数据查询`SELECT`语句，也可以包含`INSERT`、`DELETE`、`UPDATE`等数据操纵语句。需要注意的是，在`PL/SQL`中不能直接包含`DDL`语句，如果要利用`PL/SQL`块完成诸如创建表、修改表结构等操作，需要通过`SQL`语句的动态执行。

通过`SQL`语句以及流控制语句，可以编写复杂的`PL/SQL`语句块，对数据库进行复杂的访问。由于`PL/SQL`块一般是在应用程序中调用执行，而不是以交互方式执行，所以在`PL/SQL`块中的`SQL`语句与一般的`SQL`语句有所不同。使用`PL/SQL`来控制对数据库的操作流程，功能更加丰富、灵活。

### 12.5.1  数据查询

在`PL/SQL`块中通过`SELECT`语句从数据库中检索数据。由于要对数据进行查询以及处理，而不仅仅是显示出来，所以`SELECT`语句需要采用下面的特殊格式先把数据放到一个临时空间中以便后面对它进行引用：

`SELECT`列1，列2，列`3… INTO`变量1，变量2，变量`3…`

```
FROM 表…
```

与一般的`SELECT`语句相比，`PL/SQL`块中的`SELECT`语句使用了`INTO`语句，利用`INTO`子句，把查询到的数据存放在变量中，以进行相应的处理。例如下面的例子首先从学生表中检索学生的姓名、年龄、学号信息，分别存放在`O_NAME`、`O_AGE`、`O_SNO`本地变量中，然后将这些信息合起来输出。

```
CREATE OR REPLACE PROCEDURE PROC AS
DECLARE
O_NAME VARCHAR;
O_AGE INT;
O_SNO INT;
BEGIN
SELECT NAME, AGE ,SNO INTO O_NAME, O_AGE ,O_SNO
FROM STUDENT WHERE SNO = 10010;
PRINT O_NAME || ' ' || O_AGE || ' ' || O_SNO;
```

113

## 第12 章 PL/SQL

```
END;
```

需要注意的是，在`SELECT`语句中，需要查询的列与`INTO`子句中的变量在数目、类型上要一致，否则会报错。

在执行`SELECT INTO`语句时，可能会发生两种例外情况，一是没有查询到满足条件的数据，二是存在多行满足条件的数据，这就是通常所说的异常。达梦预定义了一些异常，例如在第一种情况下发生的是异常`NO_DATA_FOUND`，在第二种情况下发生的异常是`TOO_MANY_ROWS`，对于这样的异常必须做出相应处理，否则会影响`PL/SQL`块的正确执行。

### 12.5.2  数据操纵

在`PL/SQL`块中也可以包含`INSERT`、`DELETE`、`UPDATE`语句，用于对数据库中的表进行增、删、改操作，在这些语句中，可以使用数字、字符串等形式的常量，也可以使用变量。

下面是一个对表进行`INSERT`操作的例子。

```
CREATE OR REPLACE PROCEDURE PROC AS
DECLARE
NAME1 VARCHAR;
AGE1 INT;
SNO1 INT;
BEGIN
INSERT INTO STUDENT VALUES(NAME1, AGE1, SNO1);
NAME1 = 'WANGWU';
AGE1 = 23;
SNO1 = 10013;
INSERT INTO STUDENT VALUES(NAME1, AGE1, SNO1);
END;
```

两条`INSERT`语句都是将三个常量作为三个列的值，第一条记录所用的变量还没有初始化，所以插入的记录的三个字段都是`NULL`。

在删除表中的数据时，在`DELETE`语句的`WHERE`子句中也可以使用变量，例如下面的例子从`STUDENT`表中删除上面插入的两条记录。

```
CREATE OR REPLACE PROCEDURE PROC AS
DECLARE
NAME1 VARCHAR;
BEGIN
DELETE FROM STUDENT WHERE NAME IS NULL;
NAME1 = 'WANGWU';
DELETE FROM STUDENT WHERE NAME = NAME1;
END;
```

在修改表中数据时，在`UPDATE`语句的`SET`子句和`WHERE`子句中可以使用变量，如下例所示。

```
CREATE OR REPLACE PROCEDURE PROC (NAME1 VARCHAR(30), AGE1 INT) AS
BEGIN
UPDATE STUDENT SET AGE = AGE1 WHERE NAME = NAME1;
END;
```

调用存储过程`CALL PROC('ZHANGSAN',24)`，即可将学生名字为`ZHANGSAN`的年龄改为24 岁。

114

## 第12 章 PL/SQL

### 12.5.3  数据定义

在`PL/SQL`中也可以动态执行`DDL`语句。

下面是一个在`PL/SQL`中执行`CREATE TABLE`语句的例子。

```
CREATE OR REPLACE PROCEDURE PROC AS
SQL_STMT VARCHAR(100);
BEGIN
SQL_STMT := 'CREATE TABLE TEST(I INT)';
EXECUTE IMMEDIATE SQL_STMT;
END;
```

调用存储过程`CALL PROC`，即可创建表`TEST`。

## 12.6 PL/SQL 与数据库交互

没有名字的`PL/SQL`程序块被称为匿名块，它仅存放在缓冲区中，只能在当前`DISQL`环境中执行。如果希望`PL/SQL`块能随时被调用执行，并且能被数据库用户共享，就需要创建存储程序。存储程序是有名字的`PL/SQL`块，它在创建时经过了编译与优化，被存放在数据库中，任何用户只要有适合的权限，就可以根据它的名字进行多次调用。存储程序在调用时无需要再进行编译，因此能以很快的速度执行，但如果需要对存储程序进行修改，不能直接修改它的源代码，只能执行`CREATE`命令重新创建。

存储程序可以在`SQL`语句、应用程序以及其它`PL/SQL`块中被调用，在第一次被调用时，存储程序的代码被装载到系统全局区的共享池中，再次调用时即可直接从共享池中取出代码执行。存储程序的形式包括：存储过程，存储函数、触发器、包等，它为用户提供了一种高效率的编程手段，成为现代数据库系统的重要特征。

### 12.6.1  存储过程

用户在自己的模式中创建存储过程，需要具有`CREATE PROCEDURE`数据库权限，如果要在其它用户的模式中创建存储过程，则需要具有`CREATE ANY PROCEDURE`数据库权限。

创建存储过程的语法为：

```
CREATE [OR REPLACE] PROCEDURE
```

过程名`[WITH ENCRYPTION] [(`参数1，参数2，`…)]`

```
AS
```

声明部分

```
BEGIN
```

可执行部分

```
EXCEPTION
```

异常处理部分

```
END;
```

其中`OR REPLACE`选项的作用是当同名的存储过程存在时，首先将其删除，再创建新的存储过程，前提条件是当前用户具有删除原存储过程的权限，如果没有删除权限，则创建失败。存储过程可以带有参数，这样在调用存储过程时就需指定相应的实际参数，如果没有参数，过程名后面的圆括号和参数列表就可以省略了。参数定义的格式如下：

参数名 [参数传递模式] 数据类型`[:=`默认值]参数名 [参数传递模式] 数据类型`[DEFAULT`默认值]115

## 第12 章 PL/SQL

参数传递模式包括：输入参数（`IN`）、输出参数（`OUT`）、输入输出参数（`IN OUT`）三种形式，其中`IN`是默认的参数传递模式。调用存储过程时，如果没有提供实际参数，则使用参数默认值。

`WITH ENCRYPTION`为可选项，如果指定`WITH ENCRYPTION`选项，则对`BEGIN`到`END`之间的语句块进行加密，防止非法用户查看其具体内容。可直接创建加密后的存储过程或函数，语法为：

```
CREATE [OR REPLACE] PROCEDURE|FUNCTION
```

过程名|函数名`WRAPPED`密文;

加密后的存储过程或函数的定义可在`SYS.SYSTEXTS`系统表中查询。

可执行部分是存储过程的核心部分，由`SQL`语句和流控制语句构成。异常处理部分用于处理存储过程在执行过程中可能出现的错误。

下面的例子创建了一个存储过程，功能是查看`STUDENT`表中学生总数。

```
CREATE OR REPLACE PROCEDURE STUDENT_COUNT AS
TOTAL_NUM INT;
BEGIN
SELECT COUNT(*) INTO TOTAL_NUM FROM STUDENT;
PRINT TOTAL_NUM;
END;
```

调用存储过程`CALL STUDENT_COUNT`，即可获取学生总数。

所有用户都可调用自己创建的存储过程，如果要调用其他用户的存储过程，则需要对该存储过程具有`EXECUTE`权限，即存储过程的所有者将`EXECUTE`权限授予该用户。授予`EXECUTE`权限的语法为：

```
GRANT EXECUTE ON 过程名 TO 用户;
```

删除存储过程的语法为：

```
DROP PROCEDURE 过程名;
```

### 12.6.2  存储函数

存储函数与存储过程在结构和功能上十分相似，但还是有所差异的。它们的区别在于：

1. 存储过程没有返回值，调用者只能通过访问`OUT` 或`IN OUT` 参数来获得执行结果，

而存储函数有返回值，它把执行结果直接返回给调用者；

2. 存储过程中可以没有返回语句，而存储函数必须通过返回语句结束；
3. 不能在存储过程的返回语句中带表达式，而存储函数必须带表达式；
4. 存储过程不能出现在一个表达式中，而存储函数只能出现在表达式中。

创建存储函数的语法格式为：

```
CREATE OR REPLACE FUNCTION
函数名 [WITH  ENCRYPTION] (参数1,参数2,…) RETURN 返回类型
AS
```

声明部分

```
BEGIN
```

可执行部分`RETURN`表达式;

```
EXCEPTION
```

异常处理部分

```
END;
```

如果用户要在自己的模式中创建存储函数，只需具有`CREATE FUNCTION`的数据库权限，如果要在其它用户的模式中创建存储函数，则需要具有`CREATE ANY FUNCTION`的数

116

## 第12 章 PL/SQL

据库权限。

下面的例子创建一个存储函数，实现斐波那契数列算法。

```
CREATE OR REPLACE FUNCTION FIBONACCI(A INT) RETURN INT AS
DECLARE S INT; LV INT; RV INT;
BEGIN
IF A <= 0 THEN
```

`PRINT '`请输入正数`';`

```
ELSIF A = 1 OR A = 2 THEN
S := 1;
ELSE
RV := FIBONACCI (A - 1);
LV := FIBONACCI (A - 2);
S := LV + RV;
PRINT LV || '+' || RV || '=' || S;
END IF;
RETURN S;
END;
```

调用函数`SELECT FIBONACCI(4)`，即可获取4 的斐波那契数列。

每个用户都可以直接调用自己创建的存储函数，如果要调用其它用户的存储函数，则需要具有对相应存储函数的`EXECUTE`权限。为此，存储函数的所有者要将`EXECUTE`权限授予适当的用户，授予`EXECUTE`权限的语句格式为：

```
GRANT EXECUTE ON 函数名 TO 用户
```

删除存储函数的语句格式为：

```
DROP FUNCTION 函数名;
```

存储过程和存储函数统称为存储模块，存储模块的调用命令有三种：

1. `SELECT` 语句调用；
2. `CALL` 语句调用；
3. 直接在`DISQL` 中输入存储过程或函数名即可调用。

上述三种调用方式的不同之处在于：

1. `SELECT` 调用存储模块必须是有返回值的，也就是说`SELECT` 命令只能调用存储函

数；

2. 如果通过`CALL` 来调用，它不要求调用的是存储过程还是存储函数，如果存储模块

有返回值，则`CALL`命令会忽略它的返回值，执行结果是成功或者失败；

3. 如果不通过任何语句直接调用存储模块，默认方式为`CALL`。

### 12.6.3  游标

由于`DM`支持的`SQL`语言是面向集合的语言，一条`SQL`语句可以产生或处理多条记录，而`PL/SQL`语言是面向记录的，一组主变量一次只能存放一条记录，所以仅使用主变量并不能满足`SQL`语句向应用程序输出数据的要求。为解决这一问题，`SQL`语言引用了游标来协调这两种不同的工作方式，从而为应用程序逐个处理查询结果提供了强有力的手段。

使用游标必须先定义，定义游标实际上是定义了一个游标工作区，并给该工作区分配了一个指定名字的指针（即游标）。游标工作区用以存放满足查询条件行的集合，因此它是一个说明性语句，是不可执行的。在打开游标时，就可从指定的基表中取出所有满足查询条件的行送入游标工作区并根据需要分组排序，同时将游标置于第一行的前面以备读出该工作区中的数据。当对行集合操作结束后，应关闭游标，释放与游标有关的资源。

`DM`支持的`SQL`语言提供了有关游标的语句：定义游标语句、打开游标语句、拨动游标

117

## 第12 章 PL/SQL

语句和关闭游标语句。

定义游标的语法格式为：

```
CURSOR <游标名> [FAST | NO FAST] [<cursor 选项>]
```

或者

```
<游标名> CURSOR [FAST | NO FAST] <cursor 选项>
<cursor 选项> := <cursor 选项1>|<cursor 选项2>|<cursor 选项3>|<cursor 选项4>
```

`<cursor`选项`1>:= <IS|FOR> {<`查询表达式`>|<`连接表`>}`

```
<cursor 选项2>:= <IS|FOR> TABLE <表名>
```

`<cursor`选项`3>:= (<`参数声明`> {,<`参数声明`>})IS <`查询表达式>`<cursor`选项`4>:= [(<`参数声明`> {,<`参数声明`>})] RETURN <plsql`数据类型`> IS <`查询表达式><参数声明`> ::= <`参数名`> [IN] <`参数类型`> [ DEFAULT|:= <`缺省值`> ]``<plsql`数据类型`> ::= <`普通数据类型>

```
| <变量名> %TYPE
| <表名> %ROWTYPE
| CURSOR
```

`| REF <`游标名><查询表达式`>::=`请参考《`DM7_SQL`语言使用手册》<连接表`>::=`请参考《`DM7_SQL`语言使用手册》

为了处理游标中的数据，首先要打开游标。打开游标的语法格式为：

`OPEN`游标名

```
OPEN 游标名 FOR SELECT 语句;
```

游标打开后，就可以取出游标中的数据，并对其进行处理。拨动游标的语法格式为：

```
FETCH [<fetch 选项> [FROM]] <游标名> [ [BULK COLLECT]  INTO <主变量名 >{,<主变
量名>} ] [LIMIT rows]
<fetch 选项>::= NEXT | PRIOR | FIRST | LAST | ABSOLUTE n | RELATIVE n
```

`FETCH`命令可以将一行数据中各列的值依次赋给指定的变量，需要注意的是，变量的类型、数目要与游标中的一行的各列相对应。游标在使用完后应及时关闭，以释放它所占用的内存空间，关闭游标的语法格式为：

`CLOSE`游标名当游标关闭后，不能再从游标中获取数据。如果需要，可以再次打开游标。

下面给出一个典型的使用游标的例子。

```
CREATE OR REPLACE PROCEDURE PROC AS
STR VARCHAR;
CURSOR CSR FOR SELECT NAME FROM STUDENT;  --声明游标并绑定SQL 语句
```

`CURSOR CSR1;` `--`先声明，打开游标的时候再绑定`SQL`语句

```
BEGIN
OPEN CSR;
OPEN CSR1 FOR SELECT NAME FROM SYSOBJECTS
WHERE NAME='STUDENT';
LOOP
```

`FETCH CSR INTO STR;` `--`从游标`CSR`中取数据；

```
EXIT WHEN CSR%NOTFOUND;
PRINT STR;
END LOOP;
FETCH CSR1 INTO STR;  --从游标CSR1 中取数据；
PRINT STR;
CLOSE CSR;
CLOSE CSR1;
END;
```

运行结果：

118

## 第12 章 PL/SQL

```
ZHANGSAN
LISI
STUDENT
```

在`DM`中，游标的属性主要包括以下四种，如表`12.3`所示。

表`12.3`游标的属性属性描述CURSOR%ISOPEN 判断当前游标是否已经打开，如果打开，该属性值为TRUE，否则为FALSE CURSOR%ROWCOUNT 表示到目前为止，用FETCH 语句已经取到的行数表示最后一次FETCH 操作是否从游标中取到一行数据，如果已经取到，其值为CURSOR%FOUND TRUE，如果没有取到，其值为FALSE CURSOR%NOTFOUND 和CURSOR%FOUND 正好相反

以上游标的属性被称为显式游标属性。在这四个游标属性中，`%ISOPEN`属性用于测试游标的状态。其它三个属性用来测试`FETCH`命令的执行结果，`%FOUND`和`%NOTFOUND`属性用来测试最近的一次`FETCH`是否取到数据，`%ROWCOUNT`属性表示自游标打开以来，到目前为止，用`FETCH`命令获取的行数。

在大多数情况下，游标的应用步骤是：打开游标；开始循环；从游标中取出一行数据并进行处理；关闭循环；关闭游标，这一类应用称为游标用于循环。但还有一种循环与这种类型不同，这就是游标`FOR`循环。用于`FOR`循环的游标与一般游标的区别在于不需要显式的打开、关闭、取数据，测试数据的存在、定义存放数据的变量等。

下面的例子进行游标`FOR`循环，将学生的年龄加1。

```
DECLARE
CURSOR STU_CURSOR IS
SELECT * FROM STUDENT FOR UPDATE;
BEGIN
FOR STU_ROW IN STU_CURSOR LOOP
UPDATE STUDENT SET AGE = AGE + 1 WHERE CURRENT OF STU_CURSOR;
END LOOP;
COMMIT;
END;
```

从上面的例子中我们可以看到游标`FOR`循环确实很好的简化了游标的开发，我们不再需要`OPEN`、`FETCH`和`CLOSE`语句，也不需要用`%FOUND`属性检测是否到最后一条记录，这一切`DM`服务器隐式的帮我们完成了。

### 12.6.4  引用游标

定义引用游标的语法格式：

<游标变量名`> CURSOR;`或者

```
<游标变量名> CURSOR := SOURCE_CURSOR;
```

引用游标有以下几个特点：

1. 不只局限于一个查询，可以为一个查询声明或者打开一个游标，然后对其结果集进

行处理，之后又可以将这个引用游标为其它的查询打开；

2. 可以对引用游标进行赋值；
3. 可以像用一个变量一样在一个表达式中用这个引用游标；
4. 可以作为一个子程序的参数，也就是它可以像C 语言中的变量一样充当参数；
5. 可以在`PL/SQL` 的不同子程序中传递结果集。

同一个游标变量再次打开游标的时候可以关联另一个查询语句，而原来的游标句柄会被

119

## 第12 章 PL/SQL

自动关闭。

如果定义引用游标的时候没有赋值。可以在后面需要的地方赋值。引用游标赋值操作，语法如下：

```
<游标变量名> := SOURCE_CURSOR;
```

给一个引用游标变量赋值时，可以继承所有`SOURCE_CURSOR`的属性。如果`SOURCE_CURSOR`已经打开，则`DEST_CURSOR`也已经打开，也就是说`DEST_CURSOR`只是个变量，它相当于一个指针，指向的位置和`SOURCE_CURSOR`是完全一样的。

下面是一个使用引用游标的例子。

```
CREATE OR REPLACE PROCEDURE PROC AS
STR VARCHAR;
CURSOR C1 IS SELECT NAME FROM STUDENT WHERE SNO = 10010;
CURSOR C2 IS SELECT NAME FROM STUDENT WHERE SNO = 10011;
CURSOR CSR;
BEGIN
CSR := C1;
```

`OPEN C1; --`赋值后再打开

```
IF CSR%ISOPEN THEN
PRINT 'CURSOR IS ALREADY OPENED';
FETCH CSR INTO STR;
PRINT STR;
ELSE
PRINT 'CURSOR IS NOT OPENED';
END IF;
```

`OPEN C2; --`打开后再赋值

```
CSR := C2;
IF CSR%ISOPEN THEN
PRINT 'CURSOR IS ALREADY OPENED';
FETCH CSR INTO STR;
PRINT STR;
ELSE
PRINT 'CURSOR IS NOT OPENED';
END IF;
CLOSE C1;
CLOSE C2;
END;
```

运行结果：

```
CURSOR IS ALREADY OPENED
ZHANGSAN
CURSOR IS ALREADY OPENED
LISI
```

### 12.6.5  动态SQL

`SQL`的动态执行是通过语句`EXECUTE IMMEDIATE`实现的，它的作用是执行一个指定的`SQL`语句，这个`SQL`语句可以带参数，也可以不带参数。如果带参数，则`EXECUTE``IMMEDIATE`后面需要加上`USING`来指定`SQL`语句中参数的值；如果不带参数，`EXECUTE``IMMEDIATE`后面直接跟上需要执行的`SQL`语句即可。动态`SQL`的语法格式如下：

120

## 第12 章 PL/SQL

```
EXECUTE IMMEDIATE <SQL 动态语句文本> [INTO VARIABLES]
[USING [参数1][参数2]…];
```

1. 该语句只能在嵌入式方式中使用；
2. 该语句首先分析动态语句文本，检查是否有错误，如果有错误则不执行它，并在

`SQLCODE`中返回错误码；如果没发现错误则执行它；

3. 一般来说，应该使用一个字符串变量来表示一个动态`SQL` 语句的文本，下列三个语

句不能作动态`SQL`语句：`CLOSE`、`FETCH`、`OPEN`。如下面几个例子所示：

例不支持`OPEN`。调用`PROC`过程时，报错：不支持的语句类型。

```
CREATE OR REPLACE PROCEDURE PROC AS
CURSOR C1;
SQL_STMT1 VARCHAR := 'OPEN C1 FOR SELECT NAME FROM STUDENT;';
BEGIN
EXECUTE IMMEDIATE SQL_STMT1;
END;
```

例不支持`CLOSE`。调用`PROC`过程时，报错：不支持的语句类型。

```
CREATE OR REPLACE PROCEDURE PROC AS
CURSOR C1;
SQL_STMT1 VARCHAR := 'CLOSE C1;';
BEGIN
OPEN C1 FOR SELECT NAME FROM STUDENT;
EXECUTE IMMEDIATE SQL_STMT1;
END;
```

例不支持`FETCH`。调用`PROC`过程时，报错：不支持的语句类型。

```
CREATE OR REPLACE PROCEDURE PROC AS
CURSOR C1;
STR VARCHAR;
SQL_STMT1 VARCHAR := 'FETCH ABSOLUTE 1 C1 INTO STR;';
BEGIN
OPEN C1 FOR SELECT NAME FROM STUDENT;
EXECUTE IMMEDIATE SQL_STMT1;
PRINT STR;
CLOSE C1;
END;
```

动态`SQL`语句不支持嵌入式异常处理`WHENEVER`，即不支持下列类似语句：

```
EXEC SQL WHENEVER SQLERROR GOTO sql_error; ……
sql_error:
EXEC SQL WHENEVER SQLERROR CONTINUE;
```

动态`SQL`语句的文本也可以是一个`PL/SQL`语句块，如下例所示：

```
CREATE OR REPLACE PROCEDURE PROC AS
CURSOR C1;
SQL_STMT1 VARCHAR := 'DECLARE STR VARCHAR; BEGIN SELECT NAME INTO STR FROM
STUDENT WHERE SNO=10010; PRINT STR;END;';
BEGIN
EXECUTE IMMEDIATE SQL_STMT1;
END;
```

如果动态`SQL`语句的文本中有多条`SQL`语句，那么只执行第一条语句，如下例所示：

```
CREATE OR REPLACE PROCEDURE PROC AS
SQL_STMT VARCHAR := 'SELECT NAME FROM STUDENT WHERE SNO=10010;
```

121

## 第12 章 PL/SQL

```
SELECT NAME FROM STUDENT WHERE SNO=10011;';
BEGIN
EXECUTE IMMEDIATE SQL_STMT;
END;
```

运行结果：`ZHANGSAN`对于仅执行一次的动态语句，用立即执行语句较合适。如果动态`SQL`语句是查询语句并且结果集只有一条记录，则可以通过`INTO`语句把结果存储赋值给变量，如下例所示：

```
CREATE OR REPLACE PROCEDURE PROC AS
NAME VARCHAR := 'STUDENT';
SQL_STMT VARCHAR := 'SELECT NAME FROM SYSOBJECTS WHERE NAME = ?';
STR VARCHAR;
BEGIN
EXECUTE IMMEDIATE SQL_STMT INTO STR USING NAME;
PRINT STR;
END;
```

在动态执行`SQL`语句的时候也可以对指定的`SQL`语句设置参数。指定参数有两种方式，如果某个值设置为参数，可以用“？”来表示，也可以用`“:VARIABLE”`来表示，如下例所示：

```
CREATE OR REPLACE PROCEDURE PROC AS
STR VARCHAR := 'HELLO';
START_POS INT:= 1;
END_POS INT := 3;
STR_SQL VARCHAR := 'SELECT SUBSTR(:X, :Y, :Z)';
BEGIN
EXECUTE IMMEDIATE STR_SQL USING STR, START_POS, END_POS;
END;
```

运行结果：`HEL`用“？”表示参数时，在传入时可以是任意的值，但参数个数一定要与“？”的个数相同，同时数据类型一定要匹配（可以互相转换也可以），不然会报数据类型不匹配的错误。

## 12.7 自治事务

`DM`支持通过将一个`PL/SQL`语句块定义成自治事务，将该块中的`DML`语句和调用程序的事务环境隔离开。如此一来，该语句块就成为一个由其他事务启动的独立的事务，前一个事务被称为主事务。

一个定义了自治事务的语句块称为自治例程。

在自治事务块中，主事务是挂起的；等待自治事务完成后，会话自动切换回主事务。

### 12.7.1  定义自治事务

自治事务仅能在`PL/SQL`块中定义。定义自治事务，需要在`PL/SQL`块的声明单元中添加如下的语句：

```
PRAGMA  AUTONOMOUS_TRANSACTION;
```

作为自治事务的`PL/SQL`块可以是下面中的一种：

1. 最顶层的（不是嵌套的）匿名`PL/SQL` 块
2. 函数和过程，或者在一个包里定义或者是一个独立的程序
3. 对象类型的方法

122

## 第12 章 PL/SQL

4. 数据库触发器
5. 嵌套子过程

自治事务的定义语句可以放在`PL/SQL`块声明单元的任何地方，但推荐放在数据结构声明之前。

### 12.7.2  自治事务完整性与死锁检测

自治事务的语句块执行完成时，如果事务仍处于活动状态，则系统需要报错：“检测到活动的自治事务处理”，并将未提交事务回滚。所以需要在语句块结束处显式添加`COMMIT`或`ROLLBACK`语句。

另一方面，`COMMIT`和`ROLLBACK`语句只是结束了活动的自治事务，但不会终止自治例程。实际上，可以在一个自治块中使用多个`COMMIT`、`ROLLBACK`语句。

自治事务相对主事务是完全独立的。如果自治事务需要的锁资源已经被主事务拥有，则进行死锁报错。

### 12.7.3  自治事务嵌套

自治块中可以调用其它被定义自治事务的过程，从而产生嵌套的自治事务。`INI`参数`TRANSACTIONS`指定一个会话中可以并发的自治事务数量，其默认值为75。如果实际生成自治事务数超出该参数限定值时，服务器将报错：“并发事务数超出上限”。该参数理论值上下限分别为1000 和1。

## 12.8 异常处理

用户编写的`PL/SQL`块在执行过程中不可避免地会发生一些错误。这里涉及的错误并不是由于程序的语法引起的，而是因为处理的数据超出了处理的范围而引发的错误。如果给这样的错误起一个名字，这就是异常。当`PL/SQL`块在执行过程中检测到一个错误时，就会抛出相应的异常。在块中应当处理这样的异常，否则会引起应用程序的运行停止。

### 12.8.1  异常处理程序

异常一般是在`PL/SQL`程序中执行错误时由服务器抛出，也可以在`PL/SQL`块中由程序员在一定的条件下显式抛出，无论是哪种形式的异常，都可以在`PL/SQL`块的异常处理部分编写一段程序进行处理，如果不做任何处理，异常将被传递到调用者，由调用者统一处理。

如果要在`PL/SQL`块中对异常进行处理，就需要在异常处理部分编写处理程序。异常处理程序的格式如下：

```
EXCEPTION
WHEN 异常1 [OR 异常2 … ] THEN
```

异常处理程序`1;`

```
WHEN OTHERS THEN
```

异常处理程序`2;`

```
END;
```

异常处理程序以关键字`EXCEPTION`开始，以关键字`END`结束。在这部分可以对多个异常分别进行不同的处理，也可以进行相同的处理。如果没有列出所有异常，可以用关键字

123

## 第12 章 PL/SQL

`OTHERS`代替其它的异常，在异常处理程序的最后加上一条`WHEN OTHERS`子句，用来处理前面没有列出的所有异常。

如果`PL/SQL`块执行出错，或者遇到显式抛出异常的语句，则程序立即停止执行，转去执行异常处理程序。异常被处理结束后，整个`PL/SQL`块的执行便告结束。所以一旦发生异常，则在`PL/SQL`块的可执行部分中，从发生异常的地方开始，以后的代码将不再执行。

在`PL/SQL`块中有三种类型的异常，即预定义的异常、非预定义的异常和用户自定义的异常。下面分别介绍这几种异常的使用方法。

### 12.8.2  预定义的异常

为方便用户编程，`DM`提供了一些预定义的异常，这些异常与最常见的`DM`错误相对应。

如表`12.4`所示：

表12.4 数据库预定义的异常异常名称 SQLCODE 说明TOO_MANY_ROWS -3034 SELECT INTO 中包含多行数据NO_DATA_FOUND -7065 数据未找到DUP_VAL_ON_INDEX -6602 违反唯一性约束INVALID_CURSOR -4535 无效的游标操作ZERO_DIVIDE -6103 除0 错误

此外，还有一个特殊的异常名`OTHERS`，它处理所有没有明确列出的异常。`OTHERS`对应的异常处理语句必须放在其他异常处理语句之后。

下面给出一个异常处理的例子。

```
DECLARE
OBJ_NAME VARCHAR(50);
BEGIN
SELECT NAME INTO OBJ_NAME FROM STUDENT WHERE SNO = 10010;
EXCEPTION
WHEN NO_DATA_FOUND THEN
```

`PRINT '`没有找到满足条件的数据`';`

```
WHEN TOO_MANY_ROWS THEN
```

`PRINT '`找到的记录数大于1 条，不满足`SELECT INTO`的条件`';`

```
WHEN OTHERS THEN
PRINT 'OTHERS EXCEPTION';
END;
```

`PL/SQL`的`WHEN`子句中也可以指定多个异常的名字，用`OR`分隔，例如：

```
WHEN NO_DATA_FOUND OR TOO_MANY_ROWS THEN
```

`PRINT 'SELECT`结果集不符合要求`';`

在向表的主键列上写入一个重复的值时将引发异常`DUP_VAL_ON_INDEX`，如下例所示：

```
CREATE OR REPLACE PROCEDURE ADD_STUDENT
(NAME VARCHAR, AGE INT, SNO INT)  AS
BEGIN
INSERT INTO STUDENT VALUES(NAME, AGE, SNO);
EXCEPTION
WHEN DUP_VAL_ON_INDEX THEN
```

`PRINT '`违反主键的唯一性约束`';`

```
PRINT 'ERROR CODE: ' || "%DM_EXCEPTION_OBJ"."CODE";
PRINT 'DESCRIBE: ' ||  "%DM_EXCEPTION_OBJ"."DESCR";
```

124

## 第12 章 PL/SQL

```
WHEN OTHERS THEN
PRINT 'OTHERS EXCEPTION';
END;
```

从这个例子可以看出，`PL/SQL`在异常处理的异常类型中提供了两个成员，`“CODE”`和`“DESCRIBE”`，分别表示引起异常时发生错误的错误码及错误码的描述信息。在日常处理中，我们可以创建一个表用来存储在`PL/SQL`的异常处理部分出现的错误情况，或者生成日志信息，以备后续对错误的统计、分析以及处理。

引发异常的一个重要原因是处理数据时发生错误。编写`PL/SQL`的主要目的是处理数据，而`PL/SQL`块在逻辑与数据是分开的，程序员根本无法预料数据的变化，所以在编写程序时需要考虑各种可能出现异常的情况，并对这些异常进行相应的处理。

### 12.8.3  用户自定义的异常

除了`DM`定义的两种异常外，在`PL/SQL`中还可以用户自定义异常。程序员可以把一些特定的状态定义为异常，在一定的条件下抛出，然后利用`PL/SQL`的异常机制进行处理。用户自定义异常的语法格式为：

异常名称`EXCEPTION [FOR`自定义的错误码]

或

<异常变量名`> EXCEPTION;`

```
PRAGMA EXCEPTION_INIT(<异常变量名>, <错误号>);
```

抛出异常的语法格式为：

`RAISE`异常名异常一般在一定的条件下抛出，因此`RAISE`语句通常跟在某个条件判断的后面，这样就把这个异常与这个条件关联起来了，抛出异常的原因可能是数据出错，也可能是满足了某个自定义的条件，处理自定义异常的方法与处理前两种异常的方法相同。

下面是一个用户自定义异常的例子。

```
CREATE OR REPLACE PROCEDURE PROC AS
DECLARE
E1 EXCEPTION FOR -20001;
BEGIN
RAISE E1;
EXCEPTION
WHEN E1 THEN
PRINT 'NORMAL EXCEPTION' || ' ' || "%DM_EXCEPTION_OBJ"."CODE";
WHEN OTHERS THEN
PRINT 'OTHER EXCEPTION' || ' ' || "%DM_EXCEPTION_OBJ"."CODE";
END;
```

## 12.9 PL/SQL 调试工具

`DM`为用户提供了`PL/SQL`调试工具`DMDBG`。`DMDBG`可调试在`DISQL`中直接执行的非`DDL`语句或语句块，以便程序开发人员定位`PL/SQL`中存在的错误。用户要使用`DMDBG`调试工具，首先要调用系统过程`SP_INIT_DBG_SYS(1)`创建调试所需要的包。

125

## 第12 章 PL/SQL

### 12.9.1  命令行参数

`DMDBG`的整个运行过程中可以处于初始状态`(S)`、待执行`(W)`、执行`(R)`、调试`(D)`、执行结束`(O)`等不同的状态。

初始状态`(S)`：工具启动完成后，尚未设置调试语句；

待执行状态`(W)`：设置调试语句后，等待用户执行；

执行状态`(R)`：开始执行后，未中断而运行的过程；

调试状态`(D)`：执行到断点或强制中断后进入交互模式；

执行结束`(O)`：执行完当前设置的调试语句，并返回结果。

`DMDBG`在不同的状态下可以执行不同的操作，具体如表`12.5`所示。备注表示不同的命令分别在哪几种状态下可以使用。

表`12.5 DMDBG`调试命令命令行参数含义备注

```
LOGIN  登录  S/W/D/O
```

`SQL`设置调试语句`S/W/O`B 设置断点`W/D/O``INFO B`显示断点信息`W/D/O`D 取消断点`W/D/O`R 执行语句`W/O``CTRL+C`中断执行 R L显示调试脚本 D C继续执行 D N单步执行 D S执行进入 D F或`FINISH`执行跳出 D P打印变量 D`BT`显示堆栈 D`UP`上移栈帧 D`DOWN`下移栈帧 D`KILL`结束当前执行`W/D/O``QUIT`退出调试工具`S/W/D/O`

### 12.9.2  功能描述

1. 登录

提供交互与命令行2 种登录方式。交互方式与`DISQL`相同，使用者根据提示依次输入服务器、用户名、口令及端口号等登录信息。

命令行登录参数格式如下：

`DMDBG <`用户名`>/<`口令`>[@<`服务器名`|IP>[:<`端口号`>]]`

默认用户名和口令为`SYSDBA/SYSDBA`，服务器`LOCALHOST`，端口号为5236，则登录

126

## 第12 章 PL/SQL

命令为：

```
DMDBG SYSDBA/SYSDBA@LOCALHOST:5236
```

2. 设置语句

命令`SQL`供用户设置需要执行的`SQL`语句，其命令格式如下：

```
<SQL> [‘/’]
```

`SQL`语句是非`DDL`语句或语句块。如果`SQL`是单条语句，则以分号`“;”`结尾；如果是语句块，则语句块后必须以单独一行的斜杠符`“/”`结束。在调试中行数从`SQL`语句实际起始行开始计数。

在实际执行前，用户可以多次调用`SQL`命令设置待调试的语句，而`DMDBG`只是记录最后一次的设置语句。

如果需要调试自定义函数，需要和过程调用方式一样，使用`call`调用。

具体实例如下：

第一步，在`DISQL`中创建表和存储过程。

```
CREATE TABLE STUDENT (ID INT, NAME VARCHAR(20));  --创建游标类型对应的表
INSERT INTO STUDENT VALUES(10010,'ZHANGSAN');
INSERT INTO STUDENT VALUES(10011,'LISI');
CREATE OR REPLACE PROCEDURE P0 AS  --创建需要调试的存储过程
BEGIN
PRINT 'HELLO';
END;
/
CREATE CLASS MYCYCLE                                     --定义类对象
AS
ID INT;
C1 INT;
FUNCTION MYCYCLE(ID INT , C1 INT) RETURN MYCYCLE;
END;
/
CREATE OR REPLACE CLASS BODY MYCYCLE                 --定义类体
AS
FUNCTION MYCYCLE(ID INT, C1 INT) RETURN MYCYCLE
AS
BEGIN
THIS.ID = ID;
THIS.C1 = C1;
RETURN THIS;
END;
END;
/
CREATE OR REPLACE PROCEDURE P AS  --创建需要调试的存储过程
TYPE T_REC IS RECORD(ID INT, NAME VARCHAR(20));  --定义记录类型
TYPE ARR is ARRAY INT[4];  --定义数组类型
```

`R1 T_REC;` `--`声明记录类型`C1 CURSOR;` `--`声明游标类型127

## 第12 章 PL/SQL

`B ARR;` `--`声明数组类型`O MYCYCLE;` `--`声明对象类型`I1 INT;` `--`声明整型`V1 VARCHAR(20);` `--`声明字符串类型

```
BEGIN
R1.ID = 10012;
R1.NAME = 'WANGWU';
OPEN C1 FOR SELECT * FROM STUDENT;
LOOP
FETCH C1 INTO I1,V1;
EXIT WHEN C1%NOTFOUND;
END LOOP;
FOR I IN 1..4 LOOP
B[I] := I * 10;
PRINT B[I];
END LOOP;
O = NEW MYCYCLE(1, 2);
CALL P0;
END;
/
```

第二步，在`DMDBG`中调试存储过程P，设置调试语句如下：

```
DBG>SQL CALL P;
```

3. 设置断点

设置断点命令为B，可以为指定的脚本设置执行中断位置。调试执行到断点设置位置后，将自动中断当前执行。设置断点命令有2 种不同格式。

`B <`方法名>`B [<`方法名`>:]<`行号>

如果省略方法名，则为当前方法或语句块设置行号断点。包中的方法可以设置断点，但不能指定行号；如果断点设置在包上，则可以指定行号，但可以设置断点部分只能是该包体的初始化代码。

行号从1 开始计数。对于方法来说，其开始的定义声明部分语句也包含在行号计数中。

对于断点的行号设置必须遵守以下原则：

定义声明部分不能设置断点；

如果一条语句跨多行，则断点应设置在语句最后一行；

如果多条语句在同一行，则执行中断在其中第一条语句执行前；

如果设置断点行号不能中断，则自动将其下移到第一个可以中断的行；

可以在调试过程中动态添加断点。如果在同一位置重复设置断点，则重复断点被忽略。

例如：

`DBG>B 3` `--`没有方法名，则在最顶层设置断点`No line 3 in method "@dbg_main". --`由于顶层只有一行，无法设置断点，报错返回`DBG>B P:3` `--`不能设置断点，则下移到第一条可以中断的行

```
Breakpoint 1 at SYSDBA.P, line 11@{R1.ID = 10012;}
```

`DBG>B P:12` `--`直接在指定行设置断点

```
Breakpoint 2 at SYSDBA.P, line 12@{R1.NAME = 'WANGWU';}
```

4. 显示断点

显示断点命令为：

```
INFO B
```

该命令显示所有已设置的断点。显示的每个断点包含以下信息：

128

## 第12 章 PL/SQL

`1)`序号。这是一个自增值，从1 开始。设置断点时自动为其分配。

`2)`方法名。如果为语句块，则方法名为空。

`3)`行号。

例如：

```
DBG> INFO B
Num     Schema  Package  Method          What
1       SYSDBA  NULL    P       line 11@{R1.ID = 10012;}
2       SYSDBA  NULL    P       line 12@{R1.NAME = 'WANGWU';}
```

5. 取消断点

取消断点的命令格式为：

`D <`断点序号>

断点序号可以通过`INFO B`命令获取，删除后断点的编号不能重用。取消断点命令可以在工具运行的任何时间调用。

例如：

`DBG>D 1` `--`删除断点，成功则等待再次输入`DBG>D 3` `--`删除不存在的断点，则报错

```
No breakpoint number 3.
```

`DBG>INFO B` `--`显示删除后的断点信息

```
DBG> INFO B
Num     Schema  Package Method  What
2       SYSDBA  NULL    P       line 12@{R1.NAME = 'WANGWU';}
```

6. 执行语句

执行语句命令为：

```
R
```

命令R执行设置的`SQL`语句。此命令无参数，执行R命令前必须已经设置过调试语句，且调试过程中命令R不允许重复使用。

如果设置了断点，则执行到断点指定的位置时中断，中断将转入调试状态，并显示当前执行所在行的语句；否则，执行完成并显示结果。

例如：

```
DBG>R
Breakpoint 2, SYSDBA.P line: 12@{R1.NAME = 'WANGWU';}
```

`DBG>R` `--`调试过程中不可以再次运行

```
The program is already running.
```

`DBG>B P:23` `--`调试过程中可以设置断点

```
Breakpoint 3 at SYSDBA.P, line 23@{CALL P0;}
```

7. 显示脚本

可以使用命令L，在工具中显示指定的方法脚本，但不能显示包的单个方法脚本。此命令可以帮助用户准确设置断点位置。L命令每次显示5 行代码，多次执行L命令时，从以显示的下一行开始显示。L命令格式如下：

`L <`方法名>

方法名可以包含模式、包等前缀。在调试状态下，可以省略方法名，则显示当前正在运行的方法。例如：

```
DBG>L SYSDBA.P
1       CREATE OR REPLACE PROCEDURE P AS
2       TYPE T_REC IS RECORD(ID INT, NAME VARCHAR(20));
3       TYPE ARR is ARRAY INT[4];
4       R1 T_REC;
5       C1 CURSOR;
```

129

## 第12 章 PL/SQL

`DBG>L` `--`注意，第二次以后显示脚本不要带方法名，否则从第一行显示

```
6       B ARR;
7       O MYCYCLE;
8       I1 INT;
9       V1 VARCHAR(20);
10      BEGIN
```

8. 中断执行

中断执行命令为：

```
CTRL+C
```

在正常执行过程中，当监听到用户输入`CTRL+C`，则`DMDBG`强制中断当前执行，转入调试状态。该命令对于调试死循环错误非常有效。

9. 继续执行

继续执行命令为：

```
C
```

在调试状态下，可以使用命令C继续`SQL`语句的执行，直到运行到断点或执行完成。

例如：

```
DBG>C
Breakpoint 3, SYSDBA.P line: 23@{CALL P0;}
```

10. 执行进入

执行进入命令为：

```
S
```

如果当前中断语句包含方法调用，则执行进入命令S可以将方法调用展开，执行到其语句块的第一条语句中断。如果当前行没有方法调用，则命令S与单步执行命令N等效。

例如：

`DBG>S` `--`调入存储过程`P0`

```
SYSDBA.P0 line: 1       @{CREATE OR REPLACE PROCEDURE P0 AS}
```

需要说明的是，对于确定性函数，会直接进行结果重用，在重复调用时将不能执行进入调试。

11. 单步执行

单步执行命令为：

```
N
```

在调试状态下，单步执行命令N可以执行到当前层次下一个可中断的行。如果当前行包含多条语句，则所有该行语句都被执行。

例如：

`DBG>N` `--`单步执行存储过程`P0`

```
SYSDBA.P0 line: 3       @{PRINT 'HELLO';}
```

12. 执行跳出

执行进入命令为：

```
F 或FINISH
```

命令F可以执行当前函数的余下操作，如果剩余行有断点则执行到断点中断，否则返回到上层调用后中断。如果当前已经是最上层，则与单步执行命令N等效。

例如：

`DBG>F` `--`跳出存储过程`P0`

```
SYSDBA.P line: 32       @{CALL P0;}
```

13. 打印变量

打印变量命令为：

`P <`变量名>

命令P可以打印指定的变量值。`SQL`类型中，除了大字段数据，其它类型都可以打印。

130

## 第12 章 PL/SQL

`PLSQL`数据类型往往为复杂数据类型，其显示格式如下：

`1)`结构类型在大括号内显示结构所有成员的值，各成员值用`“,”`分隔。

`2)`数组类型如果是数组，则可以与结构类型一样，依次显示数组所有成员的值，也可以只显示其中某一下标的值。

`3)`对象类型可以打印对象中所有的静态成员，或者打印某一个静态成员，函数可以不打印。

`4)`游标类型游标也是对象类型，其成员如表`12.6`所示。

表`12.6`游标对象成员名称数据类型说明

```
ROWCOUNT  BIGINT
```

查询结果集总行数。如果游标未打开或查询失败时该值无效`FOUND` `INT`最近一次`FETCH`操作是否取得数据。如果取得为1，否则为0。如果游标未打开或查询失败时该值无效`ISOPEN` `INT`游标是否打开。打开为1，否则为0

P命令只能打印当前方法所在栈帧中的变量，如果要打印其它层次方法栈帧的变量，首先需要移动到对应栈帧。打印变量的信息以$开始，从1 开始计数，每打印一个变量，自动增加1。

例如：

`DBG>R` `--`开始执行

```
Breakpoint 2, SYSDBA.P line: 12@{R1.NAME = 'WANGWU';}
```

`DBG> P R1.ID` `--`打印记录类型中单个字段

```
$1 = 10012
```

`DBG> N` `----`单步执行后，`R1`所有字段都被赋值

```
SYSDBA.P line: 13       @{OPEN C1 FOR SELECT * FROM STUDENT;}
```

`DBG>P R1` `--`打印记录类型`R1`

```
$2 = {ID=10012, NAME=WANGWU}
```

`DBG>C` `--`继续运行，遇断点则中断

```
Breakpoint 2, SYSDBA.P line: 32@{CALL P0;}
```

`DBG>P C1` `--`打印游标的所有成员值

```
$3 = {ISOPEN=1,FOUND=0,ROWCOUNT=2}
```

`DBG>P B` `--`打印数组

```
$4 = {10, 20, 30, 40}
```

`DBG>P B[3]` `--`数组下标以1 开始

```
$5 = 30
```

`DBG> P O.C1` `--`打印对象类型中的成员

```
$6 = 2
```

`DBG> P O` `--`打印对象类型

```
$7 = MYCYCLE<0>{ID=1, C1=2}
```

14. 显示堆栈

显示堆栈命令为：

```
BT
```

命令`BT`可以显示当前执行的堆栈状态。首先显示当前方法执行到的行数，然后从下至上显示各层方法名称及调用参数值，输出参数不打印。

131

## 第12 章 PL/SQL

例如：

```
DBG>BT
#0      SYSDBA.P()      CALL P0;  --#0 表示最下层
#1      @dbg_main       CALL P  --表示栈帧只有两层
```

15. 下移栈帧

下移栈帧命令为：

```
DOWN
```

命令`DOWN`可以将当前调试栈帧下移一层。下移后，显示当前层执行到的语句行数。如果当前已经是堆栈最下层，则此命令无效。

例如：

`DBG>DOWN` `--`存储过程已到最下层，无法下移

```
Bottom (innermost) frame selected; you cannot go down.
```

16. 上移栈帧

上移栈帧命令为：

```
UP
```

命令`UP`可以将当前调试栈帧上移一层。上移后，显示当前层执行到的语句行数。如果当前已经是堆栈最上层，则此命令无效。

例如：

```
DBG>UP
#1      @dbg_main       CALL P
```

`DBG>UP` `--`已经到最上层，无法上移

```
Initial frame selected; you cannot go up.
```

`DBG> C` `--`执行结束，并显示结果

```
10
20
30
40
HELLO
```

17. 结束执行

结束执行命令为：

```
KILL
```

在调试过程中，用户可以使用命令`KILL`结束当前正在调试的`SQL`语句，并重新设置预调试的`SQL`语句。

`KILL`之后，必须重新设置`SQL`语句，断点信息被清空。R执行结束返回结果之后：如果没有重新设置`SQL`语句，则再次运行的仍是之前设置的`SQL`语句，断点信息可以重用；

如果重新设置了`SQL`语句，则断点信息亦被清空。

18. 退出工具

退出`DMDBG`工具的命令为：

```
QUIT
```

如果不希望继续调试，可以输入命令`QUIT`。`DMDBG`工具将中断连接，退出执行。

## 12.10  小结

`DM`的存储模块机制是一种技术，而不是一种独立的工具，它是和服务器紧密结合在一起的。可以认为这种技术是执行`DM PL/SQL`语言的一种虚拟机，它可以接受任何有效的存储模块，按照语言本身所规定的语义执行，并将结果返回给客户。

存储模块机制具有如下优点：

132

## 第12 章 PL/SQL

1. 提供更高的生产率：在设计应用时，围绕存储过程/函数设计应用，可以避免重复

编码，提高生产率；在自顶向下设计应用时，不必关心实现的细节，编程方便;

2. 便于维护：用户的存储模块在数据库集中存放，用户可以随时查询、删除、修改它

们，而应用程序可以不作任何修改，或只做少量调整；

3. 提供更好的性能：存储模块在创建时被编译成伪码序列，在运行时不需要重新进行

编译和优化处理，具有更快的执行速度，可以同时被多个用户调用，并能够减少操作错误；

4. 可以使用存储过程来帮助实施数据的安全性。可以不授权用户直接访问应用程序中

的一些表，而是授权用户执行访问这些表的一个过程。当过程被执行时，它将以过程拥有者的权限来执行。除非通过过程，否则用户就不能访问这些表；

5. 存储模块是一种高效访问数据库的机制，使用存储模块可显著减少应用对`DM` 的访

问次数，提高系统性能；

6. `DM` 存储模块的编写主要是采用`PL/SQL` 语言，`DM PL/SQL` 语言对三种控制结构（分

支结构、迭代结构和顺序结构）都提供了相应的语句支持。`DM PL/SQL`还支持异常处理、动态`SQL`、游标变量以及返回结果集等功能。同时，`DM`也预先定义了一些常用的存储过程和函数供用户使用。

133

0 表级触发器的触发事件包括某个基表上的`INSERT`、`DELETE`和`UPDATE`操作，无论对于哪种操作，都能够为其创建`BEFORE`触发器和`AFTER`触发器。如果触发器的动作代码不取决于受影响的数据，语句级触发器就非常有用。例如，可以在表上创建一个`BEFORE``INSERT`语句触发器，以防止在某些特定期限以外的时间对一个表进行插入。

每张基表上可创建的触发器的个数没有限制，但是触发器的个数越多，处理`DML`语句所需的时间就越长，这是显而易见的。创建触发器的用户必须是基表的创建者，或者拥有`DBA`权限。注意，不存在触发器的执行权限，因为用户不能主动“调用”某个触发器，是否激发一个触发器是由系统来决定的。

对于语句级和元组级的触发器来说，都是在`DML`语句运行时激发的。在执行`DML`语句的过程中，基表上所创建的触发器按照下面的次序依次执行：

1. 如果有语句级前触发器的话，先运行该触发器；
2. 对于受语句影响每一行：

1） 如果有行级前触发器的话，运行该触发器；

2） 执行该语句本身；

3） 如果有行级后触发器的话，运行该触发器；

3. 如果有语句级后触发器的话，运行该触发器。

需要注意的是，同类触发器的激发顺序没有明确的定义。如果顺序非常重要的话，应该把所有的操作组合在一个触发器中。触发器功能强大，但需要谨慎使用，过多的触发器或复杂触发器过程脚本会降低数据库的运行效率。

还需要注意的是，在`DM7`的数据守护环境下，备库上定义的触发器是不会被触发的。

管理视图、序列和同义词
