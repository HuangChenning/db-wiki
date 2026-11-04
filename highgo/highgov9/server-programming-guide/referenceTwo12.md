---
title: "后台工作者进程"
book: "服务器编程指南"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/reference/referenceTwo12.html"
tags:
  - highgo
  - highgo-v9
  - server-programming-guide
---

## 后台工作者进程

瀚高数据库可以被扩展来在独立进程中运行用户提供的代码。这种进程被postgres启动、停止和监控，这使它们的生命期与服务器的状态紧密联系。这些进程具有选项可以挂接上 瀚高数据库的共享内存区域，并且可以从内部连接到数据库。它们也可以连续地运行多个事务，就像一个正常的被客户端连接的服务器进程。同样，通过链接到libpq，它们可以连接到服务器并像一个正常客户端应用工作。

| 警告： |
| --- |
| 在使用后台工作者进程时具有相当大的鲁棒性和安全性风险，因为它们由C语言编写，对数据具有无限制的访问权。希望使用包括后台工作者进程在内的模块的管理员必须要极度小心。只有仔细审计过的模块才会被允许运行后台工作者进程。 |

通过将模块名放在shared\_preload\_libraries中，可以在瀚高数据库被启动时初始化后台工作者。一个希望运行后台工作者的模块需要通过在其\_PG\_init()中调用RegisterBackgroundWorker(BackgroundWorker \*worker)来注册它。也可以在系统启动后通过调用函数RegisterDynamicBackgroundWorker(BackgroundWorker \*worker, BackgroundWorkerHandle \*\*handle)来启动后台工作者。与只能在postmaster内调用的RegisterBackgroundWorker不同，必须从一个常规后端调用RegisterDynamicBackgroundWorker。

typedef void (\*bgworker\_main\_type)(Datum main\_arg);

typedef struct BackgroundWorker

{

char bgw\_name\[BGW\_MAXLEN\];

char bgw\_type\[BGW\_MAXLEN\];

int bgw\_flags;

BgWorkerStartTime bgw\_start\_time;

int bgw\_restart\_time; /\* in seconds, or BGW\_NEVER\_RESTART \*/

char bgw\_library\_name\[BGW\_MAXLEN\];

char bgw\_function\_name\[BGW\_MAXLEN\];

Datum bgw\_main\_arg;

char bgw\_extra\[BGW\_EXTRALEN\];

int bgw\_notify\_pid;

} BackgroundWorker;

bgw\_name和bgw\_type是要被用在日志消息、进程列表和类似环境中的字符串。对于同种类型的所有后台工作者，bgw\_type应该相同，例如这样才可能将进程列表中的这些工作组分组。

另一方面，bgw\_name可以包含有关特定进程的额外信息（通常，bgw\_name中的字符串在某种程度上也会包含类型，但是并没有严格的要求）。

bgw\_flags是一个按位与的位掩码，它用于指示模块想要的能力。可能的值是： BGWORKER\_SHMEM\_ACCESS

请求共享内存访问。没有共享内存使用权的工作者不能访问任何的瀚高数据库共享数据结构，例如重量级或者轻量级锁、共享缓冲区以及该工作者本身想要创建和使用的任何自定义数据结构。

BGWORKER\_BACKEND\_DATABASE\_CONNECTION

请求建立数据库连接的能力，这样它后面可以通过建立起的连接运行事务和查询。一个使用BGWORKER\_BACKEND\_DATABASE\_CONNECTION来连接一个数据库的后台工作者也必须使用BGWORKER\_SHMEM\_ACCESS挂接到共享内存，否则工作者启动将会失败。

bgw\_start\_time是服务器状态，在该状态中postgres会启动该进程，它可以

是BgWorkerStart\_PostmasterStart（在postgres本身完成初始化之后立即启动，这种进程不能使用数据库连接）、BgWorkerStart\_ConsistentState（当一个热后备中达到一个一致性状态之后立即启动，允许进程连接到数据库并运行只读查询）

和BgWorkerStart\_RecoveryFinished（在系统进入到正常读写状态后立即启动）之一。注意后两种值在服务器不是一个热后备的情况下是等同的。注意这种设置仅仅表示何时启动进程，当一个不同状态到达时它们不会停止。

bgw\_restart\_time是在崩溃情况下postgres启动进程之前等待的时间间隔，以秒计。它可以是任何正值，或者BGW\_NEVER\_RESTART，表示在出现崩溃后不重启进程。

bgw\_library\_name是应该在其中定位后台工作者初始入口点的库名称。所指的库将被工作者进程动态载入并且bgw\_function\_name将被用来标识要调用的函数。如果从核心代码载入一个函数，这必须被设置为"postgres"。

bgw\_function\_name是一个动态载入库中的一个函数名，该函数将被用作一个新后台工作者的初始入口点。

bgw\_main\_arg是后台工作者主函数的Datum参数。这个主函数应该有一个单一的Datum类型的参数，并且返回void。bgw\_main\_arg将被作为参数传递。此外，全局变量MyBgworkerEntry指向注册时传入的BackgroundWorker结构的一份拷贝，工作者会发现检查这个结构会很有用。

在 Windows （以及任何定义了EXEC\_BACKEND的地方）上或者动态后台工作者中，用引用的方式传递Datum是不安全的，只有传值才安全。如果要求一个参数，最安全的方式是传递一个 int32 或者其他的小型值，并且把它当做共享内存中分配的一个数组的索引来使用。如果被传递的是一个cstring或者text这样的值，那么在新的后台工作者进程中该指针将不会有效。

bgw\_extra可以包含要传递给后台工作者的额外数据。与bgw\_main\_arg不同，这个数据不会被作为一个参数传递给工作者的主函数，而是按照上面所述通过MyBgworkerEntry来访问。

bgw\_notify\_pid是一个瀚高数据库后端进程的PID， 当后台工作者进程启动或者退出时，postmaster会向这个PID所指的进程发送SIGUSR1。 对于在postmaster启动时注册的工作者，它应该为0；或者注册该工作者的后端不希望等待该工作者启动时，它也应该为0。否则，它应该被初始化为MyProcPid。

一旦运行起来，进程可以通过调用BackgroundWorkerInitializeConnection(char \*dbname, char \*username)或者BackgroundWorkerInitializeConnectionByOid(Oid dboid, Oid useroid)来连接到一个数据库。这使得该进程可以使用SPI接口运行事务和查询。 如果dbname为NULL或者dboid为InvalidOid，该会话没有连接到任何特定数据库，但共享的目录可以被访问。 如果username为NULL或者useroid为InvalidOid，该进程将以在initdb阶段创建的超级用户身份运行。如果BGWORKER\_BYPASS\_ALLOWCONN被指定为flags，就可以绕过该限制连接不允许用户连接的数据库。在每一个后台进程中，只能调用两者之一，并且只能调用一次，所以不可能切换数据库。

当控制到达后台工作者的主函数时，信号初始会被阻塞，并且必须被它解除阻塞。这是为了允许进程自定义它的信号处理器。在新进程中可以通过调用BackgroundWorkerUnblockSignals来解除对信号的阻塞，还可以通过调用BackgroundWorkerBlockSignals来阻塞信号。

如果一个后台工作者的bgw\_restart\_time被配置为 BGW\_NEVER\_RESTART，或者它退出时的退出码为0，又或者它是被 TerminateBackgroundWorker所终止，它将会被postmaster在退出时自动解除 注册。否则，它将在等待通过bgw\_restart\_time配置的时间段之后被重新启动， 或者在postmaster因为一次后端失败重新初始化集簇时立刻被重启。需要临时禁止执行的后端应该使用 可中断的休眠而不是退出，这可以通过调用WaitLatch()实现。 调用该函数时要确保WL\_POSTMASTER\_DEATH标志被设置，并且验证在 postgres本身被终止的紧急情况下产生的快速退出返回码。

当一个后台工作者是通过RegisterDynamicBackgroundWorker函数 注册时，后端可以执行该注册以获得有关该工作者的状态信息。希望这样做的后端应该把一个BackgroundWorkerHandle \*的地址作为第二个参数传递给 RegisterDynamicBackgroundWorker。如果工作者被成功地注册， 这个指针将被用一个非透明句柄初始化，它之后会被传递给

GetBackgroundWorkerPid(BackgroundWorkerHandle \*, pid\_t \*)

或者

TerminateBackgroundWorker(BackgroundWorkerHandle \*)。

GetBackgroundWorkerPid可以被用来测试工作者的状态：返回值为

BGWH\_NOT\_YET\_STARTED表示该工作者还未被postmaster启动； BGWH\_STOPPED表示它已经被启动但是不再运行； 而BGWH\_STARTED表示它正在运行。在最后一种情况下，PID也将被通过第二个参数返回。 TerminateBackgroundWorker导致postmaster发送SIGTERM 给工作者（如果它在运行），并且在它不再运行时尽快解除注册。

在某些情况下，一个注册后台工作者的进程可能希望等待该工作者启动起来。其实现方式是：把

bgw\_notify\_pid初始化成MyProcPid并且接着 把注册时得到的BackgroundWorkerHandle \*传递给WaitForBackgroundWorkerStartup(BackgroundWorkerHandle \*handle, pid\_t \*)函数。 这个函数将阻塞直到postmaster已经尝试启动该后台工作者，或者直到postmaster死亡。如果后台 工作者正在运行，返回值将是BGWH\_STARTED，并且其PID将被写入到所提供的地址。 否则，返回值将是BGWH\_STOPPED或者 BGWH\_POSTMASTER\_DIED。

进程也可以等待一个后台工作者关闭，方法是使用WaitForBackgroundWorkerShutdown(BackgroundWorkerHandle \*handle)函数并且传入注册时得到的BackgroundWorkerHandle \*。这个函数将阻塞直至后台工作者退出或者 postmaster死掉。当后台工作者退出时，返回值是BGWH\_STOPPED，如果postmaster死掉则会返回BGWH\_POSTMASTER\_DIED。

如果一个后台工作者通过服务器编程接口（SPI）用NOTIFY命令发送异步通知，在提交外层事务之后它应该显式地调用ProcessCompletedNotifies，这样通知才能被发送出去。如果一个后台工作者通过SPI使用LISTEN注册为接收异步通知，它将记录那些通知，但是对于工作者来说没有程序化的方式可以拦截以及响应那些通知。

src/test/modules/worker\_spi模块包含了一个实例，它展示了一些有用的技巧。

注册的后台工作者的最大数量由max\_worker\_processes限制。