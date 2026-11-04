---
title: "DBMS_DDL 包"
book: "DM8 系统包使用手册"
version: "DM8"
source: https://eco.dameng.com/document/dm/zh-cn/pm/dbms_ddl-package.html
tags:
  - dameng
  - dm8
  - system-packages
---

DBMS\_DDL 包用于加密 CREATE OR REPLACE 语句。

DBMS\_DDL 包的使用依赖 DBMS\_SQL 包，在创建 DBMS\_DDL 包时，系统会自动创建 DBMS\_SQL 包。

## 53.1 相关方法

1. CREATE\_WRAPPED

该过程用于加密 CREATE OR REPLACE 语句，同时执行该语句创建相应的对象。

**语法如下：**

```
PROCEDURE CREATE_WRAPPED (

  ddl   VARCHAR2

);

或

PROCEDURE CREATE_WRAPPED(

  ddl   DBMS_SQL.VARCHAR2A, 

  lb   PLS_INTEGER, 

  ub   PLS_INTEGER

);

或

PROCEDURE CREATE_WRAPPED(

  ddl   DBMS_SQL.VARCHAR2S, 

  lb    PLS_INTEGER,

  ub   PLS_INTEGER

);
```

**参数详解**

- DDL：CREATE OR REPLACE 语句，可以创建包规范、包主体、函数、过程、类型、类型体。
- LB：指定 CREATE OR REPLACE 语句的字符串表中索引的下限。
- UB：指定 CREATE OR REPLACE 语句的字符串表中索引的上限。

**返回值**

无

2. WRAP

该函数用于加密 CREATE OR REPLACE 语句。

**语法如下：**

```
FUNCTION WRAP(

  ddl   VARCHAR2

) RETURN CLOB;

或

FUNCTION WRAP(

  ddl   DBMS_SQL.VARCHAR2S, 

  lb    PLS_INTEGER, 

  ub    PLS_INTEGER

) RETURN DBMS_SQL.VARCHAR2S;

或

FUNCTION WRAP(

  ddl   DBMS_SQL.VARCHAR2A, 

  lb    PLS_INTEGER, 

  ub    PLS_INTEGER

) RETURN DBMS_SQL.VARCHAR2A;
```

**参数详解**

- DDL：CREATE OR REPLACE 语句，可以创建包规范、包主体、函数、过程、类型、类型体。
- LB：指定 CREATE OR REPLACE 语句的字符串表中索引的下限。
- UB：指定 CREATE OR REPLACE 语句的字符串表中索引的上限。

**返回值**

加密后的 CREATE OR REPLACE 语句。

## 53.2 举例说明

使用包内的过程和函数之前，如果还未创建过系统包，请先调用系统过程创建系统包。

```
SP_CREATE_SYSTEM_PACKAGES (1,'DBMS_DDL');
SET SERVEROUTPUT ON;  //PRINT需要设置这条语句，才能打印出消息
```

使用 CREATE\_WRAPPED 过程加密 CREATE OR REPLACE 语句。

```
DECLARE
    l_source DBMS_SQL.VARCHAR2A;
    l_wrap DBMS_SQL.VARCHAR2A;
BEGIN
    l_source(1) := 'CREATE OR REPLACE FUNCTION get_date_string RETURN VARCHAR2 AS ';
    l_source(2) := 'BEGIN ';
    l_source(3) := 'RETURN TO_CHAR(SYSDATE, ''DD-MON-YYYY''); ';
    l_source(4) := 'END get_date_string;';
    SYS.DBMS_DDL.CREATE_WRAPPED(ddl => l_source, lb => 1, ub => l_source.count);
END;
/
```

CREATE\_WRAPPED 过程加密语句的同时会执行该语句创建相应的对象，上例中的 get\_date\_string 函数已被创建完成，如下所示：

```
SELECT get_date_string();
行号     GET_DATE_STRING()
---------- -----------------
1          20-5月-2025
```

查看加密后的 CREATE OR REPLACE 语句。

```
SELECT TEXT FROM USER_SOURCE WHERE NAME = 'GET_DATE_STRING' AND TYPE = 'FUNCTION';
行号     TEXT
---------- -------------------------------------------------------------
1          CREATE  OR REPLACE  FUNCTION GET_DATE_STRING WRAPPED 'D56115210851B1C18565051561F1B108088551155585B10808954185C12141858C080841C508A0088151D161B108A0088551155585B10815F1F5C121418528C565C5114115513808D811117871F1B17865656565D868ECA00851B11108D15115F511411551F5C5158561B1D1EC08A0';
```