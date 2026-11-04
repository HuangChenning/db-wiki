---
title: Installing Oracle Database Client
book: Database Client Installation Guide for  Linux
doc_id: E24322-14
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/install.112/e24322/inst_task.htm
tags:
  - oracle
  - 11g
  - database-client-installation-guide-for-linux
---

## 3 Installing Oracle Database Client

The Oracle Database Client software is available on installation media or you can download it from the Oracle Technology Network website. In most cases, you use the graphical user interface (GUI) provided by Oracle Universal Installer to install the software. However, you can also use Oracle Universal Installer to complete silent-mode installations, without using the GUI.

See Also:

[Appendix A](app_nonint.md) for information about silent-mode installations

## 3.1 Reviewing Installation Guidelines

Review the following guidelines before starting Oracle Universal Installer:

- Oracle Universal Installer
	Do not use Oracle Universal Installer from an earlier Oracle release to install components from this release.
- Reinstalling Oracle Software
	If you reinstall Oracle software into an Oracle home directory where Oracle Database is installed, you must also reinstall any components, such as Oracle Partitioning, that were installed before you begin the reinstallation.

## 3.2 Accessing the Installation Software

The Oracle Database Client software is available on installation media or you can download it from the Oracle Technology Network website, or the Oracle Software Delivery Cloud portal. To install the software from the hard disk, you must either download it and unpack it, or copy it from the installation media.

You can access and install Oracle Database Client by using one of the following methods:

- To install the software from a installation media or from an existing hard disk location, refer to "Installing the Oracle Database Client Software"
- To copy the software to a hard disk, refer to "Copying the Software to the Hard Disk"
- To download the software from Oracle Technology Network, refer to "Downloading Oracle Software"

### 3.2.1 Downloading Oracle Software

You can download the trial version of the installation files from the Oracle Technology Network (OTN) or the Oracle Software Delivery Cloud portal and extract them on your hard disk. Make sure that you completely review and understand the terms of the license. Most downloads include the development license. This section contains the following topics:

- Downloading the Installation Archive Files from OTN
- Downloading the Software from Oracle Software Delivery Cloud
- Extracting the Installation Files

#### 3.2.1.1 Downloading the Installation Archive Files from OTN

To download the installation archive files from Oracle Technology Network:

1. Use any browser to access the software download page from Oracle Technology Network:
	```
	http://www.oracle.com/technetwork/indexes/downloads/index.html
	```
2. Navigate to the download page for the product to install.
3. On the download page, identify the required disk space by adding the file sizes for each required file.
	The file sizes are listed next to the file names.
4. Select a file system with enough free space to store and expand the archive files.
	In most cases, the available disk space must be at least twice the size of all of the archive files.
5. On the file system that you selected in step [^1], create a parent directory for each product, for example `OraDB11g`, to hold the installation directories.
6. Download all of the installation archive files to the directory that you created in step [^2].
7. Verify that the files you downloaded are the same size as the corresponding files on Oracle Technology Network. Also verify the checksums are the same as noted on Oracle Technology Network using a command similar to the following:
	```
	cksum filename
	.zip
	```
8. Extract the files in each directory that you just created.
9. After you have extracted the required installation files, see "Installing the Oracle Database Client Software".

#### 3.2.1.2 Downloading the Software from Oracle Software Delivery Cloud

You can download the software from Oracle Software Delivery Cloud as Media Packs. A Media Pack is an electronic version of the software that is also available to Oracle customers on CD-ROM or DVD. To download the Media Pack:

1. Use any browser to access the Oracle Software Delivery Cloud portal:
	```
	https://edelivery.oracle.com/
	```
2. Complete the Export Validation process by entering information (name, company, e-mail address, and country) in the online form.
3. In the Media Pack Search page, specify the Product Pack and Platform to identify the Media Pack you want to download. If you do not know the name of the Product Pack, you can search for it using the License List.
4. In the search results page, click Readme to download and review the Readme file for download instructions and product information.
5. After you review the Readme, choose the appropriate Media Pack from the search results to download the individual zip files. Follow the Download Notes instructions in this page. Once you download and extract the contents of the required zip files, proceed with the installation of the software.
	Note:
	Print the page with the list of downloadable files. It contains a list of part numbers and their corresponding descriptions that you may have to reference during the installation process.
6. After you download the files, click View Digest to verify that the MD5 or SHA-1 checksum matches with what is listed in the media download page.

See Also:

- My Oracle Support note 549617.1 for information on how to verify the integrity of a software download at:
	`https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=549617.1`
- Frequently Asked Questions section on the Oracle Software Delivery Cloud portal for more information about Media Packs

#### 3.2.1.3 Extracting the Installation Files

To extract the installation archive files, perform the following steps:

1. If necessary, change to the directory that contains the downloaded installation archive files.
2. Oracle RDBMS software is available as two archive files. Ensure that you extract both the archive files to the same directory.
	If the downloaded file has the `zip` extension, use the following command to extract the content:
	```
	unzip file_name.zip
	```
	If the downloaded file has the `cpio.gz` extension, use the following command:
	```
	$ gunzip filename.cpio.gz
	```
	This command creates files with names similar to the following:
	```
	filename.cpio
	```
	To extract the installation files, enter a command similar to the following:
	```
	$ cpio -idcmv < filename.cpio
	```
	Note:
	Refer to the download page for information about the correct options to use with the `cpio` command.
	Some browsers uncompress files while downloading them, but leave the `.gz` file extension.
	For each file, this command creates a subdirectory named `Disk` `n`, where `n` is the disk number identified in the file name.

When you have extracted all of the required installation files, refer to "Installing the Oracle Database Client Software".

### 3.2.2 Copying the Software to the Hard Disk

Before installing Oracle Database Client, Oracle recommends that you copy the software to the hard disk to enable the installation process to run a bit faster. Before copying the installation media content to the hard disk, you must mount the disk. The following sections describe how to mount the disk and copy its content to the hard disk:

- Mounting Disks
- Copying the Oracle Database Client Software to a Hard Disk

#### 3.2.2.1 Mounting Disks

On most Linux systems, the disk mounts automatically when you insert it into the disc drive. If the disk does not mount automatically, then follow these steps to mount it:

1. If necessary, log in as the `root` user and enter a command similar to one of the following to eject the currently mounted disk, then remove it from the drive:
	- Asianux, Oracle Linux, and Red Hat Enterprise Linux:
		```
		# sudo eject /mnt/dvd
		```
		- SUSE Linux Enterprise Server:
		```
		# eject /media/dvd
		```
	In these examples, `/mnt/dvd` and `/media/dvd` are the mount point directories for the installation media.
2. Insert the appropriate installation media into the disk drive.
3. To verify if the disk is mounted automatically, enter one of the following commands depending on the platform:
	- Asianux, Oracle Linux, and Red Hat Enterprise Linux:
		```
		# ls /mnt/dvd
		```
		- SUSE Linux Enterprise Server:
		```
		# ls /media/dvd
		```
4. Before running the following command, ensure that the `/mnt/dvd` directory exists on Red Hat Enterprise Linux. If not, create the `/mnt/dvd` as required, to mount the installation media.
	If this command fails to display the contents of the installation media, enter a command similar to the following to mount it, depending on the platform:
	- Asianux, Oracle Linux, and Red Hat Enterprise Linux:
		```
		# mount -t iso9660 /dev/dvd /mnt/dvd
		```
		- SUSE Linux Enterprise Server:
		```
		# mount -t iso9660 /dev/dvd /media/dvd
		```
	In these examples, `/mnt/dvd` and `/media/dvd` are the mount point directories for the installation media.
5. If Oracle Universal Installer is displaying the Disk Location dialog box, enter the disk mount point directory path, for example:
	```
	/mnt/dvd
	```

To continue, go to one of the following sections:

- If you want to copy software to a hard disk, refer to "Copying the Oracle Database Client Software to a Hard Disk".
- If you want to install the software from the installation media, refer to "Installing the Oracle Database Client Software".

#### 3.2.2.2 Copying the Oracle Database Client Software to a Hard Disk

If the system does not have a installation media, you can copy the software from the installation media to a file system on another system, then either mount that file system using NFS, or use FTP to copy the files to the system where you want to install the software.

To copy the contents of the installation media to a hard disk:

1. Create a directory on the hard disk to hold the Oracle software:
	```
	$ mkdir OraCl11g
	```
2. Change directory to the directory you created in Step 1:
	```
	$ cd OraCl11g
	```
3. Mount the disk, if it is not mounted.
	Some platforms automatically mount the disk when you insert it into the drive. If the disk does not mount automatically, refer to "Mounting Disks" for information about mounting it.
4. Copy the contents of the mounted disk to the corresponding new subdirectory as follows:
	```
	$ cp -R /directory_path OraCl11g
	```
	In this example, `/` `directory_path` is the disk mount point directory, for example `/mnt/dvd` on Red Hat Enterprise Linux systems, or the path of the client directory on the installation media. The mount point directory is `/dvd`.
5. If necessary, mount the next disk and repeat Step [^3].

## 3.3 Installing the Oracle Database Client Software

Use Oracle Universal Installer to install the Oracle Database Client software. The following sections describes how to install the Oracle software:

- Running Oracle Universal Installer
- Using Oracle Net Configuration Assistant
- Performing an In-place Oracle Database Client Upgrade

See Also:

["Installation Considerations"](install_overview.md) for information you should consider before deciding how to install the client

### 3.3.1 Running Oracle Universal Installer

For any type of installation process, start Oracle Universal Installer and install the software, as follows:

1. Log on as the Oracle software owner user (typically, `oracle`) to the computer on which to install Oracle components.
2. If you are installing the software from installation media, mount the disk if it is not mounted.
	If the disk does not mount automatically, refer to "Mounting Disks" for information about mounting it.
	Some platforms automatically mount the disk when you insert the installation media into the drive.
3. To start Oracle Universal Installer, complete one of the following steps depending on the location of the installation files:
	Note:
	Start Oracle Universal Installer from the terminal session where you logged in as the `oracle` user and set the user's environment.
	See Also:
	["Configuring Oracle Software Owner Environment"](pre_install.md) for information about setting the `oracle` user's environment
	- If the installation files are on disk, enter a command similar to the following, where `directory_path` is the path of the `client` directory on the installation media:
		```
		$ /directory_path/runInstaller
		```
		- If the installation files are on the hard disk, change directory to the `client` directory and enter the following command:
		```
		$ ./runInstaller
		```
		- Starting with Oracle Database 11g Release 2 (11.2.0.2), if you plan to run the installation in a secured data center, then you can download updates before starting the installation by starting Oracle Universal Installer on a system that has Internet access in update download mode. To start Oracle Universal Installer to download the updates, enter the following command:
		```
		$ ./runInstaller -downloadUpdates
		```
		Provide the My Oracle Support user name and password, and provide proxy settings, if needed, in the Provide My Oracle Support credentials screen. Then, enter the Download location and click Download in the Download software updates screen. If updates are available, then they are downloaded in the location provided. The Finish Updates screen shows the successful download of the updates. Click Close.
		After you download the updates, transfer the update file to a directory on the server where you plan to run the installation.
		See Also:
		- [Oracle Universal Installer and OPatch User's Guide for Windows and UNIX](https://docs.oracle.com/cd/E11882_01/em.112/e12255/toc.htm) for information about response file formats
		- ["Software Updates Option"](install_overview.md)
	If Oracle Universal Installer is not displayed, refer to the ["X Window Display Errors"](app_ts.md) for information about troubleshooting.
4. If you have an existing Oracle Database Client 11g Release 2 (11.2) installed on your system, the Select Installation Mode screen is displayed. Select New Install to install Oracle Database Client software in to a new location.
	Starting with Oracle Database 11g Release 2 (11.2.0.2), to upgrade an earlier release of Oracle Database Client, select Upgrade and follow the instructions in "Performing an In-place Oracle Database Client Upgrade".
5. In the Select Installation Type screen, select the type of installation: Instant Client, Administrator, Runtime, or Custom and click Next.
6. Starting with Oracle Database 11g Release 2 (11.2.0.2), you can use the Software Updates feature to dynamically download and apply latest updates. In the Download Software Updates screen, select one of the following options, and click Next:
	- Use My Oracle Support credentials for download: Select this option to download and apply the latest software updates.
		Click Proxy Settings to configure a proxy for Oracle Universal Installer to use to connect to the Internet. Provide the proxy server information for your site, along with a user account that has access to the local area network through which the server is connecting. Starting with Oracle Database 11g Release 2 (11.2.0.3), you can enter the Proxy Realm information. The proxy realm information is case-sensitive. If you do not have a proxy realm, then you do not have to provide an entry for the Proxy Username, Proxy Password, and Proxy Realm fields.
		Click Test Connection to ensure that your proxy settings are correctly entered, and the installer can download the updates.
		- Use pre-downloaded software updates: Select this option to apply the software updates previously downloaded using the `-downloadUpdates` flag.
		- Skip software updates: Select this option if you do not want to apply any updates.
	See Also:
	["Software Updates Option"](install_overview.md)
7. The Apply Software Updates screen is displayed if you select to download the software updates, or provide the pre-downloaded software updates location.
	1. If you selected Use My Oracle Support credentials for download in the previous screen, select Download and apply all updates, and then click Next to apply the updates.
		By default, the download location for software updates is placed in the home directory of the Oracle installation owner you are using to run this installation. If you choose to download the software updates in another location, then click Browse and select a different location on your server.
		2. If you selected Use pre-downloaded software updates in the previous screen, select Apply all updates, and then click Next to apply the updates downloaded before starting the installation.
8. The Select Product Languages screen enables you to select the language in which you want to run the product.
	Select the product language from the Available Languages list, transfer it to the Selected Languages list. Click Next.
	This screen is not displayed if you select Instant Client as the type of installation in Step [^6].
9. In the Specify Installation Location screen, enter the following details:
	Oracle Base: This path appears by default. You can change the path based on your requirement. The Oracle Base section is not displayed if you select Instant Client as the type of installation in Step [^6].
	In the Software Location section, accept the default value or enter the Oracle home directory path in which you want to install Oracle components. The directory path should not contain spaces. Click Next.
	See Also:
	["Identifying Required Software Directories"](pre_install.md) for information about Oracle base directory and Oracle home directory
10. In the Create Inventory screen, you are prompted by the installer to specify the directory path for central inventory the first time you install Oracle Database on your computer.
	Select the oraInventory Group Name of the operating system group that should own the Oracle Inventory directory (the Oracle Inventory group). Click Next.
	Note: By default, the Oracle Inventory directory is not installed under the Oracle Base directory. This is because all Oracle software installations share a common Oracle Inventory, so there is only one Oracle Inventory for all users, whereas there is a separate Oracle Base for each user.
11. If you selected Custom as the type of installation in Step [^6], then the Available Product Components screen is displayed. Select the products to install and click Next.
	Note:
	Starting with Oracle Database 11g Release 2 (11.2), you can install Oracle Connection Manager, Oracle Net Listener, and Oracle Scheduler Agent using the Custom install option.
12. In Step [^9], if you select Oracle Scheduler Agent as one of the components to install, then the Oracle Database Scheduler Agent screen is displayed. Enter the Scheduler Agent Hostname, and the Scheduler Agent Port Number. Click Next.
13. The Perform Prerequisite Checks screen verifies if your computer meets the minimum system requirements to install the desired product. Click Next.
	Note: Oracle recommends that you use caution in checking the Ignore All option. If you check this option, then Oracle Universal Installer may not confirm if your system can install Oracle Database successfully.
14. Review the information displayed in the Summary screen, and click Install.
	Note:
	Starting with Oracle Database 11g Release 2 (11.2), you can save all the installation steps into a response file by clicking Save Response File in the Summary screen. Later, this file can be used for a silent installation.
15. The Install Product screen displays the progress of the client installation. Starting with Oracle Database 11g Release 2 (11.2.0.3), Oracle Universal Installer prompts you to execute the root configuration script only if you selected Oracle Net Listener or Oracle Scheduler Agent using the Custom install option. If prompted, execute the `root.sh` script as the `root` user to complete the installation, and click OK.
16. If you are performing a Custom installation, and selected Oracle Net Listener from the list of components to install in Step [^9], then go to "Using Oracle Net Configuration Assistant" for instructions.
17. In the Finish screen, click Close to exit Oracle Universal Installer.

### 3.3.2 Using Oracle Net Configuration Assistant

During a Custom Oracle Database Client installation, if you select Oracle Net Listener from the list of components to install in Step [^9], then Oracle Universal Installer automatically starts Oracle Net Configuration Assistant as part of the Oracle Database Client installation. Perform the following to configure the listener and naming methods using Oracle Net Configuration Assistant:

1. In the Welcome screen, click Next.
2. In the Listener Configuration screen, enter a Listener name or accept the default value. Click Next.
3. In the Listener Configuration, Select Protocol screen, select one or more protocols from the Available Protocols list, and move it to the Selected Protocols list. Click Next.
4. In the Listener Configuration, TCP/IP Protocol screen, select the standard port number, or enter a different port number. Click Next.
5. Select No if you do not want to configure an additional listener, and click Next.
6. The listener configuration is now complete, click Next to proceed.
7. In the Naming Methods Configuration screen, select Yes to configure naming methods. Click Next.
8. In the Naming Methods Configuration screen, select the naming method you want from the list of Available Naming Methods and move it to the Selected Naming Methods list. Click Next.
	Typically, Local Naming is sufficient.
9. In the Net Service Name Configuration screen, enter Service Name, and click Next.
10. In the Net Service Name Configuration screen, select the protocol for the database you want to access, and click Next.
11. In the Net Service Name Configuration screen, enter the Host name of the computer where the Oracle database is installed. Use the standard port number, or specify a different port number, and click Next.
12. In the Net Service Name Configuration, click Yes to test the database connection. Click Next.
	In most cases, the test fails only because the default user name and password Oracle Universal Installer supplies in the dialog box do not match the user name and password for the target database. Click Change Login, reenter the user name and password, and click OK.
13. In the Connecting screen, click Next.
14. In the Net Service Name Configuration screen, enter the Net Service Name, and click Next.
15. Answer the remaining prompts to complete the configuration.
16. In the Finish screen, click Close to exit Oracle Universal Installer.

You can also run Oracle Net Configuration Assistant after the installation in standalone mode to configure the listener, naming methods, net service names, and directory server usage.

To start Oracle Net Configuration Assistant in standalone mode run `netca` from the `ORACLE_HOME/bin` directory.

### 3.3.3 Performing an In-place Oracle Database Client Upgrade

Starting with Oracle Database 11g Release 2 (11.2.0.2) you can perform an in-place upgrade of Oracle Database Client 11g Release 2 (11.2) using the following instructions:

Note:

You can perform an in-place Oracle Database Client upgrade only if you have an existing Oracle Database Client 11g Release 2 (11.2.0.1) or later client home installed on your system.
1. Perform Steps [^4] through [^5] listed in "Running Oracle Universal Installer".
2. The Select Installation Mode screen is displayed only if you have an existing Oracle Database Client 11g Release 2 (11.2.0.1) or later installed on your system. Select Upgrade to upgrade the existing Oracle Database Client software to the latest version.
3. In the Specify Installation Location screen, accept the default Software Location value or enter the Oracle home directory path in which you want to install Oracle components. The directory path should not contain spaces. Click Next.
4. In the Download Software Updates screen, select one of the following options, and click Next:
	- Use My Oracle Support credentials for download
		- Use pre-downloaded software updates
		- Skip software updates
	See Step [^7] in "Running Oracle Universal Installer" for more information about the options in the Download Software Updates screen.
5. The Apply Software Updates screen is displayed if you select to download the software updates or provide the pre-downloaded software updates location. Select either Download and apply all updates or Apply all updates, as applicable, and click Next.
	See Step [^8] in "Running Oracle Universal Installer" for more information about the options in the Apply Software Updates screen.
6. The Select Product Languages screen enables you to select the language in which you want to run the product.
	Select the product language from the Available Languages list, transfer it to the Selected Languages list. Click Next.
7. The Perform Prerequisite Checks screen verifies if your computer meets the minimum system requirements to install the desired product. Click Next.
8. Review the information displayed in the Summary screen, and click Install.
9. The Install Product screen displays the progress of the client upgrade. Starting with Oracle Database 11g Release 2 (11.2.0.3), Oracle Universal Installer prompts you to execute the root configuration script only if the existing Oracle Database Client home was installed with Oracle Scheduler Agent. If prompted, execute the `root.sh` script as the `root` user to complete the installation, and click OK.
10. Review the information in the Finish screen and click Close to exit Oracle Universal Installer.

[^1]: Select a file system with enough free space to store and expand the archive files.

In most cases, the available disk space must be at least twice the size of all of the archive files.

[^2]: On the file system that you selected in step 4, create a parent directory for each product, for example `OraDB11g`, to hold the installation directories.

[^undefined]: Download all of the installation archive files to the directory that you created in step 5.

[^undefined]: Verify that the files you downloaded are the same size as the corresponding files on Oracle Technology Network. Also verify the checksums are the same as noted on Oracle Technology Network using a command similar to the following:

```
cksum filename
.zip
```

[^undefined]: Extract the files in each directory that you just created.

[^undefined]: After you have extracted the required installation files, see "Installing the Oracle Database Client Software".

[^3]: Copy the contents of the mounted disk to the corresponding new subdirectory as follows:

```
$ cp -R /directory_path OraCl11g
```

In this example, `/` `directory_path` is the disk mount point directory, for example `/mnt/dvd` on Red Hat Enterprise Linux systems, or the path of the client directory on the installation media. The mount point directory is `/dvd`.

[^undefined]: If necessary, mount the next disk and repeat Step 4.

[^4]: Log on as the Oracle software owner user (typically, `oracle`) to the computer on which to install Oracle components.

[^undefined]: If you are installing the software from installation media, mount the disk if it is not mounted.

If the disk does not mount automatically, refer to "Mounting Disks" for information about mounting it.

Some platforms automatically mount the disk when you insert the installation media into the drive.

[^5]: To start Oracle Universal Installer, complete one of the following steps depending on the location of the installation files:

Note:

Start Oracle Universal Installer from the terminal session where you logged in as the `oracle` user and set the user's environment.

See Also:

["Configuring Oracle Software Owner Environment"](pre_install.md) for information about setting the `oracle` user's environment

- If the installation files are on disk, enter a command similar to the following, where `directory_path` is the path of the `client` directory on the installation media:
	```
	$ /directory_path/runInstaller
	```
- If the installation files are on the hard disk, change directory to the `client` directory and enter the following command:
	```
	$ ./runInstaller
	```
- Starting with Oracle Database 11g Release 2 (11.2.0.2), if you plan to run the installation in a secured data center, then you can download updates before starting the installation by starting Oracle Universal Installer on a system that has Internet access in update download mode. To start Oracle Universal Installer to download the updates, enter the following command:
	```
	$ ./runInstaller -downloadUpdates
	```
	Provide the My Oracle Support user name and password, and provide proxy settings, if needed, in the Provide My Oracle Support credentials screen. Then, enter the Download location and click Download in the Download software updates screen. If updates are available, then they are downloaded in the location provided. The Finish Updates screen shows the successful download of the updates. Click Close.
	After you download the updates, transfer the update file to a directory on the server where you plan to run the installation.
	See Also:
	- [Oracle Universal Installer and OPatch User's Guide for Windows and UNIX](https://docs.oracle.com/cd/E11882_01/em.112/e12255/toc.htm) for information about response file formats
	- ["Software Updates Option"](install_overview.md)

If Oracle Universal Installer is not displayed, refer to the ["X Window Display Errors"](app_ts.md) for information about troubleshooting.

[^undefined]: If you have an existing Oracle Database Client 11g Release 2 (11.2) installed on your system, the Select Installation Mode screen is displayed. Select New Install to install Oracle Database Client software in to a new location.

Starting with Oracle Database 11g Release 2 (11.2.0.2), to upgrade an earlier release of Oracle Database Client, select Upgrade and follow the instructions in "Performing an In-place Oracle Database Client Upgrade".

[^6]: In the Select Installation Type screen, select the type of installation: Instant Client, Administrator, Runtime, or Custom and click Next.

[^7]: Starting with Oracle Database 11g Release 2 (11.2.0.2), you can use the Software Updates feature to dynamically download and apply latest updates. In the Download Software Updates screen, select one of the following options, and click Next:

- Use My Oracle Support credentials for download: Select this option to download and apply the latest software updates.
	Click Proxy Settings to configure a proxy for Oracle Universal Installer to use to connect to the Internet. Provide the proxy server information for your site, along with a user account that has access to the local area network through which the server is connecting. Starting with Oracle Database 11g Release 2 (11.2.0.3), you can enter the Proxy Realm information. The proxy realm information is case-sensitive. If you do not have a proxy realm, then you do not have to provide an entry for the Proxy Username, Proxy Password, and Proxy Realm fields.
	Click Test Connection to ensure that your proxy settings are correctly entered, and the installer can download the updates.
- Use pre-downloaded software updates: Select this option to apply the software updates previously downloaded using the `-downloadUpdates` flag.
- Skip software updates: Select this option if you do not want to apply any updates.

See Also:

["Software Updates Option"](install_overview.md)

[^8]: The Apply Software Updates screen is displayed if you select to download the software updates, or provide the pre-downloaded software updates location.

1. If you selected Use My Oracle Support credentials for download in the previous screen, select Download and apply all updates, and then click Next to apply the updates.
	By default, the download location for software updates is placed in the home directory of the Oracle installation owner you are using to run this installation. If you choose to download the software updates in another location, then click Browse and select a different location on your server.
2. If you selected Use pre-downloaded software updates in the previous screen, select Apply all updates, and then click Next to apply the updates downloaded before starting the installation.

[^9]: If you selected Custom as the type of installation in Step 5, then the Available Product Components screen is displayed. Select the products to install and click Next.  

Note:

Starting with Oracle Database 11g Release 2 (11.2), you can install Oracle Connection Manager, Oracle Net Listener, and Oracle Scheduler Agent using the Custom install option.

[^undefined]: In Step 11, if you select Oracle Scheduler Agent as one of the components to install, then the Oracle Database Scheduler Agent screen is displayed. Enter the Scheduler Agent Hostname, and the Scheduler Agent Port Number. Click Next.

[^undefined]: The Perform Prerequisite Checks screen verifies if your computer meets the minimum system requirements to install the desired product. Click Next.

Note: Oracle recommends that you use caution in checking the Ignore All option. If you check this option, then Oracle Universal Installer may not confirm if your system can install Oracle Database successfully.

[^undefined]: Review the information displayed in the Summary screen, and click Install.

Note:

Starting with Oracle Database 11g Release 2 (11.2), you can save all the installation steps into a response file by clicking Save Response File in the Summary screen. Later, this file can be used for a silent installation.