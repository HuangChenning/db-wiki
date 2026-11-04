---
title: "Cartridge Services Using C, C++ and Java"
book: "Data Cartridge Developer's Guide"
doc_id: E10765-02
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e10765/serv_c_java_ref.htm
tags:
  - oracle
  - 11g
  - data-cartridge-developers-guide
---

## 18 Cartridge Services Using C, C++ and Java

This reference chapter describes cartridge services available to programmers using C/C++ and Java.

This chapter contains these topics:

See Also:

[Oracle Call Interface Programmer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e10646/oci20ext.htm#LNOCI190) for more details on cartridge services using C

## OCI Access Functions for External Procedures

When called from an external procedure, a service routine can raise exceptions, allocate memory, and get OCI handles for callbacks to the server. To use the functions, you must specify the `WITH` `CONTEXT` clause, which lets you pass a context structure to the external procedure. The context structure is declared in header file `ociextp.h` as follows:

```
typedef struct OCIExtProcContext OCIExtProcContext;
```

This section describes how service routines use the context information. For more information and examples of usage, see the chapter on external procedures in the [Oracle Database Advanced Application Developer's Guide.](https://docs.oracle.com/cd/E11882_01/appdev.112/e41502/toc.htm)

### OCIExtProcAllocCallMemory

This service routine allocates n bytes of memory for the duration of the external procedure call. Any memory allocated by the function is freed as soon as control returns to PL/SQL.

Note:

Do not use any other function to allocate or free memory.

The C prototype for this function follows:

```
void *OCIExtProcAllocCallMemory(
   OCIExtProcContext *with_context, 
   size_t amount);
```

The parameters with\_context and amount are the context pointer and number of bytes to allocate, respectively. The function returns an untyped pointer to the allocated memory. A return value of zero indicates failure.

### OCIExtProcRaiseExcp

This service routine raises a predefined exception, which must have a valid Oracle error number in the range `1` to `32767`. After doing any necessary cleanup, the external procedure must return immediately. (No values are assigned to `OUT` or `IN` `OUT` parameters.) The C prototype for this function follows:

```
int OCIExtProcRaiseExcp(
   OCIExtProcContext *with_context, 
   size_t error_number);
```

The parameters with\_context and error\_number are the context pointer and Oracle error number. The return values `OCIEXTPROC_SUCCESS` and `OCIEXTPROC_ERROR` indicate success or failure.

### OCIExtProcRaiseExcpWithMsg

This service routine raises a user-defined exception and returns a user-defined error message. The C prototype for this function follows:

```
int OCIExtProcRaiseExcpWithMsg(
   OCIExtProcContext *with_context, 
   size_t error_number,
   text   *error_message, 
   size_t  len);
```

The parameters `with_context`, `error_number`, and `error_message` are the context pointer, Oracle error number, and error message text. The parameter len stores the length of the error message. If the message is a null-terminated string, len is zero. The return values `OCIEXTPROC_SUCCESS` and `OCIEXTPROC_ERROR` indicate success or failure.

### OCIExtProcGetEnv

This service routine enables OCI callbacks to the database during an external procedure call. Use the OCI handles obtained by this function only for callbacks. If you use them for standard OCI calls, the handles establish a new connection to the database and cannot be used for callbacks in the same transaction. In other words, during an external procedure call, you can use OCI handles for callbacks or a new connection but not for both.

The C prototype for this function follows:

```
sword OCIExtProcGetEnv(
   OCIExtProcContext *with_context, 
   OCIEnv    **envh, 
   OCISvcCtx **svch, 
   OCIError  **errh);
```

The parameter with\_context is the context pointer, and the parameters envh, svch, and errh are the OCI environment, service, and error handles, respectively. The return values `OCIEXTPROC_SUCCESS` and `OCIEXTPROC_ERROR` indicate success or failure.

["Doing Callbacks"](c_cpp_java.md) shows how `OCIExtProcGetEnv` might be used in callbacks. For a working example, see the script extproc.sql in the PL/SQL demo directory. (For the location of this directory, see your Oracle installation or user's guide.) This script demonstrates the calling of an external procedure. The companion file extproc.c contains the C source code for the external procedure. To run the demo, follow the instructions in `extproc`.`sql`. You must use an account that has `CREATE` `LIBRARY` privileges.

## Installing Java Cartridge Services Files

The `ODCI.jar` and `CartridgeServices.jar` files must be installed into the `SYS` schema to use the Java classes described in this chapter.

If you installed the Java option, then you must install the `ODCI.jar` and `CartridgeServices.jar` files. You do not have to perform this task if you did not install the Java option.

To install ODCI.jar and CartridgeServices.jar files

1. Activate the SQL\*Plus prompt.
	```
	C:\sqlplus
	```
2. When prompted, login using the `system` account.
	```
	Enter user-name: system
	Enter password: password
	```
3. Use the server-side loadjava command to install the classes and create the synonyms in the `SYSTEM` schema.
	```
	SQL> call dbms_java.loadjava('-resolve -synonym -grant public 
	     -verbose vobs/jilip/Cartridge Services.jar');
	SQL> call dbms_java.loadjava('-resolve -synonym -grant public
	     -verbose vobs/jlib/ODCI.jar');
	```

See the chapter on what to do after migrating or updating the database, in [Oracle Database Upgrade Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23633/toc.htm), for further details on installing the `jar` files.

## Cartridge Services-Maintaining Context

The Java cartridge service is used for maintaining context. It is similar to the OCI context management service. This class is necessary when switching context between the server and the cartridge code.

### ContextManager

ContextManager is a Constructor in class Oracle that extends Object.

Class Interface

```
public static Hashtable ctx extends Object
```

Variable

```
ctx public static Hashtable ctx
```

Constructors

```
ContextManager public ContextManager()
```

Methods

The following methods are available:

```
setContext (static method in class oracle)
getContext (static method in class oracle)
clearContext (static method in class oracle)
```

### CountException()

Constructor that extends `Exception`.

```
Class oracle.CartridgeServices.CountException
```

### CountException(String)

Constructor that extends `Exception`.

```
public CountException(String s)
```

### InvalidKeyException()

Constructor that extends `Exception`.

```
public InvalidKeyException(String s)
```

### InvalidKeyException(String)

Constructor that extends `Exception`.

```
public InvalidKeyException(String s)
```