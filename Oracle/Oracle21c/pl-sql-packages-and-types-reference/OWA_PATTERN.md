---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/OWA_PATTERN.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 231 OWA\_PATTERN

The OWA\_PATTERN package provides an interface to locate text patterns within strings and replace the matched string with another string.

See Also:

For more information about implementation of this package, see the following:

- [Oracle Fusion Middleware Administrator's Guide for Oracle HTTP Server](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=HSADM)
- [Oracle Fusion Middleware User's Guide for mod\_plsql](https://docs.oracle.com/cd/E23943_01/portal.1111/e12041/toc.htm)

The chapter contains the following topics:

### 231.1 OWA\_PATTERN Types

You can use a pattern as both an input and output parameter. Because of this, you can pass the same regular expression to `OWA_PATTERN` function calls, and it only has to be parsed once.

- `OWA_PATTERN.PATTERN`

### 231.2 OWA\_PATTERN Operational Notes

The OWA\_PATTERN subprograms are overloaded. Specifically, there are six versions of `MATCH`, and four each of `AMATCH` and `CHANGE`.

The subprograms use the following parameters:

- `line` - This is the target to be examined for a match. It can be more than one line of text or a owa\_text.multi\_line datatype.
- `pat` - This is the pattern that the subprograms attempt to locate in line. The pattern can contain regular expressions. In the owa\_pattern.change function and procedure, this parameter is called `from_str`.
- `flags` - This specifies whether the search is case-sensitive or if substitutions are done globally.

Use regular expressions with the subprograms in this package. You Specify a regular expression by creating the string you want to match interspersed with various wildcard tokens and quantifiers.

- Wildcards
- Quantifiers
- Flags

#### 231.2.1 OWA\_PATTERN Wildcards

Wildcard tokens match something other than themselves.

Table 231-1 Wildcard tokens recognized by OWA\_PATTERN package

| Token | Description |
| --- | --- |
| ` ^` | Matches newline or the beginning of the target |
| `$` | Matches newline or the end of the target |
| `\n` | Matches newline |
| `.` | Matches any character except newline |
| `\t` | Matches tab |
| `\d ` | Matches digits \[0-9\] |
| `\D` | Matches non-digits \[not 0-9\] |
| `\w` | Matches word characters (0-9, a-z, A-Z, or \_) |
| `\W` | Matches non-word characters (not 0-9, a-z, A-Z, or \_) |
| `\s` | Matches whitespace characters (blank, tab, or newline). |
| `\S` | Matches non-whitespace characters (not blank, tab, or newline) |
| `\b` | Matches "word" boundaries (between \\w and \\W) |
| `\x<HEX>` | Matches the value in the current character set of the two hexadecimal digits |
| `\<OCT>` | Matches the value in the current character set of the two or three octal digits |
| `\` | Followed by any character not covered by another case matches that character |
| `&` | Applies only to `CHANGE`. This causes the string that matched the regular expression to be included in the string that replaces it. This differs from the other tokens in that it specifies how a target is changed rather than how it is matched. This is explained further under CHANGE Functions and Procedures . |

#### 231.2.2 OWA\_PATTERN Quantifiers

Any tokens except `&` can have their meaning extended by any of the following quantifiers. You can also apply these quantifiers to literals.

Table 231-2 Quantifiers

| Quantifier | Description |
| --- | --- |
| `?` | 0 or 1 occurrence(s) |
| `*` | 0 or more occurrences |
| `+` | 1 or more occurrence(s) |
| `{n}` | Exactly n occurrences |
| `(n,}` | At least n occurrences |
| `{n,m}` | At least n, but not more than m, occurrences |

#### 231.2.3 OWA\_PATTERN Flags

In addition to targets and regular expressions, the `OWA_PATTERN` functions and procedures use flags to affect how they are interpreted.

Table 231-3 Flags

| Flag | Description |
| --- | --- |
| `i` | This indicates a case-insensitive search. |
| `g` | This applies only to CHANGE. It indicates a global replace. That is, all portions of the target that match the regular expression are replaced. |

### 231.3 Summary of OWA\_PATTERN Subprograms

This table lists the OWA\_PATTERN subprograms and briefly describes them.

Table 231-4 OWA\_PATTERN Package Subprograms

| Subprogram | Description |
| --- | --- |
| AMATCH Function | Determines if a string contains the specified pattern. It lets you specify where in the string the match has to occur |
| CHANGE Functions and Procedures | Replaces a pattern within a string. If you call it as a function it returns the number of times the regular expression was found and replaced |
| GETPAT Procedure | Generates a pattern datatype from a `VARCHAR2` type |
| MATCH Function | Determines if a string contains the specified pattern |

#### 231.3.1 AMATCH Function

This function specifies if a pattern occurs in a particular location in a string.

There are four versions to this function:

- The first and second versions of the function do not save the matched tokens (these are saved in the `backrefs` parameters in the third and fourth versions). The difference between the first and second versions is the `pat` parameter, which can be a `VARCHAR2` or a pattern datatype.
- The third and fourth versions of the function save the matched tokens in the `backrefs` parameter. The difference between the third and fourth versions is the `pat` parameter, which can be a VARCHAR2 or a pattern datatype.
	Note:
	If multiple overlapping strings match the regular expression, this function takes the longest match.

Syntax

```
OWA_PATTERN.AMATCH(
   line           IN       VARCHAR2,
   from_loc       IN       INTEGER,
   pat            IN       VARCHAR2,
   flags          IN       VARCHAR2   DEFAULT NULL)
 RETURN INTEGER;

OWA_PATTERN.AMATCH(
   line           IN       VARCHAR2,
   from_loc       IN       INTEGER,
   pat            IN OUT   PATTERN,
   flags          IN       VARCHAR2   DEFAULT NULL)
 RETURN INTEGER;

OWA_PATTERN.AMATCH(
   line           IN       VARCHAR2
   from_loc       IN       INTEGER
   pat            in       varchar2
   backrefs       OUT      owa_text.vc_arr
   flags          IN       VARCHAR2   DEFAULT NULL)
 RETURN INTEGER;

OWA_PATTERN.AMATCH(
   line           IN       VARCHAR2
   from_loc       IN       INTEGER
   pat            IN OUT   PATTERN
   backrefs       OUT      owa_text.vc_arr
   flags          IN       VARCHAR2   DEFAULT NULL)
 RETURN INTEGER;
```

Parameters

Table 231-5 AMATCH Function Parameters

| Parameter | Description |
| --- | --- |
| `line` | The text to search in. |
| from\_loc | The location (in number of characters) in `line` where the search is to begin. |
| `pat` | The string to match. It can contain regular expressions. This can be either a `VARCHAR2` or a pattern. If it is a pattern, the output value of this parameter is the pattern matched. |
| backrefs | The text that is matched. Each token that is matched is placed in a cell in the `OWA_TEXT.VC_ARR DATA TYPE ` PL/SQL table. |
| flags | Whether or not the search is case-sensitive. If the value of this parameter is "i", the search is case-insensitive. Otherwise the search is case-sensitive. |

Return Values

The index of the character after the end of the match, counting from the beginning of `line`. If there was no match, the function returns `0`.

#### 231.3.2 CHANGE Functions and Procedures

This function or procedure searches and replaces a string or `multi_line` datatype. If multiple overlapping strings match the regular expression, this subprogram takes the longest match.

Syntax

```
OWA_PATTERN.CHANGE(
   line           IN OUT    VARCHAR2,
   from_str       IN        VARCHAR2,
   to_str         IN        VARCHAR2,
   flags          IN        VARCHAR2   DEFAULT NULL)
 RETURN INTEGER;

OWA_PATTERN.CHANGE(
   line           IN OUT   VARCHAR2,
   from_str       IN       VARCHAR2,
   to_str         IN       VARCHAR2,
   flags          IN       VARCHAR2   DEFAULT NULL);

owa_pattern.change(
   mline          IN OUT   owa_text.multi_line,
   from_str       IN       VARCHAR2,
   to_str         IN       VARCHAR2,
   flags          IN       VARCHAR2   DEFAULT NULL)
 RETURN INTEGER;

OWA_PATTERN.CHANGE(
   mline          IN OUT   owa_text.multi_line,
   from_str       IN       VARCHAR2,
   to_str         IN       VARCHAR2,
   flags          IN       VARCHAR2   DEFAULT NULL);
```

Parameters

Table 231-6 CHANGE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `line` | The text to search in. The output value of this parameter is the altered string. |
| mline | The text to search in. This is a `owa_text.multi_line datatype`. The output value of this parameter is the altered string. |
| `from_str` | The regular expression to replace. |
| to\_str | The substitution pattern. |
| flags | Whether or not the search is case-sensitive, and whether or not changes are to be made globally. If " `i` " is specified, the search is case-insensitive. If " `g` " is specified, changes are made to all matches. Otherwise, the function stops after the first substitution is made. |

Return Values

As a function, it returns the number of substitutions made. If the flag "g" is not used, this number can only be 0 or 1 and only the first match is replaced. The flag "g" specifies to replace all matches with the regular expression.

Examples

```
OWA_PATTERN.CHANGE('Cats in pajamas', 'C.+in', '& red ')
```

The regular expression matches the substring " `Cats` `in` ". It then replaces this string with "& red". The ampersand character " `&` " indicates " `Cats` `in` " because that is what matched the regular expression. Thus, this procedure replaces the string " `Cats` `in` `pajamas` " with " `Cats` `in` `red` " If you call this as a function instead of a procedure, the value returned is 1, indicating that a single substitution has been made.

Example 2:

```
CREATE OR REPLACE PROCEDURE test_pattern as theline VARCHAR2(256);
num_found     INTEGER;
   BEGIN
       theline := 'what is the goal?';
       num_found := OWA_PATTERN.CHANGE(theline, 'goal', 'idea', 'g');
       HTP.PRINT(num_found); -- num_found is 1
       HTP.PRINT(theline); -- theline is 'what is the idea?'
   END;
/
SHOW ERRORS
```

#### 231.3.3 GETPAT Procedure

This procedure converts a VARCHAR2 string into an `OWA_PATTERN.PATTERN DATA TYPE`.

Syntax

```
OWA_PATTERN.GETPAT(
   arg      IN          VARCHAR2, 
   pat      IN OUT      pattern);
```

Parameters

Table 231-7 GETPAT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `arg` | The string to convert. |
| pat | the `OWA_PATTERN.PATTERN DATA TYPE` initialized with `arg`. |

#### 231.3.4 MATCH Function

This function determines if a string contains the specified pattern. The pattern can contain regular expressions. If multiple overlapping strings can match the regular expression, this function takes the longest match.

Syntax

```
owa_pattern.match(
   line           IN       VARCHAR2,
   pat            IN       VARCHAR2,
   flags          IN       VARCHAR2   DEFAULT NULL)
 RETURN BOOLEAN;

owa_pattern.match(
   line           IN       VARCHAR2,
   pat            IN OUT   PATTERN,
   flags          IN       VARCHAR2   DEFAULT NULL)
 RETURN BOOLEAN;

owa_pattern.match(
   line           IN       VARCHAR2,
   pat            IN       VARCHAR2,
   backrefs       OUT      owa_text.vc_arr,
   flags          IN       VARCHAR2   DEFAULT NULL)
 RETURN BOOLEAN;

OWA_PATTERN.MATCH(
   line           IN       VARCHAR2,
   pat            IN OUT   PATTERN,
   backrefs       OUT      owa_text.vc_arr,
   flags          IN       VARCHAR2   DEFAULT NULL)
 RETURN BOOLEAN;

owa_pattern.match(
   mline          IN       owa_text.multi_line,
   pat            IN       VARCHAR2,
   rlist          OUT      owa_text.row_list,
   flags          IN       VARCHAR2   DEFAULT NULL)
 RETURN BOOLEAN;

OWA_PATTERN.MATCH(
   mline          IN       owa_text.multi_line,
   pat            IN OUT   pattern,
   rlist          OUT      owa_text.row_list,
   flags          IN       VARCHAR2   DEFAULT NULL)
 RETURN BOOLEAN;
```

Parameters

Table 231-8 MATCH Function Parameters

| Parameter | Description |
| --- | --- |
| `line` | The line to search in. |
| `mline` | The text to search in. This is a `owa_text.multi_line datatype`.. |
| `pat` | The pattern to match. This is either a `VARCHAR2` or a `OWA_PATTERN.PATTERN DATA TYPE`. It is a pattern, the output value of this parameter is the pattern matched. |
| `backrefs` | The text that is matched. Each token that is matched is placed in a cell in the `OWA_TEXT.VC_ARR DATA TYPE` PL/SQL table. `This parameter is a row_list` that holds each string in the target that was matched by a sequence of tokens in the regular expression. |
| `rlist` | An output parameter containing a list of matches. |
| `flags` | Whether or not the search is case-sensitive. If the value of this parameter is "i", the search is case-insensitive. Otherwise the search is case-sensitive. |

Return Values

`TRUE` if a match was found, `FALSE` otherwise.

Examples

`KAZOO` is the target where it is searching for the `zoo.*` regular expression. The period indicates any character other than newline, and the asterisk matches 0 or more of the preceding characters. In this case, it matches any character other than the newline.

Therefore, this regular expression specifies that a matching target consists of `zoo`, followed by any set of characters neither ending in nor including a newline (which does not match the period). The i flag indicates to ignore case in the search. In this case, the function returns `TRUE`, which indicates that a match had been found.

```
boolean foundMatch;
foundMatch := owa_pattern.match('KAZOO', 'zoo.*', 'i');
```

The following example searches for the string "goal" followed by any number of characters in `sometext`. If found,

```
sometext  VARCHAR2(256);
pat       VARCHAR2(256);

sometext    := 'what is the goal?'
pat         := 'goal.*';
IF OWA_PATTERN.MATCH(sometext, pat) 
   THEN
      HTP.PRINT('Match found');
   ELSE
     HTP.PRINT('Match not found');
END IF;
```

Operational Notes

- The regular expression in this function can be either a `VARCHAR2` or an `OWA_PATTERN.PATTERN` `DATA` `TYPE. `Create `AN OWA_PATTERN.PATTERN DATA TYPE` from a string using the `OWA_PATTERN.GETPAT` procedure.
- Create a `MULTI_LINE` `DATA` `TYPE` from a long string using the `OWA_TEXT.STREAM2MULTI` procedure. If a `multi_line` is used, the `rlist` parameter specifies a list of chunks where matches were found.
- If the line is a string and not a `multi_line`, you can add an optional output parameter called `backrefs`. This parameter is a `row_list` that holds each string in the target that was matched by a sequence of tokens in the regular expression.