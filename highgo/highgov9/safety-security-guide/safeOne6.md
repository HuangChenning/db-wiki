---
title: "数据传输安全"
book: "安全指南"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/safety/safeOne6.html"
tags:
  - highgo
  - highgo-v9
  - safety-security-guide
---

## 数据传输安全

瀚高数据库支持通过SSL协议实现客户端和服务器之间的安全数据传输，使得数据在传输过程中难以被窃听、篡改和伪造，从而增加数据传输安全性。这个特性要求在客户端和服务器端都安装OpenSSL。OpenSSL提供了必要的工具和协议，保障了数据传输安全。

## 基础配置

开启瀚高数据库通信加密，需要将参数文件postgresql.conf中的ssl设置为on，让瀚高数据库以支持ssl加密连接的方式启动。服务端在同一个TCP端口同时监听普通连接和SSL连接，并且将与任何正在连接的客户端协商是否使用SSL。默认情况下，客户端采用SSL加密连接。

要以SSL模式启动数据库服务，那么服务器证书和私钥的文件必须存在。默认情况下，这些文件应该分别被命名为server.crt和server.key并且被放在服务器的数据目录data中，但是可以通过配置参数ssl\_cert\_file和ssl\_key\_file指定其他名称和位置。

在Unix系统上，server.key上的权限必须设置为禁止其他用户或组的任何访问，通过命令chmod  
0600  
server.key来完成。或者，该文件可以由root所拥有并且具有数据库组的读访问权限（也就是0640权限）。这种设置适用于由操作系统管理证书和密钥文件的安装。用于运行瀚高数据库服务的系统用户应该被作为能够访问那些证书和密钥文件的组成员。

默认情况下数据目录为600权限，如果数据目录允许组读取访问，也就是640权限，则证书文件需要配置在数据目录data之外，以符合上面概述的安全要求。通常为data目录启用组访问权限是为了允许非特权用户备份数据库，在这种情况下，备份软件将无法读取证书文件，并且可能会出错。

## OpenSSL配置

瀚高数据库读取系统范围的OpenSSL配置文件。默认情况下，该文件被命名为openssl.cnf并位于openssl  
version  
\-d查询所示的目录中。通过将环境变量设置OPENSSL\_CONF为所需配置文件的名称，可以覆盖此默认值。

OpenSSL支持各种强度不同的密码和身份验证算法。虽然许多密码可以在OpenSSL的配置文件中被指定，也可以通过修改postgresql.conf配置文件中指定专门针对数据库服务器使用密码的 ssl\_ciphers 配置。

## SSL服务器文件用法

表7.3-1总结了与服务器上SSL配置有关的文件（显示的文件名是默认的名称。本地配置的名称可能会不同）。

| 文件 | 内容 | 效果 |
| --- | --- | --- |
| ssl\_cert\_file($PGDATA/server.crt) | 服务器证书 | 发送给客户端来说明服务器的身份 |
| ssl\_key\_file($PGDATA/server.key) | 服务器私钥 | 证明服务器证书是其所有者发送的，并不说明证书所有者是值得信任的 |
| ssl\_ca\_file | 可信的证书颁发机构 | 检查客户端证书是由一个可信的证书颁发机构签名的 |
| ssl\_crl\_file | 被证书授权机构撤销的证书 | 客户端证书不能出现在这个列表上 |

服务器在服务器启动时以及服务器配置重新加载时读取这些文件。在Windows系统上，只要  
为新客户端连接生成新的后端进程，它们也会重新读取。

如果在服务器启动时检测到这些文件中的错误，服务器将拒绝启动。但是，如果在配置重新加载过程中检测到错误，则会忽略这些文件，并继续使用旧的SSL配置。在Windows系统上，如果在后端启动时检测到这些文件中存在错误，则该后端将无法建立SSL连接。以上情况，错误情况都会在服务器日志中报告。

## 使用客户端证书

要求客户端提供受信任的证书，把你信任的根证书颁发机构（CA）的证书放置在data数据目录文件中。并且修改postgresql.conf中的参数 ssl\_ca\_file 到新的文件名，并把认证选项clientcert=verify-ca或clientcert=verify-full加入到pg\_hba.conf文件中合适的hostssl行上。然后将在SSL连接启动时从客户端请求该证书。对于具有clientcert=verify-ca的hostssl条目，服务器将验证客户端的证书是否由一个受信任的证书颁发机构签署的。如果指定了clientcert=verify-full，则服务器不仅将验证证书链，还将检查用户名或其映射是否与所提供的证书的cn（通用名称）相匹配。请注意，在使用cert身份验证方法时，要始终确保证书链验证。

clientcert认证选项适用于所有的认证方法，但仅适用于pg\_hba.conf中用hostssl指定的行。当clientcert没有指定，服务器仅在客户端证书存在并且CA被配置的时候，通过客户端的CA文件来查证客户端证书。

有两种方法可以强制用户在登录时提供证书：

第一种方法是对pg\_hba.conf文件中的hostssl条目使用cert身份验证方法，这样证书本身可以用于身份验证，同时提供ssl连接安全性。第二种方法是将对hostssl条目的任何身份验证方法和客户端证书的验证相结合，通过clientcert身份验证选项设置为verify-ca  
或  
verify-full。前一个选项仅强制证书有效，而后者还确保证书中的cn（通用名称）匹配用户名或适用的映射。

## 创建证书

要为服务器创建一个有效期为365天的简单自签名证书，可以使用下面的OpenSSL命令，并将dbhost.yourdomain.com替换为服务器的主机名：

```
openssl req -new -x509 -days 365 -nodes -text -out server.crt \

-keyout server.key -subj "/CN=dbhost.yourdomain.com"
```

然后执行：

```
chmod og-rwx server.key
```

如果文件的权限比这个更宽松，服务器将拒绝该文件。

尽管可以使用自签名证书进行测试，但是在生产中应该使用由证书颁发机构（CA）（通常是企业范围的根CA）签名的证书。

要创建其身份可以被客户端验证的服务器证书，请首先创建一个证书签名请求（CSR）和一个公共/专用密钥文件：

```
openssl req -new -nodes -text -out root.csr \

-keyout root.key -subj "/CN=root.yourdomain.com"

chmod og-rwx root.key
```

然后，使用密钥对请求进行签名以创建根证书颁发机构（使用Linux上的默认OpenSSL配置文件位置）：

```
openssl x509 -req -in root.csr -text -days 3650 \

-extfile /etc/ssl/openssl.cnf -extensions v3_ca \

-signkey root.key -out root.crt
```

最后，创建由新的根证书颁发机构签名的服务器证书：

```
openssl req -new -nodes -text -out server.csr \

-keyout server.key -subj "/CN=dbhost.yourdomain.com"

chmod og-rwx server.key

openssl x509 -req -in server.csr -text -days 365 \

-CA root.crt -CAkey root.key -CAcreateserial \

-out server.crt
```

server.crt和server.key应该存储在服务器上，并且root.crt应该存储在客户端上，以便客户端可以验证服务器的叶证书已由其受信任的根证书签名。root.key应该离线存储以用于创建将来的证书。

也可以创建一个包括中间证书的信任链：

```
# root

openssl req -new -nodes -text -out root.csr \

-keyout root.key -subj "/CN=root.yourdomain.com"

chmod og-rwx root.key

openssl x509 -req -in root.csr -text -days 3650 \

-extfile /etc/ssl/openssl.cnf -extensions v3_ca \

-signkey root.key -out root.crt

# intermediate

openssl req -new -nodes -text -out intermediate.csr \

-keyout intermediate.key -subj "/CN=intermediate.yourdomain.com"

chmod og-rwx intermediate.key

openssl x509 -req -in intermediate.csr -text -days 1825 \

-extfile /etc/ssl/openssl.cnf -extensions v3_ca \

-CA root.crt -CAkey root.key -CAcreateserial \

-out intermediate.crt

# leaf

openssl req -new -nodes -text -out server.csr \

-keyout server.key -subj "/CN=dbhost.yourdomain.com"

chmod og-rwx server.key

openssl x509 -req -in server.csr -text -days 365 \

-CA intermediate.crt -CAkey intermediate.key -CAcreateserial \

-out server.crt
```

server.crt和intermediate.crt应连接成一个证书文件包并存储在服务器上。  
server.key也应该存储在服务器上。root.crt应该被存储在客户端上，以便客户端可以验证服务器的叶证书是否已由链接到其受信任根证书的证书链签名。  
root.key和intermediate.key应离线存储以用于创建将来的证书。