---
title: JSON Data Structures
book: PL/SQL Packages and Types Reference
doc_id: E96430-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/json-types.html
tags:
  - oracle
  - 19c
  - pl-sql-packages-and-types-reference
---

To work with JSON data in PL/SQL, you can use these data structures.

**Related Topics**

### JSON\_ELEMENT\_T Object Type

`JSON_ELEMENT_T` is the supertype for the `JSON_OBJECT_T`, `JSON_SCALAR_T`, and `JSON_ARRAY_T` object types.

**Description**

Note the following:

- To create an instance of JSON\_ELEMENT\_T, use the `parse` function. See the “Constructors” section below for details.
- You cannot create an empty JSON\_ELEMENT\_T instance. To create an empty JSON container, create it based on one of the subtypes.
- To cast a JSON\_ELEMENT\_T into a subtype (for example, JSON\_OBJECT\_T), you need to perform an explicit cast using TREAT AS. For example:
	```md
	TREAT (elem AS JSON_OBJECT_T)
	```

**Constructors**

You create a JSON\_ELEMENT\_T instance using the `parse` function. The function takes as input VARCHAR2, CLOB, or BLOB data, and returns a JSON\_ELEMENT\_T instance.

```md
STATIC FUNCTION parse(json VARCHAR2) RETURN JSON_ELEMENT_T
STATIC FUNCTION parse(json CLOB)     RETURN JSON_ELEMENT_T
STATIC FUNCTION parse(json BLOB)     RETURN JSON_ELEMENT_T
```

Only UTF8-encoded JSON is passed as a BLOB.

The `parse` function takes a JSON string as input and sets up an internal representation of the JSON data. If the provided input is not valid JSON, then an error message is raised. Valid JSON has to pass the lax check of the “IS JSON” SQL condition.

**Serialization**

Serialization is the inverse of the `parse` function. The serialization operation takes the in-memory representation of the JSON data and prints it to a string. The serialization functions and procedures are:

```md
MEMBER FUNCTION to_String    RETURN VARCHAR2
MEMBER FUNCTION to_Number    RETURN NUMBER
MEMBER FUNCTION to_Date      RETURN DATE
MEMBER FUNCTION to_Timestamp RETURN TIMESTAMP
MEMBER FUNCTION to_Boolean   RETURN BOOLEAN
MEMBER FUNCTION to_Clob      RETURN CLOB
MEMBER FUNCTION to_Blob      RETURN BLOB

MEMBER PROCEDURE to_Clob(c IN OUT CLOB)
MEMBER PROCEDURE to_Blob(c IN OUT BLOB)
```

The `to_Clob` and `to_Blob` *procedures* accept a CLOB or BLOB input and enable you to provide a LOB to be used as the serialization destination. For instance, EMPTY\_LOB can be provided. The input LOB cannot be NULL.

If the `to_Clob` *function* is used, then a new CLOB is created. If you do not want to create a CLOB first, then you can use the `to_Clob` or `to_Blob` *functions*, which take no parameter and generate a temp lob.

`to_Blob` serializes to UTF8 format only.

**Introspection**

Introspection enables you to discover properties of JSON objects without modifying them. The introspection functions are:

```md
MEMBER FUNCTION is_Object    RETURN BOOLEAN
MEMBER FUNCTION is_Array     RETURN BOOLEAN
MEMBER FUNCTION is_Scalar    RETURN BOOLEAN
MEMBER FUNCTION is_String    RETURN BOOLEAN
MEMBER FUNCTION is_Number    RETURN BOOLEAN
MEMBER FUNCTION is_Boolean   RETURN BOOLEAN
MEMBER FUNCTION is_True      RETURN BOOLEAN
MEMBER FUNCTION is_False     RETURN BOOLEAN
MEMBER FUNCTION is_Null      RETURN BOOLEAN
MEMBER FUNCTION is_Date      RETURN BOOLEAN
MEMBER FUNCTION is_Timestamp RETURN BOOLEAN
MEMBER FUNCTION get_Size     RETURN NUMBER
```

The return value of the `get_size` function depends on the JSON type:

- For a scalar, it returns `1`.
- For an object, it returns the number of keys.
- For an array, it returns the number of items.

Note that JSON does not support dates and timestamps natively. Instead they are typically modeled as strings. The DOM API enables you to add dates and timestamps as scalar values and preserve them until serialization to JSON, where they are printed as string following the ISO 8601 format. If a SQL value of type date or timestamp has been added, then the `is_Date` and `is_Timestamp` functions return true. If a date has been added as a string (e.g. as ISO 8601), then the `is_Date` and `is_Timestamp` functions return false. You can use Oracle conversion function `to_Date` and `to_Timestamp` to convert a string representation of a date, and timestamp to the Oracle representation.

**Error Handling**

You can set the level of error handling for JSON processing. You might not want an error to be raised for every mismatch. The `on_Error` procedure enables you to specify when errors should be raised:

```md
MEMBER PROCEDURE on_Error(value NUMBER)
```

The `on_Error` procedure defines what happens if an error is encountered during a PL/SQL operation, for instance, a get call.

The default is to not raise an error but to return NULL instead.

You invoke `On_error` on a JSON\_ELEMENT\_T instance and it sets the error behavior for all subsequent calls. To reset the behavior to the default, you can call `on_Error(0)`.

Values for the `value` parameter are:

Table 1 Values for the value Parameter in the ON\_ERROR Procedure

| Value | Description |
| --- | --- |
| 0 | Reset to the default behavior, which is to return NULL instead of raising an error. |
| 1 | Raise all errors. |
| 2 | Raise an error if no value is detected. |
| 3 | Raise an error if the data types do not match, for example, if you call GET\_NUMBER on a string value. |
| 4 | Raise an error if the input is invalid, for example, if the array is out of bounds. |

You can combine values. For example, you can specify 7 to indicate a combination of 3 and 4.

In the following example, an error is raised because the value of “a” is “xyz”, which cannot be converted to a number. If the `on_Error` procedure had not been called, then NULL would be returned, and no error would be raised.

```md
declare
     jo JSON_OBJECT_T;
begin
     jo := JSON_OBJECT_T.parse('{a:"xyz"}');
     jo.On_error(1);
     dbms_output.put_line(jo.get_Number('a'));
end;
/
```

### JSON\_OBJECT\_T Object Type

`JSON_OBJECT_T` is a subtype of the JSON\_ELEMENT\_T object type. It corresponds to the JSON object structure.

**Constructors**

You can create an empty JSON\_OBJECT\_T instance using the following constructor.

```md
CONSTRUCTOR FUNCTION JSON_OBJECT_T RETURN SELF AS RESULT
```

You can create a JSON\_OBJECT\_T instance using one of the following `parse` functions:

```md
STATIC FUNCTION parse(json VARCHAR2) RETURN JSON_OBJECT_T
STATIC FUNCTION parse(json CLOB)     RETURN JSON_OBJECT_T
STATIC FUNCTION parse(json BLOB)     RETURN JSON_OBJECT_T
```

You can also create a JSON\_OBJECT\_T instance using one of the following constructors:

```md
CONSTRUCTOR FUNCTION JSON_OBJECT_T(jsn VARCHAR2) RETURN SELF AS RESULT,
CONSTRUCTOR FUNCTION JSON_OBJECT_T(jsn CLOB) RETURN SELF AS RESULT,
CONSTRUCTOR FUNCTION JSON_OBJECT_T(jsn BLOB) RETURN SELF AS RESULT,
CONSTRUCTOR FUNCTION JSON_OBJECT_T(e JSON_ELEMENT_T) RETURN SELF AS RESULT
```

Only UTF8-encoded JSON is passed as a BLOB.

The `parse` function takes a JSON string as input and sets up an internal representation of the JSON data. If the provided input is not a valid JSON object, then an error message is raised. The input has to specify a JSON object, not an array.

**Get Functions and Procedures**

The following functions and procedures enable you to retrieve the value of the JSON object:

```md
MEMBER FUNCTION get(key VARCHAR2)           RETURN JSON_ELEMENT_T
MEMBER FUNCTION get_String(key VARCHAR2)    RETURN VARCHAR2
MEMBER FUNCTION get_Number(key VARCHAR2)    RETURN NUMBER
MEMBER FUNCTION get_Date(key VARCHAR2)      RETURN DATE
MEMBER FUNCTION get_Timestamp(key VARCHAR2) RETURN TIMESTAMP
MEMBER FUNCTION get_Boolean(key VARCHAR2)   RETURN BOOLEAN
MEMBER FUNCTION get_Clob(key VARCHAR2)      RETURN CLOB
MEMBER FUNCTION get_Blob(key VARCHAR2)      RETURN BLOB
MEMBER FUNCTION get_Object(key VARCHAR2)    RETURN JSON_OBJECT_T
MEMBER FUNCTION get_Array(key VARCHAR2)     RETURN JSON_ARRAY_T

MEMBER PROCEDURE get_Clob(key NUMBER, c IN OUT CLOB)
MEMBER PROCEDURE get_Blob(key NUMBER, c IN OUT BLOB)
```

Note:

- The `get` function has reference semantics. This means that if the returned JSON\_ELEMENT\_T is modified, then the containing JSON\_ELEMENT\_T is also changed. See the Reference Semantics section below for details.
- The `GET_STRING` function converts the value to a string if it is not already a string. Thus, the `GET_STRING` function returns a non-null value even if IS\_STRING returns false.
- All the “get” functions perform a conversion if possible. If no conversion is possible, then an error might be raised, depending on what `ON_ERROR` is set to.

The `GET_CLOB` and `GET_BLOB` *procedures*, which accept a CLOB or BLOB as input, enable you to provide a LOB to be used as serialization destination. For instance, EMPTY\_LOB can be provided. If you use the `GET_CLOB` *function* instead, then a new CLOB will be created implicitly. The input LOB cannot be NULL. If you do not want to create a BLOB or CLOB first, you can use the GET\_CLOB or GET\_BLOB functions, which take no parameter and generates a temp LOB.

`GET_BLOB` serializes to UTF8 format only.

**Set Procedures**

The following procedures enable you to set the value of a JSON object. Existing values, if present, will be overwritten.

```md
MEMBER PROCEDURE put(key VARCHAR2, val JSON_ELEMENT_T)
MEMBER PROCEDURE put(key VARCHAR2, val VARCHAR2)
MEMBER PROCEDURE put(key VARCHAR2, val NUMBER)
MEMBER PROCEDURE put(key VARCHAR2, val BOOLEAN)
MEMBER PROCEDURE put(key VARCHAR2, val DATE)
MEMBER PROCEDURE put(key VARCHAR2, val TIMESTAMP)
MEMBER PROCEDURE put_Null(key VARCHAR2)
```

**Introspection Functions**

Introspection enables you to discover properties of JSON objects without modifying them. The introspection functions are:

```md
MEMBER FUNCTION has(key VARCHAR2)      RETURN BOOLEAN
MEMBER FUNCTION get_Type(key VARCHAR2) RETURN VARCHAR2
MEMBER FUNCTION get_Keys               RETURN JSON_KEY_LIST
```

The get\_Keys function returns an object type of JSON\_KEY\_LIST, which is a varray of VARCHAR2(4000). The varray contains the names of keys in the JSON object. The get\_Keys function returns at most 32767 field names for a given JSON object. An error is raised if it is applied to an object with more than 32767 fields.

The example below walks through the items of the varray to build a JSON\_ARRAY\_T object that contains all key names.

```md
declare
  jo JSON_OBJECT_T;
  ja JSON_ARRAY_T;
  keys JSON_KEY_LIST;
  keys_string VARCHAR2(100);

begin
  ja := new JSON_ARRAY_T;
  jo := JSON_OBJECT_T.parse('{"name":"fred",
                              "jobTitle":"codemonkey",
                              "projects":["json", "xml"]}');
  keys := jo.get_keys;
  for i in 1..keys.count loop
     ja.append(keys(i));
  end loop;

  keys_string := ja.to_string;
  dbms_output.put_line(keys_string);
end;
/
```

The output is:

```md
["name","jobTitle","projects"]
```

**Modification Procedures**

The following procedures enable you to remove or rename keys in a JSON object.

```md
MEMBER PROCEDURE remove(key VARCHAR2)
MEMBER PROCEDURE rename_Key(keyOld VARCHAR2, keyNew VARCHAR2)
```

Duplicate key names are not supported and will raise an error.

**Clone Function**

This function makes a copy of the JSON object. Reference semantics is changed to value semantics.

```md
MEMBER FUNCTION clone RETURN JSON_OBJECT_T
```

**Reference Semantics**

Calling the `get` function that returns a JSON\_ELEMENT\_T object always returns a reference to the complex values instead of a copy. This means that changing the returned value affects its container. See the example below.

```md
declare
  data    JSON_OBJECT_T;
  address JSON_OBJECT_T;
  zip     number;

begin

  data := new JSON_OBJECT_T('{
    "first": "John",
    "last": "Doe",
    "address": {
        "country": "USA",
        "zip": "94065"
    }
  }');

  address := data.get_object('address');
  dbms_output.put_line(address.to_string);

  -- 1) VALUE SEMANTICS for scalar values
  -- (changing the value has no effect on container)
  zip := address.get_number('zip');
  dbms_output.put_line(zip);
  zip := 12345;
  dbms_output.put_line(zip);
  -- address is still the same
  dbms_output.put_line(address.to_string);

  -- 2) REFERENCE SEMANTICS for complex values
  --    'address' is a reference to the complex address values inside 'data'
  address.put('zip', 12345);
  address.put('street', 'Detour Road');
  dbms_output.put_line(data.to_string);
end;
/
```

In cases where you do not want the reference semantics, you can use the `clone` function to create a copy of the returned object. This decouples the value from its container. In the example above, you can create a copy of the “address” object by replacing this line:

```md
address := data.get_object('address');
```

with this line:

```md
address := data.get_object('address').clone;
```

After this, changing the address with have no effect on the value of the ‘data’ containing object.

**Update Example**

The following example updates the price of an item by 10%.

```md
WITH
  FUNCTION updatePrice(jsonTxt in VARCHAR2 ) RETURN VARCHAR2 IS
  jo JSON_OBJECT_T;
  oldPrice NUMBER;

  BEGIN
    jo := new JSON_OBJECT_T(jsonTxt);
    oldPrice := jo.get_number('price');
    jo.put('price', oldPrice * 1.1);
    RETURN jo.to_string();
  END;
SELECT updatePrice(col)
FROM   t1;
```

### JSON\_ARRAY\_T Object Type

`JSON_ARRAY_T` is a subtype of the `JSON_ELEMENT_T` object type. `JSON_ARRAY_T` corresponds to the JSON array structure.

**Constructors**

You can create an empty JSON\_ARRAY\_T instance using the following constructor.

```md
CONSTRUCTOR FUNCTION JSON_ARRAY_T RETURN SELF AS RESULT
```

You can create a JSON\_ARRAY\_T instance using one the following `parse` functions:

```md
STATIC FUNCTION parse(json VARCHAR2) RETURN JSON_ARRAY_T
STATIC FUNCTION parse(json CLOB)     RETURN JSON_ARRAY_T
STATIC FUNCTION parse(json BLOB)     RETURN JSON_ARRAY_T
```

You can also create a JSON\_ARRAY\_T instance using one the following constructors:

```md
CONSTRUCTOR FUNCTION JSON_Array_T(jsn VARCHAR2) RETURN SELF AS RESULT
CONSTRUCTOR FUNCTION JSON_Array_T(jsn CLOB) RETURN SELF AS RESULT
CONSTRUCTOR FUNCTION JSON_Array_T(jsn BLOB) RETURN SELF AS RESULT
CONSTRUCTOR FUNCTION JSON_Array_T(e JSON_ELEMENT_T) RETURN SELF AS RESULT
```

Only UTF8-encoded JSON is passed as a BLOB.

The `parse` function takes a JSON string as input and sets up an internal representation of the JSON data. If the provided input is not valid JSON, then an error message is raised. The input has to specify a JSON array, not an object.

**Get Functions and Procedures**

The following functions and procedures enable you to retrieve the value of the JSON array:

```md
MEMBER FUNCTION get(pos NUMBER)           RETURN JSON_ELEMENT_T
MEMBER FUNCTION get_String(pos NUMBER)    RETURN VARCHAR2
MEMBER FUNCTION get_Number(pos NUMBER)    RETURN NUMBER
MEMBER FUNCTION get_Date(pos NUMBER)      RETURN DATE
MEMBER FUNCTION get_Timestamp(pos NUMBER) RETURN TIMESTAMP
MEMBER FUNCTION get_Boolean(pos NUMBER)   RETURN BOOLEAN
MEMBER FUNCTION get_Clob(pos NUMBER)      RETURN CLOB
MEMBER FUNCTION get_Blob(pos NUMBER)      RETURN BLOB

MEMBER PROCEDURE get_Clob(pos NUMBER, c IN OUT CLOB)
MEMBER PROCEDURE get_Blob(pos NUMBER, c IN OUT BLOB)
```

Note:

- The `get` function has reference semantics. This means that if the returned JSON\_ELEMENT\_T is modified, then the containing JSON\_ELEMENT\_T is changed too.
- The `GET_STRING` function converts the value to a string if it is not already a string. The function returns a non-null value even if IS\_STRING returns false.
- All the “get” functions perform a conversion if possible. If no conversion is possible, then an error might be raised, depending on what `ON_ERROR` is set to.

The `GET_CLOB` and `GET_BLOB` *procedures*, which accept a CLOB or BLOB as input, enable you to provide a LOB to be used as serialization destination. For instance, EMPTY\_LOB can be provided. If you use the `GET_CLOB` *function* instead, then a new CLOB will be created implicitly. The input LOB cannot be NULL. If you do not want to create a BLOB or CLOB first, you can use the GET\_CLOB or GET\_BLOB functions, which take no parameter and generates a temp LOB.

`GET_BLOB` serializes to UTF8 format only.

**Set Procedures**

The following procedures enable you to set the value at the specified position in the JSON array. These procedures insert (not overwrite) at the specified position unless overwrite is requested.

```md
MEMBER PROCEDURE put(pos NUMBER, value VARCHAR2, overwrite BOOLEAN DEFAULT FALSE)
MEMBER PROCEDURE put(pos NUMBER, value NUMBER, overwrite BOOLEAN DEFAULT FALSE)
MEMBER PROCEDURE put(pos NUMBER, value BOOLEAN, overwrite BOOLEAN DEFAULT FALSE)
MEMBER PROCEDURE put(pos NUMBER, value JSON_ELEMENT_T, overwrite BOOLEAN DEFAULT FALSE)
MEMBER PROCEDURE put(pos NUMBER, value DATE, overwrite BOOLEAN DEFAULT FALSE)
MEMBER PROCEDURE put(pos NUMBER, value TIMESTAMP, overwrite BOOLEAN DEFAULT FALSE)
MEMBER PROCEDURE put_Null(pos NUMBER, overwrite BOOLEAN DEFAULT FALSE)
```

The following procedures append the specified value to the end of the JSON array:

```md
MEMBER PROCEDURE append(value JSON_ELEMENT_T)
MEMBER PROCEDURE append(value VARCHAR2)
MEMBER PROCEDURE append(value NUMBER)
MEMBER PROCEDURE append(value BOOLEAN)
MEMBER PROCEDURE append(value DATE)
MEMBER PROCEDURE append(value TIMESTAMP)
MEMBER PROCEDURE append_Null
```

**Introspection Function**

Introspection enables you to discover properties of the JSON array without modifying them.

```md
MEMBER FUNCTION get_Type(pos NUMBER) RETURN VARCHAR2
```

**Modification Procedure**

The following procedure enables you to remove the value at the specified position in the JSON array.

```md
MEMBER PROCEDURE remove(pos NUMBER)
```

**Clone Function**

This function makes a copy of the JSON array. Reference semantics is changed to value semantics.

```md
MEMBER FUNCTION clone RETURN JSON_ARRAY_T
```

### JSON\_SCALAR\_T Object Type

`JSON_SCALAR_T` is a subtype of the `JSON_ELEMENT_T` object type.

**Description**

A `JSON_SCALAR_T` instance captures one scalar values, for example, the string “fred” or the number 1. This type does not have any functions or procedures other than the ones inherited from `JSON_ELEMENT_T.` You cannot create an instance of this type directly.

### JSON\_KEY\_LIST Type

`JSON_KEY_LIST` is a varray of `VARCHAR2(4000)`.

**Description**

This type is used by the `get_Keys` function in the JSON\_OBJECT\_T Object Type.