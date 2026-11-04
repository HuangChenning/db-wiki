---
title: "4 DIsql常用命令"
book: "DM7 DIsql使用手册"
version: "DM7"
source: "temp/doc/special/DM7°ïÖúÎÄµµ.chm#~htm/DIsql使用手册.htm"
tags:
  - dameng
  - dm7
  - disql
---

## 4.1 帮助HELP

`DIsql`帮助命令，可以帮助用户查看其他命令的具体用法。用户可以看到其他命令系统显示的内容，概括为：

- 命令的标题
- 命令的文本描述
- 命令的简写（例如，`AUTO`可以代替`AUTOCOMMIT`）
- 可以向命令传递的强制参数和可选参数

`help`显示相关命令的帮助信息。

语法如下：

```
HELP
```

``：命令名称或者命令名称的首字母，查询某一命令用法或者某一字母开头的所有命令用法。

示例如下：

```
SQL> HELP DEFINE
DEFINE
------
```

设置变量值，或者显示已定义的变量信息。

```
DEF[INE] [variable] | [variable = text]
```

## 4.2 输出文件SPOOL

将屏幕显示的内容输出到指定文件。

语法如下：

```
SPOOL { | OFF }
：：= [CRE[ATE]|REP[LACE]|APP[END]]
```

``：指定文件的绝对路径

`CRE[ATE]`：创建指定的文件，若指定的文件已存在，则报错，默认方式

`REP[LACE]`：创建指定的文件，若指定的文件已存在，则替换它

`APP[END]]`：将输出内容追加到指定文件的末尾

`OFF`：关闭`SPOOL`输出

> 只有SPOOL OFF之后，才能在输出文件中看到输出的内容。

示例如下：

```
SQL>spool d:\b.sql CREATE
SQL>select top 5* from sysobjects;
SQL>spool off
```

先执行上述语句，然后，查看`d:\b.sql`文件。

## 4.3 切换到操作系统命令HOST

使用`HOST`命令可以不用退出`DIsql`就能执行操作系统命令。如果单独执行`host`，则能够直接从`DIsql`界面切换到操作系统，之后可使用`EXIT`回到`DIsql`界面。

语法如下：

```
HOST[]
```

``：操作系统命令。

示例如下：

```
SQL>HOST DIR
```

## 4.4 获取对象结构信息DESCRIBE

获取表或视图、存储过程、函数、包、记录、类的结构描述。

语法如下：

```
DESC[RIBE] |||||| ;
```

各对象获取的内容略有不同：

- 表或视图获取的内容包括列名，列数据类型，列是否可以取空值。
- 函数、过程、类获取的内容包括两类：1）存储函数/过程名，类型（函数或过程），函数返回值类型；2）参数名，参数数据类型、参数输入输出属性、参数缺省值。
- 包获取的内容分为两类：1）包内存储函数/过程名，类型（函数或过程），函数返回值类型；2）包内参数名，参数数据类型、参数输入输出属性、参数缺省值。
- 记录获取的内容为：参数名，参数数据类型，参数是否可以取空值。

举例说明：

例1 获取表`sysgrants`的结构描述。

```
SQL> desc sysgrants;
行号 NAME TYPEV NULLABLE
---------- --------- ------- --------
1 URID INTEGER N
2 OBJID INTEGER N
3 COLID INTEGER N
4 PRIVID INTEGER N
5 GRANTOR INTEGER N
6 GRANTABLE CHAR(1) N
6 rows got
```

已用时间`: 2.408(`毫秒`).` 执行号`:753.`

例2 获取存储过程的结构描述。

创建一个存储过程：

```
CREATE OR REPLACE PROCEDURE PROC_1(A IN OUT INT) AS
B INT;
BEGIN
A:=A+B;
EXCEPTION
WHEN OTHERS THEN NULL;
END;
/
```

获取存储过程`PROC_1`的结构描述：

```
SQL>describe PROC_1;
行号 NAME TYPEV IO DEF RT_TYPE
---------- ------ ------- ----- --- -------
1 PROC_1 PROC
2 A INTEGER INOUT
```

已用时间`: 22.679(`毫秒`).` 执行号`:757.`

例3 获取包的结构描述

创建实例数据库：

```
CREATE TABLE Person(Id INT IDENTITY, Name VARCHAR(100), City VARCHAR(100));
INSERT INTO Person(Name, City) VALUES('Tom','武汉');
INSERT INTO Person(Name, City) VALUES('Jack','北京');
INSERT INTO Person(Name, City) VALUES('Mary','上海');
```

创建包：

```
CREATE OR REPLACE PACKAGE PersonPackage AS
E_NoPerson EXCEPTION;
PersonCount INT;
Pcur CURSOR;
PROCEDURE AddPerson(Pname VARCHAR(100), Pcity varchar(100));
PROCEDURE RemovePerson(Pname VARCHAR(100), Pcity varchar(100));
PROCEDURE RemovePerson(Pid INT);
FUNCTION GetPersonCount RETURN INT;
PROCEDURE PersonList;
END PersonPackage;
/
```

创建包主体：

```
CREATE OR REPLACE PACKAGE BODY PersonPackage AS
PROCEDURE AddPerson(Pname VARCHAR(100), Pcity varchar(100) )AS
BEGIN
INSERT INTO Person(Name, City) VALUES(Pname, Pcity);
PersonCount = PersonCount + SQL%ROWCOUNT;
END AddPerson;
PROCEDURE RemovePerson(Pname VARCHAR(100), Pcity varchar(100)) AS
BEGIN
DELETE FROM Person WHERE NAME LIKE Pname AND City like Pcity;
PersonCount = PersonCount - SQL%ROWCOUNT;
END RemovePerson;
PROCEDURE RemovePerson(Pid INT) AS
BEGIN
DELETE FROM Person WHERE Id = Pid;
PersonCount = PersonCount - SQL%ROWCOUNT;
END RemovePerson;
FUNCTION GetPersonCount RETURN INT AS
BEGIN
RETURN PersonCount;
END GetPersonCount;
PROCEDURE PersonList AS
DECLARE
V_id INT;
V_name VARCHAR(100);
V_city VARCHAR(100);
BEGIN
IF PersonCount = 0 THEN
RAISE E_NoPerson;
END IF;
OPEN Pcur FOR SELECT Id, Name, City FROM Person;
LOOP
FETCH Pcur INTO V_id,V_name,V_city;
EXIT WHEN Pcur%NOTFOUND;
PRINT ('No.' + (cast (V_id as varchar(100))) + ' ' + V_name + '来自' + V_city );
END LOOP;
CLOSE Pcur;
END PersonList;
BEGIN
SELECT COUNT(*) INTO PersonCount FROM Person;
END PersonPackage;
/
```

获取包`PersonPackage`的结构描述：

```
SQL>describe PersonPackage;
行号 NAME TYPEV IO DEF RT_TYPE
---------- -------------- ------------ -- --- -------
1 ADDPERSON PROC
2 PNAME VARCHAR(100) IN
3 PCITY VARCHAR(100) IN
4 REMOVEPERSON PROC
5 PNAME VARCHAR(100) IN
6 PCITY VARCHAR(100) IN
7 REMOVEPERSON PROC
8 PID INTEGER IN
9 GETPERSONCOUNT FUNC INTEGER
10 PERSONLIST PROC
10 rows got
```

已用时间`: 23.196(`毫秒`).` 执行号`:764.`

例4使用`DEPTH`显示列的结构信息

```
CREATE TYPE ADDRESS AS OBJECT
( STREET VARCHAR2(20),
CITY VARCHAR2(20)
);
/
CREATE TYPE ADDRESS1 AS OBJECT
( NO INT,
SADDR ADDRESS
);
/
```

创建表`EMPINFO`：

```
CREATE TABLE EMPINFO
(LAST_NAME VARCHAR2(30),
EMPADDR ADDRESS,
SMADDR ADDRESS1,
JOB_ID VARCHAR2(20),
SALARY NUMBER(7,2)
);
```

设置`DESCRIBE`的显示方式 :

```
SQL>SET DESCRIBE DEPTH 1 LINENUM ON INDENT ON;
```

获取表`EMPINFO`的结构描述如下：

```
SQL>DESC EMPINFO;
行号 ID PID NAME TYPEV NULLABLE
---------- -- --- --------- ----------- --------
1 1 LAST_NAME VARCHAR(30) Y
2 2 EMPADDR ADDRESS Y
3 3 2 STREET VARCHAR(20)
4 4 2 CITY VARCHAR(20)
5 5 SMADDR ADDRESS1 Y
6 6 5 NO INTEGER
7 7 5 SADDR ADDRESS
8 8 JOB_ID VARCHAR(20) Y
9 9 SALARY DEC(7, 2) Y
9 rows got
```

已用时间`: 18.325(`毫秒`).` 执行号`:768.`

设置`DEPTH`为1时，表`EMPINFO`的结构信息只显示至第一层。`LINENUM`为`ON`时，显示行号`ID`、`PID`信息；反之，行号`ID`、`PID`信息不显示；`INDENT`为`ON`时，`NAME`的显示方式发生了缩进；反之，不发生缩进。

重新设置`DESCRIBE`的显示方式，并获取表`EMPINFO`的结构描述如下：

```
SQL>SET DESCRIBE DEPTH 2 LINENUM ON INDENT ON;
SQL>DESC EMPINFO;
```

执行结果如下：

图`4.1`查看`DEPTH`为2时显示结果

由上图可见，与`DEPTH`为1时对比，表`EMPINFO`的结构描述增加了属于第二层的两列信息：`STREET`和`CITY`。

## 4.5 定义本地变量DEFINE和COLUMN

定义本地变量的命令有两个：一是`DEFINE`；二是`COLUMN`。

### 4.5.1 DEFINE

用来定义一个本地变量的替代变量，然后对该变量赋一个`CHAR`类型的值；或者输出变量的值和类型。

语法如下：

```
DEF[INE] [|< VARIABLE >]
```

`DEF[INE] VARIABLE = text`：申明一个变量，如果该变量存在，则重新赋值，否则新生成一个变量，并进行赋值。

`DEF[INE] VARIABLE`：如果该变量存在，则输出特定`VARIABLE`的值和类型，否则报错。

`DEF[INE]`：输出`DIsql`中所有的变量的值和类型。

该命令定义的替代变量在当前的`DIsql`环境和`/NOLOG`环境中均可以起作用。

当使用该命令定义变量时，如果变量值包含空格或区分大小写，则用引号引注。另外，使用`“DEFINE`变量名”可以检查变量是否已经定义。

`DEFINE`定义的变量会保存在环境`DIsql`环境中，可以在`SQL`语句中使用。默认的变量前缀是&。示例如下：

```
SQL>DEF VAR=666;
SQL>select * from dual where id=&VAR;
```

如果`var`没有定义，会提示输入变量的值；没有定义的`var`不会保存在`DIsql`环境中。

关闭变量替换：

```
SET define off
Define变量与其他字符之间的连接字符是点号’.’。示例如下：
SQL>set define on
SQL>def var1 = C;
SQL>def var2 = test1;
SQL>drop table test1;
SQL>create table test1(c1 int);
SQL>insert into test1 values(1);
SQL>commit;
SQL>select &var1.1 from test1;
```

行号 `C1`

```
---------- -----------
1 1
```

已用时间`: 0.428(`毫秒`).` 执行号`:702.`

```
SQL> select &var2..c1 from test1;
原值 1:select &var2..c1 from test1;
新值 1:select TEST1.c1 from test1;
```

行号 `C1`

```
---------- -----------
1 1
```

已用时间`: 0.355(`毫秒`).` 执行号`:703.`

```
DEFINE变量定义为整型。示例如下：
SQL>SET DEFINE ON --打开DEFINE变量定义
SQL>DEFINE C1=1 --定义变量C1为1
SQL>SELECT &C1 FROM DUAL;
原值 1:SELECT &C1 FROM DUAL;
新值 1:SELECT 1 FROM DUAL;
```

行号 1

```
---------- -----------
1 1
```

已用时间`: 0.477(`毫秒`).` 执行号`:704.`

`--`在存储函数中的使用

```
SQL>CREATE OR REPLACE FUNCTION F1(C1 INT)RETURN INT IS
BEGIN
C1=&C1;
RETURN(C1);
END;
/
SQL> SELECT F1(0);
```

行号 `F1(0)`

```
---------- -----------
1 1
```

已用时间`: 0.355(`毫秒`).` 执行号`:707.`

`SQL>DEFINE C2=(2+3*4) --`定义变量`C2`为表达式,定义为表达式时必须加括号

```
SQL> SELECT &C2*4 FROM DUAL;
原值 1:SELECT &C2*4 FROM DUAL;
新值 1:SELECT (2+3*4)*4 FROM DUAL;
行号 (2+(3*4))*4
---------- -----------
1 56
```

已用时间`: 0.490(`毫秒`).` 执行号`:708.`

```
DEFINE变量定义为字符型。示例如下：
SQL>SET DEFINE ON --打开DEFINE变量定义
```

`SQL>DEFINE C3="'OG'" --`定义变量`C3`为`'OG'--`一种使用`DEFINE`字符串变量的方式

```
SQL> SELECT &C3 FROM DUAL;
原值 1:SELECT &C3 FROM DUAL;
新值 1:SELECT 'OG' FROM DUAL;
```

行号 `'OG'`

```
---------- ----
1 OG
```

已用时间`: 0.470(`毫秒`).` 执行号`:709.`

```
SQL>SELECT LCASE(&C3) FROM DUAL;--引用变量为函数参数
原值 1:SELECT LCASE(&C3) FROM DUAL;
新值 1:SELECT LCASE('OG') FROM DUAL;
行号 LCASE('OG')
---------- -----------
1 og
```

已用时间`: 14.052(`毫秒`).` 执行号`:59.`

```
SQL>SET DEFINE ON --打开DEFINE变量定义
```

`SQL>DEFINE C4=OG --`定义变量`C4`为`OG --`另外一种使用`DEFINE`字符串变量的方式

```
SQL>SELECT '&C4' FROM DUAL;
原值 1:SELECT '&C4' FROM DUAL;
新值 1:SELECT 'OG' FROM DUAL;
```

行号 `'OG'`

```
---------- ----
1 OG
```

已用时间`: 0.173(`毫秒`).` 执行号`:711.`

```
SQL>CREATE OR REPLACE FUNCTION F1(&C4 INT)RETURN INT IS
BEGIN
&C4=777;
RETURN(&C4);
END;
/
SQL> SELECT F1(0);
```

行号 `F1(0)`

```
---------- -----------
1 777 -- 返回值OG=777
```

已用时间`: 0.460(`毫秒`).` 执行号`:713.`

`DEFINE`变量定义为日期类型。示例如下：

```
SQL>SET DEFINE ON --打开DEFINE变量定义
SQL>DEFINE C5="DATE'2015-10-01'"
SQL>SELECT &C5+1 FROM DUAL; --引用变量值加1天
原值 1:SELECT &C5+1 FROM DUAL;
新值 1:SELECT DATE'2015-10-01'+1 FROM DUAL;
行号 DATE'2015-10-01'+1
---------- ------------------
1 2015-10-02
```

已用时间`: 28.478(`毫秒`).` 执行号`:714.`

```
SQL>SELECT &C5+INTERVAL '01-02' YEAR TO MONTH FROM DUAL; --引用变量值与日期类型作运算
原值 1:SELECT &C5+INTERVAL '01-02' YEAR TO MONTH FROM DUAL;
新值 1:SELECT DATE'2015-10-01'+INTERVAL '01-02' YEAR TO MONTH FROM DUAL;
行号 DATE'2015-10-01'+INTERVAL+'01-02'YEARTOMONTH
---------- --------------------------------------------
1 2016-12-01
```

已用时间`: 0.482(`毫秒`).` 执行号`:715.`

### 4.5.2 COLUMN

定义一个本地列或表达式。

语法如下：

```
COL[UMN] [ []]
::= NEW_VALUE variable
```

`COL[UMN]`：列举出所有的`COLUMN`变量信息。

`COL[UMN] column | expr`：列举出某个`column`或`expr`，如果存在，则输出信息，否则报错。

`COL[UMN] column | expr option`：`option`目前仅支持`NEW_VALUE`，表示该`column|expr`的值，同时作为变量存在。但如果该变量未赋值，通过`DEFINE`查询时，不会显示该变量。

查询结果的最后一个值赋给本地变量。

示例如下：

```
SQL> COLUMN CVAR NEW_VALUE DVAR
SQL> SELECT CUSTOMERID CVAR FROM SALES.CUSTOMER;
```

行号 `CVAR`

```
---------- -----------
1 1
2 2
3 3
4 4
5 5
6 6
6 rows got
```

已用时间`: 1.105(`毫秒`).` 执行号`:1053.`

```
SQL> DEFINE DVAR
DEFINE DVAR = "6" (INT)
```

通过如下方式设置将变量`VARIABLE`与列名`column`之间的关联，默认值为`ON`，表示已关联。

语法如下：

```
COL[UMN] column
```

示例如下：

```
SQL>COLUMN CVAR OFF
```

## 4.6 查看执行计划EXPLAIN

用`explain`命令来查看查询语句的执行计划。

语法如下：

```
explain
请参考《DM_SQL》。
```

示例如下：

```
SQL>explain select count(*) from sysobjects;
```

## 4.7 设置异常处理方式whenever

用`whenever`命令可以设置异常处理方式，继续执行或退出`DIsql`。

语法如下：

```
WHENEVER SQLERROR
CONTINUE [ COMMIT | ROLLBACK | NONE ] |
EXIT [ SUCCESS | FAILURE | WARNING | n | | : ] [ COMMIT | ROLLBACK ]
```

n和``的返回值受限于操作系统，在不同平台下，会有所不同，例如：`UNIX`系统只用一个字节来存`code`，所以返回值的范围只在`0-255`之间。

示例如下：

```
SQL>whenever sqlerror exit 1
SQL>select c1 from dual;
select c1 from dual;
```

第1 行附近出现错误`[-2111]:`无效的列名`[C1].`

`--windows`系统下，输入`echo %ERRORLEVEL%`，查看返回值为：1

`--linux`系统下，输入`echo $?`，查看返回值为：1
