---
title: "大对象"
book: "客户端接口指南"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/reference/referenceOne3.html"
tags:
  - highgo
  - highgo-v9
  - client-interface-guide
---

## 大对象

瀚高数据库具有大对象的功能，它提供了对于存储在一个特殊大对象结构中的用户数据的流式访问。对于那些大得无法以一个整体处理的数据值 ，流式访问非常有用。

本章介绍了瀚高数据库中大对象数据的实现、编程和查询语言接口。在本章中我们使用名为 libpq的C库来作为例子，但是绝大部分瀚高数据库支持的本地编程接口也具有相同的功能。其他接口可能会在内部使用大对象接口来提供对大值的一般支持，但这里就不再描述。

## 简介

所有的大对象都存在一个名为pg\_largeobject的系统表中。每一个大对象还在系统表pg\_largeobject\_metadata中有一个对应的项。大对象可以通过类似于标准文件操作的读/写API来进行创建、修改和删除。

瀚高数据库也支持一种称为”TOAST”的存储系统， 它自动把大于一个数据库页的值存储到一个二级存储区域，每一个表都有专属的二级存储区域。这使得大对象功能显得有些陈旧。

但是大对象功能仍然有一个优势是能够支持高达4TB的值，而TOAST域只能支持最大1GB。此外，读写一个大对象的片段会很高效，但是大部分在TOAST域上的操作都将把整个值作为一个单元进行读或写。

## 实现特性

大对象的实现将大对象分解成很多”数据块”并且将这些数据块存储在数据库的行中。一个 B-tree索引用来保证在进行随机访问读写时能够根据数据块号快速地搜索到正确的数据块。

为一个大对象存储的数据块并不需要是连续的。例如，如果一个应用打开了一个新的大对象，移动到偏移量1000000并写了一些字节，这并不会导致分配1000000字节的存储，只有覆盖写入字节范围的数据块需要被分配。而一个读操作将会把现有最后的数据块之前还未分配的位置读出为0。这和Unix文件系统中”稀疏”文件的一般行为相对应。

自瀚高安全版数据库v4起，大对象可以有一个拥有者和一组访问权限，它们可以用GRANT和REVOKE管理。读一个大对象需要SELECT权限，而写或者截断一个大对象则需要UPDATE权限。只有大对象的拥有者（或者一个数据库超级用户）可以创建大对象、注释大对象或修改大对象的拥有者。要调整这些行为以兼容以前的发行，请见lo\_compat\_privileges的运行时参数。

## 客户端接口

本节描述瀚高数据库的libpq客户端接口为访问大对象所提供的功能。瀚高数据库的大对象接口按照Unix文件系统的接口建模，也有相似的open、read、write、lseek等。

所有使用这些函数对大对象的操作都必须发生在一个SQL事务块中，因为大对象文件描述符只在事务期间有效。

在执行任何一个这种函数期间如果发生一个错误，该函数将会返回一个其他的不可能值，典型的是0或-1。一个关于该错误的消息亦会被保存在连接对象中，可以通过PQerrorMessage检索到。

使用这些函数的客户端应用应该包括头文件libpq/libpq-fs.h并链接libpq库。

### 创建一个大对象

函数Oid lo\_creat(PGconn \*conn, int mode);创建一个新的大对象。其返回值是分配给这个新大对象的OID或者InvalidOid（0）表示失败，为了和以前的发行兼容，它最好被设置为INV\_READ、INV\_WRITE或INV\_READ | INV\_WRITE（这些符号常量定义在头文件libpq/ libpq-fs.h中）。

示例：

inv\_oid = lo\_creat(conn, INV\_READ|INV\_WRITE);

函数Oid lo\_create(PGconn \*conn, Oid lobjId);也创建一个新的大对象。分配给该大对象的OID可以通过lobjId指定，如果这样做，该OID已经被某个大对象使用时会产生错误。如果lobjId是InvalidOid（0），则lo\_create会分配一个未使用的OID（这时和lo\_creat的行为相同）。返回值是分配给新大对象的OID或InvalidOid（0）表示发生错误。

lo\_create在从PostgreSQL 8.1开始的版本中是新的，如果该函数在旧服务器版本上运行，它将失败并返回InvalidOid。

示例：

inv\_oid = lo\_create(conn, desired\_oid);

### 导入一个大对象

要将一个操作系统文件导入成一个大对象，调用：

Oid lo\_import(PGconn \*conn, const char \*filename);

filename指定了要导入为大对象的操作系统文件名。返回值是分配给新大对象的OID或InvalidOid（0）表示发生错误。注意该文件是被客户端接口库而不是服务器所读取，因此它必须存在于客户端文件系统中并且对于客户端应用是可读的。

函数Oid lo\_import\_with\_oid(PGconn \*conn, const char \*filename, Oid lobjId); 也可以导入一个新大对象。分配给新大对象的OID可以用lobjId指定，如果这样做，该OID已经被某个大对象使用时会产生错误。如果lobjId是InvalidOid（0），则lo\_import\_with\_oid会分配一个未使用的OID（这和lo\_import的行为相同）。返回值是分配给新大对象的OID或InvalidOid（0）表示发生错误。

### 导出一个大对象

要把一个大对象导出到一个操作系统文件，调用：

int lo\_export(PGconn \*conn, Oid lobjId, const char \*filename);

lobjId参数指定要导出的大对象的OID，filename参数指定操作系统文件名。注意该文件是被客户端接口库而不是服务器写入。成功返回1，错误返回-1。

### 打开一个现有的大对象

要打开一个现有的大对象进行读写，调用：

int lo\_open(PGconn \*conn, Oid lobjId, int mode);

lobjId参数指定要打开的大对象的OID。mode位控制着打开对象是为了只读（INV\_READ）、只写（INV\_WRITE）或者读写（这些符号常量定义在头文件libpq/libpq-fs.h中）。lo\_open返回一个（非负）大对象描述符以便后面用于lo\_read、lo\_write、lo\_lseek、lo\_lseek64、lo\_tell、lo\_tell64、lo\_truncate、lo\_truncate64以及lo\_close。该描述符只在当前事务期间有效。如果打开错误将会返回-1。

服务器目前并不区分模式INV\_WRITE和INV\_READ |INV\_WRITE：在两种情况中都允许从描述符读取。但是在这些模式和单独的INV\_READ之间有明显的区别：使用INV\_READ我们不能向描述符写入，从中读取的数据则反映了该大对象在活动事务快照时刻的内容（该快照在lo\_open被执行时创建），而不管之后被该事务或其他事务写入的内容。从一个以INV\_WRITE模式打开的描述符读取的数据所有其他已提交事务以及当前事务所作的写入。这与普通SQL命令 SELECT的REPEATABLE READ和READ COMMITTED事务模式之间的区别相似。

如果大对象的SELECT特权不可用，或者如果在指定了INV\_WRITE时UPDATE特权不可用，则lo\_open将会失败。这些特权检查可以用lo\_compat\_privileges运行时参数禁用。

示例：

inv\_fd = lo\_open(conn, inv\_oid, INV\_READ|INV\_WRITE);

### 向一个大对象写入数据

函数int lo\_write(PGconn \*conn, int fd, const char \*buf, size\_t len);从buf（大小必须是 len）中写出len字节到大对象描述符fd。参数fd必须是已经由前面的lo\_open返回的大对象描述符。函数将返回实际写入的字节数（在当前的实现中，除非出错，返回的字节数总是等于len）。在出错时，返回值为-1。

尽管参数len被声明为类型size\_t，该函数会拒绝超过INT\_MAX的长度值。在实际中，被传送的数据最好是每块最多数兆字节。

### 从一个大对象读取数据

函数int lo\_read(PGconn \*conn, int fd, char \*buf, size\_t len); 从大对象描述符fd中读取最多len字节到buf （大小必须是len）中。参数fd必须是已经由前面的lo\_open返回的大对象描述符。实际读出的字节数将被返回，如果先到达了大对象的末尾返回值可能会小于len。出错时返回值为-1。

尽管参数len被声明为类型size\_t，该函数会拒绝超过INT\_MAX的长度值。在实际中，被传送的数据最好是每块最多数兆字节。

### 在一个大对象中查找

要改变一个大对象描述符的当前读或写位置，调用：

int lo\_lseek(PGconn \*conn, int fd, int offset, int whence);

该函数将大对象文件描述符fd的当前位置指针移动到由offset指定的新位置。whence的可用值是SEEK\_SET（从对象开头定位）、SEEK\_CUR （从当前位置定位）以及SEEK\_END（从对象末尾定位）。返回值是新位置的指针，或者是-1表示出错。

在处理可能超过2GB大小的大对象时，换用pg\_int64 lo\_lseek64(PGconn \*conn, int fd, pg\_int64 offset, int whence);

该函数的行为和lo\_lseek相同，但是它能接受一个超过2GB的offset并/或传送一个超过2GB的结果。注意如果新位置的指针超过2GB，lo\_lseek会失败。

lo\_lseek64是从瀚高安全版数据库V4开始增加的新函数。如果该函数在一个旧服务器版本上执行，将会失败并返回-1。

### 获取一个大对象的查找位置

要得到一个大对象描述符的当前读或写位置，调用：

int lo\_tell(PGconn \*conn, int fd);

如果出现错误，返回值是-1。

在处理可能超过2GB大小的大对象时，换用：

pg\_int64 lo\_tell64(PGconn \*conn, int fd);

该函数和lo\_tell的行为相同，但是它能传递超过2GB的结果。注意如果当前读/写位置超过 2GB，lo\_tell将会失败。

### 截断一个大对象

要将一个大对象截断成一个给定长度，调用：

int lo\_truncate(PGcon \*conn, int fd, size\_t len);

该函数将大对象描述符fd截断为长度len。参数fd必须是已经由前面的lo\_open返回的大对象描述符。如果len超过了大对象的当前长度，大对象将会被使用空字节（'\\0'）扩展到指定长度。成功时lo\_truncate返回0，失败时返回值为-1。

描述fd的读/写位置不变。

尽管参数len被声明为类型size\_t，lo\_truncate会拒绝超过INT\_MAX的长度值。

在处理可能超过2GB大小的大对象时，换用：

int lo\_truncate64(PGcon \*conn, int fd, pg\_int64 len);

该函数和lo\_truncate的行为相同，但它能够接受超过2GB的len值。

### 关闭一个大对象描述符

要关闭一个大对象描述符，调用：

int lo\_close(PGconn \*conn, int fd);

其中fd是由lo\_open返回的大对象描述符。成功时，lo\_close返回0，失败时返回-1。

在事务末尾仍然保持打开的任何大对象描述符都会自动被关闭。

### 移除一个大对象

要从数据库中移除一个大对象，调用：

int lo\_unlink(PGconn \*conn, Oid lobjId);

lobjId参数指定要移除的大对象的OID。成功时返回1，失败时返回-1。

## 服务器端函数

下表列出了为从 SQL 操纵大对象定制的服务器端函数。

| 函数 | 返回类型 | 描述 | 实例 | 结果 |
| --- | --- | --- | --- | --- |
| lo\_from\_bytea(loid oid,stringbytea) | oid | 创建一个大对象并且在其中存储数据，返回它的 OID。 传递0会让系统选择一个 OID。 | lo\_from\_bytea(0, '\\xffffff00') | 24528 |
| lo\_put(loid oid, offset bigint, str bytea) | void | 在给定的偏移位置写入数据。 | lo\_put(24528, 1, '\\xaa') |  |
| lo\_get(loid oid \[, from bigint, for int\]) | bytea | 在其中抽取内容或一个子串。 | lo\_get(24528, 0, 3) | \\xffaaff |

: 表 2.1 面向 SQL 的大对象函数

之前描述过的每个客户端函数都有一个相应的服务器端函数。实际上， 多半客户端函数都是等效的服务器端函数的简单接口。这些可以从 SQL 命令方便调用的函数是： lo\_creat、 lo\_create、 lo\_unlink、 lo\_import以及 lo\_export。 下面是使用它们的例子：

CREATE TABLE image (

name text,

raster oid

);

SELECT lo\_creat(-1); -- 返回新的空大对象的OID

SELECT lo\_create(43213); -- 尝试创建OID为43213的大对象

SELECT lo\_unlink(173454); -- 删除OID为173454的大对象

INSERT INTO image (name, raster)

VALUES ('beautiful image', lo\_import('/etc/motd'));

INSERT INTO image (name, raster) -- 和上面相同，但是指定了使用的OID

VALUES ('beautiful image', lo\_import('/etc/motd', 68583));

SELECT lo\_export(image.raster, '/tmp/motd') FROM image

WHERE name = 'beautiful image';

服务器端的lo\_import和lo\_export函数具有和它们的客户端同类大不相同的行为。这两个函数从服务器的文件系统中读和写文件，使用的是数据库所有者的权限。因此，默认情况下它们的使用被限制于超级用户。相反，客户端的导入和导出函数读写的是客户端的文件系统，使用的是客户端程序的权限。除了读取或写入所请求的大对象的特权之外，客户端函数不要求任何数据库特权。

| 小心： |
| --- |
| 可以把服务器端的lo\_import和lo\_export函数GRANT给非超级用户，但需要仔细地考虑安全因素。有这类特权的恶意用户可以很容易地利用它们成为超级用户（例如通过重写服务器配置文件），或者攻击该服务器文件系统的其他部分而无需获得数据库超级用户特权。因此对具有这类特权的角色访问必须受到和超级用户角色一样的仔细保护。尽管如此，如果某些例行任务需要使用服务器端的lo\_import或者lo\_export，使用具有这类特权的角色比使用具有完整超级用户特权的角色更加安全，因为那样会减小意外错误造成的损伤风险。 |

函数lo\_read和 lo\_write的功能也可以在服务器端调用，但是在服务器端的名称与客户端接口不同：它们的名称中不包含下划线。我们必须以loread和lowrite调用这些函数。

## 例子程序

下面示例是一个展示libpq中大对象接口如何使用的例子程序。部分程序被注释但仍保留在代码中，用户可以利用之。该程序可以在源代码的src/test/examples/testlo.c中找到。

例2.1. 用libpq操作大对象的例子程序

/\*-------------------------------------------------------------------------

\*

\* testlo.c

\* 测试通过 libpq 使用大对象

\*

\* Portions Copyright (c) 1996-2018, PostgreSQL Global Development Group

\* Portions Copyright (c) 1994, Regents of the University of California

\*

\*

\* IDENTIFICATION

\* src/test/examples/testlo.c

\*

\*-------------------------------------------------------------------------

\*/

#include <stdio.h>

#include <stdlib.h>

#include <sys/types.h>

#include <sys/stat.h>

#include <fcntl.h>

#include <unistd.h>

#include "libpq-fe.h"

#include "libpq/libpq-fs.h"

#define BUFSIZE 1024

/\*

\* importFile

\* 把文件 "in\_filename" 作为一个大对象 "lobjOid" 载入到数据库

\*

\*/

static Oid

importFile(PGconn \*conn, char \*filename)

{

Oid lobjId;

int lobj\_fd;

char buf\[BUFSIZE\];

int nbytes,

tmp;

int fd;

/\*

\* 打开要读入的文件

\*/

fd = open(filename, O\_RDONLY, 0666);

if (fd < 0)

{ /\* error \*/

fprintf(stderr, "cannot open unix file\\"%s\\"\\n", filename);

}

/\*

\* 创建大对象

\*/

lobjId = lo\_creat(conn, INV\_READ | INV\_WRITE);

if (lobjId == 0)

fprintf(stderr, "cannot create large object");

lobj\_fd = lo\_open(conn, lobjId, INV\_WRITE);

/\*

\* 从该 Unix 文件读取并写入到大对象

\*/

while ((nbytes = read(fd, buf, BUFSIZE)) > 0)

{

tmp = lo\_write(conn, lobj\_fd, buf, nbytes);

if (tmp < nbytes)

fprintf(stderr, "error while reading \\"%s\\"", filename);

}

close(fd);

lo\_close(conn, lobj\_fd);

return lobjId;

}

static void

pickout(PGconn \*conn, Oid lobjId, int start, int len)

{

int lobj\_fd;

char \*buf;

int nbytes;

int nread;

lobj\_fd = lo\_open(conn, lobjId, INV\_READ);

if (lobj\_fd < 0)

fprintf(stderr, "cannot open large object %u", lobjId);

lo\_lseek(conn, lobj\_fd, start, SEEK\_SET);

buf = malloc(len + 1);

nread = 0;

while (len - nread > 0)

{

nbytes = lo\_read(conn, lobj\_fd, buf, len - nread);

buf\[nbytes\] = '\\0';

fprintf(stderr, ">>> %s", buf);

nread += nbytes;

if (nbytes <= 0)

break; /\* no more data? \*/

}

free(buf);

fprintf(stderr, "\\n");

lo\_close(conn, lobj\_fd);

}

static void

overwrite(PGconn \*conn, Oid lobjId, int start, int len)

{

int lobj\_fd;

char \*buf;

int nbytes;

int nwritten;

int i;

lobj\_fd = lo\_open(conn, lobjId, INV\_WRITE);

if (lobj\_fd < 0)

fprintf(stderr, "cannot open large object %u", lobjId);

lo\_lseek(conn, lobj\_fd, start, SEEK\_SET);

buf = malloc(len + 1);

for (i = 0; i < len; i++)

buf\[i\] = 'X';

buf\[i\] = '\\0';

nwritten = 0;

while (len - nwritten > 0)

{

nbytes = lo\_write(conn, lobj\_fd, buf + nwritten, len - nwritten);

nwritten += nbytes;

if (nbytes <= 0)

{

fprintf(stderr, "\\nWRITE FAILED!\\n");

break;

}

}

free(buf);

fprintf(stderr, "\\n");

lo\_close(conn, lobj\_fd);

}

/\*

\* exportFile -

\* 把大对象 "lobjOid" 导出成文件 "out\_filename"

\*

\*/

static void

exportFile(PGconn \*conn, Oid lobjId, char \*filename)

{

int lobj\_fd;

char buf\[BUFSIZE\];

int nbytes,

tmp;

int fd;

/\*

\* 打开大对象

\*/

lobj\_fd = lo\_open(conn, lobjId, INV\_READ);

if (lobj\_fd < 0)

fprintf(stderr, "cannot open large object %u", lobjId);

/\*

\* 打开要写入的文件

\*/

fd = open(filename, O\_CREAT | O\_WRONLY | O\_TRUNC, 0666);

if (fd < 0)

{ /\* 错误 \*/

fprintf(stderr, "cannot open unix file\\"%s\\"",

filename);

}

/\*

\* 从大对象读入并写出到 Unix 文件

\*/

while ((nbytes = lo\_read(conn, lobj\_fd, buf, BUFSIZE)) > 0)

{

tmp = write(fd, buf, nbytes);

if (tmp < nbytes)

{

fprintf(stderr, "error while writing \\"%s\\"",

filename);

}

}

lo\_close(conn, lobj\_fd);

close(fd);

return;

}

static void

exit\_nicely(PGconn \*conn)

{

PQfinish(conn);

exit(1);

}

int

main(int argc, char \*\*argv)

{

char \*in\_filename,

\*out\_filename;

char \*database;

Oid lobjOid;

PGconn \*conn;

PGresult \*res;

if (argc!= 4)

{

fprintf(stderr, "Usage: %s database\_name in\_filename out\_filename\\n",

argv\[0\]);

exit(1);

}

database = argv\[1\];

in\_filename = argv\[2\];

out\_filename = argv\[3\];

/\*

\* 设置连接

\*/

conn = PQsetdb(NULL, NULL, NULL, NULL, database);

/\* 检查看看后端连接是否成功建立 \*/

if (PQstatus(conn)!= CONNECTION\_OK)

{

fprintf(stderr, "Connection to database failed: %s",

PQerrorMessage(conn));

exit\_nicely(conn);

}

/\* 设置总是安全的搜索路径，这样恶意用户就无法取得控制权。 \*/

res = PQexec(conn,

"SELECT pg\_catalog.set\_config('search\_path', '', false)");

if (PQresultStatus(res)!= PGRES\_TUPLES\_OK)

{

fprintf(stderr, "SET failed: %s", PQerrorMessage(conn));

PQclear(res);

exit\_nicely(conn);

}

PQclear(res);

res = PQexec(conn, "begin");

PQclear(res);

printf("importing file \\"%s\\"...\\n", in\_filename);

/\* lobjOid = importFile(conn, in\_filename); \*/

lobjOid = lo\_import(conn, in\_filename);

if (lobjOid == 0)

fprintf(stderr, "%s\\n", PQerrorMessage(conn));

else

{

printf("\\tas large object %u.\\n", lobjOid);

printf("picking out bytes 1000-2000 of the large object\\n");

pickout(conn, lobjOid, 1000, 1000);

printf("overwriting bytes 1000-2000 of the large object with X's\\n");

overwrite(conn, lobjOid, 1000, 1000);

printf("exporting large object to file \\"%s\\"...\\n", out\_filename);

/\* exportFile(conn, lobjOid, out\_filename); \*/

if (lo\_export(conn, lobjOid, out\_filename) < 0)

fprintf(stderr, "%s\\n", PQerrorMessage(conn));

}

res = PQexec(conn, "end");

PQclear(res);

PQfinish(conn);

return 0;

}