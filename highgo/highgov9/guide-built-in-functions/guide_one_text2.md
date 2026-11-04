---
title: "二进制串函数"
book: "常用内置函数"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/guide/guide_one_text2.html"
tags:
  - highgo
  - highgo-v9
  - guide-built-in-functions
---

## 二进制串函数

常见的二进制函数

| 函数 | 返回类型 | 描述 | 例子 | 结果 |
| --- | --- | --- | --- | --- |
| octet\_length(st ring) | int | 二进制串中的字 节数 | octet\_length(‘jo \\000se’::bytea) | 5 |
| overlay(stringplacing stringfrom int \[for int\]) | bytea | 替换子 串 | overlay(‘Th\\000omas’::bytea placing’\\002\\003’::bytea from 2 for 3) | T\\002\\003 mas |
| position(substr ingin string) | int | 指定子串的位 置 | position(‘\\000om’in ‘Th \\000omas’::bytea) | ‘::bytea |
| substring(strin g\[from int\] \[for int\]) | bytea | 提取子 串 | substring(‘Th\\000omas’::bytea from 2 for 3) | h\\000o |
| trim(\[both\]bytes from string) | bytea | 从 string 的开头或结尾删除只包含出现在bytes中字节的最长串 | trim(‘\\000\\001’::bytea from ‘\\000Tom\\001’::bytea) |  |
| btrim(stringbytea, bytes bytea) | bytea | 从 string 的开头或 结尾删除只由出 现在 bytes 中字节 组成的最长串 | btrim(‘\\000trim\\001’::bytea,’\\000\\001’::bytea) | trim |
| decode(strin gtext, format text) | bytea | 从 string 中的文本表示解码二进制数据。format 的参数和在 encode中一样。 | decode(‘ 123\\0004 56’’escape’) | 000456 |
| encode(data bytea,format text) | text | 将二进制数据编码为一个文本表示。支持的格式有：base64 、hex、escape 。escape 将零字节和高位组字节转换为八进 | encode(‘ 123\\0004 56’::bytea,’escape’) | ::bytea, |
| get\_bit(strin g,offset) | int | 从串中抽取位 | get\_bit(‘Th\\000omas’::bytea, 45) | 1 |
| get\_byte(str ing,offset) | int | 从串中抽取字节 | get\_byte(‘Th\\000omas’::bytea, 4) | 109 |
| length(strin g) | int | 二进制串的长度 | length(‘jo\\000se’::bytea) | 5 |
| md5(string) | text | 计算 string 的 MD5 哈希码，以十六进 制形式返回结果 | md5(‘Th\\000omas’::bytea) | 8ab2d3c96 89aaf18b4958c334 c82d8b1 |
| sha224(byte a) | bytea | SHA-224 哈希 | sha224(‘abc’) | \\x23097d223405d8228642a477bda255b32aadbce4bda0b3f |
| sha256(byte a) | bytea | SHA-256 哈希 | sha256(‘abc’) | \\xba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015 |
| sha384(byte a) | bytea | SHA-384 哈希 | sha384(‘abc’) | \\xcb00753f45a35e8bb5a03d699ac65007272c32ab0eded1631a8b605a43ff5bed8086072ba1e7cc2358baeca134c825 |