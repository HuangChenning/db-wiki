---
title: "函数索引不支持的系统函数列表"
book: "数据库对象管理"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001501848.html"
tags:
  - oceanbase
  - distributed
  - ref-database-object-management
---

# 函数索引不支持的系统函数列表

在 OceanBase 数据库的 Oracle 模式中，对函数索引的表达式进行了限制。本节主要列出了禁止用于函数索引的系统函数。

## 非用户性的系统函数

非用户性的系统函数默认全部禁止用于函数索引。

## 其他系统函数

以下系统函数禁止用于函数索引。

|--------------------|-------------------|----------------|---------------------|
| AT LOCAL            | AT TIME ZONE         | CARDINALITY         | CHARSET              |
| COERCIBILITY        | COLLATION            | CONNECT_BY_PATH     | CURRENT_DATE         |
| CURRENT_TIMESTAMP   | DBTIMEZONE           | DECODE              | DEFAULT              |
| DUMP                | EXTRACT              | HOST_IP             | IS_SERVING_TENANT    |
| LAST_TRACE_ID       | LNNVL                | LOCALTIMESTAMP      | OB_VERSION           |
| REGEXP_COUNT        | REGEXP_INSTR         | REGEXP_LIKE         | REGEXP_REPLACE       |
| REGEXP_SUBSTR       | ROWNUM               | RPC_PORT            | ROWID_TO_CHAR        |
| ROWIDIDTONCHAR      | SCN_TO_TIMESTAMP     | SESSIONTIMEZONE     | SYS_CONTEXT          |
| SYS_GUID            | SYSDATE              | SYSTIMESTAMP        | TIMESTAMP_TO_SCN     |
| UID                 | USER                 | USERENV             | VALUES               |
