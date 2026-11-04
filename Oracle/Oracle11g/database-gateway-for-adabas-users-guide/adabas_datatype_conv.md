---
title: Data Type Conversion
book: "Database Gateway for Adabas User's Guide"
doc_id: E12074-01
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/gateways.112/e12074/adabas_datatype_conv.htm
tags:
  - oracle
  - 11g
  - database-gateway-for-adabas-users-guide
---

## A Data Type Conversion

This appendix contains the following section:

- Conversion of Predict Metadata
- Conversion of Metadata from DDM Files

## Conversion of Predict Metadata

The gateway converts Predict metadata data types in the advanced data dictionary (ADD) to Oracle data types as described in Table A-1.

Table A-1 Predict Metadata

| ADD Data Type | Oracle Data Type | Details |
| --- | --- | --- |
| `A` | `VARCHAR2` | A null-terminated string of alphanumeric characters; maximum length must be specified. An extra byte is required for the null flag. |
| `B1` | `Number(3)` | Unsigned byte integer.  Size: 1 byte  Range: 0 to +254 |
| `B2` | `Number(5)` | Unsigned word integer.  Size: 2 bytes  Range: 0 to +65535 |
| `B4` | `Number(10)` | Unsigned long integer.  Size: 4 bytes  Range: 0 to +4,294,967,294 |
| `F1` | `Number(3)` | Signed byte integer.  Size: 1 byte  Signed range: -128 to +127 |
| `F2` | `Number(5)` | Signed word integer.  Size: 2 bytes  Signed Range: -32768 to +32767 |
| `F4` | `Number(10)` | Signed long integer.  Size: 4 bytes  Range: -2147483648 to 2147483647 |
| `F8` | `Number(19)` | Signed long integer.  Size: 8 bytes  Range: -9223372036854775808 to +9223372036854775807 |
| `G4` | `FLOAT(23)` | Single floating-point number (F\_FLOAT).  Size: 4 bytes  Range: 0.29E-38 to 1.7E38  Precision: 6 digits |
| `G8` | `FLOAT(49)` | Double floating-point number (D\_FLOAT)  Size: 8 bytes  Range: 029E-38 to 1.7E38  Precision: 16 digits |
| `L` | `NUMBER(3)` | Unsigned byte integer.  Size: 1 byte  Values: 1 for `true`, 0 for `false` |
| `D` | `DATE` | ODBC date format. |
| `T` | `DATE` | ODBC time format. |
| `P` | `NUMBER` | Packed decimal  Maximum number of digits: 31  Maximum fractions: 11  Length = int (number of digits/2) + 1 byte |
| `N`, `U` | `NUMBER` | Signed numeric string. A right overpunched sign is implemented.  Maximum number of digits: 31  Maximum fractions: 11 |

## Conversion of Metadata from DDM Files

When you import metadata from a DDM file, the gateway maps the metadata data types as described in Table A-2.

Table A-2 Metadata from DDM Files

| DDM/Natural Data Type | ADD-Adabas Data Type | Oracle Data Type | Details |
| --- | --- | --- | --- |
| `A` | `string` | `VARCHAR2` | A null-terminated string of alphanumeric characters; maximum length must be specified. An extra byte is required for the null flag. |
| `B1` | `Uint1` | `Number(3)` | Unsigned byte integer.  Size: 1 byte  Range: 0 to +254 |
| `B2` | `Uint2` | `Number(5)` | Unsigned word integer.  Size: 2 bytes  Range: 0 to +65535 |
| `B4` | `Uint4` | `Number(10)` | Unsigned long integer.  Size: 4 bytes  Range: 0 to +4,294,967,294 |
| `I1` | `Int1` | `Number(3)` | Signed byte integer.  Size: 1 byte  Signed range: -128 to +127 |
| `I2` | `Int2` | `Number(5)` | Signed word integer.  Size: 2 bytes  Signed range: -32768 to +32767 |
| `I4` | `Int4` | `Number(10)` | Signed long integer.  Size: 4 bytes  Range: -2147483648 to 2147483647 |
| `I8` | `Int8` | `Number(19)` | Signed long integer.  Size: 8 bytes  Range: -9223372036854775808 to +9223372036854775807 |
| `F4` | `single` | `FLOAT(23)` | Single floating-point number (`F_FLOAT`).  Size: 4 bytes  Range: 0.29E-38 to 1.7E38  Precision: 6 digits |
| `F8` | `dfloat` | `Number(5)` | Double floating-point number (`D_FLOAT`)  Size: 8 bytes  Range: 0.29E-38 to 1.7E38  Precision: 16 digits |
| `L` | `Unit1` | `Number(3)` | Unsigned byte integer.  Size: 1 byte  Values: 1 for true, 0 for false |
| `D` | `ada_d_time` | `DATE` | ODBC date format. |
| `T` | `ada_time` | `DATE` | ODBC time format. |
| `P` | `decimal` | `NUMBER` | Packed decimal  Maximum number of digits: 31  Maximum fraction: 11  Length = int (number of digits/2) + 1 byte |
| `N`, `U` | `ada_numstr_s` | `NUMBER` | Signed numeric string  Maximum number of digits: 31  Maximum fractions: 11 |