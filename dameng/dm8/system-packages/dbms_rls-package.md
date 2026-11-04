---
title: "DBMS_RLS 包"
book: "DM8 系统包使用手册"
version: "DM8"
source: https://eco.dameng.com/document/dm/zh-cn/pm/dbms_rls-package.html
tags:
  - dameng
  - dm8
  - system-packages
---

在某些系统中，权限控制必须定义到数据行访问权限的控制，此需求一般出现在同一系统中，不同的相对独立机构使用的情况。例如：集团下属多个子公司，所有子公司使用同一套数据表，但不同子公司的数据相对隔离。绝大多数人会选择在表或视图加上 WHERE 子句来进行数据访问控制，此方法编码工作量大、系统适应用户管理体系的弹性空间较小，因为一旦权限逻辑发生变动，就可能需要修改权限体系，导致所有的表或视图都必须修改。

为了解决上述问题，达梦提供了 DBMS\_RLS 包，DBMS\_RLS 包通过策略 POLICY 管理来实现数据行级安全（ROW LEVEL SECURITY，简称 RLS）访问控制。

在 INI 参数 ENABLE\_RLS 为 1 的前提下，用户需要提前调用系统过程 SP\_INIT\_RLS\_SYS(1);创建 DBMS\_RLS 包之后，方可使用 DBMS\_RLS 包中的函数或过程来实现数据行级安全访问控制。开启了 ENABLE\_RLS 参数后，需初始化 DBMS\_RLS 系统包，否则即使没有为用户表、视图对象设置策略，也无法对这些对象进行 DML 操作。

为兼容 V8.4.1.113 之前的版本，支持通过 SP\_CREATE\_SYSTEM\_PACKAGES(create\_flag, pkgname)且指定 pkgname 为'DBMS\_RLS'的方式创建或删除 DBMS\_RLS 系统包，但建议使用 SP\_INIT\_RLS\_SYS 进行创建或删除 DBMS\_RLS 系统包。

需要说明的是：1. 策略对于 SYSDBA 用户不会生效；2. DM MPP 环境下不支持 DBMS\_RLS 包。

## 14.1 策略函数

策略函数的模板如下所示：

```
FUNCTION POLICY_FUNCTION (
    OBJECT_SCHEMA    IN        VARCHAR2,    // 模式名。如果为空则表示当前模式。
    OBJECT_NAME        IN        VARCHAR2    // 对象名。仅支持表或视图
)RETURN VARCHAR2
```

> **注意**
> 
> 如果不是策略函数模板形式的函数，执行时会报错“策略函数xx错误”。

策略函数中两个输入参数，一个是用户输入参数，一个是对象输入参数。两个输入参数不能不写，尽管可以在函数中没有用到，否则报错返回。

策略函数返回一个字符串，作为 WHERE 子句中的条件表达式。DMDPC 环境下仅支持返回简单类型的条件表达式，例如简单的布尔表达式。

## 14.2 策略组

### 14.2.1 创建策略组

创建一个新的策略组。

**语法如下：**

```
PROCEDURE CREATE_POLICY_GROUP(
    OBJECT_SCHEMA    IN        VARCHAR := NULL,
    OBJECT_NAME        IN        VARCHAR,
    POLICY_GROUP    IN        VARCHAR
);
```

**参数详解**

- OBJECT\_SCHEMA
	包含由策略保护的表或视图的模式。
- OBJECT\_NAME
	由策略保护的表或视图的名称。
- POLICY\_GROUP
	添加到该对象的策略组名称。

**使用说明：**

1．如果 OBJECT\_SCHEMA 为 NULL，则使用调用过程的用户的当前模式。

2．对于受保护的每个对象（表或视图），策略组必须唯一。

### 14.2.2 删除策略组

删除一个策略组。

**语法如下：**

```
PROCEDURE DELETE_POLICY_GROUP(
    OBJECT_SCHEMA    IN        VARCHAR := NULL,
    OBJECT_NAME        IN        VARCHAR,
    POLICY_GROUP    IN        VARCHAR
);
```

**参数详解**

- OBJECT\_SCHEMA
	包含由策略保护的表或视图的模式。
- OBJECT\_NAME
	由策略保护的表或视图的名称。
- POLICY\_GROUP
	要删除该对象的策略组名称。

**使用说明：**

如果 OBJECT\_SCHEMA 为 NULL，则使用调用过程的用户的当前模式。

## 14.3 策略

### 14.3.1 创建策略

创建一个新的策略。

**语法如下：**

```
PROCEDURE ADD_POLICY(
    OBJECT_SCHEMA            IN        VARCHAR := NULL,
    OBJECT_NAME                IN        VARCHAR,
    POLICY_NAME                IN        VARCHAR,
    FUNCTION_SCHEMA            IN        VARCHAR := NULL,
    POLICY_FUNCTION            IN        VARCHAR,
    STATEMENT_TYPES            IN        VARCHAR := NULL,
    UPDATE_CHECK            IN        INT  := 0,
    ENABLE                    IN        INT  := 1,
    STATIC_POLICY            IN        INT  := 0,
    POLICY_TYPE                IN        INT := NULL,
    LONG_PREDICATE                    INT  := 0,
    SEC_RELEVANT_COLS        IN        VARCHAR  := NULL,
    SEC_RELEVANT_COLS_OPT    IN        INT := NULL
);
```

**参数详解**

- OBJECT\_SCHEMA
	包含由策略保护的表或视图的模式。
- OBJECT\_NAME
	由策略保护的表或视图的名称。
- POLICY\_NAME
	添加到该对象的策略名称。
- FUNCTION\_SCHEMA
	拥有策略函数的模式。
- POLICY\_FUNCTION
	策略函数名称。
- STATEMENT\_TYPES
	应用策略的 DML 语句类型。
- UPDATE\_CHECK
	该参数对于 INSERT 或 UPDATE 类型是可选项，缺省值为 0。
- ENABLE
	表示添加该策略时是否启用它，缺省值为 1。
- STATIC\_POLICY
	表策略是静态的，即对任何访问该对象的人产生相同的谓词字符串，该参数缺省值为 0。
- POLICY\_TYPE
	表示策略静态或动态类型，缺省为 NULL。如果 POLICY\_TYPE 不是 NULL，则覆盖 STATIC\_POLICY。可允许的值是 STATIC、SHARED\_STATIC、CONTEXT\_SENSITIVE、SHARED\_CONTEXT\_SENSITIVE 和 DYNAMIC。
- LONG\_PREDICATE
	表示谓词字符串是否是长谓词，该参数缺省为 0。
- SEC\_RELEVANT\_COLS
	只应用于表和视图，在列表中指定受保护的列，使用逗号或空格作为分隔符。
- SEC\_RELEVANT\_COLS\_OPT
	该参数的默认值为 NULL；如果不是缺省值，则必须指定.ALL\_ROWS，用于显示敏感列为 NULL 的所有列。

**使用说明：**

1. 如果 OBJECT\_SCHEMA 和 FUNCTION\_SCHEMA 为 NULL，则使用调用过程的用户的当前模式。
2. 对于受保护的每个对象（表或视图），策略名必须唯一。
3. POLICY\_FUNCTION 为针对 OBJECT\_NAME 的策略生成谓词。如果函数是程序包的一部分，则 POLICY\_FUNCTION 必须指定程序包名，用于限定策略函数名。
4. STATEMENT\_TYPES 允许的值以逗号或空格分隔，可以是 SELECT、INSERT、UPDATE、DELETE 和 INDEX 的任意组合。默认情况下，除了 INDEX 之外的所有类型都适用。对于列存储表（即 HUGE 表），仅支持 SELECT 类型语句。
5. 如果 UPDATE\_CHECK 参数为 1，则会检查 INSERT 或 UPDATE 对应的数据是否满足策略函数。不满足，则报错“违反策略检查约束”。
6. 不管 LONG\_PREDICATE 是 0，还是 1，谓词字符串最多可为 4000 字节。
7. STATIC\_POLICY 和 POLICY\_TYPE 暂不支持，所有谓词都是动态的。
8. ADD\_POLICY 没有指定策略组，则使用系统默认的策略组 SYS\_DEFAULT。
9. 不支持对临时表添加策略。

创建一个新的策略。用法与 ADD\_POLICY 基本相同，只是指定了策略所属的策略组 POLICY\_GROUP，POLICY\_GROUP 缺省值为系统策略组 SYS\_DEFAULT。

**语法如下：**

```
PROCEDURE ADD_GROUPED_POLICY(
    OBJECT_SCHEMA           IN         VARCHAR := NULL,
    OBJECT_NAME             IN         VARCHAR,
    POLICY_GROUP               IN         VARCHAR := 'SYS_DEFAULT',
    POLICY_NAME             IN         VARCHAR,
    FUNCTION_SCHEMA         IN         VARCHAR := NULL,
    POLICY_FUNCTION         IN         VARCHAR,
    STATEMENT_TYPES         IN         VARCHAR := NULL,
    UPDATE_CHECK            IN         INT  := 0,
    ENABLE                    IN         INT  := 1,
    STATIC_POLICY            IN         INT  := 0,
    POLICY_TYPE                IN         INT := NULL,
    LONG_PREDICATE                    INT  := 0,
    SEC_RELEVANT_COLS        IN         VARCHAR  := NULL,
    SEC_RELEVANT_COLS_OPT    IN         INT := NULL
);
```

### 14.3.2 启用策略

启用一个策略。

**语法如下：**

```
PROCEDURE ENABLE_POLICY(
    OBJECT_SCHEMA     IN         VARCHAR := NULL,
    OBJECT_NAME       IN         VARCHAR,
    POLICY_NAME       IN         VARCHAR,
    ENABLE            IN         INT := 1 
);
```

**参数详解**

- OBJECT\_SCHEMA
	包含由策略保护的表或视图的模式。
- OBJECT\_NAME
	由策略保护的表或视图的名称。
- POLICY\_NAME
	启用该对象的策略名称。
- ENABLE
	表示是否启用该策略，默认值为 1。0 表示禁用，1 表示启用。

**使用说明：**

1．如果 OBJECT\_SCHEMA 为 NULL，则使用调用过程的用户的当前模式。

2．ENABLE\_POLICY 没有指定策略组，则使用系统默认的策略组 SYS\_DEFAULT。

启用一个策略。用法与 ENABLE\_POLICY 基本相同，只是指定了策略所属的策略组 GROUP\_NAME。

**语法如下：**

```
PROCEDURE ENABLE_GROUPED_POLICY(
    OBJECT_SCHEMA     IN         VARCHAR := NULL,
    OBJECT_NAME       IN         VARCHAR,
    GROUP_NAME        IN         VARCHAR,
    POLICY_NAME       IN         VARCHAR,
    ENABLE            IN         INT := 1
);
```

### 14.3.3 禁用策略

禁用一个策略。

**语法如下：**

```
PROCEDURE DISABLE_GROUPED_POLICY(
    OBJECT_SCHEMA     IN         VARCHAR := NULL,
    OBJECT_NAME       IN         VARCHAR,
    GROUP_NAME        IN         VARCHAR,
    POLICY_NAME       IN         VARCHAR
);
```

**参数**

- OBJECT\_SCHEMA
	包含由策略保护的表或视图的模式。
- OBJECT\_NAME
	由策略保护的表或视图的名称。
- GROUP\_NAME
	指定策略所属的策略组名称
- POLICY\_NAME
	禁用该对象的策略名称。

**使用说明：**

如果 OBJECT\_SCHEMA 为 NULL，则使用调用过程的用户的当前模式。

### 14.3.4 删除策略

删除一个策略。

**语法如下：**

```
PROCEDURE DROP_POLICY(
    OBJECT_SCHEMA     IN         VARCHAR := NULL,
    OBJECT_NAME       IN         VARCHAR,
    POLICY_NAME       IN         VARCHAR
);
```

**参数详解**

- OBJECT\_SCHEMA
	包含由策略保护的表或视图的模式。
- OBJECT\_NAME
	由策略保护的表或视图的名称。
- POLICY\_NAME
	要删除该对象的策略名称。

**使用说明：**

1．如果 OBJECT\_SCHEMA 为 NULL，则使用调用过程的用户的当前模式。

2．DROP\_POLICY 没有指定策略组，则使用系统默认的策略组 SYS\_DEFAULT。

删除一个策略。用法与 DROP\_POLICY 基本相同，只是指定了策略所属的策略组 POLICY\_GROUP，POLICY\_GROUP 默认值为系统策略组 SYS\_DEFAULT。

**语法如下：**

```
PROCEDURE DROP_GROUPED_POLICY(
    OBJECT_SCHEMA     IN         VARCHAR := NULL,
    OBJECT_NAME       IN         VARCHAR,
    POLICY_GROUP      IN         VARCHAR := 'SYS_DEFAULT',
    POLICY_NAME       IN         VARCHAR
);
```

## 14.4 上下文

### 14.4.1 创建上下文策略

创建一个上下文策略。

**语法如下：**

```
PROCEDURE ADD_POLICY_CONTEXT(
    OBJECT_SCHEMA       IN         VARCHAR := NULL,
    OBJECT_NAME         IN         VARCHAR,
    NAMESPACE           IN         VARCHAR,
    ATTRIBUTE           IN         VARCHAR
);
```

**参数详解**

- OBJECT\_SCHEMA
	包含由策略保护的表或视图的模式。
- OBJECT\_NAME
	由策略保护的表或视图的名称。
- NAMESPACE
	添加到该对象的上下文名称。
- ATTRIBUTE
	策略对应上下文的属性名称。

**使用说明：**

1．如果 OBJECT\_SCHEMA 为 NULL，则使用调用过程的用户的当前模式。

2．对于受保护的每个对象（表或视图），同一上下文的属性名必须唯一。

### 14.4.2 删除上下文策略

删除一个上下文策略。

**语法如下：**

```
PROCEDURE DROP_POLICY_CONTEXT(
    OBJECT_SCHEMA       IN         VARCHAR := NULL,
    OBJECT_NAME         IN         VARCHAR,
    NAMESPACE           IN         VARCHAR,
    ATTRIBUTE           IN         VARCHAR
);
```

**参数详解**

- OBJECT\_SCHEMA
	包含由策略保护的表或视图的模式。
- OBJECT\_NAME
	由策略保护的表或视图的名称。
- NAMESPACE
	添加到该对象的上下文名称。
- ATTRIBUTE
	策略对应上下文的属性名称。

**使用说明：**

如果 OBJECT\_SCHEMA 为 NULL，则使用调用过程的用户的当前模式。

## 14.5 启用状态检测语句

系统的 DBMS\_RLS 系统包启用状态检测。

**语法如下：**

```
INTEGER
SF_CHECK_RLS_SYS();
```

**返回值**

0：未启用；1：已启用

**举例说明**

获得 DBMS\_RLS 系统包的启用状态。

```
select SF_CHECK_RLS_SYS();
```

## 14.6 举例说明

创建 DBMS\_RLS 包之前，需先将 INI 参数 ENABLE\_RLS 设置为 1，之后才可以成功使用包中的过程或函数。

```
ALTER SYSTEM SET 'ENABLE_RLS' =1 SPFILE; --因为是静态参数，设置完需重启服务器
```

调用系统过程创建系统包。

```
SP_INIT_RLS_SYS(1);
```

例 1 通过策略过滤用户对表数据的访问控制

```
数据准备：
    CONN SYSDBA/DMdba_123  --以SYSDBA身份连接服务器
    SP_INIT_RLS_SYS(1);
    CREATE USER USER01 IDENTIFIED BY "USER01_psd";
    GRANT DBA TO USER01;
    CONN USER01/USER01_psd  --以USER01身份连接服务器

第一步：建立测试数据表(T_POLICY):
    CREATE TABLE T_POLICY( T1  VARCHAR2(10), T2  NUMBER(10));
    INSERT INTO T_POLICY VALUES('A',10);
    INSERT INTO T_POLICY VALUES('B',20);
    INSERT INTO T_POLICY VALUES('C',30);
    COMMIT;

第二步：建立测试POLICY的函数:
    CREATE OR REPLACE FUNCTION FN_GETPOLICY(
        P_SCHEMA IN VARCHAR2,
        P_OBJECT IN VARCHAR2
        ) RETURN VARCHAR2 IS RESULT VARCHAR2(1000);
    BEGIN  
        RESULT:='T2 NOT IN (10)';
        RETURN(RESULT);
    END;
    /

第三步：加入POLICY:
    DBMS_RLS.ADD_POLICY(
    OBJECT_SCHEMA =>'USER01',  //数据表(或视图)所在的SCHEMA名称
    OBJECT_NAME =>'T_POLICY', //数据表(或视图)的名称
    POLICY_NAME =>'T_TESTPOLICY', //POLICY的名称，主要用于将来对POLICY的管理
    FUNCTION_SCHEMA =>'USER01',  //返回WHERE子句的函数所在SCHEMA名称
    POLICY_FUNCTION =>'FN_GETPOLICY', //返回WHERE子句的函数名称
    STATEMENT_TYPES =>'SELECT,INSERT,UPDATE,DELETE', //要使用该POLICY的DML类型
    UPDATE_CHECK =>1,  //仅适用于STATEMENT_TYPE为'INSERT,UPDATE'，值为1或    0
    ENABLE =>1    //是否启用，值为1或0
    );

第四步：查询数据表(T_POLICY):
    SELECT * FROM T_POLICY;
    //查询结果如下：
    行号 T1 T2
    1 B 20
    2 C 30
    //从查询结果中可以看出少了T2=10这行数据。

第五步：检查更新数据
    UPDATE T_POLICY SET T2 = 10;
    //运行结果如下：
    [-6614]:违反策略检查约束.
    //注：如果UPDATE_CHECK设为1，则用户插入的值不符合POLICY_FUNCTION返回条件时，该DML执行返回错误信息。

第六步：禁用POLICY
     DBMS_RLS.ENABLE_POLICY('USER01','T_POLICY','T_TESTPOLICY',0);
    SELECT * FROM T_POLICY;
    //查询结果如下：
    行号 T1 T2
    1   A  10
    2   B  20
    3   C  30
    //从查询结果中可以看到T2=10这行数据。

第七步：删除POLICY
    DBMS_RLS.DROP_POLICY('USER01','T_POLICY','T_TESTPOLICY');
```

例 2 上下文在数据访问控制中的使用

```
数据准备：
    CONN SYSDBA/DMdba_123   --以SYSDBA身份连接服务器
    CREATE USER MYKGIS IDENTIFIED BY "MYKGIS_psd_123";
    GRANT DBA TO MYKGIS;
    CONN MYKGIS/MYKGIS_psd_123   --以MYKGIS身份连接服务器
    SP_INIT_RLS_SYS(1);
    SP_CREATE_SYSTEM_PACKAGES(1,'DBMS_SESSION');

    DROP TABLE EMPLOYEE;
    CREATE TABLE EMPLOYEE (
        EMPID INT, FIRSTNAME VARCHAR(20),
        LASTNAME VARCHAR(20),
        LOCATION VARCHAR(20) ,
        DEPARTMENT VARCHAR(20)
    );
    INSERT INTO EMPLOYEE VALUES(1, 'STEVE', 'MILLER', 'GA', 'IT');
    INSERT INTO EMPLOYEE VALUES(2, 'SCOTT', 'TIGER', 'GA', 'HR');
    INSERT INTO EMPLOYEE VALUES(3, 'TOM', 'LUTZ', 'FL', 'HR');
    INSERT INTO EMPLOYEE VALUES(4, 'HARRY', 'MYKGIS', 'FL', 'IT');
    COMMIT;

    DROP TABLE ORDERS;
    CREATE TABLE ORDERS(
        ORDER_ID INT, AMOUNT FLOAT,
         LOCATION VARCHAR(20),
         DEPARTMENT VARCHAR(20)
    );
    INSERT INTO ORDERS VALUES(1, 3454.45, 'GA', 'IT');
    INSERT INTO ORDERS VALUES(2, 324893.34, 'FL', 'IT');
    INSERT INTO ORDERS VALUES(3, 34545.11, 'FL', 'HR');
    INSERT INTO ORDERS VALUES(4, 234.99, 'GA', 'HR');
    COMMIT;

第一步：创建上下文
    CREATE CONTEXT DRIVECTX USING MYKGIS.APPSEC;

    //创建上下文所使用的包
    CREATE OR REPLACE PACKAGE MYKGIS.APPSEC AS
    V_DEPARTMENT VARCHAR2(2);
    V_LOCATION VARCHAR2(2);
    PROCEDURE SETCONT(POLICY_GROUP VARCHAR2);
    END;
    /

    //创建上下文所使用的包体
    CREATE OR REPLACE PACKAGE BODY MYKGIS.APPSEC AS
    PROCEDURE SETCONT(POLICY_GROUP VARCHAR2) AS
    V_DEPARTMENT VARCHAR2(2);
    V_LOCATION VARCHAR2(2);
    BEGIN
    DBMS_SESSION.SET_CONTEXT('DRIVECTX','ACTIVE_APP',POLICY_GROUP);
    SELECT DEPARTMENT INTO V_DEPARTMENT
    FROM MYKGIS.EMPLOYEE WHERE LASTNAME = SYS_CONTEXT('USERENV','SESSION_USER');
    DBMS_SESSION.SET_CONTEXT('DRIVECTX','DEPARTMENT',V_DEPARTMENT);
    SELECT LOCATION INTO V_LOCATION
    FROM MYKGIS.EMPLOYEE WHERE LASTNAME = SYS_CONTEXT('USERENV','SESSION_USER');
    DBMS_SESSION.SET_CONTEXT('DRIVECTX','LOCATION',V_LOCATION);
    END;
    END;
    /

第二步：为表ORDERS定义上下文
    DBMS_RLS.ADD_POLICY('MYKGIS','ORDERS','DRIVECTX','ACTIVE_APP');
  
第三步：创建策略函数
    CREATE OR REPLACE FUNCTION MYKGIS.DEP_POLICY(D1 VARCHAR2, D2 VARCHAR2)
    RETURN VARCHAR2 AS
    BEGIN
    RETURN 'DEPARTMENT = SYS_CONTEXT(''DRIVECTX'', ''DEPARTMENT'')';
    END;
    /
    CREATE OR REPLACE FUNCTION MYKGIS.LOC_POLICY(D1 VARCHAR2, D2 VARCHAR2)
    RETURN VARCHAR2 AS
    BEGIN
    RETURN 'LOCATION = SYS_CONTEXT(''DRIVECTX'', ''LOCATION'')';
    END;
    /

第四步：创建策略组
    DBMS_RLS.CREATE_POLICY_GROUP('MYKGIS','ORDERS','DEPARTMENT');
    DBMS_RLS.CREATE_POLICY_GROUP('MYKGIS','ORDERS','LOCATION');

第五步：创建策略                                                  
    DBMS_RLS.ADD_GROUPED_POLICY('MYKGIS','ORDERS','DEPARTMENT',
   'DEP_SECURITY','MYKGIS','DEP_POLICY');    
    DBMS_RLS.ADD_GROUPED_POLICY('MYKGIS','ORDERS','LOCATION',
   'LOC_SECURITY','MYKGIS','LOC_POLICY');

第六步：设置上下文中的策略组
    MYKGIS.APPSEC.SETCONT('DEPARTMENT');  
    //查询策略函数返回结果：
    SELECT MYKGIS.DEP_POLICY('MYKGIS', 'EMPLOYEE') FROM DUAL;
    //查询结果如下：
    DEPARTMENT = SYS_CONTEXT('DRIVECTX', 'DEPARTMENT')
    //查询上下文的属性值
    SELECT * FROM V$CONTEXT WHERE NAMESPACE = 'DRIVECTX';
    //查询结果如下：
    NAMESPACE ATTRIBUTE  VALUE
    --------- ---------- ----------
    DRIVECTX  ACTIVE_APP DEPARTMENT
    DRIVECTX  DEPARTMENT IT
    DRIVECTX  LOCATION   FL

第七步：查询表
    SELECT * FROM ORDERS;
    //查询结果如下：
    ORDER_ID    AMOUNT                    LOCATION DEPARTMENT
    ----------- ------------------------- -------- ----------
    1           3.454450000000000E+003    GA       IT
    2           3.248933400000000E+005    FL       IT
    //从查询结果中可以看出过滤掉了DEPARTMENT不是IT的数据。

第八步：重新设置上下文中的策略组
    MYKGIS.APPSEC.SETCONT('LOCATION');  
    //查询策略函数返回结果：
    SELECT MYKGIS.LOC_POLICY('MYKGIS', 'EMPLOYEE') FROM DUAL;
    //查询结果如下：
    LOCATION = SYS_CONTEXT('DRIVECTX', 'LOCATION')

    SELECT * FROM ORDERS;
    //查询结果如下：
    ORDER_ID    AMOUNT                    LOCATION DEPARTMENT
    ----------- ------------------------- -------- ----------
    2           3.248933400000000E+005    FL       IT
    3           3.454511000000000E+004    FL       HR
    //从查询结果中可以看出过滤掉了LOCATION不是FL的数据。
```