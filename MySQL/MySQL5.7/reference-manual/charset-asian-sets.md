---
title: "10.10.7 Asian Character Sets"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/charset-asian-sets.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 10.10.7 Asian Character Sets

The Asian character sets that we support include Chinese, Japanese, Korean, and Thai. These can be complicated. For example, the Chinese sets must allow for thousands of different characters. See [Section 10.10.7.1, “The cp932 Character Set”](charset-cp932.md), for additional information about the `cp932` and `sjis` character sets. See [Section 10.10.7.2, “The gb18030 Character Set”](charset-gb18030.md), for additional information about character set support for the Chinese National Standard GB 18030.

For answers to some common questions and problems relating support for Asian character sets in MySQL, see [Section A.11, “MySQL 5.7 FAQ: MySQL Chinese, Japanese, and Korean Character Sets”](faqs-cjk.md).

- `big5` (Big5 Traditional Chinese) collations:
	- `big5_bin`
	- `big5_chinese_ci` (default)
- [`cp932`](charset-cp932.md) (SJIS for Windows Japanese) collations:
	- `cp932_bin`
	- `cp932_japanese_ci` (default)
- `eucjpms` (UJIS for Windows Japanese) collations:
	- `eucjpms_bin`
	- `eucjpms_japanese_ci` (default)
- `euckr` (EUC-KR Korean) collations:
	- `euckr_bin`
	- `euckr_korean_ci` (default)
- `gb2312` (GB2312 Simplified Chinese) collations:
	- `gb2312_bin`
	- `gb2312_chinese_ci` (default)
- `gbk` (GBK Simplified Chinese) collations:
	- `gbk_bin`
	- `gbk_chinese_ci` (default)
- [`gb18030`](charset-gb18030.md) (China National Standard GB18030) collations:
	- `gb18030_bin`
	- `gb18030_chinese_ci` (default)
	- `gb18030_unicode_520_ci`
- `sjis` (Shift-JIS Japanese) collations:
- `tis620` (TIS620 Thai) collations:
- `ujis` (EUC-JP Japanese) collations:

The `big5_chinese_ci` collation sorts on number of strokes.