---
title: "事件触发器"
book: "服务器编程指南"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/reference/referenceTwo4.html"
tags:
  - highgo
  - highgo-v9
  - server-programming-guide
---

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