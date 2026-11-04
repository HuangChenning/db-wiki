---
title: "12.16 MySQL Server Locale Support"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/locale-support.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

The locale indicated by the [`lc_time_names`](server-system-variables.md) system variable controls the language used to display day and month names and abbreviations. This variable affects the output from the [`DATE_FORMAT()`](date-and-time-functions.md), [`DAYNAME()`](date-and-time-functions.md), and [`MONTHNAME()`](date-and-time-functions.md) functions.

[`lc_time_names`](server-system-variables.md) does not affect the [`STR_TO_DATE()`](date-and-time-functions.md) or [`GET_FORMAT()`](date-and-time-functions.md) function.

The [`lc_time_names`](server-system-variables.md) value does not affect the result from [`FORMAT()`](string-functions.md), but this function takes an optional third parameter that enables a locale to be specified to be used for the result number's decimal point, thousands separator, and grouping between separators. Permissible locale values are the same as the legal values for the [`lc_time_names`](server-system-variables.md) system variable.

Locale names have language and region subtags listed by IANA ([http://www.iana.org/assignments/language-subtag-registry](http://www.iana.org/assignments/language-subtag-registry)) such as `'ja_JP'` or `'pt_BR'`. The default value is `'en_US'` regardless of your system's locale setting, but you can set the value at server startup, or set the `GLOBAL` value at runtime if you have privileges sufficient to set global system variables; see [Section 7.1.9.1, “System Variable Privileges”](system-variable-privileges.md). Any client can examine the value of [`lc_time_names`](server-system-variables.md) or set its `SESSION` value to affect the locale for its own connection.

(The first [`SET NAMES`](set-names.md) statement in the following example may not be necessary if no settings relating to character set and collation have been changed from their defaults; we include it for completeness.)

```
mysql> SET NAMES 'utf8mb4';
Query OK, 0 rows affected (0.09 sec)

mysql> SELECT @@lc_time_names;
+-----------------+
| @@lc_time_names |
+-----------------+
| en_US           |
+-----------------+
1 row in set (0.00 sec)

mysql> SELECT DAYNAME('2020-01-01'), MONTHNAME('2020-01-01');
+-----------------------+-------------------------+
| DAYNAME('2020-01-01') | MONTHNAME('2020-01-01') |
+-----------------------+-------------------------+
| Wednesday             | January                 |
+-----------------------+-------------------------+
1 row in set (0.00 sec)

mysql> SELECT DATE_FORMAT('2020-01-01','%W %a %M %b');
+-----------------------------------------+
| DATE_FORMAT('2020-01-01','%W %a %M %b') |
+-----------------------------------------+
| Wednesday Wed January Jan               |
+-----------------------------------------+
1 row in set (0.00 sec)

mysql> SET lc_time_names = 'es_MX';
Query OK, 0 rows affected (0.00 sec)

mysql> SELECT @@lc_time_names;
+-----------------+
| @@lc_time_names |
+-----------------+
| es_MX           |
+-----------------+
1 row in set (0.00 sec)

mysql> SELECT DAYNAME('2020-01-01'), MONTHNAME('2020-01-01');
+-----------------------+-------------------------+
| DAYNAME('2020-01-01') | MONTHNAME('2020-01-01') |
+-----------------------+-------------------------+
| miércoles             | enero                   |
+-----------------------+-------------------------+
1 row in set (0.00 sec)

mysql> SELECT DATE_FORMAT('2020-01-01','%W %a %M %b');
+-----------------------------------------+
| DATE_FORMAT('2020-01-01','%W %a %M %b') |
+-----------------------------------------+
| miércoles mié enero ene                 |
+-----------------------------------------+
1 row in set (0.00 sec)
```

The day or month name for each of the affected functions is converted from `utf8mb4` to the character set indicated by the [`character_set_connection`](server-system-variables.md) system variable.

[`lc_time_names`](server-system-variables.md) may be set to any of the following locale values. The set of locales supported by MySQL may differ from those supported by your operating system.

| Locale Value | Meaning |
| --- | --- |
| `ar_AE` | Arabic - United Arab Emirates |
| `ar_BH` | Arabic - Bahrain |
| `ar_DZ` | Arabic - Algeria |
| `ar_EG` | Arabic - Egypt |
| `ar_IN` | Arabic - India |
| `ar_IQ` | Arabic - Iraq |
| `ar_JO` | Arabic - Jordan |
| `ar_KW` | Arabic - Kuwait |
| `ar_LB` | Arabic - Lebanon |
| `ar_LY` | Arabic - Libya |
| `ar_MA` | Arabic - Morocco |
| `ar_OM` | Arabic - Oman |
| `ar_QA` | Arabic - Qatar |
| `ar_SA` | Arabic - Saudi Arabia |
| `ar_SD` | Arabic - Sudan |
| `ar_SY` | Arabic - Syria |
| `ar_TN` | Arabic - Tunisia |
| `ar_YE` | Arabic - Yemen |
| `be_BY` | Belarusian - Belarus |
| `bg_BG` | Bulgarian - Bulgaria |
| `ca_ES` | Catalan - Spain |
| `cs_CZ` | Czech - Czech Republic |
| `da_DK` | Danish - Denmark |
| `de_AT` | German - Austria |
| `de_BE` | German - Belgium |
| `de_CH` | German - Switzerland |
| `de_DE` | German - Germany |
| `de_LU` | German - Luxembourg |
| `el_GR` | Greek - Greece |
| `en_AU` | English - Australia |
| `en_CA` | English - Canada |
| `en_GB` | English - United Kingdom |
| `en_IN` | English - India |
| `en_NZ` | English - New Zealand |
| `en_PH` | English - Philippines |
| `en_US` | English - United States |
| `en_ZA` | English - South Africa |
| `en_ZW` | English - Zimbabwe |
| `es_AR` | Spanish - Argentina |
| `es_BO` | Spanish - Bolivia |
| `es_CL` | Spanish - Chile |
| `es_CO` | Spanish - Colombia |
| `es_CR` | Spanish - Costa Rica |
| `es_DO` | Spanish - Dominican Republic |
| `es_EC` | Spanish - Ecuador |
| `es_ES` | Spanish - Spain |
| `es_GT` | Spanish - Guatemala |
| `es_HN` | Spanish - Honduras |
| `es_MX` | Spanish - Mexico |
| `es_NI` | Spanish - Nicaragua |
| `es_PA` | Spanish - Panama |
| `es_PE` | Spanish - Peru |
| `es_PR` | Spanish - Puerto Rico |
| `es_PY` | Spanish - Paraguay |
| `es_SV` | Spanish - El Salvador |
| `es_US` | Spanish - United States |
| `es_UY` | Spanish - Uruguay |
| `es_VE` | Spanish - Venezuela |
| `et_EE` | Estonian - Estonia |
| `eu_ES` | Basque - Spain |
| `fi_FI` | Finnish - Finland |
| `fo_FO` | Faroese - Faroe Islands |
| `fr_BE` | French - Belgium |
| `fr_CA` | French - Canada |
| `fr_CH` | French - Switzerland |
| `fr_FR` | French - France |
| `fr_LU` | French - Luxembourg |
| `gl_ES` | Galician - Spain |
| `gu_IN` | Gujarati - India |
| `he_IL` | Hebrew - Israel |
| `hi_IN` | Hindi - India |
| `hr_HR` | Croatian - Croatia |
| `hu_HU` | Hungarian - Hungary |
| `id_ID` | Indonesian - Indonesia |
| `is_IS` | Icelandic - Iceland |
| `it_CH` | Italian - Switzerland |
| `it_IT` | Italian - Italy |
| `ja_JP` | Japanese - Japan |
| `ko_KR` | Korean - Republic of Korea |
| `lt_LT` | Lithuanian - Lithuania |
| `lv_LV` | Latvian - Latvia |
| `mk_MK` | Macedonian - North Macedonia |
| `mn_MN` | Mongolia - Mongolian |
| `ms_MY` | Malay - Malaysia |
| `nb_NO` | Norwegian(Bokmål) - Norway |
| `nl_BE` | Dutch - Belgium |
| `nl_NL` | Dutch - The Netherlands |
| `no_NO` | Norwegian - Norway |
| `pl_PL` | Polish - Poland |
| `pt_BR` | Portugese - Brazil |
| `pt_PT` | Portugese - Portugal |
| `rm_CH` | Romansh - Switzerland |
| `ro_RO` | Romanian - Romania |
| `ru_RU` | Russian - Russia |
| `ru_UA` | Russian - Ukraine |
| `sk_SK` | Slovak - Slovakia |
| `sl_SI` | Slovenian - Slovenia |
| `sq_AL` | Albanian - Albania |
| `sr_RS` | Serbian - Serbia |
| `sv_FI` | Swedish - Finland |
| `sv_SE` | Swedish - Sweden |
| `ta_IN` | Tamil - India |
| `te_IN` | Telugu - India |
| `th_TH` | Thai - Thailand |
| `tr_TR` | Turkish - Turkey |
| `uk_UA` | Ukrainian - Ukraine |
| `ur_PK` | Urdu - Pakistan |
| `vi_VN` | Vietnamese - Vietnam |
| `zh_CN` | Chinese - China |
| `zh_HK` | Chinese - Hong Kong |
| `zh_TW` | Chinese - Taiwan |