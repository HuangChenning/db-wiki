---
title: "系统包"
book: "Oracle兼容性"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/compatibility/compOracle4.html"
tags:
  - highgo
  - highgo-v9
  - compatibility-oracle
---

## 系统包

## DBMS\_JOB

DBMS\_JOB 是数据库中用于创建和管理自动化任务的工具，主要用于调度定时任务，如数据备份、维护、数据抽取等操作。

### 说明

以下是关于 DBMS\_JOB 的详细说明：

#### 任务创建

通过DBMS\_JOB.SUBMIT过程创建新的任务，指定要执行的PL/SQL 代码、存储过程或 SQL语句以及任务的执行时间和频率。

DBMS\_JOB.SUBMIT (

job OUT BINARY\_INTEGER,

what IN VARCHAR2,

next\_date IN DATE DEFAULT SYSDATE,

interval IN VARCHAR2 DEFAULT ‘null’,

no\_parse IN BOOLEAN DEFAULT FALSE,

instance IN BINARY\_INTEGER DEFAULT any\_instance,

force IN BOOLEAN DEFAULT FALSE);

以下为DBMS\_JOB.SUBMIT参数说明：

| **参数** | **描述** |
| --- | --- |
| job | 正在运行的作业 ID。 |
| what | 要运行的作业的 PL/SQL 文本。 |
| next\_date | 运行作业的下一个日期。 |
| interval | 计算下次运行作业的日期算法。默认为NULL。这必须计算为未来某个时间点或NULL。 |
| no\_parse | 参数兼容。 |
| instance | 参数兼容。 |
| force | 参数兼容。 |

#### 任务修改

使用DBMS\_JOB.CHANGE过程修改已存在的任务的执行时间、间隔或内容。

DBMS\_JOB.CHANGE (

job IN BINARY\_INTEGER,

what IN VARCHAR2,

next\_date IN DATE,

interval IN VARCHAR2,

instance IN BINARY\_INTEGER DEFAULT NULL,

force IN BOOLEAN DEFAULT FALSE);

以下为DBMS\_JOB.CHANGE参数说明：

| **参数** | **描述** |
| --- | --- |
| job | 正在运行的作业 ID。 |
| what | 要运行的 PL/SQL 过程。 |
| next\_date | 运行作业的下一个日期。 |
| interval | 计算下次运行作业的日期算法。 |
| instance | 参数兼容。 |
| force | 参数兼容。 |

#### 调度内容修改

通过DBMS\_JOB.WHAT过程修改要执行的PL/SQL 代码、存储过程或 SQL语句。

DBMS\_JOB.WHAT (

job IN BINARY\_INTEGER,

what IN VARCHAR2);

以下为DBMS\_JOB.WHAT参数说明：

| **参数** | **描述** |
| --- | --- |
| job | 正在运行的作业 ID。 |
| what | 要运行的 PL/SQL 过程。 |

#### 任务运行

通过DBMS\_JOB.RUN过程立即运行作业JOB。

DBMS\_JOB.RUN (

job IN BINARY\_INTEGER,

force IN BOOLEAN DEFAULT FALSE);

以下为DBMS\_JOB.RUN参数说明：

| **参数** | **描述** |
| --- | --- |
| job | 正在运行的作业 ID。 |
| force | 参数兼容 |

#### 任务停止

通过DBMS\_JOB.BROKEN过程来停止执行的JOB。

DBMS\_JOB.BROKEN (

job IN BINARY\_INTEGER,

broken IN BOOLEAN,

next\_date IN DATE DEFAULT SYSDATE);

以下为DBMS\_JOB.BROKEN参数说明：

| **参数** | **描述** |
| --- | --- |
| job | 正在运行的作业 ID。 |
| broken | 将作业设置为中断或不中断。TRUE将其设置为中断；FALSE将其设置为不中断。 |
| next\_date | 运行作业的下一个日期。 |

#### 间隔修改

通过DBMS\_JOB.INTERVAL过程来更改作业的运行频率。

DBMS\_JOB.INTERVAL (

job IN BINARY\_INTEGER,

interval IN VARCHAR2);

以下为DBMS\_JOB.INTERVAL参数说明：

|  |  |
| --- | --- |
| **参数** | **描述** |
| Job | 正在运行的作业 ID。 |
| interval | 计算下次运行作业的日期算法。 |

#### 调度时间修改

通过DBMS\_JOB.NEXT\_DATE过程来修改下次作业自动运行的时间。

DBMS\_JOB.NEXT\_DATE (

job IN BINARY\_INTEGER,

next\_date IN DATE DEFAULT SYSDATE);

以下为DBMS\_JOB.NEXT\_DATE参数说明：

| **参数** | **描述** |
| --- | --- |
| Job | 正在运行的作业 ID。 |
| next\_date | 运行作业的下一个日期。 |

#### 任务删除

通过DBMS\_JOB.REMOVE过程删除不再需要的任务。

DBMS\_JOB.REMOVE (

job IN BINARY\_INTEGER );

以下为DBMS\_JOB.REMOVE参数说明：

| **参数** | **描述** |
| --- | --- |
| Job | 正在运行的作业 ID。 |

#### 任务导出

通过DBMS\_JOB.USER\_EXPORT过程导出JOB。

DBMS\_JOB.USER\_EXPORT (

job IN BINARY\_INTEGER,

mycall IN OUT VARCHAR2);

以下为DBMS\_JOB.USER\_EXPORT参数说明：

| **参数** | **描述** |
| --- | --- |
| job | 正在运行的作业 ID。 |
| mycall | 重新创建给定作业的调用文本。 |
| myinst | 用于更改实例相关性的调用文本。 |

#### 任务监控

通过查询DBA\_JOBS和DBA\_JOBS\_RUNNING视图，可以查看任务的详细信息和运行状态，详见系统视图章节。

#### 日历语法格式关键字及描述

FREQ：指定了重复的类型。必须指定它。指定频率值为YEARLY, MONTHLY, DAILY, HOURLY,MINUTELY,SECONDLY。

INTERVAL：指定一个正整数，表示重复频率。默认为1，最大值为99。

BYMONTH：指定希望执行作业的月份。可以使用数字，例如1代表一月，3代表三月，以及三个字母的缩写，例如FEB代表二月，JUL代表七月。

BYMONTHDAY：指定月份中的日期数字。有效值为1到 31。例如10，表示所选月份的第10天。可以使用减号 (-) 从最后一天开始倒数，例如，BYMONTHDAY=-1表示该月的最后一天，BYMONTHDAY=-2表示该月的倒数第二天。

BYHOUR：指定作业运行的时。有效值为0到23。

BYMINUTE：指定作业运行的分。有效值为0到59。

BYSECOND：指定作业运行的秒。有效值为0到59。

#### 限制

本功能需要集成pgagent插件进行使用。

### 示例

\--首先启动pgagent

pgagent hostaddr=127.0.0.1 dbname=highgo user=highgo port=1521 -s /opt/apps/highgo/hgdb-enterprise-9.0.3/data\_oracle/hgdb\_log/pgagent\_log.log -t 1

\-- 在psql中创建job并返回jobid

\-- 该job会执行对应存储过程pro\_sync

\-- 每天的次日凌晨 2 点

declare jobid integer;

begin

dbms\_job.submit(jobid,’pro\_sync;’,’2025-03-24 02:00:00’,’trunc(sysdate)+26.0/(24)’);

end;

/

## DBMS\_OUTPUT

DBMS\_OUTPUT包在V9.0.5及以后的版本中支持。

DBMS\_OUTPUT包主要用于在函数、存储过程、包的调试或打印信息。

DBMS\_OUTPUT包中共包括如下7个存储过程，分别控制DBMS\_OUTPUT包功能的开启/关闭、维护和检索DBMS\_OUTPUT缓存空间。同时支持在交互式终端PSQL中设置客户端变量serveroutput（参见 SERVEROUTPUT ）来控制是否显示输出。

| 子程序 | 描述 |
| --- | --- |
| lENABLE | 启用消息输出 |
| lDISABLE | 禁止消息输出 |
| lGET\_LINE | 从缓冲区检索一行 |
| lGET\_LINES(与Oracle存在差异) | 从缓冲区检索多行 |
| lNEW\_LINE | 终止使用 PUT 创建的行 |
| lPUT | 在缓冲区放置部分行内容 |
| lPUT\_LINE | 将行放置在缓冲区 |

### ENABLE

此过程会启用对 PUT 、 PUT\_LINE 、 NEW\_LINE 、 GET\_LINE 和 GET\_LINES  
调用。

如果不执行ENABLE，默认情况下，DBMS\_OUTPUT系统包功能是禁用的。当你使用PSQL中的  
SET SERVEROUTPUT 选项时，没有必要调用此过程。

语法：

DBMS\_OUTPUT.ENABLE (buffer\_size IN INTEGER DEFAULT 20000);

参数：

- buffer\_size：可选参数，设置缓冲区的最大值（以字节为单位），将buffer\_size设置为NULL表示没有限制，默认值为20000，最大值为1000000，最小值为2000。

说明：

- 多次调用ENABLE时，buffer\_size以最后一次为准。
- buffer\_size参数在指定其值时分为两种情况：NULL和非NULL。当非NULL时，指定的值小于最小值2000，则buffer\_size=2000；如果指定的值大于最大值1000000，则buffer\_size=1000000。当buffer\_size为NULL时不限制内存的使用，但是我们并不希望无节制的消耗物理内存，所以当buffer\_size=  
	NULL时我们实现为等价于buffer\_size约等于1GB，实际会略小于1GB。

#### 示例

drop table tb;

create table tb(c1 varchar2(10),c2 int);

begin

dbms\_output.enable;

dbms\_output.put\_line('line1');

declare

v\_line varchar2(100);

v\_status integer;

begin

dbms\_output.get\_line(v\_line, v\_status);

insert into tb values(v\_line,v\_status);

end;

end;

/

查看表数据如下，表示成功在缓冲区中插入数据并获取：

select \* from tb;

c1 | c2

\-------+----

line1 | 0

(1 行记录)

### DISABLE

此过程关闭DBMS\_OUTPUT包的PUT、PUT\_LINE、NEW\_LINE、GET\_LINE和GET\_LINES存储过程对消息缓存的使用，当关闭时应用程序调用这些接口不会产生任何影响。该过程还会清除缓冲区中所有剩余信息，刷新缓存为空。

语法：

DBMS\_OUTPUT.DISABLE;

当客户端设置了SERVEROUTPUT时，不建议调用此存储过程，因为这会影响客户端的显示。

#### 示例

drop table tb;

create table tb(c1 varchar2(10),c2 int);

begin

dbms\_output.disable;

dbms\_output.put\_line('line1');

declare

v\_line varchar2(100);

v\_status integer;

begin

dbms\_output.get\_line(v\_line, v\_status);

insert into tb values(v\_line,v\_status);

end;

end;

/

查看表数据如下，说明缓冲区数据为空：

select \* from tb;

c1 | c2

\----+----

| 1

(1 行记录)

### GET\_LINE

此过程会从buffer中获取一行信息，获取之后，buffer中该行信息会被删除。

语法：

DBMS\_OUTPUT.GET\_LINE (

line OUT VARCHAR2,

status OUT INTEGER);

参数：

- line：返回缓存的一行信息，不包括末尾的换行符。
- status：执行结果的状态，成功获取一行返回0，否则返回1。

说明：

- 单行的最大值是32767字节，如果line变量长度小于实际行则会触发错误。
- 在调用GET\_LINE或GET\_LINES之后，在下一次调用  
	PUT、PUT\_LINE或NEW\_LINE之前未检索到的任何行都会被丢弃，以避免与下一条消息混淆。

#### 示例

begin

dbms\_output.enable;

dbms\_output.put\_line('line1');

dbms\_output.put\_line('line2');

declare

v\_line char(4000);

v\_status number:=0;

begin

dbms\_output.get\_line(v\_line, v\_status);

dbms\_output.put\_line(v\_line);

end;

end;

/

输出：

line1

PL/iSQL procedure successfully completed.

### GET\_LINES

此过程会从buffer中获取一行或多行信息，获取之后，buffer中该信息会被删除。

语法：

DBMS\_OUTPUT.GET\_LINES (

lines OUT TEXT\[\],

numlines IN OUT INTEGER);

参数：

- line：从缓冲区中返回的多行数组。
- numlines：从缓冲区中检索的行数。

说明：

- 在Oracle中，lines的类型为CHARARR或者DBMSOUTPUT\_LINESARRAY，目前V9暂不支持这两种类型，所以用text\[\]代替。此处是与Oracle的DBMS\_OUTPUT不兼容的地方。
- 在调用GET\_LINE或GET\_LINES之后，在下一次调用  
	PUT、PUT\_LINE或NEW\_LINE之前未检索到的任何行都会被丢弃，以避免与下一条消息混淆。

#### 示例

declare

v\_lines text\[\];

v\_numlines number:= 100;

begin

dbms\_output.enable(1000000);

dbms\_output.put\_line('line1');

dbms\_output.put\_line('line2');

dbms\_output.get\_lines(v\_lines, v\_numlines);

for i in 1..v\_numlines loop

if v\_lines\[i\] is not null then

dbms\_output.put\_line(v\_lines\[i\]);

end if;

end loop;

end;

/

输出：

line1

line2

PL/iSQL procedure successfully completed.

### NEW\_LINE

该过程向缓冲区添加一个换行符，产生新的一行。

语法：

DBMS\_OUTPUT.NEW\_LINE;

说明：

- 添加一个换行符，缓冲区中的行以此作为分隔符。
- GET\_LINE和GET\_LINES不会返回未以换行符结尾的行。
- 调用此过程时，如果之前已经调用过GET\_LINE和GET\_LINES并且缓存不为空，则丢弃其内容刷新缓存。

#### 示例

执行如下语句，输出的line1和line2在一行中：

begin

dbms\_output.enable(40000);

dbms\_output.put('line1');

dbms\_output.put\_line('line2');

end;

/

\--输出

line1line2

PL/iSQL procedure successfully completed.

使用new\_line之后：

begin

dbms\_output.enable(40000);

dbms\_output.put('line1');

dbms\_output.new\_line;

dbms\_output.put\_line('line2');

end;

/

\--输出

line1

line2

PL/iSQL procedure successfully completed.

### PUT

该过程将在buffer中的最后一行追加指定内容。

语法：

DBMS\_OUTPUT.PUT (item IN VARCHAR2);

参数：

- item：要缓存的部分行的内容。

说明：

- 此过程将部分行放入缓冲区中。
- 与PUT\_LINE不同，PUT过程不会自动在末尾追加一个换行符，因此多与NEW\_LINE一起使用。
- 调用此过程时，如果之前已经调用过GET\_LINE和GET\_LINES并且缓存不为空，则丢弃其内容刷新缓存。

#### 示例

SET SERVEROUTPUT ON;

BEGIN

\-- 使用 PUT 输出不换行的内容

DBMS\_OUTPUT.PUT('Hello, ');

DBMS\_OUTPUT.PUT('this is ');

DBMS\_OUTPUT.PUT('a single ');

DBMS\_OUTPUT.PUT('line.');

DBMS\_OUTPUT.PUT\_LINE('Hello!');

END;

/

输出：

Hello, this is a single line.Hello!

PL/iSQL procedure successfully completed.

### PUT\_LINE

该过程用来向buffer中增加一行新信息。

语法：

DBMS\_OUTPUT.PUT\_LINE (item IN VARCHAR2);

参数：

- item：要缓存的整行的内容。

说明：

- 自动在末尾追加换行符。
- 使用PUT和PUT\_LINE创建的输出消息是被缓存起来的，直到程序执行完才检索其输出。
- 调用此过程时，如果之前已经调用过GET\_LINE和GET\_LINES并且缓存不为空，则丢弃其内容刷新缓存。

#### 示例

\-- 启用输出显示

SET SERVEROUTPUT ON;

BEGIN

\-- 直接输出文本

DBMS\_OUTPUT.PUT\_LINE('Hello, Highgo!');

\-- 输出变量值

DECLARE

v\_name VARCHAR2(20):= 'World';

v\_date DATE:= SYSDATE;

BEGIN

DBMS\_OUTPUT.PUT\_LINE('Hello, ' || v\_name || '!');

DBMS\_OUTPUT.PUT\_LINE('Today is: ' || TO\_CHAR(v\_date,  
'YYYY-MM-DD'));

END;

END;

/

结果如下：

Hello, Highgo!

Hello, World!

Today is: 2025-09-01

PL/iSQL procedure successfully completed.