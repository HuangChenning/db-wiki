---
title: "规则系统"
book: "服务器编程指南"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/reference/referenceTwo5.html"
tags:
  - highgo
  - highgo-v9
  - server-programming-guide
---

## 规则系统

## 查询树

要了解规则系统是如何工作的，必须要知道它什么时候被调用以及它的输入和结果是什么。

规则系统位于解析器和规划器之间。它采用解析器的输出（即一个查询树）和用户定义的重写规则（也是查询树，不过带有一些额外信息），并且常见零个或者更多个查询树作为结果。因此它的输入和输出总是那些规划器自身就能产生的东西，并且因此它看到的任何东西都可以被表示成一个SQL语句。

那么什么是一个查询树？它是一个SQL语句的一种内部表示，其中用于创建它的每一个单独的部分都被独立存储。如果你设置了配置参数debug\_print\_parse、debug\_print\_rewritten或debug\_print\_plan，这些查询树可以被显示在服务器日志中。规则动作也被做为查询树存储在系统目录pg\_rewrite中。它们没有被格式化为日志输出的形式，但是它们包含完全相同的信息。

阅读一棵未加工的查询树需要要一些经验。但是由于查询树的SQL表示形式足以用来理解规则系统，本章将不会教授如何阅读查询树。

在阅读本章中查询树的SQL表现形式时，读者需要能够知道语句被分解成了哪些部分并且能在查询树结构中标识它们。一棵查询树的部分有：

命令类型

这是一个简单的值来说明是哪一种命令（SELECT、INSERT、UPDATE、DELETE）产生了该查询树。

范围表

范围表是被使用在该查询中的关系的列表。在一个SELECT语句中，范围表是在关键词FROM后面给出的关系。

每一个范围表项标识一个表或视图，并且说明在该查询的其他部分要以哪个名称调用它。在查询树中，范围表项被使用编号而不是名称来引用，因此在一个SQL语句中出现重复的名字也没有关系。在规则的范围表被合并以后可能会发生这种情况。本章中的例子将不会有这种情况。

结果关系

这是一个指向范围表的索引，它标识了该查询的结果应该去哪个关系。

SELECT查询没有结果关系（特殊情况SELECT INTO几乎等于CREATE TABLE后面跟上INSERT... SELECT，并且不在这里单独讨论）。

对于INSERT、UPDATE和DELETE命令，结果关系是修改要进行的表（或视图！）。

目标列表

目标列表是一个表达式的列表，它定义了查询的结果。在一个SELECT的情况下，这些表达式会构建出该查询最终的输出。它们对应于关键字SELECT和FROM之间的表达式（\*是一个关系所有列名的缩写。解析器会把它扩展成独立的列，因此规则系统永远见不到它）。

DELETE命令不需要一个目标列表，因为它们不产生任何结果。相反，规划器会向空的目标列表中加入一个特殊的CTID项来允许执行器找到要被删除的行（当结果关系是一个普通表时才加入CTID。如果结果关系是一个视图，则会被规则系统加入一个整行变量，如第 9.2.4 节所述）。

对于INSERT命令，目标列表描述了将要进入到结果关系中的新行。它由VALUES子句中的表达式或来自INSERT... SELECT中SELECT子句的表达式构成。重写处理的第一步会为那些没有被原始命令赋值但有默认值的列增加目标列项。任何剩余的列（既没有给定值也没有默认值）将被规划器用一个常量空值表达式填充。

对于UPDATE命令，目标列表描述要替换旧行的新行。在规则系统中，它只包含来自命令的SET column = expression部分的表达式。规划器将处理缺失的列，做法是为它们插入表达式，这种表达式会把旧行的值复制到新行。正如DELETE一样，会增加一个CTID或整行变量，这样执行器能够标识要被更新的旧行。

目标列表中的每一个项所包含的表达式可以是一个常量值、一个指向范围表中关系的列的变量、一个参数或一个由函数调用、常量、变量、操作符等构成的表达式树。

条件

查询的条件是一个表达式，它很像包含在目标列表项中的表达式。这个表达式的结果值是一个布尔值，它说明对最终结果行的操作（INSERT、UPDATE、DELETE或SELECT）是否应该被执行。它对应于一个SQL语句的WHERE子句。

连接树

查询的连接树展示了FROM子句的结构。对于一个SELECT... FROM a, b, c这样的简单查询，连接树就是FROM项的一个列表，因为我们被允许以任何顺序连接它们。但是当JOIN表达式（特别是外连接）被使用时，我们必须按照连接显示的顺序来连接。在这种情况下，连接树展示了JOIN表达式的结构。与特定JOIN子句（来自ON或USING）相关的限制被存储为附加到那些连接树节点的条件表达式。我们发现把顶层WHERE表达式存储为附加到顶层连接树项的一个条件也很方便。这样实际上连接树表达了一个SELECT的FROM和WHERE子句。

其他

查询树的其他部分（如ORDER BY子句）在这里并不受到关注。规则系统在应用规则时会替换这里的某些项，但是这些与规则系统的基础没有什么关系。

## 视图和规则系统

瀚高数据库中的视图是通过规则系统来实现的。事实上，下面的命令

CREATE VIEW myview AS SELECT \* FROM mytab;

与下面两个命令相比没有不同：

CREATE TABLE myview (same column list as mytab);

CREATE RULE "\_RETURN" AS ON SELECT TO myview DO INSTEAD

SELECT \* FROM mytab;

因为这就是CREATE VIEW命令在内部所作的。 这样做有一些副作用。其中之一就是在瀚高数据库系统目录中的视图信息与表的信息完全一样。所以对于解析器来说，表和视图之间完全没有区别。它们是同样的事物：关系。

### SELECT规则如何工作

规则ON SELECT被应用于所有查询作为最后一步，即使给出的是一条INSERT、UPDATE或DELETE命令。而且它们与其他命令类型上的规则有着不同的语义，它们会就地修改查询树而不是创建一个新的查询树。因此我们首先描述SELECT规则。

目前，一个ON SELECT规则中只能有一个动作，而且它必须是一个无条件的INSTEAD的SELECT动作。 这个限制是为了令规则足够安全，以便普通用户也可以打开它们，并且它限制ON SELECT规则使之行为类似视图。

本章的例子是两个连接视图，它们做一些运算并且某些更多视图会轮流使用它们。最前面的两个视图之一后面将利用对INSERT、UPDATE和DELETE操作增加规则的方法被自定义，这样最终结果将是一个视图，它表现得像一个具有魔力的真正的表。这个例子不适合于作为简单易懂的例子，它可能会让本章更难懂。但是用一个覆盖所有关键点的例子来一步一步讨论要比举很多例子搞乱思维好。

在前两个规则系统描述中我们需要真实表是：

CREATE TABLE shoe\_data (

shoename text, -- 主键

sh\_avail integer, -- 可用的双数

slcolor text, -- 首选的鞋带颜色

slminlen real, -- 最小鞋带长度

slmaxlen real, -- 最大鞋带长度

slunit text -- 长度单位

);

CREATE TABLE shoelace\_data (

sl\_name text, -- 主键

sl\_avail integer, -- 可用的双数

sl\_color text, -- 鞋带颜色

sl\_len real, -- 鞋带长度

sl\_unit text -- 长度单位

);

CREATE TABLE unit (

un\_name text, -- 主键

un\_fact real -- 转换到厘米的参数

);

如你所见，它们表示鞋店的数据。

视图被创建为：

CREATE VIEW shoe AS

SELECT sh.shoename,

sh.sh\_avail,

sh.slcolor,

sh.slminlen,

sh.slminlen \* un.un\_fact AS slminlen\_cm,

sh.slmaxlen,

sh.slmaxlen \* un.un\_fact AS slmaxlen\_cm,

sh.slunit

FROM shoe\_data sh, unit un

WHERE sh.slunit = un.un\_name;

CREATE VIEW shoelace AS

SELECT s.sl\_name,

s.sl\_avail,

s.sl\_color,

s.sl\_len,

s.sl\_unit,

s.sl\_len \* u.un\_fact AS sl\_len\_cm

FROM shoelace\_data s, unit u

WHERE s.sl\_unit = u.un\_name;

CREATE VIEW shoe\_ready AS

SELECT rsh.shoename,

rsh.sh\_avail,

rsl.sl\_name,

rsl.sl\_avail,

least(rsh.sh\_avail, rsl.sl\_avail) AS total\_avail

FROM shoe rsh, shoelace rsl

WHERE rsl.sl\_color = rsh.slcolor

AND rsl.sl\_len\_cm >= rsh.slminlen\_cm

AND rsl.sl\_len\_cm <= rsh.slmaxlen\_cm;

创建shoelace视图的CREATE VIEW命令（也是最简单的一个）将创建一个shoelace关系和一个pg\_rewrite项， 这个pg\_rewrite项说明有一个重写规则，只要一个查询的范围表中引用了关系shoelace，就必须应用它。该规则没有规则条件（稍后和非SELECT规则一起讨论，因为目前的SELECT规则不能有规则条件）并且它是INSTEAD规则。要注意规则条件与查询条件不一样。我们的规则的动作有一个查询条件。该规则的动作是一个查询树，这个查询是视图创建命令中的SELECT语句的一个拷贝。

| 注意： |
| --- |
| 你在pg\_rewrite项中看到的两个额外的用于NEW和OLD的范围表项不是SELECT规则感兴趣的东西。 |

现在我们填充unit、shoe\_data和shoelace\_data，并且在视图上运行一个简单的查询：

INSERT INTO unit VALUES ('cm', 1.0);

INSERT INTO unit VALUES ('m', 100.0);

INSERT INTO unit VALUES ('inch', 2.54);

INSERT INTO shoe\_data VALUES ('sh1', 2, 'black', 70.0, 90.0, 'cm');

INSERT INTO shoe\_data VALUES ('sh2', 0, 'black', 30.0, 40.0, 'inch');

INSERT INTO shoe\_data VALUES ('sh3', 4, 'brown', 50.0, 65.0, 'cm');

INSERT INTO shoe\_data VALUES ('sh4', 3, 'brown', 40.0, 50.0, 'inch');

INSERT INTO shoelace\_data VALUES ('sl1', 5, 'black', 80.0, 'cm');

INSERT INTO shoelace\_data VALUES ('sl2', 6, 'black', 100.0, 'cm');

INSERT INTO shoelace\_data VALUES ('sl3', 0, 'black', 35.0, 'inch');

INSERT INTO shoelace\_data VALUES ('sl4', 8, 'black', 40.0, 'inch');

INSERT INTO shoelace\_data VALUES ('sl5', 4, 'brown', 1.0, 'm');

INSERT INTO shoelace\_data VALUES ('sl6', 0, 'brown', 0.9, 'm');

INSERT INTO shoelace\_data VALUES ('sl7', 7, 'brown', 60, 'cm');

INSERT INTO shoelace\_data VALUES ('sl8', 1, 'brown', 40, 'inch');

SELECT \* FROM shoelace;

sl\_name | sl\_avail | sl\_color | sl\_len | sl\_unit | sl\_len\_cm

\-----------+----------+----------+--------+---------+-----------

sl1 | 5 | black | 80 | cm | 80

sl2 | 6 | black | 100 | cm | 100

sl7 | 7 | brown | 60 | cm | 60

sl3 | 0 | black | 35 | inch | 88.9

sl4 | 8 | black | 40 | inch | 101.6

sl8 | 1 | brown | 40 | inch | 101.6

sl5 | 4 | brown | 1 | m | 100

sl6 | 0 | brown | 0.9 | m | 90

(8 rows)

这是你可以在我们的视图上做的最简单的SELECT，所以我们用这次机会来解释视图规则的基本要素。SELECT \* FROM shoelace会被解析器解释并生成下面的查询树：

SELECT shoelace.sl\_name, shoelace.sl\_avail,

shoelace.sl\_color, shoelace.sl\_len,

shoelace.sl\_unit, shoelace.sl\_len\_cm

FROM shoelace shoelace;

然后这将被交给规则系统。规则系统遍历范围表，检查有没有可用于任何关系的规则。在为shoelace（到目前为止的唯一一个）处理范围表时， 它会发现查询树里有\_RETURN规则：

SELECT s.sl\_name, s.sl\_avail,

s.sl\_color, s.sl\_len, s.sl\_unit,

s.sl\_len \* u.un\_fact AS sl\_len\_cm

FROM shoelace old, shoelace new,

shoelace\_data s, unit u

WHERE s.sl\_unit = u.un\_name;

要扩展该视图，重写器简单地创建一个子查询范围表项，它包含规则的动作的查询树，然后用这个范围表记录取代原来引用视图的那个。作为结果的重写后的查询树几乎与你键入的那个一样：

SELECT shoelace.sl\_name, shoelace.sl\_avail,

shoelace.sl\_color, shoelace.sl\_len,

shoelace.sl\_unit, shoelace.sl\_len\_cm

FROM (SELECT s.sl\_name,

s.sl\_avail,

s.sl\_color,

s.sl\_len,

s.sl\_unit,

s.sl\_len \* u.un\_fact AS sl\_len\_cm

FROM shoelace\_data s, unit u

WHERE s.sl\_unit = u.un\_name) shoelace;

不过有一个区别：子查询的范围表有两个额外的项shoelace old和shoelace new。这些项并不直接参与到查询中，因为它们没有被子查询的连接树或者目标列表引用。重写器用它们存储最初出现在引用视图的范围表项中表达的访问权限检查信息。以这种方式，执行器仍然会检查该用户是否有访问视图的正确权限，尽管在重写后的查询中没有对视图的直接使用。

这是被应用的第一个规则。规则系统将继续检查顶层查询里剩下的范围表项（本例中没有了），并且它将递归的检查增加的子查询中的范围表项，看看其中有没有引用视图的（不过这样不会扩展old或new — 否则我们会得到无限递归！）。在这个例子中，没有用于shoelace\_data或unit的重写规则，所以重写结束并且上面得到的就是给规划器的最终结果。

现在我们想写一个查询，它找出目前在店里哪些鞋子有匹配的（颜色和长度）鞋带并且完全匹配的鞋带双数大于等于二。

SELECT \* FROM shoe\_ready WHERE total\_avail >= 2;

shoename | sh\_avail | sl\_name | sl\_avail | total\_avail

\----------+----------+---------+----------+-------------

sh1 | 2 | sl1 | 5 | 2

sh3 | 4 | sl7 | 7 | 4

(2 rows)

这词解析器的输出是查询树：

SELECT shoe\_ready.shoename, shoe\_ready.sh\_avail,

shoe\_ready.sl\_name, shoe\_ready.sl\_avail,

shoe\_ready.total\_avail

FROM shoe\_ready shoe\_ready

WHERE shoe\_ready.total\_avail >= 2;

第一个被应用的规则将是用于shoe\_ready的规则并且它会导致查询树：

SELECT shoe\_ready.shoename, shoe\_ready.sh\_avail,

shoe\_ready.sl\_name, shoe\_ready.sl\_avail,

shoe\_ready.total\_avail

FROM (SELECT rsh.shoename,

rsh.sh\_avail,

rsl.sl\_name,

rsl.sl\_avail,

least(rsh.sh\_avail, rsl.sl\_avail) AS total\_avail

FROM shoe rsh, shoelace rsl

WHERE rsl.sl\_color = rsh.slcolor

AND rsl.sl\_len\_cm >= rsh.slminlen\_cm

AND rsl.sl\_len\_cm <= rsh.slmaxlen\_cm) shoe\_ready

WHERE shoe\_ready.total\_avail >= 2;

相似地，用于shoe和shoelace的规则被替换到子查询的范围表中，得到一个三层的最终查询树：

SELECT shoe\_ready.shoename, shoe\_ready.sh\_avail,

shoe\_ready.sl\_name, shoe\_ready.sl\_avail,

shoe\_ready.total\_avail

FROM (SELECT rsh.shoename,

rsh.sh\_avail,

rsl.sl\_name,

rsl.sl\_avail,

least(rsh.sh\_avail, rsl.sl\_avail) AS total\_avail

FROM (SELECT sh.shoename,

sh.sh\_avail,

sh.slcolor,

sh.slminlen,

sh.slminlen \* un.un\_fact AS slminlen\_cm,

sh.slmaxlen,

sh.slmaxlen \* un.un\_fact AS slmaxlen\_cm,

sh.slunit

FROM shoe\_data sh, unit un

WHERE sh.slunit = un.un\_name) rsh,

(SELECT s.sl\_name,

s.sl\_avail,

s.sl\_color,

s.sl\_len,

s.sl\_unit,

s.sl\_len \* u.un\_fact AS sl\_len\_cm

FROM shoelace\_data s, unit u

WHERE s.sl\_unit = u.un\_name) rsl

WHERE rsl.sl\_color = rsh.slcolor

AND rsl.sl\_len\_cm >= rsh.slminlen\_cm

AND rsl.sl\_len\_cm <= rsh.slmaxlen\_cm) shoe\_ready

WHERE shoe\_ready.total\_avail > 2;

这看起来是低效的，但是计划器会通过”pulling up”子查询将其折叠成一个单层查询树，然后它会计划联接， 就像我们手动写出来一样。 因此，折叠查询树是重写系统本身不必关心的一种优化。

### 非SELECT语句中的视图规则

有两个查询树的细节在上面的视图规则的描述中没有涉及。它们是命令类型和结果关系。实际上，视图规则不需要命令类型，但是结果关系可能会影响查询重写器工作的方式，因为如果结果关系是一个视图，我们需要采取特殊的措施。

一个SELECT的查询树和其它命令的查询树之间很少的几处不同。显然，它们有不同的命令类型并且对于SELECT之外的命令，结果关系指向结果将进入的范围表项。其它所有东西都完全相同。所以如果有两个表t1和t2分别有列a和b，下面两个语句的查询树：

SELECT t2.b FROM t1, t2 WHERE t1.a = t2.a;

UPDATE t1 SET b = t2.b FROM t2 WHERE t1.a = t2.a;

几乎是一样的。特别是：

• 范围表包含表t1和t2的项。

• 目标列表包含一个变量，该变量指向表t2的范围表项的列b。

• 条件表达式比较两个范围表项的列a以寻找相等。

• 连接树展示了t1和t2之间的一次简单连接。

结果是，两个查询树生成相似的执行计划：它们都是两个表的连接。 对于UPDATE语句，规划器把t1缺失的列加到目标列并且最终查询树读起来是：

UPDATE t1 SET a = t1.a, b = t2.b FROM t2 WHERE t1.a = t2.a;

因此在连接上运行的执行器将产生完全相同的结果集：

SELECT t1.a, t2.b FROM t1, t2 WHERE t1.a = t2.a;

但是在UPDATE中有个小问题：执行器计划中执行连接的部分不关心连接的结果的含义。它只是产生一个行的结果集。一个是SELECT命令而另一个是由执行器中的更高层处理的UPDATE命令，在那里执行器知道这是一个UPDATE，并且它知道这个结果应该进入表t1。但是这里的哪些行必须被新行替换呢？

要解决这个问题，在UPDATE和DELETE语句的目标列表里面增加了另外一个项：当前元组 ID（CTID）。这是一个系统列，它包含行所在的文件块编号和在块中的位置。在已知表的情况下，CTID可以被用来检索要被更新的t1的原始行。在添加CTID到目标列之后，该查询实际看起来像：

SELECT t1.a, t2.b, t1.ctid FROM t1, t2 WHERE t1.a = t2.a;

现在，另一个瀚高数据库的细节进入到这个阶段了。表中的旧行还没有被覆盖，这就是为什么ROLLBACK很快的原因。在一个UPDATE中，新的结果行被插入到表中（在剥除CTID之后），并且把CTID指向的旧行的行头部中的cmax和xmax项设置为当前命令计数器和当前事务 ID 。

这样旧的行就被隐藏起来，并且在事务提交之后 vacuum 清理器就可以最终移除死亡的行。

知道了所有这些，我们就可以用完全相同的方式简单地把视图规则应用到任意命令中。没有任何区别。

### 瀚高数据库中视图的能力

上文演示了规则系统如何把视图定义整合到原始的查询树中。在第二个例子中，一个来自于一个视图的简单SELECT创建了一个四表连接（unit以不同的名字被用了两次）的最终查询树。

用规则系统实现视图的好处是，规划器拥有关于哪些表必须被扫描、这些表之间的联系、来自于视图的限制性条件、一个单一查询树中原始查询的条件等所有信息。当原始查询已经是一个视图上的连接时仍然是这样。规划器必须决定执行查询的最优路径，而且规划器拥有越多信息，该决定就越好。并且瀚高数据库中实现的规则系统保证这些信息是此时能获得的有关该查询的所有信息。

### 更新一个视图

如果视图是INSERT、UPDATE或DELETE的目标关系会怎样？使用上文所述的替换将给出一个查询树，其中的结果关系指向一个子查询范围表项，这样无法工作。不过，瀚高数据库中有几种方法来支持更新视图。

如果子查询从一个单一基本关系选择并且该关系足够简单，重写器会自动地把该子查询替换成底层的基本关系，这样INSERT、UPDATE或DELETE会被以适当的方式应用到该基本关系。其中”足够简单”的视图被称为自动可更新。有关这种可以被自动更新的视图类别的详细信息，请见CREATE VIEW。

或者，该操作可以被定义在视图上的一个用户提供的INSTEAD OF触发器处理。在这种情况下重写工作有一点点不同。对于INSERT，重写器对视图什么也不做，让它作为查询的结果关系。对于UPDATE和DELETE，仍有必要扩展该视图查询来产生命令将尝试更新或删除的”旧”行。因此该视图被按照通常的方式扩展，但是另一个未被扩展的范围表项会被增加到查询来表示该视图会尽其所能作为结果关系。

现在出现的问题是如何标识在视图中要被更新的行。回忆一下，当结果关系是一个表时，一个特殊的CTID项会被加入到目标列表来标识要被更新的行的物理位置。如果结果关系是一个视图这就行不通，因为一个视图根本就没有CTID，它的行没有实际的物理位置。对于一个UPDATE或DELETE操作，一个特殊的wholerow项会被增加到目标列表中，它会扩展来包括来自该视图的所有列。执行器使用这个值来提供”旧”行给INSTEAD OF触发器。现在就轮到触发器来基于新旧行值来找出要更新什么了。

另外一种可能性是让用户定义INSTEAD规则，这种规则指定对视图上的INSERT\\UPDATE和DELETE命令的替代动作。这些规则将重写该命令，通常是重写成一个更新一个或多个表（而不是视图）的命令。

注意规则会首先被计算，然后在原始查询被规划和执行之前重写它。因此，如果一个视图上同时有INSTEAD OF触发器和INSERT、UPDATE或DELETE规则，那么首先会计算规则，然后根据其结果决定是否执行触发器，触发器可能完全都不会被使用。

Automatic rewriting of an 在一个简单视图上的INSERT、UPDATE或DELETE查询的自动重写总是在最后尝试。因此，如果一个视图有规则或触发器，它们将重载自动可更新视图的默认行为。

如果对该视图没有INSTEAD规则或INSTEAD OF触发器，并且重写器不能自动地把该查询重写成一个底层基本关系上的更新，将会抛出一个错误，因为执行器不能更新一个这样的视图。

## 物化视图

瀚高数据库中的物化视图像视图一样使用了规则系统，但是以一种类表的形式保留了结果。

在物化视图：

CREATE MATERIALIZED VIEW mymatview AS SELECT \* FROM mytab;

和视图：

CREATE TABLE mymatview AS SELECT \* FROM mytab;

之间的主要区别是物化视图不能直接被更新，并且用于创建物化视图的查询的存储方式和视图查询的存储方式完全相同，因此要为物化视图生成新鲜的数据：

REFRESH MATERIALIZED VIEW mymatview;

有关一个瀚高数据库系统目录中的物化视图的信息和一个表或视图的信息完全相同。因此对于解析器，一个物化视图就是一个关系，就像一个表或一个视图。当一个物化视图被一个查询引用时，数据直接从物化视图中返回，如同表一样；规则只被用来填充物化视图。

虽然对物化视图中存储的数据的访问常常要快于直接访问底层表或通过一个视图访问，但是数据并不总是最新的；但是某些时候并不需要当前数据。考虑一个记录销售情况的表：

CREATE TABLE invoice (

invoice\_no integer PRIMARY KEY,

seller\_no integer, -- 销售员的 ID

invoice\_date date, -- 销售日期

invoice\_amt numeric(13,2) -- 销售量

);

如果人们想快速绘制历史销售数据，他们可能希望汇总，并且他们可能并不关心当前日期的不完整数据：

CREATE MATERIALIZED VIEW sales\_summary AS

SELECT

seller\_no,

invoice\_date,

sum(invoice\_amt)::numeric(13,2) as sales\_amt

FROM invoice

WHERE invoice\_date < CURRENT\_DATE

GROUP BY

seller\_no,

invoice\_date

ORDER BY

seller\_no,

invoice\_date;

CREATE UNIQUE INDEX sales\_summary\_seller

ON sales\_summary (seller\_no, invoice\_date);

这个物化视图可能对在为销售员创建的控制面板上显示一个图表非常有用。可以用一个计划任务在每晚使用这个 SQL 语句更新该统计信息：

REFRESH MATERIALIZED VIEW sales\_summary;

物化视图的另一种使用是允许通过一个外部数据包装器对来 自一个远程系统的数据进行更快的访问。下面有一个使用file\_fdw的简单例子，但是由于本地系 统上可以使用高

速缓存，因此比起访问一个远程系统的性 能差异可能会比这里所展示的更大。注意鉴于file\_fdw不支持索引，我们也使用这种 能力来在物化视图上放置索引。这种优势可能不适用于其 他种类的外部数据访问。

建立：

CREATE EXTENSION file\_fdw;

CREATE SERVER local\_file FOREIGN DATA WRAPPER file\_fdw;

CREATE FOREIGN TABLE words (word text NOT NULL)

SERVER local\_file

OPTIONS (filename '/usr/share/dict/words');

CREATE MATERIALIZED VIEW wrd AS SELECT \* FROM words;

CREATE UNIQUE INDEX wrd\_word ON wrd (word);

CREATE EXTENSION pg\_trgm;

CREATE INDEX wrd\_trgm ON wrd USING gist (word gist\_trgm\_ops);

VACUUM ANALYZE wrd;

现在让我们对一个词进行拼写检查。直接使用file\_fdw：

SELECT count(\*) FROM words WHERE word = 'caterpiler';

count

\-------

0

(1 row)

通过EXPLAIN ANALYZE，我们可以看到：

Aggregate (cost=21763.99..21764.00 rows=1 width=0) (actual

time=188.180..188.181 rows=1 loops=1)

\-> Foreign Scan on words (cost=0.00..21761.41 rows=1032 width=0) (actual

time=188.177..188.177 rows=0 loops=1)

Filter: (word = 'caterpiler'::text)

Rows Removed by Filter: 479829

Foreign File: /usr/share/dict/words

Foreign File Size: 4953699

Planning time: 0.118 ms

Execution time: 188.273 ms

如果使用物化视图，该查询会快很多：

Aggregate (cost=4.44..4.45 rows=1 width=0) (actual time=0.042..0.042 rows=1

loops=1)

\-> Index Only Scan using wrd\_word on wrd (cost=0.42..4.44 rows=1 width=0)

(actual time=0.039..0.039 rows=0 loops=1)

Index Cond: (word = 'caterpiler'::text)

Heap Fetches: 0

Planning time: 0.164 ms

Execution time: 0.117 ms

不管哪种方式，单词都是被拼错的，因此让我们看看什么是我们可能想要的。再次使用file\_fdw：

SELECT word FROM words ORDER BY word <-> 'caterpiler' LIMIT 10;

word

\---------------

cater

caterpillar

Caterpillar

caterpillars

caterpillar's

Caterpillar's

caterer

caterer's

caters

catered

(10 rows)

Limit (cost=11583.61..11583.64 rows=10 width=32) (actual

time=1431.591..1431.594 rows=10 loops=1)

\-> Sort (cost=11583.61..11804.76 rows=88459 width=32) (actual

time=1431.589..1431.591 rows=10 loops=1)

Sort Key: ((word <-> 'caterpiler'::text))

Sort Method: top-N heapsort Memory: 25kB

\-> Foreign Scan on words (cost=0.00..9672.05 rows=88459 width=32)

(actual time=0.057..1286.455 rows=479829 loops=1)

Foreign File: /usr/share/dict/words

Foreign File Size: 4953699

Planning time: 0.128 ms

Execution time: 1431.679 ms

使用物化视图：

Limit (cost=0.29..1.06 rows=10 width=10) (actual time=187.222..188.257 rows=10

loops=1)

\-> Index Scan using wrd\_trgm on wrd (cost=0.29..37020.87 rows=479829

width=10) (actual time=187.219..188.252 rows=10 loops=1)

Order By: (word <-> 'caterpiler'::text)

Planning time: 0.196 ms

Execution time: 198.640 ms

如果你能够忍受定期把远程数据更新到本地数据库，其性能收益可能是巨大的。

## INSERT、UPDATE和DELETE上的规则

定义在INSERT、UPDATE和DELETE上的规则与前一节描述的视图规则有明显的不同。首先，它们的CREATE RULE命令允许更多：

• 它们可以没有动作。

• 它们可以有多个动作。

• 它们可以是INSTEAD或ALSO（缺省）。

• 伪关系NEW和OLD变得有用了。

• 它们可以有规则条件。

第二，它们不是就地修改查询树，而是创建零个或多个新查询树并且可能把原始的那个查询树扔掉。

| 小心： |
| --- |
| 在很多情况下，由INSERT/UPDATE/DELETE上的规则执行的任务用触发器能做得更好。触发器在记法上要更复杂些，但是它们的语义理解起来更简单些。当原始查询包含不稳定函数时，规则容易产生令人惊讶的结果：在执行规则的过程中不稳定函数的执行次数可能比语气中的更多。 |
| 还有，有些情况根本无法用这些类型的规则支持，典型的是在原始查询中包括WITH子句以及在UPDATE查询的SET列表中包括多个赋值的子SELECT。这是因为把这些结构复制到一个规则查询中可能导致子查询的多次计算，这与查询作者表达的意图相悖。 |

### 更新规则如何工作

记住以下语法：

CREATE \[ OR REPLACE \] RULE name AS ON event

TO table \[ WHERE condition \]

DO \[ ALSO | INSTEAD \] { NOTHING | command | ( command; command... ) }

在随后的内容中，更新规则表示定义在INSERT、UPDATE或DELETE上的规则。

如果查询树的结果关系和命令类型等于CREATE RULE命令中给出的对象和事件，规则系统就会应用更新规则。对于更新规则，规则系统会创建一个查询树列表。一开始该查询树列表是空的。更新规则中可以有零个（NOTHING关键字）、一个或多个动作。为简单起见，我们先看一个只有一个动作的规则。这个规则可以有条件或者没有条件，并且它可以是INSTEAD或ALSO（缺省）。

什么是规则条件？它是一个限制，告诉规则动作什么时候做、什么时候不做。这个条件只能引用NEW和/或OLD伪关系，它们基本上代表作为对象给定的关系（但是有着特殊含义）。

所以，对这个单动作的规则生成下面的查询树，我们有三种情况。

没有条件，有ALSO或INSTEAD来自规则动作的查询树，在其上增加原始查询树的条件给出了条件，有ALSO来自规则动作的查询树，在其上加入规则条件和原始查询树的条件给出了条件，有INSTEAD来自规则动作的查询树，在其上加入规则条件和原始查询树的条件；以及带有反规则条件的原始查询树。最后，如果规则是ALSO，那么未修改的原始查询树也被加入到列表。因为只有合格的INSTEAD规则已经被加入到原始查询树中，对于单动作的规则，我们将结束于一个或两个输出查询树。

对于ON INSERT规则，原始查询（如果没有被INSTEAD取代）是在任何规则增加的动作之前完成的。这样就允许动作看到被插入的行。但是对ON UPDATE 和ON DELETE规则，原始查询是在规则增加的动作之后完成的。这样就确保动作可以看到将要更新或者将要删除的行；否则，动作可能什么也不做，因为它们无法发现符合它们要求的行。

从规则动作生成的查询树会被再次丢给重写系统，并且可能有更多规则被应用而得到更多或更少的查询树。所以一个规则的动作必须有一种不同的命令类型或者和规则所在的关系不同的另一个结果关系。 否则这样的递归处理就会没完没了（规则的递规展开会被检测到，并当作一个错误报告）。

在pg\_rewrite系统目录中的动作中的查询树只是模板。因为它们可以引用NEW和OLD的范围表项，在使用它们之前必须做一些替换。对于任何NEW的引用，都要先在原始查询的目标列表中搜索对应的项。如果找到，该项的表达式将会替换该引用。否则NEW和OLD的含义一样（对于UPDATE）或者被替换成一个空值（对于INSERT）。任何对OLD的引用都用结果关系的范围表项的引用替换。

在系统完成应用更新规则后，它再应用视图规则到生成的查询树上。视图无法插入新的更新动作，所以没有必要向视图重写的输出应用更新规则。

#### 第一个规则循序渐进

假设我们想要跟踪shoelace\_data关系中的sl\_avail列。所以我们建立一个日志表和一条规则，这条规则每次在shoelace\_data上执行UPDATE时有条件地写入一个日志项。

CREATE TABLE shoelace\_log (

sl\_name text, -- 改变的鞋带

sl\_avail integer, -- 新的可用值

log\_who text, -- 谁做的

log\_when timestamp -- 何时做的

);

CREATE RULE log\_shoelace AS ON UPDATE TO shoelace\_data

WHERE NEW.sl\_avail <> OLD.sl\_avail

DO INSERT INTO shoelace\_log VALUES (

NEW.sl\_name,

NEW.sl\_avail,

current\_user,

current\_timestamp

);

现在有人做：

UPDATE shoelace\_data SET sl\_avail = 6 WHERE sl\_name = 'sl7';

然后看看日志表：

SELECT \* FROM shoelace\_log;

sl\_name | sl\_avail | log\_who | log\_when

\---------+----------+---------+----------------------------------

sl7 | 6 | Al | Tue Oct 20 16:14:45 1998 MET DST

(1 row)

这就是我们所期望的。在后台发生的的事情如下。解析器创建查询树：

UPDATE shoelace\_data SET sl\_avail = 6

FROM shoelace\_data shoelace\_data

WHERE shoelace\_data.sl\_name = 'sl7';

这是一个带有规则条件表达式的ON UPDATE规则log\_shoelace ，条件是：

NEW.sl\_avail <> OLD.sl\_avail

它的动作是：

INSERT INTO shoelace\_log VALUES (

new.sl\_name, new.sl\_avail,

current\_user, current\_timestamp )

FROM shoelace\_data new, shoelace\_data old;

（这看起来有点奇怪，因为你通常不能写INSERT... VALUES... FROM。这里的FROM子句只是表示查询树里有用于new和old的范围表项。这些东西是必需的，这样它们就可以被INSERT命令的查询树中的变量引用）。

该规则是一个有条件的ALSO规则，所以规则系统必须返回两个查询树：更改过的规则动作和原始查询树。在第 1 步里，原始查询的范围表被集成到规则动作的查询树中。得到：

INSERT INTO shoelace\_log VALUES (

new.sl\_name, new.sl\_avail,

current\_user, current\_timestamp )

FROM shoelace\_data new, shoelace\_data old,

shoelace\_data shoelace\_data;

第 2 步把规则条件增加进去，所以结果集被限制为sl\_avail改变了的行：

INSERT INTO shoelace\_log VALUES (

new.sl\_name, new.sl\_avail,

current\_user, current\_timestamp )

FROM shoelace\_data new, shoelace\_data old,

shoelace\_data shoelace\_data

WHERE new.sl\_avail <> old.sl\_avail;

（这看起来更奇怪，因为INSERT... VALUES也没有WHERE子句，但是规划器和执行器处理它没有任何难度。不管怎样，它们需要为INSERT... SELECT支持这种相同功能）。

第 3 步把原始查询树的条件加进去，把结果集进一步限制成只有被初始查询树改变的行：

INSERT INTO shoelace\_log VALUES (

new.sl\_name, new.sl\_avail,

current\_user, current\_timestamp )

FROM shoelace\_data new, shoelace\_data old,

shoelace\_data shoelace\_data

WHERE new.sl\_avail <> old.sl\_avail

AND shoelace\_data.sl\_name = 'sl7';

第 4 步把NEW引用替换为来自原始查询树的目标列表项或来自结果关系的相匹配的变量引用：

INSERT INTO shoelace\_log VALUES (

shoelace\_data.sl\_name, 6,

current\_user, current\_timestamp )

FROM shoelace\_data new, shoelace\_data old,

shoelace\_data shoelace\_data

WHERE 6 <> old.sl\_avail

AND shoelace\_data.sl\_name = 'sl7';

第 5 步，用结果关系引用把OLD引用替换掉：

INSERT INTO shoelace\_log VALUES (

shoelace\_data.sl\_name, 6,

current\_user, current\_timestamp )

FROM shoelace\_data new, shoelace\_data old,

shoelace\_data shoelace\_data

WHERE 6 <> shoelace\_data.sl\_avail

AND shoelace\_data.sl\_name = 'sl7';

这就完成了。因为规则是ALSO，我们还要输出原始查询树。简而言之，从规则系统输出的是一个包含两个查询树的列表，它们与下面语句相对应：

INSERT INTO shoelace\_log VALUES (

shoelace\_data.sl\_name, 6,

current\_user, current\_timestamp )

FROM shoelace\_data

WHERE 6 <> shoelace\_data.sl\_avail

AND shoelace\_data.sl\_name = 'sl7';

UPDATE shoelace\_data SET sl\_avail = 6

WHERE sl\_name = 'sl7';

这些会按照这个顺序被执行，并且这也正是规则要做的事情。

做的替换和追加的条件用于确保对于下面这样的原始查询不会有日志记录被写入：

UPDATE shoelace\_data SET sl\_color = 'green'

WHERE sl\_name = 'sl7';

在这种情况下，原始查询树不包含sl\_avail的目标列表项，因此NEW.sl\_avail将被shoelace\_data.sl\_avail代替。所以，规则生成的额外命令是：

INSERT INTO shoelace\_log VALUES (

shoelace\_data.sl\_name, shoelace\_data.sl\_avail,

current\_user, current\_timestamp )

FROM shoelace\_data

WHERE shoelace\_data.sl\_avail <> shoelace\_data.sl\_avail

AND shoelace\_data.sl\_name = 'sl7';

并且条件将永远不可能为真。

如果原始查询修改多个行，这也能争产工作。所以如果某人发出命令：

UPDATE shoelace\_data SET sl\_avail = 0

WHERE sl\_color = 'black';

实际上有四行（sl1、sl2、sl3和sl4）被更新。但sl3已经是sl\_avail = 0。在这种情况下，原始查询树的条件不同并且导致规则产生额外的查询树：

INSERT INTO shoelace\_log

SELECT shoelace\_data.sl\_name, 0,

current\_user, current\_timestamp

FROM shoelace\_data

WHERE 0 <> shoelace\_data.sl\_avail

AND shoelace\_data.sl\_color = 'black';

这个查询树将肯定插入三个新的日志项。这也是完全正确的。

到这里我们就能明白为什么原始查询树最后执行非常重要。如果UPDATE先被执行，则所有的行都已经被设为零，所以记日志的INSERT将无法找到任何符合0 <> shoelace\_data.sl\_avail的行。

### 与视图合作

要保护一个视图关系不被INSERT、UPDATE或DELETE，一种简单的方法是让那些查询树被丢掉。因此我们可以创建规则：

CREATE RULE shoe\_ins\_protect AS ON INSERT TO shoe

DO INSTEAD NOTHING;

CREATE RULE shoe\_upd\_protect AS ON UPDATE TO shoe

DO INSTEAD NOTHING;

CREATE RULE shoe\_del\_protect AS ON DELETE TO shoe

DO INSTEAD NOTHING;

如果现在某人尝试对视图关系shoe做任何这些操作，规则系统将应用这些规则。因为这些规则没有动作而且是INSTEAD，作为的查询树列表将是空的并且整个查询将变得什么也不做，因为经过规则系统处理后没有什么东西剩下来被优化或执行了。

一个更好的使用规则系统的方法是创建一些规则，这些规则把查询树重写成一个在真实表上进行正确的操作的查询树。 要在视图shoelace上做这件事，我们创建下列规则：

CREATE RULE shoelace\_ins AS ON INSERT TO shoelace

DO INSTEAD

INSERT INTO shoelace\_data VALUES (

NEW.sl\_name,

NEW.sl\_avail,

NEW.sl\_color,

NEW.sl\_len,

NEW.sl\_unit

);

CREATE RULE shoelace\_upd AS ON UPDATE TO shoelace

DO INSTEAD

UPDATE shoelace\_data

SET sl\_name = NEW.sl\_name,

sl\_avail = NEW.sl\_avail,

sl\_color = NEW.sl\_color,

sl\_len = NEW.sl\_len,

sl\_unit = NEW.sl\_unit

WHERE sl\_name = OLD.sl\_name;

CREATE RULE shoelace\_del AS ON DELETE TO shoelace

DO INSTEAD

DELETE FROM shoelace\_data

WHERE sl\_name = OLD.sl\_name;

如果你要在视图上支持RETURNING查询，你需要让规则包含RETURNING子句来计算视图行。这对于基于单个表的视图来说通常非常简单，但是对于连接视图（如shoelace）就有点冗长了。对于插入的一个例子：

CREATE RULE shoelace\_ins AS ON INSERT TO shoelace

DO INSTEAD

INSERT INTO shoelace\_data VALUES (

NEW.sl\_name,

NEW.sl\_avail,

NEW.sl\_color,

NEW.sl\_len,

NEW.sl\_unit

)

RETURNING

shoelace\_data.\*,

(SELECT shoelace\_data.sl\_len \* u.un\_fact

FROM unit u WHERE shoelace\_data.sl\_unit = u.un\_name);

注意，这个规则同时支持该视图上的INSERT和INSERT RETURNING查询 — 对于INSERT会简单地忽略RETURNING子句。

现在假设有时一包鞋带抵达了商店，并且随着它有一个大的清单。但是你不想每次都手工更新shoelace视图。取而代之的是我们建立两个小表：一个用来从清单向其中插入东西，另一个则用了一个特殊的技巧。这些东西的创建命令如下：

CREATE TABLE shoelace\_arrive (

arr\_name text,

arr\_quant integer

);

CREATE TABLE shoelace\_ok (

ok\_name text,

ok\_quant integer

);

CREATE RULE shoelace\_ok\_ins AS ON INSERT TO shoelace\_ok

DO INSTEAD

UPDATE shoelace

SET sl\_avail = sl\_avail + NEW.ok\_quant

WHERE sl\_name = NEW.ok\_name;

现在你可以用来自清单的数据填充表shoelace\_arrive：

SELECT \* FROM shoelace\_arrive;

arr\_name | arr\_quant

\----------+-----------

sl3 | 10

sl6 | 20

sl8 | 20

(3 rows)

快速地看一看当前的数据：

SELECT \* FROM shoelace;

sl\_name | sl\_avail | sl\_color | sl\_len | sl\_unit | sl\_len\_cm

\----------+----------+----------+--------+---------+-----------

sl1 | 5 | black | 80 | cm | 80

sl2 | 6 | black | 100 | cm | 100

sl7 | 6 | brown | 60 | cm | 60

sl3 | 0 | black | 35 | inch | 88.9

sl4 | 8 | black | 40 | inch | 101.6

sl8 | 1 | brown | 40 | inch | 101.6

sl5 | 4 | brown | 1 | m | 100

sl6 | 0 | brown | 0.9 | m | 90

(8 rows)

插入数据：

INSERT INTO shoelace\_ok SELECT \* FROM shoelace\_arrive;

并检查结果：

SELECT \* FROM shoelace ORDER BY sl\_name;

sl\_name | sl\_avail | sl\_color | sl\_len | sl\_unit | sl\_len\_cm

\----------+----------+----------+--------+---------+-----------

sl1 | 5 | black | 80 | cm | 80

sl2 | 6 | black | 100 | cm | 100

sl7 | 6 | brown | 60 | cm | 60

sl4 | 8 | black | 40 | inch | 101.6

sl3 | 10 | black | 35 | inch | 88.9

sl8 | 21 | brown | 40 | inch | 101.6

sl5 | 4 | brown | 1 | m | 100

sl6 | 20 | brown | 0.9 | m | 90

(8 rows)

SELECT \* FROM shoelace\_log;

sl\_name | sl\_avail | log\_who| log\_when

\---------+----------+--------+----------------------------------

sl7 | 6 | Al | Tue Oct 20 19:14:45 1998 MET DST

sl3 | 10 | Al | Tue Oct 20 19:25:16 1998 MET DST

sl6 | 20 | Al | Tue Oct 20 19:25:16 1998 MET DST

sl8 | 21 | Al | Tue Oct 20 19:25:16 1998 MET DST

(4 rows)

从一个INSERT... SELECT到这些结果经过了很长的过程。并且该查询树转换的描述将出现在本章的最后。首先，这里是解析器的输出：

INSERT INTO shoelace\_ok

SELECT shoelace\_arrive.arr\_name, shoelace\_arrive.arr\_quant

FROM shoelace\_arrive shoelace\_arrive, shoelace\_ok shoelace\_ok;

现在应用第一条规则shoelace\_ok\_ins被应用并且把这个输出转换成：

UPDATE shoelace

SET sl\_avail = shoelace.sl\_avail + shoelace\_arrive.arr\_quant

FROM shoelace\_arrive shoelace\_arrive, shoelace\_ok shoelace\_ok,

shoelace\_ok old, shoelace\_ok new,

shoelace shoelace

WHERE shoelace.sl\_name = shoelace\_arrive.arr\_name;

并且丢掉shoelace\_ok上的INSERT。这个被重写后的查询被再次传递给规则系统，并且第二个被应用的规则shoelace\_upd会产生：

UPDATE shoelace\_data

SET sl\_name = shoelace.sl\_name,

sl\_avail = shoelace.sl\_avail + shoelace\_arrive.arr\_quant,

sl\_color = shoelace.sl\_color,

sl\_len = shoelace.sl\_len,

sl\_unit = shoelace.sl\_unit

FROM shoelace\_arrive shoelace\_arrive, shoelace\_ok shoelace\_ok,

shoelace\_ok old, shoelace\_ok new,

shoelace shoelace, shoelace old,

shoelace new, shoelace\_data shoelace\_data

WHERE shoelace.sl\_name = shoelace\_arrive.arr\_name

AND shoelace\_data.sl\_name = shoelace.sl\_name;

同样这是一个INSTEAD规则并且前一个查询树会被丢弃掉。注意这个查询仍然使用视图shoelace。但是规则系统还没有完成这一步，所以它会继续并在其上应用\_RETURN规则，并且我们得到：

UPDATE shoelace\_data

SET sl\_name = s.sl\_name,

sl\_avail = s.sl\_avail + shoelace\_arrive.arr\_quant,

sl\_color = s.sl\_color,

sl\_len = s.sl\_len,

sl\_unit = s.sl\_unit

FROM shoelace\_arrive shoelace\_arrive, shoelace\_ok shoelace\_ok,

shoelace\_ok old, shoelace\_ok new,

shoelace shoelace, shoelace old,

shoelace new, shoelace\_data shoelace\_data,

shoelace old, shoelace new,

shoelace\_data s, unit u

WHERE s.sl\_name = shoelace\_arrive.arr\_name

AND shoelace\_data.sl\_name = s.sl\_name;

最后，规则log\_shoelace被应用，生成额外的查询树：

INSERT INTO shoelace\_log

SELECT s.sl\_name,

s.sl\_avail + shoelace\_arrive.arr\_quant,

current\_user,

current\_timestamp

FROM shoelace\_arrive shoelace\_arrive, shoelace\_ok shoelace\_ok,

shoelace\_ok old, shoelace\_ok new,

shoelace shoelace, shoelace old,

shoelace new, shoelace\_data shoelace\_data,

shoelace old, shoelace new,

shoelace\_data s, unit u,

shoelace\_data old, shoelace\_data new

shoelace\_log shoelace\_log

WHERE s.sl\_name = shoelace\_arrive.arr\_name

AND shoelace\_data.sl\_name = s.sl\_name

AND (s.sl\_avail + shoelace\_arrive.arr\_quant) <> s.sl\_avail;

完成这些之后，规则系统用完了所有的规则并且返回生成的查询树。

所以我们结束于两个最终查询树，它们等效于SQL语句：

INSERT INTO shoelace\_log

SELECT s.sl\_name,

s.sl\_avail + shoelace\_arrive.arr\_quant,

current\_user,

current\_timestamp

FROM shoelace\_arrive shoelace\_arrive, shoelace\_data shoelace\_data,

shoelace\_data s

WHERE s.sl\_name = shoelace\_arrive.arr\_name

AND shoelace\_data.sl\_name = s.sl\_name

AND s.sl\_avail + shoelace\_arrive.arr\_quant <> s.sl\_avail;

UPDATE shoelace\_data

SET sl\_avail = shoelace\_data.sl\_avail + shoelace\_arrive.arr\_quant

FROM shoelace\_arrive shoelace\_arrive,

shoelace\_data shoelace\_data,

shoelace\_data s

WHERE s.sl\_name = shoelace\_arrive.sl\_name

AND shoelace\_data.sl\_name = s.sl\_name;

结果是从一个关系来的数据插入了到另一个中，改变成第三个上的更新，改变成更新第四个外加做日志，在第五个中的最后更新缩减为两个查询。

有一个小细节有点丑陋。看看那两个查询，我们会发现shoelace\_data关系在范围表中出现了两次而实际上绝对可以缩为出现一次。规划器不会处理它，因此INSERT的规则系统输出的执行规划会是

Nested Loop

\-> Merge Join

\-> Seq Scan

\-> Sort

\-> Seq Scan on s

\-> Seq Scan

\-> Sort

\-> Seq Scan on shoelace\_arrive

\-> Seq Scan on shoelace\_data

在省略额外的范围表项后会得到

Merge Join

\-> Seq Scan

\-> Sort

\-> Seq Scan on s

\-> Seq Scan

\-> Sort

\-> Seq Scan on shoelace\_arrive

这在日志表中生成完全一样的项。因此，规则系统导致了shoelace\_data表上的一次绝对不必要的扫描。并且同样的冗余扫描会在UPDATE中进行。但是要把这些全部实现实在是一项很困难的工作。

现在我们对瀚高数据库规则系统及其能力做最后一个演示。假设你向你的数据库中添加一些有特别颜色的鞋带：

INSERT INTO shoelace VALUES ('sl9', 0, 'pink', 35.0, 'inch', 0.0);

INSERT INTO shoelace VALUES ('sl10', 1000, 'magenta', 40.0, 'inch', 0.0);

我们想要建立一个视图来检查哪些shoelace项在颜色上不配任何鞋子。适用的视图是：

CREATE VIEW shoelace\_mismatch AS

SELECT \* FROM shoelace WHERE NOT EXISTS

(SELECT shoename FROM shoe WHERE slcolor = sl\_color);

它的输出是：

SELECT \* FROM shoelace\_mismatch;

sl\_name | sl\_avail | sl\_color | sl\_len | sl\_unit | sl\_len\_cm

\---------+----------+----------+--------+---------+-----------

sl9 | 0 | pink | 35 | inch | 88.9

sl10 | 1000 | magenta | 40 | inch | 101.6

现在我们想建立它，这样没有库存的不匹配的鞋带都会被从数据库中删除。为了对瀚高数据库有点难度，我们不直接删除它们。而是我们再创建一个视图：

CREATE VIEW shoelace\_can\_delete AS

SELECT \* FROM shoelace\_mismatch WHERE sl\_avail = 0;

然后用下面方法：

DELETE FROM shoelace WHERE EXISTS

(SELECT \* FROM shoelace\_can\_delete

WHERE sl\_name = shoelace.sl\_name);

Voilà:

SELECT \* FROM shoelace;

sl\_name | sl\_avail | sl\_color | sl\_len | sl\_unit | sl\_len\_cm

\---------+----------+----------+--------+---------+-----------

sl1 | 5 | black | 80 | cm | 80

sl2 | 6 | black | 100 | cm | 100

sl7 | 6 | brown | 60 | cm | 60

sl4 | 8 | black | 40 | inch | 101.6

sl3 | 10 | black | 35 | inch | 88.9

sl8 | 21 | brown | 40 | inch | 101.6

sl10 | 1000 | magenta | 40 | inch | 101.6

sl5 | 4 | brown | 1 | m |

sl6 | 20 | brown | 0.9 | m | 90

(9 rows)

对一个视图上的DELETE，这个命令带有一个总共使用了四个嵌套/连接视图的子查询条件，这四个视图之一本身有一个包含一个视图的子查询条件，该条件计算使用的视图列； 这个命令被重写成了一个查询树，该查询树从一个真正的表里面把需要删除的数据删除。

在现实世界里只有很少的情况需要上面的这样的构造。但这些东西能运转肯定让你感觉不错。

## 规则和权限

由于瀚高数据库规则系统对查询的重写，会访问没有在原始查询中指定的表/视图。使用更新规则时，这可能包括对表的写权限。

重写规则并不拥有一个独立的所有者。关系（表或视图）的所有者自动成为为其所定义的重写规则的所有者。瀚高数据库规则系统改变了默认的访问控制系统的行为。由于规则被使用的关系会按照规则所有者的权限来检查，而不是调用规则的用户。这表示用户只需要在其查询中显式指定的表/视图上的所需权限。

例如：某用户有一个电话号码列表，其中一些是私人的，另外的一些是办公室助理需要的。

该用户可以构建下面的东西：

CREATE TABLE phone\_data (person text, phone text, private boolean);

CREATE VIEW phone\_number AS

SELECT person, CASE WHEN NOT private THEN phone END AS phone

FROM phone\_data;

GRANT SELECT ON phone\_number TO assistant;

除了该用户以外没有人可以访问phone\_data表。但因为GRANT的原因，助理可以在phone\_number视图上运行SELECT。规则系统将把phone\_number上的SELECT重写为phone\_data上的SELECT。因为该用户是phone\_number的所有者，因此也是规则的所有者，对phone\_data的读访问现在被根据该用户的权限检查，并且该查询被允许。同时也要检查访问phone\_number的权限，但这是针对调用用户进行的，所以除了用户自己和助理外没有人可以使用它。

权限检查是按规则逐条进行的。所以此时助理是唯一的一个可以看到公共电话号码的人。

但助理可以建立另一个视图并且赋予该视图公共权限。这样，任何人都可以通过助理的视图看到phone\_number数据。 助理不能做的事情是创建一个直接访问phone\_data的视图（实际上助理是可以的，但没有任何作用，因为每次访问都会因通不过权限检查而被否定）。而且该用户一旦注意到助理开放了他的phone\_number视图，该用户还可以收回助理的访问权限。

立刻，所有对助理视图的访问将会失败。

有人可能会认为这种逐条规则的检查是一个安全漏洞，但事实上不是。 如果这样做不能奏效，助理将必须建立一个与phone\_number有相同列的表并且每天拷贝一次数据进去。 那么这是助理自己的数据因而助理可以为每一个想要访问的人授权。一个GRANT意味着”我信任你”。 如果某个你信任的人做了上面的事情，那么是时候认为信任已经结束并且要使用REVOKE。

需要注意的是，虽然视图可以用前文展示的技术来隐藏特定列的内容，它们不能可靠地在不可见行上隐藏数据，除非标志被设置。 例如，下面的视图是不安全的：

CREATE VIEW phone\_number AS

SELECT person, phone FROM phone\_data WHERE phone NOT LIKE '412%';

这个视图看起来是安全的，因为规则系统会把任何phone\_number上的SELECT重写成 phone\_data上的SELECT，并且增加限制使得只有phone 不以 412 开头的项才被处理。但是如果用户可以创建自己的函数，那就不难让规划器在NOT LIKE表达式之前先执行用户自定义函数。例如：

CREATE FUNCTION tricky(text, text) RETURNS bool AS $$

BEGIN

RAISE NOTICE '% => %', $1, $2;

RETURN true;

END

$$ LANGUAGE plpgsql COST 0.0000000000000000000001;

SELECT \* FROM phone\_number WHERE tricky(person, phone);

phone\_data表中的每一个人和电话号码会被打印成一个NOTICE，因为规划器会选择在执行NOT LIKE之前先执行tricky，因为前者的开销大。 即使禁止用户自定义一个新函数，内置函数也可以用在类似的攻击中（例如，大部分造型函数会在它们产生的错误信息中包含它们的输入值）。

类似的考虑应用于更新规则。在前一节的例子中，例子数据库中表的所有者可以把shoelace视图上的SELECT、INSERT、UPDATE和DELETE权限授予其他人，但对shoelace\_log只有SELECT权限。写日志项的规则动作将仍然可以被成功地执行，并且其它用户可以看到日志项。但他们不能创建伪造的项，并且他们也不能操纵或移除现有的项。在这种情况下，不可能通过让规划器改变操作的顺序来推翻规则，因为引用shoelace\_log的唯一规则是无限制的INSERT。在更复杂的情景中，这可能不正确。

当需要对一个视图提供行级安全时，security\_barrier属性应该被应用到该视图。这会阻止恶意选择的函数和操作符通过行被传递，直到视图完成其工作。例如，如果前文所示的视图被创建成这样，它就是安全的：

CREATE VIEW phone\_number WITH (security\_barrier) AS

SELECT person, phone FROM phone\_data WHERE phone NOT LIKE '412%';

Views created with the 使用security\_barrier创建的视图的性能会远差于没有使用该选项的视图。通常，没有办法来避免这种现状：如果最快的候选计划可能在安全性上折衷，它就必须被拒绝。出于该原因，这个选在在默认情况下是没有启用的。

当处理没有副作用的函数时，查询规划器有更多的灵活性。这类函数被称为LEAKPROOF，并且包括很多简单常用的操作符，例如很多等于操作符。查询规划器可以安全地允许这类函数在查询执行过程中的任何点被计算，因为在用户不可见的行上调用它们将不会泄露关于不可见行的任何信息。更进一步，不接收参数或者不从安全屏障视图得到任何参数的函数不必被标记为LEAKPROOF以便被下推，因为它们从来不会从该视图接收数据。相反，一个可能会基于接收到的参数值抛出错误的函数（例如在溢出或被零除事件中抛出错误的函数）不是防泄漏的，并且如果它被应用在安全性视图的行过滤器之前，它可能会提供有关不可见行的有效信息。

有一点很重要的是理解：即使一个视图使用security\_barrier选项创建，它也只在不可见元组不会被传递给可能不安全的函数的前提下才是安全的。用户可能也有其他方式来推断不可见数据；例如，他们可以使用EXPLAIN看到查询计划，或者针对视图来测量查询的运行时间。一个恶意攻击者可能有能力推断有关不可见数据的总量，或者甚至得到有关数据分布的某些信息或最常用值（因为这些东西可以影响计划的运行时间；或者甚至计划的选择，因为它们也被反映在优化器的统计数据中）。如果这类”隐通道”攻击很重要，那么授予任何到该数据的访问都可能是不明智的。

## 规则和命令状态

瀚高数据库服务器为它收到的每个命令返回一个命令状态字符串，例如INSERT 149592 1。没有涉及规则时这很简单，但是查询被规则重写时会发生什么呢？

规则对命令状态的影响如下：

• 如果没有查询的无条件INSTEAD规则，那么原始给出的查询将会被执行，并且它的命令状态将像平常一样被返回（但是请注意如果存在任何有条件INSTEAD规则，那么它们的反条件将被加到原始查询中。这样可能会减少它处理的行数，并且报告的状态将受影响）。

• 如果有查询的任何无条件INSTEAD规则，那么原始查询将完全不被执行。在这种情况下，服务器将返回由服务器将返回由INSTEAD规则（有条件的或无条件的）插入的最后一条和原始查询命令类型（INSERT、UPDATE或DELETE）相同的查询的命令状态。如果任何规则添加的查询都不符合这些要求，那么返回的命令状态显示原始查询类型并且行计数和 OID 域为零。

通过为任何想要的INSTEAD规则指定在活动规则中排名最后的规则名，程序员可以确保该规则都是在第二种情况里设置命令状态的规则，因为它会被最后一个应用。

## 规则 vs 触发器

许多触发器可以干的事情同样也可以用瀚高数据库规则系统来实现。目前不能用规则来实现的东西之一是某些约束，特别是外键。 可以放置一个合格的规则在一列上，这个规则在列的值没有出现在另一个表中时把命令重写成NOTHING。但是这样做数据就会被不声不响地丢弃，因此也不是一个好主意。如果要求检查值的有效性，并且在出现无效值的情况下应该生成一个错误消息，这种需求就必须要用触发器来完成。

在本章中，我们关注于使用规则来更新视图。本章中所有的更新规则的例子都可以使用视图上的INSTEAD OF触发器来实现。编写这类触发器通常比编写规则要容易，特别是在要求使用复杂逻辑来执行更新的情况下。

对于两者都可实现的情况，哪个更好取决于对数据库的使用。触发器为每一个受影响的行都执行一次。规则修改查询树或生成一个额外的查询。所以如果在一个语句中影响到很多行，一个发出额外查询的规则通常可能会比一个触发器快，因为触发器对每一个行都要被调用，并且每次被调用时都需要重新判断要做什么样的操作。不过，触发器方法从概念上要远比规则方法简单，并且很容易让新人上手。

下面我们展示一个例子，该例子说明了在同种情况下两种选择的比较。这里有两个表：

CREATE TABLE computer (

hostname text, -- 被索引

manufacturer text -- 被索引

);

CREATE TABLE software (

software text, -- 被索引

hostname text -- 被索引

);

两个表都有数千行，并且在hostname上的索引是唯一的。规则或触发器应该实现一个约束，该约束从software中删除引用已删除计算机的行。 触发器可以用下面这条命令：

DELETE FROM software WHERE hostname = $1;

因为触发器会为每一个从computer中删除的独立行调用一次， 那么它可以准备并且保存这个命令的规划，把hostname作为参数传入。规则应该被写为：

CREATE RULE computer\_del AS ON DELETE TO computer

DO DELETE FROM software WHERE hostname = OLD.hostname;

现在看看不同类型的删除。在这种情况：

DELETE FROM computer WHERE hostname = 'mypc.local.net';

表computer被使用索引（快速）扫描，并且由触发器发出的命令也将使用一个索引扫描（同样快速）。来自规则的额外查询应该是：

DELETE FROM software WHERE computer.hostname = 'mypc.local.net'

AND software.hostname = computer.hostname;

由于已经建立了合适的索引，规划器将创建一个规划

Nestloop

\-> Index Scan using comp\_hostidx on computer

\-> Index Scan using soft\_hostidx on software

所以在触发器和规则的实现之间没有太多的速度差别。

在接下来的删除中，我们想要去掉所有 2000 个hostname以old开头的计算机。有两个命令可以来做这件事。一个是：

DELETE FROM computer WHERE hostname >= 'old'

AND hostname < 'ole'

被规则增加的命令将是：

DELETE FROM software WHERE computer.hostname >= 'old' AND computer.hostname <

'ole'

AND software.hostname = computer.hostname;

计划是：

Hash Join

\-> Seq Scan on software

\-> Hash

\-> Index Scan using comp\_hostidx on computer

另一个可能的命令是：

DELETE FROM computer WHERE hostname ~ '^old';

它会为规划增加的命令产生下面的执行计划：

Nestloop

\-> Index Scan using comp\_hostidx on computer

\-> Index Scan using soft\_hostidx on software

这表明，当有多个条件表达式被使用AND组合在一起时，规划器不能认识到表computer中hostname上的条件也可以被用于一个software上的索引扫描， 而在该命令的正则表达式版本中正是这样做的。触发器将为要被删除的 2000 个旧计算机中的每一个调用，并且会导致在computer上的一次索引扫描和software上的 2000 次索引扫描。采用规则的实现将会使用两个使用索引的命令来完成。 并且在顺序扫描情况下规则是否仍将更快是取决于software表的总体大小的。即使所有的索引块都将很快地进入高速缓存，通过 SPI 管理器执行来自触发器的 2000 个命令也要花不少时间。

我们要看的最后一个命令是：

DELETE FROM computer WHERE manufacturer = 'bim';

同样，这也会导致很多行被从computer中删除。所以触发器同样会通过执行器运行很多命令。规则生成的命令将会是：

DELETE FROM software WHERE computer.manufacturer = 'bim'

AND software.hostname = computer.hostname;

这个命令的计划又将是在两个索引扫描上的嵌套循环，只不过使用了computer上的另一个索引：

Nestloop

\-> Index Scan using comp\_manufidx on computer

\-> Index Scan using soft\_hostidx on software

在任何这些情况之一，来自规则系统的额外命令都或多或少与命令中影响的行数无关。

概括来说，规则只有在其动作导致了大而且糟糕的条件连接时才会明显地慢于触发器，这种情况下规划器将没有什么办法。