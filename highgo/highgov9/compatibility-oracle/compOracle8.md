---
title: "存储过程"
book: "Oracle兼容性"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/compatibility/compOracle8.html"
tags:
  - highgo
  - highgo-v9
  - compatibility-oracle
---

## 存储过程

## 说明

### CREATE PROCEDURE

与CREATE FUCTION类似，模式和用户是分开的对象，如果在其他模式下创建或替换存储过程，必须拥有这个模式上的CREATE权限。

1. 支持AS关键字
2. 支持不带language。
3. 默认情况下存储过程名后面必须带()，无参存储过程可以不带()。
4. 存储过程结束END; 语句后面在psql中以/结束。
5. 创建存储过程变量声明前必须指定DECLARE关键字。

代码示例：

CREATE OR REPLACE PROCEDURE proc(a IN int)

IS

BEGIN

NULL;

END;

/

### ALTER PROCEDURE

ALTER PROCEDURE语句显式重新编译独立的存储过程(procedure)。ALTER PROCEDURE不会改变现有存储过程的声明或定义。

如果ALTER PROCEDURE存储过程使用COMPILE语句编译函数没有任何编译错误，那么存储过程的状态是valid，数据库接下来执行存储过程时，在运行时不需要重新编译这个存储过程。如果ALTER PROCEDURE存储过程 COMPILE;语句有编译错误，存储过程的状态还是invalid。

数据库也验证依赖这个存储过程的所有对象，如果没有调用ALTER PROCEDURE COMPILE显示的重新编译存储过程，在运行时还是会重新存储过程。

代码示例：

CREATE OR REPLACE PROCEDURE proc(a IN int)

IS

BEGIN

NULL;

END;

/

Procedure created.

ALTER PROCEDURE proc COMPILE;

### DROP PROCEDURE

使用DROP PROCEDURE删除存储过程不可以使用DROP PROCEDURE 删除package中的存储过程。

如果存储过程只有一个，可以使用DROP PROCEDURE procedure\_name语句删除存储过程，不需要指定参数类型。如果存储过程有多个，必须指定参数。

代码示例：

CREATE OR REPLACE PROCEDURE proc(a IN int)

AS

BEGIN

NULL;

END;

/

DROP PROCEDURE proc;

### OUT参数

存储过程中的out参数是输出模式的参数，用于输出值，会忽略传入的值，在子程序内部可以对其进行修改，子程序执行完毕后，out模式参数最终的值会赋值给调用时对应的实参变量，其中out模式参数的调用，必须通过变量。

create or replace procedure proc (

a integer,

b in integer,

c out integer,

d in out BINARY\_FLOAT

)

as

declare

begin

raise notice ‘Inside procedure proc:’;

raise notice ‘IN a = %’, a;

raise notice ‘IN b = %’, b;

raise notice ‘OUT c = %’, c;

raise notice ‘IN OUT d =%’, d;

c:= a+10;

d:= 40/20;

end;

/

declare

aa CONSTANT integer:= 1;

bb integer:= 2;

ee integer;

ff binary\_float:= 5;

begin

call proc (1,

(bb+3)\*4,

ee,

ff

);

raise notice ‘after procedure p:’;

raise notice ‘IN aa = %’, aa;

raise notice ‘IN bb = %’, bb;

raise notice ‘OUT ee = %’, ee;

raise notice ‘IN OUT ff =%’,ff;

end;

/