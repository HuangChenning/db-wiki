---
title: "DBMS_XMLPARSER包"
book: "DM8 系统包使用手册"
version: "DM8"
source: https://eco.dameng.com/document/dm/zh-cn/pm/dbms_xmlparser-package.html
tags:
  - dameng
  - dm8
  - system-packages
---

DBMS\_XMLPARSER 包用于新建 PARSER，并通过 PARSER 可以访问 XML 文档的内容和结构。

## 55.1 数据类型

DBMS\_XMLPARSER 包定义了若干 XML 数据类型：

1. PARSER

XML 解析器，用于构建一个可通过 DOM API 访问的解析树。

## 55.2 相关方法

1. NEWPARSER

创建新的 PARSER。

**语法如下：**

FUNCTION NEWPARSER()RETURN DBMS\_XMLPARSER.PARSER;

**返回值**

创建的 PARSER 结点。

2. FREEPARSER

释放 PARSER。

**语法如下：**

```
PROCEDURE FREEPARSER(
   P IN DBMS_XMLPARSER.PARSER
);
```

**参数详解**

P：PARSER 类型结点。

3. PARSEBUFFER

解析存储在给定字符串缓冲区中的 XML。

**语法如下：**

```
PROCEDURE PARSEBUFFER(
   P IN DBMS_XMLPARSER.PARSER,
   DOC IN VARCHAR2
);
```

**参数详解**

P：PARSER 类型结点。

DOC：字符串类型 XML 数据。

4. PARSECLOB

解析存储在给定字符串缓冲区中的 XML。

**语法如下：**

```
PROCEDURE PARSECLOB(
   P IN DBMS_XMLPARSER.PARSER,
   DOC IN CLOB
);
```

**参数详解**

P：PARSER 类型结点。

DOC：CLOB 类型 XML 数据。

5. GETDOCUMENT

获取 PARSER 中的 DOCUMENT 结点。

**语法如下：**

```
FUNCTION GETDOCUMENTR(
   P IN DBMS_XMLPARSER.PARSER
)RETURN DBMS_XMLDOM.DOMDOCUMENT;
```

**参数详解**

P：PARSER 类型结点。

**返回值**

PARSER 中存储的 DOMDOCUMENT 类型结点。

6. GETDOCTYPE

获取 PARSER 中的 DOMDOCUMENTTYPE 结点。

**语法如下：**

```
FUNCTION GETDOCTYPE(
   P IN DBMS_XMLPARSER.PARSER
)RETURN DBMS_XMLDOM.DOMDOCUMENTTYPE;
```

**参数详解**

P：PARSER 类型结点。

**返回值**

PARSER 中存储的 DOMDOCUMENTTYPE 类型结点。

7. SETDOCTYPE

设置 PARSER 中的 DOMDOCUMENTTYPE 结点。

**语法如下：**

```
PROCEDURE SETDOCTYPE(
   P IN DBMS_XMLPARSER.PARSER,
   DTD IN DBMS_XMLDOM.DOMDOCUMENTTYPE
);
```

**参数详解**

P：PARSER 类型结点。

DTD：DOMDOCUMENTTYPE 结点。

8. GETRELEASEVERSION

返回用于 PL/SQL 的 XML 分析器发布版本。

**语法如下：**

```
FUNCTION RESETPARAMS()RETURN VARCHAR2;
```

**返回值**

版本信息字符串。

9. SETVALIDATIONMODE

设置验证模式。

**语法如下：**

```
PROCEDURE SETVALIDATIONMNODE(
   P IN DBMS_XMLPARSER.PARSER,
   YES IN BOOLEAN
);
```

**参数详解**

P：PARSER 类型结点。

YES：设置模式：TRUE 为验证，FALSE 为不验证。

10. GETVALIDATIONMODE

获取验证模式。

**语法如下：**

```
FUNCTION SETVALIDATIONMNODE(
   P IN DBMS_XMLPARSER.PARSER
)RETURN BOOLEAN;
```

**参数详解**

P：PARSER 类型结点。

**返回值**

是否验证模式，TRUE 为验证，FALSE 为不验证。

11. PARSE

解析存储在 URL 或文件中的 XML。

**语法如下：**

```
FUNCTION PARSE(
   URL IN VARCHAR2
)RETURN DBMS_XMLDOM.DOMDOCUMENT;

PROCEDURE PARSE(
   P IN DBMS_XMLPARSER.PARSER,
   URL IN VARCHAR2
);
```

**参数详解**

P：PARSER 类型结点。

URL：待解析的 URL/文件的完整路径。

**返回值**

解析生成的 DOMDOCUMENT 类型节点。

12. SETBASEDIR

设置用于解析相对 URL 的基础目录。

**语法如下：**

```
PROCEDURE SETBASEDIR (
   P IN DBMS_XMLPARSER.PARSER,
   DIR IN VARCHAR2
);
```

**参数详解**

P：PARSER 类型结点。

DIR：字符串类型基础路径。

13. GETBASEDIR

获取 PARSER 中解析相对 URL 的基础目录。

**语法如下：**

```
FUNCTION GETBASEDIR (
   P IN DBMS_XMLPARSER.PARSER
)RETURN VARCHAR2;
```

**参数详解**

P：PARSER 类型结点。

**返回值**

字符串类型基础路径。

14. PARSEDTD

解析存储在给定 URL 或文件中的 DTD。

**语法如下：**

```
PROCEDURE PARSEDTD(
   P IN DBMS_XMLPARSER.PARSER,
   URL IN VARCHAR2,
   ROOT IN VARCHAR2
);
```

**参数详解**

P：PARSER 类型结点。

URL：待解析的 URL/文件的完整路径。

ROOT：根元素的名称。

15. PARSEDTDBUFFER

解析存储在给定缓冲区中的 DTD。

**语法如下：**

```
PROCEDURE PARSEDTDBUFFER(
   P IN DBMS_XMLPARSER.PARSER,
   DTD IN VARCHAR2,
   ROOT IN VARCHAR2
);
```

**参数详解**

P：PARSER 类型结点。

DTD：字符串类型 DTD。

ROOT：根元素的名称。

16. PARSEDTDCLOB

解析存储在给定 CLOB 数据中的 DTD。

**语法如下：**

```
PROCEDURE PARSEDTDCLOB(
   P IN DBMS_XMLPARSER.PARSER,
   DTD IN CLOB,
   ROOT IN VARCHAR2
);
```

**参数详解**

P：PARSER 类型结点。

DTD：CLOB 类型 DTD。

ROOT：根元素的名称。

## 55.3 举例说明

使用包内的过程和函数之前，如果还未创建过系统包，请先调用系统过程创建系统包。

```
SP_CREATE_SYSTEM_PACKAGES (1,'DBMS_XMLPARSER');
```
```
以下是新建一个PARSER，通过PARSERBUFFER解析XML字符串，之后获取解析生成的DTD与DOCUMENT，最后释放PARSER。
```
```
DECLARE
   myparser DBMS_XMLPARSER.PARSER;
   doctype DBMS_XMLDOM.DOMDOCUMENTTYPE;
   doc DBMS_XMLDOM.DOMDOCUMENT;
BEGIN
   myparser := DBMS_XMLPARSER.newParser;
   DBMS_XMLPARSER.PARSEBUFFER(myparser, '<?xml version="1.0"?><!DOCTYPE test SYSTEM "test.dtd"><test/>');
   doctype :=DBMS_XMLPARSER.GETDOCTYPE(myparser);
   doc := DBMS_XMLPARSER.GETDOCUMENT(myparser);
   DBMS_XMLPARSER.FREEPARSER(myparser);
END;
/
```