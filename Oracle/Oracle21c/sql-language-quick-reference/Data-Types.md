---
title: SQL Language Quick Reference
book: SQL Language Quick Reference
doc_id: F31302-11
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqlqr/Data-Types.html
tags:
  - oracle
  - 21c
  - sql-language-quick-reference
---

This chapter presents data types that are recognized by Oracle and available for use within SQL.

This chapter includes the following sections:

### Overview of Data Types

A data type is a classification of a particular type of information or data. Each value manipulated by Oracle has a data type. The data type of a value associates a fixed set of properties with the value. These properties cause Oracle to treat values of one data type differently from values of another.

The data types recognized by Oracle are:

ANSI-supported data types

```
{ CHARACTER [VARYING] (size)
| { CHAR | NCHAR } VARYING (size)
| VARCHAR (size)
| NATIONAL { CHARACTER | CHAR }
     [VARYING] (size)
| { NUMERIC | DECIMAL | DEC }
     [ (precision [, scale ]) ]
| { INTEGER | INT | SMALLINT }
| FLOAT [ (size) ]
| DOUBLE PRECISION
| REAL
}
```

Oracle built-in data types

```
{ character_datatypes
| number_datatypes
| long_and_raw_datatypes
| datetime_datatypes
| large_object_datatypes
| rowid_datatypes
}
```

Oracle-supplied data types

```
{ any_types
| XML_types
| spatial_types
| media_types
}
```

User-defined data types

User-defined data types use Oracle built-in data types and other user-defined data types to model the structure and behavior of data in applications.

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF0021) for more information about data types

### Oracle Built-In Data Types

This section describes the kinds of Oracle built-in data types.

character\_datatypes

```
{ CHAR [ (size [ BYTE | CHAR ]) ]
| VARCHAR2 (size [ BYTE | CHAR ])
| NCHAR [ (size) ]
| NVARCHAR2 (size)
}
```

datetime\_datatypes

```
{ DATE
| TIMESTAMP [ (fractional_seconds_precision) ]
     [ WITH [ LOCAL ] TIME ZONE ]
| INTERVAL YEAR [ (year_precision) ] TO MONTH
| INTERVAL DAY [ (day_precision) ] TO SECOND
     [ (fractional_seconds_precision) ]
}
```

large\_object\_datatypes

```
{ BLOB | CLOB | NCLOB | BFILE }
```

long\_and\_raw\_datatypes

```
{ LONG | LONG RAW | RAW (size) }
```

number\_datatypes

```
{ NUMBER [ (precision [, scale ]) ]
| FLOAT [ (precision) ]
| BINARY_FLOAT
| BINARY_DOUBLE
}
```

rowid\_datatypes

```
{ ROWID | UROWID [ (size) ] }
```

The codes listed for the data types are used internally by Oracle Database. The data type code of a column or object attribute is returned by the `DUMP` function.

Table 6-1 Built-in Data Type Summary

| Code | Data Type | Description |
| --- | --- | --- |
| 1 | `VARCHAR2` (`size` \[`BYTE` \| `CHAR`\]) | Variable-length character string having maximum length `size` bytes or characters. You must specify `size` for `VARCHAR2`. Minimum `size` is 1 byte or 1 character. Maximum size is:  - 32767 bytes or characters if `MAX_STRING_SIZE` `=` `EXTENDED` - 4000 bytes or characters if `MAX_STRING_SIZE` `=` `STANDARD`  Refer to [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF55623) for more information on the `MAX_STRING_SIZE` initialization parameter.  `BYTE` indicates that the column will have byte length semantics. `CHAR` indicates that the column will have character semantics. |
| 1 | `NVARCHAR2` (`size`) | Variable-length Unicode character string having maximum length `size` characters. You must specify `size` for `NVARCHAR2`. The number of bytes can be up to two times `size` for `AL16UTF16` encoding and three times `size` for `UTF8` encoding. Maximum `size` is determined by the national character set definition, with an upper limit of:  - 32767 bytes if `MAX_STRING_SIZE` `=` `EXTENDED` - 4000 bytes if `MAX_STRING_SIZE` `=` `STANDARD`  Refer to [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF55623) for more information on the `MAX_STRING_SIZE` initialization parameter. |
| 2 | `NUMBER ` \[ (`p` \[, `s`\]) \] | Number having precision `p` and scale `s`. The precision `p` can range from 1 to 38. The scale `s` can range from -84 to 127. Both precision and scale are in decimal digits. A `NUMBER` value requires from 1 to 22 bytes. |
| 2 | `FLOAT` \[(`p`)\] | A subtype of the `NUMBER` data type having precision `p`. A `FLOAT` value is represented internally as `NUMBER`. The precision `p` can range from 1 to 126 binary digits. A `FLOAT` value requires from 1 to 22 bytes. |
| 8 | `LONG` | Character data of variable length up to 2 gigabytes, or 2 <sup>31</sup> -1 bytes. Provided for backward compatibility. |
| 12 | `DATE` | Valid date range from January 1, 4712 BC, to December 31, 9999 AD. The default format is determined explicitly by the `NLS_DATE_FORMAT` parameter or implicitly by the `NLS_TERRITORY` parameter. The size is fixed at 7 bytes. This data type contains the datetime fields `YEAR`, `MONTH`, `DAY`, `HOUR`, `MINUTE`, and `SECOND`. It does not have fractional seconds or a time zone. |
| 100 | `BINARY_FLOAT` | 32-bit floating point number. This data type requires 4 bytes. |
| 101 | `BINARY_DOUBLE` | 64-bit floating point number. This data type requires 8 bytes. |
| 180 | `TIMESTAMP` \[(`fractional_seconds_precision`)\] | Year, month, and day values of date, as well as hour, minute, and second values of time, where `fractional_seconds_precision` is the number of digits in the fractional part of the `SECOND` datetime field. Accepted values of `fractional_seconds_precision` are 0 to 9. The default is 6. The default format is determined explicitly by the `NLS_TIMESTAMP_FORMAT` parameter or implicitly by the `NLS_TERRITORY` parameter. The size is 7 or 11 bytes, depending on the precision. This data type contains the datetime fields `YEAR`, `MONTH`, `DAY`, `HOUR`, `MINUTE`, and `SECOND`. It contains fractional seconds but does not have a time zone. |
| 181 | `TIMESTAMP` \[(`fractional_seconds_precision`)\] `WITH` `TIME` `ZONE` | All values of `TIMESTAMP` as well as time zone displacement value, where `fractional_seconds_precision` is the number of digits in the fractional part of the `SECOND` datetime field. Accepted values are 0 to 9. The default is 6. The default format is determined explicitly by the `NLS_TIMESTAMP_FORMAT` parameter or implicitly by the `NLS_TERRITORY` parameter. The size is fixed at 13 bytes. This data type contains the datetime fields `YEAR`, `MONTH`, `DAY`, `HOUR`, `MINUTE`, `SECOND`, `TIMEZONE_HOUR`, and `TIMEZONE_MINUTE`. It has fractional seconds and an explicit time zone. |
| 231 | `TIMESTAMP` \[(`fractional_seconds_precision`)\] `WITH` `LOCAL` `TIME` `ZONE` | All values of `TIMESTAMP` `WITH` `TIME` `ZONE`, with the following exceptions:  - Data is normalized to the database time zone when it is stored in the database. - When the data is retrieved, users see the data in the session time zone.  The default format is determined explicitly by the `NLS_TIMESTAMP_FORMAT` parameter or implicitly by the `NLS_TERRITORY` parameter. The size is 7 or 11 bytes, depending on the precision. |
| 182 | `INTERVAL` `YEAR` \[(`year_precision`)\] `TO` `MONTH` | Stores a period of time in years and months, where `year_precision` is the number of digits in the `YEAR` datetime field. Accepted values are 0 to 9. The default is 2. The size is fixed at 5 bytes. |
| 183 | `INTERVAL` `DAY` \[(`day_precision`)\] `TO` `SECOND` \[(`fractional_seconds_precision`)\] | Stores a period of time in days, hours, minutes, and seconds, where  - `day_precision` is the maximum number of digits in the `DAY` datetime field. Accepted values are 0 to 9. The default is 2. - `fractional_seconds_precision` is the number of digits in the fractional part of the `SECOND` field. Accepted values are 0 to 9. The default is 6.  The size is fixed at 11 bytes. |
| 23 | `RAW` (`size`) | Raw binary data of length `size` bytes. You must specify `size ` for a `RAW` value. Maximum `size` is:  - 32767 bytes if `MAX_STRING_SIZE` `=` `EXTENDED` - 2000 bytes if `MAX_STRING_SIZE` `=` `STANDARD`  Refer to [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF55623) for more information on the `MAX_STRING_SIZE` initialization parameter. |
| 24 | `LONG RAW` | Raw binary data of variable length up to 2 gigabytes. |
| 69 | `ROWID` | Base 64 string representing the unique address of a row in its table. This data type is primarily for values returned by the `ROWID` pseudocolumn. |
| 208 | `UROWID` \[(`size`)\] | Base 64 string representing the logical address of a row of an index-organized table. The optional `size` is the size of a column of type `UROWID`. The maximum size and default is 4000 bytes. |
| 96 | `CHAR` \[(`size` \[`BYTE` \| `CHAR`\])\] | Fixed-length character data of length `size` bytes or characters. Maximum `size` is 2000 bytes or characters. Default and minimum `size` is 1 byte.  `BYTE` and `CHAR` have the same semantics as for `VARCHAR2`. |
| 96 | `NCHAR` \[(`size`)\] | Fixed-length character data of length `size` characters. The number of bytes can be up to two times `size` for `AL16UTF16` encoding and three times `size` for `UTF8` encoding. Maximum `size` is determined by the national character set definition, with an upper limit of 2000 bytes. Default and minimum `size` is 1 character. |
| 112 | `CLOB` | A character large object containing single-byte or multibyte characters. Both fixed-width and variable-width character sets are supported, both using the database character set. Maximum size is (4 gigabytes - 1) \* (database block size). |
| 112 | `NCLOB` | A character large object containing Unicode characters. Both fixed-width and variable-width character sets are supported, both using the database national character set. Maximum size is (4 gigabytes - 1) \* (database block size). Stores national character set data. |
| 113 | `BLOB` | A binary large object. Maximum size is (4 gigabytes - 1) \* (database block size). |
| 114 | `BFILE` | Contains a locator to a large binary file stored outside the database. Enables byte stream I/O access to external LOBs residing on the database server. Maximum size is 4 gigabytes. |

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF30020) for more information about built-in data types

### Oracle-Supplied Data Types

This section shows the syntax for the Oracle-supplied data types.

any\_types

```
{ SYS.AnyData | SYS.AnyType | SYS.AnyDataSet }
```

spatial\_types

```
{ SDO_Geometry | SDO_Topo_Geometry |SDO_GeoRaster }
```

XML\_types

```
{ XMLType | URIType }
```

### Converting to Oracle Data Types

SQL statements that create tables and clusters can also use ANSI data types and data types from the IBM products SQL/DS and DB2. Oracle recognizes the ANSI or IBM data type name that differs from the Oracle data type name, records it as the name of the data type of the column, and then stores the column data in an Oracle data type based on the conversions shown in the following table.

Table 6-2 ANSI Data Types Converted to Oracle Data Types

| ANSI SQL Data Type | Oracle Data Type |
| --- | --- |
| `CHARACTER(n)`  `CHAR(n)` | `CHAR(n)` |
| `CHARACTER VARYING(n)`  `CHAR VARYING(n)` | `VARCHAR2(n)` |
| `NATIONAL CHARACTER(n)`  `NATIONAL CHAR(n)`  `NCHAR(n)` | `NCHAR(n)` |
| `NATIONAL CHARACTER VARYING(n)`  `NATIONAL CHAR VARYING(n)`  `NCHAR VARYING(n)` | `NVARCHAR2(n)` |
| `NUMERIC[(p,s)]`  `DECIMAL[(p,s)]` (Note 1) | `NUMBER(p,s)` |
| `INTEGER`  `INT`  `SMALLINT` | `NUMBER(38)` |
| `FLOAT` (Note 2)  `DOUBLE PRECISION` (Note 3)  `REAL` (Note 4) | `FLOAT(126)`  `FLOAT(126)`  `FLOAT(63)` |

Notes:

1. The `NUMERIC` and `DECIMAL` data types can specify only fixed-point numbers. For those data types, the scale (`s`) defaults to 0.
2. The `FLOAT` data type is a floating-point number with a binary precision b. The default precision for this data type is 126 binary, or 38 decimal.
3. The `DOUBLE PRECISION` data type is a floating-point number with binary precision 126.
4. The `REAL` data type is a floating-point number with a binary precision of 63, or 18 decimal.

Do not define columns with the following SQL/DS and DB2 data types, because they have no corresponding Oracle data type:

- `GRAPHIC`
- `LONG` `VARGRAPHIC`
- `VARGRAPHIC`
- `TIME`

Note that data of type `TIME` can also be expressed as Oracle datetime data.

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF0021) for more information on data types