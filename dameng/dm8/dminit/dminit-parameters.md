---
title: "dminit 参数详解"
book: "DM8 dminit 使用手册"
version: "DM8"
source: https://eco.dameng.com/document/dm/zh-cn/pm/dminit-parameters.html
tags:
  - dameng
  - dm8
  - dminit
---

## 4.1 INI\_FILE

初始化文件 dm.ini 存放的路径，指定一个已经存在的 dm.ini 文件所在的绝对路径。作用是将现有 INI 文件，拷贝到新库，作为新库的 INI 文件直接使用。文件路径长度最大为 256 个字符。可选参数。

如果不指定该参数，那么 dminit 工具会直接生成一个新的 dm.ini 文件。如果指定了该参数但指定的 INI 文件不存在，那么 dminit 工具会报错无效的 INI 文件，同时生成一个新的 dm.ini 文件。

例 指定现有/home/test/dmdbms 库中 dm.ini，给新创建的/home/dest/dmdbms 库使用。

```
./dminit INI_FILE=/home/test/dmdbms/DAMENG/dm.ini PATH=/home/dest/dmdbms SYSDBA_PWD=DMdba_123 SYSAUDITOR_PWD=DMauditor_123
```

## 4.2 PATH

初始数据库存放的路径。默认路径为 dminit.exe 当前所在的工作目录。文件路径长度最大为 256 个字符。可选参数。

数据库创建成功后，可通过查询 V$PARAMETER 或 V$DM\_INI 的 SYSTEM\_PATH 参数名查看数据库存放的路径。

## 4.3 CTL\_PATH

初始数据库控制文件的路径，默认值 Windows 下为 PATH\\DB\_NAME\\dm.ctl，Linux 下为/PATH/DM\_NAME/dm.ctl（PATH 和 DB\_NAME 表示各自设置的值）。文件路径长度最大为 256 个字符。可选参数。

数据库创建成功后，可通过查询 V$PARAMETER 或 V$DM\_INI 的 CTL\_PATH 参数名查看数据库控制文件的路径。

## 4.4 LOG\_PATH

初始数据库日志文件的路径。默认值 Windows 下为 PATH\\DB\_NAME\\DB\_NAME01.log 和 PATH\\DB\_NAME\\DB\_NAME02.log，Linux 下为 PATH/DB\_NAME/DB\_NAME01.log 和 PATH/DB\_NAME/DB\_NAME02.log（PATH 和 DB\_NAME 表示各自设置的值）。文件路径长度最大为 256 个字符。日志文件路径个数不能超过 10 个。可选参数。

修改日志文件大小可以使用 LOG\_SIZE 参数。

例 创建一个数据库，包含两个日志文件 DATA01.log 和 DATA02.log。

```
./dminit PATH=/home/dest/dmdbms LOG_PATH=/home/dest/dmdbms/DATA01.log
LOG_PATH=/home/dest/dmdbms/DATA02.log SYSDBA_PWD=DMdba_123 SYSAUDITOR_PWD=DMauditor_123
```

数据库创建成功后，可以在运行时使用 ALTER DATABASE 修改数据库语句增加日志文件或对日志文件进行重命名。可通过查询 V$RLOGFILE 的 PATH 列查看当前系统各日志文件的路径。

## 4.5 EXTENT\_SIZE

数据文件使用的簇大小，即每次分配新的段空间时连续的页数。取值范围 16、32、64。单位：页数。缺省值为 16。可选参数。

数据库创建成功后无法再修改簇大小，可通过系统函数 SF\_GET\_EXTENT\_SIZE()获取系统的簇大小。

## 4.6 PAGE\_SIZE

数据文件使用的页大小。取值范围 4、8、16、32，单位：KB。缺省值为 8。可选参数。

选择的页大小越大，则 DM 支持的元组长度也越大，但同时空间利用率可能下降。

数据库创建成功后无法再修改页大小，可通过系统函数 SF\_GET\_PAGE\_SIZE()获取系统的页大小。

需要注意的是，在全库加密使用膨胀算法，或指定了 PAGE\_HASH\_NAME 时，数据页中将会预留一定的大小(膨胀算法占用空间，页 hash 算法散列值占用空间)，导致数据页中的 free space 比实际页大小小，DM 数据库的正常启动需要保证页的 free space 超过 4KB，因此此时 PAGE\_SIZE=4 无法使用。

## 4.7 LOG\_SIZE

重做日志文件使用的大小。在 32 位版本下，取值范围为 256 和 2048 之间的整数，单位 MB，缺省值为 2048；在 64 位版本下，取值范围为 256 和 8192 之间的整数，单位 MB，缺省值为 4096。可选参数。

每个 DM 数据库实例至少有两个重做日志文件，循环使用，LOG\_SIZE 设置每个重做日志文件的大小。

设置日志文件路径可以使用 LOG\_PATH 参数。

数据库创建成功后，可以在运行时使用 ALTER DATABASE 修改数据库语句增加日志文件的大小。可通过查询 V$RLOGFILE 的 RLOG\_SIZE 列查看当前系统各日志文件的大小。

## 4.8 CASE\_SENSITIVE

大小写是否敏感。当大小写敏感时，小写的标识符应用""括起，否则被系统自动转换为大写；当大小写不敏感时，系统不会转换字符的大小写，系统比较函数会将大写字母全部转为小写字母再进行比较。取值：Y、y、1 表示敏感；N、n、0 表示不敏感。缺省值为 Y。可选参数。

此参数在数据库创建成功后无法修改，可通过系统函数 SF\_GET\_CASE\_SENSITIVE\_FLAG()或 CASE\_SENSITIVE()查询设置的参数值。

## 4.9 CHARSET/UNICODE\_FLAG

字符集选项。取值范围 0、1、2。0 代表 GB18030，支持 GB18030-2022 版本；1 代表 UTF-8，支持 UNICODE 12.0 版本；2 代表韩文字符集 EUC-KR。缺省值为 0。可选参数。

此参数在数据库创建成功后无法修改，可通过系统函数 SF\_GET\_UNICODE\_FLAG()或 UNICODE()查询设置的参数值。

## 4.10 SEC\_PRIV\_MODE

权限管理模式。取值范围 0、1、2、3、4。0：TRADITION，表示传统模式；1：BMJ，表示专用机模式；2：EVAL，表示 EVAL 测评模式；3：ZB，表示 ZB 模式；4：ZBMM，表示 ZBMM 模式。缺省值为 0。可选参数。

数据库创建成功后，可通过修改 INI 参数 SEC\_PRIV\_MODE 的值对此参数的设置进行修改。可通过查询 V$PARAMETER 或 V$DM\_INI 中的 SEC\_PRIV\_MODE 参数名查看此参数当前的设置值，还可以通过使用系统函数 SF\_GET\_PARA\_VALUE 获取此参数当前的设置值。

## 4.11 SYSDBA\_PWD

初始化时设置 SYSDBA 的密码，不允许缺省。密码为字符串，必须同时包含大写字母、小写字母、数字，不允许与用户名重名，密码长度须大于或等于 INI 参数 PWD\_MIN\_LEN 所设定的值且小于 48，关于参数 PWD\_MIN\_LEN 的详细说明请参考《DM8 系统管理员手册》。

如果密码中包含特殊字符，则需要按照规定的书写规范进行书写，详细请参考《DM8\_DIsql 使用手册》中关于特殊字符的书写规范相关介绍。

数据库创建成功后，SYSDBA 可通过修改用户密码语句修改自己的密码。

## 4.12 SYSAUDITOR\_PWD

初始化时设置 SYSAUDITOR 的密码，不允许缺省。密码为字符串，必须同时包含大写字母、小写字母、数字，不允许与用户名重名，密码长度须大于或等于 INI 参数 PWD\_MIN\_LEN 所设定的值且小于 48，关于参数 PWD\_MIN\_LEN 的详细说明请参考《DM8 系统管理员手册》。

如果密码中包含特殊字符，则需要按照规定的书写规范进行书写，详细请参考《DM8\_DIsql 使用手册》中关于特殊字符的书写规范相关介绍。

数据库创建成功后，SYSAUDITOR 可通过修改用户密码语句修改自己的密码。

## 4.13 DB\_NAME

初始化数据库名称，缺省值为 DAMENG。名称为字符串，长度不能超过 128 个字符。可选参数。数据库名称只能由\_、$、大写字母 A 至 Z、小写字母 a 至 z、数字 0 至 9 组成，且第一个字符不能是数字。例如：一个合格的数据库名称为 Dm\_1。

数据库名称在数据库创建成功后无法修改，可通过查询 V$DATABASE 的 NAME 列获取数据库名。

## 4.14 INSTANCE\_NAME

初始化数据库实例名称，缺省值为 DMSERVER。名称为字符串，长度不能超过 16 个字符。可选参数。实例名称只能由\_、$、大写字母 A 至 Z、小写字母 a 至 z、数字 0 至 9 组成，且第一个字符不能是数字。例如：一个合格的实例名称为 Dmserver$1。

数据库创建成功后，可通过修改 INI 参数 INSTANCE\_NAME 的值对此参数的设置进行修改。可通过查询 V$PARAMETER 或 V$DM\_INI 中的 INSTANCE\_NAME 参数名获取当前的数据库实例名。

## 4.15 PORT\_NUM

初始化时设置 dm.ini 中的数据库服务器监听端口号，缺省值为 5236。服务器配置此参数，取值范围 1024~65534，发起连接端的端口在 1024~65535 之间随机分配。可选参数。

数据库创建成功后，可通过修改 INI 参数 PORT\_NUM 的值对此参数的设置进行修改。可通过查询 V$PARAMETER 或 V$DM\_INI 中的 PORT\_NUM 参数名查看此参数当前的设置值，还可以通过使用系统函数 SF\_GET\_PARA\_VALUE 获取此参数当前的设置值。

## 4.16 BUFFER

NORMAL 缓冲区大小，以 MB 为单位。推荐值：NORMAL 缓冲区大小为可用物理内存的 60%～80%。取值范围 8~16777216，在 PAGE\_SIZE 为 4K 的库中，BUFFER 最大值为 15728640。64 位系统的缺省值为 8000，32 位系统的缺省值为 64。可选参数。

数据库创建成功后，可通过修改 INI 参数 BUFFER 的值对此参数的设置进行修改。可通过查询 V$PARAMETER 或 V$DM\_INI 中的 BUFFER 参数名查看此参数当前的设置值，还可以通过使用系统函数 SF\_GET\_PARA\_VALUE 获取此参数当前的设置值。

当建库参数 AUTO\_ADJ\_PARA 为 1 时，本参数实际默认值由系统根据 AUTO\_ADJ\_MEM 自动调整，用户也可根据实际需要手动调整。

## 4.17 TIME\_ZONE

初始化时区，默认为东八区(+08:00)。格式为\[正负号\]小时\[：分钟\]，其中，正负号和分钟为可选项。时区设置范围为：-12:59~+14:00。可选参数。

此参数在数据库创建成功后无法修改，可通过查询 V$PARAMETER 或 V$DM\_INI 中的 TIME\_ZONE 参数名查看此参数的设置值，还可以通过使用系统函数获取此参数的设置值：select SF\_GET\_PARA\_VALUE(2,'TIME\_ZONE');。

## 4.18 PAGE\_CHECK、PAGE\_HASH\_NAME

PAGE\_CHECK 为页检查模式。取值范围 0、1、2、3。0：禁用页校验；1：开启页校验并使用 CRC 校验；2：开启页校验并使用指定的 HASH 算法进行校验；3：开启页校验并使用快速 CRC 校验。缺省值为 3。可选参数。

PAGE\_CHECK 为 0 时不进行页校验；非 0 表示数据页刷盘时会为数据页计算一个校验和值写入数据页头，下次从磁盘加载数据页时校验数据页内容是否正确。

当校验到数据页内容损坏时，分为以下几种情况进行处理：

- 若数据文件（或回滚文件）有镜像文件（涉及到的建库参数有 system\_mirror\_path、main\_mirror\_path 和 roll\_mirror\_path，或在创建表空间时指定镜像文件），系统会自动读取镜像文件中的数据继续提供服务；
- 若没有镜像文件，且 INI 参数 PTX\_ROLLBACK 为 0：根据 INI 参数 PAGE\_CHECK\_POLICY 的取值确定处理策略，PAGE\_CHECK\_POLICY 为 0 时忽略损坏，PAGE\_CHECK\_POLICY 为 1 时系统主动 HALT；
- 若没有镜像文件，且 INI 参数 PTX\_ROLLBACK 为 1：
	对于大部分数据页损坏的情况，系统会进行报错处理；
	对于无法报错处理的少部分情况（包括损坏的数据页是文件 0 号页、系统表空间数据页、文件系统 INODE 页或者描述页等），根据 INI 参数 PAGE\_CHECK\_POLICY 的取值确定处理策略，PAGE\_CHECK\_POLICY 为 0 时忽略损坏，PAGE\_CHECK\_POLICY 为 1 时系统主动 HALT；

PAGE\_HASH\_NAME 用于设置页检查 HASH 算法。当且仅当 PAGE\_CHECK=2 时，使用 PAGE\_HASH\_NAME 来指定用于页检查的 HASH 算法。HASH 算法可通过 SELECT CYT\_NAME FROM V$CIPHERS WHERE CYT\_TYPE=4;语法获取。

PAGE\_CHECK 在数据库创建成功后无法修改。可通过使用系统函数获取设置的页检查模式：select SF\_GET\_PARA\_VALUE(2, 'ENABLE\_PAGE\_CHECK');。

PAGE\_HASH\_NAME 在数据库创建成功后无法修改。可通过 V$PARAMETER 中的 NAME='PAGE\_CHECK\_ID'查看设置的页检查 HASH 算法 ID，进而通过算法 ID 获取算法名：SELECT CYT\_NAME FROM V$CIPHERS WHERE CYT\_ID=(SELECT VALUE FROM V$PARAMETER WHERE NAME= 'PAGE\_CHECK\_ID');，另外也可以通过 V$DM\_INI 中的 PARA\_NAME='PAGE\_CHECK\_ID'，或通过使用系统函数获取设置的页检查 HASH 算法 ID：select SF\_GET\_PARA\_VALUE(2,'PAGE\_CHECK\_ID');。

## 4.19 EXTERNAL\_CIPHER\_NAME、EXTERNAL\_HASH\_NAME、EXTERNAL\_CRYPTO\_NAME

第三方加密时使用。

EXTERNAL\_CIPHER\_NAME：设置默认加密算法，缺省为 DES\_CFB。备份、还原、建表等凡是用到加密算法，但是又未指定加密算法的情况下，如果用户指定了第三方加密，则用此算法。可选参数。加密算法可通过 SELECT CYT\_NAME FROM V$CIPHERS WHERE CYT\_TYPE<3;获得。该参数在数据库创建成功后无法修改。可通过查询 V$PARAMETER 或 V$DM\_INI 中的 EXTERNAL\_CIPHER\_ID 参数名查看设置的默认加密算法 ID，还可以通过使用系统函数获取设置的默认加密算法 ID：select SF\_GET\_PARA\_VALUE (2,'EXTERNAL\_CIPHER\_ID');。

EXTERNAL\_HASH\_NAME：设置默认 HASH 算法，缺省为 MD5 或 SHA1（系统根据不同的场景自动选定）。用来生成加密数据的校验码。可选参数。加密算法可通过 SELECT CYT\_NAME FROM V$CIPHERS WHERE CYT\_TYPE=4;获得。该参数在数据库创建成功后无法修改。可通过查询 V$PARAMETER 或 V$DM\_INI 中的 EXTERNAL\_HASH\_ID 参数名查看设置的默认 HASH 算法 ID，还可以通过使用系统函数获取设置的默认加密算法 ID：select SF\_GET\_PARA\_VALUE(2,'EXTERNAL\_HASH\_ID');。

EXTERNAL\_CRYPTO\_NAME：设置服务器根密钥加密引擎，缺省为无加密引擎。加密引擎的使用，详细请参考《DM8 安全管理》一书加密引擎章节。可选参数。加密引擎可通过 SELECT NAME FROM V$EXTERNAL\_CIPHER\_LIBS;获得。该参数在数据库创建成功后无法修改。可通过查询 V$PARAMETER 或 V$DM\_INI 中的 EXTERNAL\_CRYPTO\_NAME 参数名查看设置的服务器根密钥加密引擎。

EXTERNAL\_CIPHER\_NAME、EXTERNAL\_HASH\_NAME 与 EXTERNAL\_CRYPTO\_NAME 无关，两者没有必然联系。

## 4.20 RLOG\_ENCRYPT\_NAME

设置联机日志文件和归档日志文件的加密算法，若未设置则不加密。

RLOG\_ENCRYPT\_NAME 支持使用第三方加密算法，但不支持工作模式为 WORK\_MODE\_CBC\_NOPAD、WORK\_MODE\_ECB\_NOPAD 或 WORK\_MODE\_EXTKEY 的加密算法，关于加密算法的工作模式可参考《DM8 安全管理》8.1.1 节。

此参数在数据库创建成功后无法修改，可通过查询 V$PARAMETER 或 V$DM\_INI 中的 RLOG\_ENC\_ID 参数名查看此参数设置的加密算法 ID，还可以通过使用系统函数获取此参数设置的加密算法 ID：select SF\_GET\_PARA\_VALUE(2,'RLOG\_ENC\_ID');。

## 4.21 RLOG\_POSTFIX\_NAME

设置联机日志文件扩展名，可设置长度不超过 10 的字符串，默认为 log。

每个 DM 数据库实例必须至少有 2 个联机日志文件，默认两个日志文件为 DAMENG01.log、DAMENG02.log，这两个文件循环使用。

此参数在数据库创建成功后无法修改。

## 4.22 USBKEY\_PIN

USBKEY PIN 是登录第三方设备 UKEY 的密码。供使用 UKEY 的用户使用。UKEY 用于服务器端存储加密根密钥的证书，缺省使用磁盘物理文件 dm\_service.prikey 存储根密钥密钥的密文。

在 DM 的加密机制中，增加移动 UKEY 的使用，更能确保 SVR\_KEY 的安全性，数据安全性也得到进一步提升。

USBKEY PIN 为字符串，不能超过 48 个字节。可选参数。

此参数在数据库创建成功后无法修改。

## 4.23 PAGE\_ENC\_SLICE\_SIZE

使用数据页按扇区大小进行分片加解密时，指定数据页加解密的分片大小。可配置大小取值范围为 0、512 或 4096，单位为 byte，缺省值为 4096。其中，0 表示不按分片进行加解密，即按照页大小进行加解密, 后续查询参数时, 将显示为页大小。可选参数。

此参数在数据库创建成功后无法修改，可通过查询 V$PARAMETER 或 V$DM\_INI 中的 PAGE\_ENC\_SLICE\_SIZE 参数名查看此参数的设置值，还可以通过使用系统函数获取此参数的设置值：select SF\_GET\_PARA\_VALUE(2,'PAGE\_ENC\_SLICE\_SIZE');。

## 4.24 ENCRYPT\_NAME

指定全库加密算法，加密密钥由 DM 自动生成。不指定时，不进行全库加密。

全库加密操作流程：第一步，在创建数据库的过程中，通过参数 ENCRYPT\_NAME 的设置，使用 DM 内部支持的加密算法或是第三方的加密算法对数据库文件进行加解密。第二步，在服务器启动及运行的过程中，需要对处理的所有数据页通过指定的加密算法和 DM 自动生成的密钥进行加解密处理，即如果数据页读入缓存，需要进行解密后才能使用，在缓存中的数据页进行刷盘时，需要对数据页进行加密后存储到数据文件中。

ENCRYPT\_NAME：全库加密使用的算法名。算法可以是 DM 内部支持的加密算法，或者是第三方的加密算法，其中 DM 支持的加密算法可通过查询动态视图 V$CIPHERS 得到，相关介绍可参见《DM8 安全管理》7.1.1 节。算法名为字符串，不能超过 128 个字节。可选参数。

此参数在数据库创建成功后无法修改，可通过系统函数 SF\_GET\_ENCRYPT\_NAME()获取此参数的设置值。

## 4.25 BLANK\_PAD\_MODE

设置字符串比较时，结尾空格填充模式是否兼容 ORACLE。1：兼容；0：不兼容。缺省值为 0。可选参数。

此参数在数据库创建成功后无法修改，可通过查询 V$PARAMETER 或 V$DM\_INI 中的 BLANK\_PAD\_MODE 参数名查看此参数的设置值，还可以通过使用系统函数获取此参数的设置值：select SF\_GET\_PARA\_VALUE(2,'BLANK\_PAD\_MODE');。

## 4.26 SYSTEM\_MIRROR\_PATH

指定 system.dbf 文件的镜像绝对路径。默认为空。可选参数。

当 PAGE\_CHECK 非 0 时，此参数才有意义。

此参数在数据库创建成功后无法修改，可通过查询 V$DATAFILE 的 MIRROR\_PATH 列查看此参数的设置值。

## 4.27 MAIN\_MIRROR\_PATH

指定 main.dbf 文件的镜像绝对路径。默认为空。可选参数。

当 PAGE\_CHECK 非 0 时，此参数才有意义。

此参数在数据库创建成功后无法修改，可通过查询 V$DATAFILE 的 MIRROR\_PATH 列查看此参数的设置值。

## 4.28 ROLL\_MIRROR\_PATH

指定 roll.dbf 文件的镜像绝对路径。默认为空。可选参数。

当 PAGE\_CHECK 非 0 时，此参数才有意义。

此参数在数据库创建成功后无法修改，可通过查询 V$DATAFILE 的 MIRROR\_PATH 列查看此参数的设置值。

## 4.29 MAL\_FLAG

初始化时设置 dm.ini 中的 MAL\_INI 值。取值范围为 0 或 1。缺省值为 0。可选参数。

1 表示设置 MAL\_INI=1，启动 MAL 系统。同时，需要配置 dmmal.ini 文件。

0 表示设置 MAL\_INI=0，不启用 MAL 系统。

数据库创建成功后，可通过修改 INI 参数 MAL\_INI 重新设置 MAL\_INI。可通过查询 V$PARAMETER 或 V$DM\_INI 中的 MAL\_INI 参数名查看 MAL\_INI 当前的设置值，还可以通过使用系统函数 SF\_GET\_PARA\_VALUE 获取 MAL\_INI 当前的设置值。

## 4.30 ARCH\_FLAG

初始化时设置 dm.ini 中的 ARCH\_INI 值。取值范围为 0 或 1。缺省值为 0。可选参数。

1 表示设置 ARCH\_INI=1，启用归档。同时，需要配置 dmarch.ini 文件。

0 表示设置 ARCH\_INI=0，不启用归档。

数据库创建成功后，可通过修改 INI 参数 ARCH\_INI 重新设置 ARCH\_INI。可通过查询 V$PARAMETER 或 V$DM\_INI 中的 ARCH\_INI 参数名查看 ARCH\_INI 当前的设置值，还可以通过使用系统函数 SF\_GET\_PARA\_VALUE 获取 ARCH\_INI 当前的设置值。

## 4.31 MPP\_FLAG

MPP 系统内的库初始化时设置 dm.ini 中的 MPP\_INI。取值范围为 0 或 1。缺省值为 0。可选参数。

1 表示设置 MPP\_INI=1，启用 MPP 系统。

0 表示设置 MPP\_INI=0，不启用 MPP 系统。

数据库创建成功后，可通过修改 INI 参数 MPP\_INI 重新设置 MPP\_INI。可通过查询 V$PARAMETER 或 V$DM\_INI 中的 MPP\_INI 参数名查看 MPP\_INI 当前的设置值，还可以通过使用系统函数 SF\_GET\_PARA\_VALUE 获取 MPP\_INI 当前的设置值。

## 4.32 CONTROL

指定初始化配置文件路径。可选参数。

使用 CONTROL 参数时，CONTROL 参数必须位于首位，且 CONTROL 参数只能和 SYSDBA\_PWD、SYSAUDITOR\_PWD、SYSSSO\_PWD、SYSDBO\_PWD 参数同时使用，和其他参数同时使用时将会报错。当命令行和 ctl 文件参数值存在冲突时，以命令行给出的值为准。

CONTROL 参数主要用于将数据文件创建在 ASM 上或者 DSC 环境中。CONTROL 参数和初始化配置文件，详细信息见下一章节。

## 4.33 AUTO\_OVERWRITE

是否覆盖建库目录下所有同名文件。取值范围为 0、1、2。0 不覆盖，表示建库目录下如果没有同名文件，直接创建，如果遇到同名文件时，屏幕提示是否需要覆盖，由用户手动输入是与否（y/n，1/0），若选择不进行覆盖则初始化失败；1 部分覆盖，表示覆盖建库目录下所有同名文件；2 完全覆盖，表示先清理掉建库目录下所有文件再重新创建。缺省值为 0。可选参数。

## 4.34 USE\_NEW\_HASH

是否使用改进的字符类型 HASH 算法。字符类型在计算 HASH 值时所采用的 HASH 算法类别。0：原始 HASH 算法；1：改进的 HASH 算法。缺省值为 1。可选参数。

如果备份文件和数据库文件中该参数值不一致，则还原时会报错。

此参数在数据库创建成功后无法修改，可通过查询 V$PARAMETER 或 V$DM\_INI 中的 USE\_NEW\_HASH 参数名查看此参数的设置值，还可以通过使用系统函数获取此参数的设置值：select SF\_GET\_PARA\_VALUE(2,'USE\_NEW\_HASH');。

## 4.35 ELOG\_PATH

指定初始化过程中生成的日志文件所在路径。可选参数，缺省则生成在 DM 执行码目录同级的 log 目录中。

## 4.36 AP\_PORT\_NUM

分布式环境下协同工作的监听端口。手动配置的取值范围为 1024~65534。缺省值为 0，表示未配置。可选参数。

数据库创建成功后，可通过修改 INI 参数 AP\_PORT\_NUM 的值对此参数的设置进行修改。可通过查询 V$PARAMETER 或 V$DM\_INI 中的 AP\_PORT\_NUM 参数名查看此参数当前的设置值，还可以通过使用系统函数 SF\_GET\_PARA\_VALUE 获取此参数当前的设置值。

## 4.37 HUGE\_WITH\_DELTA

是否仅允许创建事务型 HUGE 表。1：是；0：否。缺省值为 1。可选参数。

设置为 1 时，仅允许创建事务型 HUGE 表，不允许创建非事务型 HUGE 表。若需要创建非事务型 HUGE 表，在创建数据库时需要将参数 HUGE\_WITH\_DELTA 和 RLOG\_GEN\_FOR\_HUGE 都置为 0。

此参数在数据库创建成功后无法修改，可通过查询 V$PARAMETER 或 V$DM\_INI 中的 HUGE\_WITH\_DELTA 参数名查看此参数的设置值，还可以通过使用系统函数获取此参数的设置值：select SF\_GET\_PARA\_VALUE(2,'HUGE\_WITH\_DELTA');。

## 4.38 RLOG\_GEN\_FOR\_HUGE

是否生成 HUGE 表 REDO 日志。1：是；0：否。缺省值为 1。可选参数。

参数值 1 仅在 HUGE\_WITH\_DELTA=1 时才有效，也就是仅限于对事务型 HUGE 表设置是否生成 REDO 日志。

此参数在数据库创建成功后无法修改，可通过查询 V$PARAMETER 或 V$DM\_INI 中的 RLOG\_GEN\_FOR\_HUGE 参数名查看此参数的设置值，还可以通过使用系统函数获取此参数的设置值：select SF\_GET\_PARA\_VALUE(2,'RLOG\_GEN\_FOR\_HUGE');。

## 4.39 PSEG\_MGR\_FLAG

是否仅使用管理段记录事务信息。1：是；0：否。缺省值为 0。可选参数。

配置为 1 时，仅在管理段中记录事务信息；

配置为 0 时，除了在管理段中记录事务信息外，还会在事务分配的首个回滚页中记录事务信息。 这种方式支持将带有管理段的数据库降级到支持管理段之前的版本。

配置为 0 和配置为 1 的降级策略有所不同，具体请咨询达梦技术服务人员。

此参数在数据库创建成功后无法修改，可通过查询 V$PARAMETER 或 V$DM\_INI 中的 PSEG\_MGR\_FLAG 参数名查看此参数的设置值，还可以通过使用系统函数获取此参数的设置值：select SF\_GET\_PARA\_VALUE(2,'PSEG\_MGR\_FLAG');。

## 4.40 CHAR\_FIX\_STORAGE

定长字符（CHAR）是否按定长存储，取值范围为：Y/N，1/0。缺省为 N，可选参数。

Y/1：表示定长字符（CHAR）按定长存储，即不允许 CHAR 变化为 VARCHAR2 进行存储；

N/0：表示定长字符（CHAR）按变长存储，即允许 CHAR 变化为 VARCHAR2 进行存储。

此参数在数据库创建成功后无法修改，可通过使用系统函数获取此参数的设置值：select SF\_GET\_PARA\_VALUE(2,'CHAR\_FIX\_STORAGE');。

## 4.41 SQL\_LOG\_FORBID

是否禁止打开 SQL 日志，取值范围为：Y/N，1/0。

Y/1：是；N/0：否。缺省为 N，可选参数。此功能禁用之后，无法再通过任何方式打开 SQL 日志。

例如，当 SQL\_LOG\_FORBID=1 后，即使开启 DM\_INI 的 SVR\_LOG 也不会打印 SQL 日志。

此参数在数据库创建成功后无法修改，可通过使用系统函数获取此参数的设置值：select SF\_GET\_PARA\_VALUE(2,'SQL\_LOG\_FORBID');。

## 4.42 DPC\_MODE

DMDPC 专用参数。指定 DMDPC 集群中的实例角色。取值范围为：0、1/MP、2/BP、3/BP，缺省为 0，可选参数。

0：无；1/MP：MP；2/BP：BP；3/SP：SP。

DPC\_MODE 参数值既可以使用数字 0/1/2/3，也可以使用 MP/BP/SP 字符串代替，二者作用等价。

此参数在数据库创建成功后无法修改，可通过查询 VPARAMETER或VDM\_INI 中的 DPC\_MODE 参数名查看此参数的设置值，还可以通过使用系统函数获取此参数的设置值：select SF\_GET\_PARA\_VALUE(2,'DPC\_MODE');。

## 4.43 SYSSSO\_PWD

初始化时设置数据库安全员 SYSSSO 的密码，不允许缺省。密码为字符串，必须同时包含大写字母、小写字母、数字，不允许与用户名重名，密码长度须大于或等于 INI 参数 PWD\_MIN\_LEN 所设定的值且小于 48，关于参数 PWD\_MIN\_LEN 的详细说明请参考《DM8 系统管理员手册》。

如果密码中包含特殊字符，则需要按照规定的书写规范进行书写，详细请参考《DM8\_DIsql 使用手册》中关于特殊字符的书写规范相关介绍。

仅在安全版本下可见和可设置。

数据库创建成功后，SYSSSO 可通过修改用户密码语句修改自己的密码。

## 4.44 SYSDBO\_PWD

初始化时设置数据库操作员 SYSDBO 的密码，不允许缺省。密码为字符串，必须同时包含大写字母、小写字母、数字，不允许与用户名重名，密码长度须大于或等于 INI 参数 PWD\_MIN\_LEN 所设定的值且小于 48，关于参数 PWD\_MIN\_LEN 的详细说明请参考《DM8 系统管理员手册》。

如果密码中包含特殊字符，则需要按照规定的书写规范进行书写，详细请参考《DM8\_DIsql 使用手册》中关于特殊字符的书写规范相关介绍。

仅在安全版本且 PRIV\_FLAG=1 时可见和可设置。

数据库创建成功后，SYSDBO 可通过修改用户密码语句修改自己的密码。

## 4.45 PRIV\_FLAG

是否是四权分立。1：是；0：否。缺省值为 0。可选参数。

为了保证数据库系统的安全性，DM 数据库采用“三权分立”或“四权分立”的安全机制，“三权分立”时系统内置三种系统管理员，包括数据库管理员、数据库安全员和数据库审计员，“四权分立”时新增了一类用户，称为数据库对象操作员。它们各司其职，互相制约，有效地避免了将所有权限集中于一人的风险，保证了系统的安全性。默认情况下为“三权分立”。

仅在安全版本下可见和可设置。

此参数在数据库创建成功后无法修改，可通过查询 V$PARAMETER 或 V$DM\_INI 中的 GLOBAL\_PRIV\_FLAG 参数名查看此参数的设置值，还可以通过使用系统函数获取此参数的设置值：select SF\_GET\_PARA\_VALUE(2,'GLOBAL\_PRIV\_FLAG');。

## 4.46 MAIN\_DBF\_PATH

初始化 MAIN.DBF 数据文件的存放路径。文件路径长度最大为 256 个字符。可选参数。

默认情况下 Windows 存放在 PATH\\DB\_NAME 下，Linux 存放在/PATH/DM\_NAME 下（PATH 和 DB\_NAME 表示各自设置的值）。文件名固定为 MAIN.DBF。

该路径不允许是 HUGE\_PATH 路径及其子目录。（HUGE\_PATH 默认为 PATH\\DB\_NAME\\HMAIN）。

## 4.47 SYSTEM\_DBF\_PATH

初始化 SYSTEM.DBF 数据文件的存放路径。文件路径长度最大为 256 个字符。可选参数。

默认情况下 Windows 存放在 PATH\\DB\_NAME 下，Linux 存放在/PATH/DM\_NAME 下（PATH 和 DB\_NAME 表示各自设置的值）。文件名固定为 SYSTEM.DBF。

该路径不允许是 HUGE\_PATH 路径及其子目录。（HUGE\_PATH 默认为 PATH\\DB\_NAME\\HMAIN）。

## 4.48 ROLL\_DBF\_PATH

初始化 ROLL.DBF 数据文件的存放路径。文件路径长度最大为 256 个字符。可选参数。

默认情况下 Windows 存放在 PATH\\DB\_NAME 下，Linux 存放在/PATH/DM\_NAME 下（PATH 和 DB\_NAME 表示各自设置的值）。文件名固定为 ROLL.DBF。

该路径不允许是 HUGE\_PATH 路径及其子目录。（HUGE\_PATH 默认为 PATH\\DB\_NAME\\HMAIN）。

## 4.49 TEMP\_DBF\_PATH

初始化 TEMP.DBF 数据文件的存放路径。文件路径长度最大为 256 个字符。可选参数。

默认情况下 Windows 存放在 PATH\\DB\_NAME 下，Linux 存放在/PATH/DM\_NAME 下（PATH 和 DB\_NAME 表示各自设置的值）。文件名固定为 TEMP.DBF。

该路径不允许是 HUGE\_PATH 路径及其子目录。（HUGE\_PATH 默认为 PATH\\DB\_NAME\\HMAIN）。

## 4.50 USE\_DB\_NAME

初始化数据库的路径是否拼接 DB\_NAME。Y、y、1：是；N、n、0：否。缺省值为 1。可选参数。

例如 dm.ini 的默认路径在 USE\_DB\_NAME 配置为 1 时是 PATH\\DB\_NAME\\dm.ini；在 USE\_DB\_NAME 配置为 0 时是 PATH\\dm.ini。

## 4.51 ENABLE\_MAC

是否打开强制访问控制功能，仅对安全版有效。1: 是；0: 否。缺省值为 0。可选参数。

此参数在数据库创建成功后无法修改，可以通过使用系统函数 SF\_GET\_PARA\_VALUE 获取此参数的设置值。

## 4.52 RANDOM\_CRYPTO

指定数据库中使用的随机数算法所在的加密引擎名。未指定或指定的加密引擎不存在，又或者指定的加密引擎中不存在随机数算法，则使用 OPENSSL 提供的软件随机数算法。支持的加密引擎名可以通过查询视图 V$EXTERNAL\_CIPHER\_LIBS 的 NAME 列获取。

数据库创建成功后，可通过修改 INI 参数 RANDOM\_CRYPTO 的值对此参数的设置进行修改。可通过查询 V$PARAMETER 或 V$DM\_INI 中的 RANDOM\_CRYPTO 参数名查看此参数的设置值。

## 4.53 AUTO\_ADJ\_PARA

是否对 CPU 和内存相关 INI 参数进行自动调优。1：是；0：否，缺省值为 1，为 1 时 AUTO\_ADJ\_CPUS、AUTO\_ADJ\_MEM 才生效。可选参数。

## 4.54 AUTO\_ADJ\_CPUS

指定数据库可用 CPU 核数进行 INI 参数自动调优，AUTO\_ADJ\_PARA 打开才生效。取值范围 0~64，缺省值为 0，默认根据当前所有 CPU 对于相关 INI 进行调优。可选参数。

CPU 相关的优化参数有：WORKER\_THREADS、IO\_THR\_GROUPS、TASK\_THREADS。

表4.1 CPU核数相关INI调整策略表

| CPU 核数 | <=8 | \>8, <=64 | \>64 |
| --- | --- | --- | --- |
| WORKER\_THREADS | CPU 核数 | CPU 核数 | 64 |
| IO\_THR\_GROUPS | 8 | 16 | 32 |
| TASK\_THREADS | 8 | 16 | 32 |

## 4.55 AUTO\_ADJ\_MEM

指定数据库可用内存大小进行 INI 参数自动调优，AUTO\_ADJ\_PARA 打开才生效。最大取值为 8 位整数，单位：MB，缺省值为 0，默认使用当前机器 80% 的内存对于相关 INI 进行调优。可选参数。

内存相关的优化参数有：MEMORY\_POOL、MEMORY\_N\_POOLS、MEMORY\_TARGET、BUFFER、BUFFER\_POOLS、RECYCLE、RECYCLE\_POOLS、HJ\_BUF\_GLOBAL\_SIZE、HJ\_BUF\_SIZE、HAGR\_BUF\_GLOBAL\_SIZE、HAGR\_BUF\_SIZE、SORT\_FLAG、SORT\_BLK\_SIZE、SORT\_BUF\_SIZE、SORT\_BUF\_GLOBAL\_SIZE、RLOG\_POOL\_SIZE、CACHE\_POOL\_SIZE、DICT\_BUF\_SIZE、VM\_POOL\_TARGET、SESS\_POOL\_TARGET、MAX\_SESSIONS。

请注意若指定或默认内存小于 4G，则不会进行内存相关参数调优，使用默认参数；若指定内存大于实际内存会输出警告，建库会成功，可能因 INI 参数优化导致未知问题，请谨慎设置此建库参数。当指定或默认内存值大于等于 4G 时，内存相关参数调整会根据指定或默认参数的 80% 为基准，按其一定比例和总大小进行优化，内存相关参数调整策略较复杂，具体请咨询达梦技术服务人员。

## 4.56 HELP

显示帮助信息。可选参数。