---
title: "函数"
book: "Oracle兼容性"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/compatibility/compOracle7.html"
tags:
  - highgo
  - highgo-v9
  - compatibility-oracle
---

## 函数

## 说明

语法中的各个子句，比如 [invoker\_rights\_clause](https://docs.oracle.com/en/database/oracle/oracle-database/21/lnpls/invokers_rights_clause.html%22%20/l%20%22GUID-66745CF3-81D9-491B-BD49-E83E05A5C4E4__INVOKER_RIGHTS_CLAUSE-0566ECA9) ， [accessible\_by\_clause](https://docs.oracle.com/en/database/oracle/oracle-database/21/lnpls/ACCESSIBLE-BY-clause.html%22%20/l%20%22GUID-9720619C-9862-4123-96E7-3E85F240FF36__ACCESSIBLE_BY_CLAUSE-0B7B66E4) 等所有这些子句声明与它们的顺序没有关系。

### CREATE FUNCTION

- OR REPLACE

如果函数已经存在，重建和编译函数。

数据库中所有对象的名称（函数名称+参数名称+参数类型）都一致。所以CREATE OR REPLACE一个已经存在的函数，删除已存在的函数，最后数据库中只有一个函数。

函数可以重载，即同一函数名，参数个数或参数类型不同（不包括OUT参数），都可以创建上函数。也就是如果CREATE OR REPLACE一个已经存在的函数，如果参数类型或参数个数不同（不包括OUT参数），会新建一个同名的函数。例如下面第2条语句执行时会报名字冲突，建议删除旧的函数。另外还支持函数重载。

CREATE FUNCTION foo(int) …

CREATE OR REPLACE FUNCTION foo(int, out text) …

如果两个函数差异只是多了一个带默认值的参数，在创建函数时不会报错，但是在调用函数时会报错：HINT:No function matches the given name and argument types. You might need to add explicit type casts..(没有匹配给定名称和参数类型的函数。您可能需要添加显式的类型转换。)。例如：

CREATE FUNCTION foo(int) …

CREATE OR REPLACE FUNCTION foo(int, int default 42) …

如果函数名和参数个数及类型都相同，会重建编译函数。

- \[EDITIONABLE | NONEDITIONABLE \]

指定函数是editioned 还是noneditioned 对象。默认是EDITIONABLE。

#### PLSQL\_FUNCTION\_SOURCE

- Schema 模式名
- function\_name函数名
- RETURN datatype

支持RETURNS datatype，返回值类型可以是BOOLEAN。dataype可以指定长度、精度、标度，也可以不指定长度、精度、标度。保持目前行为不变。

##### PARAMETER\_DECLARATION

- Parameter参数名
- IN, OUT, IN OUT 参数模式，目前支持的模式是：IN, OUT, INOUT，VARIADIC。默认是IN。
- NOCOPY

存储过程和函数之间传参有2种方法：传值和传引用。

默认情况，OUT和IN OUT参数通过传值方式传递，IN参数是传引用方式。程序执行前IN OUT参数的实际值将被复制给形参。程序执行中间，临时变量保存参数的输出值。如果程序正常退出，这些值将被复制回原参数。如果程序异常退出，那么原参数值将不会改变。当OUT和IN OUT参数为大数据结构，诸如：集合、记录、对象类型实例时，通过传值方式的COPY动作将会导致程序执行速度下降，使用内存量上升。尤其是该程序被多次调用时更是如此。

为避免此类情况，我们可以指定NOCOPY，告诉编译器通过传引用方式传递OUT 和IN OUT参数。这样，形参将不会COPY参数实际值，也就是说形参和ACTUAL VALUE指向同一内存地址（memory location）。以此提高程序执行性能。

- Datatype

形参的数据类型，datatype可以是约束的subtype，可以带精度、长度等约束例如NUMBER(4,2) 或VARCHAR2(20)。

- Expression

形参的默认值。Expression必须和datatype兼容。如果函数调用时实参值没有指定，使用形参默认值，如果指定了实参，形参默认值不会计算。目前IN模式参数可以带默认值， INOUT/OUT模式参数不允许带默认值。参数个数最多定为2400（block\_size为32k情况下）。

##### BODY

函数的执行部分，可以有异常。

#### DECLARE\_SECTION

函数声明，可选项。声明部分的变量是函数的局部变量，可以在函数body中引用，在函数执行完成后结束。

声明部分可以包括：类型定义（自定义类型如集合和record、refcursor、subtype）、cursor声明定义、变量定义、子函数或过程声明和定义。

目前不支持集合类型和subtype，支持record类型和refcursor。

##### IS和AS

目前支持AS、IS关键字。

#### SHARING\_CLAUSE

SHARING子句中仅支持语法

#### INVOKER\_RIGHTS\_CLAUSE

指定PL/ISQL程序的AUTHID属性。AUTHID属性影响名称解析和SQL语句权限检查。invoker\_rights\_clause子句可以出现在下面的SQL语句中：ALTER TYPE, CREATE FUNCTION, CREATE PACKAGE, CREATE PROCEDURE, CREATE TYPE, CREATE TYPE BODY。

当invoker\_rights\_clause子句出现在package声明中，指定包的函数和存储过程，及显式游标的AUTHID属性。当invoker\_rights\_clause子句出现在独立的函数或存储过程声明中，指定函数或存储过程的AUTHID属性。invoker\_rights\_clause子句也可以出现在子程序的声明中。如果invoker\_rights\_clause子句出现在自定义ADT类型时， 指定ADT 类型的member函数或存储过程的AUTHID属性。

AUTHID值是DEFINER时，称为定义者权限（DR），不指定AUTHID，默认是DEFINER，也就是存储过程执行时，以这个存储过程的创建者的身份来验证存取权限。AUTHID值是CURRENT\_USER时，称为调用者权限（IR），在执行存储过程时根据当前调用存储过程的用户权限来验证。AUTHID值影响运行时的名字解析和权限检查：

1. 名字解析是CURRENT\_SCHEMA
2. 权限检查时CURRENT\_USER和enabled roles。

目前CREATE FUNCTION支持SECURITY INVOKER和SECURITY DEFINER子句，默认是INVOKER。

#### ACCESSIBLE\_BY\_CLAUSE

accessible\_by\_clause子句中仅支持语法

#### DEFAULT\_COLLATION\_CLAUSE

default\_collation\_clause子句中仅支持语法

#### DETERMINISTIC

表示函数的返回值是确定的。函数返回值完全由输入参数决定，只要输入是确定的，返回结果也是确定的。

DETERMINISTIC子句只能出现在函数声明或定义中，并且只能出现一次。

DETERMINISTIC函数可能不会触发未处理的异常。

如果带DETERMINISTIC子句的函数违背了这些规则，那么函数调用的结果是无法定义的。

如果在基于函数索引的表达式中、虚拟列定义或者REFRESH FAST 或 ENABLE QUERY REWRITE的物化视图查询中调用函数，必须指定DETERMINISTIC。当数据库遇到DETERMINISTIC函数，会尝试使用以前计算的结果而不是重新计算函数。如果更改了函数，必须手动建基于函数的索引和视图。

下面情况下不能指定DETERMINISTIC：

1. 函数结果依赖于会话变量或模式对象。
2. 使用包变量或访问数据库可能会影响函数返回结果。
3. 多态表函数禁止使用DETERMINISTIC。

当出现DETERMINISTIC时，编译器可能使用标记提高函数执行性能。

下面情况下推荐使用DETERMINISTIC：

1. WHERE、ORDER BY 或 GROUP BY 子句中使用的函数
2. MAP或排序SQL类型方法的函数
3. 判断结果集中是否出现ROW或出现在哪的函数

#### PARALLEL\_ENABLE

PARALLEL\_ENABLE仅支持语法。

#### RESULT\_CACHE\_CLAUSE

result\_cache\_clause仅支持语法。

#### AGGREGATE\_CLAUSE

aggregate\_clause仅支持语法。

#### PIPELINED\_CLAUSE

pipelined\_clause仅支持语法。

#### SQL\_MACRO\_CLAUSE

sql\_macro\_clause仅支持语法。

代码示例：

CREATE OR REPLACE FUNCTION f1(a IN int)

RETURN int

IS

BEGIN

RETURN a;

END;

/

CREATE OR REPLACE FUNCTION f1(a IN int,b int)

RETURN int

IS

BEGIN

RETURN a;

END;

/

CREATE OR REPLACE FUNCTION f1(a IN int,b int,c int)

RETURN varchar

IS

BEGIN

RETURN a;

END;

/

Function created.

select f1(1,2,3) from dual;

### ALTER FUNCTION

ALTER FUNCTION语句显示重新编译独立的函数。ALTER FUNCTION不会改变现有函数的声明或定义。

- schema

包含函数的模式名。

- function\_name

重新编译的函数名

- \[EDITIONABLE | NONEDITIONABLE \]

指定函数是edtioned还是noneditioned对象。默认是EDITIONABLE。

如果ALTER FUNCTION 函数 COMPILE;语句编译函数没有任何编译错误（注：如果有多个同名不同参函数时，需要指定参数否则提示错误），那么函数的状态是valid， 数据库接下来执行函数时，在运行时不需要重新编译。如果ALTER FUNCTION 函数 COMPILE;语句有编译错误，函数的状态还是invalid。

数据库也验证依赖这个函数的所有对象，如果没有调用ALTER FUNCTION COMPILE显示的重新编译函数，在运行时还是会重新编译函数。

不支持EDITIONABLE | NONEDITIONABLE功能、不支持PL/SQL编译参数功能（compiler\_parameters\_clause）。

### DROP FUNCTION

使用DROP FUNCTION删除函数。不可以使用DROP FUNCTION删除package中的函数。

如果不指定模式，受search\_path影响，默认是当前用户或public模式，

如果函数只有一个，可以使用DROP FUNCTION function\_name语句删除函数，不需要指定参数类型。如果函数有多个，必须指定函数参数。

代码示例：

drop function f1;

### OUT参数

函数中的out参数是输出模式的参数，用于输出值，会忽略传入的值，在函数内部可以对其进行修改，函数执行完毕后，out模式参数最终的值会赋值给调用时对应的实参变量，其中out模式参数的调用，必须通过变量。

create or replace function func (

a integer, – IN by default

b in integer,

c out integer,

d in out BINARY\_FLOAT

) return int

as

declare

begin

raise notice ‘Inside func:’;

raise notice ‘IN a = %’, a;

raise notice ‘IN b = %’, b;

raise notice ‘OUT c = %’, c;

raise notice ‘IN OUT d =%’, d;

c:= a+10;

d:= 40/20;

return 1;

end;

/

declare

aa CONSTANT integer:= 1;

bb integer:= 2;

ee integer;

ff binary\_float:= 5;

ret integer;

begin

ret:= func (1,

(bb+3)\*4,

ee, – uninitialized variable

ff – initialized variable

);

raise notice ‘after function func:’;

raise notice ‘IN aa = %’, aa;

raise notice ‘IN bb = %’, bb;

raise notice ‘OUT ee = %’, ee;

raise notice ‘IN OUT ff =%’,ff;

end;

/