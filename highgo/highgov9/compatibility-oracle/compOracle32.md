---
title: "动态SQL"
book: "Oracle兼容性"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/compatibility/compOracle32.html"
tags:
  - highgo
  - highgo-v9
  - compatibility-oracle
---

## 动态SQL

动态 SQL 是一种在运行时生成和运行 SQL语句的编程方法。在编写通用且灵活的程序（如临时查询系统）时、编写必须运行数据库定义语言(DDL) 语句的程序时，或者在编译时不知道 SQL语句的全文或其输入和输出变量的数量或数据类型时，它很有用。

Oracle中提供两种编写动态 SQL 的方法：

- 本地动态SQL

本地动态SQL，用于构建和运行动态 SQL 语句。

- DBMS\_SQL 包（V9暂不支持）

用于构建、运行和描述动态 SQL 语句的 API。

说明：

- 该功能在V9.0.5及以后的版本中支持。
- 目前，瀚高数据库管理系统V9暂不支持DBMS\_SQL 包，仅支持本地动态SQL。

## 本地动态SQL

本地动态SQL使用 EXECUTE IMMEDIATE 语句处理大多数动态 SQL 语句。

在Oracle中，如果动态 SQL 语句是返回多行的 SELECT 语句，则本地动态SQL提供以下两种方式：

- 使用带有 BULK COLLECT INTO 子句的 EXECUTE IMMEDIATE  
	语句。（V9暂不支持）
- 使用 OPEN FOR、FETCH 和 CLOSE 语句。

目前在瀚高数据库管理系统V9中暂不支持BULK COLLECT INTO 子句，仅支持使用OPEN FOR、FETCH 和 CLOSE 语句。

SQL 游标属性在本地动态SQL中的INSERT、UPDATE、DELETE、MERGE 和单行 SELECT 语句后的工作方式与它们在静态 SQL 中相同。

### EXECUTE IMMEDIATE 语句

语法：

EXECUTE IMMEDIATE sql\_statement

\[USING \[\[IN\]\[OUT\]\]varname\[,...\]\]

\[{RETURNING|RETURN} INTO varname\[,...\]\]

如果动态 SQL 语句没有绑定变量的占位符,并且它可能返回的唯一结果是异常,则EXECUTE IMMEDIATE 语句不需要子句。

如果动态 SQL 语句包含绑定变量的占位符，则每个占位符必须在 EXECUTEIMMEDIATE 语句的相应子句中具有对应的绑定变量，如下所示：

- 如果动态 SQL 语句是最多可以返回一行的 SELECT 语句，则将out-bind变量放在 INTO 子句中，将in-bind 变量放在 USING 子句中。
- 如果动态 SQL 语句是没有 RETURNING INTO 子句的 DML 语句，而不是SELECT，则将所有绑定变量放在 USING 子句中。
- 如果动态 SQL 语句是带有 RETURNING INTO 子句的 DML 语句，则将 in-bind变量放在 USING 子句中，将out-bind 变量放在 RETURNING INTO 子句中。
- 如果动态 SQL 语句是匿名 PL/iSQL 块或 CALL 语句，则将所有绑定变量放在USING 子句中。

如果动态 SQL 语句调用子程序，需确保：

- 子程序必须是模式级别下创建，或包规范中声明和定义。每个与子程序参数占位符对应的绑定变量都具有与子程序参数相同的参数模式和与子程序参数兼容的数据类型。
- 绑定的变量不能是保留字NULL。要解决此限制，请在要使用 NULL的地方使用未初始化的变量，如下文示例”初始化的变量在 USING 子句中表示NULL”。
- 绑定的变量必须是 SQL 支持的数据类型。
- 如果数据类型是集合或记录类型，则必须在包规范中声明。

#### 示例

##### 标准SQL语句

EXECUTE IMMEDIATE 支持以下语句：

- DML：SELECT、 INSERT、 UPDATE、 DELETE、MERGE、COPY等
- DDL：CREATE、ALTER、 DROP、TRUNCATE、COMMENT、ALTER  
	DATABASE、STATISTICS等
- DCL：GRANT、 REVOKE等
- CHECKPOINT、ANALYZE、EXPLAIN \[ANALYZE\]、SET方式设置GUC参数。

EXECUTE IMMEDIATE 不支持以下语句：

- VACUUM
- ALTER SYSTEM
- COMMIT、SAVEPOINT、ROLLBACK等事务操作语句。

使用EXECUTE IMMEDIATE 执行CREATE TABLE的示例：

DROP TABLE IF EXISTS tb\_dsql;

DECLARE

dyn\_stmt VARCHAR2(100);

tb\_name VARCHAR2(100):= 'tb\_dsql';

BEGIN

dyn\_stmt:= 'create table ' || tb\_name || '(empno int, empnm  
varchar2(30))';

EXECUTE IMMEDIATE dyn\_stmt;

END;

/

需要注意的是DDL语句中的对象名（如表名）不能使用绑定变量。上述语句改写成使用绑定变量的形式，则会报错。

DROP TABLE IF EXISTS tb\_dsql;

DECLARE

dyn\_stmt VARCHAR2(200);

tb\_name VARCHAR2(100):= 't\_dsql';

BEGIN

dyn\_stmt:= 'create table ' ||:tb\_name || '( aa  
varchar2(100))';

EXECUTE IMMEDIATE dyn\_stmt USING tb\_name;

END;

/

报错如下：

Bind variable "tb\_name" not declared.

##### 动态 PL/iSQL 块调用子程序

在本例中，动态 PL/iSQL 块是一个匿名 PL/iSQL块，它调用一个在模式级别下创建的子程序。

DROP TABLE IF EXISTS student;

CREATE TABLE student (id int PRIMARY KEY, name text, score number);

DROP SEQUENCE IF EXISTS student\_seq;

CREATE SEQUENCE student\_seq start with 1;

CREATE OR REPLACE PROCEDURE create\_stu (

stuid IN OUT NUMBER,

name IN VARCHAR2,

score IN NUMBER

) AUTHID DEFINER AS

BEGIN

stuid:= student\_seq.NEXTVAL;

INSERT INTO student VALUES (stuid, name, score);

END;

/

DECLARE

plsql\_block VARCHAR2(500);

new\_stuid NUMBER(4);

new\_name VARCHAR2(30):= 'xx';

new\_score NUMBER(6):= 99;

BEGIN

\-- dynamic PL/iSQL block invokes subprogram:

plsql\_block:= 'BEGIN create\_stu(:a,:b,:c); END;';

EXECUTE IMMEDIATE plsql\_block

USING IN OUT new\_stuid, new\_name, new\_score;

END;

/

查看表student：

select \* from student;

id | name | score

\----+------+-------

1 | xx | 99

(1 行记录)

##### 使用 BOOLEAN 形式参数动态调用子程序

在此示例中，动态 PL/iSQL 块是一个匿名 PL/iSQL 块，它调用形参是数据类型BOOLEAN 的子程序。

CREATE OR REPLACE PROCEDURE p (x BOOLEAN) AUTHID DEFINER AS

BEGIN

IF x THEN

RAISE NOTICE 'x is true';

END IF;

END;

/

DECLARE

dyn\_str VARCHAR2(200);

b BOOLEAN:= TRUE;

BEGIN

dyn\_str:= 'BEGIN p(:x); END;';

EXECUTE IMMEDIATE dyn\_str USING b;

END;

/

输出：

NOTICE: x is true

##### 动态调用使用 RECORD 形式参数的子程序

在此示例中，动态 PL/iSQL 块是一个匿名 PL/iSQL 块，它调用形参具有PL/iSQL（但不是 SQL）数据类型 RECORD的子程序。RECORD类型在包规范中声明，子程序在包规范中声明并在包体中定义。

CREATE OR REPLACE PACKAGE pkg AUTHID DEFINER AS

TYPE rec IS RECORD (n1 NUMBER, n2 NUMBER);

PROCEDURE p (i OUT rec, j NUMBER, k NUMBER);

END pkg;

/

CREATE OR REPLACE PACKAGE BODY pkg AS

PROCEDURE p (i OUT rec, j NUMBER, k NUMBER) AS

BEGIN

i.n1:= j;

i.n2:= k;

END p;

END pkg;

/

DECLARE

r pkg.rec;

dyn\_str VARCHAR2(3000);

BEGIN

dyn\_str:= 'BEGIN pkg.p(:x, 3, 4); END;';

EXECUTE IMMEDIATE dyn\_str USING OUT r;

RAISE NOTICE 'r = %', r;

END;

/

输出：

NOTICE: r = (3,4)

##### 未初始化的变量在 USING 子句中表示 NULL

此示例使用未初始化的变量来表示 USING 子句中的保留字 NULL。

DROP TABLE IF EXISTS stu\_temp;

CREATE TABLE stu\_temp AS SELECT \* FROM student;

DECLARE

var\_null CHAR(1); -- Set to NULL automatically at run time

BEGIN

EXECUTE IMMEDIATE 'UPDATE stu\_temp SET name =:x'

USING var\_null;

END;

/

查看表 stu\_temp：

select \* from stu\_temp;

id | name | score

\----+------+-------

1 | | 99

(1 行记录)

##### 使用RETUNING INTO子句

\-- 创建测试表

DROP TABLE employees;

CREATE TABLE employees (

id NUMBER PRIMARY KEY,

name VARCHAR2(50),

salary NUMBER,

department\_id NUMBER,

version NUMBER DEFAULT 1

);

\-- 插入测试数据

INSERT INTO employees VALUES (1, 'Alice', 5000, 10, 1);

INSERT INTO employees VALUES (2, 'Bob', 6000, 20, 1);

INSERT INTO employees VALUES (3, 'Charlie', 7000, 20, 1);

\-- 执行动态SQL（USING子句后跟RETURNING INTO子句）

DECLARE

v\_dept\_id NUMBER:= 10; -- 输入参数：部门ID

v\_updated\_salary employees.salary%TYPE; -- 输出参数：更新后的工资

v\_new\_version employees.salary%TYPE; --输出参数：更新后的版本号

BEGIN

EXECUTE IMMEDIATE '

UPDATE employees

SET salary = salary \* 1.1, version = version + 1

WHERE department\_id =:1

RETURNING salary, version INTO:2,:3'

USING v\_dept\_id -- USING子句：传递输入参数

RETURNING INTO v\_updated\_salary, v\_new\_version; -- RETURNING  
INTO子句：返回结果

raise notice '更新后的工资:% ', v\_updated\_salary;

raise notice '更新后的版本号:% ', v\_new\_version;

COMMIT;

END;

/

输出：

NOTICE: 更新后的工资:5500.0

NOTICE: 更新后的版本号:2

查看表数据：

SELECT id, name, salary, department\_id, version FROM employees WHERE  
department\_id = 10;

id | name | salary | department\_id | version

\----+-------+--------+---------------+---------

1 | Alice | 5500.0 | 10 | 2

(1 行记录)

### OPEN FOR、FETCH 和 CLOSE 语句

如果动态 SQL 语句表示一个返回多行的 SELECT 语句，则可以使用本地动态SQL进行处理，如下所示：

1. 使用 OPEN FOR 语句将游标变量与动态 SQL 语句相关联。 在 OPEN FOR  
	语句的 USING 子句中，为动态 SQL 语句中的每个占位符指定一个绑定变量。

> USING 子句不能包含文字 NULL。 要解决此限制，请在要使用 NULL 的  
> 地方使用未初始化的变量。

2. 使用 FETCH 语句一次检索一行、多行或所有结果集。
3. 使用 CLOSE 语句关闭游标变量。

#### 示例

##### 带有 OPEN FOR、FETCH 和 CLOSE 语句的本地动态SQL

DECLARE

TYPE StuCurTyp IS REF CURSOR;

v\_stu\_cursor StuCurTyp;

stu\_record student%ROWTYPE;

v\_stmt\_str VARCHAR2(200);

v\_id student.id%TYPE;

BEGIN

\-- 动态SQL语句中使用占位符

v\_stmt\_str:= 'SELECT \* FROM student WHERE id =:j';

\-- 打开游标为占位符绑定in参数

OPEN v\_stu\_cursor FOR v\_stmt\_str USING 1;

\-- 每次从结果集中取出一行数据

LOOP

FETCH v\_stu\_cursor INTO stu\_record;

EXIT WHEN v\_stu\_cursor%NOTFOUND;

RAISE NOTICE 'stu\_record: %', stu\_record;

END LOOP;

\-- 关闭游标

CLOSE v\_stu\_cursor;

END;

/

输出：

NOTICE: stu\_record: (1,xx,99)

### 动态 SQL 语句中的重复占位符名称

如果在动态 SQL语句中使用重复占位符名称，请注意占位符与绑定变量的关联方式取决于动态 SQL语句的类型。

1. 动态 SQL 语句不是匿名块或 CALL 语句

> 如果动态 SQL 语句不是匿名 PL/iSQL 块或 CALL 语句，则占位符名称的  
> 重复无关紧要。
> 
> 占位符在 USING 子句中按位置而不是按名称与绑定变量相关联。
> 
> 例如，在这个动态 SQL 语句中，名称:x 的重复是无关紧要的：

sql\_stmt:= 'INSERT INTO payroll VALUES (:x,:x,:y,:x)';

> 在相应的 USING 子句中，您必须提供四个绑定变量。它们可以不同，例如：

EXECUTE IMMEDIATE sql\_stmt USING a, b, c, d;

> 前面的 EXECUTE IMMEDIATE 语句运行以下 SQL 语句：

INSERT INTO payroll VALUES (a, b, c, d)

> 要将相同的绑定变量与每次出现的:x 关联，您必须重复指定该绑定变量；  
> 例如：

EXECUTE IMMEDIATE sql\_stmt USING a, a, b, a;

> 前面的 EXECUTE IMMEDIATE 语句运行以下 SQL 语句：

INSERT INTO payroll VALUES (a, a, b, a)

2. 动态SQL语句是CALL语句

> 如果动态 SQL 语句是 CALL 语句，不支持使用重复的占位符。

3. 动态SQL语句是匿名块

> 如果动态 SQL 语句是匿名 PL/iSQL 块，则占位符名称的重复是有效的。
> 
> 每个唯一的占位符名称在 USING 子句中必须有一个对应的绑定变量。  
> 如果重复占位符名称，则无需重复其对应的绑定变量，对该占位符名称  
> 的所有引用都对应于 USING 子句中的一个绑定变量。

#### 示例

##### 普通动态SQL语句中的重复占位符名称

以下动态SQL为insert语句，占位符:x使用了三次，在USING子句中，需要分别为三个:x指定参数。

create table tb\_dsql(empno int, ename varchar2(20), sal int, grade int);

DECLARE

dyn\_stmt VARCHAR2(100);

lv\_empno tb\_dsql.empno%TYPE:= 7900;

lv\_ename tb\_dsql.ename%TYPE:= 'JAMES';

lv\_sal tb\_dsql.sal%TYPE:= 950;

BEGIN

dyn\_stmt:= 'INSERT INTO tb\_dsql VALUES(:x,:x,:y,:x)';

EXECUTE IMMEDIATE dyn\_stmt USING lv\_empno,lv\_ename,lv\_sal,30;

END;

/

输出：

select \* from tb\_dsql;

empno | ename | sal | grade

\-------+-------+-----+-------

7900 | JAMES | 950 | 30

(1 行记录)

如果上述语句中，USING子句中为三个:x占位符指定一个参数值：

DECLARE

dyn\_stmt VARCHAR2(100);

lv\_empno tb\_dsql.empno%TYPE:= 7900;

lv\_ename tb\_dsql.ename%TYPE:= 'JAMES';

lv\_sal tb\_dsql.sal%TYPE:= 950;

BEGIN

dyn\_stmt:= 'INSERT INTO tb\_dsql VALUES(:x,:x,:y,:x)';

EXECUTE IMMEDIATE dyn\_stmt USING lv\_empno,lv\_sal;

END;

/

会报错如下：

ERROR: there is no parameter:y

##### 动态CALL语句中的重复占位符名称

以下示例，在CALL语句中分别为存储过程的三个参数指定三个不同的占位符，执行成功。

create table t1(id int);

CREATE OR REPLACE PROCEDURE insert\_proc (p1 IN int, p2 IN int,p3 IN int)  
IS

BEGIN

insert into t1(id) values(p1);

insert into t1(id) values(p2);

insert into t1(id) values(p3);

END;

/

DECLARE

input\_val1 int:= '111';

input\_val2 int:= '222';

input\_val3 int:= '333';

BEGIN

EXECUTE IMMEDIATE 'CALL insert\_proc(:1,:2,:3)' USING input\_val1,  
input\_val2,input\_val3;

END;

/

以下示例，在CALL语句中为三个参数指定重复的占位符，无论后边USING子句中的参数如何，都会失败。

DECLARE

input\_val1 int:= '111';

input\_val2 int:= '222';

input\_val3 int:= '333';

BEGIN

EXECUTE IMMEDIATE 'CALL insert\_proc(:1,:1,:3)' USING input\_val1,  
input\_val1,input\_val3;

END;

/

报错如下：

ERROR: output parameter cannot be a duplicate bind

##### 动态PL/iSQL 块中的重复占位符名称

在此示例中，对第一个唯一占位符名称:x 的所有引用都与 USING子句中的第一个绑定变量 a 相关联，第二个唯一占位符名称:y 与 USING子句中的第二个绑定变量b相关联。

CREATE PROCEDURE add\_int (

a INTEGER,

b INTEGER,

c INTEGER,

d INTEGER )

IS

BEGIN

RAISE NOTICE 'a + b + c + d = %', a+b+c+d;

END;

/

DECLARE

a INTEGER:= 1;

b INTEGER:= 2;

plsql\_block VARCHAR2(100);

BEGIN

plsql\_block:= 'BEGIN add\_int(:x,:x,:y,:x); END;';

EXECUTE IMMEDIATE plsql\_block USING a, b;

END;

/

输出：

NOTICE: a + b + c + d = 5