---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/UTL_ENCODE.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 266 UTL\_ENCODE

The `UTL_ENCODE` package provides functions that encode `RAW` data into a standard encoded format so that the data can be transported between hosts.

You can use `UTL_ENCODE` functions to encode the body of email text. The package also contains the decode counterpart functions of the encode functions. The functions follow published standards for encoding to accommodate non-Oracle utilities on the sending or receiving ends.

This chapter contains the following topic:

- Summary of UTL\_ENCODE Subprograms

### 266.1 Summary of UTL\_ENCODE Subprograms

This table lists the `UTL_ENCODE` subprograms and briefly describes them.

Table 266-1 UTL\_ENCODE Package Subprograms

| Subprogram | Description |
| --- | --- |
| BASE64\_DECODE Function | Reads the base 64-encoded `RAW` input string and decodes it to its original `RAW` value |
| BASE64\_ENCODE Function | Encodes the binary representation of the `RAW` value into base 64 elements and returns it in the form of a `RAW` string |
| [MIMEHEADER\_DECODE Function](https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/UTL_ENCODE.html#GUID-750328A9-62A5-4DC2-8269-CE883CA02A16 "This function accepts as input an \"encoded word.”") | Decodes a string from mime header format |
| [MIMEHEADER\_ENCODE Function](https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/UTL_ENCODE.html#GUID-E3973786-34DA-48ED-964C-AF34D372B194 "This function returns as an output an \"encoded word\".") | Encodes a string into mime header format |
| QUOTED\_PRINTABLE\_DECODE Function | Reads the `varchar2` quoted printable format input string and decodes it to the corresponding `RAW` string |
| QUOTED\_PRINTABLE\_ENCODE Function | Reads the `RAW` input string and encodes it to the corresponding quoted printable format string |
| TEXT\_DECODE Function | Decodes a character set sensitive text string |
| TEXT\_ENCODE Function | Encodes a character set sensitive text string |
| UUDECODE Function | Reads the `RAW` uuencode format input string and decodes it to the corresponding `RAW` string |
| UUENCODE Function | Reads the `RAW` input string and encodes it to the corresponding uuencode format string |

#### 266.1.1 BASE64\_DECODE Function

This function reads the base 64-encoded `RAW` input string and decodes it to its original `RAW` value.

Syntax

```
UTL_ENCODE.BASE64_DECODE (
   r  IN RAW) 
RETURN RAW;
```

Pragmas

```
pragma RESTRICT_REFERENCES(base64_decode, WNDS, RNDS, WNPS, RNPS);
```

Parameters

Table 266-2 BASE64\_DECODE Function Parameters

| Parameter | Description |
| --- | --- |
| `r` | The RAW string containing base 64-encoded data. There are no defaults or optional parameters. |

Return Values

Table 266-3 BASE64\_DECODE Function Return Values

| Return | Description |
| --- | --- |
| `RAW` | Contains the decoded string |

#### 266.1.2 BASE64\_ENCODE Function

This function encodes the binary representation of the `RAW` value into base 64 elements and returns it in the form of a `RAW` string.

Syntax

```
UTL_ENCODE.BASE64_ENCODE (
   r  IN RAW) 
RETURN RAW;
```

Pragmas

```
pragma RESTRICT_REFERENCES(base64_encode, WNDS, RNDS, WNPS, RNPS);
```

Parameters

Table 266-4 BASE64\_ENCODE Function Parameters

| Parameter | Description |
| --- | --- |
| `r` | The RAW value to be encoded. There are no defaults or optional parameters. |

Return Values

Table 266-5 BASE64\_ENCODE Function Return Values

| Return | Description |
| --- | --- |
| `RAW` | Contains the encoded base 64 elements |

#### 266.1.3 MIMEHEADER\_DECODE Function

This function accepts as input an "encoded word.”

It uses the form:

```
=?<charset>?<encoding>?<encoded text>?= 
=?ISO-8859-1?Q?Here is some encoded text?=
```

The `<encoded text>` is encapsulated in mime header tags which give the `MIMEHEADER_DECODE` function information about how to decode the string. The mime header metadata tags are stripped from the input string and the `<encoded text>` is converted to the base database character set as follows:

- If this is a UTF16 platform, convert the encoded text from UTF16 to ASCII
- If this is an EBCDIC platform, convert the encoded text from EBCDIC to ASCII
- If this is an ASCII or UTF8 platform, no conversion needed

The string is decoded using either quoted-printable or base64 decoding, as specified by the `<encoding> ` metadata tag in the encoded word. The resulting converted and decoded text is returned to the caller as a `VARCHAR2` string.

Syntax

```
UTL_ENCODE.MIMEHEADER_DECODE (
   buf    IN   VARCHAR2 CHARACTER SET ANY_CS) 
  RETURN data VARCHAR2 CHARACTER SET buf%CHARSET;
```

Parameters

Table 266-6 MIMEHEADER\_DECODE Function Parameters

| Parameter | Description |
| --- | --- |
| `buf` | The encoded text data with mime header format tags. |

Return Values

Table 266-7 MIMEHEADER\_DECODE Function Return Values

| Return | Description |
| --- | --- |
| `data` | The encoded text data with mime header format tags |

Examples

```
v2:=utl_encode.mimeheader_decode('=?ISO-8859-1?Q?Here is some encoded text?=');
```

#### 266.1.4 MIMEHEADER\_ENCODE Function

This function returns as an output an "encoded word".

The output is in the following form:

```
=?<charset>?<encoding>?<encoded text>?= 
=?ISO-8859-1?Q?Here is some text?=
```

The `buf` input parameter is the text to be encoded and becomes the `<encoded text>`.

The \<encoding> value is either "Q" or "B" for quoted-printable encode or base64 encoding respectively. The ENCODING input parameter accepts as valid values `UTL_ENCODE.QUOTED_PRINTABLE` or `UTL_ENCODE.BASE64` or `NULL`. If `NULL`, quoted-printable encoding is selected as a default value.

The `<charset>` value is specified as the input parameter `encode_charset`. If `NULL`, the database character set is selected as a default value.

The mimeheader encoding process includes conversion of the `buf` input string to the character set specified by the `encode_charset` parameter. The converted string is encoded to either quoted-printable or base64 encoded format. The mime header tags are appended and prepended.

Finally, the string is converted to the base character set of the database:

- If this is a UTF16 platform, convert the encoded text to UTF16
- If this is an EBCDIC platform, convert the encoded text to EBCDIC
- If this is an ASCII or UTF8 platform, no conversion needed.

Syntax

```
UTL_ENCODE.MIMEHEADER_ENCODE (
   buf            IN  VARCHAR2 CHARACTER SET ANY_CS, 
   encode_charset IN  VARCHAR2 DEFAULT NULL, 
   encoding       IN  PLS_INTEGER DEFAULT NULL) 
 RETURN string VARCHAR2 CHARACTER SET buf%CHARSET;
```

Parameters

Table 266-8 MIMEHEADER\_ENCODE Function Parameters

| Parameter | Description |
| --- | --- |
| `buf` | The text data. |
| `encode_charset` | The target character set. |
| `encoding` | The encoding format. Valid values are `UTL_ENCODE`.`BASE64`, `UTL_ENCODE`.`QUOTED_PRINTABLE` and `NULL` |

Return Values

Table 266-9 MIMEHEADER\_ENCODE Function Return Values

| Return | Description |
| --- | --- |
| `string` | A `VARCHAR2` encoded string with mime header format tags. |

#### 266.1.5 QUOTED\_PRINTABLE\_DECODE Function

This function reads the `varchar2` quoted printable format input string and decodes it to the corresponding `RAW` string.

Syntax

```
UTL_ENCODE.QUOTED_PRINTABLE_DECODE (
   r  IN RAW)
RETURN RAW;
```

Pragmas

```
pragma RESTRICT_REFERENCES(quoted_printable_decode, WNDS, RNDS, WNPS, RNPS);
```

Parameters

Table 266-10 QUOTED\_PRINTABLE\_DECODE Function Parameters

| Parameters | Description |
| --- | --- |
| `r` | The RAW string containing a quoted printable data string. There are no defaults or optional parameters. |

Return Values

Table 266-11 QUOTED\_PRINTABLE\_DECODE Function Return Values

| Return | Description |
| --- | --- |
| `RAW` | The decoded string |

#### 266.1.6 QUOTED\_PRINTABLE\_ENCODE Function

This function reads the `RAW` input string and encodes it to the corresponding quoted printable format string.

Syntax

```
UTL_ENCODE.QUOTED_PRINTABLE_ENCODE (
   r  IN RAW)
RETURN RAW;
```

Pragmas

```
pragma RESTRICT_REFERENCES(quoted_printable_encode, WNDS, RNDS,WNPS, RNPS);
```

Parameters

Table 266-12 QUOTED\_PRINTABLE\_ENCODE Function Parameters

| Parameter | Description |
| --- | --- |
| `r` | The RAW string. There are no defaults or optional parameters. |

Return Values

Table 266-13 QUOTED\_PRINTABLE\_ENCODE Function Return Values

| Return | Description |
| --- | --- |
| `RAW` | Contains the quoted printable string |

#### 266.1.7 TEXT\_DECODE Function

This function converts the input text to the target character set as specified by the `encode_charset` parameter, if not `NULL`.

The encoded text is converted to the base character set of database, as follows:

- If this is a UTF16 platform, convert the encoded text from UTF16 to ASCII
- If this is an EBCDIC platform, convert the encoded text from EBCDIC to ASCII
- If this is an ASCII or UTF8 platform, no conversion needed

You can decode from either quoted-printable or base64 format, with regard to each `encoding` parameter. If `NULL`, quoted-printable is selected as a default decoding format. If `encode_charset` is not `NULL`, you convert the string from the specified character set to the database character set. The resulting decoded and converted text string is returned to the caller.

Syntax

```
UTL_ENCODE.TEXT_DECODE(
   buf            IN  VARCHAR2 CHARACTER SET ANY_CS, 
   encode_charset IN  VARCHAR2 DEFAULT NULL, 
   encoding       IN  PLS_INTEGER DEFAULT NULL) 
 RETURN string VARCHAR2 CHARACTER SET buf%CHARSET;
```

Parameters

Table 266-14 TEXT\_DECODE Function Parameters

| Parameter | Description |
| --- | --- |
| `buf` | The encoded text data. |
| `encode_charset` | The source character set. |
| `encoding` | The encoding format. Valid values are `UTL_ENCODE`.`BASE64`, `UTL_ENCODE`.`QUOTED_PRINTABLE` and `NULL.` |

Return Values

Table 266-15 TEXT\_DECODE Function Return Values

| Return | Description |
| --- | --- |
| `string` | A `VARCHAR2` decoded text string. |

Examples

```
v2:=UTL_ENCODE.TEXT_DECODE( 
     'Here is some text', 
      WE8ISO8859P1, 
      UTL_ENCODE.BASE64);
```

#### 266.1.8 TEXT\_ENCODE Function

This function converts the input text to the target character set as specified by the `encode_charset` parameter, if not `NULL`.

The text is encoded to either base64 or quoted-printable format, as specified by the `encoding` parameter. Quoted-printable is selected as a default if ENCODING is NULL.

The encoded text is converted to the base character set of the database:

- If this is a UTF16 platform, convert the encoded text to UTF16
- If this is an EBCDIC platform, convert the encoded text to EBCDIC
- If this is an ASCII or UTF8 platform, no conversion needed

The resulting encoded and converted text string is returned to the caller.

Syntax

```
UTL_ENCODE.TEXT_ENCODE (
   buf            IN  VARCHAR2 CHARACTER SET ANY_CS, 
   encode_charset IN  VARCHAR2 DEFAULT NULL, 
   encoding       IN  PLS_INTEGER DEFAULT NULL) 
 RETURN string VARCHAR2 CHARACTER SET buf%CHARSET;
```

Parameters

Table 266-16 TEXT\_ENCODE Function Parameters

| Parameter | Description |
| --- | --- |
| `buf` | The text data. |
| `encode_charset` | The target character set. |
| `encoding` | The encoding format. Valid values are `UTL_ENCODE`.`BASE64`, `UTL_ENCODE`.`QUOTED_PRINTABLE` and `NULL` |

Return Values

Table 266-17 TEXT\_ENCODE Function Return Values

| Return | Description |
| --- | --- |
| `string` | A `VARCHAR2` encoded string with mime header format tags. |

Examples

```
v2:=utl_encode.text_encode( 
   'Here is some text', 
   'WE8ISO8859P1', 
    UTL_ENCODE.BASE64);
```

#### 266.1.9 UUDECODE Function

This function reads the `RAW` uuencode format input string and decodes it to the corresponding `RAW` string.

See " UUENCODE Function " for discussion of the cumulative nature of `UUENCODE` and `UUDECODE` for data streams.

Syntax

```
UTL_ENCODE.UUDECODE (
   r  IN RAW) 
RETURN RAW;
```

Pragmas

```
pragma RESTRICT_REFERENCES(uudecode, WNDS, RNDS, WNPS, RNPS);
```

Parameters

Table 266-18 UUDECODE Function Parameters

| Parameter | Description |
| --- | --- |
| `r` | The RAW string containing the uuencoded data string. There are no defaults or optional parameters. |

Return Values

Table 266-19 UUDECODE Function Return Values

| Return | Description |
| --- | --- |
| `RAW` | The decoded `RAW` string |

#### 266.1.10 UUENCODE Function

This function reads the `RAW` input string and encodes it to the corresponding uuencode format string.

The output of this function is cumulative, in that it can be used to encode large data streams, by splitting the data stream into acceptably sized `RAW` values, encoded, and concatenated into a single encoded string.

Syntax

```
UTL_ENCODE.UUENCODE (
   r          IN RAW,
   type       IN PLS_INTEGER DEFAULT 1,
   filename   IN VARCHAR2 DEFAULT NULL,
   permission IN VARCHAR2 DEFAULT NULL) RETURN RAW;
```

Pragmas

```
pragma RESTRICT_REFERENCES(uuencode, WNDS, RNDS, WNPS, RNPS);
```

Parameters

Table 266-20 UUENCODE Function Parameters

| Parameter | Description |
| --- | --- |
| `r` | `RAW` string |
| `type` | Optional number parameter containing the type of uuencoded output. Options:  complete—a defined PL/SQL constant with a value of `1`. (default) header\_piece...middle\_piece...end\_piece |
| `filename` | Optional `varchar2` parameter containing the uuencode filename; the default is `uuencode.txt` |
| `permission` | Optional `varchar2` parameter containing the permission mode; the default is `0` (a text string zero). |

Return Values

Table 266-21 UUENCODE Function Return Values

| Return | Description |
| --- | --- |
| `RAW` | Contains the uuencode format string |