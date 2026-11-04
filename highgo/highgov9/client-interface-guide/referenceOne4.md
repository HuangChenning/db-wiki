---
title: "ECPG-C中的嵌入式 SQL"
book: "客户端接口指南"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/reference/referenceOne4.html"
tags:
  - highgo
  - highgo-v9
  - client-interface-guide
---

## ECPG -C中嵌入式 SQL

这一章描述了用于瀚高数据库的嵌入式SQL包。它由 Linus Tolke（< [linus@epact.se](mailto:linus@epact.se) >）和 Michael Meskes（< [meskes@postgresql.org](mailto:meskes@postgresql.org) >）编写。最初它是为了与C一起工作而编写的。它也能与C++配合，但是它还不识别所有的C++结构。

## 概念

一个嵌入式 SQL 程序由一种普通编程语言编写的代码（在这里是 C）和位于特殊标记的小节中的 SQL 命令混合组成。要构建该程序，源代码（\*.pgc）首先会通过嵌入式 SQL 预处理器，它会将源代码转换成一个普通C程序（\*.c），并且后来它能够被一个C编译器所处理（编译和链接详见第 35.10 节）。转换过的 ECPG 应用会通过嵌入式 SQL 库（ecpglib）调用 libpq 库中的函数，并且与瀚高数据库服务器使用普通的前端/后端协议通信。

嵌入式SQL在为C代码处理SQL命令方面比起其他方法来具有优势。首先，它会搞定向你的C程序变量传递或者读取信息时的繁文缛节。其次，程序中的 SQL 代码在编译时就会被检查以保证语法正确性。第三，C 中的嵌入式SQL是在SQL标准中指定的并且受到很多其他SQL数据库系统的支持。瀚高数据库实现被设计为尽可能匹配这个标准，并且通常可以相对容易地把为其他 SQL 数据库编写的SQL程序移植到瀚高数据库。

正如已经支出的，为嵌入式SQL接口编写的程序是插入了用于执行数据库相关动作的特殊代码的普通的C程序。这种特殊代码总是具有这样的形式：

EXEC SQL...;

这些语句在语法上取代了一个C语句。取决于特定的语句，它们可以出现在全局层面或者是一个函数中。嵌入式 SQL语句遵循普通SQL代码的大小写敏感性规则， 而不是C的大小写敏感性规则。它们也允许嵌套的C风格注释（SQL 标准的一部分）。 不过，程序的C部分遵循C的标准不接受嵌套注释。

下列小节解释了所有嵌入式 SQL 语句。

## 管理数据库连接

这一节描述如何打开、关闭以及切换数据库连接。

### 连接到数据库服务器

我们可以使用下列语句连接到一个数据库：

EXEC SQL CONNECT TO target \[AS connection-name\] \[USER user-name\];

target可以用下列方法指定：

• dbname\[@hostname\]\[:port\]

• tcp:postgresql://hostname\[:port\]\[/dbname\]\[?options\]

• unix:postgresql://hostname\[:port\]\[/dbname\]\[?options\]

• 一个包含上述形式之一的 SQL 字符串

• 到一个包含上述形式之一（参见例子）的字符变量的引用

• DEFAULT

如果你用字面（也就是不通过一个变量引用）指定连接目标并且你没有引用该值，那么将会应用普通 SQL 的大小写不敏感性规则。在那种情况中，你也能够按照需要单独将个体参数放置在双引号中。实际上，使用一个（单引号引用）的字符串或一个变量引用出错的可能性更小。连接目标DEFAULT会以默认用户名发起一个到默认数据库的连接。在那种情况中不能指定单独的用户名或连接名。

也有不同的方法来指定用户名：

• username

• username/password

• username IDENTIFIED BY password

• username USING password

如上所述，参数username以及password可以是一个 SQL 标识符、一个 SQL 字符串或者一个对字符变量的引用。

如果连接目标包含任何options， 这些由keyword=value组成的规范，由表示”和”的符号 (&)分隔。 允许的关键字与libpq识别的关键字相同。 在任何keyword或value之前的空格将被忽略，但其中或之后则不会。 请注意，无法将&写入value。

connection-name被用来在一个程序中处理多个连接。如果一个程序只使用一个连接，它可以被忽略。最近被打开的连接将成为当前连接，当一个 SQL 语句要被执行时，将默认使用它（见这一章稍后的部分）。

如果不可信用户能够访问一个没有采用安全方案使用模式的数据库，开始每个会话时应该从search\_path中移除公共可写的方案。 例如，把options=-c search\_path=加到options中或者在连接后发出EXEC SQL SELECT pg\_catalog.set\_config('search\_path', '',false);。

这种考虑并非专门针对ECPG，它适用于每一种用来执行任意SQL命令的接口。

这里有一些CONNECT语句的例子：

EXEC SQL CONNECT TO [mydb@sql.mydomain.com](mailto:mydb@sql.mydomain.com);

EXEC SQL CONNECT TO unix:postgresql://sql.mydomain.com/mydb AS myconnection USER

john;

EXEC SQL BEGIN DECLARE SECTION;

const char \*target = " [mydb@sql.mydomain.com](mailto:mydb@sql.mydomain.com) ";

const char \*user = "john";

const char \*passwd = "secret";

EXEC SQL END DECLARE SECTION;

...

EXEC SQL CONNECT TO:target USER:user USING:passwd;

/\* 或者 EXEC SQL CONNECT TO:target USER:user/:passwd; \*/

最后一种形式利用被上文成为字符变量引用的变体。你将在后面的小节中看到当你把C变量前放上一个冒号时，它们是怎样被用于 SQL 语句的。

注意连接目标的格式没有在 SQL 标准中说明。因此如果你想要开发可移植的应用，你可能想要使用某种基于上述最后一个例子的方法来把连接目标字符串封装在某个地方。

### 选择一个连接

嵌入式 SQL 程序中的 SQL 语句默认是在当前连接（也就是最近打开的那一个）上执行的。

如果一个应用需要管理多个连接，那么有两种方法来处理这种需求。

第一个选项是显式地为每一个 SQL 语句选择一个连接，例如：

EXEC SQL AT connection-name SELECT...;

如果应用需要以混合的顺序使用多个连接，这个选项特别合适。

如果你的应用使用多个线程执行，它们不能并发地共享一个连接。你必须显式地控制对连接的访问（使用互斥量）或者为每个线程使用一个连接。

第二个选项是执行一个语句来切换当前的连接。该语句是：

EXEC SQL SET CONNECTION connection-name;

如果很多语句要被在同一个连接上执行，这个选项特别方便。

这里有一个管理多个数据库连接的例子程序：

#include <stdio.h>

EXEC SQL BEGIN DECLARE SECTION;

char dbname\[1024\];

EXEC SQL END DECLARE SECTION;

int

main()

{

EXEC SQL CONNECT TO testdb1 AS con1 USER testuser;

EXEC SQL SELECT pg\_catalog.set\_config('search\_path', '', false); EXEC SQL

COMMIT;

EXEC SQL CONNECT TO testdb2 AS con2 USER testuser;

EXEC SQL SELECT pg\_catalog.set\_config('search\_path', '', false); EXEC SQL

COMMIT;

EXEC SQL CONNECT TO testdb3 AS con3 USER testuser;

EXEC SQL SELECT pg\_catalog.set\_config('search\_path', '', false); EXEC SQL

COMMIT;

/\* 这个查询将在最近打开的数据库 "testdb3" 中执行 \*/

EXEC SQL SELECT current\_database() INTO:dbname;

printf("current=%s (should be testdb3)\\n", dbname);

/\* 使用 "AT" 在 "testdb2" 中运行一个查询 \*/

EXEC SQL AT con2 SELECT current\_database() INTO:dbname;

printf("current=%s (should be testdb2)\\n", dbname);

/\* 切换当前连接到 "testdb1" \*/

EXEC SQL SET CONNECTION con1;

EXEC SQL SELECT current\_database() INTO:dbname;

printf("current=%s (should be testdb1)\\n", dbname);

EXEC SQL DISCONNECT ALL;

return 0;

}

这个例子将产生这样的输出：

current=testdb3 (should be testdb3)

current=testdb2 (should be testdb2)

current=testdb1 (should be testdb1)

### 关闭一个连接

要关闭一个连接，使用下列语句：

EXEC SQL DISCONNECT \[connection\];

connection可以用下列方法指定：

• connection-name

• DEFAULT

• CURRENT

• ALL

如果没有指定连接名，当前连接将被关闭。

在一个应用中总是显式地从它打开的每一个连接断开是一种好的风格。

## 运行 SQL 命令

任何 SQL 命令都可以在一个嵌入式 SQL 应用中被运行。下面是一些在嵌入式 SQL 应用中运行 SQL 命令的例子。

### 执行 SQL 语句

创建一个表：

EXEC SQL CREATE TABLE foo (number integer, ascii char(16));

EXEC SQL CREATE UNIQUE INDEX num1 ON foo(number);

EXEC SQL COMMIT;

插入行：

EXEC SQL INSERT INTO foo (number, ascii) VALUES (9999, 'doodad');

EXEC SQL COMMIT;

删除行：

EXEC SQL DELETE FROM foo WHERE number = 9999;

EXEC SQL COMMIT;

更新：

EXEC SQL UPDATE foo

SET ascii = 'foobar'

WHERE number = 9999;

EXEC SQL COMMIT;

返回一个单一结果行的SELECT语句也可以直接使用EXEC SQL执行。要处理有多行的结果集，一个应用必须使用一个游标，特殊情况下，一个应用可以一次取出多行到一个数组主变量中。

单行选择：

EXEC SQL SELECT foo INTO:FooBar FROM table1 WHERE ascii = 'doodad';

还有，一个配置参数可以用SHOW命令检索：

EXEC SQL SHOW search\_path INTO:var;

:something形式的记号是主变量，即它们指向C程序中的变量。

### 使用游标

要检索一个保持多行的结果集，一个应用必须声明一个游标并且从该游标中取得每一行。使用一个游标的步骤如下：声明一个游标、打开它、从该游标取得一行、重复并且最终关闭它。

使用游标选择：

EXEC SQL DECLARE foo\_bar CURSOR FOR

SELECT number, ascii FROM foo

ORDER BY ascii;

EXEC SQL OPEN foo\_bar;

EXEC SQL FETCH foo\_bar INTO:FooBar, DooDad;

...

EXEC SQL CLOSE foo\_bar;

EXEC SQL COMMIT;

有关声明游标的更多细节，可参考DECLARE；FETCH命令的细节则可以参考FETCH。

| 注意： |
| --- |
| ECPG DECLARE命令实际上不会导致一个语句被发送到瀚高数据库后端。在OPEN命令被执行时，游标会在后端被打开（使用后端的DECLARE命令）。 |

### 管理事务

在默认模式中，只有当EXEC SQL COMMIT被发出时才会提交命令。嵌入式 SQL 接口也通过ecpg的-t命令行选项或者通过EXEC SQL SET AUTOCOMMIT TO ON语句支持事务的自动提交（类似于psql的默认行为）。在自动提交模式中，除非位于一个显式事务块内，每一个命令都会被自动提交。这种模式可以使用EXEC SQL SET AUTOCOMMIT TO OFF显式地关闭。

可以使用下列事务管理命令：

EXEC SQL COMMIT

提交一个进行中的事务。

EXEC SQL ROLLBACK

回滚一个进行中的事务。

EXEC SQL PREPARE TRANSACTION transaction\_id

为两阶段提交准备当前事务。

EXEC SQL COMMIT PREPARED transaction\_id

提交一个处于准备好状态的事务。

EXEC SQL ROLLBACK PREPARED transaction\_id

回滚一个处于准备好状态的事务。

EXEC SQL SET AUTOCOMMIT TO ON

启用自动提交模式。

EXEC SQL SET AUTOCOMMIT TO OFF

禁用自动提交模式。这是默认值。

### 预备语句

当传递给 SQL 语句的值在编译时未知或者同一个语句要被使用多次时，那么预备语句就有用武之地了。

语句使用命令PREPARE进行预备。对于还未知的值，使用占位符”?”：

EXEC SQL PREPARE stmt1 FROM "SELECT oid, datname FROM pg\_database WHERE oid =?";

如果一个语句返回一个单一行，应用可以在PREPARE之后调用EXECUTE来执行该语句，同时要用一个USING子句为占位符提供真实的值：

EXEC SQL EXECUTE stmt1 INTO:dboid,:dbname USING 1;

如果一个语句返回多行，应用可以使用一个基于该预备语句声明的游标。要绑定输入参数，该游标必须用一个USING子句打开：

EXEC SQL PREPARE stmt1 FROM "SELECT oid,datname FROM pg\_database WHERE oid >?";

EXEC SQL DECLARE foo\_bar CURSOR FOR stmt1;

/\* 当到达结果集末尾时，跳出 while 循环 \*/

EXEC SQL WHENEVER NOT FOUND DO BREAK;

EXEC SQL OPEN foo\_bar USING 100;

...

while (1)

{

EXEC SQL FETCH NEXT FROM foo\_bar INTO:dboid,:dbname;

}

EXEC SQL CLOSE foo\_bar;

当你不再需要该预备语句时，你应该释放它：

EXEC SQL DEALLOCATE PREPARE name;

更多有关PREPARE的细节，可参考PREPARE。

## 使用主变量

在之前章节中，你了解了如何从一个嵌入式 SQL 程序执行SQL 语句。某些语句只使用固定值并且没有提供方法来插入用户提供的值到语句中或者让程序处理查询返回的值。那种语句在实际应用中其实没有什么用处。这一节详细解释了如何使用一种简单的机制（主变量）在C程序和嵌入式 SQL 语句之间传递数据。在一个嵌入式 SQL 程序中，我们认为 SQL 语句是C程序代码中的客人，而C代码是主语言。因此 C程序的变量被称为主变量。

另一种在瀚高数据库后端和 ECPG 应用之间交换值的方式是使用 SQL 描述符。

### 概述

在嵌入式 SQL 中进行C程序和 SQL 语句见的数据传递特别简单。我们不需要让程序把数据粘贴到语句（这会导致很多复杂性，例如正确地引用值），我们可以简单地在 SQL 语句中写C变量的名称，只要在它前面放上一个冒号。例如：

EXEC SQL INSERT INTO sometable VALUES (:v1, 'foo',:v2);

这个语句引用了两个C变量（名为v1和v2）并且还使用了一个常规的 SQL 字符串来说明你没有被限制于使用某一种数据。

这种在 SQL 语句中插入C变量的风格可以用在 SQL 语句中每一个应该出现值表达式的地方。

### 声明小节

要从程序传递数据给数据库（例如作为一个查询的参数）或者从数据库传数据回程序，用于包含这些数据的C变量必须在特别标记的节中被声明，这样嵌入式 SQL 预处理器才会注意它们。

这个节开始于：

EXEC SQL BEGIN DECLARE SECTION;

并且结束于：

EXEC SQL END DECLARE SECTION;

在这两行之间，必须是正常的C变量声明，例如：

int x = 4;

char foo\[16\], bar\[16\];

如你所见，你可以选择为变量赋一个初始值。变量的可见范围由定义它的节在程序中的位置决定。你也可以使用下面的语法声明变量，这种语法将会隐式地创建一个声明节：

EXEC SQL int i = 4;

你可以按照你的意愿在一个程序中放上多个声明节。

这些声明也会作为C变量被重复在输出文件中，因此无需再次声明它们。不准备在 SQL 命令中使用的变量可以正常地在这些特殊节之外声明。

一个结构或联合的定义也必须被列在一个DECLARE节中。否则预处理器无法处理这些类型，因为它不知道它们的定义。

### 检索查询结果

现在你应该能够把程序产生的数据传递到一个 SQL 命令中了。但是怎么检索一个查询的结果呢？为此，嵌入式 SQL 提供了常规命令SELECT和FETCH的特殊变体。这些命令有一个特殊的INTO子句，它指定被检索到的值要被存储在哪些主变量中。SELECT被用于只返回单一行的查询，而FETCH被用于使用一个游标返回多行的查询。

这里是一个例子：

/\*

\* 假定有这个表：

\* CREATE TABLE test1 (a int, b varchar(50));

\*/

EXEC SQL BEGIN DECLARE SECTION;

int v1;

VARCHAR v2;

EXEC SQL END DECLARE SECTION;

...

EXEC SQL SELECT a, b INTO:v1,:v2 FROM test;

那么INTO子句出现在选择列表和FROM子句之间。选择列表中的元素数量必须和INTO后面列表（也被称为目标列表）的元素数量相等。

这里有一个使用命令FETCH的例子：

EXEC SQL BEGIN DECLARE SECTION;

int v1;

VARCHAR v2;

EXEC SQL END DECLARE SECTION;

...

EXEC SQL DECLARE foo CURSOR FOR SELECT a, b FROM test;

...

do

{

...

EXEC SQL FETCH NEXT FROM foo INTO:v1,:v2;

...

} while (...);

这里INTO子句出现在所有正常子句的后面。

### 类型映射

当 ECPG 应用在瀚高数据库服务器和C应用之间交换值时（例如从服务器检索查询结果时或者用输入参数执行 SQL 语句时），值需要在瀚高数据库数据类型和主语言变量类型（具体来说是C语言数据类型）之间转换。ECPG 的要点之一就是它会在大多数情况下自动搞定这种转换。

在这方面有两类数据类型：一些简单瀚高数据库数据类型（例如integer和text）可以被应用直接读取和写入。其他瀚高数据库数据类型（例如timestamp和numeric）只能通过特殊库函数访问。

下表展示了哪种瀚高数据库数据类型对应于哪一种C数据类型。当你希望发送或接收一种给定瀚高数据库数据类型的值时，你应该在声明节中声明一个具有相应C数据类型的C变量。

下表在瀚高数据库数据类型和C变量类型之间映射

| 瀚高数据库数据类型 | 主变量类型 |
| --- | --- |
| smallint | short |
| integer | int |
| bigint | long long int |
| decimal | decimala |
| numeric | numerica |
| real | float |
| double precision | double |
| smallserial | short |
| serial | int |
| bigserial | long long int |
| oid | unsigned int |
| character(n), varchar(n), text | char\[n+1\], VARCHAR\[n+1\] |
| name | char\[NAMEDATALEN\] |
| timestamp | timestampa |
| interval | intervala |
| date | datea |
| boolean | boolb |
| bytea | char \*, bytea\[n\] |

a这种类型只能通过特殊的库函数访问。

b如果不是本地化类型，则声明在ecpglib.h中

#### 处理字符串

要处理 SQL 字符串数据类型（例如varchar以及text），有两种可能的方式来声明主变量。

一种方式是使用char\[\]（一个char字符串），这是在C中处理字符数据最常见的方式。EXEC SQL BEGIN DECLARE SECTION;

char str\[50\];

EXEC SQL END DECLARE SECTION;

注意你必须自己照看长度。如果你把这个主变量用作一个查询的目标变量并且该查询返回超过 49 个字符的字符串，那么将会发生缓冲区溢出。

另一种方式是使用VARCHAR类型，它是 ECPG 提供的一种特殊类型。在一个VARCHAR类型数组上的定义会被转变成一个命名的struct。这样一个声明：

VARCHAR var\[180\];

会被转变成：

struct varchar\_var { int len; char arr\[180\]; } var;

成员arr容纳包含一个终止零字节的字符串。因此，要在一个VARCHAR主变量中存储一个字符串，该主变量必须被声明为具有包括零字节终止符的长度。成员len保存存储在arr中的字符串的长度，不包括终止零字节。当一个主变量被用做一个查询的输入时，如果strlen(arr)和len不同，将使用短的那一个。

VARCHAR可以被写成大写或小写形式，但是不能大小写混合。

char和VARCHAR主变量也可以保存其他 SQL 类型的值，它们将被存储为字符串形式。

#### 访问特殊数据类型

ECPG 包含一些特殊类型帮助你容易地与来自瀚高数据库服务器的一些特殊数据类型交互。

特别地，它已经实现了对于numeric、decimal、date、timestamp以及interval类型的支持。这些数据类型无法有效地被映射到原始的主变量类型（例如int、long long int或者char\[\]），因为它们有一种复杂的内部结构。应用通过声明特殊类型的主变量以及使用 pgtypes 库中的函数来处理这些类型。pgtypes 库（在\[ECPG -C中的嵌入式 SQL\](#\_ECPG - C 中的嵌入式 SQL)中详细描述）包含了处理这些类型的基本函数，这样你不需要仅仅为了给一个时间戳增加一个时段而发送一个查询给 SQL 服务器。

下面的小节描述了这些特殊数据类型。关于 pgtypes 库函数的更多细节。

##### timestamp, date

这里有一种在 ECPG 主应用中处理timestamp变量的模式。

首先，程序必须包括用于timestamp类型的头文件：

#include <pgtypes\_timestamp.h>

接着，在声明节中声明一个主变量为类型timestamp：

EXEC SQL BEGIN DECLARE SECTION;

timestamp ts;

EXEC SQL END DECLARE SECTION;

并且在读入一个值到该主变量中之后，使用 pgtypes 库函数处理它。在下面的例子中，timestamp值被PGTYPEStimestamp\_to\_asc()函数转变成文本（ASCII）形式： EXEC SQL SELECT now()::timestamp INTO:ts;

printf("ts = %s\\n", PGTYPEStimestamp\_to\_asc(ts));

这个例子将展示像下面形式的一些结果：

ts = 2010-06-27 18:03:56.949343

另外，DATE 类型可以用相同的方式处理。程序必须包括pgtypes\_date.h，声明一个主变量为日期类型并且将一个 DATE 值使用PGTYPESdate\_to\_asc()函数转变成一种文本形式。关于 pgtypes 库函数的更多细节。

##### interval

对interval类型的处理也类似于timestamp和date类型。不过，必须显式为一个interval类型分配内存。换句话说，该变量的内存空间必须在堆内存中分配，而不是在栈内存中分配。

这里是一个例子程序：

#include <stdio.h>

#include <stdlib.h>

#include <pgtypes\_interval.h>

int

main(void)

{

EXEC SQL BEGIN DECLARE SECTION;

interval \*in;

EXEC SQL END DECLARE SECTION;

EXEC SQL CONNECT TO testdb;

EXEC SQL SELECT pg\_catalog.set\_config('search\_path', '', false); EXEC SQL

COMMIT;

in = PGTYPESinterval\_new();

EXEC SQL SELECT '1 min'::interval INTO:in;

printf("interval = %s\\n", PGTYPESinterval\_to\_asc(in));

PGTYPESinterval\_free(in);

EXEC SQL COMMIT;

EXEC SQL DISCONNECT ALL;

return 0;

}

##### numeric, decimal

numeric和decimal类型的处理类似于interval类型：需要定义一个指针、在堆上分配一些内存空间并且使用 pgtypes 库函数访问该变量。关于 pgtypes 库函数的更多细节。

pgtypes 库没有特别为decimal类型提供函数。一个应用必须使用一个 pgtypes 库函数把它转变成一个numeric变量以便进一步处理。

这里是一个处理numeric和decimal类型变量的例子程序。

#include <stdio.h>

#include <stdlib.h>

#include <pgtypes\_numeric.h>

EXEC SQL WHENEVER SQLERROR STOP;

int

main(void)

{

EXEC SQL BEGIN DECLARE SECTION;

numeric \*num;

numeric \*num2;

decimal \*dec;

EXEC SQL END DECLARE SECTION;

EXEC SQL CONNECT TO testdb;

EXEC SQL SELECT pg\_catalog.set\_config('search\_path', '', false); EXEC SQL

COMMIT;

num = PGTYPESnumeric\_new();

dec = PGTYPESdecimal\_new();

EXEC SQL SELECT 12.345::numeric(4,2), 23.456::decimal(4,2) INTO:num,:dec;

printf("numeric = %s\\n", PGTYPESnumeric\_to\_asc(num, 0));

printf("numeric = %s\\n", PGTYPESnumeric\_to\_asc(num, 1));

printf("numeric = %s\\n", PGTYPESnumeric\_to\_asc(num, 2));

/\* 将一个decimal转变成numeric以显示一个decimal值。 \*/

num2 = PGTYPESnumeric\_new();

PGTYPESnumeric\_from\_decimal(dec, num2);

printf("decimal = %s\\n", PGTYPESnumeric\_to\_asc(num2, 0));

printf("decimal = %s\\n", PGTYPESnumeric\_to\_asc(num2, 1));

printf("decimal = %s\\n", PGTYPESnumeric\_to\_asc(num2, 2));

PGTYPESnumeric\_free(num2);

PGTYPESdecimal\_free(dec);

PGTYPESnumeric\_free(num);

EXEC SQL COMMIT;

EXEC SQL DISCONNECT ALL;

return 0;

}

##### bytea

bytea类型的处理与VARCHAR相似。 类型bytea的数组上的定义被转换为每个变量的命名结构。声明类似于：

bytea var\[180\];

is converted into:

struct bytea\_var { int len; char arr\[180\]; } var;

成员 arr 承载二进制格式数据。 不像VARCHAR，它还可以作为数据的一部分处理 '\\0' 。数据往/来转换为十六进制格式，并通过 ecpglib 发送/接收。

| 注意： |
| --- |
| bytea 变量只有在 bytea\_output 被设置为 hex时才能够使用。 |

#### 非简单类型的主变量

你也可以把数组、typedefs、结构和指针用作主变量。

##### 数组

将数组用作主变量有两种情况。第一种是一种将一些文本字符串存储在char\[\]或VARCHAR\[\]中的方法。第二种是不用一个游标从一个查询结果中检索多行。如果没有一个数组，要处理由多个行组成的查询结果，我们需要使用一个游标以及FETCH命令。但是使用数组主变量，多个行可以被一次收取。该数组的长度必须被定义成足以容纳所有的行，否则很可能会发生一次缓冲区溢出。

下面的例子扫描pg\_database系统表并且显示所有可用数据库的 OID 和名称：

int

main(void)

{

EXEC SQL BEGIN DECLARE SECTION;

int dbid\[8\];

char dbname\[8\]\[16\];

int i;

EXEC SQL END DECLARE SECTION;

memset(dbname, 0, sizeof(char)\* 16 \* 8);

memset(dbid, 0, sizeof(int) \* 8);

EXEC SQL CONNECT TO testdb;

EXEC SQL SELECT pg\_catalog.set\_config('search\_path', '', false); EXEC SQL

COMMIT;

/\* 一次检索多行到数组中。 \*/

EXEC SQL SELECT oid,datname INTO:dbid,:dbname FROM pg\_database;

for (i = 0; i < 8; i++)

printf("oid=%d, dbname=%s\\n", dbid\[i\], dbname\[i\]);

EXEC SQL COMMIT;

EXEC SQL DISCONNECT ALL;

return 0;

}

这个例子显示下面的结果（确切的值取决于本地环境）。

oid=1, dbname=template1

oid=11510, dbname=template0

oid=11511, dbname=postgres

oid=313780, dbname=testdb

oid=0, dbname=

oid=0, dbname=

oid=0, dbname=

##### 结构

一个成员名称匹配查询结果列名的结构可以被用来一次检索多列。该结构使得我们能够在一个单一主变量中处理多列值。

下面的例子从pg\_database系统表以及使用pg\_database\_size()函数检索可用数据库的 OID、名称和尺寸。在这个例子中，一个成员名匹配SELECT结果的每一列的结构变量dbinfo\_t被用来检索结果行，而不需要把多个主变量放在FETCH语句中。

EXEC SQL BEGIN DECLARE SECTION;

typedef struct

{

int oid;

char datname\[65\];

long long int size;

} dbinfo\_t;

dbinfo\_t dbval;

EXEC SQL END DECLARE SECTION;

memset(&dbval, 0, sizeof(dbinfo\_t));

EXEC SQL DECLARE cur1 CURSOR FOR SELECT oid, datname, pg\_database\_size(oid)

AS size FROM pg\_database;

EXEC SQL OPEN cur1;

/\* 在达到结果集末尾时，跳出 while 循环 \*/

EXEC SQL WHENEVER NOT FOUND DO BREAK;

while (1)

{

/\* 将多列取到一个结构中。 \*/

EXEC SQL FETCH FROM cur1 INTO:dbval;

/\* 打印该结构的成员。 \*/

printf("oid=%d, datname=%s, size=%lld\\n", dbval.oid, dbval.datname,

dbval.size);

}

EXEC SQL CLOSE cur1;

这个例子会显示下列结果（确切的值取决于本地环境）。

oid=1, datname=template1, size=4324580

oid=11510, datname=template0, size=4243460

oid=11511, datname=postgres, size=4324580

oid=313780, datname=testdb, size=8183012

结构主变量将列尽数”吸收”成结构的域。额外的列可以被分配给其他主变量。例如，上面的程序也可以使用结构外部的size变量重新构造：

EXEC SQL BEGIN DECLARE SECTION;

typedef struct

{

int oid;

char datname\[65\];

} dbinfo\_t;

dbinfo\_t dbval;

long long int size;

EXEC SQL END DECLARE SECTION;

memset(&dbval, 0, sizeof(dbinfo\_t));

EXEC SQL DECLARE cur1 CURSOR FOR SELECT oid, datname, pg\_database\_size(oid)

AS size FROM pg\_database;

EXEC SQL OPEN cur1;

/\* 在达到结果集末尾时，跳出 while 循环 \*/

EXEC SQL WHENEVER NOT FOUND DO BREAK;

while (1)

{

/\* 将多列取到一个结构中。 \*/

EXEC SQL FETCH FROM cur1 INTO:dbval,:size;

/\* 打印该结构的成员。 \*/

printf("oid=%d, datname=%s, size=%lld\\n", dbval.oid, dbval.datname,

size);

}

EXEC SQL CLOSE cur1;

##### Typedefs

使用typedef关键词可以把新类型映射到已经存在的类型。

EXEC SQL BEGIN DECLARE SECTION;

typedef char mychartype\[40\];

typedef long serial\_t;

EXEC SQL END DECLARE SECTION;

注意你也可以使用：

EXEC SQL TYPE serial\_t IS long;

这种声明不需要位于一个声明节之中。

##### 指针

你可以声明最常见类型的指针。不过注意，你不能使用指针作为不带自动分配内存的查询的目标变量。

EXEC SQL BEGIN DECLARE SECTION;

int \*intp;

char \*\*charp;

EXEC SQL END DECLARE SECTION;

### 处理非简单 SQL 数据类型

这一节包含关于如何处理 ECPG 应用中非标量以及用户定义的 SQL 级别数据类型。注意这和上一节中描述的简单类型主变量的处理有所不同。

#### 数组

ECPG 中不直接支持 SQL 级别的多维数组。一维SQL 数组可以被映射到C数组主机变量，反之 亦然。不过，在创建一个语句时，ecpg并不知道列的类型，因此它无法检查一个C数组否是一个 SQL 数组的输入。在处理一个 SQL 语句的输出时，ecpg 有必需的信息并且进而检查是否两者都是 数组。

如果一个查询个别地访问一个数组的元素，那么这可以避免使用 ECPG 中的数组。然后，应该使用一个能被映射到该元素类型的类型的主变量。例如，如果一个列类型是integer数组，可以使用一个类型int的主变量。还有如果元素类型是varchar或text，可以使用一个类型char\[\]或VARCHAR\[\]的主变量。

这里是一个例子。假定有下面的表：

CREATE TABLE t3 (

ii integer\[\]

);

testdb=> SELECT \* FROM t3;

ii

\-------------

{1,2,3,4,5}

(1 row)

下面的例子程序检索数组的第四个元素并且把它存储到一个类型为int的主变量中：

EXEC SQL BEGIN DECLARE SECTION;

int ii;

EXEC SQL END DECLARE SECTION;

EXEC SQL DECLARE cur1 CURSOR FOR SELECT ii\[4\] FROM t3;

EXEC SQL OPEN cur1;

EXEC SQL WHENEVER NOT FOUND DO BREAK;

while (1)

{

EXEC SQL FETCH FROM cur1 INTO:ii;

printf("ii=%d\\n", ii);

}

EXEC SQL CLOSE cur1;

这个例子会显示下面的结果：

ii=4

要把多个数组元素映射到一个数组类型主变量中的多个元素，数组列的每一个元素以及主变量数组的每一个元素都必须被单独管理，例如：

EXEC SQL BEGIN DECLARE SECTION;

int ii\_a\[8\];

EXEC SQL END DECLARE SECTION;

EXEC SQL DECLARE cur1 CURSOR FOR SELECT ii\[1\], ii\[2\], ii\[3\], ii\[4\] FROM t3;

EXEC SQL OPEN cur1;

EXEC SQL WHENEVER NOT FOUND DO BREAK;

while (1)

{

EXEC SQL FETCH FROM cur1 INTO:ii\_a\[0\],:ii\_a\[1\],:ii\_a\[2\],:ii\_a\[3\];

...

}

注意

EXEC SQL BEGIN DECLARE SECTION;

int ii\_a\[8\];

EXEC SQL END DECLARE SECTION;

EXEC SQL DECLARE cur1 CURSOR FOR SELECT ii FROM t3;

EXEC SQL OPEN cur1;

EXEC SQL WHENEVER NOT FOUND DO BREAK;

while (1)

{

/\* 错误 \*/

EXEC SQL FETCH FROM cur1 INTO:ii\_a;

...

}

在这种情况中不会正确工作，因为你无法把一个数组类型列直接映射到一个数组主变量。

另一种变通方案是在类型char\[\]或VARCHAR\[\]的主变量中存储数组的外部字符串表达。注意这意味着该数组无法作为一个主程序中的数组被自然地访问（没有解析文本表达的进一步处理）。

#### 组合类型

ECPG 中并不直接支持组合类型，但是有一种可能的简单变通方案。可用的变通方案和上述用于数组的方案相似：要么单独访问每一个属性或者使用外部字符串表达。

对于下列例子，假定有下面的类型和表：

CREATE TYPE comp\_t AS (intval integer, textval varchar(32));

CREATE TABLE t4 (compval comp\_t);

INSERT INTO t4 VALUES ( (256, 'qaz') );

最显而易见的解决方案是单独访问每一个属性。下面的程序通过单独选择类型comp\_t的每一个属性从例子表中检索数据：

EXEC SQL BEGIN DECLARE SECTION;

int intval;

varchar textval\[33\];

EXEC SQL END DECLARE SECTION;

/\* 将组合类型列的每一个元素放在 SELECT 列表中。 \*/

EXEC SQL DECLARE cur1 CURSOR FOR SELECT (compval).intval, (compval).textval FROM

t4;

EXEC SQL OPEN cur1;

EXEC SQL WHENEVER NOT FOUND DO BREAK;

while (1)

{

/\* 将组合类型列的每一个元素取到主变量中。 \*/

EXEC SQL FETCH FROM cur1 INTO:intval,:textval;

printf("intval=%d, textval=%s\\n", intval, textval.arr);

}

EXEC SQL CLOSE cur1;

为了加强这个例子，在FETCH命令中存储值的主变量可以被集中在一个结构中。要切换到结构形式，该例子可以被改成下面的样子。

两个主变量intval和textval变成comp\_t结构的成员，并且该结构在FETCH命令中指定。

EXEC SQL BEGIN DECLARE SECTION;

typedef struct

{

int intval;

varchar textval\[33\];

} comp\_t;

comp\_t compval;

EXEC SQL END DECLARE SECTION;

/\* 将组合类型列的每一个元素放在 SELECT 列表中。 \*/

EXEC SQL DECLARE cur1 CURSOR FOR SELECT (compval).intval, (compval).textval FROM t4;

EXEC SQL OPEN cur1;

EXEC SQL WHENEVER NOT FOUND DO BREAK;

while (1)

{

/\* 将 SELECT 列表中的所有值放入一个结构。 \*/

EXEC SQL FETCH FROM cur1 INTO:compval;

printf("intval=%d, textval=%s\\n", compval.intval, compval.textval.arr);

}

EXEC SQL CLOSE cur1;

尽管在FETCH命令中使用了一个结构，SELECT子句中的属性名还是要一个一个指定。可以通过使用一个\*来要求该组合类型值的所有属性来改进。

...

EXEC SQL DECLARE cur1 CURSOR FOR SELECT (compval).\* FROM t4;

EXEC SQL OPEN cur1;

EXEC SQL WHENEVER NOT FOUND DO BREAK;

while (1)

{

/\* 将 SELECT 列表中的所有值放入一个结构。 \*/

EXEC SQL FETCH FROM cur1 INTO:compval;

printf("intval=%d, textval=%s\\n", compval.intval, compval.textval.arr);

}

...

通过这种方法，即便 ECPG 不理解组合类型本身，组合类型也能够几乎无缝地被映射到结构。

最后，也可以在类型char\[\]或VARCHAR\[\]的主变量中把组合类型值存储成它们的外部字符串表达。但是如果使用那种方法，就不太可能从主程序中访问该值的各个域了。

#### 用户定义的基础类型

ECPG 并不直接支持新的用户定义的基本类型。你可以使用外部字符串表达以及类型char\[\]或VARCHAR\[\]的主变量，并且这种方案事实上对很多类型都是合适和足够的。

这里有一个使用来自第 3.13 节中例子里的数据类型complex的例子。该类型的外部字符串表达是(%f,%f)，它被定义在函数complex\_in()以及complex\_out()函数内。

下面的例子把复杂类型值(1,1)和(3,3)插入到列a和b，并且之后把它们从表中选择出来。

EXEC SQL BEGIN DECLARE SECTION;

varchar a\[64\];

varchar b\[64\];

EXEC SQL END DECLARE SECTION;

EXEC SQL INSERT INTO test\_complex VALUES ('(1,1)', '(3,3)');

EXEC SQL DECLARE cur1 CURSOR FOR SELECT a, b FROM test\_complex;

EXEC SQL OPEN cur1;

EXEC SQL WHENEVER NOT FOUND DO BREAK;

while (1)

{

EXEC SQL FETCH FROM cur1 INTO:a,:b;

printf("a=%s, b=%s\\n", a.arr, b.arr);

}

EXEC SQL CLOSE cur1;

这个例子会显示下列结果：

a=(1,1), b=(3,3)

另一种变通方案是避免在 ECPG 中直接使用用户定义的类型，而是创建一个在用户定义的类型和 ECPG 能处理的简单类型之间转换的函数或者造型。不过要注意，在类型系统中引入类型造型（特别是隐式造型）要非常小心。

例如，

CREATE FUNCTION create\_complex(r double, i double) RETURNS complex

LANGUAGE SQL

IMMUTABLE

AS $$ SELECT $1 \* complex '(1,0')' + $2 \* complex '(0,1)' $$;

在这个定义之后 ，下面的语句

EXEC SQL BEGIN DECLARE SECTION;

double a, b, c, d;

EXEC SQL END DECLARE SECTION;

a = 1;

b = 2;

c = 3;

d = 4;

EXEC SQL INSERT INTO test\_complex VALUES (create\_complex(:a,:b),

create\_complex(:c,:d));

具有和 EXEC SQL INSERT INTO test\_complex VALUES ('(1,2)', '(3,4)');

相同的效果。

### 指示符

上述例子并没有处理空值。事实上，如果检索的例子从数据库取到了一个空值，它们将会产生一个错误。要能够向数据库传递空值或者从数据库检索空值，你需要对每一个包含数据的主变量追加一个次要主变量说明。这个次要主变量被称为指示符并且包含一个说明数据是否为空的标志，如果为空真正的主变量中的值就应该被忽略。这里有一个能正确处理检索空值的例子：

EXEC SQL BEGIN DECLARE SECTION;

VARCHAR val;

int val\_ind;

EXEC SQL END DECLARE SECTION:

...

EXEC SQL SELECT b INTO:val:val\_ind FROM test1;

如果值不为空，指示符变量val\_ind将为零；否则它将为负值。

指示符有另一种功能：如果指示符值为正，它表示值不为空，但是当它被存储在主变量中时已被截断。

如果参数-r no\_indicator被传递给预处理器ecpg，它会工作在”无指示符”模式。在无指示符模式中，如果没有指定指示符变量，对于字符串类型空值被标志（在输入和输出上）为空串，对于整数类型空值被标志为类型的最低可能值（例如，int的是INT\_MIN）。

## 动态 SQL

在很多情况中，一个应用必须要执行的特定 SQL 语句在编写该应用时就已知。不过在某些情况中，SQL 语句在运行时构造或者由一个外部来源提供。这样你就不能直接把 SQL 语句嵌入到C源代码，不过有一种功能允许你调用在一个字符串变量中提供的任意 SQL 语句。

### 执行没有结果集的语句

执行一个任意 SQL 语句的最简单方法是使用命令EXECUTE IMMEDIATE。例如：

EXEC SQL BEGIN DECLARE SECTION;

const char \*stmt = "CREATE TABLE test1 (...);";

EXEC SQL END DECLARE SECTION;

EXEC SQL EXECUTE IMMEDIATE:stmt;

EXECUTE IMMEDIATE可以被用于不返回结果集的 SQL 语句（例

如 DDL、INSERT、UPDATE、DELETE）。你不能用这种方法执行检索数据的语句（例如SELECT）。下一节将描述如何执行这一种语句。

### 执行一个有输入参数的语句

执行任意 SQL 语句的一种更强大的方法是准备它们一次并且在每次需要时执行该预备语句。

也可以准备一个一般化的语句，然后通过替换参数执行它的特定版本。在准备语句时，在你想要稍后替换参数的地方写上问号。例如：

EXEC SQL BEGIN DECLARE SECTION;

const char \*stmt = "INSERT INTO test1 VALUES(?,?);";

EXEC SQL END DECLARE SECTION;

EXEC SQL PREPARE mystmt FROM:stmt;

...

EXEC SQL EXECUTE mystmt USING 42, 'foobar';

当你不再需要预备语句时，你应该释放它：

EXEC SQL DEALLOCATE PREPARE name;

### 执行一个有结果集的语句

要执行一个只有单一结果行的 SQL 语句，可以使用EXECUTE。要保存结果，在其中增加一个INTO子句。

EXEC SQL BEGIN DECLARE SECTION;

const char \*stmt = "SELECT a, b,CFROM test1 WHERE a >?";

int v1, v2;

VARCHAR v3\[50\];

EXEC SQL END DECLARE SECTION;

EXEC SQL PREPARE mystmt FROM:stmt;

...

EXEC SQL EXECUTE mystmt INTO:v1,:v2,:v3 USING 37;

一个EXECUTE命令可以有一个INTO子句、一个USING子句，可以同时有这两个子句，也可以不带这两个子句。

如果一个查询被期望返回多于一个结果行，应该如下列例子所示使用一个游标（关于游标详见 使用游标 ）。

EXEC SQL BEGIN DECLARE SECTION;

char dbaname\[128\];

char datname\[128\];

char \*stmt = "SELECT u.usename as dbaname, d.datname "

" FROM pg\_database d, pg\_user u "

" WHERE d.datdba = u.usesysid";

EXEC SQL END DECLARE SECTION;

EXEC SQL CONNECT TO testdb AS con1 USER testuser;

EXEC SQL SELECT pg\_catalog.set\_config('search\_path', '', false); EXEC SQL

COMMIT;

EXEC SQL PREPARE stmt1 FROM:stmt;

EXEC SQL DECLARE cursor1 CURSOR FOR stmt1;

EXEC SQL OPEN cursor1;

EXEC SQL WHENEVER NOT FOUND DO BREAK;

while (1)

{

EXEC SQL FETCH cursor1 INTO:dbaname,:datname;

printf("dbaname=%s, datname=%s\\n", dbaname, datname);

}

EXEC SQL CLOSE cursor1;

EXEC SQL COMMIT;

EXEC SQL DISCONNECT ALL;

## pgtypes 库

pgtypes 库将瀚高数据库类型映射到C中等价的类型以便在C程序中使用。它还提供在C中对这些类型进行基本计算的函数，即不依赖瀚高数据库服务进行计算。请看下面的例子：

EXEC SQL BEGIN DECLARE SECTION;

date date1;

timestamp ts1, tsout;

interval iv1;

char \*out;

EXEC SQL END DECLARE SECTION;

PGTYPESdate\_today(&date1);

EXEC SQL SELECT started, duration INTO:ts1,:iv1 FROM datetbl WHERE d=:date1;

PGTYPEStimestamp\_add\_interval(&ts1, &iv1, &tsout);

out = PGTYPEStimestamp\_to\_asc(&tsout);

printf("Started + duration: %s\\n", out);

PGTYPESchar\_free(out);

### 字符串

PGTYPESnumeric\_to\_asc之类的一些函数返回一个新分配的字符串的指针。这些结果应该用PGTYPESchar\_free而不是free释放（这只在Windows上很重要，因为Windows上的内存分配和释放有时候需要由同一个库完成）。

### numeric类型

numeric类型用来完成对任意精度的计算。

因为要用于任意精度，这种变量需要能够动态地扩展和收缩。这也是为什么你只能用PGTYPESnumeric\_new和PGTYPESnumeric\_free函数在堆上创建numeric变量。decimal类型与numeric类型相似但是在精度上有限制，decimal类型可以在堆上创建也可以在栈上创建。

下列函数可以用于numeric类型：

PGTYPESnumeric\_new

请求一个指向新分配的numeric变量的指针。

numeric \*PGTYPESnumeric\_new(void);

PGTYPESnumeric\_free

释放一个numeric类型，释放它所有的内存。

void PGTYPESnumeric\_free(numeric \*var);

PGTYPESnumeric\_from\_asc

从字符串记号中解析一个numeric类型。

numeric \*PGTYPESnumeric\_from\_asc(char \*str, char \*\*endptr);

例如，可用的格式是：

\-2、794、+3.44、592.49E07或者-32.84e-4。

如果值能被成功地解析，将返回一个有效的指针，否则返回 NULL 指针。目前 ECPG 总是解析整个字符串并且因此当前不支持把第一个非法字符的地址存储在\*endptr中。你可以安全地把endptr设置为 NULL。

PGTYPESnumeric\_to\_asc

返回由malloc分配的字符串的指针，它包含numeric类型num的字符串表达。

char \*PGTYPESnumeric\_to\_asc(numeric \*num, int dscale);

numeric值将被使用dscale小数位打印，必要时会圆整。结果必须用PGTYPESchar\_free()释放。

PGTYPESnumeric\_add

把两个numeric变量相加放到第三个numeric变量中。

int PGTYPESnumeric\_add(numeric \*var1, numeric \*var2, numeric \*result);

该函数把变量var1和var2相加放到结果变量result中。成功时该函数返回 0，出错时返回 -1。

PGTYPESnumeric\_sub

把两个numeric变量相减并且把结果返回到第三个numeric变量。

int PGTYPESnumeric\_sub(numeric \*var1, numeric \*var2, numeric \*result);

该函数把变量var2从变量var1中减除。该操作的结果被存储在变量result中。成功时该函数返回 0，出错时返回 -1。

PGTYPESnumeric\_mul

把两个numeric变量相乘并且把结果返回到第三个numeric变量。

int PGTYPESnumeric\_mul(numeric \*var1, numeric \*var2, numeric \*result);

该函数把变量var1和var2相乘。该操作的结果被存储在变量result中。成功时该函数返回 0，出错时返回 -1。

PGTYPESnumeric\_div

把两个numeric变量相除并且把结果返回到第三个numeric变量。

int PGTYPESnumeric\_div(numeric \*var1, numeric \*var2, numeric \*result);

该函数用变量var2除变量var1。该操作的结果被存储在变量result中。成功时该函数返回 0，出错时返回 -1。

PGTYPESnumeric\_cmp

比较两个numeric变量。

int PGTYPESnumeric\_cmp(numeric \*var1, numeric \*var2)

这个函数比较两个numeric变量。错误时会返回INT\_MAX。成功时，该函数返回三种可能结果之一：

• var1大于var2则返回 1

• 如果var1小于var2则返回 -1

• 如果var1和var2相等则返回 0

PGTYPESnumeric\_from\_int

把一个整数变量转换成一个numeric变量。

int PGTYPESnumeric\_from\_int(signed int int\_val, numeric \*var);

这个函数接受一个有符号整型变量并且把它存储在numeric变量var中。成功时返回 0，失败时返回 -1。

PGTYPESnumeric\_from\_long

把一个长整型变量转换成一个numeric变量。

int PGTYPESnumeric\_from\_long(signed long int long\_val, numeric \*var);

这个函数接受一个有符号长整型变量并且把它存储在numeric变量var中。成功时返回 0，失败时返回 -1。

PGTYPESnumeric\_copy

把一个numeric变量复制到另一个中。

int PGTYPESnumeric\_copy(numeric \*src, numeric \*dst);

这个函数把src指向的变量的值复制到dst指向的变量中。成功时该函数返回 0，出错时返回 -1。

PGTYPESnumeric\_from\_double

把一个双精度类型的变量转换成一个numeric变量。

int PGTYPESnumeric\_from\_double(double d, numeric \*dst);

这个函数接受一个双精度类型的变量并且把结果存储在dst指向的变量中。成功时该函数返回 0，出错时返回 -1。

PGTYPESnumeric\_to\_double

将一个numeric类型的变量转换成双精度。

int PGTYPESnumeric\_to\_double(numeric \*nv, double \*dp)

这个函数将nv指向的变量中的numeric值转换成dp指向的双精度变量。成功时该函数返回 0，出错时返回 -1（包括溢出）。溢出时，全局变量errno将被额外地设置成PGTYPES\_NUM\_OVERFLOW。

PGTYPESnumeric\_to\_int

将一个numeric类型的变量转换成整数。

int PGTYPESnumeric\_to\_int(numeric \*nv, int \*ip);

该函数将nv指向的变量的numeric值转换成ip指向的整数变量。成功时该函数返回 0，出错时返回 -1（包括溢出）。溢出时，全局变量errno将被额外地设置成PGTYPES\_NUM\_OVERFLOW。

PGTYPESnumeric\_to\_long

将一个numeric类型的变量转换成长整型。

int PGTYPESnumeric\_to\_long(numeric \*nv, long \*lp);

该函数将nv指向的变量的numeric值转换成ip指向的长整型变量。成功时该函数返回 0，出错时返回 -1（包括溢出）。溢出时，全局变量errno将被额外地设置成PGTYPES\_NUM\_OVERFLOW。

PGTYPESnumeric\_to\_decimal

将一个numeric类型的变量转换成decimal。

int PGTYPESnumeric\_to\_decimal(numeric \*src, decimal \*dst);

该函数将nv指向的变量的numeric值转换成ip指向的decimal变量。成功时该函数返回 0，出错时返回 -1（包括溢出）。溢出时，全局变量errno将被额外地设置成PGTYPES\_NUM\_OVERFLOW。

PGTYPESnumeric\_from\_decimal

将一个decimal类型的变量转换成numeric。

int PGTYPESnumeric\_from\_decimal(decimal \*src, numeric \*dst);

该函数将nv指向的变量的decimal值转换成ip指向的numeric变量。成功时该函数返回 0，出错时返回 -1（包括溢出）。因为decimal类型被实现为numeric类型的一个有限的版本，在这个转换上不会发生溢出。

### 日期类型

C 中的日期类型允许你的程序处理 SQL 日期类型的数据。

下列函数可以被用于日期类型：

PGTYPESdate\_from\_timestamp

从一个时间戳中抽取日期部分。

date PGTYPESdate\_from\_timestamp(timestamp dt);

该函数接收一个时间戳作为它的唯一参数并且从这个时间戳返回抽取的日期部分。

PGTYPESdate\_from\_asc

从日期的文本表达解析一个日期。

date PGTYPESdate\_from\_asc(char \*str, char \*\*endptr);

该函数接收一个C的字符串str以及一个指向C字符串的指针endptr。当前 ECPG 总是解析完整的字符串并且因此当前不支持将第一个非法字符的地址存储在\*endptr中。你可以安全地把endptr设置为 NULL。

注意该函数总是假定格式按照 MDY 格式化并且当前在 ECPG 中没有变体可以改变这种格式。

下表展示了所有允许的输入格式。

| 输入 | 结果 |
| --- | --- |
| January 8, 1999 | January 8, 1999 |
| 1999-01-08 | January 8, 1999 |
| 1/8/1999 | January 8, 1999 |
| 1/18/1999 | January 18, 1999 |
| 01/02/03 | February 1, 2003 |
| 1999-Jan-08 | January 8, 1999 |
| Jan-08-1999 | January 8, 1999 |
| 08-Jan-1999 | January 8, 1999 |
| 99-Jan-08 | January 8, 1999 |
| 08-Jan-99 | January 8, 1999 |
| 08-Jan-06 | January 8, 2006 |
| Jan-08-99 | January 8, 1999 |
| 19990108 | ISO 8601; January 8, 1999 |
| 990108 | ISO 8601; January 8, 1999 |
| 1999.008 | 年以及积日 |
| J2451187 | 儒略日 |
| January 8, 99 BC | 公元前 99 年 |

: 表 3.1 PGTYPESdate\_from\_asc的合法输入格式

PGTYPESdate\_to\_asc

返回一个日期变量的文本表达。

char \*PGTYPESdate\_to\_asc(date dDate);

该函数接收日期dDate作为它的唯一参数。它将以形式1999-01-18输出该日期，即以YYYY-MM-DD格式输出。结果必须用PGTYPESchar\_free()释放。

PGTYPESdate\_julmdy

从一个日期类型变量中抽取日、月和年的值。

void PGTYPESdate\_julmdy(date d, int \*mdy);

该函数接收日期d以及一个指向有 3 个整数值的数组mdy的指针。变量名就表明了顺序：mdy\[0\]将被设置为包含月份，mdy\[1\]将被设置为日的值，而mdy\[2\]将包含年。

PGTYPESdate\_mdyjul

从一个由 3 个整数构成的数组创建一个日期值，3 个整数分别指定日、月和年。

void PGTYPESdate\_mdyjul(int \*mdy, date \*jdate);

这个函数接收 3 个整数（mdy）组成的数组作为其第一个参数，其第二个参数是一个指向日期类型变量的指针，它被用来保存操作的结果。

PGTYPESdate\_dayofweek

为一个日期值返回表示它是星期几的数字。

int PGTYPESdate\_dayofweek(date d);

这个函数接收日期变量d作为它唯一的参数并且返回一个整数说明这个日期是星期几。

• 0 - 星期日

• 1 - 星期一

• 2 - 星期二

• 3 - 星期三

• 4 - 星期四

• 5 - 星期五

PGTYPESdate\_today

得到当前日期。

void PGTYPESdate\_today(date \*d);

该函数接收一个指向一个日期变量（d）的指针并且把该参数设置为当前日期。

PGTYPESdate\_fmt\_asc

使用一个格式掩码将一个日期类型的变量转换成它的文本表达。

int PGTYPESdate\_fmt\_asc(date dDate, char \*fmtstring, char \*outbuf);

该函数接收要转换的日期（dDate）、格式掩码（fmtstring）以及将要保存日期的文本表达的字符串（outbuf）。成功时，返回 0；如果发生错误，则返回一个负值。

下面是你可以使用的域指示符：

• dd - 一个月中的第几天。

• mm - 一年中的第几个月。

• yy - 两位数的年份。

• yyyy - 四位数的年份。

• ddd - 星期几的名称（简写）。

• mmm - 月份的名称（简写）。

所有其他字符会被原封不动地复制到输出字符串中。

下表指出了一些可能的格式。这将给你一些线索如何使用这个函数。所有输出都是基于同一个日期：1959年11月23日。

| 格式 | 结果 |
| --- | --- |
| mmddyy | 112359 |
| ddmmyy | 231159 |
| yymmdd | 591123 |
| yy/mm/dd | 59/11/23 |
| yy mm dd | 59 11 23 |
| yy.mm.dd | 59.11.23 |
| .mm.yyyy.dd. | .11.1959.23. |
| mmm. dd, yyyy | Nov.23.1959 |
| mmm dd yyyy | Nov 23 1959 |
| yyyy dd mm | 1959 23 11 |
| ddd, mmm. dd, yyyy | Mon, Nov. 23, 1959 |
| (ddd) mmm. dd, yyyy | (Mon) Nov. 23, 1959 |

: 表 3.2 PGTYPES date\_fmt\_asc的合法输入格式

PGTYPESdate\_defmt\_asc

使用一个格式掩码把一个C的 char\*子返回串转换成一个日期类型的值。

int PGTYPESdate\_defmt\_asc(date \*d, char \*fmt, char \*str);

该函数接收一个用来保存操作结果的指向日期值的指针（d）、用于解析日期的格式掩码（fmt）以及包含日期文本表达的Cchar\* 串（str）。该函数期望文本表达匹配格式掩码。不过你不需要字符串和格式掩码的一一映射。该函数只分析相继顺序并且查找表示年份位置的文字yy或者yyyy、表示月份位置的mm以及表示日位置的dd。

下表给出了一些可能的格式。这将给你一些线索如何使用这个函数。

| 格式 | 字符串 | 结果 |
| --- | --- | --- |
| ddmmyy | 21-2-54 | 1954-02-21 |
| ddmmyy | 2-12-54 | 1954-12-02 |
| ddmmyy | 20111954 | 1954-11-20 |
| ddmmyy | 130464 | 1964-04-13 |
| mmm.dd.yyyy | MAR-12-1967 | 1967-03-12 |
| yy/mm/dd | 1954, February 3rd | 1954-02-03 |
| mmm.dd.yyyy | 041269 | 1969-04-12 |
| yy/mm/dd | 在 2525 年的七月二十八日，人类还将存在 | 2525-07-28 |
| dd-mm-yy | 也是 2525 年七月的二十八日 | 2525-07-28 |
| mmm.dd.yyyy | 9/14/58 | 1958-09-14 |
| yy/mm/dd | 47/03/29 | 1947-03-29 |
| mmm.dd.yyyy | oct 28 1975 | 1975-10-28 |
| mmddyy | Nov 14th, 1985 | 1985-11-14 |

: 表 3.3 rdefmtdate的合法输入格式

### 时间戳类型

C 中的时间戳类型允许你的程序处理 SQL 时间戳类型的数据。

下列函数可用于时间戳类型：

PGTYPEStimestamp\_from\_asc

从文本表达解析一个时间戳并放到一个时间戳变量中。

timestamp PGTYPEStimestamp\_from\_asc(char \*str, char \*\*endptr);

这个函数接收一个要解析的字符串（str）以及一个Cchar\* 的指针（endptr）。

当前 ECPG 总是解析完整的字符串并且因此当前不支持将第一个非法字符的地址存储在\*endptr中。你可以安全地把endptr设置为 NULL。成功时该函数返回解析到的时间戳。错误时，会返回PGTYPESInvalidTimestamp并且errno会被设置为PGTYPES\_TS\_BAD\_TIMESTAMP。关于这个值的重要提示请见PGTYPESInvalidTimestamp。

通常，该输入字符串能够包含一个允许的日期说明、一个空格字符和一个允许的时间说明的任意组合。注意 ECPG 不支持时区。它能够解析时区但是不会应用任何计算（例如数据库服务器所作的事情）。时区指示符会被无声无息地丢弃。

下表介绍了输入字符串的一些例子。

| 输入 | 结果 |
| --- | --- |
| 1999-01-08 04:05:06 | 1999-01-08 04:05:06 |
| January 8 04:05:06 1999 PST | 1999-01-08 04:05:06 |
| 1999-Jan-08 04:05:06.789-8 | 1999-01-08 04:05:06.789 （忽略了时区指示符） |
| J2451187 04:05-08:00 | 1999-01-08 04:05:00 （忽略了时区指示符） |

: 表 3.4 PGTYPEStimestamp\_from\_asc的合法输入格式

PGTYPEStimestamp\_to\_asc

将一个日期转换成一个Cchar\* 字符串。

char \*PGTYPEStimestamp\_to\_asc(timestamp tstamp);

该函数接收时间戳tstamp作为它的唯一参数并且返回一个分配好的包含该时间戳文本表达的字符串。结果必须用PGTYPESchar\_free()释放。

PGTYPEStimestamp\_current

检索当前的时间戳。

void PGTYPEStimestamp\_current(timestamp \*ts);

该函数检索当前的时间戳并且将它保存在ts指向的时间戳变量。

PGTYPEStimestamp\_fmt\_asc

使用一个格式掩码将一个时间戳变量转换成一个Cchar\* 。

int PGTYPEStimestamp\_fmt\_asc(timestamp \*ts, char \*output, int str\_len, char \*fmtstr);

该函数接收一个指向时间戳的指针作为它的第一个参数（ts）、一个指向输出缓冲区的指针（output）、为输出缓冲区分配的最大长度（str\_len）以及用于转换的格式掩码（fmtstr）。成功时，该函数返回 0；如果有错误发生，则返回一个负值。

你可以为格式掩码使用下列格式指示符。格式指示符就是用在libc的strftime函数中的那一些。任何非格式指示符将被复制到输出缓冲区。

• %A - 被完整的星期几名称的本国表达所替换。

• %a - 被简写星期几名称的本国表达所替换。

• %B - 被完整的月份名称的本国表达所替换。

• %b - 被简写月份名称的本国表达所替换。

• %C - 被十进制数（年份/100）所替换，单一数字会被前置一个零。

• %D - 等效于%m/%d/%y。

• %d - 被十进制数（01-31）的日所替换。

• %E\* %O\* - POSIX 区域扩展。序列 %Ec %EC %Ex %EX %Ey %EY %Od %Oe %OH %OI %Om %OM %OS %Ou %OU %OV %Ow %OW %Oy 被假定提供可供选择的表达。

此外还实现了%OB来表达可供选择的月份名称（单独使用）。

• %e - 被十进制数（01-31）的日所替换，单一数字被前置一个空格。

• %F - 等效于%Y-%m-%d。

• %G - 被替换为一个带有世纪的十进制数年份。这个年份是包含这一周大部分的年份（星期一作为这一周的第一天）。

• %g - 被替换为与%G中相同的年份，但是作为一个不带世纪的十进制数（00-99）。

• %H - 被替换为一个十进制数的小时（24 小时制，00-23）。

• %h - 和%b相同。

• %I - 被替换为一个十进制数的小时（12 小时制，01-12）。

• %j - 被替换为一个十进制数的积日（001-366）。

• %k - 被替换为一个十进制数的小时（24 小时制，00-23），单一数字被前置一个空白。

• %l - 被替换为一个十进制数的小时（12 小时制，01-12），单一数字被前置一个空白。

• %M - 被替换为一个十进制数的分钟（00-59）。

• %m - 被替换为一个十进制数的月份（01-12）。

• %n - 被替换为一个新行。

• %O\* - 和%E\*相同。

• %p - 根据情况被替换为”午前”或”午后”的本国表达。

• %R - 等效于%H:%M。

• %r - 等效于%I:%M:%S%p。

• %S - 被替换为十进制数的秒（00-60）。

• %s - 被替换为从 UTC 新纪元以来的秒数。

• %T - 等效于%H:%M:%S

• %t - 被替换为一个制表符。

• %U - 被替换为十进制数的周数（周日作为一周的第一天，00-53）。

• %u - 被替换为十进制数的星期几（周一作为一周的第一天，1-7）。

• %V - 被替换为十进制数的周数（周一作为一周的第一天，01-53）。如果包含 1 月 1日的周在新年中有 4 天或更多天，那么它是第一周。否则它是前一年的最后一周，并%v - 等效于%e-%b-%Y。

• %W - 被替换为十进制数的周数（周一作为一周的第一天，00-53）。

• %w - 被替换为十进制数的星期几（0-6，周日作为一周的第一天）。

• %X - 被替换为时间的本国表达。

• %x - 被替换为日期的本国表达。

• %Y - 被替换为十进制数的带世纪的年份。

• %y - 被替换为十进制数的不带世纪的年份（00-99）。

• %Z - 被替换为时区名称。

• %z - 被替换为相对于 UTC 的时区偏移；一个前导的加号表示 UTC 东部，一个负号表示 UTC 西部，接着是分别有两个数字的小时和分钟并且它们之间没有定界符（RFC 822日期头部的一般形式）。

• %+ - 被替换为日期和时间的本国表达。

• %-\* - GNU libc 扩展。在执行数值输出时不做任何填充。

• $\_\* - GNU libc 扩展。显式地指定用空格填充。

• %0\* - GNU libc 扩展。显式地指定用零填充。

• %% - 被替换为%。

PGTYPEStimestamp\_sub

从一个时间戳中减去另一个时间戳并且把结果保存在一个区间类型的变量中。

int PGTYPEStimestamp\_sub(timestamp \*ts1, timestamp \*ts2, interval \*iv);

该函数将从ts1指向的时间戳变量中减去ts2指向的时间戳变量，并且将把结果存储在iv指向的区间变量中。成功时，该函数返回 0；发生错误时则返回一个负值。

PGTYPEStimestamp\_defmt\_asc

用一个格式掩码从时间戳的文本表达解析其值。

int PGTYPEStimestamp\_defmt\_asc(char \*str, char \*fmt, timestamp \*d);

该函数接收一个放在变量str中的时间戳文本表达以及放在变量fmt中的要使用的格式掩码。结果将被存放在d指向的变量中。

如果格式掩码fmt是NULL，该函数将回退到使用默认的格式掩码%Y-%m-%d %H:%M:%S。

这是PGTYPEStimestamp\_fmt\_asc的逆函数。可能的格式掩码项可以参考那个函数的文档。

PGTYPEStimestamp\_add\_interval

int PGTYPEStimestamp\_add\_interval(timestamp \*tin, interval \*span, timestamp \*tout);

该函数接收一个指向时间戳变量的指针tin以及一个指向interval变量的指针span。它把 interval加到时间戳上，然后将结果时间戳保存在tout指向的变量中。成功时该函数返回0，如果发生错误则返回一个负值。

PGTYPEStimestamp\_sub\_interval

从一个时间戳变量中减去一个interval变量。

int PGTYPEStimestamp\_sub\_interval(timestamp \*tin, interval \*span, timestamp \*tout);

该函数从tin指向的时间戳变量中减去span指向的interval变量，然后把结果保存在tout指向的变量中。成功时该函数返回0，如果发生错误则返回一个负值。

### 区间类型

C 中的区间类型允许你的程序处理 SQL 区间类型的数据。下列函数可以用于区间类型：

PGTYPESinterval\_new

返回一个指向新分配的区间变量的指针。

interval \*PGTYPESinterval\_new(void);

PGTYPESinterval\_free

释放先前分配的区间变量的内存。

void PGTYPESinterval\_new(interval \*intvl);

PGTYPESinterval\_from\_asc

从文本表达解析一个区间。

interval \*PGTYPESinterval\_from\_asc(char \*str, char \*\*endptr);

该函数解析输入字符串str并且返回一个已分配的区间变量的指针。目前 ECPG 总是解析整个字符串并且因此当前不支持把第一个非法字符的地址存储在\*endptr中。你可以安全地把endptr设置为 NULL。

PGTYPESinterval\_to\_asc

将一个区间类型的变量转换成它的文本表达。

char \*PGTYPESinterval\_to\_asc(interval \*span);

该函数将span指向的区间变量转换成一个Cchar\*。输出看起来像这个例子： @ 1 day 12 hours 59 mins 10 secs。结果必须用PGTYPESchar\_free()释放。

PGTYPESinterval\_copy

复制一个区间类型的变量。

int PGTYPESinterval\_copy(interval \*intvlsrc, interval \*intvldest);

该函数将intvlsrc指向的区间变量复制到intvldest指向的区间变量。注意你需要现为目标变量分配好内存。

### decimal类型

decimal类型和numeric类型相似。不过，它被限制为最大精度是 30 个有效位。与numeric类型只能在堆上创建相反，decimal类型既可以在栈上也可以在堆上创建（使用函数PGTYPESdecimal\_new 和PGTYPESdecimal\_free）。

下列函数可以被用于decimal类型并且不仅被包含于libcompat库中。

PGTYPESdecimal\_new

要求一个指向新分配的decimal变量的指针。

decimal \*PGTYPESdecimal\_new(void);

PGTYPESdecimal\_free

释放一个decimal类型，释放它的所有内存。

void PGTYPESdecimal\_free(decimal \*var);

### pgtypeslib 的 errno 值

PGTYPES\_NUM\_BAD\_NUMERIC

一个参数应该包含一个numeric变量（或者指向一个numeric变量），但是实际上它的内存表达非法。

PGTYPES\_NUM\_OVERFLOW

发生一次溢出。由于numeric类型可以处理几乎任何精度，将一个numeric变量转换成其他类型可能导致溢出。

PGTYPES\_NUM\_UNDERFLOW

发生一次下溢。由于numeric类型可以处理几乎任何精度，将一个numeric变量转换成其他类型可能导致下溢。

PGTYPES\_NUM\_DIVIDE\_ZERO

尝试了一次除零。

PGTYPES\_DATE\_BAD\_DATE

一个非法的日期字符串被传给了PGTYPESdate\_from\_asc函数。

PGTYPES\_DATE\_ERR\_EARGS

非法参数被传给了PGTYPESdate\_defmt\_asc函数。

PGTYPES\_DATE\_ERR\_ENOSHORTDATE

PGTYPESdate\_defmt\_asc函数在输入字符串中发现了一个非法记号。

PGTYPES\_INTVL\_BAD\_INTERVAL

一个非法的区间字符串被传给了PGTYPESinterval\_from\_asc函数，或者一个非法的区间值被传给了PGTYPESinterval\_to\_asc函数。

PGTYPES\_DATE\_ERR\_ENOTDMY

在PGTYPESdate\_defmt\_asc函数中有日/月/年不匹配的赋值。

PGTYPES\_DATE\_BAD\_DAY

PGTYPESdate\_defmt\_asc函数发现了月中的一个非法日值。

PGTYPES\_DATE\_BAD\_MONTH

PGTYPESdate\_defmt\_asc函数发现了一个非法的月值。

PGTYPES\_TS\_BAD\_TIMESTAMP

一个非法的时间戳字符串被传给了PGTYPEStimestamp\_from\_asc函数，或者一个非法的时间戳值被传给了PGTYPEStimestamp\_to\_asc函数。

PGTYPES\_TS\_ERR\_EINFTIME

在一个无法处理无限时间戳值的环境中遇到了这样一个值。

### pgtypeslib 的特殊常量

PGTYPESInvalidTimestamp

表示一个非法时间戳的时间戳类型值。在解析错误时，函数PGTYPEStimestamp\_from\_asc会返回这个值。注意由于timestamp数据类型的内部表达，PGTYPESInvalidTimestamp在同时也是一个合法的时间戳。它被设置为1899-12-31 23:59:59。为了检测到错误，确认你的应用在每次调用PGTYPEStimestamp\_from\_asc后不仅仅测试PGTYPESInvalidTimestamp，还应该测试errno!= 0。

## 使用描述符区域

一个 SQL 描述符区域是一种处理SELECT、FETCH或者DESCRIBE语句结果的高级方法。一个 SQL 描述符区域把数据中一行的数据及元数据项组合到一个数据结构中。在执行动态 SQL 语句时（结果行的性质无法提前预知），元数据特别有用。瀚高数据库提供两种方法来使用描述符区域：命名 SQL 描述符区域和C结构 SQLDA。

### 命名 SQL 描述符区域

一个命名 SQL 描述符区域由一个头部以及一个或多个条目描述符区域构成，头部包含与整个描述符相关的信息，而条目描述符区域则描述结果行中的每一列。

在使用 SQL 描述符区域之前，需要先分配一个：

EXEC SQL ALLOCATE DESCRIPTOR identifier;

identifier 会作为该描述符区域的”变量名”。当不再需要该描述符时，应当释放它：

EXEC SQL DEALLOCATE DESCRIPTOR identifier;

要使用一个描述符区域，把它指定为INTO子句的存储目标（而不是列出主变量）：

EXEC SQL FETCH NEXT FROM mycursor INTO SQL DESCRIPTOR mydesc;

如果结果集为空，该描述符区域仍然会包含查询的元数据，即域的名称。

对于还没有执行的预备查询，DESCRIBE可以被用来得到其结果集的元数据：

EXEC SQL BEGIN DECLARE SECTION;

char \*sql\_stmt = "SELECT \* FROM table1";

EXEC SQL END DECLARE SECTION;

EXEC SQL PREPARE stmt1 FROM:sql\_stmt;

EXEC SQL DESCRIBE stmt1 INTO SQL DESCRIPTOR mydesc;

在DESCRIBE和FETCH语句中，INTO和USING关键词的使用相似：它们产生结果集以及一个描述符区域中的元数据。

现在我们如何从描述符区域得到数据呢？你可以把描述符区域看成是一个具有命名域的结构。要从头部检索一个域的值并且把它存储到一个主变量中，可使用下面的命令：

EXEC SQL GET DESCRIPTOR name:hostvar = field;

当前，只定义了一个头部域：COUNT，它告诉我们有多少个条目描述符区域（也就是，结果中包含多少列）。主变量需要是一个整数类型。要从条目描述符区域中得到一个域，可使用下面的命令：

EXEC SQL GET DESCRIPTOR name VALUE num:hostvar = field;

num可以是一个字面整数或者包含一个整数的主变量。可能的域有：

CARDINALITY （整数）

结果集中的行数

DATA

实际的数据项（因此，这个域的数据类型取决于查询）

DATETIME\_INTERVAL\_CODE （整数）

当TYPE是9时， DATETIME\_INTERVAL\_CODE将具有以下值之一： 1 表示 DATE， 2 表示TIME， 3 表示 TIMESTAMP， 4 表示 TIME WITH TIME ZONE， 5 表示 TIMESTAMP WITH TIME ZONE。

DATETIME\_INTERVAL\_PRECISION （整数）

没有实现INDICATOR （整数）

指示符（表示一个空值或者一个值截断）

KEY\_MEMBER （整数）

没有实现

LENGTH （整数）

以字符计的数据长度

NAME (string)

列名

NULLABLE （整数）

没有实现

OCTET\_LENGTH （整数）

以字节计的数据字符表达的长度

PRECISION （整数）

精度（用于类型numeric）

RETURNED\_LENGTH （整数）

以字符计的数据长度

RETURNED\_OCTET\_LENGTH （整数）

以字节计的数据字符表达的长度

SCALE （整数）

比例（用于类型numeric）

TYPE （整数）

列的数据类型的数字编码

在EXECUTE、DECLARE以及OPEN语句中，INTO和USING关键词的效果不同。也可以手工建立一个描述符区域来为一个查询或者游标提供输入参数，并且USING SQL DESCRIPTOR name是用来传递输入参数给参数化查询的方法。建立一个命名 SQL 描述符区域的语句如下：

EXEC SQL SET DESCRIPTOR name VALUE num field =:hostvar;

瀚高数据库支持在一个FETCH语句中检索多于一个记录并且在这种情况下把主变量假定为一个数组来存储数据。例如：

EXEC SQL BEGIN DECLARE SECTION;

int id\[5\];

EXEC SQL END DECLARE SECTION;

EXEC SQL FETCH 5 FROM mycursor INTO SQL DESCRIPTOR mydesc;

EXEC SQL GET DESCRIPTOR mydesc VALUE 1:id = DATA;

### SQLDA 描述符区域

SQLDA 描述符区域是一个C语言结构，它也能被用来得到一个查询的结果集和元数据。一个结构存储一个来自结果集的记录。

EXEC SQL include sqlda.h;

sqlda\_t \*mysqlda;

EXEC SQL FETCH 3 FROM mycursor INTO DESCRIPTOR mysqlda;

注意SQL关键词被省略了。在一个DESCRIBE语句中，如果使用了INTO关键词，则DESCRIPTOR关键词可以完全被省略：

EXEC SQL DESCRIBE prepared\_statement INTO mysqlda;

使用 SQLDA 的程序的一般流程是：

1\. 准备一个查询，并且为它声明一个游标。

2\. 为结果行声明一个 SQLDA 。

3\. 为输入参数声明一个 SQLDA，并且初始化它们（内存分配、参数设置）。

4\. 用输入 SQLDA 打开一个游标。

5\. 从游标中取得行，并且把它们存储到一个输出 SQLDA。

6\. 从输出 SQLDA 读取值到主变量中（必要时使用转换）。

7\. 关闭游标。

8\. 关闭为输入 SQLDA 分配的内存区域。

#### SQLDA 数据结构

SQLDA 使用三种数据结构类型：sqlda\_t、sqlvar\_t以及struct sqlname。

##### sqlda\_t 结构

结构类型sqlda\_t是实际 SQLDA 的类型。它保存一个记录。并且两个或者更多个sqlda\_t结构能够以desc\_next域中的指针连接成一个链表，这样可以表示一个有序的行集合。因此，当两个或多个行被取得时，应用可以通过沿着每一个sqlda\_t节点中的desc\_next指针读取它们。

sqlda\_t的定义是：

struct sqlda\_struct

{

char sqldaid\[8\];

long sqldabc;

short sqln;

short sqld;

struct sqlda\_struct \*desc\_next;

struct sqlvar\_struct sqlvar\[1\];

};

typedef struct sqlda\_struct sqlda\_t;

域的含义是：

sqldaid

它包含一个字符串"SQLDA "。

sqldabc

它包含已分配空间的尺寸（以字节计）。

sqln

当它被传递给使用USING关键词的OPEN、DECLARE或者EXECUTE语句时，它包含用于一个参数化查询实例的输入参数的数目。在它被用作SELECT、EXECUTE或FETCH语句的输出时，它的值和sqld一样。

sqld

它包含一个结果集中的域的数量。

desc\_next

如果查询返回不止一个记录，会返回多个链接在一起的 SQLDA 结构，并且desc\_next保存一个指向下一个项的指针。

sqlvar

这是结果集中列的数组。

##### sqlvar\_t 结构

结构类型sqlvar\_t保存一个列值和元数据（例如类型和长度）。该类型的定义是：

struct sqlvar\_struct

{

short sqltype;

short sqllen;

char \*sqldata;

short \*sqlind;

struct sqlname sqlname;

};

typedef struct sqlvar\_struct sqlvar\_t;

各个域的含义是：

sqltype

包含该域的类型标识符。值可以参考ecpgtype.h中的enum ECPGttype。

sqllen

包含域的二进制长度，例如ECPGt\_int是 4 字节。

sqldata

指向数据。数据的格式在 类型映射 章节中描述。

sqlind

指向空指示符。0 表示非空，-1 表示空。

sqlname

域的名称。

##### struct sqlname 结构

一个struct sqlname结构保持一个列名。它被用作sqlvar\_t结构的一个成员。该结构的定义是：

#define NAMEDATALEN 64

struct sqlname

{

short length;

char data\[NAMEDATALEN\];

};

各个域的含义是：

length

包含域名称的长度。

data

包含实际的域名称。

#### 使用一个 SQLDA 检索一个结果集

通过一个 SQLDA 检索一个查询结果集的一般步骤是：

1\. 声明一个sqlda\_t结构来接收结果集。

2\. 执行 FETCH/EXECUTE/DESCRIBE 命令来处理一个指定已声明 SQLDA 的查询。

3\. 通过查看sqlda\_t结构的成员sqln来检查结果集中记录的数量。

4\. 从sqlda\_t结构的成员sqlvar\[0\]、sqlvar\[1\]等中得到每一列的值。

5\. 沿着sqlda\_t结构的成员desc\_next指针到达下一行（sqlda\_t）。

6\. 根据你的需要重复上述步骤。

这里是一个通过 SQLDA 检索结果集的例子。

首先，声明一个sqlda\_t结构来接收结果集。

sqlda\_t \*sqlda1;

接下来，指定一个命令中的 SQLDA。这是一个FETCH命令的例子。

EXEC SQL FETCH NEXT FROM cur1 INTO DESCRIPTOR sqlda1;

运行一个循环顺着链表来检索行。

sqlda\_t \*cur\_sqlda;

for (cur\_sqlda = sqlda1;

cur\_sqlda!= NULL;

cur\_sqlda = cur\_sqlda->desc\_next)

{

...

}

在循环内部，运行另一个循环来检索行中每一列的数据（sqlvar\_t结构）。

for (i = 0; i < cur\_sqlda->sqld; i++)

{

sqlvar\_t v = cur\_sqlda->sqlvar\[i\];

char \*sqldata = v.sqldata;

short sqllen = v.sqllen;

...

}

要得到一列的值，应检查sqlvar\_t结构的成员sqltype的值。然后，根据列类型切换到一种合适的方法从sqlvar域中复制数据到一个主变量。

char var\_buf\[1024\];

switch (v.sqltype)

{

case ECPGt\_char:

memset(&var\_buf, 0, sizeof(var\_buf));

memcpy(&var\_buf, sqldata, (sizeof(var\_buf) <= sqllen? sizeof(var\_buf) - 1: sqllen));

break;

case ECPGt\_int: /\* integer \*/

memcpy(&intval, sqldata, sqllen);

snprintf(var\_buf, sizeof(var\_buf), "%d", intval);

break;

...

}

#### 使用一个 SQLDA 传递查询参数

使用一个 SQLDA 传递输入参数给一个预备查询的一般步骤是：

1\. 创建一个预备查询（预备语句）。

2\. 声明一个 sqlda\_t 结构作为输入 SQLDA。

3\. 为输入 SQLDA 分配内存区域（作为 sqlda\_t 结构）。

4\. 在分配好的内存中设置（复制）输入值。

5\. 打开一个说明了输入 SQLDA 的游标。

这里是一个例子。

首先，创建一个预备语句。

EXEC SQL BEGIN DECLARE SECTION;

char query\[1024\] = "SELECT d.oid, \* FROM pg\_database d, pg\_stat\_database s WHERE d.oid = s.datid AND (d.datname =? OR d.oid =?)";

EXEC SQL END DECLARE SECTION;

EXEC SQL PREPARE stmt1 FROM:query;

接下来为一个 SQLDA 分配内存，并且在sqlda\_t结构的sqln成员变量中设置输入参数的数量。当预备查询要求两个或多个输入参数时，应用必须分配额外的内存空间，空间的大小为 (参数数目 - 1) \* sizeof(sqlvar\_t)。这里的例子展示了为两个输入参数分配内存空间。

sqlda\_t \*sqlda2;

sqlda2 = (sqlda\_t \*) malloc(sizeof(sqlda\_t) + sizeof(sqlvar\_t));

memset(sqlda2, 0, sizeof(sqlda\_t) + sizeof(sqlvar\_t));

sqlda2->sqln = 2; /\* 输入变量的数目 \*/

内存分配之后，把参数值存储到sqlvar\[\]数组（当 SQLDA 在接收结果集时，这也是用来检索列值的数组）。在这个例子中，输入参数是"highgo"（字符串类型）和1（整数类型）。

sqlda2->sqlvar\[0\].sqltype = ECPGt\_char;

sqlda2->sqlvar\[0\].sqldata = "highgo";

sqlda2->sqlvar\[0\].sqllen = 8;

int intval = 1;

sqlda2->sqlvar\[1\].sqltype = ECPGt\_int;

sqlda2->sqlvar\[1\].sqldata = (char \*) &intval;

sqlda2->sqlvar\[1\].sqllen = sizeof(intval);

通过打开一个游标并且说明之前已经建立好的 SQLDA，输入参数被传递给预备语句。

EXEC SQL OPEN cur1 USING DESCRIPTOR sqlda2;

最后，用完输入 SQLDA 后必须显式地释放已分配的内存空间，这与用于接收查询结果的 SQLDA 不同。

free(sqlda2);

#### 一个使用 SQLDA 的应用例子

这里是一个例子程序，它描述了如何按照输入参数的指定从系统目录中取得数据库的访问统计。

这个应用在数据库 OID 上连接两个系统表（pg\_database 和 pg\_stat\_database），并且还取得和显示通过两个输入参数（一个数据库highgo和 OID 1）检索到的数据库统计。

首先，为输入和输出分别声明一个 SQLDA。

EXEC SQL include sqlda.h;

sqlda\_t \*sqlda1; /\* 一个输出描述符 \*/

sqlda\_t \*sqlda2; /\* 一个输入描述符 \*/

接下来，连接到数据库，准备一个语句并且为预备语句声明一个游标。

int

main(void)

{

EXEC SQL BEGIN DECLARE SECTION;

char query\[1024\] = "SELECT d.oid,\* FROM pg\_database d, pg\_stat\_database s

WHERE d.oid=s.datid AND ( d.datname=? OR d.oid=? )";

EXEC SQL END DECLARE SECTION;

EXEC SQL CONNECT TO testdb AS con1 USER testuser;

EXEC SQL SELECT pg\_catalog.set\_config('search\_path', '', false); EXEC SQL

COMMIT;

EXEC SQL PREPARE stmt1 FROM:query;

EXEC SQL DECLARE cur1 CURSOR FOR stmt1;

然后，为输入参数在输入 SQLDA 中放入一些值。为输入 SQLDA 分配内存，并且在sqln中设置输入参数的数目。在sqlvar结构的sqltype、sqldata和sqllen中存入类型、值和值长度。

/\* 为输入参数创建 SQLDA 结构。 \*/

sqlda2 = (sqlda\_t \*) malloc(sizeof(sqlda\_t) + sizeof(sqlvar\_t));

memset(sqlda2, 0, sizeof(sqlda\_t) + sizeof(sqlvar\_t));

sqlda2->sqln = 2; /\* 输入变量的数量 \*/

sqlda2->sqlvar\[0\].sqltype = ECPGt\_char;

sqlda2->sqlvar\[0\].sqldata = "highgo";

sqlda2->sqlvar\[0\].sqllen = 8;

intval = 1;

sqlda2->sqlvar\[1\].sqltype = ECPGt\_int;

sqlda2->sqlvar\[1\].sqldata = (char \*)&intval;

sqlda2->sqlvar\[1\].sqllen = sizeof(intval);

设置完输入 SQLDA 之后，用输入 SQLDA 打开一个游标。

/\* 用输入参数打开一个游标。 \*/

EXEC SQL OPEN cur1 USING DESCRIPTOR sqlda2;

从打开的游标中取行到输出 SQLDA 中（通常，你不得不在循环中反复调用FETCH来取出结果集中的所有行）。

while (1)

{

sqlda\_t \*cur\_sqlda;

/\* 分配描述符给游标 \*/

EXEC SQL FETCH NEXT FROM cur1 INTO DESCRIPTOR sqlda1;

再后，沿着sqlda\_t结构的链表从 SQLDA 中检索取得的记录。

for (cur\_sqlda = sqlda1;

cur\_sqlda!= NULL;

cur\_sqlda = cur\_sqlda->desc\_next)

{

...

读取第一个记录中的每一列。列的数量被存储在sqld中，第一列的实际数据被存储在sqlvar\[0\]中，两者都是sqlda\_t结构的成员。

/\* 打印一行中的每一列。 \*/

for (i = 0; i < sqlda1->sqld; i++)

{

sqlvar\_t v = sqlda1->sqlvar\[i\];

char \*sqldata = v.sqldata;

short sqllen = v.sqllen;

strncpy(name\_buf, v.sqlname.data, v.sqlname.length);

name\_buf\[v.sqlname.length\] = '\\0';

现在，列数据已经被存在了变量v中。把每个数据复制到主变量中，列的类型可以查看。

switch (v.sqltype) {

int intval;

double doubleval;

unsigned long long int longlongval;

case ECPGt\_char:

memset(&var\_buf, 0, sizeof(var\_buf));

memcpy(&var\_buf, sqldata, (sizeof(var\_buf) <= sqllen?

sizeof(var\_buf)-1: sqllen));

break;

case ECPGt\_int: /\* 整数 \*/

memcpy(&intval, sqldata, sqllen);

snprintf(var\_buf, sizeof(var\_buf), "%d", intval);

break;

...

default:

...

}

printf("%s = %s (type: %d)\\n", name\_buf, var\_buf, v.sqltype);

}

处理所有记录后关闭游标，并且从数据库断开连接。

EXEC SQL CLOSE cur1;

EXEC SQL COMMIT;

EXEC SQL DISCONNECT ALL;

整个程序显示在例 3.1中。

例 3.1. 示例 SQLDA 程序

#include <stdlib.h>

#include <string.h>

#include <stdlib.h>

#include <stdio.h>

#include <unistd.h>

EXEC SQL include sqlda.h;

sqlda\_t \*sqlda1; /\* 用于输出的描述符 \*/

sqlda\_t \*sqlda2; /\* 用于输入的描述符 \*/

EXEC SQL WHENEVER NOT FOUND DO BREAK;

EXEC SQL WHENEVER SQLERROR STOP;

int

main(void)

{

EXEC SQL BEGIN DECLARE SECTION;

char query\[1024\] = "SELECT d.oid,\* FROM pg\_database d, pg\_stat\_database s

WHERE d.oid=s.datid AND ( d.datname=? OR d.oid=? )";

int intval;

unsigned long long int longlongval;

EXEC SQL END DECLARE SECTION;

EXEC SQL CONNECT TO uptimedb AS con1 USER uptime;

EXEC SQL SELECT pg\_catalog.set\_config('search\_path', '', false); EXEC SQL

COMMIT;

EXEC SQL PREPARE stmt1 FROM:query;

EXEC SQL DECLARE cur1 CURSOR FOR stmt1;

/\* 为一个输入参数创建一个 SQLDA 结构 \*/

sqlda2 = (sqlda\_t \*)malloc(sizeof(sqlda\_t) + sizeof(sqlvar\_t));

memset(sqlda2, 0, sizeof(sqlda\_t) + sizeof(sqlvar\_t));

sqlda2->sqln = 2; /\* 输入变量的数量 \*/

sqlda2->sqlvar\[0\].sqltype = ECPGt\_char;

sqlda2->sqlvar\[0\].sqldata = "highgo";

sqlda2->sqlvar\[0\].sqllen = 8;

intval = 1;

sqlda2->sqlvar\[1\].sqltype = ECPGt\_int;

sqlda2->sqlvar\[1\].sqldata = (char \*) &intval;

sqlda2->sqlvar\[1\].sqllen = sizeof(intval);

/\* 用输入参数打开一个游标。 \*/

EXEC SQL OPEN cur1 USING DESCRIPTOR sqlda2;

while (1)

{

sqlda\_t \*cur\_sqlda;

/\* 给游标分配描述符 \*/

EXEC SQL FETCH NEXT FROM cur1 INTO DESCRIPTOR sqlda1;

for (cur\_sqlda = sqlda1;

cur\_sqlda!= NULL;

cur\_sqlda = cur\_sqlda->desc\_next)

{

int i;

char name\_buf\[1024\];

char var\_buf\[1024\];

/\* 打印一行中的每一列。 \*/

for (i=0; i<cur\_sqlda->sqld; i++)

{

sqlvar\_t v = cur\_sqlda->sqlvar\[i\];

char \*sqldata = v.sqldata;

short sqllen = v.sqllen;

strncpy(name\_buf, v.sqlname.data, v.sqlname.length);

name\_buf\[v.sqlname.length\] = '\\0';

switch (v.sqltype)

{

case ECPGt\_char:

memset(&var\_buf, 0, sizeof(var\_buf));

memcpy(&var\_buf, sqldata, (sizeof(var\_buf)<=sqllen?

sizeof(var\_buf)-1: sqllen) );

break;

case ECPGt\_int: /\* 整数 \*/

memcpy(&intval, sqldata, sqllen);

snprintf(var\_buf, sizeof(var\_buf), "%d", intval);

break;

case ECPGt\_long\_long: /\* 大整数 \*/

memcpy(&longlongval, sqldata, sqllen);

snprintf(var\_buf, sizeof(var\_buf), "%lld", longlongval);

break;

default:

{

int i;

memset(var\_buf, 0, sizeof(var\_buf));

for (i = 0; i < sqllen; i++)

{

char tmpbuf\[16\];

snprintf(tmpbuf, sizeof(tmpbuf), "%02x ", (unsigned char) sqldata\[i\]);

strncat(var\_buf, tmpbuf, sizeof(var\_buf));

}

}

break;

}

printf("%s = %s (type: %d)\\n", name\_buf, var\_buf, v.sqltype);

}

printf("\\n");

}

}

EXEC SQL CLOSE cur1;

EXEC SQL COMMIT;

EXEC SQL DISCONNECT ALL;

return 0;

}

这个例子的输出应该看起来类似下面的结果（一些数字会变化）。

oid = 1 (type: 1)

datname = template1 (type: 1)

datdba = 10 (type: 1)

encoding = 0 (type: 5)

datistemplate = t (type: 1)

datallowconn = t (type: 1)

datconnlimit = -1 (type: 5)

datlastsysoid = 11510 (type: 1)

datfrozenxid = 379 (type: 1)

dattablespace = 1663 (type: 1)

datconfig = (type: 1)

datacl = {=c/uptime,uptime=CTc/uptime} (type: 1)

datid = 1 (type: 1)

datname = template1 (type: 1)

numbackends = 0 (type: 5)

xact\_commit = 113606 (type: 9)

xact\_rollback = 0 (type: 9)

blks\_read = 130 (type: 9)

blks\_hit = 7341714 (type: 9)

tup\_returned = 38262679 (type: 9)

tup\_fetched = 1836281 (type: 9)

tup\_inserted = 0 (type: 9)

tup\_updated = 0 (type: 9)

tup\_deleted = 0 (type: 9)

oid = 11511 (type: 1)

datname = highgo (type: 1)

datdba = 10 (type: 1)

encoding = 0 (type: 5)

datistemplate = f (type: 1)

datallowconn = t (type: 1)

datconnlimit = -1 (type: 5)

datlastsysoid = 11510 (type: 1)

datfrozenxid = 379 (type: 1)

dattablespace = 1663 (type: 1)

datconfig = (type: 1)

datacl = (type: 1)

datid = 11511 (type: 1)

datname = highgo (type: 1)

numbackends = 0 (type: 5)

xact\_commit = 221069 (type: 9)

xact\_rollback = 18 (type: 9)

blks\_read = 1176 (type: 9)

blks\_hit = 13943750 (type: 9)

tup\_returned = 77410091 (type: 9)

tup\_fetched = 3253694 (type: 9)

tup\_inserted = 0 (type: 9)

tup\_updated = 0 (type: 9)

tup\_deleted = 0 (type: 9)

## 错误处理

这一节描述在一个嵌入式 SQL 程序中如何处理异常情况和警告。有两种非互斥的工具可以用于这个目的。

• 可以使用WHENEVER命令配置回调来处理警告和错误情况。

• 可以从sqlca变量中获得错误或警告的详细信息。

### 设置回调

一种捕捉错误和警告的简单方法是设置一个特殊的动作，只要一个特定情况发生就执行该动作。通常是这样：

EXEC SQL WHENEVER condition action;

condition可以是下列之一：

SQLERROR

只要在 SQL 语句执行期间发生一个错误就调用指定的动作。

SQLWARNING

只要在 SQL 语句执行期间发生一个警告就调用指定的动作。

NOT FOUND

只要一个 SQL 语句检索或者影响零行就调用指定的动作（这种情况不是一个错误，但是你可能需要特别地处理它）。

action可以是下列之一：

CONTINUE

这实际上表示该情况被忽略。这是默认值。

GOTO label

GO TO label

调到指定的标签（使用一个Cgoto语句）。

SQLPRINT

把一个消息打印到标准错误。对于简单程序或原型开发中这很有用。消息的细节无法配置。

STOP

调用exit(1)终止程序。

DO BREAK

执行C语句break。只应被用在循环或switch语句中。

DO CONTINUE

执行C语句continue。这应该只被用在循环语句中。如果被执行，将导致控制流返回到循环的顶层。

CALL name (args)

DO name (args)

用指定参数调用指定的C函数（这种用法不同于正常瀚高数据库语法中CALL和DO的含义）。

SQL 标准只提供动作CONTINUE和GOTO（以及GO TO）。

这里有一个可能会用在简单程序中的例子。当一个警告发生时它打印一个简单消息，而发生一个错误时它会中止程序：

EXEC SQL WHENEVER SQLWARNING SQLPRINT;

EXEC SQL WHENEVER SQLERROR STOP;

语句EXEC SQL WHENEVER是 SQL 预处理器的一个指令，而不是一个C语句。不管C程序的控制流程如何，该语句设置的错误或警告动作适用于所有位于处理程序设置点之后的嵌入式 SQL 语句，除非在第一个EXEC SQL WHENEVER和导致情况的 SQL 语句之间为同一个情况设置了不同的动作。因此下面的两个C程序都不会得到预期的效果：

/\*

\* 错误

\*/

int main(int argc, char \*argv\[\])

{

...

if (verbose) {

EXEC SQL WHENEVER SQLWARNING SQLPRINT;

}

...

EXEC SQL SELECT...;

...

}

/\*

\* 错误

\*/

int main(int argc, char \*argv\[\])

{

...

set\_error\_handler();

...

EXEC SQL SELECT...;

...

}

static void set\_error\_handler(void)

{

EXEC SQL WHENEVER SQLERROR STOP;

}

### Sqlca

为了更强大的错误处理，嵌入式 SQL 接口提供了一个名为sqlca（SQL 通讯区域）的全局变量，它具有下面的结构：

struct

{

char sqlcaid\[8\];

long sqlabc;

long sqlcode;

struct

{

int sqlerrml;

char sqlerrmc\[SQLERRMC\_LEN\];

} sqlerrm;

char sqlerrp\[8\];

long sqlerrd\[6\];

char sqlwarn\[8\];

char sqlstate\[5\];

} sqlca;

（在一个多线程程序中，每一个线程会自动得到它自己的sqlca副本。这和对于标准C全局变量errno的处理相似。）

sqlca覆盖了警告和错误。如果执行一个语句时发生了多个警告或错误，那么sqlca将只包含关于最后一个的信息。

如果在上一个SQL语句中没有产生错误，sqlca.sqlcode将为 0 并且sqlca.sqlstate将为"00000"。如果发生一个警告或错误，则sqlca.sqlcode将为负并且sqlca.sqlstate将不为"00000"。一个正的sqlca.sqlcode表示一种无害的情况，例如上一个查询返回零行。sqlcode和sqlstate是两种不同的错误代码模式，详见下文。

如果上一个 SQL 语句成功，那么sqlca.sqlerrd\[1\]包含被处理行的 OID （如果可用），并且sqlca.sqlerrd\[2\]包含被处理或被返回的行数（如果适用于该命令）。

在发生一个错误或警告的情况下，sqlca.sqlerrm.sqlerrmc将包含一个描述该错误的字符串。域sqlca.sqlerrm.sqlerrml包含存储在sqlca.sqlerrm.sqlerrmc中错误消息的长度（strlen()的结果，对于一个C程序员来说并不感兴趣）。注意一些消息可能太长不能适应定长的sqlerrmc数组，它们将被截断。

在发生一个警告的情况下，sqlca.sqlwarn\[2\]被设置为W（在所有其他情况中，它被设置为不同于W的东西）。如果sqlca.sqlwarn\[1\]被设置为W，那么一个值被存储在一个主变量中时会被截断。如果任意其他元素被设置为指示一个警告，sqlca.sqlwarn\[0\]会被设置为W。

域sqlcaid、sqlabc, sqlerrp以及 sqlerrd的剩余元素还有 sqlwarn当前不包含有用的信息。

SQL 标准中没有定义sqlca结构，但是在一些其他的 SQL 数据系统中都有实现。在核心上这些定义都想死，但是如果你想要编写可移植的应用，那么你应该仔细研究不同的实现。

这里有一个整合使用WHENEVER和sqlca的例子，当一个错误发生时打印出sqlca的内容。在安装一个更”用户友好”的错误处理器之前，这可能对调试或开发原型应用有用。

EXEC SQL WHENEVER SQLERROR CALL print\_sqlca();

void

print\_sqlca()

{

fprintf(stderr, "==== sqlca ====\\n");

fprintf(stderr, "sqlcode: %ld\\n", sqlca.sqlcode);

fprintf(stderr, "sqlerrm.sqlerrml: %d\\n", sqlca.sqlerrm.sqlerrml);

fprintf(stderr, "sqlerrm.sqlerrmc: %s\\n", sqlca.sqlerrm.sqlerrmc);

fprintf(stderr, "sqlerrd: %ld %ld %ld %ld %ld %ld\\n",

sqlca.sqlerrd\[0\],sqlca.sqlerrd\[1\],sqlca.sqlerrd\[2\],

sqlca.sqlerrd\[3\],sqlca.sqlerrd\[4\],sqlca.sqlerrd\[5\]);

fprintf(stderr, "sqlwarn: %d %d %d %d %d %d %d %d\\n", sqlca.sqlwarn\[0\],

sqlca.sqlwarn\[1\], sqlca.sqlwarn\[2\],

sqlca.sqlwarn\[3\],

sqlca.sqlwarn\[4\], sqlca.sqlwarn\[5\],

sqlca.sqlwarn\[6\],

sqlca.sqlwarn\[7\]);

fprintf(stderr, "sqlstate: %5s\\n", sqlca.sqlstate);

fprintf(stderr, "===============\\n");

}

结果看起来像（这里的错误是一个拼写错误的表名）：

\==== sqlca ====

sqlcode: -400

sqlerrm.sqlerrml: 49

sqlerrm.sqlerrmc: relation "pg\_databasep" does not exist on line 38

sqlerrd: 0 0 0 0 0 0

sqlwarn: 0 0 0 0 0 0 0 0

sqlstate: 42P01

\===============

### SQLSTATE 与 SQLCODE

域sqlca.sqlstate以及sqlca.sqlcode是提供错误代码的两种不同模式。两种都源自于 SQL标准，但是在标准的 SQL-92 版本中SQLCODE已经被标记为弃用并且在后面的版本中被删除。因此，强烈建议新应用使用SQLSTATE。

SQLSTATE是一个五字符数组。这五个字符包含数字或大写字母，它表示多种错误或警告情况的代码。SQLSTATE具有一种层次模式：前两个字符表示情况的总体分类，后三个字符表示总体情况的子类。代码00000表示一种成功的状态。SQL 标准中的大部分都有对应的SQLSTATE代码。瀚高数据库服务本地支持SQLSTATE错误代码，因此通过在所有应用中自始至终使用这种错误代码模式可以实现高度的一致性。

被弃用的错误代码模式SQLCODE是一个简单的整数。值为 0 表示成功，一个正值表示带附加信息的成功，一个负值表示一个错误。SQL 标准只定义了正值 +100，它表示上一个命令返回或者影响了零行，并且没有特定的负值。因此，这种模式只能实现很可怜的可移植性并且不具有层次性的代码分配。瀚高数据库的嵌入式 SQL 处理器已经分配了一些特定的SQLCODE值供它使用，它们的数字值和符号名称被列在下文。记住这些对其他 SQL 实现不是可移植的。为了简化移植应用到SQLSTATE模式，对应的SQLSTATE也被列出。不过，在两种模式之间没有一对一或者一对多的映射（事实上是多对多）。

这些是已分配的SQLCODE值：

0 (ECPG\_NO\_ERROR)

表示没有错误（SQLSTATE 00000）。

100 (ECPG\_NOT\_FOUND)

这是一种无害情况，它表示上一个命令检索或者处理了零行，或者你到达了游标的末尾（SQLSTATE 02000）。

在一个循环中处理一个游标时，你可以使用这个代码作为一种方法来检测何时中止该循环，像这样：

while (1)

{

EXEC SQL FETCH...;

if (sqlca.sqlcode == ECPG\_NOT\_FOUND)

break;

}

但是WHENEVER NOT FOUND DO BREAK实际上会在内部这样做，因此显式地把它写出来通常没有什么好处。

\-12 (ECPG\_OUT\_OF\_MEMORY)

表示你的虚拟内存已被耗尽。数字值被定义为-ENOMEM（SQLSTATE YE001）。

\-200 (ECPG\_UNSUPPORTED)

表示预处理器已经产生了一些该库不知道的东西。也许你正在运行一个不兼容版本的预处理和库（SQLSTATE YE002）。

\-201 (ECPG\_TOO\_MANY\_ARGUMENTS)

这表示命令指定了超过该命令预期数量的主变量（SQLSTATE 07001 或 07002）。

\-202 (ECPG\_TOO\_FEW\_ARGUMENTS)

这表示命令指定的主变量数量低于该命令的预期（SQLSTATE 07001 或 07002）

\-203 (ECPG\_TOO\_MANY\_MATCHES)

这意味着一个查询已经返回了多个行，但是该语句只准备存储一个结果行（例如，因为指定的变量不是数组）（SQLSTATE 21000）。

\-204 (ECPG\_INT\_FORMAT)

主变量是类型int而数据库中的数据是一种不同的类型并且含有一个不能被解释为int的值。该库使用strtol()进行这种转换（SQLSTATE 42804）。

\-205 (ECPG\_UINT\_FORMAT)

主变量是类型unsigned int而数据库中的数据是一种不同的类型并且含有一个不能被解释为unsigned int的值。该库使用strtoul()进行这种转换（SQLSTATE 42804）。

\-206 (ECPG\_FLOAT\_FORMAT)

主变量是类型float而数据库中的数据是另一种类型并且含有一个不能被解释为float的值。该库使用strtod()进行这种转换（SQLSTATE 42804）。

\-207 (ECPG\_NUMERIC\_FORMAT)

主变量是类型numeric而数据库中的数据是另一种类型并且含有一个不能被解释为numeric的值（SQLSTATE 42804）。

\-208 (ECPG\_INTERVAL\_FORMAT)

主变量是类型interval而数据库中的数据是另一种类型并且含有一个不能被解释为interval的值（SQLSTATE 42804）。

\-209 (ECPG\_DATE\_FORMAT)

主变量是类型date而数据库中的数据是另一种类型并且含有一个不能被解释为date的值（SQLSTATE 42804）。

\-210 (ECPG\_TIMESTAMP\_FORMAT)

主变量是类型timestamp而数据库中的数据是另一种类型并且含有一个不能被解释为timestamp的值（SQLSTATE 42804）。

\-211 (ECPG\_CONVERT\_BOOL)

这表示主变量是类型bool而数据库中的数据既不是't'也不是'f'（SQLSTATE 42804）。

\-212 (ECPG\_EMPTY)

发送给瀚高数据库服务的语句是空的（通常在一个嵌入式 SQL 程序中不会发生，因此它可能指向一个内部错误）（SQLSTATE YE002）。

\-213 (ECPG\_MISSING\_INDICATOR)

返回了一个空值并且没有提供空值指示符（SQLSTATE 22002）。

\-214 (ECPG\_NO\_ARRAY)

在要求一个数组的地方使用了一个普通变量（SQLSTATE 42804）。

\-215 (ECPG\_DATA\_NOT\_ARRAY)

在一个要求数组值的地方数据库返回了一个普通变量（SQLSTATE 42804）。

\-216 (ECPG\_ARRAY\_INSERT)

该值不能被插入到数组（SQLSTATE 42804）。

\-220 (ECPG\_NO\_CONN)

程序尝试访问一个不存在的连接（SQLSTATE 08003）。

\-221 (ECPG\_NOT\_CONN)

程序尝试访问一个存在的连接但是它没有打开（这是一个内部错误）（SQLSTATE YE002）。

\-230 (ECPG\_INVALID\_STMT)

你尝试使用的语句还没有被准备好（SQLSTATE 26000）。

\-239 (ECPG\_INFORMIX\_DUPLICATE\_KEY)

重复键错误，违背唯一约束（Informix 兼容模式）（SQLSTATE 23505）。

\-240 (ECPG\_UNKNOWN\_DESCRIPTOR)

没有找到指定的描述符。你尝试使用的语句还没有被准备好（SQLSTATE 33000）。

\-241 (ECPG\_INVALID\_DESCRIPTOR\_INDEX)

指定的描述符超出范围（SQLSTATE 07009）。

\-242 (ECPG\_UNKNOWN\_DESCRIPTOR\_ITEM)

请求了一个非法的描述符（这是一个内部错误）（SQLSTATE YE002）。

\-243 (ECPG\_VAR\_NOT\_NUMERIC)

在执行一个动态语句期间，数据库返回了一个numeric值而主变量不是numeric的（SQLSTATE 07006）。

\-244 (ECPG\_VAR\_NOT\_CHAR)

在执行一个动态语句期间，数据库返回了一个非numeric值而主变量是numeric的（SQLSTATE 07006）。

\-284 (ECPG\_INFORMIX\_SUBSELECT\_NOT\_ONE)

子查询的结果不是单一行（Informix 兼容模式）（SQLSTATE 21000）。

\-400 (ECPG\_PGSQL)

瀚高数据库服务导致了某个错误。该消息包含来自瀚高数据库服务器的错误消息。

\-401 (ECPG\_TRANS)

瀚高数据库服务通知我们不能启动、提交或回滚事务（SQLSTATE 08007）。

\-402 (ECPG\_CONNECT)

到数据库的连接尝试没有成功（SQLSTATE 08001）。

\-403 (ECPG\_DUPLICATE\_KEY)

重复键错误，违背唯一约束（SQLSTATE 23505）。

\-404 (ECPG\_SUBSELECT\_NOT\_ONE)

子查询的结果不是单一行（SQLSTATE 21000）。

\-602 (ECPG\_WARNING\_UNKNOWN\_PORTAL)

指定了一个非法的游标名（SQLSTATE 34000）。

\-603 (ECPG\_WARNING\_IN\_TRANSACTION)

事务正在进行（SQLSTATE 25001）。

\-604 (ECPG\_WARNING\_NO\_TRANSACTION)

没有活动（正在进行）的事务（SQLSTATE 25P01）。

\-605 (ECPG\_WARNING\_PORTAL\_EXISTS)

指定了一个现有的游标名（SQLSTATE 42P03）。

## 预处理器指令

一些预处理器指令可以用来改变ecpg预处理器解析和处理一个文件的方式。

### 包括文件

要包括一个外部文件到你的嵌入式 SQL 程序中，可以用：

EXEC SQL INCLUDE filename;

EXEC SQL INCLUDE \<filename>;

EXEC SQL INCLUDE "filename";

嵌入式 SQL 预处理器将查找一个名为filename.h的文件，处理它并且把它包括在结果C输出中。这样，被包括文件中的嵌入式 SQL 语句会被正确地处理。

ecpg预处理器将以下列顺序在几个目录中搜索一个文件：

• 当前目录

• /usr/local/include

• 瀚高数据库的include目录（例如/usr/local/hgdb/include）

• /usr/include

但是当使用EXEC SQL INCLUDE "filename"时，只有当前目录会被搜索。

在每一个目录中，预处理器将首先按给定的文件名搜索，如果没有找到将会追加.h到文件名并且重试（除非指定的文件名已经具有该后缀）。

注意EXEC SQL INCLUDE不同于：

#include <filename.h>

因为这个文件不服从 SQL 命令预处理。自然地，你可以继续使用C的#include指令来包括其他头文件。

| 注意： |
| --- |
| 包括文件名是大小写敏感的，即使EXEC SQL INCLUDE命令的剩余部分遵守通常的 SQL 大小写敏感规则。 |

### define 和 undef 指令

与C中我们熟知的指令#define相似，嵌入式 SQL 具有类似的概念：

EXEC SQL DEFINE name;

EXEC SQL DEFINE name value;

因此你可以定义一个名称：

EXEC SQL DEFINE HAVE\_FEATURE;

并且你也可以定义常量：

EXEC SQL DEFINE MYNUMBER 12;

EXEC SQL DEFINE MYSTRING 'abc';

使用undef来移除一个之前的定义：

EXEC SQL UNDEF MYNUMBER;

当然在你的嵌入式 SQL 程序中你可以继续使用C版本的#define和#undef。区别在于你定义的值会在哪里被计算。如果你使用EXEC SQL DEFINE，那么ecpg预处理器会计算这些定义并且替换值。例如，如果你写：

EXEC SQL DEFINE MYNUMBER 12;

...

EXEC SQL UPDATE Tbl SET col = MYNUMBER;

那么ecpg将已经做过替换并且你的C编译器将永远不会看见名为MYNUMBER的任何名称或标识符。注意你不能把#define用于一个将要在一个嵌入式 SQL 查询中使用的常量，因为在这种情况下嵌入式 SQL 预编译器不能看到这个声明。

### ifdef、ifndef、else、elif 以及 endif 指令

你可以使用下列指定来有条件地编译代码小节：

EXEC SQL ifdef name;

检查一个name，如果已经用EXEC SQL define name创建了name就处理接下来的行。

EXEC SQL ifndef name;

检查一个name，如果没有用EXEC SQL define name创建name就处理接下来的行。

EXEC SQL else;

为一个由EXEC SQL ifdef name或者EXEC SQL ifndef name引入的小节开始处理一个备选小节。

EXEC SQL elif name;

检查name，如果已经用EXEC SQL define name创建了name就开始处理一个备选小节。

EXEC SQL endif;

结束一个备选小节。

例子：

EXEC SQL ifndef TZVAR;

EXEC SQL SET TIMEZONE TO 'GMT';

EXEC SQL elif TZNAME;

EXEC SQL SET TIMEZONE TO TZNAME;

EXEC SQL else;

EXEC SQL SET TIMEZONE TO TZVAR;

EXEC SQL endif;

## 处理嵌入式 SQL 程序

现在你已经对如何构造嵌入式 SQLC程序有所了解了，你可能希望知道如何编译它们。在编译之前，你需要让该文件通过嵌入式SQL C预处理器，它会把你用到的SQL转换成特殊的函数调用。在编译之后，你必须链接一个包含所需函数的特殊库。这些函数从参数中取得信息、使用libpq执行SQL命令并且把结果放在指定的参数中用来输出。

该预处理器程序被称作ecpg并且被包括在一个正常的瀚高数据库安装中。嵌入式 SQL 程序通常带有扩展名.pgc。如果你有一个程序文件prog1.pgc，你可以调用下面的命令对它进行预处理：

ecpg prog1.pgc

这将创建一个文件prog1.c。如果你的输入文件不遵循建议的命名模式，你可以用-o选项显式地指定输出文件。

预处理过的文件可以被正常地编译，例如：

cc -c prog1.c

产生的C源文件从瀚高数据库安装中包括头文件，因此如果你把瀚高数据库安装在一个不被默认搜索的位置，你必须在编译命令行中增加一个选项（例如-I /usr/local/hgdb/include）。

要链接一个嵌入式 SQL 程序，你需要包括libecpg库，像这样：

cc -o myprog prog1.o prog2.o... -lecpg

再次，你可能不得不在命令行中增加类似-L /usr/local/hgdb/include的选项。

你可以使用pg\_config 或者pkg-config 加上包名libecpg来得到你的安装路径。

如果你使用make来管理一个大工程的构建过程，把下面的隐式规则包括在你的 makefile 中将会很方便：

ECPG = ecpg

%.c: %.pgc

$(ECPG) $<

ecpg命令的完整语法可见ecpg。

ecpg库默认是线程安全的。不过，你可能需要使用一些线程命令行选项来编译你的客户端代码。

## 库函数

libecpg库主要包含用于实现嵌入式 SQL 命令所表达功能的”隐藏”函数。但是也有一些可以被直接调用的函数。但是注意这会让你的代码不可移植。

• 如果调用时第一个参数非零，ECPGdebug(int on, FILE \*stream)会打开调试日志。调试日志在流上完成。该日志包含所有插入了输入变量的SQL语句，以及来自于瀚高数据库服务的结果。在你的SQL语句中查找错误时这会非常有用。

| 注意： |
| --- |
| 在 Windows 上，如果ecpg库和应用使用不同标志编译的，这个函数调用将会是应用崩溃，因为FILE指针的内部表达不同。特别地，库和使用库的应用应该使用相同的多线程/单线程、发行/调试以及静态/动态标志。 |

• ECPGget\_PGconn(const char \*connection\_name) 返回由给定名称标识的库数据库连接句柄。如果connection\_name被设置为NULL，当前连接句柄将被返回。如果无法定位到连接句柄，该函数返回NULL。如果需要，返回的连接句柄可以被用来调用任何其他来自于 libpq的函数。

| 注意： |
| --- |
| 直接使用libpq例程来操纵ecpg中建立的数据库连接句柄是一种糟糕的做法。 |

•ECPGtransactionStatus(const char \*connection\_name)返回由connection\_name标识的给定连接的当前事务状态。关于返回的状态代码请参考 连接状态函数 和 libpq的PQtransactionStatus()。

• 如果你连接到了一个数据库，ECPGstatus(int lineno, const char\* connection\_name)会返回真；否则返回假。 如果使用的是一个单一连接，connection\_name可以为NULL。

## 大对象

ECPG 并不直接支持大对象，在调用ECPGget\_PGconn()函数获得所需的PGconn对象后，ECPG应用能通过 libpq 大对象函数操纵大对象（不过，对ECPGget\_PGconn()函数的使用以及直接接触PGconn对象都必须非常小心，并且最好不要与其他 ECPG 数据库访问调用混合在一起）。

更多关于ECPGget\_PGconn()的细节可见 库函数 章节。大对象函数接口的相关信息可见 大对象 章节。

大对象函数必须在一个事务块中被调用，因此当自动提交关闭时，必须显式地发出BEGIN命令。

例 3.2给出了一个例子程序，它展示了在一个 ECPG 应用中如何创建、写入和读取一个大对象。

例 3.2. 访问大对象的 ECPG 程序

#include <stdio.h>

#include <stdlib.h>

#include <libpq-fe.h>

#include <libpq/libpq-fs.h>

EXEC SQL WHENEVER SQLERROR STOP;

int

main(void)

{

PGconn \*conn;

Oid loid;

int fd;

char buf\[256\];

int buflen = 256;

char buf2\[256\];

int rc;

memset(buf, 1, buflen);

EXEC SQL CONNECT TO testdb AS con1;

EXEC SQL SELECT pg\_catalog.set\_config('search\_path', '', false); EXEC SQL

COMMIT;

conn = ECPGget\_PGconn("con1");

printf("conn = %p\\n", conn);

/\* 创建 \*/

loid = lo\_create(conn, 0);

if (loid < 0)

printf("lo\_create() failed: %s", PQerrorMessage(conn));

printf("loid = %d\\n", loid);

/\* 写入测试 \*/

fd = lo\_open(conn, loid, INV\_READ|INV\_WRITE);

if (fd < 0)

printf("lo\_open() failed: %s", PQerrorMessage(conn));

printf("fd = %d\\n", fd);

rc = lo\_write(conn, fd, buf, buflen);

if (rc < 0)

printf("lo\_write() failed\\n");

rc = lo\_close(conn, fd);

if (rc < 0)

printf("lo\_close() failed: %s", PQerrorMessage(conn));

/\* 读取测试 \*/

fd = lo\_open(conn, loid, INV\_READ);

if (fd < 0)

printf("lo\_open() failed: %s", PQerrorMessage(conn));

printf("fd = %d\\n", fd);

rc = lo\_read(conn, fd, buf2, buflen);

if (rc < 0)

printf("lo\_read() failed\\n");

rc = lo\_close(conn, fd);

if (rc < 0)

printf("lo\_close() failed: %s", PQerrorMessage(conn));

/\* 检查 \*/

rc = memcmp(buf, buf2, buflen);

printf("memcmp() = %d\\n", rc);

/\* 清理 \*/

rc = lo\_unlink(conn, loid);

if (rc < 0)

printf("lo\_unlink() failed: %s", PQerrorMessage(conn));

EXEC SQL COMMIT;

EXEC SQL DISCONNECT ALL;

return 0;

}

## C++ 应用

ECPG 对于 C++ 应用提供了有限的支持。这一节描述了一些忠告。

ecpg预处理器采用一个用 C（或者类似C的东西）和嵌入式 SQL 命令编写的输入文件，把嵌入式 SQL 命令转换成C语言块，并且最终产生一个.c文件。

不过，通常ecpg预处理器只理解 C，它无法处理 C++ 语言的特殊语法和保留词。因此，一些写在 C++ 应用代码中的使用了 C++ 特定复杂特性的嵌入式 SQL 代码可能无法被正确地预处理或者无法按预期工作。

使用 C++ 应用中嵌入式 SQL 代码的安全方法是把 ECPG 调用隐藏在一个C模块中，C++ 应用代码会调用它来访问数据库，还要把它和剩余的 C++ 代码链接起来。

### 主变量的可见范围

ecpg预处理器能理解C中变量的可见范围。在C语言中，这是相当简单的，因为变量的可见范围是基于它们的代码块的。不过在 C++ 中，引用类成员变量的代码块是不同于定义它的代码块的，因此ecpg预处理器将无法理解类成员变量的可见范围。

例如，在下面的情况中，ecpg预处理器无法为test方法中的变量dbname找到任何生命，因此将发生一个错误。

class TestCpp

{

EXEC SQL BEGIN DECLARE SECTION;

char dbname\[1024\];

EXEC SQL END DECLARE SECTION;

public:

TestCpp();

void test();

~TestCpp();

};

TestCpp::TestCpp()

{

EXEC SQL CONNECT TO testdb1;

EXEC SQL SELECT pg\_catalog.set\_config('search\_path', '', false); EXEC SQL

COMMIT;

}

void Test::test()

{

EXEC SQL SELECT current\_database() INTO:dbname;

printf("current\_database = %s\\n", dbname);

}

TestCpp::~TestCpp()

{

EXEC SQL DISCONNECT ALL;

}

这段代码将导致一个这样的错误：

ecpg test\_cpp.pgc

test\_cpp.pgc:28: ERROR: variable "dbname" is not declared

为了避免这种可见性问题，可以修改test方法来把一个本地变量用作中间存储。但是这种方法只是一种比较差的变通方案，因为它让代码变得丑陋并且降低了性能。

void TestCpp::test()

{

EXEC SQL BEGIN DECLARE SECTION;

char tmp\[1024\];

EXEC SQL END DECLARE SECTION;

EXEC SQL SELECT current\_database() INTO:tmp;

strlcpy(dbname, tmp, sizeof(tmp));

printf("current\_database = %s\\n", dbname);

}

### 使用外部C模块的 C++ 应用开发

如果你理解了 C++ 中ecpg预处理器的这些技术限制，你可能已经知道在链接阶段把C对象和 C++ 对象链接起来让 C++ 应用能使用 ECPG 特性比直接在 C++ 代码中写一些嵌入式 SQL命令要更好。这一节用一个简单的例子描述了一种将嵌入式 SQL 命令从 C++ 应用代码中独立出去的方法。在这个例子中，应用由 C++ 实现，而C和 ECPG 被用来连接到 瀚高数据库服务器。

需要创建三种文件：一个C文件（\*.pgc）、一个头文件和一个 C++ 文件：

test\_mod.pgc

一个执行嵌入在C中的 SQL 命令的子例程模块。它将被预处理器转换成test\_mod.c。

#include "test\_mod.h"

#include <stdio.h>

void

db\_connect()

{

EXEC SQL CONNECT TO testdb1;

EXEC SQL SELECT pg\_catalog.set\_config('search\_path', '', false); EXEC SQL

COMMIT;

}

void

db\_test()

{

EXEC SQL BEGIN DECLARE SECTION;

char dbname\[1024\];

EXEC SQL END DECLARE SECTION;

EXEC SQL SELECT current\_database() INTO:dbname;

printf("current\_database = %s\\n", dbname);

}

void

db\_disconnect()

{

EXEC SQL DISCONNECT ALL;

}

test\_mod.h

包含C模块（test\_mod.pgc）中函数定义的头文件。它会被test\_cpp.cpp包括。这个文件必须在声明周围有一个extern "C"块，因为它将被链接到 C++ 模块。

#ifdef \_\_cplusplus

extern "C" {

#endif

void db\_connect();

void db\_test();

void db\_disconnect();

#ifdef \_\_cplusplus

}

#endif

test\_cpp.cpp

应用的主代码，包括main例程以及这个例子中的一个 C++ 类。

#include "test\_mod.h"

class TestCpp

{

public:

TestCpp();

void test();

~TestCpp();

};

TestCpp::TestCpp()

{

db\_connect();

}

void

TestCpp::test()

{

db\_test();

}

TestCpp::~TestCpp()

{

db\_disconnect();

}

int

main(void)

{

TestCpp \*t = new TestCpp();

t->test();

return 0;

}

要构建该应用，按以下步骤处理。通过运行ecpg将test\_mod.pgc转换为test\_mod.c，并且用C编译器将test\_mod.c编译成test\_mod.o：

ecpg -o test\_mod.c test\_mod.pgc

cc -c test\_mod.c -o test\_mod.o

接着，用 C++ 编译器把test\_cpp.cpp编译成test\_cpp.o：

c++ -c test\_cpp.cpp -o test\_cpp.o

最后，使用 C++ 编译器链接这些对象文件（test\_cpp.o和test\_mod.o）成为一个可执行文件：

c++ test\_cpp.o test\_mod.o -lecpg -o test\_cpp

## 嵌入式 SQL 命令

这一节描述嵌入式 SQL 所有特定的 SQL 命令。SQL 命令中的 SQL 命令也能被用于嵌入式 SQL，如果有例外会特别说明。