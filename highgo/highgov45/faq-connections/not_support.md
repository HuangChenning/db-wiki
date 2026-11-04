---
title: "10、旧版 JDK 连接数据库时报 TLS 密码套件不支持"
book: "连接使用类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/question/not_support.html"
tags:
  - highgo
  - highgo-v45
  - faq-connections
---

## 标题

**【JDBC／SSL】Oracle JDK 1.8.0\_02xx 连接数据库报 TLS 密码套件不支持，更换 OpenJDK 1.8.0-4xxx 后恢复正常**

---

## 适用范围

- Java 应用通过 `JDBC` 连接数据库
- 使用 `Highgo JDBC` 、 `PostgreSQL JDBC` 或兼容驱动
- 连接启用了 `SSL／TLS`
- 运行环境为 `JDK 8`
- 报错中出现 `CipherSuite` 、 `providers` 、 `enableSSL` 等关键词

---

## 现象描述

应用连接数据库失败，日志中出现如下异常：

```
java.lang.IllegalArgumentException:
Cannot support TLS_DHE_RSA_WITH_AES_256_GCM_SHA384 with currently installed providers
```

相关调用栈示意如下：

```
at sun.security.ssl.CipherSuiteList.<init>(CipherSuiteList.java:92)
at sun.security.ssl.SSLSocketImpl.setEnabledCipherSuites(SSLSocketImpl.java:2440)
at com.highgo.jdbc.ssl.MakeSSL.convert(MakeSSL.java:61)
at com.highgo.jdbc.core.v3.ConnectionFactoryImpl.enableSSL(ConnectionFactoryImpl.java:609)
at com.highgo.jdbc.Driver.connect Unexpected connection error
```

---

## 问题简述

在 **Oracle JDK 1.8.0\_02xx** 环境下，Java 应用通过 `Highgo JDBC` 连接数据库时，因当前 `JVM` 安全提供者不支持 `TLS_DHE_RSA_WITH_AES_256_GCM_SHA384` 密码套件，导致数据库连接失败。

将运行时更换为 **OpenJDK 1.8.0-4xxx** 后，连接恢复正常。

---

## 影响范围

- 启用 `SSL／TLS` 的数据库连接会失败
- 应用连接池无法正常创建连接
- 依赖数据库的业务功能不可用
- 若问题发生在生产环境，可能导致：
	- 应用启动失败；
		- 数据源初始化失败；
		- 部分或全部业务中断

---

## 根因分析

### 根因结论

本问题根因不是数据库实例异常，而是 **旧版 Oracle JDK 运行时的 TLS／JCE／Security Provider 能力，与 JDBC 驱动启用的密码套件不兼容** 。

### 具体分析

报错核心为：

```
Cannot support TLS_DHE_RSA_WITH_AES_256_GCM_SHA384 with currently installed providers
```

其含义是：

- 当前 `JVM` 已安装的安全提供者不支持目标密码套件；
- 异常发生在 `SSLSocketImpl.setEnabledCipherSuites()` 阶段；
- 问题出现在客户端 `SSL` 握手准备阶段；
- 数据库连接尚未进入真正的认证或 SQL 执行阶段。

### 为什么可以判定不是数据库本身问题

因为本次验证结果为：

- 原先： `Oracle JDK 1.8.0_02xx` ，连接失败；
- 更换： `OpenJDK 1.8.0-4xxx` ，连接正常。

数据库端、应用代码、驱动使用方式未发生本质变化，唯一关键变量是 `JVM` ，因此可以确认问题定位在客户端运行时。

---

## 触发条件

满足以下条件时较易触发：

- 使用较老的 `Oracle JDK 8` 更新版本；
- JDBC URL 启用了 `SSL` ；
- 驱动要求启用 `TLS_DHE_RSA_WITH_AES_256_GCM_SHA384` 等套件；
- 当前 `JVM` 的 `Provider` 、 `JCE` 策略或 `java.security` 配置不满足要求。

---

## 排查过程

### 1．确认报错位置

从异常堆栈定位到：

```
sun.security.ssl.SSLSocketImpl.setEnabledCipherSuites
```

说明问题发生在 `JVM TLS` 层，而非数据库 SQL 层。

### 2．确认是否启用 SSL

检查 JDBC 连接串或连接池配置，确认是否存在：

```
ssl=true
sslmode=require
```

### 3．比对运行时差异

对比发现：

- `Oracle JDK 1.8.0_02xx` ：失败
- `OpenJDK 1.8.0-4xxx` ：成功

### 4．收敛结论

由此确认：

- 网络不是主因；
- 数据库监听不是主因；
- 账号密码不是主因；
- 根因在 `JVM TLS` 能力兼容性。

---

## 解决方案

### 最终解决方案

将应用运行时从：

```
Oracle JDK 1.8.0_02xx
```

更换为：

```
OpenJDK 1.8.0-4xxx
```

更换后，数据库连接恢复正常。

---

## 替代方案

若必须继续使用 `Oracle JDK` ，建议：

- 不再使用 `1.8.0_02xx` 这一老版本；
- 直接升级到较新的 `Oracle JDK 8` 更新版；
- 工程上建议至少使用 `8u3xx` 及以上版本；
- 更推荐使用较新的 `8u381+` 档位。

---

## 经验结论

### 结论一

数据库连接失败，不一定是数据库问题。  
在 `JDBC + SSL` 场景中， `JVM` 、 `JSSE` 、 `JCE` 、 `Security Provider` 也是关键链路组成部分。

### 结论二

不能只写“支持 Java 8”，必须明确到：

- 发行版；
- 更新号；
- 实际运行路径。

例如：

- `Oracle JDK 1.8.0_02xx`
- `OpenJDK 1.8.0-4xxx`

虽然都属于 `Java 8` ，但 `TLS` 行为可能明显不同。

### 结论三

当日志中出现以下关键词时，应优先排查 `JVM TLS` 能力：

- `enableSSL`
- `CipherSuite`
- `currently installed providers`
- `setEnabledCipherSuites`

---

## 标准结论话术

可用于故障报告、复盘材料或对外说明：

> 应用连接数据库时报 `Cannot support TLS_DHE_RSA_WITH_AES_256_GCM_SHA384 with currently installed providers` 。排查确认并非数据库实例故障，而是旧版 Oracle JDK 1.8.0\_02xx 的 TLS／JCE Provider 能力与 JDBC 驱动的 SSL 连接要求不兼容。将运行时更换为 OpenJDK 1.8.0-4xxx 后，目标 TLS 密码套件获得支持，数据库连接恢复正常。

---

## 建议纳入的运维规范

### 1．版本规范

对启用 JDBC `SSL` 的 Java 应用，不允许仅描述为“Java 8”，必须明确：

- `JDK` 发行版；
- 更新号；
- `JAVA_HOME` ；
- 实际运行时路径。

### 2．上线检查项

上线前增加检查：

```bash
java -version
which java
echo $JAVA_HOME
```

Windows 环境可增加：

```bash
where java
echo %JAVA_HOME%
```

### 3．兼容性基线

对数据库连接类应用，建立以下兼容性矩阵：

---

## 关键词

`JDBC` 、 `SSL` 、 `TLS` 、 `CipherSuite` 、 `Provider` 、 `Oracle JDK` 、 `OpenJDK` 、 `Highgo JDBC` 、 `Java 8` 、 `数据库连接失败`

---

## 标签

- `Java`
- `JDBC`
- `SSL`
- `TLS`
- `JDK 兼容性`
- `数据库连接`
- `故障案例`
- `运行时问题`

---

## 后记

本案例最重要的价值，不在于“换了一个 `JDK` 就好了”，而在于明确了一条排障原则：

> **凡是 JDBC 报错中出现 TLS 密码套件、Provider、SSL 握手相关关键词，优先检查 JVM 运行时能力，而不是先从数据库实例本身入手。**

这条经验适用于 `Highgo` 、 `PostgreSQL` 以及大多数基于 Java 驱动连接数据库的场景。