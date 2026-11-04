---
title: "其他"
book: "Oracle兼容性"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/compatibility/compOracle35.html"
tags:
  - highgo
  - highgo-v9
  - compatibility-oracle
---

## 其他

## q\`转义

### 说明

‘’：最外面的两个单引号分别位于两个quote\_delimiter的开始和结束。

c ：是用户字符集的任何成员。可以在由 c 个字符组成的文本文字中包含引号 （‘’）。还可以包含quote\_delimiter，只要它不紧跟单引号即可。

quote\_delimiter：除空格、制表符和回车之外的任何单字节或多字节字符。可以是单引号。但是，如果 quote\_delimiter 出现在文本文字本身中，请确保它后面没有紧跟单引号。

如果开始的quote\_delimiter 是\[、{、< 或() 之一，那么结束的quote\_delimiter 必须是对应的\]、}、> 或)。在所有其他情况下，开始和结束quote\_delimiter 必须是相同的字符。

### 示例

select q’’’s is good’’ from dual;

select q’\[‘s is good\]‘ from dual;

## 大小写兼容

### 说明

支持Oracle对象大小写转换，可处理如下情况：全部大写加双引号转换为小写；全部小写加双引号转换为大写；大小写混合加双引号保持不变；不加双引号(默认)全部转为小写。

### 示例

预设关于大小写参数：

SET ivorysql.enable\_case\_switch = true; #打开大小写

SET ivorysql.identifier\_case\_switch = interchange; #大小写敏感

- 在表名不加引号情况下：
- 创建表名全小写，且不加引号的测试表

create table employee\_tb1(epno int,name varchar(20));

向表中插入数据

insert into employee\_tb1 values (1,’employee1’);

可以通过以下语句，查看已插入数据

select \* from employee\_tb1;

select \* from EMPLOYEE\_TB1;

select \* from Employee\_tb1;

- 创建表名全大写，且不加引号的测试表

create table EMPLOYEE\_TB2(epno int,name varchar(20));

向表中插入数据

insert into EMPLOYEE\_TB2 values (1,’employee2’);

可以通过以下语句，查看已插入数据

select \* from employee\_tb2;

select \* from EMPLOYEE\_TB2;

select \* from Employee\_tb2;

- 创建表名大小写混合，且不加引号的测试表

create table EMPLOYEE\_tb3(epno int,name varchar(20));

向表中插入数据

insert into EMPLOYEE\_tb3 values (1,’employee3’);

可以通过以下语句，查看已插入数据

select \* from employee\_tb3;

select \* from EMPLOYEE\_TB3;

select \* from Employee\_tb3;

- 在表名加引号情况下：
- 创建表名为全小写，且加引号的测试表

create table “employee\_tb4” (epno int,name varchar(20));

向表中插入数据

insert into “employee\_tb4” values (1,’employee4’);

可以通过以下语句，查看已插入数据

select \* from “employee\_tb4”;

- 创建表名为全大写，且加引号的测试表

create table “EMPLOYEE\_TB5” (epno int,name varchar(20));

向表中插入数据

insert into “EMPLOYEE\_TB5” values (1,’employee5’);

可以通过以下语句，查看已插入数据

select \* from “EMPLOYEE\_TB5”;

- 创建表名为全小写混合，且加引号的测试表

create table “EMPLOYEE\_tb6” (epno int,name varchar(20));

向表中插入数据

insert into “EMPLOYEE\_tb6” values (1,’employee6’);

可以通过以下语句，查看已插入数据

select \* from “EMPLOYEE\_tb6”;

## 空串转NULL

### 说明

兼容模式下支持将空字符串转换成NULL进行存储，在使用该特性时需要设置ivorysql.enable\_emptystring\_to\_null ，默认值是on。

### 示例

highgo=# create table abc (id int);

CREATE TABLE

highgo=# show ivorysql.enable\_emptystring\_to\_null;

ivorysql.enable\_emptystring\_to\_NULL

\-————————————

on

(1 row)

highgo=# insert into abc values(‘’);

INSERT 0 1

highgo=# select \* from abc;

id

\-—

(1 row)

highgo=# select \* from abc where id is null;

id

\-—

(1 row)

## 语句级回滚

语句级回滚功能主要是指，当单个 SQL 语句执行失败时，只回滚该语句所做的更改，而不影响事务中其他已成功的语句；在plisql语句块内，若发生了异常并进行了捕获，前序成功的语句可以正常被提交。

在HGDB V9.0中，可通过参数ivorysql.ora\_statement\_level\_rollback启用语句级回滚特性。默认值为off。

说明：

该功能在V9.0.5及以后的版本中支持。

### 示例一：事务中的语句级回滚

```
--使用默认值
show ivorysql.ora_statement_level_rollback;
ivorysql.ora_statement_level_rollback 
---------------------------------------
 off
(1 行记录)

--执行如下语句
CREATE TABLE test1(a int);
BEGIN;
INSERT INTO test1 VALUES(111);
INSERT INTO test1 VALUES(‘aaa’);  --failed
INSERT INTO test1 VALUES(222);
COMMIT;

--查看表数据，未成功插入数据
SELECT * FROM test1;
 a 
---
(0 行记录)
```

将ivorysql.ora\_statement\_level\_rollback参数设置为on，再次执行上面的示例：

```
--设置参数值为on
set ivorysql.ora_statement_level_rollback to on;

--再次执行如下语句
BEGIN;
INSERT INTO test1 VALUES(111);
INSERT INTO test1 VALUES(‘aaa’);  --failed
INSERT INTO test1 VALUES(222);
COMMIT;

--查看表数据，成功插入两条数据
highgo=# SELECT * FROM test1;
 a  
-----
 111
 222
(2 行记录)
```

### 示例二：plsql中的语句级回滚

–使用默认值

```
show ivorysql.ora_statement_level_rollback;

ivorysql.ora_statement_level_rollback 
---------------------------------------

 off
(1 行记录)

--执行如下语句
CREATE TABLE test2(a int);
Begin
  INSERT INTO test2 VALUES(123);
  INSERT INTO test2 VALUES('a');
 EXCEPTION
  WHEN OTHERS THEN
   COMMIT;
 END;
 /

--查看表数据，未成功插入数据
SELECT * FROM test2;

 a 
---

(0 行记录)
```

将ivorysql.ora\_statement\_level\_rollback参数设置为on，再次执行上面的示例：

```
--设置参数值为on
set ivorysql.ora_statement_level_rollback to on;

--再次执行如下语句
Begin
  INSERT INTO test2 VALUES(123);
  INSERT INTO test2 VALUES('a');
 EXCEPTION
  WHEN OTHERS THEN
   COMMIT;
 END;
 /

--查看表数据，成功插入一条数据
SELECT * FROM test2;
 a  
-----
 123
(1 行记录)
```

## 事务自动提交

说明：

该功能在V9.0.5及以后的版本中支持。

### 断开连接事务自动提交

将参数ivorysql.ora\_commit\_before\_disconnect设置为on（默认值为off）时，当事务块未提交且未回滚时断开连接，系统会自动提交事务块。

#### 示例

```
--使用默认值off
show ivorysql.ora_commit_before_disconnect;
 ivorysql.ora_commit_before_disconnect 
---------------------------------------
 off
(1 行记录)

--执行如下语句
CREATE TABLE test1(a int);
BEGIN;
INSERT INTO test1 VALUES(111);
--此时断开psql连接 

--再次登录数据库查看表test1的数据，返回0行
SELECT * FROM test1;
 a 
---

(0 行记录)
```

将参数ivorysql.ora\_commit\_before\_disconnect设置为on时，再次执行上面的示例：

```
--将参数设置为on
set ivorysql.ora_commit_before_disconnect to on;

--再次执行如下语句
BEGIN;
INSERT INTO test1 VALUES(111);
--此时断开psql连接 

--再次登录数据库查看表test1的数据，成功插入一条数据
select * from test1;
 a  
-----
 111
(1 行记录)
```

## 系统参数

### NLS\_DATE\_FORMAT

| **属性** | **描述** |
| --- | --- |
| 参数类型 | STRING |
| 语法 | NLS\_DATE\_FORMAT = “format” |
| 可修改 | ALTER SESSION |
| 取值范围 | 任何有效的日期格式掩码，但不超过固定长度 |

NLS\_DATE\_FORMAT指定to\_CHAR和to\_DATE函数使用的默认日期格式。

此参数的值可以是任何有效的日期格式掩码，并且该值必须用引号括起来。

例如：NLS\_DATE\_FORMAT = “MM/DD/YYYY”

### NLS\_TIMESTAMP\_FORMAT

| **属性** | **描述** |
| --- | --- |
| 参数类型 | STRING |
| 语法 | NLS\_TIMESTAMP\_FORMAT = “format” |
| 可修改 | ALTER SESSION |
| 取值范围 | 任何有效的日期时间格式掩码 |

NLS\_TIMESTAMP\_FORMAT定义用于to\_CHAR和to\_TIMESTAMP函数的默认时间戳格式。

该值必须用引号括起来，如下所示：

NLS\_TIMESTAMP\_FORMAT=’YYYY-MM-DD HH:MI:SS.FF’

可以通过在数据库配置文件中设置NLS\_TIMESTAMP\_FORMAT的值来指定，然后重新启动实例来更改其值。要在会话期间更改值，请使用alter session SET语句。

### NLS\_TIMESTAMP\_TZ\_FORMAT

| **属性** | **描述** |
| --- | --- |
| 参数类型 | STRING |
| 语法 | NLS\_TIMESTAMP\_TZ\_FORMAT = “format” |
| 可修改 | ALTER SESSION |
| 取值范围 | 任何有效的日期时间格式掩码 |

该值必须用引号括起来，如下所示：

NLS\_TIMESTAMP\_TZ\_FORMAT = ‘YYYY-MM-DD HH:MI:SS.FF TZH:TZM’

通过在数据库配置文件中设置NLS\_TIMESTAMP\_TZ\_FORMAT的值来指定它，然后重新启动实例来更改其值。要在会话期间更改值，请使用alter session SET语句。

### NLS\_LENGTH\_SEMANTICS

| **属性** | **描述** |
| --- | --- |
| 参数类型 | STRING |
| 语法 | NLS\_LENGTH\_SEMANTICS = string      示例: NLS\_LENGTH\_SEMANTICS = ‘CHAR’ |
| 默认值 | BYTE |
| 可修改 | ALTER SESSION |
| 取值范围 | BYTE \| CHAR |

NLS\_LENGTH\_SEMANTICS的会话级值指定用于会话中创建的数据库对象中的VARCHAR2和CHAR表列、用户定义的对象属性和PL/SQL变量的默认长度语义。此默认值可能会被列、属性和变量定义中的显式长度语义限定符BYTE和CHAR覆盖。

NCHAR、NVARCHAR2、CLOB和NCLOB列始终基于字符。

### NLS\_TERRITORY

| **属性** | **描述** |
| --- | --- |
| 参数类型 | STRING |
| 语法 | NLS\_TERRITORY = territory |
| 默认值 | 依赖操作系统 |
| 可修改 | ALTER SESSION |
| 取值范围 | 一些有效的territory |
| 基础参数 | 是 |

注：当前支持CHINA和AMERICA

### NLS\_CURRENCY

| **属性** | **描述** |
| --- | --- |
| 参数类型 | STRING |
| 语法 | NLS\_CURRENCY = currency\_symbol |
| 默认值 | 源自NLS\_TERRITORY |
| 可修改 | ALTER SESSION |
| 取值范围 | 至多十个字节（不含空）的字符串 |
| 基础参数 | 否 |

可以设置为更长，但是在使用时会自动截取其前10个字节作为该参数值（expr中可用）；可以加单引号、双引号或者不加引号（某些特殊字符必须加引号，引号影响存储大小写，前导L匹配NLS\_CURRENCY参数值大小写不敏感，0/9之后的L匹配NLS\_CURRENCY参数值大小写敏感）；使用数字时不产生歧义（如a123b）即可。

### NLS\_ISO\_CURRENCY

| **属性** | **描述** |
| --- | --- |
| 参数类型 | STRING |
| 语法 | NLS\_ISO\_CURRENCY = territory |
| 默认值 | 源自NLS\_TERRITORY |
| 可修改 | ALTER SESSION |
| 取值范围 | 任意合法NLS\_TERRITORY值（国家或地区名\*） |
| 基础参数 | 否 |

根据该参数所指定的国家或地区，按照ISO 4217 Currency Codes来确定要使用的货币代码；参数值可以加单引号、双引号或者不加引号（影响该参数值存储大小写，但是匹配时固定为该国家或地区货币代码的大写字符串）。

### NLS\_DUAL\_CURRENCY

| **属性** | **描述** |
| --- | --- |
| 参数类型 | STRING |
| 语法 | NLS\_DUAL\_CURRENCY = currency\_symbol |
| 默认值 | 源自NLS\_TERRITORY |
| 可修改 | ALTER SESSION |
| 取值范围 | 至多十个字符的任意合法格式名字 |
| 基础参数 | 否 |

可以设置为更长，但是在使用时会自动截取其前7个字节作为该参数值（expr中可用）；可以加单引号、双引号或者不加引号（某些特殊字符必须加引号，引号影响存储大小写，前导U匹配NLS\_DUAL\_CURRENCY参数值大小写不敏感，0/9之后的U匹配NLS\_DUAL\_CURRENCY参数值大小写敏感）；使用数字时不产生歧义（如a123b）即可。

### NLS\_NUMERIC\_CHARACTERS

| **属性** | **描述** |
| --- | --- |
| 参数类型 | STRING |
| 语法 | NLS\_NUMERIC\_CHARACTERS = “decimal\_character group\_separator”\* |
| 默认值 | 源自NLS\_TERRITORY |
| 可修改 | ALTER SESSION |
| 基础参数 | 否 |

两个符号必须是单字节的不同符号；不能使用数字或 +、-、<、>，可为空格；引号内只取前两字节，所以 ”.,”（点号+空格+逗号）等同于 ”. ”（点号+空格）；需要单引号或双引号。

### NLS\_SORT

| **属性** | **描述** |
| --- | --- |
| 参数类型 | STRING |
| 语法 | NLS\_SORT = { BINARY \| linguistic\_definition } |
| 默认值 | BINARY |
| 可修改 | ALTER SESSION |
| 说明 | 兼容模式 |

用于指定字符串排序的规则，影响SQL查询中字符串的排序顺序。NLS\_SORT 的设置与NLS\_COMP配合使用，可以更好地控制数据的排序和比较行为。

### NLS\_COMP

| **属性** | **描述** |
| --- | --- |
| 参数类型 | STRING |
| 语法 | NLS\_COMP = { BINARY \| LINGUISTIC \| ANSI } |
| 默认值 | BINARY |
| 可修改 | ALTER SESSION |
| 说明 | 兼容模式 |

设置数据库的比较行为，主要影响字符串的比较操作。NLS\_COMP的值影响到 SQL查询中的字符串比较，如ORDER BY和WHERE子句。

### OPEN\_LINKS

| **属性** | **描述** |
| --- | --- |
| 参数类型 | INT |
| 语法 | set OPEN\_LINKS =’N’ |
| 默认值 | N默认为4 |
| 可修改 | ALTER SYSTEM |
| 说明 | 用于限制Oracle数据库中的连接数量 |

### OPEN\_LINKS\_PER\_INSTANCE

| **属性** | **描述** |
| --- | --- |
| 参数类型 | INT |
| 语法 | set OPEN\_LINKS\_PER\_INSTANCE =’N’ |
| 默认值 | N默认为4 |
| 可修改 | ALTER SYSTEM |
| 说明 | 用于限制Oracle数据库实例的全局可迁移开放连接数量 |

### GLOBAL\_NAMES

| **属性** | **描述** |
| --- | --- |
| 参数类型 | STRING |
| 语法 | set GLOBAL\_NAMES=false |
| 默认值 | false |
| 可修改 | ALTER SESSION, ALTER SYSTEM |
| 说明 | 指定数据库链接是否需要与其连接的数据库具有相同的名称 |

### PLSQL\_WARINGS

| **属性** | **描述** |
| --- | --- |
| 参数类型 | STRING |
| 语法 | PLSQL\_WARNINGS = ‘value\_clause’ \[, ‘value\_clause’ \] …      value\_clause::=      { ENABLE \| DISABLE \| ERROR }:      { ALL      \| SEVERE      \| INFORMATIONAL      \| PERFORMANCE      \| { integer      \| (integer \[, integer \] …)      }      } |
| 默认值 | ‘DISABLE:ALL’ |
| 可修改 | ALTER SESSION, ALTER SYSTEM |
| 说明 | 启用或禁用所有的警告，或者一种或多种类别的警告，或者一种特殊的警告。      示例：      PLSQL\_WARNINGS = ‘ENABLE:SEVERE’, ‘DISABLE:INFORMATIONAL’;      PLSQL\_WARNINGS = ‘DISABLE:ALL’;      PLSQL\_WARNINGS = ‘DISABLE:5000’, ‘ENABLE:5001’, ‘ERROR:5002’;      PLSQL\_WARNINGS = ‘ENABLE:(5000,5001,5002)’, ‘DISABLE:(6000,6001)’; |

## GUC

### IVORYSQL.COMPATIBLE\_MODE

| **属性** | **描述** |
| --- | --- |
| 参数类型 | STRING |
| 语法 | set ivorysql.compatible\_mode = pg \| oracle |
| 默认值 | oracle |
| 可修改 | ALTER SESSION |
| 说明 | 兼容模式 |

### IVORYSQL.DATABASE\_MODE

| **属性** | **描述** |
| --- | --- |
| 参数类型 | STRING |
| 语法 | initdb -m pg \| oracle |
| 默认值 | oracle |
| 可修改 | 初始化实例 |
| 说明 | 数据库实例模式 |

### IVORYSQL.DATETIME\_IGNORE\_NLS\_MASK

| **属性** | **描述** |
| --- | --- |
| 参数类型 | INT |
| 语法 | set ivorysql.datetime\_ignore\_nls\_mask = 0 |
| 默认值 | 0 |
| 可修改 | ALTER SESSION |
| 说明 | 设置日期时间类型输入不受NLS参数控制      datetime\_ignore\_nls\_mask = 0 /\* 不屏蔽任何类型 \*/      datetime\_ignore\_nls\_mask = 1 /\* date \*/      datetime\_ignore\_nls\_mask = 2 /\* timestamp \*/      datetime\_ignore\_nls\_mask = 3 /\* date timestamp \*/      datetime\_ignore\_nls\_mask = 4 /\* timestamptz \*/      datetime\_ignore\_nls\_mask = 5 /\* date timestamptz \*/      datetime\_ignore\_nls\_mask = 6 /\* timestamp timestamptz \*/      datetime\_ignore\_nls\_mask = 7 /\* date timestamp timestamptz \*/      datetime\_ignore\_nls\_mask = 8 /\* timestampltz \*/      datetime\_ignore\_nls\_mask = 9 /\* date timestampltz \*/      datetime\_ignore\_nls\_mask = 10 /\* timestamp timestampltz \*/      datetime\_ignore\_nls\_mask = 11 /\* date timestamp timestampltz \*/      datetime\_ignore\_nls\_mask = 12 /\* timestamptz timestampltz \*/      datetime\_ignore\_nls\_mask = 13 /\* date timestamptz timestampltz \*/      datetime\_ignore\_nls\_mask = 14 /\* timestamp timestamptz timestampltz \*/      datetime\_ignore\_nls\_mask = 15 /\* date timestamp timestamptz timestampltz \*/ |

### IVORYSQL.ENABLE\_ORA\_MERGE\_TUNING

| **属性** | **描述** |
| --- | --- |
| 参数类型 | BOOL |
| 语法 | set ivorysql.enable\_ora\_merge\_tuning = on \| off |
| 默认值 | off |
| 可修改 | ALTER SESSION |
| 说明 | 打开merge调优功能 |

### IVORYSQL.ENABLE\_CASE\_SWITCH

| **属性** | **描述** |
| --- | --- |
| 参数类型 | BOOL |
| 语法 | set ivorysql.enable\_case\_switch = on \| off |
| 默认值 | on |
| 可修改 | ALTER SESSION |
| 说明 | 打开大小写 |

### IVORYSQL.ENABLE\_EMPTYSTRING\_TO\_NULL

| **属性** | **描述** |
| --- | --- |
| 参数类型 | BOOL |
| 语法 | set ivorysql.enable\_emptystring\_to\_NULL = on \| off |
| 默认值 | on |
| 可修改 | ALTER SESSION |
| 说明 | 是否空转null |

### IVORYSQL.IDENTIFIER\_CASE\_SWITCH

| **属性** | **描述** |
| --- | --- |
| 参数类型 | STRING |
| 语法 | set ivorysql.identifier\_case\_switch = INTERCHANGE |
| 默认值 | INTERCHANGE |
| 可修改 | ALTER SESSION |
| 说明 | NORMAL对于带双引号不做转换；      INTERCHANGE进行大小写转换；      LOWERCASE是带双引号的都转换为小写。 |
| 取值范围 | NORMAL\|INTERCHANGE\|LOWERCASE |

### IVORYSQL.INSERT\_ENABLE\_ALIAS

| **属性** | **描述** |
| --- | --- |
| 参数类型 | BOOL |
| 语法 | set ivorysql.insert\_enable\_alias = on \| off |
| 默认值 | off |
| 可修改 | ALTER SESSION |
| 说明 | 是否支持表别名插入 |

### IVORYSQL.LISTEN\_ADDRESSES

| **属性** | **描述** |
| --- | --- |
| 参数类型 | STRING |
| 语法 | set ivorysql.listen\_addresses =’\*‘ |
| 默认值 | localhost |
| 可修改 | ALTER SYSTEM |
| 说明 | Oracle兼容模式服务IP |

### IVORYSQL.PORT

| **属性** | **描述** |
| --- | --- |
| 参数类型 | NUMBER |
| 语法 | set ivorysql.port =1521 |
| 默认值 | 1521 |
| 可修改 | ALTER SYSTEM |
| 说明 | Oracle兼容模式服务端口号 |

### IVORYSQL.DEFAULT\_DBLINK\_FDW

| **属性** | **描述** |
| --- | --- |
| 参数类型 | STRING |
| 语法 | set ivorysql.default\_dblink\_fdw = ‘postgres\_fdw’ \|’oracle\_fdw’ |
| 默认值 | postgres\_fdw |
| 可修改 | ALTER SESSION, ALTER SYSTEM |
| 说明 | Dblink的不同模式 |

### IVORYSQL.CHECK\_INK\_METADATA\_CHANGED

| **属性** | **描述** |
| --- | --- |
| 参数类型 | STRING |
| 语法 | set ivorysql.check\_lnk\_metadata\_changed=on \| off |
| 默认值 | off |
| 可修改 | ALTER SESSION, ALTER SYSTEM |
| 说明 | 控制与远端表结构是否同步 |

### IVORYSQL.ENABLE\_ORA\_USER\_SCHEMA

|  |  |
| --- | --- |
| **属性** | **描述** |
| 参数类型 | STRING |
| 语法 | set ivorysql.enable\_ora\_user\_schema=on \| off |
| 默认值 | on |
| 可修改 | ALTER SESSION |
| 说明 | 兼容oracle schema的总开关：      on：默认值，符合dblink描述的所有特性。      off：关闭，用户和schema分别管理，恢复dblink修改和禁用的所有功能和特性。 |

### IVORYSQL.DBLINKREL\_SCHEMA\_USE\_USER

| **属性** | **描述** |
| --- | --- |
| 参数类型 | STRING |
| 语法 | set ivorysql.dblinkrel\_schema\_use\_user=on \| off |
| 默认值 | on |
| 可修改 | ALTER SESSION, ALTER SYSTEM |
| 说明 | 当参数设置为“on”时，“connect to user”功能会查找与连接用户同名的schema中的对象，并将远端对象的查询结果拼接为“schema.对象名”的形式。      当参数设置为“off”时，查询远端对象时会使用创建dblink的用户所在search\_path的第一个模式。      当没有用户同名模式情况下，建议显示指定模式为public。 |

### IVORYSQL.HEX\_BYTEA

| **属性** | **描述** |
| --- | --- |
| 参数类型 | STRING |
| 语法 | set ivorysql.hex\_bytea=on \| off |
| 默认值 | off |
| 可修改 | ALTER SESSION, ALTER SYSTEM |
| 说明 | 当参数设置为“on”时，开启十六进制显示转换，去掉\\x。      当参数设置为“off”时，关闭十六进制显示转换，保持现状。 |

### IVORYSQL.AGGREGATES\_WITHOUT\_GROUP\_BY

| **属性** | **描述** |
| --- | --- |
| 参数类型 | STRING |
| 语法 | set ivorysql.aggregates\_without\_group\_by=on \| off |
| 默认值 | off |
| 可修改 | ALTER SESSION, ALTER SYSTEM |
| 说明 | 当参数设置为“on”时，允许在无 GROUP BY 的单行聚合查询中直接使用非聚合列排序。   当参数设置为“off”时，排序列必须出现在GROUP BY子句或者在聚合函数中使用。 |

### IVORYSQL.ENABLE\_COMPATIBLE\_TYPE\_SHIPPABLE

| **属性** | **描述** |
| --- | --- |
| 参数类型 | BOOL |
| 语法 | set ivorysql.enable\_compatible\_type\_shippable=on \| off |
| 默认值 | on |
| 可修改 | ALTER SESSION, ALTER SYSTEM |
| 说明 | 该参数用于控制使用dblink时，Oracle兼容类型的操作符是否下推。当参数设置为“on”时，兼容类型的操作符下推到远程处理，以此提升dblink查询效率。该参数在V9 03-2-0、V9 04-1-0及以后的版本中提供。 |

### IVORYSQL.ENABLE\_RECYCLE\_BIN

| **属性** | **描述** |
| --- | --- |
| 参数类型 | BOOL |
| 语法 | set ivorysql.enable\_recycle\_bin = on \| off |
| 默认值 | off |
| 可修改 | ALTER SESSION, ALTER SYSTEM |
| 说明 | 当参数设置为“on”时，开启回收站功能。当参数设置为“off”时，关闭回收站功能。该参数在V9.0.5及以后的版本中支持。 |

### IVORYSQL.ORA\_STATEMENT\_LEVEL\_ROLLBACK

| **属性** | **描述** |
| --- | --- |
| 参数类型 | BOOL |
| 语法 | set ivorysql.ora\_statement\_level\_rollback = on \| off |
| 默认值 | off |
| 可修改 | ALTER SESSION, ALTER SYSTEM |
| 说明 | 是否启用语句级回滚特性。该参数在V9.0.5及以后的版本中支持。 |

### IVORYSQL.ORA\_COMMIT\_BEFORE\_DISCONNECT

| **属性** | **描述** |
| --- | --- |
| 参数类型 | BOOL |
| 语法 | set ivorysql.ora\_commit\_before\_disconnect = on \| off |
| 默认值 | off |
| 可修改 | ALTER SESSION, ALTER SYSTEM |
| 说明 | 是否启用断开连接事务自动提交特性。该参数在V9.0.5及以后的版本中支持。 |

### IVORYSQL.MAX\_AUTONOMOUS\_TRANSACTIONS

| **属性** | **描述** |
| --- | --- |
| 参数类型 | INT |
| 语法 | set ivorysql.max\_autonomous\_transactions = 32 |
| 默认值 | 32 |
| 可修改 | ALTER SYSTEM |
| 说明 | 实例中同时运行的自治事务的最大数量。可取值1到262143。该参数在V9.0.5及以后的版本中支持。 |

### IVORYSQL.AUTONTRANS\_NESTING\_LEVEL

| **属性** | **描述** |
| --- | --- |
| 参数类型 | INT |
| 语法 | set ivorysql.autontrans\_nesting\_level = 16 |
| 默认值 | 16 |
| 可修改 | ALTER SESSION, ALTER SYSTEM |
| 说明 | 自治事务嵌套调用的级别。参数值必须小于等于max\_autonomous\_transactions。可取值1到64。该参数在V9.0.5及以后的版本中支持。 |