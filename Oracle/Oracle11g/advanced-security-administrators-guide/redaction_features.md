---
title: Oracle Data Redaction Features and Capabilities
book: "Advanced Security Administrator's Guide"
doc_id: E40393-10
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/network.112/e40393/redaction_features.htm
tags:
  - oracle
  - 11g
  - advanced-security-administrators-guide
---

## 4 Oracle Data Redaction Features and Capabilities

Oracle Data Redaction provides a variety of ways to redact different types of data.

This chapter contains the following topics:

## 4.1 Using Full Data Redaction to Redact All Data

When an Oracle Data Redaction policy that specifies full data redaction is applied to a table or view, the entire contents of the column are redacted. By default the output is displayed as follows:

- Character data types: The output text is a single space.
- Number data types: The output text is a zero (`0`).
- Date-time data types: The output text is set to the first day of January, 2001, which appears as `01-JAN-01`.

Full redaction is the default and is used whenever a Data Redaction policy specifies the column but omits the `function_type` parameter setting. When you run the `DBMS_REDACT.ADD_POLICY` procedure, to set the `function_type` parameter setting for full redaction, you enter the following setting:

```
function_type    => DBMS_REDACT.FULL
```

You can use the `DBMS_REDACT.UPDATE_FULL_REDACTION_VALUES` procedure to change the full redaction output to different values.

## 4.2 Using Partial Data Redaction to Redact Sections of Data

In partial data redaction, you redact portions of the displayed output. You can set the position within the [actual data](asogls.md) at which to begin the redaction, the number of characters to redact starting from that position, and the redaction character to use. This type of redaction is useful for situations where you want it to be obvious to the person viewing the data that it was redacted in some way. Typically, you use this type of redaction for credit cards or ID numbers.

Be aware that partial data redaction requires that your data width remain fixed. If you want to redact columns containing string values of variable length, then you must use regular expressions, as described in "Using Regular Expressions to Redact Patterns of Data".

To specify partial redaction, you must set the `DBMS_REDACT.ADD_POLICY` procedure `function_type` parameter to `DBMS_REDACT.PARTIAL` and use the `function_parameters` parameter to define the partial redaction behavior.

The displayed output for partial data redaction can be as follows:

- Character data types: When partially redacted, a Social Security number (represented as a hyphenated string within a character data type) with value `987-65-4320` could be redacted so that it is displayed as shown in the following examples. The code on the right specifies how to redact the character data: it specifies the expected input format of the [actual data](asogls.md), the format to use for the display of the redacted output, the start position at which to begin the redaction, the character to use for the redaction, and how many characters to redact. The first example uses a predefined shortcut for character data type Social Security numbers, and the second example replaces the first five numbers with an asterisk (`*`) while preserving the hyphens (`-`) in between the numbers.
	```
	XXX-XX-4320    function_parameters => DBMS_REDACT.REDACT_US_SSN_F5,
	***-**-4320    function_parameters => 'VVVFVVFVVVV,VVV-VV-VVVV,*,1,5',
	```
- Number data types: The partially redacted `NUMBER` data type Social Security number `987654328` could appear as follows. Both redact the first five digits. The first example uses a predefined shortcut that is designed for Social Security numbers in the `NUMBER` data type, and the second replaces the first five numbers with the number `9`, starting from the first digit.
	```
	XXXXX4328    function_parameters => DBMS_REDACT.REDACT_NUM_US_SSN_F5,
	999994328    function_parameters => '9,1,5',
	```
- Date-time data types: Partially redacted datetime values can appear simply as different dates. For example, the date `29-AUG-11 10.20.50.000000 AM` could appear as follows. In the first example, the day of the month is redacted to `02` (using the setting `d02`) and in the second example, the month is redacted to `DEC` (using `m12`). The uppercase values show the actual month (`M`), year (`Y`), hour (`H`), minute (`M`), and second (`S`).
	```
	02-AUG-11 10.20.50.000000 AM   function_parameters  =>  'Md02YHMS',
	29-DEC-11 10.20.50.000000 AM   function_parameters  =>  'm12DYHMS',
	```

## 4.3 Using Regular Expressions to Redact Patterns of Data

You can use regular expressions to redact specific data within a column data value, based on a pattern search. For example, you can redact the user name of email addresses, so that only the domain shows (for example, replacing `hpreston` in the email address `hpreston@example.com` with `[redacted]` so that it appears as `[redacted]@example.com`). To perform the redaction, set the `DBMS_REDACT.ADD_POLICY` procedure `function_type` parameter to `DBMS_REDACT.REGEXP`, and then use the following parameters to build the regular expression:

- A string search pattern (that is, the values to search for), such as:
	```
	regexp_pattern         => '(.+)@(.+\.[A-Za-z]{2,4})'
	```
	This setting looks for a pattern of the following form:
	```
	one_or_more_characters@one_or_more_characters.2-4_characters_in_range_A-Z_or_a-z
	```
- A replacement string, which replaces the value matched by the `regexp_pattern` setting. The replacement string can include back references to sub-expressions of the main regular expression pattern. The following example replaces the data before the `@` symbol (from the `regexp_pattern` setting) with the text `[redacted]`. The `\2` setting refers to the second match group, which is `(.+\.[A-Za-z]{2,4})` from the `regexp_pattern` setting.
	```
	regexp_replace_string  => '[redacted]@\2'
	```
- The starting position for the string search string, such as the first character of the data, such as:
	```
	regexp_position        => DBMS_REDACT.RE_BEGINNING
	```
- The kind of search and replace operation to perform, such as the first occurrence, every fifth occurrence, or all of the occurrences, such as:
	```
	regexp_occurrence      => DBMS_REDACT.RE_ALL
	```
- The default matching behavior for the search and replace operation, such as whether the search is case-sensitive (`i` sets it to be not case-sensitive):
	```
	regexp_match_parameter => 'i
	```

In addition to the default parameters, you can use a set of predefined shortcuts that enable you to use commonly used regular expressions for telephone numbers, email addresses, and credit card numbers.

See Also:

["About Creating Regular Expression-Based Redaction Policies"](redaction_config.md)

## 4.4 Using Random Data Redaction to Generate Random Values

In random data redaction, the entire value is redacted by replacing it with a random value. The redacted values displayed in the result set of the query change randomly each time application users run the query. This type of redaction is useful in cases where you do not want it to be obvious that the data was redacted. It works especially well for number and datetime data types, where it is difficult to distinguish between random and real data.

The displayed output for random values changes based on the data type of the redacted column, as follows:

- Character data types: The random output is a mixture of characters (for example, `HTU[G{\pjkEWcK`). It behaves differently for the `CHAR` and `VARCHAR2` data types, as follows:
	- CHAR data type: The redacted output is always in the same character set as the character set of the column. The byte length of the redacted output is always the same as the column definition length (that is, the column length that was provided at the time of table creation). For example, if the column is `CHAR(20)`, then a string of 20 random characters is provided in the redacted output of the user's query.
		- VARCHAR2 data type: For random redaction of a `VARCHAR` data type, the redacted output is always in the same character set as the character set of the column. The length of the redacted output is limited based on the length of the [actual data](asogls.md) in the column. No characters in excess of the length of the actual data are displayed. For example, if the column is `VARCHAR2(20)` and the row being redacted contains actual data with a length of 12, then a string of 12 random characters (not 20) is provided in the redacted output of the user's query for that row.
- Number data types: Each actual number value is redacted by replacing it with a random, non-negative number modulo the absolute value of the actual data. This redaction results in random numbers that do not exceed the precision of the actual data. For example, the number `987654321` can be redacted by replacing it with any of the numbers `12345678`, `13579`, `0`, or `987654320`, but not by replacing it with any of the numbers `987654321`, `99987654321`, or `-1`. The number `-123` could be redacted by replacing it with the numbers `122`, `0`, or `83`, but not by replacing it with any of the numbers `123`, `1123`, or `-2`.
	The only exception to the above is when the actual value is an integer between -1 and 9. In this case, the actual data is redacted by replacing it with a random, non-negative integer modulo ten (10).
- Date-time data types: When values of the date data type are redacted using random Data Redaction, Oracle Database displays them with random dates that are always different from those of the actual data.

The setting for using random redaction is as follows:

```
function_type    => DBMS_REDACT.RANDOM
```

See Also:

["Syntax for Creating a Random Redaction Policy"](redaction_config.md)

## 4.5 Comparison of Full, Partial, and Random Redaction Based on Data Types

The full, partial, and random data redaction styles affect the Oracle built-in, ANSI, user-defined, and Oracle supplied types in different ways.

This section contains:

- Redaction Capabilities for Oracle Built-in Data Types
- Redaction Capabilities for the ANSI Data Types
- Redaction Capabilities for the User Defined Data Types or Oracle Supplied Types

### 4.5.1 Redaction Capabilities for Oracle Built-in Data Types

Table 4-1 compares how the full, partial, and random redaction styles work for Oracle built-in data types.

Table 4-1 Redaction Capabilities for Oracle Built-in Data Types

| Data Type | Notes | Full Redaction | Partial Redaction | Random Redaction |
| --- | --- | --- | --- | --- |
| Character: `CHAR`, `VARCHAR2` (including long `VARCHAR2`, for example, `VARCHAR2(20000)`), `NCHAR`, `NVARCHAR2` | None | Default redacted value is a single blank space | Supported data type | Supported data type |
| Number: `NUMBER`, `FLOAT`, `BINARY_FLOAT`, `BINARY_DOUBLE` | None | Default redacted value is zero (`0`). | Supported data type | Supported data type |
| Raw: `LONG` `RAW`, `RAW` | None | Not a supported data type | Not a supported data type | Not a supported data type |
| Date-time: `DATE`, `TIMESTAMP`, `TIMESTAMP WITH TIME ZONE`, `TIMESTAMP WITH LOCAL TIME ZONE` | None | Default redacted value is `01-01-01` or `01-01-01 01:00:00`. | Supported data type | Supported data type |
| Interval: `INTERVAL YEAR TO MONTH`, `INTERVAL DAY TO SECOND` | None | Not a supported data type | Not a supported data type | Not a supported data type |
| Large Object: `BFILE` | None | Not a supported data type | Not a supported data type | Not a supported data type |
| Large Object: `BLOB` | The No Redaction type (`DBMS_REDACT.NONE`) does not support LOB data types. | Oracle's raw representation of `[redacted]` | Not a supported data type | Not a supported data type |
| Large Object: `CLOB`, `NCLOB` | The No Redaction type (`DBMS_REDACT.NONE`) does not support LOB data types. | Default redacted value is `[redacted]`. | Not a supported data type | Not a supported data type |
| Rowid: `ROWID`, `UROWID` | None | Not a supported data type | Not a supported data type | Not a supported data type |

### 4.5.2 Redaction Capabilities for the ANSI Data Types

Table 4-2 compares how the full, partial, and random redaction styles work for ANSI data types.

Table 4-2 Redaction Capabilities for the ANSI Data Types

| Data Type | How Converted | Full Redaction | Partial Redaction | Random Redaction |
| --- | --- | --- | --- | --- |
| `CHARACTER(n)`,  `CHAR(n)` | Converted to `CHAR(``n``)` | Default redacted value is a single blank space. | Supported data type | Supported data type |
| `CHARACTER VARYING(n)`,  `CHAR VARYING(n)` | Converted to `VARCHAR2(``n``)` | Default redacted value is a single blank space. | Supported data type | Supported data type |
| `NATIONAL CHARACTER(n)`,  `NATIONAL CHAR(n)`,  `NCHAR(n)` | Converted to `NCHAR(``n``)` | Default redacted value is a single blank space. | Supported data type | Supported data type |
| `NATIONAL CHARACTER VARYING(n)`,  `NATIONAL CHAR VARYING(n)`,  `NCHAR VARYING(n)` | Converted to `NVARCHAR2(``n``)` | Default redacted value is a single blank space. | Supported data type | Supported data type |
| `NUMERIC` \[(`p``,``s`)\]  `DECIMAL` \[(`p``,``s`)\] | Converted to `NUMBER(``p,s``)` | Default redacted value is zero (`0`). | Supported data type | Supported data type |
| `INTEGER`  `INT`  `SMALLINT` | Converted to `NUMBER(``38)` | Default redacted value is zero (`0`). | Supported data type | Supported data type |
| `FLOAT`  `DOUBLE PRECISION` | Converted to `FLOAT(``126)` | Default redacted value is zero (`0`) | Supported data type | Supported data type |
| `REAL` | Converted to `FLOAT(``63)` | Default redacted value is zero (`0`). | Supported data type | Supported data type |
| `GRAPHIC`  `LONG VARGRAPHIC`  `VARGRAPHIC`  `TIME` | None | Not a supported data type | Not a supported data type | Not a supported data type |

### 4.5.3 Redaction Capabilities for the User Defined Data Types or Oracle Supplied Types

Table 4-3 compares how the full, partial, and random redaction styles work for user defined and Oracle supplied types.

Table 4-3 Redaction Capabilities for the User Defined Data Types or Oracle Supplied Types

| Data Type or Type | Full Redaction | Partial Redaction | Random Redaction |
| --- | --- | --- | --- |
| User-defined data types | Not a supported data type | Not a supported data type | Not a supported data type |
| Any types, XML types, Oracle Spatial types, Oracle Media types | Not a supported data type | Not a supported data type | Not a supported data type |

## 4.6 Using No Redaction for Testing Purposes

You can create a Data Redaction policy that does not perform redaction. This is useful for cases in which you have a redacted base table, yet you want a specific application user to have a view that always shows the [actual data](asogls.md). You can create a new view of the redacted table and then define a Data Redaction policy for this view. The policy still exists on the base table, but no redaction is performed when the application queries using the view as long as the `DBMS_REDACT.NONE` `function_type` setting was used to create a policy on the view.