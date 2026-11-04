---
title: "内置函数"
book: "Oracle兼容性"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/compatibility/compOracle6.html"
tags:
  - highgo
  - highgo-v9
  - compatibility-oracle
---

## 内置函数

## 概述

瀚高数据库管理系统V9.0提供多种兼容内置函数，内容如下：

字符类型函数：

| **函数名称** | **说明** |
| --- | --- |
| length | 给定编码字符串中的字符数。 |
| lengthb | 给定编码字符串中的字节数。 |
| trim | 从字符串的开头/结尾/两端删除最长的只包含 characters（默认是一个空格）的串 |
| ltrim | 从字符串的开头删除最长的只包含characters（默认是一个空格）的串 |
| rtrim | 从字符串的结尾删除最长的只包含characters（默认是一个空格）的串 |
| regexp\_replace | 字符串通过正则表达式来进行匹配替换 |
| regexp\_substr | 字符串通过正则表达式来返回字符串子串 |
| regexp\_instr | 字符串通过正则表达式来返回所查询字符串位置 |
| regexp\_like | 字符串通过正则表达式来判断是否符合规则 |
| regexp\_count | 字符串通过正则表达式返回匹配查询字符串出现次数 |
| substrb | 字符串截取函数，返回指定字节数的字符串 |
| replace | 字符串替换函数，替换字符串中指定内容 |
| instrb | 字符串查询函数，返回指定字符串的字节开始位置 |
| lpad | 在字符串左侧添加指定字符串 |
| rpad | 在字符串右侧添加指定字符串 |
| listagg | 将多行数据合并为单个字符串，并用指定的分隔符分隔 |

日期时间&间隔类型函数：

| sysdate | 返回系统当前日期 |
| --- | --- |
| current\_date | 返回当前会话日期 |
| systimestamp | 返回系统当前日期时间，(包括微秒和时区) |
| current\_timestamp | 返回当前会话日期时间，(包括微秒和时区) |
| localtimestamp | 返回会话中的日期和时间 |
| last\_day | 返回指定日期对应月份的最后一天 |
| add\_months | 返回指定日期的间隔月份日期 |
| round | 对输入值进行四舍五入 |
| trunc | 用于截取时间或者数值，返回指定的值 |
| next\_day | 返回从特定日期得到之后的第一个星期几的日期 |
| new\_time | 返回给出时间在c1时区对应c2时区的日期和时间 |
| tz\_offset | 返回给定时区与标准时区的偏移量 |
| months\_between | 返回两个日期之间的月份数 |
| from\_tz | 返回timstamp和timzone组成的timestamp with timezone |
| sys\_extract\_utc | 返回timestamptz转换成UTC时区的本地时间 |
| sessiontimezone | 返回当前会话时区 |
| to\_date | 返回指定字符串转换日期 |
| to\_timestamp | 返回指定字符串转换为timestamp类型的数据 |
| to\_timestamp\_tz | 返回指定字符串转换为timestamptz类型的数据 |
| to\_char | 返回指定参数转换的字符 |
| to\_yminterval | 将符合特定格式的字符串转换成INTERVAL YEAR TO MONTH类型的数值 |
| to\_dsinterval | 返回将符合特定格式的字符串转换成INTERVAL DAY TO SECOND类型的数值 |
| numtoyminterval | 把数字转换成指定的INTERVAL YEAR TO MONTH类型的数值 |
| numtodsinterval | 把数字转换成指定的INTERVAI DAY TO SECOND类型的数值 |

数值类型函数：

| bitand | 返回两个数值型数值在按位进行AND 运算后的结果 |
| --- | --- |
| to\_number | 返回将字符串转换为数值型的数值 |

其他函数：

| to\_clob | 返回字符串转换为clob类型的数值 |
| --- | --- |
| to\_blob | 返回字符串转换为blob类型的数值 |
| hextoraw | 返回字符串表示的十六进制数值转换为RAW类型的数值 |
| uid | 返回当前登录用户的ID号 |
| USERENV | 返回当前用户环境的信息 |
| decode | 返回匹配条件结果 |
| nvl | 用于替换null，返回指定值 |
| nvl2 | 用于判断条件并返回对应结果值 |
| XML函数 | 用于处理XML格式内容 |
| NLSSORT | NLSSORT 函数允许用户为字符串指定一个排序序列，使得字符串能够按照特定的语言、规则以及文化习惯进行排序。 |
| NLS\_COLLATION\_NAME | 用于接受一个排序规则ID作为参数，并返回相应的排序规则名称。 |
| NLS\_COLLATION\_ID | 用于接受一个排序规则名称作为参数，并返回相应的排序规则ID。 |
| sys\_guid | 该函数生成并返回由 16 个字节组成的全局唯一标识符,即生成一个全局唯一序列号。 |

## 示例

### LENGTH、LENGTHB

#### 说明

1. length:在给定编码字符串中的字符数。
2. lengthb:在给定编码字符串中的字节数。

#### 语法

#### 示例

本示例演示创建测试表分别插入中文和英文数据，并通过length和lengthb函数查询字符串长度。

代码示例：

create table char\_tb(types char(20),a char(10 char),b char(12 byte),c varchar2(10 char),d varchar2(12 byte),e integer);

insert into char\_tb values (‘english’,’highgo’,’highgo’,’highgo’,’highgo’,2022);

insert into char\_tb values(‘chinese’,’瀚高’,’瀚高’,’瀚高’,’瀚高’,2022);

\--length

select length(a),length(b),length(c),length(d),length(e) from char\_tb where types =’english’;

select length(a),length(b),length(c),length(d),length(e) from char\_tb where types =’chinese’;

\--lengthb

select lengthb(a),lengthb(b),lengthb(c),lengthb(d) from char\_tb where types=’english’;

select lengthb(a),lengthb(b),lengthb(c),lengthb(d) from char\_tb where types=’chinese’;

### TRIM、LTRIM、RTRIM

#### 说明

1. trim:从字符串的开头/结尾/两端删除最长的只包含 characters（默认是一个空格）的串
2. ltrim:从字符串的开头删除最长的只包含characters（默认是一个空格）的串
3. rtrim:从字符串的结尾删除最长的只包含characters（默认是一个空格）的串

#### 语法

#### 示例

本示例演示通过trim、ltrim、rtrim函数来处理字符串。

代码示例：

\--trim

select trim(‘ hello highgo! ‘) from dual;

\--ltrim

select ltrim(‘ hello highgo! ‘) from dual;

\--rtrim

select rtrim(‘ hello highgo! ‘) from dual;

### REGEXP\_REPLACE、REGEXP\_SUBSTR、REGEXP\_INSTR、REGEXP\_LIKE、REGEXP\_COUNT

#### 说明

1. regexp\_replace:字符串通过正则表达式来进行匹配替换
2. regexp\_substr:字符串通过正则表达式来返回字符串子串
3. regexp\_instr:字符串通过正则表达式来返回所查询字符串位置
4. regexp\_like:字符串通过正则表达式来判断是否符合规则
5. regexp\_count:字符串通过正则表达式返回匹配查询字符串出现次数

#### 语法

#### 示例

本示例演示通过regexp\_replace、regexp\_substr、regexp\_instr、regexp\_like、regexp\_count进行字符串操作。

代码示例：

\--regexp\_replace

select regexp\_replace(‘highgo database ‘, ‘( ){2,}’, ‘ ‘) “regexp\_replace” from dual;

\--regexp\_substr

select regexp\_substr(‘F10-11, Shandong Information and Communication Technology Innovation Industry Base, No. 789, Shuntai North Road, Licheng District, Jinan, Shandong’,’,\[^,\]+,’) “regexp\_substr” from dual;

\--regexp\_instr

select regexp\_instr(‘F10-11, Shandong Information and Communication Technology Innovation Industry Base, No. 789, Shuntai North Road, Licheng District, Jinan, Shandong’, ‘\[^ \]+’, 1, 6) “regexp\_instr” from dual;

\--regexp\_like

select regexp\_like(‘F10-11, Shandong Information and Communication Technology Innovation Industry Base, No. 789, Shuntai North Road, Licheng District, Jinan, Shandong’,’^(\[a-z\]+|\[0-9\]+)$’) from dual;

\--regexp\_count

select regexp\_count(‘F10-11, Shandong Information and Communication Technology Innovation Industry Base, No. 789, Shuntai North Road, Licheng District, Jinan, Shandong’,’\[a-z\]‘

) from dual;

### REPLACE、SUBSTRB、INSTRB

#### 说明

1. replace:字符串替换函数，替换字符串中指定内容
2. substrb:字符串截取函数，返回指定字节数的字符串
3. instrb:字符串查询函数，返回指定字符串的字节开始位置

#### 语法

#### 示例

本示例演示通过replace、substrb、instrb函数来处理字符串。

代码示例：

\--replace

select replace(‘highgo database’, ‘database’,’database system’) from dual;

\--substrb

select substrb(‘highgo database’, 1,6) from dual;

\--instrb

select instrb(‘highgo database’,’highgo’,1) from dual;

### LPAD、RPAD

#### 说明

1. lpad:在字符串左侧添加指定字符串
2. rpad:在字符串右侧添加指定字符串

#### 语法

#### 示例

本示例演示通过lpad、rpad函数来填充字符串。

代码示例：

\--lpad

select lpad(‘ database’,’15’,’highgo’) from dual;

\--rpad

select rpad(‘highgo ‘,’15’,’database’) from dual;

### SYSDATE、CURRENT\_DATE、CURRENT\_TIMESTAMP、SYSTIMESTAMP、LOCALTIMESTAMP

#### 说明

1. sysdate:返回系统当前日期
2. current\_date:返回当前会话日期
3. current\_timestamp:返回当前会话日期时间，(包括微秒和时区)
4. systimestamp:返回系统当前日期时间，(包括微秒和时区)
5. localtimestamp:返回会话中的日期和时间

#### 语法

#### 示例

本示例演示通过sysdate、current\_date、current\_timestamp、systimestamp、localtimestamp获取日期和时间。

代码示例：

\--sysdate

alter session set NLS\_DATE\_FORMAT=’yyyy-mm-dd hh24:mi:ss’;

select sysdate from dual;

\--current\_date

alter session set NLS\_DATE\_FORMAT=’yyyy-mm-dd hh24:mi:ss’;

select current\_date from dual;

\--current\_timestamp

alter session set NLS\_DATE\_FORMAT=’yyyy-mm-dd hh24:mi:ss’;

select CURRENT\_TIMESTAMP FROM DUAL;

\--systimestamp

alter session set NLS\_TIMESTAMP\_FORMAT=’DD-MON-RR HH24:MI:SS tzh:tzm’;

select systimestamp from dual;

\--localstimestamp

alter session set NLS\_TIMESTAMP\_FORMAT=’YYYY-MM-DD HH24:MI:SS’;

select localtimestamp from dual;

### LAST\_DAY、NEXT\_DAY、NEW\_TIME

#### 说明

1. last\_day:返回指定日期对应月份的最后一天
2. next\_day:返回从特定日期得到之后的第一个星期几的日期
3. new\_time:返回给出时间在c1时区对应c2时区的日期和时间

#### 语法

#### 示例

本示例演示通过last\_day、next\_day、new\_time函数来进行日期和时间处理。

代码示例：

\--last\_day

alter session set NLS\_DATE\_FORMAT=’yyyy-mm-dd hh24:mi:ss’;

select last\_day(‘2022-09-22’) from dual;

\--next\_day

alter session set NLS\_DATE\_FORMAT=’yyyy-mm-dd hh24:mi:ss’;

select next\_day(‘2022-09-22’,1) from dual;

\--new\_time

SELECT NEW\_TIME(date’1949-10-1’, ‘AST’, ‘PST’) “New Date and Time” FROM DUAL;

### ADD\_MONTHS

#### 说明

返回指定日期的间隔月份日期

#### 语法

#### 示例

本示例演示通过add\_months函数进行日期处理。

代码示例：

alter session set NLS\_DATE\_FORMAT=’yyyy-mm-dd hh24:mi:ss’;

select add\_months(‘2022-09-22’,1) from dual;

### TZ\_OFFSET

#### 说明

#### 示例

本示例演示通过tz\_offset函数来取得当前时区。

代码示例：

select tz\_offset(‘asia/shanghai’) from dual;

### MONTHS\_BETWEEN

#### 说明

返回两个日期之间的月份数

#### 语法

#### 示例

本示例演示通过months\_between函数来计算月份数。

select months\_between(to\_date(‘2022/12/31 12:13:34 am’,’yyyy/mm/dd hh:mi:ss am’),to\_date(‘2022/9/22 10:13:34 am’,’yyyy/mm/dd hh:mi:ss am’)) from dual;

### FROM\_TZ

#### 说明

返回timstamp和timzone组成的timestamp with timezone

#### 语法

#### 示例

本示例演示通过from\_tz函数将输入日期转换为带时区格式日期形式。

select from\_tz(to\_timestamp(‘2022/9/30 2:13:34 am’,’yyyy/mm/dd hh:mi:ss am’),’Asia/shanghai’) from dual;

### SYS\_EXTRACT\_UTC

#### 说明

返回timestamptz转换成UTC时区的本地时间

#### 语法

#### 示例

本示例演示通过sys\_extract\_utc函数将输入日期转换为utc日期。

select sys\_extract\_utc(to\_timestamp\_tz(‘2022/12/13 10:13:18 -8:00’,’YYYY/MM/DD HH:MI:SS TZH:TZM’)) from dual;

### SESSIONTIMEZONE

#### 说明

返回当前会话时区

#### 语法

#### 示例

本示例演示通过sessiontimezone函数取得会话时区。

select sessiontimezone from dual;

### ROUND

#### 说明

对输入值进行四舍五入

#### 语法

#### 示例

本示例演示通过round函数进行数值或日期的四舍五入处理。

select round(3.1415926,3) from dual;

select round(to\_date(‘2022-9-30’)) from dual;

### TRUNC

#### 说明

用于截取时间或者数值，返回指定的值

#### 语法

#### 示例

本示例演示通过trunc函数进行数值或日期的截取。

SELECT TRUNC(TO\_DATE(‘27-OCT-92’,’DD-MON-YY’), ‘YEAR’)

“New Year” FROM DUAL;

New Year

\-——–

01-JAN-92

SELECT TRUNC(15.79,1) “Truncate” FROM DUAL;

Truncate

\-———

15.7

SELECT TRUNC(15.79,-1) “Truncate” FROM DUAL;

Truncate

\-———

10

### TO\_DATE

#### 说明

返回指定字符串转换日期

#### 语法

#### 示例

本示例演示通过to\_date函数将输入值转换为date类型值。

select round(to\_date(‘2022/09/30 11:13:34 am’,’yyyy/mm/dd hh:mi:ss am’),’MI’) from dual;

### TO\_TIMESTAMP

#### 说明

返回指定字符串转换为timestamp类型的数据

#### 语法

#### 示例

本示例演示通过to\_timestamp函数将输入值转换为timestamp类型值。

select from\_tz(to\_timestamp(‘2022/9/30 2:13:34 am’,’yyyy/mm/dd hh:mi:ss am’),’Asia/shanghai’) from dual;

### TO\_TIMESTAMP\_TZ

#### 说明

返回指定字符串转换为timestamptz类型的数据

#### 语法

#### 示例

本示例演示通过to\_timestamp\_tz函数将输入值转换为timestamp with time zone类型值。

select to\_timestamp\_tz(‘2022/12/13 10:13:18 -8:00’,’YYYY/MM/DD HH:MI:SS TZH:TZM’) from dual;

### TO\_CHAR

#### 说明

返回指定参数转换的字符

#### 语法

#### 示例

本示例演示通过to\_char函数将输入值转换为字符串。

select to\_char(to\_date(‘2022-09-22 2:13:34 am’,’yyyy/mm/dd hh:mi:ss am’)) from dual;

### TO\_YMINTERVAL

#### 说明

将符合特定格式的字符串转换成INTERVAL YEAR TO MONTH类型的数值

#### 语法

#### 示例

本示例演示通过to\_yminterval函数进行日期计算。

select to\_date(‘20220922’,’yyyymmdd’)+to\_yminterval(‘01-06’) from dual;

### TO\_DSINTERVAL

#### 说明

返回将符合特定格式的字符串转换成INTERVAL DAY TO SECOND类型的数值。

#### 语法

#### 示例

本示例演示通过to\_dsinterval函数进行时间计算。

select to\_date(‘20221231235959’,’yyyymmdd hh24:mi:ss’)+to\_dsinterval(‘00 00:00:01’) from dual;

### NUMTOYMINTERVAL

#### 说明

把数字转换成指定的INTERVAL YEAR TO MONTH类型的数值。

#### 语法

#### 示例

本示例演示通过numtoyminterval函数进行日期计算。

select to\_date(‘2022/9/30’,’yyyy/mm/dd’)+numtoyminterval(1,’year’) from dual;

### NUMTODSINTERVAL

#### 说明

把数字转换成指定的INTERVAI DAY TO SECOND类型的数值。

#### 语法

#### 示例

本示例演示通过numtodsinterval函数进行时间计算。

select to\_date(‘2022/10/1’,’yyyy/mm/dd’)+numtodsinterval(-1,’day’) from dual;

### BITAND

#### 说明

返回两个数值型数值在按位进行AND 运算后的结果。

#### 语法

#### 示例

本示例演示通过bitand函数进行按位与运算。

select bitand(3,6) from dual;

### TO\_NUMBER

#### 说明

将expr转换为NUMBER数据类型的值。

expr可以是任意表达式：

1. CHAR、VARCHAR2等类型的字符串；
2. NUMBER、BINARY\_FLOAT或BINARY\_DOUBLE等类型的数字；
3. 空值

#### 语法

#### 示例

本示例演示通过to\_number函数将输入值转为数值。

select to\_number(‘000012134’) from dual;

### TO\_CLOB、TO\_BLOB、HEXTORAW

#### 说明

1. to\_clob:返回字符串转换为clob类型的数值
2. to\_blob:返回字符串转换为blob类型的数值
3. hextoraw:返回字符串表示的十六进制数值转换为RAW类型的数值

#### 语法

#### 示例

本示例演示to\_clob、to\_blob、hextoraw转换数据clob、blob、raw数值

代码示例：

\--to\_clob

select to\_clob(‘highgo database’) from dual;

\--to\_blob

select to\_blob(‘highgo database’) from dual;

\--hextoraw

select hextoraw(‘123BCD’) from dual;

### UID

#### 说明

返回当前登录用户的ID号

#### 语法

#### 示例

本示例演示通过uid获取用户ID。

代码示例：

select uid from dual;

### USERENV

#### 说明

返回当前用户环境的信息

#### 语法

#### 示例

本示例演示通过userenv获取用户环境变量。

支持获取如下环境变量

- ISDBA

如果用户已经被认证为管理员;或者是通过操作系统或口令文件具有管理员特权的，返回“TRUE”，否则返回”FALSE”

- LANG

返回ISO缩写语言名称

- LNAGUAGE

返回数据库当前会话的语言、地域和字符集

- SESSIONID

返回会话标识符。

- SID

返回数据库会话ID

代码示例：

select userenv(‘language’) from dual;

select userenv(‘lang’) from dual;

select userenv(‘isdba’) from dual;

select userenv(‘sid’) from dual;

select userenv(‘sessionid’) from dual;

### DECODE

#### 说明

DECODE函数按顺序将expr与每个搜索值进行比较。如果expr等于某个搜索值，则返回相应的结果。如果没有找到匹配项，则返回默认值。如果省略了默认值，则返回空。

#### 语法

#### 示例

本示例演示通过decode获取对应结果。

代码示例：

SELECT DECODE(1, 1, ‘Southlake’, 3, ‘New Jersey’, 4, ‘Seattle’, ‘Non domestic’) FROM DUAL;

### NVL

#### 说明

NVL允许在查询结果中用一个字符串替换null（显示为空）。如果expr1为null，则NVL返回expr2。如果expr1不为null，则NVL返回expr1。

#### 语法

#### 示例

本示例演示通过nvl将null替换成指定值。

代码示例：

select nvl(null,1) from dual;

### NVL2

#### 说明

NVL2 根据指定表达式是否为null来确定查询返回的值。如果expr1不为null，则NVL2返回expr2。如果expr1为null，则NVL2返回expr3。

#### 语法

#### 示例

本示例演示通过nvl2将符合条件情况下，返回指定值。

代码示例：

select nvl2(null,’ABCD’,’abcd’) from dual;

### XML函数

#### 说明

##### APPENDCHILDXML

APPENDCHILDXML 将用户提供的值附加到目标 XML 作为由 XPath 表达式指示的节点。

- XMLType\_instance 是 XMLType 的一个实例。
- XPath\_string 是一个 Xpath 表达式，指示一个或多个节点，一个或多个子节点将附加到该节点上。 您可以指定带有初始斜杠的绝对 XPath\_string 或通过省略初始斜杠来指定相对 XPath\_string。如果省略初始斜杠，则相对路径的上下文默认为根节点。
- value\_expr 指定一个或多个 XMLType 节点。 它必须解析为字符串。
- 可选的命名空间字符串为 XPath\_string提供命名空间信息。 此参数必须是 VARCHAR2 类型。

代码示例：

DROP table warehouses;

CREATE TABLE warehouses(

WAREHOUSE\_ID NUMBER(3) NOT NULL,

WAREHOUSE\_SPEC XMLTYPE,

WAREHOUSE\_NAME VARCHAR2(35)

);

INSERT INTO warehouses VALUES(1,

‘<?xml version=”1.0”?>

\<Warehouse>

\<Building>Owned\</Building>

\<Area>25000\</Area>

\<Docks>2\</Docks>

\<DockType>Rear load\</DockType>

\<WaterAccess>Y\</WaterAccess>

\<RailAccess>N\</RailAccess>

\<Parking>Street\</Parking>

\<VClearance>10 ft\</VClearance>

\</Warehouse>’, ‘Southlake, Texas’

);

INSERT INTO warehouses VALUES(2,

‘<?xml version=”1.0”?>

\<Warehouse>

\<Building>Rented\</Building>

\<Area>50000\</Area>

\<Docks>1\</Docks>

\<DockType>Side load\</DockType>

\<WaterAccess>Y\</WaterAccess>

\<RailAccess>N\</RailAccess>

\<Parking>Lot\</Parking>

\<VClearance>12 ft\</VClearance>

\</Warehouse>’, ‘San Francisco’);

INSERT INTO warehouses VALUES(3,

‘<?xml version=”1.0”?>

\<Warehouse>

\<Building>Rented\</Building>

\<Area>85700\</Area>

\<DockType>\</DockType>

\<WaterAccess>N\</WaterAccess>

\<RailAccess>N\</RailAccess>

\<Parking>Street\</Parking>

\<VClearance>11.5 ft\</VClearance>

\</Warehouse>’, ‘New Jersey’);

INSERT INTO warehouses VALUES(4,

‘<?xml version=”1.0”?>

\<Warehouse>

\<Building>Owned\</Building>

\<Area>103000\</Area>

\<Docks>3\</Docks>

\<DockType>Side load\</DockType>

\<WaterAccess>N\</WaterAccess>

\<RailAccess>Y\</RailAccess>

\<Parking>Lot\</Parking>

\<VClearance>15 ft\</VClearance>

\</Warehouse>’, ‘Seattle, Washington’);

INSERT INTO warehouses VALUES(5, ‘’, ‘Toronto’);

INSERT INTO warehouses VALUES(6, ‘’, ‘Sydney’);

INSERT INTO warehouses VALUES(7, ‘’, ‘Mexico City’);

INSERT INTO warehouses VALUES(8, ‘’, ‘Beijing’);

INSERT INTO warehouses VALUES(9, ‘’, ‘Bombay’);

SELECT \* FROM warehouses;

UPDATE warehouses

SET warehouse\_spec = APPENDCHILDXML(warehouse\_spec, ‘Warehouse/Building’,XMLType(‘\<Owner>Grandco\</Owner>’))

WHERE EXTRACTVALUE(warehouse\_spec, ‘/Warehouse/Building’) = ‘Rented’;

SELECT warehouse\_id,

warehouse\_name,

EXTRACTVALUE(warehouse\_spec,’/Warehouse/Building/Owner’) “Prop.Owner”

FROM warehouses

WHERE EXISTSNODE(warehouse\_spec,’/Warehouse/Building/Owner’) = 1;

输出：

warehouse\_id | warehouse\_name | Prop.Owner

\-————-+—————-+————

2 | San Francisco | Grandco

3 | New Jersey | Grandco

(2 rows)

##### DELETEXML

DELETEXML 删除目标 XML 中与 XPath 表达式匹配的一个或多个节点。

- XMLType\_instance 是 XMLType 的一个实例。
- XPath\_string 是一个 Xpath 表达式，指示要删除的一个或多个节点。 您可以指定带有初始斜杠的绝对 XPath\_string 或通过省略初始斜杠来指定相对 XPath\_string。 如果省略初始斜线，则相对路径的上下文默认为根节点。 XPath\_string 指定的节点的任何子节点也会被删除。
- 可选的命名空间字符串为 XPath 字符串提供命名空间信息。 此参数必须是 VARCHAR2 类型。

代码示例：

UPDATE warehouses

SET warehouse\_spec=DELETEXML(warehouse\_spec, ‘/Warehouse/Building/Owner’)

WHERE warehouse\_id = 2;

SELECT warehouse\_id, warehouse\_spec

FROM warehouses

WHERE warehouse\_id in (2,3);

输出：

warehouse\_id | warehouse\_spec

\-————-+—————————————————–

3 | \<Warehouse> +

| \<Building>Rented\<Owner>Grandco\</Owner>\</Building>+

| \<Area>85700\</Area> +

| \<DockType/> +

| \<WaterAccess>N\</WaterAccess> +

| \<RailAccess>N\</RailAccess> +

| \<Parking>Street\</Parking> +

| \<VClearance>11.5 ft\</VClearance> +

| \</Warehouse>

2 | \<Warehouse> +

| \<Building>Rented\</Building> +

| \<Area>50000\</Area> +

| \<Docks>1\</Docks> +

| \<DockType>Side load\</DockType> +

| \<WaterAccess>Y\</WaterAccess> +

| \<RailAccess>N\</RailAccess> +

| \<Parking>Lot\</Parking> +

| \<VClearance>12 ft\</VClearance> +

| \</Warehouse>

(2 rows)

##### EXISTSNODE

EXISTSNODE 确定使用指定路径遍历 XML 文档是否会产生任何节点。 它将包含 XML 的 XMLType 实例作为参数文档和一个指定路径的 VARCHAR2 XPath 字符串。 可选的 namespace\_string 必须解析为一个 VARCHAR2 值，该值指定前缀的默认映射或命名空间映射。

namespace\_string 参数默认为根元素的命名空间。 如果引用 Xpath\_string 中的任何子元素，则必须指定 namespace\_string，并且必须在这两个参数中指定“who”前缀。

返回值为 NUMBER：

- 0 如果在对文档应用 XPath 遍历后没有剩余节点
- 1（如果有任何节点）

代码示例：

SELECT warehouse\_id, warehouse\_name

FROM warehouses

WHERE EXISTSNODE(warehouse\_spec, ‘/Warehouse/Docks’) = 1

ORDER BY warehouse\_id;

输出：

warehouse\_id | warehouse\_name

\-————-+———————

1 | Southlake, Texas

2 | San Francisco

4 | Seattle, Washington

(3 rows)

##### EXTRACT (XML)

EXTRACT (XML) 类似于 EXISTSNODE 函数。 它应用一个 VARCHAR2 XPath 字符串并返回一个包含 XML 片段的 XMLType 实例。 您可以指定带有初始斜杠的绝对 XPath\_string 或通过省略初始斜杠的相对 XPath\_string。 如果省略初始斜线，则相对路径的上下文默认为根节点。 如果您正在处理的 XML 使用命名空间前缀，则需要可选的命名空间字符串。 此参数必须解析为 VARCHAR2 值，该值指定前缀的默认映射或命名空间映射。

代码示例：

SELECT warehouse\_name,

EXTRACT(warehouse\_spec, ‘/Warehouse/Docks’) “Number of Docks”

FROM warehouses

WHERE warehouse\_spec IS NOT NULL

ORDER BY warehouse\_name;

输出：

warehouse\_name | Number of Docks

\-——————–+——————

New Jersey |

San Francisco | \<Docks>1\</Docks>

Seattle, Washington | \<Docks>3\</Docks>

Southlake, Texas | \<Docks>2\</Docks>

(4 rows)

##### EXTRACTVALUE

EXTRACTVALUE函数把一个XMLType实例和一个XPath表达式作为参数表达式，并返回结果节点的一个标量值。该结果必须是一个单一的 节点，并且是一个文本节点、属性或元素。如果结果是一个元素，那么 该元素必须有一个单一的文本节点作为它的子节点，而这个值就是函数返回的就是这个值。你可以指定一个带有初始斜线的绝对XPath\_string或一个 相对的XPath\_string，省略最初的斜线。如果你省略了最初的斜线，那么 相对路径的上下文默认为根节点。

如果指定的XPath指向一个有一个以上子节点的节点，或者指向的节点 有一个非文本节点的子节点，那么会返回一个错误。可选的namespace\_string必须解析为一个VARCHAR2值，指定一个默认的映射或前缀的默认映射或命名空间映射。

代码示例：

SELECT warehouse\_name, EXTRACTVALUE(e.warehouse\_spec, ‘/Warehouse/Docks’) “Docks”

FROM warehouses e

WHERE warehouse\_spec IS NOT NULL

ORDER BY warehouse\_name;

输出：

warehouse\_name | Docks

\-——————–+——-

New Jersey |

San Francisco | 1

Seattle, Washington | 3

Southlake, Texas | 2

(4 rows)

##### INSERTCHILDXMLAFTER

INSERTXMLCHILDAFTER插入一个或多个集合元素作为目标父元素的子元素。每个目标元素的插入都紧随在指定的 现有的集合元素之后。作为插入目标的现有XML文档可以是基于模式的，也可以是非模式的。插入的现有XML文档可以是基于模式的，也可以是非基于模式的。

- XMLType\_instance标识了作为插入目标的XML数据。
- XPath\_string定位目标数据中的父元素；子数据被插入到每个父元素下面。在每个父元素下面。
- child\_expr是一个相对的XPath 1.0表达式，定位现有的子元素，它将在插入的子数据之前。将在插入的子数据之前。它必须命名一个元素的子元素 表示的元素的一个子元素，并且它可以包括一个谓词。
- value\_expr是要插入的XMLType子元素数据。这个参数中的每个顶层元素 节点必须具有与child\_expr所指示的元素相同的数据类型。child\_expr指示的元素具有相同的数据类型。
- 可选的namespace\_string指定了父元素的命名空间。现有的子元素和要插入的子元素XML数据的命名空间。

代码示例：

UPDATE warehouses

SET warehouse\_spec = INSERTCHILDXMLAFTER(warehouse\_spec, ‘/Warehouse/Building’,

‘Owner\[1\]‘, XMLType(‘\<Owner>ThirdOwner\</Owner>’))

WHERE warehouse\_id = 3;

SELECT warehouse\_name,

EXTRACT(warehouse\_spec, ‘/Warehouse/Building/Owner’) “Owners”

FROM warehouses

WHERE warehouse\_id = 3;

输出：

warehouse\_name | Owners

\-—————+—————————

New Jersey | \<Owner>Grandco\</Owner> +

| \<Owner>ThirdOwner\</Owner>

(1 row)

##### INSERTCHILDXMLBEFORE

INSERTXMLCHILDBEFORE将一个或多个集合元素作为目标父元素的子元素插入父元素的子元素。每个目标的插入都紧接在一个指定的 现有的集合元素之前。现有的XML文档是插入的目标 插入的现有XML文档可以是基于模式的，也可以是非基于模式的。

- XMLType\_instance标识了作为插入目标的XML数据。
- XPath\_string定位目标数据中的父元素；子数据被插入到每个父元素下面。在每个父元素下面。
- child\_expr是一个相对的XPath 1.0表达式，用于定位现有的子元素，它将跟随插入的子数据。将跟随插入的子数据。它必须命名一个元素的子元素 表示的元素的一个子元素，并且它可以包括一个谓词。
- value\_expr是要插入的XMLType子元素数据。这个参数中的每个顶层元素 节点必须具有与child\_expr所指示的元素相同的数据类型。child\_expr指示的元素具有相同的数据类型。
- 可选的namespace\_string指定了父元素的命名空间。现有的子元素和要插入的子元素XML数据的命名空间。

代码示例：

UPDATE warehouses

SET warehouse\_spec = INSERTCHILDXMLBEFORE(warehouse\_spec, ‘/Warehouse/Building’,

‘Owner\[2\]‘, XMLType(‘\<Owner>ThirdOwner\</Owner>’))

WHERE warehouse\_id = 3;

SELECT warehouse\_name,

EXTRACT(warehouse\_spec, ‘/Warehouse/Building/Owner’) “Owners”

FROM warehouses

WHERE warehouse\_id = 3;

输出：

warehouse\_name | Owners

\-—————+—————————

New Jersey | \<Owner>Grandco\</Owner> +

| \<Owner>ThirdOwner\</Owner>+

| \<Owner>ThirdOwner\</Owner>

(1 row)

##### INSERTCHILDXML

INSERTCHILDXML 将用户提供的值插入到目标 XML 中由 XPath 表达式指示的节点处。

- XMLType\_instance 是 XMLType 的一个实例。
- XPath\_string 是一个 Xpath 表达式，指示一个或多个节点，将插入一个或多个子节点。 您可以指定一个绝对的 XPath\_带有初始斜杠的字符串或通过省略初始斜杠的相对 XPath\_string。如果省略初始斜杠，则相对路径的上下文默认为根节点
- child\_expr 指定要插入的一个或多个元素或属性节点。
- value\_expr 是 XMLType 的一个片段，它指定要插入的一个或多个注释。 它必须解析为字符串。
- 可选的命名空间字符串为 XPath 字符串提供命名空间信息。 此参数必须是 VARCHAR2 类型。

代码示例：

UPDATE warehouses

SET warehouse\_spec = INSERTCHILDXML(warehouse\_spec, ‘/Warehouse/Building’,

‘Owner’, XMLType(‘\<Owner>LesserCo\</Owner>’))

WHERE warehouse\_id = 3;

SELECT warehouse\_spec

FROM warehouses

WHERE warehouse\_id = 3;

输出：

warehouse\_spec

\-—————————————————————————————————————————–

\<Warehouse> +

\<Building>Rented\<Owner>Grandco\</Owner>\<Owner>ThirdOwner\</Owner>\<Owner>ThirdOwner\</Owner>\<Owner>LesserCo\</Owner>\</Building>+

\<Area>85700\</Area> +

\<DockType/> +

\<WaterAccess>N\</WaterAccess> +

\<RailAccess>N\</RailAccess> +

\<Parking>Street\</Parking> +

\<VClearance>11.5 ft\</VClearance> +

\</Warehouse>

(1 row)

##### INSERTXMLAFTER

INSERTXMLAFTER在一个非属性节点的目标节点之后立即插入一个或多个任意类型的节点。不是属性节点。作为插入的目标的XML文档可以是 可以是基于模式的或非模式的。这个函数类似于 insertXMLbefore, 但它是在目标节点之后而不是之前插入的。

- XMLType\_instance指定了插入的目标节点。
- XPath\_string是一个XPath 1.0表达式，它在目标节点中定位了0个或更多的任何类型的节点，除了属性节点。除属性节点外，任何类型的节点。XML数据会紧接着插入到 紧接着这些节点插入；也就是说，每一个指定的节点都会成为一个节点的前一个在value\_expr中指定的节点的兄弟姐妹节点。
- value\_expr是要插入的XML数据。你可以指定一个或多个任何类型的节点。任何类型的节点。节点的顺序在插入后会被保留下来。
- 可选的namespace\_string是目标节点的命名空间。

代码示例：

UPDATE warehouses

SET warehouse\_spec = INSERTXMLAFTER(warehouse\_spec,

‘/Warehouse/Building/Owner\[1\]‘, XMLType(‘\<Owner>SecondOwner\</Owner>’))

WHERE warehouse\_id = 3;

SELECT warehouse\_name,

EXTRACT(warehouse\_spec, ‘/Warehouse/Building/Owner’) “Owners”

FROM warehouses

WHERE warehouse\_id = 3;

输出：

warehouse\_name | Owners

\-—————+—————————-

New Jersey | \<Owner>Grandco\</Owner> +

| \<Owner>SecondOwner\</Owner>+

| \<Owner>ThirdOwner\</Owner> +

| \<Owner>ThirdOwner\</Owner> +

| \<Owner>LesserCo\</Owner>

(1 row)

##### INSERTXMLBEFORE

INSERTXMLBEFORE在目标XML中插入一个用户提供的值，在XPath表达式指示的节点之前。这个函数与INSERTXMLAFTER相似，但是 它在目标节点之前而不是之后插入。将此函数与INSERTCHILDXML 对比。

- XMLType\_instance是XMLType的一个实例。
- XPath\_string是一个Xpath表达式，表示一个或多个节点，一个或多个子节点将被插入其中。一个或多个子节点被插入其中。你可以指定一个绝对的XPath\_string 或者通过省略初始斜线指定一个相对的XPath\_string。如果你 省略初始斜线，那么相对路径的上下文默认为根节点。
- value\_expr是XMLType的一个片段，它定义了一个或多个被插入的节点以及它们在父节点中的位置。插入的一个或多个节点以及它们在父节点中的位置。它必须解析为一个字符串。
- 可选的namespace\_string为XPath\_字符串提供命名空间信息。 字符串提供命名空间信息。这个参数必须是VARCHAR2类型。

代码示例：

UPDATE warehouses

SET warehouse\_spec = INSERTXMLBEFORE(warehouse\_spec,

‘/Warehouse/Building/Owner\[2\]‘, XMLType(‘\<Owner>ThirdOwner\</Owner>’))

WHERE warehouse\_id = 3;

SELECT warehouse\_name,

EXTRACT(warehouse\_spec, ‘/Warehouse/Building/Owner’) “Owners”

FROM warehouses

WHERE warehouse\_id = 3;

输出：

warehouse\_name | Owners

\-—————+—————————-

New Jersey | \<Owner>Grandco\</Owner> +

| \<Owner>ThirdOwner\</Owner> +

| \<Owner>SecondOwner\</Owner>+

| \<Owner>ThirdOwner\</Owner> +

| \<Owner>ThirdOwner\</Owner> +

| \<Owner>LesserCo\</Owner>

(1 row)

##### UPDATEXML

UPDATEXML 将 XMLType 实例和 XPath 值对作为参数，并返回具有更新值的 XMLType 实例。如果 XPath\_string 是 XML 元素，则对应的 value\_expr 必须是 XMLType 实例。如果 XPath\_string 是属性或文本节点，则 value\_expr 可以是任何标量数据类型。您可以通过省略初始斜杠来指定带有初始斜杠的绝对 XPath\_string 或相对 XPath\_string。如果省略初始斜线，则相对路径的上下文默认为根节点。

每个 XPath\_string 的目标的数据类型与其对应的 value\_expr 必须匹配。 可选的 namespace\_string 必须解析为 VARCHAR2 值为前缀指定默认映射或命名空间映射，数据库在评估 XPath 表达式时使用它。

如果您将 XML 元素更新为 null，则将删除该元素的属性和子元素，并且该元素变为空。 如果将某个元素的文本节点更新为 null，会删除该元素的文本值，以及该元素本身仍然是空的。

在大多数情况下，此函数在内存中具体化 XML 文档并更新值。 但是，UPDATEXML 针对对象关系列上的 UPDATE 语句进行了优化，以便函数直接更新列中的值。 此优化需要以下条件：

■ XMLType\_instance 必须与UPDATE … SET 子句中的列相同。

■ XPath\_string 必须解析为标量内容。

代码示例：

UPDATE warehouses

SET warehouse\_spec=UPDATEXML(warehouse\_spec,’/Warehouse/Building/Owner\[2\]‘,XMLType(‘\<Owner>TestOwner\</Owner>’))

WHERE warehouse\_id=3;

SELECT warehouse\_name,

EXTRACT(warehouse\_spec, ‘/Warehouse/Building/Owner’) “Owners”

FROM warehouses

WHERE warehouse\_id = 3;

输出：

warehouse\_name | Owners

\-—————+—————————-

New Jersey | \<Owner>Grandco\</Owner> +

| \<Owner>TestOwner\</Owner> +

| \<Owner>SecondOwner\</Owner>+

| \<Owner>ThirdOwner\</Owner> +

| \<Owner>ThirdOwner\</Owner> +

| \<Owner>LesserCo\</Owner>

(1 row)

### NLSSORT

#### 说明

NLSSORT 函数允许用户为字符串指定一个排序序列，使得字符串能够按照特定的语言、规则以及文化习惯进行排序。它常用于查询中进行结果集的排序，尤其是当字符串包含非 ASCII 字符时（如中文、英文、阿拉伯文等）。

#### 语法

char:必需参数。它可以是CHAR、VARCHAR2、NCHAR、NVARCHAR2中的任何一种数据类型。CHAR类型计算时去除尾部空格。

nlsparam:可选的。目前仅支持’ NLS\_SORT = collation’ 形式，其中 collation 是排序规则的名称，简体中文相关排序列表如下:

| **collation** | **排序规则** |
| --- | --- |
| BINARY | 二进制 |
| BINARY\_AI | 二进制，重音不敏感 |
| BINARY\_CI | 二进制，大小写不敏感 |
| SCHINSE\_PINYIN\_M | 拼音 |
| SCHINESE\_STROKE\_M | 笔画 |
| SCHINESE\_RADICAL\_M | 偏旁部首 |
| GENERIC\_M\_CI | 重音敏感、大小写不敏感。      仅支持纯英文不区分大小写排序(og) |
| UCA0700\_SCHINESE | 拼音 |
| UCA0700\_SCHINESE1 | 偏旁部首 |
| UCA0700\_SCHINESE2 | 笔画 |

#### 示例

CREATE TABLE people (

id NUMBER,

name NVARCHAR2(100)

);

INSERT INTO people (id, name) VALUES (1, ‘李明’);

INSERT INTO people (id, name) VALUES (2, ‘张伟’);

INSERT INTO people (id, name) VALUES (3, ‘王芳’);

INSERT INTO people (id, name) VALUES (4, ‘赵鹏’);

INSERT INTO people (id, name) VALUES (5, ‘陈刚’);

SELECT id, name

FROM people

ORDER BY NLSSORT(name, ‘nls\_sort=schinese\_pinyin\_m’);

### NLS\_COLLATION\_ID

#### 说明

用于接受一个排序规则名称作为参数，并返回相应的排序规则ID。

#### 语法

#### 示例

SELECT NLS\_COLLATION\_ID(‘BINARY\_CI’)

FROM DUAL;

nls\_collation\_id

\-—————–

147455

(1 row)

### NLS\_COLLATION\_NAME

#### 说明

用于接受一个排序规则ID以及是否简写作为参数，并返回相应的排序规则名称。

#### 语法

#### 示例

SELECT NLS\_COLLATION\_NAME(208941,’L’)

FROM DUAL;

nls\_collation\_name

\-——————-

UCA0700\_SCHINESE\_S4\_VS\_BN\_NY\_EN\_FN\_HN\_DN\_MN

(1 row)

SELECT NLS\_COLLATION\_NAME(208941,’s’)

FROM DUAL;

nls\_collation\_name

\-——————-

UCA0700\_SCHINESE

(1 row)

SELECT NLS\_COLLATION\_NAME(208941)

FROM DUAL;

nls\_collation\_name

\-——————-

UCA0700\_SCHINESE\_S4\_VS\_BN\_NY\_EN\_FN\_HN\_DN\_MN

(1 row)

具体排序规则参照下表：

| **collation** | **Collation ID** |
| --- | --- |
| BINARY | 16383 |
| BINARY\_AI | 81919 |
| BINARY\_CI | 147455 |
| SCHINSE\_PINYIN\_M | 4160 |
| SCHINESE\_STROKE\_M | 4161 |
| SCHINESE\_RADICAL\_M | 4163 |
| GENERIC\_M\_CI | 135169 |
| UCA0700\_SCHINESE | 208941 |
| UCA0700\_SCHINESE1 | 208942 |
| UCA0700\_SCHINESE2 | 208943 |
| USING\_NLS\_COMP | 16382 |
| USING\_NLS\_SORT | 16381 |
| USING\_NLS\_SORT\_CI | 16380 |
| USING\_NLS\_SORT\_AI | 16379 |
| USING\_NLS\_SORT\_CS | 16378 |
| UCA0700\_SCHINESE\_S4\_VS\_BN\_NY\_EN\_FN\_HN\_DN\_MN | 208941 |
| UCA0700\_SCHINESE1\_S4\_VS\_BN\_NY\_EN\_FN\_HN\_DN\_MN | 208942 |
| UCA0700\_SCHINESE2\_S4\_VS\_BN\_NY\_EN\_FN\_HN\_DN\_MN | 208943 |

### SYS\_GUID

#### 说明

该函数生成并返回由 16 个字节组成的全局唯一标识符,即生成一个全局唯一序列号。

#### 示例

本示例演示通过sys\_guid生成全局唯一标识符。

代码示例：

select sys\_guid() from dual;

### LISTAGG

该功能在V9.0.5及以后的版本中支持。

#### 说明

LISTAGG 函数是一个强大的字符串聚合函数，用于将多行数据合并为单个字符串，并用指定的分隔符分隔。

#### 语法

listagg



listagg\_overflow\_clause（仅语法兼容）



order\_by\_clause



query\_partition\_clause



说明：

- ALL

ALL 关键字是可选的。

- DISTINCT

从列表中删除重复值。暂不支持与OVER一起使用。

- measure\_expr

度量列，可以是任何表达式。度量列中的空值将被忽略。

- delimiter

指定了用于分隔度量列值的字符串。此子句是可选的，默认为 NULL 。

- listagg\_overflow\_clause（仅语法兼容）

该子句控制当返回值超过返回数据类型的最大长度时函数的行为。

如果指定ON OVERFLOW ERROR 子句，则函数返回 错误。默认设置。

如果指定ON OVERFLOW TRUNCATE 子句，则函数返回截断的度量值列表。

- WITHIN GROUP

指定聚合字符串内元素的排序顺序。暂不支持与OVER一起使用。

- truncation\_indicator

指定要追加到截断的度量值列表中的字符串。如果省略此子句，则截断指示符为省略号（ … ）。

- order\_by\_clause

确定连接值返回的顺序。

如果指定了 order\_by\_clause ，也必须指定 WITHIN GROUP ，反之亦然。这两个子句必须一起指定或不指定。

- OVER

指示LISTAGG函数作为分析函数（窗口函数）来使用，而不是作为聚合函数。该子句暂不支持与DISTINCT和WITHIN GROUP一起使用。

- query\_partition\_clause

使用 PARTITION BY 子句将查询结果集按一个或多个 value\_expr 分组。如果省略此子句，则函数将查询结果集中的所有行视为一个组。

要在listagg中使用 query\_partition\_clause ，请使用不带括号的语法分支。要在模型查询（在 model\_column\_clauses ）或分区外连接（在 outer\_join\_clause ）中使用此子句，请使用带括号的语法分支。

#### 示例

插入测试数据：

```
-- 创建部门表
CREATE TABLE departments (
  dept_id    NUMBER(4) PRIMARY KEY,
  dept_name   VARCHAR2(50) NOT NULL,
  location   VARCHAR2(50)
);

-- 插入部门数据
INSERT INTO departments VALUES (10, '技术部', '北京总部');
INSERT INTO departments VALUES (20, '销售部', '上海分公司');
INSERT INTO departments VALUES (30, '人力资源部', '北京总部');
INSERT INTO departments VALUES (40, '财务部', '北京总部');
INSERT INTO departments VALUES (50, '市场部', '广州分公司');

-- 创建员工表
CREATE TABLE employees (
  employee_id  NUMBER(6) PRIMARY KEY,
  emp_name    VARCHAR2(50) NOT NULL,
  email     VARCHAR2(100),
  phone     VARCHAR2(20),
  dept_id    NUMBER(4) REFERENCES departments(dept_id),
  position    VARCHAR2(50),
  salary     NUMBER(10,2),
  hire_date   DATE
);

-- 插入员工数据
INSERT INTO employees VALUES (1001, '张明', 'zhangming@company.com', '13800138001', 10, 'Java开发工程师', 15000, DATE '2020-03-15');
INSERT INTO employees VALUES (1002, '李芳', 'lifang@company.com', '13800138002', 10, '前端开发工程师', 14000, DATE '2019-07-20');
INSERT INTO employees VALUES (1003, '王强', 'wangqiang@company.com', '13800138003', 10, '架构师', 25000, DATE '2018-05-10');
INSERT INTO employees VALUES (1004, '刘婷', 'liuting@company.com', '13800138004', 10, '测试工程师', 12000, DATE '2021-01-08');

INSERT INTO employees VALUES (2001, '陈磊', 'chenlei@company.com', '13800138005', 20, '销售经理', 18000, DATE '2019-11-25');
INSERT INTO employees VALUES (2002, '杨雪', 'yangxue@company.com', '13800138006', 20, '客户经理', 16000, DATE '2020-08-12');
INSERT INTO employees VALUES (2003, '赵刚', 'zhaogang@company.com', '13800138007', 20, '销售代表', 13000, DATE '2021-03-30');

INSERT INTO employees VALUES (3001, '周敏', 'zhoumin@company.com', '13800138008', 30, '招聘专员', 11000, DATE '2020-06-18');
INSERT INTO employees VALUES (3002, '吴浩', 'wuhao@company.com', '13800138009', 30, '培训经理', 17000, DATE '2019-09-05');

INSERT INTO employees VALUES (4001, '郑琳', 'zhenglin@company.com', '13800138010', 40, '财务主管', 20000, DATE '2018-12-01');
INSERT INTO employees VALUES (4002, '孙伟', 'sunwei@company.com', '13800138011', 40, '会计', 13000, DATE '2020-04-22');

INSERT INTO employees VALUES (5001, '钱芳', 'qianfang@company.com', '13800138012', 50, '市场专员', 14000, DATE '2020-07-14');
INSERT INTO employees VALUES (5002, '马超', 'machao@company.com', '13800138013', 50, '品牌经理', 19000, DATE '2019-04-03');

-- 创建项目表
CREATE TABLE projects (
  project_id   NUMBER(6) PRIMARY KEY,
  project_name  VARCHAR2(100) NOT NULL,
  dept_id     NUMBER(4) REFERENCES departments(dept_id),
  start_date   DATE,
  end_date    DATE,
  status     VARCHAR2(20)
); 

-- 插入项目数据
INSERT INTO projects VALUES (1, '客户关系管理系统开发', 10, DATE '2023-01-10', DATE '2023-06-30', '进行中');
INSERT INTO projects VALUES (2, '电商平台重构项目', 10, DATE '2023-02-15', DATE '2023-08-20', '进行中');
INSERT INTO projects VALUES (3, '华东区域市场推广', 20, DATE '2023-03-01', DATE '2023-05-31', '已完成');
INSERT INTO projects VALUES (4, '新员工培训体系建设', 30, DATE '2023-01-20', DATE '2023-04-15', '已完成');
INSERT INTO projects VALUES (5, '财务系统升级', 40, DATE '2023-04-01', DATE '2023-09-30', '进行中');
```

##### 示例1

单集聚合 - 公司所有员工名单

```
SELECT '公司全体员工: ' || LISTAGG(emp_name, '、') WITHIN GROUP (ORDER BY hire_date) AS all_employees
FROM employees;
```

结果：

```
公司全体员工: 王强、郑琳、马超、李芳、吴浩、陈磊、张明、孙伟、周敏、钱芳、杨雪、刘婷、赵刚
```

##### 示例2

组集聚合 - 各部门员工名单

```
SELECT 
  d.dept_name AS 部门名称,
  LISTAGG(e.emp_name || '(' || e.position || ')', '、') 
    WITHIN GROUP (ORDER BY e.hire_date) AS 部门成员
FROM departments d
JOIN employees e ON d.dept_id = e.dept_id
GROUP BY d.dept_name
ORDER BY d.dept_name;
```

结果：

```
部门名称   部门成员
----------- ---------------------------------------------------------
 人力资源部 | 吴浩(培训经理)、周敏(招聘专员)
 市场部   | 马超(品牌经理)、钱芳(市场专员)
 技术部   | 王强(架构师)、李芳(前端开发工程师)、张明(Java开发工程师)、刘婷(测试工程师)
 财务部   | 郑琳(财务主管)、孙伟(会计)
 销售部   | 陈磊(销售经理)、杨雪(客户经理)、赵刚(销售代表)
```

##### 示例3

分析函数-员工明细带部门同事信息

```
SELECT 
  e.emp_name AS 员工姓名,
  e.position AS 职位,
  d.dept_name AS 部门,
  LISTAGG(e.emp_name, '、') 
   OVER (PARTITION BY e.dept_id) AS 同部门同事
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
ORDER BY d.dept_name, e.hire_date;
```

预期结果：

```
员工姓名 |    职位    |   部门   |    同部门同事    
----------+----------------+------------+------------------------
 吴浩   | 培训经理    | 人力资源部 | 周敏、吴浩
 周敏   | 招聘专员    | 人力资源部 | 周敏、吴浩
 马超   | 品牌经理    | 市场部   | 钱芳、马超
 钱芳   | 市场专员    | 市场部   | 钱芳、马超
 王强   | 架构师     | 技术部   | 张明、李芳、王强、刘婷
 李芳   | 前端开发工程师 | 技术部   | 张明、李芳、王强、刘婷
 张明   | Java开发工程师 | 技术部   | 张明、李芳、王强、刘婷
 刘婷   | 测试工程师   | 技术部   | 张明、李芳、王强、刘婷
 郑琳   | 财务主管    | 财务部   | 郑琳、孙伟
 孙伟   | 会计      | 财务部   | 郑琳、孙伟
 陈磊   | 销售经理    | 销售部   | 陈磊、杨雪、赵刚
 杨雪   | 客户经理    | 销售部   | 陈磊、杨雪、赵刚
 赵刚   | 销售代表    | 销售部   | 陈磊、杨雪、赵刚
(13 行记录)
```

##### 示例4

多表连接复杂示例– 各部门负责的项目列表

```
SELECT 
  d.dept_name AS 部门,
  LISTAGG(p.project_name || '[' || p.status || ']', ' | ') 
    WITHIN GROUP (ORDER BY p.start_date) AS 负责项目
FROM departments d
LEFT JOIN projects p ON d.dept_id = p.dept_id
GROUP BY d.dept_name
ORDER BY d.dept_name;
```

预期结果：

```
部门    负责项目
---------- ---------------------------------------------------------
人力资源部 | 新员工培训体系建设[已完成]
市场部   | []
技术部   | 客户关系管理系统开发[进行中] | 电商平台重构项目[进行中]
财务部   | 财务系统升级[进行中]
销售部   | 华东区域市场推广[已完成]
```