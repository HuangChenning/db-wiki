---
title: "不可见列"
book: "Oracle兼容性"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/compatibility/compOracle17.html"
tags:
  - highgo
  - highgo-v9
  - compatibility-oracle
---

## 不可见列

## 说明

使用SELECT语句查询时，如果要显示不可见列信息，必须显式指定该不可见列。同理插入表时，如果需要向不可见列中插入数据，需要显式指定不可见列，如果没有指定不可见列，那么只能将数据插入可见列中。

在创建表或者新增列语句中使列不可见，也可以在之后更改不可见列为可见列。或者可以将可见列更改为不可见列，以下语法图仅展示与不可见列相关语法内容：

## 示例

highgo=# CREATE TABLE tab1 (id NUMBER,description VARCHAR2(50) INVISIBLE);

CREATE TABLE

#查看表结构，不显示description列

highgo=# \\d tab1

数据表 “public.tab1”

栏位 | 类型 | 校对规则 | 可空的 | 预设

\-—–+——–+———-+——–+——

id | number | | |

highgo=# INSERT INTO tab1 VALUES (1);

INSERT 0 1

highgo=# SELECT \* FROM tab1;

id

\-—

1

(1 行记录)

highgo=# INSERT INTO tab1 (id, description) VALUES (2, ‘TWO’);

INSERT 0 1

highgo=# SELECT id, description FROM tab1;

id | description

\-—+————-

1 |

2 | TWO

(2 行记录)

#不显示指定description列

highgo=# select \* from tab1;

id

\-—

1

2

(2 行记录)

#显示隐藏列

highgo=# SET COLINVISIBLE to ON;

SET

highgo=# \\d tab1

数据表 “public.tab1”

栏位 | 类型 | 校对规则 | 可空的 | 预设

\-————+————–+———-+——–+——

id | number | | |

description | varchar2(50) | | |

highgo=# SET COLINVISIBLE to OFF;

SET

highgo=# drop table tab1;

DROP TABLE