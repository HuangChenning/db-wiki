---
title: "服务器编程接口"
book: "服务器编程指南"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/reference/referenceTwo11.html"
tags:
  - highgo
  - highgo-v9
  - server-programming-guide
---

## 服务器编程接口

服务器编程接口（SPI）给予用户定义C函数编写者在其函数内运行SQL命令的能力。SPI是一组接口函数，它们可以简化对解析器、规划器和执行器的访问。SPI也做一些内存管理。

| 注意： |
| --- |
| 可用的过程语言提供了多种方法从函数中执行 SQL 命令。大部分这些设施都是基于 SPI 的，因此这个文档也对那些语言的用户有用。 |

注意如果一个通过 SPI 调用的命令失败，那么控制将会返回到你的C函数中。当然啦，你的C函数所在的事务或者子事务将被回滚（这可能看起来令人惊讶，因为据文档所说 SPI 函数大多数都有错误返回约定。但是那些约定只适用于在 SPI 函数本身内部检测到的错误）。通过在可能失败的 SPI 调用周围建立自己的子事务可以在错误之后恢复控制。

SPI成功时返回一个非负结果（要么通过一个返回的整数值，要么如下所述放在全局变量SPI\_result中）。错误时，将会返回一个负结果或者NULL。

使用 SPI 的源代码文件必须包括头文件executor/spi.h。

## 接口函数

### SPI\_connect

SPI\_connect, SPI\_connect\_ext — 连接一个C函数到 SPI 管理器

大纲

int SPI\_connect(void)

int SPI\_connect\_ext(int options)

描述

SPI\_connect从一个C函数调用中打开一个到 SPI 管理器的连接。如果你想要通过 SPI 执行命令，你必须调用这个函数。有一些功能性 SPI 函数可以从未连接的C函数中调用。

SPI\_connect\_ext会做同样的事情，但是有一个允许传递选项标志的参数。当前有下列选项值可用：

SPI\_OPT\_NONATOMIC

设置SPI连接为nonatomic，这表示允许事务控制调用SPI\_commit、SPI\_rollback以及SPI\_start\_transaction。否则，调用这些函数将立即导致错误。

SPI\_connect()等效于SPI\_connect\_ext(0)。

返回值

SPI\_OK\_CONNECT 成功时

SPI\_ERROR\_CONNECT 错误时

### SPI\_finish

SPI\_finish -- 将一个C函数从 SPI 管理器断开

大纲

int SPI\_finish(void)

描述

SPI\_finish关闭一个到 SPI 管理器的现有连接。你必须在完成你的C函数的当前调用中所需的 SPI 操作之后必须调用这个函数。不过，如果你通过elog(ERROR)中断了事务，你无须担心这个函数的调用。在那种情况下，SPI 将自己自动进行清理。

返回值

SPI\_OK\_FINISH 如果正确地断开连接

SPI\_ERROR\_UNCONNECTED 如果从一个未连接的C函数中调用

### SPI\_execute

SPI\_execute -- 执行一个命令

大纲

int SPI\_execute(const char \* command, bool read\_only, long count)

描述

SPI\_execute执行指定的 SQL 命令以获得count行。如果read\_only为true，该命令必须是只读的，并且执行开销也会有所降低。

只能从一个已连接的C函数中调用这个函数。

如果count为零，那么该命令会为其所适用的所有行执行。如果count大于零，那么会检索不超过count行，当到达该计数时执行会停止，这很像为查询增加一个LIMIT子句。例如：SPI\_execute("SELECT \* FROM foo", true, 5);

会从表中检索至多 5 行。注意这样一个限制只有当命令真正返回行时才有效。例如：

SPI\_execute("INSERT INTO foo SELECT \* FROM bar", false, 5);

插入所有来自于bar的行，而忽略count参数。不过，通过

SPI\_execute("INSERT INTO foo SELECT \* FROM bar RETURNING \*", false, 5);

将插入至多 5 行，因为在第五个RETURNING结果行被检索到后执行就会停止。 你可以在一个字符串中传递多个命令，SPI\_execute会返回最后一个被执行的命令的结果。

count限制单独适用于每一个命令（即便只有最后一个结果会被实际返回）。该限制 不适用于由规则产生的任何隐藏命令。

当read\_only是false时，SPI\_execute增加命令计数器并且在执行字符串中每一个命令之前计算一个新的snapshot。如果当前事务隔离级别是SERIALIZABLE或REPEATABLE READ， 该快照并不会实际改变。但是在READ COMMITTED模式中，快照更新允许每个命令看到来自其他会话中新近已提交事务的结果。当命令正在修改数据库时，这对一致性行为非常重要。

当read\_only是true时，SPI\_execute不更新快照或者命令计数器，并且它只允许纯 SELECT命令出现在命令字符串中。这些命令被使用之前为周围查询建立的快照来执行。这种执行模式要比读/写模式更快，因为消除了每个命令跟新快照的开销。 它也允许建立真正stable的函数：因为连续执行将会使用同一个快照，因此结果不会有改变。

在一个使用 SPI 的单一函数中混合只读和读写命令通常是不明智的，这样可能会导致非常令人困惑的行为，因为只读查询将看不到任何由读写查询完成的数据库更新结果。被执行的（最后一个）命令的实际行数使用全局变量SPI\_processed返回。 如果该函数的返回值是SPI\_OK\_SELECT、SPI\_OK\_INSERT\_RETURNING、 SPI\_OK\_DELETE\_RETURNING或者SPI\_OK\_UPDATE\_RETURNING，那么你可以使用全局指针SPITupleTable \*SPI\_tuptable来访问结果行。某些工具命令（例如EXPLAIN）也返回行集合，并且在这些情况中SPI\_tuptable也会包含该结果。某些工具命令（COPY、CREATE TABLE AS）不返回一个行集合，因此SPI\_tuptable为 NULL，但是它们仍然会在SPI\_processed中返回被处理的行数。

结构SPITupleTable被定义为：

typedef struct

{

MemoryContext tuptabcxt; /\* 结果表的内存上下文 \*/

uint64 alloced; /\* 已分配值的数量 \*/

uint64 free; /\* 空限值的数量 \*/

TupleDesc tupdesc; /\* 行描述符 \*/

HeapTuple \*vals; /\* 行 \*/

} SPITupleTable;

vals是一个行指针的数组（可用项的数量由SPI\_processed给出）。tupdesc是一个行描述符，你可以把它传递给 SPI 函数来处理行。tuptabcxt、 alloced和free是不准备给 SPI 调用者使用的内部域。

SPI\_finish释放在当前的C函数中已分配的所有SPITupleTable。 如果你已经用完了一个结果表，你可以通过调用SPI\_freetuptable提早释放它。

参数

const char \* command

包含要执行命令的字符串

bool read\_only

对只读执行为true

long count

要返回的最大行数，或者用0表示没有限制

返回值

如果命令的执行成功，那么将会返回下列（非负）值之一：

SPI\_OK\_SELECT

如果执行了一个SELECT（但不是SELECT INTO）

SPI\_OK\_SELINTO

如果执行了一个SELECT INTO

SPI\_OK\_INSERT

如果执行了一个INSERT

SPI\_OK\_DELETE

如果执行了一个DELETE

SPI\_OK\_UPDATE

如果执行了一个UPDATE

SPI\_OK\_INSERT\_RETURNING

如果执行了一个INSERT RETURNING

SPI\_OK\_DELETE\_RETURNING

如果执行了一个DELETE RETURNING

SPI\_OK\_UPDATE\_RETURNING

如果执行了一个UPDATE RETURNING

SPI\_OK\_UTILITY

如果执行了一个工具命令（例如CREATE TABLE）

SPI\_OK\_REWRITTEN

如果该命令被一个规则重写成了另一类命令（例如UPDATE变成了一个INSERT）发生错误时，将会返回下列负值之一：

SPI\_ERROR\_ARGUMENT

如果command为NULL或者count小于 0

SPI\_ERROR\_COPY

如果尝试COPY TO stdout或者COPY FROM stdin

SPI\_ERROR\_TRANSACTION

如果尝试了一个事务操纵命令（BEGIN、COMMIT、ROLLBACK、SAVEPOINT、 PREPARE TRANSACTION、COMMIT PREPARED、ROLLBACK PREPARED或者其他变体）

SPI\_ERROR\_OPUNKNOWN

如果命令类型位置（不应该会发生）

SPI\_ERROR\_UNCONNECTED

如果从未连接的C函数中调用

注解

所有 SPI 查询执行函数都会设置SPI\_processed和SPI\_tuptable（只是指针， 而不是结构的内容）。如果你需要在以后访问SPI\_execute或另一个查询执行函数的结果表，请将这两个全局变量保存到本地的C函数变量中。

### SPI\_exec

SPI\_exec — 执行一个读/写命令

大纲

int SPI\_exec(const char \* command, long count)

描述

SPI\_exec和 SPI\_execute相同，但后者的 read\_only参数的值总是取 false。

参数

const char \* command

包含要执行的命令的字符串

long count

要返回的最大行数，0表示没有限制

返回值

见SPI\_execute。

### SPI\_execute\_with\_args

SPI\_execute\_with\_args — 用线外参数执行一个命令

大纲

int SPI\_execute\_with\_args(const char \*command,

int nargs, Oid \*argtypes,

Datum \*values, const char \*nulls,

bool read\_only, long count)

描述

SPI\_execute\_with\_args执行一个可能包括对外部提供的参数引用的命令。命令文本用 $n引用一个参数，并且调用会为每一个这种符号指定数据类型和值。 read\_only和 count的解释与 SPI\_execute中相同。

相对于SPI\_execute，这个例程的主要优点是数据值可以被插入到命令中而无需冗长的引用/转义，并且因此减少了 SQL 注入攻击的风险。

可以通过在SPI\_prepare后面跟上 SPI\_execute\_plan达到相似的结果。但是， 使用这个函数时查询计划总是被定制成提供的指定参数值。对于一次性的查询执行，这个函数应该更好。如果同样的命令需要用很多不同的参数执行，两种方法都可能会更快，这取决于重新做规划的代价与定制计划带来的好处之间的对比。

参数

const char \* command

命令字符串

int nargs

输入参数的数量（$1、$2等等）。

Oid \* argtypes

一个长度为nargs的数组，包含参数的数据类型的OID

Datum \* values

一个长度为nargs的数组，包含实际的参数值

const char \* nulls

一个长度为nargs的数组，描述哪些参数为空值

如果nulls为NULL，那么SPI\_execute\_with\_args会假设没有参数为空值。否则，如果对应的参数值为非空， nulls 数组的每一个项都应该是' '；如果对应参数值为空， nulls数组的项应为'n'（在后面的情况中，对应的values项中的值没有关系）。注意nulls不是一个文本字符串，它只是一个数组：它不需要一个'\\0'终止符。

bool read\_only

对只读执行是true

long count

要返回的最大行数，0表示没有限制

返回值

该返回值和SPI\_execute一样。

如果成功SPI\_execute会设置 SPI\_processed和 SPI\_tuptable。

### SPI\_prepare

SPI\_prepare — 准备一个语句，但不执行它

大纲

SPIPlanPtr SPI\_prepare(const char \* command, int nargs, Oid \* argtypes)

描述

SPI\_prepare为指定的命令创建并且返回一个预备语句，但是并不执行该命令。该预备语句会在稍后使用 SPI\_execute\_plan重复执行。

当相同的或者相似的命令要被重复执行时，通常来说只执行一次解析分析是有利的，并且更有利的是重用该命令的执行计划。SPI\_prepare把一个命令字符串转换成一个预备语句，它包装了解析分析的结果。如果发现为每一次执行都生成一个定制计划没有帮助，该预备语句也提供了一个地方缓存执行计划。

一个预备命令可以被一般化为在一个普通命令中应该出现常量的地方写上参数（$1、$2等等）。参数的实际值在SPI\_execute\_plan被调用时指定。这让该预备语句可以比没有参数的形式用户与更广泛的情况。

SPI\_prepare返回的语句只能在当前的C过程调用中使用，因为SPI\_finish会释放为这样一个语句分配的内存。但是可以使用函数SPI\_keepplan 或SPI\_saveplan把该语句保存更久。

参数

const char \* command

命令字符串

int nargs

输入参数（$1、$2等等）的数量

Oid \* argtypes

一个数组指针，它指向的数组包含参数的数据类型的 OID

返回值

SPI\_prepare返回一个指向SPIPlan 的非空指针，它是一个表示一个预备语句的不透明结构。发生错误时，将会返回NULL，并且 SPI\_result将被设置为一个也被 SPI\_execute使用的错误码，不过当 command为NULL、或者nargs小于零、或者nargs大于零但是argtypes为NULL 时它会被设置为SPI\_ERROR\_ARGUMENT。

注解

如果没有定义参数，在第一次使用SPI\_execute\_plan 时将会创建一个一般的计划，并且把它用于所有的后续执行。如果有参数，SPI\_execute\_plan的前几次使用将根据提供的参数值产生定制计划。在使用同一个预备语句足够多次后， SPI\_execute\_plan将构建一个一般计划，并且如果它并不比定制计划昂贵太多， SPI\_execute\_plan将开始使用一般计划来取代每次都进行重新规划。如果这种默认的行为不合适，你可以通过传递CURSOR\_OPT\_GENERIC\_PLAN或 CURSOR\_OPT\_CUSTOM\_PLAN标志给 SPI\_prepare\_cursor，以分别强制使用一般或者定制计划。

尽管一个预备语句的要点是避免对语句的重复解析分析以及规划，只要语句中 用到的数据库对象从上一次使用该预备语句以来经历过定义性（DDL）改变，瀚高数据库将会强制重新分析和重新规划该语句。还有，如果search\_path的值从一个改变成下一个，该语句将会使用新的search\_path进行重新解析。更多有关预备语句行为的信息请见PREPARE。

这个函数只能从一个已连接的C函数调用。

SPIPlanPtr被声明为spi.h中的一种不透明结构类型的指针。尝试直接访问其内容是不明智的，因为那会让你的代码更有可能会在未来版本的瀚高数据库中崩溃。

SPIPlanPtr这个名字多少有点历史原因，因为该数据结构不再需要包含一个执行计划。

### SPI\_prepare\_cursor

SPI\_prepare\_cursor — 预备一个语句，但是不执行它

大纲

SPIPlanPtr SPI\_prepare\_cursor(const char \* command, int nargs,

Oid \* argtypes, int cursorOptions)

描述

SPI\_prepare\_cursor和 SPI\_prepare一样，不过它也允许说明规划器的 “游标选项”参数。

这是一个位掩码，它的值如 nodes/parsenodes.h中 DeclareCursorStmt的options域所示。

SPI\_prepare总是把该游标选项取做零。

参数

const char \* command

命令字符串

int nargs

输入参数（$1、$2等等）的数量

Oid \* argtypes

一个数组指针，它指向的数组包含参数的数据类型的 OID

int cursorOptions

整数形式的游标选项位掩码，零会导致默认行为

返回值

SPI\_prepare\_cursor具有和 SPI\_prepare一样的返回习惯。

注解

在cursorOptions设置的有用的位包括

CURSOR\_OPT\_SCROLL、CURSOR\_OPT\_NO\_SCROLL、CURSOR\_OPT\_FAST\_PLAN、CURSOR\_OPT\_GENERIC\_PLAN以及 CURSOR\_OPT\_CUSTOM\_PLAN。注意CURSOR\_OPT\_HOLD被特别地忽略。

### SPI\_prepare\_params

SPI\_prepare\_params — 预备一个语句，但是不执行它

大纲

SPIPlanPtr SPI\_prepare\_params(const char \* command,

ParserSetupHook parserSetup,

void \* parserSetupArg,

int cursorOptions)

描述

SPI\_prepare\_params为指定的命令创建并返回一个预备语句，但是不执行该命令。这个函数等效于SPI\_prepare\_cursor，此外调用者可以指定解析器钩子函数来控制外部参数引用的解析。

参数

const char \* command

命令字符串

ParserSetupHook parserSetup

解析器钩子设置函数

void \* parserSetupArg

用于parserSetup的转嫁参数

int cursorOptions

整数形式的游标选项位掩码，零会导致默认行为

返回值

SPI\_prepare\_params具有和SPI\_prepare相同的返回习惯。

### SPI\_getargcount

SPI\_getargcount — 返回一个由SPI\_prepare 准备好的语句所需的参数数量

大纲

int SPI\_getargcount(SPIPlanPtr plan)

描述

SPI\_getargcount返回执行一个由 SPI\_prepare准备好的语句所需的参数数量。

参数

SPIPlanPtr plan

预备语句（由SPI\_prepare返回）

返回值

plan所期望的参数计数。如果该plan为NULL或者无效， SPI\_result会被设置为SPI\_ERROR\_ARGUMENT 并且返回 -1。

### SPI\_getargtypeid

SPI\_getargtypeid — 为由SPI\_prepare 准备好的一个语句的一个参数返回其数据类型OID

大纲

Oid SPI\_getargtypeid(SPIPlanPtr plan, int argIndex)

描述

SPI\_getargtypeid返回由 SPI\_prepare准备好的一个语句的第argIndex个参数的类型的OID。第一个参数的索引为零。

参数

SPIPlanPtr plan

预备语句（由SPI\_prepare返回）

int argIndex

参数的索引，从零开始

返回值

给定索引处的参数的类型OID。如果该 plan为NULL或者无效， 或者argIndex小于零或者小于为 plan声明的参数数量，SPI\_result会被设置为 SPI\_ERROR\_ARGUMENT并且将会返回 InvalidOid。

### SPI\_is\_cursor\_plan

SPI\_is\_cursor\_plan — 如果一个由SPI\_prepare预备好的语句可以用于SPI\_cursor\_open则返回 true

大纲

bool SPI\_is\_cursor\_plan(SPIPlanPtr plan)

描述

如果一个由SPI\_prepare预备好的语句可以被作为一个参数传递给SPI\_cursor\_open， SPI\_is\_cursor\_plan会返回true。否则返回false。原则是该 plan表示一个单一命令并且这个命令向其调用者返回元组。例如，只要不含INTO子句，SELECT 就被允许，而只有包含一个RETURNING子句时才允许UPDATE。

参数

SPIPlanPtr plan

预备语句（由SPI\_prepare返回）

返回值

如果该plan能产生一个游标则返回 true，否则返回false 并且把SPI\_result设置为零。如果不可能决定答案（例如，如果plan为 NULL或无效，或者在没有连接到 SPI 时调用），那么SPI\_result会被设置为一个合适的错误码并且返回false。

### SPI\_execute\_plan

SPI\_execute\_plan — 执行一个由SPI\_prepare预备好的语句

大纲

int SPI\_execute\_plan(SPIPlanPtr plan, Datum \* values, const char \* nulls,

bool read\_only, long count)

描述

SPI\_execute\_plan执行一个由 SPI\_prepare或其同类方法准备好的语句。 read\_only和 and count的解释和 SPI\_execute中相同。

参数

SPIPlanPtr plan

预备语句（由SPI\_prepare返回）

Datum \* values

一个实际参数值的数组。必须和语句的参数数量等长。

const char \* nulls

一个描述哪些参数为空值的数组。必须和语句的参数数量等长。

如果nulls为NULL，那么SPI\_execute\_plan会假设没有参数为空值。否则，如果对应的参数值为非空， nulls 数组的每一个项都应该是' '；如果对应参数值为空， nulls数组的项应为'n'（在后面的情况中，对应的values项中的值没有关系）。注意nulls不是一个文本字符串，它只是一个数组：它不需要一个'\\0'终止符。

bool read\_only

true表示只读执行

long count

要返回的行的最大数量，或者用0表示没有限制

返回值

返回值和SPI\_execute相同，还有下列额外可能的错误（负值）结果：

SPI\_ERROR\_ARGUMENT

如果plan为NULL 或者非法，或者count小于 0

SPI\_ERROR\_PARAM

如果values为NULL但是 plan被准备时用了一些参数

成功时，就像在SPI\_execute中会设置 SPI\_processed和 SPI\_tuptable。

### SPI\_execute\_plan\_with\_paramlist

SPI\_execute\_plan\_with\_paramlist — 执行一个由SPI\_prepare预备好的语句

大纲

int SPI\_execute\_plan\_with\_paramlist(SPIPlanPtr plan,

ParamListInfo params,

bool read\_only,

long count)

描述

SPI\_execute\_plan\_with\_paramlist执行一个由 SPI\_prepare准备好的语句。这个函数与 SPI\_execute\_plan等效，不过被传递给该查询的参数值的信息以不同的方式呈现。ParamListInfo表现形 式更方便于把这种格式的值向下传递。它也支持通过 ParamListInfo中指定的钩子函数动态设置参数。

参数

SPIPlanPtr plan

预备语句（由SPI\_prepare返回）

ParamListInfo params

包含参数类型和值的数据结构，如果没有则为 NULL

bool read\_only

true表示只读执行

long count

要返回的行的最大数量，或者用0表示没有限制

返回值

返回值和SPI\_execute\_plan相同。

成功时，在SPI\_execute\_plan中会设置 SPI\_processed和 SPI\_tuptable。

### SPI\_execp

SPI\_execp — 以读/写模式执行一个语句

大纲

int SPI\_execp(SPIPlanPtr plan, Datum \* values, const char \* nulls, long count)

描述

SPI\_execp与 SPI\_execute\_plan相同，不过后者的 read\_only参数总是取false。

参数

SPIPlanPtr plan

预备语句（由SPI\_prepare返回）

Datum \* values

实际参数值的数组。长度必须等于该语句的参数数量。

const char \* nulls

描述哪些参数为空值的数据。长度必须等于该语句的参数数量。

如果nulls为NULL，那么SPI\_execp会假设没有参数为空值。否则，如果对应的参数值为非空， nulls 数组的每一个项都应该是' '；如果对应参数值为空， nulls数组的项应为'n'（在后面的情况中，对应的values项中的值没有关系）。注意nulls不是一个文本字符串，它只是一个数组：它不需要一个'\\0'终止符。

long count

要返回的行的最大数量，或者用0表示没有限制

返回值

见SPI\_execute\_plan。

成功时，就像在SPI\_execute中会设置 SPI\_processed和 SPI\_tuptable。

### SPI\_cursor\_open

SPI\_cursor\_open — 使用由SPI\_prepare创建的 语句建立一个游标

大纲

Portal SPI\_cursor\_open(const char \* name, SPIPlanPtr plan,

Datum \* values, const char \* nulls,

bool read\_only)

描述

SPI\_cursor\_open建立一个游标（在内部是一个 portal），该游标将执行由SPI\_prepare准备好的一个语句。参数具有和SPI\_execute\_plan的相应参数相同的含义。

使用一个游标而不是直接执行该语句有两个好处。首先，可以一次只取出一些结果行，避免为返回很多行的查询过度使用内存。其次，一个 portal 可以比当前的C函数生存更长时间（事实上，它可以生存到当前事务结束）。把 portal 的名称返回给该C函数的调用者提供了一种将一个行集合返回为结果的方法。

被传入的参数数据将被复制到游标的 portal 中，因此在该游标仍然存在时可以释放掉被传入的参数数据。

参数

const char \* name

portal 的名字，或者设置成NULL 让系统选择一个名称

SPIPlanPtr plan

预备语句（由SPI\_prepare返回）

Datum \* values

实际参数值的数组。长度必须等于该语句的参数数量。

const char \* nulls

描述哪些参数是空值的数据。长度必须等于该语句的参数数量。

如果nulls为NULL，那么SPI\_cursor\_open会假设没有参数为空值。否则，如果对应的参数值为非空， nulls 数组的每一个项都应该是' '；如果对应参数值为空， nulls数组的项应为'n'（在后面的情况中，对应的values项中的值没有关系）。注意nulls不是一个文本字符串，它只是一个数组：它不需要一个'\\0'终止符。

bool read\_only

true表示只读执行

返回值

指向包含该游标的 portal 的指针。注意这里没有错误返回约定，任何错误都将通过elog报告。

### SPI\_cursor\_open\_with\_args

SPI\_cursor\_open\_with\_args — 使用一个查询和参数建立一个游标

大纲

Portal SPI\_cursor\_open\_with\_args(const char \*name,

const char \*command,

int nargs, Oid \*argtypes,

Datum \*values, const char \*nulls,

bool read\_only, int cursorOptions)

描述

SPI\_cursor\_open\_with\_args建立一个将 执行指定查询的游标（在内部是一个 portal）。大部分参数具有和 SPI\_prepare\_cursor 和SPI\_cursor\_open中相应参数相同的含义。

对于一次性的查询执行，这个函数应该比 SPI\_prepare\_cursor加上其后的 SPI\_cursor\_open更好。如果相同的命令要被用很多不同的参数执行，哪种方法更快就要取决于重做计划的代价与定制计划带来的好处之间谁更有利。被传入的参数数据将被复制到游标的 portal 中，因此在该游标仍然存在时可以释放掉被传入的参数数据。

参数

const char \* name

portal 的名字，或者设置成NULL 让系统选择一个名称

const char \* command

命令字符串

int nargs

输入参数的数量（$1、$2等等）

Oid \* argtypes

一个长度为nargs的数组，它包含参数的 数据类型的OID

Datum \* values

一个长度为nargs的数组，它包含实际的参数值

const char \* nulls

一个长度为nargs的数组，它描述哪些参数为空值

如果nulls为NULL， 那么SPI\_cursor\_open\_with\_args会假设没有参数为空值。否则，如果对应的参数值为非空， nulls 数组的每一个项都应该是' '；如果对应参数值为空， nulls数组的项应为'n'（在后 面的情况中，对应的values项中的值没有 关系）。

注意nulls不是一个文本字符串，它只是一个数组：它不需要一个'\\0'终止符。

bool read\_only

true表示只读执行

int cursorOptions

游标选项的整数型位掩码，为零会产生默认行为

返回值

指向包含该游标的 portal 的指针。注意这里没有错误返回约定，任何错误都将通过elog报告。

### SPI\_cursor\_open\_with\_paramlist

SPI\_cursor\_open\_with\_paramlist — 使用参数建立一个游标

大纲

Portal SPI\_cursor\_open\_with\_paramlist(const char \*name,

SPIPlanPtr plan,

ParamListInfo params,

bool read\_only)

描述

SPI\_cursor\_open\_with\_paramlist建立一个游标（在内部是一个portal），它将执行一个由 SPI\_prepare准备好的语句。这个函数等效于SPI\_cursor\_open，不过被传递给该查询的参数值的信息以不同的方式呈现。ParamListInfo表现形式更方便于把这种格式的值向下传递。它也支持通过 ParamListInfo中指定的钩子函数动态设置参数。

被传入的参数数据将被复制到游标的 portal 中，因此在该游标仍然存在时可以释放掉被传入的参数数据。

参数

const char \* name

portal 的名字，或者设置成NULL 让系统选择一个名称

SPIPlanPtr plan

预备语句（由SPI\_prepare返回）

ParamListInfo params

包含参数类型和值的数据结构，如果没有就为 NULL

bool read\_only

true表示只读执行

返回值

指向包含该游标的 portal 的指针。注意这里没有错误返回约定，任何错误都将通过elog报告。

### SPI\_cursor\_find

SPI\_cursor\_find — 用名称查找一个现有的游标

大纲

Portal SPI\_cursor\_find(const char \* name)

描述

SPI\_cursor\_find用名称查找一个现有的 portal。 这主要被用于解析由其他某个函数返回的一个游标名称。

参数

const char \* name

该 portal 的名称

返回值

带有指定名称的 portal 的指针，如果没有找到就是 NULL。

### SPI\_cursor\_fetch

SPI\_cursor\_fetch — 从一个游标取出一些行

大纲

void SPI\_cursor\_fetch(Portal portal, bool forward, long count)

描述

SPI\_cursor\_fetch从一个游标取得一些行。 这等效于 SQL 命令FETCH的一个子集（更多功能见SPI\_scroll\_cursor\_fetch）。

参数

Portal portal

包含该游标的 portal

bool forward

为真表示向前获取，为假表示向后获取

long count

要取得的最大行数

返回值

成功时，就像在SPI\_execute中会设置 SPI\_processed和 SPI\_tuptable。

注解

如果该游标的计划不是用CURSOR\_OPT\_SCROLL选项创建的，向后获取会失败。

### SPI\_cursor\_move

SPI\_cursor\_move — 移动一个游标

大纲

void SPI\_cursor\_move(Portal portal, bool forward, long count)

描述

SPI\_cursor\_move跳过一个游标中的一些行。 这等效于 SQL 命令MOVE的一个子集（更多的功能 请见SPI\_scroll\_cursor\_move）。

参数

Portal portal

包含该游标的 portal

bool forward

为真表示前移，为假表示后移

long count

要移动的最大行数

注解

如果该游标的计划不是用CURSOR\_OPT\_SCROLL 选项创建的，向后移动会失败。

### SPI\_scroll\_cursor\_fetch

SPI\_scroll\_cursor\_fetch — 从一个游标取出一些行

大纲

void SPI\_scroll\_cursor\_fetch(Portal portal, FetchDirection direction,

long count)

描述

SPI\_scroll\_cursor\_fetch从一个游标中取出一些行。 这等效于 SQL 命令FETCH。

参数

Portal portal

包含该游标的 portal

FetchDirection direction

FETCH\_FORWARD、FETCH\_BACKWARD、FETCH\_ABSOLUTE或者 FETCH\_RELATIVE之一

long count

FETCH\_FORWARD或 FETCH\_BACKWARD方式中要取出的行数； FETCH\_ABSOLUTE方式中要取出的绝对行号； FETCH\_RELATIVE方式中要取出的相对行号

返回值

成功时，就像在SPI\_execute中会设置 SPI\_processed和 SPI\_tuptable。

注解

参数direction和 count的详细解释请见 SQL FETCH命令。

如果该游标的计划不是用CURSOR\_OPT\_SCROLL 选项创建的，除FETCH\_FORWARD之外的方向值会失败。

### SPI\_scroll\_cursor\_move

SPI\_scroll\_cursor\_move — 移动一个游标

大纲

void SPI\_scroll\_cursor\_move(Portal portal, FetchDirection direction,

long count)

描述

SPI\_scroll\_cursor\_move在一个游标中跳过 一定数量的行。这等效于 SQL 命令MOVE。

参数

Portal portal

包含该游标的 portal

FetchDirection direction

FETCH\_FORWARD、 FETCH\_BACKWARD、 FETCH\_ABSOLUTE或者 FETCH\_RELATIVE之一

long count

FETCH\_FORWARD或者 FETCH\_BACKWARD方式中要移动的行数； FETCH\_ABSOLUTE方式中要移动到的绝对行号； FETCH\_RELATIVE方式中要移动到的相对行号

返回值

成功时，就像在SPI\_execute中会设置 SPI\_processed。 SPI\_tuptable被设置为NULL， 因为这个函数不需要返回行。

注解

参数direction和 count的详细解释请见 SQL FETCH命令。

如果该游标的计划不是用CURSOR\_OPT\_SCROLL 选项创建的，除FETCH\_FORWARD之外的方向值会失败。

### SPI\_cursor\_close

SPI\_cursor\_close — 关闭一个游标

大纲

void SPI\_cursor\_close(Portal portal)

描述

SPI\_cursor\_close关闭一个之前创建的游标并且释放它的 portal 存储。所有打开的游标会在事务结束时自动被关闭。只有在希望尽快释放资源时，才需要调用SPI\_cursor\_close。

参数

Portal portal

包含该游标的 portal

### SPI\_keepplan

SPI\_keepplan — 保存一个预备语句

大纲

int SPI\_keepplan(SPIPlanPtr plan)

描述

SPI\_keepplan保存一个被传入的语句（由 SPI\_prepare准备好），这样它将不会被 SPI\_finish或者事务管理器释放。这让你能够在当前会话的后续C函数调用中重用预备语句。

参数

SPIPlanPtr plan

要保存的预备语句

返回值

成功返回 0；如果plan为NULL 或者无效则返回SPI\_ERROR\_ARGUMENT

注解

这个函数通过指针调整的方法（不需要数据复制）将被传入的语句重定位到永久存储中。如果你后来需要删除它，可以对它使用 SPI\_freeplan。

### SPI\_saveplan

SPI\_saveplan — 保存一个预备语句

大纲

SPIPlanPtr SPI\_saveplan(SPIPlanPtr plan)

描述

SPI\_saveplan把一个被传入的语句（由 SPI\_prepare准备好）复制到不会被 SPI\_finish或者事务管理器释放的内存中。这让你能够在当前会话的后续C函数调用中重用预备语句。

参数

SPIPlanPtr plan

要保存的预备语句

返回值

要被复制的语句的指针；如果没有成功则返回NULL。错误时，SPI\_result会被这样设置：

SPI\_ERROR\_ARGUMENT

如果plan为NULL或无效

SPI\_ERROR\_UNCONNECTED

如果从一个未连接的C函数调用

注解

原始的被传入的语句不会被释放，因此你可能希望在其上执行SPI\_freeplan以避免在 SPI\_finish之前发生内存泄露。

在大部分情况下，SPI\_keepplan更适合于执行这种功能，因为它极大程度上达到了同样的结果而无需物理地复制该预备语句的数据结构。

### SPI\_register\_relation

SPI\_register\_relation — make an ephemeral named relation available by name in SPI queries

大纲

int SPI\_register\_relation(EphemeralNamedRelation enr)

简介

SPI\_register\_relation用相关信息建立一个短暂的命名关系，它对通过当前SPI连接规划和执行的查询可用。

参数

EphemeralNamedRelation enr

短暂的命名关系的注册项

返回值

如果该命令的执行成功，则将返回下列（非负）值：

SPI\_OK\_REL\_REGISTER

如果该关系已经成功地用名称注册

在出错时，会返回下列负值之一：

SPI\_ERROR\_ARGUMENT

如果enr是NULL或者其name字段是NULL

SPI\_ERROR\_UNCONNECTED

如果从一个未连接的C函数中调用

SPI\_ERROR\_REL\_DUPLICATE

如果enr的name字段中指定的名称已经为这个连接注册

### SPI\_unregister\_relation

SPI\_unregister\_relation — remove an ephemeral named relation from the registry

大纲

int SPI\_unregister\_relation(const char \* name)

简介

SPI\_unregister\_relation从当前连接的注册项中移除一个短暂存在的关系。

参数

const char \* name

关系的注册项名称

返回值

如果该命令的执行成功，则会返回下列（非负）值：

SPI\_OK\_REL\_UNREGISTER

如果tuplestore已经被成功地从注册项中移除

出现错误时，会返回下列负值之一：

SPI\_ERROR\_ARGUMENT

如果name为NULL

SPI\_ERROR\_UNCONNECTED

如果从一个未连接的C函数中调用

SPI\_ERROR\_REL\_NOT\_FOUND

如果没有在当前连接的注册项中找到name

### SPI\_register\_trigger\_data

SPI\_register\_trigger\_data — make ephemeral trigger data available in SPI queries

大纲

int SPI\_register\_trigger\_data(TriggerData \*tdata)

简介

SPI\_register\_trigger\_data会造出被触发器捕获的任何短暂存在的关系，它们对通过当前 SPI连接规划和执行的查询可用。当前，这表示用REFERENCING OLD/NEW TABLE AS... 子句定义的被AFTER触发器捕获的传递表。这个函数应该被一个PL触发器的处理器函数在连接之后调用。

参数

TriggerData \*tdata

以fcinfo->context传递给触发器处理器函数的TriggerData对象

返回值

如果命令的执行成功，则会返回下列（非负）值：

SPI\_OK\_TD\_REGISTER

如果被捕获的触发器数据（如果有）已经被成功地注册

出现错误时，会返回下列负值之一：

SPI\_ERROR\_ARGUMENT

如果tdata为NULL

SPI\_ERROR\_UNCONNECTED

如果从一个未连接的C函数中调用

SPI\_ERROR\_REL\_DUPLICATE

如果任何触发器数据瞬时关系的名字已经为这个连接注册过

## 接口支持函数

这里描述的函数提供了一个接口从SPI\_execute 及其他 SPI 函数返回的结果集中抽取信息。

这一小节中描述的所有函数都可以被用在已连接和未连接的C函数中。

### SPI\_fname

SPI\_fname — 为指定的列号确定列名

大纲

char \* SPI\_fname(TupleDesc rowdesc, int colnumber)

描述

SPI\_fname返回一个指定列的列名的拷贝（当你不再需要该列名拷贝后，可以使用pfree 释放它）。

参数

TupleDesc rowdesc

输入行描述

int colnumber

列号（从 1 开始计）

返回值

列名；如果colnumber超出范围则返回NULL。出错时SPI\_result会被设置成 SPI\_ERROR\_NOATTRIBUTE。

### SPI\_fnumber

SPI\_fnumber — 为一个指定的列名确定列号

大纲

int SPI\_fnumber(TupleDesc rowdesc, const char \* colname)

描述

SPI\_fnumber返回指定列名的列号。

如果colname引用的是一个系统列（例如， ctid），那么将返回对应的负值列号。调用者应该小心地测试返回值是不是正好为SPI\_ERROR\_NOATTRIBUTE 来检测错误；除非系统列应该被拒绝，测试结果是否小于或者等于零这种方式是不正确的。

参数

TupleDesc rowdesc

输入行描述

const char \* colname

列名

返回值

列号（用户定义的列从1开始计），如果没有找到所提到的列名则返回 SPI\_ERROR\_NOATTRIBUTE。

### SPI\_getvalue

SPI\_getvalue — 返回指定列的字符串值

大纲

char \* SPI\_getvalue(HeapTuple row, TupleDesc rowdesc, int colnumber)

描述

SPI\_getvalue返回指定列的值的字符串表示。

结果在使用palloc分配的内存中返回（当你不再需要该结果时，你可以使用pfree释放该内存）。

参数

HeapTuple row

要检查的输入行

TupleDesc rowdesc

输入行描述

int colnumber

列号（从 1 开始计）

返回值

列值，如果列为空值、colnumber超出范围（SPI\_result被设置为 SPI\_ERROR\_NOATTRIBUTE）或者没有输出函数可用（SPI\_result被设置为 SPI\_ERROR\_NOOUTFUNC）则返回 NULL。

### SPI\_getbinval

SPI\_getbinval — 返回指定列的二进制值

大纲

Datum SPI\_getbinval(HeapTuple row, TupleDesc rowdesc, int colnumber,

bool \* isnull)

描述

SPI\_getbinval以内部格式（以Datum类型）返回指定列的值。

这个函数不会为该 datum 分配新空间。在传引用数据类型的情况下，返回值将是一个被传递行的指针。

参数

HeapTuple row

要检查的输入行

TupleDesc rowdesc

输入行描述

int colnumber

列号（从 1 开始计）

bool \* isnull

列中是否为空值的标志

返回值

该列的二进制值会被返回。如果该列为空值，由isnull 指向的变量将被设置为真，否则会被设置为假。

错误时SPI\_result会被设置成 SPI\_ERROR\_NOATTRIBUTE。

### SPI\_gettype

SPI\_gettype — 返回指定列的数据类型名称

大纲

char \* SPI\_gettype(TupleDesc rowdesc, int colnumber)

描述

SPI\_gettype返回该指定列的数据类型名称的拷贝（当你不再需要该拷贝后，可以使用pfree 释放它）。

参数

TupleDesc rowdesc

输入行描述

int colnumber

列号（从 1 开始计）

返回值

指定列的数据类型名称，或者在错误时返回NULL。错误时SPI\_result会被设置成SPI\_ERROR\_NOATTRIBUTE。

### SPI\_gettypeid

SPI\_gettypeid — 返回指定列的数据类型的OID

大纲

Oid SPI\_gettypeid(TupleDesc rowdesc, int colnumber)

描述

SPI\_gettypeid返回该指定列的数据类型的 OID。

参数

TupleDesc rowdesc

输入行描述

int colnumber

列号（从 1 开始计）

返回值

指定列的数据类型的OID，或者出错时返回 InvalidOid。出错时， SPI\_result会被设置成SPI\_ERROR\_NOATTRIBUTE。

### SPI\_getrelname

SPI\_getrelname — 返回指定关系的名称

大纲

char \* SPI\_getrelname(Relation rel)

描述

SPI\_getrelname返回该指定关系的名称的拷贝（当你不再需要该拷贝后，可以使用pfree 释放它）。

参数

Relation rel

输入关系

返回值

指定关系的名称。

### SPI\_getnspname

SPI\_getnspname — 返回指定关系的名字空间

大纲

char \* SPI\_getnspname(Relation rel)

描述

SPI\_getnspname返回指定关系所属的名字空间的名称拷贝。这等效于该关系的模式。当你用完这个函数的返回值后，应该调用 pfree释放它。

参数

Relation rel

输入关系

返回值

指定关系的名字空间的名称。

### SPI\_result\_code\_string

SPI\_result\_code\_string — return error code as string

大纲

const char \* SPI\_result\_code\_string(int code);

简介

SPI\_result\_code\_string返回之前各种SPI函数返回的或者存储在SPI\_result中的结果代码的字符串表示。

参数

int code

结果代码

返回值

结果代码的字符串表示。

## 内存管理

瀚高数据库在内存上下文中分配内存，内存上下文为管理在多个不同位置、具有不同生存时间需要的分配提供了一种便捷的方法。销毁一个上下文会释放所有在其中分配的内存。因此不必跟踪单个对象来避免内存泄露，而是只需要管理数量相对较少的上下文即可。palloc和相关的函数可以从”当前”上下文中分配内存。

SPI\_connect创建一个新的内存上下文并且让它成为当前上下文。SPI\_finish恢复之前的当前上下文并且销毁由SPI\_connect创建的内存上下文。这些动作确保在你的C函数中分配的内存在C函数退出时被回收，从而避免内存泄露。

不过，如果你的C函数需要返回一个在已分配内存中的对象（例如一个传引用数据类型的值），你不能使用palloc 分配内存，或者说至少不能在连接到 SPI 时这样做。如果你试着这样做，该对象会被SPI\_finish接触分配，那么你的C函数将无法可靠地工作。要解决这个问题，应使用SPI\_palloc来为要返回的对象分配内存。

SPI\_palloc会在 “上层执行器上下文”中分配内存，也就是当 SPI\_connect被调用时的当前内存上下文，它才是从你的C函数中返回的值最适合的上下文。这一节中描述的几个其他实用函数也会返回在上层执行器上下文中创建的对象。

当SPI\_connect被调用时，这个C函数的私有上下文（由SPI\_connect）会被作为当前上下文。所有用palloc、repalloc或者 SPI 功能函数（除了这个小节中描述的例外）分配的内存都在这个上下文中。 当一个C函数从SPI管理器断开连接时（通过 SPI\_finish），当前上下文被恢复到上层的执行器上下文，并且在该过程的内存上下文中分配的内存都会被释放，之后再不能被使用。

### SPI\_palloc

SPI\_palloc — 在上层执行器上下文中分配内存

大纲

void \* SPI\_palloc(Size size)

描述

SPI\_palloc在上层的执行器上下文中分配内存。

这个函数只能在连接到SPI时使用。否则，它会报出错误。

参数

Size size

要分配的存储空间大小（以字节计）

返回值

指向具有指定大小的新存储空间的指针

### SPI\_repalloc

SPI\_repalloc — 在上层执行器上下文中重分配内存

大纲

void \* SPI\_repalloc(void \* pointer, Size size)

描述

SPI\_repalloc改变之前用SPI\_palloc 分配的内存段的大小。

这个函数不再和普通的repalloc相区别。保留它只是为了对现有代码保持向后兼容。

参数

void \* pointer

指向要改变的现有存储空间的指针

Size size

要分配的存储空间大小（以字节计）

返回值

指向具有指定大小的新存储空间的指针，现有区域的内容会被复制到其中

### SPI\_pfree

SPI\_pfree — 在上层执行器上下文中释放内存

大纲

void SPI\_pfree(void \* pointer)

描述

SPI\_pfree释放之前使用 SPI\_palloc或者 SPI\_repalloc分配的内存。

这个函数不再和普通的pfree相区别。保留它只是为了对现有代码保持向后兼容。

参数

void \* pointer 指向要释放的现有存储空间的指针

### SPI\_copytuple

SPI\_copytuple — 在上层执行器上下文中创建一行的拷贝

大纲

HeapTuple SPI\_copytuple(HeapTuple row)

描述

SPI\_copytuple在上层执行器上下文中为一行创建一份拷贝。这通常被用来从一个触发器中返回一个被修改的行。在一个被声明为返回组合类型的函数中，应使用 SPI\_returntuple。

这个函数只能在连接到SPI时使用。否则，它会返回NULL并且把SPI\_result设置为SPI\_ERROR\_UNCONNECTED。

参数

HeapTuple row

要拷贝的行

返回值

被拷贝的行，或者在出错时返回NULL（错误的内容请参考SPI\_result）

### SPI\_returntuple

SPI\_returntuple — 准备把一个元组返回为一个 Datum

大纲

HeapTupleHeader SPI\_returntuple(HeapTuple row, TupleDesc rowdesc)

描述

SPI\_returntuple为一个行在上层执行器上下文中创建一个拷贝，把它以一种行类型Datum的形式返回。被返回的指针只需要在返回前通过PointerGetDatum 被转换成Datum。

这个函数只能在连接到SPI时使用。否则，它会返回NULL并且把SPI\_result设置为SPI\_ERROR\_UNCONNECTED。

注意这应该被用于声明为要返回组合类型的函数。它不能用于触发器，在触发器中应使用SPI\_copytuple来返回一个被修改的行。

参数

HeapTuple row

要被拷贝的行

TupleDesc rowdesc

行的描述符（对大部分有效的缓存，每次都传递相同的描述符）

返回值

指向被拷贝行的HeapTupleHeader，或者在出错时返回NULL（错误的内容请参考SPI\_result）

### SPI\_modifytuple

SPI\_modifytuple — 通过替换一个给定行的选定域来创建一行

大纲

HeapTuple SPI\_modifytuple(Relation rel,

HeapTuple row,

int ncols,

int \* colnum,

Datum \* values,

const char \* nulls)

描述

SPI\_modifytuple创建一个新行，其中选定的列用新值替代，其他列则从输入行中拷贝。输入行本身不被修改。新行被返回在上层的执行器上下文中。

这个函数只能在连接到SPI时使用。否则，它会返回NULL并且把SPI\_result设置为SPI\_ERROR\_UNCONNECTED。

参数

Relation rel

只被用作该行的行描述符的来源（传递一个关系而不是一个行描述符是一种令人头痛的设计）。

HeapTuple row

要被修改的行

int ncols

要被修改的列数

int \* colnum

一个长度为ncols的数组，包含了要被修改的列号（列号从 1 开始）

Datum \* values

一个长度为ncols的数组，包含了指定列的新值

const char \* nulls

一个长度为ncols的数组，描述哪些新值为空值

如果nulls为NULL，那么SPI\_modifytuple假定没有新值为空值。否则，如果对应的新值为非空，nulls数组的每一项都应该是' '，而如果对应的新值为空值则为'n'（在后一种情况中，对应的values项中的新值无关紧要）。注意nulls不是一个文本字符串，只是一个数组：它不需要一个'\\0'终止符。

返回值

修改过的新行，它被分配在上层的执行器上下文中，或者在出错时返回NULL（错误的内容请参考SPI\_result）

出错时，SPI\_result被设置如下：

SPI\_ERROR\_ARGUMENT

如果rel为NULL，或者 row为NULL，或者ncols 小于等于 0，或者colnum为NULL，或者values为NULL。

SPI\_ERROR\_NOATTRIBUTE

如果colnum包含一个无效的列号（小于等于 0 或者大于 row中的列数）。

SPI\_ERROR\_UNCONNECTED

如果SPI不是活跃状态

### SPI\_freetuple

SPI\_freetuple — 释放一个在上层执行器上下文中分配的行

大纲

void SPI\_freetuple(HeapTuple row)

描述

SPI\_freetuple释放之前在上层执行器上下文中分配的一个行。

这个函数不再和普通的heap\_freetuple相区别。保留它只是为了对现有代码保持向后兼容。

参数

HeapTuple row

要释放的行

### SPI\_freetuptable

SPI\_freetuptable — 释放一个由SPI\_execute 或者类似函数创建的行集合

大纲

void SPI\_freetuptable(SPITupleTable \* tuptable)

描述

SPI\_freetuptable释放一个由之前的 SPI 命令执行函数（例如SPI\_execute）创建的行集合。因此，调用这个函数时，常常使用SPI\_tuptable作为参数。

如果一个使用SPI的C函数需要执行多个命令并且不想保留早期命令的结果，这个函数就有用了。注意，SPI\_finish会释放任何还未释放的行集合。还有，如果在一个使用SPI的C函数的执行中开始了一个子事务并且后来被中止，SPI 会自动释放该子事务运行期间创建的任何行集合。

SPI\_freetuptable包含了保护逻辑以避免对于同一行集的重复删除请求。在以前的发布中，重复的删除将会导致崩溃。

参数

SPITupleTable \* tuptable

要释放的行集的指针，NULL 表示什么也不做

### SPI\_freeplan

SPI\_freeplan — 释放一个之前保存的预备语句

大纲

int SPI\_freeplan(SPIPlanPtr plan)

描述

SPI\_freeplan释放一个之前由 SPI\_prepare返回的或者由 SPI\_keepplan、SPI\_saveplan 保存的预备语句。

参数

SPIPlanPtr plan

要释放的语句的指针

返回值

成功返回 0；

如果plan为 NULL或无效则返回 SPI\_ERROR\_ARGUMENT

## 事务管理

不能通过SPI\_execute这样的SPI函数运行COMMIT和ROLLBACK之类的事务控制命令。不过，也有单独的接口函数允许通过SPI进行事务控制。

如果不考虑被调用的上下文，在任意的用户定义的可从SQL调用的函数中开始以及结束事务通常并不是安全和明智的。例如，一个事务位于一个函数内，而该函数是某个SQL命令中的一个复杂SQL表达式的一部分，这样的事务有可能会导致隐蔽的内部错误或者崩溃。这里介绍的接口函数的主要目的是被过程语言的实现用于支持在CALL命令调用的SQL层过程中进行事务管理，同时把CALL调用的上下文也加以考虑。用C实现的使用SPI的过程可以实现同样的逻辑，但是其细节超出了这份文档的范围。

### SPI\_commit

SPI\_commit, SPI\_commit\_and\_chain — commit the current transaction

大纲

void SPI\_commit(void)

void SPI\_commit\_and\_chain(void)

简介

SPI\_commit提交当前事务。它近似等效于运行SQL命令COMMIT。在一个事务被提交后，在进一步的数据库动作被执行前必须使用SPI\_start\_transaction开始一个新的事务。

SPI\_commit\_and\_chain是相同的，事务特征与刚刚完成的事务相同的新事务会立即启动，类似 SQL 命令 COMMIT AND CHAIN。

只有当SPI连接已经在对SPI\_connect\_ext的调用中被设置为非原子的情况下才能执行这些函数。

### SPI\_rollback

SPI\_rollback, SPI\_rollback\_and\_chain — abort the current transaction

大纲

void SPI\_rollback(void)

void SPI\_rollback\_and\_chain(void)

简介

SPI\_rollback回滚当前事务。它近似等效于运行SQL命令ROLLBACK。在一个事务被回滚后，在进一步的数据库动作被执行前必须使用SPI\_start\_transaction开始一个新的事务。

SPI\_rollback\_and\_chain是相同的，事务特征与刚刚完成的事务相同的新事务会立即启动，类似 SQL 命令 ROLLBACK AND CHAIN。

只有当SPI连接已经在对SPI\_connect\_ext的调用中被设置为非原子的情况下才能执行这些函数。

### SPI\_start\_transaction

SPI\_start\_transaction — start a new transaction

大纲

void SPI\_start\_transaction(void)

简介

SPI\_start\_transaction开始一个新事务。它只能在SPI\_commit或SPI\_rollback之后被调用，因为在那时没有事务在活动。通常，当一个使用SPI的过程被调用时，会有一个事务已处于活跃状态，因此在关闭当前事务之前尝试启动另一个事务将会导致错误。

只有当SPI连接已经在对SPI\_connect\_ext的调用中被设置为非原子的情况下才能执行这个函数。

## 数据改变的可见性

下列规则主导了使用 SPI 的函数（或者任何其他 C 函数）中数据改变的可见性：

• 在一个 SQL 命令的执行期间，该命令所作的任何数据更改对该命令本身是不可见的。例如，在 INSERT INTO a SELECT \* FROM a;中，被插入的行对SELECT部分不可见。

• 一个命令C所作的更改对所有在C之后开始的命令可见，不管它们是否在 C之中（在C的执行期间）开始还是在C完成之后开始。

• 在一个 SQL 命令（或者一个普通函数或者触发器）调用的函数内通过 SPI 执行的命令遵循以上哪条规则取决于传递给 SPI 的读/写标志。以只读模式执行的命令遵循第一条规则：它们不能看到调用它们的命令的改变。在读写模式中执行的命令遵循第二条规则：它们能看见目前为止所有的改变。

• 所有的标准过程语言会基于函数的易变性属性设置 SPI 读写模式。 STABLE和IMMUTABLE函数的命令会以只读模式完成，而VOLATILE函数的命令会以读写模式完成。虽然 C 函数的作者可以违反这种习惯，但是最好不要那样做。

下一节包含一个关于这些规则应用的例子：

## 例子

这一节包含了 SPI 用法的一个非常简单的例子。C函数 execq用一个 SQL 命令作为其第一个参数并且用一个行计数作为第二个参数，使用 SPI\_exec执行该命令并且返回被该命令处理过的行的数量。你可以在源代码树的 src/test/regress/regress.c和 spi模块中找到 SPI的更复杂的例子。

#include "postgres.h"

#include "executor/spi.h"

#include "utils/builtins.h"

PG\_MODULE\_MAGIC;

PG\_FUNCTION\_INFO\_V1(execq);

Datum

execq(PG\_FUNCTION\_ARGS)

{

char \*command;

int cnt;

int ret;

uint64 proc;

/\* 把给定的文本对象转换成一个 C 字符串 \*/

command = text\_to\_cstring(PG\_GETARG\_TEXT\_PP(0));

cnt = PG\_GETARG\_INT32(1);

SPI\_connect();

ret = SPI\_exec(command, cnt);

proc = SPI\_processed;

/\*

\* 如果取出了一些行，通过 elog(INFO) 打印它们。

\*/

if (ret > 0 && SPI\_tuptable!= NULL)

{

TupleDesc tupdesc = SPI\_tuptable->tupdesc;

SPITupleTable \*tuptable = SPI\_tuptable;

char buf\[8192\];

uint64 j;

for (j = 0; j < proc; j++)

{

HeapTuple tuple = tuptable->vals\[j\];

int i;

for (i = 1, buf\[0\] = 0; i <= tupdesc->natts; i++)

snprintf(buf + strlen(buf), sizeof(buf) - strlen(buf), " %s%s",

SPI\_getvalue(tuple, tupdesc, i),

(i == tupdesc->natts)? " ": " |");

elog(INFO, "EXECQ: %s", buf);

}

}

SPI\_finish();

pfree(command);

PG\_RETURN\_INT64(proc);

}

在把该函数编译到一个共享库中之后，这样声明该函数：

CREATE FUNCTION execq(text, integer) RETURNS int8

AS 'filename'

LANGUAGE C STRICT;

下面是一个会话实例：

\=> SELECT execq('CREATE TABLE a (x integer)', 0);

execq

\-------

0

(1 row)

\=> INSERT INTO a VALUES (execq('INSERT INTO a VALUES (0)', 0));

INSERT 0 1

\=> SELECT execq('SELECT \* FROM a', 0);

INFO: EXECQ: 0 -- inserted by execq

INFO: EXECQ: 1 -- returned by execq and inserted by upper INSERT

execq

\-------

2

(1 row)

\=> SELECT execq('INSERT INTO a SELECT x + 2 FROM a', 1);

execq

\-------

1

(1 row)

\=> SELECT execq('SELECT \* FROM a', 10);

INFO: EXECQ: 0

INFO: EXECQ: 1

INFO: EXECQ: 2 -- 0 + 2，按照所指定的，只有一行被插入

execq

\-------

3 -- 10 只是最大值，3 是实际的行数

(1 row)

\=> DELETE FROM a;

DELETE 3

\=> INSERT INTO a VALUES (execq('SELECT \* FROM a', 0) + 1);

INSERT 0 1

\=> SELECT \* FROM a;

x

\---

1 -- 没有行在 a (0) + 1

(1 row)

\=> INSERT INTO a VALUES (execq('SELECT \* FROM a', 0) + 1);

INFO: EXECQ: 1

INSERT 0 1

\=> SELECT \* FROM a;

x

\---

1

2 -- 有一行在 in a + 1

(2 rows)

\-- 这证明了数据改变可见性规则：

\=> INSERT INTO a SELECT execq('SELECT \* FROM a', 0) \* x FROM a;

INFO: EXECQ: 1

INFO: EXECQ: 2

INFO: EXECQ: 1

INFO: EXECQ: 2

INFO: EXECQ: 2

INSERT 0 2

\=> SELECT \* FROM a;

x

\---

1

2

2 -- 2 行 \* 1 （第一行中的 x）

6 -- 3 rows (2 + 1 被插入) \* 2 （第二行中的 x）

(4 rows) ^^^^^^

不同调用中 execq() 的行可见性