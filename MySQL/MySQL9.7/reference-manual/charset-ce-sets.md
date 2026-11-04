---
title: "12.10.3 Central European Character Sets"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/charset-ce-sets.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

### 12.10.3 Central European Character Sets

MySQL provides some support for character sets used in the Czech Republic, Slovakia, Hungary, Romania, Slovenia, Croatia, Poland, and Serbia (Latin).

- `cp1250` (Windows Central European) collations:
- `cp852` (DOS Central European) collations:
	- `cp852_bin`
	- `cp852_general_ci` (default)
- `keybcs2` (DOS Kamenicky Czech-Slovak) collations:
	- `keybcs2_bin`
	- `keybcs2_general_ci` (default)
- `latin2` (ISO 8859-2 Central European) collations:
- `macce` (Mac Central European) collations:
	`macce` is deprecated; expect support for it to be removed in a subsequent MySQL release.