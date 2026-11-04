---
title: "输出打印信息问题"
book: "迁移兼容类"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/question/questionOne3.html"
tags:
  - highgo
  - highgo-v9
  - faq-migration-compatibility
---

##### 问题现象

在存储过程调试的时候使用DBMS\_OUTPUT.PUT\_LINE来进行打印输出报错。

```bash
CREATE OR REPLACE PROCEDURE testsum()
IS
intsum number;
BEGIN
select 1+2 into intsum ; 
DBMS_OUTPUT.PUT_LINE('SUM:' || intsum);
END testsum;
/
#调用
call testsum();
```

![4_1](img/4_1.webp)

##### 解决方案

###### 使用raise notice替换

DBMS\_OUTPUT.PUT\_LINE(‘SUM:’ || intsum); 改成 raise notice ‘SUM:%’,intsum;

![4_2](img/4_2.webp)

###### 创建一个同名的存储过程

```bash
CREATE OR REPLACE PACKAGE SYS.DBMS_OUTPUT IS
    PROCEDURE PUT_LINE(I_MESS VARCHAR2);
END DBMS_OUTPUT;
/
CREATE OR REPLACE PACKAGE BODY SYS.DBMS_OUTPUT IS
    PROCEDURE PUT_LINE(I_MESS VARCHAR2) IS
    BEGIN
        RAISE NOTICE '%',I_MESS;
    END;
END DBMS_OUTPUT;
/
grant execute on package dbms_output to public;
```

![4_3](img/4_3.webp)

![4_4](img/4_4.webp)