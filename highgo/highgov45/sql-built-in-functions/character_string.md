---
title: "字符串函数和操作符"
book: "常用内置函数"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/sql/character_string.html"
tags:
  - highgo
  - highgo-v45
  - sql-built-in-functions
---

## 字符串函数和操作符

HGDB 提供以下字符串函数和操作符：

| 函数 | 返回类型 | 描述 | 例子 | 结果 |
| --- | --- | --- | --- | --- |
| string \|\| string | text | 串接 | ‘High’ \|\| ‘Go’ | HighGo |
| string \|\| non string or non string \|\| string | text | 使用一个非字符串输入的串接 | ‘Value:’\|\|42 | Value:42 |
| bit\_length(string) | int | 串中的位数 | bit\_length(‘jose’) | 32 |
| char\_length(string) or character\_length(string) | int | 串中的位数 | char\_length(‘jose’) | 4 |
| lower(string) | text | 将字符串转换为小写形式 | lower(‘TOM’) | tom |
| octet\_length(string) | int | 串中的字节数 | octet\_length(‘jose’) | 4 |
| overlay(string placing string from int \[for int\]) | text | 替换子串 | overlay(‘Txxxxas’ placing ‘hom’ from 2 for 4) | Thomas |
| position(substring in string) | int | 定位指定子串 | position(‘om’ in ‘Thomas’) | 3 |
| substring( string \[ from int \] \[ for int \] ) | text | 提取子串 | substring(‘Thomas’ from 2 for 3) | hom |
| substring(string from pattern) | text | 提取匹配 POSIX 正则表达式的子串 | substring(‘Thomas’ from ‘…$’) | mas |
| substring(string from pattern for escape) | text | 提取匹配 SQL 正则表达式的子串 | substring(‘Thomas’ from ‘%#”o\_a#”\_’ for ‘#’) | oma |
| trim( \[ leading\|trailing\|both \] \[ characters \] from string) | text | 从 string 的开头、结尾或者两端（both是默认值）移除只包含 characters（默认是一个空格）中字符的最长字符串 | trim(both ‘xyz’ from ‘yxTomxx’) | Tom |
| trim( \[ leading \| trailing \| both \] \[ from \] string \[, characters \] ) | text | trim() 的非标准版本 | trim(both from ‘xTomxx’,’x’) | Tom |
| upper(string) | text | 将字符串转换成大写形式 | upper(‘tom’) | TOM |