---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/parameter-files.html
tags:
  - oracle
  - 12c
  - reference
---

A parameter file is a file that contains a list of initialization parameters and a value for each parameter. You specify initialization parameters in a parameter file that reflect your particular installation.

Oracle supports the following two types of parameter files:

- Server Parameter Files
- Initialization Parameter Files

### 1.3.1 Server Parameter Files

A server parameter file is a binary file that acts as a repository for initialization parameters.

The server parameter file can reside on the computer where the Oracle database server executes. Initialization parameters stored in a server parameter file are persistent, in that any changes made to the parameters while an instance is running can persist across instance shutdown and startup.

See Also:

[Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=ADMIN00202) for an introduction to and detailed information about managing and using server parameter files and initialization parameter files

### 1.3.2 Initialization Parameter Files

An initialization parameter file is a text file that contains a list of initialization parameters.

Note:

See " About the Character Set of Parameter Values " for more information about the character set to use when specifying values in an initialization parameter file.

The following are sample entries in an initialization parameter file:

```
PROCESSES = 100
OPEN_LINKS = 12
GLOBAL_NAMES = true
```

The name of the initialization parameter file varies depending on the operating system. For example, it can be in mixed case or lowercase, or it can have a logical name or a variation of the name `init.ora`. Also supplied is an `initdw.ora` file, which contains suggested parameter settings for data warehouses and data marts. The database administrator can choose a different file name for the initialization parameter file.

Refer to your operating system-specific Oracle documentation for the default locations and filenames for initialization parameter files on your operating system. The initialization parameter file is read by the client-side tool used to start the server (such as SQL\*Plus).

Sample initialization parameter files are provided on the Oracle distribution medium for each operating system. A sample file is sufficient for initial use, but you will probably want to modify the file to tune the database for best performance. Any changes will take effect after you completely shut down and restart the instance.

#### 1.3.2.1 About the Character Set of Parameter Values

Only characters from the default character set of the database platform are supported in parameter values. For all platforms except IBM z/OS and Fujitsu BS2000 the default platform character set is US7ASCII (7-bit ASCII).

The database behavior is undefined when parameter values with unsupported characters are specified. When using the `ALTER SYSTEM` statement to set a parameter value in a server parameter file, make sure only supported characters are used. The database does not always report an error when a value with unsupported characters is specified.

The initialization parameter file is a client-side file. When used, it is located on the host on which you start SQL\*Plus to start up a database instance. The initialization parameter file must be written in the client character set as specified by the `NLS_LANG` client setting. However, parameter values should not contain characters not supported by the default character set of the database.

#### 1.3.2.2 Specifying Values in an Initialization Parameter File

This section describes several aspects of setting parameter values in an initialization parameter file.

##### 1.3.2.2.1 Rules Governing Initialization Parameter Files

This section describes the rules that govern the specification of parameters in initialization parameter files.

- An initialization parameter file should contain only parameters and comments. A pound sign (#) starts a comment line. The rest of the line is ignored.
- Comments must use the same character set as parameter values.
- You can specify parameters in any order.
- Case (upper or lower) in filenames is significant only if case is significant on the host operating system.
- To enter several parameters on one line, use spaces between parameter names and values, as in the following example:
	```
	PROCESSES = 100 CPU_COUNT = 1 OPEN_CURSORS = 10
	```
- Some parameters, such as `ROLLBACK_SEGMENTS`, accept multiple values. Any of the following represent valid syntax.
	- Enter multiple values enclosed in parentheses and separated by commas. For example:
		```
		ROLLBACK_SEGMENTS = (SEG1, SEG2, SEG3, SEG4, SEG5)
		```
		- Enter multiple values without parentheses and commas. For example:
		```
		ROLLBACK_SEGMENTS = SEG1 SEG2 SEG3 SEG4 SEG5
		```
		- Enter multiple values, one per line. For example:
		```
		ROLLBACK_SEGMENTS = SEG1
		ROLLBACK_SEGMENTS = SEG2
		ROLLBACK_SEGMENTS = SEG3
		ROLLBACK_SEGMENTS = SEG4
		ROLLBACK_SEGMENTS = SEG5
		```
	If you enter values for one parameter on multiple lines, then the entries must be on consecutive lines. If they are not, then the first entry will not be processed properly. For example, in the following entry the setting for `SEG3` and `SEG4` will override the setting for `SEG1` and `SEG2`:
	```
	ROLLBACK_SEGMENTS = SEG1 SEG2
	OPEN_CURSORS = 10
	ROLLBACK_SEGMENTS = SEG3 SEG4
	```
- A backslash (\\), also known as an escape character, indicates continuation of the parameter specification. If a backslash continues a line, then the continued line must have no leading spaces. For example:
	```
	ROLLBACK_SEGMENTS = (SEG1, SEG2, \
	SEG3, SEG4, SEG5)
	```
- You can use the `IFILE` initialization parameter to embed the contents of another initialization parameter file into the current initialization parameter file.
- Enclose in quotation marks any parameter values that contain spaces or tabs. You can use either single or double quotation marks unless otherwise indicated. For example:
	```
	NLS_TERRITORY = 'CZECH REPUBLIC'
	```
	Note:
	Listing parameters in alphabetical order in the initialization parameter file can help you to find them and can help ensure that each parameter is specified only once.
- Enclose in quotation marks any parameter value that contains a special character.

See Also:

- Your operating system-specific Oracle documentation for more information on initialization parameter files
- " [IFILE](IFILE.md) "

##### 1.3.2.2.2 Using Special Characters in Parameter Values

If a parameter value contains a special character, then the special character must be preceded by a backslash or the entire parameter value must be enclosed in quotation marks.

For example, you can specify special characters using either of the following:

```
DB_DOMAIN = 'JAPAN.ACME#.COM'

DB_DOMAIN = JAPAN.ACME\#.COM
```

Table 1-1 lists the special characters you can use in initialization parameter files.

Table 1-1 Special Characters in Initialization Parameter Files

| Character | Name | Description |
| --- | --- | --- |