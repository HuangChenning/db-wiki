---
title: "字符串函数"
book: "常用内置函数"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/guide/guide_one_text9.html"
tags:
  - highgo
  - highgo-v9
  - guide-built-in-functions
---

## 字符串函数

HGDB 提供以下常见字符串函数

| 函数 | 返回类型 | 描述 | 例子 | 结果 |
| --- | --- | --- | --- | --- |
| bit\_length(string) | int | 串中的位数 | bit\_length( ‘jose’) | 32 |
| bit\_length(string) | int | 串中的位数 | bit\_length( ‘jose’) | 32 |
| char\_length(string )orcharacter\_length( string) | int | 串中的位数 | char\_length(‘jose’) | 4 |
| lower(string) | text | 将字符串转换为 小写形式 | lower(‘TOM’) | tom |
| octet\_length(strin g) | int | 串中的字节数 | octet\_length(‘jose’) | 4 |
| overlay(stringplacing stringfrom int \[for int\]) | text | 替换子串 | overlay(‘Txxxxas’ placing ‘hom’ from 2 for 4) | Thomas |
| position(substring in string) | int | 定位指定子串 | position(‘om’ in ‘Thomas’) | 3 |
| substring(string \[from int\] \[for int\]) | text | 提取子串 | substring(‘ Thomas’ from 2 for 3) |  |
| substring(string from pattern) | text | 提取匹配 POSIX 正则表达式的子串。模式匹配详 情见第 8.7 节 | substring(‘ Thomas’ from ‘…$’) |  |
| substring(string frompattern for escape) | text | 提取匹配 SQL正 则表达式的子串。 模式匹配详情 见第 8.7 节 | substring(‘Thomas’ from ‘%#”o\_a#”\_’ for’#’) |  |
| trim( \[ leading\|trailing\|both \] \[ characters \] from string) | text | 从 string 的开头、结尾或者两端（both是默认值）移除只包含 characters（默认是一个空格）中字符的最长字符串 | trim(both ‘xyz’ from ‘yxTomxx’) | Tom |
| trim( \[ leading \| trailing \| both \] \[ from \] string \[, characters \] ) | text | trim() 的非标准版本 | trim(both from ‘xTomxx’,’x’) | Tom |
| upper(string) | text | 将字符串转换成 大写形式 | upper(‘tom ‘) | TOM |
| ascii(string) | int | 参数第一个字符的ASCII 代码。对于 UTF8 返回该字符的 Unicode 代码点。对于其他多字 节编码，该参数必须是一个 ASCII 字 符。 | ascii(‘x’) | 120 |
| btrim(string text \[,characters text\]) | text | 从 string 的开头或结尾 删除最长的只包含 characters（默 认是一个空格）的串 | btrim(‘xyxtrimyyx’, ‘xyz’) | trim |
| concat(str “any” \[, str”any” \[, …\] \]) | text | 串接所有参数的文本表 示。NULL参数被忽略。 | concat(‘abcde’,2, NULL, 22) | abcde222 |
| convert\_from(st ring bytea,src\_encoding name) | text | 将字符串转换为数据库编码。原始编码由 src\_encoding指定。string 在这个编码中必须可用。 | convert\_from(‘text\_in\_utf8’,’UTF8’) | 用当前数 据库编码表示 的 text |
| format(formatstr text \[,formatarg “any” \[, …\] \]) | text | 根据一个格式字符串格 式化参数。该函数和 C 函数 sprintf 相似。见第 8.4.1 节 | format(‘Hello%s, %1$s’, ‘World’) | HelloWorld,World |
| decode(string text, format text) | bytea | 从 string 中的文本表达 解码二进制数据。format 的选项和 encode 中的一样。 | decode(‘MTIzAAE=’,’base64’) | 3132330001 |
| initcap(string) | text | 将每一个词的第一个字母转换为大写形式并把剩下的字母转换为小写形式。词是由非字母数字字符分隔的字母数字字符的序列。 | initcap(‘hiTHOMAS’) | HiThomas |
| left(str text, n int) | text | 返回字符串中的前 n 个 字符。当 n 为负时，将 返回除了最后\|n\|个 | left(‘abcde’,2) | ab |
| length(string) | int | string 中的字符数 | length(‘jose’) | 4 |
| lpad(stringtext, lengthint \[,fill text\]) | text | 将 string 通过前置字符fill（默认是一个空格）填充到长度 length。如果string 已经长于 length，则它被（从右边）截断。 | lpad(‘hi’, 5,’xy’) | xyxhi |
| ltrim(string text \[,characters text\]) | text | 从 string 的开头删除最 长的只包含 characters （默认是一个空格）的 串 | ltrim(‘zzzytest’’xyz’) | test |
| replace(string text,fromtext, to text) | text | 将 string 中出现的所有 子串 from 替换为子串 to | replace(‘abcdefabcdef ‘,’cd’, ‘XX’) |  |
| reverse(str) | text | 返回反转的字符串。 | reverse(‘ab cde’) | edcba |
| COALESCE (参数1，参数2) |  | 为null时返回参数2，不为null返回参数1 | COALESCE (‘aa’，’bb’) | aa or bb |
| right(strtext, n int) | text | 返回字符串中的最后 n 个字符。如果 n 为负， 返回除最前面的\|n\|个字符外的 所有字符。 | right(‘abcde’,2) | de |
| rpad(stringtext, lengthint \[,fill text\]) | text | 将 string 通过增加字符 fill（默认为一个空格） 填充到长度 length 。如 果 string 已经长于 length 则它会被截断。 | rpad(‘hi’, 5,’xy’) | hixyx |
| rtrim(string text \[,characters text\]) | text | 从 string 的结尾删除最 长的只包含 characters （默认是一个空格）的 串 | rtrim(‘testxxzx,’xyz’) | test |
| substr(string, from \[, count\]) | text |  | 提取子串（与substring(stringfrom fromforcount)相同） | substr(‘alphabet’, 3, 2)ph |