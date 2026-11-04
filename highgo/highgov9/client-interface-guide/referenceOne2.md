---
title: "libpq-c库"
book: "客户端接口指南"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/reference/referenceOne2.html"
tags:
  - highgo
  - highgo-v9
  - client-interface-guide
---

## libpq-c库

libpq是应用程序员使用瀚高数据库的C接口。libpq是一个库函数的集合，它们允许客户端程序传递查询给瀚高数据库后端服务器并且接收这些查询的结果。

libpq也是很多其他瀚高数据库应用接口的底层引擎，包括为 C++、Perl、Python、Tcl和ECPG编写的接口。如果你使用那些包，某些方面的libpq行为将会对你很重要。

在本章的末尾包括了一些短程序来展示如何编写使用libpq的应用。在源代码发布的src/test/examples目录中还有一些完整的libpq应用的例子。

使用libpq的客户端程序必须包括头文件libpq-fe.h并必须与libpq库链接在一起。

## 数据库连接控制函数

下列函数会建立到一个瀚高数据库后端服务器的连接。一个应用程序可以在一个时刻打开多个后端连接（原因之一就是为了访问多个数据库）。每个连接用一个PGconn对象表示，它从函数PQconnectdb、PQconnectdbParams或PQsetdbLogin得到。注意这些函数将总是返回一个非空的对象指针，除非正好没有内存来分配PGconn对象。在通过该连接对象发送查询之前，应该调用PQstatus函数来检查返回值以确定是否得到了一个成功的连接。

| 警告： |
| --- |
| 如果不可信用户能够访问一个没有采用安全方案使用模式的数据库，开始每个会话时应该从search\_path中移除公共可写的方案。我们可以把参数关键词options设置为-csearch\_path=。也可以在连接后发出PQexec(conn,"SELECT pg\_catalog.set\_config('search\_path', '', false)")。这种考虑并非专门针对libpq，它适用于每一种用来执行任意SQL命令的接口。 |

| 警告： |
| --- |
| 在 Unix 上，复制一个拥有打开 libpq 连接的进程可能导致不可以预料的结果，因为父进程和子进程会共享相同的套接字和操作系统资源。出于这个原因，我们不推荐这样的用法，尽管从子进程执行一个exec来载入新的可执行代码是安全的。 |

| 警告： |
| --- |
| 在 Windows 上，如果一个单一数据库连接被反复地开启并且关闭，这是一种提升性能的方式。在内部，libpq 为开启和关闭分别调用WSAStartup()和WSACleanup()。WSAStartup()会增加一个内部 Windows 库引用计数而WSACleanup()则会减少之。当引用计数正好为一时，调用WSACleanup()会释放所有资源并且所有 DLL 会被卸载。这是一种昂贵的操作。为了避免它，一个应用可以手动调用WSAStartup()，这样当最后的数据库连接被关闭时资源不会被释放。 |

PQconnectdbParams

开启一个到数据库服务器的新连接。

PGconn \*PQconnectdbParams(const char \* const \*keywords, const char \* const \*values, int expand\_dbname);

这个函数使用从两个以NULL结尾的数组中取得的参数打开一个新的数据库连接。第一个数组keywords被定义为一个字符串数组，每一个元素是一个关键词。第二个数组values给出了每个关键词的值。和下面的PQsetdbLogin不同，可以在不改变函数签名的情况下扩展参数集合，因此使用这个函数（或者与之相似的非阻塞的PQconnectStartParams和PQconnectPoll）对于新应用编程要更好。

当expand\_dbname为非零时，dbname关键词的值被允许识别为一个连接字符串。只有dbname的第一次出现会按这种方式扩展，任何后续dbname值会被当做一个普通数据库名处理。

被传递的数组可以为空，这样就会使用所有默认参数。也可以只包含一个或几个参数设置。两个参数数组应该在长度上匹配。对于参数数组的处理将会停止于keywords数组中第一个非-NULL元素。

如果任何一个参数是NULL或者一个空字符串，那么将会检查相应的环境变量。如果该环境变量也没有被设置，那么将使用内建的默认值。

通常，关键词的处理是从这些数组的头部开始并且以索引顺序进行。这样做的效果就是，当关键词有重复时，只会保留最后一个被处理的值。因此，通过小心地放置关键词dbname，可以决定什么会被一个conninfo字符串所重载，以及什么不会被重载。

PQconnectdb

开启一个到数据库服务器的新连接。

PGconn \*PQconnectdb(const char \*conninfo);

这个函数使用从字符串conninfo中得到的参数开启一个新的数据库连接。

被传递的字符串可以为空，这样将会使用所有的默认参数。也可以包含由空格分隔的一个或多个参数设置，还可以包含一个URI。

PQsetdbLogin

开启一个到数据库服务器的新连接。

PGconn \*PQsetdbLogin(const char \*pghost, const char \*pgport, const char \*pgoptions, const char \*pgtty, const char \*dbName, const char \*login, const char \*pwd);

这是PQconnectdb的带有固定参数集合的前辈。它具有相同的功能，不过其中缺失的参数将总是采用默认值。对任意一个固定参数写NULL或一个空字符串将会使它采用默认值。

如果dbName包含一个=符号或者具有一个合法的连接URI前缀，它会被当作一个conninfo字符串，就好像它已经被传递给了PQconnectdb，并且剩余的参数则被应用为指定给PQconnectdbParams。

PQsetdb

开启一个到数据库服务器的新连接。

PGconn \*PQsetdb(char \*pghost, char \*pgport, char \*pgoptions, char \*pgtty, char \*dbName);

这是一个调用PQsetdbLogin的宏，其中为login和pwd参数使用空指针。提供它是为了向后兼容非常老的程序。

PQconnectStartParams

PQconnectStart

PQconnectPoll

以非阻塞的方式建立一个到数据库服务器的连接。

PGconn \*PQconnectStartParams(const char \* const \*keywords, const char \* const \*values,

int expand\_dbname);

PGconn \*PQconnectStart(const char \*conninfo);

PostgresPollingStatusType PQconnectPoll(PGconn \*conn);

这三个函数被用来开启一个到数据库服务器的连接，这样你的应用的执行线程不会因为远程的I/O而被阻塞。这种方法的要点在于等待I/O完成可能在应用的主循环中发生，而不是在PQconnectdbParams或PQconnectdb中，并且因此应用能够把这种操作和其他动作并行处理。

在PQconnectStartParams中，数据库连接使用从keywords和values数组中取得的参数创建，并且被expand\_dbname控制，这和之前描述的PQconnectdbParams相同。

在PQconnectStart中，数据库连接使用从字符串conninfo中取得的参数创建，这和之前描述的PQconnectdb相同。

只要满足一些限制，PQconnectStartParams或PQconnectStart或PQconnectPoll都不会阻塞：

• hostaddr和host参数必须被合适地使用，以防止做DNS查询。 libpq-c库 这些参数的文档。

• 如果你调用PQtrace，确保你追踪的该流对象不会阻塞。

• 如后文所述，你必须要确保在调用PQconnectPoll之前，套接字处于合适的状态。

要开始无阻塞的连接请求，可调用PQconnectStart或者PQconnectStartParams。如果结果为空，则libpq无法分配一个新的PGconn结构。否则，一个有效的PGconn指针会被返回（不过还没有表示一个到数据库的有效连接）。接下来调用PQstatus(conn)。如果结果是CONNECTION\_BAD，则连接尝试已经失败，通常是因为有无效的连接参数。

如果PQconnectStart成功，下一个阶段是轮询libpq，这样它能够继续进行连接序列。使用PQsocket(conn)来获得该数据库连接底层的套接字描述符（警告：不要假定在PQconnectPoll调用之间套接字会保持相同）。这样循环：如果PQconnectPoll(conn)上一次返回PGRES\_POLLING\_READING，等到该套接字准备好读取（按照select()、poll()或类似的系统函数所指示的）。则再次调用PQconnectPoll(conn)。反之，如果PQconnectPoll(conn)上一次返回PGRES\_POLLING\_WRITING，等到该套接字准备好写入，则再次调用PQconnectPoll(conn)。在第一次迭代时，即如果你还没有调用PQconnectPoll，行为就像是它上次返回PGRES\_POLLING\_WRITING。持续这个循环直到PQconnectPoll(conn)返回PGRES\_POLLING\_FAILED指示连接过程已经失败，或者返回PGRES\_POLLING\_OK指示连接已经被成功地建立。

在连接期间的任意时刻，该连接的状态可以通过调用PQstatus来检查。如果这个调用返回CONNECTION\_BAD，那么连接过程已经失败。如果该调用返回CONNECTION\_OK，则该连接已经准备好。如前所述，这些状态同样都可以从PQconnectPoll的返回值检测。在一个异步连接过程中（也只有在这个过程中）也可能出现其他状态。这些状态指示该连接过程的当前阶段，并且可能有助于为用户提供反馈。这些状态是：

CONNECTION\_STARTED

等待连接被建立。

CONNECTION\_MADE

连接OK，等待发送。

CONNECTION\_AWAITING\_RESPONSE

等待来自服务器的一个回应。

CONNECTION\_AUTH\_OK

收到认证，等待后端启动结束。

CONNECTION\_SSL\_STARTUP

协商 SSL 加密。

CONNECTION\_SETENV

协商环境驱动的参数设置。

CONNECTION\_CHECK\_WRITABLE

检查连接是否能够处理写事务。

CONNECTION\_CONSUME

消费连接上的任何剩下的响应消息。

注意，尽管这些常数将被保留（为了维护兼容性），一个应用永远不应该依赖这些状态按照特定顺序出现，或者根本就不依赖它们，或者不依赖状态总是这些文档中所说的值。一个应用可能做些这样的事情：

switch(PQstatus(conn))

{

case CONNECTION\_STARTED:

feedback = "Connecting...";

break;

case CONNECTION\_MADE:

feedback = "Connected to server...";

break;

.

.

.

default:

feedback = "Connecting...";

}

在使用PQconnectPoll时，连接参数connect\_timeout会被忽略：判断是否超时是应用的责任。否则，PQconnectStart后面跟着后面跟着PQconnectPoll循环等效于PQconnectdb。

注意当PQconnectStart或PQconnectStart返回一个非空的指针时，你必须在用完它之后调用PQfinish来处理那些结构和任何相关的内存块。即使连接尝试失败或被放弃时也必须完成这些工作。

PQconndefaults

返回默认连接选项。

PQconninfoOption \*PQconndefaults(void);

typedef struct

{

char \*keyword; /\* 该选项的关键词 \*/

char \*envvar; /\* 依赖的环境变量名 \*/

char \*compiled; /\* 依赖的内建默认值 \*/

char \*val; /\* 选项的当前值，或者 NULL \*/

char \*label; /\* 连接对话框中域的标签 \*/

char \*dispchar; /\* 指示如何在一个连接对话框中显示这个域。值是：

"" 显示输入的值

"\*" 口令域 - 隐藏值

"D" 调试选项 - 默认不显示 \*/

int dispsize; /\* 用于对话框的以字符计的域尺寸 \*/

} PQconninfoOption;

返回一个连接选项数组。这可以用来确定用于连接服务器的所有可能的PQconnectdb选项和它们的当前缺省值。返回值指向一个PQconninfoOption结构的数组，该数组以一个包含空keyword指针的条目结束。如果无法分配内存，则返回该空指针。注意当前缺省值（val域）将依赖于环境变量和其他上下文。一个缺失或者无效的服务文件将会被无声地忽略掉。调用者必须把连接选项当作只读对待。

在处理完选项数组后，把它交给PQconninfoFree释放。如果没有这么做， 每次调用PQconndefaults都会导致一小部分内存泄漏。

PQconninfo

返回被一个活动连接使用的连接选项。

PQconninfoOption \*PQconninfo(PGconn \*conn);

返回一个连接选项数组。这可以用来确定用于连接服务器的所有可能的PQconnectdb选项和它们的当前缺省值。返回值指向一个PQconninfoOption结构的数组，该数组以一个包含空keyword指针的条目结束。上述所有对于PQconndefaults的注解也适用于PQconninfo的结果。

PQconninfoParse

返回从提供的连接字符串中解析到的连接选项。

PQconninfoOption \*PQconninfoParse(const char \*conninfo, char \*\*errmsg);

解析一个连接字符串并且将结果选项作为一个数组返回，或者在连接字符串有问题时返回NULL。这个函数可以用来抽取所提供的连接字符串中的PQconnectdb选项。返回值指向一个PQconninfoOption结构的数组，该数组以一个包含空keyword指针的条目结束。

所有合法选项将出现在结果数组中，但是任何在连接字符串中没有出现的选项的PQconninfoOption的val会被设置为NULL，默认值不会被插入。

如果errmsg不是NULL，那么成功时\*errmsg会被设置为NULL， 否则设置为被malloc过的错误字符串以说明该问题（也可以将\*errmsg设置为NULL并且函数返回NULL，这表示一种内存耗尽的情况）。

在处理完选项数组后，把它交给PQconninfoFree释放。如果没有这么做， 每次调用PQconninfoParse都会导致一小部分内存泄漏。反过来，如果发生一个错误并且errmsg不是NULL，确保使用PQfreemem释放错误字符串。

PQfinish

关闭与服务器的连接。同时释放PGconn对象使用的内存。

void PQfinish(PGconn \*conn);

注意，即使与服务器的连接尝试失败（由PQstatus指示），应用也应当调用PQfinish来释放PGconn对象使用的内存。不能在调用PQfinish之后再使用PGconn指针。

PQreset

重置与服务器的通讯通道。

void PQreset(PGconn \*conn);

此函数将关闭与服务器的连接，并且使用所有之前使用过的参数尝试重新建立与同一个服务器的连接。这可能有助于在工作连接丢失后的错误恢复。

PQresetStart

PQresetPoll

以非阻塞方式重置与服务器的通讯通道。

int PQresetStart(PGconn \*conn);

PostgresPollingStatusType PQresetPoll(PGconn \*conn);

这些函数将关闭与服务器的连接，并且使用所有之前使用过的参数尝试重新建立与同一个服务器的连接。这可能有助于在工作连接丢失后的错误恢复。它们和上面的PQreset的不同在于它们工作在非阻塞方式。这些函数受到PQconnectStartParams、PQconnectStart和PQconnectPoll相同的限制。

要发起一次连接重置，调用PQresetStart。如果它返回0，那么重置失败。如果返回1，用与使用PQresetPoll建立连接的相同方法使用PQconnectPoll重置连接。

PQpingParams

PQpingParams报告服务器的状态。它接受与PQconnectdbParams相同的连接参数。获得服务器状态不需要提供正确的用户名、口令或数据库名。不过，如果提供了不正确的值，服务器将记录一次失败的连接尝试。

PGPing PQpingParams(const char \* const \*keywords, const char \* const \*values, int expand\_dbname);

该函数返回下列值之一：

PQPING\_OK

服务器正在运行，并且看起来可以接受连接。

PQPING\_REJECT

服务器正在运行，但是处于一种不允许连接的状态（启动、关闭或崩溃恢复）。

PQPING\_NO\_RESPONSE

无法联系到服务器。这可能表示服务器没有运行，或者给定的连接参数中有些错误（例如，错误的端口号），或者有一个网络连接问题（例如，一个防火墙阻断了连接请求）。

PQPING\_NO\_ATTEMPT

没有尝试联系服务器，因为提供的参数显然不正确，或者有一些客户端问题（例如，内存用完）。

PQping

PQping报告服务器的状态。它接受与PQconnectdb相同的连接参数。获得服务器状态不需要提供正确的用户名、口令或数据库名。不过，如果提供了不正确的值，服务器将记录一次失败的连接尝试。

PGPing PQping(const char \*conninfo);

返回值和PQpingParams相同。

### 连接字符串

几个libpq函数会解析一个用户指定的字符串来获得连接参数。这些字符串有两种被接受的格式：纯关键词 = 值字符串以及URI。URI通常遵循RFC 39861，除非像下文进一步描述的那样允许多主机连接字符串。

#### 关键词/值连接字符串

在第一种格式中，每一个参数设置的形式都是关键词 = 值。等号周围的空白是可选的。要写一个空值或一个包含空白的值，将它用单引号包围，例如关键词 = 'a value'。值里面的单引号和反斜线必须用一个反斜线转义，即\\'和\\\\。

例子：

host=localhost port=5432 dbname=mydb connect\_timeout=10

#### 连接 URI

一个连接URI的一般形式是：

postgresql://\[user\[:password\]@\]\[netloc\]\[:port\]\[,...\]\[/dbname\]\[? param1=value1&...\]

URI模式标志符可以是postgresql://或postgres://。每一个URI部分都是可选的。下列例子展示了合法的URI语法：

postgresql://

postgresql://localhost

postgresql://localhost:5433

postgresql://localhost/mydb

postgresql://user@localhost

postgresql://user:secret@localhost

postgresql://other@localhost/otherdb?connect\_timeout=10&application\_name=myapp

postgresql://host1:123,host2:456/somedb?

target\_session\_attrs=any&application\_name=myapp

URI的层次部分的组件可以作为参数给出。例如：

postgresql:///mydb?host=localhost&port=5433

在任意URI部分中可以使用百分号编码来包括有特殊含义的符号，例如用%3D替换=。

任何不对应关键词的连接参数将被忽略并且关于它们的警告消息会被发送到stderr。

为了提高和JDBC连接URI的兼容性，参数ssl=true的实例会被翻译成sslmode=require。

主机部分可能是主机名或一个IP地址。要指定一个IPv6主机地址，将它封闭在方括号中：

postgresql://\[2001:db8::1234\]/database

主机组件会被按照参数host对应的描述来解释。特别地，如果主机部分是空或开始于一个斜线，将使用一个Unix域套接字连接，否则将启动一个TCP/IP连接。不过要注意，斜线是URI层次部分中的一个保留字符。因此，要指定一个非标准的Unix域套接字目录，要么忽略URI中的主机说明并且指定该主机为一个参数，要么在URI的主机部分用百分号编码路径：

postgresql:///dbname?host=/var/lib/postgresql

postgresql://%2Fvar%2Flib%2Fpostgresql/dbname

可以在一个URI中指定多个主机，每一个都有一个可选的端口。一个形式为postgresql:// host1:port1,host2:port2,host3:port3/的URI等效于host=host1,host2,host3 port=port1,port2,port3形式的连接字符串。每一个主机都将被尝试，直到成功地建立一个连接。

#### 指定多个主机

可以指定多个要连接的主机，这样它们会按给定的顺序被尝试。在键/值格式中，host、hostaddr和port选项都接受逗号分隔的值列表。在指定的每一个选项中都必须给出相同数量的元素，这样第一个hostaddr对应于第一个主机名，第二个hostaddr对应于第二个主机名，以此类推。不过，如果仅指定一个port，它将被应用于所有的主机。

在连接URI格式中，在URI的host部分我们可以列出多个由逗号分隔的host:port对。

不管是哪一种格式，单一的主机名可以被翻译成多个网络地址。常见的例子是一个主机同时具有IPv4和IPv6地址。

当多个主机被指定时或者单个主机名被翻译成多个地址时，所有的主机和地址都将按照顺序被尝试，直至遇到一个成功的。如果没有主机可以到达，则连接失败。如果成功地建立一个连接但是认证失败，也不会尝试列表中剩下的主机。

如果使用了口令文件，可以为不同的主机使用不同的口令。所有其他连接选项对列表中的每一台主机都是相同的，例如不能为不同的主机指定不同的用户名。

### 参数关键词

当前被识别的参数关键词是：

host

要连接的主机名。如果一个主机名以斜线开始，则表示一个Unix域通信而不是TCP/IP通信，其值是存储套接字文件的目录名。当host没有指定或者为空时的默认行为是连接到一个/tmp（或者瀚高数据库编译时指定的任何套接字目录）中的Unix域套接字。在没有Unix域套接字的机器上，默认是连接到localhost。

也接受由逗号分隔的主机名列表，这种情况下将依次尝试列表中的主机名，列表中的空项会选择上述的默认行为。

hostaddr

要连接的主机的数字IP地址。它应该是标准的IPv4地址格式，例如172.28.40.9。如果你的机器支持IPv6，你也可以使用那些地址。当为这个参数指定一个非空字符串时，总是会使用TCP/IP通信。

使用hostaddr代替host允许应用能避免一次主机名查找，这对于具有时间约束的应用可能非常重要。不过，GSSAPI或SSPI认证方法以及verify-full SSL 证书验证还是要求一个主机名。使用的是下列规则：

• 如果指定了host但没有hostaddr，则会发生主机名查找（在使用PQconnectPoll时，PQconnectPoll第一次考虑这个主机名时会发生查找，可能会导致PQconnectPoll阻塞可观的时间）。

• 如果hostaddr被指定且没有host，hostaddr的值给出了服务器的网络地址。如果认证方法要求一个主机名则连接尝试将会失败。

• 如果host和hostaddr都被指定，hostaddr的值给出服务器的网络地址。host的值将被忽略，除非认证方法要求它，在那种情况下它将被用作主机名。

注意如果host不是网络地址hostaddr上的服务器名，认证很可能会失败。此外，当host和hostaddr都被指定时，host被用来在口令文件中标识该连接。

逗号分隔的hostaddr值列表也被接受，这种情况下将依次尝试列表中的主机。列表中的空项会导致对应的主机名被使用，或者如果对应的主机名也为空时使用默认主机名。

如果没有一个主机名或主机地址，libpq将尝试使用一个本地Unix域套接字连接，或者在没有Unix域套接字的机器上尝试连接到localhost。

port

在服务器主机上要连接的端口号，或者用于Unix域连接的套接字文件名扩展。如果在host或hostaddr参数中给出了多个主机，这个参数可以指定一个逗号分隔的端口列表，列表长度与主机列表相同，或者这个参数可以指定一个单一的端口号用于所有的主机。空字符串或者逗号分隔列表中的空项指定的是瀚高数据库编译时建立的默认端口号。

dbname

数据库名。默认和用户名相同。在一般的环境下，会为扩展格式检查该值。

user

数据库要作为哪个用户连接。默认与运行着该应用的用户的操作系统名相同。

password

服务器要求口令认证时要使用的口令。

passfile

指定用于存放口令的文件名 libpq-c库 。默认是~/.pgpass，或者是Microsoft Windows上的%APPDATA%\\postgresql\\pgpass.conf（如果该文件不存在也不会报错）。

connect\_timeout

连接的最大等待时间，以秒为单位（写作一个十进制整数，例如10）。零、负值或者不指定表示无限等待。允许的最小超时是2秒，因此值1会被解释为2。这个超时单独应用于每个主机名或者IP地址。例如，如果指定两个主机并且connect\_timeout为5，每个主机都会在5秒内没有建立起连接的情况下超时，因此花费在等待连接上的总时间可能高达10秒。

client\_encoding

为连接设置client\_encoding配置参数。除了被相应服务器选项所接受的值，你还能使用auto从客户端的当前区域（Unix 系统上的LC\_CTYPE环境变量）决定正确的编码。

options

指定在连接开始时发送给服务器的命令行选项。例如，设置这个参数为-c geqo=off会把会话的geqo参数值设置为off。这个字符串中的空格被认为是命令行参数的分隔符，除非用一个反斜线（\\）对它转义，用\\\\可以表示一个字面意义上的反斜线。可用选项的详细讨论请参考 SQL命令 。

application\_name

为application\_name配置参数指定一个值。

fallback\_application\_name

为application\_name配置参数指定一个后补值。如果通过一个连接参数或PGAPPNAME环境变量没有为application\_name给定一个值，将使用这个值。在希望设置一个默认应用名但不希望它被用户覆盖的一般工具程序中指定一个后补值很有用。

keepalives

控制是否使用客户端的TCP保持存活机制。默认值是1，表示打开。但是如果不想要保持存活机制，你可以改成0表示关闭。对于通过一个Unix域套接字建立的连接会忽略这个参数。

keepalives\_idle

控制非活动多少秒之后TCP应该向服务器发送一个存活消息。零值表示使用系统默认值。对于一个通过Unix域套接字建立的连接将忽略这个参数，如果保持存活机制被禁用也将忽略这个参数。它只被TCP\_KEEPIDLE或等效的套接字选项可用的系统以及Windows支持，在其他系统上，它没有效果。

keepalives\_interval

控制一个TCP存活消息没有被服务器认可多少秒之后应该被重传。零值表示使用系统默认值。对于一个通过Unix域套接字建立的连接将忽略这个参数，如果保持存活机制被禁用也将忽略这个参数。它只被TCP\_KEEPINTVL或等效的套接字选项可用的系统以及Windows支持，在其他系统上，它没有效果。

keepalives\_count

控制该客户端到服务器的连接被认为死亡之前可以丢失的TCP存活消息数量。零值表示使用系统默认值。对于一个通过Unix域套接字建立的连接将忽略这个参数，如果保持存活机制被禁用也将忽略这个参数。它只被TCP\_KEEPCNT或等效的套接字选项可用的系统以及Windows支持，在其他系统上，它没有效果。

tcp\_user\_timeout

在强制关闭连接之前，控制传输数据的毫秒数可能保持未确认。值为零使用系统默认值。对于通过Unix域套接字进行的连接，将忽略此参数。它仅在TCP\_USER\_TIMEOUT可用的系统上支持；对其他系统，它没有任何影响。

tty

被忽略（之前，这指定向哪里发送服务器调试输出）。

replication

这个选项决定是否该连接应该使用复制协议而不是普通协议。这是瀚高数据库的复制连接以及pg\_basebackup之类的工具在内部使用的协议，但也可以被第三方应用使用。

支持下列值，大小写无关：

true、on、yes、1

连接进入到物理复制模式。

database

连接进入到逻辑复制模式，连接到dbname参数中指定的数据库。

false、off、no、0

该连接是一个常规连接，这是默认行为。

在物理或者逻辑复制模式中，仅能使用简单查询协议。

gssencmode

此选项确定是否与服务器协商安全GSS TCP/IP 连接是否或具有什么优先级。有三种模式:

disable

仅尝试非GSSAPI加密的连接。

prefer (default)

如果存在GSSAPI凭据（即凭据缓存中），先尝试GSSAPI加密连接; 如果失败或没有凭据，则尝试非GSSAPI加密连接。 当已使用GSSAPI支持编译时，这是默认值。

require

仅尝试GSSAPI加密连接。

对于Unix域套接字通信，gssencmode被忽略。如果瀚高数据库是在没有GSSAPI支持的情况下编译的，使用require选项将导致错误，而prefer将被接受，但libpq实际上不会尝试GSSAPI加密连接。

sslmode

这个选项决定一个SSL TCP/IP连接是否将与服务器协商，或者决定以何种优先级协商。有六种模式：disable只尝试非SSL连接

allow

首先尝试非SSL连接，如果失败再尝试SSL连接

prefer（默认）

首先尝试SSL连接，如果失败再尝试非SSL连接

require

只尝试SSL连接。如果存在一个根CA文件，以verify-ca被指定的相同方式验证该证书

verify-ca

只尝试SSL连接，并且验证服务器证书是由一个可信的证书机构颁发的（CA）

verify-full

只尝试SSL连接，验证服务器证书是由一个可信的CA颁发并且请求的服务器主机名匹配证书中的主机名对于 Unix 域套接字通信，sslmode会被忽略。如果瀚高数据库被编译为不带 SSL 支持，使用选项require、verify-ca或verify-full将导致错误，而选项allow和prefer将会被接受但是libpq将不会真正尝试SSL连接。

requiressl

为了支持sslmode模式，这个选项已被废弃。

如果设置为 1，则要求一个到服务器的SSL连接（这等效于sslmode require）。如果服务器不接受SSL连接，libpq则将拒绝连接。如果设置为0（默认），libpq将与该服务器协商连接类型（等效于sslmode prefer）。只有瀚高数据库被编译为带有SSL支持，这个选项才可用。

sslcompression

如果设置为1，通过SSL连接发送的数据将被压缩。如果设置为0，压缩将被禁用。默认值为0。如果建立的连接没有使用SSL，则这个参数会被忽略。

现如今SSL压缩被认为是不安全的，因此已经不再推荐使用。OpenSSL 1.1.0默认禁用压缩，并且很多操作系统发行版在前面的版本中也将其禁用，因此如果服务器不接受压缩，将这个参数设置为on不会有任何效果。另一方面，1.0.0之前的OpenSSL不支持禁用压缩，因此对那些版本来说会忽略这个参数，而是否使用压缩取决于服务器。

如果安全性不是主要考虑的问题，在网络是瓶颈的情况下，压缩能够改进吞吐量。如果CPU性能是受限的因素，禁用压缩能提高响应时间和吞吐量。

sslcert

这个参数指定客户端SSL证书的文件名，它替换默认的$HGDB\_HOME/etc/server.crt。如果没有建立SSL连接，这个参数会被忽略。

sslkey

这个参数指定用于客户端证书的密钥位置。它能指定一个会被用来替代默认的$HGDB\_HOME/etc/server.key的文件名，或者它能够指定一个从外部”引擎”（引擎是OpenSSL的可载入模块）得到的密钥。一个外部引擎说明应该由一个冒号分隔的引擎名称以及一个引擎相关的关键标识符组成。如果没有建立 SSL 连接，这个参数会被忽略。

sslrootcert

这个参数指定一个包含SSL证书机构（CA）证书的文件名称。如果该文件存在，服务器的证书将被验证是由这些机构之一签发。

sslcrl

这个参数指定SSL证书撤销列表（CRL）的文件名。列在这个文件中的证书如果存在，在尝试认证该服务器证书时会被拒绝。

requirepeer

这个参数指定服务器的操作系统用户，例如requirepeer=highgo。当建立一个 Unix 域套接字连接时，如果设置了这个参数，客户端在连接开始时检查服务器进程是运行在指定的用户名之下。如果发现不是，该连接会被一个错误中断。这个参数能被用来提供与TCP/IP连接上SSL证书相似的服务器认证（注意，如果Unix 域套接字在/tmp或另一个公共可写的位置，任何用户能开始一个在那里监听的服务器。使用这个参数来保证你连接的是一个由可信用户运行的服务器）。这个选项只在实现了peer认证方法的平台上受支持。

krbsrvname

当用 GSSAPI 认证时，要使用的 Kerberos 服务名。为了让 Kerberos 认证成功，这必须匹配在服务器配置中指定的服务名。

gsslib

用于GSSAPI身份验证的GSS库。目前，除了在包含GSSAPI和SSPI支持的Windows构建中，这一点被忽略了。在这种情况下，将此设置为gssapi使 libpq 使用GSSAPI库进行身份验证，而不是默认SSPI。

service

用于附加参数的服务名。它指定保持附加连接参数的pg\_service.conf中的一个服务名。这允许应用只指定一个服务名，这样连接参数能被集中维护。

target\_session\_attrs

如果这个参数被设置为read-write，只有默认接受读写事务的连接才是可接受的。在任何成功的连接上将发出查询SHOW transaction\_read\_only，如果它返回on则连接将被关闭。如果在连接字符串中指定了多个主机，只要连接尝试失败就会尝试剩余的服务器。这个参数的默认值any认为所有连接都可接受。

## 连接状态函数

这些函数可以被用来询问一个已有数据库连接对象的状态。

| 提示： |
| --- |
| libpq应用程序员应该小心地维护PGconn抽象。使用下面描述的访问函数来 理解PGconn的内容。我们不推荐使用libpq-int.h引用内部的PGconn域，因为它们可能在未来改变。 |

下列函数返回一个连接所建立的参数值。这些值在连接的生命期中是固定的。如果使用的是多主机连接字符串，如果使用同一个PGconn对象建立新连接，PQhost、PQport以及PQpass可能会改变。其他值在PGconn对象的一生中都是固定的。

PQdb

返回该连接的数据库名。

char \*PQdb(const PGconn \*conn);

PQuser

返回该连接的用户名。

char \*PQuser(const PGconn \*conn);

PQpass

返回该连接的口令。

char \*PQpass(const PGconn \*conn);

PQpass将返回连接参数中指定的口令，如果连接参数中没有口令并且能从口令文件中得到口令，则它将返回得到的口令。在后一种情况中，如果连接参数中指定了多个主机，在连接被建立之前都不能依赖PQpass的结果。连接的状态可以用函数PQstatus检查。

PQhost

返回活跃连接的服务器主机名。可能是主机名、IP地址或者一个目录路径（如果通过Unix套接字连接，路径的情况很容易区分，因为路径总是一个绝对路径，以/开始）。

char \*PQhost(const PGconn \*conn);

如果连接参数同时指定了host和hostaddr，则PQhost将返回host信息。如果仅指定了hostaddr，则返回它。如果在连接参数中指定了多个主机，PQhost返回实际连接到的主机。

如果conn参数是NULL，则PQhost返回NULL。否则，如果有一个错误产生主机信息（或许是连接没有被完全建立或者有什么错误），它会返回一个空字符串。

如果在连接参数中指定了多个主机，则在连接建立之前都不能依赖于PQhost的结果。连接的状态可以用函数PQstatus检查。

PQhostaddr

返回活动连接的服务器 IP 地址。这可以是主机名解析出的地址，也可以是通过hostaddr参数提供的IP地址。

char \*PQhostaddr(const PGconn \*conn);

如果conn 参数为NULL则 PQhostaddr 返回NULL 。否则，如果生成主机信息时出现错误（如果连接尚未完全建立或出现错误），则返回一个空字符串。

PQport

返回活跃连接的端口。

char \*PQport(const PGconn \*conn);

如果在连接参数中指定了多个端口，PQport返回实际连接到的端口。

如果conn参数是NULL，则PQport返回NULL。否则，如果有一个错误产生端口信息（或许是连接没有被完全建立或者有什么错误），它会返回一个空字符串。

如果在连接参数中指定了多个端口，则在连接建立之前都不能依赖于PQport的结果。连接的状态可以用函数PQstatus检查。

PQtty

返回该连接的调试TTY（这已被废弃，因为服务器不再关心TTY设置，但这个函数保持了向后兼容）。

char \*PQtty(const PGconn \*conn);

PQoptions

返回被传递给连接请求的命令行选项。

char \*PQoptions(const PGconn \*conn);

下列函数返回会随着在PGconn对象上执行的操作改变的状态数据。

PQstatus

返回该连接的状态。

ConnStatusType PQstatus(const PGconn \*conn);

该状态可以是一系列值之一。不过，其中只有两个在一个异步连接过程之外可见：CONNECTION\_OK和CONNECTION\_BAD。一个到数据库的完好连接的状态

为CONNECTION\_OK。一个失败的连接尝试则由状态CONNECTION\_BAD表示。通常，一个OK状态将一直保持到PQfinish，但是一次通信失败可能导致该状态过早地改变为CONNECTION\_BAD。在那种情况下，该应用可以通过调用PQreset尝试恢复。

关于其他可能会被返回的状态代码，请见PQconnectStartParams、PQconnectStart和PQconnectPoll的条目。

PQtransactionStatus

返回服务器的当前事务内状态。

PGTransactionStatusType PQtransactionStatus(const PGconn \*conn);

该状态可能是PQTRANS\_IDLE（当前空闲）、PQTRANS\_ACTIVE（一个命令运行中）、PQTRANS\_INTRANS（空闲，处于一个合法的事务块中）或者PQTRANS\_INERROR（空闲，处于一个失败的事务块中）。如果该连接损坏，将会报告PQTRANS\_UNKNOWN。只有当一个查询已经被发送给服务器并且还没有完成时，才会报告PQTRANS\_ACTIVE。

PQparameterStatus

查找服务器的一个当前参数设置。

const char \*PQparameterStatus(const PGconn \*conn, const char \*paramName);

某一参数值会被服务器在连接开始或值改变时自动报告。PQparameterStatus可以被用来询问这些设置。它为已知的参数返回当前值，为未知的参数返回NULL。

自当前发布开始会被报告的参数包括server\_version、server\_encoding、client\_encoding、application\_name、is\_superuser、session\_authorization、DateStyle、IntervalStyle、TimeZone、integer\_datetimes以及 standard\_conforming\_strings（server\_encoding、TimeZone以及integer\_datetimes在以前的发布中不被报告；standard\_conforming\_strings在以前的发布中不被报告；IntervalStyle在以前的发布中不被报告；application\_name在以前的发布中不被报告）。注意server\_version、server\_encoding以及 integer\_datetimes在启动之后无法改变。

3.0 之前协议的服务器不报告参数设置，但是libpq包括获得server\_version以及client\_encoding值的逻辑。我们鼓励应用使用PQparameterStatus而不是ad hoc代码来确定这些值（不过注意在一个3.0之前的连接上，连接开始后通过SET改变client\_encoding不会被PQparameterStatus反映）。对于server\_version（另见PQserverVersion），它以一种数字形式返回信息，这样更容易进行比较。

如果没有为standard\_conforming\_strings报告值，应用能假设它是off，也就是说反斜线会被视为字符串中的转义。还有，这个参数的存在可以被作为转义字符串语法（E'...'）被接受的指示。

尽管被返回的指针被声明成const，它事实上指向与PGconn结构相关的可变存储。假定该指针在存储之间保持有效是不明智的。

PQprotocolVersion

询问所使用的 前端/后端协议。

int PQprotocolVersion(const PGconn \*conn);

应用可能希望用这个函数来确定某些特性是否被支持。当前，可能值是2（2.0 协议）、3（3.0协议）或零（连接损坏）。协议版本在连接启动完成后将不会改变，但是理论上在连接重置期间是可以改变的。与瀚高数据库服务器通信时通常使用3.0协议。

PQserverVersion

返回一个表示服务器版本的整数。

int PQserverVersion(const PGconn \*conn);

应用可能会使用这个函数来判断它们连接到的数据库服务器的版本。结果通过将服务器的主版本号乘以10000再加上次版本号形成。

因此，出于判断特性兼容性的目的，应用应该将PQserverVersion的结果除以100而不是10000来判断逻辑的主版本号。在所有的发行序列中，只有最后两个数字在次发行（问题修正发行）之间不同。

PQerrorMessage

返回连接上的一个操作最近产生的错误消息。

char \*PQerrorMessage(const PGconn \*conn);

几乎所有的libpq在失败时都会为PQerrorMessage设置一个消息。注意按照libpq习惯，一个非空PQerrorMessage结果由多行构成，并且将包括一个尾部新行。调用者不应该直接释放结果。当相关的PGconn句柄被传递给PQfinish时，它将被释放。在PGconn结构上的多个操作之间，不能指望结果字符串会保持不变。

PQsocket

获得到服务器连接套接字的文件描述符号。一个合法的描述符将会大于等于零。结果为-1表示当前没有打开服务器连接（在普通操作期间这将不会改变，但是在连接设置或重置期间可能改变）。

int PQsocket(const PGconn \*conn);

PQbackendPID

返回处理这个连接的后端进程的进程ID（PID）。

int PQbackendPID(const PGconn \*conn);

后端PID有助于调试目的并且可用于与NOTIFY消息（它包括发出提示的后端进程的PID）进行比较。注意PID属于一个在数据库服务器主机上执行的进程，而不是本地主机进程！

PQconnectionNeedsPassword

如果连接认证方法要求一个口令但没有可用的口令，返回真（1）。否则返回假（0）。

int PQconnectionNeedsPassword(const PGconn \*conn);

这个函数可以在连接尝试失败后被应用于决定是否向用户提示要求一个口令。

PQconnectionUsedPassword

如果连接认证方法使用一个口令，返回真（1）。否则返回假（0）。

int PQconnectionUsedPassword(const PGconn \*conn);

这个函数能在一次连接尝试失败或成功后用于检测该服务器是否要求一个口令。

下面的函数返回与SSL有关的信息。这些信息在连接建立后通常不会改变。

PQsslInUse

如果该连接使用了SSL则返回真（1），否则返回假（0）。

int PQsslInUse(const PGconn \*conn);

PQsslAttribute

返回关于该连接的有关SSL的信息。

const char \*PQsslAttribute(const PGconn \*conn, const char \*attribute\_name);

可用的属性列表取决于使用的SSL库以及连接类型。如果一个属性不可用，会返回NULL。

下列属性通常是可用的：

library

正在使用的SSL实现的名称（当前只实现了"OpenSSL"）

protocol

正在使用的SSL/TLS版本。常见的值有"TLSv1"、 "TLSv1.1"以及"TLSv1.2"，但是如果 一种实现使用了其他协议，可能返回其他字符串。

key\_bits

加密算法所使用的密钥位数。

cipher

所使用的加密套件的简短名称，例如"DHE-RSA-DES-CBC3-SHA"。这些名称与每一种SSL实现相关。

compression

如果正在使用SSL压缩，则返回压缩算法的名称。如果使用了压缩但是算法未知则返回"on"。如果没有使用压缩，则返回"off"。

PQsslAttributeNames

返回一个可用的SSL名称的数组。该数组以一个NULL指针终结。

const char \* const \* PQsslAttributeNames(const PGconn \*conn);

PQsslStruct

返回一个描述该连接的SSL实现相关的对象指针。

void \*PQsslStruct(const PGconn \*conn, const char \*struct\_name);

可用的结构，这些结构取决于使用的SSL实现。对于OpenSSL，有一个结构可用，其名称为"OpenSSL"。它返回一个指向该OpenSSL SSL结构的指针。要使用这个函数，可以用下面的代码：

#include <libpq-fe.h>

#include <openssl/ssl.h>

...

SSL \*ssl;

dbconn = PQconnectdb(...);

...

ssl = PQsslStruct(dbconn, "OpenSSL");

if (ssl)

{

/\* 使用 OpenSSL 函数来访问 ssl \*/

}

这个结构可以被用来验证加密级别、检查服务器证书等等。有关这个结构 的信息请参考OpenSSL的文档。

PQgetssl

返回连接中使用的SSL结构，如果没有使用SSL则返回空。

void \*PQgetssl(const PGconn \*conn);

这个函数等效于PQsslStruct(conn, "OpenSSL")。在新的应用中不应该使用它，因为被返回的结构是OpenSSL专用的，如果使用了另一种SSL实现就不再可用。要检查一个连接是否使用SSL，应该调用PQsslInUse，而要得到有关连接的更多细节应该使用PQsslAttribute。

## 命令执行函数

一旦到一个数据库服务器的连接被成功建立，这里描述的函数可以被用来执行 SQL 查询和命令。

### 主要函数

PQexec

提交一个命令给服务器并且等待结果。

PGresult \*PQexec(PGconn \*conn, const char \*command);

返回一个PGresult指针或者可能是一个空指针。除了内存不足的情况或者由于严重错误无法将命令发送给服务器之外，一般都会返回一个非空指针。PQresultStatus函数应当被调用来检查返回值是否代表错误（包括空指针的值，它会返回PGRES\_FATAL\_ERROR）。用PQerrorMessage可得到关于那些错误的详细信息。

命令字符串可以包括多个SQL命令（用分号分隔）。在一次PQexec调用中被发送的多个查询会在一个事务中处理，除非其中有显式的BEGIN/COMMIT命令将该查询字符串划分成多个事务。但是注意，返回的PGresult结构只描述该字符串中被执行的最后一个命令的结果。如果一个命令失败，该字符串的处理会在它那里停止并且返回的PGresult会描述错误情况。

PQexecParams

提交一个命令给服务器并且等待结果，它可以在SQL命令文本之外独立地传递参数。

PGresult \*PQexecParams(PGconn \*conn,

const char \*command,

int nParams,

const Oid \*paramTypes,

const char \* const \*paramValues,

const int \*paramLengths,

const int \*paramFormats,

int resultFormat);

PQexecParams与PQexec相似，但是提供了额外的功能：参数值可以与命令字符串分开指定，并且可以以文本或二进制格式请求查询结果。PQexecParams只在 3.0 协议及其后的连接中被支持，当使用2.0协议时它会失败。

该函数的参数是：

conn

要在其中发送命令的连接对象。

command

要执行的SQL命令字符串。如果使用了参数，它们在该命令字符串中被引用为$1、$2等。

nParams

提供的参数数量。它是数组paramTypes\[\]、paramValues\[\]、paramLengths\[\]和paramFormats\[\]的长度（当nParams为零时，数组指针可以是NULL）。

paramTypes\[\]

通过OID指定要赋予给参数符号的数据类型。如果paramTypes为NULL或者该数组中任何特定元素为零，服务器会用对待未知类型文字串的方式为参数符号推测一种数据类型。

paramValues\[\]

指定参数的实际值。这个数组中的一个空指针表示对应的参数为空，否则该指针指向一个以零终止的文本字符串（用于文本格式）或者以服务器所期待格式的二进制数据（用于二进制格式）。

paramLengths\[\]

指定二进制格式参数的实际数据长度。它对空参数和文本格式参数被忽略。当没有二进制参数时，该数组指针可以为空。

paramFormats\[\]

指定参数是否为文本（在参数相应的数组项中放一个零）或二进制（在参数相应的数组项中放一个一）。如果该数组指针为空，那么所有参数都会被假定为文本串。

以二进制格式传递的值要求后端所期待的内部表示形式的知识。例如，整数必须以网络字节序被传递。传递numeric值要求关于服务器存储格式的知识，正如src/ backend/utils/adt/numeric.c::numeric\_send()以及src/backend/utils/adt/numeric.c::numeric\_recv()中所实现的。

resultFormat

指定零来得到文本格式的结果，或者指定一来得到二进制格式的结果（目前没有规定要求以不同格式得到不同的结果列，尽管在底层协议中这是可以实现的）。

PQexecParams相对于PQexec的主要优点是参数值可以从命令串中分离，因此避免了冗长的书写、容易发生错误的引用以及转义。

和PQexec不同，PQexecParams至多允许在给定串中出现一个SQL命令（其中可以有分号，但是不能有超过一个非空命令）。这是底层协议的一个限制，但是有助于抵抗SQL注入攻击。

| 提示： |
| --- |
| 通过OID指定参数类型很罗嗦，特别是如果你不愿意将特定的OID值硬编码到你的程序中时。不过，即使服务器本身也无法确定参数的类型，你可以避免这样做，或者选择一种与你想要的不同的类型。在SQL 命令文本中，附加一个显式造型给参数符号来表示你将发送什么样的数据类型。例如：SELECT \* FROM mytable WHERE x = $1::bigint; 这强制参数$1被当作bigint，而默认情况下它将被赋予与x相同的类型。当以二进制格式发送参数值时，我们强烈推荐以这种方式或通过指定一个数字类型的OID来强制参数类型决定。因为二进制格式比文本格式具有更少的冗余，并且因此服务器将不会有更多机会为你检测一个类型匹配错误。 |

PQprepare

提交一个请求用给定参数创建一个预备语句并且等待完成。

PGresult \*PQprepare(PGconn \*conn, const char \*stmtName, const char \*query, int nParams, const Oid \*paramTypes);

PQprepare创建一个后面会由PQexecPrepared执行的预备语句。这个特性允许命令被反复执行而无需每次都进行解析和规划，详见PREPARE。PQprepare只在协议 3.0 及之后的连接中被支持，当使用协议 2.0 时它将失败。

该函数从query串创建一个名为stmtName的预备语句，该串必须包含一个单一 SQL 命令。stmtName可以是""来创建一个未命名语句，在这种情况下任何已存在未命名语句将被自动替换。如果语句名称已经在当前会话中被定义，则是一种错误。如果使用了任何参数，它们在查询中以$1、$2等引用。nParams是参数的个数，其类型在数组paramTypes\[\]中被预先指定（当nParams为零时，该数组指针可以是NULL）。paramTypes\[\]通过OID指定要赋予给参数符号的数据类型。如果paramTypes是NULL或者该数组中任何特定元素为零，服务器会用对待未知类型文字串的方式为参数符号推测一种数据类型。还有，查询能够使用编号高于nParams的参数符号，它们的数据类型也会被自动推测（找出推测出的数据类型的方法见PQdescribePrepared）。

正如PQexec一样，结果通常是一个PGresult对象，其内容代表服务器端成功或失败。一个空结果表示内存不足或者根本无法发送命令。关于错误的更多信息请见PQerrorMessage。

用于PQexecPrepared的预备语句也能通过执行SQL PREPARE语句来创建。还有，尽管没有libpq函数来删除一个预备语句，SQL DEALLOCATE语句可被用于此目的。

PQexecPrepared

发送一个请求来用给定参数执行一个预备语句，并且等待结果。

PGresult \*PQexecPrepared(PGconn \*conn, const char \*stmtName, int nParams, const char \* const \*paramValues, const int \*paramLengths, const int \*paramFormats, int resultFormat);

PQexecPrepared像PQexecParams，但是要被执行的命令是用之前准备的语句的名字指定，而不是指定一个查询串。这个特性允许将被重复使用的命令只被解析和规划一次，而不是在每次被执行时都被解析和规划。这个语句必须之前在当前会话中已经被准备好。PQexecPrepared仅被协议3.0及之后的连接支持，当使用协议2.0时它会失败。

参数和PQexecParams相同，除了给定的是一个预备语句的名称而不是一个查询语句，以及不存在paramTypes\[\]参数（因为预备语句的参数类型已经在它被创建时决定好了）。

PQdescribePrepared

提交一个请求来获得有关指定预备语句的信息，并且等待完成。

PGresult \*PQdescribePrepared(PGconn \*conn, const char \*stmtName);

PQdescribePrepared允许一个应用获得有关一个之前预备好的语句的信息。PQdescribePrepared仅被协议3.0及之后的连接支持，当使用协议2.0时它会失败。

stmtName可以用""或者NULL来引用未命名语句，否则它必须是一个现有预备语句的名字。如果成功，一个PGresult以及状态PGRES\_COMMAND\_OK会被返回。函数PQnparams和PQparamtype可以被应用到这个PGresult来得到关于该预备语句参数的额信息，而函数PQnfields、PQfname、PQftype等提供该语句结果列（如果有）的信息。

PQdescribePortal

提交一个请求来得到有关指定入口的信息，并且等待完成。

PGresult \*PQdescribePortal(PGconn \*conn, const char \*portalName);

PQdescribePortal允许一个应用获得有关一个之前被创建的入口的信息（libpq不提供对入口任何直接的访问，但是你可以使用这个函数来观察一个通过DECLARE CURSOR SQL命令创建的游标的属性）。PQdescribePortal仅被协议3.0 及之后的连接支持，当使用协议2.0时它会失败。

portalName可以用""或者NULL来引用未命名入口，否则它必须是一个现有入口的名字。如果成功，一个PGresult和状态PGRES\_COMMAND\_OK会被返回。函数PQnfields、PQfname、PQftype等可以被应用到PGresult来获得有关该入口结果列（如果有）的信息。

PGresult结构封装了由服务器返回的结果。libpq应用程序员应该小心地维护PGresult的抽象。使用下面的存储器函数来得到PGresult的内容。避免直接引用PGresult结构的域，因为它们可能在未来更改。

PQresultStatus

返回该命令的结果状态。

ExecStatusType PQresultStatus(const PGresult \*res);

PQresultStatus能返回下列值之一：

PGRES\_EMPTY\_QUERY

发送给服务器的字符串为空。

PGRES\_COMMAND\_OK

一个不返回数据的命令成功完成。

PGRES\_TUPLES\_OK

一个返回数据的命令（例如SELECT或者SHOW）成功完成。

PGRES\_COPY\_OUT

从服务器复制出数据的传输开始。

PGRES\_COPY\_IN

复制数据到服务器的传输开始。

PGRES\_BAD\_RESPONSE

无法理解服务器的响应。

PGRES\_NONFATAL\_ERROR

发生了一次非致命错误（一个提示或警告）。

PGRES\_FATAL\_ERROR

发生了一次致命错误。

PGRES\_COPY\_BOTH

向服务器复制数据/从服务器复制数据的传输开始。这个特性当前只被用于流复制，因此这个状态应该不会在普通应用中出现。

PGRES\_SINGLE\_TUPLE

PGresult包含来自于当前命令的一个单一结果元组。这个状态只在查询选择了单一行模式时发生。

如果结果状态是PGRES\_TUPLES\_OK或者PGRES\_SINGLE\_TUPLE，那么下面所描述的函数能被用来检索该查询所返回的行。注意，一个恰好检索零行的SELECT命令仍然会显示PGRES\_TUPLES\_OK。PGRES\_COMMAND\_OK用于从不返回行的命令（不带RETURNING子句的INSERT或者UPDATE等）。一个PGRES\_EMPTY\_QUERY可能表示客户端软件中的一个缺陷。

一个状态为PGRES\_NONFATAL\_ERROR的结果将不会被PQexec或者其他查询执行函数直接返回，这类结果将被传递给提示处理器。

PQresStatus

将PQresultStatus返回的枚举转换成描述状态编码的字符串常量。调用者不应该释放结果。

char \*PQresStatus(ExecStatusType status);

PQresultErrorMessage

返回与该命令相关的错误消息，如果有错误则会返回一个空字符串。

char \*PQresultErrorMessage(const PGresult \*res);

如果有一个错误，被返回的字符串将包含一个收尾的新行。调用者不应该直接释放结果。它将在相关的PGresult句柄被传递给PQclear之后被释放。

紧跟着一个PQexec或PQgetResult调用，PQerrorMessage（在连接上）将返回与PQresultErrorMessage相同的字符串（在结果上）。不过，一个PGresult将保持它的错误消息直到被销毁，而连接的错误消息将在后续操作被执行时被更改。当你想要知道与一个特定PGresult相关的状态，使用PQresultErrorMessage。而当你想要知道连接上最后一个操作的状态，使用PQerrorMessage。

PQresultVerboseErrorMessage

返回与PGresult对象相关的错误消息的重新格式化的版本。

char \*PQresultVerboseErrorMessage(const PGresult \*res, PGVerbosity verbosity, PGContextVisibility show\_context);

在有些情况下，客户端可能希望得到之前报告过的错误的更加详尽的版本。如果在产生给定PGresult的连接上 verbosity 设置有效，PQresultVerboseErrorMessage会通过计算已经被PQresultErrorMessage产生过的消息来满足这种需求。如果PGresult不是一个错误结果，则会报告”PGresult is not an error result”。返回的字符串包括一个新行作为结尾。

和大部分从PGresult中提取数据的其他函数不同，这个函数的结果是一个全新分配的字符串。调用者在不需要这个字符串以后，必须使用PQfreemem()释放它。

如果内存不足，可能会返回 NULL。

PQresultErrorField

返回一个错误报告的一个域。

char \*PQresultErrorField(const PGresult \*res, int fieldcode);

fieldcode是一个错误域标识符，见下列符号。如果PGresult不是一个错误或者警告结果或者不包括指定域，会返回NULL。域通常不包括一个收尾的新行。调用者不应该直接释放结果。它将在相关的PGresult句柄被传递给PQclear之后被释放。

下列域代码可用：

PG\_DIAG\_SEVERITY

严重性。域的内容是ERROR、FATAL或PANIC（在一个错误消息中）。或者是WARNING、NOTICE、DEBUG、INFO或LOG（在一个提示消息中）。或者是其中之一的一个本地化翻译。总是存在。

PG\_DIAG\_SEVERITY\_NONLOCALIZED

域的内容是ERROR、FATAL或PANIC（在一个错误消息中）。或者是WARNING、NOTICE、DEBUG、INFO或LOG（在一个提示消息中）。这和PG\_DIAG\_SEVERITY域相同，不过内容不会被本地化。

PG\_DIAG\_SQLSTATE

用于错误的SQLSTATE代码。SQLSTATE代码标识了已经发生的错误的类型，它可以被前端应用用来执行特定操作（例如错误处理）来响应一个特定数据库错误。这个域无法被本地化，并且总是存在。

PG\_DIAG\_MESSAGE\_PRIMARY

主要的人类可读的错误消息（通常是一行）。总是存在。

PG\_DIAG\_MESSAGE\_DETAIL

细节：一个可选的次级错误消息，它携带了关于问题的等多细节。可能有多行。PG\_DIAG\_MESSAGE\_HINT

提示：一个关于如何处理该问题的可选建议。它与细节的区别在于它提供了建议（可能不合适）而不是铁的事实。可能有多行。

PG\_DIAG\_STATEMENT\_POSITION

包含一个十进制整数的字符串，它表示一个错误游标位置，该位置是原始语句字符串的索引。第一个字符的索引是 1，位置以字符计算而不是以及字节计算。

PG\_DIAG\_INTERNAL\_POSITION

这被定义为与PG\_DIAG\_STATEMENT\_POSITION域相同，但是它被用在游标位置引用一个内部产生的命令而不是客户端提交的命令时。当这个域出现时，PG\_DIAG\_INTERNAL\_QUERY域将总是出现。

PG\_DIAG\_INTERNAL\_QUERY

一个失败的内部产生的命令的文本。例如，这可能是由一个PL/pgSQL函数发出的 SQL 查询。

PG\_DIAG\_CONTEXT

指示错误发生的环境。当前这包括活动过程语言函数的调用栈追踪以及内部生成的查询。追踪是每行一项，最近的排在最前面。

PG\_DIAG\_SCHEMA\_NAME

如果错误与某个特定的数据库对象相关，这里是包含该对象的模式名（如果有）。

PG\_DIAG\_TABLE\_NAME

如果错误与某个特定表相关，这里是该表的名字（该表的模式参考模式名域）。

PG\_DIAG\_COLUMN\_NAME

如果错误与一个特定表列相关，这里是该表列的名字（参考模式和表名域来标识该表）。

PG\_DIAG\_DATATYPE\_NAME

如果错误与一个特定数据类型相关，这里是该数据了行的名字（该数据类型的模式名参考模式名域）。

PG\_DIAG\_CONSTRAINT\_NAME

如果错误与一个特定约束相关，这里是该约束的名字。相关的表或域参考上面列出的域（为了这个目的，索引也被视作约束，即使它们不是用约束语法创建的）。

PG\_DIAG\_SOURCE\_FILE

报告错误的源代码所在的文件名。

PG\_DIAG\_SOURCE\_LINE

报告错误的源代码行号。

PG\_DIAG\_SOURCE\_FUNCTION

报告错误的源代码函数的名字。

| 注意： |
| --- |
| 用于模式名、表名、列名、数据类型名和约束名的域只提供给有限的错误。类型，见附录A。不要假定任何这些域的存在保证另一个域的存在。核心错误源会遵守上面提到的内在联系，但是用户定义的函数可能以其他方式使用这些域。同样地，不要假定这些域代表当前数据库中同类的对象。 |

客户端负责格式化显示信息来迎合它的需要，特别是根据需要打断长的行。出现在错误消息域中的新行字符应该被当作分段而不是换行。

libpq内部产生的错误将有严重和主要消息，但是通常没有其他域。3.0协议之前的服务器返回的错误将包括严重和主要消息，并且有时候还有细节消息，但是没有其他域。

注意错误与只从PGresult对象中有效，对PGconn对象无效。没有PQerrorField函数。

PQclear

Frees the storage associated with a 释放与一个PGresult相关的存储。每一个命令结果不再需要时应该用PQclear释放。

void PQclear(PGresult \*res);

你可以按照需要保留PGresult对象，当你发出一个新命令时它也不会消失，甚至关闭连接时也不会消失。要去掉它，你必须调用PQclear。没有这样做将会导致在应用中的内存泄露。

### 检索查询结果信息

这些函数被用来从一个代表成功查询结果（也就是状态为PGRES\_TUPLES\_OK或者PGRES\_SINGLE\_TUPLE）的PGresult对象中抽取信息。它们也可以被用来从一个成功的Describe操作中抽取信息：一个Describe的结果具有和该查询被实际执行所提供的完全相同的列信息，但是它没有行。对于其他状态值的对象，这些函数会认为结果具有零行和零列。

PQntuples

返回查询结果中的行（元组）数（注意，PGresult对象被限制为不超过INT\_MAX行，因此一个int结果就足够了）。

int PQntuples(const PGresult \*res);

PQnfields

返回查询结果中每一行的列（域）数。

int PQnfields(const PGresult \*res);

PQfname

返回与给定列号相关联的列名。列号从0开始。调用者不应该直接释放该结果。它将在相关的PGresult句柄被传递给PQclear之后被释放。

char \*PQfname(const PGresult \*res, int column\_number);

如果列号超出范围，将返回NULL。

PQfnumber

返回与给定列名相关联的列号。

int PQfnumber(const PGresult \*res, const char \*column\_name);

如果给定的名字不匹配任何列，将返回 -1。

给定的名称被视作一个SQL命令中的一个标识符，也就是说，除非被双引号引用，它是小写形式的。例如，给定一个SQL命令：

SELECT 1 AS FOO, 2 AS "BAR";

我们将得到结果：

PQfname(res, 0) foo

PQfname(res, 1) BAR

PQfnumber(res, "FOO") 0

PQfnumber(res, "foo") 0

PQfnumber(res, "BAR") -1

PQfnumber(res, "\\"BAR\\"") 1

PQftable

返回给定列从中取出的表的OID。列号从0开始。

Oid PQftable(const PGresult \*res, int column\_number);

如果列号超出范围或者指定的列不是对一个表列的简单引用或者在使用3.0协议时，返回InvalidOid。你可以查询系统表pg\_class来确定究竟是哪个表被引用。

当你包括libpq头文件，类型oid以及常数InvalidOid将被定义。它们将都是某种整数类型。

PQftablecol

返回构成指定查询结果列的列（在其表中）的列号。查询结果列号从0开始，但是表列具有非零编号。

int PQftablecol(const PGresult \*res, int column\_number);

如果列号超出范围或者指定的列不是对一个表列的简单引用或者在使用3.0协议时，返回零。

PQfformat

返回指示给定列格式的格式编码。列号从0开始。

int PQfformat(const PGresult \*res, int column\_number);

格式代码零指示文本数据表示，而格式代码一表示二进制表示（其他代码被保留用于未来的定义）。

PQftype

返回与给定列号相关联的数据类型。被返回的整数是该类型的内部OID号。列号从0开始。

Oid PQftype(const PGresult \*res, int column\_number);

你可以查询系统表pg\_type来得到多个数据类型的名字和属性。内建数据类型的OID被定义在源代码树中的文件src/include/catalog/pg\_type\_d.h中。

PQfmod

返回与给定列号相关联的列的修饰符类型。列号从 0 开始。

int PQfmod(const PGresult \*res, int column\_number);

修饰符值的解释是与类型相关的，它们通常指示精度或尺寸限制。值-1被用来指示”没有信息可用”。大部分的数据类型不适用修饰符，在那种情况中值总是 -1。

PQfsize

返回与给定列号相关的列的尺寸（以字节计）。列号从0开始。

int PQfsize(const PGresult \*res, int column\_number);

PQfsize返回在一个数据库行中为这个列分配的空间，换句话说是服务器对该数据类型的内部表示的尺寸（因此，它对客户端并不是真地非常有用）。一个负值指示该数据类型是变长的。

PQbinaryTuples

如果PGresult包含二进制数据，返回1。如果包含的是文本数据，返回0。

int PQbinaryTuples(const PGresult \*res);

这个函数已经被废弃（除了与COPY一起使用），因为一个单一PGresult可以在某些列中包含文本数据而且在另一些列中包含二进制数据。PQfformat要更好。只有结果的所有列是二进制（格式1）时PQbinaryTuples才返回 1。

PQgetvalue

返回一个PGresult的一行的单一域值。行和列号从0开始。调用者不应该直接释放该结果。它将在相关的PGresult句柄被传递给PQclear之后被释放。

char \*PQgetvalue(const PGresult \*res, int row\_number, int column\_number);

对于文本格式的数据，PQgetvalue返回的值是该域值的一种空值结束的字符串表示。对于二进制格式的数据，该值是由该数据类型的typsend和typreceive函数决定的二进制表示（在这种情况下该值实际上也跟随着一个零字节，但是这通常没有用处，因为该值很可能包含嵌入的空）。

如果该域值为空，则返回一个空串。关于区分空值和空字符串值请见PQgetisnull。

PQgetvalue返回的指针指向作为PGresult结构一部分的存储。我们不应该修改它指向的数据，并且如果要在超过PGresult结构本身的生命期之外使用它，我们必须显式地把该数据拷贝到其他存储中。

PQgetisnull

测试一个域是否为空值。行号和列号从0开始。

int PQgetisnull(const PGresult \*res, int row\_number, int column\_number);

如果该域是空，这个函数返回1。如果它包含一个非空值，则返回0（注意PQgetvalue将为一个空域返回一个空串，不是一个空指针）。

PQgetlength

返回一个域值的真实长度，以字节计。行号和列号从0开始。

int PQgetlength(const PGresult \*res, int row\_number, int column\_number);

这是特定数据值的真实数据长度，也就是PQgetvalue指向的对象的尺寸。对于文本数据格式，这和strlen()相同。对于二进制格式这是基本信息。注意我们不应该依赖于PQfsize来得到真值的数据长度。

PQnparams

返回一个预备语句的参数数量。

int PQnparams(const PGresult \*res);

只有在查看PQdescribePrepared的结果时，这个函数才有用。对于其他类型的查询，它将返回零。

PQparamtype

返回所指示的语句参数的数据类型。参数号从0开始。

Oid PQparamtype(const PGresult \*res, int param\_number);

只有在查看PQdescribePrepared的结果时，这个函数才有用。对于其他类型的查询，它将返回零。

PQprint

将所有的行打印到指定的输出流，以及有选择地将列名打印到指定的输出流。

void PQprint(FILE \*fout, /\* 输出流 \*/

const PGresult \*res,

const PQprintOpt \*po);

typedef struct

{

pqbool header; /\* 打印输出域标题和行计数 \*/

pqbool align; /\* 填充对齐域 \*/

pqbool standard; /\* 旧的格式 \*/

pqbool html3; /\* 输出 HTML 表格 \*/

pqbool expanded; /\* 扩展表格 \*/

pqbool pager; /\* 如果必要为输出使用页 \*/

char \*fieldSep; /\* 域分隔符 \*/

char \*tableOpt; /\* 用于 HTML 表格元素的属性 \*/

char \*caption; /\* HTML 表格标题 \*/

char \*\*fieldName; /\* 替换域名称的空终止数组 \*/

} PQprintOpt;

这个函数以前被psql用来打印查询结果，但是现在不是这样了。注意它假定所有的数据都是文本格式。

### 检索其他结果信息

这些函数被用来从PGresult对象中抽取其他信息

PQcmdStatus

返回来自于产生PGresult的SQL命令的命令状态标签。

char \*PQcmdStatus(PGresult \*res);

通常这就是该命令的名称，但是它可能包括额外数据，例如已被处理的行数。调用者不应该直接释放该结果。它将在相关的PGresult句柄被传递给PQclear之后被释放。

PQcmdTuples

返回受该SQL命令影响的行数。

char \*PQcmdTuples(PGresult \*res);

这个函数返回一个字符串，其中包含着产生PGresult的SQL语句影响的行数。这个只能被用于下列情况：执行一个SELECT、CREATE TABLE AS、INSERT、UPDATE、DELETE、MOVE、FETCH或COPY语句，或者一个包含INSERT、UPDATE或DELETE语句的预备查询的EXECUTE。如果产生PGresult的命令是其他什么东西，PQcmdTuples会返回一个空串。调用者不应该直接释放该结果。它将在相关的PGresult句柄被传递给PQclear之后被释放。

PQoidValue

如果该SQL命令是一个正好将一行插入到具有OID的表的INSERT，或者是一个包含合适INSERT语句的预备查询的EXECUTE，这个函数返回被插入行的 OID。否则，这个函数返回InvalidOid。如果被INSERT语句影响的表不包含 OID，这个函数也将返回InvalidOid。

Oid PQoidValue(const PGresult \*res);

PQoidStatus

由于PQoidValue和不是线程安全的，这个函数已经被废弃。它返回包含被插入行的OID的一个字符串，而PQoidValue返回OID值。

char \*PQoidStatus(const PGresult \*res);

### 用于包含在 SQL 命令中的转移串

PQescapeLiteral

char \*PQescapeLiteral(PGconn \*conn, const char \*str, size\_t length);

为了让一个串能用在SQL命令中，PQescapeLiteral可对它进行转义。当在SQL 命令中插入一个数据值作为文字常量时，这个函数很有用。一些字符（例如引号和反斜线）必须被转义以防止它们被SQL解析器解释成特殊的意思。PQescapeLiteral执行这种操作。

PQescapeLiteral返回一个str参数的已被转义版本，该版本被放在用malloc()分配的内存中。当该结果不再被需要时，这个内存应该用PQfreemem()释放。一个终止的零字节不是必须的，并且不应该被计入length（如果在length字节被处理之前找到一个终止字节，PQescapeLiteral会停止在零，该行为更像strncpy）。返回串中的所有特殊字符都被替换掉，这样它们能被数据库字符串解析器正确地处理。还会加上一个终止零字节。包括在结果串中的字符串必须用单引号包围。

发生错误时，PQescapeLiteral返回NULL并且一个合适的消息会被存储在conn对象中。

| 提示： |
| --- |
| 在处理从一个非可信源接收到的串时，做正确的转义特别重要。否则就会 有安全性风险：你容易受到”SQL 注入”攻击，其中可能会有预期之外的 SQL 语句会被喂给你的数据库。 |

注意，当一个数据值被作为PQexecParams或其兄弟例程中的一个独立参数传递时，没有必要做转义而且做转义也不正确。

PQescapeIdentifier

char \*PQescapeIdentifier(PGconn \*conn, const char \*str, size\_t length);

PQescapeIdentifier转义一个要用作SQL标识符的字符串，例如表名、列名或函数名。 一个用户提供的标识符可能包含被SQL解析器解释为标识符一部分的特殊字符时，或者当该标识符可能包含大小写形式应该被保留的大写字符时，这个函数很有用。

PQescapeIdentifier返回一个str参数的已被转义为SQL标识符的版本，该版本被放在用malloc()分配的内存中。当该结果不再被需要时，这个内存应该用PQfreemem()释放。一个终止的零字节不是必须的，并且不应该被计入length（如果在length字节被处理之前找到一个终止字节，PQescapeIdentifier会停止在零，该行为更像strncpy）。返回串中的所有特殊字符都被替换掉，这样它们能被作为一个SQL标识符正确地处理。还会加上一个终止零字节。返回串也将被双引号包围。

发生错误时，PQescapeIdentifier返回NULL并且一个合适的消息会被存储在conn对象中。

| 提示： |
| --- |
| 与字符串一样，要阻止SQ 注入攻击，当从一个不可信的来源接收到 SQL标识符时，它们必须被转义。 |

PQescapeStringConn

size\_t PQescapeStringConn(PGconn \*conn, char \*to, const char \*from, size\_t length, int \*error);

PQescapeStringConn转义字符串，它很像PQescapeLiteral。与PQescapeLiteral不一样的是，调用者负责提供一个合适尺寸的缓冲区。此外，PQescapeStringConn不产生必须包围瀚高数据库字符串的单引号。它们应该在结果要插入的SQL命令中提供。参数from指向要被转义的串的第一个字符，并且length参数给出了这个串中的字节数。一个终止的零字节不是必须的，并且不应该被计入length（如果在length字节被处理之前找到一个终止字节，PQescapeStringConn会停止在零，该行为更像strncpy）。to应当指向一个缓冲区，它能够保持至少比length值的两倍还要多至少一个字节，否则该行为是未被定义的。如果to和from串重叠，行为也是未被定义的。

如果error参数不是NULL，那么成功时\*error被设置为零，错误时设置为非零。当前唯一可能的错误情况涉及源串中非法的多字节编码。错误时仍然会产生输出串，但是可以预期服务器将认为它是畸形的并且拒绝它。在发生错误时，一个合适的消息被存储在conn对象中，不管error是不是NULL。

PQescapeStringConn返回写到to的字节数，不包括终止的零字节。

PQescapeString

PQescapeString是一个更老的被废弃的PQescapeStringConn版本。

size\_t PQescapeString (char \*to, const char \*from, size\_t length);

PQescapeStringConn和PQescapeString之间的唯一区别是不需要PGconn或error参数。正因为如此，它不能基于连接属性（例如字符编码）调整它的行为并且因此它可能给出错误的结果。还有，它没有方法报告错误情况。

PQescapeString可以在一次只使用一个瀚高数据库连接的客户端程序中安全地使用（在这种情况下它可以”在现象后面”找出它需要知道的东西）。在其他环境中它是一个安全性灾难并且应该用PQescapeStringConn来避免。

PQescapeByteaConn

把要用于一个SQL命令的二进制数据用类型bytea转义。和PQescapeStringConn一样，只有在将数据直接插入到一个SQL命令串时才使用它。

unsigned char \*PQescapeByteaConn(PGconn \*conn, const unsigned char \*from, size\_t from\_length, size\_t \*to\_length);

当某些字节值被用作一个SQL语句中的bytea文字的一部分时，它们必须被转义。PQescapeByteaConn转义使用十六进制编码或反斜线转义的字节。

from参数指向要被转义的串的第一个字节，并且from\_length参数给出这个二进制串中的字节数（一个终止的零字节是不需要的也是不被计算的）。to\_length参数指向一个将保持生成的已转义串长度的变量。这个结果串长度包括结果的终止零字节。

PQescapeByteaConn返回一个from参数的已被转义为二进制串的版本，该版本被放在用malloc()分配的内存中。当该结果不再被需要时，这个内存应该用PQfreemem()释放。返回串中的所有特殊字符都被替换掉，这样它们能被瀚高数据库的字符串解析器以及bytea输入函数正确地处理。还会加上一个终止零字节。不是结果串一部分的瀚高数据库字符串必须被单引号包围。

在发生错误时，将返回一个空指针，并且一个合适的错误消息被存储在conn对象中。当前，唯一可能的错误是没有足够的内存用于结果串。

PQescapeBytea

PQescapeBytea是一个更老的被废弃的PQescapeByteaConn版本。

unsigned char \*PQescapeBytea(const unsigned char \*from, size\_t from\_length, size\_t \*to\_length);

与PQescapeByteaConn的唯一区别是PQescapeBytea不用一个PGconn参数。正因为这样，PQescapeBytea只能在一次只使用一个瀚高数据库连接的客户端程序中安全地使用（在这种情况下它可以”在现象后面”找出它需要知道的东西）。如果在有多个数据库连接的程序中使用，它可能给出错误的结果（在那种情况下使用PQescapeByteaConn）。

PQunescapeBytea

将二进制数据的一个字符串表示转换成二进制数据 — 它是PQescapeBytea的逆向函数。当检索文本格式的bytea数据时，需要这个函数，但检索二进制个事时则不需要它。

unsigned char \*PQunescapeBytea(const unsigned char \*from, size\_t \*to\_length); from参数指向一个字符串，例如PQgetvalue被应用到一个bytea列上所返回的。PQunescapeBytea把这个串表示转换成它的二进制表示。它返回一个指向用malloc()分配的缓冲区的指针，在错误时返回NULL，并且把缓冲区的尺寸放在to\_length中。当结果不再需要时，它必须使用PQfreemem释放。

这种转换并不完全是PQescapeBytea的逆函数，因为当从PQgetvalue接收到字符串时，我们并不能期待它被”转义”。特别地这意味着不需要考虑字符串引用，并且因此也不需要一个参数。

## 异步命令处理

PQexec函数对于在普通的同步应用中提交命令是足以胜任的。不过，它的一些缺点可能对某些用户很重要：

• PQexec会等待命令完成。该应用可能有其他的工作要做（例如维护用户界面），这时它将不希望阻塞等待回应。

• 因为客户端应用的执行在它等待结果时会被挂起，对于应用来说很难决定要不要尝试取消正在进行的命令（这可以在一个信号处理器中完成，但别无他法）。

• PQexec只能返回一个PGresult结构。如果提交的命令串包含多个SQL命令，除了最后一个PGresult之外都会被PQexec丢弃。

• PQexec总是收集命令的整个结果，把它缓存在一个单一的PGresult中。虽然这简化了应用的错误处理逻辑，它对于包含很多行的结果并不现实。

不想受到这些限制的应用可以改用构建PQexec的底层函数：PQsendQuery以及PQgetResult。还有PQsendQueryParams、PQsendPrepare、 PQsendQueryPrepared、PQsendDescribePrepared以及 PQsendDescribePortal，它们可以与PQgetResult一起使用来分别复制PQexecParams、PQprepare、 PQexecPrepared、PQdescribePrepared和PQdescribePortal的功能。

PQsendQuery

向服务器提交一个命令而不等待结果。如果该命令被成功发送则返回1，否则返回0（此时，可以用PQerrorMessage获取关于失败的信息）。

int PQsendQuery(PGconn \*conn, const char \*command);

在成功调用PQsendQuery后，调用PQgetResult一次或者多次来获取结果。

在PQgetResult返回一个空指针之前，都不能再次调用PQsendQuery，返回的空指针指示该命令已经完成。

PQsendQueryParams

向服务器提交一个命令和单独的参数，而不等待结果。

int PQsendQueryParams(PGconn \*conn, const char \*command, int nParams,

const Oid \*paramTypes,

const char \* const \*paramValues,

const int \*paramLengths,

const int \*paramFormats,

int resultFormat);

这个函数等效于PQsendQuery，不过查询参数可以独立于查询字符串分开指定。该函数的参数处理和PQexecParams一样。和PQexecParams类似，它不能在 2.0 协议的连接上工作，并且它只允许在查询字符串中有一条命令。

PQsendPrepare

发送一个请求用给定参数创建一个预备语句，而不等待完成。

int PQsendPrepare(PGconn \*conn,

const char \*stmtName,

const char \*query,

int nParams,

const Oid \*paramTypes);

这个函数是PQprepare的异步版本：如果它能发送这个请求，则返回 1；如果不能，则返回 0。在成功调用之后，调用PQgetResult判断服务器是否成功创建了预备语句。这个函数的参数的处理和PQprepare一样。和PQprepare类似，它不能在 2.0 协议的连接上工作。

PQsendQueryPrepared

发送一个请求用给定参数执行一个预备语句，而不等待结果。

int PQsendQueryPrepared(PGconn \*conn,

const char \*stmtName,

int nParams,

const char \* const \*paramValues,

const int \*paramLengths,

const int \*paramFormats,

int resultFormat);

这个函数与PQsendQueryParams类似，但是要执行的命令是通过一个之前已经命名的预备语句指定， 而不是一个给出的查询字符串。该函数的参数处理和PQexecPrepared一样。和PQexecPrepared类似，它不能在 2.0 协议的连接上工作。

PQsendDescribePrepared

发送一个请求获得指定的预备语句的信息，但不等待完成。

int PQsendDescribePrepared(PGconn \*conn, const char \*stmtName);

这个函数是PQdescribePrepared的一个异步版本：如果它能够发送请求，则返回 1；否则，返回 0。在一次成功的调用后，调用PQgetResult来得到结果。该函数的参数处理和PQdescribePrepared一样。和PQdescribePrepared类似，它不能在 2.0 协议的连接上工作。

PQsendDescribePortal

提交一个请求来获得关于指定入口的信息，但不等待完成。

int PQsendDescribePortal(PGconn \*conn, const char \*portalName);

这个函数是PQdescribePortal的一个异步版本：如果它能够发送请求，则返回 1；否则，返回 0。在一次成功的调用后，调用PQgetResult来得到结果。该函数的参数处理和PQdescribePortal一样。和PQdescribePortal类似，它不能在 2.0 协议的连接上工作。

PQgetResult

等待来自于一个之前的PQsendQuery、PQsendQueryParams、PQsendPrepare、PQsendQueryPrepared、 PQsendDescribePrepared或 PQsendDescribePortal调用的结果，并且返回它。当该命令完成并且没有更多结果时，将返回一个空指针。

PGresult \*PQgetResult(PGconn \*conn);

PQgetResult必须被反复调用直到它返回一个空指针，空指针表示该命令完成（如果在没有命令活动时被调用，PQgetResult将立即返回一个空指针）。每一个来自PQgetResult的非空结果应该使用之前描述的同一个PGresult访问器处理。不要忘记在处理完之后释放每一个结果对象。注意，只有一个命令是活动的并且PQconsumeInput还没有读取必要的响应数据时， PQgetResult将会阻塞。

| 注意： |
| --- |
| 即使当PQresultStatus指出一个致命错误时，PQgetResult也应当被调用直到它返回一个空指针，以允许libpq完全处理该错误信息。 |

使用PQsendQuery和PQgetResult解决了PQexec的一个问题：如果一个命令字符串包含多个 SQL命令，这些命令的结果可以被个别地获得（顺便说一句：这样就允许一种简单的重叠处理形式， 客户端可以处理一个命令的结果，而同时服务器可以继续处理同一命令字符串中后面的查询）。

可以被PQsendQuery和PQgetResult获得的另一种常常想要的特性是一次从大型结果中检索一行。这会在 下一节 中讨论。

如果只调用PQgetResult（不调用PQsendQuery等）将仍会导致客户端阻塞直到服务器完成下一个SQL命令。用两个函数的正确使用可以避免这种情况。

PQconsumeInput

如果有来自服务器的输入可用，则使用之。

int PQconsumeInput(PGconn \*conn);

PQconsumeInput通常返回 1 表明”没有错误”，而返回 0 表明有某种麻烦发生（此时可以用PQerrorMessage）。注意该结果并不表明是否真正收集了任何输入数据。在调用PQconsumeInput之后，应用可以检查PQisBusy和/或PQnotifies来看看它们的状态是否改变。

即使应用还不准备处理一个结果或通知，PQconsumeInput也可以被调用。这个函数将读取可用的数据并且把它保存在一个缓冲区中，从而导致一个select()的读取就绪指示消失。因此应用可以使用PQconsumeInput立即清除select()条件，并且在空闲时再检查结果。

PQisBusy

如果一个命令繁忙则返回 1，也就是说PQgetResult会阻塞等待输入。返回 0 表示可以调用PQgetResult而不用担心阻塞。

int PQisBusy(PGconn \*conn);

PQisBusy本身将不会尝试从服务器读取数据，因此必须先调用PQconsumeInput，否则繁忙状态将永远不会结束。

一个使用这些函数的典型应用将有一个主循环，在主循环中会使用select()或poll()等待所有它必须响应的情况。其中之一将是来自服务器的可用输入，对select()来说意味着PQsocket标识的文件描述符上有可读的数据。当主循环检测到输入准备好时，它将调用PQconsumeInput读取输入。然后它可以调用PQisBusy，如果PQisBusy返回假（0）则接着调用PQgetResult。它还可以调用PQnotifies检测NOTIFY消息。

一个使用PQsendQuery/PQgetResult的客户端也可以尝试取消一个正在被服务器处理的命令， 详见此节 。但是，不管PQcancel的返回值是什么，应用都必须继续使用PQgetResult进行正常的结果读取序列。一次成功的取消会让命令更快终止。

通过使用上述函数，我们可以避免在等待来自数据库服务器的输入时被阻塞。不过，在应用发送输出给服务器时还是可能出现阻塞。这种情况比较少见，但是如果发送非常长的 SQL 命令或者数据值时确实可能发生（不过，最有可能是在应用通过COPY IN发送数据时）。为了避免这种可能性并且实现完全地非阻塞数据库操作，可以使用下列附加函数。

PQsetnonblocking

把连接的状态设置为非阻塞。

int PQsetnonblocking(PGconn \*conn, int arg);

如果arg为 1，把连接状态设置为非阻塞；如果arg为 0，把连接状态设置为阻塞。如果 OK 返回 0，如果错误返回 -1。

在非阻塞状态，调用 PQsendQuery、PQputline、PQputnbytes、PQputCopyData和PQendcopy将不会阻塞， 但是如果它们需要被再次调用则会返回一个错误。

注意PQexec不会遵循任何非阻塞模式；如果调用PQexec，那么它的行为总是阻塞的。

PQisnonblocking

返回数据库连接的阻塞状态。

int PQisnonblocking(const PGconn \*conn);

如果连接被设置为非阻塞状态，返回 1，如果是阻塞状态返回 0。

PQflush

尝试把任何正在排队的输出数据刷到服务器。如果成功（或者发送队列为空）返回 0，如果因某种原因失败则返回 -1，或者如果还无法把发送队列中的所有数据都发送出去，则返回 1（这种情况只在连接为非阻塞时候才会发生）。

int PQflush(PGconn \*conn);

在一个非阻塞连接上发送任何命令或者数据之后，要调用PQflush。如果它返回 1，就要等待套接字变成读就绪或写就绪。如果它变为写就绪，应再次调用PQflush。如果它变为读就绪，则应先调用PQconsumeInput，然后再调用PQflush。一直重复直到PQflush返回0（有必要检查读就绪并且用PQconsumeInput耗尽输入，因为服务器可能阻塞给我们发送数据的尝试，例如 NOTICE 消息，并且在我们读它的数据之前它都不会读我们的数据）。一旦PQflush返回 0，应等待套接字变成读就绪并且接着按照上文所述读取响应。

## 一行一行地检索查询结果

通常，libpq会收集一个 SQL 命令的整个结果并且把它作为单个PGresult返回给应用。这对于返回大量行的命令是行不通的。对于这类情况，应用可以使用PQsendQuery和PQgetResult的单行模式。在这种模式中，结果行以一次一行的方式被返回给应用。

要进入到单行模式，在一次成功的PQsendQuery（或者其他兄弟函数）调用后立即调用PQsetSingleRowMode。这种模式选择只对当前正在执行的查询有效。然后反复调用PQgetResult，直到它返回空，如 上一节 中所示。如果该查询返回行，它们会作为单个的PGresult对象返回，它们看起来都像普通的查询结果，只不过其状态代码是PGRES\_SINGLE\_TUPLE而非PGRES\_TUPLES\_OK。在最后一行之后或者紧接着该查询返回零行之后，一个状态为PGRES\_TUPLES\_OK的零行对象会被返回，这就是代表不会有更多行的信号（但是注意仍然有必要继续调用PQgetResult直到它返回空）。所有这些PGresult对象将包含相同的行描述数据（列名、类型等等），这些数据和通常一个查询的PGresult对象的相同。每一个对象都应该按常规用PQclear释放。

PQsetSingleRowMode

为当前正在执行的查询选择单行模式。

int PQsetSingleRowMode(PGconn \*conn);

这个函数只能在调用PQsendQuery或一个其兄弟函数之后立刻调用，并且要在任何连接上的其他操作之前调用，例如PQconsumeInput或PQgetResult。如果在正确的时间被调用，该函数会为当前查询激活单行模式并且返回 1。否则模式会保持不变并且该函数返回0。在任何情况下，当前查询结束之后模式都会恢复到正常。

| 小心： |
| --- |
| 在处理一个查询时，服务器可能返回一些行并且接着遇到一个错误导致查询被中断。通常，libpq会丢弃掉这样的行并且至报告错误。但是在单行模式中，那些行（错误之前返回的行）已经被返回给应用。因此，应用将看到一些PGRES\_SINGLE\_TUPLE PGresult对象并且然后看到一个PGRES\_FATAL\_ERROR对象。为了得到正确的事务行为，如果查询最终失败，应用必须被设计为丢弃或者撤销使用之前处理的行完成的事情。 |

## 取消进行中的查询

一个客户端应用可以使用本节描述的函数请求取消一个仍在被服务器处理的命令。

PQgetCancel

创建一个数据结构，这个数据结构包含取消一个通过特定数据库连接发出的命令所需要的信息。

PGcancel \*PQgetCancel(PGconn \*conn);

一个PGconn连接对象，PQgetCancel创建一个PGcancel对象。如果给定的conn为NULL或者一个不合法的连接，它将返回NULL。PGcancel对象是一个不透明的结构，它不能直接被应用访问。它只能被传递给PQcancel或PQfreeCancel。

PQfreeCancel

释放一个由PQgetCancel创建的数据结构。

void PQfreeCancel(PGcancel \*cancel);

PQfreeCancel释放一个由前面的PQgetCancel创建的数据对象。PQfreeCancel释放一个之前由PQgetCancel创建的数据对象。

PQcancel

要求服务器放弃当前命令的处理。

int PQcancel(PGcancel \*cancel, char \*errbuf, int errbufsize);

如果取消请求成功发送，则返回值为 1，否则为 0。如果不成功，则errbuf会被填充一个解释性的错误消息。errbuf必须是一个尺寸为errbufsize的字符数组（推荐尺寸为 256 字节）。，解释为何不成功。errbuf必须是 一个大小为errbufsize的 char 数组（建议大小为 256 字节）。

不过，成功的发送并不保证请求会有任何效果。如果取消有效，那么当前的命令将提前终止并且返回一个错误结果。如果取消失败（也就是说， 因为服务器已经完成命令的处理），那么就根本不会有可见的结果。

如果PQcancel是信号handler里的一个局部变量，那么PQcancel可以在一个信号handler里安全地调用。在PQcancel涉及的范围里，PQcancel对象都是只读的，因此我们也可以从一个与处理PGconn对象的线程分离的线程里处理它。如果errbuf是信号handler中的一个局部变量，PQcancel可以从一个信号handler中安全地调用。在PGcancel有关的范围内，PQcancel都是只读的，因此也可以在一个从操纵PGconn对象的线程中独立出来的线程中调用它。

PQrequestCancel

PQrequestCancel是PQcancel的一个被废弃的变体。

int PQrequestCancel(PGconn \*conn);

要求服务器放弃当前命令的处理。它直接在PGconn对象上进行操作， 并且如果失败，就会在PGconn对象里存储错误消息（因此可以用PQerrorMessage检索出来）。尽管功能相同，这个方法在多线程程序里和信号处理器里会带来危险，因为它可能 覆盖PGconn的错误消息，进而将当前连接上正在处理的操作搞乱。

## 快速路径接口

瀚高数据库提供一种快速路径接口来向服务器发送简单的函数调用。

| 提示： |
| --- |
| 这个接口在某种程度上已被废弃，因为我们可以通过创建一个定义该函数调用的预备语句来达到类似或者更强大的功能。然后，用参数和结果的二进制传输执行该语句，从而取代快速函数调用。 |

函数PQfn请求通过快速路径接口执行服务器函数。

PGresult \*PQfn(PGconn \*conn,

int fnid,

int \*result\_buf,

int \*result\_len,

int result\_is\_int,

const PQArgBlock \*args,

int nargs);

typedef struct

{

int len;

int isint;

union

{

int \*ptr;

int integer;

} u;

} PQArgBlock;

fnid参数是要被执行的函数的OID。args和nargs定义了要传递给函数的参数；它们必须匹配已声明的函数参数列表。当一个参数结构的isint域为真时，u.integer值被以指定长度（必须是1、2或者4字节）整数的形式发送给服务器；这时候会发生恰当的字节交换。

当isint为假时，\*u.ptr中指定数量的字节将不做任何处理被发送出去；这些数据必须是服务器 预期的用于该函数参数数据类型的二进制传输的格式（由于历史原因u.ptr被声明为类型int \*，其实把它考虑成void \*会更好）。result\_buf是放置该函数返回值的缓冲区。调用者必须已经分配了足够的空间来存储返回值（这里没有检查！）。实际的结果长度将被放在result\_len指向的整数中返回。如果预期结果是 2 或 4 字节整数，把result\_is\_int设为 1；否则设为 0。把result\_is\_int设为 1 导致libpq在必要时对值进行交换字节，这样它就作为对客户端机器正确的int值被传输，注意对任一种允许的结果大小都会传递一个 4 字节到\*result\_buf。当result\_is\_int是 0 时，服务器发送的二进制格式字节将不做修改直接返回（在这种情况下，把result\_buf考虑为类型void \*更好）。

PQfn总是返回一个有效的PGresult指针。在使用结果之前应该检查结果状态。当结果不再使用后，调用者有义务使用PQclear释放PGresult。

注意我们没办法处理空参数、空结果，也没办法在使用这个接口时处理返回值为集合的结果。

## 异步提示

瀚高数据库通过LISTEN和NOTIFY命令提供了异步通知。一个客户端会话用LISTEN命令在一个特定的通知频道中注册它感兴趣的通知（也可以用UNLISTEN命令停止监听）。当任何会话执行一个带有特定频道名的NOTIFY命令时，所有正在监听该频道的会话会被异步通知。可以传递一个”载荷”字符串来与监听者沟通附加的数据。

libpq应用把LISTEN、UNLISTEN和NOTIFY命令作为通常的 SQL 命令提交。随后通过调用PQnotifies来检测NOTIFY消息的到达。

函数PQnotifies从来自服务器的未处理通知消息列表中返回下一个通知。如果没有待处理的信息则返回一个空指针。一旦PQnotifies返回一个通知，该通知会被认为已处理并且将被从通知列表中删除。

PGnotify \*PQnotifies(PGconn \*conn);

typedef struct pgNotify

{

char \*relname; /\* notification channel name \*/

int be\_pid; /\* process ID of notifying server process \*/

char \*extra; /\* notification payload string \*/

} PGnotify;

在处理完PQnotifies返回的PGnotify对象后，别忘了用PQfreemem把它释放。释放PGnotify指针就足够了；relname和extra域并不代表独立分配的内存（这些域的名称是历史性的，尤其是频道名称与关系名称没有什么联系）。

文中的libpq示例程序2 给出了一个例子程序展示异步通知的使用。

PQnotifies实际上并不从服务器读取数据；它只是返回被另一个libpq函数之前吸收的消息。在以前的libpq版本中，及时收到NOTIFY消息的唯一方法是持续地提交命令，即使是空命令也可以，并且在每次PQexec后检查PQnotifies。虽然这个方法还能用，但是由于太过浪费处理能力已被废弃。

当你没有可用的命令提交时，一种更好的检查NOTIFY消息的方法是调用PQconsumeInput，然后检查PQnotifies。你可以使用select()来等待服务器数据到达，这样在无事可做时可以不浪费CPU能力（参考PQsocket来获得用于select()的文件描述符）。注意不管是用PQsendQuery/PQgetResult提交命令还是简单地使用PQexec，这种方法都能正常工作。不过，你应该记住在每次PQgetResult或PQexec之后检查PQnotifies，看看在命令的处理过程中是否有通知到达。

## COPY命令相关的函数

瀚高数据库中的COPY命令有用于libpq的对网络连接读出或者写入的选项。这一节描述的函数允许应用通过提供或者消耗已拷贝的数据来充分利用这个功能。

整个处理是应用首先通过PQexec或者一个等效的函数发出 SQL COPY命令。对这个命令的响应（如果命令无误）将是一个状态代码是PGRES\_COPY\_OUT或 者PGRES\_COPY\_IN（取决于指定的拷贝方向）的PGresult对象。应用然后就应该使用这一节的函数接收或者传送数据行。在数据传输结束之后，另外一个PGresult对象会被返回以表明传输的成功或者失败。它的状态将是：PGRES\_COMMAND\_OK表示成功，PGRES\_FATAL\_ERROR表示发生了一些问题。此时我们可以通过PQexec发出进一步的 SQL 命令（在COPY操作的处理过程中，不能用同一个连接执行其它 SQL 命令）。

如果一个COPY命令是通过PQexec在一个可能包含额外命令的字符串中发出的，那么应用在完成COPY序列之后必须继续用PQgetResult取得结果。只有在PQgetResult返回NULL时，我们才能确信PQexec的命令字符串已经处理完毕， 并且可以安全地发出更多命令。

这一节的函数应该只在从PQexec或PQgetResult获得了PGRES\_COPY\_OUT或PGRES\_COPY\_IN结果状态的后执行。

一个承载了这些状态值之一的PGresult对象携带了正在开始的COPY操作的一些额外数据。这些额外的数据可以用于那些与带查询结果的连接一起使用的函数：

PQnfields

返回要拷贝的列（域）的个数。

PQbinaryTuples

0 表示整体拷贝格式都是文本（行用新行分隔，列用分隔字符分隔等等）。1 表示整体拷贝格式都是二进制。详见COPY。

PQfformat

返回与拷贝操的每列相关的格式代码（0 是文本，1 是二进制）。当整体拷贝格式是文本时，那么每列的格式代码将总是零，但是二进制格式可以同时支持文本和二进制列（不过，就目前的COPY实现而言，二进制拷贝中只会出现二进制列；所以目前每列的格式总是匹配总体格式）。

| 注意： |
| --- |
| 这些额外的数据值只在使用协议 3.0 时可用。在使用协议 2.0 时，所有这些函数都返回 0。 |

### 用于发送COPY数据的函数

这些函数用于在COPY FROM STDIN期间发送数据。如果在连接不是COPY\_IN状态，调用它们会失败。

PQputCopyData

在COPY\_IN状态中向服务器发送数据。

int PQputCopyData(PGconn \*conn,

const char \*buffer,

int nbytes);

传输指定buffer中长度为nbytes的COPY数据到服务器。如果数据被放在队列中，结果是1；如果因为缓冲区满而无法被放在队列中（只可能发生在连接是非阻塞模式时），那么结果是零；如果发生错误，结果为 -1（如果返回值为 -1，那么使用PQerrorMessage检索细节。如果值是零，那么等待写准备好然后重试）。

应用可以把COPY数据流划分成任意方便的大小放到缓冲区中。在发送时，缓冲区载荷的边界没有什么语意。数据流的内容必须匹配COPY命令预期的数据格式；详见COPY。

PQputCopyEnd

在COPY\_IN状态中向服务器发送数据结束的指示。

int PQputCopyEnd(PGconn \*conn, const char \*errormsg);

如果errormsg是NULL，则成功结束COPY\_IN操作。如果errormsg不是NULL则COPY被强制失败，errormsg指向的字符串是错误消息（不过，我们不应假定这个准确的错误信息将会从服务器传回，因为服务器可能已经因为其自身原因导致COPY失败。还要注意的是在使用 3.0 协议之前的连接时，强制失败的选项是不能用的）。

如果终止消息被发送，则结果为 1；在非阻塞模式中，结果为 1 也可能只表示终止消息被成功地放在了发送队列中（在非阻塞模式中，要确认数据确实被发送出去，你应该接着等待写准备好并且调用PQflush，重复这些直到返回零）。零表示该函数由于缓冲区满而无法将该终止消息放在队列中，这只会发生在非阻塞模式中（在这种情况下，等待写准备好并且再次尝试PQputCopyEnd调用）。如果发生系统错误，则返回 -1，可以使用PQerrorMessage检索详情。

在成功调用PQputCopyEnd之后，调用PQgetResult获取COPY命令的最终结果状态。我们可以用平常的方法来等待这个结果可用。然后返回到正常的操作。

### 用于接收COPY数据的函数

这些函数用于在COPY TO STDOUT的过程中接收数据。如果连接不在COPY\_OUT状态，那么调用它们将会失败。

PQgetCopyData

在COPY\_OUT状态下从服务器接收数据。

int PQgetCopyData(PGconn \*conn, char \*\*buffer, int async);

在一个COPY期间尝试从服务器获取另外一行数据。数据总是以每次一个数据行的方式被返回；如果只有一个部分行可用，那么它不会被返回。成功返回一个数据行涉及到分配一块内存来保存该数据。buffer参数必须为非NULL。\*buffer被设置为指向分配到的内存的指针，或者是在没有返回缓冲区的情况下指向NULL。一个非NULL的结果缓冲区在不需要时必须用PQfreemem释放。

在成功返回一行之后，返回的值就是该数据行里数据的字节数（将是大于零）。被返回的字符串总是空终止的，虽然这可能只是对文本COPY有用。一个零结果表示该COPY仍然在处理中，但是还没有可用的行（只在async为真时才可能）。一个 -1 结果表示COPY已经完成。-2 结果表示发生了错误（参考PQerrorMessage获取原因）。

当async为真时（非零），PQgetCopyData将不会阻塞等待输入；如果COPY仍在处理过程中并且没有可用的完整行，那么它将返回零（在这种情况下等待读准备好，然后在再次调用PQgetCopyData之前，调用PQconsumeInput）。当async为假（零）时，PQgetCopyData将阻塞，直到数据可用或者操作完成。

在PQgetCopyData返回 -1 之后，调用PQgetResult获取COPY命令的最后结果状态。我们可以用平常的方法来等待这个结果可用。然后返回到正常的操作。

### 用于COPY的废弃函数

这些函数代表了以前的处理COPY的方法。尽管它们还能用，但是现在已经被废弃，因为它们的错误处理很糟糕、检测结束数据的方法也不方便，并且缺少对二进制或非阻塞传输的支持。

PQgetline

读取一个以新行终止的字符行到（由服务器传输） 到一个长度为length的字符串缓冲区。

int PQgetline(PGconn \*conn, char \*buffer, int length);

这个函数拷贝最多length-1 个字符到该缓冲区中，并且把终止的新行转换成一个零字节。PQgetline在输入结束时返回EOF，如果整行都被读取则返回 0，如果缓冲区填满了而还没有遇到结束的新行则返回 1。

注意，应用必须检查是否一个新行包含两个字符\\.，这表明服务器 已经完成了COPY命令的结果发送。如果应用可能收到超过length-1 字符长的行， 我们就应该确保正确识别\\.行（例如，不要把一个长数据行的结束当作一个终止行）。

PQgetlineAsync

不阻塞地读取一行COPY数据（由服务器传输）到一个缓冲区中。

int PQgetlineAsync(PGconn \*conn, char \*buffer, int bufsize);

这个函数类似于PQgetline，但是可以被用于那些必须异步读取COPY数据的应用，也就是不阻塞的应用。在发出了COPY命令并得到了PGRES\_COPY\_OUT响应之后，应用应该调用PQconsumeInput和PQgetlineAsync直到检测到结束数据的信号。

不像PQgetline，这个函数负责检测结束数据。

在每次调用时，如果libpq的输入缓冲区中有一个完整的数据行可用，PQgetlineAsync都将返回数据。否则，在剩余行到达之前不会返回数据。如果识别到拷贝数据结束的标志，此函数返回 -1；如果没有可用数据则返回 0； 或者是给出一个正数给出被返回的字节数。如果返回 -1，调用者下一步必须调用PQendcopy，然后回到正常处理。

返回的数据将不超过一个数据行的范围。如果可能，每次将返回一个完整行。但如果调用者提供的缓冲区太小不足以容下服务器发送的行，那么将返回部分行。对于文本数据，这可以通过测试返回的最后一个字节是否\\n来检测（在二进制COPY中， 需要对COPY数据格式进行实际的分析，以便做相同的判断）。被返回的字符串不是空结尾的（如果你想增加一个终止空，确保传递一个比实际可用空间少一字节的bufsize）。

PQputline

向服务器发送一个空终止的字符串。如果 OK 则返回 0；如果不能发送字符串则返回EOF。

int PQputline(PGconn \*conn, const char \*string);

一系列PQputline调用发送的COPY数据流和PQgetlineAsync返回的数据具有相同的格式，只是应用不需要每次PQputline调用中发送刚好一个数据行；在每次调用中发送多行或者部分行都是可以的。

| 注意： |
| --- |
| 在HGDB协议 3.0 之前，应用必须显式地发送两个字符\\.作为最后一行来指示服务器已经完成发送COPY数据。虽然这么做仍然有效，但是它已经被废弃并且\\.的特殊含义可能在将来的版本中删除。在发送完实际数据之后， 调用PQendcopy就足够了。 |

PQputnbytes

向服务器发送一个非空终止的字符串。如果 OK 则返回 0，如果不能发送字符串则返回EOF。

int PQputnbytes(PGconn \*conn, const char \*buffer, int nbytes);

这个函数类似PQputline，除了数据缓冲区不需要是空终止，因为要发送的字节数是直接指定的。在发送二进制数据时使用这个过程。

PQendcopy

与服务器同步。

int PQendcopy(PGconn \*conn);

这个函数等待服务器完成拷贝。当最后一个字符串已经用PQputline发送给服务器时或者当最后一个字符串已经用PQgetline从服务器接收到时，就会发出这个函数。这个函数必须被发出，否则服务器将会和客户端”不同步”。从这个函数返回后，服务器就已经准备好接收下一个 SQL 命令了。函数成功完成时返回值为 0，否则返回非零值（如果返回值为非零值，用PQerrorMessage检索详情）。

在使用PQgetResult时，应用应该通过反复调用PQgetline并且在看到终止行后调用PQendcopy来响应PGRES\_COPY\_OUT结果。然后它应该返回到PQgetResult循环直到PQgetResult返回一个空指针。类似地，PGRES\_COPY\_IN结果会用一系列PQputline加上之后的PQendcopy来处理，然后返回到PQgetResult循环。这样的安排将保证嵌入到一系列SQL命令中的COPY命令将被正确执行。

旧的应用很可能会通过PQexec提交一个COPY命令并且假定事务在PQendcopy之后完成。只有在COPY是命令字符串中唯一的SQL命令时才能正确工作。

## 控制函数

这些函数控制libpq行为各种各样的细节。

PQclientEncoding

返回客户端编码。

int PQclientEncoding(const PGconn \*conn);

请注意，它返回的是编码 ID，而不是一个符号串字符串，如EUC\_JP。如果不成功，它会返回 -1。要把一个编码 ID 转换为为一个编码名称，可以用：

char \*pg\_encoding\_to\_char(int encoding\_id);

PQsetClientEncoding

设置客户端编码。

int PQsetClientEncoding(PGconn \*conn, const char \*encoding);

conn是一个到服务器的连接，而encoding是你想使用的编码。如果函数成功地设置编码，则返回 0，否则返回 -1。这个连接的当前编码可以使用PQclientEncoding确定。

PQsetErrorVerbosity

决定PQerrorMessage和PQresultErrorMessage返回的消息的细节程度。

typedef enum

{

PQERRORS\_TERSE,

PQERRORS\_DEFAULT,

PQERRORS\_VERBOSE,

PQERRORS\_SQLSTATE

} PGVerbosity;

PGVerbosity PQsetErrorVerbosity(PGconn \*conn, PGVerbosity verbosity);

PQsetErrorVerbosity设置细节模式，并返回该连接的前一个设置。在TERSE模式下，返回的消息只包括严重性、主要文本以及位置；这些东西通常放在一个单一行中。DEFAULT模式生成的消息包括上面的信息加上任何细节、提示或者上下文域（这些可能跨越多行）。VERBOSE模式包括所有可以可用的域。修改细节模式不会影响来自已有PGresult对象中的可用消息。只有随后创建的PGresult对象才受到影响。SQLSTATE模式仅包括错误严重性和SQLSTATE错误代码，如果其中之一是可用的（如果没有，输出类似于TERSE模式）。

更改详细程度设置不会影响已存在的PGresult对象的可用的消息，只会影响随后创建的对象。（如果想要用不同的详细程度打印之前的错误，请见PQresultVerboseErrorMessage）

PQsetErrorContextVisibility

决定如何处理PQerrorMessage和PQresultErrorMessage返回的消息中的CONTEXT域。

typedef enum

{

PQSHOW\_CONTEXT\_NEVER,

PQSHOW\_CONTEXT\_ERRORS,

PQSHOW\_CONTEXT\_ALWAYS

} PGContextVisibility;

PGContextVisibility PQsetErrorContextVisibility(PGconn \*conn,

PGContextVisibility show\_context);

PQsetErrorContextVisibility设置上下文显示模式，返回该连接上之前的设置。这个模式控制消息中是否包括CONTEXT域。NEVER模式不会包括CONTEXT，而ALWAYS则尽可能地包括这个域。在ERRORS模式（默认）中，只在错误消息中包括CONTEXT域，而在通知和警告消息中不会包括。（但是，如果详细程度设置为 TERSE 或SQLSTATE，则无论上下文显示模式如何，都会省略CONTEXT字段。）

更改这个模式不会影响从已经存在的PGresult对象项中得到的消息，只会影响后续创建的PGresult对象（如果想要用不同的详细程度打印之前的错误，请见PQresultVerboseErrorMessage）。

PQtrace

启用对客户端/服务器通讯的跟踪，把跟踪信息输出到一个调试文件流中。

void PQtrace(PGconn \*conn, FILE \*stream);

| 注意： |
| --- |
| 在 Windows上，如果libpq库和应用使用了不同的标志编译，那么这个函数调用会导致应用崩溃，因为FILE指针的内部表达是不一样的。特别是多线程/单线程、发布/调试 以及静态/动态标志应该是库和所有使用库的应用都一致。 |

PQuntrace

禁用PQtrace打开的跟踪。

void PQuntrace(PGconn \*conn);

## 杂项函数

一如往常，总有一些函数不适合放在任何其他地方。

PQfreemem

释放libpq分配的内存。

void PQfreemem(void \*ptr);

释放libpq分配的内存，尤其是PQescapeByteaConn、PQescapeBytea、PQunescapeBytea和PQnotifies分配的内存。特别重要的是，在微软 Windows 上使用这个函数，而不是free()。这是因为只有DLL和应用的当多线程/单线程、发布/调试以及静态/动态标志相同时，才能在一个 DLL 中分配内存并且在应用中释放它。在非微软 Windows 平台上，这个函数与标准库函数free()相同。

PQconninfoFree

释放PQconndefaults或PQconninfoParse分配的数据结构。

void PQconninfoFree(PQconninfoOption \*connOptions);

一个简单的PQfreemem不会做这些，因为数组包含对子字符串的引用。

PQencryptPasswordConn

准备一个HGDB口令的加密形式。

char \*PQencryptPasswordConn(PGconn \*conn, const char \*passwd, const char \*user, const char \*algorithm);

这个函数旨在用于那些希望发送类似于ALTER USER joe PASSWORD 'pwd'命令的客户端应用。不在这样一个命令中发送原始的明文密码是一个好习惯，因为它可能被暴露在命令日志、活动显示等等中。相反，在发送之前使用这个函数可以将口令转换为加密的形式。

passwd和user参数是明文口令以及用户的SQL名称。algorithm指定用来加密口令的加密算法。当前支持的算法是md5和scram-sha-256（on和off也被接受作为md5的别名，用于与较老的服务器版本兼容）。如果algorithm是NULL，这个函数将向服务器查询password\_encryption设置的当前值。这种行为可能会阻塞当前事务，并且当前事务被中止或者连接正忙于执行另一个查询时会失败。如果希望为服务器使用默认的算法但避免阻塞，应在调用PQencryptPasswordConn之前查询你自己的password\_encryption，并且将该值作为algorithm传入。

返回值是一个由malloc分配的字符串。调用者可以假设该字符串不含有需要转义的任何特殊字符。在处理完它之后，用PQfreemem释放结果。发生错误时，返回的是NULL，并且适当的消息会被存储在连接对象中。

PQencryptPassword

准备一个口令的md5加密形式。

char \*PQencryptPassword(const char \*passwd, const char \*user);

PQencryptPassword是PQencryptPasswodConn的一个较老的已经被废弃的版本。其差别是PQencryptPassword不要求一个连接对象，并且总是用md5作为加密算法。

PQmakeEmptyPGresult

用给定的状态，构造一个空PGresult对象。

PGresult \*PQmakeEmptyPGresult(PGconn \*conn, ExecStatusType status);

这是libpq内部用于分配并初始化一个空PGresult对象的函数。如果不能分配内存，那么这个函数返回NULL。它也是可以对外使用的，因为一些应用认为它可以用于产生结果对象（特别是带有错误状态的对象）本身。如果conn非空，并且status表示一个错误，那么指定连接的当前错误消息会被复制到PGresult中。如果conn非空，那么连接中的任何已注册事件过程也会被复制到PGresult中（它们不会获得PGEVT\_RESULTCREATE调用，但会看到PQfireResultCreateEvents）。注意在该对象上最终应该调用PQclear，正如对libpq本身返回的PGresult对象所作的那样。

PQfireResultCreateEvents

为每一个在PGresult对象中注册的事件过程触发一个PGEVT\_RESULTCREATE事件（ 见后续章节 ）。成功时返回非0，如果任何事件过程失败则返回0。

int PQfireResultCreateEvents(PGconn \*conn, PGresult \*res);

conn参数被传送给事件过程，但不会被直接使用。如果事件过程不使用它，则会返回NULL。

已经接收到这个对象的PGEVT\_RESULTCREATE或PGEVT\_RESULTCOPY事件的事件过程不会被再次触发。

这个函数与PQmakeEmptyPGresult分开的主要原因是在调用事件过程之前创建一个PGresult并且填充它常常是合适的。

PQcopyResult

为一个PGresult对象创建一个拷贝。这个拷贝不会以任何方式链接到源结果，并且当该拷贝不再需要时，必须调用PQclear进行清理。如果函数失败，返回NULL。

PGresult \*PQcopyResult(const PGresult \*src, int flags);

这个函数的意图并非是制作一个准确的拷贝。返回的结果总是会被放入PGRES\_TUPLES\_OK状态，并且不会拷贝来源中的任何错误消息（不过它确实会拷贝命令状态字符串）。flags参数决定还要拷贝些什么。它通常是几个标志位通过OR结合。PG\_COPYRES\_ATTRS指定复制源结果的属性（列定义）。PG\_COPYRES\_TUPLES指定复制源结果的元组（这也意味着复制属性）。PG\_COPYRES\_NOTICEHOOKS指定复制源结果的提醒hook。PG\_COPYRES\_EVENTS指定复制源结果的事件（但是不会复制与源结果相关的实例数据）。

PQsetResultAttrs

设置PGresult对象的属性。

int PQsetResultAttrs(PGresult \*res, int numAttributes, PGresAttDesc \*attDescs);

提供的attDescs被复制到结果中。如果attDescs指针为NULL或numAttributes小于1，那么请求将被忽略并且函数成功。如果res已经包含属性，那么函数会失败。如果函数失败，返回值是 0。如果函数成功，返回值是非 0。

PQsetvalue

设置一个PGresult对象的一个元组域值。

int PQsetvalue(PGresult \*res, int tup\_num, int field\_num, char \*value, int len);

这个函数将自动按需增加结果的内置元组数组。但是，tup\_num参数必须小于等于PQntuples，意味着这个函数对元组数组一次只能增加一个元组。但已存在的任意元组中的任意字段可以以任意顺序进行调整。如果field\_num的一个值已经存在，它会被覆盖。

如果len是-1，或value是NULL，该字段值会被设置为一个SQL空值。value会被复制到结果的私有存储中，因此函数返回后就不再需要了。如果函数失败，返回值是0。如果函数成功，返回值会是非0。

PQresultAlloc

为一个PGresult对象分配附属存储。

void \*PQresultAlloc(PGresult \*res, size\_t nBytes);

当res被清除时，这个函数分配的内存也会被释放掉。如果函数失败，返回值是NULL。结果被保证为按照数据的任意类型充分地对齐，正如malloc所作的。

PQresultMemorySize

检索为PGresult对象分配的字节数。

size\_t PQresultMemorySize(const PGresult \*res);

此值是与PGresult对象关联的所有malloc请求的总和，就是说，PQclear将释放的所有空间。此信息可用于管理内存消耗。

## 通知处理

服务器产生的通知和警告消息不会被查询执行函数返回，因为它们不代表查询失败。它们可以被传递给一个通知处理函数，并且在处理者返回后执行会继续正常进行。默认的处理函数会把消息打印在stderr上，但是应用可以通过提供它自己的处理函数来重载这种行为。

由于历史原因，通知处理有两个级别，称为通知接收器和通知处理器。通知接收器的默认行为是格式化通知并且将一个字符串传递给通知处理器来打印。不过，如果一个应用选择提供自己的通知接收器，它通常会忽略通知处理器层并且在通知接收器中完成所有工作。

函数PQsetNoticeReceiver 为一个连接对象设置或者检查当前的通知接收器。相似地， PQsetNoticeProcessor 设置或检查当前的通知处理器。

typedef void (\*PQnoticeReceiver) (void \*arg, const PGresult \*res);

PQnoticeReceiver

PQsetNoticeReceiver(PGconn \*conn,

PQnoticeReceiver proc,

void \*arg);

typedef void (\*PQnoticeProcessor) (void \*arg, const char \*message);

PQnoticeProcessor

PQsetNoticeProcessor(PGconn \*conn,

PQnoticeProcessor proc,

void \*arg);

这些函数中的每一个会返回之前的通知接收器或处理器函数指针，并且设置新值。如果你提供了一个空函数指针，将不会采取任何动作，只会返回当前指针。

当接收到一个服务器产生的或者libpq内部产生的通知或警告消息，通知接收器函数会被调用。它会以一种PGRES\_NONFATAL\_ERROR PGresult的形式传递该消息（这允许接收器使用PQresultErrorField抽取个别的域，或者使用PQresultErrorMessage或者PQresultVerboseErrorMessage得到一个完整的预格式化的消息）。被传递给PQsetNoticeReceiver的同一个空指针也被传递（必要时，这个指针可以被用来访问应用相关的状态）。

默认的通知接收器会简单地抽取消息（使用PQresultErrorMessage）并且将它传递给通知处理器。

通知处理器负责处理一个以文本形式给出的通知或警告消息。该消息的字符串文本（包括一个收尾的新行）被传递给通知处理器，外加一个同时被传递给PQsetNoticeProcessor的空指针（必要时，这个指针可以被用来访问应用相关的状态）。

默认的通知处理器很简单：

static void

defaultNoticeProcessor(void \*arg, const char \*message)

{

fprintf(stderr, "%s", message);

}

一旦你设定了一个通知接收器或处理器，你应该期待只要PGconn对象或者从它构造出的PGresult对象存在，该函数就应该能被调用。在一个PGresult创建时，PGconn的当前通知处理指针被复制到PGresult中，以备类似PQgetvalue的函数使用。

## 事件系统

libpq的事件系统被设计为通知已注册的事件处理器它感兴趣的libpq事件，例如PGconn以及PGresult对象的创建和毁灭。一种主要的使用情况是这允许应用将自己的数据与一个PGconn或者PGresult关联在一起，并且确保那些数据在适当的时候被释放。

每一个已注册的事件处理器与两部分数据相关，对于libpq它们只是透明的void \*指针。当事件处理器被注册到一个PGconn时，会有一个应用提供的转移指针。该转移指针在PGconn及其产生的所有PGresult的生命期内都不会改变。因此，如果使用它，它必须指向长期存在的数据。此外，还有一个instance data指针，它在每一个PGconn和PGresult中都开始于NULL。这个指针可以使用PQinstanceData、PQsetInstanceData、PQresultInstanceData和PQsetResultInstanceData函数操纵。注意和转移指针不同，一个PGconn的实例数据不会被从它创建的PGresult自动继承。libpq不知道转移和实例数据指针指向的是什么（如果有），并且将不会尝试释放它们 — 那是事件处理器的责任。

### 事件类型

枚举PGEventId命名了事件系统处理的事件类型。它的所有值的名称都以PGEVT开始。对于每一种事件类型，都有一个相应的事件信息结构用来承载传递给事件处理器的参数。事件类型是：

PGEVT\_REGISTER

当PQregisterEventProc被调用时，注册事件会发生。这是一个初始化事件过程可能需要的每一个instanceData的最佳时机。每个连接的每个事件处理器只会触发一个注册事件。如果该事件过程失败，注册会被中止。

typedef struct

{

PGconn \*conn;

} PGEventRegister;

当收到一个PGEVT\_REGISTER事件时，evtInfo指针应该被转换为PGEventRegister \*。这个结构包含一个状态应该为CONNECTION\_OK的PGconn，保证在得到一个良好的PGconn之后能马上调用PQregisterEventProc。当返回一个失败代码时，所有的清理都必须被执行而不会发送PGEVT\_CONNDESTROY事件。

PGEVT\_CONNRESET

连接重置事件在PQreset或PQresetPoll完成时被触发。在两种情况中，只有重置成功才会触发该事件。如果事件过程失败，整个连接重置将失败，PGconn会被置为CONNECTION\_BAD状态并且PQresetPoll将返回PGRES\_POLLING\_FAILED。

typedef struct

{

PGconn \*conn;

} PGEventConnReset;

当收到一个PGEVT\_CONNRESET事件时，evtInfo指针应该被转换为PGEventConnReset \*。

尽管所包含的PGconn刚被重置，所有的事件数据还是保持不变。这个事件应该被用来重置/重载/重新查询任何相关的instanceData。注意即使事件过程无法处理PGEVT\_CONNRESET，它仍将在连接被关闭时接收到一个PGEVT\_CONNDESTROY事件。

PGEVT\_CONNDESTROY

为了响应PQfinish，连接销毁事件会被触发。由于 libpq 没有能力管理事件数据，事件过程有责任正确地清理它的事件数据。清理失败将会导致内存泄露。

typedef struct

{

PGconn \*conn;

} PGEventConnDestroy;

当接收到一个PGEVT\_CONNDESTROY事件时，evtInfo指针应该被转换为PGEventConnDestroy \*。这个事件在PQfinish执行任何其他清理之前被触发。该事件过程的返回值被忽略，因为没有办法指示一个来自PQfinish的失败。还有，一个事件过程失败不该中断对不需要的内存的清理。

PGEVT\_RESULTCREATE

为了响应任何生成一个结果的查询执行函数，结果创建事件会被触发。这些函数包括PQgetResult。这个事件只有在结果被成功地创建之后才会被触发。

typedef struct

{

PGconn \*conn;

PGresult \*result; } PGEventResultCreate;

当接收到一个PGEVT\_RESULTCREATE事件时，evtInfo指针应该被转换为PGEventResultCreate \*。conn是用来产生结果的连接。这是初始化任何需要与结果关联的instanceData的理想位置。如果该事件过程失败，结果将被清除并且失败将会被传播。该事件过程不能尝试自己PQclear结果对象。当返回一个失败代码时，所有清理必须被执行而不会发送PGEVT\_RESULTDESTROY事件。

PGEVT\_RESULTCOPY

为了响应PQcopyResult，结果复制事件会被触发。这个事件只会在复制完成后才被触发。只有成功地处理了PGEVT\_RESULTCREATE和PGEVT\_RESULTCOPY事件的事件过程才将会收到PGEVT\_RESULTCOPY事件。

typedef struct

{

const PGresult \*src;

PGresult \*dest;

} PGEventResultCopy;

当收到一个PGEVT\_RESULTCOPY事件时，evtInfo指针应该被转换为PGEventResultCopy \*。src结果是要被复制的，而dest结果则是复制的目的地。这个事件可以被用来提供instanceData的一份深度副本，因为PQcopyResult没法这样做。如果该事件过程失败，整个复制操作将失败并且dest结果将被清除。当返回一个失败代码时，所有清理必须被执行而不会为目标结果发送PGEVT\_RESULTDESTROY事件。

PGEVT\_RESULTDESTROY

为了响应PQclear，结果销毁事件会被触发。由于 libpq 没有能力管理事件数据，事件过程有责任正确地清理它的事件数据。清理失败将会导致内存泄露。

typedef struct

{

PGresult \*result;

} PGEventResultDestroy;

当接收到一个PGEVT\_RESULTDESTROY事件时，evtInfo指针应该被转换为PGEventResultDestroy \*。这个事件在PQclear执行任何其他清理之前被触发。该事件过程的返回值被忽略，因为没有办法指示来自PQclear的失败。还有，一个事件过程失败不该中断不需要的内存的清理过程。

### 事件回调函数

PGEventProc

PGEventProc是到一个事件过程的指针的 typedef，也就是从 libpq 接收事件的用户回调函数。一个事件过程的原型必须是 int eventproc(PGEventId evtId, void \*evtInfo, void \*passThrough) evtId指示发生了哪一个PGEVT事件。evtInfo指针必须被转换为合适的结构类型才能获得关于事件的进一步信息。当事件过程已被注册时，passThrough参数是提供给PQregisterEventProc的指针。如果成功，该函数应该返回非零值，失败则返回零。

在任何一个PGconn中，一个特定事件过程只能被注册一次。这是因为该过程的地址被用作查找键来标识相关的实例数据。

+—————————————————————————————————————————————————————————————————————————————————————————————————+  
| 小心： |  
| |  
| 在 Windows 上，函数能够有两个不同的地址：一个对 DLL 之外可见而另一个对 DLL 之内可见。我们应当小心只有其中之一会被用于libpq的事件 过程函数，否则将会产生混淆。编写代码的最简单规则是将所有的事件过程声明为static。如果过程的地址必须对它自己的源代码文件之外可见，提供一个单独的函数来返回该地址。 |  
+—————————————————————————————————————————————————————————————————————————————————————————————————+

### 事件支持函数

PQregisterEventProc

为 libpq 注册一个事件回调过程。

int PQregisterEventProc(PGconn \*conn, PGEventProc proc,

const char \*name, void \*passThrough);

在每一个你想要接收事件的PGconn上必须注册一个事件过程。和内存不同，没有限制说一个连接上能注册多少个事件过程。如果该函数成功，它会返回一个非零值。如果它失败，则会返回零。

当一个 libpq 事件被触发时，proc参数将被调用。它的内存地址也被用来查找instanceData。name参数被用来在错误消息中引用该事件过程。这个值不能是NULL或一个零长度串。名字串被复制到PGconn中，因此传递进来的东西不需要长期存在。当一个事件发生时，passThrough指针被传递给proc。这个参数可以是NULL。

PQsetInstanceData

设置连接conn的用于过程proc的instanceData为data。它在成功时返回非零值，失败时返回零（只有proc没有被正确地注册在conn中，才可能会失败）。

int PQsetInstanceData(PGconn \*conn, PGEventProc proc, void \*data);

PQinstanceData

返回连接conn的与过程proc相关的instanceData，如果没有则返回NULL。

void \*PQinstanceData(const PGconn \*conn, PGEventProc proc);

PQresultSetInstanceData

把结果的用于proc的instanceData设置为data。成功返回非零，失败返回零（只有proc没有被正确地注册在conn中，才可能会失败）。

int PQresultSetInstanceData(PGresult \*res, PGEventProc proc, void \*data);

请注意，data表示的任何存储都不会由PQresultMemorySize考虑，除非使用PQresultAlloc分配。（这样做是值得推荐的，因为它消除了在销毁结果时显式释放此类存储的需要。）

PQresultInstanceData

返回结果的与过程proc相关的instanceData，如果没有则返回NULL。

void \*PQresultInstanceData(const PGresult \*res, PGEventProc proc);

### 事件实例

这里是一个管理与 libpq 连接和结果相关的私有数据的例子的框架。

/\* 要求 libpq 事件的头文件（注意：包括 libpq-fe.h） \*/

#include <libpq-events.h>

/\* instanceData \*/

typedef struct

{

int n;

char \*str;

} mydata;

/\* PGEventProc \*/

static int myEventProc(PGEventId evtId, void \*evtInfo, void \*passThrough);

int

main(void)

{

mydata \*data;

PGresult \*res;

PPGconn \*conn =

PQconnectdb("dbname=highgo options=-csearch\_path=");

if (PQstatus(conn)!= CONNECTION\_OK)

{

fprintf(stderr, "Connection to database failed: %s",

PQerrorMessage(conn));

PQfinish(conn);

return 1;

}

/\* 在任何应该接收事件的连接上调用一次。

\* 发送一个 PGEVT\_REGISTER 给 myEventProc。

\*/

if (!PQregisterEventProc(conn, myEventProc, "mydata\_proc", NULL))

{

fprintf(stderr, "Cannot register PGEventProc\\n");

PQfinish(conn);

return 1;

}

/\* conn 的 instanceData 可用 \*/

data = PQinstanceData(conn, myEventProc);

/\* 发送一个 PGEVT\_RESULTCREATE 给 myEventProc \*/

res = PQexec(conn, "SELECT 1 + 1");

/\* 结果的 instanceData 可用 \*/

data = PQresultInstanceData(res, myEventProc);

/\* 如果使用了 PG\_COPYRES\_EVENTS，发送一个 PGEVT\_RESULTCOPY 给 myEventProc \*/

res\_copy = PQcopyResult(res, PG\_COPYRES\_TUPLES | PG\_COPYRES\_EVENTS);

/\* 如果在 PQcopyResult 调用时使用了 PG\_COPYRES\_EVENTS，结果的 instanceData可用。\*/

data = PQresultInstanceData(res\_copy, myEventProc);

/\* 两个清除都发送一个 PGEVT\_RESULTDESTROY 给 myEventProc \*/

PQclear(res);

PQclear(res\_copy);

/\* 发送一个 PGEVT\_CONNDESTROY 给 myEventProc \*/

PQfinish(conn);

return 0;

}

static int

myEventProc(PGEventId evtId, void \*evtInfo, void \*passThrough)

{

switch (evtId)

{

case PGEVT\_REGISTER:

{

PGEventRegister \*e = (PGEventRegister \*)evtInfo;

mydata \*data = get\_mydata(e->conn);

/\* 将应用相关的数据与连接关联起来 \*/

PQsetInstanceData(e->conn, myEventProc, data);

break;

}

case PGEVT\_CONNRESET:

{

PGEventConnReset \*e = (PGEventConnReset \*)evtInfo;

mydata \*data = PQinstanceData(e->conn, myEventProc);

if (data)

memset(data, 0, sizeof(mydata));

break;

}

case PGEVT\_CONNDESTROY:

{

PGEventConnDestroy \*e = (PGEventConnDestroy \*)evtInfo;

mydata \*data = PQinstanceData(e->conn, myEventProc);

/\* 因为连接正在被销毁，释放示例数据 \*/

if (data)

free\_mydata(data);

break;

}

case PGEVT\_RESULTCREATE:

{

PGEventResultCreate \*e = (PGEventResultCreate \*)evtInfo;

mydata \*conn\_data = PQinstanceData(e->conn, myEventProc);

mydata \*res\_data = dup\_mydata(conn\_data);

/\* 把应用相关的数据与结果（从 conn 复制过来）关联起来 \*/

PQsetResultInstanceData(e->result, myEventProc, res\_data);

break;

}

case PGEVT\_RESULTCOPY:

{

PGEventResultCopy \*e = (PGEventResultCopy \*)evtInfo;

mydata \*src\_data = PQresultInstanceData(e->src, myEventProc);

mydata \*dest\_data = dup\_mydata(src\_data);

/\* 把应用相关的数据与结果（从一个结果复制过来）关联起来 \*/

PQsetResultInstanceData(e->dest, myEventProc, dest\_data);

break;

}

case PGEVT\_RESULTDESTROY:

{

PGEventResultDestroy \*e = (PGEventResultDestroy \*)evtInfo;

mydata \*data = PQresultInstanceData(e->result, myEventProc);

/\* 因为结果正在被销毁，释放实例数据 \*/

if (data)

free\_mydata(data);

break;

}

/\* 未知事件 ID，只返回true。\*/

default:

break;

}

return true; /\* 事件处理成功 \*/

}

## 环境变量

下列环境变量能被用于选择默认的连接参数值，如果调用代码没有直接指定值，它们将被用于PQconnectdb、PQsetdbLogin和PQsetdb。例如，这些有助于防止数据库连接信息被硬编码到简单的客户端应用中。

• PGHOST的行为和host连接参数相同。

• PGHOSTADDR的行为和hostaddr连接参数相同。可以设置它来替代或者作为PGHOST的补充来防止 DNS 查找负担。

• PGPORT的行为和port连接参数相同。

• PGDATABASE的行为和dbname连接参数相同。

• PGUSER的行为和user连接参数相同。

• PGPASSWORD的行为和password连接参数相同。出于安全原因，我们不推荐使用这个环境变量，因为某些操作系统允许非根用户通过ps看到进程的环境变量。可以考虑使用一个口令文件（ 详见此节 ）。

• PGPASSFILE的行为和passfile连接参数相同。

• PGSERVICEFILE指定针对每个用户的连接服务文件名。如果没有设置，默认为~/.pg\_service.conf（ 详见此节 ）。

• PGOPTIONS的行为和options连接参数相同。

• PGAPPNAME的行为和application\_name连接参数相同。

• PGSSLMODE的行为和sslmode连接参数相同。

• PGREQUIRESSL的行为和requiressl连接参数相同。为了支持PGSSLMODE变量，这个环境变量已被废弃。同时设置两个变量会抑制这一个的效果。

• PGSSLCOMPRESSION的行为和sslcompression连接参数相同。

• PGSSLCERT的行为和sslcert连接参数相同。

• PGSSLKEY的行为和sslkey连接参数相同。

• PGSSLROOTCERT的行为和sslrootcert连接参数相同。

• PGSSLCRL的行为和sslcrl连接参数相同。

• PGREQUIREPEER的行为和requirepeer连接参数相同。

• PGGSSENCMODE 的行为和 gssencmode连接参数相同。

• PGKRBSRVNAME的行为和krbsrvname连接参数相同。

• PGGSSLIB的行为和gsslib连接参数相同。

• PGCONNECT\_TIMEOUT的行为和connect\_timeout连接参数相同。

• PGCLIENTENCODING的行为和client\_encoding连接参数相同。

• PGTARGETSESSIONATTRS的行为和target\_session\_attrs连接参数相同。

下面的环境变量可用来为每一个会话指定默认行为（为每一个用户或每一个数据库设置默认行为的方法还可见ALTER ROLE和ALTER DATABASE命令）。

• PGDATESTYLE设置日期/时间表示的默认风格（等同于SET datestyle TO...）。

• PGTZ设置默认的时区（等同于SET timezone TO...）。

• PGGEQO为遗传查询优化器设置默认模式（等同于SET geqo TO...）。

这些环境变量的正确值可参考SQL 命令 SET。

下面的环境变量决定libpq的内部行为，它们会覆盖编译在程序中的默认值。

• PGSYSCONFDIR设置包含pg\_service.conf文件以及未来版本中可能出现的其他系统范围配置文件的目录。

## 口令文件

一个用户主目录中的.pgpass文件能够包含在连接需要时使用的口令（并且其他情况不会指定口令）。在微软的 Windows 上该文件被命名为%APPDATA%\\postgresql\\pgpass.conf（其中%APPDATA%指的是用户配置中的应用数据子目录）。另外，可以使用连接参数passfile或者环境变量PGPASSFILE指定一个口令文件。

这个文件应该包含下列格式的行：

hostname:port:database:username:password

（你可以向该文件增加一个提醒：把上面的行复制到该文件并且在前面加上#）。前四个域的每一个都可以是文字值或者匹配任何东西的\*。第一个匹配当前连接参数的行中的口令域将被使用（因此，在使用通配符时把更特殊的项放在前面）。如果一个条目需要包含:或者\\，用\\对该字符转义。如果指定了host连接参数，主机名字段会被匹配到host，否则如果指定了hostaddr参数则匹配到hostaddr，如果两者都没有给出，则会搜索主机名localhost。当连接是一个Unix域套接字连接并且host参数匹配libpq的默认套接字目录路径时，也会搜索主机名localhost。在一台后备服务器上，值为replication的数据库字段匹配连接到主服务器的里复制连接。否则数据库字段的用途有限，因为用户对同一个集簇中的所有数据库都有相同的口令。

在 Unix 系统上，口令文件上的权限必须不允许所有人或组内访问，可以用chmod 0600 ~/.pgpass这样的命令实现。如果权限没有这么严格，该文件将被忽略。在微软 Windows上，该文件被假定存储在一个安全的目录中，因此不会进行特别的权限检查。

## 连接服务文件

连接服务文件允许 libpq 连接参数与一个单一服务名称关联。那个服务名称可以被一个 libpq 连接指定，与其相关的设置将被使用。这允许在不重新编译 libpq 应用的前提下修改连接参数。服务名称也可以被使用PGSERVICE环境变量来指定。

连接服务文件可以是每个用户都有一个的服务文件，它位于~/.pg\_service.conf或者环境变量PGSERVICEFILE指定的位置。它也可以是一个系统范围的文件，位于\`pg\_config -- sysconfdir\`/pg\_service.conf的或者环境变量PGSYSCONFDIR指定的目录。如果相同名称的服务定义存在于用户和系统文件中，用户文件将优先考虑。

该文件使用一种”INI 文件”格式，其中小节名是服务名并且参数是连接参数。列表 见前文 。例如：

\# comment

\[mydb\]

host=somehost

port=5433

user=admin

share/pg\_service.conf.sample中提供了一个例子文件。

## 连接参数的 LDAP 查找

如果libpq已经在编译时打开了 LDAP 支持（configure的选项--with-ldap），就可以通过 LDAP 从一个中央服务器检索host或dbname之类的连接参数。这样做的好处是如果一个数据库的连接参数改变，不需要在所有的客户端机器上更新连接信息。

LDAP 连接参数查找使用连接服务文件pg\_service.conf（ 详见前文 ）。pg\_service.conf中一个以ldap://开始的行将被识别为一个 LDAP URL 并且将执行一个 LDAP 查询。结果必须是一个keyword = value对列表，它将被用来设置连接选项。URL 必须遵循 RFC 1959 并且是形式 ldap://\[hostname\[:port\]\]/search\_base?attribute?search\_scope?filter

其中hostname默认为localhost并且port默认为389。

一次成功的 LDAP 查找后，pg\_service.conf的处理被终止。但是如果联系不上 LDAP 则会继续处理pg\_service.conf。这就提供了后手，可以加入更多指向不同 LDAP 服务器的 LDAPURL 行、经典的keyword = value对或者默认连接选项。如果你宁愿在这种情况下得到一个错误消息，在该 LDAP URL 之后增加一个语法错误的行。

一个和 LDIF 文件一起创建的 LDAP 条目实例：

version:1

dn:cn=mydatabase,dc=mycompany,dc=com

changetype:add

objectclass:top

objectclass:groupOfUniqueNames

cn:mydatabase

uniqueMember:host=dbserver.mycompany.com

uniqueMember:port=5439

uniqueMember:dbname=mydb

uniqueMember:user=mydb\_user

uniqueMember:sslmode=require

可以用下面的 LDAP URL 查询：

ldap://ldap.mycompany.com/dc=mycompany,dc=com?uniqueMember?one?(cn=mydatabase)

你也可以将常规的服务文件条目和 LDAP 查找混合。pg\_service.conf中一节的完整例子：

version:1

dn:cn=mydatabase,dc=mycompany,dc=com

changetype:add

objectclass:top

objectclass:device

cn:mydatabase

description:host=dbserver.mycompany.com

description:port=5439

description:dbname=mydb

description:user=mydb\_user

description:sslmode=require

可以用下面的 LDAP URL 查询到：

ldap://ldap.mycompany.com/dc=mycompany,dc=com?description?one?(cn=mydatabase)

## SSL 支持

HGDB本地支持使用SSL连接加密客户端/服务器通信以提高安全性。

libpq读取系统范围的OpenSSL配置文件。默认情况下，这个文件被命名为openssl.cnf并且位于openssl version -d所报告的目录中。可以通过设置环境变量OPENSSL\_CONF把这个默认值覆盖为想要的配置文件的名称。

### 服务器证书的客户端验证

默认情况下，hgdb将不会执行服务器证书的任何验证。这意味着可以在不被客户端知晓的情况下伪造服务器身份（例如通过修改一个 DNS 记录或者接管服务器的 IP 地址）。为了阻止哄骗，客户端必须能够通过一条信任链验证服务器的身份。信任链可以这样建立：在一台计算机上放置一个根（自签名的）证书机构（CA）的证书并且在另一台计算机上放置一个由根证书签发的叶子证书。还可以使用一种”中间”证书，它由根证书签发并且可以签发叶子证书。

为了允许客户端验证服务器的身份，在客户端上放置一份根证书并且在服务器上放置由根证书签发的叶子证书。为了允许服务器验证客户端的身份，在服务器上放置一份根证书并且在客户端上放置由根证书签发的叶子证书。也可以使用一个或者更多个中间证书（通常与叶子证书存在一起）来将叶子证书链接到根证书。

一旦信任链被建立起来，客户端有两种方法验证服务器发过来的叶子证书。如果参数sslmode被设置为verify-ca，libpq将通过检查该证书是否链接到存储在客户端上的根证书来验证服务器。如果sslmode被设置为verify-full，libpq还将验证服务器的主机名匹配存储在服务器证书中的名称。如果服务器证书无法被验证，则SSL连接将失败。在大部分对安全性很敏感的环境中，推荐使用verify-full。

在verify-full模式中，主机名被拿来与证书的主体别名属性 匹配，或者在不存在类型dNSName的主体别名时与通用名称属性匹配。如果证书的名称属性以一个星号（\*）开始，这个星号将被 视作一个通配符，它将匹配所有除了句点（.）之外的字符。这意味着该证书将不会匹配子域。如果连接是使用一个 IP 地址而不是一个主机名创建的，该 IP 地址将被匹配（不做任何 DNS 查找）。

要允许服务器证书验证，必须将一个或者更多个根证书放置在用户主目录下的~/.postgresql/root.crt文件中（在Microsoft Windows上该文件名为%APPDATA%\\postgresql\\root.crt）。如果需要把服务器发来的证书链链接到存储在客户端的根证书，还应该将中间证书加到该文件中。

如果文件~/.postgresql/root.crl存在（微软 Windows 上的%APPDATA%\\postgresql \\root.crl），证书撤销列表（CRL）项也会被检查。

根证书文件和 CRL 的位置可以通过设置连接参数sslrootcert和sslcrl或环境变量PGSSLROOTCERT和PGSSLCRL改变。

| 注意： |
| --- |
| 为了与早期版本达到向后兼容，如果存在一个根CA 文件，sslmode=require的行为将与verify-ca相同，即服务器证书根据 CA 验证。我们鼓励依赖这种行为，并且需要证书验证的应用应该总是使用verify-ca或者verify-full。 |

### 客户端证书

如果服务器尝试通过请求客户端的叶子证书来验证客户端的身份，libpq将发送用户主目录下文件~/.postgresql/postgresql.crt中存储的证书。该证书必须链接到该服务器信任的根证书。也必须存在一个匹配的私钥文件~/.postgresql/postgresql.key。该私钥文件不能允许全部用户或者组用户的任何访问，可以通过命令chmod 0600 ~/.postgresql/ postgresql.key实现。在微软 Windows 上这些文件被命名为%APPDATA%\\postgresql\\postgresql.crt和%APPDATA%\\postgresql\\postgresql.key，不会有特别的权限检查，因为该目录已经被假定为安全。证书和密钥文件的位置可以使用连接参数sslcert和sslkey或者环境变量PGSSLCERT和PGSSLKEY覆盖。

postgresql.crt中的第一个证书必须是客户端的证书，因为它必须匹配客户端的私钥。可以选择将”中间”证书追加到该文件 — 这样做避免了在服务器上存放中间证书的要求（ssl\_ca\_file）。

### 不同模式中提供的保护

sslmode参数的不同值提供了不同级别的保护。SSL 能够针对三类攻击提供保护：

窃听

如果一个第三方能够检查客户端和服务器之间的网络流量，它能读取连接信息（包括用户名和口令）以及被传递的数据。SSL使用加密来阻止这种攻击。

中间人（MITM）

如果一个第三方能对客户端和服务器之间传送的数据进行修改，它就能假装是服务器并且因此能看见并且修改数据，即使这些数据已被加密。然后第三方可以将连接信息和数据转送给原来的服务器，使得它不可能检测到攻击。这样做的通常途径包括 DNS 污染和地址劫持，借此客户端被重定向到一个不同的服务器。还有几种其他的攻击方式能够完成这种攻击。SSL使用证书验证让客户端认证服务器，就可以阻止这种攻击。

模仿

如果一个第三方能假装是一个授权的客户端，它能够简单地访问它本不能访问的数据。通常这可以由不安全的口令管理所致。SSL使用客户端证书来确保只有持有合法证书的客户端才能访问服务器，这样就能阻止这种攻击。

对于一个已知的SSL-secured连接，在连接被建立之前，SSL 使用必须被配置在客户端和服务器之上。如果只在服务器上配置，客户端在知道服务器要求高安全性之前可能会结束发送敏感信息（例如口令）。在 libpq 中，要确保连接安全，可以设置sslmode参数为verifyfull或verify-ca并且为系统提供一个根证书用来验证。这类似于使用一个https URL进行加密网页浏览。

一旦服务器已经被认证，客户端可以传递敏感数据。这意味着直到这一点，客户端都不需要知道是否证书将被用于认证，这样只需要在服务器配置中指定就比较安全。

所有SSL选项都带来了加密和密钥交换的负荷，因此必须在性能和安全性之间做出平衡。如下表说明了不同sslmode值所保护的风险，以及它们是怎样看待安全性和负荷的。

| sslmode | 窃听保护 | MITM保护 | 声明 |
| --- | --- | --- | --- |
| disable | No | No | 我不关心安全性，并且我不想为加密增加负荷。 |
| allow | 可能 | No | 我不关心安全性，但如果服务器坚持，我将承担加密带来的负荷。 |
| prefer | 可能 | No | 我不关心安全性，但如果服务器支持，我希望承担加密带来的负荷。 |
| require | Yes | No | 我想要对数据加密，并且我接受因此带来的负荷。我信任该网络会保证我总是连接到想要连接的服务器。 |
| verify-ca | Yes | Depends on CA policy | 我想要对数据加密，并且我接受因此带来的负荷。我想要确保我连接到的是我信任的服务器。 |
| verify-full | Yes | Yes | 我想要对数据加密并且我接受因此带来的负荷。我想要确保我连接到的是我信任的服务器，并且就是我指定的那一个。 |

: 表 1.1 SSL 模式描述

verify-ca和verify-full之间的区别取决于根CA的策略。如果使用了一个公共CA，verify-ca允许连接到那些可能已经被其他人注册到该CA的服务器。在这种情况下，总是应该使用verify-full。如果使用了一个本地CA或者甚至是一个自签名的证书，使用verify-ca常常就可以提供足够的保护。

sslmode的默认值是prefer。如表中所示，这在安全性的角度来说没有意义，并且它只承诺可能的性能负荷。提供它作为默认值只是为了向后兼容，并且我们不推荐在安全部署中使用它。

### SSL 客户端文件使用

下表总结了与客户端 SSL 设置相关的文件。

| 文件 | 内容 | 效果 |
| --- | --- | --- |
| ~/.postgresql/postgresql.crt | 客户端证书 | 由服务器要求 |
| ~/.postgresql/postgresql.key | 客户端私钥 | 证明客户端证书是由拥有者发送；不代表证书拥有者可信 |
| ~/.postgresql/root.crt | 可信的证书机构 | 检查服务器证书是由一个可信的证书机构签发 |
| ~/.postgresql/root.crl | 被证书机构撤销的证书 | 服务器证书不能在这个列表上 |

: 表 1.2 Libpq/客户端 SSL 文件用法

### SSL 库初始化

如果你的应用初始化libssl或libcrypto库以及带有SSL支持的libpq，你应该调用PQinitOpenSSL来告诉libpq：libssl或libcrypto库已经被你的应用初始化，这样libpq将不会也去初始化那些库。关于 SSL API 详见 [http://h71000.www7.hp.com/doc/83final/](http://h71000.www7.hp.com/doc/83final/) ba554\_90007/ch04.html。

PQinitOpenSSL

允许应用选择要初始化哪个安全性库。

void PQinitOpenSSL(int do\_ssl, int do\_crypto);

当do\_ssl是非零时，libpq将在第一次打开数据库连接前初始化OpenSSL库。

当do\_crypto是非零时，libcrypto库将被初始化。默认情况下（如果没有调用PQinitOpenSSL），两个库都会被初始化。当 SSL 支持没有被编译时，这个函数也存在但是什么也不做。

如果你的应用使用并且初始化OpenSSL或者它的底层libcrypto库，你必须在第一次打开数据库连接前以合适的非零参数调用这个函数。同时要确保在打开一个数据库连接前已经完成了初始化。

PQinitSSL

允许应用选择要初始化哪个安全性库。

void PQinitSSL(int do\_ssl);

这个函数等效于PQinitOpenSSL(do\_ssl, do\_ssl)。这对于要么初始化OpenSSL以及libcrypto要么都不初始化的应用足够用了。

## 在线程化程序中的行为

libpq默认是可再入的并且是线程安全的。你可能需要使用特殊的编译器命令行选项来编译你的应用代码。参考你的系统文档来了解如何编译启用线程的应用，或者在src/Makefile.global中查找PTHREAD\_CFLAGS和PTHREAD\_LIBS。这个函数允许查询libpq的线程安全状态：

PQisthreadsafe

返回libpq库的线程安全状态。

int PQisthreadsafe();

如果libpq是线程安全的则返回 1，否则返回 0。

一个线程限制是不允许两个线程同时尝试操纵同一个PGconn对象。特别是你不能从不同的线程通过同一个连接对象发出并发的命令（如果你需要运行并发命令，请使用多个连接）。

PGresult对象在创建后通常是只读的，并且因此可以在线程之间自由地被传递。但是，如果你使用任何前文中描述的PGresult修改函数，你需要负责避免在同一个PGresult上的并发操作。

被废弃的函数PQrequestCancel以及PQoidStatus不时线程安全的并且不应当在多线程程序中使用。PQrequestCancel可以被替换为PQcancel。PQoidStatus可以被替换为PQoidValue。

如果你在应用中使用 Kerberos (除了在libpq中之外），你将需要对 Kerberos 调用加锁，因为 Kerberos 函数不是线程安全的。参考libpq源代码中的PQregisterThreadLock函数，那里有在libpq和应用之间做合作锁定的方法。

如果你在线程化应用中碰到问题，将该程序运行在src/tools/thread来查看是否你的平台有线程不安全的函数。这个程序会被configure运行，但是对于二进制发布，你的库可能不匹配用来编译二进制的库。

## 编译 libpq 程序

要编译（即编译并且链接）一个使用libpq的程序，你需要做下列所有的事情：

• 包括libpq-fe.h头文件：

#include <libpq-fe.h>

如果你无法这样做，那么你通常会从你的编译器得到像这样的错误消息：foo.c: In function \`main':

foo.c:34: \`PGconn' undeclared (first use in this function)

foo.c:35: \`PGresult' undeclared (first use in this function)

foo.c:54: \`CONNECTION\_BAD' undeclared (first use in this function)

foo.c:68: \`PGRES\_COMMAND\_OK' undeclared (first use in this function)

foo.c:95: \`PGRES\_TUPLES\_OK' undeclared (first use in this function)

• 通过为你的编译器提供-Idirectory选项，向你的编译器指出HGDB头文件安装在哪里（在某些情况下编译器默认将查看该目录，因此你可以忽略这个选项）。例如你的编译命令行可能看起来像：

cc -c -I/usr/local/pgsql/include testprog.c

如果你在使用 makefile，那么把该选项加到CPPFLAGS变量中：

CPPFLAGS += -I/usr/local/pgsql/include

如果你的程序可能由其他用户编译，那么你不应该像那样硬编码目录位置。你可以运行工具pg\_config在本地系统上找出头文件在哪里：

$ pg\_config --includedir

/usr/local/include

如果你安装了pkg-config，你可以运行：

$ pkg-config --cflags libpq

\-I/usr/local/include

注意这将在路径前面包括-I。

无法为编译器指定正确的选项将导致一个错误消息，例如：

testlibpq.c:8:22: libpq-fe.h: No such file or directory

• 当链接最终的程序时，指定选项-lpq，这样libpq库会被编译进去，也可以用选项- Ldirectory向编译器指出libpq库所在的位置（再次，编译器将默认搜索某些目录）。为了最大的可移植性，将-L选项放在-lpq选项前面。例如：

cc -o testprog testprog1.o testprog2.o -L/usr/local/pgsql/lib -lpq

你也可以使用pg\_config找出库目录：

$ pg\_config --libdir

/usr/local/pgsql/lib

或者再次使用pkg-config：

$ pkg-config --libs libpq

\-L/usr/local/pgsql/lib -lpq

再次提示这会打印出全部的选项，而不仅仅是路径。

指出这一部分问题的错误消息可能看起来像：

testlibpq.o: In function \`main':

testlibpq.o(.text+0x60): undefined reference to \`PQsetdbLogin'

testlibpq.o(.text+0x71): undefined reference to \`PQstatus'

testlibpq.o(.text+0xa4): undefined reference to \`PQerrorMessage'

This means you forgot -lpq.

/usr/bin/ld: cannot find -lpq

这意味着你忘记了-L选项或者没有指定正确的目录。

## 例子程序

这些例子和其他例子可以在源代码发布的src/test/examples目录中找到。

例 libpq 例子程序 1

/\*

\* src/test/examples/testlibpq.c

\*

\*

\* testlibpq.c

\*

\* 测试 libpq（前端库） 的C版本。

\*/

#include <stdio.h>

#include <stdlib.h>

#include "libpq-fe.h"

static void

exit\_nicely(PGconn \*conn)

{

PQfinish(conn);

exit(1);

}

int

main(int argc, char \*\*argv)

{

const char \*conninfo;

PGconn \*conn;

PGresult \*res;

int nFields;

int i,

j;

/\*

\* 如果用户在命令行上提供了一个参数，将它用作连接信息串。

\* 否则默认用设置 dbname=highgo 并且为所有其他链接参数使用环境变量或默认值。

\*/

if (argc > 1)

conninfo = argv\[1\];

else

conninfo = "dbname = highgo";

/\* 建立到数据库的一个连接 \*/

conn = PQconnectdb(conninfo);

/\* 检查看后端连接是否成功建立 \*/

if (PQstatus(conn)!= CONNECTION\_OK)

{

fprintf(stderr, "Connection to database failed: %s",

PQerrorMessage(conn));

exit\_nicely(conn);

}

/\* 设置总是安全的搜索路径，这样恶意用户就无法取得控制。\*/

res = PQexec(conn,

"SELECT pg\_catalog.set\_config('search\_path', '', false)");

if (PQresultStatus(res)!= PGRES\_TUPLES\_OK)

{

fprintf(stderr, "SET failed: %s", PQerrorMessage(conn));

PQclear(res);

exit\_nicely(conn);

}

/\*

\* 任何时候不再需要 PGresult 时，应该 PQclear 它来避免内存泄露

\*/

PQclear(res);

/\*

\* 我们的测试案例这里涉及使用一个游标，对它我们必须用在一个事务块内。

\* 我们可以在一个单一的 "select \* from pg\_database" 的 PQexec() 中做整个事情，

\* 但是作为一个好的例子它太琐碎。

\*/

/\* 开始一个事务块 \*/

res = PQexec(conn, "BEGIN");

if (PQresultStatus(res)!= PGRES\_COMMAND\_OK)

{

fprintf(stderr, "BEGIN command failed: %s", PQerrorMessage(conn));

PQclear(res);

exit\_nicely(conn);

}

PQclear(res);

/\*

\* 从 pg\_database 取得行，它是数据库的系统目录

\*/

res = PQexec(conn, "DECLARE myportal CURSOR FOR select \* from pg\_database");

if (PQresultStatus(res)!= PGRES\_COMMAND\_OK)

{

fprintf(stderr, "DECLARE CURSOR failed: %s", PQerrorMessage(conn));

PQclear(res);

exit\_nicely(conn);

}

PQclear(res);

res = PQexec(conn, "FETCH ALL in myportal");

if (PQresultStatus(res)!= PGRES\_TUPLES\_OK)

{

fprintf(stderr, "FETCH ALL failed: %s", PQerrorMessage(conn));

PQclear(res);

exit\_nicely(conn);

}

/\* 首先，打印出属性名 \*/

nFields = PQnfields(res);

for (i = 0; i < nFields; i++)

printf("%-15s", PQfname(res, i));

printf("\\n\\n");

/\* 接下来，打印出行 \*/

for (i = 0; i < PQntuples(res); i++)

{

for (j = 0; j < nFields; j++)

printf("%-15s", PQgetvalue(res, i, j));

printf("\\n");

}

PQclear(res);

/\* 关闭入口，我们不需要考虑检查错误 \*/

res = PQexec(conn, "CLOSE myportal");

PQclear(res);

/\* 结束事务 \*/

res = PQexec(conn, "END");

PQclear(res);

/\* 关闭到数据库的连接并且清理 \*/

PQfinish(conn);

return 0;

}

例 libpq例子程序 2

/\*

\* src/test/examples/testlibpq2.c

\*

\*

\* testlibpq2.c

\* 测试异步通知接口

\*

\* 开始这个程序，然后在另一个窗口的 psql 中做

\* NOTIFY TBL2;

\* 重复四次来让这个程序退出。

\*

\* 或者，如果你想要得到奇妙的事情，尝试：

\* 用下列命令填充一个数据库

\* （在 src/test/examples/testlibpq2.sql 中提供）

\*

\* CREATE SCHEMA TESTLIBPQ2;

\* SET search\_path = TESTLIBPQ2;

\* CREATE TABLE TBL1 (i int4);

\* CREATE TABLE TBL2 (i int4);

\* CREATE RULE r1 AS ON INSERT TO TBL1 DO

\* (INSERT INTO TBL2 VALUES (new.i); NOTIFY TBL2);

\*

\* 开始这个程序，然后从psql做下面的操作四次：

\*

\* INSERT INTO TESTLIBPQ2.TBL1 VALUES (10);

\*/

#ifdef WIN32

#include <windows.h>

#endif

#include <stdio.h>

#include <stdlib.h>

#include <string.h>

#include <errno.h>

#include <sys/time.h>

#include <sys/types.h>

#include "libpq-fe.h"

#ifdef HAVE\_SYS\_SELECT\_H

#include <sys/select.h>

#endif

static void

exit\_nicely(PGconn \*conn)

{

PQfinish(conn);

exit(1);

}

int

main(int argc, char \*\*argv)

{

const char \*conninfo;

PGconn \*conn;

PGresult \*res;

PGnotify \*notify;

int nnotifies;

/\*

\* 用过用户在命令行上提供了一个参数，将它用作连接信息串。

\* 否则默认用设置 dbname=highgo 并且为所有其他链接参数使用环境变量或默认值。

\*/

if (argc > 1)

conninfo = argv\[1\];

else

conninfo = "dbname = highgo";

/\* 建立一个到数据库的连接 \*/

conn = PQconnectdb(conninfo);

/\* 检查后端连接是否成功建立 \*/

if (PQstatus(conn)!= CONNECTION\_OK)

{

fprintf(stderr, "Connection to database failed: %s",

PQerrorMessage(conn));

exit\_nicely(conn);

}

/\* 设置总是安全的搜索路径，这样恶意用户就无法取得控制。\*/

res = PQexec(conn,

"SELECT pg\_catalog.set\_config('search\_path', '', false)");

if (PQresultStatus(res)!= PGRES\_TUPLES\_OK)

{

fprintf(stderr, "SET failed: %s", PQerrorMessage(conn));

PQclear(res);

exit\_nicely(conn);

}

/\*

\* 任何时候不再需要 PGresult 时，应该 PQclear 它来避免内存泄露

\*/

PQclear(res);

/\*

\* 发出 LISTEN 命令启用来自规则的 NOTIFY 的通知。

\*/

res = PQexec(conn, "LISTEN TBL2");

if (PQresultStatus(res)!= PGRES\_COMMAND\_OK)

{

fprintf(stderr, "LISTEN command failed: %s", PQerrorMessage(conn));

PQclear(res);

exit\_nicely(conn);

}

PQclear(res);

/\* 在接收到四个通知后退出。\*/

nnotifies = 0;

while (nnotifies < 4)

{

/\*

\* 休眠到在连接上发生某些事情。我们使用 select(2) 来等待输入，但是你也可以使用 poll() 或相似的设施。

\*/

int sock;

fd\_set input\_mask;

sock = PQsocket(conn);

if (sock < 0)

break; /\* 不应该发生 \*/

FD\_ZERO(&input\_mask);

FD\_SET(sock, &input\_mask);

if (select(sock + 1, &input\_mask, NULL, NULL, NULL) < 0)

{

fprintf(stderr, "select() failed: %s\\n", strerror(errno));

exit\_nicely(conn);

}

/\* 现在检查输入 \*/

PQconsumeInput(conn);

while ((notify = PQnotifies(conn))!= NULL)

{

fprintf(stderr,

"ASYNC NOTIFY of '%s' received from backend PID %d\\n",

notify->relname, notify->be\_pid);

PQfreemem(notify);

nnotifies++;

PQconsumeInput(conn);

}

}

fprintf(stderr, "Done.\\n");

/\* 关闭到数据库的连接并且清理 \*/

PQfinish(conn);

return 0;

}

例 libpq例子程序 3

/\*

\* src/test/examples/testlibpq3.c

\*

\*

\* testlibpq3.c

\* 测试线外参数和二进制 I/O。

\*

\* 在运行之前，使用下列命令填充一个数据库（在 src/test/examples/testlibpq3.sql中提供）

\*

\* CREATE SCHEMA testlibpq3;

\* SET search\_path = testlibpq3;

\* CREATE TABLE test1 (i int4, t text, b bytea);

\* INSERT INTO test1 values (1, 'joe''s place', '\\\\000\\\\001\\\\002\\\\003\\\\004');

\* INSERT INTO test1 values (2, 'ho there', '\\\\004\\\\003\\\\002\\\\001\\\\000');

\*

\* 期待的输出是：

\*

\* tuple 0: got

\* i = (4 bytes) 1

\* t = (11 bytes) 'joe's place'

\* b = (5 bytes) \\000\\001\\002\\003\\004

\*

\* tuple 0: got

\* i = (4 bytes) 2

\* t = (8 bytes) 'ho there'

\* b = (5 bytes) \\004\\003\\002\\001\\000

\*/

#ifdef WIN32

#include <windows.h>

#endif

#include <stdio.h>

#include <stdlib.h>

#include <stdint.h>

#include <string.h>

#include <sys/types.h>

#include "libpq-fe.h"

/\* for ntohl/htonl \*/

#include <netinet/in.h>

#include <arpa/inet.h>

static void

exit\_nicely(PGconn \*conn)

{

PQfinish(conn);

exit(1);

}

/\*

\* 这个函数打印一个查询结果，该结果以二进制格式从上面的注释中定义的表中取得。

\* 我们把它分离出来是因为 main() 函数需要使用它两次。

\*/

static void

show\_binary\_results(PGresult \*res)

{

int i,

j;

int i\_fnum,

t\_fnum,

b\_fnum;

/\* 使用 PQfnumber 来避免假定结果中域的顺序 \*/

i\_fnum = PQfnumber(res, "i");

t\_fnum = PQfnumber(res, "t");

b\_fnum = PQfnumber(res, "b");

for (i = 0; i < PQntuples(res); i++)

{

char \*iptr;

char \*tptr;

char \*bptr;

int blen;

int ival;

/\* 得到域值（我们忽略它们为空值的可能性！） \*/

iptr = PQgetvalue(res, i, i\_fnum);

tptr = PQgetvalue(res, i, t\_fnum);

bptr = PQgetvalue(res, i, b\_fnum);

/\*

\* INT4 的二进制表示是按照网络字节序的，我们最好强制为本地字节序。

\*/

ival = ntohl(\*((uint32\_t \*) iptr));

/\*

\* TEXT 的二进制表示是文本，并且因为 libpq 会为它追加一个零字节，它将工

作得和C字符串一样好。

\*

\* BYTEA 的二进制表示是一堆字节，其中可能包含嵌入的空值，因此我们必须注意域长度。

\*/

blen = PQgetlength(res, i, b\_fnum);

printf("tuple %d: got\\n", i);

printf(" i = (%d bytes) %d\\n",

PQgetlength(res, i, i\_fnum), ival);

printf(" t = (%d bytes) '%s'\\n",

PQgetlength(res, i, t\_fnum), tptr);

printf(" b = (%d bytes) ", blen);

for (j = 0; j < blen; j++)

printf("\\\\%03o", bptr\[j\]);

printf("\\n\\n");

}

}

int

main(int argc, char \*\*argv)

{

const char \*conninfo;

PGconn \*conn;

PGresult \*res;

const char \*paramValues\[1\];

int paramLengths\[1\];

int paramFormats\[1\];

uint32\_t binaryIntVal;

/\*

\* 如果用户在命令行上提供了一个参数，将它用作连接信息串。

\* 否则默认用设置 dbname=highgo 并且为所有其他链接参数使用环境变量或默认值。

\*/

if (argc > 1)

conninfo = argv\[1\];

else

conninfo = "dbname = highgo";

/\* 建立一个到数据库的连接 \*/

conn = PQconnectdb(conninfo);

/\* 检查看后端连接是否成功被建立 \*/

if (PQstatus(conn)!= CONNECTION\_OK)

{

fprintf(stderr, "Connection to database failed: %s",

PQerrorMessage(conn));

exit\_nicely(conn);

}

/\* 设置总是安全的搜索路径，这样恶意用户就无法取得控制。\*/

res = PQexec(conn, "SET search\_path = testlibpq3");

if (PQresultStatus(res)!= PGRES\_COMMAND\_OK)

{

fprintf(stderr, "SET failed: %s", PQerrorMessage(conn));

PQclear(res);

exit\_nicely(conn);

}

PQclear(res);

/\*

\* 这个程序的要点在于用线外参数展示 PQexecParams() 的使用，以及数据的二进制传输。

\*

\* 第一个例子将参数作为文本传输，但是以二进制格式接收结果。

\* 通过使用线外参数，我们能够避免使用繁杂的引用和转义，即便数据是文本。

\* 注意我们怎么才能对参数值中的引号不做任何事情。

\*/

/\* 这里是我们的线外参数值 \*/

paramValues\[0\] = "joe's place";

res = PQexecParams(conn,

"SELECT \* FROM test1 WHERE t = $1",

1, /\* 一个参数 \*/

NULL, /\* 让后端推导参数类型 \*/

paramValues,

NULL, /\* 因为文本不需要参数长度 \*/

NULL, /\* 对所有文本参数的默认值 \*/

1); /\* 要求二进制结果 \*/

if (PQresultStatus(res)!= PGRES\_TUPLES\_OK)

{

fprintf(stderr, "SELECT failed: %s", PQerrorMessage(conn));

PQclear(res);

exit\_nicely(conn);

}

show\_binary\_results(res);

PQclear(res);

/\*

\* 在第二个例子中，我们以二进制形式传输一个整数参数，并且再次以二进制形式接收结果。

\*

\* 尽管我们告诉 PQexecParams 我们让后端推导参数类型，我们实际上通过在查询文本中造型参数符号来强制该决定。

\* 在发送二进制参数时，这是一种好的安全测度。

\*/

/\* 将整数值 "2" 转换为网络字节序 \*/

binaryIntVal = htonl((uint32\_t) 2);

/\* 为 PQexecParams 设置参数数组 \*/

paramValues\[0\] = (char \*) &binaryIntVal;

paramLengths\[0\] = sizeof(binaryIntVal);

paramFormats\[0\] = 1; /\* binary \*/

res = PQexecParams(conn,

"SELECT \* FROM test1 WHERE i = $1::int4",

1, /\* 一个参数 \*/

NULL, /\* 让后端推导参数类型 \*/

paramValues,

paramLengths,

paramFormats,

1); /\* 要求二进制结果 \*/

if (PQresultStatus(res)!= PGRES\_TUPLES\_OK)

{

fprintf(stderr, "SELECT failed: %s", PQerrorMessage(conn));

PQclear(res);

exit\_nicely(conn);

}

show\_binary\_results(res);

PQclear(res);

/\* 关闭到数据库的连接并清理 \*/

PQfinish(conn);

return 0;

}