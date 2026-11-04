---
title: "SQL*Plus Globalization Support"
book: "SQL*Plus User's Guide and Reference"
doc_id: E16604-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e16604/ch_eleven.htm
tags:
  - oracle
  - 11g
  - sqlplus-users-guide-and-reference
---

## 11 SQL\*Plus Globalization Support

Globalization support enables the storing, processing and retrieval of data in native languages. The languages that can be stored in an Oracle database are encoded by Oracle Database-supported character sets. Globalization support ensures that database utilities, error messages, sort order, and date, time, monetary, numeric, and calendar conventions adjust to the native language and locale.

Topics:

- Configuring Globalization Support in Command-line SQL\*Plus
- NLS\_LANG Environment Variable

For more information on globalization support, see the Oracle Technology Network globalization notes at `http://www.oracle.com/technetwork/products/globalization/`

and see the [Oracle Database Globalization Support Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10729/toc.htm)

## Configuring Globalization Support in Command-line SQL\*Plus

SQL\*Plus supports multiple languages through the NLS\_LANG environment variable. To display another language in SQL\*Plus, before starting SQL\*Plus you must configure:

- NLS\_LANG in the SQL\*Plus client environment.
- The Oracle Database during installation.

### SQL\*Plus Client

The SQL\*Plus client environment is configured by setting the NLS\_LANG environment variable which is read by SQL\*Plus at startup.

### Oracle Database

The Oracle Database environment is configured by creating the database with the required character set.

## NLS\_LANG Environment Variable

The NLS\_LANG environment variable has three components, each controlling a subset of the globalization features.

Your operating system and keyboard must be able to support the character set you have chosen. You may need to install additional support software. For more information about NLS\_LANG, and software support, see the [Oracle Database Globalization Support Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10729/toc.htm).

Setting up locale specific behavior on the SQL\*Plus client is achieved with the use of NLS parameters. These parameters may be specified in a number of ways, including as an initialization parameter on the server. For settings that control the behavior of the server, see the [Oracle Database Globalization Support Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10729/toc.htm).

NLS\_LANG has the syntax:

```
NLS_LANG = language_territory.charset
```

where language specifies the conventions to use for Oracle Database messages, sorting order, day and month names. For example, to receive messages in Japanese, set language to JAPANESE. If language is not set, it defaults to AMERICAN.

where territory specifies the convention for default dates, and for monetary, and numeric formats. For example to use the Japanese territory format, set territory to JAPAN. If territory is not set, the default value is derived from the language value, and so is set to AMERICA.

where, in SQL\*Plus command-line, charset specifies the character set encoding used by SQL\*Plus for data processing, and is generally suited to that of the users terminal. Illogical combinations can be set, but will not work. For example, Japanese cannot be supported using a Western European character set such as:

```
NLS_LANG=JAPANESE_JAPAN.WE8DEC
```

However, Japanese could be supported with the Unicode character set. For example:

```
NLS_LANG=JAPANESE_JAPAN.UTF8
```

### Viewing NLS\_LANG Settings

You can view the NLS\_LANG setting by entering the SELECT command:

```
SELECT * FROM NLS_SESSION_PARAMETERS;
```

The NLS\_TERRITORY and NLS\_LANGUAGE values correspond to the language and territory components of the NLS\_LANG variable.

You can also obtain a list of valid values for the NLS\_SORT, NLS\_LANGUAGE, NLS\_TERRITORY and NLS\_CHARACTERSET by querying the NLS dynamic performance view table V$NLS\_VALID\_VALUES.

## Setting NLS\_LANG

You can set the NLS\_LANG environment variable to control globalization features.

Example 11-1 Configuring Japanese Support in SQL\*Plus on Windows

1. Ensure you have exited your current SQL\*Plus session.
2. Open System from Start > Settings > Control Panel.
3. Click the Advanced tab and select Environment Variables.
4. Create a new environment variable, NLS\_LANG, with a value of Japanese\_Japan.JA16SJIS.
5. You may need to restart Windows for this setting to take effect.

Example 11-2 Configuring Japanese Support in SQL\*Plus on UNIX

1. Ensure you have exited your current SQL\*Plus session.
2. Set the NLS\_LANG variable using either set or setenv depending on the UNIX shell you are using. For example, in csh, you would enter:
	```
	setenv NLS_LANG Japanese_Japan.UTF8
	```
	or
	```
	setenv NLS_LANG Japanese_Japan.JA16SJIS
	```
	or
	```
	setenv NLS_LANG Japanese_Japan.JA16EUC
	```
	The locale setting of your UNIX terminal determines the exact value of the NLS\_LANG parameter. For more information on the NLS\_LANG setting, see the [Oracle Database Globalization Support Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10729/toc.htm).

Example 11-3 Configuring Japanese Support in Oracle Database

To store data in the Japanese character set using UTF-8 character encoding, ensure that the Oracle database has been created with the AL32UTF8 character set. See your Oracle Database Installation Guide for information about creating your database in a character set other than US7ASCII.