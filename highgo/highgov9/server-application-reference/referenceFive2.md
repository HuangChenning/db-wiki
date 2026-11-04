---
title: "服务端应用"
book: "服务器应用参考手册"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/reference/referenceFive2.html"
tags:
  - highgo
  - highgo-v9
  - server-application-reference
---

## 服务端应用

## initdb

initdb — 创建一个新的瀚高数据库集簇

**命令**

initdb \[option...\] \[ --pgdata | -D \] directory

**描述**

initdb创建一个新的瀚高数据库集簇。一个数据库集簇是由一个单一服务器实例管理的数据库的集合。

一个数据库集簇的创建包括创建存放数据库数据的目录、生成共享目录表（属于整个集簇而不是任何特定数据库的表）并且创建template1和highgo数据库。当你后来创建一个新的数据库时，任何在template1数据库中的东西都会被复制（因此，任何已安装在template1中的东西都会被自动地复制到后来创建的每一个数据库中）。highgo数据库是便于用户、工具和第三方应用使用的默认数据库。

尽管initdb将尝试创建指定的数据目录，它可能没有权限（如果想要的数据目录的父目录属主为root）。要在这样一种设置中初始化，可使用root用户创建一个空数据目录，然后使用chown命令将该目录赋予给数据库用户账户，再使用su命令登录到数据库用户账户运行initdb。

initdb必须以将拥有该服务进程的用户运行，因为该服务需要访问initdb创建的文件和目录。

由于安全原因，由initdb创建的新集簇默认将只能由集簇拥有者访问。--allow-group-access选项允许与集簇拥有者同组的任何用户读取集簇中的文件。这对非特权用户执行备份很有用。

initdb初始化该数据库集簇的默认区域和字符集编码。当一个数据库被创建时，其字符集编码、排序顺序（LC\_COLLATE）和字符集类（LC\_CTYPE，例如大写、小写、数字）可以被独立设置。initdb为template1数据库确定这些设置，它们将作为所有其他数据库的默认值。

要修改默认排序顺序或字符集类，使用--lc-collate和--lc-ctype选项。除C或POSIX之外的排序顺序也有性能罚值。由于这些原因，在运行initdb时选择正确的区域很重要。

余下的区域分类可以在服务启动之后改变。你也可以使用--locale来为所有区域分类设置默认值，包括排序顺序和字符集类。所有服务区域值（lc\_\*）可以通过SHOW ALL显示。

要修改默认编码，使用--encoding。

**选项**

\-A authmethod

\--auth=authmethod

这个选项为本地用户指定在pg\_hba.conf中使用的默认认证方法（host和local行）。initdb将使用指定的认证方法为非复制连接以及复制连接填充pg\_hba.conf项。

\--auth-host=authmethod

这个选项为通过 TCP/IP 连接的本地用户指定在pg\_hba.conf中使用的认证方法（host行）。

\--auth-local=authmethod

这个选项为通过 Unix 域套接字连接的本地用户指定在pg\_hba.conf中使用的认证方法（local行）。

\-D directory

\--pgdata=directory

这个选项指定数据库集簇应该存放的目录。这是initdb要求的唯一必填信息，但是你可以通过设定PGDATA环境变量来避免书写它，这很方便因为之后数据库服务（postgres）可以使用同一个变量来找到数据库目录。

\-H

\--highgoDB=DBNAME

设置瀚高数据库名称

\-P

–port=PORT

设置瀚高数据库监听端口

–no-instructions

不打印后续指导信息，以减少输出的冗余信息。

\-E encoding

\--encoding=encoding

选择模板数据库的编码。这也将是后续创建的任何数据库的默认编码，除非你覆盖它。默认值来自于区域，或者如果该值不起作用则为SQL\_ASCII。

特别的，对于GB18030\_2022标准，考虑到用户环境可能不支持，在initdb时有必要提供给用户选项让其自由选择是否使用GB18030\_2022。具体逻辑是，在initdb时指定-E GB18030 或-E GB18030\_2022，前者不加载插件gb18030\_2022，后者加载，并将参数写入到ivorysql.conf的shared\_preload\_library中。默认逻辑为加载插件，仅当用户指定-E GB18030时不加载，不指定选项或指定其他选项都会加载插件，因为用户可能在之后create database时会用到此编码。

\-g

\--allow-group-access

允许与集簇拥有者同组的用户读取initdb创建的所有集簇文件。

\-k

\--data-checksums

在数据页面上使用校验码来帮助检测 I/O 系统造成的损坏。启用校验码将会引起显著的性能惩罚。如果设置，则为所有对象计算校验和，在整个数据库中。 所有校验和失败都将报告在pg\_stat\_database 视图中。

\--locale=locale

为数据库集簇设置默认区域。如果这个选项没有被指定，该区域将从initdb所运行的环境中继承。

\--lc-collate=locale

\--lc-ctype=locale

\--lc-messages=locale

\--lc-monetary=locale

\--lc-numeric=locale

\--lc-time=locale

和--locale相似，但是只在指定的分类中设置区域。

\--no-locale

等效于--locale=C。

\-N

\--no-sync

默认情况下，initdb将等待所有文件被安全地写到磁盘。指定该参数后initdb不等待文件落盘就返回，该参数会加速initdb的过程，但是如果后续操作系统发生崩溃可能会损坏数据目录。通常，这个选项对测试有用，不建议在生产安装中使用。

\--pwfile=filename

让initdb从一个文件读取数据库管理用户的口令。

\-S

\--sync-only

安全地把所有数据库文件写入到磁盘并退出。这不会执行任何正常的initdb操作。

\-T config

\--text-search-config=config

设置默认的文本搜索配置。

\-U username

\--username=username

选择数据库超级用户的用户名。这个的默认值是实际运行initdb的用户的名称。超级用户的名字是什么真的不重要，但是你可以选择保留常用的名字postgres，即使操作系统的用户名不同。

\-W

\--pwprompt

让initdb提示要求为数据库超级用户给予一个口令。如果你没有计划使用口令认证，这就不重要。否则在你设置一个口令之前你就无法使用口令认证。

\-X directory

\--waldir=directory

这个选项指定预写式日志会被存储在哪个目录中。

\--wal-segsize=size

设置WAL段尺寸，以兆字节为单位。这是WAL日志中每个文件的尺寸。默认的尺寸为16兆字节。该值必须位于2的1次幂和1024次幂（兆字节）之间。这个选项只能在初始化期间设置，并且之后不能更改。

调整这个值来控制WAL日志传送或者归档可能会有用。此外，在有大量WAL的数据库中，每个目录中数量巨大的WAL文件可能会成为性能和管理问题。增加WAL文件尺寸将会降低WAL文件的数量。

\-m

\--dbmode

设置数据库实例支持模式，可选范围为pg、oracle、mysql，默认为oracle

\-c

\--case-conversion-mode

设置数据库大小写敏感模式，默认为interchange（大小写敏感）

其他较少使用的选项：

\-d

\--debug

打印来自后端的调试输出消息。后端被程序initdb用来创建目录表。这个选项会生成大量无用输出。

\-L directory

指定initdb应从哪里寻找它的输入文件来初始化数据库集簇。这通常没有必要。如果你需要显式指定它们的位置，可以通过该参数指定。

\-n

\--no-clean

默认情况下，当initdb确定有一个错误阻止它完整地创建数据库集簇，它会移除在它发现无法完成任务之前创建的任何文件。指定该选项后不会移除已经创建的文件，可用于调试。

其他选项：

\-V

\--version

打印initdb版本并退出。

\-G

\--highgo-version

打印瀚高数据库版本信息

\-?

\--help

显示有关initdb命令行参数的帮助并退出。

\-C

–cluster-key-command=COMMAND

指定KEK的获取命令

\-R

–authprompt

当-C需要交互时需指定该参数提供交互终端

\-K

–file-encryption-method=METHOD

指定加密使用的算法

\-z

–file-encryption-mode=MODE

指定加密范围

\-u

–copy-encryption-keys=DATADIR

使用现有秘钥初始化数据库

**环境**

PGDATA

指定数据库集簇应该被存放的目录，可以使用-D选项覆盖。

PG\_COLOR

规定在诊断消息中是否使用颜色。可能的值为always、 auto、never。

TZ

指定创建的数据集簇的默认时区。值应该是一个完整的时区名称。和大部分其他数据库工具相似，这个工具也使用libpq（见开发手册）支持的环境变量。

**注释**

initdb可以通过pg\_ctl initdb被调用。

## pg\_archivecleanup

pg\_archivecleanup — 清理数据库 WAL 归档文件

**命令**

pg\_archivecleanup \[option...\] archivelocation oldestkeptwalfile

**简介**

pg\_archivecleanup被设计用作archive\_cleanup\_command在作为后备服务器运行时来清理 WAL 文件归档。pg\_archivecleanup也可以被用作一个单独的程序来清理 WAL 文件归档。

要配置一个后备服务器以使用pg\_archivecleanup，把下面的内容放在postgresql.conf配置文件中：

archive\_cleanup\_command = 'pg\_archivecleanup archivelocation %r'

其中archivelocation是要从中移除 WAL 段文件的目录。

当被用在archive\_cleanup\_command中时，所有逻辑上在 %r参数的值之前的 WAL 文件都将被从 archivelocation移除。这能最小化需要被保留的文件数量， 同时能保留崩溃后重启的能力。如果对于这台特定的后备服务器， archivelocation是一个短暂需要的区域，使用这个参数就是合适的，但是当archivelocation要用作一个长期的 WAL 归档区域或者当多个后备服务器正在从这个归档位置恢复时，使用这个参数就不合适。

当被用作一个单独的程序时，所有逻辑上在oldestkeptwalfile 之前的 WAL 文件将被从archivelocation中移除。在这种模式中，如果指定了.partial或者.backup文件名，则只有该文件前缀将被用作oldestkeptwalfile。这种对.backup文件名的处理允许你移除所有在一个特定基础备份之前归档的WAL文件而不出错。例如，下面的例子将移除所有比WAL文件名 000000010000003700000010老的文件：

pg\_archivecleanup -d archive 000000010000003700000010.00000020.backup

pg\_archivecleanup: keep WAL file "archive/000000010000003700000010" and later

pg\_archivecleanup: removing file "archive/00000001000000370000000F"

pg\_archivecleanup: removing file "archive/00000001000000370000000E"

pg\_archivecleanup假定 archivelocation是一个可读的目录并且对于服务器拥有者是可写的。

**选项**

pg\_archivecleanup支持下列命令行参数：

\-d

在stderr上打印很多调试日志输出。

\-n

在stdout上打印将被移除的文件的名字（执行一次演习）。

\-V

\--version

打印pg\_archivecleanup版本并退出。

\-x extension

提供一个扩展名，在决定所有的文件是否应该被删除之前，将从文件名中剥离这个扩展名。这通常有助于清理已经存储期间被压缩过并且被压缩程序增加了一个扩展名的归档。例如： -x.gz。

\-?

\--help

显示pg\_archivecleanup命令行参数的帮助并退出。

**示例**

在 Linux 或者 Unix 系统上，你可能会用：

archive\_cleanup\_command = 'pg\_archivecleanup -d /mnt/standby/archive %r 2>>cleanup.log'

其中归档目录位于后备服务器上，这样archive\_command通过 NFS 来访问它，但是文件对于后备服务器来说是本地的。这将会：

• 在cleanup.log中产生调试输出

• 从归档目录中移除不再需要的文件

## pg\_checksums

pg\_checksums — 在瀚高数据库集簇中启用、禁用或检查数据校验和

**命令**

pg\_checksums \[option...\] \[\[ -D | --pgdata \] datadir\]

**简介**

pg\_checksums在瀚高数据库集簇中检查、启用或禁用数据校验和。运行pg\_checksums之前，必须彻底停止服务。验证校验和时，如果没有校验和错误，则退出状态为零，如果检测到至少一个校验和失败，则退出状态为非零。启用或禁用校验和时，如果操作失败，则退出状态为非零。

验证校验和时，集簇中的每个文件都要被扫描。启用校验和时，集簇中的每个文件都会被重写。禁用校验和时，仅更新pg\_control文件。

**选项**

下列命令选项可用：  
\-D directory

\--pgdata=directory

指定存储数据库集簇的目录。

\-c

\--check

检查校验和。如果未指定其它任何内容，这是缺省模式。

\-d

\--disable

禁用校验和。

\-e

\--enable

启用校验和。

\-f filenode

\--filenode=filenode

仅验证文件节点为filenode的关系中的校验和。

\-N

\--no-sync

缺省地，pg\_checksums会等待所有文件安全地写到磁盘上。该选项使得pg\_checksums不等待就返回，这样更快，但是如果后续操作系统发生崩溃可能会损坏数据目录。一般地，该选项对测试有用，但不应用在生产安装上。当使用--check时，该选项无效。

\-P

\--progress

启用进度报告。在检查或启用校验和时，打开该选项，会提供进度报告。

\-v

\--verbose

启用详细输出。列出所有检查的文件 。

\-V

\--version

打印pg\_checksums版本并退出。

\-?

\--help

显示关于pg\_checksums命令行参数的帮助并退出。

**环境**

PGDATA

指定数据库集簇存储的目录；可以用-D选项覆盖。

PG\_COLOR

指定是否在诊断消息中使用颜色。可能的值为always, auto, never。

**注释**

在大型集簇中启用校验和的时间可能很长。在此操作期间，写到数据目录的集簇或其它程序必须是未启动的，否则可能出现数据丢失。

当复制设置与执行关系文件块的直接拷贝的工具（例如pg\_rewind）一起使用时，启用和禁用校验和会导致以不正确校验和形式出现的页面损坏，如果未在所有节点上执行一致的操作的话。故在复制设置中启用或禁用校验和时，推荐一致地切换所有集簇之前停止所有集簇。此外销毁所有备用数据库，在主数据库上执行操作，最后从头开始重建备用服务器，也是安全的。

如果在启用或禁用校验和时异常终止或杀掉pg\_checksums，那么集簇的数据校验和配置保持不变，pg\_checksums可以重新运行以执行相同操作。

## pg\_controldata

pg\_controldata — 显示一个瀚高数据库集簇的控制信息

**命令**

pg\_controldata \[option\] \[\[ --pgdata | -D \] datadir\]

**描述**

pg\_controldata打印在initdb期间初始化的信息，例如目录版本。它也显示关于预写式日志和检查点处理的信息。这种信息是集簇范围的，并且不针对任何一个数据库。

这个工具只能由初始化集簇的用户运行，因为它要求对数据目录的读访问。你可以在命令行中指定数据目录，或者使用环境变量PGDATA。这个工具支持选项-V和--version，它们打印pg\_controldata版本并退出。它也支持选项-?和--help，它们输出该工具支持的参数。

**环境**

PGDATA

默认的数据目录位置。

PG\_COLOR

规定在诊断消息中是否使用颜色。可能的值为always、 auto、never。

## pg\_ctl

pg\_ctl — 初始化、启动、停止或控制一个瀚高数据库服务

**命令**

pg\_ctl init\[db\] \[-D datadir\] \[-s\] \[-o initdb-options\]

pg\_ctl start \[-D datadir\] \[-l filename\] \[-W\] \[-t seconds\] \[-s\] \[-o options\] \[-

p path\] \[-c\]

pg\_ctl stop \[-D datadir\] \[-m s\[mart\] | f\[ast\] | i\[mmediate\] \] \[-W\] \[-t seconds\] \[-s\]

pg\_ctl restart \[-D datadir\] \[-m s\[mart\] | f\[ast\] | i\[mmediate\] \] \[-W\] \[-t seconds\]

\[-s\] \[-o options\] \[-c\]

pg\_ctl reload \[-D datadir\] \[-s\]

pg\_ctl status \[-D datadir\]

pg\_ctl promote \[-D datadir\] \[-W\] \[-t seconds\] \[-s\]

pg\_ctl logrotate \[-D datadir\] \[-s\]

pg\_ctl kill signal\_name process\_id

**描述**

pg\_ctl是一个用于初始化瀚高数据库集簇，启动、停止或重启数据库服务，或者显示一个正在运行服务的状态的工具。尽管服务可以被手工启动，pg\_ctl包装了重定向日志输出以及正确地从终端和进程组脱离等任务。它也提供了方便的选项用来控制关闭。

init或initdb模式会创建一个新的瀚高数据库集簇，也就是将由一个单一服务器实例管理的数据库集合。这个模式调用initdb命令。

start模式启动一个新的服务。该服务在后台启动，并且它的标准输出被附加到/dev/null。在 Unix 类系统上，默认情况下服务器的标准输出和标准错误被发送到pg\_ctl的标准输出（不是标准错误）。pg\_ctl的标准输出应该接着被重定向到一个文件或用管道导向另一个进程（例如日志轮转程序rotatelogs）。否则数据库进程将把它的输出写到控制终端（从后台）并且将不会离开 shell 的进程组。

stop模式关闭运行在指定数据目录中的服务。对-m选项可以选择三种不同的关闭方法。”Smart”模式等待所有客户端断开连接以及任何在线备份结束。如果该服务器是热备，一旦所有的客户端已经断开连接，恢复和流复制将被终止。”Fast”模式（默认）不会等待客户端断开连接并且将终止进行中的在线备份。所有活动事务都被回滚并且客户端被强制断开连接，然后服务器被关闭。”Immediate”模式将立刻中止所有服务器进程，而不是做一次干净的关闭。这种选择将导致下一次重启时进行一次崩溃恢复。

restart模式实际上会先执行一个停止操作然后紧接着执行一个启动操作。这使得我们能够更改数据库进程的命令行选项，或者更改不通过重启服务无法更改的配置文件选项。如果在服务启动期间在命令行上使用了相对路径，则restart可能会失败，除非pg\_ctl被运行在与上次启动服务器相同的目录中。

reload模式简单地向数据库主进程发送一个SIGHUP信号，导致它重新读取它的配置文件（postgresql.conf、pg\_hba.conf等）。这允许改变配置文件选项而无需一次完整的服务重启来让改变生效。

status模式检查一个服务是否运行在指定的数据目录中。如果有一个服务正在运行，其PID和用来调用它的命令行选项将被显示。如果服务没有在运行，pg\_ctl将返回退出状态3。如果没有指定一个可以访问的数据目录，pg\_ctl将返回退出状态 4。

promote模式命令运行在指定数据目录中的后备服务结束后备模式并且开始读写操作。

logrotate模式轮换服务日志文件。

kill模式向一个指定进程发送一个消息。使用--help来查看受支持的信号名称列表。

register模式把数据库服务注册为系统服务。-S选项允许选择服务启动类型，可以是”auto”（随系统自动启动）或”demand”（按需启动）。

unregister模式移除一个系统服务的注册。这会撤销register命令的效果。

**选项**

\-c

\--core-files

在可行的平台上尝试允许服务器崩溃产生核心文件，方法是提升在核心文件上的任何软性资源限制。这通过允许从一个失败的服务进程中获得一个栈跟踪而有助于调试或诊断问题。

\-D datadir

\--pgdata=datadir

指定数据库配置文件的文件系统位置。如果这个选项被忽略，将使用环境变量PGDATA。

\-l filename

\--log=filename

追加服务器日志输出到filename。如果该文件不存在，它会被创建。umask被设置成077，这样默认情况下不允许其他用户访问该日志文件。

\-m mode

\--mode=mode

指定关闭模式。mode可以是smart、fast或immediate，或者这三者之一的第一个字母。

如果这个选项被忽略，则默认值为fast。

\-o options

\--options=options

指定被直接传递给postgres命令的选项。-o可以被指定多次，所有给定的选项都会被传过去。

这些选项应该通常被单引号或双引号包围来确保它们被作为一个整体传递。

\-o initdb-options

\--options=initdb-options

指定要直接传递给initdb命令的选项。-o可以被指定多次，所有给定的选项都会被传过去。

这些选项应该通常被单引号或双引号包围来确保它们被作为一个整体传递。

\-p path

指定postgres可执行程序的位置。默认情况下，postgres可执行程序可以从pg\_ctl相同的目录得到，或者如果没有在那里找到，则在该参数指定的安装目录中获得。除非你正在做一些不同寻常的事并且得到错误说没有找到postgres可执行程序，这个选项不是必需的。

在init模式中，这个选项类似于指定了initdb可执行程序的位置。

\-s

\--silent

只打印错误，不打印信息性的消息。

\-t seconds

\--timeout=seconds

指定等待一个操作完成时要等待的最大秒数（见选项-w）。默认为PGCTLTIMEOUT环境变量的值，如果该环境变量没有设置则默认为60秒。

\-V

\--version

打印pg\_ctl版本并退出。

\-w

\--wait

等待操作完成。模式start、stop、restart、promote以及register支持这个选项，并且对那些模式是默认的。

在等待时，pg\_ctl会一遍又一遍地检查服务的PID文件，在两次检查之间会休眠一小段时间。当PID文件指示该服务已经做好准备接受连接时，启动操作被认为完成。当服务移除PID文件时，关闭操作被认为完成。pg\_ctl会基于启动或关闭的成功与否返回一个退出代码。

如果操作在超时时间内未能完成，则pg\_ctl会以一个非零退出状态退出。但是注意该操作可能会在后台继续进行并且最终取得成功。

\-W

\--no-wait

不等待操作完成。这是选项-w的相反选项。

如果禁用等待，所请求的动作会被触发，但是不会有关于其成功与否的反馈。在这种情况下，可能必须用服务日志文件或外部监控系统来检查该操作的进度以及成功与否。

在以前的版本中，这是除stop模式之外的模式的默认选项。

\-R

–authprompt

当-C需要交互时需指定该参数提供交互终端

\-?

\--help

显示有关pg\_ctl命令行参数的帮助并退出。

如果一个指定的选项有效，但与选中的操作模式无关，则pg\_ctl会忽略它。

**环境**

PGCTLTIMEOUT

等待启动或者关闭完成时要等待的默认秒数限制。如果没有设置，默认值是 60 秒。

PGDATA

默认的数据目录位置。

大部分的pg\_ctl模式都要求知道数据目录的位置，因此-D选项是必需的，除非PGDATA被设置。

和大部分其他数据库工具相似，pg\_ctl也使用libpq（见开发手册）支持的环境变量。

**文件**

postmaster.pid

pg\_ctl在数据目录中检查这个文件来判断服务当前是否正在运行。

postmaster.opts

如果这个文件存在于数据目录中，pg\_ctl（处于restart模式中）将把该文件的内容作为选项传递给postgres，除非通过-o选项进行了覆盖。这个文件的内容也会被显示在status模式中。

**示例**

- 启动服务

要启动服务并且等到服务接受连接：

$ pg\_ctl start

要使用端口 5433 启动服务器并且运行时不使用fsync：

$ pg\_ctl -o "-F -p 5433" start

- 停止服务

要停止服务，使用：

$ pg\_ctl stop

\-m选项允许控制服务如何关闭：

$ pg\_ctl stop -m smart

- 重启服务

重启服务几乎等价于停止服务并且再次启动它，不过pg\_ctl默认会保存并重用被传递给之前的运行实例的命令行选项。要以和之前相同的选项重启服务，使用：

$ pg\_ctl restart

但是如果指定了-o，则会替换任何之前的选项。要使用端口 5433 重启并在重启时禁用fsync：

$ pg\_ctl -o "-F -p 5433" restart

- 显示服务状态

这里是pg\_ctl状态输出的例子：

$ pg\_ctl status

pg\_ctl: server is running (PID: 13718)

/home/highgo/highgo/database/8.0/bin/postgres "-D" " /home/highgo/highgo/database/8.0/data" "-p" "5433" "-B" "18"

第二行是在重启模式可能被调用的命令行。

## pg\_resetwal

pg\_resetwal — 重置一个瀚高数据库集簇的预写式日志以及其他控制信息

**命令**

pg\_resetwal \[ --force | -f \] \[ --dry-run | -n \] \[option...\] \[ --pgdata | -D \] datadir

**描述**

pg\_resetwal会清除预写式日志（WAL）并且有选择地重置存储在pg\_control文件中的一些其他控制信息。如果这些文件已经被损坏，某些时候就需要这个功能。当服务由于这样的损坏而无法启动时，这只应该被用作最后的手段。

在运行这个命令之后，就可能可以启动服务，但是记住数据库可能包含由于部分提交事务产生的不一致数据。你应当立刻转储你的数据、运行initdb并且重新载入。重新载入后，检查不一致并且根据需要进行修复。

这个工具只能被安装数据库的用户运行，因为它要求对数据目录的读写访问。出于安全原因，你必须在命令行中指定数据目录。pg\_resetwal不支持使用环境变量PGDATA。

如果pg\_resetwal提示无法为pg\_control决定合法数据，你可以通过指定-f（强制）选项强制它继续。在这种情况下，丢失的数据将被替换为看似合理的值。可以期望大部分域是匹配的，但是下一个 OID、下一个事务 ID 和纪元、下一个多事务 ID 和偏移以及WAL 开始位置域可能还是需要人工协助。这些域可以使用下面讨论的选项设置。如果你不能为所有这些域决定正确的值，-f还是可以被使用，但是恢复的数据库还是值得怀疑：一次立即的转储和重新载入是势在必行的。在你转储之前不要在该数据库中执行任何数据修改操作，因为任何这样的动作都可能使破坏更严重。

**选项**

\-f

\--force

即使pg\_resetwal无法从pg\_control中确定有效的数据（如前面所解释的），也强迫pg\_resetwal继续运行。

\-n

\--dry-run

\-n/--dry-run选项指示pg\_resetwal打印从pg\_control重构出来的值以及要被改变的值，然后不修改任何东西退出。这主要是一个调试工具，但是可以用来在允许pg\_resetwal真正执行下去之前进行完整性检查。

\-V

\--version

显示版本信息然后退出。

\-?

\--help

显示帮助然后退出。

只有当pg\_resetwal无法通过读取pg\_control确定合适的值时，才需要下列选项。安全值可以按下文所述来确定。对于接收数字参数的值，可以使用前缀0x指定 16 进制值。

\-c xid,xid

\--commit-timestamp-ids=xid,xid

手工设置提交时间可以检索到的最老的和最新的事务 ID。

能检索到提交时间的最老事务 ID 的安全值（第一部分）可以通过在数据目录下pg\_commit\_ts目录中数字上最小的文件名来决定。反过来，能检索到提交时间的最新事务 ID 的安全值（第二部分）可以通过同一个目录中数字上最大的文件名来决定。文件名都是十六进制的。

\-e xid\_epoch

\--epoch=xid\_epoch

手工设置下一个事务 ID 的 epoch。

事务 ID 的 epoch 实际上并没有存储在数据库中的任何地方，除了被pg\_resetwal设置在这个域中，所以只要关心的是数据库本身，任何值都可以用。你可能需要调整这个值来确保诸如Slony-I和Skytools之类的复制系统正确地工作 — 如果确实需要调整，应该可以从下游的复制数据库的状态中获得一个合适的值。

\-l walfile

\--next-wal-file=walfile

通过指定下一个WAL段文件名称来手工设置WAL开始位置。

下一个WAL段文件的名称应该比当前存在于数据目录下pg\_wal目录中的任意 WAL 段文件名更大。这些名称也是十六进制的并且有三个部分。第一部分是”时间线 ID”并且通常应该被保持相同。例如，如果00000001000000320000004A是pg\_wal中最大的项，则使用-l00000001000000320000004B或更高的值。

注意在使用非默认WAL段尺寸时，WAL文件名中的数字与系统函数和系统视图报告的LSN不同。这个选项要的是WAL文件名而不是LSN。

| 注意： |
| --- |
| pg\_resetwal本身查看pg\_wal中的文件并选择一个超出最新现存文件名的默认-l设置。因此，只有当你知道 WAL 段文件当前不在pg\_wal中时，或者当pg\_wal的内容完全丢失时，才需要对-l的手工调整，例如一个离线归档中的项。 |

\-m mxid,mxid

\--multixact-ids=mxid,mxid

手工设置下一个和最老的多事务 ID。

确定下一个多事务 ID（第一部分）的安全值的方法：在数据目录下的pg\_multixact/offsets目录中查找最大的数字文件名，然后在它的基础上加一并且乘以 65536(0x10000)。反过来，确定最老的多事务 ID（-m的第二部分）的方法：在同一个目录中查找最小的数字文件名并且乘以 65536。文件名是十六进制的数字，因此实现上述方法最简单的方式是以十六进制指定选项值并且追加四个零。

\-o oid

\--next-oid=oid

手工设置下一个 OID。

没有相对容易的方法来决定超过数据库中最大 OID 的下一个 OID。但幸运的是正确地得到下一个 OID 设置并不是决定性的。

\-O mxoff

\--multixact-offset=mxoff

手工设置下一个多事务偏移量。

确定安全值的方法：查找数据目录下pg\_multixact/members目录中最大的数字文件名，然后在它的基础上加一并且乘以 52352 (0xCC80)。文件名是十六进制数字。没有像其他选项那样追加零的简单方法。

\--wal-segsize=wal\_segment\_size

设置新的WAL段尺寸，以兆字节为单位。这个值必须被设为2的1次幂和1024次幂（兆字节）之间。更多信息请参考 [\[initdb\]{.underline}](#initdb) 的相同选项。

\-C

–cluster-key-command=COMMAND

指定KEK的获取命令。

\-R

–authprompt

当-C需要交互时需指定该参数提供交互终端。

\-x xid

\--next-transaction-id=xid

手工设置下一个事务 ID。

确定安全值的方法：在数据目录下的pg\_xact目录中查找最大的数字文件名，然后在它的基础上加一并且乘以 1048576 (0x100000)。注意文件名是十六进制的数字。通常以十六进制的形式指定该选项值也是最容易的。例如，如果0011是pg\_xact中的最大项，-x0x1200000就可以（五个尾部的零就表示了前面说的乘数）。

## pg\_rewind

pg\_rewind — 把一个瀚高数据库数据目录与另一个从该目录中复制出来的数据目录同步。

**命令**

pg\_rewind \[option...\] { -D | --target-pgdata } directory { --source

pgdata=directory | --source-server=connstr }

**简介**

pg\_rewind是用于在集簇的时间线分叉以后，同步一个瀚高数据库集簇和同一集簇的另一份拷贝的工具。一种典型的场景是在失效后让一个旧的主服务器重新上线，同时有一个后备机跟随着新的主机。

其结果等效于把目标数据目录替换成源数据目录。关系文件中只有更改过的块才会被拷贝，所有其他的文件会被整个拷贝，包括配置文件。pg\_rewind比起做一个新的基础备份或者rsync等工具的优势在于，pg\_rewind不要求通读集簇中未更改的块。这使得它在数据库很大并且在集簇间只有小部分块不同时速度很快。

pg\_rewind检查源集簇和目标集簇的时间线历史来判断它们在哪一点分叉，并且期望在目标集簇的pg\_wal目录中找到 WAL 来返回到分叉点。分叉点可能会在目标时间线、源时间线或者它们的共同祖先上找到。在典型的失效场景中，目标集簇在分叉后很快就被关闭，这不是问题，但是如果目标集簇在分叉后已经运行了很长时间，旧的 WAL 文件可能已经不存在了。在这样的情况下，它们可以被手工从 WAL 归档复制到pg\_wal目录，或者通过配置primary\_conninfo 或restore\_command在启动时取得。pg\_rewind的使用并不限于失效的场景，例如一个后备服务器可能被提升、运行一些写事务，然后被降级再次成为一个后备服务器。

当目标服务器在运行了pg\_rewind之后第一次启动时，它将进入到恢复模式并且重放源服务器在分叉点之后产生的所有 WAL。当pg\_rewind被运行时有某些 WAL 在源服务器上不可用，并且因此无法被pg\_rewind会话所复制，则在目标服务器被启动时必须让这些 WAL可用。这可以通过在目标数据目录中创建一个recovery.signal文件并且在postgresql.conf中配置适合的restore\_command来实现。

pg\_rewind要求目标服务器在postgresql.conf中启用了wal\_log\_hints选项，或者在用initdb初始化集簇时启用了数据校验。目前默认情况下这两者都没有被打开。full\_page\_writes也必须被设置为on，这是默认的。

| 警告： |
| --- |
| 如果在处理时pg\_rewind失败，则目标的数据目录很可能不在可恢复的状态。在这种情况下，推荐创建一个新的备份。 |
| 如果pg\_rewind发现它无法直接写入的文件，它将立刻失败。例如当源服务器和目标服务器为只读的SSL密钥及证书使用相同的文件映射，就会发生这种情况。如果在目标服务器上存在这样的文件，推荐在运行pg\_rewind之前移除它们。在做了rewind之后，一些那样的文件可能已经被从源服务器拷贝，这样就有必要移除已经拷贝的数据并且恢复到rewind之前使用的链接集合。 |

**选项**

pg\_rewind接受下列命令行参数：

\-D directory

\--target-pgdata=directory

这个选项指定要与源数据目录同步的目标数据目录。在运行pg\_rewind之前目标服务器必须被干净地关闭。

\--source-pgdata=directory

指定要和目标服务器同步的源服务器的数据目录的文件系统路径。这个选项要求源服务器必须被干净地关闭。

\--source-server=connstr

指定一个 libpq 连接串用于连接要与目标服务器同步的源数据库服务器。连接必须是常规（非复制）连接，角色具有足够权限执行源服务器上pg\_rewind使用的函数（详请参阅备注部分）。这个选项要求源服务器正在运行且不处于恢复模式。

\-n

\--dry-run

做除了实际修改目标目录之外的其他所有事情。

\-N

\--no-sync

默认情况下，pg\_rewind将等待所有文件安全地写入磁盘。 此选项会导致pg\_rewind不等待即可返回，这更快，但意味着后续操作系统崩溃会使同步数据目录损坏。通常情况，此选项可用于测试，在创建生产安装时不应使用。

\-P

\--progress

启用进度报告。在从源集簇拷贝数据时，打开这个选项将会发送一个近似的进度报告。

\--debug

打印冗长的调试输出，这主要对于调试pg\_rewind的开发者有用。

\-V

\--version

显示版本信息然后退出。

\-C

–cluster-key-command=COMMAND

指定KEK的获取命令。

\-T

–authprompt

当-C需要交互时需指定该参数提供交互终端。

\-?

\--help

显示帮助然后退出。

**环境**

在使用--source-server选项时，pg\_rewind也使用libpq支持的环境变量

（见开发手册）。

环境变量PG\_COLOR规定在诊断消息中是否使用颜色。可能的值为always、auto、never。

**注释**

当使用在线群集作为源执行pg\_rewind时，需使用具有充足权限来执行pg\_rewind在源群集上使用的函数的角色。这里介绍如何创建这样的角色，在这里命名rewind\_user：

> CREATE USER rewind\_user LOGIN;
> 
> GRANT EXECUTE ON function pg\_catalog.pg\_ls\_dir(text, boolean, boolean) TO rewind\_user;
> 
> GRANT EXECUTE ON function pg\_catalog.pg\_stat\_file(text, boolean) TO rewind\_user;
> 
> GRANT EXECUTE ON function pg\_catalog.pg\_read\_binary\_file(text) TO rewind\_user;
> 
> GRANT EXECUTE ON function pg\_catalog.pg\_read\_binary\_file(text, bigint, bigint, boolean) TO rewind\_user;

当使用近期升级的在线群集作为源执行pg\_rewind时，必须在升级后执行CHECKPOINT以便其控制文件反映最新的时间线信息， pg\_rewind使用这些信息检查目标群集是否可以使用指定的源群集倒回。

**工作原理**

其基本思想是从源集簇拷贝所有文件系统级别的变更到目标集簇：

1\. 以源集簇的时间线历史从目标集簇分叉出来的点之前的最后一个检查点为起点，扫描目标集簇的 WAL 日志。对于每一个 WAL 记录，读取每一个被动过的数据块。这会得到在目标集簇中从源集簇被分支出去以后所有被更改过的数据块列表。

2\. 使用直接的文件系统访问（--source-pgdata）或者 SQL （--source-server），把所有那些更改过的块从源集簇拷贝到目标集簇。

3\. 把所有其他诸如pg\_xact和配置文件（除了关系文件之外所有的东西）从源集簇拷贝到目标集簇。与基础备份类似，在从源集簇拷贝的数据中，目录pg\_dynshmem/、pg\_notify/、pg\_replslot/、pg\_serial/、pg\_snapshots/、pg\_stat\_tmp/以及pg\_subtrans/的内容会被忽略。任何以pgsql\_tmp开始的文件或目录都会被忽略，backup\_label、tablespace\_map、pg\_internal.init、postmaster.opts以及postmaster.pid也是这样。

4\. 从源集簇应用 WAL，从失效处创建的检查点开始（严格来说，pg\_rewind并不应用 WAL，它只是创建一个备份标签文件，该文件让数据库从那个检查点开始向前重放所有 WAL）。

## pg\_test\_fsync

pg\_test\_fsync — 为瀚高数据库判断最快的 wal\_sync\_method

**命令**

pg\_test\_fsync \[option...\]

**简介**

pg\_test\_fsync是想告诉你在特定的系统上，哪一种 wal\_sync\_method最快，还可以在发生认定的 I/O 问题时提供诊断信息。不过，pg\_test\_fsync 显示的区别可能不会在真实的数据库吞吐量上产生显著的区别，特别是由于很多数据库服务被它们的预写日志限制了速度。 pg\_test\_fsync为wal\_sync\_method报告以微秒计的平均文件同步操作时间，也能被用来提示用于优化commit\_delay值的方法。

**选项**

pg\_test\_fsync接受下列命令行选项：

\-f

\--filename

指定要写入测试数据到其中的文件名。这个文件必须位于和pg\_wal目录所在或者将被放置的同一个文件系统中（pg\_wal包含WAL文件）。默认是当前 目录中的pg\_test\_fsync.out。

\-s

\--secs-per-test

指定每次测试的秒数。每个测试的时间越长，测试的精度就越高，但是它需要更多时间来运行。默认是 5 秒，这允许程序在 2 分钟以内完成。

\-V

\--version

打印pg\_test\_fsync版本并且退出。

\-?

\--help

显示有关pg\_test\_fsync命令行参数的帮助并且退出。

## pg\_test\_timing

pg\_test\_timing — 度量计时开销

**命令**

pg\_test\_timing \[option...\]

**描述**

pg\_test\_timing是一种度量在你的系统上计时开销以及确认系统时间绝不会回退的工具。收集计时数据很慢的系统会给出不太准确的EXPLAIN ANALYZE结果。

**选项**

pg\_test\_timing接受下列命令行选项：

\-d duration

\--duration=duration

指定测试的持续时间，以秒计。更长的持续时间会给出更好一些的精确度，并且更可能发现系统时钟回退的问题。默认的测试持续时间是 3 秒。

\-V

\--version

打印pg\_test\_timing版本并退出。

\-?

\--help

显示有关pg\_test\_timing的命令行参数，然后退出。

**用法**

- 结果解读

好的结果将显示大部分（>90%）的单个计时调用用时都小于 1 微秒。每次循环的平均开销将会更低，低于 100 纳秒。下面的例子来自于一台使用了一份 TSC 时钟源码的 Intel i7-860系统，它展示了非常好的性能：

Testing timing overhead for 3 seconds.

Per loop time including overhead: 35.96 ns

Histogram of timing durations:

< us % of total count

1 96.40465 80435604

2 3.59168 2999652

4 0.00015 126

8 0.00002 13

16 0.00000 2

注意每次循环时间和柱状图用的单位是不同的。循环的解析度可以在几个纳秒（ns），而单个计时调用只能解析到一个微秒（us）。

- 度量执行器计时开销

当查询执行器使用EXPLAIN ANALYZE运行一个语句时，单个操作会被计时，总结也会被显示。你的系统的负荷可以通过使用psql程序计数行来检查：

> CREATE TABLE t AS SELECT \* FROM generate\_series(1,100000);
> 
> \\timing
> 
> SELECT COUNT(\*) FROM t;
> 
> EXPLAIN ANALYZE SELECT COUNT(\*) FROM t;

i7-860 系统测到运行该计数查询用了 9.8 ms 而EXPLAIN ANALYZE版本则需要 16.6 ms，每次处理都在 100,000 行上进行。6.8 ms 的差别意味着在每行上的计时负荷是 68 ns，大概是 pg\_test\_timing 估计的两倍。即使这样相对少量的负荷也造成了带有计时的计数语句耗时多出了 70%。在更大量的查询上，计时开销带来的问题不会有这么明显。

- 改变时间来源Changing time sources

在一些较新的 Linux 系统上，可以在任何时候更改用来收集计时数据的时钟来源。第二个例子显示了在上述快速结果的相同系统上切换到较慢的 acpi\_pm 时间源可能带来的降速：

> \# cat /sys/devices/system/clocksource/clocksource0/available\_clocksource
> 
> tsc hpet acpi\_pm
> 
> \# echo acpi\_pm > /sys/devices/system/clocksource/clocksource0/
> 
> current\_clocksource
> 
> \# pg\_test\_timing
> 
> Per loop time including overhead: 722.92 ns
> 
> Histogram of timing durations:
> 
> < us % of total count
> 
> 1 27.84870 1155682
> 
> 2 72.05956 2990371
> 
> 4 0.07810 3241
> 
> 8 0.01357 563
> 
> 16 0.00007 3

在这种配置中，上面的例子EXPLAIN ANALYZE用了 115.9 ms。其中有 1061 ns 的计时开销，还是用这个工具直接度量结果的一个小倍数。这么多的计时开销意味着实际的查询本身只占了时间的一个很小的分数，大部分的时间都耗在了计时所需的管理开销上。在这种配置中，任何涉及到很多计时操作的EXPLAIN ANALYZE都会受到计时开销的显著影响。

FreeBSD 也允许即时更改时间源，并且它会记录在启动期间有关计时器选择的信息：

> \# dmesg | grep "Timecounter"
> 
> Timecounter "ACPI-fast" frequency 3579545 Hz quality 900
> 
> Timecounter "i8254" frequency 1193182 Hz quality 0
> 
> Timecounters tick every 10.000 msec
> 
> Timecounter "TSC" frequency 2531787134 Hz quality 800
> 
> \# sysctl kern.timecounter.hardware=TSC
> 
> kern.timecounter.hardware: ACPI-fast -> TSC

其他系统可能只允许在启动时设定时间源。在旧的 Linux 系统上，”clock”内核设置是做这类更改的唯一方法。并且即使在一些更近的系统上，对于一个时钟源你将只能看到唯一的选项 "jiffies"。Jiffies 是老的 Linux 软件时钟实现，当有足够快的计时硬件支持时，它能够具有很好的解析度，就像在这个例子中：

> $ cat /sys/devices/system/clocksource/clocksource0/available\_clocksource
> 
> jiffies
> 
> $ dmesg | grep time.c
> 
> time.c: Using 3.579545 MHz WALL PM GTOD PIT/TSC timer.
> 
> time.c: Detected 2400.153 MHz processor.
> 
> $ pg\_test\_timing
> 
> Testing timing overhead for 3 seconds.
> 
> Per timing duration including loop overhead: 97.75 ns
> 
> Histogram of timing durations:
> 
> < us % of total count
> 
> 1 90.23734 27694571
> 
> 2 9.75277 2993204
> 
> 4 0.00981 3010
> 
> 8 0.00007 22
> 
> 16 0.00000 1
> 
> 32 0.00000 1

- 时钟硬件和计时准确性

收集准确的计时信息在计算机上通常是使用具有不同精度的时钟硬件完成的。使用一些硬件，操作系统能几乎直接把系统时钟时间传递给程序。一个系统时钟也可以得自于一块简单地提供计时中断、在某个已知时间区间内的周期性滴答的芯片。在两种情况中，操作系统内核提供一个隐藏这些细节的时钟源。但是时钟源的精确度以及能多快返回结果会根据底层硬件而变化。

不精确的计时能够导致系统不稳定性。对任何时钟源的更改都要仔细地测试。操作系统默认是有时会更倾向于可靠性而不是最好的精确性。并且如果你在使用一个虚拟机器，应查看与之兼容的推荐时间源。在模拟计时器时虚拟硬件面临着额外的困难，并且提供商常常会建议每个操作系统的设置。

时间戳计数器（TSC）时钟源是当前一代 CPU 上最精确的一种。当操作系统支持TSC 并且 TSC 可靠时，它是跟踪系统时间更好的方式。有多种方式会使 TSC无法提供准确的计时源，这会让它不可靠。旧的系统能有一种基于 CPU 温度变化的 TSC 时钟，这让它不能用于计时。尝试在一些就的多核 CPU 上使用TSC 可能在多个核心之间给出不一致的时间报告。这可能导致时间倒退，这个程序会检查这种问题。并且即使最新的系统，在非常激进的节能配置下也可能无法提供准确的 TSC 计时。

更新的操作系统可能检查已知的 TSC 问题并且当它们被发现时切换到一种更慢、更稳定的时钟源。如果你的系统支持 TSC 时间但是并不默认使用它，很可能是由于某种充分的理由才禁用它。某些操作系统可能无法正确地检测所有可能的问题，或者即便在知道 TSC 不精确的情况下也允许使用 TSC。

如果系统上有高精度事件计时器（HPET）并且 TSC 不准确，该系统将会更喜欢 HPET 计时器。计时器芯片本身是可编程的，最高允许 100 纳米的解析度，但是在你的系统时钟中可能见不到那么高的准确度。

高级配置和电源接口（ACPI）提供了一种电源管理（PM）计时器，Linux 把它称之为acpi\_pm。得自于 acpi\_pm 的时钟最好时将能提供 300 纳秒的解析度。

在旧的 PC 硬件上使用的计时器包括 8254 可编程区间计时器（PIT）、实时时钟（RTC）、高级可编程中断控制器（APIC）计时器以及 Cyclone 计时器。这些计时器是以毫秒解析度为目标的。

## pg\_upgrade

pg\_upgrade — 升级瀚高数据库服务实例

**命令**

pg\_upgrade -b oldbindir -B newbindir -d oldconfigdir -D newconfigdir \[option...\]

**描述**

pg\_upgrade（之前被称为pg\_migrator） 允许存储在数据文件中的数据被升级到一个较晚的主版本而无需进行主版本升级通常所需的数据转储/重载。 对于次版本升级则不需要这个程序。

主瀚高数据库发行通常会加入新的特性，这些新特性常常会更改系统表的 布局，但是内部数据存储格式很少会改变。pg\_upgrade 使用这一事实来通过创建新系统表并且重用旧的用户数据文件来执行快速升级。如果一个未来的主发行没有把数据存储格式改得让旧数据格式不可读取，这类升级就用不上pg\_upgrade。

pg\_upgrade会尽力（例如通过检查兼容的编译时设 置）确保新旧集簇在二进制上也是兼容的，包括 32/64 位二进制。保持外部模块也是二进制兼容的也很重要，不过 pg\_upgrade无法检查这一点。

**选项**

pg\_upgrade接受下列命令行参数：

\-b bindir

\--old-bindir=bindir

旧的数据库可执行文件目录； 环境变量PGBINOLD

\-B bindir

\--new-bindir=bindir

新的数据库可执行文件目录； 环境变量PGBINNEW

\-c

\--check

只检查集簇，不更改任何数据

\-d configdir

\--old-datadir=configdir

旧的集簇数据目录；环境变量 PGDATAOLD

\-D configdir

\--new-datadir=configdir

新的集簇数据目录；环境变量 PGDATANEW

\-j

\--jobs

要同时使用的进程或线程数

\-k

\--link

使用硬链接来代替将文件拷贝到新集簇

\-o options

\--old-options options

直接传送给旧 postgres命令的选项，多个选项可以追加在后面

\-O options

\--new-options options

直接传送给新 postgres命令的选项，多个选项可以追加在后面

\-p port

\--old-port=port

旧的集簇端口号；环境变量 PGPORTOLD

\-P port

\--new-port=port

新的集簇端口号；环境变量 PGPORTNEW

\-q

–old-oraport=PORT

旧集群 oracle 端口号 (默认值为 50433)

\-Q

–new-oraport=PORT

新集群 oracle 端口号 (默认值为 50433)

\-y

–old-mysport=PORT

旧集群mysql端口号 (默认值为 50434)

\-Y

–new-mysport=PORT

新集群mysql集群端口号 (默认值为 50434)

\-r

\--retain

即使在成功完成后也保留 SQL 和日志文件

\-N,

\--dbname=DBNAME

数据库实例中默认数据库名称

\-s dir

\--socketdir=dir

用于升级期间postmaster套接字的目录;默认是当前目录; 环境变量 PGSOCKETDIR

\-U username

\--username=username

集簇的安装用户名；环境变量 PGUSER

\-v

\--verbose

启用详细的内部日志

\-V

\--version

显示版本信息，然后退出

\-G

–highgo-version

输出瀚高版本信息, 然后退出

\--clone

使用有效的文件克隆（在一些系统上也被称为”reflinks”），而不是将文件拷贝到新群集。 这可以导致数据文件接近瞬时的复制，从而获得-k/--link的速度优势，同时保留旧群集不受影响。

文件克隆仅在某些操作系统和文件系统上得到支持。如果选中但不被支持，则 pg\_upgrade运行将会出错。 目前，它支持在Linux（内核4.5或更高版本）上的Btrfs和XFS（在文件系统创建reflink支持），以及macOS上的APFS。

\-?

\--help

显示帮助，然后退出

**注释**

pg\_upgrade创建不同的工作文件，如模式转储，在当前工作目录中。为了安全，请确保该目录不可被任何其他用户读取或者写入。

pg\_upgrade在新旧数据目录中启动短期的postmasters。临时 Unix 套接字文件用于与这些postmasters通信，默认情况下，在当前工作目录中进行。 在某些情况下，当前目录的路径名称可能太长，无法成为有效的套接字名称。这种情况下你可以使用-s选项将套接字文件放在某些具有较短路径名称的目录中。 为了安全原因，请确保该目录不可被任何其他用户读取或者写入。

如果失败、重建和重索引会影响你的安装，pg\_upgrade 将会报告这些情况。用来重建表和索引的升级后脚本将会自动被建立。 如果你正在尝试自动升级很多集簇，你应该发现具有相同数据库模式的集簇对所有集簇升级都要求同样的升级后步骤，这是因为升级后步骤是基于数据 库模式而不是用户数据。

对于部署测试，创建一个只有模式的旧集簇副本，在其中插入假数据并且升级。

pg\_upgrade不支持包含使用这些reg\* OID-引用 系统数据类型的表列的数据库的升级：regproc, regprocedure, regoper, regoperator, regconfig, 和 regdictionary. (regtype 能够被升级.)

如果你想要使用链接模式并且你不想让你的旧集簇在新集簇启动时被修改，考虑使用克隆模式。 如果(克隆模式)不可用，可以复制一份旧集簇并且在副本上以链接模式进行升级。要创建旧集簇的一 份合法拷贝，可以在服务器运行时使用rsync创建旧集簇的 一份脏拷贝，然后关闭旧服务器并且再次运行rsync --checksum 把更改更新到该拷贝以让其一致（--checksum是必要的，因为 rsync在判断文件修改时间的更改时的精度只能到秒级）。如果你的文件系统支持文件系统快照或者 copy-on-write 文件副本，你可以使用它们来创建旧集簇和表空间的一个备份，不过快照和副本必须被同时创建或者在数据库服务器关闭 期间被创建。

## pg\_waldump

pg\_waldump — 以用户可读的形式显示一个数据库集簇的预写式日志，该工具支持FDE加密格式的WAL日志的读取。

**命令**

pg\_waldump \[option...\] \[startseg \[endseg\]\]

**简介**

pg\_waldump显示预写式日志（WAL），它主要用于调试或者学习目的。这个工具只能由安装数据库服务的用户运行，因为它要求对数据目录的只读访问。

**选项**

下列命令行选项控制输出的位置和格式：

startseg

从指定的日志段文件开始读取。这也隐含地决定了要搜索文件的路径以及要使用的时间线。

endseg

在读取指定的日志段文件后停止。

\-b

\--bkp-details

输出有关备份块的详细信息。

\-e end

\--end=end

在指定的WAL位置停止读取，而不是一直读取到日志流的末尾。

\-f

\--follow

在到达可用 WAL 的末尾之后，保持每秒轮询一次是否有新的 WAL 出现。

\-n limit

\--limit=limit

显示指定数量的记录，然后停止。

\-p path

\--path=path

指定搜索日志段文件的目录或包含这些文件的包含pg\_wal子目录的目录。 缺省值是在当前目录中搜索，当前目录的pg\_wal子目录和 PGDATA的pg\_wal子目录。

\-r rmgr

\--rmgr=rmgr

只显示由指定资源管理器生成的记录。如果把list作为资源管理器名称 传递给这个选项，则打印出可用资源管理器名称的列表然后退出。

\-s start

\--start=start

要从哪个WAL位置开始读取。默认是从找到的最早的文件的第一个可用日志记录开始。

\-t timeline

\--timeline=timeline

要从哪个时间线读取日志记录。默认是使用startseg（如果指定） 中的值，否则默认为1。

\-V

\--version

打印pg\_waldump版本并且退出。

\-x xid

\--xid=xid

只显示用给定事务 ID 标记的记录。

\-z

\--stats\[=record\]

显示概括统计信息（记录的数量和尺寸以及全页镜像）而不是显示每个记录。可以选择针对每个记录生成统计信息，而不是针对每个资源管理器生成。

\-C

–cluster-key-command=COMMAND

指定KEK的获取命令

\-R

–authprompt

当-C需要交互时需指定该参数提供交互终端

\-K

–file-encryption-method=METHOD

指定加密使用的算法

\-W

–wal-key

指定wal日志密钥的位置

\-G

–highgo-version

输出瀚高版本信息，然后退出。

\-?

\--help

显示有关pg\_waldump命令行参数的帮助并且退出。

**环境**

PGDATA

数据目录；另请参阅 -p 选项。

PG\_COLOR

规定在诊断消息中是否使用颜色。可能的值为always、 auto、never。

**注释**

当服务器正在运行时可能会给出错误的结果。

只有指定的时间线会被显示（如果没有指定，则显示默认时间线）。其他时间线上的记录会被忽略。

pg\_waldump不能读取具有后缀.partial 的 WAL 文件。如果需要读取那些文件，需要从文件名中移除.partial后缀。

## postgres

postgres — 瀚高数据库服务

**命令**

postgres \[OPTION\]...

**描述**

postgres是瀚高数据库服务。一个客户端应用为了能访问一个数据库，它会（通过一个网络或者本地）连接到一个运行着的瀚高数据库实例。该实例接着会开始一个独立的服务进程来处理该连接。

一个postgres实例总是管理正好一个数据库集簇的数据。一个数据库集簇是一个数据库的集合，它们被存储在一个共同的文件系统位置（”数据区”）上。 一个系统上可以同时运行多个postgres实例，只要它们使用不同的数据区和不同的通信端口（见下文）。postgres启动时需要知道数据区的位置，该位置必须通过-D选项或PGDATA环境变量指定，对此是没有默认值的。通常，-D或PGDATA会直接指向由initdb创建的数据区目录。其他可能的文件布局在 [\[文件位置\]{.underline}](#_2.2_%E6%96%87%E4%BB%B6%E4%BD%8D%E7%BD%AE) 中讨论。

默认情况下，postgres会在前台启动并将日志消息打印到标准错误流。但在实际应用中，postgres应当作为一个后台进程启动，而且多数是在系统启动时自动启动。

postgres还能在单用户模式中被调用。这种模式的主要用途是在启动过程中由initdb使用。

有时候它也被用于调试或者灾难性恢复。注意，运行一个单用户模式服务器并不真地适合调试服务，因为不会发生实际的进程间通信和锁定。当从 shell 中调用单用户模式时，用户可以输入查询并且结果会被以一种更适合开发者阅读（不适合普通用户）的形式打印在屏幕上。在单用户模式中，会话用户将被设置为 ID 为 1 的用户，并且这个用户会被隐式地赋予超级用户权限。该用户不必实际存在，因此单用户模式运行可以被用来对某些意外损坏的系统目录进行手工恢复。

**选项**

postgres接受下列命令行参数。你也可以通过设置一个配置文件来减少键入大部分这些选项。有些（安全）选项还可以从连接的客户端以一种与应用相关只应用于会话的方法设置。例如，如果设置了PGOPTIONS环境变量，那么基于libpq的客户端将都把那个字符串传递给服务器，它将被数据库服务解释成postgres命令行选项。

- **通用选项**

\-B nbuffers

设置被服务进程使用的共享内存缓冲区数量。这个参数的默认值是initdb自动选择的。指定这个选项等效于设置shared\_buffers配置参数。

\-c name=value

设置一个命名的运行时参数。大多数其它命令行选项实际上都是这种参数赋值的短形式。-c可以出现多次用于设置多个参数。

\-C name

打印命名运行时参数的值，并且退出（详见上面的-c选项）。这可以被用在一个运行服务上，并且从postgresql.conf中返回值，这些值可能被在这次调用中的任何参数修改过。它并不反映集簇启动时提供的参数。

这个选项用于与一个数据库服务实例交互的其他程序来查询配置参数值，例如pg\_ctl。面向用户的应用应该使用SHOW或者pg\_settings视图。

\-d debug-level

设置调试级别。数值设置得越高，写到数据库日志的调试输出就越多。取值范围是从 1到 5。还可以针对某个特定会话使用-d 0来阻止父postgres进程的服务器日志级别被传播到这个会话。

\-D datadir

指定数据库配置文件的文件系统位置。

\-e

把默认日期风格设置为”European”，也就是输入日期域的顺序是DMY。这也导致在一些日期输出格式中把日期打印在月之前。

\-F

禁用fsync调用以提高性能，但是要冒系统崩溃时数据损坏的风险。指定这个选项等效于禁用fsync配置参数。

\-h hostname

指定postgres监听来自客户端应用 TCP/IP 连接的 IP 主机名或地址。该值也可以是一个用逗号分隔的地址列表，或者\*表示监听所有可用的地址。一个空值表示不监听任何 IP地址，在这种情况下可以使用 Unix 域套接字连接到服务器。缺省只监听localhost。声明这个选项等效于设置listen\_addresses配置参数。默认只监听localhost。指定这个选项等效于设listen\_addresses配置参数。

\-i

允许远程客户端使用 TCP/IP （互联网域）连接。没有这个选项，将只接受本地连接。这个选项等效于在postgresql.conf中或者通过-h选项将listen\_addresses设为\*。

这个选项已经被废弃，因为它不允许访问listen\_addresses的完整功能。所以最好直接设置listen\_addresses。

\-k directory

指定postgres用来监听来自客户端应用连接的 Unix 域套接字的目录。这个值也可以是一个逗号分隔的目录列表。一个空值指定不监听任何 Unix 域套接字，在这种情况下只能用 TCP/IP 套接字来连接到数据库。默认值通常是/tmp，但是可以在编译的时候修改。指定这个选项等效于设置unix\_socket\_directories配置参数。

\-l

启用使用SSL的安全连接。

\-N max-connections

设置该服务将接受的最大客户端连接数。该参数的默认值由initdb自动选择。指定这个选项等效于设置max\_connections配置参数。

\-o extra-options

在extra-options中指定的命令行风格的参数会被传递给所有由这个postgres进程派生的服务进程。

extra-options中的空格被视作参数分隔符，除非用反斜线（\\）转义。要表示一个字面意义上的反斜线，可以写成\\\\。通过多次使用-o 也可以指定多个参数。

这个选项的使用已经被废弃。用于服务进程的所有命令行选项可以在postgres命令行上直接指定。

\-p port

PG兼容模式的监听端口号。

默认为PGPORT环境变量的值。如果PGPORT没有设置，那么默认值是5866。如果你指定了一个非默认端口，那么所有客户端应用都必须用命令行选项或者PGPORT指定同一个端口。

\-o PORT

Oracle兼容模式的监听端口号。

\-s

在每条命令结束时打印时间信息和其它统计信息。这个选项对测试基准和调节缓冲区数量有用处。

\-S work-mem

指定内部排序和散列在使用临时磁盘文件之前能使用的内存数量。

\-V

\--version

打印postgres版本并退出。

\--name=value

设置一个命名的运行时参数；其缩写形式是-c。

\--describe-config

这个选项会用制表符分隔的COPY格式导出数据库服务的内部配置变量、描述以及默认值。设计它的目的是用于管理工具。

\-G

–highgo-version

输出postgres瀚高的版本信息，然后退出

\-?

\--help

显示有关postgres的命令行参数，并且退出。

- 半内部选项

这里描述的选项主要被用于调试目的，并且在某些情况下可以协助恢复严重受损的数据库。在生产数据库环境中应该不会去使用它们。在这里列举它们只是为了让数据库系统开发者使用。此外，这些选项可能在将来的版本中更改或删除，但不会另行通知。

\-f { s | i | o | b | t | n | m | h }

禁止某种扫描和连接方法的使用：s和i分别禁用顺序和索引扫描，o、b和t分别禁用只用索引扫描、位图索引扫描以及 TID 扫描，而n、m和h则分别禁用嵌套循环、归并和哈希连接。

顺序扫描和嵌套循环连接都不可能完全被禁用。-fs和-fn选项仅仅是在有其他选择时不鼓励优化器使用这些计划类型。

\-n

该选项主要用于调试导致服务器进程异常崩溃的问题。对付这种情况的一般策略是通知所有其它服务器进程，让它们终止并且接着重新初始化共享内存和信号量。这是因为一个错误的服务器进程可能在终止之前就已经对共享状态造成了破坏。该选项指定postgres将不会重新初始化共享数据结构。一个有经验的系统程序员这时就可以使用调试器检查共享内存和信号量状态。

\-O

允许修改系统表的结构。这个选项用于initdb。

\-P

读取系统表时忽略系统索引（但在更改系统表时仍然更新索引）。这在从损坏的系统索引中恢复时有用。

\-t pa\[rser\] | pl\[anner\] | e\[xecutor\]

打印与每个主要系统模块相关的查询的时间统计。这个选项不能和-s选项一起使用。

\-T

该选项主要用于调试导致服务进程异常崩溃的问题。对付这种情况的一般策略是通知所有其它服务进程，让它们终止并且接着重新初始化共享内存和信号量。这是因为一个错误的服务进程可能在终止之前就已经对共享状态造成了破坏。该选项指定postgres将通过发送SIGSTOP信号停止其他所有服务进程，但是并不让它们终止。这样就允许系统程序员手动从所有服务进程收集内核转储。

\-v protocol

声明这次会话使用的前/后服务器协议的版本数。该选项仅在内部使用。

\-W seconds

在一个新服务进程被启动时，它实施认证过程之后会延迟这个选项所设置的秒数。这就留出了机会来用一个调试器附着在服务进程上。

- 用于单用户模式的选项

下面的选项仅适用于单用户模式（见下文的单用户模式介绍）。

\--single

选择单用户模式。这必须是命令行中的第一个选项。

database

指定要访问的数据库的名称。这必须是命令行中的最后一个参数。如果省略它，则默认为用户名。

\-E

在执行命令之前回显所有命令到标准输出。

\-j

使用跟着两个新行的分号而不是仅用新行作为命令终止符。

\-r filename

将所有数据库日志输出发送到filename中。只有在作为一个命令行选项提供时，这个选项才会生效。

**环境**

PGCLIENTENCODING

客户端使用的默认字符编码（客户端可以独立地覆盖它）。这个值也可以在配置文件中设置。

PGDATA

默认的数据目录位置。

PGDATESTYLE

DateStyle运行时参数的默认值（这个环境变量的使用已被废弃）。

PGPORT

默认端口号（在配置文件中设置更好）

**诊断**

一个提到了semget或shmget的错误消息可能意味着你需要配置内核来提供足够的共享内存和信号量。你也可以通过降低shared\_buffers值减少数据库的共享内存消耗， 或者降低max\_connections值减少信号量消耗，这样可以推迟对内核的重新配置。

如果一个消息说另外一个服务已经在运行，应该仔细地检查，例如根据你的系统可以用命令

$ ps ax | grep postgres

或

$ ps -ef | grep postgres

如果你确信没有冲突的服务正在运行，那么你可以删除消息中提到的锁文件然后再次尝试。

如果一个失败消息指示它无法绑定到一个端口，可能意味着该端口已经被某些非瀚高数据库进程所使用。如果你终止postgres并且立即使用相同的端口重启它，你也可能会得到这种错误。在这种情况下，你必须等待几秒直到操作系统关闭该端口，然后再重试。最后，如果你指定了一个操作系统认为需要保留的端口号，你可能也会得到这个错误。例如，很多版本的Unix 认为低于 1024 的端口号是”可信的”并且只允许 Unix 超级用户访问它们。

**注释**

实用命令pg\_ctl可以用来安全方便地启动和关闭瀚高数据库服务。只要有可能，就不要使用SIGKILL杀死主postgres服务。这样会阻止postgres在终止前释放它持有的系统资源（例如共享内存和信号量）。这样可能会导致启动新的postgres进程时出现问题。

要正常地终止数据库服务，可以使用SIGTERM、SIGINT或者SIGQUIT信号。第一个在退出前将等待所有客户端终止，第二个将强行断开所有客户端的连接，第三个会不做正确的关闭立即退出并且会导致重启时进行恢复。

SIGHUP信号会重新加载服务器配置文件。也可以向一个单独的服务进程发送SIGHUP信号，但是这样做通常没什么意义。

要取消一个正在运行的查询，可以向运行该查询的进程发送SIGINT信号。要干净地终止一个后端进程，可向它发送SIGTERM。在 SQL 中可调用的与这两种动作等效的命令可参考用户手册第8章中的pg\_cancel\_backend和pg\_terminate\_backend。

数据库服务使用SIGQUIT来告诉子服务进程终止但不做正常的清理。该信号不应该被用户使用。向一个服务进程发送SIGKILL也是不明智的 — 主postgres进程将把这解释为一次崩溃，并且作为其标准崩溃恢复过程的一部分，它将强制所有的后代进程退出。

**缺陷**

\--选项在FreeBSD或OpenBSD上无法运行，应该使用-c。这在受影响的系统里是个缺陷；如果这个缺陷没有被修复，将来的瀚高数据库版本将提供一种解决方案。

**单用户模式**

要启动一个单用户模式的服务器，使用这样的命令

postgres --single -D /home/highgo/highgo/database/8.0/data other-options my\_database

用-D给数据库服务提供正确的数据库目录的路径，或者确保环境变量PGDATA被设置。同时还要指定你想在其中工作的特定数据库的名字。

通常，单用户模式的服务会把换行符当做命令输入的终止符。它不明白分号的作用，因为那属于psql。要想把一个命令分成多行，必须在最后一个换行符以外的每个换行符前面敲一个反斜线。这个反斜线和旁边的新行都会被从输入命令中去掉。注意即使在字符串或者注释中也会这样做。

但是如果使用了-j命令行选项，那么单个新行将不会终止命令输入。相反，分号-新行-新行的序列才会终止命令输入。也就是说，输入一个紧跟着空行的分号。在这种模式下，反斜线-新行不会被特殊对待。此外，在字符串或者注释内的这类序列也不会被特殊对待。

不管在哪一种输入模式中，如果输入的一个分号不是正好在命令终止符之前或者不是命令终止符的一部分，它会被认为是一个命令分隔符。当真正输入一个命令终止符时，已经输入的多个语句将被作为一个单个事务执行。

要退出会话，输入EOF（通常是Control+D）。如果从上一个命令终止符以来已经输入了任何文本，那么EOF将被当作命令终止符，并且如果要退出则需要另一个EOF。

请注意单用户模式的服务器不会提供复杂的行编辑特性（例如没有命令历史）。单用户模式也不会做任何后台处理，例如自动检查点或者复制。

**示例**

要用默认值在后台启动postgres：

> $ nohup postgres >logfile 2>&1 </dev/null &

要用指定端口启动postgres，例如 1234：

> $ postgres -p 1234

要使用psql连接到这个服务器，用 -p 选项指定这个端口：

> $ psql -p 1234

或者设置环境变量PGPORT：

> $ export PGPORT=1234
> 
> $ psql

命名运行时参数可以用这些形式之一设置：

> $ postgres -c work\_mem=1234
> 
> $ postgres --work-mem=1234

两种形式都覆盖postgresql.conf中可能存在的work\_mem设置。请注意在参数名中的下划线在命令行可以写成下划线或连字符。除了用于短期的实验外，更好的习惯是编辑postgresql.conf中的设置， 而不是倚赖命令行开关来设置参数。

## postmaster

postmaster — 瀚高数据库服务

**命令**

postmaster \[option...\]

**描述**

postmaster是postgres的一个废弃的别名。

## licchk

licchk — license检查工具

**命令**

/licchk \[OPTION\]... \[DATADIR\]

**描述**

licchk程序参数化查询客户端client\_info.dat、服务端license.dat文件,主要用来验证授权license.dat二进制文件的有效性，并对用户展示license基本信息和功能列表。

**选项**

\-l

\--list

列出启用的功能项。

\-a

\--all

所有功能项

\-v

\--view

显示描述信息

\-f

\--filename=xxx.dat

设置许可证文件名

\-c

\--check=xxx.txt

检查硬件码，并退出。

\-C

\--client-information

查询客户端client\_info.dat文件。

\-S

\--server-license

查询服务端icense.dat文件，不带参数默认查询服务端license.dat文件。

\-d

\--ignore-datetime-check

忽略license授权时间校验。

\-m

\--max-connections

显示license.dat中的最大连接数。

\-U

\--username

从license文件中获取用户名。

\-P

\--port

从license文件中获取端口号。

\-V

\--version

显示版本信息，并退出。

\-?

\--help

显示帮助信息，并退出。

## highgo2pg

highgo2pg主要适用于从瀚高数据库管理系统迁移至Postgresql14的数据库管理系统使用。

其使用方式及参数与pg\_upgrade保持一致。

限制使用说明：如需使用该工具，请联系瀚高工作人员获取相应介质。

## pg2highgo

pg2highgo主要适用于从Postgresql10到Postgresql14内核版本数据库管理系统迁移到瀚高数据库管理系统系统使用。

其使用方式及参数与pg\_upgrade保持一致。

限制使用说明：如需使用该工具，请联系瀚高工作人员获取相应介质。

## pg\_alterckey

pg\_alterckey-用于TDE的密钥轮换。支持更新主密钥，重新解密加密数 据密钥完成密钥轮换。

**命令**

pg\_alterckey \[OPTION\] old\_cluster\_key\_command new\_cluster\_key\_command \[DATADIR\]

pg\_alterckey \[repair\_option\] \[DATADIR\]

**选项**

其中OPTION可以为：

\-R

–authprompt

提示输入密码或PIN

\-D DATADIR

–pgdata=DATADIR

指定数据库目录

\-V

输出版本号

\-u

–upgrade

升级pg\_control文件

\-d

–downgrade

降级pg\_control文件

\-?

输出帮助信息

其中repair\_option为：

\-r

–repair

修复密钥

**说明**

因为加密机方式的特殊性，密钥轮换暂时不支持加密机方式。

## pg\_pgpass

pg\_pgpass - 加密或解密.pgpass 文件。

**命令**

pg\_pgpass \[OPTION\] \[DATADIR\]

**选项**

\-d

解密.pgpass文件。如果不指定该参数，表示加密.pgpass文件。

\[-P, –pgpass=\] PGPASSFILE

指定.pgpass目录。

\[-D, –pgdata=\]

指定数据库的data目录，表示使用数据库ID加密.pgpass文件。

\[-M, –interface=\]

获取指定网卡的 MAC 地址，表示使用MAC地址加密.pgpass文件。

\[-C, –customkey=\]

指定自定义密钥，表示使用自定义密钥加密.pgpass文件。

\-V

–version

输出版本信息，然后退出。

\-?

–help

显示帮助信息，然后退出。

**说明**

在使用pg\_pgpass工具加密时，需要按照hostname:port:database:username:password标准格式编写pgpass文件，该工具只加密用户密码部分，其它ip、端口、用户名等部分不会加密。详细用法可参加安全指南。