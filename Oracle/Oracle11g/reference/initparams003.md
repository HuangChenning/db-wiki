---
title: Parameter Files
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams003.htm
tags:
  - oracle
  - 11g
  - reference
---

A parameter file is a file that contains a list of initialization parameters and a value for each parameter. You specify initialization parameters in a parameter file that reflect your particular installation. Oracle supports the following two types of parameter files:

- Server Parameter Files
- Initialization Parameter Files

## Server Parameter Files

A server parameter file is a binary file that acts as a repository for initialization parameters. The server parameter file can reside on the machine where the Oracle database server executes. Initialization parameters stored in a server parameter file are persistent, in that any changes made to the parameters while an instance is running can persist across instance shutdown and startup.

## Initialization Parameter Files

An initialization parameter file is a text file that contains a list of initialization parameters. The file should be written in the client's default character set.

The following are sample entries in an initialization parameter file:

```
PROCESSES = 100
OPEN_LINKS = 12
GLOBAL_NAMES = true
```

The name of the initialization parameter file varies depending on the operating system. For example, it can be in mixed case or lowercase, or it can have a logical name or a variation of the name `init.ora`. Also supplied is an `initdw.ora` file, which contains suggested parameter settings for data warehouses and data marts. The database administrator can choose a different filename for the initialization parameter file.

Refer to your operating system-specific Oracle documentation for the default locations and filenames for initialization parameter files on your operating system. The initialization parameter file is read by the client-side tool used to start the server (such as SQL\*Plus).

Sample initialization parameter files are provided on the Oracle distribution medium for each operating system. A sample file is sufficient for initial use, but you will probably want to modify the file to tune the database for best performance. Any changes will take effect after you completely shut down and restart the instance.

### Specifying Values in an Initialization Parameter File

This section describes several aspects of setting parameter values in an initialization parameter file.

#### Rules Governing Initialization Parameter Files

The following rules govern the specification of parameters in initialization parameter files:

- An initialization parameter file should contain only parameters and comments. A pound sign (#) starts a comment line. The rest of the line is ignored.
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
- ["IFILE"](initparams103.md)

#### Using Special Characters in Parameter Values

If a parameter value contains a special character, then the special character must be preceded by a backslash or the entire parameter value must be enclosed in quotation marks. For example, you can specify special characters using either of the following:

```
DB_DOMAIN = 'JAPAN.ACME#.COM'

DB_DOMAIN = JAPAN.ACME\#.COM
```

Table 1-1 lists the special characters you can use in initialization parameter files.

Table 1-1 Special Characters in Initialization Parameter Files

| Character | Name | Description |
| --- | --- | --- |