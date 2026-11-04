---
title: "触发器"
book: "服务器编程指南"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/reference/referenceTwo3.html"
tags:
  - highgo
  - highgo-v9
  - server-programming-guide
---

## 触发器

## 触发器行为概述

一个触发器声明了当执行一种特定类型的操作时数据库应该自动执行一个特殊的函数。触发器可以被附加到表（分区的或者不分区的）、视图和外部表。

在表和外部表上，触发器可以被定义为在 INSERT、UPDATE或 DELETE操作之前或之后被执行， 可以为每个SQL语句被执行一次或者为每个修改的行 被执行一次。UPDATE 触发器可以进一步地设置为只针对UPDATE 语句的SET子句的特定列出发。触发器也可以被 TRUNCATE语句触发。如果一个触发器事件发生， 触发器函数会在适当的事件被调用来处理该事件。

在视图上，触发器可以被定义来取代INSERT、UPDATE或

DELETE操作的执行。这种INSTEAD OF触发器对视图中需要被修改的每一行触发一次。触发器函数的职责是对视图的底层基本表执行必要的修改，并且在合适的时候返回被修改的行以便显示在视图中。视图上的触发器也可以被定义为对每个SQL语句执行一次，在INSERT\\UPDATE或DELETE操作之前或之后。不过，只有在该视图上还有一个INSTEAD OF触发器时，上述那些触发器才会被触发。否则，以该视图为目标的任何语句都必须被重写成一个影响其底层基表的语句，然后附着在那些基表上的触发器将会被引发。

触发器函数必须在触发器本身被创建之前被定义好。触发器函数必须被定义成一个没有参数的函数，并且返回类型为trigger（触发器函数通过一个特殊传递的TriggerData结构作为其输入，而不是以普通函数参数的形式）。

一旦一个合适的触发器函数被创建，就可以使用CREATE TRIGGER建立触发器。同一个触发器函数可以被用于多个触发器。

瀚高数据库同时提供每行的触发器和每语句的触发器。对于一个每行的触发器，对于触发触发器的语句所修改的每一行都会调用一次触发器函数。相反，一个每语句的触发器对于其触发语句只被调用一次，而不管该语句影响了多少行。特别地，一个不影响任何行的语句仍然会导致任何可用每语句的触发器的执行。这两类触发器有时也分别被称作行级触发器和语句级触发器。TRUNCATE上的触发器只能被定义在语句级。

触发器也可以根据它们是否在操作之前、之后触发，或者被触发来取代操作来分类。它们分别指BEFORE触发器、AFTER 触发器以及INSTEAD OF触发器。语句级BEFORE触发器在语句开始做任何事情之前被触发，而语句级AFTER触发器则在语句做完所有事情之后被触发。这些触发器类型可以被定义在表、视图或外部表上。行级BEFORE触发器在每一个行被操作之前被触发，而行级AFTER触发器在语句结束之后被触发（但在任何语句级AFTER触发器之前）。这些触发器类型只能被定义在非分区表和外部表上，但不能定义在视图上。INSTEAD OF触发器只能被定义在视图上，并且只能定义在行级，当视图中的每一行被标识为需要被操作时，它们会立即触发。

一个以继承或者分区层次中父表为目标的语句不会导致受影响的子表的语句级触发器被引发，只有父表的语句级触发器会被引发。不过，受影响的子表的行级触发器将被引发。

如果一个INSERT包含ON CONFLICT DO UPDATE子句并且引用了EXCLUDED列，有可能所有行级BEFORE INSERT触发器和所有行级 BEFORE UPDATE触发器的效果可能会以一种对于 被更新行最终状态透明的方式被应用。不过，对于要执行的两种集合的行级 BEFORE触发器都不需要有EXCLUDED列引用。当同时有行级 BEFORE INSERT和 BEFORE UPDATE触发器影响被插入/ 更新的行时（如果在两者不幂等时修改或多或少地等价，这仍可能是有问题的）， 应该考虑可能出现的意料之外的结果。注意在指定了 ON CONFLICT DO UPDATE时，不管有没有行被 UPDATE影响（并且不管是否采用了其他 UPDATE路径），语句级 UPDATE都将被执行。一个带有 ON CONFLICT DO UPDATE子句的INSERT 将首先执行语句级BEFORE INSERT， 然后执行语句级BEFORE UPDATE触发器， 接着是语句级AFTER UPDATE触发器， 最后是语句级AFTER INSERT触发器。

如果一个分区表上的UPDATE导致一行移动到另一个分区，它将被从原始分区DELETE掉然后再INSERT到新分区中。在这种情况下，原始分区上所有的行级BEFORE UPDATE触发器和所有行级BEFORE DELETE触发器会被引发。然后目标分区上所有的行级BEFORE INSERT触发器会被引发。当所有这些触发器都影响被移动的行时，应该对令人惊讶的结果有心理准备。至于AFTER ROW触发器，AFTER DELETE和AFTER INSERT触发器会被应用，但AFTER UPDATE触发器不会被应用，因为UPDATE已经被转换成了一个DELETE和一个INSERT。

对于语句级触发器，即便发生行移动，DELETE和INSERT触发器也都不会被引发，只有UPDATE语句中用到的目标表上的UPDATE触发器将被引发。

被语句级触发器调用的触发器函数应该总是返回NULL。根据行级触发器的选择，被其调用的触发器函数可以返回一个表行（类型HeapTuple的一个值）给执行器。在一个操作前触发的行级触发器有下列选择：

• 它可以返回NULL来跳过对当前行的操作。这指示执行器不要执行调用触发器的行级操作（对一个特定表行的插入、修改或删除）。

• 仅对行级INSERT和UPDATE触发器来说，被返回的行称为将要被插入的行或者替代将被更新的行。这允许触发器函数修改将要被插入或更新的行。

一个无意导致任何这些行为的行级BEFORE触发器必须小心地它的结果，使之和被传入的行一样（即，INSERT和UPDATE触发器的NEW行，DELETE触发器的OLD行）。

一个行级INSTEAD OF触发器可以返回NULL来指示它没有修改任何来自于视图底层基表的数据，也可以返回被传入的视图行（INSERT和UPDATE操作的NEW行，或者DELETE操作的OLD行）。一个非空返回值被用于标志触发器在视图中执行了必须的数据修改。这将会导致被命令修改的行计数被增加。仅对于INSERT和UPDATE操作，触发器可能会在返回NEW行之前对其进行修改。这将会改变INSERT RETURNING或UPDATE RETURNING返回的数据，并在视图无法正确地显示提供给它的相同数据时有用。

对于在一个操作之后触发的行级触发器，返回值会被忽略，因此它们可以返回NULL。

一些情况适用于生成的列。存储生成的列在BEFORE 触发器之后和AFTER 触发器之前计算. 因此，生成的值可以在AFTER触发器中检查。 在BEFORE触发器中，OLD行包含旧的生成的值，正如人们所期待的，但 NEW 行尚未包含新的生成值并且不应访问。 在C语言界面中，此时列的内容还没有被定义；在BEFORE触发器中，高级别编程语言应阻止访问NEW行中存储生成的列，。 在BEFORE触发器中更改到生成列的值将被忽略并覆盖。

如果为同一个关系上的同一事件定义了超过一个触发器，它们将按照其名称的字母表顺序被触发。在BEFORE和INSTEAD OF触发器的情况下，每一个触发器返回的可能被修改的行将成为下一个触发器的输入。如果任何一个BEFORE或INSTEAD OF触发器返回NULL，该操作将在该行上被禁用并且对于该行不会触发后续的触发器。

一个触发器定义也能指定一个布尔的WHEN条件，它将被测试来看该触发器是否应该被触发。

在行级触发器中，WHEN条件可以检查该行的旧列值和/或新列值（语句级触发器也能有WHEN条件，但是该特性对它们不太有用）。在一个BEFORE触发器中，WHEN条件只是在该函数被或者将被执行前计算，因此使用WHEN条件与在该触发器函数的开始测试相同的条件没有本质区别。不过，在一个AFTER触发器中，WHEN条件只是在行更新发生之后被计算，并且它决定在语句的末尾一个事件是否被排队来触发该触发器。因此当一个AFTER触发器的WHEN不返回真时，在语句的末尾没有必要将一个事件进行排队，也没有必要重新取出该行。如果触发器只对少数行触发，这可以使得修改很多行的语句明显加快。INSTEAD OF触发器不支持WHEN条件。

通常，行级BEFORE被用来检查或修改即将被插入或更新的数据。例如，一个BEFORE触发器可以被用来把当前时间插入到一个timestamp列中，或者检查该行的两个元素之间是否一致。

行级AFTER触发器大多数被用来将更新传播到其他表，或者针对其他表进行一致性检查。进行这种工作分工的原因是，一个AFTER触发器可以肯定它看到的是该行的最终值，而一个BEFORE触发器则不能，因为还可能有其他BEFORE触发器在它之后触发。如果你不知道让一个触发器是BEFORE或AFTER，则BEFORE形式更加有效，因为关于该操作的信息直到语句的末尾都不需要被保存。

如果一个触发器函数执行 SQL 命令，则这些命令可能会再次引发触发器。这就是所谓的级联触发器。对于级联的层数没有直接的限制。级联有可能会导致对同一个触发器的递归调用。

例如，一个INSERT触发器可能执行一个向同一个表插入一个额外行的命令，这就导致该INSERT触发器被再次引发。所以在这种情形下，触发器程序员应该负责避免无限递归。

在定义一个触发器时，可以为它指定参数。在触发器定义中包括参数的目的是允许具有相似需求的不同触发器调用同一个函数。例如，可能有一个一般性的触发器函数，它需要两个列名作为参数，一个放当前用户而另一个放当前时间戳。在正确编写的情况下，这个触发器函数应该独立于它所触发的表。因此同一个函数可以被用于具有适当列的任意表上的INSERT事件，这样做的用途之一是可以自动追踪一个交易表中记录的创建。如果被定义成一个UPDATE触发器，它也可以被用来追踪最新的更新事件。

每一种支持触发器的编程语言都有自己的方法来让触发器输入数据对触发器函数可用。这种输入数据包括触发器事件的类型（如INSERT或UPDATE）以及被列在CREATE TRIGGER中的任何参数。对于一个行级触发器，输入数据还包括用于INSERT和UPDATE触发器的NEW行，和/或用于UPDATE和DELETE触发器的OLD行。语句级触发器当前没有任何方法检查被语句修改的单个行。

默认情况下，语句级触发器没有办法检查该语句修改的行。但是AFTER STATEMENT触发器可以请求创建传递表，这样可以让受影响的行集合对该触发器可用。AFTER ROW触发器也可以请求传递表，这样它们可以看到表中的整个变化，同时也能看到当前引发它们的个体行中的变化。检查传递表的方法仍是取决于使用的编程语言，但是通常的方法让传递表变得像触发器函数内部发出的SQL命令能够访问的只读临时表一样。

## 数据改变的可见性

如果你在你的触发器函数中执行 SQL 命令，并且这些命令会访问触发器所在的表，那么你需要注意数据可见性规则。因为这些规则决定了这些 SQL 命令是否将能看见引发触发器的数据改变。简单地：

• 语句级触发器遵循简单的可见性规则：一个语句所作的改变对于语句级 BEFORE触发器都不可见，而所有修改对于语句级 AFTER触发器都是可见的。

• 导致触发器被引发的数据更改（插入、更新或删除）自然对于在一个行级BEFORE触发器中执行的 SQL 命令不可见，因为它还没有发生。

• 但是，在一个行级BEFORE触发器中执行的 SQL 命令将会看见之前在同一个外层命令中所作的数据更改的效果。这里需要小心，因为这些更改时间的顺序通常是不可预测的，一个影响多行的 SQL 命令可能以任何顺序访问这些行。

• 类似地，一个行级INSTEAD OF触发器将会看见之前在同一个外层命令中INSTEAD OF触发器引发所作的数据更改。

• 当一个行级AFTER触发器被引发时，所有由外层命令所作的数据更改已经完成，并且对于该被调用的触发器函数是可见的。

如果你的触发器函数使用任何一种标准过程语言编写的，那么只有在该函数被声明为VOLATILE时上述陈述才适用。被声明为STABLE或IMMUTABLE的函数在任何情况下将不能看到由调用命令所作出的更改。

## 用 C 编写触发器函数

这一节描述了一个触发器函数的接口的低层细节。只有用 C 编写触发器函数时才需要这些信息。如果你使用一种更高层的语言，那么这些细节就不需要你来处理。在大部分情况下，你应该优先考虑使用一种过程语言。每一种过程语言的文档阐述了如何使用那种语言编写一个触发器。

触发器函数必须使用”版本 1”函数管理器接口。

当一个函数被触发器管理器调用时，不会给它传递任何常规的参数，但是会有一个”context”指针传递给它，该指针指向一个TriggerData结构。C 函数可以通过执行一个宏来检查它们是否是从触发器管理器被调用：

CALLED\_AS\_TRIGGER(fcinfo)

它会展开成为：

((fcinfo)->context!= NULL && IsA((fcinfo)->context, TriggerData))

如果这返回真，那么将fcinfo->context造型成类型TriggerData \*并且利用所指向的TriggerData结构就是安全的。该函数不能修改该TriggerData结构或者它指向的任何数据。

struct TriggerData被定义在commands/trigger.h中：

typedef struct TriggerData

{

NodeTag type;

TriggerEvent tg\_event;

Relation tg\_relation;

HeapTuple tg\_trigtuple;

HeapTuple tg\_newtuple;

Trigger \*tg\_trigger;

TupleTableSlot \*tg\_trigslot;

TupleTableSlot \*tg\_newslot;

Tuplestorestate \*tg\_oldtable;

Tuplestorestate \*tg\_newtable;

} TriggerData;

其中的成员被定义如下：

type

总是T\_TriggerData.

tg\_event

描述该函数是为什么事件被调用的。你可以使用下列宏来检查tg\_event：

TRIGGER\_FIRED\_BEFORE(tg\_event)

如果该触发器在操作前被引发则返回真。

TRIGGER\_FIRED\_AFTER(tg\_event)

如果该触发器在操作后被引发则返回真。

TRIGGER\_FIRED\_INSTEAD(tg\_event)

如果该触发器被引发替代操作则返回真。

TRIGGER\_FIRED\_FOR\_ROW(tg\_event)

如果该触发器为一个行级事件而引发则返回真。

TRIGGER\_FIRED\_FOR\_STATEMENT(tg\_event)

如果该触发器为一个语句级事件而引发则返回真。

TRIGGER\_FIRED\_BY\_INSERT(tg\_event)

如果该触发器由一个INSERT命令引发则返回真。

TRIGGER\_FIRED\_BY\_UPDATE(tg\_event)

如果该触发器由一个UPDATE命令引发则返回真。

TRIGGER\_FIRED\_BY\_DELETE(tg\_event)

如果该触发器由一个DELETE命令引发则返回真。

TRIGGER\_FIRED\_BY\_TRUNCATE(tg\_event)

如果该触发器由一个TRUNCATE命令引发则返回真。

tg\_relation

一个结构指针，该结构描述该触发器为其引发的关系。关于这个结构的细节请参考utils/rel.h。最有趣的东西是tg\_relation->rd\_att（该关系元组的描述符）

和tg\_relation->rd\_rel->relname（关系名称，该类型不是char\*而是NameData。如果你需要该名称的一个拷贝，可使用SPI\_getrelname(tg\_relation)来得到一个char\*）。

tg\_trigtuple

一个该触发器为其引发的行的指针。这是被插入、更新或删除的行。如果这个触发器是为一个INSERT或DELETE而引发，在你不想把该行替换成另一行（在INSERT的情况中）或不想跳过该操作时你应该从该函数中返回它。 对于外部表上的触发器，此中的系统列值未被指定。

tg\_newtuple

如果该触发器为一个UPDATE而引发，则是一个指向该行新版本的指针。如果是为一个INSERT或DELETE而引发，则是NULL。如果事件是一个UPDATE并且你并不想用一个不同的行替换这个行或者不想跳过该操作时，你必须从函数中返回它。对于外部表上的触发器，此中的系统列值未被指定。

tg\_trigger

一个指向类型为Trigger的结构的指针，定义在utils/reltrigger.h中：

typedef struct Trigger

{

Oid tgoid;

char \*tgname;

Oid tgfoid;

int16 tgtype;

char tgenabled;

bool tgisinternal;

Oid tgconstrrelid;

Oid tgconstrindid;

Oid tgconstraint;

bool tgdeferrable;

bool tginitdeferred;

int16 tgnargs;

int16 tgnattr;

int16 \*tgattr;

char \*\*tgargs;

char \*tgqual;

char \*tgoldtable;

char \*tgnewtable;

} Trigger;

其中tgname是该触发器的名称，tgnargs是tgargs中参数的数量，而tgargs是一个指向CREATE TRIGGER语句中指定的参数的指针数组。其他成员只用于内部用途。

tg\_trigtuplebuf

包含tg\_trigtuple的插槽。或者一个NULL指针，如果没有这样的元组的话。

tg\_newtuplebuf

包含tg\_trigtuple的插槽。或者一个NULL指针，如果没有这样的元组的话。

tg\_oldtable

一个指向Tuplestorestate类型的结构的指针，该结构包含格式由tg\_relation指定的零行或者多行。如果没有OLD TABLE传递关系，则为NULL指针。

tg\_newtable

一个指向Tuplestorestate类型的结构的指针，该结构包含格式由tg\_relation指定的零行或者多行。如果没有NEW TABLE传递关系，则为NULL指针。

为了允许通过SPI发出的查询引用传递表，请参考SPI\_register\_trigger\_data。

一个触发器函数必须返回一个HeapTuple指针或一个NULL指针（不是一个 SQL 空值，也就是不会设置isNull为真）。如果你不希望修改正在被操作的行，要小心地根据情况返回tg\_trigtuple或tg\_newtuple。

## 一个完整的触发器实例

这里有一个用 C 编写的触发器函数的非常简单的例子（用过程语言编写的触发器的例子可以在过程语言的文档中找到）。

如果该命令试图向列x中插入一个空值，函数trigf报告表ttest中的行数并且跳过实际的操作（这样该触发器会作为一个非空约束但不会中止事务）。

首先，表定义：

CREATE TABLE ttest (

x integer

);

这是该触发器函数的源代码：

#include "postgres.h"

#include "fmgr.h"

#include "executor/spi.h" /\* this is what you need to work with SPI \*/

#include "commands/trigger.h" /\*... triggers... \*/

#include "utils/rel.h" /\*... and relations \*/

PG\_MODULE\_MAGIC;

PG\_FUNCTION\_INFO\_V1(trigf);

Datum

trigf(PG\_FUNCTION\_ARGS)

{

TriggerData \*trigdata = (TriggerData \*) fcinfo->context;

TupleDesc tupdesc;

HeapTuple rettuple;

char \*when;

bool checknull = false;

bool isnull;

int ret, i;

/\* make sure it's called as a trigger at all \*/

if (!CALLED\_AS\_TRIGGER(fcinfo))

elog(ERROR, "trigf: not called by trigger manager");

/\* tuple to return to executor \*/

if (TRIGGER\_FIRED\_BY\_UPDATE(trigdata->tg\_event))

rettuple = trigdata->tg\_newtuple;

else

rettuple = trigdata->tg\_trigtuple;

/\* check for null values \*/

if (!TRIGGER\_FIRED\_BY\_DELETE(trigdata->tg\_event)

&& TRIGGER\_FIRED\_BEFORE(trigdata->tg\_event))

checknull = true;

if (TRIGGER\_FIRED\_BEFORE(trigdata->tg\_event))

when = "before";

else

when = "after ";

tupdesc = trigdata->tg\_relation->rd\_att;

/\* connect to SPI manager \*/

if ((ret = SPI\_connect()) < 0)

elog(ERROR, "trigf (fired %s): SPI\_connect returned %d", when, ret);

/\* get number of rows in table \*/

ret = SPI\_exec("SELECT count(\*) FROM ttest", 0);

if (ret < 0)

elog(ERROR, "trigf (fired %s): SPI\_exec returned %d", when, ret);

/\* count(\*) returns int8, so be careful to convert \*/

i = DatumGetInt64(SPI\_getbinval(SPI\_tuptable->vals\[0\],

SPI\_tuptable->tupdesc,

1,

&isnull));

elog (INFO, "trigf (fired %s): there are %d rows in ttest", when, i);

SPI\_finish();

if (checknull)

{

SPI\_getbinval(rettuple, tupdesc, 1, &isnull);

if (isnull)

rettuple = NULL;

}

return PointerGetDatum(rettuple);

}

在你编译了该源代码之后，声明该函数和触发器：

CREATE FUNCTION trigf() RETURNS trigger

AS 'filename'

LANGUAGE C;

CREATE TRIGGER tbefore BEFORE INSERT OR UPDATE OR DELETE ON ttest

FOR EACH ROW EXECUTE FUNCTION trigf();

CREATE TRIGGER tafter AFTER INSERT OR UPDATE OR DELETE ON ttest

FOR EACH ROW EXECUTE FUNCTION trigf();

现在你可以测试该触发器的操作：

\=> INSERT INTO ttest VALUES (NULL);

INFO: trigf (fired before): there are 0 rows in ttest

INSERT 0 0

\-- Insertion skipped and AFTER trigger is not fired

\=> SELECT \* FROM ttest;

x

\---

(0 rows)

\=> INSERT INTO ttest VALUES (1);

INFO: trigf (fired before): there are 0 rows in ttest

INFO: trigf (fired after ): there are 1 rows in ttest

^^^^^^^^

remember what we said about visibility.

INSERT 167793 1

vac=> SELECT \* FROM ttest;

x

\---

1

(1 row)

\=> INSERT INTO ttest SELECT x \* 2 FROM ttest;

INFO: trigf (fired before): there are 1 rows in ttest

INFO: trigf (fired after ): there are 2 rows in ttest

^^^^^^

remember what we said about visibility.

INSERT 167794 1

\=> SELECT \* FROM ttest;

x

\---

1

2

(2 rows)

\=> UPDATE ttest SET x = NULL WHERE x = 2;

INFO: trigf (fired before): there are 2 rows in ttest

UPDATE 0

\=> UPDATE ttest SET x = 4 WHERE x = 2;

INFO: trigf (fired before): there are 2 rows in ttest

INFO: trigf (fired after ): there are 2 rows in ttest

UPDATE 1

vac=> SELECT \* FROM ttest;

x

\---

1

4

(2 rows)

\=> DELETE FROM ttest;

INFO: trigf (fired before): there are 2 rows in ttest

INFO: trigf (fired before): there are 1 rows in ttest

INFO: trigf (fired after ): there are 0 rows in ttest

INFO: trigf (fired after ): there are 0 rows in ttest

^^^^^^

remember what we said about visibility.

DELETE 2

\=> SELECT \* FROM ttest;

x

\---

(0 rows)

在src/test/regress/regress.c和spi中有更多复杂的例子。

## 事件触发器

为了对第 7章中讨论的触发器机制加以补充，瀚高数据库也提供了事件触发器。和常规触发器（附着在 一个表上并且只捕捉 DML 事件）不同，事件触发器对一个特定数据库来说是全局 的，并且可以捕捉 DDL 事件。

和常规触发器相似，可以用任何包括了事件触发器支持的过程语言或者 C 编写 事件触发器，但是不能用纯 SQL 编写。

## 事件触发器行为总览

只要与一个事件触发器相关的事件在事件触发器所在的数据库中发生， 该事件触发器就会被引发。当前支持的事件是 ddl\_command\_start、ddl\_command\_end、 table\_rewrite和sql\_drop。未来的发行版 中可能会增加对更多事件的支持。

ddl\_command\_start事件就在CREATE、 ALTER、DROP、SECURITY LABEL、 COMMENT、GRANT或者REVOKE 命令的执行之前发生。在事件触发器引发前不会做受影响对象是否存在的检查。

不过，一个例外是，这个事件不会为目标是共享对象 — 数据库、角色 以及表空间 — 的 DDL 命令发生，也不会为目标是事件触发器的 DDL 命令发生。事件触发器机制不支持这些对象类型。 ddl\_command\_start也会在SELECT INTO 命令的执行之前发生，因为这等价于 CREATE TABLE AS。

ddl\_command\_end事件就在同一组命令的执行之后发生。为了 得到发生的DDL操作的更多细节，可以从 ddl\_command\_end事件触发器代码中使用集合返回函数 pg\_event\_trigger\_ddl\_commands()。注意该触发器是在那些动作 已经发生之后（但是在事务提交前）引发，并且因此系统目录会被读作已更改。

sql\_drop事件为任何删除数据库对象的操作在 ddl\_command\_end事件触发器之前发生。要列出已经被删除的 对象，可以从sql\_drop事件触发器代码中使用集合返回函数 pg\_event\_trigger\_dropped\_objects()。注意该触发器是在对象已经 从系统目录删除以后执行，因此不能再查看它们。

table\_rewrite事件在表被命令ALTER TABLE和 ALTER TYPE的某些动作重写之前发生。虽然其他控制语句（例如 CLUSTER和VACUUM）也可以用来重 写表，但是它们不会触发table\_rewrite事件。

不能在一个中止的事务中执行事件触发器（其他函数也一样）。因此，如果一个 DDL 命令出现错误失败，将不会执行任何相关的 ddl\_command\_end触发器。反过来，如果一个ddl\_command\_start触发器出现错误失败，将不会引发进一步的 事件触发器，并且不会尝试执行该命令本身。类似地，如果一个 ddl\_command\_end触发器出现错误失败，DDL 命令的效果将被 回滚，就像其他包含事务中止的情况中那样。

第 8.2 节中有事件触发器机制所支持的完整 命令列表。

事件触发器通过命令CREATE EVENT TRIGGER创建。为了 创建一个事件触发器，你必须首先创建一个有特殊返回类型 event\_trigger的函数。这个函数不一定需要返回一个值， 该返回类型仅仅是作为一种信号表示该函数要被作为一个事件触发器调用。

如果对于一个特定的事件定义了多于一个事件触发器，它们将按照触发器名称 的字母表顺序被引发。

一个触发器定义也可以指定一个WHEN条件，这样事件触 发器（例如ddl\_command\_start触发器）就可以只对用户 希望介入的特定命令触发。这类触发器的通常用法是用于限制用户可能执行的 DDL 操作的范围。

## 事件触发器触发矩阵

下表列出了所有命令的事件触发器支持情况。

**表 8.1 支持事件触发器的命令标签**

| 命令标签 | ddl\_command\_start | ddl\_command\_end | sql\_drop | table\_rewrite | 注解 |
| --- | --- | --- | --- | --- | --- |
| ALTER AGGREGATE | X | X | \- | \- |  |
| ALTER COLLATION | X | X | \- | \- |  |
| ALTER CONVERSION | X | X | \- | \- |  |
| ALTER DOMAIN | X | X | \- | \- |  |
| ALTER DEFAULT PRIVILEGES | X | X | \- | \- |  |
| ALTER EXTENSION | X | X | \- | \- |  |
| ALTER FOREIGN DATA WRAPPER | X | X | \- | \- |  |
| ALTER FOREIGN TABLE | X | X | X | \- |  |
| ALTER FUNCTION | X | X | \- | \- |  |
| ALTER LANGUAGE | X | X | \- | \- |  |
| ALTER LARGE OBJECT | X | X | \- | \- |  |
| ALTER MATERIALIZED VIEW | X | X | \- | \- |  |
| ALTER OPERATOR | X | X | \- | \- |  |
| ALTER OPERATOR CLASS | X | X | \- | \- |  |
| ALTER OPERATOR FAMILY | X | X | \- | \- |  |
| ALTER POLICY | X | X | \- | \- |  |
| ALTER PROCEDURE | X | X | \- | \- |  |
| ALTER PUBLICATION | X | X | \- | \- |  |
| ALTER SCHEMA | X | X | \- | \- |  |
| ALTER SEQUENCE | X | X | \- | \- |  |
| ALTER SERVER | X | X | \- | \- |  |
| ALTER STATISTICS | X | X | \- | \- |  |
| ALTER SUBSCRIPTION | X | X | \- | \- |  |
| ALTER TABLE | X | X | X | X |  |
| ALTER TEXT SEARCH CONFIGURATION | X | X | \- | \- |  |
| ALTER TEXT SEARCH DICTIONARY | X | X | \- | \- |  |
| ALTER TEXT SEARCH PARSER | X | X | \- | \- |  |
| ALTER TEXT SEARCH TEMPLATE | X | X | \- | \- |  |
| ALTER TRIGGER | X | X | \- | \- |  |
| ALTER TYPE | X | X | \- | X |  |
| ALTER USER MAPPING | X | X | \- | \- |  |
| ALTER VIEW | X | X | \- | \- |  |
| COMMENT | X | X | \- | \- | Only for local objects |
| CREATE ACCESS METHOD | X | X | \- | \- |  |
| CREATE AGGREGATE | X | X | \- | \- |  |
| CREATE CAST | X | X | \- | \- |  |
| CREATE COLLATION | X | X | \- | \- |  |
| CREATE CONVERSION | X | X | \- | \- |  |
| CREATE DOMAIN | X | X | \- | \- |  |
| CREATE EXTENSION | X | X | \- | \- |  |
| CREATE FOREIGN DATA WRAPPER | X | X | \- | \- |  |
| CREATE FOREIGN TABLE | X | X | \- | \- |  |
| CREATE FUNCTION | X | X | \- | \- |  |
| CREATE INDEX | X | X | \- | \- |  |
| CREATE LANGUAGE | X | X | \- | \- |  |
| CREATE MATERIALIZED VIEW | X | X | \- | \- |  |
| CREATE OPERATOR | X | X | \- | \- |  |
| CREATE OPERATOR CLASS | X | X | \- | \- |  |
| CREATE OPERATOR FAMILY | X | X | \- | \- |  |
| CREATE POLICY | X | X | \- | \- |  |
| CREATE PROCEDURE | X | X | \- | \- |  |
| CREATE PUBLICATION | X | X | \- | \- |  |
| CREATE RULE | X | X | \- | \- |  |
| CREATE SCHEMA | X | X | \- | \- |  |
| CREATE SEQUENCE | X | X | \- | \- |  |
| CREATE SERVER | X | X | \- | \- |  |
| CREATE STATISTICS | X | X | \- | \- |  |
| CREATE SUBSCRIPTION | X | X | \- | \- |  |
| CREATE TABLE | X | X | \- | \- |  |
| CREATE TABLE AS | X | X | \- | \- |  |
| CREATE TEXT SEARCH CONFIGURATION | X | X | \- | \- |  |
| CREATE TEXT SEARCH DICTIONARY | X | X | \- | \- |  |
| CREATE TEXT SEARCH PARSER | X | X | \- | \- |  |
| CREATE TEXT SEARCH TEMPLATE | X | X | \- | \- |  |
| CREATE TRIGGER | X | X | \- | \- |  |
| CREATE TYPE | X | X | \- | \- |  |
| CREATE USER MAPPING | X | X | \- | \- |  |
| CREATE VIEW | X | X | \- | \- |  |
| DROP ACCESS METHOD | X | X | X | \- |  |
| DROP AGGREGATE | X | X | X | \- |  |
| DROP CAST | X | X | X | \- |  |
| DROP COLLATION | X | X | X | \- |  |
| DROP CONVERSION | X | X | X | \- |  |
| DROP DOMAIN | X | X | X | \- |  |
| DROP EXTENSION | X | X | X | \- |  |
| DROP FOREIGN DATA WRAPPER | X | X | X | \- |  |
| DROP FOREIGN TABLE | X | X | X | \- |  |
| DROP FUNCTION | X | X | X | \- |  |
| DROP INDEX | X | X | X | \- |  |
| DROP LANGUAGE | X | X | X | \- |  |
| DROP MATERIALIZED VIEW | X | X | X | \- |  |
| DROP OPERATOR | X | X | X | \- |  |
| DROP OPERATOR CLASS | X | X | X | \- |  |
| DROP OPERATOR FAMILY | X | X | X | \- |  |
| DROP OWNED | X | X | X | \- |  |
| DROP POLICY | X | X | X | \- |  |
| DROP PROCEDURE | X | X | X | \- |  |
| DROP PUBLICATION | X | X | X | \- |  |
| DROP RULE | X | X | X | \- |  |
| DROP SCHEMA | X | X | X | \- |  |
| DROP SEQUENCE | X | X | X | \- |  |
| DROP SERVER | X | X | X | \- |  |
| DROP STATISTICS | X | X | X | \- |  |
| DROP SUBSCRIPTION | X | X | X | \- |  |
| DROP TABL | X | X | X | \- |  |
| DROP TEXT SEARCH CONFIGURATION | X | X | X | \- |  |
| DROP TEXT SEARCH DICTIONARY | X | X | X | \- |  |
| DROP TEXT SEARCH PARSER | X | X | X | \- |  |
| DROP TEXT SEARCH TEMPLATE | X | X | X | \- |  |
| DROP TRIGGER | X | X | X | \- |  |
| DROP TYPE | X | X | X | \- |  |
| DROP USER MAPPING | X | X | X | \- |  |
| DROP VIEW | X | X | X | \- |  |
| GRANT | X | X | \- | \- | 只对本地对象 |
| IMPORT FOREIGN SCHEMA | X | X | \- | \- |  |
| REFRESH ATERIALIZED VIEW | X | X | \- | \- |  |
| REVOKE | X | X | \- | \- | 只对本地对象 |
| SECURITY LABEL | X | X | \- | \- | 只对本地对象 |
| SELECT INTO | X | X | \- | \- |  |

## 用 C 编写事件触发器函数

这一节描述了事件触发器函数接口的低层细节。只有在用 C 编写事件 触发器函数时才需要用到这里的信息。如果使用更高层的语言，那么 这些细节已经被处理好了。在大部分情况下都应该优先考虑使用过程 语言来编写你的事件触发器。每一种过程语言的文档都解释了如何用 它编写事件触发器。

事件触发器函数必须使用”版本 1”的函数管理器接口。

当一个函数被事件触发器管理器调用时，向它传递的并不是普通参数， 而是一个指向EventTriggerData结构的 “context”指针。C 函数可以通过执行以下宏来检查它是否被事件触发器管理器调用：

CALLED\_AS\_EVENT\_TRIGGER(fcinfo)

这个宏会被扩展为：

((fcinfo)->context!= NULL && IsA((fcinfo)->context, EventTriggerData))

如果这个宏返回真，那么就可以安全地把

fcinfo->context造型为类型EventTriggerData

\*并且使用所指向的EventTriggerData结构。 函数不能修改 EventTriggerData结构以及它指向的任何内容。

struct EventTriggerData在 commands/event\_trigger.h中定义：

typedef struct EventTriggerData

{

NodeTag type;

const char \*event; /\* 事件名称 \*/

Node \*parsetree; /\* 解析树 \*/

const char \*tag; /\* 命令标签 \*/

} EventTriggerData;

其中的成员定义如下：

type

总是T\_EventTriggerData。

event

描述要为其调用这个函数的事件，可以是 "ddl\_command\_start"、"ddl\_command\_end"、 "sql\_drop"、"table\_rewrite"之一。 这些事件的含义请见第 39.1 节。

parsetree

该命令的解析树的指针。解析树结构可能会在未经通知的情况下改变。

tag

与事件触发器的事件相关联的命令标签，例如 "CREATE FUNCTION"。

一个事件触发器函数必须返回一个NULL指针（ 不是一个 SQL 空值，也就是不要把 isNull设置为真）。

## 一个完整的事件触发器例子

这里是一个用 C 编写的事件触发器函数的简单例子（用过程语言编写的触发器 例子可以在过程语言的文档中找到）。

函数noddl在每一次被调用时抛出一个异常。 事件触发器定义把该函数和

ddl\_command\_start事件关联在了一起。其效果就是所有 DDL 命令都被阻止运行。

这是该触发器函数的源代码：

#include "postgres.h"

#include "commands/event\_trigger.h"

PG\_MODULE\_MAGIC;

PG\_FUNCTION\_INFO\_V1(noddl);

Datum

noddl(PG\_FUNCTION\_ARGS)

{

EventTriggerData \*trigdata;

if (!CALLED\_AS\_EVENT\_TRIGGER(fcinfo)) /\* internal error \*/

elog(ERROR, "not fired by event trigger manager");

trigdata = (EventTriggerData \*) fcinfo->context;

ereport(ERROR,

(errcode(ERRCODE\_INSUFFICIENT\_PRIVILEGE),

errmsg("command \\"%s\\" denied", trigdata->tag)));

PG\_RETURN\_NULL();

}

声明函数和触发器：

CREATE FUNCTION noddl() RETURNS event\_trigger

AS 'noddl' LANGUAGE C;

CREATE EVENT TRIGGER noddl ON ddl\_command\_start

EXECUTE FUNCTION noddl();

现在你可以测试该触发器的操作：

\=# \\dy

List of event triggers

Name | Event | Owner | Enabled | Function | Tags

\-------+-------------------+-------+---------+----------+------

noddl | ddl\_command\_start | dim | enabled | noddl |

(1 row)

\=# CREATE TABLE foo(id serial);

ERROR: command "CREATE TABLE" denied

在这种情况下，为了在需要时能运行某些 DDL 命令，你必须删除该事件触发器 或者禁用它。只在一个事务期间禁用该触发器会比较方便：

BEGIN;

ALTER EVENT TRIGGER noddl DISABLE;

CREATE TABLE foo (id serial);

ALTER EVENT TRIGGER noddl ENABLE;

COMMIT;

（回忆一下，事件触发器本身上的 DDL 命令不受事件触发器影响）。

## 一个表重写事件触发器例子

得益于table\_rewrite事件的存在，我们可以实现一种只允许在 维护窗口中重写的表重写策略。

这里是实现这种策略的例子。

CREATE OR REPLACE FUNCTION no\_rewrite()

RETURNS event\_trigger

LANGUAGE plpgsql AS

$$

\---

\--- 实现本地表重写策略：

\--- public.foo 不允许重写，其他表只允许在 1am 和 6am 之间重写，

\--- 且前提是它们拥有不超过 100 块

\---

DECLARE

table\_oid oid:= pg\_event\_trigger\_table\_rewrite\_oid();

current\_hour integer:= extract('hour' from current\_time);

pages integer;

max\_pages integer:= 100;

BEGIN

IF pg\_event\_trigger\_table\_rewrite\_oid() = 'public.foo'::regclass

THEN

RAISE EXCEPTION 'you''re not allowed to rewrite the table %',

table\_oid::regclass;

END IF;

SELECT INTO pages relpages FROM pg\_class WHERE oid = table\_oid;

IF pages > max\_pages

THEN

RAISE EXCEPTION 'rewrites only allowed for table with less than %

pages',

max\_pages;

END IF;

IF current\_hour NOT BETWEEN 1 AND 6

THEN

RAISE EXCEPTION 'rewrites only allowed between 1am and 6am';

END IF;

END;

$$;

CREATE EVENT TRIGGER no\_rewrite\_allowed

ON table\_rewrite

EXECUTE FUNCTION no\_rewrite();