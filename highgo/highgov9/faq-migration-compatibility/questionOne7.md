---
title: "V9 MySQL模式报错：操作符不是唯一的character varying=character"
book: "迁移兼容类"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/question/questionOne7.html"
tags:
  - highgo
  - highgo-v9
  - faq-migration-compatibility
---

## 问题现象：

V9 MySQL兼容模式，操作符不是唯一的: character varying = character

## 解决方案：

创建 char = varchar 操作符

```
CREATE OR REPLACE FUNCTION varchar_char_equal(varchar1  VARCHAR, char1 CHAR)
RETURNS BOOLEAN AS $$
BEGIN
    RETURN varchar1=  TRIM(char1) ;
END;

$$ LANGUAGE plpgsql IMMUTABLE STRICT;
CREATE OPERATOR = (
    LEFTARG =  VARCHAR,
    RIGHTARG = CHAR,
    PROCEDURE = varchar_char_equal
);
```