---
title: "6.数据查询"
book: "HGDB-SEE V4.5 SQL语言基础"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/develop/data_sel.html"
tags:
  - highgo
  - highgo-v45
  - develop-sql-language-basics
---

## 6\. 数据查询

前面的章节解释了如何创建表、如何用填充数据以及如何操作数据。现在我们讨论如何从数据库中检索数据了。

## 6.1. 概述

从数据库中检索数据的过程或命令叫做查询。在SQL里SELECT命令用于指定查询。

SELECT命令的一般语法是

\[WITH with\_queries\] SELECT select\_list FROM table\_expression

\[sort\_specification\]

下面几个小节描述选择列表、表表达式和排序声明的具体内容。WITH查询等高级特性将在最后讨论。

一个简单类型的查询形式：

SELECT \* FROM table1;

假设有一个表叫做table1，这条命令将table1中检索所有行和所有用户定义的列（检索的方法取决于客户端应用。例如，psql程序将在屏幕上显示一个 ASCII 形式的表格，而客户端库将提供函数来从检索结果中抽取单个值）。选择列表声明\*意味着所有列。一个选择列表也可以选择可用列的一个子集或者在使用它们之前对列进行计算。例如，如果table1有叫做a、b和c的列（可能还有其他），那么你可以用下面的查询：

SELECT a, b + c FROM table1;（假设b和c都是数字数据类型）。

FROM table1是一种非常简单的表表达式：它只读取了一个表。通常，表表达式可以是基本表、连接和子查询组成的复杂结构。但你也可以省略整个表表达式而把SELECT命令当做一个计算器：

SELECT 3 \* 4;

如果选择列表里的表达式返回变化的结果，那么省略整个表表达式就更有用了。例如，你可以用这种方法调用函数：

SELECT random();

## 6.2. 表达式

表表达式计算一个表。该表表达式包含一个FROM子句，该子句后面可以根据需要选用WHERE、GROUP BY和HAVING子句。最简单的表表达式只是引用磁盘上的一个表，一个所谓的基本表，但是我们可以用更复杂的表表达式以多种方法修改或组合基本表。

表表达式里可选的WHERE、GROUP BY和HAVING子句指定一系列对源自FROM子句的表的转换操作。所有这些转换最后生成一个虚拟表，它提供行内容传递给选择列表计算查询的输出行。

### 6.2.1. FROM子句

FROM 子句从一个用逗号分隔的表引用列表中的一个或多个其它表中生成一个表。

FROM table\_reference \[, table\_reference \[, …\]\]

表引用可以是一个表名字（可能有模式限定），或者是一个生成的表，例如子查询、一个JOIN结构或者这些东西的复杂组合。如果在FROM子句中引用了多于一个表，那么它们被交叉连接（即构造它们的行的笛卡尔积，见下文）。FROM列表的结果是一个中间的虚拟表，该表可以进行由WHERE、GROUP BY和HAVING子句指定的转换，并最后生成全局的表表达式结果。

如果一个表引用是一个简单的表名字并且它是表继承层次中的父表，那么该表引用将产生该表和它的子表中的行，除非你在该表名字前面加上ONLY关键字。加上ONLY关键字后只会涉及该命名表中的列，在子表中增加的列都会被忽略。

除了在表名前写ONLY，你可以在表名后面写上\*来显式地指定要包括所有的后代表。搜索后代表现在总是默认行为，为了保持与旧版本的兼容性，仍然支持这种语法。

#### 6.2.1.1. 连接表

一个连接表是根据特定的连接类型的规则从两个其它表（真实表或生成表）中派生的表。目前支持内连接、外连接和交叉连接。一个连接表的一般语法是：

T1 join\_type T2 \[ join\_condition \]

所有类型的连接都可以被链在一起或者嵌套：T1和T2都可以是连接表。在JOIN子句周围可以使用圆括号来控制连接顺序。如果不使用圆括号，JOIN子句会从左至右嵌套。

连接类型：

交叉连接

T1 CROSS JOIN T2

对来自于T1和T2的行的每一种可能的组合（即笛卡尔积），连接表将包含这样一行：它由所有T1里面的列后面跟着所有T2里面的列构成。如果两个表分别有 N 和 M 行，连接表将有 N \* M 行。

FROM T1 CROSS JOIN T2等效于FROM T1 INNER JOIN T2 ON TRUE（见下文）。它也等效于FROM T1,T2。

| **注意：** |
| --- |
| 当多于两个表出现时，后一种等效并不严格成立，因为JOIN比逗号绑得更紧。例如FROM T1 CROSS JOIN T2 INNER JOIN T3 ON condition和FROM   T1,T2 INNER JOIN T3 ON condition并不完全相同，因为第一种情况中的condition可以引用T1，但在第二种情况中却不行。 |

条件连接

T1 { \[INNER\] | { LEFT | RIGHT | FULL } \[OUTER\] } JOIN T2

ON boolean\_expression

T1 { \[INNER\] | { LEFT | RIGHT | FULL } \[OUTER\] } JOIN T2 USING ( join column

list )

T1 NATURAL { \[INNER\] | { LEFT | RIGHT | FULL } \[OUTER\] } JOIN T2

INNER和OUTER对所有连接形式都是可选的。INNER是默认的；LEFT、RIGHT和FULL指示一个。

外连接。

连接条件在ON或USING子句中指定，或者用关键字NATURAL隐含地指定。连接条件决定来自两个源表中的哪些行是“匹配”的，这些我们将在后文详细解释。

可能的条件连接类型是：

INNER JOIN

对于 T1 的每一行 R1，生成的连接表都有一行对应 T2 中的每一个满足和 R1 的连接条件的行。

LEFT OUTER JOIN

首先，执行一次内连接。然后，为 T1 中每一个无法在连接条件上匹配 T2 里任何一行的行返回一个连接行，该连接行中 T2 的列用空值补齐。因此，生成的连接表里为来自 T1 的每一行都至少包含一行。

RIGHT OUTER JOIN

首先，执行一次内连接。然后，为 T2 中每一个无法在连接条件上匹配 T1 里任何一行的行返回一个连接行，该连接行中 T1 的列用空值补齐。因此，生成的连接表里为来自 T2 的每一行都至少包含一行。

FULL OUTER JOIN

首先，执行一次内连接。然后，为 T1 中每一个无法在连接条件上匹配 T2 里任何一行的行返回一个连接行，该连接行中 T2 的列用空值补齐。同样，为 T2 中每一个无法在连接条件上匹配 T1 里任何一行的行返回一个连接行，该连接行中 T1 的列用空值补齐。

ON子句是最常见的连接条件的形式：它接收一个和WHERE子句里用的一样的布尔值表达式。如果两个分别来自T1和T2的行在ON表达式上运算的结果为真，那么它们就算是匹配的行。

USING是一种快捷方法，用于连接的两端都具有相同的连接列名。它接受一个逗号分隔的共享列名的列表，并且为其中每一个共享列构造一个包含等值比较的连接条件。例如用USING (a, b)连接T1和T2会产生连接条件ON T1.a = T2.a AND T1.b= T2.b。

更进一步，JOIN USING的输出会排除冗余列，因为它们必须具有相等的值。不过JOIN ON会先产生来自T1的所有列，后面跟上所有来自T2的列；而JOIN USING会先为列出的每一个列对产生一个输出列，然后先跟上来自T1的剩余列，最后跟上来自T2的剩余列。

最后，NATURAL是USING的快捷形式：它形成一个USING列表，该列表由那些在两个表里都出现了的列名组成。和USING一样，这些列只在输出表里出现一次。如果不存在公共列，NATURAL JOIN的行为将和JOIN … ON TRUE一样产生交叉集连接。

| **提示：** |
| --- |
| USING对于连接关系中的列改变是相当安全的，因为只有被列出的列会被组合成连接条件。NATURAL的风险大一些，因为如果其中一个关系的模式改变会导致出现一个新的匹配列名，就会导致连接将新列也组合成连接条件。 |

举个例子，假设我们有一个表t1：

num | name

—–+——

1 | a

2 | b

3 | c

和t2：

num | value

—–+——-

1 | xxx

3 | yyy

5 | zzz

然后我们用不同的连接方式可以获得各种结果：

\=> SELECT \* FROM t1 CROSS JOIN t2;

num | name | num | value

—–+——+—–+——-

1 | a | 1 | xxx

1 | a | 3 | yyy

1 | a | 5 | zzz

2 | b | 1 | xxx

2 | b | 3 | yyy

2 | b | 5 | zzz

3 | c | 1 | xxx

3 | c | 3 | yyy

3 | c | 5 | zzz

(9 rows)

\=> SELECT \* FROM t1 INNER JOIN t2 ON t1.num = t2.num;

num | name | num | value

—–+——+—–+——-

1 | a | 1 | xxx

3 | c | 3 | yyy

(2 rows)

\=> SELECT \* FROM t1 INNER JOIN t2 USING (num);

num | name | value

—–+——+——-

1 | a | xxx

3 | c | yyy

(2 rows)

\=> SELECT \* FROM t1 NATURAL INNER JOIN t2;

num | name | value

—–+——+——-

1 | a | xxx

3 | c | yyy

(2 rows)

\=> SELECT \* FROM t1 LEFT JOIN t2 ON t1.num = t2.num;

num | name | num | value

—–+——+—–+——-

1 | a | 1 | xxx

2 | b | |

3 | c | 3 | yyy

(3 rows)

\=> SELECT \* FROM t1 LEFT JOIN t2 USING (num);

num | name | value

—–+——+——-

1 | a | xxx

2 | b |

3 | c | yyy

(3 rows)

\=> SELECT \* FROM t1 RIGHT JOIN t2 ON t1.num = t2.num;

num | name | num | value

—–+——+—–+——-

1 | a | 1 | xxx

3 | c | 3 | yyy

| | 5 | zzz

(3 rows)

\=> SELECT \* FROM t1 FULL JOIN t2 ON t1.num = t2.num;

num | name | num | value

—–+——+—–+——-

1 | a | 1 | xxx

2 | b | |

3 | c | 3 | yyy

| | 5 | zzz

(4 rows)

用ON指定的连接条件也可以包含与连接不直接相关的条件。这种功能可能对某些查询很有用。例如：

\=> SELECT \* FROM t1 LEFT JOIN t2 ON t1.num = t2.num AND t2.value = ‘xxx’;

num | name | num | value

—–+——+—–+——-

1 | a | 1 | xxx

2 | b | |

3 | c | |

(3 rows)

注意把限制放在WHERE子句中会产生不同的结果：

\=> SELECT \* FROM t1 LEFT JOIN t2 ON t1.num = t2.num WHERE t2.value = ‘xxx’;

num | name | num | value

—–+——+—–+——-

1 | a | 1 | xxx

(1 row)

这是因为放在ON子句中的一个约束在连接之前被处理，而放在WHERE子句中的一个约束是在连接之后被处理。这对内连接没有关系，但是对于外连接会带来麻烦。

#### 6.2.1.2. 表和列别名

你可以给一个表或复杂的表引用指定一个临时的名字，用于剩下的查询中引用那些派生的表。这被叫做表别名。

要创建一个表别名，我们可以写：

FROM table\_reference AS alias

或者

FROM table\_reference alias

AS关键字是可选的。别名可以是任意标识符。

表别名的典型应用是给长表名赋予比较短的标识符，好让连接子句更易读。例如：

SELECT \* FROM some\_very\_long\_table\_name s JOIN another\_fairly\_long\_name a ON

s.id = a.num;

到这里，别名成为当前查询的表引用的新名称 — 我们不能够再用该表最初的名字引用它了。因此，下面的用法是不合法的：

SELECT \* FROM my\_table AS m WHERE my\_table.a > 5; – 错误

表别名主要用于简化符号，但是当把一个表连接到它自身时必须使用别名，例如：

SELECT \* FROM people AS mother JOIN people AS child ON mother.id =

child.mother\_id;

此外，如果一个表引用是一个子查询，则必须要使用一个别名。

圆括弧用于解决歧义。在下面的例子中，第一个语句将把别名b赋给第二个my\_table，但是第二个语句把别名赋给连接的结果：

SELECT \* FROM my\_table AS a CROSS JOIN my\_table AS b …

SELECT \* FROM (my\_table AS a CROSS JOIN my\_table) AS b …

另外一种给表指定别名的形式是给表的列赋予临时名字，就像给表本身指定别名一样：

FROM table\_reference \[AS\] alias ( column1 \[, column2 \[, …\]\] )

如果指定的列别名比表里实际的列少，那么剩下的列就没有被重命名。这种语法对于自连接或子查询特别有用。

如果用这些形式中的任何一种给一个JOIN子句的输出附加了一个别名，那么该别名就在JOIN的作用下隐去了其原始的名字。例如：

SELECT a.\* FROM my\_table AS a JOIN your\_table AS b ON …

是合法 SQL，但是：

SELECT a.\* FROM (my\_table AS a JOIN your\_table AS b ON …) AS c

是不合法的：表别名a在别名c外面是看不到的。

#### 6.2.1.3. 子查询

子查询指定了一个派生表，它必须被包围在圆括弧里并且必须被赋予一个表别名。例如：

FROM (SELECT \* FROM table1) AS alias\_name

这个例子等效于FROM table1 AS alias\_name。更有趣的情况是在子查询里面有分组或聚集的时候，子查询不能被简化为一个简单的连接。

一个子查询也可以是一个VALUES列表：

FROM (VALUES (‘anne’, ‘smith’), (‘bob’, ‘jones’), (‘joe’, ‘blow’))

AS names(first, last)

再次的，这里要求一个表别名。为VALUES列表中的列分配别名是可选的，但是选择这样做是一个好的开发习惯。

#### 6.2.1.4. 表函数

表函数是那些生成一个行集合的函数，这个集合可以是由基本数据类型（标量类型）组成，也可以是由复合数据类型（表行）组成。它们的用法类似一个表、视图或者在查询的FROM子句里的子查询。表函数返回的列可以像一个表、视图或者子查询中的列那样被包含在SELECT、JOIN或WHERE子句里。

也可以使用ROWS FROM语法将平行列返回的结果组合成表函数；这种情况下结果行的数量是最大一个函数结果的数量，较小的结果会用空值来填充。

function\_call \[WITH ORDINALITY\] \[\[AS\] table\_alias \[(column\_alias \[, … \])\]\]

ROWS FROM( function\_call \[, … \] ) \[WITH ORDINALITY\] \[\[AS\] table\_alias

\[(column\_alias \[, … \])\]\]

如果指定了WITH ORDINALITY子句，一个额外的 bigint类型的列将会被增加到函数的结果列中。这个列对函数结果集的行进行编号，编号从 1 开始（这是对 SQL 标准语法 UNNEST … WITH ORDINALITY的一般化）。默认情况下，序数列被称为ordinality，但也可以通过使用一个AS子句给它分配一个不同的列名。

调用特殊的表函数UNNEST可以使用任意数量的数组参数，它会返回对应的列数，就好像在每一个参数上单独调用 UNNEST并且使用 ROWS FROM结构把它们组合起来。

UNNEST( array\_expression \[, … \] ) \[WITH ORDINALITY\] \[\[AS\] table\_alias

\[(column\_alias \[, … \])\]\]

如果没有指定table\_alias，该函数名将被用作表名。在使用ROWS FROM()构建的情况中，会使用第一个函数名。

如果没有提供列的别名，那么对于一个返回基本数据类型的函数，列名也与该函数名相同。

对于一个返回组合类型的函数，结果列会使用该类型中的各个属性的名称。

例子：

CREATE TABLE foo (fooid int, foosubid int, fooname text);

CREATE FUNCTION getfoo(int) RETURNS SETOF foo AS $$

SELECT \* FROM foo WHERE fooid = $1;

$$ LANGUAGE SQL;

SELECT \* FROM getfoo(1) AS t1;

SELECT \* FROM foo

WHERE foosubid IN (

SELECT foosubid

FROM getfoo(foo.fooid) z

WHERE z.fooid = foo.fooid

);

CREATE VIEW vw\_getfoo AS SELECT \* FROM getfoo(1);

SELECT \* FROM vw\_getfoo;

有时侯，定义一个能够根据它们被调用方式返回不同列集合的表函数很有用。为了支持这些，表函数可以被声明为返回伪类型record。如果在查询里使用这样的函数，那么我们必须在查询中指定所需要的行结构，这样系统才知道如何分析和规划该查询。这种语法是这样的：

function\_call \[AS\] alias (column\_definition \[, … \])

function\_call AS \[alias\] (column\_definition \[, … \])

ROWS FROM( … function\_call AS (column\_definition \[, … \]) \[, … \] )

在没有使用ROWS FROM()语法时，column\_definition列表会取代无法附着在 FROM项上的列别名列表，列定义中的名称就起到列别名的作用。在使用ROWS FROM()语法时，可以为每一个成员函数单独附着一个column\_definition列表；或者在只有一个成员函数并且没有WITH ORDINALITY子句的情况下，可以在 ROWS FROM()后面写一个 column\_definition列表来取代一个列别名列表。

考虑下面的例子：

SELECT \*

FROM dblink(‘dbname=mydb’, ‘SELECT proname, prosrc FROM pg\_proc’)

AS t1(proname name, prosrc text)

WHERE proname LIKE ‘bytea%’;

dblink函数（dblink模块的一部分）执行一个远程的查询。它被声明为返回record，因为它可能会被用于任何类型的查询。实际的列集必须在调用它的查询中指定，这样分析器才知道类似\*这样的东西应该扩展成什么样子。

#### 6.2.1.5. LATERAL子查询

可以在出现于FROM中的子查询前放置关键词LATERAL。这允许它们引用前面的FROM项提供的列（如果没有LATERAL，每一个子查询将被独立计算，并且因此不能被其他FROM项交叉引用）。

出现在FROM中的表函数的前面也可以被放上关键词LATERAL，但对于函数该关键词是可选的，在任何情况下函数的参数都可以包含对前面的FROM项提供的列的引用。

一个LATERAL项可以出现在FROM列表顶层，或者出现在一个JOIN树中。在后一种情况下，如果它出现在JOIN的右部，那么它也可以引用在JOIN左部的任何项。

如果一个FROM项包含LATERAL交叉引用，计算过程如下：对于提供交叉引用列的FROM项的每一行，或者多个提供这些列的多个FROM项的行集合，LATERAL项将被使用该行或者行集中的列值进行计算。得到的结果行将和它们被计算出来的行进行正常的连接。对于来自这些列的源表的每一行或行集，该过程将重复。

LATERAL的一个简单例子：

SELECT \* FROM foo, LATERAL (SELECT \* FROM bar WHERE bar.id = foo.bar\_id) ss;

等价于：

SELECT \* FROM foo, bar WHERE bar.id = foo.bar\_id;

在必须要使用交叉引用列来计算那些即将要被连接的行时，LATERAL是最有用的。一种常用的应用是为一个返回集合的函数提供一个参数值。例如，假设vertices(polygon)返回一个多边形的顶点集合，我们可以这样标识存储在一个表中的多边形中靠近的顶点：

SELECT p1.id, p2.id, v1, v2

FROM polygons p1, polygons p2,

LATERAL vertices(p1.poly) v1,

LATERAL vertices(p2.poly) v2

WHERE (v1 <-> v2) < 10 AND p1.id!= p2.id;

这个查询也可以被写成：

SELECT p1.id, p2.id, v1, v2

FROM polygons p1 CROSS JOIN LATERAL vertices(p1.poly) v1,

polygons p2 CROSS JOIN LATERAL vertices(p2.poly) v2

WHERE (v1 <-> v2) < 10 AND p1.id!= p2.id;

或者写成其他几种等价的公式（正如以上提到的，LATERAL关键词在这个例子中并不是必不可少的，但是我们在这里使用它是为了使表述更清晰）。

有时候也会很特别地把LEFT JOIN放在一个LATERAL子查询的前面，这样即使LATERAL子查询对源行不产生行，源行也会出现在结果中。例如，如果get\_product\_names()返回一个制造商制造的产品的名字，但是某些制造商在我们的表中目前没有制造产品，我们可以找出哪些制造商是这样：

SELECT m.name

FROM manufacturers m LEFT JOIN LATERAL get\_product\_names(m.id) pname ON true

WHERE pname IS NULL;

### 6.2.2. WHERE子句

WHERE 子句的语法是

WHERE search\_condition

这里的search\_condition是任意返回一个boolean类型值的值表达式。

在完成对FROM子句的处理之后，生成的虚拟表的每一行都会对根据搜索条件进行检查。如果该条件的结果是真，那么该行被保留在输出表中；否则就把它抛弃。搜索条件通常至少要引用一些在FROM子句里生成的列。

| **注意：** |
| --- |
| 内连接的连接条件既可以写在WHERE子句也可以写在JOIN子句里。例如，这些表表达式是等效的：   FROM a, b WHERE a.id = b.id AND b.val > 5   和：   FROM a INNER JOIN b ON (a.id = b.id) WHERE b.val > 5   或者可能还有：   FROM a NATURAL JOIN b WHERE b.val > 5   你想用哪个只是一个风格问题。FROM子句里的JOIN语法可能不容易移植到其它SQL数据库管理系统中。对于外部连接而言没有选择：它们必须在FROM子句中完成。外部连接的ON或USING子句不等于WHERE条件，因为它导致最终结果中行的增加（对那些不匹配的输入行）和减少。 |

这里是一些WHERE子句的例子：

SELECT … FROM fdt WHERE c1 > 5

SELECT … FROM fdt WHERE c1 IN (1, 2, 3)

SELECT … FROM fdt WHERE c1 IN (SELECT c1 FROM t2)

SELECT … FROM fdt WHERE c1 IN (SELECT c3 FROM t2 WHERE c2 = fdt.c1 + 10)

SELECT … FROM fdt WHERE c1 BETWEEN (SELECT c3 FROM t2 WHERE c2 = fdt.c1 + 10)

AND 100

SELECT … FROM fdt WHERE EXISTS (SELECT c1 FROM t2 WHERE c2 > fdt.c1)

在上面的例子里，fdt是从FROM子句中派生的表。那些不符合WHERE子句的搜索条件的行会被从fdt中删除。请注意我们把标量子查询当做一个值表达式来用。和任何其它查询一样，子查询里可以使用复杂的表表达式。同时还请注意fdt在子查询中也被引用。只有在c1也是作为子查询输入表的生成表的列时，才必须把c1限定成fdt.c1。但限定列名字可以增加语句的清晰度，即使有时候不是必须的。这个例子展示了一个外层查询的列名范围如何扩展到它的内层查询。

### 6.2.3. GROUP BY和HAVING子句

在通过了WHERE过滤器之后，生成的输入表可以使用GROUP BY子句进行分组，然后用HAVING子句删除一些分组行。

SELECT select\_list

FROM …

\[WHERE …\]

GROUP BY grouping\_column\_reference \[, grouping\_column\_reference\]…

GROUP BY 子句被用来把表中在所列出的列上具有相同值的行分组在一起。这些列的列出顺序并没有什么关系。其效果是把每组具有相同值的行组合为一个组行，它代表该组里的所有行。这样就可以删除输出里的重复和/或计算应用于这些组的聚集。例如：

\=> SELECT \* FROM test1;

x | y

—+—

a | 3

c | 2

b | 5

a | 1

(4 rows)

\=> SELECT x FROM test1 GROUP BY x;

x

\-–

a

b

c

(3 rows)

在第二个查询里，我们不能写成SELECT \* FROM test1 GROUP BY x，因为列y里没有哪个值可以和每个组相关联起来。被分组的列可以在选择列表中引用是因为它们在每个组都有单一的值。

通常，如果一个表被分了组，那么没有在GROUP BY中列出的列都不能被引用，除非在聚集表达式中被引用。一个用聚集表达式的例子是：

\=> SELECT x, sum(y) FROM test1 GROUP BY x;

x | sum

—+—–

a | 4

b | 5

c | 2

(3 rows)

这里的sum是一个聚集函数，它在整个组上计算出一个单一值。

| **提示：** |
| --- |
| 没有聚集表达式的分组实际上计算了一个列中可区分值的集合。我们也可以用DISTINCT子句实现。 |

这里是另外一个例子：它计算每种产品的总销售额（而不是所有产品的总销售额）：

SELECT product\_id, p.name, (sum(s.units) \* p.price) AS sales

FROM products p LEFT JOIN sales s USING (product\_id)

GROUP BY product\_id, p.name, p.price;

在这个例子里，列product\_id、p.name和p.price必须在GROUP BY子句里，因为它们都在查询的选择列表里被引用到（见下文）。列s.units不必在GROUP BY列表里，因为它只是在一个聚集表达式（sum(…)）里使用，它代表一组产品的销售额。对于每种产品，这个查询都返回一个该产品的所有销售额的总和行。

如果产品表被建立起来，例如product\_id是主键，那么在上面的例子中用product\_id来分组就够了，因为名称和价格都是函数依赖于产品ID。

在严格的 SQL 里，GROUP BY只能对源表的列进行分组，但瀚高数据库把这个扩展为也允许GROUP BY去根据选择列表中的列分组。也允许对值表达式进行分组，而不仅是简单的列名。

如果一个表已经用GROUP BY子句分了组，然后你又只对其中的某些组感兴趣，那么就可以用HAVING子句，它很像WHERE子句，用于从结果中删除一些组。其语法是：

SELECT select\_list FROM … \[WHERE …\] GROUP BY … HAVING boolean\_expression在HAVING子句中的表达式可以引用分组的表达式和未分组的表达式（后者必须涉及一个聚集函数）。

例子：

\=> SELECT x, sum(y) FROM test1 GROUP BY x HAVING sum(y) > 3;

x | sum

—+—–

a | 4

b | 5

(2 rows)

\=> SELECT x, sum(y) FROM test1 GROUP BY x HAVING x < ‘c’;

x | sum

—+—–

a | 4

b | 5

(2 rows)

再次，一个更现实的例子：

SELECT product\_id, p.name, (sum(s.units) \* (p.price - p.cost)) AS profit

FROM products p LEFT JOIN sales s USING (product\_id)

WHERE s.date > CURRENT\_DATE - INTERVAL ‘4 weeks’

GROUP BY product\_id, p.name, p.price, p.cost

HAVING sum(p.price \* s.units) > 5000;

在上面的例子里，WHERE子句用那些非分组的列选择数据行（表达式只是对那些最近四周发生的销售为真）。而HAVING子句限制输出为总销售收入超过 5000 的组。

如果一个查询包含聚集函数调用，但是没有GROUP BY子句，分组仍然会发生：结果是一个单一行（或者根本就没有行，如果该单一行被HAVING所消除）。它包含一个HAVING子句时也是这样，即使没有任何聚集函数调用或者GROUP BY子句。

### 6.2.4. GROUPING SETS、CUBE和ROLLUP

使用分组集的概念可以实现比上述更加复杂的分组操作。由 FROM和WHERE子句选出的数据被按照每一个指定的分组集单独分组，按照简单GROUP BY子句对每一个分组计算聚集，然后返回结果。例如：

\=> SELECT \* FROM items\_sold;

brand | size | sales

——-+——+——-

Foo | L | 10

Foo | M | 20

Bar | M | 15

Bar | L | 5

(4 rows)

\=> SELECT brand, size, sum(sales) FROM items\_sold GROUP BY GROUPING SETS

((brand), (size), ());

brand | size | sum

——-+——+—–

Foo | | 30

Bar | | 20

| L | 15

| M | 35

| | 50

(5 rows)

GROUPING SETS的每一个子列表可以指定一个或者多个列或者表达式，它们将按照直接出现在GROUP BY子句中的方式被解释。一个空的分组集表示所有的行都要被聚集到一个单一分组（即使没有输入行存在也会被输出）中，这就像前面所说的没有GROUP BY子句的聚集函数的情况一样。

对于分组列或表达式没有出现在其中的分组集的结果行，对分组列或表达式的引用会被空值所替代。要区分一个特定的输出行来自于哪个分组，请见 表 9.59。

瀚高数据库中提供了一种简化方法来指定两种常用类型的分组集。下面形式的子句 ROLLUP ( e1, e2, e3, … ) 表示给定的表达式列表及其所有前缀（包括空列表），因此它等效于

GROUPING SETS (

( e1, e2, e3, … ),

…

( e1, e2 ),

( e1 ),

( )

)

这通常被用来分析历史数据，例如按部门、区和公司范围计算的总薪水。

下面形式的子句

CUBE ( e1, e2, … )

表示给定的列表及其可能的子集（即幂集）。因此

CUBE ( a, b, c )

等效于

GROUPING SETS (

( a, b, c ),

( a, b ),

( a, c ),

( a ),

( b, c ),

( b ),

( c ),

( )

)

CUBE或ROLLUP子句中的元素可以是表达式或者圆括号中的元素子列表。在后一种情况中，对于生成分组集的目的来说，子列表被当做单一单元来对待。例如：

CUBE ( (a, b), (c, d) )

等效于

GROUPING SETS (

( a, b, c, d ),

( a, b ),

( c, d ),

( )

)

并且

ROLLUP ( a, (b, c), d )

等效于

GROUPING SETS (

( a, b, c, d ),

( a, b, c ),

( a ),

( )

)

CUBE和ROLLUP可以被直接用在 GROUP BY子句中，也可以被嵌套在一个 GROUPING SETS子句中。如果一个 GROUPING SETS子句被嵌套在另一个同类子句中，效果和把内层子句的所有元素直接写在外层子句中一样。

如果在一个GROUP BY子句中指定了多个分组项，那么最终的分组集列表是这些项的叉积。例如：

GROUP BY a, CUBE (b, c), GROUPING SETS ((d), (e))

等效于

GROUP BY GROUPING SETS (

(a, b, c, d), (a, b, c, e),

(a, b, d), (a, b, e),

(a, c, d), (a, c, e),

(a, d), (a, e)

)

| **注意：** |
| --- |
| 在表达式中，结构(a, b)通常被识别为一个 a 行构造器。在 GROUP BY子句中，这不会在表达式的顶层应用，并且 (a, b)会按照上面所说的被解析为一个表达式的列表。如果出于某种原因你在分组表达式中需要一个行构造器，请使用 ROW(a, b)。 |

### 6.2.5. 窗口函数处理

如果查询包含任何窗口函数，这些函数将在任何分组、聚集和HAVING过滤被执行之后被计算。也就是说如果查询使用了任何聚集、GROUP BY或HAVING，则窗口函数看到的行是分组行而不是来自于FROM/WHERE的原始表行。

当使用多个窗口函数时，所有在其窗口定义中具有语法等效的 PARTITION BY 和 ORDER BY 子句的窗口函数都保证在一次数据传递中被评估。因此它们将会看到相同的排序顺序，即使ORDER BY没有唯一地决定一个顺序。但是，对于具有不同PARTITION BY或ORDER BY定义的函数的计算就没有这种保证（在这种情况中，在多个窗口函数计算之间通常要求一个排序步骤，并且并不保证保留行的顺序，即使它的ORDER BY把这些行视为等效的）。

目前，窗口函数总是要求排序好的数据，并且这样查询的输出总是被根据窗口函数的PARTITION BY/ORDER BY子句的一个或者另一个排序。但是，我们不推荐依赖于此。如果你希望确保结果以特定的方式排序，请显式使用顶层的ORDER BY子句。

## 6.3. 选择列表

如前面的小节说明的那样，在SELECT命令里的表表达式构造了一个中间的虚拟表，方法可能有组合表、视图、消除行、分组等等。这个表最后被选择列表传递下去处理。选择列表判断中间表的哪些列会实际输出。

### 6.3.1. 选择列表项

最简单的选择列表类型是\*，它发出表表达式生成的所有列。否则，一个选择列表是一个逗号分隔的值表达式的列表。例如，它可能是一个列名的列表：

SELECT a, b, c FROM …

列名字a、b和c要么是在FROM子句里引用的表中列的实际名字，要么是别名。在选择列表里可用的名字空间和在WHERE子句里的一样，除非你使用了分组，这时候它和HAVING子句一样。

如果超过一个表有同样的列名，那么你还必须给出表名字，如：

SELECT tbl1.a, tbl2.a, tbl1.b FROM …

在使用多个表时，要求一个特定表的所有列也是有用的：

SELECT tbl1.\*, tbl2.a FROM …

如果将任意值表达式用于选择列表，那么它在概念上向返回的表中增加了一个新的虚拟列。

值表达式为结果的每一行进行一次计算，对任何列引用替换行的值。不过选择列表中的这个表达式并非一定要引用来自FROM子句中表表达式里面的列，例如它也可以是任意常量算术表达式。

### 6.3.2. 列标签

选择列表中的项可以被赋予名字，用于进一步的处理。比如为了在一个ORDER BY子句中使用或者为了客户端应用显示。例如：

SELECT a AS value, b + c AS sum FROM …

如果没有使用AS指定输出列名，那么系统会分配一个缺省的列名。对于简单的列引用，它是被引用列的名字。对于函数调用，它是函数的名字。对于复杂表达式，系统会生成一个通用的名字。

只有在新列无法匹配任何数据库关键词时，AS关键词是可选的。为了避免一个关键字的意外匹配，你可以使用双引号来修饰列名。例如，VALUE是一个关键字，所以下面的语句不会生效：

SELECT a value, b + c AS sum FROM …

但是这个可以：

SELECT a “value”, b + c AS sum FROM …

为了防止未来可能会增加新关键词，我们推荐总是写AS或者用双引号修饰输出列名。

| **注意：** |
| --- |
| 输出列的命名和在FROM子句里的命名是不一样的。它实际上允许你对同一个列命名两次，但是在选择列表中分配的名字才是要传递下去的名字。 |

### 6.3.3. DISTINCT

在处理完选择列表之后，可以选择在结果中删除重复的行。我们可以直接在SELECT后面写上DISTINCT关键字来指定即可：

SELECT DISTINCT select\_list …

（如果不用DISTINCT你可以用ALL关键词来指定获得的所有行的缺省行为）。

显然，如果两行里至少有一个列有不同的值，那么我们认为它是可区分的。空值在这种比较中被认为是相同的。

另外，我们还可以用任意表达式来判断什么行可以被认为是可区分的：

SELECT DISTINCT ON (expression \[, expression …\]) select\_list …

这里expression是任意值表达式，它为所有行计算。如果一个行集合里所有表达式的值是一样的，那么我们认为它们是重复的并且因此只有第一行保留在输出中。请注意这里的一个集合的“第一行”是不可预料的，除非你在足够多的列上对该查询排了序，保证到达DISTINCT过滤器的行的顺序是唯一的（DISTINCT ON处理是发生在ORDER BY排序后面的）。

DISTINCT ON子句不是 SQL 标准的一部分，在一些指南中不推荐使用，因为它的结果是不可判定的。如果有选择的使用GROUP BY和在FROM中的子查询，那么我们可以避免使用这个构造，但是通常它是更方便的候选方法。

## 6.4. 组合查询

两个查询的结果可以用集合操作，组合方式有并、交、差。语法是

query1 UNION \[ALL\] query2

query1 INTERSECT \[ALL\] query2

query1 EXCEPT \[ALL\] query2

query1和query2都是可以使用以上所有特性的查询。集合操作也可以嵌套和级连，例如 query1 UNION query2 UNION query3

实际执行的是：

(query1 UNION query2) UNION query3

UNION有效地把query2的结果附加到query1的结果上（不过我们不能保证返回的顺序）。此外，它将删除结果中所有重复的行，类似DISTINCT，除非你使用的UNION ALL。

INTERSECT返回那些同时存在于query1和query2的结果中的行，除非声明了INTERSECT ALL，否则所有重复行都被消除。

EXCEPT返回所有在query1的结果中但是不在query2的结果中的行（有时侯这叫做两个查询的差）。同样的，除非声明了EXCEPT ALL，否则所有重复行都被消除。

为了计算两个查询的并、交、差，这两个查询必须是“并操作兼容的”，也就意味着它们都返回同样数量的列，并且对应的列有兼容的数据类型。

## 6.5. 行排序

在一个查询生成一个输出表之后（在处理完选择列表之后），还可以选择性地对它进行排序。如果没有选择排序，那么行将以未指定的顺序返回。这时候的实际顺序将取决于扫描和连接计划类型以及行在磁盘上的顺序，但是这种顺序不可控。如需按照特定的顺序只能在显式地选择了排序步骤之后才能被保证。

ORDER BY子句指定了排序顺序：

SELECT select\_list

FROM table\_expression

ORDER BY sort\_expression1 \[ASC | DESC\] \[NULLS { FIRST | LAST }\]

\[, sort\_expression2 \[ASC | DESC\] \[NULLS { FIRST | LAST }\] …\]

排序表达式可以是任何在查询的选择列表中合法的表达式。一个例子是：

SELECT a, b FROM table1 ORDER BY a + b, c;

当多于一个表达式被指定，后面的值将被用于排序那些在前面值上相等的行。每一个表达式后可以选择性地放置一个ASC或DESC关键词来设置排序方向为升序或降序。ASC顺序是默认值。升序会把较小的值放在前面，而“较小”则由<操作符定义。相似地，降序则由>操作符定义。1

NULLS FIRST和NULLS LAST选项将可以被用来决定在排序顺序中，空值是出现在非空值之前或者出现在非空值之后。默认情况下，排序时空值被认为比任何非空值都要大，即NULLS FIRST是DESC顺序的默认值。

注意顺序选项是对每一个排序列独立考虑的。例如ORDER BY x, y DESC表示ORDER BY x ASC, y DESC，和ORDER BY x DESC, y DESC不同。

一个sort\_expression也可以是列标签或者一个输出列的编号，如：

SELECT a + b AS sum, c FROM table1 ORDER BY sum;

SELECT a, max(b) FROM table1 GROUP BY a ORDER BY 1;

两者都根据第一个输出列排序。注意一个输出列的名字必须确定，即它不能被用在一个表达式中 — 例如，这是不正确的：

SELECT a + b AS sum, c FROM table1 ORDER BY sum + c; – 错误

ORDER BY可以被应用于UNION、INTERSECT或EXCEPT组合的结果，但是在这些情况中它只被允许根据输出列名或编号排序，而不能根据表达式排序。

## 6.6. LIMIT和OFFSET

LIMIT和OFFSET允许你只检索查询剩余部分产生的行的一部分：

SELECT select\_list

FROM table\_expression

\[ ORDER BY … \]

\[ LIMIT { number | ALL } \] \[ OFFSET number \]

如果给出了一个限制计数，那么会返回数量不超过该限制的行（但可能更少些，因为查询本身可能生成的行数就比较少）。LIMIT ALL的效果和省略LIMIT子句一样，就像是LIMIT带有 NULL 参数一样。

OFFSET说明在开始返回行之前忽略多少行。OFFSET 0的效果和省略OFFSET子句是一样的，并且LIMIT NULL的效果和省略LIMIT子句一样，就像是OFFSET带有 NULL 参数一样。

如果OFFSET和LIMIT都出现了，那么在返回LIMIT个行之前要先忽略OFFSET行。

重要的是，如果使用LIMIT，那么需要用ORDER BY子句把结果集约束成固定的顺序。否则结果预期可能会和实际不一致。比如你要的可能是第十到第二十行，但以什么顺序的第十到第二十？除非你指定了ORDER BY，否则顺序是未知的。

查询优化器在生成查询计划时会考虑LIMIT，因此如果你给定LIMIT和OFFSET，那么你很可能收到不同的规划（产生不同的行顺序）。因此，使用不同的LIMIT/OFFSET值选择查询结果的不同子集将生成不一致的结果，除非你用ORDER BY固定顺序。这并非bug，这是一个很自然的结果，因为 SQL 没有许诺把查询的结果按照任何特定的顺序发出，除非用了ORDER BY来约束顺序。

被OFFSET子句忽略的行仍然需要在服务器内部计算；因此，一个很大的OFFSET的效率可能会很低下。

## 6.7. VALUES列表

VALUES提供了一种生成“常量表”的方法，它可以被使用在一个查询中而不需要实际在磁盘上创建一个表。语法是：

VALUES ( expression \[, …\] ) \[, …\]

每一个被圆括号包围的表达式列表生成表中的一行。列表都必须具有相同数据的元素（即表中列的数目），并且在每个列表中对应的项必须具有可兼容的数据类型。分配给结果的每一列的实际数据类型使用和UNION相同的规则确定。

一个例子：

VALUES (1, ‘one’), (2, ‘two’), (3, ‘three’);

将会返回一个有两列三行的表。它实际上等效于：

SELECT 1 AS column1, ‘one’ AS column2

UNION ALL

SELECT 2, ‘two’

UNION ALL

SELECT 3, ‘three’;

在默认情况下，数据库将column1、column2等名字分配给一个VALUES表的列。这些列名不是由SQL标准指定的，并且不同的数据库系统的做法也不同，因此通常最好使用表别名列表来重写这些默认的名字，像这样：

\=> SELECT \* FROM (VALUES (1, ‘one’), (2, ‘two’), (3, ‘three’)) AS t

(num,letter);

num | letter

—–+——–

1 | one

2 | two

3 | three

(3 rows)

在句法上，后面跟随着表达式列表的VALUES列表被视为和 SELECT select\_list FROM table\_expression一样。例如，你可以把它用作UNION的一部分，或者附加一个sort\_specification（ORDER BY、LIMIT和/或OFFSET）给它。VALUES最常见的用途是作为一个INSERT命令的数据源，以及作为一个子查询。

更多信息请见VALUES。

## 6.8. WITH查询（CTE）

WITH提供了一种方式来书写在一个大型查询中使用的辅助语句。这些语句通常被称为公共表表达式或CTE，它们可以被看成是定义只在一个查询中存在的临时表。在WITH子句中的每一个辅助语句可以是一个SELECT、INSERT、UPDATE或DELETE，并且WITH子句本身也可以被附加到一个主语句，主语句也可以是SELECT、INSERT、UPDATE或DELETE。

### 6.8.1. WITH中的SELECT

WITH中SELECT的基本价值是将复杂的查询分解称为简单的部分。一个例子：

WITH regional\_sales AS (

SELECT region, SUM(amount) AS total\_sales

FROM orders

GROUP BY region

), top\_regions AS (

SELECT region

FROM regional\_sales

WHERE total\_sales > (SELECT SUM(total\_sales)/10 FROM regional\_sales)

)

SELECT region,

product,

SUM(quantity) AS product\_units,

SUM(amount) AS product\_sales

FROM orders

WHERE region IN (SELECT region FROM top\_regions)

GROUP BY region, product;

它只显示在高销售区域每种产品的销售总额。WITH子句定义了两个辅助语句regional\_sales和top\_regions，其中regional\_sales的输出用在top\_regions中，而top\_regions的输出用在主SELECT查询。这个例子可以不用WITH来书写，但是我们必须要用两层嵌套的子SELECT。使用这种方法要更简单些。

可选的RECURSIVE修饰符将WITH从单纯的句法便利变成了一种在标准SQL中不能完成的特性。通过使用RECURSIVE，一个WITH查询可以引用它自己的输出。一个非常简单的例子是计算从1到100的整数合的查询：

WITH RECURSIVE t(n) AS (

VALUES (1)

UNION ALL

SELECT n+1 FROM t WHERE n < 100

)

SELECT sum(n) FROM t;

一个递归WITH查询的通常形式总是一个非递归项，然后是UNION（或者UNION ALL），再然后是一个递归项，其中只有递归项能够包含对于查询自身输出的引用。这样一个查询可以被这样执行：

递归查询求值

\\1. 计算非递归项。对UNION（但不对UNION ALL），抛弃重复行。把所有剩余的行包括在递归查询的结果中，并且也把它们放在一个临时的工作表中。

\\2. 只要工作表不为空，重复下列步骤：

a. 计算递归项，用当前工作表的内容替换递归自引用。对UNION（不是UNION ALL），抛弃重复行以及那些与之前结果行重复的行。将剩下的所有行包括在递归查询的结果中，并且也把它们放在一个临时的中间表中。

b. 用中间表的内容替换工作表的内容，然后清空中间表。

| **注意：** |
| --- |
| 严格来说，这个处理是迭代而不是递归，但是RECURSIVE是SQL标准委员会选择的术语。 |

在上面的例子中，工作表在每一步只有一个行，并且它在连续的步骤中取值从1到100。在第100步，由于WHERE子句导致没有输出，因此查询终止。

递归查询通常用于处理层次或者树状结构的数据。一个有用的例子是这个用于找到一个产品的直接或间接部件的查询，只要给定一个显示了直接包含关系的表：

WITH RECURSIVE included\_parts(sub\_part, part, quantity) AS (

SELECT sub\_part, part, quantity FROM parts WHERE part = ‘our\_product’

UNION ALL

SELECT p.sub\_part, p.part, p.quantity

FROM included\_parts pr, parts p

WHERE p.part = pr.sub\_part

)

SELECT sub\_part, SUM(quantity) as total\_quantity

FROM included\_parts

GROUP BY sub\_part

在使用递归查询时，需要确保查询的递归部分到最终将不返回元组，否则查询将会无限循环。在某些时候，使用UNION替代UNION ALL可以通过抛弃与之前输出行重复的行来达到这个目的。不过，经常有循环不涉及到完全重复的输出行：它可能只需要检查一个或几个域来看相同点之前是否达到过。处理这种情况的标准方法是计算一个已经访问过值的数组。例如，考虑下面这个使用link域搜索表graph的查询：

WITH RECURSIVE search\_graph(id, link, data, depth) AS (

SELECT g.id, g.link, g.data, 1

FROM graph g

UNION ALL

SELECT g.id, g.link, g.data, sg.depth + 1

FROM graph g, search\_graph sg

WHERE g.id = sg.link

)

SELECT \* FROM search\_graph;

如果link关系包含环，这个查询将会循环。因为我们要求一个“depth”输出，仅仅将UNION ALL 改为UNION不会消除循环。反过来在我们顺着一个特定链接路径搜索时，我们需要识别我们是否再次到达了一个相同的行。我们可以向这个有循环倾向的查询增加两个列path和cycle：

WITH RECURSIVE search\_graph(id, link, data, depth, path, cycle) AS (

SELECT g.id, g.link, g.data, 1,

ARRAY\[g.id\],

false

FROM graph g

UNION ALL

SELECT g.id, g.link, g.data, sg.depth + 1,

path || g.id,

g.id = ANY(path)

FROM graph g, search\_graph sg

WHERE g.id = sg.link AND NOT cycle

)

SELECT \* FROM search\_graph;

除了阻止环，数组值对于它们自己的工作显示到达任何特定行的“path”也会用到。

在通常情况下如果需要检查多于一个域来识别一个环，可以用行数组。例如，如果我们需要比较域f1和f2：

WITH RECURSIVE search\_graph(id, link, data, depth, path, cycle) AS (

SELECT g.id, g.link, g.data, 1,

ARRAY\[ROW(g.f1, g.f2)\],

False

FROM graph g

UNION ALL

SELECT g.id, g.link, g.data, sg.depth + 1,

path || ROW(g.f1, g.f2),

ROW(g.f1, g.f2) = ANY(path)

FROM graph g, search\_graph sg

WHERE g.id = sg.link AND NOT cycle

)

SELECT \* FROM search\_graph;

| **提示：** |
| --- |
| 在通常情况下只有一个域需要被检查来识别一个环时，可以省略ROW()语法。这允许使用一个简单的数组而不是一个组合类型数组，这样可以获得更高效率。 |

| **提示：** |
| --- |
| 递归查询计算算法使用宽度优先搜索顺序产生它的输出。你可以通过让外部查询ORDER BY一个以这种方法构建的“路径”，用来以深度优先搜索顺序显示结果。 |

当你不确定查询是否可能循环时，一个测试查询的有用技巧是在父查询中放一个LIMIT。例如，这个查询没有LIMIT时会永远循环：

WITH RECURSIVE t(n) AS (

SELECT 1

UNION ALL

SELECT n+1 FROM t

)

SELECT n FROM t LIMIT 100;

这会起作用，因为瀚高数据库的实现只计算WITH查询中被父查询实际取到的行。不推荐在生产中使用这个技巧，因为其他数据库系统可能以不同方式工作。同样，如果你让外层查询排序递归查询的结果或者把它们连接成某种其他表，这个技巧将不会起作用，因为在这些情况下外层查询通常将尝试取得WITH查询的所有输出。

WITH查询的一个有用的特性是在每一次父查询的执行中它们通常只被计算一次，即使它们被父查询或兄弟WITH查询引用了超过一次。因此，在多个地方需要的复杂计算可以被放在一个WITH查询中来避免冗余工作。另一种可能的应用是阻止不希望的多个函数计算产生副作用。但是，缺点是优化器不能将来自父查询的约束下推到多重引用的WITH查询里，因为当他应该只影响一个时它可能会影响所有使用WITH查询的输出的使用。多重引用WITH查询通常将会被按照所写的方式计算，而不抑制父查询以后可能会抛弃的行（但是，如上所述，如果对查询的引用只请求有限数目的行，计算可能会提前停止）。

但是，如果 WITH 查询是非递归和简单的（就是说，它是一个SELECT包含没有可变函数），则它可以合并到父查询中，允许两个查询级别的联合优化。默认情况下，这发生在如果父查询仅引用WITH查询一次的时候，而不是它引用WITH查询多于一次时。你可以推翻这个规则，通过指定 MATERIALIZED 来强制分开计算 WITH 查询，或者通过指定 NOT MATERIALIZED来强制它被合并到父查询中。后一种选择存在重复计算WITH查询的风险，但当WITH查询的每个使用只需要WITH查询的完整输出的一小部分时，它仍然能提供更低的成本，。

这些规则的一个简单示例是

WITH w AS (

SELECT \* FROM big\_table

)

SELECT \* FROM w WHERE key = 123;

这个 WITH 查询将被合并，生成相同的执行计划为

SELECT \* FROM big\_table WHERE key = 123;

特别是，如果在key上有一个索引，它可能只用于获取具有 key = 123的行。另一方面，在 WITH w AS (

SELECT \* FROM big\_table

)

SELECT \* FROM w AS w1 JOIN w AS w2 ON w1.key = w2.ref

WHERE w2.key = 123;

WITH查询将被物化，生成一个big\_table的临时拷贝，然后与其自身 — 联合，这样将不能从索引上获得任何性能提升。如果写成下面的形式，这个查询将被执行得更有效率。

WITH w AS NOT MATERIALIZED (

SELECT \* FROM big\_table

)

SELECT \* FROM w AS w1 JOIN w AS w2 ON w1.key = w2.ref

WHERE w2.key = 123;

所以父查询的限制可以直接应用于big\_table的扫描。

一个NOT MATERIALIZED 可能不理想的例子为

WITH w AS (

SELECT key, very\_expensive\_function(val) as f FROM some\_table

)

SELECT \* FROM w AS w1 JOIN w AS w2 ON w1.f = w2.f;

在这里，WITH查询的物化确保very\_expensive\_function每个表行只计算一次，而不是两次。

以上的例子只展示了和SELECT一起使用的WITH，但是它可以被以相同的方式附加在INSERT、UPDATE或DELETE上。在每一种情况中，它实际上提供了可在主命令中引用的临时表。

### 6.8.2. WITH中的数据修改语句

你可以在WITH中使用数据修改语句（INSERT、UPDATE或DELETE）。这允许你在同一个查询中执行多个而不同操作。一个例子：

WITH moved\_rows AS (

DELETE FROM products

WHERE

“date” >= ‘2010-10-01’ AND

“date” < ‘2010-11-01’

RETURNING \*

)

INSERT INTO products\_log

SELECT \* FROM moved\_rows;

这个查询实际上从products把行移动到products\_log。WITH中的DELETE删除来自products的指定行，以它的RETURNING子句返回它们的内容，并且接着主查询读该输出并将它插入到products\_log。

上述例子中好的一点是WITH子句被附加给INSERT，而没有附加给INSERT的子SELECT。这是必需的，因为数据修改语句只允许出现在附加给顶层语句的WITH子句中。不过，普通WITH可见性规则应用，这样才可能从子SELECT中引用到WITH语句的输出。

正如上述例子所示，WITH中的数据修改语句通常具有RETURNING子句。它是RETURNING子句的输出，不是数据修改语句的目标表，它形成了剩余查询可以引用的临时表。如果一个WITH中的数据修改语句缺少一个RETURNING子句，则它形不成临时表并且不能在剩余的查询中被引用。但是这样一个语句将被执行。一个非特殊使用的例子：

WITH t AS (

DELETE FROM foo

)

DELETE FROM bar;

这个例子将从表foo和bar中移除所有行。被报告给客户端的受影响行的数目可能只包括从bar中移除的行。

数据修改语句中不允许递归自引用。在某些情况中可以采取引用一个递归WITH的输出来操作这个限制，例如：

WITH RECURSIVE included\_parts(sub\_part, part) AS (

SELECT sub\_part, part FROM parts WHERE part = ‘our\_product’

UNION ALL

SELECT p.sub\_part, p.part

FROM included\_parts pr, parts p

WHERE p.part = pr.sub\_part

)

DELETE FROM parts

WHERE part IN (SELECT part FROM included\_parts);

这个查询将会移除一个产品的所有直接或间接子部件。

WITH中的数据修改语句只被执行一次，并且总是能结束，而不管主查询是否读取它们的输出。注意这和WITH中SELECT的规则不同：正如前一小节所述，直到主查询要求SELECT的输出时，SELECT才会被执行。

The sub-statements in WITH中的子语句被和每一个其他子语句以及主查询并发执行。因此在使用WITH中的数据修改语句时，指定更新的顺序实际是以不可预测的方式发生的。所有的语句都使用同一个快照里执行，因此它们不能“看见”在目标表上另一个执行的效果。这减轻了行更新的实际顺序的不可预见性的影响，并且意味着RETURNING数据是在不同WITH子语句和主查询之间传达改变的唯一方法。其例子

WITH t AS (

UPDATE products SET price = price \* 1.05

RETURNING \*

)

SELECT \* FROM products;

外层SELECT可以返回在UPDATE动作之前的原始价格，而在

WITH t AS (

UPDATE products SET price = price \* 1.05

RETURNING \*

)

SELECT \* FROM t;

外部SELECT将返回更新过的数据。

在一个语句中试图两次更新同一行是不被支持的。虽然只会发生一次修改，但是该办法难以预测哪一个会被执行。这也应用于删除一个已经在同一个语句中被更新过的行：只有更新被执行。因此你通常应该避免尝试在一个语句中尝试两次修改同一个行。尤其是防止书写可能影响被主语句或兄弟子语句修改的相同行。这样一个语句的效果将是不可预测的。

当前，在WITH中一个数据修改语句中被用作目标的任何表不能有条件规则、ALSO规则或INSTEAD规则，这些规则会扩展成为多个语句。