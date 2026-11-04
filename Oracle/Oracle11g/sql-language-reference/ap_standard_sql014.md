---
title: Character Set Support
book: SQL Language Reference
doc_id: E41084-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41084/ap_standard_sql014.htm
tags:
  - oracle
  - 11g
  - sql-language-reference
---

Oracle supports most national, international, and vendor-specific encoded character set standards. A complete list of character sets supported by Oracle appears in [Oracle Database Globalization Support Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10729/applocaledata.htm#NLSPG014).

Unicode is a universal encoded character set that lets you store information from any language using a single character set. Unicode is required by modern standards such as XML, Java, JavaScript, and LDAP. Unicode is compliant with ISO/IEC standard 10646. You can obtain a copy of ISO/IEC standard 10646 from this address:

International Organization for Standardization

1 Rue de Varembé

Case postale 56

CH-1211, Geneva 20, Switzerland

Phone: +41.22.749.0111

Fax: +41.22.733.3430

Web site: http://www.iso.ch/

Oracle Database complies fully with Unicode 4.0, the fourth and most recent version of the Unicode standard. For up-to-date information on this standard, visit the Web site of the Unicode Consortium:

```
http://www.unicode.org
```

Oracle uses UTF-8 (8-bit) encoding by way of three database character sets, two for ASCII-based platforms (UTF8 and AL32UTF8) and one for EBCDIC platforms (UTFE). If you prefer to implement Unicode support incrementally, then you can store Unicode data in either the UTF-16 or UTF-8 encoding form, in the national character set, for the SQL `NCHAR` data types (`NCHAR`, `NVARCHAR2`, and `NCLOB`).

See Also:

[Oracle Database Globalization Support Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10729/applocaledata.htm#NLSPG014) for details on Oracle character set support