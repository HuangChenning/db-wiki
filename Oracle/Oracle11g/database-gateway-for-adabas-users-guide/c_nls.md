---
title: Globalization Support
book: "Database Gateway for Adabas User's Guide"
doc_id: E12074-01
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/gateways.112/e12074/c_nls.htm
tags:
  - oracle
  - 11g
  - database-gateway-for-adabas-users-guide
---

## D Globalization Support

The main aspect of the Globalization Support in Oracle Connect for IMS, VSAM, and Adabas Gateways is the recognition of the different characters associated with a language and the way they are encoded in various operating systems and data sources. For each supported language, a special definition file called a character set file is supplied where all the language related information is stored. For complex languages such as Chinese, Japanese, and Korean, a special library is also provided where specific conversion rules are implemented.

As a distributed product that accesses heterogeneous data sources on varied platforms, Oracle Connect for IMS, VSAM, and Adabas Gateways offers seamless conversion of text between the different character encodings used on the different platforms. Examples of such automatic conversion include:

- Conversion between ASCII based encoding on open systems and EBCDIC based encoding on IBM mainframes and AS/400 machines
- Conversions to and from Unicode for databases that store data in Unicode
- Conversions between different encodings of the same language used on different platforms
- Conversions of legacy data stored using old character encodings (such as 7-bit encoding) into the current platform encoding standard

Getting this kind of seamless Globalization Support requires the proper setting of the character set definitions according to the kind of encoding in use in the various data sources and platforms.

This section discusses the different encoding schemes in use, the character set definitions required and other Globalization Support related aspects, and contains information on the following topics:

- Character Set Terminology
- Globalization Support Settings

## Character Set Terminology

The following terminology is used to describe character sets.

Single-Byte Character Sets

In a single-byte character set, each character is represented by a single-byte value, that is, a number between 1 and 255, inclusive. Single-byte character sets are typical of Western languages. For example, in the ISO-8859-1 (Latin) character set, the character 'A' is represented by the single byte value of 65, whereas in the US-EBCDIC character set (or in the IBM-037 character set), the same character is represented by the single-byte value of 193.

Multibyte Character Sets

In a multibyte character set, some or all of the characters are represented by more than one byte value. Multibyte character sets are typical in complex languages such as Chinese, Japanese and Korean.

Unicode Character Sets

Unicode is a universal numbering of all known characters, with each character identified by a unique number - its codepoint. Unicode has several encoding schemes, of which Oracle Application Development Framework Controller API Reference supports UTF-8 and, to a lesser extent, UCS-2.

Since the product uses 8-bit characters, the only Unicode encoding that qualifies as a 'character set' is the UTF-8 encoding. The product supports UCS-2 in its data sources (through special Unicode data types).

Customized Character Sets

The Globalization Support of Oracle Connect can be customized to add new languages and character sets not currently supported as well as to introduce special conversion cases. The customization involves editing special character set source files and building.cp files from them using the NAV\_UTIL program.

## Globalization Support Settings

The minimal globalization Support configuration amounts to adding the HS\_LANGUAGE parameter to the HS initialization parameter file and telling the product what national language is in use.

For information on how to add the parameter to the HS initialization parameter file, see [Oracle Database Gateway for IMS, VSAM, and Adabas Installation and Configuration Guide for Microsoft Windows](https://docs.oracle.com/cd/E11882_01/gateways.112/e12077/toc.htm) or [Oracle Database Gateway for IMS, VSAM, and Adabas Installation and Configuration Guide for AIX 5L Based Systems (64-Bit), HP-UX Itanium, Solaris Operating System (SPARC 64-Bit), Linux x86, and Linux x86-64](https://docs.oracle.com/cd/E11882_01/gateways.112/e12076/toc.htm).

To set the language in Studio

1. In the Oracle Studio for IMS, VSAM, and Adabas Gateways Design perspective, open the machine for which you want to set the language.
2. Expand the Bindings and right-click the NAV binding.
3. Select Edit Binding.
4. Open the Misc category and fill in the language parameter with the desired language code from Globalization Support Language Codes.
5. Save the change. New servers will use the language selected.

When a language is selected, a default character set is automatically used based on the language and the platform. Table D-1 summarizes the languages, their codes, and their character sets.

Table D-1 Globalization Support Language Codes

| EBCDIC CP Name | Description | Base ASCII CP | Multibyte |
| --- | --- | --- | --- |
| AR8EBCDIC420 | Arabic bilingual | AR8ISO8859P6 |  |
| AR8EBCDICX | Arabic + Latin | AR8ISO8859P6 |  |
| BLT8EBCDIC1112 | Baltic multilingual | BLT8ISO8859P13 |  |
| CL8EBCDIC1025 | Cyrillic multilingual | CL8ISO8859P5 |  |
| CL8EBCDIC1158 | Cyrillic Ukraine + Euro | CLMSWIN1251 |  |
| D8EBCDIC1141 | Austria - Germany + Euro | WE8ISO8859P15 |  |
| D8EBCDIC273 | Germany - Austria | WE8ISO8859P1 |  |
| DK8EBCDIC1142 | Denmark - Norway + Euro | WE8ISO8859P15 |  |
| DK8EBCDIC277 | Denmark - Norway | NE8ISO8859P10 |  |
| EE8EBCDIC870 | Latin 2 multilingual | EE8ISO8859P2 |  |
| EL8EBCDIC423 | Greece | EL8ISO8859P7 |  |
| EL8EBCDIC875 | Greece | EL8ISO8859P7 |  |
| EL8EBCDIC875R | Greece | EL8ISO8859P7 |  |
| F8EBCDIC1147 | France + Euro | WE8ISO8859P15 |  |
| F8EBCDIC297 | France | WE8ISO8859P1 |  |
| I8EBCDIC1144 | Italy + Euro | WE8ISO8859P15 |  |
| I8EBCDIC280 | Italy | WE8ISO8859P1 |  |
| IW8EBCDIC1086 | Hebrew | IW8ISO8859P8 |  |
| IW8EBCDIC424 | Hebrew | IW8ISO8859P8 |  |
| JA16DBCS | Japan | JA16SJIS | Yes |
| JA16EBCDIC930 | Japan | JA16SJIS | Yes |
| KO16DBCS | Korea | KO16KSC5601 | Yes |
| S8EBCDIC1143 | Finland - Sweden + Euro | WE8ISO8859P15 |  |
| S8EBCDIC278 | Finland - Sweden | WE8ISO8859P1 |  |
| TH8TISEBCDIC | Thai IS 620-2533 EBCDIC 8-bit | TH8TISASCII |  |
| TR8EBCDIC1026 | Turkey | WE8ISO8859P9 |  |
| WE8EBCDIC1047 | Latin 1 | WE8ISO8859P1 |  |
| WE8EBCDIC1140 | USA, Canada + Euro | WE8ISO8859P15 |  |
| WE8EBCDIC1145 | Spanish + Euro | WE8ISO8859P15 |  |
| WE8EBCDIC1146 | UK + Euro | WE8ISO8859P15 |  |
| WE8EBCDIC1148 | International ECECP + Euro | WE8ISO8859P15 |  |
| WE8EBCDIC1148 | Western Europe + Euro | WE8ISO8859P15 |  |
| WE8EBCDIC284 | Spanish | WE8ISO8859P1 |  |
| WE8EBCDIC285 | UK | WE8ISO8859P1 |  |
| WE8EBCDIC37 | USA + Canada | WE8ISO8859P1 |  |
| WE8EBCDIC37 | Canadian French | WE8ISO8859P1 |  |
| WE8EBCDIC500 | Western Europe | WE8ISO8859P1 |  |
| WE8EBCDIC871 | Iceland | NE8ISO8859P10 |  |
| WE8EBCDIC924 | Latin 9 | WE8ISO8859P9 |  |
| ZHS16DBCS | Simplified Chinese | ZHS16CGB231280 | Yes |
| ZHT16DBCS | Traditional Chinese | ZHT16BIG5 | Yes |