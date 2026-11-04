---
title: "13、HGDB重建控制文件"
book: "数据库使用类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/question/HGDB_reset.html"
tags:
  - highgo
  - highgo-v45
  - faq-database-usage
---

## HGDB重建控制文件

## 1、文档用途

当控制文件损坏时，重建控制文件

## 2、详细信息

### (1) 介绍

如果控制文件$PGDATA/global/pg\_control损坏或丢失, 数据库将运行异常, 无法启动.  
pg\_resetwal会清除预写式日志（WAL）并且有选择地重置存储在pg\_control文件中的一些其他控制信息。如果这些文件已经被损坏，某些时候就需要这个功能。当服务器由于这样的损坏而无法启动时，这只应该被用作最后的手段。

使用此方法后数据库可能包含由于部分提交事务产生的不一致数据。应当立刻转储你的数据，即将数据导入一个新库中。

这个工具只能被安装服务器的用户运行，因为它要求对数据目录的读写访问。  
出于安全原因，必须在命令行中指定数据目录。pg\_resetwal不使用环境变量PGDATA。  
如果无法为pg\_control决定合法数据，可以通过指定-f（强制）选项强制它继续。但恢复的数据库可能存在损坏，且需要立即转储数据。

### (2) 使用方法

```
pg_resetwal --help
pg_resetwal -l 000000010000000000000002 -O 0xCC80 -x 0x100000 -f -D /opt/HighGo4.5.7-see/data
```

> \-l walfile  
> 通过指定下一个WAL段文件名称来手工设置WAL开始位置。下一个WAL段文件的名称应该比当前存在于数据目录下pg\_wal目录中的任意 WAL 段文件名更大。如果00000001000000320000004A是pg\_wal中最大的项，则使用-l 00000001000000320000004B或更高的值。pg\_resetwal本身查看pg\_wal中的文件并选择一个超出最新现存文件名的默认-l设置。因此，只有当你知道 WAL 段文件当前不在pg\_wal中时，或者当pg\_wal的内容完全丢失时，才需要对-l的手工调整，例如一个离线归档中的项。

> \-m mxid,mxid  
> 手工设置下一个和最老的多事务 ID。确定下一个多事务 ID（第一部分）的安全值的方法：在数据目录下的pg\_multixact/offsets目录中查找最大的数字文件名，adding one, and then multiplying by 65536 (0x10000)。反过来，确定最老的多事务 ID（-m的第二部分）的方法：在同一个目录中查找最小的数字文件名并且乘以 65536。文件名是十六进制的数字，因此实现上述方法最简单的方式是以十六进制指定文件名并且追加四个零。例如做大的文件是0002，最小文件是0001，则安全值是0x30000，0x10000

> \-O mxoff  
> 手工设置下一个多事务偏移量。确定安全值的方法：查找数据目录下pg\_multixact/members目录中最大的数字文件名，adding one, and then multiplying by 52352 (0xCC80)。文件名是十六进制数字。没有像其他选项那样追加零的简单方法。例如最大文件名是0002，则安全值是3\*52352=157056，转换成十六进制0x26580
> 
> \-x xid  
> 手工设置下一个事务 ID。确定安全值的方法：在数据目录下的pg\_xact目录中查找最大的数字文件名，然后在它的基础上 adding one, and then multiplying by 1048576 (0x100000).注意文件名是十六进制的数字。通常以十六进制的形式指定该选项值也是最容易的。例如，如果0011是pg\_xact中的最大项，-x 0x1200000就可以（五个尾部的零就表示了前面说的乘数）。（十进制算法，12转成十进制是18也就是18\*1048576=18,874,368 转成十六进制是1200000）

注意， 这个命令不能在服务器正在运行时被使用。如果在数据目录中发现一个服务器锁文件，pg\_resetwal将拒绝启动。这种情况下可以移除该锁文件来让pg\_resetwal运行。

### (3) 问题

如果数据库使用了sm4加密，此方法不适用。会有如下错误信息

```
[root@0253a756e869 members]# pg_ctl start
waiting for server to start....2022-04-22 15:09:40.818 CST [1832] LOG:  data encryption performed by sm4
2022-04-22 15:09:40.819 CST [1832] FATAL:  database files are incompatible with server
2022-04-22 15:09:40.819 CST [1832] DETAIL:  The database cluster was initialized with LOBLKSIZE �!Q-��^Z�H��s, but the server was compiled with LOBLKSIZE .
2022-04-22 15:09:40.819 CST [1832] HINT:  It looks like you need to recompile or initdb.
2022-04-22 15:09:40.819 CST [1832] LOG:  database system is shut down
 stopped waiting
pg_ctl: could not start server
Examine the log output.
[root@0253a756e869 members]#
```

查看是否启用加密命令

```
# pg_controldata |grep encryption
```