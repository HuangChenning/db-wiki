---
title: Using Cartridge Services
book: "Data Cartridge Developer's Guide"
doc_id: E10765-02
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e10765/cart_services.htm
tags:
  - oracle
  - 11g
  - data-cartridge-developers-guide
---

## 12 Using Cartridge Services

This chapter describes how to use cartridge services.

This chapter contains these topics:

## Introduction to Cartridge Services

This chapter describes a set of services that help you create data cartridges in the Oracle Extensibility framework.

Using Oracle Cartridge Services offers you the following advantages:

Portability

Oracle Cartridge Services offers you the flexibility to work across different machine architectures

Flexibility Within Oracle Environments

Another type of flexibility is offered to you in terms of the fact that all cartridge services work with your Oracle Database, irrespective of the configuration of operations that has been purchased by your client.

Language Independence

The use of the Globalization Support services lets you internationalize your cartridge. Language independence means that you can have different instances of your cartridge operating in different language environments.

Tight Integration with the Server

Various cartridge services have been designed to facilitate access with Oracle ORDBMS. This offers far superior performance to client -side programs attempting to perform the same operations.

Guaranteed Compatibility

Oracle Database is a rapidly evolving technology and it is likely that your clients might be operating with different releases of Oracle. The cartridge services operate with all versions of Oracle Database.

Integration of Different Cartridges

The integration of cartridge services lets you produce a uniform integration of different data cartridges.

The following sections provide a brief introduction to the set of services that you can use as part of your data cartridge. The APIs that describe these interfaces are in [Chapter 18, "Cartridge Services Using C, C++ and Java"](serv_c_java_ref.md)

## Cartridge Handle

Cartridge services require various handles that are encapsulated inside two types of OCI handles:

Environment Handle

The environment handle is either `OCIEnv` or `OCI_HTYPE_ENV`. Various cartridge services are required at the process level when no session is available. The `OCIInitialize` () should use the `OCI_OBJECT` option for cartridge service.

User Session handle

The user session handle is either `OCISession` or `OCI_HTYPE_SESSION`. In a callout, the services can be used when the handle is allocated even without opening a connection back to the database.

All cartridge service calls take a `void` `*` OCI handle as one of the arguments that may be either an environment or a session handle. While most service calls are allowed with either of the handles, certain calls may not be valid with one of the handles. For example, it may be an error to allocate `OCI_DURATION_SESSION` with an environment handle. An error is typically returned in an error handle.

### Client Side Usage

Most of the cartridge service can also be used on the client side code. Refer to individual services for restrictions. To use cartridge service on the client side, the OCI environment has to be initialized with `OCI_OBJECT` option. This is automatically effected in a cartridge.

### Cartridge Side Usage

Most of the services listed in this document can be used in developing a database cartridge, but please refer to documentation of each individual service for restrictions. New service calls are available to obtain the session handle in a callout. The session handle is available without opening a connection back to the server.

### Service Calls

Before using any service, the OCI environment handle must be initialized. All the services take an OCI environment (or user\_session) handle as an argument. Errors are returned in an OCI error handle. The sub handles required for various service calls are not allocated along with the OCI environment handle. Services which must initialize an environment provide methods to initialize it. Example 12-1 demonstrates the initialization of these handles.

Example 12-1 Initializing OCI Handles

```
{
  OCIEnv *envhp;
  OCIError *errhp;
  (void) OCIInitialize(OCI_OBJECT, (dvoid *)0, 0, 0, 0);
  (void) OCIEnvInit(&envhp, OCI_OBJECT, (size_t)0, (dvoid **)0);
  (void) OCIHandleAlloc((dvoid *)envhp, (dvoid **)errhp,   OCI_HTYPE_ERROR, 
      (size_t)0, (dvoid **)0);
  /* ... use the handles ... */
  (void) OCIHandleFree((dvoid *)errhp, OCI_HTYPE_ERROR);
}
```

### Error Handling

Routines that return errors generally return `OCI_SUCCESS` or `OCI_ERROR`. Some routines may return `OCI_SUCCESS_WITH_INFO`, `OCI_INVALID_HANDLE`, or `OCI_NO_DATA`. If `OCI_ERROR` or `OCI_SUCCESS_WITH_INFO` is returned, then an error code, an error facility, and possibly an error message can be retrieved by calling `OCIErrorGet`, as demonstrated in Example 12-2.

Example 12-2 Retrieving Error Information Using OCIErrorGet()

```
{
  OCIError *errhp;
  ub4 errcode;
  text buffer[512];
  (void) OCIErrorGet((dvoid *)errhp, 1, (text *)NULL, &errcode, buffer,
      sizeof(buffer), OCI_HTYPE_ERROR);
}
```

## Memory Services

The memory service allows the client to allocate or free memory chunks. Each memory chunk is associated with a duration. This allows clients to automatically free all memory associated with a duration (at the end of the duration). The duration determines the heap that is used to allocate the memory. The memory service predefines three kinds of durations: call (`OCI_DURATION_CALL`), statement (`OCI_DURATION_STATEMENT`) and session (`OCI_DURATION_SESSION`).

The client can also create a user duration. The client has to explicitly start and terminate a user duration. Thus, the client can control the length of a user duration. Like the predefined durations, a user duration can be used to specify the allocation duration (for example, memory chunks are freed at the end of the user duration).

Each user duration has a parent duration. A user duration terminates implicitly when its parent duration terminates. A parent duration can be call, statement, transaction, session or any other user duration. Memory allocated in the user duration comes from the heap of its parent duration.

The Oracle RDBMS memory manager supports a variety of memory models. Currently callouts support memory for the duration of that callout. With the extension of row sources to support external indexing, there is a need for memory of durations greater than a callout.

The following functionality is supported:

- Allocate (permanent and friable) memory of following durations
	- call to agent process
		- statement
		- session
		- shared attributes (metadata) for cartridges
- Ability to re-allocate memory
- Ability to create a subduration memory, a sub heap which gets freed up when the parent heap gets freed up. Memory for this sub heap can be allocated and freed.
- Ability to specify zeroed memory
- Ability to allocate large contiguous memory

## Maintaining Context

Context management allows the clients to store values across calls. Cartridge services provide a mechanism for saving and restoring context.

Most operating systems that support threads have the concept of thread context. Threads can store thread specific data in this context (or state) and retrieve it at any point. This provides a notion of thread global variable. Typically a pointer which points to the root of a structure is stored in the context.

When the row source mechanism is externalized, you must have a mechanism to maintain state between multiple calls to the same row source.

You must maintain session, statement and process states. Session state includes information about multiple statements that are open, message files based on sessions' Globalization Support settings, and so on. Process state includes shared metadata (including systemwide metadata), message files, and so on. Depending on whether the cartridge application is truly multi threaded, information sharing can be at a process level or system level.

Since a user can be using multiple cartridges at any time, the state must be maintained for each cartridge. This is done by requiring the user to supply a key for each duration.

### Durations

There are various predefined types of durations supported on memory and context management calls. An additional parameter in all these calls is a context.

- `OCI_DURATION_CALL`. The duration of this operation is that of a callout.
- `OCI_DURATION_STATEMENT`. The duration of this operation is the external row source.
- `OCI_DURATION_SESSION`. The duration of this operation is the user session.
- `OCI_DURATION_PROCESS`. The duration of this is agent process.

## Globalization Support

To support multilingual application, Globalization Support functionality is required for cartridges and callouts. `NLSRTL` is a multiplatform, multilingual library current used in RDBMS and provides consistent Globalization Support behavior to all Oracle products.

Globalization Support basic services provide the following language and cultural sensitive functionality:

- Locale information retrieval.
- String manipulation in the format of multibyte and wide-char.
- Character set conversion including Unicode support.
- Messaging mechanism.

### Globalization Support Language Information Retrieval

An Oracle locale consists of language, territory and character set definitions. The locale determines conventions such as native day and month names; and date, time, number, and currency formats. An internationalized application obeys a user's locale setting and cultural convention. For example, in a German locale setting, users expect to see day and month names in German spelling. The following interface provides a simple way to retrieve local sensitive information.

### String Manipulation

Two types of data structure are supported for string manipulation: multibyte string and wide char string. Multibyte string is in native Oracle character set encoding, and functions operated on it take the string as a whole unit. Wide char string function provides more flexibility in string manipulation and supports character-based and string-based operations.

The wide char data type we use here is Oracle-specific and not to be confused with the `wchar_t` defined by the ANSI/ISO C standard. The Oracle wide char is always 4 bytes in all the platforms, while `wchar_t` is dependent on the implementation and platform. The idea of Oracle wide char is to normalize multibyte characters to have a fixed-width for easy processing. Round-trip conversion between Oracle wide char and native character set is guaranteed.

The string manipulation can be classified into the following categories:

- Conversion of string between multibyte and wide char.
- Character classifications.
- Case conversion.
- Display length calculation.
- General string manipulation, such as compare, concatenation and searching.

## Parameter Manager Interface

The parameter manager provides a set of routines to process parameters from a file or a string. Routines are provided to process the input and to obtain key and value pairs. These key and value pairs are stored in memory and routines are provided which can access the values of the stored parameters.

The input processing routines match the contents of the file or the string against an existing grammar and compare the key names found in the input against the list of known keys that the user has registered. The behavior of the input processing routines can be configured depending on the bits that are set in the flag argument.

The parameters can be retrieved either one at a time, or all at the same time by calling a function that iterates over the stored parameters.

### Input Processing

Parameters consist of a key, or parameter name, type, and a value and must be specified by the format `key` `=` `value`.

Parameters can optionally accept lists of values which may be surrounded by parentheses, either as `key` `= (``value1``, ...,` `valuen`) or as `key` `=` `value1``, ...,` `valuen`.

A value can be a string, integer, `OCINumber`, or Boolean. A boolean value starting with ' `y` ' or ' `t` ' maps to `TRUE` and a boolean value starting with ' `n` ' or ' `f` ' maps to `FALSE`. The matching for boolean values is case insensitive.

The parameter manager views certain characters as special characters which are not parsed literally. The special characters and their meanings are indicated in Table 12-1.

Table 12-1 Special Characters

| Character | Description |
| --- | --- |
| `#` | Comment (only for files) |
| `(` | Start a list of values |
| `)` | End a list of values |
| `"` | Start or end of quoted string |
| `'` | Start or end of quoted string |
| `=` | Separator of keyword and value |
| `\` | Escape character |

If a special character must be treated literally, then it must either be prefaced by the escape character or the entire string must be surrounded by single or double quotes.

A key string can contain alphanumeric characters only. A value can contain any characters. However, the value cannot contain special characters unless they are quoted or escaped.

### Parameter Manager Behavior Flag

The routines to process a file or a string use a behavior flag that alters default characteristics of the parameter manager. These bits can be set in the flag:

- `OCI_EXTRACT_CASE_SENSITIVE`. All comparisons are case sensitive. The default is to use case insensitive comparisons.
- `OCI_EXTRACT_UNIQUE_ABBREVS`. Unique abbreviations are allowed for keys. The default is that unique abbreviations are not allowed.
- `OCI_EXTRACT_APPEND_VALUES`. If a value or values are stored for a particular key, then any new values for this key should be appended. The default is to return an error.

### Key Registration

Before invoking the input processing routines (`OCIExtractFromFile()` or `OCIExtractFromString()`, all of the keys must be registered by calling `OCIExtractSetNumKeys()` followed by `OCIExtractSetKey()`, which requires:

- Name of the key
- Type of the key (`integer`, `string`, `boolean`, `OCINumber`)
- `OCI_EXTRACT_MULTIPLE` is set for the flag value if multiple values are allowed (default: only one value allowed)
- Default value to be used for the key (may be `NULL`)
- Range of allowable integer values specified by starting and ending values, inclusive (may be `NULL`)
- List of allowable string values (may be `NULL`)

### Parameter Storage and Retrieval

The results of processing the input into a set of keys and values are stored. The validity of the parameters is checked before storing the parameters in memory. The values are checked to see if they are of the proper type. In addition, if you wish, the values can be checked to see if they fall within a certain range of integer values or are members of a list of enumerated string values. Also, if you do not specify that a key can accept multiple values, then an error is returned if a key is specified more than one time in a particular input source. Also, an error is returned if the key is unknown. Values of keys can be retrieved when processing is completed, using specific routines for retrieving string, integer, `OCINumber`, or boolean values.

It is possible to retrieve all parameters at the same timr. The function `OCIExtractToList()` must first be called to generate a list of parameters that is created from the parameter structures stored in memory. `OCIExtractToList()` returns the number of unique keys stored in memory, and then `OCIExtractFromList()` can be called to return the list of values associated with each key.

### Parameter Manager Context

The parameter manager maintains its own context within the `OCI` environment handle. This context stores all the processed parameter information and some internal information. It must be initialized with a call to `OCIExtractInit()` and cleaned up with a call to `OCIExtractTerm()`.

## File I/O

The OCI file I/O package is designed to make it easier for you to write portable code that interacts with the file system by providing a consistent view of file I/O across multiple platforms.

You must be aware of two issues when using this package in a data cartridge environment. The first issue is that this package does not provide any security when opening files for writing or when creating new files in a directory other than the security provided by the operating system protections on the file and directory. The second issue is that this package does not support the use of file descriptors across calls in a multithreaded server environment.

## String Formatting

The OCI string formatting package facilitates writing portable code that handles string manipulation by means of the `OCIFormatString()` routine. This is an improved and portable version of `sprintf` that incorporates additional functionality and error checking that the standard `sprintf` does not. This additional functionality includes:

- Arbitrary argument selection.
- Variable width and precision specification.
- Length checking of the buffer.
- Oracle Globalization Support for internationalization.