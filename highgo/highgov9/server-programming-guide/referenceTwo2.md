---
title: "扩展SQL"
book: "服务器编程指南"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/reference/referenceTwo2.html"
tags:
  - highgo
  - highgo-v9
  - server-programming-guide
---

## 扩展 SQL

## 扩展性如何工作

瀚高数据库是可扩展的，因为它的操作是目录驱动的。如果你熟悉标准的关系型数据库系统，你会知道它们把有关数据库、表、列等的信息存储在众所周知的系统目录中（某些系统称之为数据目录）。目录对于用户来说好像其他的表一样，但是DBMS把自己的内部信息记录在其中。瀚高数据库和标准关系型数据库系统的一个关键不同是瀚高数据库在其目录中存储更多信息：不只是有关表和列的信息，还有关于数据类型、函数、访问方法等等的信息。这些表可以被用户修改，并且因为瀚高数据库的操作是基于这些表的，所以瀚高数据库可以被用户扩展。通过比较，传统数据库系统只能通过在源代码中改变硬编码的过程或者载入由 DBMS提供者特殊编写的模块进行扩展。

此外，瀚高数据库服务器能够通过动态载入把用户编写的代码结合到它自身中。也就是，用户能够指定一个实现了一个新类型或函数的对象代码文件（例如一个共享库），并且数据库将按照要求载入它。把用SQL编写的代码加入到服务器会更繁琐。这种”即时”修改其操作的能力让数据库独特地适合新应用和存储结构的快速原型设计。

## 数据库类型系统

数据类型被划分为基础类型、容器类型、域和伪类型。

### 基础类型

基础类型是那些被实现在SQL语言层面之下的类型（通常用一种底层语言，如 C），例如integer。它们通常对应于常说的抽象数据类型。瀚高数据库只能通过由用户提供的函数在这类类型上操作，并且只能理解到用户描述这种类型行为的程度。枚举（enum）类型可以被认为是基础类型的一个子类。主要区别是它们可以使用SQL命令创建，不需要用到底层的编程。

### 容器类型

瀚高数据库有三种”容器”类型，它们是包含多个其他类型值的类型。它们是数组、组合以及范围。

数组可以保存全部是同种类型的多个值。为每一种基本类型、组合类型、范围类型以及域类型都会自动创建一个数组类型。但是没有数组的数组。就类型系统的认知而言，多维数组就和一维数组一样。

只要用户创建一个表，就会创建组合类型或者行类型。也可以使用CREATE TYPE来定义一个没有关联表的”stand-alone”组合类型。一个组合类型只是一个具有相关域名称的类型列表。一个组合类型的值是一个行或者域值记录。用户可以访问来自SQL查询的组成域。

范围类型可以保存同种类型的两个值，它们是该范围的上下界。范围类型是用户创建的，不过也存在一些内建的范围类型。

### 域

一个域是基于一种特定底层类型的，并且出于很多目的它可以与其底层类型互换。不过，一个域能够具有约束来限制它的合法值于其底层基础类型允许值的一个子集。可以使用SQL命令CREATE DOMAIN创建域。

### 伪类型

有一些用于特殊目的”伪类型”。伪类型不能作为表列或者容器类型的组件出现，但是它们能被用于声明函数的参数和结果类型。这在类型系统中提供了一种机制来标识函数的特殊分类。

### 多态类型

特别让人感兴趣的五种伪类型是anyelement、anyarray、anynonarray、anyenum以及anyrange，它们被统称为多态类型。任何使用这些类型声明的函数被称作是一个多态函数。通过使用根据一次特定调用实际传递的数据类型所决定的相关数据类型，一个多态函数能够在多种不同数据类型上操作。

多态参数和结果是相互关联的，并且它们在解析调用多态函数的查询时被决定到一种特定的数据类型。每一个被声明为anyelement的位置（参数或返回值）被允许具有任意特定的实际数据类型，但是在任何给定的查询中它们必须全部是相同的实际类型。每一个被声明为anyarray的位置可以有任意数组数据类型，但是相似地，它们必须全部具有相同类型。并且类似地，被声明为anyrange的位置必须是全部是相同的范围类型。此外，如果有位置被声明为anyarray并且其他位置被声明为anyelement，anyarray位置中的实际数组类型必须是一个数组，该数组的元素都是出现在anyelement位置的同一种类型。相似地，如果有位置被声明为anyrange并且其他位置被声明为anyelement，anyrange位置的实际范围类型必须是一个范围，该范围的子类型是出现在anyelement位置的同一种类型。anynonarray被当做和anyelement相同，但是增加了额外的约束要求实际类型不能是一种数组类型。anyenum被当做和anyelement相同，但是增加了额外的约束要求实际类型不能是一种枚举类型。

因此，当使用一种多态类型声明了多于一个参数位置，有效效果是只有实际参数类型的某些组合才被允许。例如，一个被声明为equal(anyelement, anyelement)的函数将要求任意两个输入值，只要它们是同一种数据类型。

当一个函数的返回值被声明为多态类型时，必须至少有一个参数位置也是多态的，并且作为该参数提供的实际数据类型决定了该调用的实际结果类型。例如，如果还没有一种数组下标机制，我们可以定义一个函数来实现下标：subscript(anyarray, integer) returns anyelement。这个声明约束了实际的第一个参数是一种数组类型，并且允许解析器从实际的第一个参数类型推断正确的结果类型。另一个例子是一个被声明为f(anyarray) returns anyenum的函数将只接受枚举类型的数组。

注意anynonarray和anyenum并不表示独立的类型变量，它们是和anyelement相同的类型，只是有一个额外的约束。例如，将一个函数声明为f(anyelement, anyenum)等效于把它声明为f(anyenum, anyenum)：两种实际参数必须是相同的枚举类型。

一个可变函数能够是多态的：这可以通过声明其最后一个参数为VARIADIC anyarray来实现。为了匹配和决定实际结果类型的参数，这样一种函数的行为和写了合适数量的anynonarray参数是一样的。

## 用户定义的函数

瀚高数据库提供四种函数：

• 查询语言函数（用SQL编写的函数）

• 过程语言函数（例如，用PL/pgSQL或PL/Tcl编写的函数）

• 内部函数

• C 语言函数

每一类函数可以采用基本类型、组合类型或者它们的组合作为参数。此外，每一类函数可以返回一个基本类型或一个组合类型。函数也能被定义成返回基本类型或组合类型值的集合。

很多类函数可以接受或者返回特定的伪类型（例如，多态类型），但是可用的功能会变化。

详情可以参考每一种函数的描述。

定义SQL函数最容易，因此我们将从讨论SQL函数开始。大部分SQL函数的概念也能用到其他类型的函数上。

在这一章中，查看CREATE FUNCTION命令的参考页有助于更好地理解例子。

## 用户定义的过程

过程是一种类似于函数的数据库对象。两者的区别在于过程不返回值，因此没有返回类型声明。而函数可以作为一个查询或者DML命令的一部分被调用，过程则需要明确地用CALL语句调用。

本章剩余部分中对如何定义用户定义的函数的解释同样适用于过程，不同的地方有：需要使用CREATE PROCEDURE命令定义、没有返回类型、一些如严格性这样的其他特性不适用。

函数和过程一起构成了例程。有ALTER ROUTINE以及DROP ROUTINE这样的命令可以操作函数和过程而不需要知道它们是哪一种。不过，要注意没有CREATE ROUTINE命令。

## 查询语言（SQL）函数

SQL 函数执行一个由任意 SQL 语句构成的列表，返回列表中最后一个查询的结果。在简单（非集合）的情况中，最后一个查询的结果的第一行将被返回（记住一个多行结果的”第一行”不是良定义的，除非你使用ORDER BY）。如果最后一个查询正好根本不返回行，将会返回空值。

或者，一个 SQL 函数可以通过指定函数的返回类型为SETOF sometype被声明为返回一个集合（也就是多个行），或者等效地声明它为RETURNS TABLE(columns)。在这种情况下，最后一个查询的结果的所有行会被返回。下文将给出进一步的细节。

一个 SQL 函数的主体必须是一个由分号分隔的 SQL 语句的列表。最后一个语句之后的分号是可选的。除非函数被声明为返回void，最后一个语句必须是一个SELECT或者一个带有RETURNING子句的INSERT、UPDATE或者DELETE。

SQL语言中的任何命令集合都能被打包在一起并且被定义成一个函数。除了SELECT查询，命令可以包括数据修改查询（INSERT、UPDATE以及DELETE）和其他 SQL 命令（你不能在SQL函数中使用事务控制命令，例如COMMIT、SAVEPOINT，以及一些工具命令，例如VACUUM）。不过，最后一个命令必须是一个SELECT或者带有一个RETURNING子句，该命令必须返回符合函数返回类型的数据。或者，如果你想要定义一个执行动作但是不返回有用的值的函数，你可以把它定义为返回void。例如，这个函数从emp表中移除具有负值薪水的行：

CREATE FUNCTION clean\_emp() RETURNS void AS '

DELETE FROM emp

WHERE salary < 0;

' LANGUAGE SQL;

SELECT clean\_emp();

clean\_emp

\-----------

(1 row)

| 注意： |
| --- |
| 在被执行前，SQL 函数的整个主体都要被解析。虽然 SQL 函数可以包含修改系统目录的命令（如CREATE TABLE），但这类命令的效果对于该函数中后续命令的解析分析不可见。例如，如果把CREATE TABLE foo (...); INSERT INTO foo VALUES(...);打包到一个 SQL 函数中是得不到预期效果的，因为在解析INSERT命令时foo还不存在。在这类情况下，推荐使用PL/pgSQL而不是 SQL函数。 |

CREATE FUNCTION命令的语法要求函数体被写作一个字符串常量。使用用于字符串常量的美元引用通常最方便。你过你选择使用常规的单引号引用的字符串常量语法，你必须在函数体中双写单引号（'）和反斜线（\\）（假定转义字符串语法）。

### SQL函数的参数

一个 SQL 函数的参数可以在函数体中用名称或编号引用。下面会有两种方法的例子。

要使用一个名称，将函数参数声明为带有一个名称，然后在函数体中只写该名称。如果参数名称与函数内当前 SQL 命令中的任意列名相同，列名将优先。如果不想这样，可以用函数本身的名称来限定参数名，也就是function\_name.argument\_name（如果这会与一个被限定的列名冲突，照例还是列名赢得优先。你可以通过为 SQL 命令中的表选择一个不同的别名来避免这种混淆）。

在更旧的数字方法中，参数可以用语法$n引用：$1指的是第一个输入参数，$2指的是第二个，以此类推。不管特定的参数是否使用名称声明，这种方法都有效。

如果一个参数是一种组合类型，那么点号记法（如 argname.fieldname 或$1.fieldname）也可以被用来访问该参数的属性。同样，你可能需要用函数的名称来限定参数的名称以避免歧义。

SQL 函数参数只能被用做数据值而不能作为标识符。例如这是合理的：

INSERT INTO mytable VALUES ($1);

但这样就不行：

INSERT INTO $1 VALUES (42);

### 基本类型上的SQL

最简单的SQL函数没有参数并且简单地返回一个基本类型，例如integer：

CREATE FUNCTION one() RETURNS integer AS $$

SELECT 1 AS result;

$$ LANGUAGE SQL;

\-- Alternative syntax for string literal:

CREATE FUNCTION one() RETURNS integer AS '

SELECT 1 AS result;

' LANGUAGE SQL;

SELECT one();

one

\-----

1

注意我们为该函数的结果在函数体内定义了一个列别名（名为result），但是这个列别名在函数以外是不可见的。因此，结果被标记为one而不是result。

定义用基本类型作为参数的SQL函数也很容易：

CREATE FUNCTION add\_em(x integer, y integer) RETURNS integer AS $$

SELECT x + y;

$$ LANGUAGE SQL;

SELECT add\_em(1, 2) AS answer;

answer

\--------

3

我们也能省掉参数的名称而使用数字：

CREATE FUNCTION add\_em(integer, integer) RETURNS integer AS $$

SELECT $1 + $2;

$$ LANGUAGE SQL;

SELECT add\_em(1, 2) AS answer;

answer

\--------

3

这里是一个更有用的函数，它可以被用来借记一个银行账号：

CREATE FUNCTION tf1 (accountno integer, debit numeric) RETURNS numeric AS $$

UPDATE bank

SET balance = balance - debit

WHERE accountno = tf1.accountno;

SELECT 1;

$$ LANGUAGE SQL;

一个用户可以这样执行这个函数来从账户 17 中借记 $100.00：

SELECT tf1(17, 100.0);

在这个例子中，我们为第一个参数选择了名称accountno，但是这和表bank中的一个列名相同。 在UPDATE命令中， accountno引用列bank.accountno，因此 tf1.accountno必须被用来引用该参数。 我们当然可以通过为该参数使用一个不同的名称来避免这样的问题。

实际上我们可能喜欢从该函数得到一个更有用的结果而不是一个常数 1，因此一个更可能的定义是：

CREATE FUNCTION tf1 (accountno integer, debit numeric) RETURNS numeric AS $$

UPDATE bank

SET balance = balance - debit

WHERE accountno = tf1.accountno;

SELECT balance FROM bank WHERE accountno = tf1.accountno;

$$ LANGUAGE SQL;

它会调整余额并且返回新的余额。 同样的事情也可以用一个使用RETURNING的命令实现：

CREATE FUNCTION tf1 (accountno integer, debit numeric) RETURNS numeric AS $$

UPDATE bank

SET balance = balance - debit

WHERE accountno = tf1.accountno

RETURNING balance;

$$ LANGUAGE SQL;

SQL函数必须恰好返回其声明的结果类型。这可能会要求插入一个显式的造型。例如，假设我们想要之前的add\_em函数返回类型float8。下面的做法是不行的：

CREATE FUNCTION add\_em(integer, integer) RETURNS float8 AS $$

SELECT $1 + $2;

$$ LANGUAGE SQL;

即便在其他的环境中瀚高数据库也会想要插入一个隐式造型把integer转换成float8。我们需要把它写成

CREATE FUNCTION add\_em(integer, integer) RETURNS float8 AS $$

SELECT ($1 + $2)::float8;

$$ LANGUAGE SQL;

### 组合类型上的SQL函数

在编写使用组合类型参数的函数时，我们必须不仅指定我们想要哪些参数，还要指定参数的期望属性（域）。例如，假定 emp是一个包含雇员数据的表，并且因此它也是该表每一行的组合类型的名称。 这里是一个函数double\_salary，它计算某个人的双倍薪水：

CREATE TABLE emp (

name text,

salary numeric,

age integer,

cubicle point

);

INSERT INTO emp VALUES ('Bill', 4200, 45, '(2,1)');

CREATE FUNCTION double\_salary(emp) RETURNS numeric AS $$

SELECT $1.salary \* 2 AS salary;

$$ LANGUAGE SQL;

SELECT name, double\_salary(emp.\*) AS dream

FROM emp

WHERE emp.cubicle ~= point '(2,1)';

name | dream

\------+-------

Bill | 8400

注意语法$1.salary的使用是要选择参数行值的一个域。 还要注意调用的SELECT命令是如何使用table\_name.\*来选择一个表的整个当前行作为一个组合值的。该表行也可以只用表名来引用：

SELECT name, double\_salary(emp) AS dream

FROM emp

WHERE emp.cubicle ~= point '(2,1)';

有时候实时构建一个组合参数很方便。这可以用ROW结构完成。例如，我们可以调整被传递给函数的数据：

SELECT name, double\_salary(ROW(name, salary\*1.1, age, cubicle)) AS dream

FROM emp;

也可以构建一个返回组合类型的函数。这是一个返回单一emp行的函数例子：

CREATE FUNCTION new\_emp() RETURNS emp AS $$

SELECT text 'None' AS name,

1000.0 AS salary,

25 AS age,

point '(2,2)' AS cubicle;

$$ LANGUAGE SQL;

在这个例子中，我们为每一个属性指定了一个常量值，但是可以用任何计算来替换这些常量。

有关定义函数有两件重要的事情：

• 查询中的选择列表顺序必须和列在与组合类型相关的表中出现的顺序完全相同（如我们上面所作的，列的命名与系统无关）。

• 我们必须确保每个表达式的类型匹配该组合类型相应的列，必要时插入一个造型。否则我们将会得到像这样的错误：

ERROR: function declared to return emp returns varchar instead of text at

column 1

与基础类型的情况一样，该函数将不会自动插入任何造型。

定义同样的函数的一种不同的方法是：

CREATE FUNCTION new\_emp() RETURNS emp AS $$

SELECT ROW('None', 1000.0, 25, '(2,2)')::emp;

$$ LANGUAGE SQL;

这里我们写了一个只返回正确组合类型的单一列的SELECT。 在这种情况下这种写法实际并非更好，但是它在一些情况下比较方便 — 例如，我们需要通过调用另一个返回所期望的组合值的函数来计算结果。另一个例子是，如果我们尝试写一个函数返回组合上的一个域，而不是返回纯粹的组合类型，那么总是有必要把它写成返回单一列，因为没有其他办法能够产生一个正好是那种域类型的值。

我们可以直接调用这个函数或者在一个值表达式中使用它：

SELECT new\_emp();

new\_emp

\--------------------------

(None,1000.0,25,"(2,2)")

或者把它当做一个表函数调用：

SELECT \* FROM new\_emp();

name | salary | age | cubicle

\------+--------+-----+---------

None | 1000.0 | 25 | (2,2)

第二种方式在第 37.5.7 节中有更完全的描述。

当你使用一个返回组合类型的函数时，你可能只想要其结果中的一个域（属性）。 你可以这样做：

SELECT (new\_emp()).name;

name

\------

None

额外的圆括号是必须的，它用于避免解析器被搞混。如果你不写这些括号，会这样：

SELECT new\_emp().name;

ERROR: syntax error at or near "."

LINE 1: SELECT new\_emp().name;

另一个选项是使用函数记号来抽取一个属性：

SELECT name(new\_emp());

name

\------

None

字段记法和函数记法是等效的。

另一种使用返回组合类型的函数的方法是把结果传递给另一个接收正确行类型作为输入的函数：

CREATE FUNCTION getname(emp) RETURNS text AS $$

SELECT $1.name;

$$ LANGUAGE SQL;

SELECT getname(new\_emp());

getname

\---------

None

(1 row)

### 带有输出参数的SQL函数

一种描述一个函数的结果的替代方法是定义它的输出参数，例如：

CREATE FUNCTION add\_em (IN x int, IN y int, OUT sum int)

AS 'SELECT x + y'

LANGUAGE SQL;

SELECT add\_em(3,7);

add\_em

\--------

10

(1 row)

输出参数的真正价值是它们提供了一种方便的方法来定义返回多个列的函数。例如，

CREATE FUNCTION sum\_n\_product (x int, y int, OUT sum int, OUT product int)

AS 'SELECT x + y, x \* y'

LANGUAGE SQL;

SELECT \* FROM sum\_n\_product(11,42);

sum | product

\-----+---------

53 | 462

(1 row)

这里实际发生的是我们为该函数的结果创建了一个匿名的组合类型。上述例子具有与下面相同的最终结果

CREATE TYPE sum\_prod AS (sum int, product int);

CREATE FUNCTION sum\_n\_product (int, int) RETURNS sum\_prod

AS 'SELECT $1 + $2, $1 \* $2'

LANGUAGE SQL;

但是不必单独定义组合类型常常很方便。注意输出参数的名称并非只是装饰，而且决定了匿名组合类型的列名（如果你为一个输出参数忽略了名称，系统将自行选择一个名称）。

在从 SQL 调用这样一个函数时，输出参数不会被包括在调用参数列表中。这是因为 瀚高数据库只考虑输入参数来定义函数的调用签名。这也意味着在为诸如删除函数等目的引用该函数时只有输入参数有关系。我们可以用下面的命令之一删除上述函数

DROP FUNCTION sum\_n\_product (x int, y int, OUT sum int, OUT product int);

DROP FUNCTION sum\_n\_product (int, int);

参数可以被标记为IN（默认）、OUT、INOUT或者VARIADIC。一个INOUT参数既作为一个输入参数（调用参数列表的一部分）又作为一个输出参数（结果记录类型的一部分）。VARIADIC参数是输入参数，但被按照后文所述特殊对待。

### 带有可变数量参数的SQL函数

只要”可选的”参数都是相同的数据类型，SQL函数可以被声明为接受可变数量的参数。可选的参数将被作为一个数组传递给该函数。声明该函数时要把最后一个参数标记为VARIADIC，这个参数必须被声明为一个数组类型，例如：

CREATE FUNCTION mleast(VARIADIC arr numeric\[\]) RETURNS numeric AS $$

SELECT min($1\[i\]) FROM generate\_subscripts($1, 1) g(i);

$$ LANGUAGE SQL;

SELECT mleast(10, -1, 5, 4.4);

mleast

\--------

\-1

(1 row)

实际上，所有位于或者超过VARIADIC位置的实参会被收集成一个一位数组，就好像你写了：

SELECT mleast(ARRAY\[10, -1, 5, 4.4\]); -- 不起作用

但是你实际无法这样写 — 或者说至少它将无法匹配这个函数定义。一个被标记为VARIADIC的参数匹配其元素类型的一次或者多次出现，而不是它自身类型的出现。

有时候能够传递一个已经构造好的数组给 variadic 函数是有用的，特别是当 一个 variadic 函数想要把它的数组参数传递给另一个函数时这会特别方便。此外，这是在一个允许不可信用户创建对象的方案中调用一个variadic函数的唯一安全的方式，见第 10.3 节。你可以通过在调用中指定VARIADIC来做到这一点：

SELECT mleast(VARIADIC ARRAY\[10, -1, 5, 4.4\]);

这会阻止该函数的 variadic 参数扩展成它的元素结构，从而允许数组参 数值正常匹配。VARIADIC只能被附着在函数调用的最后一 个实参上。

在调用中指定VARIADIC也是将空数组传递给 variadic 函数 的唯一方式，例如：

SELECT mleast(VARIADIC ARRAY\[\]::numeric\[\]);

简单地写成SELECT mleast()是没有作用的，因为一个 variadic 参数必须匹配至少一个实参（如果想允许这类调用，你可以定义第二个没有 参数且也叫mleast的函数）。

从一个 variadic 参数产生的数组元素参数会被当做自己不具有名称。这 意味着不能使用命名参数调用 variadic 函数，除非你指定了 VARIADIC。例如下面的调用是可以工作的：

SELECT mleast(VARIADIC arr => ARRAY\[10, -1, 5, 4.4\]);

但这些就不行：

SELECT mleast(arr => 10);

SELECT mleast(arr => ARRAY\[10, -1, 5, 4.4\]);

### 带有参数默认值的SQL函数

函数可以被声明为对一些或者所有输入参数具有默认值。只要调用函数时 没有给出足够多的实参，就会插入默认值来弥补缺失的实参。由于参数只 能从实参列表的尾部开始被省略，在一个有默认值的参数之后的所有参数 都不得不也具有默认值（尽管使用命名参数记法可以允许放松这种限制， 这种限制仍然会被强制以便位置参数记法能工作）。不管你是否使用它，这种能力都要求在某些用户不信任其他用户的数据中调用函数时做一些预防措施。

例如：

CREATE FUNCTION foo(a int, b int DEFAULT 2, c int DEFAULT 3)

RETURNS int

LANGUAGE SQL

AS $$

SELECT $1 + $2 + $3;

$$;

SELECT foo(10, 20, 30);

foo

\-----

60

(1 row)

SELECT foo(10, 20);

foo

\-----

33

(1 row)

SELECT foo(10);

foo

\-----

15

(1 row)

SELECT foo(); -- 因为第一个参数没有默认值，所以会失败

ERROR: function foo() does not exist

\=符号也可以用来替代关键词 DEFAULT。

### SQL 函数作为表来源

所有的 SQL 函数都可以被用在查询的FROM子句中，但是 对于返回组合类型的函数特别有用。如果函数被定义为返回一种基本类型， 该表函数会产生一个单列表。如果该函数被定义为返回一种组合类型，该 表函数会为该组合类型的每一个属性产生一列。

这里是一个例子：

CREATE TABLE foo (fooid int, foosubid int, fooname text);

INSERT INTO foo VALUES (1, 1, 'Joe');

INSERT INTO foo VALUES (1, 2, 'Ed');

INSERT INTO foo VALUES (2, 1, 'Mary');

CREATE FUNCTION getfoo(int) RETURNS foo AS $$

SELECT \* FROM foo WHERE fooid = $1;

$$ LANGUAGE SQL;

SELECT \*, upper(fooname) FROM getfoo(1) AS t1;

fooid | foosubid | fooname | upper

\-------+----------+---------+-------

1 | 1 | Joe | JOE

(1 row)

正如例子所示，我们可以把函数结果的列当作常规表的列来使用。

注意我们只从函数得到了一行。这是因为我们没有使用SETOF。 这会在下一节中介绍。

### 返回集合的SQL函数

当一个 SQL 函数被声明为返回SETOF sometype时，该函数的 最后一个查询会被执行完，并且它输出的每一行都会被 作为结果集的一个元素返回。

在FROM子句中调用函数时通常会使用这种特性。在这种 情况下，该函数返回的每一行都变成查询所见的表的一行。例如，假设 表foo具有和上文一样的内容，并且我们做了以下动作：

CREATE FUNCTION getfoo(int) RETURNS SETOF foo AS $$

SELECT \* FROM foo WHERE fooid = $1;

$$ LANGUAGE SQL;

SELECT \* FROM getfoo(1) AS t1;

那么我们会得到：

fooid | foosubid | fooname

\-------+----------+---------

1 | 1 | Joe

1 | 2 | Ed

(2 rows)

也可以返回多个带有由输出参数定义的列的行，像这样：

CREATE TABLE tab (y int, z int);

INSERT INTO tab VALUES (1, 2), (3, 4), (5, 6), (7, 8);

CREATE FUNCTION sum\_n\_product\_with\_tab (x int, OUT sum int, OUT product int)

RETURNS SETOF record

AS $$

SELECT $1 + tab.y, $1 \* tab.y FROM tab;

$$ LANGUAGE SQL;

SELECT \* FROM sum\_n\_product\_with\_tab(10);

sum | product

\-----+---------

11 | 10

13 | 30

15 | 50

17 | 70

(4 rows)

这里的关键点是必须写上RETURNS SETOF record来指示 该函数返回多行而不是一行。如果只有一个输出参数，则写上该参数的 类型而不是record。

通过多次调用集合返回函数来构建查询的结果非常有用，每次调用的参数 来自于一个表或者子查询的连续行。这里是一个使用集合返回函数枚举树结构中元素的例子：

SELECT \* FROM nodes;

name | parent

\-----------+--------

Top |

Child1 | Top

Child2 | Top

Child3 | Top

SubChild1 | Child1

SubChild2 | Child1

(6 rows)

CREATE FUNCTION listchildren(text) RETURNS SETOF text AS $$

SELECT name FROM nodes WHERE parent = $1

$$ LANGUAGE SQL STABLE;

SELECT \* FROM listchildren('Top');

listchildren

\--------------

Child1

Child2

Child3

(3 rows)

SELECT name, child FROM nodes, LATERAL listchildren(name) AS child;

name | child

\--------+-----------

Top | Child1

Top | Child2

Top | Child3

Child1 | SubChild1

Child1 | SubChild2

(5 rows)

这个例子和我们使用的简单连接的效果没什么不同，但是在更复杂的 计算中，把一些工作放在函数中会是一种很方便的选项。

返回集合的函数也能在查询的选择列表中调用。对于该查询本身产生的每一行都会调用集合返回函数，并且会从该函数的结果集中的每一个元素生成一个输出行。之前的例子也可以用这样的查询实现：

SELECT listchildren('Top');

listchildren

\--------------

Child1

Child2

Child3

(3 rows)

SELECT name, listchildren(name) FROM nodes;

name | listchildren

\--------+--------------

Top | Child1

Top | Child2

Top | Child3

Child1 | SubChild1

Child1 | SubChild2

(5 rows)

在最后一个SELECT中，注意对于Child2、Child3等没有出现输出行。这是因为listchildren 对这些参数返回空集，因此没有产生结果行。这和使用LATERAL 语法时，我们从与该函数结果的内连接得到的行为是一样的。

瀚高数据库中，写在查询的选择列表中的集合返回函数的行为几乎和写在LATERAL FROM子句项中的集合返回函数完全一样。例如：

SELECT x, generate\_series(1,5) AS g FROM tab;

几乎等效于 SELECT x, g FROM tab, LATERAL generate\_series(1,5) AS g;

这会是完全一样的，除了在这个特别的例子中，规划器会选择把g放在嵌套循环连接的外侧，因为g对tab没有实际的横向依赖。那会导致一种不同的输出行顺序。选择列表中的集合返回函数总是会被计算，就好像它们在FROM子句剩余部分的嵌套循环连接的内侧一样，因此在考虑来自FROM子句的下一行之前，这些函数会运行到完成。

如果在查询的选择列表中有不止一个集合返回函数，则行为类似于把那些函数放到一个单一的LATERAL ROWS FROM(... ) FROM子句项中的行为。对于来自底层查询的每一行，都有一个用到每个函数首个结果的输出行，然后是一个使用每个函数第二个结果的输出行，以此类推。如果某些集合返回函数产生的输出比其他函数少，会用空值代替缺失的数据，因此为一个底层行形成的总行数等于产生最多输出的集合返回函数的输出行数。因此集合返回函数会”步调一致”地运行直到它们的输出被耗尽，然后用下一个底层行继续执行。

集合返回函数可以被嵌套在一个选择列表中，不过在FROM子句项中不允许这样做。在这种情况下，嵌套的每一层会被单独对待，就像它是一个单独的LATERAL ROWS FROM(... )项一样。例如，在

SELECT srf1(srf2(x), srf3(y)), srf4(srf5(z)) FROM tab;

中，集合返回函数srf2、srf3和srf5将为tab的每一行步调一致地运行，然后会对较低层的函数产生的每一行以步调一致的形式应用srf1和srf4。

在CASE或COALESCE这样的条件计算结构中，不能使用集合返回函数。例如，考虑 SELECT x, CASE WHEN x > 0 THEN generate\_series(1, 5) ELSE 0 END FROM tab;

看起来这个语句应该产生满足x > 0的输入行的五次重复，以及不满足的行的一次重复。但实际上，由于在CASE表达时被计算前，generate\_series(1, 5)会被运行在一个隐式的LATERAL FROM项中，它会为每个输入行产生五次重复。为了减少混乱，这类情况会产生一个解析时错误。

| 注意： |
| --- |
| 如果函数的最后一个命令是带有RETURNING的 INSERT、UPDATE或者 DELETE，该命令将总是会被执行完，即使函数没有用SETOF定义或者调用查询不要求取出所有结果行也是如此。 RETURNING子句产生的多余的行会被悄无声息地丢掉，但是 在命令的目标表上的修改仍然会发生（而且在从该函数返回前就会全部完成）。 |

### 返回TABLE的SQL函数

还有另一种方法可以把函数声明为返回一个集合，即使用 RETURNS TABLE(columns)语法。

这等效于使用一个或者多个OUT参数外加把函数标记为返回 SETOF record（或者是SETOF单个输出参数的 类型）。这种写法是在最近的 SQL 标准中指定的，因此可能比使用 SETOF的移植性更好。

例如，前面的求和并且相乘的例子也可以这样来做：

CREATE FUNCTION sum\_n\_product\_with\_tab (x int)

RETURNS TABLE(sum int, product int) AS $$

SELECT $1 + tab.y, $1 \* tab.y FROM tab;

$$ LANGUAGE SQL;

不允许把显式的OUT或者INOUT参数用于 RETURNS TABLE记法 — 必须把所有输出列放在 TABLE列表中。

### 多态SQL函数

SQL函数可以被声明为接受并且返回多态类型

anyelement、anyarray、 anynonarray、anyenum以及 anyrange。更多关于多态函数的解释请见第 37.2.5 节。这里是一个从两种任意数据 类型的元素构建一个数组的多态函数make\_array：

CREATE FUNCTION make\_array(anyelement, anyelement) RETURNS anyarray AS $$

SELECT ARRAY\[$1, $2\];

$$ LANGUAGE SQL;

SELECT make\_array(1, 2) AS intarray, make\_array('a'::text, 'b') AS textarray;

intarray | textarray

\----------+-----------

{1,2} | {a,b}

(1 row)

注意类型造型'a'::text的使用是为了指定该参数的类型 是text。如果该参数只是一个字符串这就是必须的，因为 否则它会被当作unknown类型，并且 unknown的数组也不是一种合法的类型。如果没有改类型 造型，将得到这样的错误：

ERROR: could not determine polymorphic type because input has type "unknown"

允许具有多态参数和固定的返回类型，但是反过来不行。例如：

CREATE FUNCTION is\_greater(anyelement, anyelement) RETURNS boolean AS $$

SELECT $1 > $2;

$$ LANGUAGE SQL;

SELECT is\_greater(1, 2);

is\_greater

\------------

f

(1 row)

CREATE FUNCTION invalid\_func() RETURNS anyelement AS $$

SELECT 1;

$$ LANGUAGE SQL;

ERROR: cannot determine result data type

DETAIL: A function returning a polymorphic type must have at least one

polymorphic argument.

多态化可以用在具有输出参数的函数上。例如：

CREATE FUNCTION dup (f1 anyelement, OUT f2 anyelement, OUT f3 anyarray)

AS 'select $1, array\[$1,$1\]' LANGUAGE SQL;

SELECT \* FROM dup(22);

f2 | f3

\----+---------

22 | {22,22}

(1 row)

多态化也可以用在 variadic 函数上。例如：

CREATE FUNCTION anyleast (VARIADIC anyarray) RETURNS anyelement AS $$

SELECT min($1\[i\]) FROM generate\_subscripts($1, 1) g(i);

$$ LANGUAGE SQL;

SELECT anyleast(10, -1, 5, 4);

anyleast

\----------

\-1

(1 row)

SELECT anyleast('abc'::text, 'def');

anyleast

\----------

abc

(1 row)

CREATE FUNCTION concat\_values(text, VARIADIC anyarray) RETURNS text AS $$

SELECT array\_to\_string($2, $1);

$$ LANGUAGE SQL;

SELECT concat\_values('|', 1, 4, 2);

concat\_values

\---------------

1|4|2

(1 row)

### 带有排序规则的SQL函数

当一个 SQL 函数具有一个或者更多可排序数据类型的参数时，对每一次函数调用都会根据分配给实参的排序规则为其确定一个排序规则。如果成功地确定（即在 参数之间没有隐式排序规则的冲突），那么所有的可排序参数都被认 为隐式地具有该排序规则。这将会影响函数中对排序敏感的操作的行为。例如，使用上述的anyleast函数时， SELECT anyleast('abc'::text, 'ABC');的结果将依赖于数据库的默认排序规则。在C区域中， 结果将是ABC，但是在很多其他区域中它将是 abc。可以在任意参数上增加一个COLLATE 子句来强制要使用的排序规则，例如：

SELECT anyleast('abc'::text, 'ABC' COLLATE "C");

此外，如果你希望一个函数用一个特定的排序规则工作而不管用什么排序规则 调用它，可根据需要在函数定义中插入COLLATE子句。 这种版本的anyleast将总是使用en\_US区域来比较字符串：

CREATE FUNCTION anyleast (VARIADIC anyarray) RETURNS anyelement AS $$

SELECT min($1\[i\] COLLATE "en\_US") FROM generate\_subscripts($1, 1) g(i);

$$ LANGUAGE SQL;

但是注意如果应用到不可排序数据类型上，这将会抛出一个错误。

如果在实参之间无法确定共同的排序规则，那么 SQL 函数会把它的参数 当作拥有其数据类型的默认排序规则（通常是数据库的默认排序规则， 但是域类型的参数可能会不同）。

可排序参数的行为可以被想成是多态的一种受限形式，只对于文本数据类型有效。

## 函数重载

可以用同样的 SQL 名称定义多于一个函数，只要它们的参数不同即可。 换句话说，函数名可以被重载。不管你是否使用它，这种能力都要求在某些用户不信任其他用户的数据中调用函数时做一些预防措施。当一个查询被执行时，服务器将从数据类型和所提供的参数个数来决定要调用哪个函数。重载也可用来模拟具有可变参数个数（最大个数有限）的函数。

在创建一个重载函数家族时，应该小心不要创建歧义。例如，给定函数：

CREATE FUNCTION test(int, real) RETURNS...

CREATE FUNCTION test(smallint, double precision) RETURNS...

对于test(1, 1.5)这样的输入就无法立刻清楚地知道应该调用哪个函数。一个具有单个组合类型参数的函数通常不应与该类型的任何属性（域） 重名。回想一下，attribute(table)被认为等效于 table.attribute。在出现”一个组合类型 上的函数”与”组合类型的一个属性”的情况下，将总是使用属性。 可以通过用模式限定该函数名（即 schema.func(table) ）来覆盖这种选择，但是最好不要选择有冲突的名称以避免此类问题。

另一种可能的冲突在于 variadic 和非 variadic 函数之间。例如，可以创建

foo(numeric)和foo(VARIADIC numeric\[\])。 在这种情况下，对于提供了一个数字参数的调用（例如foo(10.1)） 就不清楚应该匹配哪一个函数。规则是使用在搜索路径中出现得较早的函数，或者当两者都在同一个模式中时优先使用非 variadic 的那一个函数。

在重载 C 语言函数时有一个额外的约束：重载函数家族中的每一个函数的 C 名称必须与其他所有函数的 C 名称不同，不管是内部的还是动态载入的。如果这条规则被违背，该行为将不可移植。你可能会得到一个运行时链接器错误，或者这些函数之一将被调用（通常是内部的那一个）。SQL CREATE FUNCTION命令的AS子句的另一种形式可以把 SQL 函数名和 C源代码中的函数名分离。例如：

CREATE FUNCTION test(int) RETURNS int

AS 'filename', 'test\_1arg'

LANGUAGE C;

CREATE FUNCTION test(int, int) RETURNS int

AS 'filename', 'test\_2arg'

LANGUAGE C;

这里的 C 函数名称反映了很多种可能的习惯之一。

## 函数易变性分类

每一个函数都有一个易变性分类，可能是 VOLATILE、STABLE或者IMMUTABLE。 如果CREATE FUNCTION命令没有指定一个分类，则默认是 VOLATILE。易变性分类是给优化器的关于该函数行为的一种承诺：

• 一个VOLATILE函数可以做任何事情，包括修改数据库。在 使用相同的参数连续调用时，它能返回不同的结果。优化器不会对这类函 数的行为做任何假定。在每一行需要volatile 函数值时，一个使用 volatile 函数的查询都会重新计算该函数。

• 一个STABLE函数不能修改数据库并且被确保对一个语句中 的所有行用给定的相同参数返回相同的结果。这种分类允许优化器把该函 数的多个调用优化成一个调用。特别是，在一个索引扫描条件中使用包含 这样一个函数的表达式是安全的（因为一次索引扫描只会计算一次比较值， 而不是为每一行都计算一次，在一个索引扫描条件中不能使用 VOLATILE函数）。

• 一个IMMUTABLE函数不能修改数据库并且被确保用相同的参数 永远返回相同的结果。这种分类允许优化器在一个查询用常量参数调用该函数 时提前计算该函数。例如，一个

SELECT... WHERE x = 2 + 2这样的查询可以被简化为 SELECT... WHERE x = 4，因为整数加法操作符底层的函数被 标记为IMMUTABLE。

为了最好的优化结果，你应该把函数标记为对它们合法的易变性分类中最严格 的那种。

任何带有副作用的函数必须被标记为VOLATILE， 这样对它的调用就不能被优化掉。甚至如果一个函数的值在一个查询中会 变化，即使它没有副作用也需要被标记为VOLATILE。这样的例子有random()、currval()、 timeofday()等。

另一种重要的例子是current\_timestamp家族的函数有资格 被标记为STABLE，因为它们的值在一个事务中不会改变。

在考虑先规划然后立即执行的简单交互式查询时，在STABLE和 IMMUTABLE分类间的区别相对较小：一个函数是在规划时只 执行一次还是在查询执行开始期间只执行一次没有太大关系。但是如果计划 被保存下来然后在后面被重用，区别就大了。如果在不允许过早把一个函数 变成规划期间的一个常数时把它标记为IMMUTABLE，会导致 在后续重用该计划时用到一个陈旧的值。当使用预备语句或者使用会缓存计 划的函数语言（PL/pgSQL）时，这就会是一种灾难。

对于用 SQL 或者其他任何标准过程语言编写的函数，还有第二种由易变性分类 决定的特性，即由调用该函数的 SQL 命令所作的数据修改的可见性。 VOLATILE函数将看到这些更改，STABLE 或者IMMUTABLE函数则看不到。这种行为使用 MVCC 的快照行为实现：STABLE和 IMMUTABLE函数使用一个在调用查询开始时建立的快照，而 VOLATILE函数在它们执行的每一个查询的开始都获得一个新鲜 的快照。

| 注意： |
| --- |
| 用 C 编写的函数按照它们自己需要的方式管理快照，但是通常最好 让 C 函数也按照上面的方式来。 |

由于这种快照行为，一个只包含SELECT命令的函数可以被 安全地标记为STABLE，即便它选择的表可能正在被并发查询所 修改。瀚高数据库将使用为调用查询所 建立的快照来执行STABLE函数中的所有命令，因此它将在整个 查询期间看到一种数据库的固定视图。

对IMMUTABLE函数中的SELECT使用了相同 的快照行为。通常在一个IMMUTABLE函数中从数据库表选择是 不明智的，因为如果表内容变化就会破坏不变性。不过， 瀚高数据库不会强制不让你这样做。

一种常见的错误是当一个函数的结果依赖于一个配置参数时把它标记为 IMMUTABLE。例如，一个操纵时间戳的函数有可能结果 依赖于TimeZone设置。为了安全起见，这类 函数应该被标记为STABLE。

| 注意： |
| --- |
| 瀚高数据库要求STABLE 和IMMUTABLE函数中不包含非SELECT 的 SQL 命令以阻止数据修改（这也不是完全万无一失，因为这类函数还可以调用修改数据库的VOLATILE函数。如果那样做，你将发现 该STABLE或IMMUTABLE函数不会发现由被调 用函数所作的数据库改变，因为它们对它的快照不可见）。 |

## 过程语言函数

瀚高数据库允许用除 SQL 和 C 之外 的语言编写用户定义的函数。这些语言通常被称为过程语言（PL）。 过程语言并不内建在瀚高数据库服务器中， 它们通过可装载模块提供。

## 内部函数

内部函数由 C 编写并且已经被静态链接到数据库服务器中。该函数定义的”主体”指定该函数的 C 语言名称，它必须和声明 SQL 函数所用的名称一样（为了向后兼容性的原因，也接受空主体，那时会认为 C 语言函数名与 SQL 函数名相同）。

通常，所有存在于服务器中的内部函数都在数据库集簇的初始化期间被声明，但是用户可以使用 CREATE FUNCTION为一个内部函数创建 额外的别名。在CREATE FUNCTION中用 语言名internal来声明内部函数。例如，要为 sqrt函数创建一个别名：

CREATE FUNCTION square\_root(double precision) RETURNS double precision

AS 'dsqrt'

LANGUAGE internal

STRICT;

（大部分内部函数应该被声明为”严格”）。

| 注意： |
| --- |
| 上述场景中并非所有”预定义”的函数都是 “内部”函数。有些预定义的函数由 SQL 编写。 |

## C 语言函数

用户定义的函数可以用 C 编写（或者可以与 C 兼容的语言，例如 C++）。 这类函数被编译成动态载入对象（也被称为共享库）并且由服务器在需要时载入。动态载入是把”C语言”函数和 “内部”函数区分开的特性 — 两者真正的编码习惯 实际上是一样的（因此，标准的内部函数库是用户定义的 C 函数很好的源代码实例）。

当前仅有一种调用约定被用于C函数（”版本1”）。如下文所示，为函数编写一个PG\_FUNCTION\_INFO\_V1()宏就能指示对该调用约定的支持。

### 动态载入

在一个会话中第一次调用一个特定可载入对象文件中的用户定义函数时， 动态载入器会把那个对象文件载入到内存以便该函数被调用。因此用户定义的 C 函数的CREATE FUNCTION必须为该函数指定两块信息：可载入对象文件的名称，以及要在该对象文件中调用的特定函数的 C 名称（链接符号）。如果没有显式指定 C 名称，则它被假定为和 SQL 函数名相同。

下面的算法被用来基于CREATE FUNCTION 命令中给定的名称来定位共享对象文件：

1\. 如果名称是一个绝对路径，则载入给定的文件。

2\. 如果该名称以字符串$libdir开始，那么这一部分会被 Highgo Database包的库目录名（在编译时确定）替换。

3\. 如果该名称不包含目录部分，会在配置变量 dynamic\_library\_path指定的路径中搜索该文件。

4\. 否则（在该路径中没找到该文件，或者它包含一个非绝对目录）， 动态载入器将尝试接受给定的名称，这大部分会导致失败（依赖 当前工作目录是不可靠的）。

如果这个序列不起作用，会把平台相关的共享库文件名扩展（通常是.so）追加到给定的名称并且再次尝试上述的过程。如果还是失败，则载入失败。

我们推荐相对于$libdir或者通过动态库路径来 定位共享库。如果升级版本时新的安装在一个不同的位置，则可以简化升级过程。$libdir实际表示的目录可以用命令pg\_config -- pkglibdir来找到。

用于运行Highgo Database服务器的用户 ID 必须能够通过要载入文件的路径。常见的错误是把文件或更高层的目录变得对postgres用户不可读或者不可执行。

在任何情况下，CREATE FUNCTION命令中给定的文件名会被原封不动地记录在系统目录中，这样如果需要再次载入该文件则会应用同样的过程。

| 注意： |
| --- |
| Highgo Database不会自动编译 C 函数。在从CREATE FUNCTION命令中引用对象文件之前，它必须先被编译好。 |

为了确保动态载入对象文件不会被载入到一个不兼容的服务器，Highgo Database会检查该文件是否包含一个带有合适内容的”magic block”。这允许服务器检测到明显的不兼容，例如为不同Highgo Database主版本编译的代码。要包括一个magic block，在写上包括头文件fmgr.h的语句之后，在该模块的源文件之一（并且只能在其中一个）中写上这些：

PG\_MODULE\_MAGIC;

在被第一次使用后，动态载入对象文件会留在内存中。在同一个会话中对该函数未来的调用将只会消耗很小的负荷进行符号表查找。如果需要重新载入一个对象文件（例如重新编译以后），需要开始一个新的会话。

可以选择让一个动态载入文件包含初始化和终止化函数。如果文件包含一个名为\_PG\_init的函数，则文件被载入后会立刻调用该函数。该函数不接受参数并且应该返回void。如果文件包括一个名为\_PG\_fini的函数，则在卸载该文件之前会立即调用该函数。

同样地，该函数不接受参数并且应该返回void。注意将只在卸载文件的过程中会调用\_PG\_fini，进程结束时不会调用它（当前，卸载被禁用并且从不发生，但是未来可能会改变）。

### C 语言函数中的基本类型

要了解如何编写 C 语言函数，你需要了解 Highgo Database如何在内部表达基本数据类型以及如何与函数传递它们。在内部，Highgo Database把一个基本类型认为是 “一团内存”。在类型上定义的用户定义函数说明了 Highgo Database在该类型上操作的方式。也就是说，Highgo Database将只负责把数据存在磁盘以及从磁盘检索数据，而使用你的用户定义函数来输入、处理和输出该数据。

基本类型可以有三种内部格式之一：

• 传值，定长

• 传引用，定长

• 串引用，变长

传值类型在长度上只能是 1、2 或 4 字节（如果你的机器上sizeof(Datum)是8，则还有8字节）。你应当小心地定义你的类型以便它们在所有的架构上都是相同的尺寸（字节）。

例如， long类型很危险，因为它在某些机器上是 4 字节但在另外一些机器上是 8 字节，而int类型在大部分 Unix 机器上都是 4 字节。在 Unix 机器上int4类型一种合理的实现可能是：

/\* 4 字节整数，传值 \*/

typedef int int4;

（实际的Highgo Database C代码会把这种类型称为int32，因为 C 中的习惯是intXX 表示XX位。注意因此还有尺寸为 1 字节的 C 类型int8。SQL 类型 int8在 C 中被称为int64。）。

在另一方面，任何尺寸的定长类型可以用传引用的方法传递。例如，这里有一种瀚高数据库类型的实现示例：

/\* 16 字节结构，传引用 \*/

typedef struct

{

double x, y;

} Point;

在Highgo Database函数中传进或传出这种类型时，只能使用指向这种类型的指针。要返回这样一种类型的值，用 palloc分配正确的内存量，然后填充分配好的内存，并且返回一个指向该内存的指针（还有，如果只想返回与具有相同数据类型的一个输入参数相同的值，可以跳过额外的palloc并且返回指向该输入值的指针）。

最后，所有变长类型必须也以引用的方式传递。所有变长类型必须用一个正好 4 字节的不透明长度域开始，该域会由SET\_VARSIZE 设置，绝不要直接设置该域！所有要被存储在该类型中的数据必须在内存中接着该长度域的后面存储。长度域包含该结构的总长度，也就是包括长度域本身的尺寸。

另一个重点是要避免在数据类型值中留下未被初始化的位。例如，要注意把可能存在于结构中的任何对齐填充字节置零。如果不这样做，你的数据类型的逻辑等价常量可能会被规划器认为是不等的，进而导致低效的（不过还是正确的）计划。

| 警告： |
| --- |
| 绝不要修改通过引用传递的输入值的内容。如果这样做很可能会破坏磁盘上的数据，因为给出的指针可能直接指向一个磁盘缓冲区。 |

例如，我们可以这样定义类型text：

typedef struct {

int32 length;

char data\[FLEXIBLE\_ARRAY\_MEMBER\];

} text;

\[FLEXIBLE\_ARRAY\_MEMBER\]记号表示数据部分的实际长度不由该声明指定。

在操纵变长字节时，我们必须小心地分配正确数量的内存并且正确地设置长度域。例如，如果我们想在一个text结构中存储 40 字节，我们可以使用这样的代码片段：

#include "postgres.h"

...

char buffer\[40\]; /\* our source data \*/

...

text \*destination = (text \*) palloc(VARHDRSZ + 40);

SET\_VARSIZE(destination, VARHDRSZ + 40);

memcpy(destination->data, buffer, 40);

VARHDRSZ和sizeof(int32)一样， 但是用宏VARHDRSZ来引用变长类型的载荷的尺寸被认为是比较好的风格。还有，必须使用SET\_VARSIZE宏来设置长度域，而不是用简单的赋值来设置。

下表指定在编写使用一种 Highgo Database内建类型的 C 语言函数时，哪一种 C 类型对应于哪一种 SQL 类型。”定义文件”列给出了要得到该类型定义需要包括的头文件（实际的定义可能在一个由列举文件包括的不同文件中。推荐用户坚持使用已定义的接口）。注意在任何源文件中应该总是首先包括postgres.h， 因为它声明了很多你需要的东西。

**表 6.1 内建 SQL 类型等效的 C 类型**

| SQL 类型 | C 类型 | 定义文件 |
| --- | --- | --- |
| boolean | bool | postgres.h（可能是编译器内建） |
| box | BOX | utils/geo\_decls.h |
| bytea | bytea | postgres.h |
| "char" | char | （编译器内建） |
| character | BpChar | postgres.h |
| cid | CommandId | postgres.h |
| date | DateADT | utils/date.h |
| smallint (int2) | int16 | postgres.h |
| int2vector | int2vector | postgres.h |
| integer (int4) | int32 | postgres.h |
| real (float4) | float4 | postgres.h |
| double precision (float8) | float8 | postgres.h |
| interval | Interval | datatype/timestamp.h |
| lseg | LSEG | utils/geo\_decls.h |
| name | Name | postgres.h |
| oid | oid | postgres.h |
| oidvector | oidvector | postgres.h |
| path | PATH | utils/geo\_decls.h |
| point | POINT | utils/geo\_decls.h |
| regproc | regproc | postgres.h |
| text | text | postgres.h |
| tid | ItemPointer | storage/itemptr.h |
| time | TimeADT | utils/date.h |
| time with time zone | TimeTzADT | utils/date.h |
| timestamp | Timestamp | datatype/timestamp.h |
| varchar | VarChar | postgres.h |
| xid | TransactionId | postgres.h |

### 版本 1 的调用约定

版本-1 的调用规范依赖于宏来降低传参数和结果的复杂度。版本-1 函数的 C 声明总是：

Datum funcname(PG\_FUNCTION\_ARGS)

此外，宏调用：

PG\_FUNCTION\_INFO\_V1(funcname);

必须出现在同一个源文件中（按惯例会正好写在该函数本身之前）。 这种宏调用不是internal语言函数所需要的，因为 Highgo Database会假定所有内部函数都使用版本-1 规范。

不过，对于动态载入函数是必需的。

在版本-1 函数中，每一个实参都使用对应于该参数数据类型的PG\_GETARG\_xxx()宏取得。在非严格的函数中，需要使用PG\_ARGNULL\_xxx()对参数是否为空提前做检查。结果要用对应于返回类型的PG\_RETURN\_xxx()宏返回。PG\_GETARG\_xxx()的参数是要取得的函数参数的编号，从零开始计。PG\_RETURN\_xxx()的参数是实际要返回的值。

这里是一些使用版本-1调用约定的例子：

#include "postgres.h"

#include <string.h>

#include "fmgr.h"

#include "utils/geo\_decls.h"

PG\_MODULE\_MAGIC;

/\* 传值 \*/

PG\_FUNCTION\_INFO\_V1(add\_one);

Datum

add\_one(PG\_FUNCTION\_ARGS)

{

int32 arg = PG\_GETARG\_INT32(0);

PG\_RETURN\_INT32(arg + 1);

}

/\* 传引用，定长 \*/

PG\_FUNCTION\_INFO\_V1(add\_one\_float8);

Datum

add\_one\_float8(PG\_FUNCTION\_ARGS)

{

/\* FLOAT8 的宏隐藏了它的传引用本质。 \*/

float8 arg = PG\_GETARG\_FLOAT8(0);

PG\_RETURN\_FLOAT8(arg + 1.0);

}

PG\_FUNCTION\_INFO\_V1(makepoint);

Datum

makepoint(PG\_FUNCTION\_ARGS)

{

/\* 这里，Point 的传引用本质没有被掩盖。 \*/

Point \*pointx = PG\_GETARG\_POINT\_P(0);

Point \*pointy = PG\_GETARG\_POINT\_P(1);

Point \*new\_point = (Point \*) palloc(sizeof(Point));

new\_point->x = pointx->x;

new\_point->y = pointy->y;

PG\_RETURN\_POINT\_P(new\_point);

}

/\* 传引用，变长 \*/

PG\_FUNCTION\_INFO\_V1(copytext);

Datum

copytext(PG\_FUNCTION\_ARGS)

{

text \*t = PG\_GETARG\_TEXT\_PP(0);

/\*

\* VARSIZE\_ANY\_EXHDR是该结构的尺寸（以字节为单位）减去其头部的

\* VARHDRSZ或VARHDRSZ\_SHORT。用一个完整长度的头部构建该拷贝。

\*/

text \*new\_t = (text \*) palloc(VARSIZE\_ANY\_EXHDR(t) + VARHDRSZ);

SET\_VARSIZE(new\_t, VARSIZE\_ANY\_EXHDR(t) + VARHDRSZ);

/\*

\* VARDATA是指向新结构的数据区域的指针。来源可以是一个短数据，

\* 所以要通过VARDATA\_ANY检索它的数据。

\*/

memcpy((void \*) VARDATA(new\_t), /\* 目标 \*/

(void \*) VARDATA\_ANY(t), /\* 源头 \*/

VARSIZE\_ANY\_EXHDR(t)); /\* 多少字节 \*/

PG\_RETURN\_TEXT\_P(new\_t);

}

PG\_FUNCTION\_INFO\_V1(concat\_text);

Datum

concat\_text(PG\_FUNCTION\_ARGS)

{

text \*arg1 = PG\_GETARG\_TEXT\_PP(0);

text \*arg2 = PG\_GETARG\_TEXT\_PP(1);

int32 arg1\_size = VARSIZE\_ANY\_EXHDR(arg1);

int32 arg2\_size = VARSIZE\_ANY\_EXHDR(arg2);

int32 new\_text\_size = arg1\_size + arg2\_size + VARHDRSZ;

text \*new\_text = (text \*) palloc(new\_text\_size);

SET\_VARSIZE(new\_text, new\_text\_size);

memcpy(VARDATA(new\_text), VARDATA\_ANY(arg1), arg1\_size);

memcpy(VARDATA(new\_text) + arg1\_size, VARDATA\_ANY(arg2), arg2\_size);

PG\_RETURN\_TEXT\_P(new\_text);

}

假定上述代码已经准备在文件funcs.c中并且被编译成一个共享对象，我们可以用这样的命令在Highgo Database中定义函数：

CREATE FUNCTION add\_one(integer) RETURNS integer

AS 'DIRECTORY/funcs', 'add\_one'

LANGUAGE C STRICT;

\-- 注意SQL函数名”add\_one”的重载

CREATE FUNCTION add\_one(double precision) RETURNS double precision

AS 'DIRECTORY/funcs', 'add\_one\_float8'

LANGUAGE C STRICT;

CREATE FUNCTION makepoint(point, point) RETURNS point

AS 'DIRECTORY/funcs', 'makepoint'

LANGUAGE C STRICT;

CREATE FUNCTION copytext(text) RETURNS text

AS 'DIRECTORY/funcs', 'copytext'

LANGUAGE C STRICT;

CREATE FUNCTION concat\_text(text, text) RETURNS text

AS 'DIRECTORY/funcs', 'concat\_text'

LANGUAGE C STRICT;

这里，DIRECTORY表示共享库文件的目录（例如Highgo Database的教程目录，它包含这一节中用到的例子的代码）。（更好的风格是先把DIRECTORY放入搜索路径，在AS子句中只使用'funcs'。在任何情况下，我们可以为一个共享库省略系统相关的扩展名，通常是.so）。

注意我们已经把函数指定为”strict”，这意味着如果有任何输入值为空，系统应该自动假定得到空结果。通过这种做法，我们避免在函数代码中检查空值输入。如果不这样做，我们必须使用PG\_ARGISNULL()明确地检查空值输入。

乍一看，版本-1编码习惯好像是在使用普通C调用约定之上的无意义的愚民政策。不过，它们确实允许处理可为NULL的参数/返回值以及被”TOAST”过（压缩或者线外）的值。

宏PG\_ARGISNULL(n)允许一个函数测试是否每一个输入为空（当然，只需要在没有声明为”strict”的函数中这样做）。和PG\_GETARG\_xxx()宏一样，输入参数也是从零开始计数。注意应该在验证了一个参数不是空之后才执行PG\_GETARG\_xxx()。要返回一个空结果，应执行PG\_RETURN\_NULL()，它对严格的以及非严格的函数都有用。

在版本-1接口中提供的其他选项是PG\_GETARG\_xxx()宏的两个变种。其中的第一种是PG\_GETARG\_xxx\_COPY()，它确保返回的指定参数的拷贝可以被安全地写入（通常的宏有时会返回一个指向表中物理存储的值，它不能被写入。使用PG\_GETARG\_xxx\_COPY()宏可以保证得到一个可写的结果）。第二种变种PG\_GETARG\_xxx\_SLICE()宏有三个参数。第一个是函数参数的编号（如上文）。第二个和第三个是要被返回的段的偏移量和长度。偏移量从零开始计算，而负值的长度则表示要求返回该值的剩余部分。当大型值的存储类型为”external”时，这些宏提供了访问这些大型值的更有效的方法（列的存储类型可以使用ALTER TABLE tablename ALTER COLUMN colname SET STORAGE storagetype来指定。storagetype取plain、external、extended或者main）。

最后，版本-1 的函数调用规范可以返回集合结果（ 第6.10.8节 ）、实现触发器函数(第7章)和过程语言调用处理器。更多细节可见源代码发布中的src/backend/utils/fmgr/README。

### 编写代码

在开始更高级的话题之前，我们应该讨论一下用于 Highgo Database C 语言函数的编码规则。虽然可以把不是 C 编写的函数载入到Highgo Database中，这通常是很困难的，因为其他语言（例如 C++、FORTRAN 或者 Pascal）通常不会遵循和 C 相同的调用规范。也就是说，其他语言不会以同样的方式在函数之间传递参数以及返回值。由于这个原因，我们会假定你的 C 语言函数确实是用 C 编写的。

编写和编译 C 函数的基本规则如下：

• 使用pg\_config --includedir-server 找出Highgo Database服务器头文件安装在系统的哪个位置。

• 编译并且链接你的代码（这样它就能被动态载入到Highgo Database中）总是要求特殊的标志。对特定的操作系统的做法 详见 。

• 记住为你的共享库按 第6.10.1节 中所述 定义一个”magic block”。

• 在分配内存时，使用Highgo Database函数 palloc和 pfree， 而不是使用对应的 C 库函数 malloc和free。在每个事务结束时会自动释放通过palloc 分配的内存，以免内存泄露。

• 总是要使用memset把你的结构中的字节置零（或者 最开始就用palloc0分配它们）。即使你对结构中的每个域都赋值，也可能有对齐填充（结构中的空洞）包含着垃圾值。 如果不这样做，很难支持哈希索引或哈希连接，因为你必须选出数据结构中有意义的位进行哈希计算。规划器有时也依赖于用按位相等来比较常量，因此如果逻辑等价的值不是按位相等的会导致出现不想要的规划结果。

• 大部分的内部Highgo Database类型 都声明在postgres.h中，不过函数管理器接口（PG\_FUNCTION\_ARGS等）在fmgr.h中，因此你将需要包括至少这两个文件。

为了移植性，最好在包括任何其他系统或者用户头文件之前，先包括postgres.h。包括postgres.h也将会为你包括 elog.h和palloc.h。

• 对象文件中定义的符号名不能相互冲突或者与Highgo Database服务器可执行程序中定义的符号冲突。如果出现有关于此的错误消息，你将必须重命名你的函数或者变量。

### 编译和链接动态载入的函数

在使用C编写的瀚高数据库扩展函数之前，必须以一种特殊的方式编译并且链接它们，以便产生一个能被服务器动态载入的文件。简而言之，需要创建一个共享库。

超出本节所含内容之外的信息请参考你的操作系统文档，特别是 C 编译器（cc）和链接编辑器（ld）的手册页。另外，瀚高数据库源代码的contrib目录中包含了一些可以工作的例子。但是，如果你依靠这些例子，也会使你的模块依赖于瀚高数据库源码的可用性。

创建共享库通常与链接可执行文件相似：首先源文件被编译成对象文件，然后对象文件被链接起来。对象文件需要被创建为独立位置代码（PIC），，这在概念上意味着当它们被可执行文件载入时，它们可以被放置在内存中的任意位置（用于可执行文件的对象文件通常不会以那种方式编译）。链接一个共享库的命令会包含特殊标志来把它与链接一个可执行文件区分开（至少在理论上 — 在某些系统上实际上很丑陋）。

在下列例子中，我们假定你的源代码在一个文件foo.c中，并且我们将创建一个共享库foo.so。除非特别注明，中间的对象文件将被称为foo.o。一个共享库能包含多于一个对象文件，但是我们在这里只使用一个。

FreeBSD

用来创建PIC的编译器标志是-fPIC。要创建共享库，编译器标志是-shared。

gcc -fPIC -c foo.c

gcc -shared -o foo.so foo.o

这适用于FreeBSD从 3.0 开始的版本。

HP-UX

该系统编译器创建PIC的编译器标志是+z。当使用GCC自己的-fPIC时。用于共享库的链接器标志是-b。因此：

cc +z -c foo.c

或者：

gcc -fPIC -c foo.c

并且然后：

ld -b -o foo.sl foo.o

和大部分其他系统不同，HP-UX为共享库使用扩展.sl。

Linux

创建PIC的编译器标志是-fpic。创建一个共享库的编译器标志是-shared。一个完整的例子看起来像：

cc -fPIC -c foo.c

cc -shared -o foo.so foo.o

macOS

这里是一个例子。它假定安装了开发者工具。

cc -c foo.c

cc -bundle -flat\_namespace -undefined suppress -o foo.so foo.o

NetBSD

创建PIC的编译器标志是-fPIC。对于ELF系统，带着标志-shared的编译器被用来链接共享库。在旧的非 ELF 系统上，ld -Bshareable会被使用。

gcc -fPIC -c foo.c

gcc -shared -o foo.so foo.o

OpenBSD

创建PIC的编译器标志是-fPIC。ld -Bshareable被用来链接共享库。

gcc -fPIC -c foo.c

ld -Bshareable -o foo.so foo.o

Solaris

创建PIC的编译器标志是-KPIC（用于 Sun 编译器）以及-fPIC（用于GCC）。要链接共享库，编译器选项对几种编译器都是-G或者是对GCC使用-shared。

cc -KPIC -c foo.c

cc -G -o foo.so foo.o

或

gcc -fPIC -c foo.c

gcc -G -o foo.so foo.o

| 提示： |
| --- |
| 如果这对你来说太复杂，你应该考虑使用 GNU Libtool1，它会用一个统一的接口隐藏平台差异。 |

结果的共享库文件接着就可以被载入到瀚高数据库。当把文件名指定给CREATE FUNCTION命令时，必须把共享库文件的名字给它，而不是中间的对象文件。注意系统的标准共享库扩展（通常是.so或者.sl）在CREATE FUNCTION命令中可以被忽略，并且通常为了最好的可移植性应该被忽略。

### 组合类型参数

组合类型没有像 C 结构那样的固定布局。组合类型的实例可能包含空值域。此外，继承层次中的组合类型可能具有和同一继承层次中其他成员不同的域。因此，瀚高数据库提供了函数接口来访问 C 的组合类型的域。

假设我们想要写一个函数来回答查询：

SELECT name, c\_overpaid(emp, 1500) AS overpaid

FROM emp

WHERE name = 'Bill' OR name = 'Sam';

如果使用版本-1的调用规范，我们可以定义 c\_overpaid为：

#include "postgres.h"

#include "executor/executor.h" /\* 用于 GetAttributeByName() \*/

PG\_MODULE\_MAGIC;

PG\_FUNCTION\_INFO\_V1(c\_overpaid);

Datum

c\_overpaid(PG\_FUNCTION\_ARGS)

{

HeapTupleHeader t = PG\_GETARG\_HEAPTUPLEHEADER(0);

int32 limit = PG\_GETARG\_INT32(1);

bool isnull;

Datum salary;

salary = GetAttributeByName(t, "salary", &isnull);

if (isnull)

PG\_RETURN\_BOOL(false);

/\* 另外，我们可能更想对空 salary 用 PG\_RETURN\_NULL() 。\*/

PG\_RETURN\_BOOL(DatumGetInt32(salary) > limit);

}

GetAttributeByName是返回指定行的属性的 Highgo Database系统函数。它有三个参数： 类型为HeapTupleHeader的传入参数、想要访问的函数名以及一个说明该属性是否为空的返回参数。GetAttributeByName返回一个Datum 值，可以把它用合适的DatumGetXXX() 宏转换成正确的数据类型。注意如果空值标志被设置，那么返回值是没有 意义的，所以在对结果做任何事情之前应该先检查空值标志。

也有GetAttributeByNum函数，它可以用目标属性的属性号而不是属性名来选择目标属性。

下面的命令声明 SQL中的c\_overpaid：

CREATE FUNCTION c\_overpaid(emp, integer) RETURNS boolean

AS 'DIRECTORY/funcs', 'c\_overpaid'

LANGUAGE C STRICT;

注意我们用了STRICT，这样我们不需要检查输入参数是否为NULL。

### 返回行（组合类型）

要从一个 C 语言函数中返回一个行或者组合类型值，你可以使用一种特殊的 API，它提供的宏和函数隐藏了大部分的构建组合数据类型的复杂性。要使用这种 API，源文件中必须包括：

#include "funcapi.h"

有两种方式可以构建一个组合数据值（以后就叫一个”元组”）： 可以从一个 Datum 值的数组构造，或者从一个 C 字符串（可被传递给该元组各列的数据类型的输入转换函数）的数组构造。在两种情况下，都首先需要为该元组的结构获得或者构造一个TupleDesc描述符。在处理Datum 时，需要把该TupleDesc传递给 BlessTupleDesc，接着为每一行调用 heap\_form\_tuple。在处理 C 字符串时，需要把该TupleDesc传递给TupleDescGetAttInMetadata，接着为每一行调用 BuildTupleFromCStrings。对于返回一个元组集合的函数， 这些设置步骤可以在第一次调用该函数时一次性完成。

有一些助手函数可以用来设置所需的TupleDesc。在大部分返回组合值的函数中推荐的方式是调用：

TypeFuncClass get\_call\_result\_type(FunctionCallInfo fcinfo,

Oid \*resultTypeId,

TupleDesc \*resultTupleDesc)

传递传给调用函数本身的同一个fcinfo结构（这当然要求使用的是版本-1 的调用规范）。resultTypeId可以被指定为NULL或者一个本地变量的地址以接收该函数的结果类型 OID。

resultTupleDesc应该是一个本地 TupleDesc变量的地址。检查结果是不是 TYPEFUNC\_COMPOSITE，如果是则 resultTupleDesc已经被用所需的 TupleDesc填充（如果不是，你可以报告一个错误，并且 返回”function returning record called in context that cannot accept type record”字样的消息）。

| 提示： |
| --- |
| get\_call\_result\_type能够解析一个多态函数结果的实际类型， 因此不仅在返回组合类型的函数中，在返回标量多态结果的函数中它也是非常 有用的。resultTypeId输出主要用于返回多态标量的函数。 |

| 注意： |
| --- |
| get\_call\_result\_type有一个兄弟 get\_expr\_result\_type，它被用来解析被表示为一棵表达式 树的函数调用的输出类型。在尝试确定来自函数外部的结果类型时可以用它。也有一个get\_func\_result\_type，当只有函数的 OID 可用时 可以用它。不过这些函数无法处理被声明为返回record的函数，并且get\_func\_result\_type无法解析多态类型，因此你 应该优先使用get\_call\_result\_type。 |

比较老的，现在已经被废弃的获得TupleDesc的函数是：

TupleDesc RelationNameGetTupleDesc(const char \*relname)

它可以为一个提到的关系的行类型得到TupleDesc， 还有：

TupleDesc TypeGetTupleDesc(Oid typeoid, List \*colaliases)

可以基于一个类型 OID 得到TupleDesc。这可以被用来为一种基础或者组合类型获得TupleDesc。不过，对于返回record的函数它不起作用，并且它无法解析多态类型。

一旦有了一个TupleDesc，如果计划处理 Datum可以调用：

TupleDesc BlessTupleDesc(TupleDesc tupdesc)

如果计划处理 C 字符串，可调用：

AttInMetadata \*TupleDescGetAttInMetadata(TupleDesc tupdesc)

如果正在编写一个返回集合的函数，你可以把这些函数的结果保存在 FuncCallContext结构中 — 分别使用 tuple\_desc或者attinmeta域。

在处理 Datum 时，使用

HeapTuple heap\_form\_tuple(TupleDesc tupdesc, Datum \*values, bool \*isnull)

来用 Datum 形式的用户数据构建一个HeapTuple。

在处理 C 字符串时，使用 HeapTuple BuildTupleFromCStrings(AttInMetadata \*attinmeta, char \*\*values)

来用 C 字符串形式的用户数据构建一个HeapTuple。 values是一个 C 字符串数组，每一个元素是返回行的一个属性。每一个 C 字符串应该是该属性数据类型的输入函数所期望的格式。为了对一个属性返回空值，values数组中对应的指针应该被设置为NULL。对于你返回的每一行都将再次调用这个函数。

一旦已经构建了一个要从函数中返回的元组，它必须被转换成一个Datum。使用 HeapTupleGetDatum(HeapTuple tuple)可把一个HeapTuple转换成合法的Datum。如果你只想返回一行，那么这个Datum可以被直接返回，在一个集合返回函数中它也可以被当做当前的返回值。

### 返回集合

也提供了一种特殊的API来支持从 C 语言函数中返回集合（多个行）。 集合返回函数必须遵循版本-1 的调用规范。如上文所述，源文件中还必须包括funcapi.h。

对返回的每一个项，一个集合返回函数（SRF）都会被调用一次。因此，这个SRF必须保存足够的状态来 记住它正在做什么并且在每次调用时返回下一个项。结构FuncCallContext被提供来帮助控制这个过程。在一个函数中，fcinfo->flinfo->fn\_extra被用来在多次调用中保持指向FuncCallContext的指针。

typedef struct FuncCallContext

{

/\*

\* 本次调用以前已经被调用过多少次

\*

\* SRF\_FIRSTCALL\_INIT() 会为你把 call\_cntr 初始化为 0，

\* 并且在每次调用 SRF\_RETURN\_NEXT() 时增加。

\*/

uint64 call\_cntr;

/\*

\* 可选：最大调用次数

\*

\* 这里的 max\_calls 只是为了方便，设置它是可选的。

\* 如果没有设置，你必须提供替代的方法来了解函数什么时候做完。

\*/

uint64 max\_calls;

/\*

\* 可选：指向用户提供的上下文信息的指针

\*

\* user\_fctx 是一个指向你自己的数据的指针，它可用来在函数的多次

\* 调用之间保存任意的上下文信息。

\*/

void \*user\_fctx;

/\*

\* 可选：指向包含属性类型输入元数据的结构的指针

\*

\* attinmeta 被用在返回元组（即组合数据类型）时，在返回基本数据类型

\* 时不会使用。只有想用BuildTupleFromCStrings()创建返回元组时才需要它。

\*/

AttInMetadata \*attinmeta;

/\*

\* 用于保存必须在多次调用间都存在的结构的内存上下文

\*

\* SRF\_FIRSTCALL\_INIT() 会为你设置 multi\_call\_memory\_ctx，并且由

\* SRF\_RETURN\_DONE() 来清理。对于任何需要在 SRF 的多次调用间都

\* 存在的内存来说，它是最合适的内存上下文。

\*/

MemoryContext multi\_call\_memory\_ctx;

/\*

\* 可选：指向包含元组描述的结构的指针

\*

\* tuple\_desc 被用在返回元组（即组合数据类型）时，并且只有在用

\* heap\_form\_tuple() 而不是 BuildTupleFromCStrings() 构建元组时才需要它。

\* 注意这里存储的 TupleDesc 指针通常已经被先运行过 BlessTupleDesc()。

\*/

TupleDesc tuple\_desc;

} FuncCallContext;

SRF使用一些自动操纵FuncCallContext （并且期望通过fn\_extra找到它）的函数和宏。可使用：

SRF\_IS\_FIRSTCALL()

来判断你的函数是否是第一次被调用。在第一次调用时（只能在第一次调用时）使用：

SRF\_FIRSTCALL\_INIT()

可初始化FuncCallContext。在每一次函数调用时（包括第一次） 可使用：

SRF\_PERCALL\_SETUP()

为使用FuncCallContext做适当的设置并且清除上一次 留下来的任何已返回的数据。

如果你的函数有数据要返回，可使用：

SRF\_RETURN\_NEXT(funcctx, result)

把它返回给调用者（result必须是类型Datum， 可以是一个单一值或者按上文所述准备好的元组）。最后，当函数完成了 数据返回后，可使用：

SRF\_RETURN\_DONE(funcctx)

来清理并且结束SRF。

SRF被调用时的当前内存上下文被称作一个瞬时上下文， 在两次调用之间会清除它。这意味着你不必对用palloc 分配的所有东西调用pfree，它们将自动被释放。不过， 如果你想要分配任何需要在多次调用间都存在的数据结构，需要把它们放在其他地方。对于任何需要在SRF结束运行之前都存在的数据来说，multi\_call\_memory\_ctx引用的内存上下文是一个合适的位置。在大部分情况中，这意味着应该在做第一次调用设置时就切换到multi\_call\_memory\_ctx中。

| 警告： |
| --- |
| 虽然函数的实参在多次调用之间保持不变，但如果在瞬时上下文中 反 TOAST了参数（通常由 PG\_GETARG\_xxx 宏完成），那么被反 TOAST 的拷贝将在每次循环中被释放。相应地，如果你把这些值的引用保存在user\_fctx中，你也必须在反 TOAST 之后把它们拷贝到 multi\_call\_memory\_ctx中，或者确保你只在那个上下文中反 TOAST 这些值。 |

一个完整的伪代码例子：

Datum

my\_set\_returning\_function(PG\_FUNCTION\_ARGS)

{

FuncCallContext \*funcctx;

Datum result;

further declarations as needed

if (SRF\_IS\_FIRSTCALL())

{

MemoryContext oldcontext;

funcctx = SRF\_FIRSTCALL\_INIT();

oldcontext = MemoryContextSwitchTo(funcctx->multi\_call\_memory\_ctx);

/\* 这里是一次性设置代码： \*/

user code

if returning composite

build TupleDesc, and perhaps AttInMetadata

endif returning composite

user code

MemoryContextSwitchTo(oldcontext);

}

/\* 这里是每一次都要做的设置代码： \*/

user code

funcctx = SRF\_PERCALL\_SETUP();

user code

/\* 这里只是一种测试是否执行完的方法： \*/

if (funcctx->call\_cntr < funcctx->max\_calls)

{

/\* 这里返回另一个项： \*/

user code

obtain result Datum

SRF\_RETURN\_NEXT(funcctx, result);

}

else

{

/\* 这里已经完成了项的返回并且需要进行清理： \*/

user code

SRF\_RETURN\_DONE(funcctx);

}

}

一个返回组合类型的简单SRF的完整例子：

PG\_FUNCTION\_INFO\_V1(retcomposite);

Datum

retcomposite(PG\_FUNCTION\_ARGS)

{

FuncCallContext \*funcctx;

int call\_cntr;

int max\_calls;

TupleDesc tupdesc;

AttInMetadata \*attinmeta;

/\* 只在第一次函数调用时做的事情 \*/

if (SRF\_IS\_FIRSTCALL())

{

MemoryContext oldcontext;

/\* 创建一个函数上下文，让它在多次调用间都保持存在 \*/

funcctx = SRF\_FIRSTCALL\_INIT();

/\* 切换到适合多次函数调用的内存上下文 \*/

oldcontext = MemoryContextSwitchTo(funcctx->multi\_call\_memory\_ctx);

/\* 要返回的元组总数 \*/

funcctx->max\_calls = PG\_GETARG\_UINT32(0);

/\* 为结果类型构造一个元组描述符 \*/

if (get\_call\_result\_type(fcinfo, NULL, &tupdesc)!= TYPEFUNC\_COMPOSITE)

ereport(ERROR,

(errcode(ERRCODE\_FEATURE\_NOT\_SUPPORTED),

errmsg("function returning record called in context "

"that cannot accept type record")));

/\*

\* 生成后面需要用来从原始 C 字符串产生元组的属性元数据

\*/

attinmeta = TupleDescGetAttInMetadata(tupdesc);

funcctx->attinmeta = attinmeta;

MemoryContextSwitchTo(oldcontext);

}

/\* 在每一次函数调用都要完成的事情 \*/

funcctx = SRF\_PERCALL\_SETUP();

call\_cntr = funcctx->call\_cntr;

max\_calls = funcctx->max\_calls;

attinmeta = funcctx->attinmeta;

if (call\_cntr < max\_calls) /\* 如果还有要发送的 \*/

{

char \*\*values;

HeapTuple tuple;

Datum result;

/\*

\* 为构建返回元组准备一个值数组。这应该是一个 C

\* 字符串数组，之后类型输入函数会处理它。

\*/

values = (char \*\*) palloc(3 \* sizeof(char \*));

values\[0\] = (char \*) palloc(16 \* sizeof(char));

values\[1\] = (char \*) palloc(16 \* sizeof(char));

values\[2\] = (char \*) palloc(16 \* sizeof(char));

snprintf(values\[0\], 16, "%d", 1 \* PG\_GETARG\_INT32(1));

snprintf(values\[1\], 16, "%d", 2 \* PG\_GETARG\_INT32(1));

snprintf(values\[2\], 16, "%d", 3 \* PG\_GETARG\_INT32(1));

/\* 构建一个元组 \*/

tuple = BuildTupleFromCStrings(attinmeta, values);

/\* 把元组变成 datum \*/

result = HeapTupleGetDatum(tuple);

/\* 清理（实际并不必要） \*/

pfree(values\[0\]);

pfree(values\[1\]);

pfree(values\[2\]);

pfree(values);

SRF\_RETURN\_NEXT(funcctx, result);

}

else /\* 如果没有要发送的 \*/

{

SRF\_RETURN\_DONE(funcctx);

}

}

在 SQL 中声明这个函数的一种方法是：

CREATE TYPE \_\_retcomposite AS (f1 integer, f2 integer, f3 integer);

CREATE OR REPLACE FUNCTION retcomposite(integer, integer)

RETURNS SETOF \_\_retcomposite

AS 'filename', 'retcomposite'

LANGUAGE C IMMUTABLE STRICT;

一种不同的方法是使用 OUT 参数：

CREATE OR REPLACE FUNCTION retcomposite(IN integer, IN integer,

OUT f1 integer, OUT f2 integer, OUT f3 integer)

RETURNS SETOF record

AS 'filename', 'retcomposite'

LANGUAGE C IMMUTABLE STRICT;

注意在这种方法中，函数的输出类型在形式上是一种匿名的 record类型。

源码中的目录contrib/tablefunc 下的模块包含集合返回函数更加复杂的例子。

### 多态参数和返回类型

C语言函数可以被声明为接受和返回多态类型 anyelement、anyarray、 anynonarray、 anyenum以及anyrange。关于多态函数的详细介绍 请见第 6.2.5节 。当函数参数或者返回类型被定义为多态类型时，函数的编写者无法提前知道会用什么数据类型调用该函数或者该函数需要返回什么数据类型。在fmgr.h中提供了两种例程来允许版本-1 的 C 函数发现其参数的实际数据类型以及它要返回的类型。这些例程被称为get\_fn\_expr\_rettype(FmgrInfo \*flinfo)和 get\_fn\_expr\_argtype(FmgrInfo \*flinfo, int argnum)。它们返回结果或者参数的类型的 OID，或者当该信息不可用时返回 InvalidOid。结构flinfo通常被当做 fcinfo->flinfo访问。参数argnum则是从零 开始计。get\_call\_result\_type也可被用作 get\_fn\_expr\_rettype的一种替代品。还有 get\_fn\_expr\_variadic，它可以被用来找出 variadic 参数 是否已经被合并到了一个数组中。这主要用于 VARIADIC "any"函数，因为对于接收普通数组类型的 variadic 函数来说总是会发生这类合并。

例如，假设我们想要写一个接收一个任意类型元素并且返回一个该类型的一维 数组的函数：

PG\_FUNCTION\_INFO\_V1(make\_array);

Datum

make\_array(PG\_FUNCTION\_ARGS)

{

ArrayType \*result;

Oid element\_type = get\_fn\_expr\_argtype(fcinfo->flinfo, 0);

Datum element;

bool isnull;

int16 typlen;

bool typbyval;

char typalign;

int ndims;

int dims\[MAXDIM\];

int lbs\[MAXDIM\];

if (!OidIsValid(element\_type))

elog(ERROR, "could not determine data type of input");

/\* 得到提供的元素，小心它为 NULL 的情况 \*/

isnull = PG\_ARGISNULL(0);

if (isnull)

element = (Datum) 0;

else

element = PG\_GETARG\_DATUM(0);

/\* 只有一个维度 \*/

ndims = 1;

/\* 和一个元素 \*/

dims\[0\] = 1;

/\* 且下界是 1 \*/

lbs\[0\] = 1;

/\* 得到该元素类型所需的信息 \*/

get\_typlenbyvalalign(element\_type, &typlen, &typbyval, &typalign);

/\* 现在构建数组 \*/

result = construct\_md\_array(&element, &isnull, ndims, dims, lbs,

element\_type, typlen, typbyval, typalign);

PG\_RETURN\_ARRAYTYPE\_P(result);

}

下面的命令在 SQL 中声明函数make\_array：

CREATE FUNCTION make\_array(anyelement) RETURNS anyarray

AS 'DIRECTORY/funcs', 'make\_array'

LANGUAGE C IMMUTABLE;

有一种只对 C 语言函数可用的多态变体：它们可以被声明为接受类型为 "any"的参数（注意这种类型名必须用双引号引用，因为它也是一个 SQL 保留字）。这和anyelement相似，不过它不约束不同的"any"参数为同一种类型，它们也不会帮助确定函数的结果类型。C语言函数也能声明它的第一个参数为 VARIADIC "any"。这可以匹配一个或者多个任意类型的实参（ 不需要是同一种类型）。这些参数不会像普通 variadic 函数那样被收集到一个数组中，它们将被单独传递给该函数。使用这种特性时， 必须用PG\_NARGS()宏以及上述方法来判断实参的个数和类型。还有，这种函数的用户可能希望在他们的函数调用中使用 VARIADIC关键词，以期让该函数将数组元素作为单独的参数对待。如果想要这样，在使用get\_fn\_expr\_variadic检测被标记为VARIADIC的实参之后，函数本身必须实现这种行为。

### 共享内存和 LWLock

外接程序可以在服务器启动时保留 LWLock 和共享内存。 必须通过在shared\_preload\_libraries 中指定外接程序的共享库来预先载入它。从\_PG\_init 函数中调用

void RequestAddinShmemSpace(int size)

可以保留共享内存。

通过从\_PG\_init中调用

void RequestNamedLWLockTranche(const char \*tranche\_name, int num\_lwlocks)

可以保留 LWLock。这将确保一个名为tranche\_name 的 LWLock 数组可用，该数组的长度为num\_lwlocks。 使用GetNamedLWLockTranche可得到该数组的指针。

为了避免可能的竞争情况，在连接并且初始化共享内存时，每一个后端应该使用 LWLock AddinShmemInitLock，如下所示：

static mystruct \*ptr = NULL;

if (!ptr)

{

bool found;

LWLockAcquire(AddinShmemInitLock, LW\_EXCLUSIVE);

ptr = ShmemInitStruct("my struct name", size, &found);

if (!found)

{

initialize contents of shmem area;

acquire any requested LWLocks using:

ptr->locks = GetNamedLWLockTranche("my tranche name");

}

LWLockRelease(AddinShmemInitLock);

}

### 把 C++ 用于可扩展性

尽管Highgo Database后端是用 C 编写的，只要遵循下面的指导方针也可以用 C++ 编写扩展：

• 所有被后端访问的函数必须对后端呈现一种 C 接口，然后这些 C 函数调用 C++ 函数。

例如，对后端访问的函数要求extern C 链接。对需要在后端和 C++ 代码之间作为指针传递的任何函数也要这样做。

• 使用合适的释放方法释放内存。例如，大部分后端内存是通过 palloc()分配的，所以应使用pfree() 来释放。在这种情况中使用 C++ 的delete会失败。

• 防止异常传播到 C 代码中（在所有extern C函数的顶层使用一个捕捉全部异常的块）。

即使 C++ 代码不会显式地抛出任何异常也需要这样做，因为类似内存不足等事件仍会抛出异常。任何异常都必须被捕捉并且用适当的错误传回给 C 接口。如果可能，用 –fno-exceptions 来编译 C++ 以完全消灭异常。在这种情况下，你必须在 C++ 代码中检查失败，例如检查new() 返回的 NULL。

• 如果从 C++ 代码调用后端函数，确定 C++ 调用栈值包含传统 C 风格的数据结构（POD）。这是必要的，因为后端错误会产生远距离的longjmp()，它无法正确的退回具有非 POD 对象的 C++ 调用栈。

总之，最好把 C++ 代码放在与后端交互的extern C函数之后， 并且避免异常、内存和调用栈泄露。

## 函数优化信息

默认情况下，函数只是一个”black box”，数据库系统对它的行为了解得很少。 不过，这意味着使用函数的查询执行效率可能会低于它们的能力。可以提供额外的知识帮助计划器优化函数调用。

一些基本事实可以通过CREATE FUNCTION命令中提供的声明性注释来提供。 这里面最重要的是函数的volatility category (IMMUTABLE、STABLE或 VOLATILE)；在定义函数时，要始终小心地正确指定这个。 并行安全属性(PARALLEL UNSAFE、PARALLEL RESTRICTED或PARALLEL SAFE)也必须被指定，如果你希望在并行查询中使用该函数。指定函数的估算执行开销也会有作用，和/或集返回函数估计返回的行数。不过，指定这两个事实的声明方式只允许指定常数值，而这通常是不够的。

也可以将一个planner support function 附加到SQL-可调用函数（称为target function）， 从而提供关于目标函数的知识，该函数过于复杂而无法以声明方式表示。 计划器支持函数必须写在 C 中（尽管它们的目标函数可以不是），所以这是一个高级功能，相对很少有人会使用。

计划器支持函数必须具有SQL签名

supportfn(internal) returns internal

当建立目标函数时，它通过指定SUPPORT子句附加到它的目标函数。

计划器支持函数的 API 的详细信息可以在Highgo Database源代码中的src/include/nodes/ supportnodes.h文件中找到。 这里我们提供了计划器支持函数的概述。支持函数的可能请求集合是可扩展的，所以在将来的版本中可能会有更多(功能)。

在规划期间，根据指定函数的特性，一些函数调用可以进行简化。 例如，int4mul(n, 1)可以被简化为n。 这种类型的转换可以通过计划器支持函数执行，通过它实现SupportRequestSimplify请求类型。 对于在查询解析树中找到其目标函数的每个实例，将调用支持函数。如果它发现特定的调用可以简化成某种其他窗体，它可以构建并返回表示该表达式的解析树。 这将为基于函数的操作符自动工作，非常—在刚才的示例中，n \*1也将简化为n。（但注意这只是一个例子；这个特殊的优化实际上不是标准的Highgo Database执行）。我们不保证Highgo Database在支持函数能够简化的情况下，永远不会调用目标函数。

确保简化表达式与目标函数的实际执行之间严格等效。

对于返回 boolean 的目标函数，估计使用该函数的 WHERE 子句将选择的行的比重通常会有用。这可以通过实现SupportRequestSelectivity请求类型的支持函数来完成。

如果目标函数的运行时间高度依赖于其输入，提供非固定开销估算可能很有用。这可以通过实现SupportRequestCost请求类型的支持函数来完成。

对于返回集的目标函数，为提供要返回的行数的非常量估计通常很有用。这可以通过实现SupportRequestRows请求类型的支持函数来完成。

对于返回 boolean的目标函数，可以将WHERE中出现的函数调用转换为一个可索引操作符子句或多个子句。 转换的子句可能与函数的条件完全相同，或者它们可能比较弱态一些 (也就是说，它们可能接受函数条件所不接受的一些值)。在后一种情况下，索引条件被称作lossy；它仍然可用于扫描索引，但必须为索引返回的每一行执行函数调用，以看它是否真的通过WHERE条件或没有。要建立这样的条件，支持函数必须实现SupportRequestIndexCondition需求类型。

## 用户定义的聚集

瀚高数据库中的聚集函数用状态值和状态转换函数定义。也就是，一个聚集操作使用一个状态值，它在每一个后续输入行被处理时被更新。要定义一个新的聚集函数，我们要为状态值选择一种数据类型、一个状态的初始值和一个状态转换函数。状态转换函数接收前一个状态值和该聚集当前行的输入值，并且返回一个新的状态值。万一该聚集的预期结果与需要保存在运行状态之中的数据不同，还能指定一个最终函数。最终函数接受结束状态值并且返回作为聚集结果的任何东西。原则上，转换函数和最终函数只是也可以在聚集环境之外使用的普通函数（实际上，通常出于性能的原因，会创建特殊的只能作为聚集的一部分工作的转换函数）。

因此，除了该聚集的用户所见的参数和结果数据类型之外，还有一种可能不同于参数和结果状态的内部状态值数据类型。

如果我们定义一个聚集但不使用一个最终函数，我们就得到了一个从每一行的列值计算一个运行函数的聚集。sum是这类聚集的一个例子。sum从零开始，并且总是把当前行的值加到它的运行总和上。例如，如果我们希望让一个sum聚集能工作在复数数据类型上，我们只需要该数据类型的加法函数。聚集定义是：

CREATE AGGREGATE sum (complex)

(

sfunc = complex\_add,

stype = complex,

initcond = '(0,0)'

);

我们可以这样使用：

SELECT sum(a) FROM test\_complex;

sum

\-----------

(34,53.9)

（注意我们依赖于函数重载：有多于一个名为sum的聚集，但是Highgo Database能够找出哪种sum 适用于一个类型为complex的列）。

如果没有非空输入值，上述的sum定义将返回零（初始状态值）。也许我们想要在这种情况下返回空 — SQL 标准期望sum以这种方式行事。我们可以通过忽略initcond阶段简单地做到这一点，这样初始状态值就为空。通常这表示sfunc将需要检查一个空状态值输入。但是对于sum和一些其他简单聚集（如max和min），把第一个非空输入值插入到状态变量中并且接着在第二个非空输入值上开始应用转换函数就足够了。如果初始状态值为空并且转换函数被标记为”strict”（即不为空输入调用），Highgo Database会自动这样做。

“strict”转换函数的另一点默认行为是只要碰到了一个空输入值，之前的状态值就保持不变。因此，空值会被忽略。如果你需要某些其他用于空输入的行为，不要把你的转换函数声明为 strict，而是把它编码为测试空输入并且做所需要的事情。

avg（均值）是一种更复杂的聚集例子。它要求两份运行状态：输入的总和以及输入的计数。最终结果通过将这些量相除而得到。均值是使用一个数组作为状态值的典型实现。例如，内建的avg(float8)实现看起来像：

CREATE AGGREGATE avg (float8)

(

sfunc = float8\_accum,

stype = float8\[\],

finalfunc = float8\_avg,

initcond = '{0,0,0}'

);

| 注意： |
| --- |
| float8\_accum要求一个三元素的数组，而不只是两个元素，因为它累积平方和以及输入的总和以及计数。因此它也可以被用于其他聚集函数以及avg。 |

SQL中的聚集函数调用允许用DISTINCT和ORDER BY选项控制以什么顺序把行传递给该聚集的转换函数。这些选项的实现不需要该聚集的支持函数关心。

进一步的细节可见CREATE AGGREGATE命令。

### 移动聚集模式

聚集函数可以选择性地支持移动聚集模式，这种模式允许很大程度上提高在具有移动帧起点的窗口中执行的聚集函数的速度。基本思想是在通常的”前向”转换函数之外，聚集提供一个逆向转换函数，该函数允许当行退出窗口帧时从聚集的运行状态值中移除它们的值。例如一个sum聚集使用加法作为前向转换函数，它可以使用减法作为逆向转换函数。如果没有一个逆向转换函数，每一次帧起点移动时，窗口函数机制必须重新从头计算该聚集，这会导致运行时间与输入行的数量乘以平均帧长度成比例。如果有一个逆向转换函数，运行时间只与输入行的数量成比例。

当前状态值和包含在当前状态中最早的行的聚集输入值被传递给逆向转换函数。它必须重新构建出如果给定的输入行不再被聚集（只聚集其后的行）时状态值会是什么样。这有时要求前向转换函数保存比普通聚集模式下更多的状态。因此，移动聚集模式使用一种完全不同于普通模式的实现：它有自己的状态数据类型、自己的前向转换函数以及自己的状态函数（如果需要）。如果不需要额外的状态，这些可以和普通模式的数据类型和函数相同。

作为一个例子，我们可以把上面给定的sum聚集扩展成支持移动聚集模式：

CREATE AGGREGATE sum (complex)

(

sfunc = complex\_add,

stype = complex,

initcond = '(0,0)',

msfunc = complex\_add,

minvfunc = complex\_sub,

mstype = complex,

minitcond = '(0,0)'

);

名称以m开始的参数定义移动聚集实现。除了逆向转换函数minvfunc，它们都对应于没有m的普通聚集参数。

用于移动聚集模式的前向转换函数不允许返回空值作为新状态值。如果逆向转换函数返回空值，这被当作一种指示，它表明该逆向函数无法为这个特定输入逆转状态计算，因此该聚集计算将根据当前的帧开始位置重新从头计算。这种习惯允许移动聚集模式被用在一些不适合逆转运行状态值的少数情况下。逆向转换函数在这些情况下可以”撒手不管”，然后在它能够工作的大部分情况中再出来干活。例如，一个浮点数的聚集可能会在必须从运行状态值中移除一个NaN（不是一个数字）输入时撒手不管。

在编写移动聚集支持函数时，很重要的是确保逆向转换函数能够准确地重构正确的状态值。否则会导致用不用移动聚集模式时结果中产生用户可见的差别。为一个聚集增加一个逆向转换函数的例子最初看起来很简单，但是却无法满足float4或者float8输入上的sum的要求。sum(float8)的一种未经考虑的定义可以是

CREATE AGGREGATE unsafe\_sum (float8)

(

stype = float8,

sfunc = float8pl,

mstype = float8,

msfunc = float8pl,

minvfunc = float8mi

);

但是，这个聚集可能给出与没有逆向转换函数时很不同的结果。例如，考虑

SELECT

unsafe\_sum(x) OVER (ORDER BY n ROWS BETWEEN CURRENT ROW AND 1 FOLLOWING)

FROM (VALUES (1, 1.0e20::float8),

(2, 1.0::float8)) AS v (n,x);

这个查询返回0作为它的第二个结果，而不是我们期待的1。其原因是浮点值的有限精度：

把1加到1e20还是会得到1e20，因此从中减去1e20会得到0而不是1。这是对于浮点计算的一种一般性限制，而不是Highgo Database的限制。

### 多态和可变聚集

聚集函数可以使用多态状态转换函数或最终函数，这样同样的函数能被用来实现多个聚集。

关于多态函数的解释可参见 第 6.2.5节 。更进一步，聚集函数本身可以被指定为具有多态输入类型和状态类型，允许一个聚集函数服务于多种输入数据类型。这里是一个多态聚集的例子：

CREATE AGGREGATE array\_accum (anyelement)

(

sfunc = array\_append,

stype = anyarray,

initcond = '{}'

);

这里，每一次给定聚集调用的实际状态类型是把实际输入类型作为元素的数组类型。该聚集的行为是串接所有输入成一个该类型的数组（注意：内建的聚集array\_agg提供了相似的功能，但是具有比上述定义更好的性能）。

这里是使用两种不同实际数据类型作为参数的输出：

SELECT attrelid::regclass, array\_accum(attname)

FROM pg\_attribute

WHERE attnum > 0 AND attrelid = 'pg\_tablespace'::regclass

GROUP BY attrelid;

attrelid | array\_accum

\---------------+---------------------------------------

pg\_tablespace | {spcname,spcowner,spcacl,spcoptions}

(1 row)

SELECT attrelid::regclass, array\_accum(atttypid::regtype)

FROM pg\_attribute

WHERE attnum > 0 AND attrelid = 'pg\_tablespace'::regclass

GROUP BY attrelid;

attrelid | array\_accum

\---------------+---------------------------

pg\_tablespace | {name,oid,aclitem\[\],text\[\]}

(1 row)

如上述例子所示，通常一个具有多态结果类型的聚集函数有一个多态状态类型。这是必须的，因为否则就无法有意义地声明最终函数：它会需要有一个多态结果类型但是不能有多态参数类型，CREATE FUNCTION将当场拒绝那些无法从调用中推断结果类型的函数。但是使用一个多态状态类型有时并不方便。最常见的情况是，聚集支持函数使用 C 编写并且状态类型应该被声明为internal，因为在 SQL 层面上没有与它等效的类型。为了表述这种情况，可以声明最终函数为接受额外的匹配该聚集输入参数的”dummy”参数。这种假参数总是被传递为空值，因为当最终函数被调用时没有特定的值可用。它们的唯一用途是允许一个多态最终函数的结果类型被连接到该聚集的输入类型。例如，内建聚集array\_agg的定义等效于：

CREATE FUNCTION array\_agg\_transfn(internal, anynonarray)

RETURNS internal...;

CREATE FUNCTION array\_agg\_finalfn(internal, anynonarray)

RETURNS anyarray...;

CREATE AGGREGATE array\_agg (anynonarray)

(

sfunc = array\_agg\_transfn,

stype = internal,

finalfunc = array\_agg\_finalfn,

finalfunc\_extra

);

这里，finalfunc\_extra选项指定该最终函数接收除了状态值之外，还接收对应于该聚集输入参数的额外假参数。额外的anynonarray参数允许array\_agg\_finalfn的声明成为合法。

与常规函数的习惯大致相同，可以通过把一个聚集函数的最后一个参数声明为一个VARIADIC数组，这样可以让该函数接受可变数量的参数（ 见第6.5.5 节 ）。该聚集的转换函数也必须有相同的数组类型作为它们的最后一个参数。通常这类转换函数也会被标上VARIADIC，但这不被严格要求。

| 注意： |
| --- |
| 可变聚集最容易被误用的情况是与ORDER BY选项一起使用，因为解析器无法在这样一种组合中是否给出了错误的实际参数数量。要记住在ORDER BY右侧的任何东西都是一个排序键，而不是一个聚集的参数。例如，在 SELECT myaggregate(a ORDER BY a, b, c) FROM...中，解析器将认为看到的是一个聚集函数参数和三个排序键。但是，用户可能想要的是 SELECT myaggregate(a, b, c ORDER BY a) FROM... |
| 如果myaggregate是可变的，两种调用都是合法的。 |
| 出于相同的原因，在创建具有相同名称以及不同数量的常规参数的聚集函数时一定要三思而后行。 |

### 有序集聚集

目前为止我们已经描述的聚集都是”普通”聚集。Highgo Database还支持有序集聚集，它和普通聚集在两个关键点上相区别。首先，除了对每个输入行都要计算一次的普通聚集参数之外，一个有序集聚集可以有”直接”参数，这类参数针对每次聚集操作只计算一次。其次，用于普通聚集参数的语法需要显式地为它们指定一个排序顺序。一个有续集聚集通常被用来实现一种依赖于特定行序的计算（例如排名或者百分位数），因此排序是任何调用都要求的。例如，percentile\_disc的内建定义等效于：

CREATE FUNCTION ordered\_set\_transition(internal, anyelement)

RETURNS internal...;

CREATE FUNCTION percentile\_disc\_final(internal, float8, anyelement)

RETURNS anyelement...;

CREATE AGGREGATE percentile\_disc (float8 ORDER BY anyelement)

(

sfunc = ordered\_set\_transition,

stype = internal,

finalfunc = percentile\_disc\_final,

finalfunc\_extra

);

这个聚集接受一个float8直接参数（百分位数分数）以及一个可以是任意可排序数据类型的聚集输入。它可以用来得到一个家庭收入的中位数：

SELECT percentile\_disc(0.5) WITHIN GROUP (ORDER BY income) FROM households;

percentile\_disc

\-----------------

50489

这里0.5是一个直接参数，它对于要作为一个在行之间变化的百分位数分数没有意义。

和普通聚集的情况不同，用于有序集聚集的输入行排序不是在幕后完成的，而是由该聚集的支持函数负责完成。典型的实现方法是在该聚集的状态值中保持对于一个”tuplesort”对象的引用，把到来的行输入给该对象，然后完成排序并且在最终函数中读出该数据。这种设计允许最终函数能够执行特殊操作，例如把附加的”假想”行注入到被排序的数据中。虽然用由PL/pgSQL或另一种 PL 语言编写的支持函数通常能够实现普通聚集，但是有序集聚集通常必须用 C 编写，因为它们的状态值无法用任何 SQL 数据类型来定义（在上面的例子中，注意状态值被声明为类型internal — 这很典型）。此外，由于最终函数会执行排序，后面就不能继续通过再次执行转移函数增加输入行。这意味着最终函数不是READ\_ONLY的，它必须在CREATE AGGREGATE中被声明为 READ\_WRITE，或者在可以有额外的最终函数调用利用已经排序好的状态时声明为SHAREABLE。

用于一个有序集聚集的状态转移函数接收当前状态值外加对于每一行的聚集输入值，并且返回更新后的状态值。这和普通聚集的定义相同，但是注意没有提供直接参数（如果有）。最终函数接收最后的状态值、直接参数（如果有）的值以及对应于聚集输入的空值（如果指定了finalfunc\_extra）。正如普通聚集，只有聚集是多态时finalfunc\_extra才真正有用，那时就需要额外的假参数把最终函数的结果类型连接到该聚集的输入类型。

当前，有序集聚集不能被用做窗口函数，并且因此没有必要让它们支持移动聚集模式。

### 部分聚集

可选地，一个聚集函数可以支持部分聚集。部分聚集的思想是在输入数据的不同子集上独立的运行该聚集的状态转移函数，然后把从这些子集得到的状态值组合起来产生最终的状态值，这样得到的状态值与在单次聚集操作中扫描所有输入得到的状态值相同。这种模式可以被用来进行并行聚集，用不同的工作者进程扫描表的不同部分。每一个工作者产生一个部分状态值，最后把这些部分状态值组合产生最终状态值（在未来，这种模式可能也会被用于组合在本地表和远程表上的聚集，但目前还未实现）。

为了支持部分聚集，聚集定义必须提供一个组合函数，这个函数接收两个该聚集的状态类型（表示在输入行的两个不同子集上得到的聚集结果）并且产生一个该状态类型的新值，该结果表示组合哪些聚集结果后的状态。至于来自两个集合的输入行的相对顺序则并没有指定。

这意味着通常不可能为对输入行顺序敏感的聚集定义出可用的组合函数。

作为简单的例子，通过指定组合函数为与其转移函数中相同的”两者中较大者”和”两者中较小者”比较函数，MAX和MIN聚集可以支持部分聚集。SUM聚集则只需要一个额外的函数作为组合函数（同样，组合函数与其转移函数相同，除非状态值的宽度比输入数据类型更宽）。

组合函数很像一个把状态类型值而不是底层输入类型值作为其第二个参数的转移函数。尤其是处理空值和严格函数的规则是相似的。此外，如果聚集定义指定了非空的initcond，记住那不仅会被作为每一次部分聚集运行的初始状态，还会被作为组合函数的初始状态，对每一个部分结果都会调用组合函数将部分结果组合到该初始状态中。

如果聚集的状态类型被声明为internal，则组合函数应负责在用于聚集状态值的内存上下文中分配其结果。这意味着当第一个输入为NULL时，不能简单地返回第二个输入，因为那个值将会在错误的上下文中并且将不具有足够的寿命。

当聚集的状态类型被声明为internal时，通常聚集定义提供序列化函数和反序列化函数也是合适的，这两个函数允许这样一种状态值被从一个进程复制到另一个进程。如果没有这些函数就无法执行并行聚集，并且未来的本地/远程聚集之类的应用也可能无法工作。

一个序列化函数必须接收一个单一的internal类型参数并且返回一个bytea类型的结果，它表示把状态值打包成一个平面化的字节串。反过来，反序列化函数是上述转换的逆变换。反序列化函数必须接收两个类型为bytea和internal的参数，并且返回类型为internal的结果（第二个参数没有被使用并且总是为零，它的存在是由于类型安全性的原因）。反序列化函数的结果应该直接在当前内存上下文中分配，这与组合函数的结果不同，因为它不需要长期存在。

还有一点值得提示的是关于要被并行执行的聚集，聚集本身必须被标记上PARALLEL SAFE其支持函数上的并行安全性标记不会被参考。

### 聚集的支持函数

用 C 编写的函数能够通过调用AggCheckCallContext检测它是作为聚集支持函数调用的，例如：

if (AggCheckCallContext(fcinfo, NULL))

检查这个区别的原因是当它为真时，第一个输入必须是一个临时状态值并且可以因此安全地被就地修改而不是分配一个新的副本。例子可见int8inc()（虽然聚集的转移函数总是被允许就地修改转移值，但不鼓励聚集的最终函数这样做。如果最终函数要这样做，必须在创建聚集时声明这种行为。更多细节请参考CREATE AGGREGATE）。

AggCheckCallContext的第二个参数可以被用来检索保存有聚集状态值的内存上下文。这对希望把”扩展”对象（\[见第 6.13.1 节\](#\_TOAST 考量)）用作状态值的转移函数有用。在第一次调用时，转移函数应该返回一个扩展对象，其内存上下文是聚集状态上下文的一个子节点，然后在后续的调用中都保持返回同一个扩展对象。示例请见array\_append()（array\_append()不是任意内建聚集的转移函数，但其编写的目的就是在被用作一种自定义聚集的转移函数时表现得有效）。

另一种可用于由 C 编写的聚集函数的支持例程是AggGetAggref，它返回定义该聚集调用的Aggref解析节点。这主要对有序集聚集有用，它能检查Aggref的子结构来找出它们本应实现的排序顺序。在Highgo Database源代码的orderedsetaggs.c中可以找到例子。

## 用户定义的类型

如 第6.2 节 中所述， Highgo Database能够被扩展成支持新的数据类型。这一节描述了如何定义新的基本类型，它们是被定义在SQL语言层面之下的数据类型。创建一种新的基本类型要求使用低层语言（通常是 C）实现在该类型上操作的函数。

这一节中的例子可以在源代码src/tutorial目录下的complex.sql和complex.c中找到。运行这些例子的指令可以在该目录的README文件中找到。

一种用户定义的类型必须总是具有输入和输出函数。这些函数决定该类型如何出现在字符串中（用于用户输入或者对用户的输出）以及如何在内存中组织该类型。输入函数采用一个空终止的字符串作为它的参数并且返回该类型的内部（内存）表达。输出函数采用该类型的内部表达作为参数并且返回一个空终止的字符串。如果我们想要对该类型做更多事情而不是只存储它，我们必须提供为我们想要的任何操作提供额外的实现函数。

假设我们想要定义一种类型complex，它表示复数。一种在内存中表达复数的自然的方法是下面的 C 结构：

typedef struct Complex {

double x;

double y;

} Complex;

我们将需要让它成为一种传引用类型，因为它没办法放到一个单一的Datum值中。

至于该类型的外部字符串表达，我们选择了一种字符串形式的(x,y)。

输入和输出函数通常并不难编写，特别是输出函数。但是在定义类型的外部字符串表达时，记住你必须最终为该表达编写一个完整的解析器作为你的输入函数。例如：

PG\_FUNCTION\_INFO\_V1(complex\_in);

Datum

complex\_in(PG\_FUNCTION\_ARGS)

{

char \*str = PG\_GETARG\_CSTRING(0);

double x,

y;

Complex \*result;

if (sscanf(str, " ( %lf, %lf )", &x, &y)!= 2)

ereport(ERROR,

(errcode(ERRCODE\_INVALID\_TEXT\_REPRESENTATION),

errmsg("invalid input syntax for type %s: \\"%s\\"",

"complex", str)));

result = (Complex \*) palloc(sizeof(Complex));

result->x = x;

result->y = y;

PG\_RETURN\_POINTER(result);

}

输出函数可以简单地写作：

PG\_FUNCTION\_INFO\_V1(complex\_out);

Datum

complex\_out(PG\_FUNCTION\_ARGS)

{

Complex \*complex = (Complex \*) PG\_GETARG\_POINTER(0);

char \*result;

result = psprintf("(%g,%g)", complex->x, complex->y);

PG\_RETURN\_CSTRING(result);

}

你应当让输入和输出函数互为彼此的逆函数。如果不这样做，当你需要把数据转储到一个文件并且以后将它重新读入时会遇到很严重的问题。在涉及到浮点数时这是一个特别常见的问题。

可选地，一种用户定义的类型可以提供二进制输入和输出例程。二进制 I/O 通常比文本 I/ O 更快但是可移植性更差。与文本 I/O 一样，定义准确的外部二进制表达是你需要负责的工作。大部分的内建数据类型都尝试提供一种不依赖机器的二进制表达。对于complex，我们的工作将建立在为类型float8提供的二进制 I/O 转换器上：

PG\_FUNCTION\_INFO\_V1(complex\_recv);

Datum

complex\_recv(PG\_FUNCTION\_ARGS)

{

StringInfo buf = (StringInfo) PG\_GETARG\_POINTER(0);

Complex \*result;

result = (Complex \*) palloc(sizeof(Complex));

result->x = pq\_getmsgfloat8(buf);

result->y = pq\_getmsgfloat8(buf);

PG\_RETURN\_POINTER(result);

}

PG\_FUNCTION\_INFO\_V1(complex\_send);

Datum

complex\_send(PG\_FUNCTION\_ARGS)

{

Complex \*complex = (Complex \*) PG\_GETARG\_POINTER(0);

StringInfoData buf;

pq\_begintypsend(&buf);

pq\_sendfloat8(&buf, complex->x);

pq\_sendfloat8(&buf, complex->y);

PG\_RETURN\_BYTEA\_P(pq\_endtypsend(&buf));

}

一旦我们编写了 I/O 函数并且把它们编译到了一个共享库中，我们就可以在 SQL 中定义complex类型。首先我们把它声明为一种 shell 类型：

CREATE TYPE complex;

这个语句的作用是为要定义的类型创建了一个占位符，这样允许我们在定义其 I/O 函数时引用该类型。现在我们可以定义 I/O 函数：

CREATE FUNCTION complex\_in(cstring)

RETURNS complex

AS 'filename'

LANGUAGE C IMMUTABLE STRICT;

CREATE FUNCTION complex\_out(complex)

RETURNS cstring

AS 'filename'

LANGUAGE C IMMUTABLE STRICT;

CREATE FUNCTION complex\_recv(internal)

RETURNS complex

AS 'filename'

LANGUAGE C IMMUTABLE STRICT;

CREATE FUNCTION complex\_send(complex)

RETURNS bytea

AS 'filename'

LANGUAGE C IMMUTABLE STRICT;

最后，我们可以提供该数据类型的完整定义：

CREATE TYPE complex (

internallength = 16,

input = complex\_in,

output = complex\_out,

receive = complex\_recv,

send = complex\_send,

alignment = double

);

在定义了一种新的基本类型后， Highgo Database会自动提供对这种类型的数组支持。数组类型通常具有和基本类型相同的名称以及一个前置的下划线字符（\_）。

一旦数据类型存在，我们就能够声明额外的函数来提供在该数据类型上有用的操作。然后可以在函数之上定义操作符，并且如果需要，可以创建操作符类来支持对该数据类型进行索引。这些额外的内容会在下面的小节中讨论。

如果数据类型的内部表达是可变长的，则内部表达必须遵循可变长数据的标准布局： 头四个字节必须是一个char\[4\]域，它从来不会被直接访问（通常 被称为vl\_len\_）。你必须使用SET\_VARSIZE() 宏在这个域中存储整个数据的尺寸（包括长度域本身），并且使用VARSIZE()来检索它（这些宏之所以存在，是因为长度域 可能会根据平台来进行解码）。

更多细节请见CREATE TYPE命令的描述。

### TOAST 考量

如果你的数据类型值的尺寸（内部形式）是可变的，更适合让该数据类型变成可 TOAST的。即便值总是很小不会被压缩或者线外存储你也应该这样做，因为TOAST也能通过减少头部负荷来为小数据减少空间。

为了支持TOAST存储，在该数据类型上操作的 C 函数必须总是要使用PG\_DETOAST\_DATUM解包任何交给它们的被 TOAST 过的值（习惯上这些细节都通过定义类型相关的GETARG\_DATATYPE\_P宏隐藏起来）。然后，在运行CREATE TYPE命令时，指定内部长度为variable并且选择某个不是plain的适当的存储选项。

如果数据对齐无关紧要（不管是为一个特定函数或者因为数据类型指定了字节对齐），那么有可能避免PG\_DETOAST\_DATUM的一些开销。你可以转而使用PG\_DETOAST\_DATUM\_PACKED（习惯上通过定义一个GETARG\_DATATYPE\_PP宏隐藏）并且使用宏VARSIZE\_ANY\_EXHDR以及VARDATA\_ANY来访问一个可能包装过的数据。此外，即使数据类型定义指定了一种对齐方式，这些宏返回的数据也不是对齐过的。如果对齐对你很重要，你必须使用常规的PG\_DETOAST\_DATUM接口。

| 注意： |
| --- |
| 老的代码经常声明vl\_len\_为一个int32域而不是char\[4\]。只要结构定义含有其他具有至少int32对齐的域，这就是 OK 的。但是在使用可能未对齐的数据时，使用这样一种结构定义就是危险的，编译器可能会把它当作一个授权来假定数据实际上已经被对齐，在对于对齐很严格的架构上会导致核心转储。 |

TOAST支持带来的另一个特性是能够拥有一种 扩展内存中数据表达，它比存储在磁盘上的格式使用起来更方便。 常规的或者”扁平的” varlena 存储格式最终只是一堆字节，它不能包含指针，因为它可能会被复制到内存中的其他位置。对于复杂数据类型，扁平格式使用起来可能代价更高，因此Highgo Database提供了一种方式把扁平格式”扩展”成更适合计算的一种表达，然后在该数据类型的函数之间传递这种在内存中的格式。

要使用扩展存储，数据类型必须遵循src/include/utils/expandeddatum.h 中给定的规则定义一种扩展的格式，并且提供函数把扁平的 varlena 值”扩展” 到该格式以及从该格式”扁平化”回常规的 varlena 表达。然后确保所有该数据类型的 C 函数都能接受这两种表达（可能通过一接收到其中一种就立刻转换成另一种来做到）。这不要求一次性修改所有该数据类型的现有函数，因为标准的PG\_DETOAST\_DATUM宏可以把扩展输入转换成常规扁平格式。因此，现有的用于扁平 varlena 格式的函数仍然能够用于扩展输入（虽然效率略低）。它不需要被转换，直到需要提高性能。

直到如何对付扩展表达的 C 函数通常分为两类：只能处理扩展格式的，以及 能同时处理扩展或扁平 varlena 输入的。前者更容易编写，但是可能总体效率较低，因为由单个函数将一种扁平输入转换为扩展的形式的开销可能会超过在扩展格式上操作所节省的开销。在只需要处理扩展格式时，可以把扁平输入到扩展形式的转换隐藏在一个参数获取宏中，这样该函数就显得不比处理传统 varlena 输入的函数更复杂了。要处理两种类型的输入，需要编写一个参数获取函数来反 TOAST 外部、短头部以及压缩的 varlena 输入，但不需要处理扩展输入。这样一个函数可以被定义为返回一个指向由扁平 varlena 格式和扩展格式组成的联合的指针。调用者可以使用 VARATT\_IS\_EXPANDED\_HEADER()宏来判断它们接收到的是哪种格式。

TOAST机制不仅允许把常规 varlena 值同扩展值区分开来，还能区分指向扩展值的”read-write”和”read-only” 指针。只需要检查扩展值或者只会以安全的并且非语义可见的方式更改扩展值的 C 函数不需要关心它们收到的是哪种类型的指针。如果收到一个读写指针，要为输入值产生一个修改版本的 C 函数将被允许就地修改该扩展输入值，但是如果它们收到的是一个只读指针则不能修改，在这种情况下它们不得不先复制该值产生一个用于修改的新值。构建了新扩展值的 C 函数应该总是返回一个指向该值的读写指针。还有，如果一个就地修改读写扩展值的 C 函数中途失败，它应该负责让该值处于一种正常的状态。

## 用户定义的操作符

对于一个完成实际工作的底层函数的调用来说，每一个操作符都是”语法糖”，因此在创建操作符之前你必须先创建底层函数。不过，一个操作符不只是语法糖，因为它携带了额外的信息来帮助查询规划器优化使用该操作符的查询。下一节将致力于解释这些额外信息。

瀚高数据库支持左一元、右一元和二元操作符。操作符可以被重载，也就是说相同的操作符名称可以被用于具有不同操作数数量和类型的操作符。在执行一个查询时，系统会根据提供的操作数的数量和类型决定要调用的操作符。

这里有一个创建用于对两个复数做加法的操作符的例子。我们假设我们已经创建了类型complex（见第 6.13 节）的定义。首先我们需要一个函数做这个加法，然后我们可以定义该操作符：

CREATE FUNCTION complex\_add(complex, complex)

RETURNS complex

AS 'filename', 'complex\_add'

LANGUAGE C IMMUTABLE STRICT;

CREATE OPERATOR + (

leftarg = complex,

rightarg = complex,

function = complex\_add,

commutator = +

);

现在我们可以执行一个这样的查询：

SELECT (a + b) AS c FROM test\_complex;

c

\-----------------

(5.2,6.05)

(133.42,144.95)

这里我们已经展示了如何创建一个二元操作符。要创建一元操作符，只要忽略leftarg（左一元）和rightarg（右一元）之一即可。在CREATE OPERATOR中只要求procedure子句和参数子句。例子中展示的commutator子句是一个可选的子句，它被用作一个查询优化器使用的提示。有关commutator以及其他优化器提示的细节出现在下一小节中。

## 操作符优化信息

一个瀚高数据库的操作符定义能够包括几种可选的子句，它们可以把有关操作符行为的有用的事情告诉系统。只要合适就应该提供这些子句，因为它们能够为使用该操作符的查询带来可观的速度提升。但是如果你提供了它们，你必须确保它们是正确的！不正确地使用一个优化子句可能导致很慢的查询、错误的输出或者其他不好的事情。如果你没有把握你可以总是省去优化子句，这样做的唯一后果是查询会比正常的速度慢。

还可以将计划器支持的函数附加到作为操作符基础的函数中，从而提供另一种向系统讲述操作符行为的方法。更多信息参见第6.11 节.

### COMMUTATOR

如果提供了COMMUTATOR子句，它指定一个操作符作为被定义的操作符的交换子。如果对于所有可能输入的 x、y 值， (x A y) 等于 (y B x)，我们可以说操作符 A 是操作符 B 的交换子。注意，B 也是 A 的交换子。例如，用于一种特定数据类型的操作符 < 和 > 通常互为交换子，并且操作符 + 通常和它本身是交换的。但是操作符 - 通常不能与任何东西交换。

一个可交换操作符的左操作数类型与其交换子的右操作数类型相同，反之亦然。因此要查找交换子，只需要给数据库该交换子操作符的名称即可，并且在COMMUTATOR子句中也只需要提供它的名称。

为将要在索引和连接子句中使用的操作符提供交换子信息是很关键的，因为这允许查询优化器把这样一个子句”翻转”成不同计划类型所需的形式。例如，考虑一个这样的 WHERE 子句tab1.x = tab2.y，其中tab1.x和tab2.y是一种用户定义的类型，并且假设tab2.y被索引。

除非优化器能决定如何把该子句翻转成tab2.y = tab1.x，否则它无法产生一个索引扫描，因为索引扫描机制期望看到被索引列出现在被给出的操作符的左边。数据库将无法简单地假定有一个可用的变换 — =操作符的创建者必须指定它是合法的（通过为该操作符标记交换子信息）。

在你定义一个子交换的操作符时，你这样做就行了。自拟定义一堆交换的操作符时，事情有一点棘手：如何在没有定义第二个操作符时完成第一个操作符的定义？因为第一个操作符需要第二个操作符作为其交换子。对这个问题有两种解决方案：

• 一种方法是忽略你定义的第一个操作符的COMMUTATOR子句，并且然后在第二个操作符的定义中提供第一个操作符作为交换子。由于数据库知道交换的操作符是成对出现的，当它看到第二个定义时它将自动回去并且填上第一个定义中缺失的COMMUTATOR子句。

• 另一种更直接的方法是就在两个定义中包括COMMUTATOR子句。当数据库处理第一个定义并且意识到COMMUTATOR引用了一个不存在的操作符时，系统将为那个操作符在系统目录中创造一个虚拟项。这个虚拟项只有操作符名称、左右操作数类型和结果类型的数据，因为这些是数据库在此时能够推断出来的所有东西。第一个操作符的目录项将会链接到这个虚拟项。稍后，当你定义第二个操作符时，系统用来自第二个定义的额外信息更新那个虚拟项。如果你尝试在虚拟操作符还未被填充之前使用它，你将只会得到一个错误消息。

### NEGATOR

如果提供了NEGATOR子句，它指定一个操作符是正在被定义的操作符的求反器。如果操作符 A 和 B 都返回布尔结果并且对于所有可能的 x、y 输入都有 (x A y) 等于 NOT (x B y)，那么我们可以说 A 是 B 的求反器。注意 B 也是 A 的求反器。例如，< 和 >= 就是大部分数据类型的一对求反器。一个操作符不可能是它自身的求反器。

与交换子不同，一对一元操作符可以合法地被标记为对方的求反器。这意味着对于所有 x 有 (A x) 等于 NOT (B x)，或者对右一元操作符也相似。

一个操作符的求反器必须具有和被定义的操作符相同的左或右操作数类型，因此正如COMMUTATOR一样，NEGATOR子句中只需要给出操作符的名称即可。

提供一个求反器对查询优化器非常有帮助，因为它允许NOT (x = y)这样的表达式被简化为x <> y。这可能比你想象的更多地发生，因为NOT操作可能会被作为其他调整的结果被插入。

求反器对的定义可以使用与定义交换子对相同的方法来完成。

### RESTRICT

如果提供了RESTRICT子句，它为该操作符指定一个限制选择度估计函数（注意这是一个函数名而不是一个操作符名）。RESTRICT子句只对返回boolean的二元操作符有意义。一个限制选择度估计器背后的思想是猜测一个表中有多大比例的行对于当前的操作符和一个特定的常数值将会满足一个

column OP constant

形式的WHERE子句条件。这能通过告知优化器具有这种形式的WHERE子句将会消除掉多少行来协助它的工作（你可能会好奇，如果常数位于左部会发生什么？好吧，COMMUTATOR就是干这个的）。

编写一个新的限制选择度估算函数已经超出了本章的范围，但是幸运地是你通常可以将系统的一个标准估算器用于很多你自己的操作符。标准的限制估算器有：

eqsel用于=

neqsel用于<>

scalarltsel用于<

scalarlesel用于<=

scalargtsel用于>

scalargesel用于>=

你能经常成功地为具有非常高或者非常低选择度的操作符使用eqsel或neqsel，即使它们实际上并非相等或不相等。例如，近似相等几何操作符使用eqsel的前提是假定它们通常只匹配表中的一小部分项。

你可以使用scalarltsel、scalarlesel、scalargtsel以及scalargesel来比较被转换为数字标量进行范围比较具有意义的数据类型。如果可能，增加一种能被src/backend/utils/adt/ selfuncs.c中的函数convert\_to\_scalar()所理解的数据类型（最后，这个函数应该被通过pg\_type系统目录的一列所标识的针对每个数据类型的函数所替换，但是那还没有发生）。如果你没有这样做，还是能工作，但是优化器的估计将不会达到最好的效果。

有一些额外的选择度估算函数是为src/backend/utils/adt/geo\_selfuncs.c中的几何操作符设计的：areasel、positionsel和contsel。在写这份材料时，这些还只是存根，但是你可能想要使用它们（或者甚至改进它们）。

### JOIN

如果提供了JOIN子句，表示用于该操作符的一个连接选择度估计函数（注意这是一个函数名而不是一个操作符名）。JOIN子句只对返回boolean的二元操作符有意义。一个连接选择度估算器背后的思想是猜测一对表中有多大比例的行对于当前的操作符将会满足一个 table1.column1 OP table2.column2

形式的WHERE子句条件。和RESTRICT子句一样，这通过让优化器知道哪种连接序列需要做的工作最少来极大地帮助优化器。

一如既往，这一章将不会尝试解释如何编写一个连接选择度估算函数，而只是建议你在适当的时候使用一种标准估算器：

eqjoinsel用于=

neqjoinsel用于<>

scalarltjoinsel用于<

scalarlejoinsel用于<=

scalargtjoinsel用于>

scalargejoinsel用于>=

areajoinsel用于基于 2D 区域比较

positionjoinsel用于基于 2D 位置比较

contjoinsel用于基于 2D 包含比较

### HASHES

如果存在HASHES子句，它告诉系统它被许可为基于这个操作符的一个连接使用哈希连接方法。HASHES只对返回boolean的二元操作符有意义，并且实际上该操作符必须必须表达某种数据类型或数据类型对的相等。

哈希连接之下的假设是连接操作符只能对哈希到相同哈希码的左右值返回真。如果两个值被放到不同的哈希桶中，连接将根本不会比较它们，这隐式地假定该连接操作符的结果必须是假。因此，为不表示某种形式相等的操作符指定HASHES是没有意义的。在大部分情况下，只有为在两端都是相同数据类型的操作符支持哈希才有意义。不过，有时可以为两种或更多数据类型设计兼容的哈希函数，也就是说，对于”相等”的值（即使具有不同的表达）会产生相同哈希码的函数。例如，在哈希不同宽度的证书时，安排这个属性相当简单。

要被标记为HASHES，连接操作符必须出现在一个哈希索引操作符族中。当你创建该操作符时这不会被强制，因为要引用的操作符族当然不可能已经存在。但是如果这样的操作符族不存在，尝试在哈希连接中使用该操作符将在运行时失败。系统需要用该操作符族来为操作符的输入数据类型寻找数据类型相关的哈希函数。当然，在创建操作符族之前，你还必须创建合适的哈希函数。

在准备一个哈希函数时应当慎重，因为有一些方法是依赖于机器的，这样它可能无法做正确的事情。例如，如果你的数据类型是一个结构，其中可能有无用的填充位，你不能简单地把整个结构传递给hash\_any（除非你编写你自己的操作符和函数按照推荐的策略来保证未被使用的位总是为零）。另一个例子是在符合IEEE浮点标准的机器上，负数零和正数零是不同的值（不同的位模式），但是它们被定义为相等。如果一个浮点值可能包含负数零，那么需要额外的步骤来保证它产生的哈希值与正数零产生的相同。

一个可哈希连接的操作符必须拥有一个出现在同一操作符族中的交换子（如果两个操作数数据类型相同，那么就是它自身，否则是一个相关的相等操作符）。如果情况不是这样，在使用该操作符时，可能会发生规划器错误。此外，一个支持多种数据类型的哈希操作符族为数据类型的每一种组合都提供相等操作符是一个好主意（但是并不被严格要求），这会带来更好的优化。

| 注意： |
| --- |
| 一个可哈希连接的操作符底层的函数必须被标记为可交换或者稳定。如果它是不稳定的，系统将永远不会为一个哈希连接尝试使用该操作符。 |

| 注意： |
| --- |
| 如果一个可哈希连接的操作符有一个被标记为 strict 的底层函数，该函数必须也是 complete：也就是对于任意两个非空输入它应当返回真或假，从不会返回空。如果没有遵守这个规则，IN操作的哈希优化可能产生错误的结果（特别是，当依据标准的正确答案可能是空时，IN可能会返回假，或者它会产生一个错误来抱怨它没有准备会收到一个空结果）。 |

### MERGES

如果存在MERGES子句，它告诉系统它被许可为基于这个操作符的一个连接使用归并连接方法。MERGES只对返回boolean的二元操作符有意义，并且实际上该操作符必须必须表达某种数据类型或数据类型对的相等。

归并连接的思想是排序左右手表并且接着并行扫描它们。这样，两种数据类型必须能够被完全排序，并且该连接操作符必须只为落在排序顺序上”同一位置”的值对返回成功。实际上这意味着该连接操作符必须和相等的行为一样。但是只要两种不同的数据类型在逻辑上是兼容的，就能对它们使用归并连接。例如，smallint-versus-integer相等操作符就是可归并连接的。我们只需要将两种数据类型变成逻辑上兼容的序列的排序操作符。

要被标记为MERGES，该连接操作符必须作为一个btree索引操作符的相等成员出现。当你创建该操作符时，这不是强制的，因为要引用的操作符族当然可能还不存在。但是除非能找到一个匹配的操作符族，否则该操作符将不会被实际用于归并连接。MERGES标志因此扮演着一种对于规划器的提示，表示值得去寻找一个匹配的操作符族。

一个可归并连接的操作符必须拥有一个出现在同一操作符族中的交换子（如果两个操作数数据类型相同，那么就是它自身，否则是一个相关的相等操作符）。如果情况不是这样，在使用该操作符时，可能会发生规划器错误。此外，一个支持多种数据类型的btree操作符族为数据类型的每一种组合都提供相等操作符是一个好主意（但是并不被严格要求），这会带来更好的优化。

| 注意： |
| --- |
| 一个可归并连接的操作符底层的函数必须被标记为可交换或者稳定。如果它是不稳定的，系统将永远不会为一个归并连接尝试使用该操作符。 |

## 索引的接口扩展

迄今为止已经描述的过程让我们能够定义新的类型、新的函数以及新的操作符。但是，我们还不能在一种新数据类型的列上定义索引。要做这件事情，我们必须为新数据类型定义一个操作符类。在这一小节稍后的部分，我们将用一个例子阐述这部份内容：一个用于 B-树索引方法的操作符类，它以绝对值的升序存储和排序复数。

操作符类可以被分组成操作符族来体现语义兼容的类之间的联系。当只涉及到一种单一数据类型时，一个操作符类就足矣。因此我们将先把重点放在这种情况上，然后再回到操作符族。

### 索引方法和操作符类

pg\_am表为每一种索引方法都包含一行（内部被称为访问方法）。瀚高数据库中内建了对表常规访问的支持，但是所有的索引方法则是在pg\_am中描述。

一个索引方法的例程并不直接了解它将要操作的数据类型。而是由一个操作符类标识索引方法用来操作一种特定数据类型的一组操作。之所以被称为操作符类是因为它们指定的一件事情就是可以被用于一个索引的WHERE子句操作符集合（即，能被转换成一个索引扫描条件）。一个操作符类也能指定一些索引方法内部操作所需的支持函数，这些过程不能直接对应于能用于索引的任何WHERE子句操作符。

可以为相同的数据类型和索引方法定义多个操作符类。通过这种方式，可以为一种数据类型定义多个索引语义集合。例如，一个B-树索引要求在它要操作的每一种数据类型上都定义一个排序顺序。对一种复数数据类型来说，拥有一个可以根据复数绝对值排序的 B-树操作符类和另一个可以根据实数部分排序的操作符类可能会有用。典型地，其中一个操作符类将被认为是最常用的并且将被标记为那种数据类型和索引方法的默认操作符类。

相同的操作符类名称可以被用于多个不同的索引方法（例如，B-树和哈希索引方法都有名为int4\_ops的操作符类）。但是每一个这样的类都是一个独立实体并且必须被单独定义。

### 索引方法策略

与一个操作符类关联的操作符通过”策略号”标识，它被用来标识每个操作符在其操作符类中的语义。例如，B-树在键上施行了一种严格的顺序（较小到较大），因此”小于”和”大于等于”这样的操作符就是 B-树所感兴趣的。因为数据库允许用户定义操作符，不能看着一个操作符（如<和>=）的名字并且说出它是哪一种比较。取而代之的是，索引方法定义了一个”策略”集合，它们可以被看成是广义的操作符。每一个操作符类会说明对于一种特定的数据类型究竟是哪个实际的操作符对应于每一种策略以及该索引语义的解释。

B-树索引方法定义了五种策略，如下表所示。

**表 6.2 树策略**

| 操作 | 策略号 |
| --- | --- |
| 小于 | 1 |
| 小于等于 | 2 |
| 等于 | 3 |
| 大于等于 | 4 |
| 大于 | 5 |

哈希索引只支持等值比较，因此它们只使用一种策略，如下表所示。

**表 6.3 哈希策略**

| 操作 | 策略号 |
| --- | --- |
| 等于 | 1 |

GiST 索引更加灵活：它们根本没有一个固定的策略集合。取而代之的是，每一个特定 GiST操作符类的”consistency”支持例程会负责解释策略号。例如，一些内建的 GiST 索引操作符类索引二维几何对象，它们提供表 6.4中所示的”R-树”策略。其中四个是真正的二维测试（重叠、相同、包含、被包含），其中四个只考虑 X 方向，其他四个提供 Y 方向上的相同测试。

**表 6.4 GiST 二维”R-树” 策略**

| 操作 | 策略号 |
| --- | --- |
| 左参数严格地位于右参数的左边 | 1 |
| 左参数不会延伸到右参数的右边 | 2 |
| 重叠 | 3 |
| 左参数不会延伸到右参数的左边 | 4 |
| 左参数严格地位于右参数的右边 | 5 |
| 相同 | 6 |
| 包含 | 7 |
| 被包含 | 8 |
| 不会延伸到高于 | 9 |
| 严格低于 | 10 |
| 严格高于 | 11 |
| 不会延伸到低于 | 12 |

SP-GiST 索引在灵活性上与索引相似：它们没有一个固定的策略集合。取而代之的是，每一个操作符类的支持例程负责根据该操作符类的定义解释策略号。例如，被内建操作符类用于点的策略号如下表中所示。

**表 6.5 SP-GiST 点策略**

| 操作 | 策略号 |
| --- | --- |
| 左参数严格地位于右参数的左边 | 1 |
| 左参数严格地位于右参数的右边 | 5 |
| 相同 | 6 |
| 被包含 | 8 |
| 严格地低于 | 10 |
| 严格地高于 | 11 |

GIN 索引与 GiST 和 SP-GiST 索引类似，它们也没有一个固定的策略集合。取而代之的是，每一个操作符类的支持例程负责根据该操作符类的定义解释策略号。例如，被内建操作符类用于数组的策略号如下表所示。

**表 6.6 GIN 数组策略**

| 操作 | 策略号 |
| --- | --- |
| 重叠 | 1 |
| 包含 | 2 |
| 被包含 | 3 |
| 等于 | 4 |

在没有固定的策略集合这一点上，BRIN 索引和 GiST、SP-GiST 和 GIN 索引是类似的。每一个操作符类的支持函数会根据操作符类的定义解释策略编号。例如，下表中展示了内建的Minmax操作符类所使用的策略编号。

**表 6.7 BRIN 最小最大策略**

| 操作 | 策略号 |
| --- | --- |
| 小于 | 1 |
| 小于等于 | 2 |
| 等于 | 3 |
| 大于等于 | 4 |
| 大于 | 5 |

注意上文列出的所有操作符都返回布尔值。实际上，所有作为索引方法搜索操作符定义的操作符必须返回类型boolean，因为它们必须出现在一个WHERE子句的顶层来与一个索引一起使用（某些索引访问方法还支持排序操作符，它们通常不返回布尔值，这种特性在第6.16.7 节中讨论）。

### 索引方法支持例程

对于系统来说只有策略信息通常不足以断定如何使用一种索引。实际上，为了能工作，索引方法还要求额外的支持例程。例如，B-树索引方法必须能比较两个键并且决定其中一个是否大于、等于或小于另一个。类似地，哈希索引方法必须能够为键值计算哈希码。这些操作并不对应在 SQL 命令的条件中使用的操作符。它们是索引方法在内部使用的管理例程。

与策略一样，操作符类会标识哪些函数应该为一种给定的数据类型扮演这些角色以及相应的语义解释。索引方法定义它需要的函数集合，而操作符类则会通过为函数分配由索引方法说明的”支持函数号”来标识正确的函数。

如下表所示， B-树要求一个比较支持函数，并且允许在操作符类作者的选项中提供两个额外的支持函数。

**表 6.8 B-树支持函数**

| 函数 | 支持号 |
| --- | --- |
| 比较两个键并且返回一个小于零、等于零或大于零的整数，它表示第一个键小于、等于或者大于第二个键。 | 1 |
| 返回C可调用的排序支持函数的地址（可选）。 | 2 |
| 将一个测试值与一个基础值加上/减去一个偏量的结果进行比较，根据比较的结果返回 真或假（可选）。 | 3 |

如表 6.9所示，哈希索引要求一个支持函数，并且允许在操作符类作者的选项中提供第二个支持函数。

**表 6.9 哈希支持函数**

| 函数 | 支持号 |
| --- | --- |
| 为一个键计算32位哈希值。 | 1 |
| 给定一个64-位salt，计算一个键的64位哈希值。如果salt为0，结果的低32位必须匹配会由函数1计算出来的值（可选）。 | 2 |

如表 6.10所示，GiST 索引有九个支持函数，其中两个是可选的。

**表 6.10 GiST 支持函数**

| 函数 | 描述 | 支持号 |
| --- | --- | --- |
| consistent | 判断键是否满足查询修饰语 | 1 |
| union | 计算一个键集合的联合 | 2 |
| compress | 计算一个要被索引的键或值的压缩表达 | 3 |
| decompress | 计算一个压缩键的解压表达 | 4 |
| penalty | 计算把新键插入到带有给定子树键的子树中带来的罚值 | 5 |
| picksplit | 判断一个页面中的哪些项要被移动到新页面中并且计算结果页面的联合键 | 6 |
| equal | 比较两个键并且在它们相等时返回真 | 7 |
| distance | 判断键到查询值的距离（可选） | 8 |
| fetch | 为只用索引扫描计算一个压缩键的原始表达（可选） | 9 |

如表 6.11所示，SP-GiST 索引要求五个支持函数。

**表 6.11 SP-GiST 支持函数**

| 函数 | 描述 | 支持号 |
| --- | --- | --- |
| config | 提供有关该操作符类的基本信息 | 1 |
| choose | 判断如何把一个新值插入到一个内元组中 | 2 |
| picksplit | 判断如何划分一组值 | 3 |
| inner\_consistent | 判断对于一个查询需要搜索哪一个子划分 | 4 |
| leaf\_consistent | 判断键是否满足查询修饰语 | 5 |

如表 6.12所示，GIN 索引有六个支持函数，其中三个是可选的。

**表 6.12 GIN 支持函数**

| 函数 | 描述 | 支持号 |
| --- | --- | --- |
| compare | 比较两个键并且返回一个小于零、等于零或大于零的整数，它表示第一个键小于、等于或者大于第二个键。 | 1 |
| extractValue | 从一个要被索引的值中抽取键 | 2 |
| extractQuery | 从一个查询条件中抽取键 | 3 |
| consistent | 判断值是否匹配查询条件（布尔变体）（如果支持函数 6 存在则是可选的） | 4 |
| comparePartial | 比较来自查询的部分键和来自索引的键，并且返回一个小于零、等于零或大于零的数，表示 GIN 是否应该忽略该索引项、把该项当做一个匹配或者停止索引扫描（可选） | 5 |
| triConsistent | 判断值是否匹配查询条件（三元变体）（如果支持函数 4 存在则是可选的） | 6 |

如表 6.13中所示，BRIN 索引具有四个基本的支持函数。这些基本函数可能会要求提供额外的支持函数。

**表 6.13 BRIN 支持函数**

| 函数 | 描述 | 支持号 |
| --- | --- | --- |
| opcInfo | 返回描述被索引列的摘要数据的内部信息 | 1 |
| add\_value | 向一个现有的摘要索引元组增加一个新值 | 2 |
| consistent | 判断值是否匹配查询条件 | 3 |
| union | 计算两个摘要元组的联合 | 4 |

和搜索操作符不同，支持函数返回特定索引方法所期望的数据类型，例如在 B 树的比较函数中是一个有符号整数。每个支持函数的参数数量和类型也取决于索引方法。对于 B 树和哈希，比较和哈希支持函数和包括在操作符类中的操作符接收一样的输入数据类型，但是大部分 GiST、SP-GiST、GIN 和 BRIN 支持函数则不是这样。

### 一个例子

现在我们已经看过了基本思想，这里是创建一个新操作符类的例子（可以在源代码的src/ tutorial/complex.c和src/tutorial/complex.sql中找到这个例子）。该操作符类封装了以绝对值顺序排序复数的操作符，因此我们为它取名为complex\_abs\_ops。首先，我们需要一个操作符集合。定义操作符的过程已经在第 6.14 节中讨论过。对于一个 B-树上的操作符类，我们需要的操作符有：

• 绝对值小于（策略 1）

• 绝对值小于等于（策略 2）

• 绝对值等于（策略 3）

• 绝对值大于等于（策略 4）

• 绝对值大于（策略 5）

定义一个比较操作符的相关集合最不容易出错的方式是，先编写 B-树比较支持函数，然后编写该支持函数的包装器函数。这降低了极端情况下得到不一致结果的几率。遵照这种方法，我们首先编写：

#define Mag(c) ((c)->x\*(c)->x + (c)->y\*(c)->y)

static int

complex\_abs\_cmp\_internal(Complex \*a, Complex \*b)

{

double amag = Mag(a),

bmag = Mag(b);

if (amag < bmag)

return -1;

if (amag > bmag)

return 1;

return 0;

}

现在小于函数看起来像这样：

PG\_FUNCTION\_INFO\_V1(complex\_abs\_lt);

Datum

complex\_abs\_lt(PG\_FUNCTION\_ARGS)

{

Complex \*a = (Complex \*) PG\_GETARG\_POINTER(0);

Complex \*b = (Complex \*) PG\_GETARG\_POINTER(1);

PG\_RETURN\_BOOL(complex\_abs\_cmp\_internal(a, b) < 0);

}

其他四个函数的区别只在于它们如何比较内部函数的结果与 0。

接下来我们基于这些函数声明 SQL 的函数和操作符：

CREATE FUNCTION complex\_abs\_lt(complex, complex) RETURNS bool

AS 'filename', 'complex\_abs\_lt'

LANGUAGE C IMMUTABLE STRICT;

CREATE OPERATOR < (

leftarg = complex, rightarg = complex, procedure = complex\_abs\_lt,

commutator = >, negator = >=,

restrict = scalarltsel, join = scalarltjoinsel

);

指定正确的交换子和求反器操作符很重要，合适的限制和连接选择度函数也是一样，否则优化器将无法有效地利用索引。

其他值得注意的事情：

• 只能有一个操作符被命名为=且两个操作数都为类型complex。在这种要求下，我们对于complex没有任何其他操作符=。但是如果我们是在构建一种实际的数据类型，我们可能想让=成为复数的普通等值操作（不是绝对值的相等）。这样，我们需要为complex\_abs\_eq使用某种其他的操作符名称。

• 尽管瀚高数据库能够处理具有相同 SQL 名称的函数（只要它们具有不同的参数数据类型），但 C 只能处理具有给定名称一个全局函数。因此，我们不能简单地把 C 函数命名为abs\_eq之类的东西。通常，在 C 函数名中包括数据类型的名称是一种好习惯，这样就不会与其他数据类型的函数发生冲突。

• 我们可以让函数也具有abs\_eq这样的 SQL 名称，而依靠数据库通过参数数据类型来区分它和其他同名 SQL 函数。为了保持例子的简洁，我们这里让 C 级别和 SQL 级别的函数具有相同的名称。

下一步是注册 B-树所要求的支持例程。实现支持例程的 C 代码例子在包含操作符函数的同一文件中。我们这样来声明该函数：

CREATE FUNCTION complex\_abs\_cmp(complex, complex)

RETURNS integer

AS 'filename'

LANGUAGE C IMMUTABLE STRICT;

现在我们已经有了所需的操作符和支持例程，就可以最终创建操作符类：

CREATE OPERATOR CLASS complex\_abs\_ops

DEFAULT FOR TYPE complex USING btree AS

OPERATOR 1 <,

OPERATOR 2 <=,

OPERATOR 3 =,

OPERATOR 4 >=,

OPERATOR 5 >,

FUNCTION 1 complex\_abs\_cmp(complex, complex);

做好了！现在应该可以在complex列上创建并且使用 B-树索引了。

我们可以把操作符项写得更繁琐，像这样：

OPERATOR 1 < (complex, complex),

但是当操作符操作的数据类型和正在定义的操作符类所服务的数据类型相同时可以不用这么做。

上述例子假定这个新操作符类是complex数据类型的默认 B-树操作符类。如果不是这样，只需要省去关键词DEFAULT。

### 操作符类和操作符族

到目前为止，我们暗地里假设一个操作符类只处理一种数据类型。虽然在一个特定的索引列中必定只有一种数据类型，但是把被索引列与一种不同数据类型的值比较的索引操作通常也很有用。还有，如果与一种操作符类相关的扩数据类型操作符有用，通常情况是其他数据类型也有其自身相关的操作符类。在相关的类之间建立起明确的联系会很有用，因为这可以帮助规划器进行 SQL 查询优化（尤其是对于 B-树操作符类，因为规划器包含了大量有关如何使用它们的知识）。

为了处理这些需求，瀚高数据库使用了操作符族的概念。一个操作符族包含一个或者多个操作符类，并且也能包含属于该族整体而不属于该族中任何单一类的可索引操作符和相应的支持函数。我们说这样的操作符和函数是”松散地”存在于该族中，而不是被绑定在一个特定的类中。通常每个操作符类包含单一数据类型的操作符，而跨数据类型操作符则松散地存在于操作符族中。

一个操作符族中的所有操作符和函数必须具有兼容的语义，其中的兼容性要求由索引方法设定。你可能因此而奇怪为什么要这么麻烦地把族的特定子集单另出来成为操作符类，并且实际上（由于很多原因）这种划分与操作符之间没有什么直接的关联，只有操作符族才是实际的分组。定义操作符类的原因是，它们指定了特定索引对操作符族的依赖程度。如果一个索引使用着一个操作符类，那么不删除该索引是不能删除该操作符类的 — 但是操作符族的其他部分（即其他操作符类和松散的操作符）可以被删除。因此，一个操作符类应该包含一个索引在特定数据类型上正常工作所需要的最小操作符和函数集合，而相关但不关键的操作符可以作为操作符族的松散成员被加入。

例如，有一个内建的 B-树操作符族integer\_ops，它包括分别用于类型bigint (int8)、integer (int4)和smallint (int2)列上索引的操作符类int8\_ops、int4\_ops以及int2\_ops。这个族也包含跨数据类型比较操作符，它们允许对这些类型中的任意两种进行比较，这样可以通过一种类型的比较值来搜索另一种类型之上的索引。这个族可以用这些定义来重现：

CREATE OPERATOR FAMILY integer\_ops USING btree;

CREATE OPERATOR CLASS int8\_ops

DEFAULT FOR TYPE int8 USING btree FAMILY integer\_ops AS

\-- 标准 int8 比较

OPERATOR 1 <,

OPERATOR 2 <=,

OPERATOR 3 =,

OPERATOR 4 >=,

OPERATOR 5 >,

FUNCTION 1 btint8cmp(int8, int8),

FUNCTION 2 btint8sortsupport(internal),

FUNCTION 3 in\_range(int8, int8, int8, boolean, boolean);

CREATE OPERATOR CLASS int4\_ops

DEFAULT FOR TYPE int4 USING btree FAMILY integer\_ops AS

\-- 标准 int4 比较

OPERATOR 1 <,

OPERATOR 2 <=,

OPERATOR 3 =,

OPERATOR 4 >=,

OPERATOR 5 >,

FUNCTION 1 btint4cmp(int4, int4),

FUNCTION 2 btint4sortsupport(internal),

FUNCTION 3 in\_range(int4, int4, int4, boolean, boolean);

CREATE OPERATOR CLASS int2\_ops

DEFAULT FOR TYPE int2 USING btree FAMILY integer\_ops AS

\-- 标准 int2 比较

OPERATOR 1 <,

OPERATOR 2 <=,

OPERATOR 3 =,

OPERATOR 4 >=,

OPERATOR 5 >,

FUNCTION 1 btint2cmp(int2, int2),

FUNCTION 2 btint2sortsupport(internal),

FUNCTION 3 in\_range(int2, int2, int2, boolean, boolean);

ALTER OPERATOR FAMILY integer\_ops USING btree ADD

\-- 跨类型比较 int8 vs int2

OPERATOR 1 < (int8, int2),

OPERATOR 2 <= (int8, int2),

OPERATOR 3 = (int8, int2),

OPERATOR 4 >= (int8, int2),

OPERATOR 5 > (int8, int2),

FUNCTION 1 btint82cmp(int8, int2),

\-- 跨类型比较 int8 vs int4

OPERATOR 1 < (int8, int4),

OPERATOR 2 <= (int8, int4),

OPERATOR 3 = (int8, int4),

OPERATOR 4 >= (int8, int4),

OPERATOR 5 > (int8, int4),

FUNCTION 1 btint84cmp(int8, int4),

\-- 跨类型比较 int4 vs int2

OPERATOR 1 < (int4, int2),

OPERATOR 2 <= (int4, int2),

OPERATOR 3 = (int4, int2),

OPERATOR 4 >= (int4, int2),

OPERATOR 5 > (int4, int2),

FUNCTION 1 btint42cmp(int4, int2),

\-- 跨类型比较 int4 vs int8

OPERATOR 1 < (int4, int8),

OPERATOR 2 <= (int4, int8),

OPERATOR 3 = (int4, int8),

OPERATOR 4 >= (int4, int8),

OPERATOR 5 > (int4, int8),

FUNCTION 1 btint48cmp(int4, int8),

\-- 跨类型比较 int2 vs int8

OPERATOR 1 < (int2, int8),

OPERATOR 2 <= (int2, int8),

OPERATOR 3 = (int2, int8),

OPERATOR 4 >= (int2, int8),

OPERATOR 5 > (int2, int8),

FUNCTION 1 btint28cmp(int2, int8),

\-- 跨类型比较 int2 vs int4

OPERATOR 1 < (int2, int4),

OPERATOR 2 <= (int2, int4),

OPERATOR 3 = (int2, int4),

OPERATOR 4 >= (int2, int4),

OPERATOR 5 > (int2, int4),

FUNCTION 1 btint24cmp(int2, int4),

\-- 跨类型的in\_range函数

FUNCTION 3 in\_range(int4, int4, int8, boolean, boolean),

FUNCTION 3 in\_range(int4, int4, int2, boolean, boolean),

FUNCTION 3 in\_range(int2, int2, int8, boolean, boolean),

FUNCTION 3 in\_range(int2, int2, int4, boolean, boolean);

注意这种定义”重载”了操作符策略和支持函数号：每一个编号在该族中出现多次。只要一个特定编号的每一个实例都有可区分的输入数据类型，就允许这样做。输入类型等于操作符类输入类型的实例是该操作符类的主要操作符和支持函数，并且在大部分情况下应该被声明为该操作符类的一部分而不是作为操作符族的松散成员存在。

在一个 B-树操作符族中，所有该族中的操作符必须以兼容的方式排序。对该族中的每一个操作符都必须有一个与该操作符具有相同的两个输入数据类型的支持函数。我们推荐让操作符族保持完整，即对每一种数据类型的组合都应该包括所有的操作符。每个操作符类只应该包括非跨类型操作符和用于其数据类型的支持函数。

为了构建一个多数据类型的哈希操作符族，必须为该族支持的每一种数据类型创建相兼容的哈希支持函数。这里的兼容性是指这些函数对于任意两个被该族中等值操作符认为相等的值会保证返回相同的哈希码，即便这些值具有不同的类型时也是如此。当这些类型具有不同的物理表示时，这通常难以实现，但是在某些情况下是可以做到的。此外，将该操作符族中一种数据类型的值通过隐式或者二进制强制造型转换成该族中另一种数据类型时，不应该改变所计算出的哈希值。注意每种数据类型只有一个支持函数，而不是每个等值操作符一个。我们推荐让操作符族保持完整，即对每一种数据类型的组合提供一个等值操作符。每个操作符类只应该包括非跨类型等值操作符和用于其数据类型的支持函数。

GiST、SP-GiST 和 GIN 索引没有任何明显的跨数据类型操作的概念。它们所支持的操作符集合就是一个给定操作符类能够处理的主要支持函数。

在 BRIN 中，需求取决于提供操作符类的框架。对于基于minmax的操作符类，必要的行为和 B-树操作符族相同：族中的所有操作符必须以兼容的方式排序，并且转换不能改变相关的排序顺序。

### 操作符类上的系统依赖

瀚高数据库使用操作符类来以更多方式推断操作符的属性，而不仅仅是它们是否能被用于索引。因此，即便不准备对你的数据类型的列建立索引，也可能想要创建操作符类。

特别地，ORDER BY和DISTINCT等 SQL 特性要求对值的比较和排序。为了在用户定义的数据类型上实现这些特性，数据库会为数据类型查找默认 B-树操作符类。这个操作符类的”equals”成员定义了用于GROUP BY和DISTINCT的值的等值概念，而该操作符类施加的排序顺序定义了默认的ORDER BY顺序。

如果一种数据类型没有默认的 B-树操作符类，系统将查找默认的哈希操作符类。但由于这类操作符类只提供等值，所以它只能支持分组而不能支持排序。

在一种数据类型没有默认操作符类时，如果尝试对该数据类型使用这些 SQL 特性，你将得到类似”could not identify an ordering operator”（无法标识排序操作符）的错误。

通过在一个USING选项中指定一个非默认B-树操作符类的小于操作符，可以使用该操作符进行排序，例如

SELECT \* FROM mytable ORDER BY somecol USING ~<~;

或者，在USING中指定该操作符类的大于操作符可以选择升序的排序。

用户定义类型的数组的比较还依赖于该类型的默认B-树操作符类所定义的语义。如果没有默认的B-树操作符类，但有一个默认的哈希操作符类，则支持数组的相等比较，但不支持顺序的比较。

另一种要求更多数据类型相关知识的SQL特性是窗口函数（见第 4.2.8 节）的RANGE offset PRECEDING/FOLLOWING帧选项。对于这样的一个查询

SELECT sum(x) OVER (ORDER BY x RANGE BETWEEN 5 PRECEDING AND 10 FOLLOWING) FROM mytable;

不足以了解如何用x进行排序，数据库还必须理解如何对当前行的x值”减5”或者”加10”以标识当前窗口帧的边界。把得到的边界与其他行的x值用B-树操作符类提供的比较操作符（定义了ORDER BY顺序）进行比较是可能的 — 但是加和减操作符并不是该操作符类的一部分，因此应该用哪些操作符呢？硬编码的选择是不切实际的，因为不同的排序顺序（不同的B-树操作符）可能需要不同的行为。因此，一个B-树操作符类可以指定一个in\_range支持函数，它封装有对排序顺序有意义的加和减行为。如果有多种数据类型可以用作RANGE子句中的偏移量，甚至可以提供多个in\_range支持函数。如果与窗口的ORDER BY子句关联的B-树操作符类没有一个匹配的in\_range支持函数，则不支持RANGE

offset

PRECEDING/

FOLLOWING选项。

另一个要点是，出现在一个哈希操作符族中的操作符是哈希连接、哈希聚集和相关优化的候选。这些情况下哈希操作符族就是至关重要的，因为它标识了要使用的哈希函数。

### 排序操作符

有些索引访问方法（当前只有 GiST和SP-GiST）支持排序操作符的概念。到目前为止我们所讨论的都是搜索操作符。搜索索引时，会用搜索操作符来寻找所有满足 WHERE indexed\_column operator constant 的行。注意被返回的匹配行的顺序是没有任何保证的。

相反，一个排序操作符并不限制能被返回的行集合，而是决定它们的顺序。扫描索引时，会使用排序操作符来以

ORDER BY

indexed\_column

operator

constant 所表示的顺序返回行。这样定义排序操作符的原因是，如果该操作符能度量距离，它就能支持最近邻搜索。例如，这样的一个查询

SELECT \* FROM places ORDER BY location <-> point '(101,456)' LIMIT 10;

寻找离一个给定目标点最近的十个位置。位置列上的 GiST 索引可以有效地完成这个查询，因为<->是一个排序操作符。

搜索操作符必须返回布尔结果，排序操作符通常返回某种其他类型，例如浮点、数字或者距离。这种类型通常不同于被索引的数据类型。为了避免硬编码有关不同数据类型行为的假设，需要定义一个排序操作符来提名一个 B-树操作符族指定结果数据类型的排序顺序。正如我们在前一节介绍的，B-树操作符族定义了瀚高数据库的顺序概念，因此这是一种自然的表达。由于点<->操作符返回float8，可以在一个操作符类创建命令中这样指定它：

OPERATOR 15 <-> (point, point) FOR ORDER BY float\_ops

其中float\_ops是包括float8上操作的内建操作符族。这种声明说明该索引能够以<->操作符的递增值顺序返回行。

### 操作符类的特性

有两个操作符类的特性我们还没有讨论，主要是因为它们对于最常用的索引方法不太有用。

通常，把一个操作符声明为一个操作符类（或操作符族）的成员意味着该索引方法能够使用该操作符准确地检索满足WHERE条件的行集。例如：

SELECT \* FROM table WHERE integer\_column < 4;

恰好可以被该整数列上一个 B-树索引满足。但是也有情况下索引只是作为匹配行的非精确向导。例如，如果一个 GiST 索引只存储几何对象的边界框，那么它无法精确地满足测试非矩形对象（如多边形）之间相交的WHERE条件。但是我们可以使用该索引来寻找边界框与目标对象的边界框相交的对象，并且只在通过该索引找到的对象上做精确的相交测试。如果适用于这种场景，该索引被称为对该操作符是”有损的”。有损索引搜索通过在一行可能满足或者不满足该查询条件时返回一个recheck标志来实现。核心系统将接着在检索到的行上测试原始查询条件来看它是否应该被作为一个合法匹配返回。如果索引被保证能返回所有所需的行外加一些额外的行，这种方法就能有效，因为那些额外的行可以通过执行原始的操作符调用来消除。支持有损搜索的索引方法（当前有 GiST、SP-GiST 和 GIN）允许个别操作符类的支持函数设置 recheck 标志，因此这也是一种操作符类的重要特性。

再次考虑在索引中只存储复杂对象（如多边形）的边界框的情况。在这种情况下，把整个多边形存储在索引项中没有很大价值 — 我们也可以只存储一个更简单的box类型对象。这种情况通过CREATE OPERATOR CLASS中的STORAGE选项表示：

CREATE OPERATOR CLASS polygon\_ops

DEFAULT FOR TYPE polygon USING gist AS

...

STORAGE box;

当前，只有 GiST、GIN 和 BRIN 索引方法支持不同于列数据类型的STORAGE类型。在使用STORAGE时，GiST 的支持例程compress和decompress必须处理数据类型转换。在 GIN中，STORAGE类型标识”key”值的类型，它通常不同于被索引列的类型 — 例如，一个用于整数数组列的操作符类可能具有整数键值。GIN 的支持例程extractValue和extractQuery负责从被索引值中抽取键。BRIN 类似于 GIN：STORAGE类型标识被存储的摘要值的类型，而操作符类的支持过程负责正确解释摘要值。

## 打包相关对象到一个扩展中

一个对数据库有用的扩展通常包括多个 SQL 对象，例如，一种新的数据类型将需要新函数、新操作符以及可能的新索引操作符类。将所有这些对象收集到一个单一包中有助于简化数据库管理。瀚高数据库称这样一个包为一个扩展。要定义一个扩展，你至少需要一个包含创建该扩展的对象的SQL命令的脚本文件以及一个指定扩展本身的一些基本属性的控制文件。如果扩展包括 C 代码，通常还有一个 C 代码编译而成的共享库文件。一旦你有了这些文件，一个简单的CREATE EXTENSION命令可以把这些对象载入到你的数据库。

使用一个扩展而不是只运行SQL脚本载入一堆”松散”对象到数据库的主要优点是，瀚高数据库将能理解该扩展的对象是一起的。你可以用一个单一的DROP EXTENSION命令删除所有的对象（不用维护一个单独的”卸载”脚本）。 甚至更有用的一点是，pg\_dump知道它不应该转储该扩展中的个体成员对象 — 它将只在转储中包括一个CREATE EXTENSION命令。这大大简化了迁移到一个包含不同于旧版扩展中对象的新版扩展的工作。不过，注意在把这样一个转储载入到一个新数据库时，该扩展的控制、脚本和其他文件必须可用。

瀚高数据库不会让你删除包含在一个扩展中的个体对象，除非删除整个扩展。还有，虽然你能够改变一个扩展的成员对象的定义（例如，通过CREATE OR REPLACE FUNCTION改变一个函数），记住被修改后的定义将不会被pg\_dump转储。这种改变通常只有在你并发地在扩展脚本文件中做出相同更改时才有意义（但是对于包含配置数据的表有特殊的规定，见第6.17.4 节）。在生产环境中，通常更好的方式是创建一个扩展更新脚本来执行对扩展中成员对象的更改。

扩展脚本可能会通过GRANT和REVOKE语句设置扩展中所含对象的特权。每一个对象的最终特权集合（如果设置了任何特权）将被存储在pg\_init\_privs系统目录中。使用pg\_dump时，CREATE EXTENSION命令将被包括在转储中，后面会跟着必要的GRANT和REVOKE语句集合来将对象的特权设置成取得该转储时的样子。

瀚高数据库当前不支持扩展脚本发出CREATE POLICY或者SECURITY LABEL语句。这些东西的设置应该在扩展被创建好之后来进行。所有在扩展对象上创建的 RLS 策略和安全标签都将被包括在pg\_dump创建的转储中。

扩展机制也对打包调整一个扩展中所含 SQL 对象定义的修改脚本有规定。例如，如果一个扩展的 1.1 版本比 1.0 版本增加了一个函数并且更改了另一个函数的函数体，该扩展的作者可以提供一个更新脚本来做这两个更改。那么ALTER EXTENSION UPDATE命令可以被用来应用这些更改并且跟踪在给定数据库中实际安装的是该扩展的哪个版本。

能作为一个扩展的成员的 SQL 对象的种类如ALTER EXTENSION所示。尤其是数据库集簇范围的对象（例如数据库、角色和表空间）不能作为扩展成员，因为一个扩展只在一个数据库范围内可见（尽管一个扩展脚本并没有被禁止创建这些对象，但是这样做将无法把它们作为扩展的一部分来跟踪）。还要注意虽然一个表可以是一个扩展的成员，它的扶助对象（例如索引）不会被直接认为是该扩展的成员。另一个重点是模式可以属于扩展，但是反过来不行：

一个扩展本身有一个不被限定的名称并且不存在于任何模式”中”。不过，扩展的成员对象只要对象类型合适就可以属于模式。一个扩展拥有包含其成员对象的模式可能合适也可能不合适。

如果一个扩展的脚本创建任何临时对象（例如临时表），在当前会话的剩余部分会把它们当作扩展的成员，但是在会话结束会自动删除它们，这和任何其他临时对象是一样的。对于不删除整个扩展就不能删除扩展的成员对象的规则来说，这是一种例外。

### 定义扩展对象

广泛分发的扩展应该尽量少地假定它们所占据的数据库。特别是，除非你发出了SET search\_path = pg\_temp，应该假定每一个未限定的名称都可能解析成恶意用户定义的对象。

要小心隐式依赖于search\_path的结构：IN以及CASE expression WHEN总是使用搜索路径选择操作符。对于它们，可使用OPERATOR(schema.=) ANY和CASE WHEN expression。

### 扩展文件

CREATE EXTENSION命令依赖每一个扩展都有的控制文件，控制文件必须被命名为扩展的名称加上一个后缀.control，并且必须被放在安装的SHAREDIR/extension目录中。还必须至少有一个SQL脚本文件，它遵循命名模式extension--version.sql（例如，foo--1.0.sql表示扩展foo的1.0版本）。默认情况下，脚本文件也被放置在SHAREDIR/extension目录中，但是控制文件中可以为脚本文件指定一个不同的目录。

一个扩展控制文件的格式与postgresql.conf文件相同，即是一个parameter\_name = value赋值的列表，每行一个。允许空行和#引入的注释。注意对任何不是单一词或数字的值加上引号。

一个控制文件可以设置下列参数：

directory (string)

包含扩展的SQL脚本文件的目录。除非给出一个绝对路径，这个目录名是相对于安装的SHAREDIR目录。默认行为等效于指定directory = 'extension'。

default\_version (string)

该扩展的默认版本（就是如果在CREATE EXTENSION中没有指定版本时将会被安装的那一个）。尽管可以忽略这个参数，但如果没有出现VERSION选项时那将会导致CREATE EXTENSION失败，因此你通常不会希望这样做。

comment (string)

一个关于该扩展的注释（任意字符串）。该注释会在初始创建扩展时应用，但是扩展更新时不会引用该注释（因为可能会覆盖用户增加的注释）。扩展的注释也可以通过在脚本文件中写上COMMENT命令来设置。

encoding (string)

该脚本文件使用的字符集编码。当脚本文件包含任何非 ASCII 字符时，可以指定这个参数。否则文件都会被假定为数据库编码。

module\_pathname (string)

这个参数的值将被用于替换脚本文件中每一次出现的MODULE\_PATHNAME。如果设置，将不会进行替换。通常，这会被设置为$libdir/shared\_library\_name并且接

着MODULE\_PATHNAME被用在CREATE FUNCTION命令中进行 C-语言函数的创建，因此该脚本文件不必把共享库的名称硬编码在其中。

requires (string)

这个扩展依赖的其他扩展名的一个列表，例如requires = 'foo, bar'。被依赖的扩展必须先于这个扩展安装。

superuser (boolean)

如果这个参数为true（默认情况），只有超级用户能够创建该扩展或者将它更新到一个新版本。如果被设置为false，只需要用来执行安装中命令或者更新脚本的特权。

relocatable (boolean)

如果一个扩展可能在初始创建之后将其所含的对象移动到一个不同的模式中，它就是relocatable。默认值是false，即该扩展是不可重定位的。详见第 37.17.3 节。

schema (string)

这个参数只能为非可重定位扩展设置。它强制扩展被载入到给定的模式中而非其他模式中。只有在初始创建一个扩展时才会参考schema参数，扩展更新时则不会参考这个参数。详见第6.17.3 节。

除了主要控制文件extension.control，一个扩展还可以有二级控制文件，它们以extension--version.control的风格命名。如果提供了二级控制文件，它们必须被放置在脚本文件的目录中。二级控制文件遵循主要控制文件相同的格式。在安装或更新该扩展的版本时，一个二级控制文件中设置的任何参数将覆盖主要控制文件中的设置。不过，参数directory以及default\_version不能在二级控制文件中设置。

一个扩展的SQL脚本文件能够包含任何 SQL 命令，除了事务控制命令（BEGIN、COMMIT等）以及不能在一个事务块中执行的命令（如VACUUM）。这是因为脚本文件会被隐式地在一个事务块中被执行。

一个扩展的SQL脚本文件也能包含以\\echo开始的行，它将被扩展机制忽略（当作注释）。如果脚本文件被送给psql而不是由CREATE EXTENSION载入（见第6.17.7 节中的示例脚本），这种机制通常被用来抛出错误。如果没有这种功能，用户可能会意外地把该扩展的内容作为”松散的”对象而不是一整个扩展载入，这样的状态恢复起来比较麻烦。

尽管脚本文件可以包含指定编码允许的任何字符，但是控制文件应该只包含纯 ASCII 字符，因为瀚高数据库没有办法知道一个控制文件是什么编码。实际上，如果你想在扩展的注释中使用非 ASCII 字符只有一个问题。推荐的方法是不使用控制文件的comment参数，而是使用脚本文件中的COMMENT ON EXTENSION来设置注释。

### 扩展可再定位性

用户常常希望把扩展中包含的对象载入到一个与扩展的作者所设想的不一样的模式中。对于这种可重定位性，有三种支持的级别：

• 一个完全可重定位的扩展能在任何时候被移动到另一个模式中，即使在它被载入到一个数据库中之后。这种移动通过ALTER EXTENSION SET SCHEMA命令完成，该命令会自动地把所有成员对象重命名到新的模式中。通常，只有扩展不包含任何对其所在模式的内部假设时才可能这样做。还有，该扩展的对象必须全部在同一个模式中（忽略那些不属于任何模式的对象，例如过程语言）。要让一个扩展变成完全可定位，在它的控制文件中设置relocatable = true。

• 一个扩展可能在安装过程中是可重定位的，但是安装完后就不再可重定位。典型的情况是扩展的脚本文件需要显式地引用目标模式，例如为 SQL 函数设置search\_path属性。对于这样一种扩展，在其控制文件中设置relocatable = false，并且使用@extschema@在脚本文件中引用目标模式。在脚本被执行前，所有这个字符串的出现都将被替换为实际的目标模式名。用户可以使用CREATE EXTENSION的SCHEMA选项设置目标模式名。

• 如果扩展根本就不支持重定位，在它的控制文件中设置relocatable = false，并且还设置schema为想要的目标模式的名称。这将阻止使用CREATE EXTENSION的SCHEMA选项修改目标模式，除非它指定的是和控制文件中相同的模式。如果该扩展包括关于模式名的内部假设且模式名不能使用@extschema@的方法替换，这种选择通常是必须的。@extschema@替换机制在这种情况中也是可用的，不过由于模式名已经被控制文件所决定，它的使用受到了很大的限制。

在所有情况下，脚本文件将被用search\_path执行，它最初会被设置为指向目标模式，也就是说CREATE EXTENSION做的也是等效的工作：

SET LOCAL search\_path TO @extschema@;

这允许由这个脚本文件创建的对象进入到目标模式中。如果脚本文件希望，它可以改变search\_path，但这种用法通常是不受欢迎的。在CREATE EXTENSION结束后，search\_path会被恢复到之前的设置。

如果控制文件中给出了schema参数，目标模式就由该参数决定，否则目标模式由CREATE EXTENSION的SCHEMA选项给出，如果以上两者都没有给出则会用当前默认的对象创建模式（在调用者search\_path中的第一个）。当使用扩展文件的schema参数时，如果目标模式还不存在将创建它，但是在另外两种情况下它必须已经存在。

如果在控制文件中的requires中列举了任何先导扩展，它们的目标模式会被追加到search\_path的初始设置中。这允许新扩展的脚本文件能够看到它们的对象。

尽管一个不可重定位的扩展能够包含散布在多个模式中的对象，通常还是值得将意图用于外部使用的所有对象放置在一个模式中，这被认为是该扩展的目标模式。这样一种安排可以在依赖的扩展创建过程中方便地与search\_path的默认设置一起工作。

### 扩展配置表

某些扩展包括配置表，其中包含可以由用户在扩展安装后增加或修改的数据。通常，如果一个表是一个扩展的一部分，该表的定义和内容都不会被pg\_dump转储。但是对于一个配置表来说并不希望是这样的行为，任何用户做出的数据修改都需要被包括在转储中，否则该扩展在重载之后的行为将和转储之前不同。

要解决这个问题，一个扩展的脚本文件可以把一个它创建的表或者序列标记为配置关系，这将导致pg\_dump把该表或者序列的内容（而不是它的定义）包括在转储中。要这样做，在创建表或序列之后调用函数pg\_extension\_config\_dump(regclass, text)，例如

CREATE TABLE my\_config (key text, value text);

CREATE SEQUENCE my\_config\_seq;

SELECT pg\_catalog.pg\_extension\_config\_dump('my\_config', '');

SELECT pg\_catalog.pg\_extension\_config\_dump('my\_config\_seq', '');

可以用这种方法标记任意数量的表或者序列。与serial或者bigserial列相关联的序列也可以被标记。

当pg\_extension\_config\_dump的第二个参数是一个空字符串时，该表的全部内容都会被 pg\_dump转储。这通常只有在表被扩展脚本创建为初始为空时才正确。如果在表中混合有初始数据和用户提供的数据，pg\_extension\_config\_dump的第二个参数提供了一种WHERE条件来选择要被转储的数据。例如，你可能会做

CREATE TABLE my\_config (key text, value text, standard\_entry boolean);

SELECT pg\_catalog.pg\_extension\_config\_dump('my\_config', 'WHERE NOT

standard\_entry');

并且确保只有扩展脚本创建的行中standard\_entry才为真。

对于序列，pg\_extension\_config\_dump的第二个参数没有影响。

更复杂的情况（例如用户可能会修改初始提供的数据）可以通过在配置表上创建触发器来处理，触发器将负责保证被修改的行会被正确地标记。

你可通过再次调用pg\_extension\_config\_dump来修改与一个配置表相关的过滤条件（这通常对于一个扩展更新脚本有用）。将一个表标记为不再是一个配置表的方法是用ALTER EXTENSION... DROP TABLE将它与扩展脱离开。

注意这些表之间的外键关系将会指导这些表被 pg\_dump 转储的顺序。特别地，pg\_dump 将尝试 先转储被引用的表再转储引用表。由于外键关系是在 CREATE EXTENSION 时间（先于数据被载入 到表中）建立的，环状依赖还没有建立。当环状依赖存在时，数据将仍然被转储，但是该转储无法被 直接恢复并且必须要用户的介入。

与serial或者bigserial列相关联的序列需要被直接标记以转储它们的状态。只标记它们的父关系不足以转储它们的状态。

### 扩展更新

扩展机制的一个优点是它提供了方便的方法来管理那些定义扩展中对象的 SQL 命令的更新。 这是通过为扩展的安装脚本的每一个发行版本关联一个版本名称或者版本号实现的。 此外，如果你希望用户能够动态地把他们的数据库从一个版本更新到下一个版本，你应该提供更新脚本来做必要的更改。 更新脚本的名称遵循extension--old\_version-- target\_version.sql模式 （例如，foo--1.0--1.1.sql包含着把扩展foo的版本1.0修改成版本1.1的命令）。

假定有一个合适的更新脚本可用，命令ALTER EXTENSION UPDATE将把一个已安装的扩展更新到指定的新版本。更新脚本运行在与CREATE EXTENSION提供给安装脚本相同的环境中：特别是search\_path会按照相同的方式设置，并且该脚本创建的任何新对象会被自动地加入到扩展中。此外，如果脚本选择删除扩展的成员对象，它们会自动与扩展解除关联。

如果一个扩展具有二级控制文件，用于更新脚本的控制参数是那些与新目标版本相关的参数。

更新机制可以被用来解决一种重要的特殊情况：将一个”松散的”对象集合转变成一个扩展。给定一个包含这类对象的现有数据库，我们怎样才能将这些对象转变成一个正确打包的扩展？将它们全部删除然后做一次CREATE EXTENSION是一种方法，但是如果对象之间有依赖（例如，如果有一些表列使用了扩展创建的数据类型）这就行不通。

修正这种情况的方法是创建一个空扩展，然后使用ALTER EXTENSION ADD把每一个以前就存在的对象附着到该扩展，最后创建在当前扩展版本中而不再未打包版本中的任何新对象。CREATE EXTENSION用它的FROM old\_version选项支持这种情况，这会导致它不为目标版本运行正常的安装脚本，而是运行名为extension--old\_version--target\_version.sql的更新脚本。选择作为old\_version使用的虚假版本名称是扩展作者的工作，不过unpackaged是一种习惯用法。如果你有多个早期版本需要更新到扩展风格，使用多个虚假版本名称来标识它们。

ALTER EXTENSION能够执行更新脚本的序列来实现一个要求的更新。例如，如果只有foo--1.0--1.1.sql和foo--1.1--2.0.sql可用，当前安装了1.0版本并且要求更新到版本2.0，ALTER EXTENSION将依次应用它们。

瀚高数据库并不假定任何有关版本名称的性质：例如，它不知道1.1是否跟在1.0后面。它只是匹配可用的版本名称并且遵照要求应用最少更新脚本的路径进行（一个版本名称实际上可以是不含--或者前导或后缀-的字符串）。

有时提供”降级”脚本也有用，例如foo--1.1--1.0.sql允许把版本1.1相关的改变恢复原状。如果你这样做，要当心降级脚本被意外应用的可能性，因为它会得到一个较短的路径。

危险的情况是，有一个跳过几个版本的”快速路径”更新脚本还有一个降级到该快速路径开始点的降级脚本。先应用降级然后再应用快速路径可能比一次升级一个版本需要更少的步骤。如果降级版本删除了任何不可替代的对象，这将会得到意想不到的结果。

要检查意料之外的更新路径，可使用这个命令：

SELECT \* FROM pg\_extension\_update\_paths('extension\_name');

这会为指定的扩展显示已知的每一个可区分的版本名对，每一个版本名对还带有一个从源版本到目标版本的更新路径序列，如果没有可用的更新路径则这部份信息为NULL。该路径显示为用--分隔符的文本形式。如果你更喜欢数组格式，可以使用regexp\_split\_to\_array(path,'--')。

### 用更新脚本安装扩展

一个已经存在一段时间的扩展可能存在多个版本，作者将需要为它们编写更新脚本。例如，如果你已经发布了扩展foo的版本1.0、1.1和1.2，就应该有更新脚本foo--1.0--1.1.sql和foo--1.1--1.2.sql。例如，如果只有脚本文件foo--1.0.sql、foo--1.0--1.1.sql和foo--1.1--1.2.sql可用，那么安装版本1.2的请求会通过按顺序运行上述三个脚本来实现。这种处理和先安装1.0然后更新到1.2是一样的（和ALTER EXTENSION UPDATE一样，如果有多条路径可用则优先选择最短的）。按这种风格安排扩展 的脚本文件可以减少生产小更新所需的维护工作量。

如果以这种风格维护的扩展中使用了二级（版本相关的）控制文件，记住每个版本都需要一个控制文件，即使它没有单独的安装脚本，因为该控制文件将决定如何执行到这个版本的隐式更新。例如，如果foo--1.0.control指定有requires = 'bar'，但foo的其他控制文件没有这样做，在从1.0更新到另一个版本时，该扩展对bar的依赖将被删除。

### 扩展实例

这里是一个只用SQL的扩展的完整例子，一个两个元素的组合类型，它可以在它的槽（命名为”k”和”v”）中存储任何类型的值。非文本值会被自动强制为文本进行存储。

脚本文件pair--1.0.sql看起来像这样：

\-- 如果脚本是由 psql 而不是 CREATE EXTENSION 执行，则报错

\\echo Use "CREATE EXTENSION pair" to load this file. \\quit

CREATE TYPE pair AS ( k text, v text );

CREATE OR REPLACE FUNCTION pair(text, text)

RETURNS pair LANGUAGE SQL AS 'SELECT ROW($1, $2)::@extschema@.pair;';

CREATE OPERATOR ~> (LEFTARG = text, RIGHTARG = text, FUNCTION = pair);

\-- "SET search\_path"容易操作，但限定名称更好。

CREATE OR REPLACE FUNCTION lower(pair)

RETURNS pair LANGUAGE SQL

AS 'SELECT ROW(lower($1.k), lower($1.v))::@extschema@.pair;'

SET search\_path = pg\_temp;

CREATE OR REPLACE FUNCTION pair\_concat(pair, pair)

RETURNS pair LANGUAGE SQL

AS 'SELECT ROW($1.k OPERATOR(pg\_catalog.||) $2.k,

$1.v OPERATOR(pg\_catalog.||) $2.v)::@extschema@.pair;';

控制文件pair.control看起来像这样：

\# pair 扩展

comment = 'A key/value pair data type'

default\_version = '1.0'

relocatable = false

虽然你几乎不会需要一个 makefile 来安装这两个文件到正确的目录，你还是可以使用一个Makefile：

EXTENSION = pair

DATA = pair--1.0.sql

PG\_CONFIG = pg\_config

PGXS:= $(shell $(PG\_CONFIG) --pgxs)

include $(PGXS)

这个 makefile 依赖于PGXS。命令make install将把控制和脚本文件安装到pg\_config报告的正确的目录中。

一旦文件被安装，使用CREATE EXTENSION命令就可以把对象载入到任何特定的数据库中。

## 扩展的构建基础设施

如果你正在考虑发布你的数据库扩展模块，为它们建立一个可移植的构建系统实在是相当困难。因此瀚高数据库安装为扩展提供了一种被称为PGXS构建基础设施，因此简单的扩展模块能够在一个已经安装的服务器上简单地编译。PGXS主要是为了包括 C 代码的扩展而设计，不过它也能用于纯 SQL 的扩展。注意PGXS并不想成为一种用于构建任何与数据库交互的软件的通用构建系统框架。它只是简单地把简单服务器扩展模块的公共构建规则自动化。对于更复杂的包，你可能需要编写你自己的构建系统。

要把PGXS基础设施用于你的扩展，你必须编写一个简单的 makefile。在这个 makefile 中，你需要设置一些变量并且把它们包括在全局的PGXS makefile 中。这里有一个例子，它构建一个名为isbn\_issn的扩展模块，其中包括一个含有 C 代码的共享库、一个扩展控制文件、一个 SQL 脚本、一个包括文件（仅当其他模块可能需要通过调用而不是SQL访问这个扩展的函数时才需要）以及一个文档文件：

MODULES = isbn\_issn

EXTENSION = isbn\_issn

DATA = isbn\_issn--1.0.sql

DOCS = README.isbn\_issn

HEADERS\_isbn\_issn = isbn\_issn.h

PG\_CONFIG = pg\_config

PGXS:= $(shell $(PG\_CONFIG) --pgxs)

include $(PGXS)

最后三行应该总是相同的。在这个文件的前面部分，你要对变量赋值或者增加自定义的make规则。

设置这三个变量之一来指定要构建什么：

MODULES

要从源文件构建的具有相同词干的共享库对象的列表（不要在这个列表中包括库后缀）

MODULE\_big

一个要从多个源文件中构建的共享库（在OBJS中列出对象文件）

PROGRAM

一个要构建的可执行程序（在OBJS中列出对象文件）

还可以设置下列变量：

EXTENSION

扩展名称；你必须为每一个名称提供一个extension.control文件，它将被安装到prefix/share/extension中

MODULEDIR

subdirectory of prefix/share的子目录，DATA 和 DOCS 文件会被安装到其中（如果没有设置，设置了EXTENSION时默认为extension，没有设置EXTENSION时默认为contrib）

DATA

要安装到prefix/share/$MODULEDIR中的随机文件

DATA\_built

要安装到prefix/share/$MODULEDIR中的随机文件，它们需要先被构建

DATA\_TSEARCH

要安装到prefix/share/tsearch\_data中的随机文件

DOCS

要安装到prefix/doc/$MODULEDIR中的随机文件

HEADERS

HEADERS\_built

要（构建并且）安装在prefix/include/server/$MODULEDIR/$MODULE\_big下面的文件。

和DATA\_built不同，HEADERS\_built中的文件不会被clean目标移除，如果想要移除它们，把它们也加入到EXTRA\_CLEAN或者增加自己的规则来做这件事。

HEADERS\_$MODULE

HEADERS\_built\_$MODULE

要安装（如果指定了构建则在构建之后安装）在prefix/include/server/$MODULEDIR/ $MODULE之下的文件，这里$MODULE必须是一个在MODULES or MODULE\_big中用到的模块名。

和DATA\_built不同，HEADERS\_built\_$MODULE中的文件不会被clean目标移除，如果想要移除它们，把它们也加入到EXTRA\_CLEAN或者增加自己的规则来做这件事。

可以为同一个模块同时使用这两个变量或者两者的任意组合，除非你在MODULES列表中有两个模块名称仅有前缀built\_上的区别，因为那样会导致歧义。在那种情况下（还好不太可能），应该仅使用HEADERS\_built\_$MODULE变量。

SCRIPTS

要安装到prefix/bin中的脚本文件（非二进制）

SCRIPTS\_built

要安装到prefix/bin中的脚本文件（非二进制），它们需要先被构建

REGRESS

回归测试案例（不带后缀）的列表，见下文

REGRESS\_OPTS

要传递给pg\_regress的附加开关

ISOLATION

隔离测试用例列表，请参阅下文了解更多详细信息。

ISOLATION\_OPTS

要传递给pg\_isolation\_regress的附加开关

TAP\_TESTS

是否需要运行 TAP 测试的开关定义，请参阅下文

NO\_INSTALLCHECK

不定义installcheck目标，如果测试要求特殊的配置就会很有用，或者不使用

pg\_regress

EXTRA\_CLEAN

要在make clean中移除的额外文件

PG\_CPPFLAGS

将被加到CPPFLAGS前面

PG\_CFLAGS

将被加到CFLAGS后面

PG\_CXXFLAGS

将被加到CXXFLAGS后面

PG\_LDFLAGS

将被加到LDFLAGS前面

PG\_LIBS

将被加到PROGRAM链接行

SHLIB\_LINK

将被加到MODULE\_big链接行

PG\_CONFIG

要在其中构建的瀚高数据库安装的pg\_config程序的路径（通常只用在你的PATH中的第一个pg\_config）

把这个 makefile 作为Makefile放在保存你扩展的目录中。然后你可以执行make进行编译，并且接着make install来安装你的模块。默认情况下，该模块会为在你的PATH中找到的第一个pg\_config程序所对应的瀚高数据库安装编译和安装。你可以通过在 makefile 中或者make命令行中设置PG\_CONFIG指向另一个pg\_config程序来使用一个不同的安装。

如果你想保持编译目录独立，你也可以在你的扩展所属的源代码树之外的目录中运行 make。 这个过程也被称为一个 VPATH 编译。下面是做法：

mkdir build\_dir

cd build\_dir

make -f /path/to/extension/source/tree/Makefile

make -f /path/to/extension/source/tree/Makefile install

此外，你可以以对核心代码所作的方式一样为 VPATH 设置一个目录。一种方式是使用核心脚本 config/prep\_buildtree。一旦这样做，你可以这样设置 make变量VPATH：

make VPATH=/path/to/extension/source/tree

make VPATH=/path/to/extension/source/tree install

这个过程可以在很多种目录布局下工作。

列举在REGRESS变量中的脚本会被用来对你的扩展进行回归测试，回归测试可以在做完make install之后用make installcheck调用。要让这能够工作，你必须已经有一个运行着的数据库服务器。列举在REGRESS中的脚本文件必须在你扩展目录的名为sql/的子目录中出现。这些文件必须带有扩展.sql，但扩展不能被包括在 makefile 的REGRESS列表中。对每一个测试还应该在名为expected/的子目录中有一个包含预期输出的文件，它具有和脚本文件相同的词干并带有扩展.out。make installcheck会用psql执行每一个测试脚本，并且将得到结果输出与相应的预期输出比较。任何区别都将以diff -c格式写入到文件regression.diffs中。注意尝试运行一个不带预期文件的测试将被报告为”故障”，因此确保你拥有所有的预期文件。

ISOLATION变量中列出的脚本用于测试强调与模块并发会话的行为，可以在make install之后通过make installcheck 调用。 要实现这个工作，你必须有一个正在运行的数据库服务器。 ISOLATION中列出的脚本文件必须显示在扩展名目录中名为 specs/的子目录中。 这些文件必须具备扩展名.spec，并且不得包含在 makefile 中的ISOLATION列表中。 对于每个测试，在名为expected/的子目录中还应该有一个包含预期输出的文件，并且具有相同的词干和扩展名.out。 make installcheck执行每个测试脚本，并将结果输出与匹配的预期文件进行比较。 任何差异都将以diff -c的格式写入到output\_iso/regression.diffs文件中。 请注意，尝试运行缺少其预期文件的测试将会报告”trouble”，因此请确保你具有全部的预期文件。

TAP\_TESTS 启用TAP测试. 每个运行中的数据都存在于名为 tmp\_check/的子目录中。

| 提示： |
| --- |
| 创建预期文件最简单的方法是创建空文件，然后做一次测试运行（这当然将报告区别）。检查在results/目录中找到的实际结果文件 (对于 REGRESS中的测试), 或output\_iso/results/ 目录(对于ISOLATION)中的测试，如果它们符合你的预期则把它们复制到expected/中。 |