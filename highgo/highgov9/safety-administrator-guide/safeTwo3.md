---
title: "客户端认证"
book: "管理员指南"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/safety/safeTwo3.html"
tags:
  - highgo
  - highgo-v9
  - safety-administrator-guide
---

## 客户端认证

## pg\_hba.conf文件

客户端认证是由一个配置文件（通常名为pg\_hba.conf并被存放在数据库集簇目录中，HBA表示基于主机的认证）控制。在initdb初始化数据目录时，会在数据目录下生成一个默认的pg\_hba.conf文件。我们也可以把认证配置文件放在其它地方。

pg\_hba.conf文件的常用格式是一组记录，每行一条。空白行将被忽略， #注释字符后面的任何文本也被忽略。记录不能跨行。一条记录由若干用空格 或制表符分隔的域组成。如果域值用双引号包围，那么它可以包含空。在数据库、用户或地址域中引用一个关键字（例如all或replication）将使该词失去其特殊含义，将会只匹配一个有该名字的数据库、用户或主机。

每条记录指定一种连接类型、一个客户端 IP 地址范围（如果和连接类型相关）、一个数据库名、一个用户名以及对匹配这些参数的连接所使用的认证方法。第一条匹配连接类型、客户端地址、连接请求的数据库和用户名的记录将被用于执行认证。这个过程没有”落空”或者”后备”的说法：如果选择了一条记录而且认证失败，那么将不再考虑后面的记录。如果没有匹配的记录，那么访问将被拒绝。

记录可以是下面七种格式之一：

local database user auth-method \[auth-options\]

host database user address auth-method \[auth-options\]

hostssl database user address auth-method \[auth-options\]

hostnossl database user address auth-method \[auth-options\]

host database user IP-address IP-mask auth-method \[auth-options\]

hostssl database user IP-address IP-mask auth-method \[auth-options\]

hostnossl database user IP-address IP-mask auth-method \[auth-options\]

hostgssenc database user IP-address IP-mask auth-method \[auth-options\]

hostnogssenc database user IP-address IP-mask auth-method \[auth-options\]

各个域的含义如下：

•local

这条记录匹配企图使用 Unix 域套接字的连接。如果没有这种类型的记录，就不允许Unix 域套接字连接。

•host

这条记录匹配企图使用 TCP/IP 建立的连接。host记录匹配SSL和非SSL的连接尝试，此外还有GSSAPI 加密的或non-GSSAPI 加密的连接尝试。

| **注意：** |
| --- |
| 除非服务器带着合适的listen\_addresses配置参数值启动，否则将不可能进行远程的 TCP/IP 连接，因为默认的行为是只监听在本地环回地址localhost上的 TCP/IP 连接。 |

•hostssl

这条记录匹配企图使用 TCP/IP 建立的连接，但必须是使用SSL加密的连接。

要使用这个选项，编译服务器的时候必须打开SSL支持。此外，在服务器启动的时候必须通过设置ssl配置参数打开SSL。否则，hostssl记录会被忽略，并且会记录一个警告说它无法匹配任何连接。

•hostnossl

这条记录的行为与hostssl相反；它只匹配那些在TCP/IP上不使用SSL的连接企图。

•hostgssenc

这条记录匹配企图使用TCP/IP建立的连接，但仅当使用GSSAPI加密建立连接时。

要使用这个选项，必须使用GSSAPI支持来构建服务器。否则，该hostgssenc记录将被忽略，除了记录一条警告，指出该记录无法匹配任何连接。

注意使用GSSAPI加密时能够支持的身份认证方法只包括gss,reject和trust.

•hostnogssenc

这个记录类型具有与hostgssenc相反的表现; 它仅匹配通过不使用GSSAPI加密的TCP/IP进行的连接尝试。

•database

指定记录所匹配的数据库名称。值all指定该记录匹配所有数据库。值 sameuser指定如果被请求的数据库和请求的用户同名，则匹配。值samerole指定请求的用户必须是一个与数据库同名的角色中的成员（samegroup是一个已经废弃了，但目前仍然被接受的samerole同义词）。对于一个用于samerole目的的角色，超级用户不会被考虑为其中的成员，除非它们是该角色的显式成员（直接或间接），而不是由于超级用户的原因。值replication指定如果一个物理复制连接被请求则该记录匹配（注意复制连接不指定任何特定的数据库）。在其它情况里，这就是一个特定的瀚高数据库名字。可以通过用逗号分隔的方法指定多个数据库，也可以通过在文件名前面放@来指定一个包含数据库名的文件。

•user

指定这条记录匹配哪些数据库用户名。值all指定它匹配所有用户。否则，它要么是一个特定数据库用户的名字或者是一个有前导+的组名称（回想一下，在瀚高数据库里，用户和组没有真正的区别，+实际表示”匹配这个角色的任何直接或间接成员角色”，而没有+记号的名字只匹配指定的角色）。出于这个目的，如果超级用户显式的是一个角色的成员（直接或间接），那么超级用户将只被认为是该角色的一个成员而不是作为一个超级用户。多个用户名可以通过用逗号分隔的方法提供。一个包含用户名的文件可以通过在文件名前面加上@来指定。

•address

指定这个记录匹配的客户端机器地址。这个域可以包含一个主机名、一个 IP地址范围或下文提到的特殊关键字之一。

一个IP地址范围以该范围的开始地址的标准数字记号指定，然后是一个斜线（/）和一个CIDR掩码长度。掩码长度表示客户端IP地址必须匹配的高位位数。在给出的IP地址中，这个长度的右边的位必须为零。在IP地址、/和CIDR掩码长度之间不能有空白。

以这种方法指定一个IPv4地址范围的典型例子是：172.20.143.89/32用于一个主机，172.20.143.0/24用于一个小型网络，10.6.0.0/16用于一个大型网络。一个单主机的IPv6地址范围看起来像这样：::1/128（IPv6 回环地址），一个小型网络的IPv6地址范围则类似于：fe80::7a31:c1ff:0000:0000/96。0.0.0.0/0表示所有IPv4地址，并且::0/0表示所有IPv6地址。要指定一个单一主机，IPv4用一个长度为32的CIDR掩码或者IPv6用长度为128的CIDR掩码。在一个网络地址中，不要省略结尾的零。

一个以IPv4格式给出的项将只匹配IPv4连接并且一个以IPv6格式给出的项将只匹配IPv6连接，即使对应的地址在IPv4-in-IPv6范围内。请注意如果系统的C库不支持IPv6地址，那么IPv6格式中的项将被拒绝。

你也可以写all来匹配任何IP地址、写samehost来匹配任何本服务器自身的IP地址或者写samenet来匹配本服务器直接连接到的任意子网的任意地址。

若果指定了一个主机名（任何除IP地址单位或特殊关键字之外的都被作为主机名处理），该名称会与客户端的IP地址的反向名字解析（例如使用DNS时的反向DNS查找）结果进行比较。主机名比较是大小写敏感的。如果匹配上，那么将在主机名上执行一次正向名字解析（例如正向DNS查找）来检查它解析到的任何地址是否等于客户端的IP地址。如果两个方向都匹配，则该项被认为匹配（pg\_hba.conf中使用的主机名应该是客户端IP地址的地址到名字解析返回的结果，否则该行将不会匹配。某些主机名数据库允许将一个IP地址关联多个主机名，但是当被要求解析一个IP地址时，操作系统将只返回一个主机名）。

一个以点号（.）开始的主机名声明匹配实际主机名的后缀。因此.example.com将匹配foo.example.com（不仅仅匹配example.com）。当主机名在pg\_hba.conf中被指定时，应确保名称解析速度相当快。建立一个类似nscd的本地名字解析缓存是一种不错的选择。另外，你可能希望启用配置参数log\_hostname来在日志中查看客户端的主机名而不是IP地址。

这些字段不适用于local记录。

| 注意： |
| --- |
| 用户有时会想知道为什么用这种看似复杂的方式来处理主机名，并具有两个名称解析，包括对客户端IP地址的反向查找。如果未设置客户端的反向DNS条目或产生某些不良的主机名，则会使该功能的使用复杂化。这样做主要是为了提高效率：通过这种方式，连接尝试最多需要两次解析器查找，一次反向查找和一次正向查找。如果有一个解析器对于该地址有问题，这仅仅是客户端的问题。一种假想的替代实现是只做前向查找，这种方法不得不在每一次连接尝试期间解析pg\_hba.conf中提到的每一个主机名。如果列出了很多名称，这就会很慢。并且如果主机名之一有解析器问题，它会变成所有人的问题。同样，为了实现后缀匹配功能，必须进行反向查找，因为需要知道实际的客户端主机名，以便将其与模式进行匹配。 |

•IP-address

IP-mask

这两个域可以被用作IP-address/mask-length记号法的替代方案。和指定掩码长度不同，实际的掩码被指定在一个单独的列中。例如255.0.0.0表示 IPv4 CIDR 掩码长度8，而255.255.255.255表示 CIDR 掩码长度32。

这些域不适用于local记录。

•auth-method

指定连接与该记录匹配时要使用的身份验证方法。这里总结了可能的选择。

（1）reject

无条件地拒绝连接。这有助于从一个组中”过滤出”特定主机，例如一个reject行可以阻塞一个特定的主机连接，而后面一行允许一个特定网络中的其余主机进行连接。

（2）scram-sha-256

执行SCRAM-SHA-256认证来验证用户的口令。

（3）md5

执行MD5认证来验证用户的口令。

（4）password

要求客户端提供一个未加密的口令进行认证。因为口令是以明文形式在网络上发送的，所以我们不应该在不可信的网络上使用这种方式。

（5）gss

用GSSAPI认证用户。只对TCP/IP连接可用。它可以与GSSAPI加密一起结合使用。

（6）sspi

用SSPI来认证用户。

（7）ident

通过联系客户端的ident服务器获取客户端的操作系统名，并且检查它是否匹配被请求的数据库用户名。Ident认证只能在TCIP/IP连接上使用。当为本地连接指定这种认证方式时，将用peer认证来替代。

（8）peer

从操作系统获得客户端的操作系统用户，并且检查它是否匹配被请求的数据库用户。

（9）ldap

使用LDAP服务器认证。

（10）radius

用RADIUS服务器认证。

（11）cert

使用SSL客户端证书认证。

（12）pam

使用操作系统提供的可插入认证模块服务（PAM）认证。

（13）bsd

使用由操作系统提供的BSD认证服务进行认证。

•auth-options

在auth-method域的后面，可以是形如name=value的域，它们指定认证方法的选项。

除了下文列出的与方法相关的选项之外，还有一个与方法无关的认证选项clientcert，它可以在任何hostssl记录中指定。这个选项可以被设置到verify-ca或verifyfull. 这两个选项都需要客户端提供有效的(受信任的)SSL证书，并且verify-full额外强制证书中的cn(通用名称)匹配用户名或适用的映射。这种行为类似于cert认证方法，但是允许客户端证书的验证与任何支持hostssl登记的认证方法相搭配。

用@结构包括的文件被读作一个名字列表，它们可以用空白或者逗号分隔。注释用#引入，就像在pg\_hba.conf中那样，并且允许嵌套@结构。除非跟在@后面的文件名是一个绝对路径，文件名都被认为是相对于包含引用文件的目录。 因为每一次连接尝试都会顺序地检查pg\_hba.conf记录，所以这些记录的顺序是非常关键的。通常，靠前的记录有比较严的连接匹配参数和比较弱的认证方法，而靠后的记录有比较松的匹配参数和比较强的认证方法。

在启动以及主服务器进程收到SIGHUP信号时，pg\_hba.conf文件会被读取。如果你在运行的系统上编辑了该文件，你将需要通知 postmaster（使用pg\_ctl reload，调用SQL函数pg\_reload\_conf(),或使用kill -HUP）使其重新读取该文件。

系统视图pg\_hba\_file\_rules有助于预先测试对pg\_hba.conf文件的更改，或者如果文件加载未达到预期效果，则有助于诊断问题。该视图中带有非空error域的行就表示该文件对应行中存在问题。

| **提示：** |
| --- |
| 要连接到一个特定数据库，一个用户必须不仅要通过pg\_hba.conf检查，还必须要有该数据库上的CONNECT权限。如果你希望限制哪些用户能够连接到哪些数据库，授予/撤销CONNECT权限通常比在pg\_hba.conf项中设置规则简单。 |

pg\_hba.conf条目示例：

1\. 如果用户的口令被正确提供，允许本地系统上的任何用户通过Unix域套接字以任意数据库用户名连接到任意数据库（本地连接的默认值）。

#TYPE DATABASE USER ADDRESS METHOD

local all all md5

2.相同的规则，但是使用本地环回TCP/IP连接。

#TYPE DATABASE USER ADDRESS METHOD

host all all 127.0.0.1/32 md5

3.和前一行相同，但是使用了一个独立的掩码列

#TYPE DATABASE USER IP-ADDRESS IP-MASK METHOD

host all all 127.0.0.1 255.255.255.255 md5

4.IPv6上相同的规则

#TYPE DATABASE USER ADDRESS METHOD

host all all::1/128 md5

5.使用主机名的相同规则（通常同时覆盖IPv4和IPv6）。

#TYPE DATABASE USER ADDRESS METHOD

host all all localhost md5

6.允许来自任意具有IP地址192.168.93.x 的主机上任意用户连接与ident为之报告的数据库 "highgo"。

#TYPE DATABASE USER ADDRESS METHOD

host highgo all 192.168.93.0/24 ident

7.如果用户的口令被正确提供，允许来自主机 192.168.12.10 的任意用户连接到数据库 "highgo"。

#TYPE DATABASE USER ADDRESS METHOD

host highgo all 192.168.12.10/32 scram-sha-256

8.如果用户的口令被正确提供，允许example.com中主机上的任意用户连接到任意数据库。大部分用户要求SCRAM认证，但是用户'mike'是个例外，他使用的是不支持SCRAM认证的旧客户端。

#TYPE DATABASE USER ADDRESS METHOD

host all mike.example.com md5

host all all.example.com scram-sha-256

9.如果没有前面的 "host" 行，这三行将拒绝所有来自192.168.54.1的连接（因为那些项将首先被匹配），但是允许来自互联网其他任何地方的GSSAPI-encrypted连接。零掩码导致主机IP地址中的所有位都不会被考虑，因此它匹配任意主机。未加密的GSSAPI连接是被允许的,但只能来自192.168.12.10.

#TYPE DATABASE USER ADDRESS METHOD

host all all 192.168.54.1/32 reject

hostgssenc all all 0.0.0.0/0 gss

host all all 192.168.12.10/32 gss

10\. 如果它们能够通过 ident检查，将允许来自192.168.x.x主机的用户连接到任意数据库。例如,假设ident说用户是 "bryanh" 并且他要求以瀚高数据库用户 "guest1" 连接，如果在 pg\_ident.conf 有一个映射"omicron" 的选项说 "bryanh" 被允许以 "guest1" 连接，则该连接将被允许。

#TYPE DATABASE USER ADDRESS METHOD

host all all 192.168.0.0/16 ident map=omicron

11.如果这些是本地连接的唯一三行，它们将允许本地用户只连接到它们自己的数据库（与其数据库用户名同名的数据库），不过管理员和角色 "support" 的成员除外（它们可以连接到所有数据库）。文件$PGDATA/admins 包含一个管理员名字的列表。在所有情况下都要求口令。

#TYPE DATABASE USER ADDRESS METHOD

local sameuser all md5

local all @admins md5

local all +support md5

上面的最后两行可以被整合为一行：

local all @admins,+support md5

数据库列也可以用列表和文件名：

local db1,db2,@demodbs all md5

## 用户名映射

当使用外部身份验证系统（例如Ident或GSSAPI）时，发起连接的操作系统用户的名称可能与要使用的数据库用户（角色）不同。在这种情况下，可以应用用户名映射将操作系统用户名映射到数据库用户。要使用用户名映射，在pg\_hba.conf的选项域指定map=map-name。此选项支持所有接收外部用户名的认证方法。由于不同的连接可能需要不同的映射，在pg\_hba.conf中的map-name参数中指定要被使用的映射名，以指示每个单独的连接使用哪个映射。

用户名映射定义在 ident 映射文件中，默认情况下它被命名为pg\_ident.conf并被存储在集簇的数据目录中。ident映射文件包含的行格式一般为：

map-name system-username database-username

以在pg\_hba.conf中同样的方式处理注释和空格。map-name是一个任意名称，它将被用于在pg\_hba.conf中引用该映射。其他两个域指定一个操作系统用户名和一个匹配的数据库用户名。相同的map-name可以被反复地用在同一个映射中指定多个用户映射。

对于一个给定操作系统用户可以对应多少个数据库用户没有限制，反之亦然。因此，一个映射中的项应该被看成意味着”这个操作系统用户被允许作为这个数据库用户连接”，而不是暗示它们等价。如果有任何映射项把从外部认证系统获得的用户名和用户要求的数据库用户名配对，该连接将被允许。

如果system-username域以一个斜线（/）开始，域的剩余部分被当做一个正则表达式。正则表达式可以包括一个单一的捕获，或圆括号子表达式，然后它可以在database-username域中以\\1（反斜线一）被引用。这允许在单个行中多个用户名的映射，这特别有助于简单的语法替换。例如，这些项：

mymap /^(.\*)@mydomain\\.com$ \\1

mymap /^(.\*)@otherdomain\\.com$ guest

将为用户移除以@mydomain.com结束的系统用户名的域部分，以及允许系统名以@otherdomain.com结束的任意用户作为guest登入。

| **提示：** |
| --- |
| 记住在默认情况下，一个正则表达式可以只匹配字符串的一部分。如上例所示，使用^和$来强制匹配整个系统用户名通常是明智的。 |

在启动以及主服务器进程收到SIGHUP信号时，pg\_ident.conf文件会被读取。如果你在运行的系统上编辑了该文件，你将需要通知 postmaster（使用pg\_ctl reload，调用SQL函数pg\_reload\_conf(), 或用kill -HUP）重新读取文件。

以下示例给出了一个可以联合pg\_hba.conf文件使用的pg\_ident.conf文件。在这个例子中，对于任何登入到192.168网络上的一台机器的用户，如果该用户没有操作系统用户名bryanh、ann或robert，则他不会被授予访问权限。只有当 Unix 用户robert尝试作为瀚高用户bob（而不是作为robert或其他人）连接时，他才被允许访问。ann只被允许作为ann连接。用户bryanh被允许以bryanh或者guest1连接。

示例：

\# MAPNAME SYSTEM-USERNAME PG-USERNAME

omicron bryanh bryanh

omicron ann ann

\# bob 在这些机器上有用户名 robert

omicron robert bob

\# bryanh 也可以作为 guest1 连接

omicron bryanh guest1

## 认证方法

瀚高数据库为认证用户提供不同的方法:

• Password authentication, 需要用户提供密码。

• GSSAPI authentication, 依靠GSSAPI兼容的安全库，常常用于访问认证服务器，例如：Kerberos或微软活动目录服务器。

• SSPI authentication, 类似于GSSAPI的协议。

• Ident authentication, 依靠客户机器上的”Identification Protocol”(RFC 1413)服务，(在本地Unix-socket连接,这个按对等认证处理)。

• Peer authentication, 依靠操作系统工具来识别本地连接另一端的进程。这种方法不支持远程连接。

• LDAP authentication, 依靠LDAP认证服务器.

• RADIUS authentication, 依靠RADIUS认证服务器.

• Certificate authentication, 需要SLL连接和通过SSL证书检查的认证用户。

• PAM authentication, 依靠PAM库(Pluggable Authentication Modules，可插拔认证模块)。

• BSD authentication, 依靠BSD认证框架(当前仅在OpenBSD上应用)。

对等身份验证通常适用于本地连接,信任认证在某些情况下也许是比较适合的。密码认证是远程连接的常见选择。所有其它的选项都需要某种外部安全基础架构(通常是认证服务器或颁发SSL证书的证书颁发机构。)，或用于某些特定平台。

以下各节将更详细地介绍这些身份认证方法。

### 口令认证

有几种基于口令的认证方法。这些方法的过程类似，区别在于用户口令如何被存放在服务器上以及客户端提供的口令如何被通过连接发送。

•scram-sha-256

它使用的是一种质询-响应的方案，可以防止在不可信连接上对口令的嗅探，并且支持在服务器上以一种加密哈希的方式存放口令，因此被认为是安全的。

•md5

方法md5使用一种自定义的安全性较低的质询-响应机制。它能防止口令嗅探并且防止口令在服务器上以明文存储，但是无法保护攻击者想办法从服务器上窃取了口令哈希的情况。此外，现在认为MD5哈希算法对于确定攻击已经不再安全。md5方法不能与db\_user\_namespace特性一起使用。

为了简化从md5方法到较新的SCRAM方法的转变，如果在pg\_hba.conf中指定了md5但是用户在服务器上的口令是为SCRAM加密的，则将自动选择基于SCRAM的认证。

•password

方法password以明文形式发送口令，因此它对于口令”嗅探”攻击很脆弱。如果可能应该尽量避免使用它。不过，如果连接被SSL加密保护着，那么可以安全地使用password（不过如果依靠SSL，SSL证书认证可能是更好的选择）。

瀚高数据库用户口令独立于操作系统用户口令。每个数据库用户的口令被存储在pg\_authid系统目录中。口令可以用SQL命令CREATE USER和ALTER ROLE管理，例如CREATE ROLE foo WITH LOGIN PASSWORD 'Heegh@123'。如果没有为一个用户设置口令，那么用户创建将会失败。

不同的基于口令的认证方法的可用性取决于用户的口令在服务器上是如何被加密（或者更准确地说是哈希）的。这由设置口令时的配置参数password\_encryption控制。如果口令使用scram-sha-256设置加密，那么它可以被用于认证方法scram-sha-256和password（但后一种情况中口令将以明文传输）。如上所述，在这种情况下，身份验证方法规范md5将自动切换为使用该scram-sha-256方法，因此它也将起作用。如果使用该md5设置对密码进行了加密，则该密码只能用于md5和password身份验证方法规范（同样，在后一种情况下，密码以纯文本格式传输）。要检查当前存储的密码哈希，请参见系统目录pg\_authid。

要把现有的安装从md5升级到scram-sha-256，可以在确保所有在用的客户端已经足以支持 SCRAM之后，在postgresql.conf中设置password\_encryption = 'scram-sha-256'，然后让所有用户设置新口令并且在pg\_hba.conf中将认证方法说明改为scram-sha-256。

### GSSAPI认证

GSSAPI是用于RFC 2743中定义的安全认证的一个行业标准协议。瀚高数据库根据RFC 1964支持带Kerberos认证的GSSAPI。GSSAPI为支持它的系统提供自动认证（单点登录）。认证本身是安全的，但通过数据库连接发送的数据将不被加密，除非使用SSL。瀚高数据库支持GSSAPI用于加密、认证层或仅用于认证。GSSAPI提供自动认证(single sign-on单点登录) 给支持该功能的系统。认证本身是安全的。如果使用了GSSAPI加密或SSL加密, 数据库连接发送的数据将被加密，否则将不加密。

构建瀚高数据库时必须启用GSSAPI支持。

当GSSAPI使用Kerberos时，它会使用格式servicename/hostname@realm的标准principal。瀚高数据库服务器将接受该服务器所使用的keytab中包括的任何principal，但是在从使用krbsrvname连接参数的客户端建立连接时要注意指定正确的principal细节。安装的默认值可以在编译时使用./configure --with-krb-srvnam=其他值修改。在大部分的环境中，这个参数从不需要被更改。某些Kerberos实现可能要求一个不同的服务名，例如 Microsoft Active Directory要求服务名是大写形式。

hostname是服务器计算机的标准主机名。服务principal的realm 是该服务器机器的首选realm。

客户端principal可以被通过pg\_ident.conf映射到不同的瀚高数据库用户名。例如highgousername@realm可能会被映射到highgousername。或者，你可以使用完整的username@realm作为瀚高数据库中的角色而无需任何映射。

瀚高数据库也支持一个参数把realm从principal中剥离。这种方法是为了向后兼容性，并且我们强烈反对使用它，因为这样就无法区分具有相同用户名却来自不同realm的不同用户了。要启用这种方法，可将include\_realm设置为0。对于简单的单realm安装，这样做并且设置krb\_realm参数（这会检查principal的realm是否正好匹配krb\_realm中的参数）仍然是安全的。但比起在pg\_ident.conf中指定一个显式映射来说，这种方法的能力较低。

确认你服务器的keytab文件是可以被瀚高数据库服务器帐户读取的（最好是只读的）。密钥文件的位置由配置参数krb\_server\_keyfile指定。默认是/usr/local/pgsql/etc/krb5.keytab（或者任何在编译的时候作为sysconfdir的目录）。出于安全原因，推荐对瀚高数据库服务器使用一个独立的keytab而不是开放系统keytab文件的权限。

keytab文件由Kerberos软件生成。下面是MIT兼容的Kerberos 5实现的例子：

kadmin% ank -randkey highgo/server.my.domain.org

kadmin% ktadd -k krb5.keytab highgo/server.my.domain.org

当连接到数据库时，确保你有一个匹配被请求数据库用户名的principal 的票据。例如对于数据库用户名fred，principal [fred@EXAMPLE.COM](mailto:fred@EXAMPLE.COM) 将能够连接。要也允许principal fred/ [users.example.com@EXAMPLE.COM](mailto:users.example.com@EXAMPLE.COM) ，可使用一个用户名映射。

GSSAPI支持以下配置选项：

•include\_realm

如果设置为0，在通过用户名映射之前，来自已认证用户principal的realm名称会被剥离掉。我们不鼓励这样做，这种方法主要是为了向后兼容性而存在的，因为它在多realm环境中是不安全的（除非也使用krb\_realm）。推荐用户让include\_realm设置为默认值（1）并且在pg\_ident.conf中提供一条显式的映射来把 principal 名称转换成瀚高用户名。

•map

允许在系统和数据库用户名之间的映射。对于一个GSSAPI/Kerberos原则，例如 [username@EXAMPLE.COM](mailto:username@EXAMPLE.COM) （或者更不常见的username/ [hostbased@EXAMPLE.COM](mailto:hostbased@EXAMPLE.COM) ），用于映射的用户名会是 [username@EXAMPLE.COM](mailto:username@EXAMPLE.COM) （或者 username/ [hostbased@EXAMPLE.COM](mailto:hostbased@EXAMPLE.COM) ，相应地），除非include\_realm已经被设置为0，在那种情况下username（或者username/hostbased）是映射时被视作系统用户名的东西。

•krb\_realm

设置realm为对用户principal名进行匹配的范围。如果这个参数被设置，只有那个realm 的用户将被接受。如果它没有被设置，任何realm的用户都能连接，服从任何已完成的用户名映射。

### SSPI认证

SSPI用于通过单点登录进行安全身份验证。瀚高数据库将在negotiate模式下使用SSPI，在可能的情况下将使用Kerberos，在其他情况下将自动退回到NTLM。在Linux平台上，当GSSAPI可用时，SSPI身份验证才起作用。

当使用Kerberos认证时，SSPI和GSSAPI的工作方式相同。

SSPI支持以下配置选项：

•include\_realm

如果设置为0，在通过用户名映射之前，来自已认证用户principal的 realm名称会被剥离掉。我们不鼓励这样做，这种方法主要是为了向后兼容性而存在的，因为它在多realm环境中是不安全的（除非也使用krb\_realm）。推荐用户让include\_realm设置为默认值（1）并且在pg\_ident.conf中提供一条显式的映射来把principal名称转换成瀚高数据用户名。

•compat\_realm

如果被设置为1，该域的SAM兼容名称（也被称为NetBIOS名称）被用于include\_realm选项。这是默认值。如果被设置为0，会使用来自Kerberos用户主名的真实realm名称。

不要禁用这个选项，除非你的服务器运行在一个域账号（这包括一个域成员系统上的虚拟服务账号）下并且所有通过 SSPI 认证的所有客户端也在使用域账号，否则认证将会失败。

•upn\_username

如果这个选项和compat\_realm一起被启用，来自 Kerberos UPN 的用户名会被用于认证。如果它被禁用（默认），会使用SAM兼容的用户名。默认情况下，对于新用户账号这两种名称是一样的。

注意如果没有显式指定用户名，libpq会使用SAM兼容的名称。如果你使用的是libpq或者基于它的驱动，你应该让这个选项保持禁用或者在连接字符串中显式指定用户名。

•map

允许在系统和数据库用户名之间的映射。对于一个 GSSAPI/Kerberos 原则，例如 [username@EXAMPLE.COM](mailto:username@EXAMPLE.COM) （或者更不常见的username/ [hostbased@EXAMPLE.COM](mailto:hostbased@EXAMPLE.COM) ），用于映射的用户名会是 [username@EXAMPLE.COM](mailto:username@EXAMPLE.COM) （或者 username/ [hostbased@EXAMPLE.COM](mailto:hostbased@EXAMPLE.COM) ，相应地），除非include\_realm已经被设置为0，在那种情况下username（或者username/hostbased）是映射时被视作系统用户名的东西。

•krb\_realm

设置领域为对用户principal名进行匹配的范围。如果这个参数被设置，只有那个领域的用户将被接受。如果它没有被设置，任何领域的用户都能连接，服从任何已完成的用户名映射。

### Ident认证

ident认证方法通过从一个ident服务器获得客户端的操作系统用户名并且用它作为被允许的数据库用户名（和可选的用户名映射）来工作。它只在 TCP/IP连接上支持。

| **注意：** |
| --- |
| 当为一个本地（非TCP/IP）连接指定ident时，将实际使用peer认证。 |

ident支持以下配置选项：

•map

允许系统和数据库用户名之间的映射。。

“Identification Protocol（标识协议）”在RFC 1413中描述。实际上每个类Unix操作系统都带着一个默认监听TCP 113端口的ident服务器。ident服务器的基本功能是回答类似这样的问题：”哪个用户从你的端口X发起了连接并且连到了我的端口Y？”。因为当一个物理连接被建立后，瀚高数据库既知道X也知道Y，所以它可以询问尝试连接的客户端主机上的ident服务器并且在理论上可以判断任意给定连接的操作系统用户。

这个过程的缺点是它依赖于客户端的完整性：如果客户端机器不可信或者被攻破，攻击者可能在113端口上运行任何程序并且返回他们选择的任何用户。因此这种认证方法只适用于封闭的网络，这样的网络中的每台客户端机器都处于严密的控制下并且数据库和操作系统管理员操作时可以方便地联系。换句话说，你必须信任运行ident服务器的机器。注意这样的警告：

The Identification Protocol is not intended as an authorization or access control protocol.

\--RFC 1413

有些ident服务器有一个非标准的选项，它导致返回的用户名是被加密的，使用的是只有原机器管理员知道的一个密钥。当与瀚高数据库配合使用 ident服务器时，一定不要使用这个选项，因为瀚高数据库没有任何方法对返回的字符串进行解密以获取实际的用户名。

### Peer认证

Peer认证方法通过从内核获得客户端的操作系统用户名并把它用作被允许的数据库用户名（和可选的用户名映射）来工作。这种方法只在本地连接上支持。

peer支持以下配置选项：

•map

允许在系统和数据库用户名之间的映射。

对等身份验证仅在提供getpeereid()功能，SO\_PEERCRED套接字参数或类似机制的操作系统上可用。当前包括Linux，大多数版本的BSD（包括macOS）和Solaris。

### LDAP认证

这种认证方法操作起来类似于password，只不过它使用LDAP作为密码验证方法。LDAP只被用于验证用户名/口令对。因此，在使用LDAP进行认证之前，用户必须已经存在于数据库中。

LDAP认证可以在两种模式下操作。在第一种模式中（我们将称之为简单绑定模式），服务器将绑定到构造成prefix username suffix的可区分名称。通常，prefix参数被用于指定cn=或者一个活动目录环境中的DOMAIN\\。suffix被用来指定非活动目录环境中的DN的剩余部分。

在第二种模式中（我们将称之为搜索与绑定模式），服务器首先用一个固定的用户名和密码（用ldapbinddn和ldapbindpasswd指定）绑定到LDAP目录，并为试图登入该数据库的用户执行一次搜索。如果没有配置用户名和密码，将尝试一次匿名绑定到目录。搜索将在位于ldapbasedn的子树上被执行，并将尝试做一次ldapsearchattribute中指定属性的精确匹配。一旦在这次搜索中找到用户，服务器断开并且作为这个用户重新绑定到目录，使用由客户端指定的口令来验证登录是正确的。这种模式与在其他软件中的LDAP认证所使用的相同，例如Apache mod\_authnz\_ldap和pam\_ldap。这种方法允许位于目录中用户对象的更大灵活性，但是会导致建立两个到LDAP服务器的独立连接。

下列配置选项被用于两种模式：

•ldapserver

要连接的LDAP服务器的名称或IP地址。可以指定多个服务器，用空格分隔。

•ldapport

要连接的LDAP服务器的端口号。如果没有指定端口，LDAP库的默认端口设置将被使用。ldapscheme设置为ldaps可以使用LDAPS。这是一种非标准的在SSL之上使用LDAP的方法，在有一些LDAP服务器实现上可以支持。其他选择还可以参考ldaptls选项。

•ldaptls

设置为1以使瀚高数据库和LDAP服务器之间的连接使用TLS加密。这会按照RFC 4163使用StartTLS操作。其他选择还可以参考ldapscheme选项。

注意使用ldapscheme或ldaptls仅会加密瀚高数据库服务器和LDAP服务器之间的通信。瀚高数据库服务器和瀚高数据库客户端之间的连接仍是未加密的，除非也在其上使用SSL。

下列选项只被用于简单绑定模式：

•ldapprefix

当做简单绑定认证时，前置到用户名形成要用于绑定的DN的字符串。

•ldapsuffix

当做简单绑定认证时，前置到用户名形成要用于绑定的DN的字符串。

下列选项只被用于搜索与绑定模式：

•ldapbasedn

当做搜索与绑定认证时，开始搜索用户的根DN。

•ldapbinddn

当做搜索与绑定认证时，用户要绑定到目录开始执行搜索的DN。

•ldapbindpasswd

当做搜索与绑定认证时，用户用于绑定到目录开始执行搜索的口令。

•ldapsearchattribute

当做搜索与绑定认证时，在搜索中用来与用户名匹配的属性。如果没有指定属性，将会使用uid属性。

•ldapsearchfilter

在做search+bind认证时使用的搜索过滤器。$username的出现将被替换为用户名。这允许比ldapsearchattribute更加灵活的搜索过滤器。

•ldapurl

一个RFC 4166 LDAP URL。这是一种用更紧凑和标准的形式书写某些其他LDAP选项的可选方法。格式是 ：ldap\[s\]://host\[:port\]/basedn\[?\[attribute\]\[?\[scope\]\[?\[filter\]\]\]\]

scope必须是base、one、sub之一，通常是最后一个（默认是base，但它在这个应用中通常没啥用）。attribute可以指定一个属性，在这种情况中它被用作ldapsearchattribute的一个值。如果attribute为空，那么filter可以被用作ldapsearchfilter的一个值。

URL模式ldaps选择LDAPS方法来在SSL上建立LDAP连接，等效于使用ldapscheme=ldaps。要使用StartTLS操作加密LDAP连接，可以用普通的URL模式ldap并且在ldapurl之外指定ldaptls选项。

对于非匿名绑定，ldapbinddn和ldapbindpasswd必须被指定为独立选项。

LDAP URLs当前只支持OpenLDAP。

将简单绑定的选项中混合用于搜索与绑定的选项是一种错误。

在使用search+bind模式时，可以用ldapsearchattribute指定的单个属性执行搜索，或者使用ldapsearchfilter指定的自定义搜索过滤器执行搜索。指定ldapsearchattribute=foo等效于指定ldapsearchfilter="(foo=$username)"。如果两个选项都没有被指定，则默认为ldapsearchattribute=uid。

如果瀚高数据库与OpenLDAP一起编译为LDAP客户端库，ldapserver 设置可能被省略。在这种情况下，主机名和端口列表通过RFC 2782 DNS SRV记录来进行查询。查询名称\_ldap.\_tcp.DOMAIN，DOMAIN是从ldapbasedn中摘取的。

这里是一个简单绑定 LDAP 配置的例子：

host... ldap ldapserver=ldap.example.net ldapprefix="cn=" ldapsuffix=", dc=example, dc=net"

当请求一个作为数据库用户someuser到数据库服务器的连接时，瀚高数据库将尝试使用cn=someuser, dc=example, dc=net和客户端提供的口令来绑定到LDAP服务器。如果那个连接成功，将被授予数据库访问。

这里是一个搜索与绑定配置的例子：

host... ldap ldapserver=ldap.example.net ldapbasedn="dc=example, dc=net" ldapsearchattribute=uid

当请求一个作为数据库用户someuser到数据库服务器的连接时，瀚高数据库将尝试匿名绑定（因为没有指定ldapbinddn）到LDAP服务器，在指定的基础DN 下执行一次对于(uid=someuser)的搜索。如果找到一个项，则它将尝试使用找到的信息和客户端提供的口令进行绑定。如果第二个连接成功，将被授予数据库访问。

这里是被写成一个URL的相同搜索与绑定配置：

host... ldap ldapurl="ldap://ldap.example.net/dc=example,dc=net?uid?sub"

一些支持根据LDAP认证的其他软件使用相同的URL格式，因此很容易共享该配置。

这里是一个search+bind配置的例子，它使用ldapsearchfilter而不是ldapsearchattribute来允许用用户ID或电子邮件地址进行认证：

host... ldap ldapserver=ldap.example.net ldapbasedn="dc=example, dc=net" ldapsearchfilter="(|(uid=$username)(mail=$username))"

这是一个search+bind配置的例子，它使用DNS SRV discovery来查找域名example.net的LDAP服务的主机名和端口。

host... ldap ldapbasedn="dc=example,dc=net"

| **提示：** |
| --- |
| 如例子中所示，由于LDAP通常使用逗号和空格来分割一个DN的不同部分，在配置LDAP选项时通常有必要使用双引号包围的参数值。 |

### RADIUS认证

这种认证方法的操作类似于password，不过它使用RADIUS作为密码验证方式。RADIUS只被用于验证用户名/密码对。因此，在RADIUS能被用于认证之前，用户必须已经存在于数据库中。

当使用RADIUS认证时，一个访问请求消息将被发送到配置好的RADIUS服务器。这一请求将是Authenticate Only类型，并且包含参数user name、password（加密的）和NAS Identifier。该请求将使用一个与服务器共享的密钥加密。RADIUS服务器将对这个请求响应Access Accept或者Access Reject。不支持RADIUS accounting。

可以指定多个RADIUS服务器，这种情况下将会依次尝试它们。如果从一台服务器接收到否定响应，则认证失败。如果没有接收到响应，则将会尝试列表中的下一台服务器。要指定多台服务器，可用双引号括住列表并用逗号将服务器名称分开。如果指定了多台服务器，其他RADIUS选项也可以用逗号分隔的列表给出，用来为每台服务器应用个别的值。它们也可以指定为单个值，这种情况下该值将被应用到所有的服务器。

RADIUS支持下列配置项：

•radiusservers

连接到RADIUS服务器的DNS名称或IP地址。此参数是必需的。

•radiussecrets

和RADIUS服务器秘密交谈时会用到共享密钥。这在瀚高数据库和RADIUS 服务器之间必须有完全相同的值。我们推荐用一个至少16个字符的字符串。这个参数是必需的。

| **注意：** |
| --- |
| 如果瀚高数据库编译为支持OpenSSL，所用的加密向量将只是强密码。在其他情况下，到RADIUS服务器的传输应该被视为被混淆的、不安全的。如有必要，应采用外部安全措施。 |

•radiusports

连接RADIUS服务器的端口号。如果没有指定端口，则使用默认RADIUS端口1812。

•radiusidentifiers

在RADIUS请求中字符串被用作NAS Identifier。这个参数可以被用于识别用户尝试连接哪些数据库集群，可以被用于RADIUS服务器上的策略匹配。如果没有指定标识符，默认使用highgo。

如果RADIUS参数值中需要有逗号或者空格，可以通过双引号括住该值来完成，但这样做是比较繁琐的因为需要两层双引号。将空格放到RADIUS秘密字符串的一个示例为：

host... radius radiusservers="server1,server2" radiussecrets="""secret one"",""secret two"""

### 证书认证

这种认证方法使用SSL客户端证书执行认证。因此，它只适用于SSL连接。当使用这种认证方法时，服务器将要求客户端提供一个有效的、可信的证书。不会有密码提示将被发送到客户端。证书的cn（通用名）属性将与被请求的数据库用户名进行比较，并且如果匹配将允许登录。用户名映射可以被用来允许cn与数据库用户名不同。

SSL证书认证支持以下配置项：

•map

允许在系统和数据库用户名之间的映射。

在一条指定证书认证的pg\_hba.conf记录中，认证选项clientcert被假定为verify-ca或verify-full，并且它不能被关掉，因为在这种方法中客户端证书是必需的。cert方法增加到基本clientcert证书有效性测试是一个cn属性匹配数据库用户名的检查。

### PAM认证

这种认证方法操作起来类似password，只不过它使用PAM（插入式验证模块）作为认证机制。PAM只被用于验证用户名/口令对并且可以有选择地验证已连接的远程主机名或IP地址。因此，在使用PAM进行认证之前，用户必须已经存在于数据库中。

PAM支持的配置选项：

•pamservice

PAM服务名称。

•pam\_use\_hostname

判断是否通过PAM\_RHOST项把远程IP地址或者主机名提供给PAM模块。默认情况下会使用IP地址。把这个选项设置为1可以使用解析过的主机名。主机名解析可能导致登录延迟（大部分的PAM配置不使用这些信息，因此只有使用为利用这种信息而特别创建的PAM配置时才需要考虑这个设置）。

### BSD认证

这种认证方法操作起来类似于password，不过它使用BSD认证来验证口令。BSD认证只被用来验证用户名/口令对。因此，在BSD认证可以被用于认证之前，用户的角色必须已经存在于数据库中。BSD认证框架当前只在OpenBSD上可用。

瀚高数据库中的BSD认证使用auth-postgresql登录类型，如果login.conf中定义了瀚高数据库登录分类，就会用它来认证。默认情况下这种登录分类不存在，瀚高数据库将使用默认的登录分类。

## 认证问题

认证失败以及相关的问题通常由类似下面的错误消息显示：

FATAL: no pg\_hba.conf entry for host "123.123.123.123", user "andym", database "testdb"

这条消息最可能出现的情况是你成功地联系了服务器，但它不愿意和你说话。就像消息本身所建议的，服务器拒绝了连接请求，因为它没有在其pg\_hba.conf配置文件里找到匹配项。

FATAL: password authentication failed for user "andym"

这样的消息表示你联系了服务器，并且它也愿意和你交谈，但是你必须通过pg\_hba.conf文件中指定的认证方法。检查你提供的口令，或者如果错误消息提到了 Kerberos 或 ident 认证类型，检查那些软件。

FATAL: user "andym" does not exist

指示的数据库用户没有被找到。

FATAL: database "testdb" does not exist

你试图连接的数据库不存在。请注意如果你没有声明数据库名，默认会用数据库用户名作为数据库名，这可能正确也可能不正确。

| **提示：** |
| --- |
| 服务器日志可能包含比报告给客户端的更多的有关认证失败的信息。如果你为失败的原因而困惑，那么请检查服务器日志。 |