---
title: SQL Language Reference
book: SQL Language Reference
doc_id: F31301-19
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqlrf/Multilingual-Regular-Expression-Syntax.html
tags:
  - oracle
  - 21c
  - sql-language-reference
---

## Multilingual Regular Expression Syntax

Table D-1 lists the full set of operators defined in the POSIX standard Extended Regular Expression (ERE) syntax. Oracle follows the exact syntax and matching semantics for these operators as defined in the POSIX standard for matching ASCII (English language) data. For more complete descriptions of the operators, examples of their use, and Oracle multilingual enhancements of the operators, refer to Oracle Database Development Guide. Notes following the table provide more complete descriptions of the operators and their functions, as well as Oracle multilingual enhancements of the operators. [Table D-2](Regular-Expression-Operator-Multilingual-Enhancements.md) summarizes Oracle support for and multilingual enhancement of the POSIX operators.

Table D-1 Regular Expression Operators and Metasymbols

| Operator | Description |
| --- | --- |
| \\ | The backslash character can have four different meanings depending on the context. It can:  - Stand for itself - Quote the next character - Introduce an operator - Do nothing |
| \* | Matches zero or more occurrences |
| + | Matches one or more occurrences |
| ? | Matches zero or one occurrence |
| \| | Alternation operator for specifying alternative matches |
| ^ | Matches the beginning of a string by default. In multiline mode, it matches the beginning of any line anywhere within the source string. |
| $ | Matches the end of a string by default. In multiline mode, it matches the end of any line anywhere within the source string. |
| . | Matches any character in the supported character set except `NULL` |
| \[ \] | Bracket expression for specifying a matching list that should match any one of the expressions represented in the list. A non-matching list expression begins with a circumflex (^) and specifies a list that matches any character except for the expressions represented in the list.  To specify a right bracket (\]) in the bracket expression, place it first in the list (after the initial circumflex (^), if any).  To specify a hyphen in the bracket expression, place it first in the list (after the initial circumflex (^), if any), last in the list, or as an ending range point in a range expression. |
| ( ) | Grouping expression, treated as a single subexpression |
| {m} | Matches exactly m times |
| {m,} | Matches at least m times |
| {m,n} | Matches at least m times but no more than n times |
| \\n | The backreference expression (n is a digit between 1 and 9) matches the n <sup>th</sup> subexpression enclosed between '(' and ')' preceding the \\n |
| \[..\] | Specifies one collation element, and can be a multicharacter element (for example, \[.ch.\] in Spanish) |
| \[::\] | Specifies character classes (for example, \[:alpha:\]). It matches any character within the character class. |
| \[==\] | Specifies equivalence classes. For example, \[=a=\] matches all characters having base letter 'a'. |