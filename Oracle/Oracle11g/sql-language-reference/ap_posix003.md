---
title: Perl-influenced Extensions in Oracle Regular Expressions
book: SQL Language Reference
doc_id: E41084-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41084/ap_posix003.htm
tags:
  - oracle
  - 11g
  - sql-language-reference
---

Oracle Database regular expression functions and conditions accept a number of Perl-influenced operators that are in common use, although not part of the POSIX standard. Table D-3 lists those operators. For more complete descriptions with examples, refer to [Oracle Database Advanced Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e41502/adfns_regexp.htm#ADFNS1012).

Table D-3 Perl-influenced Operators in Oracle Regular Expressions

| Operator | Description |
| --- | --- |
| \\d | A digit character. |
| \\D | A nondigit character. |
| \\w | A word character. |
| \\W | A nonword character. |
| \\s | A whitespace character. |
| \\S | A non-whitespace character. |
| \\A | Matches only at the beginning of a string, or before a newline character at the end of a string. |
| \\Z | Matches only at the end of a string. |
| \*? | Matches the preceding pattern element 0 or more times (nongreedy). |
| +? | Matches the preceding pattern element 1 or more times (nongreedy). |
| ?? | Matches the preceding pattern element 0 or 1 time (nongreedy). |
| {n}? | Matches the preceding pattern element exactly `n` times (nongreedy). |
| {n,}? | Matches the preceding pattern element at least `n` times (nongreedy). |
| {n,m}? | Matches the preceding pattern element at least `n` but not more than `m` times (nongreedy). |