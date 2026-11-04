---
title: "内置函数"
book: "MySQL兼容性"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/compatibility/compMySql5.html"
tags:
  - highgo
  - highgo-v9
  - compatibility-mysql
---

## 内置函数

## 概述

V9.0.4实现以下时间日期函数的兼容：

| 函数类型 | 函数名称 | 说明 |
| --- | --- | --- |
| 时间日期函数 | DAY() | DAYOFMONTH()的同义词 |
| DAYOFMONTH() | 返回月份中的天数（0~31） |  |
| DAYOFWEEK() | 返回参数的星期几索引 |  |
| DAYOFYEAR() | 返回年份中的天数（1-366） |  |
| QUARTER() | 从日期参数中返回季度 |  |
| HOUR() | 提取小时 |  |
| MICROSECOND() | 返回参数中的微秒数 |  |
| MINUTE() | 返回参数中的分钟数 |  |
| SECOND() | 返回秒数（0-59） |  |
| WEEKDAY() | 返回星期几的索引 |  |
| WEEKOFYEAR() | 返回日期的日历周数（1-53） |  |
| YEAR() | 返回年份 |  |
| CURDATE() | 返回当前日期 |  |
| CURRENT\_DATE(), CURRENT\_DATE | CURDATE()的同义词 |  |
| CURTIME() | 返回当前时间 |  |
| CURRENT\_TIME(), CURRENT\_TIME | CURTIME()的同义词 |  |
| NOW() | 返回当前日期和时间 |  |
| CURRENT\_TIMESTAMP | NOW()的同义词 |  |
| LOCALTIME | NOW()的同义词 |  |
| LOCALTIMESTAMP | NOW()的同义词 |  |
| SYSDATE() | 返回函数执行时的时间 |  |
| MAKEDATE() | 根据年份和年中的天数创建日期 |  |
| MAKETIME() | 根据小时、分钟、秒创建时间 |  |
| PERIOD\_ADD() | 向年月添加一个时期 |  |
| PERIOD\_DIFF() | 返回两个时期之间的月份数 |  |
| SEC\_TO\_TIME() | 将秒转换为 ‘hh:mm:ss’ 格式 |  |
| SUBTIME() | 从给定的时间或日期中减去指定的时间间隔 |  |
| TIMEDIFF() | 计算两个时间之间的差值 |  |
| TIME() | 提取传入表达式的时间部分 |  |
| TIMESTAMP() | 当只有一个参数时，此函数返回日期或日期时间表达式；当有两个参数时，返回两个参数的和。 |  |
| TIMESTAMPADD() | 向日期时间表达式添加一个时间间隔 |  |

V9.0.5增加以下函数的兼容：

| 函数类型 | 函数名称 | 说明 |
| --- | --- | --- |
| 时间日期函数 | TO\_DAYS() | 返回转换为天数的日期参数 |
| TO\_SECONDS() | 返回转换为自公元0年以来的秒数的日期或日期时间参数 |  |
| UNIX\_TIMESTAMP() | 返回Unix时间戳 |  |
| UTC\_DATE() | 返回当前UTC日期 |  |
| UTC\_TIME() | 返回当前UTC时间 |  |
| UTC\_TIMESTAMP() | 返回当前UTC日期和时间 |  |
| DAYNAME() | 返回星期几的名称 |  |
| MONTHNAME() | 返回月份的名称 |  |
| TIME\_TO\_SEC() | 返回转换为秒数的参数 |  |
| MONTH() | 从传入的日期中提取月份 |  |
| DATE() | 从日期或日期时间表达式中提取日期部分 |  |
| WEEK() | 返回星期数 |  |
| YEARWEEK() | 从某个日期中提取出年份和对应的周数 |  |
| DATEDIFF() | 计算两个日期之间的差距 |  |
| FROM\_DAYS() | 将天数转换为日期 |  |
| CONVERT\_TZ() | 从一个时区转换到另一个时区 |  |
| GET\_FORMAT() | 返回日期格式字符串 |  |
| TIMESTAMPDIFF() | 返回两个日期时间表达式的差异，并使用指定的单位 |  |
| STR\_TO\_DATE() | 将字符串转换为日期 |  |
| 字符串函数和操作符 | LOCATE() | 返回子字符串第一次出现的位置 |
| LCASE() | LOWER()的同义词 |  |
| UCASE() | UPPER()的同义词 |  |
| INSERT() | 在指定位置插入子字符串，直到指定字符数 |  |
| BIN() | 返回包含数字二进制表示的字符串 |  |
| CHAR() | 返回传入整数的字符 |  |
| ELT() | 返回指定索引位置的字符串 |  |
| FIELD() | 返回第一个参数在随后的参数中的索引（位置） |  |
| FIND\_IN\_SET() | 返回第一个参数在第二个参数内的索引（位置） |  |
| HEX() | 十六进制表示十进制或字符串值 |  |
| SPACE() | 返回指定数量空格的字符串 |  |
| SOUNDEX() | 返回一个Soundex字符串 |  |
| EXPORT\_SET() | 返回一个字符串，对于值中每个设置的位，得到一个开字符串，对于每个未设置的位，得到一个关字符串 |  |
| ORD() | 返回参数的最左字符的字符代码 |  |
| SUBSTRING\_INDEX() | 从字符串中提取子字符串，在指定的分隔符的指定次数之前 |  |
| FROM\_BASE64() | 解码Base64编码的字符串并返回结果 |  |
| TO\_BASE64() | 返回转换为Base64字符串的参数 |  |
| LENGTH() | 返回字符串的字节长度 |  |
| BIT\_LENGTH() | 返回参数的位长度 |  |
| OCTET\_LENGTH() | LENGTH()的同义词 |  |
| LEFT() | 返回最左边的指定字符数 |  |
| RIGHT() | 返回指定的右边字符数 |  |
| REPLACE() | 替换指定字符串 |  |
| UNHEX() | 返回包含数字十六进制表示的字符串 |  |
| WEIGHT\_STRING() | 返回字符串的权重字符串 |  |
| STRCMP() | 比较两个字符串 |  |
| 流控制函数 | IF() | IF/else结构 |
| IFNULL() | NULL IF/else结构 |  |
| 比较函数和操作符 | ISNULL() | 测试参数是否为NULL |
| INTERVAL() | 返回小于第一个参数的参数的索引 |  |
| 数学函数 | CONV() | 在不同的数字基数之间转换数字 |
| 其他函数 | INET\_ATON() | 返回IP地址的数字值 |
| INET\_NTOA() | 从数字值返回IP地址 |  |
| INET6\_ATON() | 返回IPv6地址的数字值 |  |
| INET6\_NTOA() | 从数字值返回IPv6地址 |  |

## 示例

V9.0.4实现的函数：

SELECT DAY('2007-02-03');

SELECT DAYOFMONTH('2007-02-03');

SELECT DAYOFWEEK('2007-02-03');

SELECT DAYOFYEAR('2007-02-03');

SELECT QUARTER('2008-04-01');

SELECT HOUR('10:05:03');

SELECT MICROSECOND('12:00:00.123456');

SELECT MINUTE('2008-02-03 10:05:03');

SELECT SECOND('10:05:03');

SELECT WEEKDAY('2008-02-03 22:23:00');

SELECT WEEKOFYEAR('2008-02-20');

SELECT YEAR('1987-01-01');

SELECT CURDATE();

SELECT CURRENT\_DATE();

SELECT CURRENT\_DATE;

SELECT CURTIME();

SELECT CURRENT\_TIME();

SELECT CURRENT\_TIME;

SELECT NOW();

SELECT CURRENT\_TIMESTAMP;

SELECT LOCALTIME;

SELECT LOCALTIMESTAMP;

SELECT SYSDATE();

SELECT MAKEDATE(2011,31), MAKEDATE(2011,32);

SELECT MAKETIME(12,15,30);

SELECT PERIOD\_ADD(200801,2);

SELECT PERIOD\_DIFF(200802,200703);

SELECT SEC\_TO\_TIME(2378);

SELECT SUBTIME('2007-12-31 23:59:59.999999','1 1:1:1.000002');

SELECT TIMEDIFF('2000:01:01 00:00:00','2000:01:01 00:00:00.000001');

SELECT TIME('2003-12-31 01:02:03');

SELECT TIMESTAMP('2003-12-31 12:00:00','12:00:00');

SELECT TIMESTAMPADD(MINUTE,1,'2003-01-02');

V9.0.5增加的函数：

SELECT TO\_DAYS(950501);

SELECT TO\_SECONDS(950501);

SELECT UNIX\_TIMESTAMP('2025-09-08 08:30:06');

SELECT UTC\_DATE(), UTC\_DATE() + 0;

SELECT UTC\_TIME(), UTC\_TIME() + 0;

SELECT UTC\_TIMESTAMP(), UTC\_TIMESTAMP() + 0;

SELECT DAYNAME('2025-05-12');

SELECT MONTHNAME('2008-02-03');

SELECT TIME\_TO\_SEC('22:23:00');

SELECT MONTH('2008-02-03');

SELECT DATE('2003-12-31 01:02:03');

SELECT WEEK('2008-02-20',1);

SELECT YEARWEEK('2025-06-01');

SELECT DATEDIFF('2025-10-01 20:09:50','2025-02-09');

SELECT FROM\_DAYS(700669);

SELECT CONVERT\_TZ('2024-01-01 12:00:00','+00:00','+10:00');

SELECT GET\_FORMAT(DATE,'USA');

SELECT TIMESTAMPDIFF(MONTH,'2003-02-01','2003-05-01');

SELECT STR\_TO\_DATE('01,5,2013','%d,%m,%Y');

SELECT LOCATE('bar','foobarbar',5);

SELECT LCASE('GOOD');

SELECT UCASE('hello');

SELECT INSERT('Quadratic',3, 4,'What');

SELECT BIN(12);

SELECT CHAR(77,121,83,81,'76');

SELECT ELT(1,'Aa','Bb','Cc','Dd');

SELECT FIELD('Bb','Aa','Bb','Cc','Dd','Ff');

SELECT FIND\_IN\_SET('b','a,b,c,d');

SELECT HEX(255);

SELECT SPACE(6);

SELECT SOUNDEX('Hello');

SELECT EXPORT\_SET(5,'Y','N',',',4);

SELECT ORD('ABAC2');

SELECT SUBSTRING\_INDEX(' [www.mysql.com\\',\\'.\\',2](http://www.mysql.com/',/'./',2));

SELECT FROM\_BASE64('YWJj');

SELECT TO\_BASE64('abc');

SELECT LENGTH('text');

SELECT BIT\_LENGTH('text');

SELECT OCTET\_LENGTH('text');

SELECT LEFT('foobarbar',5);

SELECT RIGHT('foobarbar',4);

SELECT REPLACE(' [www.mysql.com\\',\\'w\\',\\'Ww\\](http://www.mysql.com/',/'w/',/'Ww/) ‘);

SELECT UNHEX('2567');

SELECT HEX('mysql');

SELECT STRCMP('text','text2');

SELECT IF(1<2,'yes','no');

SELECT IFNULL(NULL,10);

SELECT ISNULL(1+1);

SELECT INTERVAL(10,1,10,100,1000);

SELECT CONV('6E',18,8);

SELECT INET\_ATON('10.0.5.9');

SELECT INET\_NTOA(167773449);

SELECT HEX(INET6\_ATON('fdfe::5a55:caff:fefa:9089'));

SELECT INET6\_NTOA(UNHEX('FDFE0000000000005A55CAFFFEFA9089'));