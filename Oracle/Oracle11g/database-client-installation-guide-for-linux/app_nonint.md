---
title: Installing Oracle Database Client Using Response Files
book: Database Client Installation Guide for  Linux
doc_id: E24322-14
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/install.112/e24322/app_nonint.htm
tags:
  - oracle
  - 11g
  - database-client-installation-guide-for-linux
---

## A Installing Oracle Database Client Using Response Files

This appendix describes how to use response files to perform a silent or response file installation of Oracle Database Client. It includes information about the following topics:

## A.1 How Response Files Work

You can automate the installation and configuration of Oracle software, either fully or partially, by specifying a response file when you start Oracle Universal Installer. Oracle Universal Installer uses the values contained in the response file to provide answers to some or all of Oracle Universal Installer prompts. It includes information about the following topics:

- Reasons for Using Silent Mode or Response File Mode
- General Procedure for Using Response Files

Typically, Oracle Universal Installer runs in interactive mode, which means that it prompts you to provide information in graphical user interface (GUI) screens. When you use response files to provide this information, you run Oracle Universal Installer at a command prompt using either of the following modes:

- Silent mode
	If you include responses for all of the prompts in the response file and specify the `-silent` option when starting Oracle Universal Installer, then Oracle Universal Installer runs in silent mode. During a silent-mode installation, Oracle Universal Installer does not display any screens. Instead, it displays progress information in the terminal that you used to start it.
- Response file mode
	If you include responses for some or all of the prompts in the response file and omit the `-silent` option, then Oracle Universal Installer runs in response file mode. During a response file mode installation, Oracle Universal Installer displays all the screens, screens for which you specify information in the response file and also screens for which you did not specify the required information in the response file. The enables you to validate values in the screens for which you have provided the information in the response file and continue with the installation.

You define the settings for a silent or response file installation by entering values for the variables listed in the response file. For instance, to specify the Oracle home location, you would supply the appropriate value for the `ORACLE_HOME` variable as follows:

```
ORACLE_HOME=/u01/app/oracle/product/11.2.0/dbhome_1
```

Another way of specifying the variable settings of the response file is to pass them as command line arguments when you run Oracle Universal Installer. For example:

```
-silent directory_path
```

In this command, `directory_path` is the path of the database directory on the installation media or on the hard drive.

See Also:

- [Oracle Universal Installer and OPatch User's Guide for Windows and UNIX](https://docs.oracle.com/cd/E11882_01/em.112/e12255/toc.htm) for more information about response file formats
- My Oracle Support website for more information on response files:
	`https://support.oracle.com/`

### A.1.1 Reasons for Using Silent Mode or Response File Mode

The following table describes several reasons why you might want to run Oracle Universal Installer in silent mode or response file mode.

| Mode | Uses |
| --- | --- |
| Silent | Use silent mode to: - Complete an unattended installation, which you might schedule using an operating system utility such as `cron`. - Complete several similar installations on multiple systems without user interaction. - Install the software on a system that does not have X Window System software installed on it.  Oracle Universal Installer displays progress information in the terminal that you used to start it, but it does not display any of Oracle Universal Installer screens. |
| Response file | Use response file mode to complete similar Oracle software installations on more than one systems, providing default answers to some, but not all of Oracle Universal Installer prompts.  In response file mode, all the installer screens are displayed, but defaults for the fields in these screens are provided by the response file. You have to provide information for the fields in screens where you have not provided values in the response file. |

### A.1.2 General Procedure for Using Response Files

The following are the general steps to install and configure Oracle products using Oracle Universal Installer in silent or response file mode:

Note:

You must complete all required preinstallation tasks on a system before running Oracle Universal Installer in silent or response file mode.
1. Prepare a response file.
2. Run Oracle Universal Installer in silent or response file mode.
3. Run the root scripts as prompted by Oracle Universal Installer.
4. If you completed a software-only installation, then run Net Configuration Assistant and Database Configuration Assistant in silent or response file mode if required.

These steps are described in the following sections.

## A.2 Preparing a Response File

This section describes the following methods to prepare a response file for use during silent mode or response file mode installations:

- Editing a Response File Template
- Saving a Response File

### A.2.1 Editing a Response File Template

This method is useful for the Enterprise Edition, or Standard Edition installation types.

Oracle provides response file templates for each product and installation type, and for each configuration tool. These files are located in the `client\response` directory on the Oracle Database installation media.

Note:

If you copied the software to a hard disk, the response files are located in the `database/response` directory.

Table A-1 lists the response files provided with Oracle Database.

Table A-1 Response Files

| Response File | Description |
| --- | --- |
| `client_install.rsp` | Client installation of Oracle Database Client. |
| `netca.rsp` | Oracle Net Configuration Assistant to perform the configuration with the client installation types. |

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
	Oracle Universal Installer or configuration assistant fails if you do not correctly configure the response file. Refer to ["Silent-Mode Response File Error Handling"](app_ts.md) for information about troubleshooting a failed silent-mode installation.

### A.2.2 Saving a Response File

You can use Oracle Universal Installer in interactive mode to save a response file, which you can edit and then use to complete silent mode or response file mode installations.

Starting with Oracle Database 11g Release 2 (11.2), you can save all the installation steps into a response file during installation. You can click the Save Response File button on the Summary page to do this. Later, this file can be used for a silent installation.

When you save the response file, you can either complete the installation, or you can exit from Oracle Universal Installer on the Summary page, before it starts to copy the software to the system.

If you save a response file during a silent installation, then Oracle Universal Installer saves the variable values that were specified in the original source response file into the new response file.

Note:

Oracle Universal Installer does not save passwords in the response file.

To save a response file:

1. Complete the preinstallation tasks listed in [Chapter 2](pre_install.md).
	When you run Oracle Universal Installer to save a response file, it checks the system to verify that it meets the requirements to install the software. For this reason, Oracle recommends that you complete all of the required preinstallation tasks and save the response file while completing an installation.
2. Ensure that the Oracle software owner user (typically, `oracle`) has permissions to create or write to the Oracle home path that you specify when you run Oracle Universal Installer.
3. On each Oracle Universal Installer screen, specify the required information.
4. When Oracle Universal Installer displays the Summary screen, perform the following actions:
	1. Click Save Response File and specify a file name and location for the response file. Then, click Save to save the values to the file.
		2. Click Finish to continue with the installation.
		Click Cancel if you do not want to continue with the installation. The installation stops, but the saved response file is retained.
5. Before using the saved response file on another system, edit the file and make any required changes.
	Use the instructions in the file as a guide when editing it.

## A.3 Running Oracle Universal Installer Using a Response File

Now, you are ready to run Oracle Universal Installer at the command line, specifying the response file you created, to perform the installation. The Oracle Universal Installer executable, `runInstaller`, provides several options. For help information on the full set of these options, run the `runInstaller` command with the `-help` option, for example:

```
$ directory_path/runInstaller -help
```

The help information appears in a window after some time.

To run Oracle Universal Installer using a response file:

1. Complete the preinstallation tasks listed in [Chapter 2](pre_install.md).
2. Log in as the Oracle software owner user (typically, `oracle`).
3. If you are completing a response file mode installation, set the `DISPLAY` environment variable.
	Note:
	You do not have to set the `DISPLAY` environment variable if you are completing a silent-mode installation.
4. To start Oracle Universal Installer in silent or response file mode, enter a command similar to the following:
	```
	$ /directory_path/runInstaller [-silent] [-noconfig] \
	 -responseFile responsefilename
	```
	Note:
	Do not specify a relative path to the response file. If you specify a relative path, then Oracle Universal Installer fails.
	In this example:
	- `directory_path` is the path of the database directory on the DVD or on the hard drive.
		- `-silent` runs Oracle Universal Installer in silent mode.
		See ["Silent-Mode Response File Error Handling"](app_ts.md)
		- `-noconfig` suppresses running the configuration assistants during installation, and a software-only installation is performed instead.
		- `responsefilename` is the full path and file name of the installation response file that you configured.
	Note:
	For more information about other options for the `runInstaller` command, enter the following command:
	```
	$ /directory_path/runInstaller -help
	```
5. When the installation completes, log in as the `root` user and run the `root.sh` script:
	```
	$ sudo sh
	password:
	# /oracle_home_path/root.sh
	```
6. If this is the first time you are installing Oracle software on your system, then Oracle Universal Installer prompts you to run the `orainstRoot.sh` script. Log in as the `root` user and run the `orainstRoot.sh` script:
	```
	$ sudo sh
	password:
	# /oracle_home_path/orainstRoot.sh
	```

## A.4 Performing an In-place Oracle Database Client Upgrade Using the Response File

Starting with Oracle Database 11g Release 2 (11.2.0.2), you can perform an in-place Oracle Database Client upgrade using the response file:

1. Edit the `oracle.install.client.upgrading` entry in the `client_install.rsp` file and set it to `true`. By default, the `oracle.install.client.upgrading` entry is set to `false`.
2. Run Oracle Universal Installer in silent mode as described in "Running Oracle Universal Installer Using a Response File".