---
title: "5.数据安全性"
book: "HGDB 安全管理手册"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/develop/data_safty.html"
tags:
  - highgo
  - highgo-v45
  - develop-security-management
---

## 5\. 数据安全性

瀚高数据库提供多种数据加密手段及数据编辑（动态数据脱敏）技术，确保用户数据在存储、访问、备份、传输等方面的安全性。

## 5.1. 通信加密

瀚高数据库提供对使用 SSL 连接加密客户端/服务器通讯的本地支持，它可以增强传输链路的安全性。

### 5.1.1. 通信加密介绍

开启瀚高数据库通信加密，需要将参数文件postgresql.conf中的ssl设置为on，让瀚高数据库以支持ssl加密连接的方式启动。服务端在同一个 TCP 端口同时监听普通连接和SSL连接，并且将与任何正在连接的客户端协商是否使用SSL。默认情况下，客户端采用SSL加密连接。

要以SSL模式启动数据库服务，那么服务器证书和私钥的文件必须存在。默认情况下，这些文件应该分别被命名为server.crt和server.key并且被放在服务器的数据目录data中，但是可以通过配置参数ssl\_cert\_file和ssl\_key\_file指定其他名称和位置。

在 Unix 系统上，server.key上的权限必须设置为禁止其他用户或组的任何访问，通过命令chmod 0600 server.key来完成。或者，该文件可以由root 所拥有并且具有数据库组的读访问权限（也就是0640权限）。这种设置适用于由操作系统管理证书和密钥文件的安装。用于运行瀚高数据库服务的系统用户应该被作为能够访问那些证书和密钥文件的组成员。

默认情况下数据目录为600权限，如果数据目录允许组读取访问，也就是640权限，则证书文件需要配置在数据目录data之外，以符合上面概述的安全要求。通常，为data目录启用组访问权限是为了允许非特权用户备份数据库，在这种情况下，备份软件将无法读取证书文件，并且可能会出错。

### 5.1.2. SSL服务器文件用法

表5.1总结了与服务器上 SSL 配置有关的文件（显示的文件名是默认的名称。本地配置的名称可能会不同）。

表 5.1 服务器文件用法

| **文件** | **内容** | **效果** |
| --- | --- | --- |
| ssl\_cert\_file ($PGDATA/server.crt) | 服务器证书 | 发送给客户端来说明服务器的身份 |
| ssl\_key\_file($PGDATA/server.key) | 服务器私钥 | 证明服务器证书是其所有者发送的，并不说明证书所有者是值得信任的 |
| ssl\_ca\_file | 可信的证书颁发机构 | 检查客户端证书是由一个可信的证书颁发机构签名的 |
| ssl\_crl\_file | 被证书授权机构撤销的证书 | 客户端证书不能出现在这个列表上 |

服务器在服务器启动时以及服务器配置重新加载时读取这些文件。在linux系统上，只要为新客户端连接生成新的后端进程，它们也会重新读取。

如果在服务器启动时检测到这些文件中的错误，服务器将拒绝启动。但是，如果在配置重新加载过程中检测到错误，则会忽略这些文件，并继续使用旧的SSL配置。在linux系统上，如果在后端启动时检测到这些文件中存在错误，则该后端将无法建立SSL连接。以上情况，错误信息都会在服务器日志中报告。

### 5.1.3. 创建证书

为数据库创建证书并应用到数据库参数的方法非常简单。

瀚高数据库提供了一个脚本用来完成上述工作。该脚本位于数据库安装目录下的bin目录中，名称为hg\_sslkeygen.sh。例如：

```bash
$ which hg_sslkeygen.sh
/opt/HighGo4.5.7-see/bin/hg_sslkeygen.sh
```

使用方法页非常简单，直接在脚本后跟上数据库data目录即可。

```bash
$ hg_sslkeygen.sh /opt/HighGo4.5.7-see/data
Setting the ssl configuration to /opt/HighGo4.5.7-see/data
Generating RSA private key, 2048 bit long modulus
............................................................................+++
........+++
e is 65537 (0x10001)
```

这样，server.crt、server.key、root.crt就被放置到data目录下，并修改权限为600。且相关数据库参数也已被自动修改。

```bash
$ ls -l|grep 'crt\|key'                   
-rw------- 1 root root  1338 May 31 01:09 root.crt
-rw------- 1 root root  1338 May 31 01:09 server.crt
-rw------- 1 root root  1675 May 31 01:09 server.key
$ cat postgresql.conf |grep ssl_|grep file
ssl_ca_file = 'root.crt'
ssl_cert_file = 'server.crt'
#ssl_crl_file = ''
ssl_key_file = 'server.key'
#ssl_dh_params_file = ''
```

## 5.2. FDE

FDE（Full Database Encryption）是一种全数据库加密手段，即对数据库保存在持久化介质（比如磁盘，CD等）中的数据进行全数据库的加密操作。该方式对用户完全透明。其原理即在缓冲层和持久化层之间进行加密，对缓冲层的数据以数据库PAGE页作为基础，加密后写入介质，读数据反之。优点在于使保存在介质中的数据更加安全，如有恶意操作员进行数据介质的窃取行为，在进行介质中的数据恢复时，也不能通过数据重新导入的方式，进行数据恢复处理，这样保护了数据的安全性。但数据加密也会导致数据写入和读取的速率变慢，需要在数据库安全和数据库性能之间进行权衡。

### 5.2.1. 使用方法

1.企业版

数据库初始化时，根据用户输入的信息生成秘钥并加密，通过加密通信与LDAP服务器交互，把算法和加密后的秘钥存储到LDAP服务器中。

数据库启动时，通过加密通信从LDAP服务器上取得秘钥并通过pg\_contrl文件校验秘钥，在读写物理文件时，使用秘钥对数据进行加解密。

数据库加密只能在初始化的时候启动。启动加密时需要指定以下的参数：

通过initdb的参数–data-encryption(-K) 指定需要的模块；（必须指定）

通过–key-url(-P)指定存储秘钥的LDAP服务器的url; （必须指定）

通过 –encryption-algo(-C)指定加密算法；（必须指定）

（可选的选项：aes-128、aes-192、aes-256、blowfish、des、3des、cast5）

通过–new-key(-e)指定是否使用新的秘钥; （可选，当使用–new-key参数时，表示需要指定新的秘钥，否则，使用LDAP中既存的秘钥。）

例子如下：

initdb –data-encryption pgcrypto –key-url ldaps://192.168.10.40:636?cn=hgdb,dc= highgo,dc=com?123 -C blowfish –new-key -D../data

初始化命令示例：

```bash
initdb --data-encryption pgcrypto  --key-url  ldaps://192.168.10.40:636?cn=hgdb,dc= highgo,dc=com?123  -C  blowfish --new-key   -D /opt/highgo/hgdb-see-4.5.8/data
initdb -D data -e sm4 -c "echo 12345678"
```

2.安全版

在使用initdb命令进行数据初始化时，指定加密参数可启用FDE功能。数据库初始化完成以后，数据库会默认对写入介质中的数据进行加密。

初始化命令示例：

```bash
initdb -D /opt/highgo/hgdb-see-4.5.8/data -e sm4 -c "echo 12345678"
```

其中，-c或–cluster-passphrase-command=COMMAND，使用该选项指定一个指令，COMMAND指的是标准的linux命令，比如“echo 12345678”这样的指令。该指令会在进行密钥封装时执行，成为密钥加密的一部分。

\-e或–enc-cipher该选项指定数据加密算法，目前支持的算法有aes-128、aes-192、aes-256、sm4、blowfish、des、3des、cast5，默认为sm4，可以通过国密算法sm4对数据进行加密处理。

### 5.2.2. 加密文件

FDE会对下表中的文件进行加密。

表 5.2 加密文件列表

| **编号** | **数据库文件** | **文件类型** |
| --- | --- | --- |
| 1 | base/xxxx/xxxx | 数据文件 |
| 2 | base/xxxx/xxxx\_vm | vm文件 |
| 3 | base/xxxx/xxxx\_fsm | fsm文件 |
| 4 | base/xxxx/xxxx\_init | init文件 |
| 5 | pg\_wal/xxxx | wal日志 |
| 6 | pg\_xact/xxxx | 事物状态日志 |
| 7 | pg\_subtrans/xxxx | 子事务日志 |
| 8 | pg\_commit\_ts/xxxx | 事务提交日志 |
| 9 | pg\_multixact/xxxx | 组合事务日志 |
| 10 | pg\_notify/xxxx | LISTEN/NOTIFY状态数据 |

## 5.3. 新一代加密技术

仅安全版提供该功能。

在对安全性要求比较严格，或者数据库管理员不受信任的环境中（如数据库托管维护服务，云数据库等场景）可以使用增强数据透明加密功能来防止数据的泄露。此功能可以使数据库中存取的数据始终为密文，并且支持密文做等值比较等一些数据操作。

### 5.3.1. 新一代加密技术环境搭建

使用增强数据透明加密功能需要两台服务器，一台为加密机，一台为数据库服务器。使用过程中，数据会先经过加密机处理再进入数据库服务器，取出数据亦然。而若不经过加密机直接操作数据库服务器则看到数据均为密文。

在数据库服务器中，正常安装数据库，并且允许加密机连接即可。

在加密机中，我们需要安装crypt\_fdw插件，在postgresql.conf配置文件中的shared\_preload\_libraries参数中增加“crypt\_fdw”然后重启。

连接到加密机中的数据库并执行以下步骤：

1. 执行CREATE EXTENSION crypt\_fdw; 命令，创建扩展。
2. 执行CREATE SERVER \[自定义一个数据服务器名\] FOREIGN DATA WRAPPER crypt\_fdw OPTIONS (host ‘\[数据服务器主机名\]’, port ‘\[数据服务器端口\]’, dbname ‘\[数据服务器的数据库名\]’, use\_remote\_estimate ‘true’); 创建外部服务器。
3. 执行CREATE USER MAPPING FOR \[加密机数据库用户名\] SERVER \[上一步中自定义的数据服务器名\] OPTIONS(user ‘\[数据服务器的数据库用户名\]’, password ‘\[数据服务器的数据库用户密码\]’);

### 5.3.2. 数据库表的创建

在数据服务器中正常创建数据表。

在加密机数据库中执行以下操作：

1. 执行IMPORT FOREIGN SCHEMA \[数据服务器中数据库模式名\] FROM SERVER \[自定义的数据服务器名\] INTO \[加密机数据库模式名\];导入数据库表结构。
2. 执行SELECT encrypt\_column函数加密指定表的指定列。此函数包含四个参数，分别为：  
	a) 表名 text：要加密的表，格式为\[模式名.\]表名，模式名可省略。  
	b) 列名 text：要加密的列，若要指定多个列，用逗号隔开。  
	c) 算法 text：对加密列使用的加密算法，若要使用多个算法，用逗号隔开。  
	d) 层级 text：加密列加密的层级，可以省略，默认为column级别。
3. 可以使用\\d \[表名\]查看列的加密相关信息
	### 5.3.3. 数据的增删改查操作

在数据服务器中执行查询看到的已加密列均为密文，且在增删改查过程中密文始终不会在数据服务器中进行解密。

在加密机数据库中正常执行增删改查操作即可。

| **提示：** |
| --- |
| 使用了增强数据透明加密功能功能后，所有的数据传输会经过加密机加密解密，因此效率会受到一定的影响，所以在进行配置时，应当适当选择要加密的列。并且当前版本中密文支持的操作类型有限，不支持的操作类型会将数据全部在加密机中解密然后操作，此操作会比较耗时。 |

### 5.3.4. 调整加密层级

加密了列后默认的层级为column，此层级允许列自身排序以及和常量值的比较，但是不支持不同列之间的比较，因此不可以支持join操作。若需要支持不同列的比较，需要调整加密列的加密层级。

1. 执行SELECT adjust\_column函数调整指定列的加密层级。此函数包含三个参数，分别为：
	1. 表名：要调整的表，格式为\[模式名.\]表名，模式名可以省略。
		2. 列名：要调整的列， 若要指定多个列，用逗号隔开。
		3. 层级：调整的目标层级，可选择的层级有“database”，“schema”和“column”。
2. 可以使用\\d \[表名\]查看修改后的列加密相关信息

## 5.4. 备份加密

仅安全版提供该功能。

在数据库使用过程中经常用到备份功能。采用通常的备份方式，备份出的数据为明文存储，而在备份文件的传输或者使用过程中，可能会发生丢失备份数据造成数据泄露的情况。为避免此类情况，就需要对备份出的数据进行加密存储。瀚高数据库安全版就提供了备份加密的功能。

### 5.4.1. 限制

- 目前的备份数据只进行异或和口令双重加密，尚未引入对称加密算法。
- 目前使用pg\_dump进行加密备份时，只支持-Fc格式。进行恢复时，只能使用pg\_restore工具进行恢复，需要输入口令，该口令需要与pg\_dump设定的口令一致。
- 为同时解决大数据的备份速度和备份恢复时的解密问题，备份加密使用简单的异或操作进行。

### 5.4.2. 使用方法

使用方式：

进行备份时：使用pg\_dump -Fc -d 数据库名称 -e “口令” > 输出文件名称

进行恢复时：使用pg\_restore -d 数据库名称 -r “口令“ -Fc 输出文件名称

## 5.5. 数据编辑 仅限安全版

仅安全版提供该功能。

数据编辑（Data Redaction）功能是一种动态数据脱敏机制，针对数据查询时的敏感数据进行动态的安全保护，通过设置策略对表的字段进行动态查询时动态修订。

一个完整的数据编辑策略由三部分组成：数据编辑函数、数据编辑策略应用SQL命令、相应的权限配置。

- 使用内置的数据编辑函数；
- 通过绑定策略语句将函数与目标数据关联；
- 数据编辑函数及策略仅可通过SYSSSO用户创建、修改、删除、禁用、启用、授权操作，普通用户和数据库管理员仅可查看管理视图。

在启用数据编辑之前，需打开参数开关：redaction\_policy。可通过命令行或直接修改conf文件进行修改。命令行格式如下：

```sql
alter system set redaction_policy to on;
select pg_reload_conf();
```

### 5.5.1.创建数据编辑策略

语法：

```sql
CREATE REDACTION POLICY <name> ON <table_name>
[ ADD [ COLUMN ] <column_name>[,…] USING <funcname_clause> ]  
[, ...] 
[ FOR ( <expression> ) ] 
DISABLE/ENABLE;
```

解析：

> name：当前策略的名称，
> 
> table\_name：当前数据编辑策略作用为哪张表
> 
> column\_name：策略应用于哪个列
> 
> funcname\_clause：数据编辑函数名称，目前支持的脱敏函数见下文函数列表
> 
> expression：表达式，即对哪些用户执行数据编辑策略。比如user=’u1’，就是对u1用户执行数据编辑策略，其他用户不执行

示例：

> 1）确认参数开启
> 
> highgo=> show redaction\_policy;
> 
> 　redaction\_policy
> 
> \-—————–
> 
> 　on
> 
> (1 row)
> 
> 2）创建测试用户
> 
> create user u1 password ‘Hello@123’;
> 
> create user u2 password ‘Hello@123’;
> 
> create user u3 password ‘Hello@123’;
> 
> 3）在用户u3下创建测试表，并赋予u1和u2用户select权限
> 
> \\c highgo u3
> 
> create table test(id int, col1 varchar,info text);
> 
> insert into test values(1,’abc’,’test’);
> 
> insert into test values(2,’abcabcabc’,’testtesttest’);
> 
> grant select on test to u1,u2;
> 
> 4）使用syssso用户创建数据编辑策略
> 
> \\c highgo syssso
> 
> create redaction policy p1 on test add column col1 using redact\_all for (user = ‘u1’);
> 
> //该策略仅对u1用户生效
> 
> 5）查看数据
> 
> \\c highgo u1
> 
> select \* from test; —-期望查看到col1列为脱敏后数据
> 
> 结果如下：
> 
> 　id | col1 | info
> 
> —-+———–+————–
> 
> 　1 | xxx | test
> 
> 　2 | xxxxxxxxx | testtesttest
> 
> (2 rows)
> 
> \\c highgo u2
> 
> select \* from test; —–期望查看到明文
> 
> 结果如下：
> 
> 　id | col1 | info
> 
> —-+———–+————–
> 
> 　1 | abc | test
> 
> 　2 | abcabcabc | testtesttest
> 
> (2 rows)
> 
> 6） 同时指定多列
> 
> 　由于同一个表只能创建一个数据编辑策略，所以先删掉p1，再创建：
> 
> 　\\c highgo syssso
> 
> drop redaction policy p1;
> 
> 　create redaction policy p2 on test add column id using redact\_bankcard,add column info using redact\_shuffle for (user = ‘u1’);
> 
> 即：对列id使用redact\_bankcard函数，列info使用redact\_shuffle函数。
> 
> 查看数据：
> 
> \\c highgo u1
> 
> select \* from test;
> 
> 结果如下：
> 
> id | col1 | info
> 
> —-+———–+————–
> 
> 　0 | abc | tset
> 
> 　0 | abcabcabc | etststttetse
> 
> (2 rows)
> 
> //redact\_bankcard函数不支持对int类型进行脱敏，所以自动使用redact\_all对int类型进行脱敏，结果为0。
> 
> 7） 创建数据编辑策略，但是不启用
> 
> \\c highgo syssso
> 
> drop redaction policy p2;
> 
> 　create redaction policy p3 on test add column id using redact\_bankcard,add column info using redact\_shuffle for (user = ‘u1’) disable;
> 
> 　查看数据：
> 
> \\c highgo u1
> 
> select \* from test;
> 
> 结果为明文：
> 
> 　id | col1 | info
> 
> —-+———–+————–
> 
> 　1 | abc | test
> 
> 　2 | abcabcabc | testtesttest
> 
> (2 rows)

### 5.5.2. 修改数据编辑策略

目前修改策略可使用以下几种方式：

（1）ALTER REDACTION POLICY policyname MODIFY COLUMN colname USING func\_name;

修改当前策略中，列colname使用的数据编辑函数

（2）ALTER REDACTION POLICY policyname RENAME TO policyname2;

修改当前策略的名字

（3）ALTER REDACTION POLICY policyname DISABLE/ENABLE;

修改当前策略是否启用

（4）ALTER REDACTION POLICY policyname DROP COLUMN colname;

修改当前策略，删除掉其中的某一行数据编辑列

（5）ALTER REDACTION POLICY policyname for (user = ‘username’);

修改当前策略，增加数据编辑表达式

（6）ALTER REDACTION POLICY policyname ADD COLUMN colname USING func\_name

修改当前策略，增加数据编辑列

### 5.5.3. 删除数据编辑策略

DROP REDACTION POLICY policynamelist;

例：

DROP REDACTION POLICY p1;

删除数据编辑策略p1

DROP REDACTION POLICY p1,p2;

删除数据编辑策略p1,p2

### 5.5.4. 限制

- 创建策略只能使用syssso进行设定，其他用户无权限。
- 一张表中只能创建一个策略
- 一个列只能指定一个数据编辑函数

### 5.5.5. 数据编辑函数列表

| **函数名称** | **支持的数据类型** | **描述** |
| --- | --- | --- |
| redact\_bankcard | BPCHAR, VARCHAR, NVARCHAR, TEXT（注：仅针对信用卡格式的文本类数据） | ‘4880-9898-4545-2525’ 将会被脱敏为 ‘xxxx-xxxx-xxxx-2525’，该函数仅对后4位之前的数字进行脱敏。 |
| redact\_emailname | BPCHAR, VARCHAR, NVARCHAR, TEXT (注：仅针对email格式的文本类型数据) | ‘ [abcd@gmail.com](mailto:abcd@gmail.com) ‘ 将会被脱敏为‘ [xxxx@gmail.com](mailto:xxxx@gmail.com) ‘， 对出现第一个‘@’之前的文本进行脱敏 |
| redact\_emailfull | BPCHAR, VARCHAR, NVARCHAR, TEXT (注：仅针对email格式的文本类型数据) | ‘ [abcd@gmail.com](mailto:abcd@gmail.com) ‘ 将会被脱敏为 ‘ [xxxx@xxxxx.com](mailto:xxxx@xxxxx.com) ‘，对出现最后一个’.’之前的文本（除‘@’符外）进行脱敏 |
| redact\_digits | BPCHAR, VARCHAR, NVARCHAR, TEXT (注：仅针对包含数字的文本类型数据) | ‘alex123alex’ 将会被脱敏为 ‘alex000alex’， 仅对文本中的数字进行脱敏。 |
| redact\_shuffle | BPCHAR, VARCHAR, NVARCHAR, TEXT (注：仅针对文本类型数据) | ‘hello word’ 将会被随机打乱顺序脱敏为 ‘hlwoeor dl’， 该函数通过字符乱序排列的方式实现，属于弱脱敏函数，语义较强的字符串不建议使用该函数脱敏。 |
| redact\_random | BPCHAR, VARCHAR, NVARCHAR, TEXT (注：仅针对文本类型数据) | ‘hello word’ 将会被脱敏为 ‘ad5f5ghdf5’，将文本按字符随机脱敏 |
| redact\_all | BOOL, RELTIME, TIME, TIMETZ, INTERVAL, TIMESTAMP, TIMESTAMPTZ, SMALLDATETIME, ABSTIME,TEXT, BPCHAR, VARCHAR, NVARCHAR2, NAME, INT8, INT4, INT2, INT1, NUMRIC, FLOAT4, FLOAT8, CASH | ‘4880-9898-4545-2525’ 将会被脱敏为 ‘xxxxxxxxxxxxxxxxxxx’；   数据类型123将被脱敏为0。 |
| redact\_idcard | BPCHAR, VARCHAR, NVARCHAR, TEXT (注：仅针对身份证格式的文本类型数据) | 对身份证号进行脱敏。130623202101010623’将被脱敏为’130623\*\*\*\*\*\*\*\*0623’，该函数保留身份证号的前六位和后四位，中间的号码用\*代替。 |
| redact\_name | BPCHAR, VARCHAR, NVARCHAR, TEXT (注：仅针对姓名的文本类型数据) | 对姓名进行脱敏。两个字的姓名将第一个字用\*脱敏，三个字及以上的将倒数第二个字用\*脱敏。如“张三”被脱敏为“张\*”，“张三丰”被脱敏为“张\*丰”，“富兰克林”被脱敏为“富兰\*林” |
| redact\_phone | BPCHAR, VARCHAR, NVARCHAR, TEXT (注：仅针对电话号码的文本类型数据) | 对电话号码进行脱敏。适用于手机号和固话号。保留前三位和后四位，对中间数字进行脱敏。如“13534556093”脱敏为“135\*\*\*\*6093” |

### 5.5.6. 数据类型与数据编辑函数的表现

| **数据类型** | **字符类型** | **数字类型** | **日期类型** | **布尔类型** |
| --- | --- | --- | --- | --- |
| redact\_bankcard | 仅对后4位之前的数字进行脱敏 | 均脱敏为一个数字0 | 1）不带时间戳的timestamp和date类型脱敏为：1970-01-01 00:00:00   2）带时间戳的timestamp类型脱敏为：1970-01-01 00:00:00-05   3）不带时间戳的time类型脱敏为：00:00:00   4）带时间戳的time类型脱敏为：00:00:00+00   5）interval类型脱敏为：00:00:00 | 均脱敏为f |
| redact\_emailna me | 仅对后4位之前的数字进行脱敏 |  |  |  |
| redact\_emailfull | 出现最后一个’.’之前的文本（除‘@’符外）进行脱敏 |  |  |  |
| redact\_digits | 对文本中的数字进行脱敏 |  |  |  |
| redact\_shuffle | 该函数通过字符乱序排列的方式实现 |  |  |  |
| redact\_random | 文本按字符随机脱敏 |  |  |  |
| redact\_all | 每个字符均脱敏为x |  |  |  |
| redact\_idcard | 该函数保留身份证号的前六位和后四位，中间的号码用\*代替 |  |  |  |
| redact\_name | 两个字的姓名将第一个字用\*脱敏，三个字及以上的将倒数第二个字用\*脱敏 |  |  |  |
| redact\_phone | 保留前三位和后四位，对中间数字进行脱敏。 |  |  |  |

目前，数据编辑不支持瀚高的特有数据类型，例如： money、bytea、enum、几何类型、网络地址类型、bit、文本搜索类型、uuid、xml、json、数组类型、组合类型、范围类型、域类型、oid、pg\_lsn、伪类型和用户自定义类型等。

数据编辑不支持兼容类型章节中列出的数据类型。