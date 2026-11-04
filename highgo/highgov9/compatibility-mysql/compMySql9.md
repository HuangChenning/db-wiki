---
title: "其他"
book: "MySQL兼容性"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/compatibility/compMySql9.html"
tags:
  - highgo
  - highgo-v9
  - compatibility-mysql
---

## 其他

## 字符集

支持MySQL的以下字符集。

| 字符集 |
| --- |
| ascii |
| big5 |
| binary |
| cp1250 |
| cp1251 |
| cp1256 |
| cp1257 |
| cp866 |
| cp932 |
| eucjpms |
| euckr |
| gb18030 |
| gb2312 |
| gbk |
| greek |
| hebrew |
| koi8r |
| koi8u |
| latin1 |
| latin2 |
| latin5 |
| latin7 |
| sjis |
| ujis |
| utf8 |
| utf8mb3 |
| utf8mb4 |

## 排序规则

字符集默认排序规则：

| ascii\_general\_ci |
| --- |
| big5\_chinese\_ci |
| binary |
| cp1250\_general\_ci |
| cp1251\_general\_ci |
| cp1256\_general\_ci |
| cp1257\_general\_ci |
| cp866\_general\_ci |
| cp932\_japanese\_ci |
| eucjpms\_japanese\_ci |
| euckr\_korean\_ci |
| gb18030\_chinese\_ci |
| gbk\_chinese\_ci |
| greek\_general\_ci |
| hebrew\_general\_ci |
| koi8r\_general\_ci |
| koi8u\_general\_ci |
| latin1\_swedish\_ci |
| latin2\_general\_ci |
| latin5\_turkish\_ci |
| latin7\_general\_ci |
| sjis\_japanese\_ci |
| ujis\_japanese\_ci |
| utf8\_general\_ci |
| utf8mb3\_general\_ci |
| utf8mb4\_general\_ci |

中文语境排序规则：

| gb2312\_chinese\_ci |
| --- |
| gb2312\_bin |
| gbk\_chinese\_ci |
| gbk\_bin |
| gb18030\_chinese\_ci |
| gb18030\_bin |
| gb18030\_unicode\_520\_ci |
| utf8\_general\_ci |
| utf8\_bin |
| utf8\_unicode\_ci |
| utf8\_tolower\_ci |
| utf8\_general\_mysql500\_ci |
| utf8mb4\_general\_ci |
| utf8mb4\_bin |
| utf8mb4\_unicode\_ci |

## 协议

从V9.0.5开始支持兼容MySQL协议。

新增mysql.protocol\_type参数，取值范围 ：mysql、pg，默认为mysql。通过端口mysql.port（默认为3306）连接。

- 当值为mysql时，允许用户从兼容MySQL协议工具连接到瀚高数据库；
- 当值为pg时，允许用户从psql连接到瀚高数据库。
	该参数值重启数据库生效。