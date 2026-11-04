---
title: DBMS_DEVELOPER
book: PL/SQL Packages and Types Reference
doc_id: E96430-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/dbms_developer1.html
tags:
  - oracle
  - 19c
  - pl-sql-packages-and-types-reference
---

The package `DBMS_DEVELOPER` provides simple and developer friendly methods to retrieve information about database objects.

This chapter contains the following topics:

- DBMS\_DEVELOPER Overview
- Summary of DBMS\_DEVELOPER Subprograms

### DBMS\_DEVELOPER Overview

The package `DBMS_DEVELOPER` provides subprograms to retrieve information about database objects.

The `DBMS_DEVELOPER` package provides simple methods to retrieve relevant information about the database objects. This package is useful for developer tools and developers who would like to get information about the objects in the database, their shape, their structure, etc.

In terms of performance, the `DBMS_DEVELOPER` package retrieves information within few milliseconds.

### DBMS\_DEVELOPER Security

This section lists the security restrictions related to `DBMS_DEVELOPER` package.

The function is executed with invoker rights. You will be allowed to access metadata for a database object ONLY if you are authorized to do a “describe” on the object. If a you do not have such authorization, an error will be raised and no metadata will be retrieved.

Here’s a summary of privileges required:

- **Tables and Views**: You need **SELECT** or **READ** privileges on the table or view.
- **Indexes**: You need **SELECT** or **READ** privileges on the table on which the index is defined.
- **Synonyms**: You need **SELECT** or **READ** privileges on the synonym as well as the underlying object.

If you’re describing objects in your own schema, no additional privilege is needed. However, if you’re describing objects in another schema, you’ll need at least the **SELECT** privilege on those objects.

If you are a DBA or have the **SELECT ANY TABLE**, **READ ANY TABLE**, and **SELECT ANY VIEW** system privilege, you can call `DBMS_DEVELOPER.GET_METADATA` on any table, index, or view in the database without needing explicit grants.

### Summary of DBMS\_DEVELOPER Subprograms

The table lists the `DBMS_DEVELOPER` subprograms and briefly describes them.

The following table specifies the subprograms for `DBMS_DEVELOPER` package and its brief description.

|  |  |
| --- | --- |
| **Subprogram** | **Description** |
| `GET_METADATA` | The function takes information about the object including: `name`,`object_type`,`schema`,`etag` and produces the corresponding metadata in CLOB containing JSON-formatted text output. The level of information that needs to be produced in the output can be specified in the input parameter - `level`. |

### GET\_METADATA Function

This section describes the syntax, input and output formats of the `GET_METADATA` function.

This function takes information about the object and produces the corresponding metadata as a CLOB containing JSON-formatted text output.

**Syntax**

```md
DBMS_DEVELOPER.GET_METADATA (
name            IN VARCHAR2,
schema          IN VARCHAR2 DEFAULT NULL,
object_type     IN VARCHAR2 DEFAULT NULL,
level           IN VARCHAR2 DEFAULT 'TYPICAL'
etag            IN RAW      DEFAULT NULL)
RETURN CLOB;
```

Table 1 Input Configuration Fields

| Field | Value |
| --- | --- |
| `name` | The object name. A synonym of the object name can also be provided. It is case sensitive and should be provided as it appears in the data dictionary. |
| `schema` | The schema name. The default is the current user. It is case sensitive and should be provided as it appears in the data dictionary. |
| `object_type` | The type of object that you want to be retrieved. This is optional as name resolution can also be done without specifying `object_type.`  Supported values: `TABLE`, `INDEX`, and `VIEW` |
| `level` | The level of detail. The default is `TYPICAL`.  Supported values:  1. `BASIC`: Describes essential information. 2. `TYPICAL`: Includes more information of specified objects. 3. `ALL`: Provides the most comprehensive level of information. |
| `etag` | A unique identifier for a specific version of the document. This `etag` value lets an application determine whether the content of a particular version of a document is the same as that of another version.  1. If an `etag` is provided and it matches with current `etag`, the function returns an empty document. 2. If the `etag` of the document in the database does not match the `etag` that was provided, a new document is returned (along with the new embedded `etag`). |

`GET_METADATA` function will not return a JSON schema, instead, it will return a JSON document. Depending on the level of metadata you would like to retrieve, you can use the appropriate parameters for `GET_METADATA` function to obtain the desired metadata JSON document.

Refer to JSON Schema for Different Object and Sub-Object Types to understand which schema you would need for your application.

**Examples**

This section provides example usage for `DBMS_DEVELOPER.GET_METADATA` for different values of `object_type` and `level`. 1. Retrieving metadata for `level` set to `BASIC` and for `object_type` set to `TABLE`:

```md
<pre class="copy"><code>SQL&gt; conn hr/hr Connected. SQL&gt; SELECT JSON_SERIALIZE(dbms_developer.get_metadata(name =&gt; &#39;EMPLOYEES&#39;, level =&gt; &#39;BASIC&#39;)RETURNING CLOB PRETTY) from dual;</code></pre>

Executing this query would produce the following:

<pre class="copy"><code>{   &quot;objectType&quot; : &quot;TABLE&quot;,   &quot;objectInfo&quot; :   {     &quot;name&quot; : &quot;EMPLOYEES&quot;,     &quot;schema&quot; : &quot;HR&quot;,     &quot;columns&quot; :     [       {         &quot;name&quot; : &quot;EMPLOYEE_ID&quot;,         &quot;notNull&quot; : true,         &quot;dataType&quot; :         {           &quot;type&quot; : &quot;NUMBER&quot;,           &quot;precision&quot; : 6         }       },       {         &quot;name&quot; : &quot;FIRST_NAME&quot;,         &quot;notNull&quot; : false,         &quot;dataType&quot; :         {           &quot;type&quot; : &quot;VARCHAR2&quot;,           &quot;length&quot; : 20,           &quot;sizeUnits&quot; : &quot;BYTE&quot;         }       },       {         &quot;name&quot; : &quot;LAST_NAME&quot;,         &quot;notNull&quot; : true,         &quot;dataType&quot; :         {           &quot;type&quot; : &quot;VARCHAR2&quot;,           &quot;length&quot; : 25,           &quot;sizeUnits&quot; : &quot;BYTE&quot;         }       },       {         &quot;name&quot; : &quot;EMAIL&quot;,         &quot;notNull&quot; : true,         &quot;dataType&quot; :         {           &quot;type&quot; : &quot;VARCHAR2&quot;,           &quot;length&quot; : 25,           &quot;sizeUnits&quot; : &quot;BYTE&quot;         }       },       {         &quot;name&quot; : &quot;PHONE_NUMBER&quot;,         &quot;notNull&quot; : false,         &quot;dataType&quot; :         {           &quot;type&quot; : &quot;VARCHAR2&quot;,           &quot;length&quot; : 20,           &quot;sizeUnits&quot; : &quot;BYTE&quot;         }       },       {         &quot;name&quot; : &quot;HIRE_DATE&quot;,         &quot;notNull&quot; : true,         &quot;dataType&quot; :         {           &quot;type&quot; : &quot;DATE&quot;         }       },       {         &quot;name&quot; : &quot;JOB_ID&quot;,         &quot;notNull&quot; : true,         &quot;dataType&quot; :         {           &quot;type&quot; : &quot;VARCHAR2&quot;,           &quot;length&quot; : 10,           &quot;sizeUnits&quot; : &quot;BYTE&quot;         }       },       {         &quot;name&quot; : &quot;SALARY&quot;,         &quot;notNull&quot; : false,         &quot;dataType&quot; :         {           &quot;type&quot; : &quot;NUMBER&quot;,           &quot;precision&quot; : 8,           &quot;scale&quot; : 2         }       },       {         &quot;name&quot; : &quot;COMMISSION_PCT&quot;,         &quot;notNull&quot; : false,         &quot;dataType&quot; :         {           &quot;type&quot; : &quot;NUMBER&quot;,           &quot;precision&quot; : 2,           &quot;scale&quot; : 2         }       },       {         &quot;name&quot; : &quot;MANAGER_ID&quot;,         &quot;notNull&quot; : false,         &quot;dataType&quot; :         {           &quot;type&quot; : &quot;NUMBER&quot;,           &quot;precision&quot; : 6         }       },       {         &quot;name&quot; : &quot;DEPARTMENT_ID&quot;,         &quot;notNull&quot; : false,         &quot;dataType&quot; :         {           &quot;type&quot; : &quot;NUMBER&quot;,           &quot;precision&quot; : 4         }       }     ]   },   &quot;etag&quot; : &quot;C2BAA871FC47AF364A441F1DCBDBB9D8&quot; }</code></pre>
```
1. Retrieving metadata for `level` set to `TYPICAL` and for `object_type` set to `VIEW`:
	```md
	SQL> conn hr/hr
	Connected.
	SQL> SELECT JSON_SERIALIZE(dbms_developer.get_metadata(name => 'EMP_DETAILS_VIEW',
	level => 'TYPICAL')RETURNING CLOB PRETTY) from dual;
	```
	Executing this query would produce the following:
	```md
	{
	  "objectType" : "VIEW",
	  "objectInfo" :
	  {
	    "name" : "EMP_DETAILS_VIEW",
	    "schema" : "HR",
	    "columns" :
	    [
	      {
	        "name" : "EMPLOYEE_ID",
	        "notNull" : true,
	        "dataType" :
	        {
	          "type" : "NUMBER",
	          "precision" : 6
	        }
	      },
	      {
	        "name" : "JOB_ID",
	        "notNull" : true,
	        "dataType" :
	        {
	          "type" : "VARCHAR2",
	          "length" : 10,
	          "sizeUnits" : "BYTE"
	        }
	      },
	      {
	        "name" : "MANAGER_ID",
	        "notNull" : false,
	        "dataType" :
	        {
	          "type" : "NUMBER",
	          "precision" : 6
	        }
	      },
	      {
	        "name" : "DEPARTMENT_ID",
	        "notNull" : false,
	        "dataType" :
	        {
	          "type" : "NUMBER",
	          "precision" : 4
	        }
	      },
	      {
	        "name" : "LOCATION_ID",
	        "notNull" : false,
	        "dataType" :
	        {
	          "type" : "NUMBER",
	          "precision" : 4
	        }
	      },
	      {
	        "name" : "COUNTRY_ID",
	        "notNull" : false,
	        "dataType" :
	        {
	          "type" : "CHAR",
	          "length" : 2,
	          "sizeUnits" : "BYTE"
	        }
	      },
	      {
	        "name" : "FIRST_NAME",
	        "notNull" : false,
	        "dataType" :
	        {
	          "type" : "VARCHAR2",
	          "length" : 20,
	          "sizeUnits" : "BYTE"
	        }
	      },
	      {
	        "name" : "LAST_NAME",
	        "notNull" : true,
	        "dataType" :
	        {
	          "type" : "VARCHAR2",
	          "length" : 25,
	          "sizeUnits" : "BYTE"
	        }
	      },
	      {
	        "name" : "SALARY",
	        "notNull" : false,
	        "dataType" :
	        {
	          "type" : "NUMBER",
	          "precision" : 8,
	          "scale" : 2
	        }
	      },
	      {
	        "name" : "COMMISSION_PCT",
	        "notNull" : false,
	        "dataType" :
	        {
	          "type" : "NUMBER",
	          "precision" : 2,
	          "scale" : 2
	        }
	      },
	      {
	        "name" : "DEPARTMENT_NAME",
	        "notNull" : true,
	        "dataType" :
	        {
	          "type" : "VARCHAR2",
	          "length" : 30,
	          "sizeUnits" : "BYTE"
	        }
	      },
	      {
	        "name" : "JOB_TITLE",
	        "notNull" : true,
	        "dataType" :
	        {
	          "type" : "VARCHAR2",
	          "length" : 35,
	          "sizeUnits" : "BYTE"
	        }
	      },
	      {
	        "name" : "CITY",
	        "notNull" : true,
	        "dataType" :
	        {
	          "type" : "VARCHAR2",
	          "length" : 30,
	          "sizeUnits" : "BYTE"
	        }
	      },
	      {
	        "name" : "STATE_PROVINCE",
	        "notNull" : false,
	        "dataType" :
	        {
	          "type" : "VARCHAR2",
	          "length" : 25,
	          "sizeUnits" : "BYTE"
	        }
	      },
	      {
	        "name" : "COUNTRY_NAME",
	        "notNull" : false,
	        "dataType" :
	        {
	          "type" : "VARCHAR2",
	          "length" : 40,
	          "sizeUnits" : "BYTE"
	        }
	      },
	      {
	        "name" : "REGION_NAME",
	        "notNull" : false,
	        "dataType" :
	        {
	          "type" : "VARCHAR2",
	          "length" : 25,
	          "sizeUnits" : "BYTE"
	        }
	      }
	    ],
	    "readOnly" : true,
	    "constraints" :
	    [
	      {
	        "name" : "SYS_C007578",
	        "constraintType" : "VIEW READONLY",
	        "status" : "ENABLED",
	        "deferrable" : false,
	        "validated" : "NOT VALIDATED",
	        "sysGeneratedName" : true
	      }
	    ]
	  },
	  "etag" : "C08C2ECBBE343A51060D8C475E16968E"
	}
	```
2. Retrieving metadata for `level` set to `ALL` and for `object_type` set to `VIEW`:
	```md
	SQL> conn hr/hr
	Connected.
	SQL> SELECT JSON_SERIALIZE(dbms_developer.get_metadata(name => 'EMP_DETAILS_VIEW',
	level => 'ALL')RETURNING CLOB PRETTY) from dual;
	```
	Executing this query would produce the following:
	```md
	{
	  "objectType" : "VIEW",
	  "objectInfo" :
	  {
	    "name" : "EMP_DETAILS_VIEW",
	    "schema" : "HR",
	    "columns" :
	    [
	      {
	        "name" : "EMPLOYEE_ID",
	        "notNull" : true,
	        "dataType" :
	        {
	          "type" : "NUMBER",
	          "precision" : 6
	        }
	      },
	      {
	        "name" : "JOB_ID",
	        "notNull" : true,
	        "dataType" :
	        {
	          "type" : "VARCHAR2",
	          "length" : 10,
	          "sizeUnits" : "BYTE"
	        }
	      },
	      {
	        "name" : "MANAGER_ID",
	        "notNull" : false,
	        "dataType" :
	        {
	          "type" : "NUMBER",
	          "precision" : 6
	        }
	      },
	      {
	        "name" : "DEPARTMENT_ID",
	        "notNull" : false,
	        "dataType" :
	        {
	          "type" : "NUMBER",
	          "precision" : 4
	        }
	      },
	      {
	        "name" : "LOCATION_ID",
	        "notNull" : false,
	        "dataType" :
	        {
	          "type" : "NUMBER",
	          "precision" : 4
	        }
	      },
	      {
	        "name" : "COUNTRY_ID",
	        "notNull" : false,
	        "dataType" :
	        {
	          "type" : "CHAR",
	          "length" : 2,
	          "sizeUnits" : "BYTE"
	        }
	      },
	      {
	        "name" : "FIRST_NAME",
	        "notNull" : false,
	        "dataType" :
	        {
	          "type" : "VARCHAR2",
	          "length" : 20,
	          "sizeUnits" : "BYTE"
	        }
	      },
	      {
	        "name" : "LAST_NAME",
	        "notNull" : true,
	        "dataType" :
	        {
	          "type" : "VARCHAR2",
	          "length" : 25,
	          "sizeUnits" : "BYTE"
	        }
	      },
	      {
	        "name" : "SALARY",
	        "notNull" : false,
	        "dataType" :
	        {
	          "type" : "NUMBER",
	          "precision" : 8,
	          "scale" : 2
	        }
	      },
	      {
	        "name" : "COMMISSION_PCT",
	        "notNull" : false,
	        "dataType" :
	        {
	          "type" : "NUMBER",
	          "precision" : 2,
	          "scale" : 2
	        }
	      },
	      {
	        "name" : "DEPARTMENT_NAME",
	        "notNull" : true,
	        "dataType" :
	        {
	          "type" : "VARCHAR2",
	          "length" : 30,
	          "sizeUnits" : "BYTE"
	        }
	      },
	      {
	        "name" : "JOB_TITLE",
	        "notNull" : true,
	        "dataType" :
	        {
	          "type" : "VARCHAR2",
	          "length" : 35,
	          "sizeUnits" : "BYTE"
	        }
	      },
	      {
	        "name" : "CITY",
	        "notNull" : true,
	        "dataType" :
	        {
	          "type" : "VARCHAR2",
	          "length" : 30,
	          "sizeUnits" : "BYTE"
	        }
	      },
	      {
	        "name" : "STATE_PROVINCE",
	        "notNull" : false,
	        "dataType" :
	        {
	          "type" : "VARCHAR2",
	          "length" : 25,
	          "sizeUnits" : "BYTE"
	        }
	      },
	      {
	        "name" : "COUNTRY_NAME",
	        "notNull" : false,
	        "dataType" :
	        {
	          "type" : "VARCHAR2",
	          "length" : 40,
	          "sizeUnits" : "BYTE"
	        }
	      },
	      {
	        "name" : "REGION_NAME",
	        "notNull" : false,
	        "dataType" :
	        {
	          "type" : "VARCHAR2",
	          "length" : 25,
	          "sizeUnits" : "BYTE"
	        }
	      }
	    ],
	    "readOnly" : true,
	    "constraints" :
	    [
	      {
	        "name" : "SYS_C007578",
	        "constraintType" : "VIEW READONLY",
	        "status" : "ENABLED",
	        "deferrable" : false,
	        "validated" : "NOT VALIDATED",
	        "sysGeneratedName" : true
	      }
	    ],
	    "editioningView" : false
	  },
	  "etag" : "ED648644C063A29B04E2A65CFC2D2E76"
	}
	```
3. Retrieving metadata for `level` set to `ALL` and for `object_type` set to `INDEX`:
	```md
	SQL> conn hr/hr
	Connected.
	SQL> SELECT JSON_SERIALIZE(dbms_developer.get_metadata(name => 'EMP_EMP_ID_PK',
	level => 'ALL')RETURNING CLOB PRETTY) from dual;
	```
	Executing this query would produce the following:
	```md
	{
	  "objectType" : "INDEX",
	  "objectInfo" :
	  {
	    "name" : "EMP_EMP_ID_PK",
	    "indexType" : "NORMAL",
	    "owner" : "HR",
	    "tableName" : "EMPLOYEES",
	    "status" : "VALID",
	    "columns" :
	    [
	      {
	        "name" : "EMPLOYEE_ID",
	        "notNull" : true,
	        "dataType" :
	        {
	          "type" : "NUMBER",
	          "precision" : 6
	        },
	        "isPk" : true,
	        "isUk" : true,
	        "isFk" : false,
	        "numDistinct" : 107,
	        "density" : 0.00934579439252336,
	        "avgColLen" : 4,
	        "lowValue" : "C202",
	        "highValue" : "C20307",
	        "hiddenColumn" : false
	      }
	    ],
	    "uniqueness" : "UNIQUE",
	    "lastAnalyzed" : "2025-05-09T06:44:31",
	    "numRows" : 107,
	    "sampleSize" : 107,
	    "partitioned" : false,
	    "distinctKeys" : 107,
	    "compression" : "DISABLED",
	    "segmentCreated" : "YES",
	    "visibility" : "VISIBLE",
	    "toBeDropped" : false
	  },
	  "etag" : "752F0B7990BD188863BBBB80D5248F35"
	}
	```
4. Retrieving metadata where `level` and `object_type` are not explicitly specified:
	```md
	SQL> conn hr/hr
	Connected.
	SQL>
	SQL> SELECT JSON_SERIALIZE(dbms_developer.get_metadata(name => 'EMPLOYEES')
	RETURNING CLOB PRETTY) from dual;
	```
	Even though the `object_type` is not specified, the name resolution happens under the hood. The name `object_type` corresponding to the `name => 'EMPLOYEES'` is determined to be `table`. So the JSON document is produced at the default `typical level` for the `table object_type`. The output JSON document corresponding to the above example is shown here:
	```md
	{
	  "objectType" : "TABLE",
	  "objectInfo" :
	  {
	    "name" : "EMPLOYEES",
	    "schema" : "HR",
	    "columns" :
	    [
	      {
	        "name" : "EMPLOYEE_ID",
	        "notNull" : true,
	        "dataType" :
	        {
	          "type" : "NUMBER",
	          "precision" : 6
	        },
	        "isPk" : true,
	        "isUk" : true,
	        "isFk" : false
	      },
	      {
	        "name" : "FIRST_NAME",
	        "notNull" : false,
	        "dataType" :
	        {
	          "type" : "VARCHAR2",
	          "length" : 20,
	          "sizeUnits" : "BYTE"
	        },
	        "isPk" : false,
	        "isUk" : false,
	        "isFk" : false
	      },
	      {
	        "name" : "LAST_NAME",
	        "notNull" : true,
	        "dataType" :
	        {
	          "type" : "VARCHAR2",
	          "length" : 25,
	          "sizeUnits" : "BYTE"
	        },
	        "isPk" : false,
	        "isUk" : false,
	        "isFk" : false
	      },
	      {
	        "name" : "EMAIL",
	        "notNull" : true,
	        "dataType" :
	        {
	          "type" : "VARCHAR2",
	          "length" : 25,
	          "sizeUnits" : "BYTE"
	        },
	        "isPk" : false,
	        "isUk" : true,
	        "isFk" : false
	      },
	      {
	        "name" : "PHONE_NUMBER",
	        "notNull" : false,
	        "dataType" :
	        {
	          "type" : "VARCHAR2",
	          "length" : 20,
	          "sizeUnits" : "BYTE"
	        },
	        "isPk" : false,
	        "isUk" : false,
	        "isFk" : false
	      },
	      {
	        "name" : "HIRE_DATE",
	        "notNull" : true,
	        "dataType" :
	        {
	          "type" : "DATE"
	        },
	        "isPk" : false,
	        "isUk" : false,
	        "isFk" : false
	      },
	      {
	        "name" : "JOB_ID",
	        "notNull" : true,
	        "dataType" :
	        {
	          "type" : "VARCHAR2",
	          "length" : 10,
	          "sizeUnits" : "BYTE"
	        },
	        "isPk" : false,
	        "isUk" : false,
	        "isFk" : true
	      },
	      {
	        "name" : "SALARY",
	        "notNull" : false,
	        "dataType" :
	        {
	          "type" : "NUMBER",
	          "precision" : 8,
	          "scale" : 2
	        },
	        "isPk" : false,
	        "isUk" : false,
	        "isFk" : false
	      },
	      {
	        "name" : "COMMISSION_PCT",
	        "notNull" : false,
	        "dataType" :
	        {
	          "type" : "NUMBER",
	          "precision" : 2,
	          "scale" : 2
	        },
	        "isPk" : false,
	        "isUk" : false,
	        "isFk" : false
	      },
	      {
	        "name" : "MANAGER_ID",
	        "notNull" : false,
	        "dataType" :
	        {
	          "type" : "NUMBER",
	          "precision" : 6
	        },
	        "isPk" : false,
	        "isUk" : false,
	        "isFk" : true
	      },
	      {
	        "name" : "DEPARTMENT_ID",
	        "notNull" : false,
	        "dataType" :
	        {
	          "type" : "NUMBER",
	          "precision" : 4
	        },
	        "isPk" : false,
	        "isUk" : false,
	        "isFk" : true
	      }
	    ],
	    "lastAnalyzed" : "2025-05-09T06:44:29",
	    "numRows" : 107,
	    "sampleSize" : 107,
	    "avgRowLen" : 69,
	    "external" : "NO",
	    "temporary" : "NO",
	    "indexes" :
	    [
	      {
	        "name" : "EMP_EMAIL_UK",
	        "indexType" : "NORMAL",
	        "uniqueness" : "UNIQUE",
	        "status" : "VALID",
	        "lastAnalyzed" : "2025-05-09T06:44:30",
	        "numRows" : 107,
	        "sampleSize" : 107,
	        "partitioned" : false,
	        "columns" :
	        [
	          {
	            "name" : "EMAIL"
	          }
	        ]
	      },
	      {
	        "name" : "EMP_EMP_ID_PK",
	        "indexType" : "NORMAL",
	        "uniqueness" : "UNIQUE",
	        "status" : "VALID",
	        "lastAnalyzed" : "2025-05-09T06:44:31",
	        "numRows" : 107,
	        "sampleSize" : 107,
	        "partitioned" : false,
	        "columns" :
	        [
	          {
	            "name" : "EMPLOYEE_ID"
	          }
	        ]
	      },
	      {
	        "name" : "EMP_DEPARTMENT_IX",
	        "indexType" : "NORMAL",
	        "uniqueness" : "NONUNIQUE",
	        "status" : "VALID",
	        "lastAnalyzed" : "2025-05-09T06:44:31",
	        "numRows" : 106,
	        "sampleSize" : 106,
	        "partitioned" : false,
	        "columns" :
	        [
	          {
	            "name" : "DEPARTMENT_ID"
	          }
	        ]
	      },
	      {
	        "name" : "EMP_JOB_IX",
	        "indexType" : "NORMAL",
	        "uniqueness" : "NONUNIQUE",
	        "status" : "VALID",
	        "lastAnalyzed" : "2025-05-09T06:44:32",
	        "numRows" : 107,
	        "sampleSize" : 107,
	        "partitioned" : false,
	        "columns" :
	        [
	          {
	            "name" : "JOB_ID"
	          }
	        ]
	      },
	      {
	        "name" : "EMP_MANAGER_IX",
	        "indexType" : "NORMAL",
	        "uniqueness" : "NONUNIQUE",
	        "status" : "VALID",
	        "lastAnalyzed" : "2025-05-09T06:44:32",
	        "numRows" : 106,
	        "sampleSize" : 106,
	        "partitioned" : false,
	        "columns" :
	        [
	          {
	            "name" : "MANAGER_ID"
	          }
	        ]
	      },
	      {
	        "name" : "EMP_NAME_IX",
	        "indexType" : "NORMAL",
	        "uniqueness" : "NONUNIQUE",
	        "status" : "VALID",
	        "lastAnalyzed" : "2025-05-09T06:44:32",
	        "numRows" : 107,
	        "sampleSize" : 107,
	        "partitioned" : false,
	        "columns" :
	        [
	          {
	            "name" : "LAST_NAME"
	          },
	          {
	            "name" : "FIRST_NAME"
	          }
	        ]
	      }
	    ],
	    "constraints" :
	    [
	      {
	        "name" : "EMP_LAST_NAME_NN",
	        "constraintType" : "CHECK - NOT NULL",
	        "searchCondition" : ""LAST_NAME" IS NOT NULL",
	        "columns" :
	        [
	          {
	            "name" : "LAST_NAME"
	          }
	        ],
	        "status" : "ENABLED",
	        "deferrable" : false,
	        "validated" : "VALIDATED",
	        "sysGeneratedName" : false
	      },
	      {
	        "name" : "EMP_EMAIL_NN",
	        "constraintType" : "CHECK - NOT NULL",
	        "searchCondition" : ""EMAIL" IS NOT NULL",
	        "columns" :
	        [
	          {
	            "name" : "EMAIL"
	          }
	        ],
	        "status" : "ENABLED",
	        "deferrable" : false,
	        "validated" : "VALIDATED",
	        "sysGeneratedName" : false
	      },
	      {
	        "name" : "EMP_HIRE_DATE_NN",
	        "constraintType" : "CHECK - NOT NULL",
	        "searchCondition" : ""HIRE_DATE" IS NOT NULL",
	        "columns" :
	        [
	          {
	            "name" : "HIRE_DATE"
	          }
	        ],
	        "status" : "ENABLED",
	        "deferrable" : false,
	        "validated" : "VALIDATED",
	        "sysGeneratedName" : false
	      },
	      {
	        "name" : "EMP_JOB_NN",
	        "constraintType" : "CHECK - NOT NULL",
	        "searchCondition" : ""JOB_ID" IS NOT NULL",
	        "columns" :
	        [
	          {
	            "name" : "JOB_ID"
	          }
	        ],
	        "status" : "ENABLED",
	        "deferrable" : false,
	        "validated" : "VALIDATED",
	        "sysGeneratedName" : false
	      },
	      {
	        "name" : "EMP_SALARY_MIN",
	        "constraintType" : "CHECK",
	        "searchCondition" : "salary > 0",
	        "columns" :
	        [
	          {
	            "name" : "SALARY"
	          }
	        ],
	        "status" : "ENABLED",
	        "deferrable" : false,
	        "validated" : "VALIDATED",
	        "sysGeneratedName" : false
	      },
	      {
	        "name" : "EMP_EMAIL_UK",
	        "constraintType" : "UNIQUE",
	        "columns" :
	        [
	          {
	            "name" : "EMAIL"
	          }
	        ],
	        "status" : "ENABLED",
	        "deferrable" : false,
	        "validated" : "VALIDATED",
	        "sysGeneratedName" : false
	      },
	      {
	        "name" : "EMP_EMP_ID_PK",
	        "constraintType" : "PRIMARY KEY",
	        "columns" :
	        [
	          {
	            "name" : "EMPLOYEE_ID"
	          }
	        ],
	        "status" : "ENABLED",
	        "deferrable" : false,
	        "validated" : "VALIDATED",
	        "sysGeneratedName" : false
	      },
	      {
	        "name" : "EMP_DEPT_FK",
	        "constraintType" : "REFERENTIAL INTEGRITY",
	        "columns" :
	        [
	          {
	            "name" : "DEPARTMENT_ID"
	          }
	        ],
	        "status" : "ENABLED",
	        "deferrable" : false,
	        "validated" : "VALIDATED",
	        "sysGeneratedName" : false,
	        "referencedConstraintName" : "DEPT_ID_PK",
	        "referencedTable" : "DEPARTMENTS",
	        "referencedOwner" : "HR",
	        "Action" : "RESTRICT",
	        "referencedColumns" :
	        [
	          {
	            "name" : "DEPARTMENT_ID"
	          }
	        ]
	      },
	      {
	        "name" : "EMP_JOB_FK",
	        "constraintType" : "REFERENTIAL INTEGRITY",
	        "columns" :
	        [
	          {
	            "name" : "JOB_ID"
	          }
	        ],
	        "status" : "ENABLED",
	        "deferrable" : false,
	        "validated" : "VALIDATED",
	        "sysGeneratedName" : false,
	        "referencedConstraintName" : "JOB_ID_PK",
	        "referencedTable" : "JOBS",
	        "referencedOwner" : "HR",
	        "Action" : "RESTRICT",
	        "referencedColumns" :
	        [
	          {
	            "name" : "JOB_ID"
	          }
	        ]
	      },
	      {
	        "name" : "EMP_MANAGER_FK",
	        "constraintType" : "REFERENTIAL INTEGRITY",
	        "columns" :
	        [
	          {
	            "name" : "MANAGER_ID"
	          }
	        ],
	        "status" : "ENABLED",
	        "deferrable" : false,
	        "validated" : "VALIDATED",
	        "sysGeneratedName" : false,
	        "referencedConstraintName" : "EMP_EMP_ID_PK",
	        "referencedTable" : "EMPLOYEES",
	        "referencedOwner" : "HR",
	        "Action" : "RESTRICT",
	        "referencedColumns" :
	        [
	          {
	            "name" : "EMPLOYEE_ID"
	          }
	        ]
	      }
	    ]
	  },
	  "etag" : "250A14E4E687854657E7336BCE46432F"
	}
	```
5. Retrieving metadata when the specified `etag` matches the current `etag` would return an empty document:
	```md
	SQL> conn hr/hr
	Connected.
	SQL>
	SQL> SELECT JSON_SERIALIZE(dbms_developer.get_metadata(name => 'REGIONS',
	etag => '9ADC6D08AE0D5C82C0188D53F3ECD5B9')RETURNING CLOB PRETTY) from dual;
	```
	Executing this query would produce an empty JSON document:
	```md
	{
	}
	```

### JSON Schema for Different Object and Sub-Object Types

This section provides an overview to the different schema possible for various object types, sub-object types and levels.

The JSON Schema can be used as a reference by applications to parse the JSON document returned. If you are programming against a specific version of the database program, you use that specific version of the JSON schema for that database version, and that schema will always be the same. But, if you upgrade or downgrade to a different release, you will be using a different schema version and then you need to use that correct schema. If there is any change in the schema, the version number in the `$id` field will be changed. Applications can rely on this number in case Oracle plans to revise the JSON schema in the future. Existing versions will remain unchanged, so applications will remain fully functional and unaffected by the updates.

- The detailed description of the JSON schema for the `object_type` `TABLE` at all levels is described in the section: JSON Schema for Object Type: `TABLE`
- The detailed description of the JSON schema for the `object_type` `INDEX` at all levels is described in the section: JSON Schema for Object Type: `INDEX`
- The detailed description of the JSON schema for the `object_type` `VIEW` at all levels is described in the section: JSON Schema for Object Type: `VIEW`
- The detailed description of the JSON schema for the sub-object type `COLUMNS` at all levels is described in the section: JSON Schema for Sub-Object Type: columns
- The detailed description of the JSON schema for the sub-object type `CONSTRAINTS` at all levels is described in the section: JSON Schema for Sub-Object Type: constraints

### JSON Schema for Object Type: TABLE

This section describes the JSON schema for the object type `TABLE` at all levels.

**JSON Schema for TABLE Object Type in Tabular Form**

Table 2 JSON schema for object type: TABLE

<table><thead><tr><th width="0%">FIELDS</th><th width="0%"></th><th width="0%"></th><th colspan="3">LEVELS</th></tr></thead><tbody><tr><td headers="d492043e3050" width="0%"></td><td headers="d492043e3058 d492043e3052" width="0%"></td><td headers="d492043e3058 d492043e3053" width="0%"></td><td headers="d492043e3058 d492043e3054" width="0%">BASIC</td><td headers="d492043e3058 d492043e3054" width="0%">TYPICAL</td><td headers="d492043e3058 d492043e3054" width="0%">ALL</td></tr><tr><td headers="d492043e3050" width="0%"><p>name</p></td><td headers="d492043e3068 d492043e3052" width="0%"></td><td headers="d492043e3068 d492043e3053" width="0%"></td><td headers="d492043e3068 d492043e3054" width="0%">✔</td><td headers="d492043e3068 d492043e3054" width="0%">✔</td><td headers="d492043e3068 d492043e3054" width="0%">✔</td></tr><tr><td headers="d492043e3050" width="0%"><p>schema</p></td><td headers="d492043e3082 d492043e3052" width="0%"></td><td headers="d492043e3082 d492043e3053" width="0%"></td><td headers="d492043e3082 d492043e3054" width="0%">✔</td><td headers="d492043e3082 d492043e3054" width="0%">✔</td><td headers="d492043e3082 d492043e3054" width="0%">✔</td></tr><tr><td headers="d492043e3050" width="0%"><p>columns</p></td><td headers="d492043e3096 d492043e3052" width="0%"></td><td headers="d492043e3096 d492043e3053" width="0%"></td><td headers="d492043e3096 d492043e3054" width="0%">✔</td><td headers="d492043e3096 d492043e3054" width="0%">✔</td><td headers="d492043e3096 d492043e3054" width="0%">✔</td></tr><tr><td headers="d492043e3050" width="0%"><p>hasBeenAnalyzed</p></td><td headers="d492043e3110 d492043e3052" width="0%"></td><td headers="d492043e3110 d492043e3053" width="0%"></td><td headers="d492043e3110 d492043e3054" width="0%"></td><td headers="d492043e3110 d492043e3054" width="0%">✔</td><td headers="d492043e3110 d492043e3054" width="0%">✔</td></tr><tr><td headers="d492043e3050" width="0%"><p>lastAnalyzed</p></td><td headers="d492043e3123 d492043e3052" width="0%"></td><td headers="d492043e3123 d492043e3053" width="0%"></td><td headers="d492043e3123 d492043e3054" width="0%"></td><td headers="d492043e3123 d492043e3054" width="0%">✔</td><td headers="d492043e3123 d492043e3054" width="0%">✔</td></tr><tr><td headers="d492043e3050" width="0%"><p>numRows</p></td><td headers="d492043e3136 d492043e3052" width="0%"></td><td headers="d492043e3136 d492043e3053" width="0%"></td><td headers="d492043e3136 d492043e3054" width="0%"></td><td headers="d492043e3136 d492043e3054" width="0%">✔</td><td headers="d492043e3136 d492043e3054" width="0%">✔</td></tr><tr><td headers="d492043e3050" width="0%"><p>sampleSize</p></td><td headers="d492043e3149 d492043e3052" width="0%"></td><td headers="d492043e3149 d492043e3053" width="0%"></td><td headers="d492043e3149 d492043e3054" width="0%"></td><td headers="d492043e3149 d492043e3054" width="0%">✔</td><td headers="d492043e3149 d492043e3054" width="0%">✔</td></tr><tr><td headers="d492043e3050" width="0%"><p>avgRowLen</p></td><td headers="d492043e3162 d492043e3052" width="0%"></td><td headers="d492043e3162 d492043e3053" width="0%"></td><td headers="d492043e3162 d492043e3054" width="0%"></td><td headers="d492043e3162 d492043e3054" width="0%">✔</td><td headers="d492043e3162 d492043e3054" width="0%">✔</td></tr><tr><td headers="d492043e3050" width="0%"><p>clusterName</p></td><td headers="d492043e3175 d492043e3052" width="0%"></td><td headers="d492043e3175 d492043e3053" width="0%"></td><td headers="d492043e3175 d492043e3054" width="0%"></td><td headers="d492043e3175 d492043e3054" width="0%">✔</td><td headers="d492043e3175 d492043e3054" width="0%">✔</td></tr><tr><td headers="d492043e3050" width="0%"><p>clusterOwner</p></td><td headers="d492043e3188 d492043e3052" width="0%"></td><td headers="d492043e3188 d492043e3053" width="0%"></td><td headers="d492043e3188 d492043e3054" width="0%"></td><td headers="d492043e3188 d492043e3054" width="0%">✔</td><td headers="d492043e3188 d492043e3054" width="0%">✔</td></tr><tr><td headers="d492043e3050" width="0%"><p>external</p></td><td headers="d492043e3202 d492043e3052" width="0%"></td><td headers="d492043e3202 d492043e3053" width="0%"></td><td headers="d492043e3202 d492043e3054" width="0%"></td><td headers="d492043e3202 d492043e3054" width="0%">✔</td><td headers="d492043e3202 d492043e3054" width="0%">✔</td></tr><tr><td headers="d492043e3050" width="0%"><p>temporary</p></td><td headers="d492043e3215 d492043e3052" width="0%"></td><td headers="d492043e3215 d492043e3053" width="0%"></td><td headers="d492043e3215 d492043e3054" width="0%"></td><td headers="d492043e3215 d492043e3054" width="0%">✔</td><td headers="d492043e3215 d492043e3054" width="0%">✔</td></tr><tr><td headers="d492043e3050" width="0%"><p>indexes</p></td><td headers="d492043e3228 d492043e3052" width="0%"></td><td headers="d492043e3228 d492043e3053" width="0%"></td><td headers="d492043e3228 d492043e3054" width="0%"></td><td headers="d492043e3228 d492043e3054" width="0%">✔</td><td headers="d492043e3228 d492043e3054" width="0%">✔</td></tr><tr><td headers="d492043e3050" width="0%"><p>constraints</p></td><td headers="d492043e3241 d492043e3052" width="0%"></td><td headers="d492043e3241 d492043e3053" width="0%"></td><td headers="d492043e3241 d492043e3054" width="0%"></td><td headers="d492043e3241 d492043e3054" width="0%">✔</td><td headers="d492043e3241 d492043e3054" width="0%">✔</td></tr><tr><td headers="d492043e3050" width="0%"><p>segmentCreated</p></td><td headers="d492043e3254 d492043e3052" width="0%"></td><td headers="d492043e3254 d492043e3053" width="0%"></td><td headers="d492043e3254 d492043e3054" width="0%"></td><td headers="d492043e3254 d492043e3054" width="0%"></td><td headers="d492043e3254 d492043e3054" width="0%">✔</td></tr><tr><td headers="d492043e3050" width="0%"><p>inMemory</p></td><td headers="d492043e3266 d492043e3052" width="0%"></td><td headers="d492043e3266 d492043e3053" width="0%"></td><td headers="d492043e3266 d492043e3054" width="0%"></td><td headers="d492043e3266 d492043e3054" width="0%"></td><td headers="d492043e3266 d492043e3054" width="0%">✔</td></tr><tr><td headers="d492043e3050" width="0%"><p>compression</p></td><td headers="d492043e3278 d492043e3052" width="0%"></td><td headers="d492043e3278 d492043e3053" width="0%"></td><td headers="d492043e3278 d492043e3054" width="0%"></td><td headers="d492043e3278 d492043e3054" width="0%"></td><td headers="d492043e3278 d492043e3054" width="0%">✔</td></tr><tr><td headers="d492043e3050" width="0%"><p>dependencies</p></td><td headers="d492043e3290 d492043e3052" width="0%"></td><td headers="d492043e3290 d492043e3053" width="0%"></td><td headers="d492043e3290 d492043e3054" width="0%"></td><td headers="d492043e3290 d492043e3054" width="0%"></td><td headers="d492043e3290 d492043e3054" width="0%">✔</td></tr><tr><td headers="d492043e3050" rowspan="3" width="0%"><p>authorizations</p></td><td headers="d492043e3302 d492043e3052" width="0%">grantee</td><td headers="d492043e3302 d492043e3053" width="0%"></td><td headers="d492043e3302 d492043e3054" rowspan="3" width="0%"></td><td headers="d492043e3302 d492043e3054" rowspan="3" width="0%"></td><td headers="d492043e3302 d492043e3054" rowspan="3" width="0%">✔</td></tr><tr><td headers="d492043e3302 d492043e3052" rowspan="2" width="0%">privileges</td><td headers="d492043e3302 d492043e3053" width="0%">name</td></tr><tr><td headers="d492043e3302 d492043e3053" width="0%">grantable</td></tr><tr><td headers="d492043e3050" width="0%"><p>inMemoryPriority</p></td><td headers="d492043e3324 d492043e3052" width="0%"></td><td headers="d492043e3324 d492043e3053" width="0%"></td><td headers="d492043e3324 d492043e3054" width="0%"></td><td headers="d492043e3324 d492043e3054" width="0%"></td><td headers="d492043e3324 d492043e3054" width="0%">✔</td></tr><tr><td headers="d492043e3050" width="0%"><p>inMemoryDistribute</p></td><td headers="d492043e3336 d492043e3052" width="0%"></td><td headers="d492043e3336 d492043e3053" width="0%"></td><td headers="d492043e3336 d492043e3054" width="0%"></td><td headers="d492043e3336 d492043e3054" width="0%"></td><td headers="d492043e3336 d492043e3054" width="0%">✔</td></tr><tr><td headers="d492043e3050" width="0%"><p>inMemoryCompression</p></td><td headers="d492043e3348 d492043e3052" width="0%"></td><td headers="d492043e3348 d492043e3053" width="0%"></td><td headers="d492043e3348 d492043e3054" width="0%"></td><td headers="d492043e3348 d492043e3054" width="0%"></td><td headers="d492043e3348 d492043e3054" width="0%">✔</td></tr><tr><td headers="d492043e3050" width="0%"><p>inMemoryDuplicate</p></td><td headers="d492043e3360 d492043e3052" width="0%"></td><td headers="d492043e3360 d492043e3053" width="0%"></td><td headers="d492043e3360 d492043e3054" width="0%"></td><td headers="d492043e3360 d492043e3054" width="0%"></td><td headers="d492043e3360 d492043e3054" width="0%">✔</td></tr><tr><td headers="d492043e3050" width="0%"><p>iotType</p></td><td headers="d492043e3372 d492043e3052" width="0%"></td><td headers="d492043e3372 d492043e3053" width="0%"></td><td headers="d492043e3372 d492043e3054" width="0%"></td><td headers="d492043e3372 d492043e3054" width="0%"></td><td headers="d492043e3372 d492043e3054" width="0%">✔</td></tr></tbody></table>

**Note:** The fields of the sub-objects `columns` and `constraints` varies depending on the choice of the `level`. The detailed information of the fields present in the sub-object `columns` is described in the section: JSON Schema for Sub-Object Type: `columns`. The detailed information of the fields present in the sub-object `constraints` is described in the section: JSON Schema for Sub-Object Type: `constraints`.

**JSON Schema for TABLE object type at level BASIC**

```md
{
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "https://oracle.com/schema/
19.28/DBMS_DEVELOPER.GET_METADATA/BASIC/object_info/table",
    "title": "DBMS_DEVELOPER.GET_METADATA/BASIC/OBJECT_INFO/TABLE",
    "description": "Information for a table object",
    "type": "object",
    "properties": {
        "name": {
            "description": "Table name",
            "type": "string"
        },
        "schema": {
            "description": "Table schema",
            "type": "string"
        },
        "columns": {
            "description": "Table columns",
            "type": "array",
            "items": {
                "$ref": "../column"
            }
        }
    },
    "required": [
        "name",
        "schema",
        "columns"
    ]
}
```

**JSON Schema for TABLE object type at level TYPICAL**

```md
{
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "https://oracle.com/schema/19.28/DBMS_DEVELOPER.GET_METADATA/TYPICAL/object_info/table",
    "title": "DBMS_DEVELOPER.GET_METADATA/TYPICAL/OBJECT_INFO/TABLE",
    "description": "Information for a table object",
    "type": "object",
    "properties": {
        "name": {
            "description": "Table name",
            "type": "string"
        },
        "schema": {
            "description": "Table schema",
            "type": "string"
        },
        "columns": {
            "description": "Table columns",
            "type": "array",
            "items": {
                "$ref": "../column"
            }
        },
        "hasBeenAnalyzed": {
            "description": "Indicates whether table has been analyzed",
            "type": "boolean",
            "default": false
        },
        "lastAnalyzed": {
            "description": "Last time table was analyzed",
            "type": "string",
            "format": "date-time"
        },
        "numRows": {
            "description": "Number of rows",
            "type": "integer"
        },
        "sampleSize": {
            "description": "Analyzed sample size",
            "type": "integer"
        },
        "avgRowLen": {
            "description": "Average row length",
            "type": "integer"
        },
        "clusterName": {
            "description": "Name of the cluster, if any, to which the table belongs",
            "type": "string"
        },
        "clusterOwner": {
            "description": "Owner of the cluster, if any, to which the table belongs",
            "type": "string"
        },
        "external": {
            "description": "Indicates whether the table is an external table (YES) or not (NO)",
            "type": "string"
        },
        "temporary": {
            "description": "Indicates whether the table is temporary (YES) or not (NO)",
            "type": "string"
        },
        "indexes": {
            "description": "Table indexes",
            "type": "array",
            "items": {
                "$ref": "../index"
            }
        },
        "constraints": {
            "description": "Table constraints",
            "type": "array",
            "items": {
                "$ref": "../constraint"
            }
        }
    },
    "required": [
        "name",
        "schema",
        "columns",
        "external",
        "temporary"
    ]
}
```

**JSON Schema for TABLE object type at level ALL**

```md
{
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "https://oracle.com/schema/19.28/DBMS_DEVELOPER.GET_METADATA/ALL/object_info/table",
    "title": "DBMS_DEVELOPER.GET_METADATA/ALL/OBJECT_INFO/TABLE",
    "description": "Information for a table object",
    "type": "object",
    "properties": {
        "name": {
            "description": "Table name",
            "type": "string"
        },
        "schema": {
            "description": "Table schema",
            "type": "string"
        },
        "columns": {
            "description": "Table columns",
            "type": "array",
            "items": {
                "$ref": "../column"
            }
        },
        "hasBeenAnalyzed": {
            "description": "Indicates whether table has been analyzed",
            "type": "boolean",
            "default": false
        },
        "lastAnalyzed": {
            "description": "Last time table was analyzed",
            "type": "string",
            "format": "date-time"
        },
        "numRows": {
            "description": "Number of rows",
            "type": "integer"
        },
        "sampleSize": {
            "description": "Analyzed sample size",
            "type": "integer"
        },
        "avgRowLen": {
            "description": "Average row length",
            "type": "integer"
        },
        "clusterName": {
            "description": "Name of the cluster, if any, to which the table belongs",
            "type": "string"
        },
        "clusterOwner": {
            "description": "Owner of the cluster, if any, to which the table belongs",
            "type": "string"
        },
        "external": {
            "description": "Indicates whether the table is an external table (YES) or not (NO)",
            "type": "string"
        },
        "temporary": {
            "description": "Indicates whether the table is temporary (YES) or not (NO)",
            "type": "string"
        },
        "indexes": {
            "description": "Table indexes",
            "type": "array",
            "items": {
                "$ref": "../index"
            }
        },
        "constraints": {
            "description": "Table constraints",
            "type": "array",
            "items": {
                "$ref": "../constraint"
            }
        },
        "segmentCreated": {
            "description": "Indicates whether the table segment is created.",
            "type": "string"
        },
        "inMemory": {
            "description": "Indicates whether the In-Memory Column Store (IM column store) is
                            enabled (ENABLED) or disabled (DISABLED) for the table",
            "type": "string"
        },
        "compression": {
            "description": "Indicates whether table compression is enabled (ENABLED) or not (DISABLED)",
            "type": "string"
        },
        "dependencies": {
            "description": "Indicates whether the table is an external table (YES) or not (NO)",
            "type": "string"
        },
         "authorizations": {
            "description": "Table authorizations",
            "type": "object",
            "properties": {
                "grantee": {
                    "description": "Name of the user to whom access was granted",
                    "type": "string"
                },
                "privileges": {
                    "description": "All privileges granted to grantee",
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "name": {
                                "description": "Privilege on the object,
                                "type": "string"
                            },
                            "grantable": {
                                "description": "Indicates whether the privilege was granted with the GRANT OPTION",
                                "type": "string"
                            }
                        }
                    }
                }
            }
        },
        "inMemoryPriority": {
            "description": "Indicates the priority for In-Memory Column Store (IM column store) population. ",
            "type": "string"
        },
        "inMemoryDistribute": {
            "description": "Indicates how the IM column store is distributed in an
                            Oracle Real Application Clusters (Oracle RAC) environment",
            "type": "string"
        },
        "inMemoryCompression": {
            "description": "Indicates the compression level for the IM column store",
            "type": "string"
        },
        "inMemoryDuplicate": {
            "description": "Indicates the duplicate setting for the IM column store in an Oracle RAC environment",
            "type": "string"
        },
        "iotType": {
            "description": "If the table is an index-organized table, then IOT_TYPE is IOT,
                            IOT_OVERFLOW, or IOT_MAPPING. If the table is not an
                            index-organized table, then IOT_TYPE is NULL.",
            "type": "string"
        }
    },
    "required": [
        "name",
        "schema",
        "columns",
        "external",
        "temporary",
        "inMemory",
        "compression",
        "dependencies",
        "segmentCreated"
    ]
}
```

### JSON Schema for Object Type: VIEW

This section describes the JSON schema for the object type `VIEW` at all levels.

**JSON Schema for VIEW Object Type in Tabular Form**

Table 3 JSON Schema for VIEW Object Type

<table><thead><tr><th width="0%">Fields</th><th width="0%"></th><th width="0%"></th><th colspan="3">LEVELS</th></tr></thead><tbody><tr><td headers="d492043e4038" width="0%"></td><td headers="d492043e4046 d492043e4040" width="0%"></td><td headers="d492043e4046 d492043e4041" width="0%"></td><td headers="d492043e4046 d492043e4042" width="0%">BASIC</td><td headers="d492043e4046 d492043e4042" width="0%">TYPICAL</td><td headers="d492043e4046 d492043e4042" width="0%">ALL</td></tr><tr><td headers="d492043e4038" width="0%"><p>name</p></td><td headers="d492043e4056 d492043e4040" width="0%"></td><td headers="d492043e4056 d492043e4041" width="0%"></td><td headers="d492043e4056 d492043e4042" width="0%">✔</td><td headers="d492043e4056 d492043e4042" width="0%">✔</td><td headers="d492043e4056 d492043e4042" width="0%">✔</td></tr><tr><td headers="d492043e4038" width="0%"><p>schema</p></td><td headers="d492043e4070 d492043e4040" width="0%"></td><td headers="d492043e4070 d492043e4041" width="0%"></td><td headers="d492043e4070 d492043e4042" width="0%">✔</td><td headers="d492043e4070 d492043e4042" width="0%">✔</td><td headers="d492043e4070 d492043e4042" width="0%">✔</td></tr><tr><td headers="d492043e4038" width="0%"><p>columns</p></td><td headers="d492043e4084 d492043e4040" width="0%"></td><td headers="d492043e4084 d492043e4041" width="0%"></td><td headers="d492043e4084 d492043e4042" width="0%">✔</td><td headers="d492043e4084 d492043e4042" width="0%">✔</td><td headers="d492043e4084 d492043e4042" width="0%">✔</td></tr><tr><td headers="d492043e4038" width="0%"><p>readOnly</p></td><td headers="d492043e4098 d492043e4040" width="0%"></td><td headers="d492043e4098 d492043e4041" width="0%"></td><td headers="d492043e4098 d492043e4042" width="0%"></td><td headers="d492043e4098 d492043e4042" width="0%">✔</td><td headers="d492043e4098 d492043e4042" width="0%">✔</td></tr><tr><td headers="d492043e4038" width="0%"><p>constraints</p></td><td headers="d492043e4111 d492043e4040" width="0%"></td><td headers="d492043e4111 d492043e4041" width="0%"></td><td headers="d492043e4111 d492043e4042" width="0%"></td><td headers="d492043e4111 d492043e4042" width="0%">✔</td><td headers="d492043e4111 d492043e4042" width="0%">✔</td></tr><tr><td headers="d492043e4038" width="0%"><p>editioningView</p></td><td headers="d492043e4124 d492043e4040" width="0%"></td><td headers="d492043e4124 d492043e4041" width="0%"></td><td headers="d492043e4124 d492043e4042" width="0%"></td><td headers="d492043e4124 d492043e4042" width="0%"></td><td headers="d492043e4124 d492043e4042" width="0%">✔</td></tr><tr><td headers="d492043e4038" rowspan="3" width="0%"><p>authorizations</p></td><td headers="d492043e4136 d492043e4040" width="0%"><p>grantee</p></td><td headers="d492043e4136 d492043e4041" width="0%"></td><td headers="d492043e4136 d492043e4042" rowspan="3" width="0%"></td><td headers="d492043e4136 d492043e4042" rowspan="3" width="0%"></td><td headers="d492043e4136 d492043e4042" rowspan="3" width="0%">✔</td></tr><tr><td headers="d492043e4136 d492043e4040" rowspan="2" width="0%"><p>privileges</p></td><td headers="d492043e4136 d492043e4041" width="0%">name</td></tr><tr><td headers="d492043e4136 d492043e4041" width="0%">grantable</td></tr></tbody></table>

**Note:** The fields of the sub-objects `columns` and `constraints` varies depending on the choice of the `level`. The detailed information of the fields present in the sub-object `columns` is described in the section: JSON Schema for Sub-Object Type: `columns`. The detailed information of the fields present in the sub-object `constraints` is described in the section: JSON Schema for Sub-Object Type: `constraints`.

**JSON Schema for VIEW object type at level BASIC**

```md
{
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "https://oracle.com/schema/
19.28/DBMS_DEVELOPER.GET_METADATA/BASIC/object_info/view",
    "title": "DBMS_DEVELOPER.GET_METADATA/BASIC/OBJECT_INFO/VIEW",
    "description": "Information for a View object",
    "type": "object",
    "properties": {
        "name": {
            "description": "View name",
            "type": "string"
        },
        "schema": {
            "description": "View schema",
            "type": "string"
        },
        "columns": {
            "description": "View columns",
            "type": "array",
            "items": {
                "$ref": "../column"
            }
        }
    },
    "required": [
        "name",
        "schema",
        "columns"
    ]
}
```

**JSON Schema for VIEW object type at level TYPICAL**

```md
{
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "https://oracle.com/schema/19.28/DBMS_DEVELOPER.GET_METADATA/TYPICAL/object_info/view",
    "title": "DBMS_DEVELOPER.GET_METADATA/TYPICAL/OBJECT_INFO/VIEW",
    "description": "Information for a View object",
    "type": "object",
    "properties": {
        "name": {
            "description": "View name",
            "type": "string"
        },
        "schema": {
            "description": "View schema",
            "type": "string"
        },
        "columns": {
            "description": "View columns",
            "type": "array",
            "items": {
                "$ref": "../column"
            }
        },
        "readOnly": {
            "description": "An indicator of whether the view is a Read Only View",
            "type": "boolean",
            "default": true
        },
        "constraints": {
            "description": "View constraints",
            "type": "array",
            "items": {
                "$ref": "../constraint"
            }
        }
    },
    "required": [
         "name",
         "schema",
         "readOnly",
         "columns"
    ]
}
```

**JSON Schema for VIEW object type at level ALL**

```md
{
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "https://oracle.com/schema/19.28/DBMS_DEVELOPER.GET_METADATA/ALL/object_info/view",
    "title": "DBMS_DEVELOPER.GET_METADATA/ALL/OBJECT_INFO/VIEW",
    "description": "Information for a View object",
    "type": "object",
    "properties": {
        "name": {
            "description": "View name",
            "type": "string"
        },
        "schema": {
            "description": "View schema",
            "type": "string"
        },
        "columns": {
            "description": "View columns",
            "type": "array",
            "items": {
                "$ref": "../column"
            }
        },
        "readOnly": {
            "description": "An indicator of whether the view is a Read Only View",
            "type": "boolean",
            "default": true
        },
        "constraints": {
            "description": "View constraints",
            "type": "array",
            "items": {
                "$ref": "../constraint"
            }
        },,
        "editioningView": {
            "description": "An indicator of whether the view is an Editioning view",
            "type": "boolean",
            "default": false
        },
        "authorizations": {
            "description": "View authorizations",
            "type": "object",
            "properties": {
                "grantee": {
                    "description": "Name of the user to whom access was granted",
                    "type": "string"
                },
                "privileges": {
                    "description": "All privileges granted to grantee",
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "name": {
                                "description": "Privilege on the object,
                                "type": "string"
                            },
                            "grantable": {
                                "description": "Indicates whether the privilege was granted with the GRANT OPTION",
                                "type": "string"
                            }
                        }
                    }
                }
            }
        }
    },
    "required": [
         "name",
         "schema",
         "columns"
    ]
}
```

### JSON Schema for Object Type: INDEX

This section describes the JSON schema for the object type `INDEX` at all levels.

**JSON Schema for INDEX Object Type in Tabular Form**

Table 4 JSON Schema for INDEX Object Type

| Fields |  |  | LEVELS |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  | BASIC | TYPICAL | ALL |
| name |  |  | ✔ | ✔ | ✔ |
| indexType |  |  | ✔ | ✔ | ✔ |
| owner |  |  | ✔ | ✔ | ✔ |
| tableName |  |  | ✔ | ✔ | ✔ |
| status |  |  | ✔ | ✔ | ✔ |
| columns |  |  | ✔ | ✔ | ✔ |
| uniqueness |  |  |  | ✔ | ✔ |
| funcIdxStatus |  |  |  | ✔ | ✔ |
| hasBeenAnalyzed |  |  |  | ✔ | ✔ |
| lastAnalyzed |  |  |  | ✔ | ✔ |
| numRows |  |  |  | ✔ | ✔ |
| sampleSize |  |  |  | ✔ | ✔ |
| partitioned |  |  |  | ✔ | ✔ |
| distinctKeys |  |  |  |  | ✔ |
| compression |  |  |  |  | ✔ |
| segmentCreated |  |  |  |  | ✔ |
| visibility |  |  |  |  | ✔ |
| toBeDropped |  |  |  |  | ✔ |

**Note:** The fields of the sub-object `columns` varies depending on the choice of `level`. The detailed information of the fields present in the sub-object `columns` is described in the section: JSON Schema for Sub-Object Type: `columns`.

**JSON Schema for INDEX object type at level BASIC**

```md
{
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "https://oracle.com/schema/
19.28/DBMS_DEVELOPER.GET_METADATA/BASIC/object_info/index",
    "title": "DBMS_DEVELOPER.GET_METADATA/BASIC/OBJECT_INFO/INDEX",
    "description": "Information for index",
    "type": "object",
    "properties": {
        "name": {
            "description": "Index name",
            "type": "string"
        },
        "indexType": {
            "description": "Index Types i.e. CLUSTER, NORMAL, NORMAL/REV, BITMAP, DOMAIN,
                            LOB, IOT - TOP, FUNCTION-BASED NORMAL, FUNCTION-BASED NORMAL/REV,
                            FUNCTION-BASED BITMAP, FUNCTION-BASED DOMAIN, VECTOR",
            "type": "string"
        },
        "owner": {
            "description": "Owner of the indexed object",
            "type": "string"
        },
        "tableName": {
            "description": "Name of the indexed object",
            "type": "string"
        },
        "status": {
            "description": "Status",
            "type": {
                "enum": [
                    "VALID",
                    "UNUSABLE",
                    "INPROGRS",
                    "N/A"
                ]
            }
        },
        "columns": {
            "description": "Index column(s)",
            "type": "array",
            "items": {
                "$ref": "../column"
            }
        }
    },
    "required": [
        "name",
        "indexType",
        "owner",
        "tableName",
        "status",
        "columns"
    ]
}
```

**JSON Schema for INDEX object type at level TYPICAL**

```md
{
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "https://oracle.com/schema/19.28/DBMS_DEVELOPER.GET_METADATA/TYPICAL/object_info/index",
    "title": "DBMS_DEVELOPER.GET_METADATA/TYPICAL/OBJECT_INFO/INDEX",
    "description": "Information for index",
    "type": "object",
    "properties": {
        "name": {
            "description": "Index name",
            "type": "string"
        },
        "indexType": {
            "description": "Index Types i.e. CLUSTER, NORMAL, NORMAL/REV, BITMAP, DOMAIN,
                            LOB, IOT - TOP, FUNCTION-BASED NORMAL, FUNCTION-BASED NORMAL/REV,
                            FUNCTION-BASED BITMAP, FUNCTION-BASED DOMAIN, VECTOR",
            "type": "string"
        },
        "owner": {
            "description": "Owner of the indexed object",
            "type": "string"
        },
        "tableName": {
            "description": "Name of the indexed object",
            "type": "string"
        },
        "status": {
            "description": "Status",
            "type": {
                "enum": [
                    "VALID",
                    "INVALID",
                    "INPROGRS",
                    "N/A"
                ]
            }
        },
        "columns": {
            "description": "Index column(s)",
            "type": "array",
            "items": {
                "$ref": "../column"
            }
        },
        "uniqueness": {
            "description": "Uniqueness",
            "type": "string",
            "enum": [
                "UNIQUE",
                "NONUNIQUE"
            ]
        },
        "funcIdxStatus": {
            "description": "Functional index status",
            "type": "string"
        },
        "hasBeenAnalyzed": {
            "description": "Indicates whether index has been analyzed",
            "type": "boolean",
            "default": false
        },
        "lastAnalyzed": {
            "description": "Last time View was analyzed",
            "type": "string",
            "format": "date-time"
        },
        "numRows": {
            "description": "Number of rows",
            "type": "integer"
        },
        "sampleSize": {
            "description": "Analyzed sample size",
            "type": "integer"
        },
        "partitioned": {
            "description": "Indicates whether the index is partitioned",
            "type": "boolean",
            "default": false
        }
    },
    "required": [
        "name",
        "indexType",
        "owner",
        "tableName",
        "status",
        "columns"
    ]
}
```

**JSON Schema for INDEX object type at level ALL**

```md
{
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "https://oracle.com/schema/19.28/DBMS_DEVELOPER.GET_METADATA/ALL/object_info/index",
    "title": "DBMS_DEVELOPER.GET_METADATA/ALL/OBJECT_INFO/INDEX",
    "description": "Information for index",
    "type": "object",
    "properties": {
        "name": {
            "description": "Index name",
            "type": "string"
        },
        "indexType": {
            "description": "Index Types i.e. CLUSTER, NORMAL, NORMAL/REV, BITMAP, DOMAIN,
                            LOB, IOT - TOP, FUNCTION-BASED NORMAL, FUNCTION-BASED NORMAL/REV,
                            FUNCTION-BASED BITMAP, FUNCTION-BASED DOMAIN, VECTOR",
            "type": "string"
        },
        "owner": {
            "description": "Owner of the indexed object",
            "type": "string"
        },
        "tableName": {
            "description": "Name of the indexed object",
            "type": "string"
        },
        "status": {
            "description": "Status",
            "type": {
                 "enum": [
                    "VALID",
                    "INVALID",
                    "INPROGRS",
                    "N/A"
                ]
            }
        },
        "columns": {
            "description": "Index column(s)",
            "type": "array",
            "items": {
                "$ref": "../column"
            }
        },
        "uniqueness": {
            "description": "Uniqueness",
            "type": "string",
            "enum": [
                "UNIQUE",
                "NONUNIQUE"
            ]
        },
        "funcIdxStatus": {
            "description": "Functional index status",
            "type": "string"
        },
        "hasBeenAnalyzed": {
            "description": "Indicates whether index has been analyzed",
            "type": "boolean",
            "default": false
        },
        "lastAnalyzed": {
            "description": "Last time View was analyzed",
            "type": "string",
            "format": "date-time"
        },
        "numRows": {
            "description": "Number of rows",
            "type": "integer"
        },
        "sampleSize": {
            "description": "Analyzed sample size",
            "type": "integer"
        },
        "partitioned": {
            "description": "Indicates whether the index is partitioned",
            "type": "boolean",
            "default": false
        },
        "distinctKeys": {
            "description": "Number of distinct keys in the index",
            "type": "integer"
        },
        "compression": {
            "description": "Compression property of the index: ENABLED, DISABLED, ADVANCED HIGH, ADVANCED LOW",
            "type": "string",
            "enum": [
                "ENABLED",
                "DISABLED",
                "ADVANCED HIGH",
                "ADVANCED LOW"
            ]
        },
        "segmentCreated": {
            "description": "Whether the index segment has been created",
            "type": "string",
            "enum": [
                "YES",
                "NO",
                "N/A"
            ]
        },
        "visibility": {
            "description": "Whether the index is VISIBLE or INVISIBLE to the optimizer",
            "type": "string",
            "enum": [
                "VISIBLE",
                "INVISIBLE"
            ]
        },
        "toBeDropped": {
            "description": "Whether index is dropped and is in Recycle Bin",
            "type": "boolean"
        }
    },
    "required": [
         "name",
         "indexType",
         "owner",
         "tableName",
         "status",
         "columns",
         "partitioned"
         "compression",
         "segmentCreated",
         "visibility",
         "tobeDropped"
   ]
}
```

### JSON Schema for Sub-Object Type: columns

JSON schema for the sub-object `columns` for the levels: `basic`, `typical` and `all`.

**JSON Schema for columns Sub-Object Type in Tabular Form**

Table 5 JSON Schema for COLUMNS

<table><thead><tr><th width="0%">Fields</th><th width="0%"></th><th colspan="3">Levels</th></tr></thead><tbody><tr><td headers="d492043e5652" width="0%"></td><td headers="d492043e5659 d492043e5654" width="0%"></td><td headers="d492043e5659 d492043e5655" width="0%">BASIC</td><td headers="d492043e5659 d492043e5655" width="0%">TYPICAL</td><td headers="d492043e5659 d492043e5655" width="0%">ALL</td></tr><tr><td headers="d492043e5652" width="0%">name</td><td headers="d492043e5668 d492043e5654" width="0%"></td><td headers="d492043e5668 d492043e5655" width="0%">✔</td><td headers="d492043e5668 d492043e5655" width="0%">✔</td><td headers="d492043e5668 d492043e5655" width="0%">✔</td></tr><tr><td headers="d492043e5652" width="0%">default</td><td headers="d492043e5678 d492043e5654" width="0%"></td><td headers="d492043e5678 d492043e5655" width="0%">✔</td><td headers="d492043e5678 d492043e5655" width="0%">✔</td><td headers="d492043e5678 d492043e5655" width="0%">✔</td></tr><tr><td headers="d492043e5652" width="0%">notNull</td><td headers="d492043e5688 d492043e5654" width="0%"></td><td headers="d492043e5688 d492043e5655" width="0%">✔</td><td headers="d492043e5688 d492043e5655" width="0%">✔</td><td headers="d492043e5688 d492043e5655" width="0%">✔</td></tr><tr><td headers="d492043e5652" rowspan="9" width="0%">dataType</td><td headers="d492043e5698 d492043e5654" width="0%">type</td><td headers="d492043e5698 d492043e5655" rowspan="9" width="0%">✔</td><td headers="d492043e5698 d492043e5655" rowspan="9" width="0%">✔</td><td headers="d492043e5698 d492043e5655" rowspan="9" width="0%">✔</td></tr><tr><td headers="d492043e5698 d492043e5654" width="0%">precision</td></tr><tr><td headers="d492043e5698 d492043e5654" width="0%">length</td></tr><tr><td headers="d492043e5698 d492043e5654" width="0%">scale</td></tr><tr><td headers="d492043e5698 d492043e5654" width="0%">size</td></tr><tr><td headers="d492043e5698 d492043e5654" width="0%">sizeUnits</td></tr><tr><td headers="d492043e5698 d492043e5654" width="0%">fractionalSecondsPrecision</td></tr><tr><td headers="d492043e5698 d492043e5654" width="0%">yearPrecision</td></tr><tr><td headers="d492043e5698 d492043e5654" width="0%">dayPrecision</td></tr><tr><td headers="d492043e5652" width="0%">isPk</td><td headers="d492043e5734 d492043e5654" width="0%"></td><td headers="d492043e5734 d492043e5655" width="0%"></td><td headers="d492043e5734 d492043e5655" width="0%">✔</td><td headers="d492043e5734 d492043e5655" width="0%">✔</td></tr><tr><td headers="d492043e5652" width="0%">isUk</td><td headers="d492043e5743 d492043e5654" width="0%"></td><td headers="d492043e5743 d492043e5655" width="0%"></td><td headers="d492043e5743 d492043e5655" width="0%">✔</td><td headers="d492043e5743 d492043e5655" width="0%">✔</td></tr><tr><td headers="d492043e5652" width="0%">isFk</td><td headers="d492043e5752 d492043e5654" width="0%"></td><td headers="d492043e5752 d492043e5655" width="0%"></td><td headers="d492043e5752 d492043e5655" width="0%">✔</td><td headers="d492043e5752 d492043e5655" width="0%">✔</td></tr><tr><td headers="d492043e5652" width="0%">numDistinct</td><td headers="d492043e5761 d492043e5654" width="0%"></td><td headers="d492043e5761 d492043e5655" width="0%"></td><td headers="d492043e5761 d492043e5655" width="0%"></td><td headers="d492043e5761 d492043e5655" width="0%">✔</td></tr><tr><td headers="d492043e5652" width="0%">lowValue</td><td headers="d492043e5769 d492043e5654" width="0%"></td><td headers="d492043e5769 d492043e5655" width="0%"></td><td headers="d492043e5769 d492043e5655" width="0%"></td><td headers="d492043e5769 d492043e5655" width="0%">✔</td></tr><tr><td headers="d492043e5652" width="0%">highValue</td><td headers="d492043e5777 d492043e5654" width="0%"></td><td headers="d492043e5777 d492043e5655" width="0%"></td><td headers="d492043e5777 d492043e5655" width="0%"></td><td headers="d492043e5777 d492043e5655" width="0%">✔</td></tr><tr><td headers="d492043e5652" width="0%">density</td><td headers="d492043e5785 d492043e5654" width="0%"></td><td headers="d492043e5785 d492043e5655" width="0%"></td><td headers="d492043e5785 d492043e5655" width="0%"></td><td headers="d492043e5785 d492043e5655" width="0%">✔</td></tr><tr><td headers="d492043e5652" width="0%">avgColLen</td><td headers="d492043e5793 d492043e5654" width="0%"></td><td headers="d492043e5793 d492043e5655" width="0%"></td><td headers="d492043e5793 d492043e5655" width="0%"></td><td headers="d492043e5793 d492043e5655" width="0%">✔</td></tr><tr><td headers="d492043e5652" width="0%">hiddenColumn</td><td headers="d492043e5801 d492043e5654" width="0%"></td><td headers="d492043e5801 d492043e5655" width="0%"></td><td headers="d492043e5801 d492043e5655" width="0%"></td><td headers="d492043e5801 d492043e5655" width="0%">✔</td></tr><tr><td headers="d492043e5652" width="0%">virtualColumn</td><td headers="d492043e5810 d492043e5654" width="0%"></td><td headers="d492043e5810 d492043e5655" width="0%"></td><td headers="d492043e5810 d492043e5655" width="0%"></td><td headers="d492043e5810 d492043e5655" width="0%">✔</td></tr><tr><td headers="d492043e5652" width="0%">identityColumn</td><td headers="d492043e5818 d492043e5654" width="0%"></td><td headers="d492043e5818 d492043e5655" width="0%"></td><td headers="d492043e5818 d492043e5655" width="0%"></td><td headers="d492043e5818 d492043e5655" width="0%">✔</td></tr><tr><td headers="d492043e5652" width="0%">encryptedColumn</td><td headers="d492043e5826 d492043e5654" width="0%"></td><td headers="d492043e5826 d492043e5655" width="0%"></td><td headers="d492043e5826 d492043e5655" width="0%"></td><td headers="d492043e5826 d492043e5655" width="0%">✔</td></tr></tbody></table>

**Note:** Certain fields are required based on the value of the `type` field. The following table lists the required fields for each `type` value.

| | | | — | — | | **Value of thetypeField** | **Corresponding Required Columns** | | `NUMBER` | `precision` and `scale` | | `FLOAT` | `precision` | | `VARCHAR2` | `size` and `sizeUnits` | | `RAW` | `size` | | `CHAR` | `size` and `sizeUnits` | | `NCHAR` | `size` | | `UROWID` | `size` | | `NVARCHAR2` | `size` | | `TIMESTAMP` or `TIMESTAMP WITH TIME ZONE` or `TIMESTAMP WITH LOCAL TIME ZONE` | `fractionalSecondsPrecision` | | `INTERVAL YEAR TO MONTH` | `yearPrecision` | | `INTERVAL DAY TO SECOND` | `yearPrecision` and `fractionalSecondsPrecision` |

**JSON Schema for COLUMN sub-object type at level BASIC**

```md
{
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "https://oracle.com/schema/
19.28/DBMS_DEVELOPER.GET_METADATA/BASIC/object_info/column",
    "title": "DBMS_DEVELOPER.GET_METADATA/BASIC/OBJECT_INFO/COLUMN",
    "description": "Information for column",
    "type": "object",
    "properties": {
        "name": {
            "description": "Column name",
            "type": "string"
        },
        "notNull": {
            "description": "Not null",
            "type": "boolean",
            "default": false
        },
        "default": {
            "description": "Default value",
            "anyOf": [
                {
                    "type": "string"
                },
                {
                    "type": "number"
                }
            ]
        },
        "dataType": {
            "description": "Datatype",
            "type": "object",
            "properties": {
                "type": {
                    "description": "dataType",
                    "type": "string"
                },
                "precision": {
                    "description": "precision",
                    "type": "integer",
                    "minimum": 1
                },
                "scale": {
                    "description": "scale",
                    "type": "integer",
                    "minimum": 0
                },
                "length": {
                    "description": "length",
                    "type": "integer",
                    "minimum": 0
                },
                "size": {
                    "description": "size",
                    "type": "integer",
                    "minimum": 1
                },
                "sizeUnits": {
                    "description": "varchar size units",
                    "type": "string",
                    "enum": [
                        "BYTE",
                        "CHAR"
                    ]
                },
                "fractionalSecondsPrecision": {
                    "description": "fractionalSecondsPrecision",
                    "type": "integer"
                },
                "yearPrecision": {
                    "description": "yearPrecision",
                    "type": "integer"
                },
                "dayPrecision": {
                    "description": "dayPrecision",
                    "type": "integer"
                }
            },
            "anyOf": [
                {
                    "if": {
                        "properties": {
                            "type": {
                                "const": "NUMBER"
                            }
                        }
                    },
                    "then": {
                        "required": [
                            "precision",
                            "scale"
                        ]
                    }
                },
                {
                    "if": {
                        "properties": {
                            "type": {
                                "const": "FLOAT"
                            }
                        }
                    },
                    "then": {
                        "required": [
                            "precision"
                        ]
                    }
                },
                {
                    "if": {
                        "properties": {
                            "type": {
                                "const": "VARCHAR2"
                            }
                        }
                    },
                    "then": {
                        "required": [
                            "length",
                            "sizeUnits"
                        ]
                    }
                },
                {
                    "if": {
                        "properties": {
                            "type": {
                                "const": "RAW"
                            }
                        }
                    },
                    "then": {
                        "required": [
                            "size"
                        ]
                    }
                },
                {
                    "if": {
                        "properties": {
                            "type": {
                                "const": "CHAR"
                            }
                        }
                    },
                    "then": {
                        "required": [
                            "length",
                            "sizeUnits"
                        ]
                    }
                },
                {
                    "if": {
                        "properties": {
                            "type": {
                                "const": "NCHAR"
                            }
                        }
                    },
                    "then": {
                        "required": [
                            "length"
                        ]
                    }
                },
                {
                    "if": {
                        "properties": {
                            "type": {
                                "const": "UROWID"
                            }
                        }
                    },
                    "then": {
                        "required": [
                            "size"
                        ]
                    }
                },
                {
                    "if": {
                        "properties": {
                            "type": {
                                "const": "NVARCHAR2"
                            }
                        }
                    },
                    "then": {
                        "required": [
                            "length"
                        ]
                    }
                },
                {
                    "if": {
                        "properties": {
                            "type": {
                                "enum": [
                                    "TIME",
                                    "TIME WITH TIMEZONE",
                                    "TIMESTAMP",
                                    "TIMESTAMP WITH TIME ZONE",
                                    "TIMESTAMP WITH LOCAL TIME ZONE"
                                ]
                            }
                        }
                    },
                    "then": {
                        "required": [
                            "fractionalSecondsPrecision"
                        ]
                    }
                },
                {
                    "if": {
                        "properties": {
                            "type": {
                                "const": "INTERVAL YEAR TO MONTH"
                            }
                        }
                    },
                    "then": {
                        "required": [
                            "yearPrecision"
                        ]
                    }
                },
                {
                    "if": {
                        "properties": {
                            "type": {
                                "const": "INTERVAL DAY TO SECOND"
                            }
                        }
                    },
                    "then": {
                        "required": [
                            "dayPrecision",
                            "fractionalSecondsPrecision"
                        ]
                    }
                }
            ]
        }
    },
    "required": [
        "name",
        "dataType",
        "notNull"
    ]
}
```

**JSON Schema for COLUMN sub-object type at level TYPICAL**

```md
{
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "https://oracle.com/schema/19.28/DBMS_DEVELOPER.GET_METADATA/TYPICAL/object_info/column",
    "title": "DBMS_DEVELOPER.GET_METADATA/TYPICAL/OBJECT_INFO/COLUMN",
    "description": "Information for column",
    "type": "object",
    "properties": {
        "name": {
            "description": "Column name",
            "type": "string"
        },
        "default": {
            "description": "Default value",
            "anyOf": [
                {
                    "type": "string"
                },
                {
                    "type": "number"
                }
            ]
        },
        "notNull": {
            "description": "Not null",
            "type": "boolean",
            "default": false
        },
        "dataType": {
            "description": "Datatype",
            "type": "object",
            "properties": {
                "type": {
                    "description": "dataType",
                    "type": "string"
                },
                "precision": {
                    "description": "precision",
                    "type": "integer",
                    "minimum": 1
                },
                "scale": {
                    "description": "scale",
                    "type": "integer",
                    "minimum": 0
                },
                "length": {
                    "description": "length",
                    "type": "integer",
                    "minimum": 0
                },
                "size": {
                    "description": "size",
                    "type": "integer",
                    "minimum": 1
                },
                "sizeUnits": {
                    "description": "varchar size units",
                    "type": "string",
                    "enum": [
                        "BYTE",
                        "CHAR"
                    ]
                },
                "fractionalSecondsPrecision": {
                    "description": "fractionalSecondsPrecision",
                    "type": "integer"
                },
                "yearPrecision": {
                    "description": "yearPrecision",
                    "type": "integer"
                },
                "dayPrecision": {
                    "description": "dayPrecision",
                    "type": "integer"
                }
            },
            "anyOf": [
                {
                    "if": {
                        "properties": {
                            "type": {
                                "const": "NUMBER"
                            }
                        }
                    },
                    "then": {
                        "required": [
                            "precision",
                            "scale"
                        ]
                    }
                },
                {
                    "if": {
                        "properties": {
                            "type": {
                                "const": "FLOAT"
                            }
                        }
                    },
                    "then": {
                        "required": [
                            "precision"
                        ]
                    }
                },
                {
                    "if": {
                        "properties": {
                            "type": {
                                "const": "VARCHAR2"
                            }
                        }
                    },
                    "then": {
                        "required": [
                            "length",
                            "sizeUnits"
                        ]
                    }
                },
                {
                    "if": {
                        "properties": {
                            "type": {
                                "const": "RAW"
                            }
                        }
                    },
                    "then": {
                        "required": [
                            "size"
                        ]
                    }
                },
                {
                    "if": {
                        "properties": {
                            "type": {
                                "const": "CHAR"
                            }
                        }
                    },
                    "then": {
                        "required": [
                            "length",
                            "sizeUnits"
                        ]
                    }
                },
                {
                    "if": {
                        "properties": {
                            "type": {
                                "const": "NCHAR"
                            }
                        }
                    },
                    "then": {
                        "required": [
                            "length"
                        ]
                    }
                },
                {
                    "if": {
                        "properties": {
                            "type": {
                                "const": "UROWID"
                            }
                        }
                    },
                    "then": {
                        "required": [
                            "size"
                        ]
                    }
                },
                {
                    "if": {
                        "properties": {
                            "type": {
                                "const": "NVARCHAR2"
                            }
                        }
                    },
                    "then": {
                        "required": [
                            "length"
                        ]
                    }
                },
                {
                    "if": {
                        "properties": {
                            "type": {
                                "enum": [
                                    "TIME",
                                    "TIME WITH TIMEZONE",
                                    "TIMESTAMP",
                                    "TIMESTAMP WITH TIME ZONE",
                                    "TIMESTAMP WITH LOCAL TIME ZONE"
                                ]
                            }
                        }
                    },
                    "then": {
                        "required": [
                            "fractionalSecondsPrecision"
                        ]
                    }
                },
                {
                    "if": {
                        "properties": {
                            "type": {
                                "const": "INTERVAL YEAR TO MONTH"
                            }
                        }
                    },
                    "then": {
                        "required": [
                            "yearPrecision"
                        ]
                    }
                },
                {
                    "if": {
                        "properties": {
                            "type": {
                                "const": "INTERVAL DAY TO SECOND"
                            }
                        }
                    },
                    "then": {
                        "required": [
                            "dayPrecision",
                            "fractionalSecondsPrecision"
                        ]
                    }
                }
            ]
        },
        "isPk": {
            "description": "Is Primary Key",
            "type": "boolean",
            "default": false
        },
        "isUk": {
            "description": "Is Unique Key",
            "type": "boolean",
            "default": false
        },
        "isFk": {
            "description": "Is Foreign Key",
            "type": "boolean",
            "default": false
        }
    },
    "required": [
        "name",
        "isPk",
        "isUk",
        "isFk",
        "dataType",
        "notNull"
    ]
}
```

**JSON Schema for COLUMN sub-object type at level ALL**

```md
{
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "https://oracle.com/schema/19.28/DBMS_DEVELOPER.GET_METADATA/ALL/object_info/column",
    "title": "DBMS_DEVELOPER.GET_METADATA/ALL/OBJECT_INFO/COLUMN",
    "description": "Information for column",
    "type": "object",
    "properties": {
        "name": {
            "description": "Column name",
            "type": "string"
        },
        "default": {
            "description": "Default value",
            "anyOf": [
                {
                    "type": "string"
                },
                {
                    "type": "number"
                }
            ]
        },
        "notNull": {
            "description": "Not null",
            "type": "boolean",
            "default": false
        },
        "dataType": {
            "description": "Datatype",
            "type": "object",
            "properties": {
                "type": {
                    "description": "dataType",
                    "type": "string"
                },
                "precision": {
                    "description": "precision",
                    "type": "integer",
                    "minimum": 1
                },
                "scale": {
                    "description": "scale",
                    "type": "integer",
                    "minimum": 0
                },
                "length": {
                    "description": "length",
                    "type": "integer",
                    "minimum": 0
                },
                "size": {
                    "description": "size",
                    "type": "integer",
                    "minimum": 1
                },
                "sizeUnits": {
                    "description": "varchar size units",
                    "type": "string",
                    "enum": [
                        "BYTE",
                        "CHAR"
                    ]
                },
                "fractionalSecondsPrecision": {
                    "description": "fractionalSecondsPrecision",
                    "type": "integer"
                },
                "yearPrecision": {
                    "description": "yearPrecision",
                    "type": "integer"
                },
                "dayPrecision": {
                    "description": "dayPrecision",
                    "type": "integer"
                }
            },
            "anyOf": [
                {
                    "if": {
                        "properties": {
                            "type": {
                                "const": "NUMBER"
                            }
                        }
                    },
                    "then": {
                        "required": [
                            "precision",
                            "scale"
                        ]
                    }
                },
                {
                    "if": {
                        "properties": {
                            "type": {
                                "const": "FLOAT"
                            }
                        }
                    },
                    "then": {
                        "required": [
                            "precision"
                        ]
                    }
                },
                {
                    "if": {
                        "properties": {
                            "type": {
                                "const": "VARCHAR2"
                            }
                        }
                    },
                    "then": {
                        "required": [
                            "length",
                            "sizeUnits"
                        ]
                    }
                },
                {
                    "if": {
                        "properties": {
                            "type": {
                                "const": "RAW"
                            }
                        }
                    },
                    "then": {
                        "required": [
                            "size"
                        ]
                    }
                },
                {
                    "if": {
                        "properties": {
                            "type": {
                                "const": "CHAR"
                            }
                        }
                    },
                    "then": {
                        "required": [
                            "length",
                            "sizeUnits"
                        ]
                    }
                },
                {
                    "if": {
                        "properties": {
                            "type": {
                                "const": "NCHAR"
                            }
                        }
                    },
                    "then": {
                        "required": [
                            "length"
                        ]
                    }
                },
                {
                    "if": {
                        "properties": {
                            "type": {
                                "const": "UROWID"
                            }
                        }
                    },
                    "then": {
                        "required": [
                            "size"
                        ]
                    }
                },
                {
                    "if": {
                        "properties": {
                            "type": {
                                "const": "NVARCHAR2"
                            }
                        }
                    },
                    "then": {
                        "required": [
                            "length"
                        ]
                    }
                },
                {
                    "if": {
                        "properties": {
                            "type": {
                                "enum": [
                                    "TIME",
                                    "TIME WITH TIMEZONE",
                                    "TIMESTAMP",
                                    "TIMESTAMP WITH TIME ZONE",
                                    "TIMESTAMP WITH LOCAL TIME ZONE"
                                ]
                            }
                        }
                    },
                    "then": {
                        "required": [
                            "fractionalSecondsPrecision"
                        ]
                    }
                },
                {
                    "if": {
                        "properties": {
                            "type": {
                                "const": "INTERVAL YEAR TO MONTH"
                            }
                        }
                    },
                    "then": {
                        "required": [
                            "yearPrecision"
                        ]
                    }
                },
                {
                    "if": {
                        "properties": {
                            "type": {
                                "const": "INTERVAL DAY TO SECOND"
                            }
                        }
                    },
                    "then": {
                        "required": [
                            "dayPrecision",
                            "fractionalSecondsPrecision"
                        ]
                    }
                }
            ]
        },
        "isPk": {
            "description": "Is Primary Key",
            "type": "boolean",
            "default": false
        },
        "isUk": {
            "description": "Is Unique Key",
            "type": "boolean",
            "default": false
        },
        "isFk": {
            "description": "Is Foreign Key",
            "type": "boolean",
            "default": false
        },
        "numDistinct": {
            "description": "The number of distinct values in the column",
            "type": "integer"
        },
        "lowValue": {
            "description": "The low value in the column",
            "type": "string"
        },
        "highValue": {
            "description": "The high value in the column",
            "type": "string"
        },
        "density": {
            "description": "The average length of the column in bytes",
            "type": "integer"
        },
        "avgColLen": {
            "description": "The number of distinct values in the column",
            "type": "integer"
        },
        "hiddenColumn": {
            "description": "Indicates whether the column is a hidden column",
            "type": "boolean"
        },
        "virtualColumn": {
            "description": "Indicates whether the column is a virtual column",
            "type": "boolean"
        }
        "identityColumn": {
            "description": "Indicates whether the column is a identity column",
            "type": "boolean"
        },
        "encryptedColumn": {
            "description": "Indicates whether the column is a encrypted column",
            "type": "boolean"
        }
    },
    "required": [
         "name",
         "isPk",
         "isUk",
         "isFk",
         "dataType",
         "notNull",
         "hiddenColumn",
         "virtualColumn",
         "identityColumn",
         "encryptedColumn"
    ]
}
```

### JSON Schema for Sub-Object Type: constraints

JSON schema for the sub-object `constraints` for the levels: `typical` and `all`.

**JSON Schema for constraints Sub-Object Type in Tabular Form**

Table 6 JSON Schema for Sub-Object Type: CONSTRAINTS

| Fields |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | BASIC | TYPICAL | ALL |
| name |  |  | ✔ | ✔ |
| constraintType |  |  | ✔ | ✔ |
| searchCondition |  |  | ✔ | ✔ |
| columns | name |  | ✔ | ✔ |
| referencedConstraintName |  |  | ✔ | ✔ |
| referencedTable |  |  | ✔ | ✔ |
| action |  |  | ✔ | ✔ |
| referencedOwner |  |  | ✔ | ✔ |
| referencedColumns | name |  | ✔ | ✔ |
| status |  |  | ✔ | ✔ |
| deferrable |  |  | ✔ | ✔ |
| validated |  |  | ✔ | ✔ |
| sysGeneratedName |  |  | ✔ | ✔ |

**Note:** If the `constraintType` is set to \`REFERENTIAL

```md
INTEGRITY\`, the following fields are required in the schema: \`referencedConstraintName\`,\`referencedOwner\`, \`referencedTable\`, and \`referencedColumns\`.
{: .infoboxnote}
```

**JSON Schema for CONSTRAINT sub-object type at level TYPICAL**

**Note:** Constraint schema is not available for the `BASIC level`.

```md
{
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "https://oracle.com/schema/23.10/DBMS_DEVELOPER.GET_METADATA/TYPICAL/object_info/constraint",
    "title": "DBMS_DEVELOPER.GET_METADATA/TYPICAL/OBJECT_INFO/CONSTRAINT",
    "description": "Information for constraint",
    "type": "object",
    "properties": {
        "name": {
            "description": "Constraint name",
            "type": "string"
        },
        "constraintType": {
            "description": "Type of constraint definition: CHECK, CHECK - NOT NULL, PRIMARY KEY, UNIQUE,
                            REFERENTIAL INTEGRITY, VIEW CHECK, VIEW READONLY",
            "type": "string"
        },
        "searchCondition": {
            "description": "Text of search condition for a check constraint",
            "type": "string"
        },
        "columns": {
            "description": "Table columns",
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "name": {
                        "description": "Name associated with column or attribute of object column
                                        specified in the constraint definition",
                        "type": "string"
                    }
                }
            }
        },
        "referencedConstraintName": {
            "description": "Name of unique constraint definition for Referenced table",
            "type": "string"
        },
        "referencedTable": {
            "description": "Name of table used in referential constraint",
            "type": "string"
        },
        "action": {
            "description": "On delete rule",
            "type": {
                "enum": [
                    "RESTRICT",
                    "CASCADE",
                    "SET NULL",
                    "SET DEFAULT"
                ]
            }
        },
        "referencedOwner": {
            "description": "Owner of table used in referential constraint",
            "type": "string"
        },
        "referencedColumns": {
            "description": "Referenced table columns",
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "name": {
                        "description": "Referenced table column name",
                        "type": "string"
                    }
                }
            }
        },
        "status": {
            "description": "Constraint status",
            "type": {
                "enum": [
                    "ENABLED",
                    "DISABLED"
                ]
            }
        },
        "deferrable": {
            "description": "Deferrable",
            "type": "boolean",
            "default": false
        },
        "validated": {
            "description": "Validated",
            "type": {
                "enum": [
                    "VALIDATED",
                    "NOT VALIDATED"
                ]
            }
        },
        "sysGeneratedName": {
            "description": "System Generated constraint",
            "type": "boolean"
        }
    },
    "required": [
        "name",
        "constraintType",
        "status",
        "deferrable",
        "validated",
        "sysGeneratedName"
    ],
    "if": {
        "properties": {
            "constraintType": {
                "const": "REFERENTIAL INTEGRITY"
             }
         }
    },
    "then": {
        "required": [
            "referencedConstraintName",
             "referencedOwner",
             "referencedTable",
             "referencedColumns"
         ]
    }
}
```

**JSON Schema for CONSTRAINT sub-object type at level ALL**

```md
{
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "https://oracle.com/schema/23.10/DBMS_DEVELOPER.GET_METADATA/ALL/object_info/constraint",
    "title": "DBMS_DEVELOPER.GET_METADATA/ALL/OBJECT_INFO/CONSTRAINT",
    "description": "Information for constraint",
    "type": "object",
     "properties": {
        "name": {
            "description": "Constraint name",
            "type": "string"
        },
        "constraintType": {
            "description": "Type of constraint definition",
            "type": "string"
        },
        "searchCondition": {
            "description": "Text of search condition for a check constraint",
            "type": "string"
        },
        "columns": {
            "description": "Table columns",
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "name": {
                        "description": "Name associated with column or attribute of object column
                                        specified in the constraint definition",
                        "type": "string"
                    },
                    "position": {
                        "description": "Original position of column or attribute in definition",
                        "type": "integer"
                    }
                }
            }
        },
        "referencedConstraintName": {
            "description": "Name of unique constraint definition for Referenced table",
            "type": "string"
        },
        "referencedTable": {
            "description": "Name of table used in referential constraint",
            "type": "string"
        },
        "action": {
            "description": "On delete rule",
            "type": {
                "enum": [
                     "RESTRICT",
                     "CASCADE",
                     "SET NULL",
                     "SET DEFAULT"
                ]
            }
        },
        "referencedOwner": {
            "description": "Owner of table used in referential constraint",
            "type": "string"
        },
        "referencedColumns": {
            "description": "Referenced table columns",
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "name": {
                        "description": "Referenced table column name",
                        "type": "string"
                    },
                    "position": {
                        "description": "Original position of column or attribute in definition",
                        "type": "integer"
                    }
                }
            }
        },
        "status": {
            "description": "Constraint status",
            "type": {
                "enum": [
                    "ENABLED",
                    "DISABLED"
                ]
            }
        },
        "deferrable": {
            "description": "Deferrable",
            "type": "boolean",
            "default": false
        },
        "validated": {
            "description": "Validated",
            "type": {
                "enum": [
                    "VALIDATED",
                    "NONVALIDATED"
                ]
            }
        },
        "sysGeneratedName": {
            "description": "System Generated constraint",
            "type": "boolean"
        }
    },
    "required": [
         "name",
         "constraintType"
    ],
    "if": {
         "properties": {
              "constraintType": {
                    "const": "REFERENTIAL INTEGRITY"
               }
          }
    },
    "then": {
         "required": [
              "referencedConstraintName",
              "referencedOwner",
              "referencedTable",
              "referencedColumns"
         ]
    }
}
```