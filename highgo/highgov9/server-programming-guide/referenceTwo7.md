---
title: "PLpgSQL-SQL过程语言"
book: "服务器编程指南"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/reference/referenceTwo7.html"
tags:
  - highgo
  - highgo-v9
  - server-programming-guide
---

## PL/pgSQL - SQL过程语言

## 综述

PL/pgSQL是一种用于瀚高数据库系统的可载入的过程语言。PL/pgSQL的设计目标是创建一种这样的可载入过程语言

• 可以被用来创建函数和触发器过程，

• 对SQL语言增加控制结构，

• 可以执行复杂计算，

• 继承所有用户定义类型、函数和操作符，

• 可以被定义为受服务器信任，

• 便于使用。

用PL/pgSQL创建的函数可以被用在任何可以使用内建函数的地方。例如，可以创建复杂条件的计算函数并且后面用它们来定义操作符或把它们用于索引表达式。

在瀚高数据库以后的版本中，PL/pgSQL是默认被安装的。但是它仍然是一种可载入模块，因此特别关注安全性的管理员可以选择移除它。

### 使用PL/pgSQL的优点

SQL被瀚高数据库和大多数其他关系数据库用作查询语言。它是可移植的并且容易学习。但是每一个SQL语句必须由数据库服务器单独执行。

这意味着你的客户端应用必须发送每一个查询到数据库服务器、等待它被处理、接收并处理结果、做一些计算，然后发送更多查询给服务器。如果你的客户端和数据库服务器不在同一台机器上，所有这些会引起进程间通信并且将带来网络负担。

通过PL/pgSQL，你可以将一整块计算和一系列查询分组在数据库服务器内部，这样就有了一种过程语言的能力并且使 SQL 更易用，但是节省了相当多的客户端/服务器通信开销。

• 客户端和服务器之间的额外往返通信被消除

• 客户端不需要的中间结果不必被整理或者在服务器和客户端之间传送

• 多轮的查询解析可以被避免

与不使用存储函数的应用相比，这能够导致可观的性能提升。

还有，通过PL/pgSQL你可以使用 SQL 中所有的数据类型、操作符和函数。

### 支持的参数和结果数据类型

PL/pgSQL编写的函数可以接受服务器支持的任何标量或数组数据类型作为参数，并且它们能够返回任何这些类型的结果。它们也能接受或返回任何用名称指定的组合类型（行类型）。

还可以声明一个PL/pgSQL函数为接受record，这表示任意组合类型都将作为输入，或者声明为返回record，表示结果是一种行类型，它的列由调用查询中的说明确定。

PL/pgSQL函数可以通过使用VARIADIC标记被声明为接受数量不定的参数。

PL/pgSQL函数也可以被声明为接受并返回多态类型anyelement、anyarray、anynonarray、anyenum以及anyrange。如 前面的章节 中所讨论的，由一个多态函数处理的实际数据类型会随着调用改变。在 后面的章节 中展示了一个例子。

PL/pgSQL函数还能够被声明为返回一个任意（可作为一个单一实例返回的）数据类型的”集合”（或表）。这样的一个函数通过为结果集的每个期望元素执行RETURN NEXT来产生输出，或者通过使用RETURN QUERY来输出一个查询计算的结果。

最后，如果一个PL/pgSQL函数没有可用的返回值，它可以被声明为返回void（另外一种选择是，在那种情况下它可以被写作一个过程）。

PL/pgSQL函数也能够被声明为用输出参数代替返回类型的一个显式说明。这没有为该语言增加任何基础功能，但是它常常很方便，特别是对于要返回多个值的情况。RETURNS TABLE符号也可以被用来替代RETURNS SETOF。

## PL/pgSQL的结构

通过执行CREATE FUNCTION命令，以PL/pgSQL写成的函数可以被定义到服务器中。这种命令通常看起来是这样：

CREATE FUNCTION somefunc(integer, text) RETURNS integer

AS 'function body text'

LANGUAGE plpgsql;

就目前CREATE FUNCTION所关心的来说，函数体就是简单的一个字符串。通常在写函数体时，使用美元符号引用通常比使用普通单引号语法更有帮助。如果没有美元引用，函数体中的任何单引号或者反斜线必须通过双写来转义。这一章中几乎所有的例子都在其函数体中使用美元符号引用。

PL/pgSQL是一种块结构的语言。一个函数体的完整文本必须是一个块。一个块被定义为：

\[ <\<label>> \]

\[ DECLARE

declarations \]

BEGIN

statements

END \[ label \];

在一个块中的每一个声明和每一个语句都由一个分号终止。如上所示，出现在另一个块中的块必须有一个分号在END之后。不过最后一个结束函数体的END不需要一个分号。

| 提示： |
| --- |
| 一种常见的错误是直接在BEGIN之后写一个分号。这是不正确的并且将会导致一个语法错误。 |

如果你想要标识一个块以便在一个EXIT语句中使用或者标识在该块中声明的变量名，那么label是你唯一需要的。如果一个标签在END之后被给定，它必须匹配在块开始处的标签。

所有的关键词都是大小写无关的。除非被双引号引用，标识符会被隐式地转换为小写形式，就像它们在普通 SQL 命令中。

PL/pgSQL代码中的注释和普通 SQL 中的一样。一个双连字符（--）开始一段注释，它延伸到该行的末尾。一个/\*开始一段块注释，它会延伸到匹配\*/出现的位置。块注释可以嵌套。

一个块的语句节中的任何语句可以是一个子块。子块可以被用来逻辑分组或者将变量局部化为语句的一个小组。在子块的持续期间，在一个子块中声明的变量会掩盖外层块中相同名称的变量。但是如果你用块的标签限定外层变量的名字，你仍然可以访问它们。例如：

CREATE FUNCTION somefunc() RETURNS integer AS $$

<< outerblock >>

DECLARE

quantity integer:= 30;

BEGIN

RAISE NOTICE 'Quantity here is %', quantity; -- Prints 30

quantity:= 50;

\--

\-- 创建一个子块

\--

DECLARE

quantity integer:= 80;

BEGIN

RAISE NOTICE 'Quantity here is %', quantity; -- Prints 80

RAISE NOTICE 'Outer quantity here is %', outerblock.quantity; -- Prints

50

END;

RAISE NOTICE 'Quantity here is %', quantity; -- Prints 50

RETURN quantity;

END;

$$ LANGUAGE plpgsql;

| 注意： |
| --- |
| 在任何PL/pgSQL函数体的外部确实有一个隐藏的”外层块”包围着。这个块提供了该函数参数（如果有）的声明，以及某些诸如FOUND之类特殊变量 （ 详见 ）。外层块被标上函数的名称，这意味着参数和特殊变量可以用该函数的名称限定。 |

重要的是不要把PL/pgSQL中用来分组语句的BEGIN/END与用于事务控制的同名 SQL 命令弄混。PL/pgSQL的BEGIN/END只用于分组，它们不会开始或结束一个事务。此外，一个包含EXCEPTION子句的块实际上会形成一个子事务，它可以被回滚而不影响外层事务。

## 声明

在一个块中使用的所有变量必须在该块的声明小节中声明（唯一的例外是在一个整数范围上迭代的FOR循环变量会被自动声明为一个整数变量，并且相似地在一个游标结果上迭代的FOR循环变量会被自动地声明为一个记录变量）。

PL/pgSQL变量可以是任意 SQL 数据类型，例如integer、varchar和char。

这里是变量声明的一些例子：

user\_id integer;

quantity numeric(5);

url varchar;

myrow tablename%ROWTYPE;

myfield tablename.columnname%TYPE;

arow RECORD;

一个变量声明的一般语法是：

name \[ CONSTANT \] type \[ COLLATE collation\_name \] \[ NOT NULL \] \[ { DEFAULT |:=

| = } expression \];

如果给定DEFAULT子句，它会指定进入该块时分 配给该变量的初始值。如果没有给出DEFAULT子句，则该变量被初始化为SQL空值。CONSTANT选项阻止该变量在初始化之后被赋值，这样它的值在块的持续期内保持不变。COLLATE 选项指定用于该变量的一个排序规则（ 详见 ）。如果指定了NOT NULL，对该变量赋值为空值会导致一个运行时错误。所有被声明为NOT NULL的变量必须 被指定一个非空默认值。等号（=）可以被用来代替 PL/SQL-兼容的:=。

一个变量的默认值会在每次进入该块时被计算并且赋值给该变量（不是每次函数调用只计算一次）。因此，例如将now()赋值给类型为timestamp的一个变量将会导致该变量具有当前函数调用的时间，而不是该函数被预编译的时间。

例子：

quantity integer DEFAULT 32;

url varchar:= ' [http://mysite.com\\](http://mysite.com/) ‘;

user\_id CONSTANT integer:= 10;

### 声明函数参数

传递给函数的参数被命名为标识符$1、$2等等。可选地，能够为$n参数名声明别名来增加可读性。不管是别名还是数字标识符都能用来引用参数值。

有两种方式来创建一个别名。比较好的方式是在CREATE FUNCTION命令中为参数给定一个名称。例如：

CREATE FUNCTION sales\_tax(subtotal real) RETURNS real AS $$

BEGIN

RETURN subtotal \* 0.06;

END;

$$ LANGUAGE plpgsql;

另一种方式是显式地使用声明语法声明一个别名。

name ALIAS FOR $n;

使用这种风格的同一个例子看起来是：

CREATE FUNCTION sales\_tax(real) RETURNS real AS $$

DECLARE

subtotal ALIAS FOR $1;

BEGIN

RETURN subtotal \* 0.06;

END;

$$ LANGUAGE plpgsql;

| 注意： |
| --- |
| 这两个例子并非完全等效。在第一种情况中，subtotal可以被引用为sales\_tax.subtotal，但在第二种情况中它不能这样引用（如果我们为内层块附加了一个标签，subtotal则可以用那个标签限定）。 |

更多一些例子：

CREATE FUNCTION instr(varchar, integer) RETURNS integer AS $$

DECLARE

v\_string ALIAS FOR $1;

index ALIAS FOR $2;

BEGIN

\-- 这里是一些使用 v\_string 和 index 的计算

END;

$$ LANGUAGE plpgsql;

CREATE FUNCTION concat\_selected\_fields(in\_t sometablename) RETURNS text AS $$

BEGIN

RETURN in\_t.f1 || in\_t.f3 || in\_t.f5 || in\_t.f7;

END;

$$ LANGUAGE plpgsql;

当一个PL/pgSQL函数被声明为带有输出参数，输出参数可以用普通输入参数相同的方式被给定$n名称以及可选的别名。一个输出参数实际上是一个最初为 NULL 的变量，它应当在函数的执行期间被赋值。该参数的最终值就是要被返回的东西。例如，sales-tax 例子也可以用这种方式来做：

CREATE FUNCTION sales\_tax(subtotal real, OUT tax real) AS $$

BEGIN

tax:= subtotal \* 0.06;

END;

$$ LANGUAGE plpgsql;

注意我们忽略了RETURNS real — 我们也可以包括它，但是那将是冗余。

当返回多个值时，输出参数最有用。一个小例子是：

CREATE FUNCTION sum\_n\_product(x int, y int, OUT sum int, OUT prod int) AS $$

BEGIN

sum:= x + y;

prod:= x \* y;

END;

$$ LANGUAGE plpgsql;

如 前面的章节 中所讨论的，这实际上为该函数的结果创建了一个匿名记录类型。如果给定了一个RETURNS子句，它必须RETURNS record。

声明一个PL/pgSQL函数的另一种方式是用RETURNS TABLE，例如：

CREATE FUNCTION extended\_sales(p\_itemno int)

RETURNS TABLE(quantity int, total numeric) AS $$

BEGIN

RETURN QUERY SELECT s.quantity, s.quantity \* s.price FROM sales AS s

WHERE s.itemno = p\_itemno;

END;

$$ LANGUAGE plpgsql;

这和声明一个或多个OUT参数并且指定RETURNS SETOF sometype完全等效。

当一个PL/pgSQL函数的返回类型被声明为一个多态类型

（anyelement、anyarray、anynonarray、anyenum或anyrange），一个特殊参数$0会被创建。它的数据类型是该函数的实际返回类型，这是从实际输入类型（ 详见 ）推演得来。$0被初始化为空并且不能被该函数修改，因此它能够被用来保持可能需要的返回值，不过这不是必须的。$0也可以被给定一个别名。例如，这个函数工作在任何具有一个+操作符的数据类型上：

CREATE FUNCTION add\_three\_values(v1 anyelement, v2 anyelement, v3 anyelement)

RETURNS anyelement AS $$

DECLARE

result ALIAS FOR $0;

BEGIN

result:= v1 + v2 + v3;

RETURN result;

END;

$$ LANGUAGE plpgsql;

通过声明一个或多个输出参数为多态类型可以得到同样的效果。在这种情况下，不使用特殊的$0参数，输出参数本身就用作相同的目的。例如：

CREATE FUNCTION add\_three\_values(v1 anyelement, v2 anyelement, v3 anyelement,

OUT sum anyelement)

AS $$

BEGIN

sum:= v1 + v2 + v3;

END;

$$ LANGUAGE plpgsql;

### ALIAS

newname ALIAS FOR oldname;

ALIAS语法比前一节中建议的更一般化：你可以为任意变量声明一个别名，而不只是函数参数。其主要实际用途是为预先决定了名称的变量分配一个不同的名称，例如在一个触发器过程中的NEW或OLD。

例子：

DECLARE

prior ALIAS FOR old;

updated ALIAS FOR new;

因为ALIAS创造了两种不同的方式来命名相同的对象，如果对其使用不加限制就会导致混淆。最好只把它用来覆盖预先决定的名称。

### 复制类型

variable%TYPE

%TYPE提供了一个变量或表列的数据类型。你可以用它来声明将保持数据库值的变量。例如，如果你在users中有一个名为user\_id的列。要定义一个与users.user\_id具有相同数据类型的变量：

user\_id users.user\_id%TYPE;

通过使用%TYPE，你不需要知道你要引用的结构的实际数据类型，而且最重要地，如果被引用项的数据类型在未来被改变（例如你把user\_id的类型从integer改为real），你不需要改变你的函数定义。

%TYPE在多态函数中特别有价值，因为内部变量所需的数据类型能在两次调用时改变。可以把%TYPE应用在函数的参数或结果占位符上来创建合适的变量。

### 行类型

name table\_name%ROWTYPE;

name composite\_type\_name;

一个组合类型的变量被称为一个行变量（或行类型变量）。这样一个变量可以保持一个SELECT或FOR查询结果的一整行，前提是查询的列集合匹配该变量被声明的类型。该行值的各个域可以使用通常的点号标记访问，例如rowvar.field。

通过使用table\_name%ROWTYPE标记，一个行变量可以被声明为具有和一个现有表或视图的行相同的类型。它也可以通过给定一个组合类型名称来声明（因为每一个表都有一个相关联的具有相同名称的组合类型，所以在瀚高数据库中实际上写不写%ROWTYPE都没有关系。但是带有%ROWTYPE的形式可移植性更好）。

一个函数的参数可以是组合类型（完整的表行）。在这种情况下，相应的标识符$n将是一个行变量，并且可以从中选择域，例如$1.user\_id。

这里是一个使用组合类型的例子。table1和table2是已有的表，它们至少有以下提到的域：

CREATE FUNCTION merge\_fields(t\_row table1) RETURNS text AS $$

DECLARE

t2\_row table2%ROWTYPE;

BEGIN

SELECT \* INTO t2\_row FROM table2 WHERE...;

RETURN t\_row.f1 || t2\_row.f3 || t\_row.f5 || t2\_row.f7;

END;

$$ LANGUAGE plpgsql;

SELECT merge\_fields(t.\*) FROM table1 t WHERE...;

### 记录类型

name RECORD;

记录变量和行类型变量类似，但是它们没有预定义的结构。它们采用在一个SELECT或FOR命令期间为其赋值的行的真实行结构。一个记录变量的子结构能在每次它被赋值时改变。这样的结果是直到一个记录变量第一次被赋值之前，它都没有子结构，并且任何尝试访问其中一个域都会导致一个运行时错误。

注意RECORD并非一个真正的数据类型，只是一个占位符。我们也应该认识到当一个PL/pgSQL函数被声明为返回类型record，这与一个记录变量并不是完全相同的概念，即便这样一个函数可能会用一个记录变量来保持其结果。在两种情况下，编写函数时都不知道真实的行结构，但是对于一个返回record的函数，当调用查询被解析时就已经决定了真正的结构，而一个行变量能够随时改变它的行结构。

### PL/pgSQL变量的排序规则

当一个PL/pgSQL函数有一个或多个可排序数据类型的参数时，为每一次函数调用都会基于赋值给实参的排序规则来确定出一个排序规则。如果一个排序规则被成功地确定（即在参数之间隐式排序规则没有冲突），那么所有的可排序参数会被当做隐式具有那个排序规则。这将在函数中影响行为受到排序规则影响的操作。例如，考虑

CREATE FUNCTION less\_than(a text, b text) RETURNS boolean AS $$

BEGIN

RETURN a < b;

END;

$$ LANGUAGE plpgsql;

SELECT less\_than(text\_field\_1, text\_field\_2) FROM table1;

SELECT less\_than(text\_field\_1, text\_field\_2 COLLATE "C") FROM table1;

less\_than的第一次使用将会采用text\_field\_1和text\_field\_2共同的排序规则进行比较，而第二次使用将采用C排序规则。

此外，被确定的排序规则也被假定为任何可排序数据类型本地变量的排序规则。因此，当这个函数被写为以下形式时，它工作将不会有什么不同

CREATE FUNCTION less\_than(a text, b text) RETURNS boolean AS $$

DECLARE

local\_a text:= a;

local\_b text:= b;

BEGIN

RETURN local\_a < local\_b;

END;

$$ LANGUAGE plpgsql;

如果没有可排序数据类型的参数，或者不能为它们确定共同的排序规则，那么参数和本地变量会使用它们数据类型的默认排序规则（通常是数据库的默认排序规则，但是可能不同于域类型的变量）。

通过在一个可排序数据类型的本地变量的声明中包括COLLATE选项，可以为它指定一个不同的排序规则，例如

DECLARE

local\_a text COLLATE "en\_US";

这个选项会覆盖根据上述规则被给予该变量的排序规则。

还有，如果一个函数想要强制在一个特定操作中使用一个特定排序规则，当然可以在该函数内部写一个显式的COLLATE子句。例如：

CREATE FUNCTION less\_than\_c(a text, b text) RETURNS boolean AS $$

BEGIN

RETURN a < b COLLATE "C";

END;

$$ LANGUAGE plpgsql;

这会覆盖表达式中使用的表列、参数或本地变量相关的排序规则，就像在纯 SQL 命令中发生的一样。

## 表达式

PL/pgSQL语句中用到的所有表达式会被服务器的主SQL执行器处理。例如，当你写一个这样的PL/pgSQL语句时

IF expression THEN...

PL/pgSQL将通过给主 SQL 引擎发送一个查询

SELECT expression

来计算该表达式。如 前面的章节 中所详细讨论的，在构造该SELECT命令时，PL/pgSQL变量名的每一次出现会被参数所替换。这允许SELECT的查询计划仅被准备一次并且被重用于之后的对于该变量不同值的计算。因此，在一个表达式第一次被使用时实际发生的本质上是一个PREPARE命令。例如，如果我们已经声明了两个整数变量x和y，并且我们写了

IF x < y THEN...

在现象之后发生的等效于

PREPARE statement\_name(integer, integer) AS SELECT $1 < $2;

并且然后为每一次IF语句的执行，这个预备语句都会被EXECUTE，执行时使用变量的当前值作为参数值。通常这些细节对于一个PL/pgSQL用户并不重要，但是在尝试诊断一个问题时了解它们很有用。

## 基本语句

### 赋值

为一个PL/pgSQL变量赋一个值可以被写为：

variable {:= | = } expression;

正如以前所解释的，这样一个语句中的表达式被以一个 SQL SELECT命令被发送到主数据库引擎的方式计算。 该表达式必须得到一个单一值（如果该变量是一个行或记录变量， 它可能是一个行值）。该目标变量可以是一个简单变量（ 可以选择用一个块名限定）、一个行或记录变量的域或是一个简单 变量或域的数组元素。 等号（=）可以被用来代替 PL/SQL-兼容的:=。

如果该表达式的结果数据类型不匹配变量的数据类型，该值将被强制为变量 的类型，就好像做了赋值造型一样。 如果没有用于所涉及到的数据类型的赋值造型可用， PL/pgSQL解释器将尝试以文本的方式转换结果值，也就 是在应用结果类型的输出函数之后再应用变量类型的输入函数。注意如果结果 值的字符串形式无法被输入函数所接受，这可能会导致由输入函数产生的运行 时错误。例子：

tax:= subtotal \* 0.06;

my\_record.user\_id:= 20;

### 执行一个没有结果的命令

对于任何不返回行的 SQL 命令（例如没有一个RETURNING子句的INSERT），你可以通过把该命令直接写在一个 PL/pgSQL 函数中执行它。

任何出现在该命令文本中的PL/pgSQL变量名被当作一个参数，并且接着该变量的当前值被提供为运行时该参数的值。这与早前描述的对表达式的处理完全相似， 详见 。

当以这种方式执行一个 SQL 命令时，如 前面的章节 中讨论的，PL/pgSQL会为该命令缓存并重用执行计划。

有时候计算一个表达式或SELECT查询但抛弃其结果是有用的，例如调用一个有副作用但是没有有用的结果值的函数。在PL/pgSQL中要这样做，可使用PERFORM语句：

PERFORM query;

这会执行query并且丢弃掉结果。以写一个SQL SELECT命令相同的方式写该query，并且将初始的关键词SELECT替换为PERFORM。对于WITH查询，使用PERFORM并且接着把该查询放在圆括号中（在这种情况中，该查询只能返回一行）。PL/pgSQL变量将被替换到该查询中，正像对不返回结果的命令所作的那样，并且计划被以相同的方式被缓存。还有，如果该查询产生至少一行，特殊变量FOUND会被设置为真，而如果它不产生行则设置为假。

| 注意： |
| --- |
| 我们可能期望直接写SELECT能实现这个结果，但是当前唯一被接受的方式是PERFORM。一个能返回行的 SQL 命令（例如SELECT）将被当成一个错误拒绝，除非它像下一节中讨论的有一个INTO子句。 |

一个例子：

PERFORM create\_mv('cs\_session\_page\_requests\_mv', my\_query);

### 执行一个有单一行结果的查询

一个产生单一行（可能有多个列）的 SQL 命令的结果可以被赋值给一个记录变量、行类型变量或标量变量列表。这通过书写基础 SQL 命令并增加一个INTO子句来达成。例如：

SELECT select\_expressions INTO \[STRICT\] target FROM...;

INSERT... RETURNING expressions INTO \[STRICT\] target;

UPDATE... RETURNING expressions INTO \[STRICT\] target;

DELETE... RETURNING expressions INTO \[STRICT\] target;

其中target可以是一个记录变量、一个行变量或一个有逗号分隔的简单变量和记录/行域列表。PL/pgSQL变量将被替换到该查询的剩余部分中，并且计划会被缓存，正如之前描述的对不返回行的命令所做的。这对SELECT、带有RETURNING的INSERT/UPDATE/DELETE以及返回行集结果的工具命令（例如EXPLAIN）。除了INTO子句，SQL 命令和它在PL/pgSQL之外的写法一样。

| 提示： |
| --- |
| 注意带INTO的SELECT的这种解释和瀚高数据库常规的SELECT INTO命令有很大的不同，后者的INTO目标是一个新创建的表。如果你想要在一个PL/pgSQL函数中从一个SELECT的结果创建一个表，请使用语法CREATE TABLE... AS SELECT。 |

如果一行或一个变量列表被用作目标，该查询的结果列必须完全匹配该结果的结构，包括数量和数据类型，否则会发生一个运行时错误。当一个记录变量是目标时，它会自动地把自身配置成查询结果列组成的行类型。

INTO子句几乎可以出现在 SQL 命令中的任何位置。通常它被写成刚好在SELECT命令中的select\_expressions列表之前或之后，或者在其他命令类型的命令最后。我们推荐你遵循这种惯例，以防PL/pgSQL的解析器在未来的版本中变得更严格。

如果STRICT没有在INTO子句中被指定，那么target将被设置为该查询返回的第一个行，或者在该查询不返回行时设置为空（注意除非使用了ORDER BY，否则”第一行”的界定并不清楚）。第一行之后的任何结果行都会被抛弃。你可以检查特殊的FOUND变量来确定是否返回了一行：

SELECT \* INTO myrec FROM emp WHERE empname = myname;

IF NOT FOUND THEN

RAISE EXCEPTION 'employee % not found', myname;

END IF;

如果指定了STRICT选项，该查询必须刚好返回一行或者将会报告一个运行时错误，该错误可能是NO\_DATA\_FOUND（没有行）或TOO\_MANY\_ROWS（多于一行）。如果你希望捕捉该错误，可以使用一个异常块，例如：

BEGIN

SELECT \* INTO STRICT myrec FROM emp WHERE empname = myname;

EXCEPTION

WHEN NO\_DATA\_FOUND THEN

RAISE EXCEPTION 'employee % not found', myname;

WHEN TOO\_MANY\_ROWS THEN

RAISE EXCEPTION 'employee % not unique', myname;

END;

成功执行一个带STRICT的命令总是会将FOUND置为真。

对于带有RETURNING的INSERT/UPDATE/DELETE，即使没有指定STRICT，PL/pgSQL也会针对多于一个返回行的情况报告一个错误。这是因为没有类似于ORDER BY的选项可以用来决定应该返回哪个被影响的行。

如果为该函数启用了If print\_strict\_params，那么当因为STRICT的要求没有被满足而抛出一个错误时，该错误消息 的DETAIL将包括传递给该查询的参数信息。可以通过设置 plpgsql.print\_strict\_params为所有函数更改 print\_strict\_params设置，但是只有修改后被编译的函数 才会生效。也可以使用一个编译器选项来为一个函数启用它，例如：

CREATE FUNCTION get\_userid(username text) RETURNS int

AS $$

#print\_strict\_params on

DECLARE

userid int;

BEGIN

SELECT users.userid INTO STRICT userid

FROM users WHERE users.username = get\_userid.username;

RETURN userid;

END

$$ LANGUAGE plpgsql;

失败时，这个函数会产生一个这样的错误消息

ERROR: query returned no rows

DETAIL: parameters: $1 = 'nosuchuser'

CONTEXT: PL/pgSQL function get\_userid(text) line 6 at SQL statement

| 注意： |
| --- |
| STRICT选项匹配 Oracle PL/SQL 的SELECT INTO和相关语句的行为。 |

对于要处理来自于一个 SQL 查询的结果行的情况， 请见 11.6.6。

### 执行动态命令

很多时候你将想要在PL/pgSQL函数中产生动态命令，也就是每次执行中会涉及到不同表或不同数据类型的命令。PL/pgSQL通常对于命令所做的缓存计划尝试（如 后面的章节 中讨论）在这种情境下无法工作。要处理这一类问题，需要提供EXECUTE语句：

EXECUTE command-string \[ INTO \[STRICT\] target \] \[ USING expression \[,... \] \];

其中command-string是一个能得到一个包含要被执行命令字符串（类型text）的表达式。可选的target是一个记录变量、一个行变量或者一个逗号分隔的简单变量以及记录/行域的列表，该命令的结果将存储在其中。可选的USING表达式提供要被插入到该命令中的值。

在计算得到的命令字符串中，不会做PL/pgSQL变量的替换。任何所需的变量值必须在命令字符串被构造时被插入其中，或者你可以使用下面描述的参数。

还有，对于通过EXECUTE执行的命令不会有计划被缓存。该命令反而在每次运行时都会被做计划。因此，该命令字符串可以在执行不同表和列上动作的函数中被动态创建。

INTO子句指定一个返回行的 SQL 命令的结果应该被赋值到哪里。如果提供了一个行或变量列表，它必须完全匹配查询结果的结构（当使用一个记录变量时，它会自动把它自己配置为匹配结果结构）。如果返回多个行，只有第一个行会被赋值给INTO变量。如果没有返回行，NULL 会被赋值给INTO变量。如果没有指定INTO变量，该查询结果会被抛弃。

如果给出了STRICT选项，除非该查询刚好产生一行，否则将会报告一个错误。

命令字符串可以使用参数值，它们在命令中用$1、$2等引用。这些符号引用在USING子句中提供的值。这种方法常常更适合于把数据值作为文本插入到命令字符串中：它避免了将该值转换为文本以及转换回来的运行时负荷，并且它更不容易被 SQL 注入攻击，因为不需要引用或转义。一个例子是：

EXECUTE 'SELECT count(\*) FROM mytable WHERE inserted\_by = $1 AND inserted <= $2'

INTO c

USING checked\_user, checked\_date;

需要注意的是，参数符号只能用于数据值 — 如果想要使用动态决定的表名或列名，你必须将它们以文本形式插入到命令字符串中。例如，如果前面的那个查询需要在一个动态选择的表上执行，你可以这么做：

EXECUTE 'SELECT count(\*) FROM '

|| quote\_ident(tabname)

|| ' WHERE inserted\_by = $1 AND inserted <= $2'

INTO c

USING checked\_user, checked\_date;

一种更干净的方法是为表名或者列名使用format()的 %I规范（被新行分隔的字符串会被串接起来）：

EXECUTE format('SELECT count(\*) FROM %I '

'WHERE inserted\_by = $1 AND inserted <= $2', tabname)

INTO c

USING checked\_user, checked\_date;

另一个关于参数符号的限制是，它们只能在SELECT、INSERT、UPDATE和DELETE命令中工作。

在另一种语句类型（通常被称为实用语句）中，即使值是数据值，你也必须将它们以文本形式插入。

在上面第一个例子中，带有一个简单的常量命令字符串和一些USING参数的EXECUTE命令在功能上等效于直接用PL/pgSQL写的命令，并且允许自动发生PL/pgSQL变量替换。重要的不同之处在于，EXECUTE会在每一次执行时根据当前的参数值重新规划该命令，而PL/pgSQL则是创建一个通用计划并且将其缓存以便重用。在最佳计划强依赖于参数值的情况中，使用EXECUTE来明确地保证不会选择一个通用计划是很有帮助的。

EXECUTE目前不支持SELECT INTO。但是可以执行一个纯的SELECT命令并且指定INTO作为EXECUTE本身的一部分。

| 注意： |
| --- |
| PL/pgSQL中的EXECUTE语句与EXECUTE 瀚高数据库服务器支持的 SQL 语句无关。服务器的EXECUTE语句不能直接在PL/pgSQL函数中使用（并且也没有必要）。 |

例11.1. 在动态查询中引用值

在使用动态命令时经常不得不处理单引号的转义。我们推荐在函数体中使用美元符号引用来引用固定的文本（如果你有没有使用美元符界定的老代码， 请参考这里 的概述，这样在把上述代码转换成更合理的模式时会省力些）。

动态值需要被小心地处理，因为它们可能包含引号字符。一个使用 format()的例子（这假设你用美元符号引用了函数 体，因此引号不需要被双写）：

EXECUTE format('UPDATE tbl SET %I = $1 '

'WHERE key = $2', colname) USING newvalue, keyvalue;

还可以直接调用引用函数：

EXECUTE 'UPDATE tbl SET '

|| quote\_ident(colname)

|| ' = '

|| quote\_literal(newvalue)

|| ' WHERE key = '

|| quote\_literal(keyvalue);

这个例子展示了quote\_ident和quote\_literal函数的使用。为了安全，在进行一个动态查询中的插入之前，包含列或表标识符的表达式应该通过quote\_ident被传递。

如果表达式包含在被构造出的命令中应该是字符串的值时，它应该通过quote\_literal被传递。这些函数采取适当的步骤来分别返回被封闭在双引号或单引号中的文本，其中任何嵌入的特殊字符都会被正确地转义。

因为quote\_literal被标记为STRICT，当用一个空参数调用时，它总是会返回空。在上面的例子中，如果newvalue或keyvalue为空，整个动态查询字符串会变成空，导致从EXECUTE得到一个错误。可以通过使用quote\_nullable函数来避免这种问题，它工作起来和quote\_literal相同，除了用空参数调用时会返回一个字符串NULL。例如：

EXECUTE 'UPDATE tbl SET '

|| quote\_ident(colname)

|| ' = '

|| quote\_nullable(newvalue)

|| ' WHERE key = '

|| quote\_nullable(keyvalue);

如果正在处理的参数值可能为空，那么通常应该用quote\_nullable来代替quote\_literal。

通常，必须小心地确保查询中的空值不会递送意料之外的结果。例如如果keyvalue为空，下面的WHERE子句

'WHERE key = ' || quote\_nullable(keyvalue)

永远不会成功，因为在=操作符中使用空操作数得到的结果总是为空。如果想让空和一个普通键值一样工作，你应该将上面的命令重写成 'WHERE key IS NOT DISTINCT FROM ' || quote\_nullable(keyvalue) （目前，IS NOT DISTINCT FROM的处理效率不如=，因此只有在非常必要时才这样做。）。

请注意美元符号引用只对引用固定文本有用。尝试写出下面这个例子是一个非常糟糕的主意：

EXECUTE 'UPDATE tbl SET '

|| quote\_ident(colname)

|| ' = $$'

|| newvalue

|| '$$ WHERE key = '

|| quote\_literal(keyvalue);

因为如果newvalue的内容碰巧含有$$，那么这段代码就会出问题。同样的缺点可能适用于你选择的任何其他美元符号引用定界符。因此，要想安全地引用事先不知道的文本，必须恰当地使用quote\_literal、quote\_nullable或quote\_ident。

动态 SQL 语句也可以使用format函数来安全地构造。例如：

EXECUTE format('UPDATE tbl SET %I = %L '

'WHERE key = %L', colname, newvalue, keyvalue);

%I等效于quote\_ident并且 %L等效于quote\_nullable。 format函数可以和 USING子句一起使用：

EXECUTE format('UPDATE tbl SET %I = $1 WHERE key = $2', colname)

USING newvalue, keyvalue;

这种形式更好，因为变量被以它们天然的数据类型格式处理，而不是无 条件地把它们转换成文本并且通过%L引用它们。这也效率 更高。

动态命令和EXECUTE的一个更大的例子可以在例 11.10中找到，它会构建并且执行一个CREATE FUNCTION命令来定义一个新的函数。

### 获得结果状态

有好几种方法可以判断一条命令的效果。第一种方法是使用GET DIAGNOSTICS命令，其形式如下：

GET \[ CURRENT \] DIAGNOSTICS variable { = |:= } item \[,... \];

这条命令允许检索系统状态指示符。CURRENT是一个噪声词（ 另见这里 的GET STACKED DIAGNOSTICS）。每个item是一个关键字， 它标识一个要被赋予给指定变量的状态值（变量应具有正确的数据类型来接收状态值）。表11.1中展示了当前可用的状态项。冒号等号（:=）可以被用来取代 SQL 标准的=符号。例如：

GET DIAGNOSTICS integer\_var = ROW\_COUNT;

**表 11.1 可用的诊断项**

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| ROW\_COUNT | bigint | 最近的SQL命令处理的行数 |
| PG\_CONTEXT | text | 描述当前调用栈的文本行（ 详见 ） |

第二种判断命令效果的方法是检查一个名为FOUND的boolean类型的特殊变量。在每一次PL/ pgSQL函数调用时，FOUND开始都为假。它的值会被下面的每一种类型的语句设置：

• 如果一个SELECT INTO语句赋值了一行，它将把FOUND设置为真，如果没有返回行则将之设置为假。

• 如果一个PERFORM语句生成（并且抛弃）一行或多行，它将把FOUND设置为真，如果没有产生行则将之设置为假。

• 如果UPDATE、INSERT以及DELETE语句影响了至少一行，它们会把FOUND设置为真，如果没有影响行则将之设置为假。

• 如果一个FETCH语句返回了一行，它将把FOUND设置为真，如果没有返回行则将之设置为假。

• 如果一个MOVE语句成功地重定位了游标，它将会把FOUND设置为真，否则设置为假。

• 如果一个FOR或FOREACH语句迭代了一次或多次，它将会把FOUND设置为真，否则设置为假。当循环退出时，FOUND用这种方式设置；在循环执行中，尽管FOUND可能被循环体中的其他语句的执行所改变，但它不会被循环语句修改。

• 如果查询返回至少一行，RETURN QUERY和RETURN QUERY EXECUTE语句会把FOUND设为真，如果没有返回行则设置为假。

其他的PL/pgSQL语句不会改变FOUND的状态。尤其需要注意的一点是：EXECUTE会修改GET DIAGNOSTICS的输出，但不会修改FOUND的输出。

FOUND是每个PL/pgSQL函数的局部变量；任何对它的修改只影响当前的函数。

### 什么也不做

有时一个什么也不做的占位语句也很有用。例如，它能够指示 if/then/else 链中故意留出的空分支。可以使用NULL语句达到这个目的：

NULL;

例如，下面的两段代码是等价的：

BEGIN

y:= x / 0;

EXCEPTION

WHEN division\_by\_zero THEN

NULL; -- 忽略错误

END;

BEGIN

y:= x / 0;

EXCEPTION

WHEN division\_by\_zero THEN -- 忽略错误

END;

究竟使用哪一种取决于各人的喜好。

| 注意： |
| --- |
| 在 Oracle 的 PL/SQL 中，不允许出现空语句列表，并且因此在这种情况下必须使用NULL语句。而PL/pgSQL允许你什么也不写。 |

## 控制结构

控制结构可能是PL/pgSQL中最有用的（以及最重要）的部分了。利用PL/pgSQL的控制结构，你可以以非常灵活而且强大的方法操纵瀚高数据库的数据。

### 从一个函数返回

有两个命令让我们能够从函数中返回数据：RETURN和RETURN NEXT。

#### RETURN

RETURN expression;

带有一个表达式的RETURN用于终止函数并把expression的值返回给调用者。这种形式被用于不返回集合的PL/pgSQL函数。

如果一个函数返回一个标量类型，表达式的结果将被自动转换成函数的返回类型。但是要返回一个复合（行）值，你必须写一个正好产生所需列集合的表达式。这可能需要使用显式造型。

如果你声明带输出参数的函数，那么就只需要写不带表达式的RETURN。输出参数变量的当前值将被返回。

如果你声明函数返回void，一个RETURN语句可以被用来提前退出函数；但是不要在RETURN后面写一个表达式。

一个函数的返回值不能是未定义。如果控制到达了函数最顶层的块而没有碰到一个RETURN语句，那么会发生一个运行时错误。不过，这个限制不适用于带输出参数的函数以及返回void的函数。在这些情况中，如果顶层的块结束，将自动执行一个RETURN语句。

一些例子：

\-- 返回一个标量类型的函数

RETURN 1 + 2;

RETURN scalar\_var;

\-- 返回一个组合类型的函数

RETURN composite\_type\_var;

RETURN (1, 2, 'three'::text); -- 必须把列造型成正确的类型

#### RETURN NEXT以及RETURN QUERY

RETURN NEXT expression;

RETURN QUERY query;

RETURN QUERY EXECUTE command-string \[ USING expression \[,... \] \];

当一个PL/pgSQL函数被声明为返回SETOF sometype，那么遵循的过程则略有不同。在这种情况下，要返回的个体项被用一个RETURN NEXT或者RETURN QUERY命令的序列指定，并且接着会用一个不带参数的最终RETURN命令来指示这个函数已经完成执行。RETURN NEXT可以被用于标量和复合数据类型；对于复合类型，将返回一个完整的结果”表”。RETURN QUERY将执行一个查询的结果追加到一个函数的结果集中。在一个单一的返回集合的函数中，RETURN NEXT和RETURN QUERY可以被随意地混合，这样它们的结果将被串接起来。

RETURN NEXT和RETURN QUERY实际上不会从函数中返回 — 它们简单地向函数的结果集中追加零或多行。然后会继续执行PL/pgSQL函数中的下一条语句。随着后继的RETURN NEXT和RETURN QUERY命令的执行，结果集就建立起来了。最后一个RETURN（应该没有参数）会导致控制退出该函数（或者你可以让控制到达函数的结尾）。

RETURN QUERY有一种变体RETURN QUERY EXECUTE，它可以动态指定要被执行的查询。可以通过USING向计算出的查询字符串插入参数表达式，这和在EXECUTE命令中的方式相同。

如果你声明函数带有输出参数，只需要写不带表达式的RETURN NEXT。在每一次执行时，输出参数变量的当前值将被保存下来用于最终返回为结果的一行。注意为了创建一个带有输出参数的集合返回函数，在有多个输出参数时，你必须声明函数为返回SETOF record；或者如果只有一个类型为sometype的输出参数时，声明函数为SETOF sometype。

下面是一个使用RETURN NEXT的函数例子：

CREATE TABLE foo (fooid INT, foosubid INT, fooname TEXT);

INSERT INTO foo VALUES (1, 2, 'three');

INSERT INTO foo VALUES (4, 5, 'six');

CREATE OR REPLACE FUNCTION get\_all\_foo() RETURNS SETOF foo AS

$BODY$

DECLARE

r foo%rowtype;

BEGIN

FOR r IN

SELECT \* FROM foo WHERE fooid > 0

LOOP

\-- 这里可以做一些处理

RETURN NEXT r; -- 返回 SELECT 的当前行

END LOOP;

RETURN;

END

$BODY$

LANGUAGE plpgsql;

SELECT \* FROM get\_all\_foo();

这里是一个使用RETURN QUERY的函数的例子：

CREATE FUNCTION get\_available\_flightid(date) RETURNS SETOF integer AS

$BODY$

BEGIN

RETURN QUERY SELECT flightid

FROM flight

WHERE flightdate >= $1

AND flightdate < ($1 + 1);

\-- 因为执行还未结束，我们可以检查是否有行被返回

\-- 如果没有就抛出异常。

IF NOT FOUND THEN

RAISE EXCEPTION 'No flight at %.', $1;

END IF;

RETURN;

END

$BODY$

LANGUAGE plpgsql;

\-- 返回可用的航班或者在没有可用航班时抛出异常。

SELECT \* FROM get\_available\_flightid(CURRENT\_DATE);

| 注意： |
| --- |
| 如上所述，目前RETURN NEXT和RETURN QUERY的实现在从函数返回之前会把整个结果集都保存起来。这意味着如果一个PL/pgSQL函数生成一个非常大的结果集，性能可能会很差：数据将被写到磁盘上以避免内存耗尽，但是函数本身在整个结果集都生成之前不会退出。将来的PL/pgSQL版本可能会允许用户定义没有这种限制的集合返回函数。目前，数据开始被写入到磁盘的时机由配置变量work\_mem控制。拥有足够内存来存储大型结果集的管理员可以考虑增大这个参数。 |

### 从过程中返回

过程没有返回值。因此，过程的结束可以不用RETURN语句。 如果想用一个RETURN语句提前退出代码，只需写一个没有表达式的RETURN。

如果过程有输出参数，那么输出参数最终的值会被返回给调用者。

### 调用存储过程

PL/pgSQL函数，存储过程或DO块可以使用 CALL调存储用过程。 输出参数的处理方式与纯SQL中CALL的工作方式不同。 存储过程的每个INOUT参数必须和CALL语句中的变量对应， 并且无论存储过程返回什么，都会在返回后赋值给该变量。 例如：

CREATE PROCEDURE triple(INOUT x int)

LANGUAGE plpgsql

AS $$

BEGIN

x:= x \* 3;

END;

$$;

DO $$

DECLARE myvar int:= 5;

BEGIN

CALL triple(myvar);

RAISE NOTICE 'myvar = %', myvar; -- prints 15

END

$$;

### 条件

IF和CASE语句让你可以根据某种条件执行二选其一的命令。PL/pgSQL有三种形式的IF：

• IF... THEN... END IF

• IF... THEN... ELSE... END IF

• IF... THEN... ELSIF... THEN... ELSE... END IF

以及两种形式的CASE：

• CASE... WHEN... THEN... ELSE... END CASE

• CASE WHEN... THEN... ELSE... END CASE

#### IF-THEN

IF boolean-expression THEN

statements

END IF;

IF-THEN语句是IF的最简单形式。 如果条件为真，在THEN和END IF之间的语句将被执行。否则，将忽略它们。

例子：IF v\_user\_id <> 0 THEN

UPDATE users SET email = v\_email WHERE user\_id = v\_user\_id;

END IF;

#### IF-THEN-ELSE

IF boolean-expression THEN

statements

ELSE

statements

END IF;

IF-THEN-ELSE语句对IF-THEN进行了增加，它让你能够指定一组在条件不为真时应该被执行的语句（注意这也包括条件为 NULL 的情况）。

例子：

IF parentid IS NULL OR parentid = ''

THEN

RETURN fullname;

ELSE

RETURN hp\_true\_filename(parentid) || '/' || fullname;

END IF;

IF v\_count > 0 THEN

INSERT INTO users\_count (count) VALUES (v\_count);

RETURN 't';

ELSE

RETURN 'f';

END IF;

#### IF-THEN-ELSIF

IF boolean-expression THEN

statements

\[ ELSIF boolean-expression THEN

statements

\[ ELSIF boolean-expression THEN

statements

...

\]

\]

\[ ELSE

statements \]

END IF;

有时会有多于两种选择。IF-THEN-ELSIF则提供了一个简便的方法来检查多个条件。IF条件会被一个接一个测试，直到找到第一个为真的。然后执行相关语句，然后控制会被交给END IF之后的下一个语句（后续的任何IF条件不会被测试）。如果没有一个IF条件为真，那么ELSE块（如果有）将被执行。

这里有一个例子：

IF number = 0 THEN

result:= 'zero';

ELSIF number > 0 THEN

result:= 'positive';

ELSIF number < 0 THEN

result:= 'negative';

ELSE

\-- 嗯，唯一的其他可能性是数字为空

result:= 'NULL';

END IF;

关键词ELSIF也可以被拼写成ELSEIF。

另一个可以完成相同任务的方法是嵌套IF-THEN-ELSE语句，如下例：

IF demo\_row.sex = 'm' THEN

pretty\_sex:= 'man';

ELSE

IF demo\_row.sex = 'f' THEN

pretty\_sex:= 'woman';

END IF;

END IF;

不过，这种方法需要为每个IF都写一个匹配的END IF，因此当有很多选择时，这种方法比使用ELSIF要麻烦得多。

#### 简单CASE

CASE search-expression

WHEN expression \[, expression \[... \]\] THEN

statements

\[ WHEN expression \[, expression \[... \]\] THEN

statements

... \]

\[ ELSE

statements \]

END CASE;

CASE的简单形式提供了基于操作数等值判断的有条件执行。search-expression会被计算（一次）并且一个接一个地与WHEN子句中的每个expression比较。如果找到一个匹配，那么相应的statements会被执行，并且接着控制会被交给END CASE之后的下一个语句（后续的WHEN表达式不会被计算）。如果没有找到匹配，ELSE 语句会被执行。但是如果ELSE不存在，将会抛出一个CASE\_NOT\_FOUND异常。

这里是一个简单的例子：

CASE x

WHEN 1, 2 THEN

msg:= 'one or two';

ELSE

msg:= 'other value than one or two';

END CASE;

#### 搜索CASE

CASE

WHEN boolean-expression THEN

statements

\[ WHEN boolean-expression THEN

statements

... \]

\[ ELSE

statements \]

END CASE;

CASE的搜索形式基于布尔表达式真假的有条件执行。每一个WHEN子句的boolean-expression会被依次计算，直到找到一个得到真的。然后相应的statements会被执行，并且接下来控制会被传递给END CASE之后的下一个语句（后续的WHEN表达式不会被计算）。如果没有找到为真的结果，ELSE statements会被执行。但是如果ELSE不存在，那么将会抛出一个CASE\_NOT\_FOUND异常。

这里是一个例子：

CASE

WHEN x BETWEEN 0 AND 10 THEN

msg:= 'value is between zero and ten';

WHEN x BETWEEN 11 AND 20 THEN

msg:= 'value is between eleven and twenty';

END CASE;

这种形式的CASE整体上等价于IF-THEN-ELSIF，不同之处在于CASE到达一个被忽略的ELSE子句时会导致一个错误而不是什么也不做。

### 简单循环

使用LOOP、EXIT、CONTINUE、WHILE、FOR和FOREACH语句，你可以安排PL/pgSQL重复一系列命令。

#### LOOP

\[ <\<label>> \]

LOOP

statements

END LOOP \[ label \];

LOOP定义一个无条件的循环，它会无限重复直到被EXIT或RETURN语句终止。可选的label可以被EXIT和CONTINUE语句用在嵌套循环中指定这些语句引用的是哪一层循环。

#### EXIT

EXIT \[ label \] \[ WHEN boolean-expression \];

如果没有给出label，那么最内层的循环会被终止，然后跟在END LOOP后面的语句会被执行。如果给出了label，那么它必须是当前或者更高层的嵌套循环或者语句块的标签。然后该命名循环或块就会被终止，并且控制会转移到该循环/块相应的END之后的语句上。

如果指定了WHEN，只有boolean-expression为真时才会发生循环退出。否则，控制会转移到EXIT之后的语句。

EXIT可以被用在所有类型的循环中，它并不限于在无条件循环中使用。

在和BEGIN块一起使用时，EXIT会把控制交给块结束后的下一个语句。需要注意的是，一个标签必须被用于这个目的；一个没有被标记的EXIT永远无法被认为与一个BEGIN块匹配。

例子：

LOOP

\-- 一些计算

IF count > 0 THEN

EXIT; -- 退出循环

END IF;

END LOOP;

LOOP

\-- 一些计算

EXIT WHEN count > 0; -- 和前一个例子相同的结果

END LOOP;

<\<ablock>>

BEGIN

\-- 一些计算

IF stocks > 100000 THEN

EXIT ablock; -- 导致从 BEGIN 块中退出

END IF;

\-- 当stocks > 100000时，这里的计算将被跳过

END;

#### CONTINUE

CONTINUE \[ label \] \[ WHEN boolean-expression \];

如果没有给出label，最内层循环的下一次迭代会开始。也就是，循环体中剩余的所有语句将被跳过，并且控制会返回到循环控制表达式（如果有）来决定是否需要另一次循环迭代。

如果label存在，它指定应该继续执行的循环的标签。

如果指定了WHEN，该循环的下一次迭代只有在boolean-expression为真时才会开始。否则，控制会传递给CONTINUE后面的语句。

CONTINUE可以被用在所有类型的循环中，它并不限于在无条件循环中使用。

例子：

LOOP

\-- 一些计算

EXIT WHEN count > 100;

CONTINUE WHEN count < 50;

\-- 一些用于 count IN \[50.. 100\] 的计算

END LOOP;

#### WHILE

\[ <\<label>> \]

WHILE boolean-expression LOOP

Statements

END LOOP \[ label \];

只要boolean-expression被计算为真，WHILE语句就会重复一个语句序列。在每次进入到循环体之前都会检查该表达式。

例如：

WHILE amount\_owed > 0 AND gift\_certificate\_balance > 0 LOOP

\-- 这里是一些计算

END LOOP;

WHILE NOT done LOOP

\-- 这里是一些计算

END LOOP;

#### FOR（整型变体）

\[ <\<label>> \]

FOR name IN \[ REVERSE \] expression.. expression \[ BY expression \] LOOP

statements

END LOOP \[ label \];

这种形式的FOR会创建一个在一个整数范围上迭代的循环。变量name会自动定义为类型integer并且只在循环内存在（任何该变量名的现有定义在此循环内都将被忽略）。给出范围上下界的两个表达式在进入循环的时候计算一次。如果没有指定BY子句，迭代步长为1，否则步长是BY中指定的值，该值也只在循环进入时计算一次。如果指定了REVERSE，那么在每次迭代后步长值会被减除而不是增加。

整数FOR循环的一些例子：

FOR i IN 1..10 LOOP

\-- 我在循环中将取值 1,2,3,4,5,6,7,8,9,10

END LOOP;

FOR i IN REVERSE 10..1 LOOP

\-- 我在循环中将取值 10,9,8,7,6,5,4,3,2,1

END LOOP;

FOR i IN REVERSE 10..1 BY 2 LOOP

\-- 我在循环中将取值 10,8,6,4,2

END LOOP;

如果下界大于上界（或者在REVERSE情况下是小于），循环体根本不会被执行。而且不会抛出任何错误。

如果一个label被附加到FOR循环，那么整数循环变量可以用一个使用那个label的限定名引用。

### 通过查询结果循环

使用一种不同类型的FOR循环，你可以通过一个查询的结果进行迭代并且操纵相应的数据。

语法是：

\[ <\<label>> \]

FOR target IN query LOOP

statements

END LOOP \[ label \];

target是一个记录变量、行变量或者逗号分隔的标量变量列表。target被连续不断被赋予来自query的每一行，并且循环体将为每一行执行一次。下面是一个例子：

CREATE FUNCTION refresh\_mviews() RETURNS integer AS $$

DECLARE

mviews RECORD;

BEGIN

RAISE NOTICE 'Refreshing all materialized views...';

FOR mviews IN

SELECT n.nspname AS mv\_schema,

c.relname AS mv\_name,

pg\_catalog.pg\_get\_userbyid(c.relowner) AS owner

FROM pg\_catalog.pg\_class c

LEFT JOIN pg\_catalog.pg\_namespace n ON (n.oid = c.relnamespace)

WHERE c.relkind = 'm'

ORDER BY 1

LOOP

\-- Now "mviews" has one record with information about the materialized

view

RAISE NOTICE 'Refreshing materialized view %.% (owner: %)...',

quote\_ident(mviews.mv\_schema),

quote\_ident(mviews.mv\_name),

quote\_ident(mviews.owner);

EXECUTE format('REFRESH MATERIALIZED VIEW %I.%I', mviews.mv\_schema,

mviews.mv\_name);

END LOOP;

RAISE NOTICE 'Done refreshing materialized views.';

RETURN 1;

END;

$$ LANGUAGE plpgsql;

如果循环被一个EXIT语句终止，那么在循环之后你仍然可以访问最后被赋予的行值。

在这类FOR语句中使用的query可以是任何返回行给调用者的 SQL 命令：最常见的是SELECT，但你也可以使用带有RETURNING子句的INSERT、UPDATE或DELETE。一些EXPLAIN之类的功能性命令也可以用在这里。

PL/pgSQL变量会被替换到查询文本中，并且如(链接 和 链接)中详细讨论的，查询计划会被缓存以用于可能的重用。

FOR-IN-EXECUTE语句是在行上迭代的另一种方式：

\[ <\<label>> \]

FOR target IN EXECUTE text\_expression \[ USING expression \[,... \] \] LOOP

statements

END LOOP \[ label \];

这个例子类似前面的形式，只不过源查询被指定为一个字符串表达式，在每次进入FOR循环时都会计算它并且重新规划。这允许程序员在一个预先规划好了的命令的速度和一个动态命令的灵活性之间进行选择，就像一个纯EXECUTE语句那样。在使用EXECUTE时，可以通过USING将参数值插入到动态命令中。

另一种指定要对其结果迭代的查询的方式是将它声明为一个游标。这会在 后面的章节 中描述。

### 通过数组循环

FOREACH循环很像一个FOR循环，但不是通过一个 SQL 查询返回的行进行迭代，它通过一个数组值的元素来迭代（通常，FOREACH意味着通过一个组合值表达式的部件迭代；用于通过除数组之外组合类型进行循环的变体可能会在未来被加入）。在一个数组上循环的FOREACH语句是：

\[ <\<label>> \]

FOREACH target \[ SLICE number \] IN ARRAY expression LOOP

statements

END LOOP \[ label \];

如果没有SLICE，或者如果没有指定SLICE 0，循环会通过计算expression得到的数组的个体元素进行迭代。target变量被逐一赋予每一个元素值，并且循环体会为每一个元素执行。这里是一个通过整数数组的元素循环的例子：

CREATE FUNCTION sum(int\[\]) RETURNS int8 AS $$

DECLARE

s int8:= 0;

x int;

BEGIN

FOREACH x IN ARRAY $1

LOOP

s:= s + x;

END LOOP;

RETURN s;

END;

$$ LANGUAGE plpgsql;

元素会被按照存储顺序访问，而不管数组的维度数。尽管target通常只是一个单一变量，当通过一个组合值（记录）的数组循环时，它可以是一个变量列表。在那种情况下，对每一个数组元素，变量会被从组合值的连续列赋值。

通过一个正SLICE值，FOREACH通过数组的切片而不是单一元素迭代。SLICE值必须是一个不大于数组维度数的整数常量。target变量必须是一个数组，并且它接收数组值的连续切片，其中每一个切片都有SLICE指定的维度数。这里是一个通过一维切片迭代的例子：

CREATE FUNCTION scan\_rows(int\[\]) RETURNS void AS $$

DECLARE

x int\[\];

BEGIN

FOREACH x SLICE 1 IN ARRAY $1

LOOP

RAISE NOTICE 'row = %', x;

END LOOP;

END;

$$ LANGUAGE plpgsql;

SELECT scan\_rows(ARRAY\[\[1,2,3\],\[4,5,6\],\[7,8,9\],\[10,11,12\]\]);

NOTICE: row = {1,2,3}

NOTICE: row = {4,5,6}

NOTICE: row = {7,8,9}

NOTICE: row = {10,11,12}

### 俘获错误

默认情况下，任何在PL/pgSQL函数中发生的错误会中止该函数的执行，而且实际上会中止其周围的事务。你可以使用一个带有EXCEPTION子句的BEGIN块俘获错误并且从中恢复。其语法是BEGIN块通常的语法的一个扩展：

\[ <\<label>> \]

\[ DECLARE

declarations \]

BEGIN

statements

EXCEPTION

WHEN condition \[ OR condition... \] THEN

handler\_statements

\[ WHEN condition \[ OR condition... \] THEN

handler\_statements

... \]

END;

如果没有发生错误，这种形式的块只是简单地执行所有statements， 并且接着控制转到END之后的下一个语句。但是如果在statements内发生了一个错误，则会放弃对statements的进一步处理，然后控制会转到EXCEPTION列表。系统会在列表中寻找匹配所发生错误的第一个condition。如果找到一个匹配，则执行对应的handler\_statements，并且接着把控制转到END之后的下一个语句。如果没有找到匹配，该错误就会传播出去，就好像根本没有EXCEPTION一样：错误可以被一个带有EXCEPTION的闭合块捕捉，如果没有EXCEPTION则中止该函数的处理。

condition的名字可以是附录 A中显示的任何名字。一个分类名匹配其中所有的错误。特殊的条件名OTHERS匹配除了QUERY\_CANCELED和ASSERT\_FAILURE之外的所有错误类型（虽然通常并不明智，还是可以用名字捕获这两种错误类型）。条件名是大小写无关的。一个错误条件也可以通过SQLSTATE代码指定，例如以下是等价的：

WHEN division\_by\_zero THEN...

WHEN SQLSTATE '22012' THEN...

如果在选中的handler\_statements内发生了新的错误，那么它不能被这个EXCEPTION子句捕获，而是被传播出去。一个外层的EXCEPTION子句可以捕获它。

当一个错误被EXCEPTION捕获时，PL/pgSQL函数的局部变量会保持错误发生时的值，但是该块中所有对持久数据库状态的改变都会被回滚。例如，考虑这个片段：

INSERT INTO mytab(firstname, lastname) VALUES('Tom', 'Jones');

BEGIN

UPDATE mytab SET firstname = 'Joe' WHERE lastname = 'Jones';

x:= x + 1;

y:= x / 0;

EXCEPTION

WHEN division\_by\_zero THEN

RAISE NOTICE 'caught division\_by\_zero';

RETURN x;

END;

当控制到达对y赋值的地方时，它会带着一个division\_by\_zero错误失败。这个错误将被EXCEPTION子句捕获。而在RETURN语句中返回的值将是x增加过后的值。但是UPDATE命令的效果将已经被回滚。不过，在该块之前的INSERT将不会被回滚，因此最终的结果是数据库包含Tom Jones但不包含Joe Jones。

| 提示： |
| --- |
| 进入和退出一个包含EXCEPTION子句的块要比不包含EXCEPTION的块开销大的多。因此，只在必要的时候使用EXCEPTION。 |

例 11.2. UPDATE/INSERT的异常

这个例子使用异常处理来酌情执行UPDATE或 INSERT。我们推荐应用使用带有 ON CONFLICT DO UPDATE的INSERT 而不是真正使用这种模式。下面的例子主要是为了展示 PL/pgSQL如何控制流程：

CREATE TABLE db (a INT PRIMARY KEY, b TEXT);

CREATE FUNCTION merge\_db(key INT, data TEXT) RETURNS VOID AS

$$

BEGIN

LOOP

\-- 首先尝试更新见

UPDATE db SET b = data WHERE a = key;

IF found THEN

RETURN;

END IF;

\-- 不在这里，那么尝试插入该键

\-- 如果其他某人并发地插入同一个键，

\-- 我们可能得到一个唯一键失败

BEGIN

INSERT INTO db(a,b) VALUES (key, data);

RETURN;

EXCEPTION WHEN unique\_violation THEN

\-- 什么也不做，并且循环再次尝试 UPDATE

END;

END LOOP;

END;

$$

LANGUAGE plpgsql;

SELECT merge\_db(1, 'david');

SELECT merge\_db(1, 'dennis');

这段代码假定unique\_violation错误是INSERT造成，并且不是由该表上一个触发器函数中的INSERT导致。如果在该表上有多于一个唯一索引，也可能会发生不正确的行为，因为不管哪个索引导致该错误它都将重试该操作。通过接下来要讨论的特性来检查被捕获的错误是否为所预期的会更安全。

#### 得到有关一个错误的信息

异常处理器经常被用来标识发生的特定错误。有两种方法来得到PL/pgSQL中当前异常的信息：特殊变量和GET STACKED DIAGNOSTICS命令。

在一个异常处理器内，特殊变量SQLSTATE包含了对应于被抛出异常的错误代码（可能的错误代码列表见表 A.1）。特殊变量SQLERRM包含与该异常相关的错误消息。这些变量在异常处理器外是未定义的。

在一个异常处理器内，我们也可以用GET STACKED DIAGNOSTICS命令检索有关当前异常的信息，该命令的形式为：

GET STACKED DIAGNOSTICS variable { = |:= } item \[,... \];

每个item是一个关键词，它标识一个被赋予给指定变量（应该具有接收该值的正确数据类型）的状态值。表11.2中显示了当前可用的状态项。

**表 11.2 错误诊断项**

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| RETURNED\_SQLSTATE | text | 该异常的 SQLSTATE 错误代码 |
| COLUMN\_NAME | text | 与异常相关的列名 |
| CONSTRAINT\_NAME | text | 与异常相关的约束名 |
| PG\_DATATYPE\_NAME | text | 与异常相关的数据类型名 |
| MESSAGE\_TEXT | text | 该异常的主要消息的文本 |
| TABLE\_NAME | text | 与异常相关的表名 |
| SCHEMA\_NAME | text | 与异常相关的模式名 |
| PG\_EXCEPTION\_DETAIL | text | 该异常的详细消息文本（如果有） |
| PG\_EXCEPTION\_HINT | text | 该异常的提示消息文本（如果有） |
| PG\_EXCEPTION\_CONTEXT | text | 描述产生异常时调用栈的文本行（见第11.6.9 节） |

如果异常没有为一个项设置值，将返回一个空字符串。

这里是一个例子：

DECLARE

text\_var1 text;

text\_var2 text;

text\_var3 text;

BEGIN

\-- 某些可能导致异常的处理

...

EXCEPTION WHEN OTHERS THEN

GET STACKED DIAGNOSTICS text\_var1 = MESSAGE\_TEXT,

text\_var2 = PG\_EXCEPTION\_DETAIL,

text\_var3 = PG\_EXCEPTION\_HINT;

END;

### 获得执行位置信息

GET DIAGNOSTICS（在 前面的章节 中描述）命令检索有关当前执行状态的信息（反之上文讨论的GET STACKED DIAGNOSTICS命令会把有关执行状态的信息报告成一个以前的错误）。

它的PG\_CONTEXT状态项可用于标识当前执行位置。状态项PG\_CONTEXT将返回一个文本字符串，其中有描述该调用栈的多行文本。第一行会指向当前函数以及当前正在执行GET DIAGNOSTICS的命令。第二行及其后的行表示调用栈中更上层的调用函数。例如：

CREATE OR REPLACE FUNCTION outer\_func() RETURNS integer AS $$

BEGIN

RETURN inner\_func();

END;

$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION inner\_func() RETURNS integer AS $$

DECLARE

stack text;

BEGIN

GET DIAGNOSTICS stack = PG\_CONTEXT;

RAISE NOTICE E'--- Call Stack ---\\n%', stack;

RETURN 1;

END;

$$ LANGUAGE plpgsql;

SELECT outer\_func();

NOTICE: --- Call Stack ---

PL/pgSQL function inner\_func() line 5 at GET DIAGNOSTICS

PL/pgSQL function outer\_func() line 3 at RETURN

CONTEXT: PL/pgSQL function outer\_func() line 3 at RETURN

outer\_func

\------------

1

(1 row)

GET STACKED DIAGNOSTICS... PG\_EXCEPTION\_CONTEXT返回同类的栈跟踪，但是它描述检测到错误的位置而不是当前位置。

## 游标

和一次执行整个查询不同，可以建立一个游标来封装该查询，并且接着一次读取该查询结果的一些行。这样做的原因之一是在结果中包含大量行时避免内存不足（不过，PL/pgSQL用户通常不需要担心这些，因为FOR循环在内部会自动使用一个游标来避免内存问题）。一种更有趣的用法是返回一个函数已经创建的游标的引用，允许调用者读取行。这提供了一种有效的方法从函数中返回大型行集。

### 声明游标变量

所有在PL/pgSQL中对游标的访问都会通过游标变量，它总是特殊的数据类型refcursor。创建游标变量的一种方法是把它声明为一个类型为refcursor的变量。另外一种方法是使用游标声明语法，通常是：

name \[ \[ NO \] SCROLL \] CURSOR \[ ( arguments ) \] FOR query;

（为了对Oracle的兼容性，可以用IS替代FOR）。如果指定了SCROLL，那么游标可以反向滚动；如果指定了NO SCROLL，那么反向取的动作会被拒绝；如果二者都没有被指定，那么能否进行反向取就取决于查询。如果指定了arguments， 那么它是一个逗号分隔的name datatype对的列表， 它们定义在给定查询中要被参数值替换的名称。实际用于替换这些名字的值将在游标被打开之后指定。

一些例子：

DECLARE

curs1 refcursor;

curs2 CURSOR FOR SELECT \* FROM tenk1;

curs3 CURSOR (key integer) FOR SELECT \* FROM tenk1 WHERE unique1 = key;

所有这三个变量都是refcursor类型，但是第一个可以用于任何查询，而第二个已经被绑定了一个完全指定的查询，并且最后一个被绑定了一个参数化查询。（游标被打开时，key将被一个整数参数值替换）。变量curs1被称为未绑定，因为它没有被绑定到任何特定查询。

### 打开游标

在一个游标可以被用来检索行之前，它必需先被打开（这是和 SQL 命令DECLARE CURSOR等效的操作）。PL/pgSQL有三种形式的OPEN命令，其中两种用于未绑定游标变量，另外一种用于已绑定的游标变量。

| 注意： |
| --- |
| 可以通过 通过一个游标的结果循环 中描述的FOR语句在不显式打开游标的情况下使用已绑定的游标变量。 |

#### OPEN FOR query

OPEN unbound\_cursorvar \[ \[ NO \] SCROLL \] FOR query;

该游标变量被打开并且被给定要执行的查询。游标不能是已经打开的，并且它必需已经被声明为一个未绑定的游标变量（也就是声明为一个简单的refcursor变量）。该查询必须是一条SELECT或者其它返回行的东西（例如EXPLAIN）。该查询会按照其它PL/pgSQL中的 SQL 命令同等的方式对待：先代换PL/pgSQL变量名，并且执行计划会被缓存用于可能的重用。当一个PL/pgSQL变量被替换到游标查询中时，替换的值是在OPEN时它所具有的值。对该变量后续的改变不会影响游标的行为。对于一个已经绑定的游标，SCROLL和NO SCROLL选项具有相同的含义。

一个例子：

OPEN curs1 FOR SELECT \* FROM foo WHERE key = mykey;

#### OPEN FOR EXECUTE

OPEN unbound\_cursorvar \[ \[ NO \] SCROLL \] FOR EXECUTE query\_string

\[ USING expression \[,... \] \];

打开游标变量并且执行指定的查询。该游标不能是已打开的，并且必须已经被声明为一个未绑定的游标变量（也就是声明为一个简单的refcursor变量）。该查询以和EXECUTE中相同的方式被指定为一个字符串表达式。照例，这提供了灵活性，因此查询计划可以在两次运行之间变化（见 计划缓存 ），并且它也意味着在该命令字符串上还没有完成变量替换。正如EXECUTE，可以通过format()和USING将参数值插入到动态命令中。SCROLL和NO SCROLL选项具有和已绑定游标相同的含义。

一个例子：

OPEN curs1 FOR EXECUTE format('SELECT \* FROM %I WHERE col1 = $1',tabname) USING keyvalue;

在这个例子中，表名被通过format()插入到查询中。 col1的比较值被通过一个USING参数插入， 所以它不需要引用。

#### 打开一个已绑定的游标

OPEN bound\_cursorvar \[ ( \[ argument\_name:= \] argument\_value \[,...\] ) \];

这种形式的OPEN被用于打开一个游标变量，它的查询是在声明时绑定的。该游标不能是已经打开的。当且仅当该游标被声明为接收参数时，才必需出现一个实际参数值表达式的列表，这些值将被替换到命令中。

一个已绑定游标的查询计划总是被认为是可缓存的，在这种情况中没有EXECUTE的等效形式。注意SCROLL和NO SCROLL不能在OPEN中指定，因为游标的滚动行为已经被确定。

使用位置或命名记号可以传递参数值。在位置记号中，所有参数都必须按照顺序指定。在命名记号中，每一个参数的名字被使用:=指定以将它和参数表达式分隔开。类似于 OCIEnvInit 中描述的调用函数，也允许混合位置和命名记号。

例子（这些例子使用上面例子中的游标声明）：

OPEN curs2;

OPEN curs3(42);

OPEN curs3(key:= 42);

因为在一个已绑定游标的查询上已经完成了变量替换，实际有两种方式将值传到游标中：给OPEN一个显式参数，或者在查询中隐式引用一个PL/pgSQL变量。不过，只有在已绑定游标之前声明的变量才将会被替换到游标中。在两种情况下，要被传递的值都是在OPEN时确定的。例如，得到上例中curs3相同效果的另一种方式是

DECLARE

key integer;

curs4 CURSOR FOR SELECT \* FROM tenk1 WHERE unique1 = key;

BEGIN

key:= 42;

OPEN curs4;

### 使用游标

一旦一个游标已经被打开，那么就可以用这里描述的语句操作它。

这些操作不需要发生在打开该游标开始操作的同一个函数中。你可以从一个函数返回一个refcursor值，并且让调用者在该游标上操作（在内部，refcursor值只是一个包含该游标活动查询的所谓入口的字符串名称。这个名字可以被传递、赋予给其它refcursor变量等等，而不用担心扰乱入口）。

所有入口会在事务的结尾被隐式地关闭。因此一个refcursor值只能在该事务结束前用于引用一个打开的游标。

#### FETCH

FETCH \[ direction { FROM | IN } \] cursor INTO target;

就像SELECT INTO一样，FETCH从游标中检索下一行到目标中，目标可以是一个行变量、记录变量或者逗号分隔的简单变量列表。如果没有下一行，目标会被设置为 NULL。与SELECT INTO一样，可以检查特殊变量FOUND来看一行是否被获得。

direction子句可以是 SQL FETCH命令中允许的任何变体，除了那些能够取得多于一行的。即它可以是NEXT、 PRIOR、 FIRST、LAST、ABSOLUTE count、 RELATIVE count、 FORWARD或者 BACKWARD。省略direction和指定NEXT是一样的。在使用count的形式中，count可以是任意的整数值表达式（与SQL命令FETCH不一样，FETCH仅允许整数常量）。除非游标被使用SCROLL选项声明或打开，否则要求反向移动的direction值很可能会失败。

cursor必须是一个引用已打开游标入口的refcursor变量名。

例子：

FETCH curs1 INTO rowvar;

FETCH curs2 INTO foo, bar, baz;

FETCH LAST FROM curs3 INTO x, y;

FETCH RELATIVE -2 FROM curs4 INTO x;

#### MOVE

MOVE \[ direction { FROM | IN } \] cursor;

MOVE重新定位一个游标而不检索任何数据。MOVE的工作方式与FETCH命令很相似，但是MOVE只是重新定位游标并且不返回至移动到的行。与SELECT INTO一样，可以检查特殊变量FOUND来看要移动到的行是否存在。

例子：

MOVE curs1;

MOVE LAST FROM curs3;

MOVE RELATIVE -2 FROM curs4;

MOVE FORWARD 2 FROM curs4;

#### UPDATE/DELETE WHERE CURRENT OF

UPDATE table SET... WHERE CURRENT OF cursor;

DELETE FROM table WHERE CURRENT OF cursor;

当一个游标被定位到一个表行上时，使用该游标标识该行就可以对它进行更新或删除。对于游标的查询可以是什么是有限制的（尤其是不能有分组），并且最好在游标中使用FOR UPDATE。详见DECLARE参考页。

一个例子：

UPDATE foo SET dataval = myval WHERE CURRENT OF curs1;

#### CLOSE

CLOSE cursor;

CLOSE关闭一个已打开游标的底层入口。这样就可以在事务结束之前释放资源，或者释放掉该游标变量以便再次打开。

一个例子：

CLOSE curs1;

#### 返回游标

PL/pgSQL函数可以向调用者返回游标。这对于返回多行或多列（特别是巨大的结果集）很有用。要想这么做，该函数打开游标并且把该游标的名字返回给调用者（或者简单的使用调用者指定的或已知的入口名打开游标）。调用者接着可以从游标中取得行。游标可以由调用者关闭，或者是在事务关闭时自行关闭。

用于一个游标的入口名可以由编程者指定或者自动生成。要指定一个入口名，只需要在打开refcursor变量之前简单地为它赋予一个字符串。OPEN将把refcursor变量的字符串值用作底层入口的名字。不过，如果refcursor变量为空，OPEN会自动生成一个与任何现有入口不冲突的名称，并且将它赋予给refcursor变量。

| 注意： |
| --- |
| 一个已绑定的游标变量被初始化为表示其名称的字符串值，因此入口的名字和游标变量名相同，除非程序员在打开游标之前通过赋值覆盖了这个名字。但是一个未绑定的游标变量最初默认为空值，因此它会收到一个自动生成的唯一名字，除非被覆盖。 |

下面的例子显示了一个调用者提供游标名字的方法：

CREATE TABLE test (col text);

INSERT INTO test VALUES ('123');

CREATE FUNCTION reffunc(refcursor) RETURNS refcursor AS '

BEGIN

OPEN $1 FOR SELECT col FROM test;

RETURN $1;

END;

' LANGUAGE plpgsql;

BEGIN;

SELECT reffunc('funccursor');

FETCH ALL IN funccursor;

COMMIT;

下面的例子使用了自动游标名生成：

CREATE FUNCTION reffunc2() RETURNS refcursor AS '

DECLARE

ref refcursor;

BEGIN

OPEN ref FOR SELECT col FROM test;

RETURN ref;

END;

' LANGUAGE plpgsql;

\-- 需要在一个事务中使用游标。

BEGIN;

SELECT reffunc2();

reffunc2

\--------------------

\<unnamed cursor 1>

(1 row)

FETCH ALL IN "\<unnamed cursor 1>";

COMMIT;

下面的例子展示了从一个函数中返回多个游标的一种方法：

CREATE FUNCTION myfunc(refcursor, refcursor) RETURNS SETOF refcursor AS $$

BEGIN

OPEN $1 FOR SELECT \* FROM table\_1;

RETURN NEXT $1;

OPEN $2 FOR SELECT \* FROM table\_2;

RETURN NEXT $2;

END;

$$ LANGUAGE plpgsql;

\-- 需要在一个事务中使用游标。

BEGIN;

SELECT \* FROM myfunc('a', 'b');

FETCH ALL FROM a;

FETCH ALL FROM b;

COMMIT;

### 通过一个游标的结果循环

有一种FOR语句的变体，它允许通过游标返回的行进行迭代。语法是：

\[ <\<label>> \]

FOR recordvar IN bound\_cursorvar \[ ( \[ argument\_name:= \] argument\_value

\[,...\] ) \] LOOP

statements

END LOOP \[ label \];

该游标变量必须在声明时已经被绑定到某个查询，并且它不能已经被打开。FOR语句会自动打开游标，并且在退出循环时自动关闭游标。当且仅当游标被声明要使用参数时，才必须出现一个实际参数值表达式的列表。这些值会被替换到查询中，采用OPEN期间的方式（见 打开一个已绑定的游标 ）。

变量recordvar会被自动定义为record类型，并且只存在于循环内部（循环中该变量名任何已有定义都会被忽略）。每一个由游标返回的行都会被陆续地赋值给这个记录变量并且执行循环体。

## 事务管理

在由CALL命令调用的过程中以及匿名代码块（DO命令）中，可以用命令COMMIT和ROLLBACK结束事务。在一个事务被使用这些命令结束后，一个新的事务会被自动开始，因此没有单独的START TRANSACTION命令（注意BEGIN和END在PL/pgSQL中有不同的含义）。

这里是一个简单的例子：

CREATE PROCEDURE transaction\_test1()

LANGUAGE plpgsql

AS $$

BEGIN

FOR i IN 0..9 LOOP

INSERT INTO test1 (a) VALUES (i);

IF i % 2 = 0 THEN

COMMIT;

ELSE

ROLLBACK;

END IF;

END LOOP;

END

$$;

CALL transaction\_test1();

新事务开始时具有默认事务特征，如事务隔离级别。在循环中提交事务的情况下，可能需要以与前一个事务相同的特征来自动启动新事务。 命令COMMIT AND CHAIN和ROLLBACK AND CHAIN可以完成此操作。

只有在从顶层调用的CALL或DO中才能进行事务控制，在没有任何其他中间命令的嵌套CALL或DO调用中也能进行事务控制。例如，如果调用栈是CALL proc1() → CALL proc2()→ CALL proc3()，那么第二个和第三个过程可以执行事务控制动作。但是如果调用栈是CALL proc1() → SELECT func2() → CALL proc3()，则最后一个过程不能做事务控制，因为中间有SELECT。

对于游标循环有特殊的考虑。看看这个例子：

CREATE PROCEDURE transaction\_test2()

LANGUAGE plpgsql

AS $$

DECLARE

r RECORD;

BEGIN

FOR r IN SELECT \* FROM test2 ORDER BY x LOOP

INSERT INTO test1 (a) VALUES (r.x);

COMMIT;

END LOOP;

END;

$$;

CALL transaction\_test2();

通常，游标会在事务提交时被自动关闭。但是，一个作为循环的组成部分创建的游标会自动被第一个COMMIT或ROLLBACK转变成一个可保持游标。这意味着该游标在第一个COMMIT或ROLLBACK处会被完全计算出来，而不是逐行被计算。该游标在循环后仍会被自动删除，因此这通常对用户是不可见的。

有非只读命令（UPDATE... RETURNING）驱动的游标循环中不允许有事务命令。

事务在一个具有异常处理部分的块中不能被结束。

## 错误和消息

### 报告错误和消息

使用RAISE语句报告消息以及抛出错误。

RAISE \[ level \] 'format' \[, expression \[,... \]\] \[ USING option = expression

\[,... \] \];

RAISE \[ level \] condition\_name \[ USING option = expression \[,... \] \];

RAISE \[ level \] SQLSTATE 'sqlstate' \[ USING option = expression \[,... \] \];

RAISE \[ level \] USING option = expression \[,... \];

RAISE;

level选项指定了错误的严重性。允许的级别有DEBUG、LOG、INFO、NOTICE, WARNING以及EXCEPTION，默认级别是EXCEPTION。EXCEPTION会抛出一个错误（通常会中止当前事务）。其他级别仅仅是产生不同优先级的消息。不管一个特定优先级的消息是被报告给客户端、还是写到服务器日志、亦或是二者同时都做，这都由log\_min\_messages和client\_min\_messages配置变量控制。详见 SQL命令 。

如果有level， 在它后面可以写一个format（ 它必须是一个简单字符串而不是表达式）。该格式字符串指定要被报告的 错误消息文本。在格式字符串后面可以跟上可选的要被插入到该消息的 参数表达式。在格式字符串中，%会被下一个可选参数 的值所替换。写%%可以发出一个字面的 %。参数的数量必须匹配格式字符串中% 占位符的数量，否则在函数编译期间就会发生错误。

在这个例子中，v\_job\_id的值将替换字符串中的%：

RAISE NOTICE 'Calling cs\_create\_job(%)', v\_job\_id;

通过写一个后面跟着option = expression项的USING，可以为错误报告附加一些额外信息。

每一个expression可以是任意字符串值的表达式。允许的option关键词是：

MESSAGE

设置错误消息文本。这个选项可以被用于在USING之前包括一个格式字符串的RAISE形式。

DETAIL

提供一个错误的细节消息。

HINT

提供一个提示消息。

ERRCODE

指定要报告的错误代码（SQLSTATE），可以用附录 A中所示的条件名，或者直接作为一

个五字符的 SQLSTATE 代码。

COLUMN

CONSTRAINT

DATATYPE

TABLE

SCHEMA

提供一个相关对象的名称。

这个例子将用给定的错误消息和提示中止事务：

RAISE EXCEPTION 'Nonexistent ID --> %', user\_id

USING HINT = 'Please check your user ID';

这两个例子展示了设置 SQLSTATE 的两种等价的方法：

RAISE 'Duplicate user ID: %', user\_id USING ERRCODE = 'unique\_violation';

RAISE 'Duplicate user ID: %', user\_id USING ERRCODE = '23505';

还有第二种RAISE语法，在其中主要参数是要被报告的条件名或 SQLSTATE，例如：

RAISE division\_by\_zero;

RAISE SQLSTATE '22012';

在这种语法中，USING能被用来提供一个自定义的错误消息、细节或提示。另一种做前面的例子的方法是

RAISE unique\_violation USING MESSAGE = 'Duplicate user ID: ' || user\_id;

仍有另一种变体是写RAISE USING或者RAISE level USING并且把所有其他东西都放在USING列表中。

RAISE的最后一种变体根本没有参数。这种形式只能被用在一个BEGIN块的EXCEPTION子句中，它导致当前正在被处理的错误被重新抛出。

| 注意： |
| --- |
| 没有参数的RAISE被解释为重新抛出来自包含活动异常处理器的块的错误。因此一个嵌套在那个处理器中的EXCEPTION子句无法捕捉它，即使RAISE位于嵌套EXCEPTION子句的块中也是这样。这种行为很奇怪，也并不兼容 Oracle 的 PL/SQL。 |

如果在一个RAISE EXCEPTION命令中没有指定条件名以及 SQLSTATE，默认是使用ERRCODE\_RAISE\_EXCEPTION (P0001)。如果没有指定消息文本，默认是使用条件名或SQLSTATE 作为消息文本。

| 注意： |
| --- |
| 当用 SQLSTATE 代码指定一个错误代码时，你不会受到预定义错误代码的限制，而是可以选择任何由五位以及大写 ASCII 字母构成的错误代码，只有00000不能使用。我们推荐尽量避免抛出以三个零结尾的错误代码，因为这些是分类代码并且只能用来捕获整个类别。 |

### 检查断言

ASSERT语句是一种向 PL/pgSQL函数中插入调试检查的方便方法。

ASSERT condition \[, message \];

condition是一个布尔表达式，它被期望总是计算为真。如果确实如此， ASSERT语句不会再做什么。但如果结果是假 或者空，那么将发生一个ASSERT\_FAILURE异常（如果在计算 condition时发生错误，它会被报告为一个普通错误）。

如果提供了可选的message，它是一个结果（如果非空）被用来替换默认错误消息文本 “assertion failed”的表达式（如果 condition失败）。 message表达式在 断言成功的普通情况下不会被计算。

通过配置参数plpgsql.check\_asserts可以启用或者禁用断言测试，这个参数接受布尔值且默认为on。如果这个参数为off，则ASSERT语句什么也不做。

注意ASSERT是为了检测程序的 bug，而不是 报告普通的错误情况。如果要报告普通错误，请使用前面介绍的 RAISE语句。

## 触发器函数

PL/pgSQL可以被用来在数据更改或者数据库事件上定义触发器函数。触发器函数用CREATE FUNCTION命令创建，它被声明为一个没有参数并且返回类型为trigger（对于数据更改触发器）或者event\_trigger（对于数据库事件触发器）的函数。名为PG\_something的特殊局部变量将被自动创建用以描述触发该调用的条件。

### 数据改变的触发器

一个数据更改触发器被声明为一个没有参数并且返回类型为trigger的函数。注意，如下所述，即便该函数准备接收一些在CREATE TRIGGER中指定的参数 — 这类参数通过TG\_ARGV传递，也必须把它声明为没有参数。

当一个PL/pgSQL函数当做触发器调用时，在顶层块会自动创建一些特殊变量。它们是：

NEW

数据类型是RECORD；该变量为行级触发器中的INSERT/UPDATE操作保持新数据行。在语句级别的触发器以及DELETE操作，这个变量是null。

OLD

数据类型是RECORD；该变量为行级触发器中的UPDATE/DELETE操作保持新数据行。在语句级别的触发器以及INSERT操作，这个变量是null。

TG\_NAME

数据类型是name；该变量包含实际触发的触发器名。

TG\_WHEN

数据类型是text；是值为BEFORE、AFTER或INSTEAD OF的一个字符串，取决于触发器的定义。

TG\_LEVEL

数据类型是text；是值为ROW或STATEMENT的一个字符串，取决于触发器的定义。

TG\_OP

数据类型是text；是值为INSERT、UPDATE、DELETE或TRUNCATE的一个字符串，它说明触发器是为哪个操作引发。

TG\_RELID

数据类型是oid；是导致触发器调用的表的对象 ID。

TG\_RELNAME

数据类型是name；是导致触发器调用的表的名称。现在已经被废弃，并且可能在未来的一个发行中消失。使用TG\_TABLE\_NAME替代。

TG\_TABLE\_NAME

数据类型是name；是导致触发器调用的表的名称。

TG\_TABLE\_SCHEMA

数据类型是name；是导致触发器调用的表所在的模式名。

TG\_NARGS

数据类型是integer；在CREATE TRIGGER语句中给触发器函数的参数数量。

TG\_ARGV\[\]

数据类型是text数组；来自CREATE TRIGGER语句的参数。索引从 0 开始记数。非法索引（小于 0 或者大于等于tg\_nargs）会导致返回一个空值。

一个触发器函数必须返回NULL或者是一个与触发器为之引发的表结构完全相同的记录/行值。

BEFORE引发的行级触发器可以返回一个空来告诉触发器管理器跳过对该行剩下的操作（即后续的触发器将不再被引发，并且不会对该行发生INSERT/UPDATE/DELETE)。如果返回了一个非空值，那么对该行值会继续操作。返回不同于原始NEW的行值将修改将要被插入或更新的行。因此，如果该触发器函数想要触发动作正常成功而不修改行值，NEW（或者另一个相等的值）必须被返回。要修改将被存储的行，可以直接在NEW中替换单一值并且返回修改后的NEW，或者构建一个全新的记录/行来返回。在一个DELETE上的前触发器情况下，返回值没有直接效果，但是它必须为非空以允许触发器动作继续下去。注意NEW在DELETE触发器中是空值，因此返回它通常没有意义。在DELETE中的常用方法是返回OLD.

INSTEAD OF触发器（总是行级触发器，并且可能只被用于视图）能够返回空来表示它们没有执行任何更新，并且对该行剩余的操作可以被跳过（即后续的触发器不会被引发，并且该行不会被计入外围INSERT/UPDATE/DELETE的行影响状态中）。否则一个非空值应该被返回用以表示该触发器执行了所请求的操作。对于INSERT 和UPDATE操作，返回值应该是NEW，触发器函数可能对它进行了修改来支持INSERT RETURNING和UPDATE RETURNING（这也将影响被传递给任何后续触发器的行值，或者被传递给带有ON CONFLICT DO UPDATE的INSERT语句中一个特殊的EXCLUDED别名引用）。对于DELETE操作，返回值应该是OLD。

一个AFTER行级触发器或一个BEFORE或AFTER语句级触发器的返回值总是会被忽略，它可能也是空。不过，任何这些类型的触发器可能仍会通过抛出一个错误来中止整个操作。

例11.3展示了PL/pgSQL中一个触发器函数的例子。

这个例子触发器保证：任何时候一个行在表中被插入或更新时，当前用户名和时间也会被标记在该行中。并且它会检查给出了一个雇员的姓名以及薪水是一个正值。

CREATE TABLE emp (

empname text,

salary integer,

last\_date timestamp,

last\_user text

);

CREATE FUNCTION emp\_stamp() RETURNS trigger AS $emp\_stamp$

BEGIN

\-- 检查给出了 empname 以及 salary

IF NEW.empname IS NULL THEN

RAISE EXCEPTION 'empname cannot be null';

END IF;

IF NEW.salary IS NULL THEN

RAISE EXCEPTION '% cannot have null salary', NEW.empname;

END IF;

\-- 谁会倒贴钱为我们工作？

IF NEW.salary < 0 THEN

RAISE EXCEPTION '% cannot have a negative salary', NEW.empname;

END IF;

\-- 记住谁在什么时候改变了工资单

NEW.last\_date:= current\_timestamp;

NEW.last\_user:= current\_user;

RETURN NEW;

END;

$emp\_stamp$ LANGUAGE plpgsql;

CREATE TRIGGER emp\_stamp BEFORE INSERT OR UPDATE ON emp

FOR EACH ROW EXECUTE FUNCTION emp\_stamp();

另一种记录对表的改变的方法涉及到创建一个新表来为每一个发生的插入、更新或删除保持一行。这种方法可以被认为是对一个表的改变的审计。例 11.4展示了PL/pgSQL中一个审计触发器函数的例子。

例11.4. 一个用于审计的 PL/pgSQL 触发器函数

这个例子触发器保证了在emp表上的任何插入、更新或删除一行的动作都被记录（即审计）在emp\_audit表中。当前时间和用户名会被记录到行中，还有在其上执行的操作类型。

CREATE TABLE emp (

empname text NOT NULL,

salary integer

);

CREATE TABLE emp\_audit(

operation char(1) NOT NULL,

stamp timestamp NOT NULL,

userid text NOT NULL,

empname text NOT NULL,

salary integer

);

CREATE OR REPLACE FUNCTION process\_emp\_audit() RETURNS TRIGGER AS $emp\_audit$

BEGIN

\--

\-- 在 emp\_audit 中创建一行来反映 emp 上执行的动作，

\-- 使用特殊变量 TG\_OP 来得到操作。

\--

IF (TG\_OP = 'DELETE') THEN

INSERT INTO emp\_audit SELECT 'D', now(), user, OLD.\*;

ELSIF (TG\_OP = 'UPDATE') THEN

INSERT INTO emp\_audit SELECT 'U', now(), user, NEW.\*;

ELSIF (TG\_OP = 'INSERT') THEN

INSERT INTO emp\_audit SELECT 'I', now(), user, NEW.\*;

END IF;

RETURN NULL; -- 因为这是一个 AFTER 触发器，结果被忽略

END;

$emp\_audit$ LANGUAGE plpgsql;

CREATE TRIGGER emp\_audit

AFTER INSERT OR UPDATE OR DELETE ON emp

FOR EACH ROW EXECUTE FUNCTION process\_emp\_audit();

前一个例子的一种变体使用一个视图将主表连接到审计表来展示每一项最后被修改是什么时间。这种方法还是记录了对于表修改的完整审查跟踪，但是也提供了审查跟踪的一个简化视图，只为每一个项显示从审查跟踪生成的最后修改时间戳。例 11.5展示了在PL/pgSQL中一个视图上审计触发器的例子。

例11.5. 一个用于审计的 PL/pgSQL 视图触发器函数 。

这个例子在视图上使用了一个触发器让它变得可更新，并且确保视图中一行的任何插入、更新或删除被记录（即审计）在emp\_audit表中。当前时间和用户名会被与执行的操作类型一起记录，并且该视图会显示每一行的最后修改时间。

CREATE TABLE emp (

empname text PRIMARY KEY,

salary integer

);

CREATE TABLE emp\_audit(

operation char(1) NOT NULL,

userid text NOT NULL,

empname text NOT NULL,

salary integer,

stamp timestamp NOT NULL

);

CREATE VIEW emp\_view AS

SELECT e.empname,

e.salary,

max(ea.stamp) AS last\_updated

FROM emp e

LEFT JOIN emp\_audit ea ON ea.empname = e.empname

GROUP BY 1, 2;

CREATE OR REPLACE FUNCTION update\_emp\_view() RETURNS TRIGGER AS $$

BEGIN

\--

\-- 执行 emp 上所要求的操作，并且在 emp\_audit 中创建一行来反映对 emp 的改变。

\--

IF (TG\_OP = 'DELETE') THEN

DELETE FROM emp WHERE empname = OLD.empname;

IF NOT FOUND THEN RETURN NULL; END IF;

OLD.last\_updated = now();

INSERT INTO emp\_audit VALUES('D', user, OLD.\*);

RETURN OLD;

ELSIF (TG\_OP = 'UPDATE') THEN

UPDATE emp SET salary = NEW.salary WHERE empname = OLD.empname;

IF NOT FOUND THEN RETURN NULL; END IF;

NEW.last\_updated = now();

INSERT INTO emp\_audit VALUES('U', user, NEW.\*);

RETURN NEW;

ELSIF (TG\_OP = 'INSERT') THEN

INSERT INTO emp VALUES(NEW.empname, NEW.salary);

NEW.last\_updated = now();

INSERT INTO emp\_audit VALUES('I', user, NEW.\*);

RETURN NEW;

END IF;

END;

$$ LANGUAGE plpgsql;

CREATE TRIGGER emp\_audit

INSTEAD OF INSERT OR UPDATE OR DELETE ON emp\_view

FOR EACH ROW EXECUTE FUNCTION update\_emp\_view();

触发器的一种用法是维护一个表的另一个汇总表。作为结果的汇总表可以用来在特定查询中替代原始表 — 通常会大量减少运行时间。这种技术常用于数据仓库中，在其中被度量或被观察数据的表（称为事实表）可能会极度大。例11.6展示了PL/pgSQL中一个为数据仓库事实表维护汇总表的触发器函数的例子。

例11.6. 一个 PL/pgSQL 用于维护汇总表的触发器函数。

\--

\-- 主表 - 时间维度和销售事实。

\--

CREATE TABLE time\_dimension (

time\_key integer NOT NULL,

day\_of\_week integer NOT NULL,

day\_of\_month integer NOT NULL,

month integer NOT NULL,

quarter integer NOT NULL,

year integer NOT NULL

);

CREATE UNIQUE INDEX time\_dimension\_key ON time\_dimension(time\_key);

CREATE TABLE sales\_fact (

time\_key integer NOT NULL,

product\_key integer NOT NULL,

store\_key integer NOT NULL,

amount\_sold numeric(12,2) NOT NULL,

units\_sold integer NOT NULL,

amount\_cost numeric(12,2) NOT NULL

);

CREATE INDEX sales\_fact\_time ON sales\_fact(time\_key);

\--

\-- 汇总表 - 按时间汇总销售

\--

CREATE TABLE sales\_summary\_bytime (

time\_key integer NOT NULL,

amount\_sold numeric(15,2) NOT NULL,

units\_sold numeric(12) NOT NULL,

amount\_cost numeric(15,2) NOT NULL

);

CREATE UNIQUE INDEX sales\_summary\_bytime\_key ON sales\_summary\_bytime(time\_key);

\--

\-- 在 UPDATE、INSERT、DELETE 时修改汇总列的函数和触发器。

\--

CREATE OR REPLACE FUNCTION maint\_sales\_summary\_bytime() RETURNS TRIGGER

AS $maint\_sales\_summary\_bytime$

DECLARE

delta\_time\_key integer;

delta\_amount\_sold numeric(15,2);

delta\_units\_sold numeric(12);

delta\_amount\_cost numeric(15,2);

BEGIN

\-- 算出增量/减量数。

IF (TG\_OP = 'DELETE') THEN

delta\_time\_key = OLD.time\_key;

delta\_amount\_sold = -1 \* OLD.amount\_sold;

delta\_units\_sold = -1 \* OLD.units\_sold;

delta\_amount\_cost = -1 \* OLD.amount\_cost;

ELSIF (TG\_OP = 'UPDATE') THEN

\-- 禁止更改 the time\_key 的更新-

\-- （可能不会太麻烦，因为大部分的更改是用 DELETE + INSERT 完成的）。

IF ( OLD.time\_key!= NEW.time\_key) THEN

RAISE EXCEPTION 'Update of time\_key: % -> % not allowed',

OLD.time\_key,

NEW.time\_key;

END IF;

delta\_time\_key = OLD.time\_key;

delta\_amount\_sold = NEW.amount\_sold - OLD.amount\_sold;

delta\_units\_sold = NEW.units\_sold - OLD.units\_sold;

delta\_amount\_cost = NEW.amount\_cost - OLD.amount\_cost;

ELSIF (TG\_OP = 'INSERT') THEN

delta\_time\_key = NEW.time\_key;

delta\_amount\_sold = NEW.amount\_sold;

delta\_units\_sold = NEW.units\_sold;

delta\_amount\_cost = NEW.amount\_cost;

END IF;

\-- 插入或更新带有新值的汇总行。

<<insert\_update>>

LOOP

UPDATE sales\_summary\_bytime

SET amount\_sold = amount\_sold + delta\_amount\_sold,

units\_sold = units\_sold + delta\_units\_sold,

amount\_cost = amount\_cost + delta\_amount\_cost

WHERE time\_key = delta\_time\_key;

EXIT insert\_update WHEN found;

BEGIN

INSERT INTO sales\_summary\_bytime (

time\_key,

amount\_sold,

units\_sold,

amount\_cost)

VALUES (

delta\_time\_key,

delta\_amount\_sold,

delta\_units\_sold,

delta\_amount\_cost

);

EXIT insert\_update;

EXCEPTION

WHEN UNIQUE\_VIOLATION THEN

\-- 什么也不做

END;

END LOOP insert\_update;

RETURN NULL;

END;

$maint\_sales\_summary\_bytime$ LANGUAGE plpgsql;

CREATE TRIGGER maint\_sales\_summary\_bytime

AFTER INSERT OR UPDATE OR DELETE ON sales\_fact

FOR EACH ROW EXECUTE FUNCTION maint\_sales\_summary\_bytime();

INSERT INTO sales\_fact VALUES(1,1,1,10,3,15);

INSERT INTO sales\_fact VALUES(1,2,1,20,5,35);

INSERT INTO sales\_fact VALUES(2,2,1,40,15,135);

INSERT INTO sales\_fact VALUES(2,3,1,10,1,13);

SELECT \* FROM sales\_summary\_bytime;

DELETE FROM sales\_fact WHERE product\_key = 1;

SELECT \* FROM sales\_summary\_bytime;

UPDATE sales\_fact SET units\_sold = units\_sold \* 2;

SELECT \* FROM sales\_summary\_bytime;

AFTER也可以利用传递表来观察被触发语句更改的整个行集合。CREATE TRIGGER命令会为一个或者两个传递表分配名字，然后函数可以引用那些名字，就好像它们是只读的临时表一样。例11.7展示了一个例子。

例11.7. 用传递表进行审计

这个例子产生和例11.4相同的结果，但并未使用一个为每一行都触发的触发器，而是在把相关信息收集到一个传递表中之后用了一个只为每个语句引发一次的触发器。当调用语句修改了很多行时，这种方法明显比行触发器方法快。注意我们必须为每一种事件建立一个单独的触发器声明，因为每种情况的REFERENCING子句必须不同。但是这并不能阻止我们使用单一的触发器函数（实际上，使用三个单独的函数会更好，因为可以避免在TG\_OP上的运行时测试）。

CREATE TABLE emp (

empname text NOT NULL,

salary integer

);

CREATE TABLE emp\_audit(

operation char(1) NOT NULL,

stamp timestamp NOT NULL,

userid text NOT NULL,

empname text NOT NULL,

salary integer

);

CREATE OR REPLACE FUNCTION process\_emp\_audit() RETURNS TRIGGER AS $emp\_audit$

BEGIN

\--

\-- 在emp\_audit中创建行来反映在emp上执行的操作，

\-- 利用特殊变量TG\_OP来区分操作。

\--

IF (TG\_OP = 'DELETE') THEN

INSERT INTO emp\_audit

SELECT 'D', now(), user, o.\* FROM old\_table o;

ELSIF (TG\_OP = 'UPDATE') THEN

INSERT INTO emp\_audit

SELECT 'U', now(), user, n.\* FROM new\_table n;

ELSIF (TG\_OP = 'INSERT') THEN

INSERT INTO emp\_audit

SELECT 'I', now(), user, n.\* FROM new\_table n;

END IF;

RETURN NULL; -- 由于这是一个AFTER触发器，所以结果被忽略

END;

$emp\_audit$ LANGUAGE plpgsql;

CREATE TRIGGER emp\_audit\_ins

AFTER INSERT ON emp

REFERENCING NEW TABLE AS new\_table

FOR EACH STATEMENT EXECUTE FUNCTION process\_emp\_audit();

CREATE TRIGGER emp\_audit\_upd

AFTER UPDATE ON emp

REFERENCING OLD TABLE AS old\_table NEW TABLE AS new\_table

FOR EACH STATEMENT EXECUTE FUNCTION process\_emp\_audit();

CREATE TRIGGER emp\_audit\_del

AFTER DELETE ON emp

REFERENCING OLD TABLE AS old\_table

FOR EACH STATEMENT EXECUTE FUNCTION process\_emp\_audit();

### 事件触发器

PL/pgSQL可以被用来定义事件触发器。瀚高数据库要求一个可以作为事件触发器调用的函数必须被声明为没有参数并且返回类型为event\_trigger。

当一个PL/pgSQL函数被作为一个事件触发器调用，在顶层块中会自动创建一些特殊变量。它们是：

TG\_EVENT

数据类型是text；它是一个表示引发触发器的事件的字符串。

TG\_TAG

数据类型是text；它是一个变量，包含了该触发器为之引发的命令标签。

例11.8展示了PL/pgSQL中一个事件触发器函数的例子。

例 11.8. 一个 PL/pgSQL 事件触发器函数

这个例子触发器在受支持命令每一次被执行时会简单地抛出一个NOTICE消息。

CREATE OR REPLACE FUNCTION snitch() RETURNS event\_trigger AS $$

BEGIN

RAISE NOTICE 'snitch: % %', tg\_event, tg\_tag;

END;

$$ LANGUAGE plpgsql;

CREATE EVENT TRIGGER snitch ON ddl\_command\_start EXECUTE FUNCTION snitch();

## PL/pgSQL的内部

这一节讨论了一些PL/pgSQL用户应该知道的一些重要的实现细节。

### 变量替换

一个PL/pgSQL函数中的 SQL 语句和表达式能够引用该函数的变量和参数。在现象背后，PL/ pgSQL会为这些引用替换查询参数。只有在语法上允许一个参数或列引用的地方才会替换参数。作为一种极端情况，考虑这个编程风格糟糕的例子：

INSERT INTO foo (foo) VALUES (foo);

foo的第一次出现在语法上必须是一个表名， 因此它将不会被替换，即使该函数有一个名为foo的变量。第二次出现必须是该表的一列的名称，因此它也将不会被替换。只有第三次出现是对该函数变量引用的候选。

因为变量名在语法上与表列的名字没什么区别，在也引用表的语句中会有歧义：一个给定的名字意味着一个表列或一个变量？让我们把前一个例子改成：

INSERT INTO dest (col) SELECT foo + bar FROM src;

这里，dest和src必须是表名，并且col必须是dest的一列，但是foo和bar可能该函数的变量或者src的列。

默认情况下，如果一个 SQL 语句中的名称可能引用一个变量或者一个表列，PL/pgSQL将报告一个错误。修复这种问题的方法很多：你可以重命名变量或列来，或者对有歧义的引用加以限定，或者告诉PL/pgSQL要引用哪种解释。

最简单的解决方案是重命名变量或列。一种常用的编码规则是为PL/pgSQL变量使用一种不同于列名的命名习惯。例如，如果你将函数变量统一地命名为v\_something，而你的列名不会开始于v\_，就不会发生冲突。

另外你可以限定有歧义的引用让它们变清晰。在上面的例子中，src.foo将是对表列的一种无歧义的引用。要创建对一个变量的无歧义引用，在一个被标记的块中声明它并且使用块的标签（见 PL/pgSQL的结构 ）。例如

<\<block>>

DECLARE

foo int;

BEGIN

foo:=...;

INSERT INTO dest (col) SELECT block.foo + bar FROM src;

这里block.foo表示变量，即使在src中有一个列foo。函数参数以及诸如FOUND的特殊变量，都能通过函数的名称被限定，因为它们被隐式地声明在一个带有该函数名称的外层块中。

有时候在一个大型的PL/pgSQL代码体中修复所有的有歧义引用是不现实的。在这种情况下，你可以指定PL/pgSQL应该将有歧义的引用作为变量。

要在系统范围内改变这种行为，将配置参数plpgsql.variable\_conflict设置为error、use\_variable或者use\_column（这里error是出厂设置）之一。这个参数会影响PL/pgSQL函数中语句的后续编译，但是不会影响在当前会话中已经编译过的语句。因为改变这个设置能够导致PL/pgSQL函数中行为的意想不到的改变，所以只能由一个超级用户来更改它。

你也可以对逐个函数设置该行为，做法是在函数文本的开始插入这些特殊命令之一：

#variable\_conflict error

#variable\_conflict use\_variable

#variable\_conflict use\_column

这些命令只影响它们所属的函数，并且会覆盖plpgsql.variable\_conflict的设置。一个例子是：

CREATE FUNCTION stamp\_user(id int, comment text) RETURNS void AS $$

#variable\_conflict use\_variable

DECLARE

curtime timestamp:= now();

BEGIN

UPDATE users SET last\_modified = curtime, comment = comment

WHERE users.id = id;

END;

$$ LANGUAGE plpgsql;

在UPDATE命令中，curtime、comment以及id将引用该函数的变量和参数，不管users有没有这些名称的列。注意，我们不得不在WHERE子句中对users.id的引用加以限定，以便让它引用表列。但是我们不需要在UPDATE列表中把对comment的引用限定为一个目标，因为语法上那必须是users的一列。我们可以用下面的方式写一个相同的不依赖于variable\_conflict设置的函数：

CREATE FUNCTION stamp\_user(id int, comment text) RETURNS void AS $$

<\<fn>>

DECLARE

curtime timestamp:= now();

BEGIN

UPDATE users SET last\_modified = fn.curtime, comment =

stamp\_user.comment

WHERE users.id = stamp\_user.id;

END;

$$ LANGUAGE plpgsql;

被交给EXECUTE或其变体的命令字符串中不会发生变量替换。如果你需要插入一个变化值到这样一个命令中，在构建该字符串值时就这样做，或者使用USING，如 执行动态命令 中所阐明的。

当前变量替换只能在SELECT、INSERT、UPDATE和DELETE命令中工作，因为主 SQL 引擎只允许查询参数在这些命令中。要在其他语句类型（通常被称为实用语句）中使用一个非常量名称或值，你必须将实用语句构建为一个字符串并且EXECUTE它。

### 计划缓存

在函数被第一次调用时（在每个会话中），PL/pgSQL解释器解析函数的源文本并且产生一个内部的二进制指令树。该指令树完全翻译了PL/pgSQL语句结构，但是该函数中使用的SQL表达式以及SQL命令并没有被立即翻译。

作为该函数中每一个表达式和第一次被执行的SQL命令，PL/pgSQL解释器使用SPI管理器的SPI\_prepare函数解析并且分析该命令来创建一个预备语句。对于那个表达式或命令的后续访问将会重用该预备语句。因此，一个带有很少被访问的条件性代码路径的函数将永远不会发生分析那些在当前会话中永远不被执行的命令的开销。一个缺点是在一个特定表达式或命令中的错误将不能被检测到，直到函数的该部分在执行时被到达（不重要的语法错误在初始的解析中就会被检测到，但是任何更深层次的东西将只有在执行时才能检测到）。

PL/pgSQL（或者更准确地说是 SPI 管理器）能进一步尝试缓冲与任何特定预备语句相关的执行计划。如果没有使用一个已缓存的计划，那么每次访问该语句时都会生成一个新的执行计划，并且当前的参数值（也就是PL/pgSQL的变量值）可以被用来优化被选中的计划。如果该语句没有参数，或者要被执行很多次，SPI 管理器将考虑创建一个不依赖特定参数值的一般计划并且将其缓存用于重用。通常只有在执行计划对其中引用的PL/pgSQL变量值不那么敏感时，才会这样做。如果这样做，每一次生成的计划就是纯利。关于预备语句的行为请详见PREPARE。

由于PL/pgSQL保存预备语句并且有时候以这种方式保存执行计划，直接出现在一个PL/pgSQL函数中的 SQL 命令必须在每次执行时引用相同的表和列。也就是说，你不能在一个 SQL 命令中把一个参数用作表或列的名字。要绕过这种限制，你可以构建PL/pgSQL EXECUTE使用的动态命令，但是会付出在每次执行时需要执行新解析分析以及构建新执行计划的代价。

记录变量的易变天性在这个关系中带来了另一个问题。当一个记录变量的域被用在表达式或语句中时，域的数据类型不能在该函数的调用之间改变，因为每一个表达式被分析时都将使用第一次到达该表达式时存在的数据类型。必要时，可以用EXECUTE来绕过这个问题。

如果同一个函数被用作一个服务于多个表的触发器，PL/pgSQL会为每一个这样的表独立地准备并缓存语句 — 也就是对每一种触发器函数和表的组合都会有一个缓存，而不是每个函数一个缓存。这减轻了数据类型变化带来的问题。例如，一个触发器函数将能够成功地使用一个名为key的列工作，即使该列正好在不同的表中有不同的类型。

同样，具有多态参数类型的函数也会为它们已经被调用的每一种实参类型组合都保留一个独立的缓存，这样数据类型差异不会导致意想不到的失败。

语句缓存有时可能在解释时间敏感的值时产生令人惊讶的效果。例如这两个函数做的事情就有区别：

CREATE FUNCTION logfunc1(logtxt text) RETURNS void AS $$

BEGIN

INSERT INTO logtable VALUES (logtxt, 'now');

END;

$$ LANGUAGE plpgsql;

以及：

CREATE FUNCTION logfunc2(logtxt text) RETURNS void AS $$

DECLARE

curtime timestamp;

BEGIN

curtime:= 'now';

INSERT INTO logtable VALUES (logtxt, curtime);

END;

$$ LANGUAGE plpgsql;

在logfunc1中，瀚高数据库的主解析器在分析INSERT时就知道字符串'now'应该被解释为timestamp，因为logtable的目标列是这种类型。因此，在INSERT被分析时'now'将被转换为一个timestamp常量，并且在该会话的生命周期内被用于所有对logfunc1的调用。不用说，这不是程序员想要的。一个更好的主意是使用now()或current\_timestamp函数。

在logfunc2中，瀚高数据库的主解析器不知道'now'应该变成什么类型并且因此返回一个text类型的包含字符串now的数据值。在确定对本地变量curtime的赋值期间，PL/pgSQL解释器通过调用用于转换的text\_out以及timestamp\_in函数将这个字符串造型为timestamp类型。因此，计算出来的时间戳会按照程序员的期待在每次执行时更新。虽然这正好符合预期，但是它的效率很糟糕，因此使用now()函数仍然是一种更好的方案。

## PL/pgSQL开发提示

在PL/pgSQL中进行开发的一种好方法是使用你自己选择的文本编辑器来创建函数，并且在另一个窗口中使用psql来载入并且测试那些函数。如果你正在这样做，使用CREATE OR REPLACE FUNCTION来编写函数是一个好主意。用那种方式你只需要重载该文件来更新函数的定义。例如：

CREATE OR REPLACE FUNCTION testfunc(integer) RETURNS integer AS $$

.…

$$ LANGUAGE plpgsql;

在运行psql期间，你可以用下面的命令载入或者重载这样一个函数定义文件：

\\i filename.sql

并且接着立即发出 SQL 命令来测试该函数。

另一种在PL/pgSQL中开发的方式是用一个 GUI 数据库访问工具，它能方便对过程语言的开发。这种工具的一个例子是pgAdmin。这些工具通常提供方便的特性，例如转义单引号以及便于重新创建和调试函数。

### 处理引号

一个PL/pgSQL函数的代码在一个CREATE FUNCTION中被指定为一个字符串。如果你用通常的方式把该字符串写在单引号中间，那么该函数体中的任何单引号都必须被双写；同样任何反斜线也必须被双写（假定使用了转义字符串语法）。双写引号最多有点冗长，并且在更复杂的情况中代码会变得完全无法理解，因为你很容易发现你需要半打或者更多相邻的引号。我们推荐你转而把函数体写成一个”美元引用”的字符串（见第 4.1.2.4 节）。在美元引用方法中，你从不需要双写任何引号。但是要注意为你需要的每一层嵌套选择一个不同的美元引用定界符。例如，你可能把CREATE FUNCTION命令写成：

CREATE OR REPLACE FUNCTION testfunc(integer) RETURNS integer AS $PROC$

.…

$PROC$ LANGUAGE plpgsql;

在这里面，你可以在 SQL 命令中为简单字符串使用引号并且用$$来界定被你组装成字符串的SQL 命令片段。如果你需要引用包括$$的文本，你可以使用$Q$等等。

下列图表展示了在写没有美元引用的引号时需要做什么。在将之前用美元引用的代码翻译成更容易理解的代码时，它们会有所帮助。

1 个引号

用来开始和结束函数体，例如：

CREATE FUNCTION foo() RETURNS integer AS '

.…

' LANGUAGE plpgsql;

在一个单引号引用的函数体中的任何位置，引号必须成对出现。

2 个引号

用于函数体内的字符串，例如：

a\_output:= ''Blah'';

SELECT \* FROM users WHERE f\_name=''foobar'';

在美元引用方法中，你只需要写：

a\_output:= 'Blah';

SELECT \* FROM users WHERE f\_name='foobar';

这恰好就是PL/pgSQL在两种情况中会看到的。

4 个引号

当你在函数内的一个字符串常量中需要一个单引号时，例如：

a\_output:= a\_output || '' AND name LIKE ''''foobar'''' AND xyz''

实际会被追加到a\_output的值将是： AND name LIKE 'foobar' AND xyz。

在美元引用方法中，你可以写：

a\_output:= a\_output || $$ AND name LIKE 'foobar' AND xyz$$

要小心在这周围的任何美元引用定界符不只是$$。

6 个引号

当在函数体内的一个字符串中的一个单引号与该字符串常量末尾相邻，例如：

a\_output:= a\_output || '' AND name LIKE ''''foobar''''''

被追加到a\_output的值则将是： AND name LIKE 'foobar'。

在美元引用方法中，这会变成：

a\_output:= a\_output || $$ AND name LIKE 'foobar'$$

10 个引号

当你想在一个字符串常量（占 8 个引号）中有两个单引号时并且这会挨着该字符串常量的末尾（另外 2 个）。如果你正在写一个产生其他函数的函数（如例 42.10中），你将很可能只需要这种。例如：

a\_output:= a\_output || '' if v\_'' ||

referrer\_keys.kind || '' like ''''''''''

|| referrer\_keys.key\_string || ''''''''''

then return '''''' || referrer\_keys.referrer\_type

|| ''''''; end if;'';

a\_output的值将是：

if v\_... like ''...'' then return ''...''; end if;

在美元引用方法中，这会变成：

a\_output:= a\_output || $$ if v\_$$ || referrer\_keys.kind || $$ like '$$

|| referrer\_keys.key\_string || $$'

then return '$$ || referrer\_keys.referrer\_type

|| $$'; end if;$$;

这里我们假定我们只需要把单引号放在a\_output中，因为在使用前它将被再引用。

### 额外的编译时和运行时检查

为了辅助用户在一些简单但常见的问题产生危害之前找到它们， PL/pgSQL提供了额外的检查。当被启用时， 根据配置，它们可以在一个函数的编译期间被用来发出 WARNING或者ERROR。一个已经收到了 WARNING的函数可以被继续执行而不会产生进一步的消息， 因此建议你在一个单独的开发环境中进行测试。

根据需要设置 plpgsql.extra\_warnings 或 plpgsql.extra\_errors，适当情况下，在开发和/或测试环境中可以设置为 "all"。

这些附加检查通过配置变量启用， plpgsql.extra\_warnings用于警告，plpgsql.extra\_errors 用于错误。 两者都可以设置为逗号分隔的检查列表，"none" 或 "all"。 默认值为"none"。当前可用的检查列表包括：

shadowed\_variables

检查声明是否遮盖了以前定义的变量

strict\_multi\_assignment

某些PL/PgSQL命令允许一次将值分配给多个变量，例如SELECT INTO。 通常，目标变量的数量和源变量的数量应匹配，尽管PL/PgSQL将使用NULL来处理缺失的值和被忽略的额外变量。 启用此检查将导致 PL/PgSQL在目标变量数和源变量数不同时引发WARNING或ERROR。

too\_many\_rows

Enabling this check will cause PL/PgSQL to check if a given query returns

more than one row when an INTO clause is used. As an INTO statement will only

ever use one row, having a query return multiple rows is generally either

inefficient and/or nondeterministic and therefore is likely an error. 启用此

检查将导致PL/PgSQL检查在使用INTO子句时给定查询是否返回多行。 由于INTO语句只会使用一行，让查询返回多行通常会效率低下和/或不确定性，因此很可能会出现错误。

下面的示例显示了plpgsql.extra\_warnings 设置为shadowed\_variables的效果：

SET plpgsql.extra\_warnings TO 'shadowed\_variables';

CREATE FUNCTION foo(f1 int) RETURNS int AS $$

DECLARE

f1 int;

BEGIN

RETURN f1;

END

$$ LANGUAGE plpgsql;

WARNING: variable "f1" shadows a previously defined variable

LINE 3: f1 int;

^

CREATE FUNCTION

下面的示例显示了将plpgsql.extra\_warnings 设置为strict\_multi\_assignment：

SET plpgsql.extra\_warnings TO 'strict\_multi\_assignment';

CREATE OR REPLACE FUNCTION public.foo()

RETURNS void

LANGUAGE plpgsql

AS $$

DECLARE

x int;

y int;

BEGIN

SELECT 1 INTO x, y;

SELECT 1, 2 INTO x, y;

SELECT 1, 2, 3 INTO x, y;

END;

$$;

SELECT foo();

WARNING: number of source and target fields in assignment does not match

DETAIL: strict\_multi\_assignment check of extra\_warnings is active.

HINT: Make sure the query returns the exact list of columns.

WARNING: number of source and target fields in assignment does not match

DETAIL: strict\_multi\_assignment check of extra\_warnings is active.

HINT: Make sure the query returns the exact list of columns.

foo

\-----

(1 row)

## 从Oracle PL/SQL 移植

这一节解释了瀚高数据库的PL/pgSQL语言和 Oracle 的PL/SQL语言之间的差别，用以帮助那些从Oracle®向瀚高数据库移植应用的人。

PL/pgSQL与 PL/SQL 在许多方面都非常类似。它是一种块结构的、命令式的语言并且所有变量必须先被声明。赋值、循环和条件则很类似。在从PL/SQL向PL/pgSQL移植时必须记住一些事情：

• 如果一个 SQL 命令中使用的名字可能是一个表的列名或者是对一个函数中变量的引用，那么PL/SQL会将它当作一个列名。如 变量替换 中所述，这对应的是PL/pgSQL的 plpgsql.variable\_conflict = use\_column行为（不是默认行为）。通常最好是首先避免这种歧义，但如果不得不移植依赖于该行为的大量代码，那么设置variable\_conflict将是最好的方案。

• 在瀚高数据库中，函数体必须写成字符串文本。因此你需要使用美元符引用或者转义函数体中的单引号（见 处理引号 ）。

• 数据类型名称常常需要翻译。例如，在 Oracle 中字符串值通常被声明为类型varchar2，这并非 SQL 标准类型。在瀚高数据库中则要使用类型varchar或者text来替代。类似地，要把类型number替换成numeric，或者在适当的时候使用某种其他数字数据类型。

• 因为没有包，所以也没有包级别的变量。这一点有时候挺讨厌。你可以在临时表里保存会话级别的状态。

• 带有REVERSE的整数FOR循环的工作方式不同：PL/SQL中是从第二个数向第一个数倒数，而 PL/pgSQL是从第一个数向第二个数倒数，因此在移植时需要交换循环边界。不幸的是这种不兼容性是不太可能改变的（见 FOR（整型变体） ）。

• 查询上的FOR循环（不是游标）的工作方式同样不同：目标变量必须已经被声明，而PL/SQL总是会隐式地声明它们。但是这样做的优点是在退出循环后，变量值仍然可以访问。

• 在使用游标变量方面，存在一些记法差异。

### 移植示例

例11.9展示了如何从PL/SQL移植一个简单的函数到PL/pgSQL中。

例11.9. 从PL/SQL移植一个简单的函数到PL/pgSQL

这里有一个Oracle PL/SQL函数：

CREATE OR REPLACE FUNCTION cs\_fmt\_browser\_version(v\_name varchar2,

v\_version varchar2)

RETURN varchar2 IS

BEGIN

IF v\_version IS NULL THEN

RETURN v\_name;

END IF;

RETURN v\_name || '/' || v\_version;

END;

/

show errors;

让我们过一遍这个函数并且看看与PL/pgSQL相比有什么样的不同：

• 类型名称varchar2被改成了varchar或者text。在这一节的例子中，我们将使用varchar，但如果不需要特定的字符串长度限制，text常常是更好的选择。

• 在函数原型中（不是函数体中）的RETURN关键字在瀚高数据库中变成了RETURNS。还有，IS变成了AS，并且你还需要增加一个LANGUAGE子句，因为PL/pgSQL并非唯一可用的函数语言。

• 在瀚高数据库中，函数体被认为是一个字符串，所以你需要使用引号或者美元符号包围它。这代替了Oracle 方法中的用于终止的/。

• 在瀚高数据库中没有show errors命令, 并且也不需要这个命令，因为错误是自动报告的。

这个函数被移植到瀚高数据库后看起来会是这样：

CREATE OR REPLACE FUNCTION cs\_fmt\_browser\_version(v\_name varchar,

v\_version varchar)

RETURNS varchar AS $$

BEGIN

IF v\_version IS NULL THEN

RETURN v\_name;

END IF;

RETURN v\_name || '/' || v\_version;

END;

$$ LANGUAGE plpgsql;

例11.10展示了如何移植一个会创建另一个函数的函数，以及如何处理引号问题。例11.10. 从PL/SQL移植一个创建另一个函数的函数到PL/pgSQL

下面的过程从一个SELECT语句抓取行，并且为了效率而构建一个带有IF语句中结果的大型函数。

这是 Oracle 版本：

CREATE OR REPLACE PROCEDURE cs\_update\_referrer\_type\_proc IS

CURSOR referrer\_keys IS

SELECT \* FROM cs\_referrer\_keys

ORDER BY try\_order;

func\_cmd VARCHAR(4000);

BEGIN

func\_cmd:= 'CREATE OR REPLACE FUNCTION cs\_find\_referrer\_type(v\_host IN

VARCHAR2,

v\_domain IN VARCHAR2, v\_url IN VARCHAR2) RETURN VARCHAR2 IS

BEGIN';

FOR referrer\_key IN referrer\_keys LOOP

func\_cmd:= func\_cmd ||

' IF v\_' || referrer\_key.kind

|| ' LIKE ''' || referrer\_key.key\_string

|| ''' THEN RETURN ''' || referrer\_key.referrer\_type

|| '''; END IF;';

END LOOP;

func\_cmd:= func\_cmd || ' RETURN NULL; END;';

EXECUTE IMMEDIATE func\_cmd;

END;

/

show errors;

这里是瀚高数据库的版本：

CREATE OR REPLACE PROCEDURE cs\_update\_referrer\_type\_proc() RETURNS void AS $func

$

DECLARE

referrer\_keys CURSOR IS

SELECT \* FROM cs\_referrer\_keys

ORDER BY try\_order;

func\_body text;

func\_cmd text;

BEGIN

func\_body:= 'BEGIN';

FOR referrer\_key IN referrer\_keys LOOP

func\_body:= func\_body ||

' IF v\_' || referrer\_key.kind

|| ' LIKE ' || quote\_literal(referrer\_key.key\_string)

|| ' THEN RETURN ' || quote\_literal(referrer\_key.referrer\_type)

|| '; END IF;';

END LOOP;

func\_body:= func\_body || ' RETURN NULL; END;';

func\_cmd:=

'CREATE OR REPLACE FUNCTION cs\_find\_referrer\_type(v\_host varchar,

v\_domain varchar,

v\_url varchar)

RETURNS varchar AS '

|| quote\_literal(func\_body)

|| ' LANGUAGE plpgsql;';

EXECUTE func\_cmd;

END;

$func$ LANGUAGE plpgsql;

请注意函数体是如何被单独构建并且通过quote\_literal被传递以双写其中的任何引号。需要这个技术是因为无法安全地使用美元引用定义新函数：我们不确定从referrer\_key.key\_string域中来的什么字符串会被插入（我们这里假定referrer\_key.kind可以确信总是为host、domain或者url，但是referrer\_key.key\_string可能是任何东西，特别是它可能包含美元符号）。这个函数实际上是在 Oracle 的原版上的改进，因为当referrer\_key.key\_string或者referrer\_key.referrer\_type包含引号时，它将不会生成坏掉的代码。

例11.11展示了如何移植一个带有OUT参数和字符串处理的函数。瀚高数据库没有内建的instr函数，但是你可以用其它函数的组合来创建一个。在 附录 中有一个instr的 PL/pgSQL实现，你可以用它让你的移植变得更容易。

例11.11. 从PL/SQL移植一个带有字符串操作以及OUT参数的过程到PL/pgSQL下面的Oracle PL/SQL 过程被用来解析一个 URL 并且返回一些元素（主机、路径和查询）。

这是 Oracle 版本：

CREATE OR REPLACE PROCEDURE cs\_parse\_url(

v\_url IN VARCHAR2,

v\_host OUT VARCHAR2, -- 这将被传回去

v\_path OUT VARCHAR2, -- 这个也是

v\_query OUT VARCHAR2) -- 还有这个

IS

a\_pos1 INTEGER;

a\_pos2 INTEGER;

BEGIN

v\_host:= NULL;

v\_path:= NULL;

v\_query:= NULL;

a\_pos1:= instr(v\_url, '//');

IF a\_pos1 = 0 THEN

RETURN;

END IF;

a\_pos2:= instr(v\_url, '/', a\_pos1 + 2);

IF a\_pos2 = 0 THEN

v\_host:= substr(v\_url, a\_pos1 + 2);

v\_path:= '/';

RETURN;

END IF;

v\_host:= substr(v\_url, a\_pos1 + 2, a\_pos2 - a\_pos1 - 2);

a\_pos1:= instr(v\_url, '?', a\_pos2 + 1);

IF a\_pos1 = 0 THEN

v\_path:= substr(v\_url, a\_pos2);

RETURN;

END IF;

v\_path:= substr(v\_url, a\_pos2, a\_pos1 - a\_pos2);

v\_query:= substr(v\_url, a\_pos1 + 1);

END;

/

show errors;

这里是一种到PL/pgSQL的可能翻译：

CREATE OR REPLACE FUNCTION cs\_parse\_url(

v\_url IN VARCHAR,

v\_host OUT VARCHAR, -- 这将被传递回去

v\_path OUT VARCHAR, -- 这个也是

v\_query OUT VARCHAR) -- 以及这个

AS $$

DECLARE

a\_pos1 INTEGER;

a\_pos2 INTEGER;

BEGIN

v\_host:= NULL;

v\_path:= NULL;

v\_query:= NULL;

a\_pos1:= instr(v\_url, '//');

IF a\_pos1 = 0 THEN

RETURN;

END IF;

a\_pos2:= instr(v\_url, '/', a\_pos1 + 2);

IF a\_pos2 = 0 THEN

v\_host:= substr(v\_url, a\_pos1 + 2);

v\_path:= '/';

RETURN;

END IF;

v\_host:= substr(v\_url, a\_pos1 + 2, a\_pos2 - a\_pos1 - 2);

a\_pos1:= instr(v\_url, '?', a\_pos2 + 1);

IF a\_pos1 = 0 THEN

v\_path:= substr(v\_url, a\_pos2);

RETURN;

END IF;

v\_path:= substr(v\_url, a\_pos2, a\_pos1 - a\_pos2);

v\_query:= substr(v\_url, a\_pos1 + 1);

END;

$$ LANGUAGE plpgsql;

这个函数可以这样使用：

SELECT \* FROM cs\_parse\_url(' [http://foobar.com/query.cgi?baz\\](http://foobar.com/query.cgi?baz%5C) ‘);

例11.12展示了如何移植一个使用了多种 Oracle 特性的过程。

例 11.12. 从PL/SQL移植一个过程到PL/pgSQL

Oracle 版本：

CREATE OR REPLACE PROCEDURE cs\_create\_job(v\_job\_id IN INTEGER) IS

a\_running\_job\_count INTEGER;

BEGIN

LOCK TABLE cs\_jobs IN EXCLUSIVE MODE;

SELECT count(\*) INTO a\_running\_job\_count FROM cs\_jobs WHERE end\_stamp IS

NULL;

IF a\_running\_job\_count > 0 THEN

COMMIT; -- 释放锁

raise\_application\_error(-20000,

'Unable to create a new job: a job is currently running.');

END IF;

DELETE FROM cs\_active\_job;

INSERT INTO cs\_active\_job(job\_id) VALUES (v\_job\_id);

BEGIN

INSERT INTO cs\_jobs (job\_id, start\_stamp) VALUES (v\_job\_id, now());

EXCEPTION

WHEN dup\_val\_on\_index THEN NULL; -- 如果已经存在也不用担心

END;

COMMIT;

END;

/

show errors

这是我们如何将这个过程移植到PL/pgSQL：

CREATE OR REPLACE PROCEDURE cs\_create\_job(v\_job\_id integer) RETURNS void AS $$

DECLARE

a\_running\_job\_count integer;

BEGIN

LOCK TABLE cs\_jobs IN EXCLUSIVE MODE;

SELECT count(\*) INTO a\_running\_job\_count FROM cs\_jobs WHERE end\_stamp IS

NULL;

IF a\_running\_job\_count > 0 THEN

COMMIT; -- 释放锁

RAISE EXCEPTION 'Unable to create a new job: a job is currently

running'; -- 1

END IF;

DELETE FROM cs\_active\_job;

INSERT INTO cs\_active\_job(job\_id) VALUES (v\_job\_id);

BEGIN

INSERT INTO cs\_jobs (job\_id, start\_stamp) VALUES (v\_job\_id, now());

EXCEPTION

WHEN unique\_violation THEN -- 2

\-- 如果已经存在不要担心

END;

COMMIT;

END;

$$ LANGUAGE plpgsql;

RAISE的语法与 Oracle 的语句相当不同，尽管基本的形式RAISE exception\_name工作起来是相似的。

PL/pgSQL所支持的异常名称不同于 Oracle。内建的异常名称集合要更大。目前没有办法声明用户定义的异常名称，尽管你能够抛出用户选择的 SQLSTATE 值。

### 其他要关注的事项

这一节解释了在移植 Oracle PL/SQL函数到瀚高数据库中时要关注的一些其他问题。

#### 异常后隐式回滚

在PL/pgSQL，当一个异常被EXCEPTION子句捕获之后，从该块的BEGIN以来的所有数据库改变都会被自动回滚。也就是，该行为等效于你在 Oracle 中用下面的代码得到的效果：

BEGIN

SAVEPOINT s1;

... 代码...

EXCEPTION

WHEN... THEN

ROLLBACK TO s1;

... 代码...

WHEN... THEN

ROLLBACK TO s1;

... 代码...

END;

如果你正在翻译一个使用这种风格的SAVEPOINT以及ROLLBACK TO的 Oracle 过程，你的工作比较简单：只要忽略掉SAVEPOINT以及ROLLBACK TO。如果你的 Oracle 过程是以不同的方法使用SAVEPOINT以及ROLLBACK TO，那么就要真正地动一番脑筋了。

#### EXECUTE

PL/pgSQL的EXECUTE与PL/SQL中的工作相似，但是必须要记住按照第 11.5.4 节中所述地使用quote\_literal以及quote\_ident。EXECUTE 'SELECT \* FROM $1';类型的结构将无法可靠地工作除非你使用这些函数。

#### 优化 PL/pgSQL 函数

瀚高数据库提供了两种函数创建修饰符来优化执行：”volatility”（对于给定的相同参数，函数是否总是返回相同的结果）以及”strictness” （如果任何参数为空，函数是否返回空）。详见CREATE FUNCTION参考页。

在利用这些优化属性时，你的CREATE FUNCTION语句应该看起来像这样：

CREATE FUNCTION foo(...) RETURNS integer AS $$

...

$$ LANGUAGE plpgsql STRICT IMMUTABLE;

### 附录

这一节包含了一组 Oracle 兼容的instr函数代码，你可以用它来简化你的移植工作。

\--

\-- instr 函数模仿 Oracle 的对应函数

\-- 语法: instr(string1, string2 \[, n \[, m\]\])

\-- 其中 \[\] 表示可选参数。

\--

\-- 从第n个字符开始搜索string1，要求找到string2的第m次出现。

\-- 如果n为负，则从后向前搜索，从string1的末尾开始的第abs(n)个字符开始。

\-- 如果没有传n，假定它为1（从第1个字符开始搜索）。

\-- 如果没有传m，假定它为1（找第1次出现）。

\-- 在string1中返回string2的开始索引，如果没有找到string2则为0。

\--

CREATE FUNCTION instr(varchar, varchar) RETURNS integer AS $$

BEGIN

RETURN instr($1, $2, 1);

END;

$$ LANGUAGE plpgsql STRICT IMMUTABLE;

CREATE FUNCTION instr(string varchar, string\_to\_search\_for varchar,

beg\_index integer)

RETURNS integer AS $$

DECLARE

pos integer NOT NULL DEFAULT 0;

temp\_str varchar;

beg integer;

length integer;

ss\_length integer;

BEGIN

IF beg\_index > 0 THEN

temp\_str:= substring(string FROM beg\_index);

pos:= position(string\_to\_search\_for IN temp\_str);

IF pos = 0 THEN

RETURN 0;

ELSE

RETURN pos + beg\_index - 1;

END IF;

ELSIF beg\_index < 0 THEN

ss\_length:= char\_length(string\_to\_search\_for);

length:= char\_length(string);

beg:= length + 1 + beg\_index;

WHILE beg > 0 LOOP

temp\_str:= substring(string FROM beg FOR ss\_length);

IF string\_to\_search\_for = temp\_str THEN

RETURN beg;

END IF;

beg:= beg - 1;

END LOOP;

RETURN 0;

ELSE

RETURN 0;

END IF;

END;

$$ LANGUAGE plpgsql STRICT IMMUTABLE;

CREATE FUNCTION instr(string varchar, string\_to\_search\_for varchar,

beg\_index integer, occur\_index integer)

RETURNS integer AS $$

DECLARE

pos integer NOT NULL DEFAULT 0;

occur\_number integer NOT NULL DEFAULT 0;

temp\_str varchar;

beg integer;

i integer;

length integer;

ss\_length integer;

BEGIN

IF occur\_index <= 0 THEN

RAISE 'argument ''%'' is out of range', occur\_index

USING ERRCODE = '22003';

END IF;

IF beg\_index > 0 THEN

beg:= beg\_index - 1;

FOR i IN 1..occur\_index LOOP

temp\_str:= substring(string FROM beg + 1);

pos:= position(string\_to\_search\_for IN temp\_str);

IF pos = 0 THEN

RETURN 0;

END IF;

beg:= beg + pos;

END LOOP;

RETURN beg;

ELSIF beg\_index < 0 THEN

ss\_length:= char\_length(string\_to\_search\_for);

length:= char\_length(string);

beg:= length + 1 + beg\_index;

WHILE beg > 0 LOOP

temp\_str:= substring(string FROM beg FOR ss\_length);

IF string\_to\_search\_for = temp\_str THEN

occur\_number:= occur\_number + 1;

IF occur\_number = occur\_index THEN

RETURN beg;

END IF;

END IF;

beg:= beg - 1;

END LOOP;

RETURN 0;

ELSE

RETURN 0;

END IF;

END;

$$ LANGUAGE plpgsql STRICT IMMUTABLE;