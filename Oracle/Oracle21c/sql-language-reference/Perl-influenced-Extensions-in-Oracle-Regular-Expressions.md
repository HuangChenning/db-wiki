---
title: SQL Language Reference
book: SQL Language Reference
doc_id: F31301-19
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqlrf/Perl-influenced-Extensions-in-Oracle-Regular-Expressions.html
tags:
  - oracle
  - 21c
  - sql-language-reference
---

## Perl-influenced Extensions in Oracle Regular Expressions

Oracle Database regular expression functions and conditions accept a number of Perl-influenced operators that are in common use, although not part of the POSIX standard. Table D-3 lists those operators. For more complete descriptions with examples, refer to [Oracle Database Development Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlrf&id=ADFNS1012).

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