---
title: "UTL_MAIL 包"
book: "DM8 系统包使用手册"
version: "DM8"
source: https://eco.dameng.com/document/dm/zh-cn/pm/utl_mail-package.html
tags:
  - dameng
  - dm8
  - system-packages
---

为了在 PL/SQL 中，提供 email 发送的支持，开发 UTL\_MAIL 包，提供一组 API，实现发送简单的邮件和包含附件的邮件。服务器默认不安装 UTL\_MAIL 包，需要用户主动通过系统函数 SP\_CREATE\_SYSTEM\_PACKAGES 指定包名方式进行创建。UTL\_MAIL 包中的配置信息将以明文传输，存在邮件密码泄露的风险，建议谨慎开启 UTL\_MAIL 包，可由 UTL\_SMTP 包替代相关功能。

## 26.1 相关方法

1. INIT

包需要的配置信息。

**语法如下：**

```
PROCEDURE INIT(
    SMTP_SERVER        VARCHAR2(128),
    SMTP_PORT        INT         DEFAULT 25,
    SENDER            VARCHAR2(128),
    PASSWORD        VARCHAR2(128)
);
```

**参数详解**

- SMPT\_SERVER smtp 服务器的地址，如 smtp.163.com。
- SMTP\_PORT smtp 的端口号，一般都是 25。
- SENDER 设置发送的邮箱，也就是要认证的邮箱。
- PASSWORD 设置发送邮箱的密码。
2. SEND

发送 message 的信息。

**语法如下：**

```
PROCEDURE SEND (
    SENDER         IN         VARCHAR2,
    RECIPIENTS     IN         VARCHAR2,
    CC             IN         VARCHAR2     DEFAULT NULL,
    BCC         IN         VARCHAR2     DEFAULT NULL,
    SUBJECT     IN         VARCHAR2     DEFAULT NULL,
    MESSAGE     IN         VARCHAR2,
    MIME_TYPE     IN         VARCHAR2     DEFAULT 'TEXT/PLAIN; CHARSET=US-ASCII',
    PRIORITY     IN         INT         DEFAULT NULL
);
```

**参数详解**

- SENDER 发送的邮箱地址。
- RECIPIENTS 接收邮件的地址。
- CC 抄送的邮件的地址。
- BCC 秘密抄送的邮件的地址。
- SUBJECT 邮件的主题。
- MESSAGE 邮件的内容，正文部分。
- MIME\_TYPE 邮件的内容格式，default is 'text/plain; charset=us-ascii'。
- PRIORITY 优先级（不用设置）。
3. SEND\_ATTACH\_RAW

发送带附件的邮件。

**语法如下：**

```
PROCEDURE SEND_ATTACH_RAW (
    SENDER             IN         VARCHAR2,
    RECIPIENTS         IN         VARCHAR2,
    CC                 IN         VARCHAR2     DEFAULT NULL,
    BCC             IN         VARCHAR2     DEFAULT NULL,
    SUBJECT         IN         VARCHAR2     DEFAULT NULL,
    MESSAGE         IN         VARCHAR2     DEFAULT NULL,
    MIME_TYPE         IN         VARCHAR2     DEFAULT 'TEXT/PLAIN; CHARSET=US-ASCII',
    PRIORITY         IN         INT         DEFAULT NULL,
    ATTACHMENT         IN         BLOB,
    ATT_INLINE         IN         BOOLEAN     DEFAULT TRUE,
    ATT_MIME_TYPE     IN         VARCHAR2     DEFAULT 'APPLICATION/OCTET-STREAM',
    ATT_FILENAME     IN         VARCHAR2     DEFAULT NULL
);
```

**参数详解**

- SENDER 发送的邮箱地址。
- RECO\[OEMTS 接收邮件的地址。
- CC 抄送的邮件的地址。
- BCC 秘密抄送的邮件的地址。
- SUBJECT 邮件的主题。
- MESSAGE 邮件的内容，正文部分。
- MIME\_TYPE 邮件的内容格式：文本、html 等。缺省为'text/plain;charset=us-ascii'。
- PRIORITY 优先级（不用设置）。
- ATTACHMENT 附件。
- ATT\_INLINE 附件在文件中显示是否使用下划线。
- ATT\_MIME\_TYPE 邮件附件的类型，如文本。
- ATT\_FILENAME 附件的文件名。

## 26.2 举例说明

使用包内的过程和函数之前，如果还未创建过系统包，请先调用系统过程创建系统包。

```
SP_CREATE_SYSTEM_PACKAGES (1,'UTL_MAIL');
```

例 在使用该包前，需要先初始化该包，调用 init 函数，设置使用 smtp 服务器，端口（一般默认 25，设置用于认证的邮箱，认证的密码。设置完后，就可以使用包的函数：send 和 send\_attach\_raw。

```
//初始化包的函数
UTL_MAIL.INIT(
    'SMTP.163.COM',  //SMTP 服务器
    25,  //端口
    'UTL_MAIL@163.COM',  //认证的邮箱
    'DM_UTL_MAIL'  //认证邮箱的密码
);
//发送不带附件的邮件
UTL_MAIL.SEND(
    'UTL_MAIL@163.COM',  //发送的邮箱地址
    'RECIPIENT@DAMENG.COM',  //接受的邮箱地址
    '',
    '',
    'TEST',  //主题
    'THIS IS A MAIL FOR TEST .',      //正文
    'TEXT/PLAIN; CHARSET=US-ASCII',  //类型
    3
); 
//发送带附件的邮件 
UTL_MAIL.SEND_ATTACH_RAW(
    'UTL_MAIL@163.COM',
    'RECIPIENT@DAMENG.COM',
    '',
    '',
    'TEST',
    'THIS IS A MAIL FOR TEST .',
    'TEXT/PLAIN; CHARSET=US-ASCII',
    3,
    HEXTORAW('1234567890564531813169434196431651398320843126465465465465461564'),  //附件二进制的内容
    FALSE,
    'APPLICATION/OCTET-STREAM',  //附件的类型
    'ATTACH.ZIP'      //附件的名字
);
```