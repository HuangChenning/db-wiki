---
title: "第6章 DM PHP编程指南"
book: "DM7程序员手册"
version: "DM7"
source: "temp/doc/DM7³ÌÐòÔ±ÊÖ²á.pdf#page=183"
tags:
  - dameng
  - dm7
  - programmer
---

## 第6 章 DM PHP 编程指南

## 6.1 DM PHP 介绍

本章主要介绍DM PHP 扩展的基本概念以及使用方法，以便于用户更好地使用DM PHP扩展库编写PHP 应用程序。

在使用PHP 语言的Web 应用中，为了可以和DM 数据库的服务器端进行通信，并且获得更快的速度以及对系统更强的控制，我们可以通过一个用C语言函数实现的瘦中间层来实现这个目标。该瘦中间层就是PHP 扩展，它实现了一组C语言API，成为PHP 语言级别的函数调用。

DM PHP 是在PHP 开放源码的基础上开发的一个动态扩展库，接口的实现参考了MySQL 的PHP 扩展，无论在功能、参数以及调用过程都和后者十分类似，命名统一采用dm 开头的小写英文字母方式，各个单词之间以下划线分割。PHP 应用程序可通过DM PHP扩展接口库访问DM 数据库服务器。

下面列出DM 提供的PHP 扩展函数，并简要说明每个函数的功能。

扩展库接口函数作用描述dm_connect 打开一个到DM 服务器的连接dm_pconnect 打开一个到DM 服务器的持久连接dm_close 关闭DM 连接dm_set_connect 设置连接dm_error 返回上一个DM 操作产生的文本错误信息dm_errno 返回上一个DM 操作中的错误信息的数字编码dm_query 发送一条DM 查询dm_unbuffered_query 向DM 发送一条SQL 查询，并不获取和缓存结果的行dm_more_query_no_result 获取下一个ResultSet 结果集，如果无结果集，返回False dm_db_query 发送一条DM 查询dm_affected_rows 取得前一次DM 操作所影响的记录行数dm_escape_string 转义一个字符串用于dm_query dm_fetch_array 从结果集中取得一行作为关联数组，或数字数组，或二者兼有dm_fetch_assoc 从结果集中取得一行作为关联数组dm_fetch_field 从结果集中取得列信息并作为对象返回dm_num_fields 取得结果集中字段的数目dm_fetch_length: 取得结果集中每个输出的长度dm_fetch_object 从结果集中取得一行作为对象dm_fetch_row 从结果集中取得一行作为枚举数组dm_field_flags 从结果中取得和指定字段关联的标志dm_field_len 返回指定字段的长度dm_field_name 取得结果中指定字段的字段名dm_field_seek 将结果集中的指针设定为制定的字段偏移量

## 第6 章 DM PHP 编程指南

dm_field_table 取得指定字段所在的表名dm_field_type 取得结果集中指定字段的类型dm_free_result 释放结果内存dm_get_server_info 取得DM 服务器信息dm_list_fields 列出DM 结果中的字段dm_list_tables 列出DM 数据库中的表dm_num_rows 取得结果集中行的数目dm_ping Ping 一个服务器连接，如果没有连接则重新连接dm_result 取得结果数据dm_insert_id 取得上一步INSERT 操作产生的ID dm_insert_id_ex 取得上一步INSERT 操作产生的ID dm_tablename 取得表名dm_data_seek 移动内部结果的指针dm_set_object_name_case 设置比较时的大小写方式

## 6.2 基本示例

利用DM PHP 驱动程序进行编程的一般步骤为：

1. 利用dm_connect（）建立同数据库的连接。
2. DM PHP 数据操作。数据操作主要分为两个方面，一个是更新操作，例如更新数据

库、删除一行、创建一个新表等；另一个就是查询操作。dm_query()执行完查询之后，会得到一个记录集。可以操作该对象来获得指定列的信息、读取指定行的某一列的值。

3. 释放资源。在操作完成之后，用户需要释放系统资源，主要是关闭结果集、关闭语

句对象，释放连接。

下面用具体的编程实例来展示利用DM PHP 对示例数据库BOOKSHOP，以产品信息表product 的增加、删除、修改、查询为例子进行数据库操作的基本步骤。

1. 增加记录

<?php/* 连接选择数据库 */$link = dm_connect("localhost", "SYSDBA", "SYSDBA")or die("Could not connect : " . dm_error());

print "Connected successfully";

/* 执行 SQL 查询 */$query = " INSERT INTO production.product(name,author,publisher,publishtime,product_subcategoryid,productno,satetystocklevel,originalprice,nowprice,discount,description,photo,sellstarttime)VALUES('三国演义','罗贯中','中华书局','2005-04-01','4','9787101046121','10','19.0000','15.2000','8.0','《三国演义》是中国第一部长篇章回体小说!',null,'2006-03-20')";

$result = dm_query($query) or die("Query failed : " . dm_error());

/* 释放资源 */dm_free_result($result);

/* 断开连接 */

## 第6 章 DM PHP 编程指南

dm_close($link);

?>

2. 修改数据

<?php/* 连接选择数据库 */$link = dm_connect("localhost", "SYSDBA", "SYSDBA")or die("Could not connect : " . dm_error());

print "Connected successfully";

/* 执行 SQL 查询 */$query = " UPDATE production.product SET TYPE =1000 WHERE productid = 10";

$result = dm_query($query) or die("Query failed : " . dm_error());

/* 释放资源 */dm_free_result($result);

/* 断开连接 */dm_close($link);

?>

3. 删除记录

<?php/* 连接选择数据库 */$link = dm_connect("localhost", "SYSDBA", "SYSDBA")or die("Could not connect : " . dm_error());

print "Connected successfully";

/* 执行 SQL 查询 */$query = " DELETE FROM production.product WHERE productid = 10";

$result = dm_query($query) or die("Query failed : " . dm_error());

/* 释放资源 */dm_free_result($result);

/* 断开连接 */dm_close($link);

?>

4. 查询记录

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN""http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><html xmlns="http://www.w3.org/1999/xhtml"><head><meta http-equiv="Content-Type" content="text/html; charset=gb2312" /><style type="text/css"><!--body,td,th {font-size: 12px;

}--></style></head>

## 第6 章 DM PHP 编程指南

<body><?php/* 连接选择数据库 */$link = dm_connect("localhost", "SYSDBA", "SYSDBA")or die("Could not connect : " . dm_error());

print "Connected successfully";

/* 执行 SQL 查询 */$query = " select * from production.product";

$result = dm_query($query) or die("Query failed : " . dm_error());

/* 在 HTML 中打印结果 */print "<table border=\"1\" cellspacing=\"1\" cellpadding=\"1\">\n";

while ($line = dm_fetch_array($result, DM_ASSOC)) {print "\t<tr>\n";

foreach ($line as $col_value) {print "\t\t<td>$col_value</td>\n";

}print "\t</tr>\n";

}print "</table>\n";

/* 断开连接 */dm_close($link);

?></body></html>

5. 存储过程

运行程序，启动达梦数据库服务器并创建用于修改产品信息的存储过程。存储过程代码如下：

create or replace procedure "PRODUCTION"."updateProduct"(v_id int,v_name varchar(50))as begin UPDATE production.product SET name = v_name WHERE productid = v_id;

end;

在PHP 里得到返回的结果集。

<head><meta http-equiv="Content-Type" content="text/html; charset=gb2312" /><style type="text/css"><!--body,td,th {font-size: 12px;

}-->

## 第6 章 DM PHP 编程指南

</style></head><body><?php/* 连接选择数据库 */$link = dm_connect("localhost", "SYSDBA", "SYSDBA")or die("Could not connect : " . dm_error());

print "Connected successfully";

dm_select_db("system") or die("Could not select database");

/* 执行 SQL 查询 */$query = " CALL production.updateProduct(1,'红楼梦')";

$result = dm_query($query) or die("Query failed : " . dm_error());

/* 释放资源 */dm_free_result($result);

/* 断开连接 */dm_close($link);

?></body></html>

## 6.3 DM PHP 模块加载

目前DM 支持的PHP 版本为PHP5.2~5.5，用户可根据自己安装的PHP 版本选择对应的接口库。下面的示例均以PHP5.3 版本为例，如果版本不同，将53 改为对应值即可。

1. linux 系统下加载

步骤：

1) 下载并安装apache从网络中下载apache-2.0.48.tar.gz存至/home/tmp

cd /home/tmp tar -xvzf apache-2.0.48.tar.gz /usr/local cd /usr/local/apache-2.0.48./configure --prefix=/usr/local/apache --enable-module=so make make install cd /usr/local/apache/conf vi httpd.conf ServerName localhost port 80 DirectoryIndex default.php default.phtml default.php3 default.html default.htm AddType application/x-httpd-php .php .phtml .php3 .inc AddType application/x-httpd-php-source .phps

2) 下载并安装php从网络中下载最新php-5.2.6.tar.gz存至/home/tmp

## 第6 章 DM PHP 编程指南

cd /home/tmp tar -xvzf php-x.x.x.tar.gz /usr/local cd /usr/local/php-x.x.x./buildconf --force./configure --with-apache2=/usr/local/apache/bin/apxs make make install

cp php.ini-dist /usr/local/lib/php.ini 3) 安装DM DBMS假定安装到/usr/local/DMDBMS 目录4) 安装DM PHP cp dm_php /home

cd /home/dm_php; 执行/usr/local/bin/phpize./configure make cd /usr/local/lib vi php.ini

; 修改下面配置，假设“/home/dm_php/modules”为libphp53ts_dm.so 所在路径

; libphp53ts_dm.so 中的ts 表示线程安全版本，不带ts 表示非线程安全版本register_globals=on extension_dir=/home/dm_php/modules; 添加下面语句extensions=libphp53ts_dm.so; 添加php.ini 中有关连接的配置[dm]; 是否允许持久性连接dm.allow_persistent = 1; 允许建立持久性连接的最大数. -1 为没有限制.

dm.max_persistent = -1; 允许建立连接的最大数(包括持久性连接). -1 为没有限制.

dm.max_links = -1; 默认的主库地址dm.default_host = localhost; 默认的连接用户名dm.default_user = SYSDBA; 默认的连接口令.

dm.default_pw = SYSDBA; 连接超时，这个参数未实际的用到，等待服务器支持dm.connect_timeout = 10; 对于各种变长数据类型，每列最大读取的字节数。如果它设置为0 或是小于0,那么，读取变长字段时，将显示NULL 值dm.defaultlrl = 4096

## 第6 章 DM PHP 编程指南

; 是否读取二进制类型数据，如果它设置为0，那么二进制将被NULL 值代替dm.defaultbinmode = 1; 是否允许检察持久性连接的有效性，如果设置为ON，那么当重用一个持久性连接时，会检察该连接是否还有效dm.check_persistent = ON

2. Windows 系统下加载模块

步骤：

1) 下载apache 的windows 版本并安装，同时修改httpd.conf；

2) 下载php 并安装；

3) 安装DM DBMS，拷贝bin 目录下php53_dm.dll 到php 目录下的extensions 目录中，修改php.ini，添加extension=php53_dm.dll，添加php.ini 中有关连接的配置；

4) 重启apache 服务器，在浏览器中输入http:\\localhost\php_info.php 查看是否有dm模块项，如有说明加载DM PHP 成功。

## 6.4 编程接口

1． dm_affected_rows描述取得前一次数据库操作INSERT、UPDATE 或 DELETE 查询所影响的记录行数。

如果连接句柄没有指定，则默认使用最近一次由dm_connect()函数打开的连接句柄。

格式int dm_affected_rows ( [resource link_identifier])参数

参数描述link_identifier [IN]连接句柄

返回值如果最近一次操作是没有任何条件（WHERE）的 DELETE 查询，在表中所有的记录都会被删除，但该函数返回值为0。

2． dm_connect描述建立一个到DM 服务器的连接。

格式resource dm_connect ( [string server [, string username [, string password]]])参数

参数描述server [IN]服务器名称username [IN]用户名称password [IN]用户密码

返回值如果成功则返回一个连接标识，失败则返回 FALSE。

> 3． dm_pconnect

## 第6 章 DM PHP 编程指南

描述分配用户描述符。

格式resource dm_pconnect ( [string server [, string username [, string password]]]);

参数

参数描述

server [IN]服务器名称username [IN]用户名称password [IN]用户密码返回值如果成功则返回一个正的持久连接标识符，出错则返回FALSE。

4． dm_close描述关闭指定的连接标识所关联的DM 服务器的连接。如果没有指定 link_identifier，则关闭上一个打开的连接格式bool dm_close ( [resource link_identifier])参数

参数描述

link_identifier [IN]连接标识符返回值如果成功则返回TRUE，失败则返回FALSE。

5． dm_error描述返回上一个DM 操作产生的文本错误信息。

格式string dm_error ( [resource link_identifier])参数

参数描述link_identifier [IN]连接标识符

返回值返回上一个DM 函数的错误文本，如果没有出错则返回 ''（空字符串）。如果没有指定连接资源号，则使用上一个成功打开的连接从DM 服务器提取错误信息。

6． dm_errno描述返回上一个 DM 操作中的错误信息的数字编码。

格式int dm_errno ( [resource link_identifier])参数

参数描述link_identifier [IN]连接标识符

## 第6 章 DM PHP 编程指南

返回值返回上一个 DM 函数的错误号码，如果没有出错则返回0（零）。

7． dm_query描述发送一条 DM 查询。

格式resource dm_query ( string query [, resource link_identifier])参数

参数描述query [IN]查询字符串link_identifier [IN]连接标识符

返回值仅对SELECT、EXPLAIN 语句返回一个资源标识符，如果查询执行不正确则返回FALSE。对于其它类型的 SQL 语句，dm_query() 在执行成功时返回TRUE，出错时返回FALSE。非FALSE 的返回值意味着查询是合法的并能够被服务器执行。这并不说明任何有关影响到的或返回的行数。

8． dm_unbuffered_query描述向DM 发送一条SQL 查询，并不获取和缓存结果的行。

格式resource dm_unbuffered_query ( string query [, resource link_identifier])参数

参数描述query [IN]查询字符串link_identifier [IN]连接标识符

返回值向DM 发送一条SQL 查询query，但不像dm_query()那样自动获取并缓存结果集。

一方面，这在处理很大的结果集时会节省可观的内存；另一方面，可以在获取第一行后立即对结果集进行操作，而不用等到整个 SQL 语句都执行完毕。当使用多个数据库连接时，必须指定可选参数 link_identifier。

9． dm_db_query描述发送一条DM 查询。

格式resource dm_db_query ( string database, string query [, resource link_identifier])参数

参数描述database [IN]指定的数据库名称query [IN]查询字符串link_identifier [IN]连接标识符

返回值根据查询结果返回一个正的DM 结果资源号，出错时返回FALSE。

## 第6 章 DM PHP 编程指南

10． dm_escape_string描述转义一个字符串用于 dm_query。

格式string dm_escape_string ( string unescaped_string)参数

参数描述unescaped_string [IN]被转义字符串

返回值返回转义以后的字符串。

11． dm_fetch_array描述从结果集中取得一行作为关联数组，或数字数组，或二者兼有。

格式array dm_fetch_array ( resource result [, int result_type])参数

参数描述result [IN]结果集资源[IN]是一个常量，可以接受以下值：DM_ASSOC,DM_NUM 和 DM_BOTH，result_type 如果用了 DM_BOTH，将得到一个同时包含关联和数字索引的数组。用

DM_ASSOC 只得到关联索引, DM_NUM 只得到数字索引返回值返回根据从结果集取得的行生成的数组，如果没有更多行则返回FALSE。

12． dm_fetch_assoc描述从结果集中取得一行作为关联数组。

格式array dm_fetch_assoc ( resource result)参数

参数描述result [IN]连接句柄

返回值返回根据从结果集取得的行生成的关联数组，如果没有更多行则返回FALSE。

13． dm_fetch_field描述从结果集中取得列信息并作为对象返回。

格式object dm_fetch_field ( resource result [, int field_offset])参数

参数描述result [IN]结果集资源field_offset [IN]字段偏移

## 第6 章 DM PHP 编程指南

返回值返回一个包含字段信息的对象。

14． dm_num_fields描述取得结果集中字段的数目。

格式int dm_num_fields ( resource result)参数

参数描述result [IN]结果集资源

返回值返回结果集中字段的数目。

15． dm_fetch_lengths描述取得结果集中每个输出的长度。

格式array dm_fetch_lengths ( resource result)参数

参数描述result [IN]结果集资源

返回值以数组返回上一次用dm_fetch_row 取得的行中每个字段的长度，如果出错返回FALSE。

16． dm_fetch_object描述从结果集中取得一行作为对象。

格式object dm_fetch_object ( resource result)参数

参数描述result [IN]结果集资源

返回值返回根据所取得的行生成的对象，如果没有更多行则返回FALSE。

17． dm_fetch_row描述从结果集中取得一行作为枚举数组。

格式array dm_fetch_row ( resource result)参数

参数描述result [IN]结果集资源

返回值

## 第6 章 DM PHP 编程指南

返回根据所取得的行生成的数组，如果没有更多行则返回FALSE。

18． dm_field_flags描述从结果中取得和指定字段关联的标志。

格式string dm_field_flags ( resource result, int field_offset)参数

参数描述result [IN]结果集资源field_offset [IN]字段偏移

返回值返回指定字段的字段标志。每个标志都用一个单词表示，之间用一个空格分开。

19． dm_field_len描述返回指定字段的长度。

格式int dm_field_len ( resource result, int field_offset)参数

参数描述result [IN]结果集资源

返回值返回指定字段的长度。

20． dm_field_name描述取得结果中指定字段的字段名。

格式string dm_field_name ( resource result, int field_index)参数

参数描述result [IN]结果集资源field_index [IN]字段索引号

返回值返回指定字段索引的字段名。result 必须是一个合法的结果标识符，field_index是该字段的数字偏移量。

21． dm_field_seek描述将结果集中的指针设定为制定的字段偏移量。

格式int dm_field_seek ( resource result, int field_offset)参数

参数描述result [IN]结果集资源

## 第6 章 DM PHP 编程指南

field_offset [IN]字段偏移

返回值返回指定字段的字段偏移量。

22． dm_field_table描述取得指定字段所在的表名。

格式string dm_field_table ( resource result, int field_offset)参数

参数描述field_offset [IN]字段偏移result [IN]结果集资源

返回值返回指定字段所在的表名。

23． dm_field_type描述取得结果集中指定字段的类型。

格式string dm_field_type ( resource result, int field_offset)参数

参数描述field_offset [IN]字段偏移result [IN]结果集资源

返回值返回字段类型有“int”，“real”，“char”，“blob”等。

24． dm_free_result描述释放结果内存。

格式bool dm_free_result ( resource result)参数

参数描述result [IN]结果集资源

返回值如果成功则返回TRUE，失败则返回FALSE。

25． dm_get_server_info描述取得 DM 服务器信息。

格式string dm_get_server_info ( [resource link_identifier])参数

参数描述

## 第6 章 DM PHP 编程指南

link_identifier [IN]连接标识符

返回值返回 link_identifier 所使用的服务器版本。如果省略 link_identifier，则使用上一个打开的连接。

26． dm_list_fields描述列出 DM 结果中的字段。

格式resource dm_list_fields ( string database_name, string table_name [, resource link_identifier])参数

参数描述database_name [IN]数据库名link_identifier [IN]连接标识符

table_name [IN]表名返回值返回一个结果指针。

27． dm_list_tables描述列出 DM 数据库中的表。

格式resource dm_list_tables ( string database [, resource link_identifier])参数

参数描述database_name [IN]数据库名link_identifier [IN]连接标识符

返回值返回一个结果指针。

28． dm_num_rows描述取得结果集中行的数目。

格式int dm_num_rows ( resource result)参数

参数描述

result [IN]结果集返回值返回结果集中行的数目。此命令仅对SELECT 语句有效。

29． dm_ping描述Ping 一个服务器连接，如果没有连接则重新连接。

格式bool dm_ping ( [resource link_identifier])

## 第6 章 DM PHP 编程指南

参数

参数描述link_identifier [IN]连接标识符

返回值如果到服务器的连接可用则dm_ping()返回TRUE，否则返回FALSE。

30． dm_result描述取得结果数据。

格式mixed dm_result ( resource result, int row [, mixed field])参数

参数描述result [IN]结果集row [IN]指定行序号

返回值返回 DM 结果集中一个单元的内容。

31． dm_insert_id描述取得上一步INSERT 操作产生的ID。

格式int dm_insert_id ( [resource link_identifier])参数

参数描述link_identifier [IN]连接标识符

返回值返回给定的link_identifier 中上一步INSERT 查询中产生的AUTO_INCREMENT的ID 号。如果没有指定link_identifier，则使用上一个打开的连接。如果上一查询没有产生AUTO_INCREMENT 的值，则dm_insert_id()返回0。

32． dm_tablename描述取得表名。

格式string dm_tablename ( resource result, int i)参数

参数描述result [IN]表结果集i [OUT]表索引序号

返回值接受dm_list_tables()返回的结果指针以及一个整数索引作为参数并返回表名。

33． dm_tablename描述取得表名。

## 第6 章 DM PHP 编程指南

格式string dm_tablename ( resource result, int i)参数

参数描述result [IN]表结果集i [OUT]表索引序号

返回值接受dm_list_tables()返回的结果指针以及一个整数索引作为参数并返回表名。

34． dm_data_seek描述移动内部结果的指针。

格式bool dm_data_seek ( resource result_identifier, int row_number)参数

参数描述result_identifier [IN]结果集row_number [OUT]行索引序号

返回值指定的结果标识所关联的DM 结果内部的行指针移动到指定的行号。

35． dm_set_object_name_case描述设置使用列名称时的大小写方式。

格式bool dm_set_object_name_case(resource con, int Case_sensitive)参数

参数描述

resource con PHP 传入的要连接的连接资源，可选参数

Case_sensitive 大小写方式

返回值设置成功，返回TRUE；否则返回FALSE。
