---
title: "创建存储过程报错：syntax error at or near _PLSQL_UNIT_"
book: "数据库使用类"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/question/questionTwo7.html"
tags:
  - highgo
  - highgo-v9
  - faq-database-usage
---

**环境信息：**

数据库版本：hgdbv9.0.5

安装包名称：hgdbv9-05-0-0-5022-20251223-a09fff4-linux.x86\_64.bin

---

**场景描述：**

ORACLE存储过程中存在$$PLSQL\_UNIT，用来获取当前执行的存储过程的名字，目前V9-ORACLE模式不支持该语法，创建/编译的时候会报错，报错信息如下：

```
WARNING:  there was an compilation error
HINT:  syntax error at or near "PLSQL_UNIT"
```

**解决方案：**

将 $$PLSQL\_UNIT 修改为对应存储过程的名字大写；

**ORACLE示例：**

```
CREATE OR REPLACE PROCEDURE demo_plsql_unit_proc AS
    v_user_name VARCHAR2(50);
BEGIN
    DBMS_OUTPUT.PUT_LINE('开始执行程序单元: ' || $$PLSQL_UNIT);

    v_user_name := 'Admin';
    DBMS_OUTPUT.PUT_LINE(v_user_name || ' 正在操作...');
    
    DECLARE
        v_test NUMBER;
    BEGIN
        v_test := 1 / 0; 
    END;

EXCEPTION
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('------------------------------------');
        DBMS_OUTPUT.PUT_LINE('发生异常！');
        DBMS_OUTPUT.PUT_LINE('错误源头对象: ' || $$PLSQL_UNIT);
        DBMS_OUTPUT.PUT_LINE('错误详细信息: ' || SQLERRM);
        
END demo_plsql_unit_proc;
/

CALL demo_plsql_unit_proc();
```

**修改为HGDBV9：**

```
CREATE OR REPLACE PROCEDURE demo_plsql_unit_proc AS
    v_user_name VARCHAR2(50);
BEGIN
    DBMS_OUTPUT.PUT_LINE('开始执行程序单元: ' || 'DEMO_PLSQL_UNIT_PROC');

    v_user_name := 'Admin';
    DBMS_OUTPUT.PUT_LINE(v_user_name || ' 正在操作...');
    
    DECLARE
        v_test NUMBER;
    BEGIN
        v_test := 1 / 0; 
    END;

EXCEPTION
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('------------------------------------');
        DBMS_OUTPUT.PUT_LINE('发生异常！');
        DBMS_OUTPUT.PUT_LINE('错误源头对象: ' || 'DEMO_PLSQL_UNIT_PROC');
        DBMS_OUTPUT.PUT_LINE('错误详细信息: ' || SQLERRM);
        
END demo_plsql_unit_proc;
/
```