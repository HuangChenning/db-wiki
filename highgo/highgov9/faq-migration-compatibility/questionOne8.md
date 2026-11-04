---
title: "V9 MySQL模式报错：操作符不是唯一的character=character varying"
book: "迁移兼容类"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/question/questionOne8.html"
tags:
  - highgo
  - highgo-v9
  - faq-migration-compatibility
---

## 问题现象：

V9 MySQL兼容模式，操作符不是唯一的: character = character varying

## 解决方案：

创建 char = varchar 操作符

```
CREATE OR REPLACE FUNCTION char_varchar_equal(char1 CHAR, varchar1 VARCHAR)
RETURNS BOOLEAN AS $$
BEGIN
    RETURN TRIM(char1) = varchar1;
END;
$$ LANGUAGE plpgsql IMMUTABLE STRICT;

CREATE OPERATOR = (
    LEFTARG = CHAR,
    RIGHTARG = VARCHAR,
    PROCEDURE = char_varchar_equal
);
```