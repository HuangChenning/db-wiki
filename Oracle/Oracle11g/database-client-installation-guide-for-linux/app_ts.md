---
title: Troubleshooting
book: Database Client Installation Guide for  Linux
doc_id: E24322-14
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/install.112/e24322/app_ts.htm
tags:
  - oracle
  - 11g
  - database-client-installation-guide-for-linux
---

## C Troubleshooting

This appendix contains information about troubleshooting. It includes information about the following topics:

## C.1 Verify Requirements

Before performing any of the troubleshooting steps in this appendix, ensure that the system meets the requirements and that you have completed all of the preinstallation tasks specified in [Chapter 2](pre_install.md).

Read the Release Notes

Read the release notes for the product before installing it. The release notes are available on the Oracle Database 11g DVD. The latest version of the release notes is also available at:

```
http://docs.oracle.com/
```

## C.2 X Window Display Errors

If you run Oracle Universal Installer on a remote system and you want to display Oracle Universal Installer's user interface on your local system, you might see error messages similar to the following:

```
"Failed to connect to server"
"Connection refused by server"
"Can't open display"
```

If you see one of these error messages, follow these steps:

Note:

This procedure applies only to users of UNIX workstations. If you are using a PC or other system with X server software installed, refer to the X server documentation, or contact your X server vendor or system administrator for information about how to permit remote systems to display X applications on the local system.
1. In a local terminal window, log in as the user that started the X Window session.
2. Enter the following command:
	```
	$ xhost fully_qualified_remote_host_name
	```
	For example:
	```
	$ xhost somehost.us.example.com
	```
3. Enter the following commands, where `workstation_name` is the host name or IP address of your workstation:
	- Bourne, Bash, or Korn shell:
		```
		$ DISPLAY=workstation_name:0.0
		$ export DISPLAY
		```
		- C shell:
		```
		% setenv DISPLAY workstation_name:0.0
		```
4. To determine whether X Window applications display correctly on the local system, enter the following command:
	```
	$ xclock
	```
	The X clock should appear on your monitor.
5. If the X clock appears, close the X clock and start Oracle Universal Installer again.

## C.3 What to Do If an Installation Error Occurs?

If you encounter an error during installation:

- Do not exit Oracle Universal Installer.
- If you clicked Next after you entered incorrect information on one of the installation screens, click Back to return to the screen and correct the information.
- If you encounter an error while Oracle Universal Installer is copying or linking files, then rerun Oracle Universal Installer with the `-debug` option:
	```
	$./runInstaller -debug
	```
	Check the log file for details. Refer to "Reviewing the Log of an Installation Session" section.
- If you encounter an error while a configuration assistant is running, refer to "Troubleshooting Configuration Assistants" section.
- If you cannot resolve the problem, remove the failed installation by following the steps listed in the "Cleaning Up After a Failed Installation" section.

## C.4 Reviewing the Log of an Installation Session

During an installation, Oracle Universal Installer records all of the actions that it performs in a log file. If you encounter problems during the installation, review the log file for information about possible causes of the problem.

To view the log file, follow these steps:

1. If necessary, enter the following command to determine the location of the `oraInventory` directory:
	```
	$ cat etc/oraInst.loc
	```
	The `inventory_loc` parameter in this file specifies the location of the `oraInventory` directory.
2. Enter the following command to change directory to Oracle Universal Installer log file directory, where `orainventory_location` is the location of the `oraInventory` directory:
	```
	$ cd /orainventory_location/logs
	```
3. Enter the following command to determine the name of the log file:
	```
	$ ls -ltr
	```
	This command lists the files in the order of creation, with the most recent file shown last. Installer log files have names similar to the following, where `date_time` indicates the date and time that the installation started:
	```
	installActionsdate_time.log
	```
4. To view the most recent entries in the log file, where information about a problem is most likely to appear, enter a command similar to the following:
	```
	$ tail -50 installActionsdate_time.log | more
	```
	This command displays the last 50 lines in the log file.
5. If the error displayed by Oracle Universal Installer or listed in the log file indicates a relinking problem, refer to the following file for more information:
	```
	$ORACLE_HOME/install/make.log
	```

## C.5 Troubleshooting Configuration Assistants

To troubleshoot an installation error that occurs when a configuration assistant is running:

- Review the installation log files listed in the "Reviewing the Log of an Installation Session" section.
- Review the specific configuration assistant log file located in the `$ORACLE_HOME/cfgtoollogs` directory. Try to fix the issue that caused the error.
- If you see the "Fatal Error. Reinstall" message, look for the cause of the problem by reviewing the log files. Refer to "Fatal Errors" for further instructions.

### C.5.1 Configuration Assistant Failure

Oracle configuration assistant failures are noted at the bottom of the installation screen. The configuration assistant interface displays additional information, if available. The configuration assistant execution status is stored in the following file:

```
oraInventory_location/logs/installActionsdate_time.log
```

The execution status codes are listed in the following table:

| Status | Result Code |
| --- | --- |
| Configuration assistant succeeded | 0 |
| Configuration assistant failed | 1 |
| Configuration assistant canceled | \-1 |

### C.5.2 Fatal Errors

If you receive a fatal error while a configuration assistant is running, you must remove the current installation and reinstall the Oracle software, as follows:

1. Remove the failed installation as described in the "Cleaning Up After a Failed Installation" section.
2. Correct the cause of the fatal error.
3. Reinstall the Oracle software.

## C.6 Troubleshooting Inventory Issues

If you face any of the following situations for Oracle home, then run the `opatch lsinventory -detail` command to list the contents of the inventory and see section "Recovering from inventory corruption" in the [Oracle Universal Installer and OPatch User's Guide for Windows and UNIX](https://docs.oracle.com/cd/E11882_01/em.112/e12255/toc.htm) for information on fixing the issue.

- Oracle home is cloned without completing the inventory steps.
- There is bad inventory.
- Inventory is not available but it is created when the Oracle Enterprise Manager Agent is installed in a separate Oracle home.

## C.7 Troubleshooting Screen Display Issues

If you connect to Oracle database with a screen resolution of 640X480 or 800X600, then the Next button in the GUI is not visible as it hides behind the Taskbar. To fix this problem, perform one of the following:

- Hide the Taskbar.
- Move the Oracle Universal Installer screen up.
- Set the screen resolution to 1024X768 or higher.

## C.8 Silent-Mode Response File Error Handling

To determine whether a silent-mode installation succeeds or fails, refer to the following log file:

```
/oraInventory_location/logs/silentInstalldate_time.log
```

If necessary, refer to the previous section for information about determining the location of the `oraInventory` directory.

A silent installation fails if:

- You do not specify a response file
- You specify an incorrect or incomplete response file
- Oracle Universal Installer encounters an error, such as insufficient disk space

Oracle Universal Installer or configuration assistant validates the response file at run time. If the validation fails, the silent-mode installation or configuration process ends.

## C.9 Cleaning Up After a Failed Installation

If an installation fails, you must remove the files that Oracle Universal Installer created during the attempted installation using the Deinstallation Tool. For more information on how to run the Deinstallation Tool refer to ["About the Deinstallation Tool"](remove_oracle_sw.md).