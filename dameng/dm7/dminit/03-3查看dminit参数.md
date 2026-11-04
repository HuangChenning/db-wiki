---
title: "3 查看dminit参数"
book: "DM7 dminit使用手册"
version: "DM7"
source: "temp/doc/special/DM7°ïÖúÎÄµµ.chm#~htm/dminit使用手册.htm"
tags:
  - dameng
  - dm7
  - dminit
---

`dminit`使用较为灵活，参数较多。用户可使用`“dminit HELP”`快速查看各参数。

```
dminit HELP
格式: dminit KEYWORD=value
例如: dminit PATH=c:\dm7data PAGE_SIZE=16
关键字 说明（默认）
-----------------------------------------------------------------------------
INI_FILE 初始化文件dm.ini存放的路径
PATH 初始数据库存放的路径
CTL_PATH 控制文件路径
LOG_PATH 日志文件路径
EXTENT_SIZE 数据文件使用的簇大小(16)，可选值：16、32，单位：页
PAGE_SIZE 数据页大小(8)，可选值：4、8、16、32，单位：K
LOG_SIZE 日志文件大小(256)，单位为：M，范围为：64M ~ 2G
CASE_SENSITIVE 大小敏感(Y)，可选值：Y/N，1/0
CHARSET/UNICODE_FLAG 字符集(0)，可选值：0[GB18030]，1[UTF-8]，2[EUC-KR]
LENGTH_IN_CHAR VARCHAR类型长度是否以字符为单位(N)，可选值：Y/N，1/0
SYSDBA_PWD 设置SYSDBA密码(SYSDBA)，密码长度为6到48
SYSAUDITOR_PWD 设置SYSAUDITOR密码(SYSAUDITOR)，密码长度为6到48
DB_NAME 数据库名(DAMENG)
INSTANCE_NAME 实例名(DMSERVER)
PORT_NUM 监听端口号(5236)
TIME_ZONE 设置时区(+08:00)
PAGE_CHECK 页检查模式(0)，可选值：0/1/2
RAC_NODE 高性能集群的节点数目，可选值: 2..16
EXTERNAL_CIPHER_NAME 设置默认加密算法
EXTERNAL_HASH_NAME 设置默认HASH算法
EXTERNAL_CRYPTO_NAME 设置根密钥加密引擎
SVR_KEY 设置服务器密钥
DB_KEY 设置库密钥
ENCRYPT_PWD 设置全库加密密码
RLOG_ENC_FLAG 设置日志文件是否加密(N)，可选值：Y/N，1/0
USBKEY_PIN 设置USBKEY PIN
ENCRYPT_NAME 设置全库加密算法
BLANK_PAD_MODE 设置空格填充模式(0)，可选值：0/1
SYSTEM_MIRROR_PATH SYSTEM数据文件镜像路径
MAIN_MIRROR_PATH MAIN数据文件镜像
ROLL_MIRROR_PATH 回滚文件镜像路径
SVR_MODE 设置系统的初始模式(0) 0：normal 1：primary 2：standby
MAL_FLAG 初始化时设置dm.ini中的MAL_INI(0)
ARCH_FLAG 初始化时设置dm.ini中的ARCH_INI(0)
MPP_FLAG Mpp系统内的库初始化时设置dm.ini中的mpp_ini(0)
CONTROL 初始化配置文件（配置文件格式见系统管理员手册）
AUTO_OVERWRITE 是否覆盖所有同名文件(0) 0:不覆盖 1:部分覆盖 2:完全覆盖
USE_NEW_HASH 是否使用改进的字符类型HASH算法(1)
DCP_MODE 是否是DCP代理模式(0)
DCP_PORT_NUM DCP代理模式下管理端口
SYSSSO_PWD 设置SYSSSO密码(SYSSSO)，密码长度为6到48
SYSDBO_PWD 设置SYSDBO密码(SYSDBO)，密码长度为6到48
PRIV_FLAG 设置权限标记，可选值：0、1
ELOG_PATH 指定初始化过程中生成的日志文件所在路径
HELP 打印帮助信息
```
