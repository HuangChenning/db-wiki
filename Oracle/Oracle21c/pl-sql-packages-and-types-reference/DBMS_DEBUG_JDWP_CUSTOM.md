---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/DBMS_DEBUG_JDWP_CUSTOM.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 64 DBMS\_DEBUG\_JDWP\_CUSTOM

The `DBMS_DEBUG_JDWP_CUSTOM` package provides database users a means to perform custom handling of a debug connection request of a database session to a debugger using the Java Debug Wire Protocol (JDWP).

This chapter contains the following topics:

### 64.1 DBMS\_DEBUG\_JDWP\_CUSTOM Overview

`DBMS_DEBUG_JDWP_CUSTOM` package is invoked when you attempt to connect your database session to a debugger, using the Java Debug Wire Protocol (JDWP). Before connecting to the database, you must set the `ORA_DEBUG_JDWP` environment variable in your client-side OCI application. Defining this package in your schema enables you to perform custom actions before connecting your database session to the debugger.

### 64.2 DBMS\_DEBUG\_JDWP\_CUSTOM Security Model

This default implementation of the `DBMS_DEBUG_JDWP_CUSTOM` package does not perform any additional security checks and only invokes the `DBMS_DEBUG_JDWP` package for making the debug connection. When the `DBMS_DEBUG_JDWP` package is invoked, it checks for the necessary `DEBUG CONNECT` system or user privilege before making the connection.

A database user who wants to perform additional custom security checks, must perform the following steps to override this default implementation:

- Define the `DBMS_DEBUG_JDWP_CUSTOM` package in the user's own schema.
- Implement the check before invoking the `DBMS_DEBUG_JDWP` package in the user's local copy of the package.

### 64.3 Summary DBMS\_DEBUG\_JDWP\_CUSTOM Subprograms

This table summarizes the DBMS\_DEBUG\_JDWP\_CUSTOM subprograms.

Table 64-1 DBMS\_DEBUG\_JDWP\_CUSTOM Subprograms

| Subprogram | Description |
| --- | --- |
| CONNECT\_DEBUGGER Procedure | This procedure is invoked to handle the debug connection request of the current database session to the debugger. |

#### 64.3.1 CONNECT\_DEBUGGER Procedure

This procedure is invoked to handle the debug connection request of the current database session to the debugger.

Syntax

```
PROCEDURE CONNECT_DEBUGGER
(
   HOST                VARCHAR2,
   PORT                VARCHAR2,
   DEBUG_ROLE          VARCHAR2 := NULL,
   DEBUG_ROLE_PWD      VARCHAR2 := NULL,
   OPTION_FLAGS        PLS_INTEGER := 0,
   EXTENSIONS_CMD_SET  PLS_INTEGER := 128
)
```

Parameters

The preceding parameters are for the default implementation of the procedure for handling the debug connection request. A user, who wants to customize the handling of the request, must override this default implementation of the `DBMS_DEBUG_JDWP_CUSTOM` package procedure by defining the package (specification and body) with a procedure of the same name in the user's own schema. The user may customize the number and names of the arguments, but must have the same name for the package and the procedure, namely, `DBMS_DEBUG_JDWP_CUSTOM` and `CONNECT_DEBUGGER` respectively. The user's customized version of the package may contain overloaded versions of the `CONNECT_DEBUGGER` procedure with different arguments. All of the arguments to the custom package procedure must either be of VARCHAR2 type or of types that PL/SQL can implicitly convert from VARCHAR2.

For example, if a user wants to disallow debugging outside business hours, while applying optional NLS settings to the program values displayed during debugging, then the user can define a custom implementation of the package in the user's schema in the following way:

```
CREATE OR REPLACE PACKAGE DBMS_DEBUG_JDWP_CUSTOM AUTHID CURRENT_USER IS
  PROCEDURE CONNECT_DEBUGGER(HOST VARCHAR2,
                             PORT VARCHAR2,
                             NLS_LANGUAGE VARCHAR2 DEFAULT NULL,
                             NLS_TERRITORY VARCHAR2 DEFAULT NULL);
END;
/

CREATE OR REPLACE PACKAGE BODY DBMS_DEBUG_JDWP_CUSTOM IS

  PROCEDURE CONNECT_DEBUGGER(HOST VARCHAR2,
                             PORT VARCHAR2,
                             NLS_LANGUAGE VARCHAR2 DEFAULT NULL,
                             NLS_TERRITORY VARCHAR2 DEFAULT NULL) IS
  BEGIN
    SELECT EXTRACT(HOUR FROM LOCALTIMESTAMP) INTO HOUR FROM DUAL;
    IF (HOUR < 9 OR HOUR > 5) THEN
      RAISE_APPLICATION_ERROR(-20000,
        'Debug connection disallowed outside business hours');
    ELSE
      IF (NLS_LANGUAGE IS NOT NULL) THEN
        DBMS_DEBUG_JDWP.SET_NLS_PARAMETER('NLS_LANGUAGE', NLS_LANGUAGE);
      END IF;
      IF (NLS_TERRITORY IS NOT NULL) THEN
        DBMS_DEBUG_JDWP.SET_NLS_PARAMETER('NLS_TERRITORY', NLS_TERRITORY);
      END IF;
      DBMS_DEBUG_JDWP.CONNECT_TCP(HOST, PORT);
    END IF;
  END;

END;
/
```

Before executing the client application for passing arguments to the procedure parameters, the user must set the `ORA_DEBUG_JDWP` environment variable as follows:

```
> setenv ORA_DEBUG_JDWP "host=123.45.67.89;port=4000;nls_language=american"
> myapp -user HR/<password>
...
```