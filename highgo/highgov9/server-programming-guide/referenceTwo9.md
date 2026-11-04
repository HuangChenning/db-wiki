---
title: "PLPerl-Perl过程语言"
book: "服务器编程指南"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/reference/referenceTwo9.html"
tags:
  - highgo
  - highgo-v9
  - server-programming-guide
---

## PL/Perl - Perl 过程语言

PL/Perl 是一种可载入过程语言，它允许我们用 Perl 编程语言1编写瀚高数据库函数。

使用 PL/Perl 的主要优势它允许在存储函数中使用大量 Perl 的 “串整理”操作符和函数。

使用 Perl 解析复杂 串比使用 PL/pgSQL 中提供的串函数和控制结构要更容易。

要在一个特定数据库中安装 PL/Perl，使用 CREATE EXTENSION plperl。

| 提示： |
| --- |
| 如果把语言安装在template1中，所有后续创建的数据库 都将自动地安装有该语言。 |

| 注意： |
| --- |
| 使用源码包安装的用户必须在安装过程中开启对 PL/Perl 的编译。使用二进制包 安装的用户可能会在独立的子包中找到 PL/Perl。 |

## PL/Perl 函数和参数

要用 PL/Perl 语言创建一个函数，可使用标准的 CREATE FUNCTION语法：

CREATE FUNCTION funcname (argument-types) RETURNS return-type AS $$

\# PL/Perl 函数体

$$ LANGUAGE plperl;

函数的主体就是普通的 Perl 代码。事实上，PL/Perl 的粘合代码会把它 包裹在一个 Perl子程序中。一个 PL/Perl 函数会在一种标量上下文中 被调用，因此它无法返回列表。如下文所述，可以通过返回引用来返回 非标量值（数组、记录和集合）。

在一个PL/Perl过程中，任何从Perl代码返回的值都会被忽略。

PL/Perl 也支持用DO语句调用的匿名代码块：

DO $$

\# PL/Perl 代码

$$ LANGUAGE plperl;

一个匿名代码块没有参数，并且它返回的任何值都会被抛弃。否则 其行为就像一个函数。

| 注意： |
| --- |
| 在 Perl 中使用命名嵌套子程序是有危险的，特别是当它们在作用域内 引用局部变量时。因为 PL/Perl 函数被包装成一个子程序，任何放在 其中的命名子程序都会被嵌套。总之，创建通过 coderef 调用的匿名 子程序要安全得多。 |
| 更多信息可见 perldiag手册页 中的Variable "%s" will not stay shared以及 Variable "%s" is not available，或者在互联网上 搜索”perl nested named subroutine”。 |

CREATE FUNCTION命令的语法要求函数 体被写作一个字符串常量。通常对字符串常量使用美元引用（见 第 4.1.2.4 节）最方便。如果选择使用 转义字符串语法E''，必须双写任何在函数体中使用的单引号 （'）和反斜线（\\）（见 第 4.1.2.1 节）。

参数和结果的处理和在任何其他 Perl 子程序中一样：参数被传递到 @\_中，并且结果值用return 返回或者把函数中计算的最后一个表达式作为结果值。

例如，一个返回两个整数值中较大值的函数可以定义为：

CREATE FUNCTION perl\_max (integer, integer) RETURNS integer AS $$

if ($\_\[0\] > $\_\[1\]) { return $\_\[0\]; }

return $\_\[1\];

$$ LANGUAGE plperl;

| 注意： |
| --- |
| 参数将被从数据库的编码转换到 PL/Perl 中使用的 UTF-8，返回时再从 UTF-8转回到数据库编码。 |

如果一个 SQL 空值被传给一个函数，在 Perl 中该参数值将呈现为”undefined”。上述函数定义对于 空输入的行为不太好（实际上，它会把它们当作零）。我们可以为函数 定义增加STRICT让瀚高数据库干得更合理：如果空值被传入，函数将根本不会被调用，而只是自动 返回一个空结果。另外一种方式，我们可以在函数体中检查未定义的 输入。例如，假设我们想让带有一个空参数或者一个非空参数的 perl\_max返回非空参数而不是空值：

CREATE FUNCTION perl\_max (integer, integer) RETURNS integer AS $$

my ($x, $y) = @\_;

if (not defined $x) {

return undef if not defined $y;

return $y;

}

return $x if not defined $y;

return $x if $x > $y;

return $y;

$$ LANGUAGE plperl;

如上所述，要从一个 PL/Perl 函数返回一个 SQL 空值，就返回一个未定义值。 不管函数是严格的还是非严格的都可以这样做。

一个非引用的函数参数中的任何东西都是一个串，是相关数据类型的标准 瀚高数据库外部文本表达。在普通 数字或文本类型的情况下，Perl 将会做正确的事情并且程序员通常不需要 操心。不过，在其他情况下将需要被转换成在 Perl 中更可用的形式。例如， decode\_bytea函数可以被用来把类型 bytea的参数转换成未转义的二进制形式。

类似地，回传给瀚高数据库的值必须 是外部文本表达格式。例如，encode\_bytea 函数可以被用来转义二进制数据得到类型bytea的返回值。

Perl 可以把瀚高数据库数组返回为对 Perl 数组的引用。这里有一个例子：

CREATE OR REPLACE function returns\_array()

RETURNS text\[\]\[\] AS $$

return \[\['a"b','c,d'\],\['e\\\\f','g'\]\];

$$ LANGUAGE plperl;

select returns\_array();

Perl 把瀚高数据库数组作为被 bless 过的 PostgreSQL::InServer::ARRAY对象传递。这个对象可以被当作 一个数组引用或者一个串，例如：

CREATE OR REPLACE FUNCTION concat\_array\_elements(text\[\]) RETURNS TEXT AS $$

my $arg = shift;

my $result = "";

return undef if (!defined $arg);

\# as an array reference

for (@$arg) {

$result.= $\_;

}

\# also works as a string

$result.= $arg;

return $result;

$$ LANGUAGE plperl;

SELECT concat\_array\_elements(ARRAY\['PL','/','Perl'\]);

| 注意： |
| --- |
| 多维数组被以一种对每一个 Perl 程序员都公认的方法表示为对较低维引用数组的引用。 |

组合类型参数被作为哈希的引用传递给函数。哈希的键是组合类型的 属性名。这里是一个

例子：

CREATE TABLE employee (

name text,

basesalary integer,

bonus integer

);

CREATE FUNCTION empcomp(employee) RETURNS integer AS $$

my ($emp) = @\_;

return $emp->{basesalary} + $emp->{bonus};

$$ LANGUAGE plperl;

SELECT name, empcomp(employee.\*) FROM employee;

PL/Perl 函数可以使用相同的方法返回组合类型：返回具有所要求属性的 哈希的引用。例如：

CREATE TYPE testrowperl AS (f1 integer, f2 text, f3 text);

CREATE OR REPLACE FUNCTION perl\_row() RETURNS testrowperl AS $$

return {f2 => 'hello', f1 => 1, f3 => 'world'};

$$ LANGUAGE plperl;

SELECT \* FROM perl\_row();

任何所要求结果数据类型中不存在于哈希中的列将被返回为空值。

类似的，过程的输出参数也可以被返回为哈希引用：

CREATE PROCEDURE perl\_triple(INOUT a integer, INOUT b integer) AS $$

my ($a, $b) = @\_;

return {a => $a \* 3, b => $b \* 3};

$$ LANGUAGE plperl;

CALL perl\_triple(5, 10);

PL/Perl 函数也能返回标量或者组合类型集合。为了加速启动并且避免在 内存中让整个结果集排队等候，我们通常希望能一次返回一行。可以按 下文所说的用return\_next来这样做。

注意在 最后一次return\_next后，必须放上 return或者return undef（后者更好）。

CREATE OR REPLACE FUNCTION perl\_set\_int(int)

RETURNS SETOF INTEGER AS $$

foreach (0..$\_\[0\]) {

return\_next($\_);

}

return undef;

$$ LANGUAGE plperl;

SELECT \* FROM perl\_set\_int(5);

CREATE OR REPLACE FUNCTION perl\_set()

RETURNS SETOF testrowperl AS $$

return\_next({ f1 => 1, f2 => 'Hello', f3 => 'World' });

return\_next({ f1 => 2, f2 => 'Hello', f3 => 'PostgreSQL' });

return\_next({ f1 => 3, f2 => 'Hello', f3 => 'PL/Perl' });

return undef;

$$ LANGUAGE plperl;

对于小结果集，可以返回到一个数组的引用，该数组分别包含用于 简单类型、数组类型和组合类型的标量、数组引用或者哈希引用。 这里有一些简单的例子把整个结果集作为数组引用返回：

CREATE OR REPLACE FUNCTION perl\_set\_int(int) RETURNS SETOF INTEGER AS $$

return \[0..$\_\[0\]\];

$$ LANGUAGE plperl;

SELECT \* FROM perl\_set\_int(5);

CREATE OR REPLACE FUNCTION perl\_set() RETURNS SETOF testrowperl AS $$

return \[

{ f1 => 1, f2 => 'Hello', f3 => 'World' },

{ f1 => 2, f2 => 'Hello', f3 => 'PostgreSQL' },

{ f1 => 3, f2 => 'Hello', f3 => 'PL/Perl' }

\];

$$ LANGUAGE plperl;

SELECT \* FROM perl\_set();

如果你想要对你的代码使用strict编译指示，有几种选项可用。 对于临时的全局使用，你可以SET plperl.use\_strict为真。这将影响后续 PL/Perl函数的编译，但是对当前会话中已经编译过的 函数没有影响。对于持久的全局使用，可以在 postgresql.conf文件中设置 plperl.use\_strict为真。

对于在特定函数中的持久使用，可以简单地把

use strict;

放在函数体的顶层。

如果 Perl 版本是 5.10.0 或者更高，也可以使用 feature编译指示。

## PL/Perl 中的数据值

提供给 PL/Perl 函数代码的参数值是被转换成文本形式的输入参数（就像它们 被SELECT语句显示的那样）。反过来， return和return\_next命令 将接受任何该函数返回类型可接受的输入格式的串。

## 内建函数

### 从 PL/Perl 访问数据库

可以通过下列函数从 Perl 函数中访问数据库本身：

spi\_exec\_query(query \[, max-rows\])

spi\_exec\_query执行一个 SQL 命令并且以哈希引用数组 的引用的形式返回整个行集。只有在知道结果集相对较小时才 应该使用这个命令。这里是一个带有可选最大行数的查询（ SELECT命令）的例子：

$rv = spi\_exec\_query('SELECT \* FROM my\_table', 5);

这会从表my\_table.返回最多 5 行。如果 my\_table有一个列my\_column， 可以从结果的$i行得到值：

$foo = $rv->{rows}\[$i\]->{my\_column};

可以这样访问从一个SELECT查询返回 的总行数：

$nrows = $rv->{processed}

这里是使用不同命令类型的一个例子：

$query = "INSERT INTO my\_table VALUES (1, 'test')";

$rv = spi\_exec\_query($query);

你可以这样访问命令状态（例如SPI\_OK\_INSERT）：

$res = $rv->{status};

要得到受影响的行数：

$nrows = $rv->{processed};

这里是一个完整的例子：

CREATE TABLE test (

i int,

v varchar

);

INSERT INTO test (i, v) VALUES (1, 'first line');

INSERT INTO test (i, v) VALUES (2, 'second line');

INSERT INTO test (i, v) VALUES (3, 'third line');

INSERT INTO test (i, v) VALUES (4, 'immortal');

CREATE OR REPLACE FUNCTION test\_munge() RETURNS SETOF test AS $$

my $rv = spi\_exec\_query('select i, v from test;');

my $status = $rv->{status};

my $nrows = $rv->{processed};

foreach my $rn (0.. $nrows - 1) {

my $row = $rv->{rows}\[$rn\];

$row->{i} += 200 if defined($row->{i});

$row->{v} =~ tr/A-Za-z/a-zA-Z/ if (defined($row->{v}));

return\_next($row);

}

return undef;

$$ LANGUAGE plperl;

SELECT \* FROM test\_munge();

spi\_query(command)

spi\_fetchrow(cursor)

spi\_cursor\_close(cursor)

spi\_query和spi\_fetchrow 结对用于可能比较大的行集合，或者用于希望在行到达时返回的情况。 spi\_fetchrow只和 spi\_query一起工作。下面的例子展示了如何使用 它们：

CREATE TYPE foo\_type AS (the\_num INTEGER, the\_text TEXT);

CREATE OR REPLACE FUNCTION lotsa\_md5 (INTEGER) RETURNS SETOF foo\_type AS $$

use Digest::MD5 qw(md5\_hex);

my $file = '/usr/share/dict/words';

my $t = localtime;

elog(NOTICE, "opening file $file at $t" );

open my $fh, '<', $file # ooh, it's a file access!

or elog(ERROR, "cannot open $file for reading: $!");

my @words = <$fh>;

close $fh;

$t = localtime;

elog(NOTICE, "closed file $file at $t");

chomp(@words);

my $row;

my $sth = spi\_query("SELECT \* FROM generate\_series(1,$\_\[0\]) AS b(a)");

while (defined ($row = spi\_fetchrow($sth))) {

return\_next({

the\_num => $row->{a},

the\_text => md5\_hex($words\[rand @words\])

});

}

return;

$$ LANGUAGE plperlu;

SELECT \* from lotsa\_md5(500);

通常，spi\_fetchrow应该重复执行直到它返回

undef（表示没有更多行要读取）。当 spi\_fetchrow返回undef时， spi\_query返回的游标会自动被释放。如果不 想读取所有的行，可以调用spi\_cursor\_close来 释放游标。如果没有这样做会导致内存泄露。

spi\_prepare(command, argument types)

spi\_query\_prepared(plan, arguments)

spi\_exec\_prepared(plan \[, attributes\], arguments)

spi\_freeplan(plan)

spi\_prepare、spi\_query\_prepared、 spi\_exec\_prepared和spi\_freeplan 为预备查询实现了相同的功能。spi\_prepare接受一个查询 字符串，其中包括编好号的参数占位符（$1、$2 等）以及参数类型的字符串 列表：

$plan = spi\_prepare('SELECT \* FROM test WHERE id > $1 AND name = $2',

'INTEGER', 'TEXT');

一旦通过调用spi\_prepare准备好一个查询计划，就可以在

spi\_exec\_prepared（返

回的结果和spi\_exec\_query相同）或者spi\_query\_prepared （返回的结果

和spi\_query一样，后面会被传给spi\_fetchrow）中用该计划来取代字符串查询。

spi\_exec\_prepared可选的第二个参数是属性的哈希引用， 当前唯一支持的属性是limit，它限定了一个查询返回的最大行数。

预备查询的有点是可以把一个准备好的计划用于多次查询执行。不再需要该计划后， 可以用spi\_freeplan释放它：

CREATE OR REPLACE FUNCTION init() RETURNS VOID AS $$

$\_SHARED{my\_plan} = spi\_prepare('SELECT (now() + $1)::date AS now',

'INTERVAL');

$$ LANGUAGE plperl;

CREATE OR REPLACE FUNCTION add\_time( INTERVAL ) RETURNS TEXT AS $$

return spi\_exec\_prepared(

$\_SHARED{my\_plan},

$\_\[0\]

)->{rows}->\[0\]->{now};

$$ LANGUAGE plperl;

CREATE OR REPLACE FUNCTION done() RETURNS VOID AS $$

spi\_freeplan( $\_SHARED{my\_plan});

undef $\_SHARED{my\_plan};

$$ LANGUAGE plperl;

SELECT init();

SELECT add\_time('1 day'), add\_time('2 days'), add\_time('3 days');

SELECT done();

add\_time | add\_time | add\_time

\------------+------------+------------

2005-12-10 | 2005-12-11 | 2005-12-12

注意spi\_prepare中的参数下标通过 $1、$2、$3 等定义， 这样避免了用双引号来声明查询串（容易导致难以捕捉的缺陷）。

另一个展示spi\_exec\_prepared中可选参数用法的例子：

CREATE TABLE hosts AS SELECT id, ('192.168.1.'||id)::inet AS address

FROM generate\_series(1,3) AS id;

CREATE OR REPLACE FUNCTION init\_hosts\_query() RETURNS VOID AS $$

$\_SHARED{plan} = spi\_prepare('SELECT \* FROM hosts

WHERE address << $1', 'inet');

$$ LANGUAGE plperl;

CREATE OR REPLACE FUNCTION query\_hosts(inet) RETURNS SETOF hosts AS $$

return spi\_exec\_prepared(

$\_SHARED{plan},

{limit => 2},

$\_\[0\]

)->{rows};

$$ LANGUAGE plperl;

CREATE OR REPLACE FUNCTION release\_hosts\_query() RETURNS VOID AS $$

spi\_freeplan($\_SHARED{plan});

undef $\_SHARED{plan};

$$ LANGUAGE plperl;

SELECT init\_hosts\_query();

SELECT query\_hosts('192.168.1.0/30');

SELECT release\_hosts\_query();

query\_hosts

\-----------------

(1,192.168.1.1)

(2,192.168.1.2)

(2 rows)

spi\_commit()

spi\_rollback()

提交或者回滚当前事务。只能在从顶层调用的过程或者匿名代码块（DO命令）中调用这个函数（注意不能通过spi\_exec\_query或者类似的函数运行SQL命令COMMIT或者ROLLBACK。这样的工作只能使用这些函数完成）。在一个事务结束后，一个新的事务会自动开始，因此没有单独的函数来开始新事务。

这里是一个例子：

CREATE PROCEDURE transaction\_test1()

LANGUAGE plperl

AS $$

foreach my $i (0..9) {

spi\_exec\_query("INSERT INTO test1 (a) VALUES ($i)");

if ($i % 2 == 0) {

spi\_commit();

} else {

spi\_rollback();

}

}

$$;

CALL transaction\_test1();

### PL/Perl 中的工具函数

elog(level, msg)

发出一个日志或者错误消息。可用的级别有 DEBUG、LOG、INFO、 NOTICE、WARNING以及ERROR。 ERROR产生一种错误情况，如果它没有被周围的 Perl 代码 捕获，错误会传播到调用查询中，导致当前事务或者子事务被中止。这实际 上和 Perl 的die 命令相同。其他级别只产生不同优先级的消息。 特定优先级的消息是被报告给客户端、写到服务器日志或者两者都做由 配置变量log\_min\_messages和 client\_min\_messages控制。

quote\_literal(string)

返回给定字符串的被适当引用后的形式，这种形式能被用作 SQL 语句字符串中的字符串。 嵌入的引号和反斜线会被正确地双写。注意对 undef 输入quote\_literal 会返回 undef。如果参数可能是 undef，quote\_nullable通常更合适。

quote\_nullable(string)

返回给定字符串的被适当引用后的形式，这种形式能被用作 SQL 语句字符串中的字符串。 或者在参数为 undef 时，返回未引用的串 "NULL"。 嵌入的引号和反斜线会被正确地双写。

quote\_ident(string)

返回给定字符串的被适当引用后的形式，这种形式能被用作 SQL 语句字符串 中的标识符。只有在必要时才增加引号（即，如果串包含非标识符字符或者是 大小写折叠的）。

嵌入的引号会被正确地双写。

decode\_bytea(string)

返回由给定串的内容（应该用bytea编码）表示的未转义二进制数据。

encode\_bytea(string)

返回给定串的二进制数据内容的bytea编码形式。

encode\_array\_literal(array)

encode\_array\_literal(array, delimiter)

把被引用的数组的内容返回成数组文字格式（见第 8.15.2 节） 的一个串。如果它不是一个数组的引用，则不加修改地返回参数值。如果没有指定 定界符或者定界符为 undef，则默认把", "用作数组文字的元素 之间的定界符。

encode\_typed\_literal(value, typename)

把一个 Perl 变量转换为由第二个参数传入的数据类型的值，并且返回该值 的字符串表达。它能正确地处理嵌套数组和组合类型的值。

encode\_array\_constructor(array)

把被引用数组的内容返回为数组构造器格式（ 第 4.2.12 节）的一个串。其中的个体值用 quote\_nullable引用。如果参数不是一个数组引用，则 返回用quote\_nullable引用的该参数值。

looks\_like\_number(string)

如果给定串的内容对于 Perl 看起来像是数字则返回真，否则返回假。如果 参数是 undef 则返回 undef。前导和结尾的空格会被忽略。 Inf和Infinity被视作数字。

is\_array\_ref(argument)

如果给定参数可以被当作一个数组引用对待则返回真值，即该参数的定义为

ARRAY或者PostgreSQL::InServer::ARRAY时返回 真。否则返回假。

## PL/Perl 中的全局值

可以在函数调用之间或者当前会话的生命期中用全局哈希 %\_SHARED来存储数据，包括代码引用。

这是共享数据的一个简单例子：

CREATE OR REPLACE FUNCTION set\_var(name text, val text) RETURNS text AS $$

if ($\_SHARED{$\_\[0\]} = $\_\[1\]) {

return 'ok';

} else {

return "cannot set shared variable $\_\[0\] to $\_\[1\]";

}

$$ LANGUAGE plperl;

CREATE OR REPLACE FUNCTION get\_var(name text) RETURNS text AS $$

return $\_SHARED{$\_\[0\]};

$$ LANGUAGE plperl;

SELECT set\_var('sample', 'Hello, PL/Perl! How''s tricks?');

SELECT get\_var('sample');

这是一个使用代码引用的稍微复杂一点的例子：

CREATE OR REPLACE FUNCTION myfuncs() RETURNS void AS $$

$\_SHARED{myquote} = sub {

my $arg = shift;

$arg =~ s/(\['\\\\\])/\\\\$1/g;

return "'$arg'";

};

$$ LANGUAGE plperl;

SELECT myfuncs(); /\* 初始化函数 \*/

/\* 设置一个使用引用函数的函数 \*/

CREATE OR REPLACE FUNCTION use\_quote(TEXT) RETURNS text AS $$

my $text\_to\_quote = shift;

my $qfunc = $\_SHARED{myquote};

return &$qfunc($text\_to\_quote);

$$ LANGUAGE plperl;

（你可以把上面的代码用一行 return $\_SHARED{myquote}->($\_\[0\]);替换，代价是牺牲了可读性）。

处于安全原因，PL/Perl 一个 SQL 角色独立的 Perl 解释器中执行该角色调用 的任何一个函数。这可以避免一个用户无意或者恶意地干涉另一个用户的 PL/Perl 函数的行为。每一个这样的解释器都具有其自身的 %\_SHARED变量值和其他全局状态。因此，只有当 两个 PL/Perl函数是由同一个 SQL 角色执行时，它们才能共享同一个 %\_SHARED值。在使用单个会话执行多个 SQL 角色 的代码（通过SECURITY DEFINER函数、使用 SET ROLE等）的应用中，需要采取显式的步骤以保证 PL/Perl 函数能够通过%\_SHARED共享数据。要这样做，需要 确保要通信的函数都属于同一个用户，并且把它们标记为 SECURITY DEFINER。当然，要小心这样的函数被滥用。

## 可信的和不可信的 PL/Perl

通常，PL/Perl 被作为一种”可信的”编程语言安装，其名称 为plperl。在这种设置下，为了保持安全性禁用了某些 Perl 操作。一般来说，被限制的操作是那些与环境交互的操作。

它们 包括文件处理操作、require以及 use（外部模块）。没有办法像 C 函数那样访问数据库服务器进程的内部或者用服务器进程的权限得到 OS 级别的访问。 因此，任何没有特权的数据库用户也被允许使用这种语言。

下面例子中的函数将无法工作，因为出于安全原因不允许它做文件操作：

CREATE FUNCTION badfunc() RETURNS integer AS $$

my $tmpfile = "/tmp/badfile";

open my $fh, '>', $tmpfile

or elog(ERROR, qq{could not open the file "$tmpfile": $!});

print $fh "Testing writing to a file\\n";

close $fh or elog(ERROR, qq{could not close the file "$tmpfile": $!});

return 1;

$$ LANGUAGE plperl;

这个函数的创建会失败，因为验证器会捕捉到它使用了禁用的操作。

有些时候需要编写不受限制的 Perl 函数。例如，我们可能想要一个能发送电子邮件的 Perl 函数。要处理这些情况，可以把 PL/Perl 安装成一种 “不可信的”语言（通常被称作PL/PerlU）。 在这种情况下整个 Perl 语言的特性都可以使用。在安装语言时，用语言名称plperlu将会选择不可信的 PL/Perl 变体。

PL/PerlU函数的编写者必须注意该函数不能被用来做 其设计目的之外的事情，因为该函数能做一个作为数据库管理员登录的用户可以做的任何事情。注意数据库系统只允许数据库超级用户用不可信语言创建函数。

如果上述函数是一个超级用户用语言plperlu创建的，则可以执行成功。

以和plperl语言同样的方式，可以用 plperlu 编写 Perl 中的匿名代码块，这样的代码块能够使用受限的操作，不过调用者必须是超级用户。

| 注意： |
| --- |
| 虽然对每个 SQL 角色会在一个独立的 Perl 解释器中运行 PL/Perl函数，但是在一个给定会话中执行的所有 PL/PerlU函数都运行在一个 Perl 解释器中（与用于任何PL/Perl函数的解释器不同）。这允许 PL/PerlU函数自由地共享数据，但是 PL/Perl和PL/PerlU函数之间不会发生任何交流。 |

| 注意： |
| --- |
| Perl 不支持一个进程中的多个解释器，除非编译它时使用了合适的标志，即usemultiplicity或者useithreads（ usemultiplicity会更好，除非你确实需要使用线程。更多细节， 请见perlembed手册页）。 如果PL/Perl用的是一份没有这样编译的 Perl 拷贝，那么 在每个会话中只能有一个 Perl 解释器，并且因此任一会话只能要么执行 PL/PerlU函数，要么执行同一个 SQL 角色调用的 PL/Perl函数。 |

## PL/Perl 触发器

PL/Perl 可以被用来编写触发器函数。在触发器函数中，哈希引用 $\_TD包含有关当前触发器事件的信息。 $\_TD是一个全局变量，对触发器的每一次调用它都会得到一个独立的本地值。$\_TD哈希引用的域有：

$\_TD->{new}{foo}

列foo的NEW值

$\_TD->{old}{foo}

列foo的OLD值

$\_TD->{name}

要被调用的触发器的名称

$\_TD->{event}

触发器事件：INSERT、UPDATE、 DELETE、TRUNCATE或者UNKNOWN

$\_TD->{when}

什么时候调用触发器：BEFORE、 AFTER、INSTEAD OF或者 UNKNOWN

$\_TD->{level}

触发器级别：ROW、STATEMENT或者UNKNOWN

$\_TD->{relid}

触发器定义在其上的表的 OID

$\_TD->{table\_name}

触发器定义在其上的表的名称

$\_TD->{relname}

触发器定义在其上的表的名称。这已经被废弃，并且可能会在 未来的发布中被移除。请

使用 $\_TD->{table\_name}。

$\_TD->{table\_schema}

触发器定义在其上的表所在的模式的名称

$\_TD->{argc}

触发器函数的参数数目

@{$\_TD->{args}}

触发器函数的参数。如果$\_TD->{argc}为 0 则不存在

行级触发器可以返回下列之一：

return;

执行操作

"SKIP"

不执行操作

"MODIFY"

指示触发器函数修改了NEW行

这里是一个触发器函数的例子，展示上文所说的一些东西：

CREATE TABLE test (

i int,

v varchar

);

CREATE OR REPLACE FUNCTION valid\_id() RETURNS trigger AS $$

if (($\_TD->{new}{i} >= 100) || ($\_TD->{new}{i} <= 0)) {

return "SKIP"; # skip INSERT/UPDATE command

} elsif ($\_TD->{new}{v} ne "immortal") {

$\_TD->{new}{v}.= "(modified by trigger)";

return "MODIFY"; # 修改行并且执行 INSERT/UPDATE 命令

} else {

return; # 执行 INSERT/UPDATE 命令

}

$$ LANGUAGE plperl;

CREATE TRIGGER test\_valid\_id\_trig

BEFORE INSERT OR UPDATE ON test

FOR EACH ROW EXECUTE FUNCTION valid\_id();

## PL/Perl 事件触发器

PL/Perl 可以被用来编写事件触发器函数。在事件触发器函数中，哈希引用 $\_TD包含有关当前触发器事件的信息。 $\_TD是一个全局变量，对触发器的每一次调用它都会 得到一个独立的本地值。$\_TD哈希引用的域有：

$\_TD->{event}

触发器为其触发的事件名称。

$\_TD->{tag}

触发器为其触发的命令标签。

触发器函数的返回值会被忽略。

这里是一个事件触发器函数的例子，展示了上文所说的一些东西：

CREATE OR REPLACE FUNCTION perlsnitch() RETURNS event\_trigger AS $$

elog(NOTICE, "perlsnitch: ". $\_TD->{event}. " ". $\_TD->{tag}. " ");

$$ LANGUAGE plperl;

CREATE EVENT TRIGGER perl\_a\_snitch

ON ddl\_command\_start

EXECUTE FUNCTION perlsnitch();

## PL/Perl 下面的东西

### 配置

这一节列出了影响PL/Perl的配置参数。

plperl.on\_init (string)

指定当第一次初始化一个 Perl 解释器时要执行的 Perl 代码，这会在 具体用于plperl或plperlu之前做完。当 这段代码被执行时 SPI 函数不可用。如果该代码由于错误失败，它 将中止解释器的初始化并且把错误传播到调用查询，最终导致当前 事务或者子事务被中止。

该 Perl 代码被限制为一个单一的字符串。更长的代码可以放在一个 模块中，然后由on\_init字符串载入。例子：

plperl.on\_init = 'require "plperlinit.pl"'

plperl.on\_init = 'use lib "/my/app"; use MyApp::PgInit;'

任何被plperl.on\_init载入的模块（不管是直接还是间接）都 可以被plperl使用。这可能会导致安全性风险。要看哪些模块 已经被载入，可以使用：

DO 'elog(WARNING, join ", ", sort keys %INC)' LANGUAGE plperl;

如果 plperl 库被包括在shared\_preload\_libraries 中，那么初始化将发生在postmaster 中，在这种情况下要特别地考虑对 postmaster 带来的不稳定风险。使用这种特性的主要原因是， plperl.on\_init载入的 Perl 模块只需要在 postmaster 开始时被载入，并且在数据库会话中不需要任何工作就立刻可用。不过，要记住这 只免除了一个数据库会话中使用的第一个 Perl 解释器的负载 — 不管 是 PL/PerlU 还是用于第一个 SQL 角色调用 PL/Perl 函数的 PL/Perl。在一个 数据库会话中创建的任何额外的 Perl 解释器将不得不重新执行 plperl.on\_init。还有，在 Windows 上无论从什么里面进行 预先载入，都不会有这种节约，因为在 postmaster 进程中创建的 Perl 解释器 不会传播到子进程中。

这个参数只能在postgresql.conf文件或者服务器命令中设置。

plperl.on\_plperl\_init (string)

plperl.on\_plperlu\_init (string)

这些参数分别指定当为plperl或plperlu专门准备好 一个 Perl 解释器时要执行的 Perl代码。当一个 PL/Perl 或者 PL/PerlU 函数 第一次在一个数据库会话中被执行时会发生这种动作，或者由于调用其他语言 或者新的 SQL 角色调用 PL/Perl 函数导致创建额外的解释器时也会发生这种 动作。这些初始化跟随着plperl.on\_init所作的初始化。当这段 代码被执行时，SPI 函数不可用。plperl.on\_plperl\_init中的 Perl 代码在”锁闭”解释器之后被执行，因此它只能执行可信的操作。

如果该代码由于错误失败，它将中止初始化并且把错误传播到调用查询， 最终导致当前事务或者子事务被中止。在 Perl 中已经完成的任何动作都 不会被撤销。不过，该解释器将不能被再次使用。如果再次使用该语言， 将在一个新鲜的 Perl 解释器中再次尝试初始化。

只有超级用户能够更改这些设置。尽管这些设置可以在会话中被修改， 但是这类更改将不会影响已经被用来执行函数的 Perl 解释器。

plperl.use\_strict (boolean)

如果被设置为真，则后续的 PL/Perl 函数编译将会启用 strict编译指示。这个参数不影响当前会话中已编译的函数。

### 限制和缺失的特性

PL/Perl 中目前缺少下列特性，但是欢迎大家对此作出贡献。

• PL/Perl 函数不能直接调用彼此。

• SPI 还没有被完全实现。

• 如果正在使用spi\_exec\_query取一个非常大的数据集， 你应该注意它们都会进入到内存中。可以按先前所述，通过使用 spi\_query/spi\_fetchrow来避免发生 这类情况。

如果一个集合返回函数通过return把一个大型的行集合 返回给瀚高数据库，同样会发生这种情况。同样如前所述，可以为每一个 要返回的行使用return\_next来避免这种问题。

• 当会话正常结束（而不是由于致命错误结束）时，任何已经定义的 END块将被执行。当前不会执行其他动作。特别地， 此时文件句柄不会被自动刷写并且对象不会被自动销毁。