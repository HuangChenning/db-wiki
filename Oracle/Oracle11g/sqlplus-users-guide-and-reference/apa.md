---
title: "SQL*Plus Limits"
book: "SQL*Plus User's Guide and Reference"
doc_id: E16604-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e16604/apa.htm
tags:
  - oracle
  - 11g
  - sqlplus-users-guide-and-reference
---

## A SQL\*Plus Limits

The general SQL\*Plus limits shown are valid for most operating systems.

Table A-1 SQL\*Plus Limits

| Item | Limit |
| --- | --- |
| filename length | system dependent |
| username length | 30 bytes |
| substitution variable name length | 30 bytes |
| substitution variable value length | 240 characters |
| command-line length | 2500 characters |
| LONG | 2,000,000,000 bytes |
| LINESIZE | system dependent |
| LONGCHUNKSIZE value | system dependent |
| output line size | system dependent |
| SQL or PL/SQL command- line size after variable substitution | 3,000 characters (internal only) |
| number of characters in a COMPUTE command label | 500 characters |
| number of lines per SQL command | 500 (assuming 80 characters per line) |
| maximum PAGESIZE | 50,000 lines |
| total row width | 32,767 characters |
| maximum ARRAYSIZE | 5000 rows |
| maximum number of nested scripts | 20 |
| maximum page number | 99,999 |
| maximum PL/SQL error message size | 2K |
| maximum ACCEPT character string length | 240 Bytes |
| maximum number of substitution variables | 2048 |