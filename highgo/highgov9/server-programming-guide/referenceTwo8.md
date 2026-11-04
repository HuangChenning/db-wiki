---
title: "PLTcl-Tcl过程语言"
book: "服务器编程指南"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/reference/referenceTwo8.html"
tags:
  - highgo
  - highgo-v9
  - server-programming-guide
---

## PL/Tcl - Tcl 过程语言

PL/Tcl 是一种用于瀚高数据库数据库系统的可载入过程语言， 它可以让Tcl 语言1被用来编写瀚高数据库函数。

## 概述

PL/Tcl 提供了大部分函数编写者在 C 语言中能够获得的能力，虽然有一些限制，但是却额外提供了 Tcl 中强大的字符串处理库。

一种强制性的好限制是所有被执行的东西都处于 Tcl 解释器的安全上下文中。除了安全 Tcl的有限的命令集合之外，只有几个通过 SPI 访问数据库的命令以及通过elog()产生消息的命令。PL/Tcl 没有提供访问数据库服务器内部或者在瀚高数据库服务器进程权限之下得到 OS-级访问的方法，而 C 函数是可以那样做的。因此，非特权数据库用户可以使用这种语言，它不会给予他们无限制的权利。

其他值得注意的实现限制是 Tcl 函数不能被用来创建新数据类型的输入/输出函数。

有时候我们想要编写不受安全 Tcl 限制的 Tcl 函数。例如，我们可能想要一个能发送电子邮件的 Tcl 函数。要处理这些情况，可以使用一种PL/Tcl的变体，它被称为PL/TclU（用于非可信 Tcl）。它其实是完全相同的一种语言，不过它使用了一个完整的Tcl 解释器。如果使用了PL/TclU，它必须被安装为一种非可信的过程语言，这样只有数据库超级用户可以用它来创建函数。PL/TclU函数的编写者必须注意该函数不能被用来做其设计目的之外的事情，因为该函数能做一个作为数据库管理员登录的用户可以做的任何事情。

如果在安装过程的配置步骤中指定了 Tcl 支持，PL/Tcl以及PL/TclU调用处理器的共享对象代码会被自动编译并且被安装在瀚高数据库的库目录中。要在一个特定数据库中安装PL/Tcl或者PL/TclU，请使用CREATE EXTENSION命令，例如CREATE EXTENSION pltcl或者CREATE EXTENSION pltclu。

## PL/Tcl 函数和参数

要用PL/Tcl语言创建函数，可使用标准的CREATE FUNCTION语法：

CREATE FUNCTION funcname (argument-types) RETURNS return-type AS $$

\# PL/Tcl function body

$$ LANGUAGE pltcl;

PL/TclU的函数是一样的语法，只是语言被指定为pltclu。

函数的主体就是一个 Tcl 脚本。当函数被调用时，参数值会被以变量名$1... $n传递给该 Tcl脚本。结果会以常见的方式通过一个return语句从 Tcl 脚本中返回。在一个过程中，Tcl代码的返回值会被忽略。

例如，一个返回两个整数值中较大值的函数可以定义为：

CREATE FUNCTION tcl\_max(integer, integer) RETURNS integer AS $$

if {$1 > $2} {return $1}

return $2

$$ LANGUAGE pltcl STRICT;

注意子句STRICT，它让我们不用去操心空输入值：如果空值被传入，函数根本就不会被调用，而是自动地返回一个空结果。

在非严格函数中，如果一个参数的实际值为空，对应的$n变量将被设置为一个空串。为了检测一个特定参数是否为空，可使用函数argisnull。例如，假设我们想要带有一个空参数和一个非空参数并且返回非空参数的tcl\_max：

CREATE FUNCTION tcl\_max(integer, integer) RETURNS integer AS $$

if {\[argisnull 1\]} {

if {\[argisnull 2\]} { return\_null }

return $2

}

if {\[argisnull 2\]} { return $1 }

if {$1 > $2} {return $1}

return $2

$$ LANGUAGE pltcl;

如上所述，要从一个 PL/Tcl 函数返回空值，可执行return\_null。不管函数是严格还是非严格都可以这样做。

组合类型参数会被作为 Tcl 数组传递给函数。该数组的元素名就是组合类型的属性值。如果被传入行的一个属性为空值，它不会出现在数组中。这里是一个例子：

CREATE TABLE employee (

name text,

salary integer,

age integer

);

CREATE FUNCTION overpaid(employee) RETURNS boolean AS $$

if {200000.0 < $1(salary)} {

return "t"

}

if {$1(age) < 30 && 100000.0 < $1(salary)} {

return "t"

}

return "f"

$$ LANGUAGE pltcl;

PL/Tcl函数也能返回组合类型的结果。要返回组合类型结果，Tcl代码必须返回匹配预期结果类型的”列名/值”对的列表。任何从该列表中省略的列名将被返回为空，如果有预期之外的列名则会报出错误。这里是一个例子：

CREATE FUNCTION square\_cube(in int, out squared int, out cubed int) AS $$

return \[list squared \[expr {$1 \* $1}\] cubed \[expr {$1 \* $1 \* $1}\]\]

$$ LANGUAGE pltcl;

过程的输出参数以相同的方式返回，例如：

CREATE PROCEDURE tcl\_triple(INOUT a integer, INOUT b integer) AS $$

return \[list a \[expr {$1 \* 3}\] b \[expr {$2 \* 3}\]\]

$$ LANGUAGE pltcl;

CALL tcl\_triple(5, 10);

| 提示： |
| --- |
| 结果列表可以用Tcl的array get命令从想得到的元组的数组表示中造出。例如： CREATE FUNCTION raise\_pay(employee, delta int) RETURNS employee AS $ $ set 1(salary) \[expr {$1(salary) + $2}\] return \[array get 1\] $$ LANGUAGE pltcl; |

PL/Tcl函数能够返回集合。要返回集合，Tcl代码应该对每一个要返回的行调用一次return\_next，在返回标量类型时传入合适的值或者在返回组合类型时传入”列名/值”堆的列表。这里是一个返回标量类型的例子：

CREATE FUNCTION sequence(int, int) RETURNS SETOF int AS $$

for {set i $1} {$i < $2} {incr i} {

return\_next $i

}

$$ LANGUAGE pltcl;

这里是一个返回组合类型的例子：

CREATE FUNCTION table\_of\_squares(int, int) RETURNS TABLE (x int, x2 int) AS $$

for {set i $1} {$i < $2} {incr i} {

return\_next \[list x $i x2 \[expr {$i \* $i}\]\]

}

$$ LANGUAGE pltcl;

## PL/Tcl 中的数据值

提供给 PL/Tcl 函数代码的参数值是输入参数简单转换而成的文本形式（就像被SELECT语句显示的那样）。反过来，return和return\_next命令将接受任何字符串，只要它是该函数声明的返回类型的可接受的输入格式，或者是组合结果类型的指定列的可接受输入格式。

## PL/Tcl 中的全局数据

有时候需要在同一个函数的两次调用间保持某些全局数据或者在不同的函数之间共享全局数据。在 PL/Tcl中这很容易做到，但是必须了解一些限制。

由于安全性原因，PL/Tcl会为一个SQL角色建立一个单独的Tcl解释器来执行该角色调用的函数。这可以避免一个用户无意或者恶意地干涉另一个用户的PL/Tcl 函数的行为。对任何”全局”Tcl 变量，每一个这样的解释器都有其自身的值。因此，当且仅当两个PL/ Tcl函数由用一个SQL角色执行时，它们才能共享相同的全局变量。在使用单个会话执行多个SQL 角色的代码（通过SECURITY DEFINER函数、使用SET ROLE等）的应用中，需要采取显式的步骤以保证PL/Tcl函数能共享数据。要这样做，需要确保要通信的函数都属于同一个用户，并且把它们标记为SECURITY DEFINER。当然，要小心这样的函数被滥用。

在一个会话中使用的所有 PL/TclU函数都在同一个Tcl解释器中执行，这当然与用于 PL/ Tcl 函数的解释器不同。因此，在 PL/TclU函数之间会自动地共享全局数据。这并不是一种安全性风险，因为所有的 PL/TclU 函数都在同样的信任级别上执行，即都以数据库超级用户的级别执行。

为了保护 PL/Tcl 函数不会无意间彼此干扰，通过upvar命令可以建立一个对每个函数可用的全局数组。这个变量的全局名称是该函数的内部名称，并且本地名称为GD。推荐使用GD来保持一个函数的持久私有数据。只对你特别希望在多个函数之间共享的值使用常规的 Tcl 全局变量（注意GD数组只在一个特定的解释器中是全局的，因此它们不会绕过上文提到的安全性限制）。

下文的spi\_execp例子中有一个使用GD的例子。

## 从 PL/Tcl 访问数据库

下面的命令可以用来从 PL/Tcl 函数体中访问数据库：

spi\_exec?-count n??-array name? command?loop-body?

执行一个以字符串给出的SQL命令。命令中错误将会导致错误发生。否则，spi\_exec的返回值是被命令处理的行数（选择、插入、更新或者删除），如果命令是一条功能性语句则返回零。此外，如果命令是一条SELECT语句，被选中的列的值会被放在上文所述的Tcl变量中。

可选的-count值告诉spi\_exec命令中要处理的最大行数。这种效果类似于用游标建立一个查询然后使用FETCH n。

如果命令是一条SELECT语句，结果列的值会被放在以列名命名的Tcl变量中。如果给出了-array选项，列值会被存储在所提及的关联数组的元素中，而列名则被用作数组索引。此外，结果中的当前行号（从零开始记）被存储在数组元素”.tupno”中，除非这个名字在结果中已经被用作一个列名。

如果命令是一条SELECT语句并且没有给出loop-body脚本，则只有结果的第一行被存储在Tcl 变量或数组元素中。如果结果中有剩余的行，它们会被忽略。如果查询不返回行则不存储任何东西（这种情况可以通过spi\_exec的结果检测到）。例如：

spi\_exec "SELECT count(\*) AS cnt FROM pg\_proc"

将把Tcl变量$cnt设置为pg\_proc系统目录中的行数。

如果给出了可选的loop-body参数，它会是一个Tcl脚本，对查询结果中的每一行都要执行这个脚本（如果给出的查询不是SELECT则忽略loop-body）。在每次迭代前当前行的列值会被存储在 Tcl 变量或数组元素中。例如：

spi\_exec -array C "SELECT \* FROM pg\_class" {

elog DEBUG "have table $C(relname)"

}

会对pg\_class的每一行打印一段日志消息。这种特性工作起来类似于其他的 Tcl 循环结构。特别是continue和break的动作方式与在循环体中的通常方式相同。

如果一个查询结果的一列为空，为它准备的目标变量不会被建立，而是会被”unset”。

spi\_prepare query typelist

为后面的执行准备并且保存一个查询计划。保存下来的计划将在当前会话的生命期内存在。

查询可以使用参数，也就是占位符。在计划真正被执行时将会为占位符提供值。在查询字符串中，可以用符号$1... $n引用参数。如果查询使用了参数，参数类型的名称必须以一个 Tcl 列表的形式给出（如果不使用参数，可以为typelist写一个空列表）。

从spi\_prepare返回的值是一个查询 ID，在后续的spi\_execp调用中需要用到这个 ID。

例子可见spi\_execp。

spi\_execp?-count n??-array name??-nulls string? queryid?value-list??loop-body?

执行一个之前用spi\_prepare准备的查询。queryid是spi\_prepare返回的 ID。如果查询引用参数，则必须提供一个value-list。这是一个参数实际值的Tcl列表。这个列表必须和之前传给spi\_prepare的参数类型列表具有相同的长度。如果查询没有参数则可省略value-list。

\-nulls的值可选，它是一个空格和'n'字符构成的串，它告诉spi\_execp哪些参数是空值。如果给出这个值，它必须正好和value-list长度相等。如果没有给出这个值，所有的参数值都是空。

除了指定查询及其参数的方法，spi\_execp和spi\_exec很像。-count、-array以及loop-body选项是相同的，并且结果值也一样。

这里是一个使用预设计划的 PL/Tcl 函数的例子：

CREATE FUNCTION t1\_count(integer, integer) RETURNS integer AS $$

if {!\[ info exists GD(plan) \]} {

\# 第一次调用时准备保存的计划

set GD(plan) \[ spi\_prepare \\

"SELECT count(\*) AS cnt FROM t1 WHERE num >= \\$1 AND num <= \\

$2" \\

\[ list int4 int4 \] \]

}

spi\_execp -count 1 $GD(plan) \[ list $1 $2 \]

return $cnt

$$ LANGUAGE pltcl;

我们需要在给spi\_prepare的查询字符串里放上反斜线来确保$n标记会被原样传递给spi\_prepare，并且不会被 Tcl 变量替换。

subtransaction command

command中包含的Tcl脚本会被在一个SQL子事务中执行。如果该脚本返回一个错误，那么整个子事务会在把错误返回到外围的Tcl代码之前就回滚。更多细节和例子请参考第12.9 节。

quote string

在给定的字符串中双写所有单引号和反斜线字符。这可以被用来引用字符串，以便它们能被安全地插入到传给spi\_exec或者spi\_prepare的 SQL 命令字符串中。例如，考虑这样的 SQL命令字符串：

"SELECT '$val' AS ret"

这里的 Tcl 变量val实际上包含doesn't。这将会导致最终的命令串：

SELECT 'doesn't' AS ret

这种命令串会导致spi\_exec或spi\_prepare期间的解析错误。要正确地工作，提交的命令应该包含：

SELECT 'doesn''t' AS ret

在 PL/Tcl 中可以这样做：

"SELECT '\[ quote $val \]' AS ret"

spi\_execp的一个好处是你不必这样引用参数值，因为参数值不会被作为 SQL 命令串的一部分被解析。

elog level msg

发出一段日志或者错误消息。可能的级别是DEBUG、LOG、INFO、NOTICE、WARNING、ERROR以及FATAL。ERROR产生一个错误情况。

如果周围的Tcl代码没有捕捉它，错误会传播到调用查询，导致当前事务或者子事务被中止。这实际上与 Tcl 的error命令相同。FATAL中止事务并且导致当前会话关闭（可能在 PL/Tcl 函数中没有很好的理由来使用这种错误级别，但是为了完整性还是提供了这种级别）。其他级别只产生不同优先级的消息。一个特定级别的消息是被报告给客户端、写入到服务器日志或者两者都做，是由配置变量log\_min\_messages和client\_min\_messages所控制。

## PL/Tcl中的触发器函数

触发器函数也可以用 PL/Tcl 编写。瀚高数据库要求能作为触发器被调用的函数必须被声明为没有参数并且返回类型为trigger。

来自于触发器管理器的信息通过下列变量被传递给函数体：

$TG\_name

CREATE TRIGGER语句中触发器的名字。

$TG\_relid

导致触发器函数被调用的表的对象 ID。

$TG\_table\_name

导致触发器函数被调用的表的名字。

$TG\_table\_schema

导致触发器函数被调用的表所在的模式。

$TG\_relatts

表列名的 Tcl 列表，前面放上一个空列表元素。因此用Tcl的lsearch命令在该列表中查找一个列名返回的元素编号会从 1 开始（对于第一列），这和瀚高数据库中的自定义编号是同样的方式（空列表元数也出现在被删除的列的位置上，这样其右边的列的属性编号才是正确的）。

$TG\_when

可以为BEFORE、AFTER或者INSTEAD OF，具体的选择取决于触发器事件的类型。

$TG\_level

可以为ROW或者STATEMENT，取决于触发器事件的类型。

$TG\_op

可以为INSERT、UPDATE、DELETE或者TRUNCATE，取决于触发器事件的类型。

$NEW

对于INSERT或者UPDATE动作是一个包含着新表行值的关联数组，对于DELETE为空。该数组以列名为索引。为空的列不会出现在数组中。对于语句级触发器这个变量不会被设置。

$OLD

对于UPDATE或者DELETE动作是一个包含着新表行值的关联数组，对于INSERT为空。该数组以列名为索引。为空的列不会出现在数组中。对于语句级触发器这个变量不会被设置。

$args

在CREATE TRIGGER语句中对过程给出的参数的 Tcl 列表。在过程体中也可以用$1...

$n来访问这些参数。

一个触发器函数的返回值可以是字符串OK或者SKIP，或者是一个”列名/值”对的列表。如果返回值是OK，引发该触发器的操作（INSERT/UPDATE/DELETE）将正常继续下去。SKIP告诉触发器管理器悄悄地抑制对这一行的该操作。如果返回一个列表，它告诉PL/Tcl返回一个被修改的行给触发器管理器，这个被修改的行的内容由列表中的列名和值指定。该列表中没有提到的任何列会被设置为空。返回被修改行只对行级BEFORE INSERT或UPDATE触发器有意义，对它们来说这个被修改的行将被插入而不是插入$NEW中给出的行。返回被修改行还对行级INSTEAD OF INSERT或UPDATE触发器有意义，其中被返回的行被用作INSERT RETURNING或UPDATE RETURNING子句的源数据。在行级BEFORE DELETE或INSTEAD OF DELETE触发器中，返回一个被修改行的效果和返回OK的效果相同，即操作继续。对所有其他类型的触发器来说，触发器返回值会被忽略。

| 提示： |
| --- |
| 结果列表可以用Tcl的array get命令从被修改的元组的数组表示中造出。 |

这里有一个触发器函数的例子，它用一个表中的整数值来跟踪在行上被执行的更新数。对于被插入的新行，该值被初始化为 0 并且之后在每一次更新操作时被加一。

CREATE FUNCTION trigfunc\_modcount() RETURNS trigger AS $$

switch $TG\_op {

INSERT {

set NEW($1) 0

}

UPDATE {

set NEW($1) $OLD($1)

incr NEW($1)

}

default {

return OK

}

}

return \[array get NEW\]

$$ LANGUAGE pltcl;

CREATE TABLE mytab (num integer, description text, modcnt integer);

CREATE TRIGGER trig\_mytab\_modcount BEFORE INSERT OR UPDATE ON mytab

FOR EACH ROW EXECUTE FUNCTION trigfunc\_modcount('modcnt');

注意触发器函数本身不知道列名，列名由触发器参数提供。这让触发器函数可以被重用于不同的表。

## PL/Tcl 中的事件触发器函数

事件触发器函数也可以用 PL/Tcl 编写。瀚高数据库要求能作为事件触发器被调用的函数必须被声明为没有参数并且返回类型为event\_trigger。

来自于触发器管理器的信息通过下列变量被传递给函数体：

$TG\_event

触发器为其引发的事件名。

$TG\_tag

触发器为其引发的命令标签。

触发器函数的返回值被忽略。

这里是一个事件触发器函数的小例子，它在所支持的命令每次执行时简单地产生一个NOTICE消息：

CREATE OR REPLACE FUNCTION tclsnitch() RETURNS event\_trigger AS $$

elog NOTICE "tclsnitch: $TG\_event $TG\_tag"

$$ LANGUAGE pltcl;

CREATE EVENT TRIGGER tcl\_a\_snitch ON ddl\_command\_start EXECUTE FUNCTION

tclsnitch();

## PL/Tcl 中的错误处理

PL/Tcl 函数中的 Tcl 代码或者从 PL/Tcl 函数中调用的代码可以抛出一个错误，错误可以由执行某些非法操作产生或者通过使用 Tcl error命令或者 PL/Tcl 的elog命令产生。Tcl中可以使用 Tcl catch命令捕获这类错误。如果一个错误没有被捕捉但是被允许传播到该PL/Tcl函数执行的顶层，它会在该函数的调用查询中被报告为一个SQL错误。

相反，在 PL/Tcl 的spi\_exec、spi\_prepare以及spi\_execp命令中发生的SQL错误会被报告为 Tcl 错误，因此它们也可以被 Tcl 的catch命令捕获（这些PL/Tcl命令中的每一个都在一个子事务中运行它的SQL操作，该子事务在错误时会被回滚，这样任何部分完成的操作也会被自动清除）。同样地，如果一个错误被传播到顶层而没有被捕获，它会转变成SQL错误。

Tcl 提供了一个errorCode变量，它表示有关于一个错误的附加信息，它的格式易于 Tcl 程序解释。该变量的内容符合 Tcl 列表格式，第一个词标识报告该错误的子系统或者库，之后的内容则留给子系统或者库来填充。对于 PL/Tcl 命令报告的数据库错误，第一个词是POSTGRES，第二个词是瀚高数据库的版本号，剩下的部分是域名称/域值构成的对，它们提供有关该错误的详细信息。域SQLSTATE、condition以及message总是会被提供（前两个表示附录 A中所示的错误代码和情况名称）。可能出现的域包括 detail、hint、context、schema、table、column、 datatype、constraint、 statement、cursor\_position、 filename、lineno以及 funcname。

使用 PL/Tcl 的errorCode信息的一种便捷方式是把它载入到一个数组中，这样域名称就变成了数组下标。这样做的代码看起来像这样

if {\[catch { spi\_exec $sql\_command }\]} {

if {\[lindex $::errorCode 0\] == "POSTGRES"} {

array set errorArray $::errorCode

if {$errorArray(condition) == "undefined\_table"} {

\# deal with missing table

} else {

\# deal with some other type of SQL error

}

}

}

（双冒号显式地指定errorCode是一个全局变量）。

## PL/Tcl中的显式子事务

从第 12.8 节中介绍的数据库访问导致的错误中恢复可能导致一种不可取的情况，其中一些操作在它们中的一个失败前成功完成，并且在从错误中恢复过来后数据还处于一种不一致的状态。PL/Tcl以显式子事务的形式为这类问题提供了一个解决方案。

考虑一个在两个账户间实现转账的函数：

CREATE FUNCTION transfer\_funds() RETURNS void AS $$

if \[catch {

spi\_exec "UPDATE accounts SET balance = balance - 100 WHERE account\_name

\= 'joe'"

spi\_exec "UPDATE accounts SET balance = balance + 100 WHERE account\_name

\= 'mary'"

} errormsg\] {

set result \[format "error transferring funds: %s" $errormsg\]

} else {

set result "funds transferred successfully"

}

spi\_exec "INSERT INTO operations (result) VALUES ('\[quote $result\]')"

$$ LANGUAGE pltcl;

如果第二个UPDATE语句导致一个异常，这个函数将记下该失败，但是第一个UPDATE的结果将被提交。换句话说，资金将从Joe的账户中被取走，但不会被转到Mary的账户。这是因为每个spi\_exec都是一个单独的子事务，并且那些子事务中只有一个被回滚。

为了处理这类情况，你可以把多个数据库操作包裹在一个显式子事务中，它将作为一个整体成功完成或者回滚。PL/Tcl提供了一个subtransaction命令来做这件事情。我们可以把我们的函数写成：

CREATE FUNCTION transfer\_funds2() RETURNS void AS $$

if \[catch {

subtransaction {

spi\_exec "UPDATE accounts SET balance = balance - 100 WHERE

account\_name = 'joe'"

spi\_exec "UPDATE accounts SET balance = balance + 100 WHERE

account\_name = 'mary'"

}

} errormsg\] {

set result \[format "error transferring funds: %s" $errormsg\]

} else {

set result "funds transferred successfully"

}

spi\_exec "INSERT INTO operations (result) VALUES ('\[quote $result\]')"

$$ LANGUAGE pltcl;

注意，为了实现这个目的仍要求使用catch。否则错误将传播到该函数的顶层，导致想要对operations表的插入被阻止。subtransaction命令不会捕捉错误，它仅确保报告错误时在其范围内执行的所有数据库操作将被一起回滚。

一个显式子事务的回滚发生在包含它的Tcl代码报告任何错误时，而不仅仅是数据库访问导致的错误。因此一个subtransaction命令中发生的常规Tcl异常也将导致该子事务被回滚。

不过，无错误退出到包含子事务的Tcl代码外面（例如，由于return）不会导致回滚。

## 事务管理

在从顶层调用的过程中或者从顶层调用的匿名代码块（DO命令）中，可以控制事务。要提交当前的事务，可调用commit。要回滚当前事务，可调用rollback（注意不能通过spi\_exec或类似的函数运行SQL命令COMMIT或者ROLLBACK。这类工作必须用这些函数完成）。在事务结束以后，一个新的事务会自动开始，因此没有独立的函数用来开始新事务。

这里是一个例子：

CREATE PROCEDURE transaction\_test1()

LANGUAGE pltcl

AS $$

for {set i 0} {$i < 10} {incr i} {

spi\_exec "INSERT INTO test1 (a) VALUES ($i)"

if {$i % 2 == 0} {

commit

} else {

rollback

}

}

$$;

CALL transaction\_test1();

当一个显式的子事务处于活跃状态时，事务不能被结束。

## PL/Tcl配置

这一节列举影响PL/Tcl的配置参数。

pltcl.start\_proc (string)

如果被设置为一个非空字符串，这个参数指定一个无参数PL/Tcl函数的名称（可能是方案限定的），只要为PL/Tcl创建一个新的Tcl解释器，就会执行这个函数。这样一个函数可以执行针对会话的初始化，例如载入额外的Tcl代码。当一个PL/Tcl在一个数据库会话中被第一次执行时，或者由于一个PL/Tcl函数被一个新的SQL角色调用而必须创建一个额外的解释器时，一个新的Tcl解释器会被创建。

被引用的函数必须用pltcl语言编写，并且不能被标记为SECURITY DEFINER（这些限制确保它运行在它应该要初始化的解释器中）。当前用户也必须有权限调用它。

如果该函数带着一个错误失败，它将中止导致新解释器创建的函数并且把错误传播到调用查询，进而导致当前事务或子事务被中止。在Tcl中已完成的任何动作将不会被撤销，不过，那个解释器将不会被再次使用。如果该语言被再次使用，则初始化将在一个全新的Tcl解释器中被再次尝试。

只有超级用户能够更改这个设置。尽管这个设置能在会话中更改，但这种更改将不会影响已经被创建的Tcl解释器。

pltclu.start\_proc (string)

这个参数与pltcl.start\_proc几乎一模一样，只不过它适用于PL/TclU。被引用的函数必须用pltclu语言编写。

## Tcl 过程名

在瀚高数据库，同一个函数名可以被用于不同的函数定义，只要它们的参数个数或者类型不同。不过，Tcl 要求所有过程名必须能区分。PL/Tcl 通过让内部 Tcl 过程名称包含该函数在系统表pg\_proc中的对象 ID 作为名称的一部分来解决这样的限制。因此，具有相同名称和不同参数类型的瀚高数据库函数也将是不同的 Tcl 过程。这对 PL/Tcl 程序员来说通常不需要关心，但是在调试时可见。