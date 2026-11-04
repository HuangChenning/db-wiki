---
title: UTL_COLL
book: PL/SQL Packages and Types Reference
doc_id: E96430-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/UTL_COLL.html
tags:
  - oracle
  - 19c
  - pl-sql-packages-and-types-reference
---

`The` `UTL_COLL` package lets PL/SQL programs use collection locators to query and update.

This chapter contains the following topics:

- Summary of UTL\_COLL Subprograms

### Summary of UTL\_COLL Subprograms

The `UTL_COLL` package has one subprogram, the `IS_LOCATOR` function.

Table 1 UTL\_COLL Package Subprograms

| Subprogram | Description |
| --- | --- |
| IS\_LOCATOR Function | Determines whether a collection item is actually a locator or not |

### IS\_LOCATOR Function

This function determines whether a collection item is actually a locator or not.

**Syntax**

```md
UTL_COLL.IS_LOCATOR (
   coln IN STANDARD)
  RETURNS BOOLEAN;
```

**Pragmas**

Asserts `WNDS`, `WNPS` and `RNPS` pragmas

**Parameters**

Table 2 *IS\_LOCATOR Function Parameters*

| Parameter | Description |
| --- | --- |
| `coln` | Nested table or varray item. |

**Return Values**

Table 3 IS\_LOCATOR Function Return Values

| Return Value | Description |
| --- | --- |
| `1` | Collection item is indeed a locator. |
| `0` | Collection item is not a locator. |

**Examples**

```md
CREATE OR REPLACE TYPE list_t as TABLE OF VARCHAR2(20);
/

CREATE OR REPLACE TYPE phone_book_t AS OBJECT (
  pno  number,
  ph   list_t );
/

CREATE TABLE phone_book OF phone_book_t
      NESTED TABLE ph STORE AS nt_ph;
CREATE TABLE phone_book1 OF phone_book_t
      NESTED TABLE ph STORE AS nt_ph_1 RETURN LOCATOR;

INSERT INTO phone_book VALUES(1, list_t('650-633-5707','650-323-0953'));
INSERT INTO phone_book1 VALUES(1, list_t('415-555-1212'));

CREATE OR REPLACE PROCEDURE chk_coll IS
  plist list_t;
  plist1 list_t;
BEGIN
  SELECT ph INTO plist FROM phone_book WHERE pno=1;

  SELECT ph INTO plist1 FROM phone_book1 WHERE pno=1;

  IF (UTL_COLL.IS_LOCATOR(plist)) THEN
    DBMS_OUTPUT.PUT_LINE('plist is a locator');
  ELSE
    DBMS_OUTPUT.PUT_LINE('plist is not a locator');
  END IF;

  IF (UTL_COLL.IS_LOCATOR(plist1)) THEN
    DBMS_OUTPUT.PUT_LINE('plist1 is a locator');
  ELSE
    DBMS_OUTPUT.PUT_LINE('plist1 is not a locator');
  END IF;

END chk_coll;

SET SERVEROUTPUT ON
EXECUTE chk_coll;
```