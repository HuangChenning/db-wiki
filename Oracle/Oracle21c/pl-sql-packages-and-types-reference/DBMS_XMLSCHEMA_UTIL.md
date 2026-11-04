---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/DBMS_XMLSCHEMA_UTIL.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 216 DBMS\_XMLSCHEMA\_UTIL

The `DBMS_XMLSCHEMA_UTIL` package provides an interface for XML schema validation.

This chapter contains the following topics:

- DBMS\_XMLSCHEMA\_UTIL Security Model
- Summary of DBMS\_XMLSCHEMA\_UTIL Subprograms

See Also:

- [Oracle XML DB Developer's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADXDB-GUID-B8507F44-B010-4384-94E6-101131DD7D88)

### 216.1 DBMS\_XMLSCHEMA\_UTIL Security Model

Applications must have the `EXECUTE` privilege on the `DBMS_XMLSCHEMA_UTIL` package

### 216.2 Summary of DBMS\_XMLSCHEMA\_UTIL Subprograms

This topic lists the `DBMS_XMLSCHEMA_UTIL` subprograms in alphabetical order and briefly describes them.

Table 216-1 DBMS\_XMLSCHEMA\_UTIL Package Subprograms

| Subprogram | Description |
| --- | --- |
| CONFORMING Function | Validates an XML document against a schema |
| VALIDATE Procedure | Validates an XML document against a schema |

#### 216.2.1 CONFORMING Function

This function is used to validate an XML document against a schema.

Syntax

```
DBMS_XMLSCHEMA_UTIL.CONFORMING (
   doc             IN NUMBER,
   sch             IN NUMBER)
RETURN NUMBER;
```

Parameters

Table 216-2 CONFORMING Function Parameters

| Parameter | Description |
| --- | --- |
| `doc` | The XML instance |
| `sch` | The XML schema |

Function Exceptions

The exceptions of `DBMS_XMLSCHEMA_UTIL.CONFORMING` function are as follows:

- The function returns zero if the schema is legal and the document conforms to the schema; otherwise it returns an LSX error code from the schema validation.

Note:

The function takes an xml data instance and xml schema instance. The user does not have to register the schema.

Example: The document conforms to the schema

```
SELECT DBMS_XMLSCHEMA_UTIL.CONFORMING(
     XMLType('<A/>'),
     XMLType(
    '<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
      <xs:element name="A" type="xs:string"/>
     </xs:schema>')) "LSX CODE"
    FROM DUAL;
```

#### 216.2.2 VALIDATE Procedure

This procedure is used to validate an XML document against a schema.

Syntax

```
DBMS_XMLSCHEMA_UTIL.VALIDATE (
   doc             IN XMLTYPE,
   sch             IN XMLTYPE);
```

Parameters

Table 216-3 VALIDATE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `doc` | The XML instance |
| `sch` | The XML schema |

Procedure Exceptions

The exceptions of `DBMS_XMLSCHEMA_UTIL.VALIDATE` procedure are as follows:

- The procedure raises ORA-31154 if either the schema is not legal, or the document does not conform to the schema.

Note:

The procedure takes an xml data instance and xml schema instance. The user does not have to register the schema.

Example: The document conforms to the schema

```
BEGIN
      DBMS_XMLSCHEMA_UTIL.VALIDATE(
         XMLType('<A/>'),
         XMLType(
                 '<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
                  <xs:element name="A" type="xs:string"/>
                  </xs:schema>'));
END;
/
```