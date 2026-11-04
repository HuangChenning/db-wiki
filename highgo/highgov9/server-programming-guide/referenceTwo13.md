---
title: "逻辑解码"
book: "服务器编程指南"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/reference/referenceTwo13.html"
tags:
  - highgo
  - highgo-v9
  - server-programming-guide
---

## 逻辑解码

瀚高数据库提供了方法将所执行的修改通过 SQL 以流的方式传送给外部消费者。 这种功能可以被用于多种目的，包括复制方案以及审计。

在流中被送出的更改通过逻辑复制槽标识。

流式传输这些更改的格式由使用的输出插件决定。瀚高数据库发布中包括了 一个例子插件。可以编写额外的插件来扩展可用的格式选择，而无需修改任何 核心代码。每一个输出插件都能访问每一个由INSERT产生的新行以及每一个由 UPDATE创建的新行版本。

UPDATE和DELETE 的旧行版本的可用性取决于配置的复制标识（见 REPLICA IDENTITY）。

可以通过流复制协议或者通过 SQL 调用函数来接收流式传送的更改。也可以编写额外的 接收复制槽输出的模块而无需修改核心代码。

## 逻辑解码的例子

下面的例子演示了使用 SQL 接口控制逻辑解码。

在你能使用逻辑解码之前，你必须设置wal\_level为 logical，并且max\_replication\_slots必须至少被设置为 1。然后，你应该作为一个超级用户连接到目标数据库（在下面 的例子中是postgres）。

postgres=# -- 使用输出插件'test\_decoding'创建一个名为'regression\_slot'的槽

postgres=# SELECT \* FROM pg\_create\_logical\_replication\_slot('regression\_slot',

'test\_decoding');

slot\_name | lsn

\-----------------+-----------

regression\_slot | 0/16B1970

(1 row)

postgres=# SELECT slot\_name, plugin, slot\_type, database, active, restart\_lsn,

confirmed\_flush\_lsn FROM pg\_replication\_slots;

slot\_name | plugin | slot\_type | database | active | restart\_lsn |

confirmed\_flush\_lsn

\-----------------+---------------+-----------+----------+--------+-------------

+-----------------

regression\_slot | test\_decoding | logical | postgres | f | 0/16A4408 |

0/16A4440

(1 row)

postgres=# -- 目前还看不到更改

postgres=# SELECT \* FROM pg\_logical\_slot\_get\_changes('regression\_slot', NULL,

NULL);

lsn | xid | data

\-----+-----+------

(0 rows)

postgres=# CREATE TABLE data(id serial primary key, data text);

CREATE TABLE

postgres=# -- DDL 没有被复制，因此你将看到的东西只有事务

postgres=# SELECT \* FROM pg\_logical\_slot\_get\_changes('regression\_slot', NULL,

NULL);

lsn | xid | data

\-----------+-------+--------------

0/BA2DA58 | 10297 | BEGIN 10297

0/BA5A5A0 | 10297 | COMMIT 10297

(2 rows)

postgres=# -- 一单读到更改，它们会被消费掉并且不会在一个后续调用中被发出：

postgres=# SELECT \* FROM pg\_logical\_slot\_get\_changes('regression\_slot', NULL,

NULL);

lsn | xid | data

\-----+-----+------

(0 rows)

postgres=# BEGIN;

postgres=# INSERT INTO data(data) VALUES('1');

postgres=# INSERT INTO data(data) VALUES('2');

postgres=# COMMIT;

postgres=# SELECT \* FROM pg\_logical\_slot\_get\_changes('regression\_slot', NULL,

NULL);

lsn | xid | data

\-----------+-------+---------------------------------------------------------

0/BA5A688 | 10298 | BEGIN 10298

0/BA5A6F0 | 10298 | table public.data: INSERT: id\[integer\]:1 data\[text\]:'1'

0/BA5A7F8 | 10298 | table public.data: INSERT: id\[integer\]:2 data\[text\]:'2'

0/BA5A8A8 | 10298 | COMMIT 10298

(4 rows)

postgres=# INSERT INTO data(data) VALUES('3');

postgres=# -- 你也可以不消费更改而在更改流中先看一看

postgres=# SELECT \* FROM pg\_logical\_slot\_peek\_changes('regression\_slot', NULL,

NULL);

lsn | xid | data

\-----------+-------+---------------------------------------------------------

0/BA5A8E0 | 10299 | BEGIN 10299

0/BA5A8E0 | 10299 | table public.data: INSERT: id\[integer\]:3 data\[text\]:'3'

0/BA5A990 | 10299 | COMMIT 10299

(3 rows)

postgres=# -- 接下来对 pg\_logical\_slot\_peek\_changes() 的调用再次返回相同的更改

postgres=# SELECT \* FROM pg\_logical\_slot\_peek\_changes('regression\_slot', NULL,

NULL);

lsn | xid | data

\-----------+-------+---------------------------------------------------------

0/BA5A8E0 | 10299 | BEGIN 10299

0/BA5A8E0 | 10299 | table public.data: INSERT: id\[integer\]:3 data\[text\]:'3'

0/BA5A990 | 10299 | COMMIT 10299

(3 rows)

postgres=# -- 可以向输出插件传递选项来影响格式化

postgres=# SELECT \* FROM pg\_logical\_slot\_peek\_changes('regression\_slot', NULL,

NULL, 'include-timestamp', 'on');

lsn | xid | data

\-----------+-------+---------------------------------------------------------

0/BA5A8E0 | 10299 | BEGIN 10299

0/BA5A8E0 | 10299 | table public.data: INSERT: id\[integer\]:3 data\[text\]:'3'

0/BA5A990 | 10299 | COMMIT 10299 (at 2017-05-10 12:07:21.272494-04)

(3 rows)

postgres=# -- 当不再需要一个槽后记住销毁它以停止消耗服务器资源：

postgres=# SELECT pg\_drop\_replication\_slot('regression\_slot');

pg\_drop\_replication\_slot

\-----------------------

(1 row)

下面的例子展示了如何在流复制协议上使用 瀚高数据库发布所包括的程序pg\_recvlogical来控制逻辑解码。这要求设置客户端认证以允许复制连接，并且把max\_wal\_senders设置成足够高以允许一个额外的连接。

$ pg\_recvlogical -d postgres --slot=test --create-slot

$ pg\_recvlogical -d postgres --slot=test --start -f -

Control+Z

$ psql -d postgres -c "INSERT INTO data(data) VALUES('4');"

$ fg

BEGIN 693

table public.data: INSERT: id\[integer\]:4 data\[text\]:'4'

COMMIT 693

Control+C

$ pg\_recvlogical -d postgres --slot=test --drop-slot

## 逻辑解码概念

### 逻辑解码

逻辑解码是一种将对数据库表的所有持久更改抽取到一种清晰、易于理解的格式 的处理，这种技术允许在不了解数据库内部状态的详细知识的前提下解释该格式。

在瀚高数据库中，逻辑解码通过解码 预写式日志的内容来实现，预写式日志描述了存储 层面上的更改，而逻辑解码则会把更改解码成一种应用相关的形式，例如一个元组流或者 SQL语句流。

### 复制槽

在逻辑复制的环境下，一个槽表示一个更改流，这些更改可以在客户机上以它们在原服务器上产生的顺序被重播。每一个流从一个单一数据库中流式传送更改序列。

| 注意： |
| --- |
| 瀚高数据库也有流复制槽，但是它们的使用有所不同。 |

一个复制槽在一个瀚高数据库集簇的所 有数据库之间具有一个唯一的标识符。槽在使用它们的连接之间保持独立并且 对于崩溃是安全的。

在常规操作中，一个逻辑槽只会把每次更改发出一次。只有在检查点时才会持久化每一个槽的当前位置，因此如果发生崩溃，槽可能会回到一个较早的 LSN，这会导致服务器重启时重新发送最近的更改。逻辑解码客户端负责避免多次处理同一消息导致的副作用。客户端可能会希望在解码时记录它们看到的最新的 LSN，并且跳过任何从该 LSN 解码得到的重复数据或者（使用复制协议时的）请求，而不是让服务器来决定开始点。复制进度跟踪特性就是为此服务的，请参考复制源头。

对于同一个数据库可能会存在多个独立的槽。每一个槽有自己的状态，允许不 同的消费者从该数据库的更改流中的不同点开始接收更改。对于大多数应用， 每一个消费者都将要求一个单独的槽。

逻辑复制槽完全不知道接收者的状态。甚至可能会有多个不同的接收者在不同 时间使用同一个槽，它们将只是从上一个接收者停止消费更改的地方开始得到 更改。但在任一给定时刻，只有一个接收者可以从一个槽中消费更改。

### 输出插件

输出插件将数据从预写式日志的内部表示转换成复制槽的消费者所需的格式。

### 导出快照

当使用流复制接口创建一个新的复制槽时（见CREATE\_REPLICATION\_SLOT），一个快照将被导出，在它所显示的 数据库状态之后所有的更改都将被包括在更改流中。通过使用 SET TRANSACTION SNAPSHOT读取槽被创建时的数据库状态，这可以用来创建 一个新的复制。然后这个事务可以被用来及时转储那一点的数据库状态，它后来可以被槽的内容更新而不丢失任何更改。

并非总能够创建快照。特别是在连接到热备时，快照创建将会失败。不要求快照导出的应用可以用NOEXPORT\_SNAPSHOT选项来抑制它。

## 流复制协议接口

命令

• CREATE\_REPLICATION\_SLOT slot\_name LOGICAL output\_plugin

• DROP\_REPLICATION\_SLOT slot\_name \[ WAIT \]

• START\_REPLICATION SLOT slot\_name LOGICAL...

被用来创建、删除以及流式传送一个复制槽。这些命令只能在一个复制连接上使用。 它们不同通过 SQL 使用。

命令pg\_recvlogical可以被用来控制一个流复制连接上的逻辑 解码（它在内部使用上述命令）。

## 逻辑解码的 SQL 接口

同步复制只在使用流复制接口的复制槽上 支持。函数接口以及额外的、非核心的接口不支持同步复制。

## 与逻辑解码相关的系统目录

pg\_replication\_slots 视图和 pg\_stat\_replication 视图分别提供了有关复制槽和流复制连接的当前状态的信息。这些视图适用于物理和逻辑复制。

## 逻辑解码输出插件

可以在瀚高数据库源码树的 contrib/test\_decoding 子目录中找到一个输出插件的例子。

### 初始化函数

一个输出插件是通过动态载入一个以输出插件名称作为基础名称的共享库来载入的。将使用普通的库搜索路径来定位该库。为了提供所要求的输出插件回调并且指示该 库确实是一个输出插件，需要提供一个名为 \_PG\_output\_plugin\_init的函数。这个函数会被传入一个结构，其中被填充了各个动作的回调函数指针。

typedef struct OutputPluginCallbacks

{

LogicalDecodeStartupCB startup\_cb;

LogicalDecodeBeginCB begin\_cb;

LogicalDecodeChangeCB change\_cb;

LogicalDecodeTruncateCB truncate\_cb;

LogicalDecodeCommitCB commit\_cb;

LogicalDecodeMessageCB message\_cb;

LogicalDecodeFilterByOriginCB filter\_by\_origin\_cb;

LogicalDecodeShutdownCB shutdown\_cb;

} OutputPluginCallbacks;

typedef void (\*LogicalOutputPluginInit) (struct OutputPluginCallbacks \*cb);

回调函数begin\_cb、change\_cb 以及commit\_cb是必需的，而startup\_cb、filter\_by\_origin\_cb、truncate\_cb 和shutdown\_cb是可选的。如果没有设置truncate\_cb但是要对一个TRUNCATE进行编码，则该动作将被忽略。

### 能力

要解码、格式化并且输出更改，输出插件可以使用大部分后端的标准功能，包括调用 输出函数。只要访问的关系是initdb在 pg\_catalog模式中创建的或者被使用

ALTER TABLE user\_catalog\_table SET (user\_catalog\_table = true);

CREATE TABLE another\_catalog\_table(data text) WITH (user\_catalog\_table = true);

标记为用户提供的系统表，就允许对关系的只读访问。任何导致事务 ID 分配的动作 都被禁止。其中包括写表、执行 DDL 更改以及调用txid\_current()。

### 输出模式

输出插件回调可以以近乎任意格式向消费者传递数据。对于某些用例，例如通过 SQL 查看更改，以可能包含任何数据的数据类型（例如bytea）返回数据 可能会很麻烦。如果输出插件只输出服务器编码的文本数据，它可以在启动回调中通过把OutputPluginOptions.output\_type设 置为OUTPUT\_PLUGIN\_TEXTUAL\_OUTPUT替代 OUTPUT\_PLUGIN\_BINARY\_OUTPUT来声明这一点。在这种情况下， 所有的数据必须是属于服务器的编码，这样一个text数据就能包含它。在 启用了断言的编译中会检查这一点。

### 输出插件回调

一个输出插件需要提供一些回调，它通过它们得到有关更改发生的通知。

并发事务以提交顺序被解码，并且只有属于特定事务的更改会在 begin和commit回调之间被解码。被显式 或隐式回滚的事务不会被解码。成功的检查点被折叠到包含它们的事务中，并且 保持它们在该事务中被执行的顺序。

| 注意： |
| --- |
| 只有已经被安全地刷入磁盘的事务将会被解码。当 synchronous\_commit被设置为off 时，这会导致一个COMMIT在随后的pg\_logical\_slot\_get\_changes()中不会立即被解码。 |

#### 启动回调

只要一个复制槽被创建或者被要求流式传送更改，可选的 startup\_cb回调就会被调用，不管有多少更改准备输出。

typedef void (\*LogicalDecodeStartupCB) (struct LogicalDecodingContext \*ctx,

OutputPluginOptions \*options,

bool is\_init);

当复制槽被创建时，is\_init参数将为真，否则为假。 options指向一个输出插件可以设置的选项的结构：

typedef struct OutputPluginOptions

{

OutputPluginOutputType output\_type;

bool receive\_rewrites;

} OutputPluginOptions;

output\_type必须被设置为

OUTPUT\_PLUGIN\_TEXTUAL\_OUTPUT 或者OUTPUT\_PLUGIN\_BINARY\_OUTPUT。另见第17.6.3 节。如果receive\_rewrites为真，还将为在某些DDL操作期间的堆重写造成的更改调用输出插件。这些是处理DDL复制的插件感兴趣的事情，但是它们要求特殊的处理。

启动回调应该验证出现在 ctx->output\_plugin\_options中的选项。如果输出插件 需要有一个状态，它可以使用 ctx->output\_plugin\_private来存储之。

#### 关闭回调

只要一个之前活跃的复制槽不再使用，就会调用可选的shutdown\_cb回调，它可以被用来释放输出插件私有的资源。该槽并不一定需要被删除，只要其中的流被停止即可。

typedef void (\*LogicalDecodeShutdownCB) (struct LogicalDecodingContext \*ctx);

#### 事务开始回调

只要一个已提交事务的开始动作被解码，就会调用必须提供的 begin\_cb回调。被中止的事务及其内容不会被解码。

typedef void (\*LogicalDecodeBeginCB) (struct LogicalDecodingContext \*ctx,

ReorderBufferTXN \*txn);

txn参数包含有关该事务的元信息，例如该 事务被提交的时间戳以及该事务的 XID。

#### 事务结束回调

只要一个已提交事务的提交动作被解码，就会调用必须提供的 commit\_cb回调。在此之前，如果有任何被修改 的行，将为所有被修改的行调用change\_cb回调。

typedef void (\*LogicalDecodeCommitCB) (struct LogicalDecodingContext \*ctx,

ReorderBufferTXN \*txn,

XLogRecPtr commit\_lsn);

#### 更改回调

对于一个事务中的每一个行修改，都将调用必须提供的 change\_cb回调，这种修改可能是一个 INSERT、UPDATE或者 DELETE。即使原始命令一次修改了多行，该回调也会 为其中的每一行调用一次。

typedef void (\*LogicalDecodeChangeCB) (struct LogicalDecodingContext \*ctx,

ReorderBufferTXN \*txn,

Relation relation,

ReorderBufferChange \*change);

ctx和txn参数与 begin\_cb和commit\_cb 回调具有相同的内容，但是额外多出一个关系描述符 relation指向该行所属的关系以及一个结构 change描述被传入的行修改。

| 注意： |
| --- |
| 只有没有被标记为”不做日志”（见 UNLOGGED）并且非临时（见 TEMPORARY or TEMP）的用户定义表中的 更改才能用逻辑解码抽取。 |

#### 截断回调

truncate\_cb回调会为一个TRUNCATE命令被调用。

typedef void (\*LogicalDecodeTruncateCB) (struct LogicalDecodingContext \*ctx,

ReorderBufferTXN \*txn,

int nrelations,

Relation relations\[\],

ReorderBufferChange \*change);

参数类似于change\_cb回调。不过，由于通过外键连接起来的表上的TRUNCATE动作需要一起被执行，这个回调会接收到一个关系的数组而不是单个关系。详情请见对TRUNCATE语句的介绍。

#### 源过滤器回调

可选的filter\_by\_origin\_cb回调被用来 决定从origin\_id重放的数据是否是 输出插件感兴趣的数据。

typedef bool (\*LogicalDecodeFilterByOriginCB) (struct LogicalDecodingContext

\*ctx,

RepOriginId origin\_id);

ctx参数具有和其他回调相同的内容。 对这个回调只有复制源的信息可用。要标志传进来的节点上发生的 更改是无关的，返回真，这会导致这些更改被过滤掉，否则返回假。 对于被过滤掉的事务和更改将不会调用其他回调。

在实现级联或者多向复制方案时，这个回调可以派上用场。用源头 过滤允许阻止在这样的设置下来回地复制同样的更改。虽然事务和 更改也携带了有关源头的信息，通过这个回调过滤明显更有效些。

#### 通用消息回调

只要一个逻辑解码消息被解码出来，可选的message\_cb回调就会被调用。

typedef void (\*LogicalDecodeMessageCB) (struct LogicalDecodingContext \*ctx,

ReorderBufferTXN \*txn,

XLogRecPtr message\_lsn,

bool transactional,

const char \*prefix,

Size message\_size,

const char \*message);

txn参数包含关于该事务的元信息，如被提交的时间戳和 XID。不过要注意，当消息是非事务性的并且记录该消息的事务中还没有被分配 XID 时，这个参数可以为 NULL。lsn是该消息的 WAL 位置。transactional说明该消息是否为事务性的。prefix是一个任意的空终结的前缀，它当前插件被用来标识感兴趣的消息。最后的message参数保存着大小为message\_size的消息。

应该格外小心确保输出插件用于标识感兴趣消息的前缀是唯一的。建议使用扩展或者输出插件本身的名称。

### 用于产生输出的函数

在begin\_cb、commit\_cb或者 change\_cb回调中，为了实际产生输出， 输出插件可以把数据写入到ctx->out中的 StringInfo输出缓冲区中。在写出到输出缓冲区之前，必须先调用OutputPluginPrepareWrite(ctx, last\_write)，在完 成写入到缓冲区后，必须调用OutputPluginWrite(ctx, last\_write)来执行写出。 last\_write指出一次特定的写出是否为该回调的最后 一次写出。

下面的例子展示了如何把数据输出给一个输出插件的消费者：

OutputPluginPrepareWrite(ctx, true);

appendStringInfo(ctx->out, "BEGIN %u", txn->xid);

OutputPluginWrite(ctx, true);

## 逻辑解码输出写入器

可以为逻辑解码增加更多输出方法。本质上，需要提供三个函数：一个读取 WAL，一个准备写输出，另一个写输出（ 见第 17.6.5 节）。

## 逻辑解码的同步复制支持

逻辑解码可以被用来构建 同步复制方案，该方案 具有和流复制的同步复制 相同的用户接口。要这样做，流复制接口（见 第 17.3 节）必须被用来流式传出数据。 正如流复制客户端所作的一样，逻辑解码的客户端必须发出 后备机状态更新 (F) 消息。

| 注意： |
| --- |
| 一个通过逻辑解码接收更改的同步复制机将工作在一个单一数据库的范围内。因为与之相反，synchronous\_standby\_names 当前是服务器范围的，这意味着如果有多于一个数据库被活跃地使用，这种技术将无法正常工作。 |