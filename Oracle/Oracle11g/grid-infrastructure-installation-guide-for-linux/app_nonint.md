---
title: Installing and Configuring Oracle Database Using Response Files
book: Grid Infrastructure Installation Guide for Linux
doc_id: E41961-10
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/install.112/e41961/app_nonint.htm
tags:
  - oracle
  - 11g
  - grid-infrastructure-installation-guide-for-linux
---

## B Installing and Configuring Oracle Database Using Response Files

This appendix describes how to install and configure Oracle products using response files. It includes information about the following topics:

## B.1 How Response Files Work

When you start the installer, you can use a response file to automate the installation and configuration of Oracle software, either fully or partially. The installer uses the values contained in the response file to provide answers to some or all installation prompts.

Typically, the installer runs in interactive mode, which means that it prompts you to provide information in graphical user interface (GUI) screens. When you use response files to provide this information, you run the installer from a command prompt using either of the following modes:

- Silent mode
	If you include responses for all of the prompts in the response file and specify the `-silent` option when starting the installer, then it runs in silent mode. During a silent mode installation, the installer does not display any screens. Instead, it displays progress information in the terminal that you used to start it.
- Response file mode
	If you include responses for some or all of the prompts in the response file and omit the `-silent` option, then the installer runs in response file mode. During a response file mode installation, the installer displays all the screens, screens for which you specify information in the response file, and also screens for which you did not specify the required information in the response file.

You define the settings for a silent or response file installation by entering values for the variables listed in the response file. For example, to specify the Oracle home name, supply the appropriate value for the `ORACLE_HOME` variable:

```
ORACLE_HOME="OraDBHome1"
```

Another way of specifying the response file variable settings is to pass them as command line arguments when you run the installer. For example:

```
-silent "ORACLE_HOME=OraDBHome1" ...
```

See Also:

[Oracle Universal Installer and OPatch User's Guide for Windows and UNIX](https://docs.oracle.com/cd/E11882_01/em.112/e12255/toc.htm) for more information about response files

### B.1.1 Reasons for Using Silent Mode or Response File Mode

The following table provides use cases for running the installer in silent mode or response file mode.

| Mode | Uses |
| --- | --- |
| Silent | Use silent mode to do the following installations: - Complete an unattended installation, which you schedule using operating system utilities such as `at`. - Complete several similar installations on multiple systems without user interaction. - Install the software on a system that does not have X Window System software installed on it.  The installer displays progress information on the terminal that you used to start it, but it does not display any of the installer screens. |
| Response file | Use response file mode to complete similar Oracle software installations on multiple systems, providing default answers to some, but not all of the installer prompts.  In response file mode, all the installer screens are displayed, but defaults for the fields in these screens are provided by the response file. You have to provide information for the fields in screens where you have not provided values in the response file. |

### B.1.2 General Procedure for Using Response Files

The following are the general steps to install and configure Oracle products using the installer in silent or response file mode:

Note:

You must complete all required preinstallation tasks on a system before running the installer in silent or response file mode.
1. Prepare a response file.
2. Run the installer in silent or response file mode.
3. If you completed a software-only installation, then run Net Configuration Assistant and Database Configuration Assistant in silent or response file mode.

These steps are described in the following sections.

## B.2 Preparing a Response File

This section describes the following methods to prepare a response file for use during silent mode or response file mode installations:

- Editing a Response File Template
- Recording a Response File

### B.2.1 Editing a Response File Template

Oracle provides response file templates for each product and installation type, and for each configuration tool. These files are located at `database/response` directory on the installation media.

Note:

If you copied the software to a hard disk, then the response files are located in the directory `/response`.

Table B-1 lists the response files provided with this software:

Table B-1 Response Files for Oracle Database

| Response File | Description |
| --- | --- |
| `db_install.rsp` | Silent installation of Oracle Database 11g |
| `dbca.rsp` | Silent installation of Database Configuration Assistant |
| `netca.rsp` | Silent installation of Oracle Net Configuration Assistant |

Table B-2 Response files for Oracle Grid Infrastructure

| Response File | Description |
| --- | --- |
| grid\_install.rsp | Silent installation of Oracle Grid Infrastructure installations |

Caution:

When you modify a response file template and save a file for use, the response file may contain plain text passwords. Ownership of the response file should be given to the Oracle software installation owner only, and permissions on the response file should be changed to 600. Oracle strongly recommends that database administrators or other administrators delete or secure response files when they are not in use.

To copy and modify a response file:

1. Copy the response file from the response file directory to a directory on your system:
	```
	$ cp /directory_path/response/response_file.rsp local_directory
	```
	In this example, `directory_path` is the path to the `database` directory on the installation media. If you have copied the software to a hard drive, then you can edit the file in the `response` directory if you prefer.
2. Open the response file in a text editor:
	```
	$ vi /local_dir/response_file.rsp
	```
	See Also:
	[Oracle Universal Installer and OPatch User's Guide for Windows and UNIX](https://docs.oracle.com/cd/E11882_01/em.112/e12255/toc.htm) for detailed information on creating response files
3. Follow the instructions in the file to edit it.
	Note:
	The installer or configuration assistant fails if you do not correctly configure the response file.
4. Change the permissions on the file to 600:
	```
	$ chmod 600 /local_dir/response_file.rsp
	```
	Note:
	A fully specified response file for an Oracle Database installation contains the passwords for database administrative accounts and for a user who is a member of the OSDBA group (required for automated backups). Ensure that only the Oracle software owner user can view or modify response files or consider deleting them after the installation succeeds.

### B.2.2 Recording a Response File

You can use the installer in interactive mode to record a response file, which you can edit and then use to complete silent mode or response file mode installations. This method is useful for custom or software-only installations.

Starting with Oracle Database 11g Release 2 (11.2), you can save all the installation steps into a response file during installation by clicking Save Response File on the Summary page. You can use the generated response file for a silent installation later.

When you record the response file, you can either complete the installation, or you can exit from the installer on the Summary page, before it starts to copy the software to the system.

If you use record mode during a response file mode installation, then the installer records the variable values that were specified in the original source response file into the new response file.

Note:

Oracle Universal Installer does not record passwords in the response file.

To record a response file:

1. Complete preinstallation tasks as for a normal installation.
2. Ensure that the Oracle Grid Infrastructure software owner user (typically `grid`) has permissions to create or write to the Grid home path that you specify when you run the installer.
3. On each installation screen, specify the required information.
4. When the installer displays the Summary screen, perform the following steps:
	1. Click Save Response File and specify a file name and location to save the values for the response file, and click Save.
		2. Click Finish to create the response file and continue with the installation.
		Click Save Response File and Cancel if you only want to create the response file but not continue with the installation. The installation will stop, but the settings you have entered will be recorded in the response file.
5. Before you use the saved response file on another system, edit the file and make any required changes.
	Use the instructions in the file as a guide when editing it.

## B.3 Running the Installer Using a Response File

Run Oracle Universal Installer at the command line, specifying the response file you created. The Oracle Universal Installer executable, `runInstaller`, provides several options. For help information on the full set of these options, run the `runInstaller` command with the `-help` option. For example:

```
$ directory_path/runInstaller -help
```

The help information appears in a window.

To run the installer using a response file:

1. Complete the preinstallation tasks as for a normal installation
2. Log in as the software installation owner user.
3. If you are completing a response file mode installation, then set the `DISPLAY` environment variable.
	Note:
	You do not have to set the `DISPLAY` environment variable if you are completing a silent mode installation.
4. To start the installer in silent or response file mode, enter a command similar to the following:
	```
	$ /directory_path/runInstaller [-silent] [-noconfig] \
	 -responseFile responsefilename
	```
	Note:
	Do not specify a relative path to the response file. If you specify a relative path, then the installer fails.
	In this example:
	- `directory_path` is the path of the DVD or the path of the directory on the hard drive where you have copied the installation binaries.
		- `-silent` runs the installer in silent mode.
		- `-noconfig` suppresses running the configuration assistants during installation, and a software-only installation is performed instead.
		- `responsefilename` is the full path and file name of the installation response file that you configured.
5. When the installation completes, log in as the `root` user and run the `root.sh` script. For example
	```
	$ su root
	password:
	# /oracle_home_path/root.sh
	```

## B.4 Running Net Configuration Assistant Using a Response File

You can run Net Configuration Assistant in silent mode to configure and start an Oracle Net listener on the system, configure naming methods, and configure Oracle Net service names. To run Net Configuration Assistant in silent mode, you must copy and edit a response file template. Oracle provides a response file template named `netca.rsp` in the `response` directory in the `database` `/response` directory on the DVD.

Note:

If you copied the software to a hard disk, then the response file template is located in the `database/response` directory.

To run Net Configuration Assistant using a response file:

1. Copy the `netca.rsp` response file template from the response file directory to a directory on your system:
	```
	$ cp /directory_path/response/netca.rsp local_directory
	```
	In this example, `directory_path` is the path of the `database` directory on the DVD. If you have copied the software to a hard drive, you can edit the file in the `response` directory if you prefer.
2. Open the response file in a text editor:
	```
	$ vi /local_dir/netca.rsp
	```
3. Follow the instructions in the file to edit it.
	Note:
	Net Configuration Assistant fails if you do not correctly configure the response file.
4. Log in as the Oracle software owner user, and set the `ORACLE_HOME` environment variable to specify the correct Oracle home directory.
5. Enter a command similar to the following to run Net Configuration Assistant in silent mode:
	```
	$ $ORACLE_HOME/bin/netca -silent -responsefile /local_dir/netca.rsp
	```
	In this command:
	- The `-silent` option indicates runs Net Configuration Assistant in silent mode.
		- `local_dir` is the full path of the directory where you copied the `netca.rsp` response file template.

## B.5 Postinstallation Configuration Using a Response File

Use the following sections to create and run a response file configuration after installing Oracle software.

### B.5.1 About the Postinstallation Configuration File

When you run a silent or response file installation, you provide information about your servers in a response file that you otherwise provide manually during a graphical user interface installation. However, the response file does not contain passwords for user accounts that configuration assistants require after software installation is complete. The configuration assistants are started with a script called `configToolAllCommands`. You can run this script in response file mode by creating and using a password response file. The script uses the passwords to run the configuration tools in succession to complete configuration.

If you keep the password file to use for clone installations, then Oracle strongly recommends that you store it in a secure location. In addition, if you have to stop an installation to fix an error, you can run the configuration assistants using `configToolAllCommands` and a password response file.

The `configToolAllCommands` password response file consists of the following syntax options:

- internal\_component\_name is the name of the component that the configuration assistant configures
- variable\_name is the name of the configuration file variable
- value is the desired value to use for configuration.

The command syntax is as follows:

internal\_component\_name|variable\_name=value

For example:

```
oracle.assistants.asm|S_ASMPASSWORD=welcome
```

Oracle strongly recommends that you maintain security with a password response file:

- Permissions on the response file should be set to 600.
- The owner of the response file should be the installation owner user, with the group set to the central inventory (oraInventory) group.

### B.5.2 Running Postinstallation Configuration Using a Response File

To run configuration assistants with the `configToolAllCommands` script:

1. Create a response file using the syntax filename.properties. For example:
	```
	$ touch cfgrsp.properties
	```
2. Open the file with a text editor, and cut and paste the password template, modifying as needed.
	Example B-1 Password response file for Oracle Grid Infrastructure installation for a cluster
	Oracle Grid Infrastructure requires passwords for Oracle Automatic Storage Management Configuration Assistant (ASMCA), and for Intelligent Platform Management Interface Configuration Assistant (IPMICA) if you have a BMC card and you want to enable this feature. Provide the following response file:
	```
	oracle.assistants.asm|S_ASMPASSWORD=password
	oracle.assistants.asm|S_ASMMONITORPASSWORD=password
	oracle.crs|S_BMCPASSWORD=password
	```
	If you do not have a BMC card, or you do not want to enable IPMI, then leave the S\_BMCPASSWORD input field blank.
	Example B-2 Password response file for Oracle Real Application Clusters
	Oracle Database configuration requires configuring a password for the SYS, SYSTEM, SYSMAN, and DBSNMP passwords for use with Database Configuration Assistant (DBCA). In addition, if you use Oracle ASM storage, then configure the ASMSNMP password. Also, if you selected to configure Oracle Enterprise Manager, then you must provide the password for the Oracle software installation owner for the S\_HOSTUSERPASSWORD response.
	```
	oracle.assistants.server|S_SYSPASSWORD=password
	oracle.assistants.server|S_SYSTEMPASSWORD=password
	oracle.assistants.server|S_SYSMANPASSWORD=password
	oracle.assistants.server|S_DBSNMPPASSWORD=password
	oracle.assistants.server|S_HOSTUSERPASSWORD=password
	oracle.assistants.server|S_ASMSNMPPASSWORD=password
	```
	If you do not want to enable Oracle Enterprise Manager or Oracle ASM, then leave those password fields blank.
3. Change permissions to secure the file. For example:
	```
	$ ls -al cfgrsp.properties
	-rw------- 1 oracle oinstall 0 Apr 30 17:30 cfgrsp
	```
4. Change directory to `$ORACLE_HOME/cfgtoollogs`, and run the configuration script using the following syntax:
	configToolAllCommands RESPONSE\_FILE=/path/name.properties
	for example:
	```
	$ ./configToolAllCommands RESPONSE_FILE=/home/oracle/cfgrsp.properties
	```