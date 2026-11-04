---
title: "pgpass加密"
book: "安全指南"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/safety/safeOne5.html"
tags:
  - highgo
  - highgo-v9
  - safety-security-guide
---

## pgpass加密

pgpass文件主要用于存储瀚高数据库的连接密码，以便用户在不直接输入密码的情况下进行数据库的访问。瀚高数据库支持对pgpass文件中密码部分进行加密，避免密码硬编码在脚本中或在命令行历史记录中暴露，从而增强系统安全性。

## pg\_pgpass加解密工具

新增pg\_pgpass加解密工具对pgpass文件中password字段进行加解密处理，客户端访问pgpass时自动识别是否为密文password，对密文password先解密再使用。pg\_pgpass工具解密pgpass文件必须使用与加密时使用的密钥相同，否则解密失败。

pg\_pgpass加密或解密密钥由内置固定密钥和可选的数据库ID、设备MAC地址、自定义密码共同做为密钥种子生成。已加密pgpass文件不可被再次加密；对于pgpass文件中的相同的password加密后密文不一样；对于pgpass文件中的同一个password每次加密后的密文都不一样。

```
pg_pgpass - 加密或解密 .pgpass 文件。
```

**命令**

```
pg_pgpass [OPTION] [DATADIR]
```

**选项**

```
-d

解密.pgpass文件。如果不指定该参数，表示加密.pgpass文件。

[-P, --pgpass=] PGPASSFILE

指定.pgpass目录。

[-D, --pgdata=]

指定数据库的data目录，表示使用数据库ID加密.pgpass文件。

[-M, --interface=]

获取指定网卡的 MAC 地址，表示使用MAC地址加密.pgpass文件。

[-C, --customkey=]

指定自定义密钥，表示使用自定义密钥加密.pgpass文件。

-V

--version

输出版本信息，然后退出。

-?

--help

显示帮助信息，然后退出。
```

## 服务器端加解密

服务器端加密方式如下：

使用固定密钥加密：

```
./pg_pgpass .pgpass
```

使用固定密钥、数据库ID加密：

```
./pg_pgpass -D../data .pgpass
```

使用固定密钥、数据库ID、本机MAC地址加密：

```
./pg_pgpass -D../data -Mens33 .pgpass
```

使用固定密钥、数据库ID、本机MAC地址、自定义密码加密：

```
./pg_pgpass -D../data -Mens33 -C123456 .pgpass
```

在使用pg\_pgpass工具加密时，需要按照hostname:port:database:username:password标准格式编写pgpass文件，该工具只加密用户密码部分，其它ip、端口、用户名等部分不会加密。

服务器端解密方式如下：

使用固定密钥解密：

```
./pg_pgpass -d .pgpass
```

使用固定密钥、数据库ID解密：

```
./pg_pgpass -d -D../data .pgpass
```

使用固定密钥、数据库ID、本机MAC地址解密：

```
./pg_pgpass -d -D../data -Mens33 .pgpass
```

使用固定密钥、数据库ID、本机MAC地址、自定义密码解密：

```
./pg_pgpass -d -D../data -Mens33 -C123456 .pgpass
```

psql等客户端使用pgpass文件登录时，可以识别未加密的pgpass文件，也可以识别已加密的pgpass文件。psql解密pgpass文件中的password字段使用的密钥由内置固定密钥和可选的数据库ID、设备MAC地址、自定义密码共同生成，这里与服务器端pg\_pgpass加密密钥必须保持一致。

## 客户端解密登录

客户端解密登录方式如下：

使用固定密钥：

```
./psql
```

使用固定密钥、数据库ID解密：

```
./psql -D../data
```

使用固定密钥、数据库ID、本机MAC地址解密：

```
./psql -D../data -M ens33
```

使用固定密钥、数据库ID、本机MAC地址、自定义密码解密：

```
./psql -D../data -M ens33 -C 123456
```

注意：

psql使用.pgpass文件通过libpq参数passfile或环境变量PGPASSFILE指定

提示：

psql之外的其他客户端工具，只支持使用固定密钥加密后的pgpass。