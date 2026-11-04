---
title: Upgrading Applications After Upgrading Oracle Database
book: Upgrade Guide
doc_id: E23633-11
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e23633/app.htm
tags:
  - oracle
  - 11g
  - upgrade-guide
---

## 5 Upgrading Applications After Upgrading Oracle Database

Many new features and enhancements are available after upgrading to a new release of Oracle Database. To take advantage of the new features, you must upgrade applications running in the new release.

This chapter contains the following topics:

## Overview of Upgrading Applications

You are not required to modify existing applications that do not use features available in the new Oracle Database 11g release. Existing applications running against a new Oracle Database 11g database function the same as they did in prior releases and achieve the same, or enhanced, performance.

Many new features and enhancements are available after upgrading to the new Oracle Database 11g release. Some of these features provide added features and functions, while others provide improved performance. Before you upgrade your applications, you should review these new features to decide which ones you want to use.

See Also:

[Oracle Database New Features Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41360/toc.htm) for information about the features available in the new Oracle Database 11g release

## Compatibility Issues for Applications When Upgrading

There might be compatibility issues between different releases of Oracle Database that could affect your applications. These compatibility issues result from differences in Oracle Database in various releases. Also, in each new release of Oracle Database, new Oracle reserved words might be added, changes might be made to initialization parameters, and changes might be made to the data dictionary.

When you upgrade your Oracle Database software to a new release, make sure that your applications do not use any Oracle reserved words, that your applications are compatible with the initialization parameters of the database, and that your applications are compatible with the data dictionary of the database. Finally, a new release of Oracle Database software might require certain operating system releases or the application of certain patchsets.

See Also:

- [Appendix A, "Behavior Changes After Upgrading Oracle Database"](changes.md) for information about initialization parameter changes and data dictionary changes
- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/ap_keywd.htm#SQLRF022) for a complete list of Oracle reserved words
- Your operating system-specific Oracle documentation for information about operating system requirements

## Upgrading Precompiler and OCI Applications

The upgrade path is very similar for precompiler and OCI applications. This section guides you through your upgrade options for these applications and notes differences between precompiler and OCI applications whenever necessary.

Create a test environment before you upgrade your production environment. Your test environment should include your upgraded application and the new Oracle Database software. Also, your test environment should provide a realistic test of your application.

This section contains these topics:

- Understanding Software Upgrades and Your Client/Server Configuration
- Compatibility Rules for Applications When Upgrading Client/Server Software
- Upgrading Options for Your Precompiler and OCI Applications

See Also:

[Pro\*C/C++ Programmer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e10825/toc.htm), [Pro\*COBOL Programmer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e10826/toc.htm), and [Oracle Call Interface Programmer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e10646/toc.htm) for more information about using these programming environments.

### Understanding Software Upgrades and Your Client/Server Configuration

To understand your options for upgrading precompiler and OCI applications, you first must understand the type of software upgrade you are performing and your client/server configuration.

This section contains these topics:

- Types of Software Upgrades for Oracle Database
- Possible Client/Server Configurations

#### Types of Software Upgrades for Oracle Database

When you upgrade Oracle Database, you are typically upgrading to a major release or you are applying patches for a maintenance release. The types of upgrades possible for Oracle Database client and server software are as follows:

- Major Database Release Upgrade
- Database Maintenance Release Upgrade

##### Major Database Release Upgrade

The upgrade changes the first digit of the release number. For example, upgrading from Oracle9i to Oracle Database 11g is a major database release upgrade.

##### Database Maintenance Release Upgrade

The upgrade changes the second digit of the release number. For example, upgrading from Oracle Database 11g Release 1 (11.1) to Oracle Database 11g Release 2 (11.2) is a database maintenance release upgrade.

#### Possible Client/Server Configurations

Your precompiler and OCI applications run on the client in a client/server environment, where the Oracle Database server is the server. You can use one or more of the following client/server configurations in your environment:

- Different Computers
- Different Oracle Home Directories on the Same Computer
- Same Oracle Home

##### Different Computers

The client software and the server software are on different computers, and they are connected through a network. The client and server environments are separate.

##### Different Oracle Home Directories on the Same Computer

The client software and the server software are on the same computer, but they are installed in different Oracle home directories. Again, the client and server environments are separate.

##### Same Oracle Home

The client software and server software are installed in the same Oracle home on the same computer. In this case, any upgrade of the server software is also an upgrade of the client software.

See Also:

[Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/dist_pro.htm#CNCPT701) and [Oracle Database Heterogeneous Connectivity User's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e11050/toc.htm) for more information about client/server environments

### Compatibility Rules for Applications When Upgrading Client/Server Software

This section covers compatibility rules that apply when you upgrade Oracle Database client or server software. The rules are based on the type of software upgrade you are performing and on your client/server configuration.

The following sections contain compatibility rules for the following types of upgrades:

- Upgrading the Oracle Database Server Software
- Upgrading the Oracle Database Client Software

Note:

This section uses the terms introduced in "Understanding Software Upgrades and Your Client/Server Configuration".

#### Upgrading the Oracle Database Server Software

The following rules apply when you upgrade the Oracle Database server software.

- If You Do Not Change the Client Environment, Then You Are Not Required to Relink.
- Applications Can Run Against Newer or Older Oracle Database Server Releases

##### If You Do Not Change the Client Environment, Then You Are Not Required to Relink.

If your client and server are on different computers or are in different Oracle home directories on the same computer, and you upgrade the Oracle Database server software without changing the client software, then you are not required to precompile, compile, or relink your applications. In these cases, the client software is separate from the server software and continues to function against the server.

However, if your applications are using the same Oracle home as the Oracle Database server, then your server upgrade also upgrades your client software, and you must follow the rules in "Upgrading the Oracle Database Client Software".

Note:

It is possible to upgrade the Oracle Database server software but not install the new precompiler or OCI client software when you are using the same Oracle home for both. In this case, the client software is not upgraded. However, such a configuration is not recommended.

##### Applications Can Run Against Newer or Older Oracle Database Server Releases

When you run a precompiler or OCI application against a database server, Oracle recommends that the release of the database server software be equal to or higher than the client software release, but this configuration is not strictly required. For example, if your client software is Oracle9i Release 2 (9.2.0.8), then it is recommended that your server software be Oracle9i Release 2 (9.2.0.8) or higher to run a precompiler application on the client against the server.

#### Upgrading the Oracle Database Client Software

Oracle recommends that you upgrade your client software to match the current server software. For example, if you upgrade your server to Oracle Database 11g Release 2 (11.2), then Oracle recommends upgrading the client software to Oracle Database 11g Release 2 (11.2) as well. Keeping the server and client software at the same release number ensures the maximum stability for your applications. In addition, the latest Oracle Database client software might provide added features and performance enhancements that were not available with previous releases.

The following rules apply when you upgrade the Oracle Database client software:

- Applications Can Be Linked with Newer Libraries
- Statically Linked Applications Must Always Be Relinked
- Relinking Dynamically Linked Applications

##### Applications Can Be Linked with Newer Libraries

The code generated by precompiler applications can be linked with a release of the client library that is equal to or higher than the server release.

OCI applications can be linked with a version of the OCI runtime library that is equal to or higher than the version of the OCI library with which the application was developed.

##### Statically Linked Applications Must Always Be Relinked

Statically linked OCI applications need to be re-linked for both major and minor releases, because the statically linked Oracle client-side library code may be incompatible with the error messages in the upgraded `ORACLE_HOME`. For example, if an error message was updated with additional parameters, then it will not be compatible with the statically-linked code.

##### Relinking Dynamically Linked Applications

Dynamically linked OCI applications from Oracle Database 10g Release 1 (10.1) and later releases are upward compatible with the current release. That is, the Oracle client-side dynamic library is upward compatible with the previous version of the library. Oracle Universal Installer creates a symbolic link for the previous version of the library that resolves to the current version. Therefore, an application that is dynamically linked with the previous version of the Oracle client-side dynamic library does not need to be relinked to operate with the current version of the Oracle client-side library.

Note:

If the application is linked with a runtime library search path (such as `-rpath` on Linux), then the application may still run with the version of the Oracle client-side library with which it is linked. To run with the current version of the Oracle client-side library, it must be relinked.

If the application is linked with the deferred option (for example, statically-linked application), it must be relinked.

If the application is from a release before Oracle Database 10g Release 1 (10.1), then it must be relinked.

### Upgrading Options for Your Precompiler and OCI Applications

You have the following options for upgrading your precompiler and OCI applications:

- Option 1: Leave the Application Unchanged. Do not relink, precompile, or compile the application, and do not change the application code. The application continues to work against the new Oracle Database 11g release.
- Option 2: Precompile or Compile the Application Using the New Software. Application code must be changed if any APIs are deprecated, desupported, or changed.
- Option 3: Change the Application Code to Use New Oracle Database 11g Features. Subsequently, precompile or compile and then relink the code.

These options are listed in order of increasing difficulty and increasing potential benefits. That is, Option 1 is the least difficult option, but it offers the least potential benefits, while Option 3 is the most difficult option, but it offers the most potential benefits. These options are discussed in the following sections.

#### Option 1: Leave the Application Unchanged

This option requires that the Oracle home environment of the application is not upgraded. You can leave the application unchanged, and it continues to work with the new Oracle Database 11g server. The major advantage to this option is that it is simple and easy. In addition, this option requires the least amount of administration, because you are not required to upgrade any of your client computers. If you have a large number of client computers, then avoiding the administrative costs of upgrading all of them can become very important.

The major disadvantage to this option is that your application cannot use the features that are available in the new Oracle Database 11g release. In addition, your application cannot leverage some of the possible performance benefits of the new Oracle Database 11g release.

#### Option 2: Precompile or Compile the Application Using the New Software

When upgrading from a maintenance release to the new Oracle Database 11g software, you must precompile or compile the application with the new software after making necessary code changes to account for APIs that are deprecated or changed. Recompiling is not required if you are upgrading to a minor release within Oracle Database 11g software.

This option requires that you install the new Oracle Database client software on each client computer. You are required to precompile or compile, and relink your application only once, regardless of the number of clients you have.

By recompiling, you perform a syntax check of your application code. Some problems in the application code that were not detected by previous releases of the Oracle software might emerge when you precompile or compile with the new Oracle software. Therefore, precompiling and compiling with the new software often helps you detect and correct problems in the application code that might have gone unnoticed before.

Also, recompiling affords maximum stability for your application, because you are sure that it works with the new Oracle software. Further, your environment is ready for new development using the latest tools and features available. In addition, you might benefit from performance improvements that are available with the new Oracle software only after you recompile and relink.

#### Option 3: Change the Application Code to Use New Oracle Database 11g Features

You can make code changes to your application to take advantage of new Oracle Database 11g features. This option is the most difficult, but it can provide the most potential benefits. You gain all of the advantages described in "Option 2: Precompile or Compile the Application Using the New Software". In addition, you also benefit from changes to your application that might leverage performance and scalability benefits available with the new Oracle Database 11g release. Further, you can add new features to your application that are available only with the new Oracle Database 11g release.

Become familiar with the features of the new Oracle Database 11g release by reading [Oracle Database New Features Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41360/toc.htm). Also, consult the Oracle documentation for your development environment so that you understand how to implement the features you want to use. For the precompilers, see [Pro\*C/C++ Programmer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e10825/toc.htm) and [Pro\*COBOL Programmer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e10826/toc.htm). For OCI, see [Oracle Call Interface Programmer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e10646/toc.htm).

When you have decided on the new features you want to use, change the code of your application to use these features. Follow the appropriate instructions in the following sections based on your development environment:

- Changing Precompiler Applications
- Changing OCI Applications

##### Changing Precompiler Applications

Complete the following steps to change your precompiler application to use features of the new Oracle Database 11g release:

1. If you want to take advantage of features of the new Oracle Database 11g release, then incorporate the code for these new features into the existing application.
2. Precompile the application using the Oracle precompiler.
3. Compile the application.
4. Relink the application with the runtime library of the new Oracle Database 11g release, `SQLLIB`, which is included with the precompiler.

##### Changing OCI Applications

Complete the following steps to change your OCI application to use features of the new Oracle Database 11g release:

1. Incorporate OCI calls of the new Oracle Database 11g release into the existing application.
2. Compile the application.
3. Relink the application with the runtime library of the new Oracle Database 11g release.

## Upgrading SQL\*Plus Scripts and PL/SQL

To use features and functions of the new Oracle Database 11g release, change existing SQL scripts to use the syntax of the new Oracle Database 11g release. Existing SQL scripts run unchanged on the new Oracle Database 11g release, and require no modification, if they do not use features and functions of the new Oracle Database 11g release.

Note that improved error checking in the new Oracle Database 11g release might now identify errors at compile time rather than at run time.

Related topic:

- Change to Evaluation of Numeric Literals

### Change to Evaluation of Numeric Literals

Evaluation of numeric literals has changed such that at least one of the constants in a numeric computation with literals must be a decimal specified to the 10th place. This is because Oracle Database releases after Oracle Database 10g Release 1 (10.1) use `INTEGER` arithmetic (approximately 9 significant digits) for some expressions whereas Oracle9i Release 2 (9.2) used `NUMBER` arithmetic (approximately 38 significant digits).

Therefore, if you are dealing with results of greater than 9 significant digits, then one of the literals should be in decimal format to prevent numeric overflow errors. For example, in Oracle Database 10g, the computation of `v1` in the following example causes a numeric overflow error:

```
DECLARE
  v1 NUMBER(38);
BEGIN
  v1 := 256*256*256*256;
  DBMS_OUTPUT.PUT_LINE(v1);
END;
/
```

The solution to the error is to specify one of the numeric literals as a decimal (256.0), as follows:

```
DECLARE
  v1 NUMBER(38);
BEGIN
  v1 := 256*256*256*256.0;
  DBMS_OUTPUT.PUT_LINE(v1);
END;
/
```

See Also:

- The "What's New in SQL\*Plus" section in the [SQL\*Plus User's Guide and Reference](https://docs.oracle.com/cd/E11882_01/server.112/e16604/toc.htm) to learn about new features in SQL\*Plus
- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/toc.htm) for more information about upgrading SQL scripts

## Upgrading Oracle Forms or Oracle Developer Applications

Forms applications run the same on Oracle9i, Oracle Database 10g, and Oracle Database 11g. However, review the new features described in [Oracle Database New Features Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41360/toc.htm) to determine whether any of the features of the new Oracle Database 11g release would be beneficial to your applications or might otherwise affect them. Information about the ways in which the features of the new Oracle Database 11g release interact with forms and developer applications is provided in the Oracle Developer documentation set. Also, the Oracle Developer documentation for your operating system contains instructions for upgrading your forms or developer applications.

Note:

New releases of Oracle Developer might introduce new reserved words that are specific to Oracle Developer. Code changes might be required if your application uses any of these new reserved words.