---
title: "10.3.1 Collation Naming Conventions"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/charset-collation-names.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 10.3.1 Collation Naming Conventions

MySQL collation names follow these conventions:

- A collation name starts with the name of the character set with which it is associated, generally followed by one or more suffixes indicating other collation characteristics. For example, `utf8_general_ci` and `latin1_swedish_ci` are collations for the `utf8` and `latin1` character sets, respectively. The `binary` character set has a single collation, also named `binary`, with no suffixes.
- A language-specific collation includes a language name. For example, `utf8_turkish_ci` and `utf8_hungarian_ci` sort characters for the `utf8` character set using the rules of Turkish and Hungarian, respectively.
- Collation suffixes indicate whether a collation is case-sensitive, accent-sensitive, or kana-sensitive (or some combination thereof), or binary. The following table shows the suffixes used to indicate these characteristics.
	**Table 10.1 Collation Suffix Meanings**
	| Suffix | Meaning |
	| --- | --- |
	| `_ai` | Accent-insensitive |
	| `_as` | Accent-sensitive |
	| `_ci` | Case-insensitive |
	| `_cs` | Case-sensitive |
	| `_bin` | Binary |
	For nonbinary collation names that do not specify accent sensitivity, it is determined by case sensitivity. If a collation name does not contain `_ai` or `_as`, `_ci` in the name implies `_ai` and `_cs` in the name implies `_as`. For example, `latin1_general_ci` is explicitly case-insensitive and implicitly accent-insensitive, and `latin1_general_cs` is explicitly case-sensitive and implicitly accent-sensitive.
	For the `binary` collation of the `binary` character set, comparisons are based on numeric byte values. For the `_bin` collation of a nonbinary character set, comparisons are based on numeric character code values, which differ from byte values for multibyte characters. For information about the differences between the `binary` collation of the `binary` character set and the `_bin` collations of nonbinary character sets, see [Section 10.8.5, “The binary Collation Compared to \_bin Collations”](charset-binary-collations.md).
- Collation names for Unicode character sets may include a version number to indicate the version of the Unicode Collation Algorithm (UCA) on which the collation is based. UCA-based collations without a version number in the name use the version-4.0.0 UCA weight keys. For example:
	- `utf8_unicode_520_ci` is based on UCA 5.2.0 weight keys ([http://www.unicode.org/Public/UCA/5.2.0/allkeys.txt](http://www.unicode.org/Public/UCA/5.2.0/allkeys.txt)).
	- `utf8_unicode_ci` (with no version named) is based on UCA 4.0.0 weight keys ([http://www.unicode.org/Public/UCA/4.0.0/allkeys-4.0.0.txt](http://www.unicode.org/Public/UCA/4.0.0/allkeys-4.0.0.txt)).
- For Unicode character sets, the ``*`xxx`*_general_mysql500_ci`` collations preserve the pre-5.1.24 ordering of the original ``*`xxx`*_general_ci`` collations and permit upgrades for tables created before MySQL 5.1.24 (Bug #27877).