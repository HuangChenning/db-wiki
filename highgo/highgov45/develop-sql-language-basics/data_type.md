---
title: "7.数据类型"
book: "HGDB-SEE V4.5 SQL语言基础"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/develop/data_type.html"
tags:
  - highgo
  - highgo-v45
  - develop-sql-language-basics
---

## 字符类型

| 名字 | 描述 |
| --- | --- |
| character varying(n)，varchar(n) | 有限制的变长 |
| character(n)，char(n) | 定长，空格填充 |
| text | 无限变长 |

n 是一个正整数，character varying(n) 、varchar(n) 、character(n)、char(n) 将存储长度不超过 n 位的的串。text 类型可以存储任何长度的串。这三种类型之间没有性能差别，只是 character(n) 由于可能需要额外的存储开销，因而在大多数情况下，text 或者 character varying 是更好的选择。

如果串的长度小于 n，character(n) 和 char(n) 将会用空白对剩余的长度进行填充，而 character varying(n) 和 varchar(n) 将直接存储串的内容，不会对剩余的长度进行填充。character 结尾的空白在进行两个值比较时不会进行考虑，character varying 和 text 结尾的空白语意上是有含义的，在模式匹配时会进行考虑。没有长度声明的 character 等效于 character(1)，没有长度声明的 character varying 接受任何长度的串。varchar(n) 和 char(n) 的概念分别是 character varying(n) 和 character(n) 的别名。