---
title: "无法确定参数的数据类型问题"
book: "应用开发类"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/question/questionThree6.html"
tags:
  - highgo
  - highgo-v9
  - faq-application-development
---

#### 问题描述

应用代码报错如下：

```java
com.highgo.jdbc.util.PSQLException: 错误: 无法确定参数 $6 的数据类型
at com.highgo.jdbc.core.v3.QueryExecutorImpl.receiveErrorResponse(QueryExecutorImpl.java:2719)
at com.highgo.jdbc.core.v3.QueryExecutorImpl.processResults(QueryExecutorImpl.java:2402)
at com.highgo.jdbc.core.v3.QueryExecutorImpl.execute(QueryExecutorImpl.java:372)
at com.highgo.jdbc.jdbc.PgStatement.executeInternal(PgStatement.java:501)
at com.highgo.jdbc.jdbc.PgStatement.execute(PgStatement.java:418)
at com.highgo.jdbc.jdbc.PgPreparedStatement.executeWithFlags(PgPreparedStatement.java:238)
at com.highgo.jdbc.jdbc.PgPreparedStatement.executeQuery(PgPreparedStatement.java:154)
```

#### 环境信息

操作系统：Linux

数据库版本：HighgoV9\_O

#### 现象

应用代码执行sql语句报错，代码如下：

```java
StringBuilder sb = new StringBuilder();
sb.append(" select nvl(sxzfbl,0) sxzfbl,nvl(sm,'无') sm,nvl(xj,0) xj   ");
sb.append("   from si_medi_item_first_pay                              ");
sb.append("   where ylxmbm=? and zcbh=? and ? >= qsrq                  ");
sb.append("   and (? <= zzrq or zzrq is null)                          ");
sb.append("   and (xzbz=? or (xzbz='C' and ? is null))   ");
sb.append("   and nvl(rqlb,?)=?                                        ");
sb.append("   and ( yljglb is null or  instr(yljglb,?) > 0  )          ");
sb.append("   and (yyjb is null or instr(yyjb, ?) > 0 )                ");
sb.append("   and (yybm is null or instr(yybm, ?) > 0 )                ");

ps = conn.prepareStatement(sb.toString());
"ZA04BAQ0395020103845"
"370699MD3100001"
"20251217"
"20251217"
"C"
"C"
"B"
"B"
""
"1"
"180010"
rs = ps.executeQuery();
```

#### 原因分析

当调用 connection.prepareStatement(sql) 时，JDBC 驱动会把 SQL 语句发送给数据库服务器进行解析（parse）和计划（plan）。在这个阶段，数据库需要知道每一个参数占位符的数据类型，以便为查询生成正确的执行计划。

- 解析器会分析 SQL 语法树，为每个表达式推断类型。
- 对于 WHERE? IS NULL 这样的表达式，IS NULL 不限制左操作数的类型，所以解析器无法推断? 的类型，于是报告错误。

补充：为什么 setString 本身不足以告诉数据库类型？

setString 确实向 JDBC 驱动声明了“我要传一个字符串”，但驱动将这个信息传递给服务器时，通常是在绑定参数（bind）消息中。而绑定发生在解析/计划之后。如果解析阶段就失败了，绑定消息永远不会被发送。因此，类型信息必须在 SQL 文本中显式给出，或者在准备语句时通过某些数据库特定的语法传递，而标准 SQL 中只有显式转换能做到。

#### 解决方案

在 SQL 中显式指定参数类型，让解析器能顺利通过第一阶段：

```java
sb.append("   and (xzbz=? or (xzbz='C' and ? :: text is null))         ");
```

这里?::text 告诉数据库：这个参数将被当作 text 类型处理。解析器现在知道了类型，就能成功生成执行计划，后续 setString 才能正常绑定值。