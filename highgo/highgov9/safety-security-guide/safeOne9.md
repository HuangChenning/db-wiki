---
title: "加密模块"
book: "安全指南"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/safety/safeOne9.html"
tags:
  - highgo
  - highgo-v9
  - safety-security-guide
---

## 加密模块

## pgcrypto

瀚高数据库管理系统V9支持pgcrypto扩展模块，pgcrypto提供了多种加密和哈希算法的实现。它允许用户直接在数据库层面存储和操作加密数据，这些功能可以用来保护敏感数据，如密码、个人信息等，从而增强了数据的安全性。

pgcrypto模块通过内部源码、调用openssl等方式实现了多种加密算法，包括对称加密算法（如AES）、非对称加密算法（如 RSA）、哈希算法（如SHA-256）以及随机数生成等，在此基础上瀚高数据库增加国密算法SM3、SM4。pgcrypto模块提供了四十多种函数用法，其中有四类函数涉及新增SM3、SM4算法支持，详见下文描述。其他函数用法与原先保持一致，本文档不再展开描述。另外，在使用瀚高加密模块前首先需要创建pgcrypto扩展。

### digest函数

‌pgcrypto和digest()函数可以根据不同的算法生成数据的二进制哈希值‌。该函数可以根据不同的加密算法生成数据的二进制哈希值，支持的算法包括MD5、SH1A1、SHA224、SHA256、SHA384、SHA512、和SM3。

digest()函数基本语法如下：

```
digest(data text, type text)
digest(data bytea, type text)
```

参数说明：

- data：表示原始数据；
- type：表示加密算法，函数的返回结果为二进制字符串。

示例：

假如存在以下用户表：

```
highgo=# create extension pgcrypto;

highgo=# create table users (

id serial primary key,

username varchar(20) not null unique,

password text not null

);
```

创建新用户时，可以使用 digest() 函数对密码进行加密存储：

```
highgo=# insert into users(username, password) values ('tony',encode(digest('123456','md5'), 'hex'));

highgo=# insert into users(username, password) values ('anne',encode(digest('123456','md5'), 'hex'));

#查询users用户表，检查password字段是否加密存储：

highgo=# select * from users;

id | username | password

---------+-------------+----------

1 | tony | e10adc3949ba59abbe56e057f20f883e

2 | anne | e10adc3949ba59abbe56e057f20f883e
```

### hmac函数

通用哈希函数这类加密算法的主要问题是相同的数据经过加密之后的结果相同。因此。在实际应用中可以将用户名和密码字符串连接之后再进行加密。就是使用hmac()函数。

hmac函数基本语法如下：

```
hmac(data text, key text, type text)
hmac(data bytea, key bytea, type text)
```

参数说明：

- data：是原始数据；
- key：是加密密钥；
- type：是加密算法，包括SM3、 md5、sha1、sha224、sha256、sha384 以及  
	sha512；函数的返回结果为二进制字符串。

示例：

以下语句使用 hmac() 函数重新设置了用户的密码：

```
highgo=# update users set password = encode(hmac('123456', username,
'md5'), 'hex');

highgo=# select * from users;

id | username | password

---------+-------------+----------

1 | tony | 7a86cd4a12d7a54d65a4fe5854aaf41f

2 | anne | 9079d683b5fc5033427c2af2b6de4d01

(2 行记录)

#上述查询可以看到，相同密码加密后结果不同。
```

### encrypt函数

‌\[pgcrypto\]([https://www.baidu.com/s?rsv\_dl=re\_dqa\_generate&sa=re\_dqa\_generate&wd=pgcrypto&rsv\_pq=94c7eb7b00000e0b&oq=pgcrypto](https://www.baidu.com/s?rsv_dl=re_dqa_generate&sa=re_dqa_generate&wd=pgcrypto&rsv_pq=94c7eb7b00000e0b&oq=pgcrypto) encrypt%E5%87%BD%E6%95%B0%E4%BD%BF%E7%94%A8&rsv\_t=96a4uYVG4t0kl5cmm+i/1aJNvtBdOiaOFJ3WEEotwP/Fmt4NRYLf2zGI4OgKPNnt5Jid&tn=baiduhome\_pg&ie=utf-8)的encrypt函数用于对称加密，主要支持\[AES\]([https://www.baidu.com/s?rsv\_dl=re\_dqa\_generate&sa=re\_dqa\_generate&wd=AES&rsv\_pq=94c7eb7b00000e0b&oq=pgcrypto](https://www.baidu.com/s?rsv_dl=re_dqa_generate&sa=re_dqa_generate&wd=AES&rsv_pq=94c7eb7b00000e0b&oq=pgcrypto) encrypt%E5%87%BD%E6%95%B0%E4%BD%BF%E7%94%A8&rsv\_t=96a4uYVG4t0kl5cmm+i/1aJNvtBdOiaOFJ3WEEotwP/Fmt4NRYLf2zGI4OgKPNnt5Jid&tn=baiduhome\_pg&ie=utf-8)等算法。encrypt()和encrypt\_iv()新增支持SM4-ECB和SM4-CBC算法。

encrypt函数的基本语法如下：

```
encrypt(data bytea, key bytea, type text)
```

参数说明：

- data：是需要加密的数据。
- key：是加密密钥。
- type：指定加密方法，如 aes、des、sm4-ecb、sm4-cbc等。
	encrypt\_iv()：函数用于在提供初始化向量（IV）的情况下对数据进行加密。函数基本语法如下：

encrypt\_iv(data bytea, key bytea, iv bytea, type text)

参数说明：

- data：是需要加密的数据。
- key：加密所需密钥。
- iv：是初始化向量。
- type：指定加密方法，如aes、des、sm4-ecb、sm4-cbc等。
```
示例：

highgo=# select encrypt('aqaz','123','sm4-cbc');

encrypt

--------------------------------------------

\x9232333e983ecd2a6baaf8344afe4288

(1 行记录)
```

### decrypt函数

对称解密函数decrypt()和decrypt\_iv()新增支持SM4-ECB和SM4-CBC算法。

decrypt()函数基本语法如下：

```
decrypt(data bytea, key bytea, type text)
```

参数说明：

- data：需要解密的数据。
- key：解密所需的密钥。
- type：加密算法的类型，例如aes、des、sm4-ecb、sm4-cbc等。

decrypt\_iv()函数用于在提供初始化向量（IV）的情况下对数据进行解密。函数基本语法如下：

```
decrypt_iv(data bytea, key bytea, iv bytea, type text)
```

参数说明：

- data：需要解密的数据。
- key：解密所需的密钥。
- iv：初始化向量。
- type：解密算法的类型，例如aes、des、sm4-ecb、sm4-cbc等。

示例：

```
#查看服务器编码格式

highgo=# show server_encoding ;

server_encoding

------------------------------------------

UTF8

(1 行记录)

#字符串加密

highgo=# select encrypt_iv('foo', '0123456', 'abcd','aes');

encrypt_iv

------------------------------------------

\x2c24cb7da91d6d5699801268b0f5adad

(1 行记录)

#字符串解密，并使用convert_from()函数将二进制数据按照指定的字符集编码转换为文本字符串。

highgo=# select
convert_from(decrypt_iv('\x2c24cb7da91d6d5699801268b0f5adad',
'0123456', 'abcd','aes'),'utf-8');

convert_from

--------------------------------

foo

(1 行记录)
```

## TDE透明加密

瀚高数据库管理系统V9.0.4版本新增TDE透明加密模块。

数据库透明加密技术是针对关系型数据库保密需求应运而生的一种数据库加密技术。所谓透明，是指对用户来说无需更改现有的应用系统和操作习惯。当用户通过数据库访问数据时，得到的是明文数据，而未授权的用户通过非法手段直接访问数据文件得到的都是密文数据。数据在数据库应用中返回明文，数据在硬盘中保存为密文，一旦脱离数据库或无法合法的访问数据库便无法得到明文，从而起到保护数据库中数据的效果。数据透明加密所应对的威胁为不安全的存储介质。其它的威胁不在本模块考虑范围之内。

### 密钥管理

密钥管理模块是确保数据安全的核心组件，负责生成、存储、分发、轮换及销毁加密密钥。有效的密钥管理能够保证即使数据被非法获取，没有正确的密钥也无法解读实际内容，从而维护数据的机密性和完整性。良好的密钥管理策略还可以预防密钥泄露和滥用，增强系统的抗攻击能力，并且对于满足合规要求、保护用户隐私以及维持企业信誉具有关键意义。

透明加密模块中我们使用二级密钥系统管理密钥，其中主密钥也叫密钥加密密钥  
Key Encrypt  
Key，简称KEK。主密钥由用户保管，不存在于任何数据库文件中。数据密钥：也叫数据加密密钥Data  
Encrypt  
Key，简称DEK。数据密钥由数据库或加密机随机生成，并使用KEK加密存储，本模块包含3种数据加密密钥，分别为:

relation key: 用来加密表或索引这类关系文件。存储文件名rel.wkey。

wal key: 用来加密预写式日志。存储文件名wal.wkey。

key wrap key:  
用户密钥加密密钥，用来加密用户生成的密钥。存储文件名kwp.wkey。所有数据密钥都存储于数据目录的pg\_cryptokeys/live/目录下。为了避免小概率的存储介质比特位错误，会自动复制3份live目录。

#### 自定义多种主密钥获取方式

支持主密钥可以通过配置参数-C或--cluster-key-command，指定获取密钥的脚本或加密机相关参数。

语法：

```
initdb [-C key_command] [-R]
```

其中-R或--authprompt选项会打开一个终端句柄，用于输入在进程间的传递。特别注意：如果您在初始化时使用了交互输入，那么在启动数据库时同样需要指定-R或--authprompt做口令或密钥交互。

其中key\_command支持以下输入：

shell\_command: shell脚本，要求最终输出64位长度16进制的密钥字符串。

%d: 占位符，会被替换为存放密钥的位置。

%R: 占位符，会被替换为终端句柄。

%%: 转义为%

说明：

在无硬件安全模块的情况下，通过指定脚本获取到主密钥，然后对数据密钥进行解密使用。在使用usbkey的情况下，主密钥被usbkey加密存储，文件名为pivpass.wkey。通过指定脚本将主密钥交给usbkey进行解密，然后再用主密钥解密数据密钥。

示例1：直接echo返回主密钥（不推荐使用）

```
initdb -C "echo 123|sha256sum|cut -d ' ' -f1"
```

示例2：提示用户输入口令

透明加密功能实现了口令输入的脚本，在安装数据库后会被安装到数据库安装目录下/share/postgresql/auth\_commands目录中存放了一些样例脚本文件。提示用户输入口令可以用该目录下的ckey\_passphrase.sh.sample脚本，因为使用了交互输入，还需要指定-R参数。注意脚本的路径，示例中均以相对路径为例。

```
initdb -C 'sh ./ckey_passphrase.sh.sample %R' -R
```

示例3：提示用户输入密钥

此方式要求直接输入64位长度的16进制字符串格式的密钥。提示用户输入密钥可以使用ckey\_direct.sh.sample脚本。

```
initdb -C 'sh ./ckey_direct.sh.sample %R' -R
```

示例4：使用不带PIN验证的PIV

此方式要求配合PIV硬件例如Ukey，其中%d指示将被加密的KEK保存的位置。

```
initdb -C 'sh ./ckey_piv_nopin.sh.sample %d'
```

示例5：使用带PIN验证的PIV

此方式要求配合PIV硬件例如Ukey，并且需要输入pin验证身份。

```
initdb -C 'sh ./ckey_piv_pin.sh.sample %d %R' -R
```

示例6：使用aws保存密钥

此方式将密钥由云平台保存，本地存储密钥ID。

```
initdb -C 'sh ./ckey_aws.sh.sample %d'
```

#### 支持加密机管理数据密钥

在使用加密机时，数据密钥不再由数据库生成，也不再在本地保存。主密钥保存于加密机中不会脱离硬件设备，数据密钥也不允许被解密。数据密钥在使用时交给加密机获取操作句柄，然后使用。

使用加密机时，指定脚本要求返回的不是主密钥，而是特定标识：

HSM\_KEK\_ID=XX

其中XX为主密钥在加密机中的索引ID。

示例7：使用加密机管理密钥和加解密数据

```
initdb -C 'sh ./ckey_hsm.sh %d 1'
```

在使用加密机时，需要在/etc/目录下放入加密机的配置文件，配置加密机的连接信息等内容。配置文件模板与密钥管理示例脚本在同一目录中，文件名为swsds.ini.sample。

#### 支持密钥轮换

新增密钥轮换工具pg\_alterckey，支持更新主密钥，重新解密加密数据密钥完成密钥轮换。

```
pg_alterckey [OPTION] old_cluster_key_command new_cluster_key_command
[DATADIR]

pg_alterckey [repair_option] [DATADIR]

其中OPTION可以为：

-R, --authprompt: 提示输入密码或PIN

-D, --pgdata: 指定数据库目录

-V, --version: 输出版本号

-u, --upgrade：升级pg_control文件

-d, --downgrade：降级pg_control文件

-?, --help: 输出帮助信息

其中repair_option为：

-r, --repair: 修复密钥
```

特别说明：

因为加密机方式的特殊性，密钥轮换暂时不支持加密机方式。

示例8：进行密钥轮换

```
pg_alterckey "echo 123|sha256sum|cut -d ' ' -f1" "echo
321|sha256sum|cut -d ' ' -f1" -D ./data
```

示例9：密钥修复

当进行密钥轮换时发生意外中止，可以进行密钥修复操作

```
pg_alterckey -r -D ./data
```

示例10：升级pg\_control文件

```
pg_alterckey -D ./data -u
```

主要为解决升级后由于透明加密而造成pg\_control文件不一致问题，如遇到：致命错误:  
控制文件的校验值不正确。

#### 使用现有密钥初始化数据库

我们在初始化数据库时，可以使用随机生成的密钥，也可以选择使用已有密钥。通过指定参数-u或--copy-encryption-keys使用已有密钥。

```
initdb [-u data_path]
```

其中data\_path可以为已有数据库data目录，该目录下应包含pg\_cryptokeys/live/目录。

示例11：使用现有密钥初始化数据库

```
initdb -C "echo 123|sha256sum|cut -d ' ' -f1" -u ./backup_data
```

### 数据文件加密

开启透明加密功能后，瀚高数据库支持对WAL日志文件和表文件进行加密。加密范围支持数据库集簇级别加密和自定义加密。数据库集簇级别加密即加密整个数据库，包括所有的表，索引以及WAL。加密整个数据库包括其WAL是推荐的加密方式，在此模式下，数据库产生的所有表，索引等数据文件，以及WAL日志文件均被加密。自定义级别加密即自定义要加密的表，索引。因为WAL是整个数据库集簇共用的，目前还未实现针对部分表的相应WAL的加密，因此在自定义级别下WAL不进行加密。在自定义加密模式下，将一个已经加密的表的ENCRYPT选项重新设置为off后，表不会立即解密，而是在每次访问其page时对page解密。因此在对该表数据全部访问一次后，表数据会完成全部解密。

#### 支持全库加密和自定义表加密

初始化数据库时，可以通过-z或--file-encryption-mode参数指定加密哪些对象：

- ALL:  
	表示加密所有WAL日志和表文件，（创建表支持ENCRYPT语法但不生效）。
- WAL: 表示加密所有WAL日志。（表可通过语法指定ENCRYPT选项进行加密）
- REL: 表示加密所有表，（创建表支持ENCRYPT语法但不生效）。
- 空或不写-z选项：默认都不加密。（但可通过语法指定ENCRYPT选项进行加密）

自定义加密模式下仅支持加密：表，索引，无日志表，物化视图；暂不支持：分区表，临时表，toast表，序列。开启透明加密功能后自动加密，可以查看WAL日志和表数据文件，内容为密文。

语法：

```
CREATE TABLE table_name [WITH (encrypt=on)];
```

说明：

示例12：使用全加密

```
initdb -C "echo 123\|sha256sum|cut -d ' ' -f1" -z 'all'
```

示例13：对单表开启加密

CREATE TABLE table\_name \[WITH (encrypt=on)\];

#### 加密算法支持

瀚高透明加密模块支持AES和SM4加密算法，初始化数据库时，可以通过参数-K或--file-encryption-method指定加密的算法。不指定时默认使用AES加密。

initdb -K ‘encrypt\_method’

其中encrypt\_method可以是：

- AES: AES128算法加密
- AES192: AES192加密
- AES256: AES256加密
- SM4: SM4算法加密

示例14：使用SM4算法进行加密

```
initdb -C "echo 123|sha256sum|cut -d ' ' -f1" -K 'SM4'
```

#### 通过加密机方式加密

因为加密机方式管理密钥的特殊性，在使用加密机管理密钥的同时也会强制使用加密机方式加密解密数据。

注意在使用加密机方式加密解密数据时，所有数据需要先发送至加密机，然后完成加密或解密后再返回到数据库。因此加密机与数据库服务器需要有较大的带宽进行连接，否则容易因通信瓶颈导致数据库性能急剧下降。

示例15：使用加密机方式进行加密

```
initdb -C 'sh ./ckey_hsm.sh %d 1'
```

### 周边工具与TDE适配

---

| 工具 | 已适配 | 未适配 | 不涉及 |
| --- | --- | --- | --- |
| initdb | √ |  |  |
| licchk |  |  | √ |
| pg\_alterckey | √ |  |  |
| pg\_amcheck |  |  | √ |
| pg\_archivecleanup |  |  | √ |
| pg\_basebackup | √ |  |  |
| pg\_checksums |  |  | √ |
| pg\_config |  |  | √ |
| pg\_controldata | √ |  |  |
| pg\_ctl | √ |  |  |
| pg\_dump |  |  | √ |
| pg\_resetwal | √ |  |  |
| pg\_rewind | √ |  |  |
| pg\_test\_fsync |  |  | √ |
| pg\_test\_timing |  |  | √ |
| pg\_upgrade |  | √ |  |
| pg\_verifybackup | √ |  |  |
| pg\_waldump | √ |  |  |
| pg\_bench |  |  | √ |
| pg\_event |  |  | √ |
| psql |  |  | √ |
| clusterdb |  |  | √ |
| createdb |  |  | √ |
| createuser |  |  | √ |
| dropdb |  |  | √ |
| dropuser |  |  | √ |
| pg\_isready |  |  | √ |
| reindexdb |  |  | √ |
| vacuumdb |  |  | √ |