---
title: "dimp 逻辑导入"
book: "DM8 dexp 和 dimp 手册"
version: "DM8"
source: https://eco.dameng.com/document/dm/zh-cn/pm/dimp-logical import.html
tags:
  - dameng
  - dm8
  - dexp-dimp
---

dimp 逻辑导入工具利用 dexp 工具生成的备份文件对本地或远程的数据库进行联机逻辑还原。dimp 导入是 dexp 导出的相反过程。还原的方式可以灵活选择，如是否忽略对象存在而导致的创建错误、是否导入约束、是否导入索引、导入时是否需要编译、是否生成日志等。

dimp 工具名称有两种写法 dimp 和 dimpdp，两者区别在于：dimp 导入的文件必须存放在客户端，dimpdp 导入的文件必须存放在服务器端。另外由于 dimpdp 是将客户端命令发给服务器启动 dimp 执行，如果客户端连接使用 dm\_svc.conf 配置，服务器端也应该跟客户端配置一致。

## 3.1 使用 dimp 工具

dimp 工具需要从命令行启动。在 cmd 命令行工具中找到 dimp 所在安装目录/dmdbms/bin，输入 dimp 和参数后回车。参数在下一节详细介绍。

**语法如下：**

```
dimp PARAMETER=value { PARAMETER=value }
或
dimpdp  PARAMETER=value { PARAMETER=value }
```

PARAMETER：dimp 参数。其中 USERID 必须为第一个参数，其余参数之间排列顺序无影响，参数之间使用空格间隔。

value：参数取值。

例 将逻辑备份采用 FULL 方式完全导入到用户名为 SYSDBA，密码以“Dmsys\_123”为例，实际运行中需要用户自行替换为数据库初始化时设定的密码。IP 地址为 192.168.0.248，端口号为 8888 的数据库。导入文件名为 db\_str.dmp，导入的日志文件名为 db\_str.log，路径为/mnt/data/dexp。

```
./dimp USERID=SYSDBA/Dmsys_123@192.168.0.248:8888 FILE=db_str.dmp DIRECTORY=/mnt/data/dexp LOG=db_str.log FULL=Y
```

## 3.2 dimp 参数一览表

本节提供 dimp 的参数一览表，供用户快速参考。

表3.1 dimp参数一览表

<table><tbody><tr height="20"><td height="20" width="191"><b>参数</b></td><td width="612"><b>含义</b></td><td width="412"><b>备注</b></td></tr><tr height="33"><td height="33" width="191"><span>USERID</span></td><td width="612">数据库的连接信息</td><td width="412">必选</td></tr><tr height="20"><td height="20" width="191"><span>FILE</span></td><td width="612">输入文件，即dexp或dexpdp导出的文件</td><td width="412">可选</td></tr><tr height="20"><td height="20" width="191"><span>LOG</span></td><td width="612">日志文件</td><td width="412">可选</td></tr><tr height="20"><td height="20" width="191"><span>DIRECTORY</span></td><td width="612">导入文件所在目录</td><td width="412">可选</td></tr><tr height="20"><td height="20" width="191"><span>FULL</span></td><td width="612">整库导入(N)</td><td rowspan="4" width="412">可选，四者中选其一。缺省为导入的文件导出时所用的方式</td></tr><tr height="20"><td height="20" width="191"><span>OWNER</span></td><td width="612">以用户方式导入</td></tr><tr height="20"><td height="20" width="191"><span>SCHEMAS</span></td><td width="612">以模式方式导入</td></tr><tr height="20"><td height="20" width="191"><span>TABLES</span></td><td width="612">以表名方式导入，指定导入的 <font>tables</font> <font>名称。不支持对外部表进行导入</font></td></tr><tr height="20"><td height="20" width="191"><span>PARALLEL</span></td><td width="612">用于指定导入的过程中所使用的线程数目(16)</td><td width="412">可选</td></tr><tr height="20"><td height="20" width="191"><span>TABLE_PARALLEL</span></td><td width="612">用于指定导入的过程中每个表所使用的子线程数目(8)</td><td width="412">可选。在 <font>FAST_LOAD</font> <font>为</font> <font>Y</font> <font>时有效</font></td></tr><tr height="20"><td height="20" width="191"><span>IGNORE</span></td><td width="612">忽略创建错误 <font>(N)</font> <font>。如果表已经存在则向表中插入数据，否则报错表已经存在。</font></td><td width="412">可选</td></tr><tr height="19"><td height="19" width="191"><span>TABLE_EXISTS_ACTION</span></td><td width="612">需要的导入表在目标库中存在时采取的操作[SKIP | APPEND | TRUNCATE | REPLACE | TRUNCATE_CASCADE]</td><td width="412">可选</td></tr><tr height="20"><td height="20" width="191"><span>FAST_LOAD</span></td><td width="612">是否使用 <font>dmfldr</font> <font>进行数据导入</font> <font>(N)</font></td><td width="412">可选</td></tr><tr height="20"><td height="20" width="191"><span>FLDR_ORDER</span></td><td width="612">使用 <font>dmfldr</font> <font>是否需要严格按顺序来导数据</font> <font>(Y)</font></td><td width="412">可选</td></tr><tr height="20"><td height="20" width="191"><span>COMMIT_ROWS</span></td><td width="612">批量提交的行数 <font>(5000)</font></td><td width="412">可选</td></tr><tr height="32"><td rowspan="2" height="147"><span>EXCLUDE</span></td><td>批量设置导入时忽略的对象种类。<br><span>1.EXCLUDE=[(]<对象种类名>{,<对象种类名>}[)]<br><font>对象种类可为：</font> <font>CONSTRAINTS</font> <font>、</font> <font>INDEXES</font> <font>、</font> <font>ROWS</font> <font>、</font> <font>TRIGGERS</font> <font>、</font> <font>GRANTS</font> <font>、</font> <font>VIEWS</font> <font>、</font> <font>PROCEDURE</font> <font>、</font> <font>PACKAGE</font> <font>、</font> <font>SEQUENCE</font> <font>、</font> <font>TABLES</font> <font>、</font> <font>JOB</font> <font>、</font> <font>STATISTICS</font> <font>、</font> <font>HINT</font> <font>。</font></span></td><td rowspan="2">可选</td></tr><tr height="48"><td height="48"><span>2. <font>EXCLUDE=TYPE:name1,name2<br>TYPE</font> <font>可为</font> <font>SCHEMAS、TABLES、VIEWS、PROCEDURE、PACKAGE、SEQUENCE。</font></span></td></tr><tr height="32"><td rowspan="2" height="147"><span>INCLUDE</span></td><td>批量设置导入时只导入指定的对象种类或某个具体对象。<br><span>1.INCLUDE=[(]<对象种类名>{,<对象种类名>}[)]<br><font>对象种类可为：</font> <font>CONSTRAINTS</font> <font>、</font> <font>INDEXES</font> <font>、</font> <font>ROWS</font> <font>、</font> <font>TRIGGERS</font> <font>、</font> <font>GRANTS</font> <font>、</font> <font>VIEWS</font> <font>、</font> <font>PROCEDURE</font> <font>、</font> <font>PACKAGE</font> <font>、</font> <font>SEQUENCE</font> <font>、</font> <font>TABLES</font> <font>、</font> <font>JOB</font> <font>、</font> <font>STATISTICS</font> <font>、</font> <font>HINT</font> <font>。</font></span></td><td rowspan="2">可选</td></tr><tr height="48"><td height="48"><span>2. <font>INCLUDE=TYPE:name1,name2<br>TYPE</font> <font>可为</font> <font>SCHEMAS、TABLES、VIEWS、PROCEDURE、PACKAGE、SEQUENCE。</font></span></td></tr><tr height="20"><td height="20" width="191"><span>GRANTS</span></td><td width="612">导入权限 <font>(Y)</font></td><td width="412">可选</td></tr><tr height="20"><td height="20" width="191"><span>CONSTRAINTS</span></td><td width="612">导入约束 <font>(Y)</font></td><td width="412">可选</td></tr><tr height="20"><td height="20" width="191"><span>INDEXES</span></td><td width="612">导入索引 <font>(Y)</font></td><td width="412">可选</td></tr><tr height="20"><td height="20" width="191"><span>TRIGGERS</span></td><td width="612">导入触发器（ <font>Y</font> <font>）</font></td><td width="412">可选</td></tr><tr height="20"><td height="20" width="191"><span>ROWS</span></td><td width="612">导入数据行 <font>(Y)</font></td><td width="412">可选</td></tr><tr height="20"><td height="20" width="191"><span>NOLOGFILE</span></td><td width="612">不使用日志文件 <font>(N)</font></td><td width="412">可选</td></tr><tr height="20"><td height="20" width="191"><span>NOLOG</span></td><td width="612">屏幕上不显示日志信息 <font>(N)</font></td><td width="412">可选</td></tr><tr height="19"><td height="39" width="191"><span>DUMMY</span></td><td width="612">设置交互信息处理(P：打印)</td><td width="412">可选</td></tr><tr height="20"><td height="20" width="191"><span>LOG_WRITE</span></td><td width="612">日志信息实时写入文件 <font>(N)</font></td><td width="412">可选</td></tr><tr height="20"><td height="20" width="191"><span>PARFILE</span></td><td width="612">参数文件名，如果 <font>dimp</font> <font>的参数很多，可以存成参数文件</font></td><td width="412">可选</td></tr><tr height="20"><td height="20" width="191"><span>FEEDBACK</span></td><td width="612">显示每 <font>x</font> <font>行</font> <font>(0)</font> <font>的进度</font></td><td width="412">可选</td></tr><tr height="20"><td height="20" width="191"><span>COMPILE</span></td><td width="612">编译过程<font>,</font> <font>程序包和函数</font> <font>(Y)</font></td><td width="412">可选</td></tr><tr height="20"><td height="20" width="191"><span>INDEXFILE</span></td><td width="612">将表的索引 <font>/</font> <font>约束信息写入指定的文件</font></td><td width="412">可选</td></tr><tr height="20"><td height="20" width="191"><span>INDEXFIRST</span></td><td width="612">导入时先建索引 <font>(N)</font></td><td width="412">可选</td></tr><tr height="20"><td height="20" width="191"><span>REMAP_SCHEMA</span></td><td width="612"><span>SOURCE_SCHEMA <font>：</font> <font>TARGET_SCHEMA</font> <font>将</font> <font>SOURCE_SCHEMA</font> <font>中的数据导入到</font> <font>TARGET_SCHEMA</font> <font>中</font></span></td><td width="412">可选</td></tr><tr height="20"><td height="20" width="191"><span>ENCRYPT_PASSWORD</span></td><td width="612">数据的加密密钥</td><td width="412">可选。和 <font>dexp</font> <font>中的</font> <font>ENCRYPT_PASSWORD</font> <font>设置的密钥一样</font></td></tr><tr height="20"><td height="20" width="191"><span>ENCRYPT_NAME</span></td><td width="612">数据的加密算法的名称</td><td width="412">可选。和 <font>dexp</font> <font>中的</font> <font>ENCRYPT_NAME</font> <font>设置的加密算法一样</font></td></tr><tr height="20"><td height="20" width="191"><span>SHOW/ DESCRIBE</span></td><td width="612">打印出指定文件的信息 <font>(N)</font></td><td width="412">可选</td></tr><tr height="60"><td height="60" width="191"><span>TASK_THREAD_NUMBER</span></td><td width="612">用于设置 <font>dmfldr</font> <font>处理用户数据的线程数目</font></td><td width="412">可选</td></tr><tr height="59"><td height="59" width="191"><span>BUFFER_NODE_SIZE</span></td><td width="612">用于设置 <font>dmfldr</font> <font>读入文件缓冲区大小</font></td><td width="412">可选</td></tr><tr height="72"><td height="72" width="191"><span>TASK_SEND_NODE_NUMBER</span></td><td width="612">用于设置 <font>dmfldr</font> <font>发送节点个数，取值范围16~65535</font></td><td width="412">可选</td></tr><tr height="20"><td height="20" width="191"><span>LOB_NOT_FAST_LOAD</span></td><td width="612">如果一个表含有大字段，则不使用 <font>dmfldr(N)</font></td><td width="412">可选</td></tr><tr height="20"><td height="20" width="191"><span>PRIMARY_CONFLICT</span></td><td width="612">主键冲突的处理方式， <font>默认报错</font></td><td width="412">可选</td></tr><tr height="53"><td height="53" width="191"><span>TABLE_FIRST</span></td><td width="612">是否强制先导入表 <font>(</font><font>缺省</font> <font>N)。Y</font> <font>表示先导入表</font> <font>，N</font> <font>正常导入</font></td><td width="412">可选</td></tr><tr height="53"><td height="53" width="191"><span>SHOW_SERVER_INFO</span></td><td width="612">是否显示服务器信息 <font>(</font><font>N)，Y</font> <font>表示显示导出文件对应服务器信息，实际不导入</font> <font>，N</font> <font>表示不显示导出文件对应服务器信息，正常导入</font></td><td width="412">可选</td></tr><tr height="53"><td height="53" width="191"><span>IGNORE_INIT_PARA</span></td><td width="612">指定源库和目标库之间忽略差异的建库参数(0)。0：不忽略建库参数差异，1：忽略CASE_SENSITIVE，2：忽略LENGTH_IN_CHAR，3：忽略CASE_SENSITIVE和LENGTH_IN_CHAR</td><td width="412">可选</td></tr><tr height="50"><td height="50" width="191"><span>AUTO_FREE_KEY</span></td><td width="612">导入数据完成后, 是否释放密钥(N)。Y：是，N：否</td><td width="412">可选</td></tr><tr height="50"><td height="50" width="191"><span>REMAP_TABLE</span></td><td width="612">格式(SOURCE_TABLE:TARGET_TABLE)，<br>将SOURCE_TABLE中的数据导入到TARGET_TABLE中</td><td width="412">可选</td></tr><tr height="50"><td height="50" width="191"><span>REMAP_TABLESPACE</span></td><td width="612">格式(SOURCE_TABLESPACE:TARGET_TABLESPACE)<br>将SOURCE_TABLESPACE表空间映射到TARGET_TABLESPACE表空间中</td><td width="412">可选</td></tr><tr height="50"><td height="50" width="191"><span>SIMPLE_LOG</span></td><td width="612">导入日志是否使用简要日志(N)</td><td width="412">可选</td></tr><tr height="50"><td height="50" width="191"><span>DATA_ONLY</span></td><td width="612">是否只导入表数据(N)</td><td width="412">可选</td></tr><tr height="50"><td height="50" width="191"><span>INDEX_OPTION</span></td><td width="612">使用快速装载时索引的设置选项(2)。1：不刷新二级索引，数据按照索引先排序，装载完后再将排序的数据插入索引；2：不刷新二级索引，数据装载完成重建后所有二级索引；刷新二级索引，数据装载的同时将数据插入二级索引；3：代表服务器使用追加模式来进行二级索引的插入，在数据装载的过程中，同时进行二级索引的插入。若未禁用全局索引，则在非DPC环境下，全局索引可通过设置INDEX_OPTION为3进行插入</td><td width="412">可选</td></tr><tr height="50"><td height="50" width="191"><span>CTRL_INFO</span></td><td width="612">控制信息用来控制一些特殊情况导入(2)。0：不导入表空间定义，1：导入表空间定义，2：校验导入文件的MD5值，并执行导入，4：校验导入文件的MD5值，但不执行导入，8：导入对象时忽略OR REPLACE条件，16：导入时使用指定的remap_schema参数替换列定义默认值序列的模式名，32：当remap_schema参数设置出现报错时终止导入，64：控制每张表在数据导入完成后提交一次，保证表级原子性</td><td width="412">可选</td></tr><tr height="50"><td height="50" width="191"><span>CONFIG_FILE</span></td><td width="612">配置文件路径，配置默认连接串和密码信息</td><td width="412">可选</td></tr><tr height="50"><td height="50" width="191"><span>FILE_VERSION</span></td><td width="612">用于指定将dmp文件降级后生成的新dmp文件的逻辑版本，可以通过帮助信息查看取值范围</td><td width="412">可选</td></tr><tr height="50"><td height="50" width="191"><span>HELP</span></td><td width="612">显示帮助信息</td><td width="412">可选</td></tr></tbody></table>

> **说明**
> 
> 每个参数含义后面的括号内为(N)则表示该参数缺省为否，为(Y)表示缺省为是；“()”内的值表示的是参数的缺省值。

## 3.3 dimp 参数详解

### 3.3.1 特殊参数

特殊参数中介绍了必选参数的和最常用的可选参数。

#### 3.3.1.1 USERID

USERID 用于指定数据库的连接信息。

若配置文件 dm\_svc.conf 中配置了导入导出默认连接串，或者使用 CONFIG\_FILE 参数指定了局部配置文件，并且局部配置文件中配置了导入导出默认连接串，则可以不指定 USERID 参数；否则必须指定 USERID 参数。用法请参考 dexp 中 USERID。

#### 3.3.1.2 FILE

FILE 用于指定导入文件（可以包含路径）。导入文件是之前使用 dexp 或 dexpdp 导出的文件，其中文件名不能包含特殊符号（\\、/、:、\*、？、"、<、>、|）。可选参数，dimp 默认使用 dexp.dmp 作为导入文件，dimpdp 默认使用 dexpdp.dmp 作为导入文件 。长度不超过 128 个字符。

**语法如下：**

```
FILE=<文件>
```

例 之前导出的文件路径为：FILE=/mnt/data/dexp/db\_str.dmp，那么导入文件可以写成如下所示：

```
./dimp USERID=SYSDBA/Dmsys_123 FILE=/mnt/data/dexp/db_str.dmp LOG=db_str.log DIRECTORY=/mnt/data/dimp
```

若 FILE 没有指定文件路径，则可在 DIRECTORY 中指定。

> **说明**
> 
> 如果FILE指定的文件包含生成路径，则忽略DIRECTORY中的路径；  
> 如果FILE没有指定路径时，使用DIRECTORY中指定的路径；  
> 如果FILE和DIRECTORY都没有指定路径，则使用系统当前路径。

#### 3.3.1.3 LOG

LOG 用于明确指定导入过程产生的日志文件名称（可以包含路径），可以包含多个文件，用逗号分隔，其中文件名不能包含特殊符号（\\、/、:、\*、？、"、<、>、|）。可选参数，如果不选用 LOG 参数（来明确指定日志文件名称），那么 dimp 默认的导入日志文件名称为 dimp.log，dimpdp 默认的导入日志文件名称为 dimpdp.log。长度不超过 256 个字符，绝对路径不超过 256 个字符。

**语法如下：**

```
LOG=<文件名>
```

例 指定日志文件名为 db\_str.log。

```
./dimp USERID=SYSDBA/Dmsys_123 FILE=/mnt/data/dexp/db_str.dmp LOG=db_str.log FULL=Y
DIRECTORY=/mnt/data/dimp
```

> **说明**
> 
> 如果LOG指定的文件包含生成路径，则忽略DIRECTORY中的路径；  
> 如果LOG没有指定路径时，使用DIRECTORY中指定的路径；  
> 如果LOG和DIRECTORY都没有指定路径，则使用系统当前路径。

文件也可以在生成过程中自动扩展成多个，详细的扩展规则介绍和 dexp LOG 中一样，请参考 dexp 的 LOG。

导入日志记录了导入的整个过程信息和导入对象的统计信息，供用户查看。详细的 dimp 日志格式介绍和 dexp LOG 中一样，请参考 dexp 的 LOG。

和 LOG 有关的参数还有 NOLOGFILE、NOLOG 和 LOG\_WRITE。NOLOGFILE=Y 用于设置不使用日志文件。NOLOG=Y 用于设置不在屏幕上显示日志信息。LOG\_WRITE=Y 用于设置日志的实时打印（到日志文件）功能。

#### 3.3.1.4 DIRECTORY

DIRECTORY 用于指定导入文件及日志文件生成的路径。长度不超过 256 个字符。

使用 dimp 工具时，DIRECTORY 为可选参数，缺省导出到 dimp 所在路径。

使用 dimpdp 工具时，DIRECTORY 为必选参数，并且指定的路径必须是通过 CREATE DIRECTORY 定义的目录名。

**语法如下：**

```
DIRECTORY=<path>
```

\<path>：导入文件路径和日志文件生成的路径。

如果 FILE 和 LOG 参数指定的文件包含生成路径，则 FILE 和 LOG 参数中指定的路径将替代 DIRECTORY 所指定的路径；如果 FILE 和 LOG 参数指定的文件未包含路径信息，则导入文件路径和日志生成的文件路径都是 DIRECTORY 指定的路径；如果都没有指定路径，程序将根据当前的运行环境来设置相应的导出路径，一般为当前路径。

例 1 没有指定路径，使用当前路径。

```
./dimp USERID=SYSDBA/Dmsys_123 FILE=db_str.dmp LOG=db_str.log FULL=Y
```

例 2 指定 FILE 使用/mnt/data/dexp 路径，LOG 使用/mnt/data/dimp 路径。

```
./dimp USERID=SYSDBA/Dmsys_123 FILE=/mnt/data/dexp db_str.dmp LOG=db_str.log FULL=Y DIRECTORY=/mnt/data/dimp
```

> **说明**
> 
> FILE和LOG中指定的路径，优先级高于DIRECTORY中指定的路径；  
> 当FILE和LOG不指定路径时，才使用DIRECTORY指定的路径；  
> 如果都没有指定路径，则使用系统当前路径。

#### 3.3.1.5 四种级别的导入方式

针对数据库对象，有 FULL、OWNER、SCHEMAS、TABLES 四种导入方式可供选择。一次导入只能指定一种方式。可选参数，缺省为导入的文件导出时所用的方式。

> **小窍门**
> 
> 导入方式可以和导出方式不一致。  
> 例如：当导出方式不为FULL时，导入时也可以指定为FULL方式，此时 的FULL会将导出文件包含的全部内容导入到指定的实例中。

##### 3.3.1.5.1 FULL

FULL 方式导入整个数据库。

**语法如下：**

```
FULL=Y/N
```

设置 FULL=Y 时指定以 FULL 方式导入整个数据库；设置 FULL=N 相当于没有设置 FULL 参数，缺省为 N。

例 设置 FULL=Y，导入整个数据库，导入的数据库文件在/mnt/data/dexp，即将生成的日志文件放在/mnt/data/dimp。

```
./dimp USERID=SYSDBA/Dmsys_123 FILE=/mnt/data/dexp/db_str.dmp LOG=db_str.log FULL=Y
DIRECTORY=/mnt/data/dimp
```

##### 3.3.1.5.2 OWNER

OWNER 方式导入一个或多个用户拥有的所有对象。

**语法如下：**

```
OWNER=<用户名>{,<用户名>}
```

例 设置 OWNER=USER01，导入用户 USER01 所拥有的对象全部导出。导入的数据库文件在/mnt/data/dexp，即将生成的日志文件放在/mnt/data/dimp。

```
./dimp USERID=SYSDBA/Dmsys_123 FILE=/mnt/data/dexp/db_str.dmp LOG=db_str.log
OWNER=USER01 DIRECTORY=/mnt/data/dimp
```

##### 3.3.1.5.3 SCHEMAS

SCHEMAS 方式的导入一个或多个模式下的所有对象。

**语法如下：**

```
SCHEMAS=<模式名>{,<模式名>}
```

例 设置 SCHEMAS=USER01，导入模式 USER01 模式下的所有对象。导入的数据库文件在/mnt/data/dexp，即将生成的日志文件放在/mnt/data/dimp。

```
./dimp USERID=SYSDBA/Dmsys_123 FILE=/mnt/data/dexp/db_str.dmp LOG=db_str.log
SCHEMAS=USER01 DIRECTORY=/mnt/data/dimp
```

> **说明**
> 
> 一般情况下，OWNER与SCHEMAS导入导出是相同的。 但是用户可以包含多个模式，在这种情况下SCHEMAS的导入导出是OWNER导入导出的一个子集。

##### 3.3.1.5.4 TABLES

TABLES 方式导入一个或多个指定的表或表分区。导入所有数据行、约束、索引等信息。

**语法如下：**

```
TABLES=[模式名.]表名[:表分区名] [, ...]
```

例 设置 TABLES=table1,table2，导入 table1,table2 两张表的所有数据和信息。导入的数据库文件在/mnt/data/dexp，即将生成的日志文件放在/mnt/data/dimp。

```
./dimp USERID=SYSDBA/Dmsys_123 FILE=/mnt/data/dexp/db_str.dmp LOG=db_str.log
TABLES=table1,table2 DIRECTORY=/mnt/data/dimp
```

和 TABLES 导入有关的参数还有 EXCLUDE，用来指定导入时过滤掉某类对象。

### 3.3.2 普通参数

#### 3.3.2.1 PARALLEL

PARALLEL 用于指定导入的过程中所使用的线程数目。可选参数。如果 CPU 核数为 N 的话，那一般来说 PARALLEL 为 N 或者 N+1 最合适。

**语法如下：**

```
PARALLEL=<num>
```

\<num>：线程数。整数类型，取值范围：1~100，缺省为 16。

例 设置 PARALLEL=2 时，则线程数为 2。

```
./dimp USERID=SYSDBA/Dmsys_123 FILE=/mnt/data/dexp/db_str.dmp LOG=db_str.log FULL=Y
DIRECTORY=/mnt/data/dimp PARALLEL=2
```

#### 3.3.2.2 TABLE\_PARALLEL

TABLE\_PARALLEL 在 FAST\_LOAD 为 Y 时有效，用于指定导入每张表所使用的线程数。可选参数。如果 CPU 核数为 N 的话，那一般来说 TABLE\_PARALLEL 为 N 或者 N+1 最合适。在 MPP 模式下会转换成单线程。

**语法如下：**

```
TABLE_PARALLEL=<num>
```

\<num>：线程数。整数类型，取值范围 1~16，缺省值为 8。

例 设置 TABLE\_PARALLEL=3 时则线程数为 3。

```
./dimp USERID=SYSDBA/Dmsys_123 FILE=/mnt/data/dexp/db_str.dmp LOG=db_str.log FULL=Y
DIRECTORY=/mnt/data/dimp TABLE_PARALLEL=3
```

#### 3.3.2.3 IGNORE

IGNORE 指定忽略创建数据库对象（表、类、java 类、domain、sequence、  
comment、view、synonym、trigger、package、dblink、user、存储过程/函数、role 对象创建、权限授权语句、索引、约束等）错误。可选参数。缺省为 N，不忽略。

**语法如下：**

```
IGNORE=Y/N
```

Y：忽略导入时所产生的创建数据库对象错误并继续执行。

N：不忽略导入时所产生的创建数据库对象错误。遇到错误的表会停止执行并报错，其他正常的表继续执行。缺省值

#### 3.3.2.4 TABLE\_EXISTS\_ACTION

TABLE\_EXISTS\_ACTION 用于要导入的表已经存在时的处理方式。默认为直接报错。

**语法如下：**

```
TABLE_EXISTS_ACTION=[SKIP | APPEND | TRUNCATE | REPLACE | TRUNCATE_CASCADE]
```

SKIP：跳过此表。

APPEND：直接向现有表中导入数据。

TRUNCATE：先删除现有表中的数据，再向表中导入数据。

REPLACE：先删除现有表，再导数据。

TRUNCATE\_CASCADE：先删除现有表中的数据，并且级联删除依赖表数据，再向表中导入数据。

#### 3.3.2.5 FAST\_LOAD

FAST\_LOAD 用于设置是否使用 dmfldr 进行数据导入，缺省为 N。

**语法如下：**

```
FAST_LOAD=Y/N
```

Y：是。

N：否，缺省值。

> **注意**
> 
> 当FAST\_LOAD=Y时才可以设置TABLE\_PARALLEL参数，否则TABLE\_PARALLEL参数无效。  
> 当FAST\_LOAD=Y时可能会因为启动多个dmfldr造成内存不足，若服务器端出现OUT OF MEMORY情况，建议调小PARALLEL的值。

#### 3.3.2.6 FLDR\_ORDER

FLDR\_ORDER 用于设置使用 dmfldr 时，是否严格按导出顺序来导入数据。可选参数。

**语法如下：**

```
FLDR_ORDER=Y/N
```

Y：表示按照导出顺序来导入数据，缺省值。

N：表示不按照导出顺序来导入，数据的创建为随机生成。

#### 3.3.2.7 COMMIT\_ROWS

COMMIT\_ROWS 用于设置批量提交的行数，默认为 5000 行。用户可以根据实际情况调整每次提交的行数，以达到性能的最佳点。一般情况下可不设置。可选参数。

**语法如下：**

```
COMMIT_ROWS=<num>
```

\<num>：行数。取值范围：1~1000000，缺省为 5000。

#### 3.3.2.8 EXCLUDE

EXCLUDE 用来批量设置导入时忽略的对象种类。可选参数。

**语法如下：**

```
EXCLUDE=[(]<对象种类名>{,<对象种类名>}[)]
或
EXCLUDE=TYPE:name1,name2
```

< 对象种类名 >：包括 CONSTRAINTS、INDEXES、ROWS、TRIGGERS、GRANTS、VIEWS、PROCEDURE、PACKAGE、SEQUENCE、TABLES、JOB、STATISTICS、HINT。例如：EXCLUDE=(CONSTRAINTS, INDEXES)。

TYPE：包括 SCHEMAS、TABLES、VIEWS、PROCEDURE、PACKAGE、SEQUENCE。

- 当 TYPE 为 SCHEMAS 时，忽略指定的模式，使用 SCHEMAS:INFO 格式。例如：EXCLUDE= SCHEMAS:SCH1,SCH2。
- 当 TYPE 为 TABLES 时，忽略指定的表，使用 TABLES:INFO 格式。例如：EXCLUDE= TABLES:table1,table2。
- 当 TYPE 为 VIEWS 时，忽略指定的视图，使用 VIEWS:INFO 格式。例如：EXCLUDE= VIEWS:view1,view2。
- 当 TYPE 为 PROCEDURE 时，忽略指定的存储过程和存储函数。
- 当 TYPE 为 PACKAGE 时，忽略指定的包。
- 当 TYPE 为 SEQUENCE 时，忽略指定的序列。

例 设置 EXCLUDE=(CONSTRAINTS)，将当前用户下的 table1、table2 的对象信息导入时不导入除主键和非空约束外的其他约束。

```
./dimp SYSDBA/Dmsys_123 FILE=/mnt/data/db_str.dmp LOG=db_str.log
TABLES=table1,table2 EXCLUDE=\(CONSTRAINTS\) DIRECTORY=/mnt/data/dimp
```

#### 3.3.2.9 INCLUDE

INCLUDE 用来批量设置导入时只导入指定的对象种类或某个具体对象。可选参数。

```
INCLUDE=[(]<对象种类名>{,<对象种类名>}[)]
或
INCLUDE=TYPE:name1,name2
```

< 对象种类名 >：包括 CONSTRAINTS、INDEXES、ROWS、TRIGGERS、GRANTS、VIEWS、PROCEDURE、PACKAGE、SEQUENCE、TABLES、JOB、STATISTICS、HINT。例如：INCLUDE=(CONSTRAINTS, INDEXES)。

TYPE：包括 SCHEMAS、TABLES、VIEWS、PROCEDURE、PACKAGE、SEQUENCE。

- 当 TYPE 为 SCHEMAS 时，只导入指定的模式，使用 SCHEMAS:INFO 格式。例如：INCLUDE=SCHEMAS:SCH1,SCH2。
- 当 TYPE 为 TABLES 时，只导入指定的表，使用 TABLES:INFO 格式。例如：INCLUDE= TABLES:table1,table2。
- 当 TYPE 为 VIEWS 时，只导入指定的视图，使用 VIEWS:INFO 格式。例如：INCLUDE= VIEWS:view1,view2。
- 当 TYPE 为 PROCEDURE 时，只导入指定的存储过程和存储函数。
- 当 TYPE 为 PACKAGE 时，只导入指定的包。
- 当 TYPE 为 SEQUENCE 时，只导入指定的序列。

例 设置 INCLUDE=(CONSTRAINTS)，将当前用户下的 table1、table2 的对象信息导入时只导入约束。

```
./dimp SYSDBA/Dmsys_123 FILE=/mnt/data/db_str.dmp LOG=db_str.log TABLES=table1,table2  INCLUDE=\(CONSTRAINTS\) DIRECTORY=/mnt/data/dimp
```

#### 3.3.2.10 GRANTS、CONSTRAINTS、INDEXES、TRIGGERS、ROWS

这些参数用来指定某类对象是否被导入。类别分别为约束、权限、索引、触发器和数据。

**语法如下：**

```
GRANTS=Y/N
CONSTRAINTS=Y/N
INDEXES=Y/N
TRIGGERS=Y/N
ROWS=Y/N
```

GRANTS：设置是否导入权限，可选参数。取值范围：Y/N。Y：导入权限，缺省值；N：不导入权限。

CONSTRAINTS：设置是否导入约束，可选参数。取值范围：Y/N。Y：导入约束，缺省值；N：不导入约束。主键和非空约束不受该参数限制，始终会导入。

INDEXES：设置是否导入索引，可选参数。取值范围：Y/N。Y：导入索引，缺省值；N：不导入索引。

TRIGGERS：设置是否导入触发器，可选参数。取值范围：Y/N。Y：导入触发器，缺省值；N：不导入触发器。

ROWS：设置是否导入数据，可选参数。取值范围：Y/N。Y：导入数据，缺省值；N：不导入数据。

例 设置 ROWS=N 不导入表中的数据。

```
./dimp USERID=SYSDBA/Dmsys_123 FILE=/mnt/data/dexp/db_str.dmp NOLOGFILE=Y FULL=Y DIRECTORY=/mnt/data/dimp ROWS=N
```

> **注意**
> 
> **此处，对象（CONSTRAINTS、GRANTS、INDEXES、TRIGGERS、ROWS）分别单独设置为N和EXCLUDE批量设置功能一样，设置一个即可。  
> 对象（CONSTRAINTS、GRANTS、INDEXES、TRIGGERS、ROWS）分别单独设置为Y和INCLUDE批量设置功能略有区别，设置INCLUDE时只导入指定了的对象；单独设置CONSTRAINTS、GRANTS、INDEXES、TRIGGERS、ROWS仅用于控制是否导入该对象。  
> 如果单独设置和批量设置同时出现时，那么以最后出现的那个为准。**

#### 3.3.2.11 NOLOGFILE

NOLOGFILE 用于设置是否使用日志文件。可选参数。

**语法如下：**

```
NOLOGFILE=Y/N
```

Y：不使用日志文件。此时即使存在 LOG 参数，LOG 参数也为无效。

N：使用日志文件，缺省值。

例 设置 NOLOGFILE=Y，不使用日志文件。

```
./dimp USERID=SYSDBA/Dmsys_123 FILE=/mnt/data/dexp/db_str.dmp NOLOGFILE=Y FULL=Y
```

#### 3.3.2.12 NOLOG

NOLOG 设置屏幕上是否显示日志信息。可选参数。缺省为 N，显示日志信息。

**语法如下：**

```
NOLOG=Y/N
```

Y：不显示。

N：显示，缺省值。

例 设置 NOLOG=Y 屏幕不显示日志信息。

```
./dimp USERID=SYSDBA/Dmsys_123 FILE=/mnt/data/dexp/db_str.dmp LOG=db_str.log NOLOG=Y FULL=Y DIRECTORY=/mnt/data/dimp
```

#### 3.3.2.13 LOG\_WRITE

LOG\_WRITE 用于日志信息实时写入日志文件。可选参数。

**语法如下：**

```
LOG_WRITE=Y/N
```

Y：一边将日志内容打印到屏幕上，一边将日志内容写入日志文件。

N：日志内容先在屏幕上全部打印完毕再写入日志文件，缺省值。

#### 3.3.2.14 DUMMY

DUMMY 用于设置交互信息处理。可选参数，缺省使用 P 打印交互信息。在使用 dimpdp 的时候，此参数无需设置，不提供交互信息，全部按 YES 处理。

**语法如下：**

```
DUMMY=P/Y/N
```

P：打印交互信息，默认方式。

Y：不打印交互信息，所有交互都按 YES 处理。

N：不打印交互信息，所有交互都按 NO 处理。

#### 3.3.2.15 PARFILE

PARFILE 用于将常用的参数设置保存到文件中，然后使用参数文件 PARFILE 进行导出、导入操作。可选参数。长度不超过 256 个字符。在使用 dimpdp 的时候，该文件须放在服务器端。

**语法如下：**

```
PARFILE=<path>
```

\<path>：PARFILE 文件的绝对路径。

例 在 dimp 中使用 PARFILE，设置路径 PARFILE=/mnt/data/dimp/para.txt。

```
./dimp USERID=SYSDBA/Dmsys_123 PARFILE=/mnt/data/dimp/para.txt
```

其中，参数文件/mnt/data/dimp/para.txt 的内容如下：

```
FILE=/mnt/data/dexp/db_str.dmp

LOG=db_str.log

TABLES=table1

DIRECTORY=/mnt/data/dimp
```

#### 3.3.2.16 FEEDBACK

FEEDBACK 用来指明在导入数据的过程中每间隔多少行打印一次进度信息。可选参数。实际间隔打印行数与参数 COMMIT\_ROWS 值和导出文件中实际数据存储格式有关。

当参数缺省时，缺省值为 0，只打印导入表的总行数。

**语法如下：**

```
FEEDBACK=<num>
```

\<num>：表间隔的行数。大于等于 0 的整数。缺省为 0，只打印导入表的总行数。

例 将文件 dexp.dmp 中的对象和数据导入到数据库时，要求在导入的过程中每隔 100 行打印一次进度信息。

```
./dimp SYSDBA/Dmsys_123 FULL=Y FILE=/mnt/data/dexp/dexp.dmp LOG=db_str.log
DIRECTORY=/mnt/data/dimp FEEDBACK=100
```

#### 3.3.2.17 COMPILE

如果导入时包含过程/函数、视图、物化视图、触发器、类和包，那么导入时会执行一个编译语句（alter...compile）。COMPILE 用于设置是否在导入时，对过程或函数执行编译。

编译相当于执行重建操作，用于检查过程或函数是否还有效。编译操作仅仅用于防止由于导入顺序导致的对象处于失效状态， 编译失败不影响导入结果。

不编译就不检查有效性，直接导入。

**语法如下：**

```
COMPILE=N/Y
```

Y：执行，缺省值。

N：不执行。

例 导入的过程中含有函数 FUN\_01，那么导入时会自动执行如下语句：

```
alter function "SYSDBA"."FUN_01" compile;
```

如果不想编译，需要设置 COMPILE=N。

#### 3.3.2.18 INDEXFILE

用于将表的索引/约束创建信息写入指定的文件。指定该参数时，索引不执行导入，仅将创建信息和属性信息写入指定的文件。长度不超过 256 个字符，绝对路径不超过 256 个字符。

**语法如下：**

```
INDEXFILE=<文件>
```

例 设置 INDEXFILE=/mnt/data/dimp/dimp.txt。

```
./dimp USERID=SYSDBA/Dmsys_123 FILE=/mnt/data/dexp/db_str.dmp LOG=db_str.log FULL=Y
INDEXFILE=/mnt/data/dimp/dimp.txt
```

#### 3.3.2.19 INDEXFIRST

INDEXFIRST 用于设置导入时是否先建索引。可选参数。

创建索引的过程是先遍历数据再创建索引树。数据量比较大时，应该选择 INDEXFIRST=Y，先创建索引再导入数据，这样就避免创建索引之前遍历大量数据而耗费时间；数据量小时，可任意选择。

**语法如下：**

```
INDEXFIRST=Y/N
```

Y：是。

N：否，缺省值。

#### 3.3.2.20 REMAP\_SCHEMA

将源模式中的数据导入到目标模式中。可选参数。

跨用户导入数据时，必须指定 REMAP\_SCHEMA 参数，若需要跨用户导入多个模式中的数据，则针对每个源模式均需指定模式映射关系，多个模式映射关系之间使用逗号分隔。

**语法如下：**

```
REMAP_SCHEMA=<模式映射关系>{,<模式映射关系>}
<模式映射关系>::=<source_schema>:<target_schema>
```

<source\_schema>：源模式。如果指定的源模式不存在，则导入到对象原来所在的模式。

<target\_schema>：目标模式。如果目标模式不存在，系统会先创建目标模式，再继续导入。

例 将 SYSDBA 模式中的数据导入到 PERSON 模式中。

```
./dimp SYSDBA/Dmsys_123 FILE=/mnt/data/dexp/imp_exp.dmp DIRECTORY=/mnt/data/dimp
FULL=Y REMAP_SCHEMA=SYSDBA:PERSON
```

#### 3.3.2.21 ENCRYPT\_PASSWORD、ENCRYPT\_NAME

如果数据文件是通过加密后得到的，在数据文件导入到数据库时，需要提供加密密钥和加密算法。同时，在 1 个小时内密码只有 10 次错误机会。

**语法如下：**

```
ENCRYPT_PASSWORD=<加密密钥>

ENCRYPT_NAME=<加密算法>
```

<加密密钥>：与导出文件的加密密钥相同。

<加密算法>：与导出文件的加密算法相同。导出加密算法缺省的情况下，此处加密算法可不写；导出文件中记录了加密算法的情况下，此处加密算法可不写。

例 将 2.3.2.17 ENCRYPT、ENCRYPT\_PASSWORD、ENCRYPT\_NAME 中导出的数据再导入进来。

```
./dimp SYSDBA/Dmsys_123 FILE=/mnt/data/dexp/dk15.dmp LOG=db_str19.log
FULL=Y DIRECTORY=/mnt/data/dimp ENCRYPT_PASSWORD=abc123_DBA ENCRYPT_NAME=DES_CBC
```

#### 3.3.2.22 SHOW/DESCRIBE

SHOW/DESCRIBE 用于设置是否打印待导入的数据文件的内容信息列表，当设置 SHOW/DESCRIBE=Y 时，仅展示待导入的数据文件的内容信息列表，实际不执行导入操作。可选参数。

**语法如下：**

```
SHOW=Y/N 
或
DESCRIBE=Y/N
```

Y：是。

N：否，缺省值。

例 想查看/mnt/data/dexp 中待导入的 db\_str.dmp 文件的内容信息列表。

```
./dimp USERID=SYSDBA/Dmsys_123 FILE=/mnt/data/dexp/db_str.dmp SHOW=Y
```

打印结果如下：

```
--------------------------------导入文件列表信息--------------------------------
共包含1个文件，文件如下：
./dimp USERID=SYSDBA/Dmsys_123 FILE=/mnt/data/dexp/db_str.dmp SHOW=Y

导入文件为 FULL 方式导出，共包含以下 7 个模式
模式SYSDBA  含有 2 个表
TT1, 0行
TT2, 0行
模式RESOURCES  含有 4 个表
DEPARTMENT, 5行
EMPLOYEE, 8行
EMPLOYEE_ADDRESS, 8行
EMPLOYEE_DEPARTMENT, 7行
模式PERSON  含有 4 个表
ADDRESS, 16行
ADDRESS_TYPE, 4行
PERSON, 17行
PERSON_TYPE, 4行
模式SALES  含有 5 个表
CUSTOMER, 6行
CUSTOMER_ADDRESS, 12行
SALESPERSON, 2行
SALESORDER_HEADER, 2行
SALESORDER_DETAIL, 4行
模式PRODUCTION  含有 7 个表
PRODUCT_CATEGORY, 7行
PRODUCT_SUBCATEGORY, 40行
PRODUCT, 10行
LOCATION, 38行
PRODUCT_INVENTORY, 8行
PRODUCT_REVIEW, 20行
PRODUCT_VENDOR, 8行
模式PURCHASING  含有 5 个表
VENDOR, 12行
VENDOR_ADDRESS, 24行
VENDOR_PERSON, 12行
PURCHASEORDER_HEADER, 1行
PURCHASEORDER_DETAIL, 0行
模式OTHER  含有 10 个表
DEPARTMENT, 9行
EMPSALARY, 14行
ACCOUNT, 5行
ACTIONS, 7行
READER, 3行
READERAUDIT, 0行
DEPTTAB, 0行
EMPTAB, 0行
SALGRADE, 0行
COMPANYHOLIDAYS, 0行

文件中对象统计信息如下：
INDEX：1个
TRIGGER：3个
PROCEDURE：2个
VIEW：2个
SEQUENCE：2个
USER：1个
SYS_PRIV：1个
SCHEMA_GRANT：4个
PACKAGE：3个
TABLEV_GRANT：1个
PKG_BODY：1个
SYSPACKAGES_DEF：1个
TABLE_CONS_UNIQUE：1个
SR_PRIV：3个
```

#### 3.3.2.23 TASK\_THREAD\_NUMBER

TASK\_THREAD\_NUMBER 用于设置 dmfldr 处理用户数据的线程数目。可选参数。

**语法如下：**

```
TASK_THREAD_NUMBER=<num>
```

\<num>：线程数。取值范围：1~128，缺省为 CPU 个数。但当 CPU 个数大于 128 时，默认值都被置为 128。

#### 3.3.2.24 BUFFER\_NODE\_SIZE

BUFFER\_NODE\_SIZE 用于设置 dmfldr 指定读取文件缓冲区页大小。可选参数，缺省为 10。

值越大，缓冲区的页数越多，每次可以读取的数据就越多，每次发送到服务器的数据也就越多，效率越高。但其大小受 dmfldr 客户端内存大小限制。

**语法如下：**

```
BUFFER_NODE_SIZE=<size_num>
```

<size\_num>：缓冲区页数。整数类型，取值范围：1~2048，缺省为 10。单位为 M。

#### 3.3.2.25 TASK\_SEND\_NODE\_NUMBER

TASK\_SEND\_NODE\_NUMBER 用于设置 dmfldr 发送节点个数。可选参数。

**语法如下：**

```
TASK_SEND_NODE_NUMBER=<num>
```

\<num>：节点个数。整数类型，取值范围：16~65535。在系统内存够的情况下可以适当的设大数值以提升效率。缺省情况下，由程序自动计算。

#### 3.3.2.26 LOB\_NOT\_FAST\_LOAD

LOB\_NOT\_FAST\_LOAD 用于设置当表中含有大字段时不使用 dmfldr，而使用普通的 INSERT 进行插入，根据 COMMIT\_ROWS 参数决定提交的行数。因为当表中有大字段的时候，dmfldr 是一行一行提交表数据。

**语法如下：**

```
LOB_NOT_FAST_LOAD=Y/N
```

Y：表中含有大字段时不使用 dmfldr。

N：表中含有大字段时使用 dmfldr，缺省值。

#### 3.3.2.27 PRIMARY\_CONFLICT

PRIMARY\_CONFLICT 用于设置主键冲突的处理方式。可选参数，不设置此参数时主键冲突报错，设置时不报错，可指定对主键冲突的数据进行不同的处理。

**语法如下：**

```
PRIMARY_CONFLICT=[IGNORE|OVERWRITE|OVERWRITE2]
```

IGNORE：不覆盖主键冲突行数据。

OVERWRITE：覆盖主键冲突行数据，删除原表有冲突的行。

OVERWRITE2：覆盖主键冲突行数据，更新原表有冲突的行。

#### 3.3.2.28 TABLE\_FIRST

TABLE\_FIRST 用于控制是否强制先导入表对象。可选参数，缺省为 N。

**语法如下：**

```
TABLE_FIRST=Y/N
```

N：正常导入，缺省值。顺序为：1.没有依赖的对象（除了表之外的数据库对象）；2.有依赖的 class；3.表；4.依赖对象。

Y：强制先导入表。顺序为：1.表；2.没有依赖的对象（除了表之外的数据库对象）；3.有依赖的 class；4.依赖对象。

#### 3.3.2.29 SHOW\_SERVER\_INFO

SHOW\_SERVER\_INFO 用于控制是否显示服务器信息。可选参数，缺省为 N。

**语法如下：**

```
SHOW_SERVER_INFO=Y/N
```

N：不显示导出文件对应服务器信息，正常导入，缺省值。

Y：显示导出文件对应服务器信息，实际不导入。

#### 3.3.2.30 IGNORE\_INIT\_PARA

IGNORE\_INIT\_PARA 用于指定源库和目标库之间忽略差异的建库参数。取值范围：0、1、2 和 3。缺省为 0。

若不忽略建库参数 CASE\_SENSITIVE 的差异，导入时大小写是否敏感以目标库的 CASE\_SENSITIVE 参数为准。

0：不忽略；

1：忽略 CASE\_SENSITIVE 参数差异；

2：忽略 LENGTH\_IN\_CHAR 参数差异；

3：忽略 CASE\_SENSITIVE、LENGTH\_IN\_CHAR 参数差异可选参数。

**语法如下：**

```
IGNORE_INIT_PARA=<num>
```

\<num>：需要忽略的建库参数代号。取值范围：0、1、2 和 3，缺省为 0。

#### 3.3.2.31 AUTO\_FREE\_KEY

如果数据文件是通过工作模式为 WORK\_MODE\_KID 的加密算法加密后得到的，则可通过 AUTO\_FREE\_KEY 指定在数据导入完成后是否释放加密文件使用的密钥，密钥释放后该数据文件将无法使用。关于工作模式的详细介绍可参考《DM8 安全管理》。

**语法如下：**

```
AUTO_FREE_KEY=Y/N
```

Y：是。

N：否，缺省值。

#### 3.3.2.32 REMAP\_TABLE

将源表/视图中的数据导入到目的表/视图中。可选参数。

**语法如下：**

```
[<SOURCE_SCHEMA>.]<SOURCE_TABLE>:<TARGET_TABLE>
```

<SOURCE\_SCHEMA>：源表/视图所属的模式。如果缺省则代表所有模式下的 <SOURCE\_TABLE> 都是源表/视图。目的表/视图存在则报错。

<SOURCE\_TABLE>：源表/视图。

<TARGET\_TABLE>：目的表/视图。

例 将源表 T1 中的数据导入到目的表 T2 中。

```
./dimp SYSDBA/Dmsys_123 FILE=/mnt/data/dexp/imp_exp.dmp DIRECTORY=/mnt/data/dimp FULL=Y REMAP_TABLE=T1:T2
```

#### 3.3.2.33 REMAP\_TABLESPACE

将源表空间中的数据导入到目的表空间中。使用该参数的前提是导出文件中包含源表表空间。可选参数。

**语法如下：**

```
<SOURCE_TABLESPACE>:<TARGET_TABLESPACE>
```

<SOURCE\_TABLESPACE>：源表空间。

<TARGET\_TABLESPACE>：目的表空间，如果目的表空间不存在，需要用户提前创建。

例 将 MAIN 表空间中的数据导入到 TS 表空间。

```
./dimp SYSDBA/Dmsys_123 FILE=/mnt/data/dexp/imp_exp.dmp DIRECTORY=/mnt/data/dimp FULL=Y REMAP_TABLESPACE=MAIN:TS
```

#### 3.3.2.34 SIMPLE\_LOG

SIMPLE\_LOG 用于设置导入日志是否只打印简要日志，简要日志只打印导入对象个数和导入表数据行数。可选参数。

**语法如下：**

```
SIMPLE_LOG=N/Y
```

N：导入日志不使用简要日志，缺省值。

Y：导入日志使用简要日志。

#### 3.3.2.35 DATA\_ONLY

DATA\_ONLY 用于控制是否只导入表数据。可选参数。

**语法如下：**

```
DATA_ONLY=N/Y
```

N：对象定义和数据都导入，缺省值。

Y：只导入表数据。

需要注意的是，如果指定 DATA\_ONLY=Y,同时指定了其余参数不导入表数据(如 ROWS=Y，INCLUDE=INDEXES，EXCLUDE=ROWS 等)，会报错参数不兼容。

#### 3.3.2.36 INDEX\_OPTION

使用快速装载时索引的设置选项，整型数值。取值范围：1、2 和 3，缺省为 2。可选参数。

1：服务器装载数据时先不刷新二级索引，而是将新数据按照索引预先排序，在装载完成后，再将排好序的数据插入索引；

2：服务器在快速装载过程中不刷新二级索引数据，只在装载完成时，重建所有二级索引；

3：代表服务器使用追加模式来进行二级索引的插入，在数据装载的过程中，同时进行二级索引的插入。若未禁用全局索引，则在非 DPC 环境下，全局索引可通过设置 INDEX\_OPTION 为 3 进行插入。

**语法如下：**

```
INDEX_OPTION=<num>
```

\<num>：索引设置选项。取值范围：1、2 和 3，缺省为 2。

#### 3.3.2.37 CTRL\_INFO

CTRL\_INFO 控制信息，用来控制一些特殊情况导入。可选参数，缺省为 2。

**语法如下：**

```
CTRL_INFO=[n]
```

n 取值为整型数值。如果要控制多种情况，可设置为多种值相加。

0：不导入表空间定义。

1：导入表空间定义。

2：先校验导入文件的 MD5 值再执行导入。只有 MD5 值校验成功的文件才能导入成功。dexp 执行导出时会为导出文件生成一个 MD5 值，记录在导出文件中，用于标识文件的完整性。dimp 导入时使用同样的方法再次为该文件生成一个 MD5 值。通过比较，如果前后两个 MD5 值一致，说明该文件完好无损；如果 MD5 值不一致，则说明文件已损坏。

4：校验导入文件的 MD5 值。此处不会执行导入，只是用于校验文件的完整性。

8：导入对象时忽略 OR REPLACE 条件。其中对象包括：视图、同义词、触发器、类、域、过程、函数、索引、包、目录、上下文、DBLINK。

16：将源模式中的数据导入到目标模式时，使用指定的 remap\_schema 参数替换列定义默认值序列的模式名。

32：当 remap\_schema 参数中设置的源模式不存在时报错，并直接终止导入。

64：控制每张表在数据导入完成后提交一次，保证表级原子性。

128：控制导入索引定义时忽略聚集索引记录地址功能。

#### 3.3.2.38 CONFIG\_FILE

CONFIG\_FILE 用于指定局部配置文件路径，局部配置文件中可以配置导入导出默认连接串和默认密码。可选参数。长度不超过 256 个字符。

**语法如下：**

```
CONFIG_FILE=<path>
```

\<path>：局部配置文件路径。

例 设置 CONFIG\_FILE=/mnt/data/dexp/local\_config.txt。

```
./dimp CONFIG_FILE=/mnt/data/dexp/local_config.txt FILE=test.dmp
```

其中，局部配置文件 local\_config.txt 中的内容如下：

```
DUMP_CONN_STR=(SYSDBA/Dmsys_123@LOCALHOST:5236)

DUMP_PASSWORD=(Dmsys_123)
```

局部配置文件目前仅支持以下两个配置项：

DUMP\_CONN\_STR：指定导入导出默认连接串。没有指定 USERID 连接串时，使用该连接串。

DUMP\_PASSWORD：指定导入导出默认连接密码。

全局配置文件 dm\_svc.conf 中也支持配置 DUMP\_CONN\_STR 和 DUMP\_PASSWORD，局部配置文件的优先级高于全局配置文件 dm\_svc.conf。

#### 3.3.2.39 FILE\_VERSION

FILE\_VERSION 用来指定将 dmp 文件降级后的新 dmp 文件的逻辑版本，不执行导入操作，可以通过帮助信息查看取值范围。可选参数。

**语法如下：**

```
FILE_VERSION = <num>
```

\<num>：将 dmp 文件降级成后的新 dmp 文件的逻辑版本，为取值范围内的正整数。

注：使用 dimp 进行文件降级操作，指定的降级文件版本需小于 dmp 文件当前的版本。

例 将逻辑版本为 15 的 dmp 文件 dexp.dmp 降级生成逻辑版本为 14 的 dmp 文件 dexp\_ver14.dmp。

```
./dimp SYSDBA/Dmsys_123 FILE=dexp.dmp DIRECTORY=/mnt/data/dexp FILE_VERSION=14
```

#### 3.3.2.40 HELP

输入 dimp HELP 即可查看帮助信息。

**语法如下：**

```
HELP
```

例 使用 HELP 查看帮助信息。

```
./dimp HELP
```

HELP 信息会显示 dimp 版本信息以及所有参数的大致信息，供用户快速参考。