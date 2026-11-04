---
title: "客户端认证"
book: "安全指南"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/safety/safeOne4.html"
tags:
  - highgo
  - highgo-v9
  - safety-security-guide
---

## 客户端认证

客户端认证是数据库服务器建立客户端身份的过程，并且服务器决定客户端应用（或者运行客户端应用的用户）是否被允许以请求的数据库用户名来连接。瀚高数据库提供多种不同的客户端认证方式。被用来认证一个特定客户端连接的方法可以基于（客户端）主机地址、数据库和用户来选择。

## pg\_hba.conf文件

客户端认证是由配置文件pg\_hba.conf控制。在瀚高数据库initdb初始化数据目录时，会安装一个默认的pg\_hba.conf文件。

pg\_hba.conf文件的常用格式是一组记录，每行一条，空白行将被忽略，#注释字符后面的任何文本也被忽略。记录可以延续到下一行并以反斜线结束该行。一条记录由若干用空格和/或制表符分隔的域组成，如果域值用双引号包围，那么它可以包含空白。在数据库、用户或地址域中引用一个关键字（例如all或replication）将使该词失去其特殊含义，并且只是匹配一个有该名字的数据库、用户或主机。

每条记录指定一种连接类型、一个客户端IP地址范围（如果和连接类型相关）、一个数据库名、一个用户名以及对匹配这些参数的连接使用的认证方法。第一条匹配连接类型、客户端地址、连接请求的数据库和用户名的记录将被用于执行认证。这个过程没有”落空”或者”后备”的说法：如果选择了一条记录而且认证失败，那么将不再考虑后面的记录。如果没有匹配到合适的记录，那么访问将被拒绝。

记录可以有多种格式：

```
local database user auth-method [auth-options]

Host database user address auth-method [auth-options]

hostssl database user address auth-method [auth-options]

hostnossl database user address auth-method [auth-options]

hostgssenc database user address auth-method [auth-options]

hostnogssenc database user address auth-method [auth-options]

host database user IP-address IP-mask auth-method [auth-options]

hostssl database user IP-address IP-mask auth-method [auth-options]

hostnossl database user IP-address IP-mask auth-method [auth-options]

hostgssenc database user IP-address IP-mask auth-method [auth-options]

hostnogssenc database user IP-address IP-mask auth-method
[auth-options]
```

各个域的含义如下：

local

这条记录匹配使用Unix域套接字的连接。如果没有这种类型的记录，就不允许Unix域套接字连接。

host

这条记录匹配使用TCP/IP建立的连接。host记录匹配SSL和非SSL的连接尝试，此外还有GSSAPI加密的或non-GSSAPI加密的连接尝试。

如果服务器启动时，配置了合适的listen\_addresses参数，则不进行远程的TCP/IP连接，因为数据库默认行为是只监听在本地环回地址localhost上的TCP/IP连接。

hostssl

这条记录匹配使用TCP/IP建立的连接，但必须是使用SSL加密的连接。要使用这个选项，编译服务器的时候必须打开SSL支持。另外，在服务器启动的时候必须通过设置 ssl 配置参数打开SSL。否则，hostssl记录会被忽略，并且会记录一个警告说它无法匹配任何连接。

hostnossl

这条记录的行为与hostssl相反；它只匹配那些在TCP/IP上不使用SSL的连接。

hostgssenc

这条记录匹配使用TCP/IP建立的连接，但仅当使用GSSAPI加密建立连接时。要使用这个选项，服务器必须具备GSSAPI支持。否则，除了记录无法匹配任何连接的警告以外，hostgssenc记录将被忽略。

hostnogssenc

这个记录类型具有与hostgssenc相反的表现;它仅匹配通过不使用GSSAPI加密的TCP/IP进行的连接尝试。

database

指定记录所匹配的数据库名称。设置为all表示指定该记录匹配所有数据库。值sameuser指定如果被请求的数据库和请求的用户同名，则匹配。值samerole指定请求的用户必须是一个与数据库同名的角色中的成员。对于一个用于samerole目的的角色，超级用户不会被考虑为其中的成员，除非它们是该角色的显式成员（直接或间接），而不是由于超级用户的原因。值replication指定如果一个物理复制连接被请求则该记录匹配，但是，它不匹配逻辑复制连接。注意，物理复制连接不指定任何特定的数据库而逻辑复制连接需要指定。在其它情况下，这是一个特定的瀚高数据库库的名字。可以通过用逗号分隔的方法指定多个数据库，也可以通过在文件名前面放@来指定一个包含数据库名的文件。

user

指定这条记录匹配哪些数据库用户名。值all指定它匹配所有用户。否则，它要么是一个特定数据库用户的名字或者是一个有前导+的组名称（+实际表示”匹配这个角色的任何直接或间接成员角色”，而没有+记号的名字只匹配指定的角色）。如果超级用户显式的是一个角色的成员（直接或间接），那么超级用户将只被认为是该角色的一个成员而不是作为一个超级用户。多个用户名可以通过用逗号分隔的方法提供。一个包含用户名的文件可以通过在文件名前面加上@来指定。

address

指定这个记录匹配的客户端机器地址。这个域可以包含一个主机名、一个IP地址范围或下文提到的特殊关键字之一。一个IP地址范围以该范围的开始地址的标准数字记号指定，然后是一个斜线（/）和一个CIDR掩码长度。掩码长度表示客户端IP地址必须匹配的高序二进制位位数。在给出的IP地址中，这个长度的右边的二进制位必须为零。在IP地址、/和CIDR掩码长度之间不能有空白。

这种方法指定一个IPv4地址范围的典型例子是： [172.20.143.89](https://www.highgo.com/document/v9/zh-cn/safety/172.20.143.89) /32用于一个主机， [172.20.143.0](https://www.highgo.com/document/v9/zh-cn/safety/172.20.143.0) /24用于一个小型网络， [10.6.0.0](https://www.highgo.com/document/v9/zh-cn/safety/10.6.0.0) /16用于一个大型网络。一个单主机的IPv6地址范围看起来像样：::1/128（IPv6回环地址），小型网络的IPv6地址范围则类似于：fe80::7a31:c1ff:0000:0000/96。 [0.0.0.0](https://www.highgo.com/document/v9/zh-cn/safety/0.0.0.0) /0表示所有IPv4地址，并且::0/0表示所有IPv6地址。要指定一个单一主机，IPv4需要用一个长度为32的CIDR掩码或者IPv6用长度为128的CIDR掩码。在网络地址中，不能省略结尾的零。

一个以IPv4格式给出的项将只匹配IPv4连接，一个以IPv6格式给出的项将只匹配IPv6连接，即使对应的地址在IPv4-in-IPv6范围内。请注意如果系统的C库不支持IPv6地址，那么IPv6格式中的项将被拒绝。

你也可以写all来匹配任何IP地址、写samehost来匹配任何本服务器自身的IP地址或者写samenet来匹配本服务器直接连接到的任意子网的任意地址。

如果指定了一个主机名，该名称会与客户端的IP地址的反向名字解析（例如使用DNS时的反向DNS查找）结果进行比较。主机名比较是大小写敏感的。如果匹配上那么将在主机名上执行一次正向名字解析（例如正向DNS查找）来检查它解析到的任何地址是否等于客户端的IP地址。如果两个方向都匹配，则该项被认为匹配（pg\_hba.conf中使用的主机名应该是客户端IP地址的地址到名字解析返回的结果，否则该行将不会匹配。某些主机名数据库允许将一个IP地址关联多个主机名，但是当被要求解析一个IP地址时，操作系统将只返回一个主机名）。

一个以点号（.）开始的主机名声明匹配实际主机名的后缀。因此.example.com将匹配foo.example.com（但不匹配example.com）。

另外当主机名在pg\_hba.conf中被指定时，可建立一个类似nscd的本地名字解析缓存或可通过启用配置参数log\_hostname来在日志中查看客户端的主机名。

IP-addressIP-mask

这两个域可以被用作IP-address/mask-length记号法的替代方案。和指定掩码长度不同，实际的掩码被指定在一个单独的列中。例如， [255.0.0.0](https://www.highgo.com/document/v9/zh-cn/safety/255.0.0.0) 表示IPv4CIDR掩码长度8，而 [255.255.255.255](https://www.highgo.com/document/v9/zh-cn/safety/255.255.255.255) 表示CIDR掩码长度32。需要注意的是这些域不适用于local记录。

auth-method

指定当一个连接匹配这个记录时要使用的认证方法。认证算法如下：

Trust无条件地允许连接。这种方法允许任何可以与瀚高数据库服务器连接的用户以他们期望的任意数据库用户身份登入，不需要口令或者其他任何认证。详见 第4.4 节。

Reject无条件地拒绝连接。这有助于从一个组中”过滤出”特定主机，例如一个reject行可以阻塞一个特定的主机连接，而后面一行允许一个特定网络中的其余主机进行连接。

scram-sha-256执行SCRAM-SHA-256认证来验证用户的口令。详见 第4.5 节。

md5执行SCRAM-SHA-256或MD5认证来验证用户的口令。详见 第4.5 节。

Password要求客户端提供一个未加密的口令进行认证。口令以明文形式在网络上发送的，我们不建议在不可信的网络上使用这种方式，详见 第4.5 节。

gss用GSSAPI认证用户。只对TCP/IP连接可用。详见 第4.6 节,它可以与GSSAPI加密一起结合使用。

sspi用SSPI来认证用户。只在Windows上可用。详见 第4.7 节。

ident通过联系客户端的ident服务器获取客户端的操作系统名，并且检查它是否匹配被请求的数据库用户名。Ident认证只能在TCIP/IP连接上使用。当为本地连接指定这种认证方式时，将用peer认证来替代。

peer从操作系统获得客户端的操作系统用户，并且检查它是否匹配被请求的数据库用户名。这只对本地连接可用。详见 第4.9 节。

ldap使用LDAP服务器认证。详见 第4.10 节。

radius用RADIUS服务器认证。详见 第4.11 节。

cert使用SSL客户端证书认证。详见 第4.12 节。

pam使用操作系统提供的可插入认证模块服务（PAM）认证。详见 第4.13 节。

bsd使用由操作系统提供的BSD认证服务进行认证。详见 第4.14 节。

auth-options

在auth-method域的后面，可以是形如name=value的域，它们指定认证方法的选项。

除了下文列出的与方法相关的选项之外，还有一个与方法无关的认证选项clientcert，它可以在任何hostssl记录中指定。这个选项可以被设置到verify-ca或verify-full.这两个选项都需要客户端提供有效的(受信任的)SSL证书，并且verify-full额外强制证书中的cn(通用名称)匹配用户名或适用的映射。这种行为类似于cert认证方法(参见 第4.12 节)，但是允许客户端证书的验证与任何支持hostssl登记的认证方法相搭配。

在使用客户端证书任何记录上(即一个使用cert认证方法或一个使用clientcert选项)，可以使用clientname选项指定要匹配的客户端证书凭证的哪一部分。这个选项可以用两个值中的一个。如果你指定clientname=CN，这是默认值，则用户名将与证书的CommonName(CN)进行匹配。如果你指定clientname=DN，则用户名将与证书的整个DistinguishedName(DN)进行匹配。这个选项最好与用户名映射一起使用。DN在 [RFC2253](https://tools.ietf.org/html/rfc2253) 1格式的完成完成比较要在这种格式中查看客户端证书的DN，请执行opensslx509-inmyclient.crt-noout--subject-nameoptRFC2253|sed"s/^subject=//"使用这个选项时要小心，特别是使用正则表达式匹配DN的时候。

用@结构包括的文件被读作一个名字列表，它们可以用空白或者逗号分隔。注释用#引入，就像在pg\_hba.conf中那样，并且允许嵌套@结构。除非跟在@后面的文件名是一个绝对路径，文件名都被认为是相对于包含引用文件的目录。

因为每一次连接尝试都会顺序地检查pg\_hba.conf记录，所以这些记录的顺序是非常关键的。通常，靠前的记录有比较严的连接匹配参数和比较弱的认证方法，而靠后的记录有比较松的匹配参数和比较强的认证方法。例如，我们希望对本地TCP/IP连接使用trust认证，而对远程TCP/IP连接要求口令。在这种情况下为来自于 [127.0.0.1](https://www.highgo.com/document/v9/zh-cn/safety/127.0.0.1) 的连接指定trust认证的记录将出现在为一个更宽范围的客户端IP地址指定口令认证的记录前面。

在启动以及主服务器进程收到SIGHUP信号时，pg\_hba.conf文件会被读取。如果你在活动的系统上编辑了该文件，你将需要通知管理员（使用pg\_ctlreload，调用SQL函数pg\_reload\_conf(),或使用kill-HUP）使其重新读取该文件。

注意

上述描述，不适用于Windows平台，在Windows上，pg\_hba.conf文件中的任何更改会立即被应用到后续的新连接上。

系统视图 pg\_hba\_file\_rules 可以预先测试对pg\_hba.conf文件的更改，该视图也可以在该文件的装载没有产生预期效果时用于诊断问题。该视图中带有非空error域的行就表示该文件对应行中存在问题。

要连接到一个特定数据库，一个用户必须不仅要通过pg\_hba.conf检查，还必须要有该数据库上的CONNECT权限。如果你希望限制哪些用户能够连接到哪些数据库，授予/撤销CONNECT权限通常比在pg\_hba.conf项中设置规则简单。

如下展示了pg\_hba.conf项的一些例子。不同认证方法的详情请见下一节。

pg\_hba.conf项示例。

```
# 允许本地系统上的任何用户

# 通过 Unix 域套接字以任意

# 数据库用户名连接到任意数据库（本地连接的默认值）。

#

# TYPE DATABASE USER ADDRESS METHOD

local all all trust

# 相同的规则，但是使用本地环回 TCP/IP 连接。

#

# TYPE DATABASE USER ADDRESS METHOD

host all all [127.0.0.1](127.0.0.1)/32 trust

# 和前一行相同，但是使用了一个独立的掩码列

#

# TYPE DATABASE USER IP-ADDRESS IP-MASK METHOD

host all all [127.0.0.1](127.0.0.1) [255.255.255.255](255.255.255.255)
trust

# IPv6 上相同的规则

#

# TYPE DATABASE USER ADDRESS METHOD

host all all ::1/128 trust

# 使用主机名的相同规则（通常同时覆盖 IPv4 和 IPv6）。

#

# TYPE DATABASE USER ADDRESS METHOD

host all all localhost trust

# 允许来自任意具有 IP 地址192.168.93.x 的主机上任意用户以 ident
为该连接所报告的相同用户名连接到数据库
"postgres"（通常是操作系统用户名）。

#

# TYPE DATABASE USER ADDRESS METHOD

host postgres all [192.168.93.0](192.168.93.0)/24 ident

# 如果用户的口令被正确提供，允许来自主机
[192.168.12.10](192.168.12.10)的任意用户连接到数据库 "postgres"。

#

# TYPE DATABASE USER ADDRESS METHOD

host postgres all [192.168.12.10](192.168.12.10)/32 scram-sha-256

# 如果用户的口令被正确提供，允许 example.com
中主机上的任意用户连接到任意数据库。
```
```
#

#
为大部分用户要求SCRAM认证，但是用户'mike'是个例外，他使用的是不支持SCRAM认证的旧客户端。
#
# TYPE DATABASE USER ADDRESS METHOD
host all mike .example.com md5
host all all .example.com scram-sha-256
```

\# 如果没有前面的 "host" 行，这三行将拒绝所有来自  
[192.168.54.1](https://www.highgo.com/document/v9/zh-cn/safety/192.168.54.1) 的连接（因为那些项将首先被匹配），但是允许来自互联网其他任何地方的GSSAPI-encrypted连接。零掩码导致主机IP  
地址中的所有位都不会被考虑， #  
因此它匹配任意主机。未加密GSSAPI连接(which  
"跳转"到第三行是因为"hostgssenc" 仅匹配加密的 GSSAPI 连接)  
是被允许的, 但只能来自 [192.168.12.10](https://www.highgo.com/document/v9/zh-cn/safety/192.168.12.10).

```
#

# TYPE DATABASE USER ADDRESS METHOD

host all all [192.168.54.1](192.168.54.1)/32 reject

hostgssenc all all [0.0.0.0](0.0.0.0)/0 gss

host all all [192.168.12.10](192.168.12.10)/32 gss

# 允许来自 192.168.x.x 主机的用户连接到任意数据库，如果它们能够通过
```

ident 检查。例如，假设 ident说用户是 "bryanh" 并且他要求以 #  
PostgreSQL 用户 "guest1" 连接，如果在 pg\_ident.conf  
有一个映射"omicron" 的选项说 "bryanh" 被允许以 "guest1"  
连接，则该连接将被允许。

```
#

# TYPE DATABASE USER ADDRESS METHOD

host all all [192.168.0.0](192.168.0.0)/16 identmap=omicron

#
```

如果这些是本地连接的唯一三行，它们将允许本地用户只连接到它们自己的数据库（与其数据库用户名同名的数据库），不过管理员和角色  
"support" 的成员除外（它们可以连接到所有数据库）。文件$PGDATA/admins  
包含一个管理员名字的列表。在所有情况下都要求口令。

```
#

# TYPE DATABASE USER ADDRESS METHOD

local sameuser all md5

local all @admins md5

local all +support md5

# 上面的最后两行可以被整合为一行：

local all @admins,+support md5

# 数据库列也可以用列表和文件名：

local db1,db2,@demodbs all md5
```

#bookmark3068)

## 用户名映射

当使用像Ident或者GSSAPI之类的外部认证系统时，发起连接的操作系统用户名可能不同于要被使用的数据库用户（角色）。在这种情况下，一个用户名映射可被用来把操作系统用户名映射到数据库用户。要使用用户名映射，需在pg\_hba.conf的选项域指定map=map-name。此选项支持所有接收外部用户名的认证方法。由于不同的连接可能需要不同的映射，在pg\_hba.conf中的map-name参数中指定要被使用的映射名，用以指示哪个映射用于每个个体连接。

用户名映射定义在ident映射文件中，默认情况下它被命名为pg\_ident.conf并被存储在集簇的数据目录中（不过，可以把该映射文件放在其他地方，见 [ident\_file 配置参数）。ident映射文件包含的行的一般格式：

```
map-name system-username database-username
```

以pg\_hba.conf中同样的方式处理注释，空白和行延续。map-name是一个任意名称，它被用于在pg\_hba.conf中引用该映射。其他两个域指定一个操作系统用户名和一个匹配的数据库用户名。相同的map-name可以被反复地用在同一个映射中指定多个用户映射。

对于一个给定操作系统用户可以对应多少个数据库用户没有限制。因此，一个映射中的项应该被看成意味着”这个操作系统用户被允许作为这个数据库用户连接”。如果有任何映射项把从外部认证系统获得的用户名和用户要求的数据库用户名配对，该连接将被允许。

如果system-username域以一个斜线（/）开始，域的剩余部分被当做一个正则表达式处理。正则表达式可以包括一个单一的捕获，或圆括号子表达式，然后它可以在database-username域中以\\1（反斜线一）被引用。这允许在单个行中多个用户名的映射，这特别有助于简单的语法替换。例如，这些项：

```
mymap /\^(.*)@mydomain\.com$ \1

mymap /\^(.*)@otherdomain\.com$ guest
```

将为用户移除以@mydomain.com结束的系统用户名的域部分，及允许系统名以@otherdomain.com结束的任意用户作为guest登入。

在默认情况下，一个正则表达式可以只匹配字符串的一部分。如上例所示，使用^和$来强制匹配整个系统用户名通常是明智的。

在启动以及主服务器进程收到SIGHUP信号时，pg\_ident.conf文件会被读取。如果在已启动的系统上编辑了该文件，你将需要通知管理员（使用pg\_ctlreload,调用SQL函数pg\_reload\_conf(),或用kill-HUP）重新读取文件。

下列示例中展示了一个可以联合pg\_hba.conf文件使用的pg\_ident.conf文件。在这个例子中，对于任何登入到192.168网络上的一台机器的用户，如果该用户没有操作系统用户名bryanh、ann或robert，则他不会被授予访问权限。只有当Unix用户robert尝试作为瀚高数据库用户bob连接时，他才被允许访问。ann只被允许作为ann连接。用户bryanh被允许以bryanh或者guest1连接。

pg\_ident.conf文件示例

```
# MAPNAME SYSTEM-USERNAME PG-USERNAME

omicron bryanh bryanh

omicron ann ann

# bob 在这些机器上有用户名 robert

omicron robert bob

# bryanh 也可以作为 guest1 连接

omicron bryanh guest1
```

## 认证方法

瀚高数据库为认证用户提供不同的方法：

Trust authentication,简单的信任用户声称的身份。

Password authentication,需要用户提供密码。

GSSAPI  
authentication,依靠GSSAPI兼容的安全库，常常用于访问认证服务器，例如Kerberos或微软活动目录服务器。

SSPI authentication,用windows规定的类似于GSSAPI的协议。

Ident authentication,依靠客户机器上的”Identification  
Protocol”([RFC1413](https://tools.ietf.org/html/rfc1413) 2)服务，(在本地Unix-socket连接,这个按对等认证处理)。

Peer  
authentication,依靠操作系统工具来识别本地连接另一端的进程。这种方法不支持远程连接。

LDAP authentication,依靠LDAP认证服务器.

RADIUS authentication,依靠RADIUS认证服务器.

Certificate  
authentication,需要SSL连接和通过SSL证书检查的认证用户。

PAM authentication,依靠PAM库(Pluggable Authentication  
Modules，可插拔认证模块)。

BSD  
authentication,依靠BSD认证框架(当前仅在OpenBSD上应用)。

对等身份验证通常适用于本地连接，信任认证在某些情况下可能是适合的。密码认证是远程连接的常见选择。所有其它的选项都需要某种外部安全基础架构(通常是认证服务器或颁发SSL证书的证书颁发机构)，或用于某些特定平台。以下各节将更详细地介绍这些身份认证方法。

## 信任认证

当trust认证方式时，瀚高数据库支持任何可以连接到服务器的人都被授权使用他们指定的任何数据库用户名访问数据库。当然，在database和user列中设置的限制仍然适用。只有当在操作系统层对进入服务器的连接有足够保护时，才推荐使用这种方法。

trust认证对于单用户工作站的本地连接是非常合适和方便的。通常它本身不适用于一台多用户机器。不过，只要你利用文件系统权限限制了对服务器的Unix域套接字文件的访问，即使在多用户机器上，你也可以使用trust。要做这些限制，你可以设置unix\_socket\_permissions配置参数或unix\_socket\_group。或者你可以设置unix\_socket\_directories配置参数来把Unix域套接字文件放在一个经过恰当限制的目录中。

设置文件系统权限只能有助于Unix套接字连接。本地TCP/IP连接不会被文件系统权限限制。因此，如果你想利用文件系统权限来控制本地安全，可以从pg\_hba.conf中移除host...[127.0.0.1](https://www.highgo.com/document/v9/zh-cn/safety/127.0.0.1)...行，或者把它改为一个非trust认证方法。

如果通过指定trust的pg\_hba.conf行让你信任每一个被允许连接到服务器的机器上的用户，trust认证只适合TCP/IP连接。为任何不是来自localhost（ [127.0.0.1](https://www.highgo.com/document/v9/zh-cn/safety/127.0.0.1) ）的TCP/IP连接使用trust是不合理的。

## 口令认证

瀚高数据库支持多种基于口令的认证方法。这些方法的过程类似，但是区别在于用户口令如何被存放在服务器上以及客户端提供的口令如何被通过连接发送。

sm3

sm3方法是中国国家标准的密码杂凑算法，用于生成固定长度的哈希值，以确保数据的完整性和支持数字签名。SM3产生一个256位（32字节）长的哈希值，该算法考虑了对差分攻击和其他已知攻击方式的抵抗能力，提供了一定程度的安全保障，适用于多种安全应用场景。

scram-sm3

瀚高数据库支持scram-sm3算法认证。scram是指包含服务器和客户端双向确认的用户认证体系，配合信道加密可以比较好地抵御中间人、拖库、伪造等攻击。为符合国密标准，瀚高数据库使用sm3  
hmac算法完成scram认证流程。

scram-sha-256

scram-sha-256方法按照 [RFC7677](https://tools.ietf.org/html/rfc7677) 3中的描述执行SCRAM-SHA-256认证。它使用的是一种挑战-响应的方案，可以防止在不可信连接上对口令的嗅探并且支持在服务器上以一种加密哈希的方式存放口令，因此被认为是安全的。

md5

md5方法使用一种自定义的安全性较低的挑战-响应机制。它能防止口令嗅探并且防止口令在服务器上以明文存储，但是无法保护攻击者想办法从服务器上窃取了口令哈希的情况。此外，现在认为MD5哈希算法对于确定攻击已经不再安全。md5方法不能与 db\_user\_namespace 特性一起使用。为了简化从md5方法到较新的SCRAM方法的转变，如果在pg\_hba.conf中指定了md5但是用户在服务器上的口令是为SCRAM加密的，则将自动选择基于SCRAM的认证。

瀚高数据库支持交叉认证，即实际应用场景中我们常会遇见存储算法与认证算法的配置不统一的问题，增加交叉认证算法后，其存储与认证算法的16种组合中有12种无需修改用户密码可直接使用，有4种需要修改用户密码后使用。通常在认证算法安全级别低于存储算法安全级别时需要修改用户密码。比如：要把现有的口令认证从md5升级到scram-sha-256，可以在确保所有在用的客户端已经足以支持SCRAM之后，在postgresql.conf中设置password\_encryption='scram-sha-256'，然后让所有用户设置新口令并且在pg\_hba.conf中将认证方法说明改为scram-sha-256。

交叉认证规则详见下表：

---

| 认证算法 | 存储算法 | 是否修改密码 | 实际使用认证算法 |
| --- | --- | --- | --- |
| MD5 | MD5 | 不需要 | MD5 |
| SM3 | SM3 | 不需要 | SM3 |
| SCRAM-SHA-256 | SCRAM-SHA-256 | 不需要 | SCRAM-SHA-256 |
| SCRAM-SM3 | SCRAM-SM3 | 不需要 | SCRAM-SM3 |
| MD5 | SCRAM-SHA-256 | 不需要 | SCRAM-SHA-256 |
| MD5 | SCRAM-SM3 | 不需要 | SCRAM-SM3 |
| SM3 | SCRAM-SHA-256 | 不需要 | SCRAM-SHA-256 |
| SM3 | SCRAM-SM3 | 不需要 | SCRAM-SM3 |
| SCRAM-SHA-256 | MD5 | 需要 | N/A |
| SCRAM-SHA-256 | SM3 | 需要 | N/A |
| SCRAM-SM3 | MD5 | 需要 | N/A |
| SCRAM-SM3 | SM3 | 需要 | N/A |
| MD5 | SM3 | 不需要 | SM3-MD5 |
| SM3 | MD5 | 不需要 | MD5-SM3 |
| SCRAM-SHA-256 | SCRAM-SM3 | 不需要 | SCRAM-SM3-SHA256 |
| SCRAM-SM3 | SCRAM-SHA-256 | 不需要 | SCRAM-SHA256-SM3 |

---

## GSSAPI认证

GSSAPI是用于 [RFC2743](https://tools.ietf.org/html/rfc2743) 4中定义的安全认证的一个工业标准协议。瀚高数据库支持GSSAPI用于认证，通讯加密或两者都做。GSSAPI为支持它的系统提供自动认证（单点登录）。认证本身是安全的。如果使用了GSSAPI加密或SSL加密，数据库连接发送的数据将被加密，否则将不加密。

当编译瀚高数据库时，GSSAPI支持必须被启用。当GSSAPI使用Kerberos时，它使用一个标准服务主体(身份验证)名称，以servicename/hostname@realm的格式。特定安装使用的主体名称(principalname)没有被以任何方式编码在瀚高数据库服务器中；而是被指定在keytab文件中，服务器读取该文件以决定它的身份。如果在keytab文件中罗列着多个主体，服务器将接受其中任何一个。服务器的领域名称(realmname)是在服务器可访问的Kerberos配置文件中指定的优先领域。

当连接时，客户端必须知道它打算连接的服务器的主体名称。主体名称的servicename部分通常是postgres，但是其他值可以通过libpq的 krbsrvname 连接参数来选择。hostname部分是libpq告知要连接的全限制的主机名称。领域名称是在客户端可访问的Kerberos配置文件中指定的优先领域。

客户端也可以有主体名称作为它自己的身份(并且它必须拥有针对这个主体的有效的标签

\[ticket\])。要使用GSSAPI做身份验证，客户端的主体必须与瀚高数据库用户名关联。pg\_ident.conf配置文件可以用于映射主体到用户名；例如，pgusername@realm可能会被映射到pgusername。或者，你可以使用完整的username@realm作为瀚高数据库中的角色而无需任何映射。

瀚高数据库也支持映射客户端主体到用户名，通过从主体中剥离领域(realm)的方式。这种方法是为了产品向后兼容性，并且我们不建议使用它，因为这样就无法区分具有相同用户名却来自不同realm的不同用户了。要启用这种方法，可将include\_realm设置为0。对于简单的单realm安装，这样做并且设置krb\_realm参数（这会检查principal的realm是否正好匹配krb\_realm中的参数）仍然是安全的。但比起在pg\_ident.conf中指定一个显式映射来说，这种方法的效率较低。

服务器的keytab文件的位置是由 krb\_server\_keyfile 配置参数指定的。出于安全原因，它建议针对瀚高数据库使用独立的keytab而不是允许服务器读取系统的keytab文件。确保你的服务器的keytab文件是对瀚高数据库服务器账号可读的(并且最好是只读的，不可写)。keytab文件用Kerberos软件生成。下面展示了用MIT兼容的Kerberos5实现的kadmin来做这个的例子：

```
kadmin% addprinc -randkey postgres/server.my.domain.org

kadmin% ktadd -k krb5.keytab postgres/server.my.domain.org
```

GSSAPI验证方法支持下列身份验证选项:

include\_realm

如果设置为0，在通过用户名映射之前，来自已认证用户principal的realm名称会被剥离掉。我们不建议这样做，这种方法主要是为了向后兼容性而存在的，因为它在多realm环境中是不安全的（除非也使用krb\_realm）。推荐用户让include\_realm设置为默认值（1）并且在pg\_ident.conf中提供一条显式的映射来把principal名称转换成瀚高数据库用户名。

map

允许从客户端主体到数据库用户名之间的映射。对于一个GSSAPI/Kerberos原则，例如 [username@EXAMPLE.COM](mailto:username@EXAMPLE.COM) （或者username/ [hostbased@EXAMPLE.COM](mailto:hostbased@EXAMPLE.COM) ），用于映射的用户名会是 [username@EXAMPLE.COM](mailto:username@EXAMPLE.COM) （或者username/ [hostbased@EXAMPLE.COM](mailto:hostbased@EXAMPLE.COM) ），除非include\_realm已经被设置为0，在那种情况下username（或者username/hostbased）是映射时被视作系统用户名。

krb\_realm

设置realm为对用户principal名进行匹配的范围。如果这个参数被设置，只有那个realm的用户将被接受。如果它没有被设置，任何realm的用户都能连接，服从任何已完成的用户名映射。

在这些设置之外，对于不同的pg\_hba.conf项可能有所不同，还有服务器范围的 krb\_caseins\_users 配置参数。如果设置为真，客户端主体匹配用户映射条目是大小写不敏感的。如果设置了krb\_realm，也不区分大小写。

## SSPI认证

SSPI是一种用于带单点登录的安全认证的Windows技术。瀚高数据库在negotiate模式中将使用SSPI，它在可能的情况下使用Kerberos并在其他情况下自动降回到NTLM。只有在服务器和客户端都运行着Windows时，SSPI才能工作。或者在非Windows平台上GSSAPI可用时，SSPI也能工作。当使用Kerberos认证时，SSPI和GSSAPI的工作方式相同。

SSPI支持的选项：

include\_realm

设置为0，在通过用户名映射之前来自已认证用户principal的realm名称会被剥离掉。我们不建议这样做，这种方法主要是为了向后兼容性而存在的，因为它在多realm环境中是不安全的（除非也使用krb\_realm）。推荐用户将include\_realm设置为默认值（1）并且在pg\_ident.conf中提供一条显式的映射来把principal名称转换成瀚高数据库用户名。

compat\_realm

设置为1，表示该域的SAM兼容名称（也被称为NetBIOS名称）被用于include\_realm选项。这是默认值。如果被设置为0，会使用来自Kerberos用户主名的真实realm名称。不建议禁用这个选项，除非你的服务器运行在一个域账号（这包括一个域成员系统上的虚拟服务账号）下并且所有通过SSPI认证的所有客户端也在使用域账号，否则认证将会失败。

upn\_username

如果这个选项和compat\_realm一起被启用，来自KerberosUPN的用户名会被用于认证。如果它被禁用（默认），会使用SAM兼容的用户名。默认情况下，对于新用户账号这两种名称是一样的。注意如果没有显式指定用户名，libpq会使用SAM兼容的名称。如果你使用的是libpq或者基于它的驱动，你应该让这个选项保持禁用或者在连接字符串中显式指定用户名。

map

允许在系统和数据库用户名之间的映射。对于一个GSSAPI/Kerberos原则，例如 [username@EXAMPLE.COM](mailto:username@EXAMPLE.COM) （或者更不常见的username/ [hostbased@EXAMPLE.COM](mailto:hostbased@EXAMPLE.COM) ），用于映射的用户名会是 [username@EXAMPLE.COM](mailto:username@EXAMPLE.COM) （或者username/ [hostbased@EXAMPLE.COM](mailto:hostbased@EXAMPLE.COM) ，相应地），除非include\_realm已经被设置为0，在那种情况下username（或username/hostbased）是映射时被视作系统用户名的东西。

krb\_realm

设置领域为对用户principal名进行匹配的范围。如果这个参数被设置，只有那个领域的用户将被接受。如果它没有被设置，任何领域的用户都能连接，服从任何已完成的用户名映射。

## Ident认证

ident认证方法通过从一个ident服务器获得客户端的操作系统用户名并且用它作为被允许的数据库用户名（和可选的用户名映射）来工作。它只在TCP/IP连接上支持。

当为一个本地（非TCP/IP）连接指定ident时，将实际使用peer认证。

ident支持的选项：

map

允许系统和数据库用户名之间的映射。”Identification  
Protocol（标识协议）”在 [RFC1413](https://tools.ietf.org/html/rfc1413) 5中描述。实际上每个类Unix操作系统都带着一个默认监听TCP113端口的ident服务器。ident服务器的基本功能是回答类似这样的问题：”哪个用户从你的端口X发起了连接并且连到了我的端口Y？”。因为当一个物理连接被建立后，瀚高数据库既知道X也知道Y，所以它可以询问尝试连接的客户端主机上的ident服务器并且在理论上可以判断任意给定连接的操作系统用户。

这个过程的缺点是它依赖于客户端的完整性：如果客户端机器不可信或者被攻破，攻击者可能在113端口上运行任何程序并且返回他们选择的任何用户。因此这种认证方法只适用于封闭的网络，这样的网络中的每台客户端机器都处于严密的控制下并且数据库和操作数据库管理员操作时可以方便地联系。换句话说，你必须信任运行ident服务器的机器。注意这样的警告：标识协议的本意不是作为一种认证或访问控制协议。

有些ident服务器有一个非标准的选项，它导致返回的用户名是被加密的，使用的是只有原机器管理员知道的一个密钥。当与瀚高数据库配合使用ident服务器时，一定不要使用这个选项，因为瀚高数据库无法对返回的字符串进行解密以获取实际的用户名。

## Peer认证

Peer认证方法通过从内核获得客户端的操作系统用户名并把它用作被允许的数据库用户名（和可选的用户名映射）来工作。这种方法只在本地连接上支持。

peer支持的配置选项：

map

允许在系统和数据库用户名之间的映射。Peer认证只在提供getpeereid()函数、SO\_PEERCRED套接字参数或相似机制的操作系统上可用。这些OS当前包括Linux、大部分的BSD包括OSX以及Solaris。

## LDAP认证

LDAP认证方法操作起来类似于password，只不过它使用LDAP作为密码验证方法。LDAP只被用于验证用户名/口令对。因此，在使用LDAP进行认证之前，用户必须已经存在于数据库中。

LDAP认证可以在两种模式下操作。在第一种模式中（我们将称之为简单绑定模式），服务器将绑定到构造成prefix  
username  
suffix的可区分名称。通常，prefix参数被用于指定cn=或者一个活动目录环境中的DOMAIN\\。suffix被用来指定非活动目录环境中的DN的剩余部分。

在第二种模式中（我们将称之为搜索与绑定模式），服务器首先用一个固定的用户名和密码（用ldapbinddn和ldapbindpasswd指定）绑定到LDAP目录，并为试图登入该数据库的用户执行一次搜索。如果没有配置用户名和密码，将尝试一次匿名绑定到目录。搜索将在位于ldapbasedn的子树上被执行，并将尝试做一次ldapsearchattribute中指定属性的精确匹配。一旦在这次搜索中找到用户，服务器断开并且作为这个用户重新绑定到目录，使用由客户端指定的口令来验证登录是正确的。这种模式与在其他软件中的LDAP认证所使用的相同，例如Apachemod\_authnz\_ldap和pam\_ldap。这种方法允许位于目录中用户对象的更大灵活性，但是会导致建立两个到LDAP服务器的独立连接。

下列配置选项被用于两种模式：

ldapserver

要连接的LDAP服务器的名称或IP地址。可以指定多个服务器，用空格分隔。

ldapport

要连接的LDAP服务器的端口号。如果没有指定端口，LDAP库的默认端口设置将被使用。

ldapscheme

设置为ldaps可以使用LDAPS。这是一种非标准的在SSL之上使用LDAP的方法，在有一些LDAP服务器实现上可以支持。其他选择还可以参考ldaptls选项。

ldaptls

设置为1以使瀚高数据库和LDAP服务器之间的连接使用TLS加密。这会按照 [RFC4513](https://tools.ietf.org/html/rfc4513) 6使用StartTLS操作。其他选择还可以参考ldapscheme选项。

注意使用ldapscheme或ldaptls仅会加密瀚高数据库服务器和LDAP服务器之间的通信。瀚高数据库服务器和瀚高数据库客户端之间的连接仍是未加密的，除非也在其上使用SSL。

下列选项只被用于简单绑定模式：

ldapprefix

当做简单绑定认证时，前置到用户名形成要用于绑定的DN的字符串。

ldapsuffix

当做简单绑定认证时，前置到用户名形成要用于绑定的DN的字符串。

下列选项只被用于搜索与绑定模式：

ldapbasedn

当做搜索与绑定认证时，开始搜索用户的根DN。

ldapbinddn

当做搜索与绑定认证时，用户要绑定到目录开始执行搜索的DN。

ldapbindpasswd

当做搜索与绑定认证时，用户用于绑定到目录开始执行搜索的口令。

ldapsearchattribute

当做搜索与绑定认证时，在搜索中用来与用户名匹配的属性。如果没有指定属性，将会使用uid属性。

ldapsearchfilter

在做search+bind认证时使用的搜索过滤器。$username的出现将被替换为用户名。允许比ldapsearchattribute更加灵活的搜索过滤器。

ldapurl

一个 [RFC4516](https://tools.ietf.org/html/rfc4516) 7LDAPURL。这是一种用更紧凑和标准的形式书写某些其他LDAP选项的可选方法。格式为

ldap\[s\]://host\[:port\]/basedn\[?\[attribute\]\[?\[scope\]\[?\[filter\]\]\]\]

scope必须是base、one、sub之一，通常是最后一个（默认是base，但它在这个应用中作用不大）。attribute可以指定一个属性，在这种情况中它被用作ldapsearchattribute的一个值。如果attribute为空，那么filter可以被用作ldapsearchfilter的一个值。

URL模式ldaps选择LDAPS方法来在SSL上建立LDAP连接，等效于使用ldapscheme=ldaps。要使用StartTLS操作加密LDAP连接，可以用普通的URL模式ldap并且在ldapurl之外指定ldaptls选项。

对于非匿名绑定，ldapbinddn和ldapbindpasswd必须被指定为独立选项。LDAPURL当前只支持OpenLDAP，而不支持Windows。将简单绑定的选项中混合用于搜索与绑定的选项是一种错误。在使用search+bind模式时，可以用ldapsearchattribute指定的单个属性执行搜索，或者使用ldapsearchfilter指定的自定义搜索过滤器执行搜索。指定ldapsearchattribute=foo等效于指定ldapsearchfilter="(foo=$username)"。如果两个选项都没有被指定，则默认为ldapsearchattribute=uid。

一个简单绑定LDAP配置的例子：

```
host...ldapldapserver=ldap.example.netldapprefix="cn="ldapsuffix=",

dc=example,dc=net"
```

当请求一个作为数据库用户someuser到数据库服务器的连接时，瀚高数据库将尝试使用cn=someuser,dc=example,dc=net和客户端提供的口令来绑定到LDAP服务器。如果那个连接成功，将被授予数据库访问权限。

一个搜索与绑定配置的例子：

```
host...ldapldapserver=ldap.example.netldapbasedn="dc=example,dc=net"

ldapsearchattribute=uid
```

当请求一个作为数据库用户someuser到数据库服务器的连接时，瀚高数据库将尝试匿名绑定（因为没有指定ldapbinddn）到LDAP服务器，在指定的基础DN下执行一次对于(uid=someuser)的搜索。如果找到一个项，则它将尝试使用找到的信息和客户端提供的口令进行绑定。如果第二个连接成功，将被授予数据库访问。

这里是被写成一个URL的相同搜索与绑定配置：

host...ldapldapurl=" [ldap://ldap.example.net/dc=example](ldap://ldap.example.net/dc=example),dc=net?uid?sub"

一些支持根据LDAP认证的其他软件使用相同的URL格式，因此很容易共享该配置。这里是一个search+bind配置的例子，它使用ldapsearchfilter而不是ldapsearchattribute来允许用用户ID或电子邮件地址进行认证：

```
host...ldapldapserver=ldap.example.netldapbasedn="dc=example,dc=net"

ldapsearchfilter="(|(uid=$username)(mail=$username))"
```

这是一个search+bind配置的例子，它使用DNSSRVdiscovery来查找域名example.net的LDAP服务的主机名和端口。

```
host...ldapldapbasedn="dc=example,dc=net"
```

如例子中所示，由于LDAP通常使用逗号和空格来分割一个DN的不同部分，在配置LDAP选项时通常有必要使用双引号包围的参数值。

## RADIUS认证

这种认证方法的操作类似于password，不过它使用RADIUS作为密码验证方式。RADIUS只被用于验证用户名/密码对。因此，在RADIUS能被用于认证之前，用户必须已经存在于数据库中。

当使用RADIUS认证时，一个访问请求消息将被发送到配置好的RADIUS服务器。这一请求需要是AuthenticateOnly类型，并且包含参数username、password和NASIdentifier。该请求将使用一个与服务器共享的密钥加密。RADIUS服务器将对这个请求响应AccessAccept或者AccessReject。不支持RADIUSaccounting。

可以指定多个RADIUS服务器，这种情况下将会依次尝试它们。如果从一台服务器接收到否定响应，则认证失败。如果没有接收到响应，则将会尝试列表中的下一台服务器。要指定多台服务器，可用双引号括住列表并用逗号将服务器名称分开。如果指定了多台服务器，其他RADIUS选项也可以用逗号分隔的列表给出，用来为每台服务器应用个别的值。它们也可以指定为单个值，这种情况下该值将被应用到所有的服务器。

RADIUS支持下列配置选项：

radiusservers

连接到RADIUS服务器的DNS名称或IP地址。此参数是必选参数。

radiussecrets

和RADIUS服务器秘密交谈时会用到共享密钥。这在瀚高数据库和RADIUS服务器之间必须有完全相同的值。我们推荐用一个至少16个字符的字符串。此参数是必选参数。

如果瀚高数据库编译为支持OpenSSL，所用的加密向量将只是强密码。在其他情况下，到RADIUS服务器的传输应该被视为应该被视为被混淆的、不安全的。如有必要，应采用外部安全措施。

radiusports

连接RADIUS服务器的端口号。如果没有指定端口，则使用默认RADIUS端口1812。

radiusidentifiers

在RADIUS请求中字符串被用作NASIdentifier。这个参数可以被用于识别用户尝试连接哪些数据库集群，可以被用于RADIUS服务器上的策略匹配。如果没有指定标识符，默认使用瀚高数据库。

如果RADIUS参数值中需要有逗号或者空格，可以通过双引号括住该值来完成，但这样做是比较繁琐的因为需要两层双引号。将空格放到RADIUS秘密字符串的一个示例为：

```
host...radiusradiusservers="server1,server2"radiussecrets="""secret

one"",""secrettwo"""
```

## 证书认证

这种认证方法使用SSL客户端证书执行认证。因此，它只适用于SSL连接。当使用这种认证方法时，服务器将要求客户端提供一个有效的、可信的证书。不会有密码提示将被发送到客户端。证书的cn（通用名）属性将与被请求的数据库用户名进行比较，并且如果匹配将允许登录。用户名映射可以被用来允许cn与数据库用户名不同。

下列被支持的配置选项用于SSL证书认证：

map

允许在系统和数据库用户名之间的映射。将clientcert选项与cert验证一起使用是多余的，因为cert身份验证是经过clientcert=verify-full的有效的trust验证。

## PAM认证

这种认证方法操作起来类似password，只不过它使用PAM（插入式验证模块）作为认证机制。默认的PAM服务名是瀚高数据库。PAM只被用于验证用户名/口令对并且可以有选择地验证已连接的远程主机名或IP地址。因此，在使用PAM进行认证之前，用户必须已经存在于数据库中。

下列被支持的配置选项用于PAM：

pamservice

PAM服务名称。

pam\_use\_hostname

判断是否通过PAM\_RHOST项把远程IP地址或者主机名提供给PAM模块。默认情况下会使用IP地址。把这个选项设置为1可以使用解析过的主机名。主机名解析可能导致登录延迟（大部分的PAM配置不使用这些信息，因此只有使用为利用这种信息而特别创建的PAM配置时才需要考虑这个设置）。

如果PAM被设置为读取/etc/shadow，认证将会失败，因为瀚高数据库服务器是由一个非root用户启动。然而，当PAM被配置为使用LDAP或其他认证验证方法时这就不是一个问题。

## BSD认证

这种认证方法操作起来类似于password，不过它使用BSD认证来验证口令。BSD认证只被用来验证用户名/口令对。因此，在BSD认证可以被用于认证之前，用户的角色必须已经存在于数据库中。BSD认证框架当前只在OpenBSD上可用。

瀚高数据库中的BSD认证使用auth-瀚高数据库登录类型，如果login.conf中定义了瀚高数据库登录分类，就会用它来认证。默认情况下这种登录分类不存在，瀚高数据库将使用默认的登录分类。

要使用BSD认证，瀚高数据库用户账号（也就是运行服务器的操作系统用户）必须首先被加入到auth组中。在OpenBSD系统上默认存在auth组。

## 双因素认证

双因素认证是一种安全过程，在用户登录或执行敏感操作时，除了要求用户提供传统的用户名和密码（第一因素，即”你知道的东西”），还需要提供第二种验证形式（第二因素）。这种额外的验证步骤能够显著提高账户的安全性，因为它使得即使攻击者获取了用户的密码，也难以未经授权访问系统。在数据库环境中，双因素认证可以用于保护对数据库的访问，确保只有授权人员能够查询、修改或管理数据。瀚高数据库在支持口令认证的基础上进行二次认证，当前支持一次一密口令认证（TOTP）、公钥认证（RSA/SM2）、证书认证（SM2）三种双因素认证中的第二因素类型。

启用双因素认证首先需要在pg\_hba.conf文件中原始认证后面添加’totp/pkey/cert’四种类型中的一项，另外，二次认证算法必需的参数通过函数pg\_set\_2fa()来设置。

TOTP认证

TOTP认证为基于时间的一次一密手机令牌形式的二次认证方式。开启TOTP认证需要首先通过超级用户或安全管理员使用函数pg\_set\_2fa()设置基础密钥，其中base32编码的基础密钥可通过外部工具生成。TOTP基础密钥需同步到用户手机APP用于登录时生成临时密码，用户登录时在常规认证(MD5等)认证通过后等待用户输入TOTP临时密码。临时密码为六位阿拉伯数字，每30秒变换一次。使用TOTP认证需要确保手机时间与数据库服务器时间一致。

TOTP认证需要管理员预先设置基础密钥，设置方式如下：

```
select pg_set_2fa('username'，'totp','base32编码密钥');
```

公钥认证

公钥认证是在支持SM2或RSA算法的openssl环境中，实现预置SM2/RSA公钥形式的二次认证方式。开启公钥认证需要首先通过函数pg\_set\_2fa()设置密钥，其中base64编码的DER格式的SM2/RSA公钥可通过外部工具生成。客户端通过设置base64编码的DER格式的私钥到环境变量PGPRIVATEKEY或libpq参数privatekey。

公钥认证需要管理员预先设置用户公钥，设置方式如下：

```
select pg_set_2fa('username','pkey','base64编码的DER格式的SM2/RSA公钥');
```

证书认证

证书认证是在支持SM2或RSA算法（本阶段未实现）和X509证书的openssl环境中，实现SM2或RSA证书认证形式的二次认证方式。管理员需要通过外部工具或调用openssl生成根证书root.crt，并将根证书保存到数据库数据目录，管理员通过根证书来签发客户端证书。用户需要将客户端证书和客户端私钥保存到客户端本地，并设置参数clientcertfile和clientkey，或者环境变量PGCLIENTCERTFILE和PGCLIENTKEYFILE；

证书认证需要管理员预先设置用户证书类型，设置方式为如下：

select pg\_set\_2fa(‘username’,’cert’,’sm2/rsa’);

## 认证问题

认证失败以及相关的问题通常由类似下面的错误消息显示

FATAL:nopg\_hba.conf entry for  
host" [123.123.123.123](https://www.highgo.com/document/v9/zh-cn/safety/123.123.123.123) ",user"andym",database

"testdb"

这条消息最可能出现的情况是你成功地联系了服务器，但它不愿意和你对话。就像消息本身所建议的，服务器拒绝了连接请求，因为它没有在其pg\_hba.conf配置文件里找到匹配项。

FATAL:password authentication failed for user"andym"

这样的消息表示你联系了服务器，并且它也愿意和你交谈，但是你必须通过pg\_hba.conf文件中指定的认证方法。检查你提供的口令，或者如果错误消息提到了Kerberos或ident认证类型，检查那些软件。

FATAL:user "andym" does not exist

指示的数据库用户没有被找到。

FATAL:database "testdb" does not exist

试图连接的数据库不存在。请注意如果没有声明数据库名，默认会用数据库用户名作为数据库名。服务器日志包含比报告给客户端的更多的有关认证失败的信息。必要时请检查服务器日志。

## 客户端访问控制黑白名单

瀚高数据库通过使用pg\_hba.conf文件管理客户端对于服务器的访问权限。文件中实现了对连接方式、连接数据库、连接用户、连接的主机IP、认证方式的限制。pg\_hba.conf作为基础限制，在一些实际应用场景中仍无法满足需求。所以我们新增高级连接访问控制功能，实现对客户端MAC地址和用户访问时间段的限制，对于不符合限制规则的的用户MAC和访问时间段，数据库将不允许登录。

数据库安全员或超级用户有权限对要登录数据库的用户及MAC地址或访问时间段进行设置，对于处于黑名单中的用户及MAC，数据库将不允许登录。本模块通过插件的方式实现连接访问控制。这种方式更为灵活，当数据库的实用场景需要进行连接访问控制时，打开插件开关。而不需要该功能时，关闭插件开关即可。

客户端访问控制黑白名单为V9.0.5版本新增功能。

### 客户端访问控制黑白名单插件

\[为使该模块生效，需要通过配置文件postgresql.conf  
中的shared\_preload\_libraries  
进行加载，给shared\_preload\_libraries参数追加conn\_restrict，随后重启服务器。然后登录数据库管理员创建扩展：\]{.mark}

```
highgo=# \c highgo highgo

hgdb-client-V9.0.5

您现在已经连接到数据库 "highgo",用户 "highgo".

highgo=# create extension conn_restrict ;

CREATE EXTENSION
```

### 插件开关

\[新增GUC参数conn\_restrict.enable作为连接访问控制扩展的开关，仅数据库安全员或超级用户可以修改，本参数重启数据库生效。开关开启后，支持对客户端MAC地址和用户连接时间段的访问限制，时间段包括具体时间段和规则时间段：\]{.mark}

\[具体时间段：如 2025 年 1 月 1 日 8：30 至 2025 年 7 月 1 日  
17：00；\]{.mark}

\[规则时间段：如每天 8：30 至 17：00；\]{.mark}

### 创建访问控制规则

\[通过系统函数来添加连接访问控制规则：\]{.mark}

```
hg_security.add_rules(

filter_type int,

rule_user text,

include_mac text,

exclude_mac text,

include_time text,

exclude_time text

)
```

参数说明

- filter\_type
	0表示白名单，1表示黑名单。
- rule\_user

被限制的用户，同一个用户只允许添加一条规则，未在规则中配置的用户，表示当前不做限制。

- include\_mac

filter\_type =0白名单时，表示不受限的MAC地址；

filter\_type =1黑名单时，表示受限的MAC地址。

多个MAC地址用逗号分隔。该参数允许为null。

- exclude\_mac
	该参数表示与include\_mac含义相反，用法相同。
	该参数允许为null。
	当exclude\_mac与include\_mac存在重复值时，等效于将重复值从include\_mac中剔除。
	例如：include\_mac为a、b、c三个值，exclude\_mac为c、d、e三个值，在白名单下等效于以a、b为白名单，其它MAC地址禁止访问；在黑名单下等效于以a、b为黑名单，其它mac地址允许访问。
- include\_time
	filter\_type =0白名单时，表示允许访问的时间段；
	filter\_type =1黑名单时，表示不允许访问的时间段。
	时间段支持标准PG时间类型设置如yyyy-MM-dd HH:mm:ss，因为具体时间段和规则时间段的设置不同，也存在省略年月日或者时分秒的情况。该参数允许为null。
- exclude\_time
	该参数表示与include\_time含义相反。该参数允许为null。
	当exclude\_time与include\_time存在重复时段时，等效于将重复时段从include\_time中剔除。
	例如：include\_time为6点至9点，exclude\_time为7至10点，在白名单下等效于以6至7点为白名单，其它时间禁止访问；在黑名单下等效于以6至7点为黑名单，其它时间允许访问。
	注意：include\_mac、exclude\_mac、include\_time、exclude\_time  
	不允许同时为null。

### 删除访问控制规则

通过系统函数来删除连接访问控制规则：

```
hg_security.remove_rules(rule_user text)
```

参数说明

- rule\_user

> 取消限制的用户，可通过指定rule\_user删除该用户的访问控制规则。

### 规则查询

新增视图hg\_security.show\_rules，可通过视图查询当前连接访问控制规则，数据库安全员和超级用户有查看权限。

使用示例：

用户usera允许访问的时间段为8:00-12:00，13：-17:00，禁止访问的时间段为12:00-13:00；禁止客户端MAC=F4:D1:08:4B:A9:C9、F4:D1:08:4B:A9:C8连接访问。

手动修改配置文件，在shared\_preload\_libraries参数后追加conn\_restrict，重启数据库生效。

数据库管理员用户登录创建扩展

```
highgo=# \c highgo highgo

hgdb-client-V9.0.5

您现在已经连接到数据库 "highgo",用户 "highgo".

highgo=# create extension conn_restrict ;

CREATE EXTENSION
```

打开三权分立模块的开关

```
highgo=# alter system set se_feature.mode=on;
```

ALTER SYSTEM

```
highgo=# select pg_reload_conf();
```

切换数据库安全员登录，打开插件开关并生效

```
highgo=# \c - syssso
```

用户 syssso 的口令：

```
hgdb-client-V9.0.5

您现在已经连接到数据库 "highgo",用户 "syssso".

highgo=> alter system set conn_restrict.enable=on;

ALTER SYSTEM

highgo=> select pg_reload_conf();

pg_reload_conf

---------------------

t

(1 行记录)
```

创建访问控制规则

```
highgo=> select * from
hg_security.add_rules(0,'u1',null,'F4:D1:08:4B:A9:C9,F4:D1:08:4B:A9:C8','8:00:00
to 17:00:00','12:00:00 to 13:00:00');

add_rules

---------------------

(1 行记录)

highgo=> select * from
hg_security.add_rules(1,'u2','F4:D1:08:4B:A9:C9, F4:D1:08:4B:A9:C8',
null, '12:00:00 to 13:00:00', '8:00:00 to 17:00:00');

add_rules

---------------------

(1 行记录)
```

用户usera无MAC限制，允许访问的时间段为2023年6月1日至2024年12月1日，其他时间不允许访问。

创建访问控制规则

```
highgo=> select * from
hg_security.add_rules(0,'u3',null,null,'2023-06-01 00:00:00 to
2026-12-01 23:59:59',null);

add_rules

---------------------

(1 行记录)

highgo=> select * from
hg_security.add_rules(0,'u4',null,null,'2023-06-01 to
2026-12-01',null);

add_rules

---------------------

(1 行记录)
```

查询规则视图

```
highgo=> select * from hg_security.show_rules ;
```

删除访问控制规则

```
highgo=> select * from hg_security.remove_rules('u4');
```