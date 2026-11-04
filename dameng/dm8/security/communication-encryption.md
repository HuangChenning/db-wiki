---
title: "通信加密"
book: "DM8 安全管理"
version: "DM8"
source: https://eco.dameng.com/document/dm/zh-cn/pm/communication-encryption.html
tags:
  - dameng
  - dm8
  - security
---

DM 提供两种通信加密方式：一基于传输层的 SSL 协议加密；二基于应用层的消息包加密。两个层次的加密互不影响，可以同时使用。因为任何一种加密方式都足够安全，而且双重加密会占用更多的数据库资源，所以通常情况下，没必要同时开启这两种加密。

当未采用通信加密时，为了提高安全性，数据库系统自动对登录消息中的用户名密码使用内部算法进行了简单的加解密操作，这里的简单加解密操作为使用 AES256\_CFB 算法加解密。如果用户需要对用户名密码进行增强加密，请参考 [11 登录用户名密码增强加密](user-name-password.md) 。

下面对基于传输层的 SSL 协议加密和基于应用层的消息包加密进行详细介绍。

## 6.1 基于传输层的 SSL 协议加密

### 6.1.1 SSL 模式说明

达梦数据库为用户提供了不同的 SSL 加密认证机制，具体内容和配置需求如下：

**1\. 基于 SSL 协议**

SSL 仅加密：仅对通信数据进行 SSL 加密。客户端和服务器需要配置 SSL 环境，但不需要加载证书。

SSL 仅认证：仅对通信双方进行 SSL 证书验证。客户端和服务器需要配置 SSL 环境，双方都需要加载 CA 证书和自己的证书，并验证对端证书的有效性。

SSL 认证加密：对通信双方进行 SSL 证书验证并对通信数据进行加密。客户端和服务器需要配置 SSL 环境，双方都需要加载 CA 证书和自己的证书，并验证对端证书的有效性。

SSL 单向认证和加密：客户端单向校验服务器端证书的有效性并对通信数据进行加密。客户端和服务器需要配置 SSL 环境，服务器端需要加载 CA 证书和服务器证书，客户端需要加载 CA 证书并验证服务器端证书的有效性。

**2\. 基于商密 TLCP 协议**

商密 TLCP 认证加密：OpenEuler 操作系统在其发布的开源版本基础上增加了对商密 TLCP 协议支持的 OpenSSL，基于商密 TLCP 协议对通信双方进行证书验证和通信数据的加密。客户端和服务器需要配置 SSL 环境，双方都需要加载签名证书和加密证书，并验证对端证书的有效性。

**SSL 参数介绍如下：**

用户可通过设置服务器配置文件 DM.INI 中的 ENABLE\_ENCRYPT 参数来指定 SSL 协议加密的模式，客户端以服务器采用的通信方式与其进行通信，具体如下：

ENABLE\_ENCRYPT 取值 0、1、2、3、4 或 5，缺省值为 0。不论设置为 1、2、4 或 5，它内部所使用的密码套件是 SSL 协议自动协商的，达梦未进行任何干涉。

0：通信数据不经 SSL 加密，通信双方也不进行证书验证。

1：通信数据会被加密，并且通信双方需要交换并验证对方证书是否匹配。

2：通信数据不会被加密，但通信双方会交换并验证对方证书是否匹配。

4：通信数据会被加密，但通信双方不需要验证证书。

5：通信数据会被加密，仅客户端会验证服务器端证书。

6：通信数据基于商密 TLCP 协议加密，通信双方交换并验证对方证书是否匹配。

另外，DM.INI 中的 MIN\_SSL\_VERSION 参数指定了允许连接的 SSL 最低版本，此参数设置仅当 ENABLE\_ENCRYPT 不为 0 时有效。MIN\_SSL\_VERSION 的可取值包括：

0：所有版本

0x0301：TLSv1

0x0302：TLSv1.1

0x0303：TLSv1.2

0x0304：TLSv1.3

MIN\_SSL\_VERSION 缺省为 0，为静态 INI 参数，修改后需要重启 DM 数据库服务器才能生效。

### 6.1.2 SSL 环境配置

当 ENABLE\_ENCRYPT 配置为 0 以外的值时，需要在服务器和客户端分别配置 SSL 环境。若服务器未配置 SSL 环境则服务器无法正常启动，若客户端未配置 SSL 环境则无法连接服务器。

安装达梦数据库时会自动配置 SSL 环境，即在客户端/服务器端配置 Openssl 的核心加密库和 SSL/TLS 协议库。

当服务器/客户端启动时，按照如下顺序在机器上查找动态库：

1. 在当前目录下查找动态库文件。
2. 在当前目录下的 dependencies 文件夹下查找动态库文件。
3. 在 DM 安装目录下 bin 文件夹、即 $DM\_HOME/bin 目录下查找。
4. $DM\_HOME/bin/dependencies 目录下查找。
5. 在系统上查找。

### 6.1.3 SSL 证书配置

- ENABLE\_ENCRYPT 取值为 0 或 4。

通信双方不进行证书验证，不需要进行证书配置。

- ENABLE\_ENCRYPT 取值为 1 或 2。

通信双方需要交换并验证对方证书是否匹配，需要先联系证书颁发机构获取 SSL 证书及证书的密码，具体如下：

服务器证书：CA 证书（ca-cert.pem）、服务器证书（server-cert.pem）、服务器私钥（server-key.pem）。

客户端证书：.keystore 文件、CA 证书（ca-cert.pem）、客户端证书（client-cert.pem）、客户端私钥（client-key.pem）。

- ENABLE\_ENCRYPT 取值为 5。

仅客户端验证服务器端证书，在客户端目录中仅需存放 CA 证书，用于对服务器证书的校验。需要联系证书颁发机构获取相关证书及密码，具体如下：

服务器证书：CA 证书（ca-cert.pem）、服务器证书（server-cert.pem）、服务器私钥（server-key.pem）。

客户端证书：.keystore 文件、CA 证书（ca-cert.pem）。

- ENABLE\_ENCRYPT 取值为 6。

通信数据基于商密 TLCP 协议进行加密，通信双方交换并验证对方证书是否匹配。需要联系证书颁发机构获取相关证书及密码，具体如下：

服务器证书：服务器加密证书（server-enc.crt），服务器加密 key（server-enc.key），服务器签名证书（server-sign.crt），服务器签名 key（server-sign.key）

客户端证书：客户端加密证书（client-enc.crt），客户端加密 key（client-enc.key），客户端签名证书（client-sign.crt），客户端签名 key（client-sign.key）

**证书放置目录：**

证书获取后，需要将准备好的证书放到数据库服务器和客户端的指定目录下。

服务器目录：$DM\_HOME/bin/server\_ssl

客户端目录：$DM\_HOME/bin/client\_ssl/username，或者在客户端的配置文件中设置 ssl\_path，指定客户端证书存放目录。其中，当用户名中含有具有大小写概念的多字节字符时，连接服务器时用户名需要与客户端证书存放目录$DM\_HOME/bin/client\_ssl/username 中文件名以及证书中的通用名保持一致，否则无法连接。

### 6.1.4 服务器配置

系统管理员登录数据库。

```
D:\dmdbms\bin>disql.exe SYSDBA/DMsys_123@localhost:5236
```

通过查询 V$PARAMETER 动态视图查询 ENABLE\_ENCRYPT 的当前值。

```
SQL>SELECT * FROM V$PARAMETER WHERE NAME='ENABLE_ENCRYPT';
```

调用系统过程 SP\_SET\_PARA\_VALUE 系统过程修改 ENABLE\_ENCRYPT 参数的取值。

```
--取值1表示开启SSL加密认证
SQL>SP_SET_PARA_VALUE(2,'ENABLE_ENCRYPT',1);
```

指定 TLS 协议版本。

```
--TLSv1.2
SQL>SP_SET_PARA_VALUE(2,'MIN_SSL_VERSION', 0x0303);
```

重新启动数据库服务器，使 INI 参数生效。

### 6.1.5 客户端连接

使用 DISql 登录时可以在连接串中指定用户的 SSL 证书路径(ssl\_path)。若证书私钥使用密码加密，需要在连接串中指定 ssl\_pwd 参数，如果证书没有密码则可以缺省或使用任意数字代替。

```
D:\dmdbms\bin>disql.exe SYSDBA/DMsys_123 @localhost:5236#"{ssl_path=D:\dmdbms\bin\client_ssl\SYSDBA,ssl_pwd=12345}"
```

可以通过查询 V$DM\_INI 视图中的 ENABLE\_ENCRYPT 参数确定是否开启 SSL 加密通信。

```
SQL> select para_name, para_value FROM V$DM_INI where para_name='ENABLE_ENCRYPT';

行号    PARA_NAME   PARA_VALUE
---------- -------------- ----------
1     ENABLE_ENCRYPT 1
```

使用 DM 管理工具连接数据库时，可在“高级”选项卡的连接属性新增 sslFilesPath 属性和 sslKeystorePass 属性，分别用于指定证书目录和.keystore 文件密码，没有密码时可输入默认密码 changeit。

图6.1 DM管理工具基于SSL协议连接数据库

### 6.1.6 举例说明

以 ENABLE\_ENCRYPT=5，进行 SSL 单向认证和加密的情形为例进行说明。

第一步：获取 SSL 证书，保证用户拥有自己的 SSL 数字证书，并且确认 DM 服务器和 DM 客户端均已配置好 SSL 环境。

第二步：修改 ENABLE\_ENCRYPT 参数取值。

系统管理员使用 DISql 连接服务器。

```
D:\dmdbms\bin>disql.exe SYSDBA/DMsys_123@localhost:5236
```

在数据库中创建 DM\_ssl 用户。

```
SQL>CREATE USER DM_ssl IDENTIFIED BY "Dm_12345";
```

使用 SP\_SET\_PARA\_VALUE 系统过程将 ENABLE\_ENCRYPT 参数的取值修改为 5。

```
SQL> SP_SET_PARA_VALUE(2,'ENABLE_ENCRYPT',5);
```

重新启动数据库服务器，使 INI 参数生效。

第三步：配置 SSL 证书。

当 ENABLE\_ENCRYPT 取值为 5 时，客户端对服务器端进行单向的证书校验。因此在 server\_ssl 目录下，需要存放 CA 证书（ca-cert.pem）、服务器证书（server-cert.pem）与服务器私钥（server-key.pem），在 client\_ssl 目录下的 DM\_ssl 用户目录中，仅需存放 CA 证书，用于对服务器证书的校验。

第四步：数据库连接。

DM\_ssl 用户连接 DM 服务器，输入用户名和密码、DM 服务器 IP 地址和端口号以及当前登录用户自身的 SSL 数字证书路径以及相应的 SSL 证书密码。

```
D:\dmdbms\bin>disql.exe DM_ssl/Dm_12345@localhost:5236#"{ssl_path=D:\dmdbms\bin\client_ssl\DM_ssl,ssl_pwd=12345}"
```

第五步：确定是否通信加密开启成功。

系统管理员通过查询 V$DM\_INI 视图中的 ENABLE\_ENCRYPT 参数确定是否开启 SSL 加密通信。

```
SQL> select para_name, para_value FROM V$DM_INI where para_name='ENABLE_ENCRYPT';

行号    PARA_NAME   PARA_VALUE
---------- -------------- ----------
1     ENABLE_ENCRYPT 5
```

### 6.1.7 常见问题

1.认证方式：

通过设置 INI 参数 ENABLE\_ENCRYPT 来指定认证方式，调用系统过程修改该参数后需要重启数据库服务器使参数生效。

2.客户端登录失败的原因：

1）环境未正确配置：

INI 参数 ENABLE\_ENCRYPT 大于 0 时，根据具体取值，客户端需要配置 SSL 环境。否则报错初始化 SSL 环境失败。

2）证书加载失败：

INI 参数 ENABLE\_ENCRYPT 设置为客户端需要加载证书的取值时，客户端需要在指定位置配置 SSL 证书，或在配置信息中指定证书文件地址。否则报错“初始化 SSL 环境失败”。

3）建立连接失败：

可能是证书校验失败等原因，报错“网络通讯失败”。

## 6.2 基于应用层的消息包加密

选择是否使用基于应用层的消息包加密以 DM 数据库服务器端的设置为准，即通过设置服务器配置文件 DM.INI 中的 COMM\_ENCRYPT\_NAME 参数来指定，客户端以服务器采用的通信方式与其进行通信。

COMM\_ENCRYPT\_NAME 取值空串、算法名分别代表不加密、加密。缺省为空串。算法名可以通过查询动态视图 V$CIPHERS 获取。本节的算法名必须为分组加密算法或流加密算法(即 CYT\_TYPE 为 1 或 2)，且不为非填充模式（即 WORK\_MODE 不能是 ECB\_NOPAD 或 CBC\_NOPAD）。当算法名写错，则使用加密算法 AES256\_CFB。应用层加密的密钥是通过 DH 密钥交换算法协商生成。

用户可通过 V$CIPHERS 动态视图查询达梦支持的 COMM\_ENCRYPT\_NAME 算法名。

```
SELECT CYT_NAME FROM V$CIPHERS WHERE (CYT_TYPE=1 OR CYT_TYPE=2 ) AND （WORK_MODE!='ECB_NOPAD' AND WORK_MODE!='CBC_NOPAD'）;
```

用户可通过 V$PARAMETER 动态视图查询 COMM\_ENCRYPT\_NAME 的当前值。

```
SELECT * FROM V$PARAMETER WHERE NAME='COMM_ENCRYPT_NAME';
```

也可以通过使用客户端工具 Console 或调用系统过程 SP\_SET\_PARA\_STRING\_VALUE 重新设置 COMM\_ENCRYPT\_NAME 的值。不过由于这个参数都为静态 INI 参数，修改后需要重启 DM 数据库服务器才能生效。

```
SP_SET_PARA_STRING_VALUE(2,'COMM_ENCRYPT_NAME','DES_OFB');
```