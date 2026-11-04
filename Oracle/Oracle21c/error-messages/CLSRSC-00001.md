---
title: Database Error Messages
book: Database Error Messages
doc_id: F30283-07
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/errmg/CLSRSC-00001.html
tags:
  - oracle
  - 21c
  - error-messages
---

CLSRSC-00001: Insufficient privileges to execute this script

Cause: The script was invoked by a non-root or a non-administrator user.

Action: Run the script as the root or administrative user.

CLSRSC-00003: No value set for the required parameter 'string'

Cause: The required parameter file is missing, or no value is set for the parameter yet.

Action: Use the correct parameter file and provide each paramter with a valid value.

CLSRSC-00004: No value passed as Oracle CRS home

Cause: No value was passed as Oracle CRS home.

Action: None

CLSRSC-00005: The Oracle CRS home 'string' does not exist

Cause: The Oracle CRS home does not exist.

Action: Make sure that the Oracle Grid Infrastructure software is properly installed.

CLSRSC-00006: No value passed as Oracle Clusterware name

Cause: No value was passed as Oracle Clusterware name.

Action: None

CLSRSC-00007: The OCR location file '/etc/oracle/ocr.loc' is corrupted

Cause: The OCR location file '/etc/oracle/ocr.loc' is corrupted.

Action: Make sure that the '/etc/oracle' directory is empty if this is a fresh install.

CLSRSC-00008: No value passed as OCR locations

Cause: No value was passed as OCR locations.

Action: None

CLSRSC-00009: No value passed as OLR locations

Cause: No value was passed as OLR locations.

Action: None

CLSRSC-00010: The VIP resource was not created due to VIP address not available.

Cause: There was an error in obtaining a VIP address from the DHCP server.

Action: Run the command 'cluvfy comp dhcp' to check the DHCP server.

CLSRSC-00011: No value passed for OLR locations

Cause: No value was passed as OLR locations.

Action: None

CLSRSC-00012: The ASM resource ora.asm did not start

Cause: There was an error in starting the ASM resource.

Action: Check the accompanying messages and contact Oracle Support Services.

CLSRSC-00013: The file 'string' does not exist

Cause: The specified file does not exist.

Action: None

CLSRSC-00014: CSS is configured for single instance Oracle databases

Cause: The current configuraiton is for previous installation.

Action: Delete this configuration using the command 'localconfig delete' before proceeding with Oracle RAC configuration.

CLSRSC-00015: No value passed for host name

Cause: No value was passed as the host name.

Action: None

CLSRSC-00016: No value passed for Oracle CRS user

Cause: No value was passed as Oracle crs user.

Action: None

CLSRSC-00017: Invalid GPnP setup

Cause: GPnP directories do not exist.

Action: Make sure that GPnP directories must exist.

CLSRSC-00018: The GPnP peer wallet file 'string' does not exist or is not readable

Cause: The GPnP peer wallet file does not exist or is not readable.

Action: None

CLSRSC-00019: 9i GSD is running on the Cluster nodes (string)

Cause: 9i GSD is running on the Cluster nodes.

Action: Stop the GSD and re-run 'root.sh' on UNIX platforms or 'gridconfig.bat' on Windows.

CLSRSC-00020: Invalid network type in the network specification string 'string'. Only 'public' and 'cluster\_interconnect' are allowed

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00021: No value passed for the directory name

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00022: The directory 'string' does not exist

Cause: The specified directory does not exist.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00023: No value passed for the file name

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00024: No value passed for the host name.

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00025: Unable to find the command 'string' to stop Clusterware

Cause: Cannot stop Clusterware because the required executable file does not exist.

Action: Make sure that the Oracle Grid Infrastructure software is properly installed.

CLSRSC-00026: The file system of 'string' is invalid

Cause: The root is not able to perform any operations on this file system.

Action: Check export options on NAS filer and make sure that the file system is not corrupted.

CLSRSC-00027: The GPnP configuration reader wallet in given directory 'string' is missing

Cause: The setup in GPnP configuration directory is incomplete.

Action: Make sure that the Oracle Grid Infrastructure software is properly installed.

CLSRSC-00028: The GPnP configuration reader wallet in given directory 'string' is invalid

Cause: The setup in GPnP configuration directory is invalid.

Action: Make sure that the Oracle Grid Infrastructure software is properly installed.

CLSRSC-00029: Invalid GPnP configuration directories. The cluster-wide 'string' and node-specific 'string' must be different

Cause: Invalid configuration was found while verifying the GPnP local and cluster-wide setup.

Action: None

CLSRSC-00030: No parameters specified to query from GPnP profile 'string'

Cause: The required parameters were not supplied while querying from GPnP profile.

Action: None

CLSRSC-00031: GPnP profile signature verification failed

Cause: The signature status string was not found in the output of 'gpnptool' execution.

Action: If error persists, contact Oracle Support Services.

CLSRSC-00032: The 'string' file is not readable

Cause: No read access to the specified file.

Action: Check the permissons on this file and make sure it is readable.

CLSRSC-00033: The OLR from version 'string' is missing or unusable for upgrade

Cause: Invalid OLR file was found during upgrade.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00034: IPv6 is currently not supported

Cause: Attempt was made to use IPv6.

Action: None

CLSRSC-00035: The value set for the parameter 'CRS\_NODEVIPS' is null

Cause: No value set for the parameter 'CRS\_NODEVIPS'.

Action: Set 'CRS\_NODEVIPS' parameter in 'crsconfig\_params' and re-run 'rootupgrade.sh'. The format is as follows: CRS\_NODEVIPS='node1-vip/ node1-netmask/node1-interface,node2-vip/node2-netmask/ node2-interface'.

CLSRSC-00036: The file 'string' does not exist to proceed with deconfiguration

Cause: Some files are missing in the Grid Infrastructure Home.

Action: Contact Oracle Support Services.

CLSRSC-00037: Run the deconfiguration script with a -force option.

Cause: The deconfiguration failed due to a missing file.

Action: Perform the deconfiguration using the -force option and manually stop any processes running from the GI home.

CLSRSC-00038: Oracle Clusterware stack is not active on this node

Cause: Oracle Clusterware is not running on this node.

Action: Restart the Clusterware stack using 'crsctl start crs' and retry.

CLSRSC-00039: Oracle Restart stack is not active on this node

Cause: Oracle SIHA stack is not running on this node.

Action: Restart the SIHA stack using 'crsctl start has' and retry.

CLSRSC-00040: No value passed for owner name

Cause: Internal error.

Action: Contact Oracle Support Services.

CLSRSC-00041: No value passed for group name

Cause: Internal error.

Action: Contact Oracle Support Services.

CLSRSC-00042: No value passed for the file or directory name

Cause: Internal error.

Action: Contact Oracle Support Services.

CLSRSC-00043: No value passed for permissions

Cause: Internal error.

Action: Contact Oracle Support Services.

CLSRSC-00044: The init script file name passed is null

Cause: Internal error.

Action: Contact Oracle Support Services.

CLSRSC-00045: The init script file 'string' does not exist

Cause: Internal error.

Action: Contact Oracle Support Services.

CLSRSC-00046: Error: 'string' does not exist

Cause: The specified file or directory does not exist.

Action: None

CLSRSC-00047: The Oracle Home User string does not match the Oracle Home User string of the Grid Infrastructure homes currently in use in this cluster.

Cause: An attempt to switch to a different Grid Infrastructure home was rejected because the Oracle Home User of the destination home did not match the Oracle Home User of the Grid Infrastructure homes currently in use for the cluster.

Action: Specify a destination Grid Infrastructure home with the current Oracle Home User.

CLSRSC-00048: Failure in execution, multi-line command is not supported.

Cause: Internal error.

Action: Contact Oracle Support Services.

CLSRSC-00049: Directory in which to create Oracle Notification Server wallet does not exist.

Cause: The root script did not find the directory to create Oracle Notification Server wallet.

Action: Examine the root script logs for errors during the creation of the directory such as lack of space or permissions, rectify the errors and rerun the root script.

CLSRSC-00050: failed to create wallet for use by Oracle Notification Service (ONS)

Cause: The root script was unable to write the ONS wallet file in the wallet directory.

Action: Examine the root script logs for errors during the creation of the wallet, such as lack of space or permissions, rectify the errors and rerun the root script.

CLSRSC-00051: failed to add certificate to wallet to be used by Oracle Notification Service (ONS)

Cause: This is an internal error.

Action: Contact Oracle Support Services.

CLSRSC-00052: failed to get the HAIP address

Cause: An attempt to get the HAIP address using ifconfig failed.

Action: Examine the accompanying error messages.

CLSRSC-00101: Could not copy OCR locations

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00102: Could not delete the OLR file 'string' (error: string)

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00103: An error occurred while accessing the file 'string'

Cause: The specified file does not exist or is not readable.

Action: Make sure the file exists and it has read and execute access.

CLSRSC-00104: Could not execute 'string -g' and read output (error: string)

Cause: Unable to execute the specified command.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00105: Failed to copy 'string' to 'string' (error: string)

Cause: An error occurred while copying the specified file.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00106: Copy of older local-only OCR failed

Cause: An error occurred while copying over older local-only OCR to SIHA home.

Action: None

CLSRSC-00107: Start of GNS failed

Cause: This is a status message.

Action: None

CLSRSC-00108: Failed to start VIP on node 'string'

Cause: This is a status message.

Action: None

CLSRSC-00109: Start of ASM diskgroup failed

Cause: This is a status message.

Action: None

CLSRSC-00110: Failed to start the specified SCAN VIP

Cause: This is a status message.

Action: None

CLSRSC-00111: Failed to start the specified SCAN listener

Cause: This is a status message.

Action: None

CLSRSC-00112: Start of the CVU resource failed

Cause: This is a status message.

Action: None

CLSRSC-00113: Start of ASM instance failed

Cause: This is a status message.

Action: None

CLSRSC-00114: Force stop of ASM instance failed

Cause: This is a status message.

Action: None

CLSRSC-00115: Start of resource 'string' failed

Cause: This is a status message.

Action: None

CLSRSC-00116: Stop of resource 'string' failed

Cause: This is a status message.

Action: None

CLSRSC-00117: Failed to start Oracle Clusterware stack from the Grid Infrastructure home string

Cause: An error occurred while starting Oracle Clusterware stack.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00119: Start of the exclusive mode cluster failed

Cause: Internal error.

Action: If the problem persists, Contact Oracle Support Services

CLSRSC-00120: Timed out waiting for the CRS stack to start

Cause: Internal error.

Action: If the problem persists,contact Oracle Support Services.

CLSRSC-00121: Timed out waiting for the GPNPD to start

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00122: Failed to create a root wallet for Oracle Cluster GPnP

Cause: Internal error.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00123: Failed to create a root certificate for Oracle Cluster GPnP

Cause: Internal error.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00124: Failed to export root certificate for Oracle Cluster GPnP

Cause: Internal error.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00125: Failed to create a peer wallet for Oracle Cluster GPnP

Cause: Internal error.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00126: Failed to create a profile reader wallet for Oracle Cluster GPnP

Cause: Internal error.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00127: Failed to create a provisioning authority wallet for Oracle Cluster GPnP

Cause: Internal error.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00128: Failed to make a peer wallet for Oracle Cluster GPnP. Could not add private key to a wallet

Cause: Internal error.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00129: Failed to make a provisioning authority wallet for Oracle Cluster GPnP. Could not add private key to a wallet.

Cause: Internal error.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00130: Failed to make a peer wallet for Oracle Cluster GPnP. Could not export a certificate request from a wallet.

Cause: Internal error.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00131: Failed to make a provisioning authority wallet for Oracle Cluster GPnP. Could not export a certificate request from a wallet.

Cause: Internal error.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00132: Failed to make a peer wallet for Oracle Cluster GPnP. Could not create a peer certificate.

Cause: Internal error.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00133: Failed to make a provisioning authority wallet for Oracle Cluster GPnP. Could not create a PA certificate.

Cause: Internal error.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00134: Failed to make a peer wallet for Oracle Cluster GPnP. Could not add a root TP certificate.

Cause: Internal error.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00135: Failed to make a profile reader wallet for Oracle Cluster GPnP. Could not add a root TP certificate.

Cause: Internal error.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00136: Failed to make a provisioning authority wallet for Oracle Cluster GPnP. Could not add a root TP certificate.

Cause: Internal error.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00137: Failed to make a peer wallet for Oracle Cluster GPnP. Could not add a PA TP certificate.

Cause: Internal Error.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00138: Failed to make a provisioning authority wallet for Oracle Cluster GPnP. Could not add a peer TP certificate.

Cause: Internal error.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00139: Failed to make a profile reader wallet for Oracle Cluster GPnP. Could not add a PA TP certificate.

Cause: Internal error.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00140: Failed to make a profile reader wallet for Oracle Cluster GPnP. Could not add a peer TP certificate.

Cause: Internal error.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00141: Failed to make a peer wallet for Oracle Cluster GPnP. Could not add a PA TP certificate.

Cause: Internal error.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00142: Failed to make a provisioning authority wallet for Oracle Cluster GPnP. Could not add a peer TP certificate.

Cause: Internal error.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00143: Failed to string a peer profile for Oracle Cluster GPnP using 'gpnptool' (error code string)

Cause: Internal error.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00144: Failed to sign a peer profile for Oracle Cluster GPnP using 'gpnptool' (error code string)

Cause: Internal error.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00145: Failed to verify a peer profile 'string' with WRL='string' using 'gpnptool' (error code string)

Cause: Internal error.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00146: Failed to take cluster-wide GPnP setup as local

Cause: Internal error.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00147: Failed to get parameter values from GPnP profile 'string'

Cause: Internal error.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00148: Errors occurred while setting GPnP wallets ownership/permissions

Cause: Failed to set GPnP wallets ownership/permissions.

Action: None

CLSRSC-00149: Creation of Oracle GPnP wallets failed for host 'string'

Cause: Failed to create Oracle GPnP wallets for the specified host.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00150: Creation of Oracle GPnP peer profile failed for host 'string'

Cause: Failed to create Oracle GPnP peer profile for the specified host.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00151: Failed to promote local GPnP setup to other cluster nodes

Cause: Internal error.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00152: Could not set ownership on 'string'

Cause: Failed to set ownership on the specified file or directory.

Action: None

CLSRSC-00153: Could not set permissions on 'string'

Cause: Failed to set permissions on the specified file or directory.

Action: None

CLSRSC-00154: Check of resource "string" failed

Cause: Internal error.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00155: Replace of older local-only OCR failed

Cause: Internal error.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00156: Error creating local-only OCR

Cause: Internal error.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00157: Failed to create Oracle Cluster Registry configuration

Cause: Internal error.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00158: Failed to reset the OCR location in 'srvconfig.loc' file

Cause: Internal error.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00159: Failed to initialize Oracle Cluster Registry for cluster

Cause: Internal error.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00160: Failed to create local-only OCR using the command 'string'

Cause: Internal error.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00161: Pin node using the command 'string' failed

Cause: Internal error.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00162: Upgrade of ASM Windows Service failed

Cause: Internal error.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00163: ASM rolling upgrade action failed

Cause: Internal error.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00164: ASM upgrade failed

Cause: Internal error.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00165: Backup of file 'string' failed

Cause: The copy of the file to a backup file failed.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00166: Failed to stop or deconfigure older version Cluster Support Services daemon.

Cause: There was an error during the operation.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00167: Restore of file 'string' failed

Cause: The copy of the file from a backup file failed.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00168: Could not delete the file 'string' (error: string)

Cause: Unable to delete the specified file.

Action: None

CLSRSC-00169: Failed to create or upgrade OLR

Cause: The 'ocrconfig -local -upgrade' command failed.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00170: Failed to deconfigure Oracle ASM (error code string)

Cause: Internal error.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00171: Failed to get a list of CSS nodes from OCR

Cause: Internal error.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00172: Failed to get a list of interfaces from OCR

Cause: Internal error.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00173: Error: string \\nError getting networks interface information using 'oifcfg'

Cause: Internal error.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00174: Error: string \\nAn error occurred while executing the command 'olsnodes'

Cause: Internal error.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00175: Failed to write the checkpoint 'string' with status 'string' (error code string)

Cause: An attempt to execute the root script failed because of a failure to write the indicated checkpoint file. Additional failure information is provided in the accompanying messages.

Action: Correct the problem indicated in the accompanying messages and retry.

CLSRSC-00176: Failed to write contents of pfile 'string' for checkpoint 'string' (error code string)

Cause: Internal error.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00177: Failed to add (property/value):('string'/'string') for checkpoint 'string' (error code string)

Cause: Internal error.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00178: Failed to get property value for property 'string' for checkpoint 'string' (error code string)

Cause: Internal error.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00179: Failed to get value of 'string' for checkpoint 'string' (error code string)

Cause: Internal error.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00180: An error occurred while executing the command 'string'

Cause: Failed to execute the indicated command. Additional failure information is provided in the accompanying messages.

Action: Correct the problem indicated in the accompanying messages and retry.

CLSRSC-00181: Failed to find earlier version database home

Cause: Internal error.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00182: Failed to add the resource for ASM diskgroup 'string'

Cause: An internal error occurred while creating the ASM diskgroup resource.

Action: Contact Oracle Support Services.

CLSRSC-00183: OCR manual backup operation failed (error code string)

Cause: Internal error.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00184: Configuration of ASM failed

Cause: Errors occurred while configuring ASM via 'asmca'.

Action: See 'asmca' logs for details. If the problem persists, contact Oracle Support Services.

CLSRSC-00185: Could not open file string (error: string)

Cause: An error occurred while attempting to open a specified file.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00186: Failed to copy file from local path 'string' to remote path 'string' for given list of nodes 'string'

Cause: Internal error.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00187: Failure with signal 'string' from command 'string'

Cause: Internal error.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00188: Failed to create keys in Oracle Local Registry

Cause: Internal error.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00189: Failed to add type 'ora.registry.acfs.type'

Cause: Internal error.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00190: Failed to add resource 'ora.registry.acfs'

Cause: Internal error.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00191: Failed to stop Oracle Clusterware stack

Cause: An error occurred while stopping Oracle Clusterware stack.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00192: Unable to stop Oracle Restart

Cause: Internal error.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00193: Platform-specific setup failed

Cause: Internal error.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00195: Failed to create OHASD resources for cluster and ASM

Cause: An error occurred while adding OHASD resource types and resources.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00196: ACFS driver install actions failed

Cause: An error occurred while installing ACFS drivers using the 'acfsroot install' command.

Action: Examine the accompanying messages from the 'acfsroot install' command, correct the problem and retry.

CLSRSC-00197: Cluster configuration upgrade failed

Cause: This is a status message.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00198: Initial cluster configuration failed

Cause: This is a status message.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00199: Timed out waiting for OHASD to start

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00200: Failed to create HA resources for HAS daemon and ASM

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00201: Failed to start CSS daemon

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00202: Failed to start EVM daemon

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00203: Failed to stop resources from database home 'string'

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00204: Failed to downgrade OCR to version 'string'

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00205: Failed to uninstall ADVM/ACFS

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00206: Could not open file string for reading (error: string)

Cause: An error occurred while attempting to open a specified file for reading.

Action: Check that the file exists and has the proper permissions.

CLSRSC-00207: Could not open file string for writing (error: string)

Cause: An error occurred while attempting to open a specified file for writing.

Action: Check that the file exists and has the proper permissions.

CLSRSC-00208: Could not open file string for appending (error: string)

Cause: An error occurred while attempting to open a specified file for appending.

Action: Check that the file exists and has the proper permissions.

CLSRSC-00209: Could not move 'string' to 'string' (error: string)

Cause: An error occurred while moving the specified file.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00210: Current Oracle Cluster Registry location 'string' in file 'string' and the diskgroup 'string' do not match

Cause: Internal error.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00211: Current Oracle Cluster Registry mirror location 'string' in file 'string' and the diskgroup 'string' do not match

Cause: Internal error.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00213: Failure in reading file 'string' (error: string)

Cause: Internal error.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00214: Failed to start the resource 'string'

Cause: Internal error.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00215: Could not open file 'string' to read permisisons (error: string)

Cause: Internal error.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00216: Insufficient free space available in Cluster Health Monitor repository 'string'

Cause: The available space was less than the minimum space required (1024 MB).

Action: Run the command 'oclumon manage -repos reploc <new\_path>' to change Cluster Health Monitor repository and make sure its free space meets the minimum requirement.

CLSRSC-00217: Could not open file 'string' to write permisisons (error: string)

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00218: Failed to install the OHASD startup script (error: string)

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00219: Unable to get Oracle owner for the home 'string'

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00220: Unable to retrieve database home information

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00221: The patch 'string' apply failed for home 'string'

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00222: The patch 'string' apply successful for home 'string'

Cause: This is a status message.

Action: None

CLSRSC-00223: The patch 'string' rollback failed for home 'string'

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00224: The patch 'string' rollback successful for home 'string'

Cause: This is a status message.

Action: None

CLSRSC-00225: The prepatch execution for database home failed

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00226: The postpatch execution for database home failed

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00227: Patch information file 'string' does not exist. Not a valid GI Bundle patch.

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00228: Timed out waiting for server assignments

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00242: Failed to start Oracle Grid Plug and Play (GPnP) component

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00243: Failed to upgrade the voting disks for Cluster Synchronization Service

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00244: Failed to start Cluster Synchronization Service in clustered mode

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00245: Failed to start Cluster Time Synchronization Service (CTSS)

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00246: HAIP startup failure considered fatal, terminating...

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00247: Failed to start ASM

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00248: Failed to upgrade Oracle Clusterware Repository

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00249: Failed to start Cluster Ready Services

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00250: Failed to start Event Manager

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00251: Oracle Clusterware stack start initiated but failed to complete

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00252: Old CRS Home directory is invalid

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00253: Failed to call 'gethostbyname' with the argument 'string' (error: string)

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00254: Could not create the directory 'string' (error: string)

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00255: Could not create the file 'string' (error: string)

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00256: Could not eval string: string

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00257: Cluster Time Synchronization Service start in exclusive mode failed

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00258: Failed to configure and start ASM

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00259: Oracle Clusterware Repository configuration failed

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00260: Clusterware exclusive mode start of Cluster Ready Services failed

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00261: Failed to add voting disks

Cause: An attempt to add voting disks failed.

Action: Contact Oracle Support Services.

CLSRSC-00262: Failed to promote local GPnP setup to other cluster nodes

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00267: CSS could not exit exclusive mode

Cause: An attempt to stop running OHASD resources failed.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00268: ORACLE\_HOME is not set in the environment

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00269: Failed to add base type cluster\_resource

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00270: Failed to register Clusterware type 'string'

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00271: Failed to add resource 'string'

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00272: Could not close file 'string' (error: string)

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00273: Failed to register the resource 'string' with the OHASD

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00274: Mismatching host to VIP IPs specified

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00275: No more elements in crs\_nodevip\_list

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00276: Unable to get VIP info for new node

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00277: Failed to perform new node configuration

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00278: Failed to perform last node configuration for upgrade

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00279: Failed to perform first node non rolling asm upgrade tasks for cluster

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00280: Failed to perform first node tasks for cluster modeling upgrade

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00281: Failed to set active version of Oracle Clusterware

Cause: An error occurred while executing the 'crsctl set crs activeversion' command.

Action: Correct the problem indicated in the accompanying messages, and then retry.

CLSRSC-00284: Failed to perform last node tasks for cluster modeling upgrade

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00285: Failed to perform upgrade configuration from old 11.2 install

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00286: Failed to add Grid Infrastructure node applications

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00287: FirstNode configuration failed

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00288: Failed to start Grid Infrastructure node applications

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00289: Could not get existing VIP information

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00290: Error: validation of Single Instance CSS failed

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00291: Error: validation of 9i GSD failed

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00292: Error: validation of OLR config failed

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00293: Error: validation of OCR location 'string' failed

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00294: CSS cannot be run in realtime mode

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00296: No configuration parameter file was specified

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00297: Configuration parameter file 'string' could not be found

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00298: The Oracle CRS home path not found in the configuration parameters

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00299: The configuration parameter file 'string' is not valid

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00300: Parameter 'string' not defined

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00301: Error in validate\_ocrconfig

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00302: Unable to delete old services

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00303: Cannot complete the upgrade without the voting file list

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00304: Failed to upgrade ASM for Oracle Restart configuration

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00305: Failed to upgrade ASM in a rolling fashion for Oracle Clusterware configuration

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00306: Failed to upgrade ASM in a nonrolling fashion for Oracle Clusterware configuration

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00307: Failed to upgrade ASM service a rolling fashion for Oracle clusterware configuration

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00308: Failed to get non-FQDN host name

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00309: Failed to get node network interfaces, error: (string)

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00310: Could not open log file string for append (error: string)

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00311: Failed to verify resources

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00312: Failed to verify HA resources

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00313: Error: 'string' is an unknown Operating System

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00314: Failed to call 'tolower\_host' (error: string)

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00315: Clusterware configuration check failed

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00316: OLR configuration failed

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00317: Failed to register Oracle OHASD service

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00318: Failed to start Oracle OHASD service

Cause: An attempt to start the Oracle OHASD service failed.

Action: Check the alert log and the accompanying messages and retry after correcting the problem.

CLSRSC-00319: Unable to stop running CSS

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00320: Migration of older version local\_only to SIHA failed

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00323: Error: readlink failed (error: string)

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00324: Could not open old init.cssd

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00325: Configure Oracle Grid Infrastructure for a Cluster... succeeded

Cause: This is a status message.

Action: None

CLSRSC-00326: Configure Oracle Grid Infrastructure for a Cluster... failed

Cause: Internal error.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00327: Successfully configured Oracle Restart for a standalone server

Cause: This is a status message.

Action: None

CLSRSC-00328: Removing Clusterware entries in file 'string'

Cause: This is a status message.

Action: None

CLSRSC-00329: Replacing Clusterware entries in file 'string'

Cause: This is a status message.

Action: None

CLSRSC-00330: Adding Clusterware entries to file 'string'

Cause: This is a status message.

Action: None

CLSRSC-00331: Failure initializing entries in file 'string'

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00332: CRS resources for listeners are still configured

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00333: Failed to remove database listener

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00334: Failed to remove database listener, but continuing to deconfigure with force option

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00335: Successfully downgraded Oracle Clusterware stack on this node

Cause: This is a status message.

Action: None

CLSRSC-00336: Successfully deconfigured Oracle Clusterware stack on this node

Cause: This is a status message.

Action: None

CLSRSC-00337: Successfully deconfigured Oracle Restart stack

Cause: This is a status message.

Action: None

CLSRSC-00338: Successfully downgraded OCR to version string

Cause: This is a status message.

Action: None

CLSRSC-00348: The Oracle Restart stack failed to stop

Cause: There was a failure in stopping the Oracle Restart stack.

Action: Stop the stack with 'crsctl stop has -f' and rerun the root script.

CLSRSC-00349: The Oracle Clusterware stack failed to stop

Cause: There was a failure in stopping the Oracle Clusterware stack.

Action: Stop the stack with 'crsctl stop crs -f' and rerun the root script.

CLSRSC-00350: Cannot configure two CRS instances on the same cluster

Cause: CRS is already configured on this node.

Action: Must deconfigure before proceeding with the configuration of new home.

CLSRSC-00351: Improper Oracle Clusterware configuration found on this host

Cause: There was an existing configuration found.

Action: Deconfigure the existing cluster configuration before starting to configure a new Clusterware.

CLSRSC-00352: CRS is already configured on this node for the CRS home location string

Cause: There was an attempt to configure the cluster when the cluster is already configured.

Action: None

CLSRSC-00353: Run 'string/crs/install/string -deconfig' to deconfigure existing failed configuration and then re-run 'string'

Cause: There was an attempt to configure the cluster when a prior failed configuration was not cleaned up.

Action: Perform the action specified in the message.

CLSRSC-00354: Error: invalid interface

Cause: Internal error.

Action: Contact Oracle Support Services.

CLSRSC-00355: Error: Cannot change directory to 'string', invalid Berkeley Database path

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00356: Error in opening directory 'string'

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00357: Failed to stop current Oracle Clusterware stack during upgrade

Cause: An error occurred while executing the 'crsctl stop crs -f' command from the current CRS home.

Action: Either manually stop the current Oracle Clusterware stack or reboot the local node to properly clean up the processes started by Oracle Clusterware, and then rerun rootupgrade.sh.

CLSRSC-00359: Unable to get owner information for the executable string

Cause: This is an internal error.

Action: Contact Oracle Support Services.

CLSRSC-00360: Owner 'string' of the old CRS home differs from owner 'string' of the new CRS home

Cause: The new CRS home was installed as the wrong OS user.

Action: Install the new CRS home as the owner of the old CRS home.

CLSRSC-00361: The Oracle Cluster Repository (OCR) check failed

Cause: This is an internal error.

Action: Contact Oracle Support Services.

CLSRSC-00362: The pre-upgrade checks failed, aborting the upgrade

Cause: One or more pre-upgrade checks failed. This message is accompanied by others providing details of the error.

Action: Correct the problem indicated by the accompanying messages and retry.

CLSRSC-00363: User ignored prerequisites during installation

Cause: Informational message.

Action: None

CLSRSC-00364: Failed to propagate ASM credentials to the other nodes

Cause: An attempt to copy the ASM credentials to all remote cluster nodes failed

Action: Contact Oracle Support Services.

CLSRSC-00365: Failed to create credentials for ASM on the local node

Cause: Internal Error

Action: Contact Oracle Support Services.

CLSRSC-00366: Failed to import credentials for ASM

Cause: Internal Error

Action: Contact Oracle Support Services.

CLSRSC-00367: The value set for the parameter 'GNS\_ADDR\_LIST' is null

Cause: No GNS address was found while configuring the big cluster discovery address.

Action: Contact Oracle Support Services.

CLSRSC-00368: Failed to set the node role 'string' for the local node

Cause: An error occurred while executing the 'crsctl set node role' command.

Action: Examine the accompanying messages from the 'crsctl set node role' command, correct the problem and retry.

CLSRSC-00370: Cloud Cluster requires Cloud ASM Server

Cause: Cloud ASM Server was not configured in the cluster.

Action: Contact Oracle Support Services.

CLSRSC-00371: Failed to add flex ASM configuration

Cause: An error occurred while executing the 'srvctl add asm -flex' command.

Action: Correct the problem indicated in the accompanying messages, and then retry.

CLSRSC-00372: Failed to enable ASM proxy configuration

Cause: An error occurred while executing the 'srvctl enable asm -proxy' command.

Action: Correct the problem indicated in the accompanying messages, and then retry.

CLSRSC-00373: Failed to start ASM proxy instance

Cause: An error occurred while executing the command 'srvctl start asm -proxy'. The accompanying messages provide detailed failure information.

Action: Correct the problems indicated in the accompanying messages, and retry the operation.

CLSRSC-00375: Failed to copy ASM credentials to the GPnP directory

Cause: An error occurred while processing a copy operation.

Action: Correct the problem indicated in the accompanying messages, and then retry.

CLSRSC-00376: Failed to get the configured node role for the node string

Cause: An error occurred while executing the 'crsctl get node role config -node nodename' command.

Action: Examine the accompanying messages from the 'crsctl get node role config -node nodename' command, correct the problem and retry.

CLSRSC-00377: Failed to create ASM credential domains

Cause: An error occurred while executing the 'crsctl add credmaint -path -ASM \[-local\]' command.

Action: Contact Oracle Support Services.

CLSRSC-00378: Failed to get the configured node role for the local node

Cause: An error occurred while executing the 'crsctl get node role config' command.

Action: Examine the accompanying messages from the 'crsctl get node role config' command, correct the problem and retry.

CLSRSC-00379: Invalid path for the password file used by ASM

Cause: The path for the password file used by ASM was not properly set in ASM configuration.

Action: Contact Oracle Support Services.

CLSRSC-00380: Failed to create the Rapid Home Provisioning Server credential domain

Cause: An error occurred while executing the 'crsctl add credmaint -path GRIDHOME' command.

Action: Contact Oracle Support Services.

CLSRSC-00381: Failed to create the Grid Plug and Play (GPnP) credential domain

Cause: The reason for this issue was one of the following: - The 'crsctl add credmaint -path <path\_name>' command failed because the requesting user was not root (UNIX) or Administrator (WINDOWS). - An internal error occurred while executing the 'crsctl add credmaint -path /gpnp' command.

Action: (a) Check if the command 'crsctl add credmaint -path <path\_name>' is requested by the root(UNIX) or Administrator (WINDOWS). (b) Contact Oracle Support Services.

CLSRSC-00398: Failed to retrieve old Grid Infrastructure home location during upgrade

Cause: An attempt to locate the previous version Oracle Clusterware home location failed during upgrade, possibly because its configuration was corrupt or removed.

Action: Contact Oracle Support Services.

CLSRSC-00399: Failed to retrieve the network configuration during upgrade

Cause: Private interconnect configuration could not be retrieved from the previous version Oracle Clusterware, possibly because its configuration was corrupt or removed.

Action: Contact Oracle Support Services.

CLSRSC-00400: A system reboot is required to continue installing.

Cause: The installation of new drivers requires a node reboot to continue the install.

Action: Reboot the node and rerun the install or patch configuration step.

CLSRSC-00404: Failed to upgrade Cluster Health Monitor service in rolling fashion for Oracle Clusterware configuration.

Cause: This is an internal error.

Action: Contact Oracle Support Services.

CLSRSC-00405: Unable to access old configuration file string of Cluster Health Monitor.

Cause: Old Cluster Health Monitor configuration file was absent.

Action: None

CLSRSC-00406: Failed to find new administrative directory string of Cluster Health Monitor.

Cause: This is an internal error.

Action: Contact Oracle Support Services.

CLSRSC-00408: Failed to create new configuration file string of Cluster Health Monitor.

Cause: New configuration file of Cluster Health Monitor could not be created.

Action: Ensure that you have the required OS authority or permissions for creating the indicated file.

CLSRSC-00409: Failed to patch Cluster Health Monitor service for Oracle Clusterware configuration.

Cause: This is an internal error.

Action: Contact Oracle Support Services.

CLSRSC-00410: Cannot change directory to 'string'.

Cause: During OCFS upgrade, an attempt to change to the indicated file system directory failed.

Action: Ensure that the directory ORACLE\_HOME\\cfs exists

CLSRSC-00411: A system reboot is required before using OCFS.

Cause: The existing OCFS driver could not be unloaded.

Action: Reboot the local node.

CLSRSC-00412: Failed to enable CRS after successfully installing the ACFS drivers.

Cause: After successfully configuring ACFS during an install, upgrade, or patch, the root script failed to enable CRS again, using the command 'crsctl enable crs'.

Action: Correct the errors accompanying the failure of the enable command and rerun the install configuration step.

CLSRSC-00413: Failed to disable CRS in preparation for a node reboot.

Cause: After a failure to install ACFS drivers, CRS is disabled. This allows the user to reboot and install the drivers for the new version successfully.

Action: Correct the errors accompanying the failure of the disable command, run 'crsctl disable crs', reboot, and continue the install configuration step.

CLSRSC-00415: Failed to delete voting disks

Cause: An attempt to delete voting disks failed.

Action: Contact Oracle Support Services.

CLSRSC-00416: Failed to retrieve old Grid Infrastructure configuration data during downgrade

Cause: An attempt to collect the older version Oracle Clusterware configuration data failed during downgrade, possibly because the upgrade of the first node had not reached a point where the configuration had been modified, or the configuration was corrupt or had been removed.

Action: Rerun rootupgrade.sh. Contact Oracle Support Services if the problem persists.

CLSRSC-00418: Failed to create the ADVM volume resource for device string.

Cause: An error occurred while executing the 'srvctl add volume' command.

Action: Correct the problem indicated in the accompanying messages and retry.

CLSRSC-00419: An error occurred attempting to query the volume resource.

Cause: An error occurred while executing the 'srvctl status volume' command.

Action: Correct the problem indicated in the accompanying messages and retry.

CLSRSC-00420: The ACFS registration for device 'string' on mount path 'string' could not be registered with CRS.

Cause: An error occurred while executing the 'acfsutil registry -a' command.

Action: Correct the problem indicated in the accompanying messages and retry.

CLSRSC-00421: An error occurred attempting to query the file system resource.

Cause: An error occurred while executing the 'srvctl status // filesystem' command.

Action: Correct the problem indicated in the accompanying messages and retry.

CLSRSC-00422: Failed to perform ACFS registry upgrade.

Cause: An error occurred while performing the ACFS registry upgrade.

Action: Correct the problem indicated in the accompanying messages and retry.

CLSRSC-00423: Failed to stop database listener

Cause: An error occurred while stopping the database listener.

Action: Try to stop the database listener manually using 'srvctl stop listener' command.

CLSRSC-00424: Failed to stop database listener, but continuing to deconfigure with force option

Cause: An error occurred while stopping the database listener.

Action: None

CLSRSC-00425: Failed to create the ACFS drivers resource but continuing with the installation

Cause: An error occurred while creating the ACFS drivers resource.

Action: Check if your OS kernel is supported and run 'acfsroot enable' to create and start the ACFS drivers resource.

CLSRSC-00426: Failed to create and start the ACFS drivers resource but continuing with the patching

Cause: An error occurred while creating and starting the ACFS drivers resource.

Action: Check if your OS kernel is supported and run 'acfsroot enable' to create and start the ACFS drivers resource.

CLSRSC-00427: failed to remove OCR file string on ASM using command string

Cause: An error occurred while executing the 'asmcmd rm' command.

Action: Examine the accompanying messages, correct the problem and retry.

CLSRSC-00428: Existing OCR configuration found, aborting the configuration. Rerun configuration setup after deinstall.

Cause: While configuring a new cluster, OCR was found to be already configured.

Action: Deinstall and rerun configuration setup.

CLSRSC-00429: The Oracle Clusterware force upgrade was aborted

Cause: One or more pre-upgrade checks failed.

Action: Address the issues reported by accompanying messages and follow the suggested action.

CLSRSC-00430: Failed to start rolling patch mode

Cause: An error occurred while executing the 'crsctl start rollingpatch' command.

Action: Examine the accompanying messages, correct the problem and retry.

CLSRSC-00431: Failed to stop rolling patch mode

Cause: An error occurred while executing the 'crsctl stop rollingpatch' command.

Action: Examine the accompanying messages, correct the problem and retry.

CLSRSC-00432: Invalid destination CRS home

Cause: The CRS home specified by '-dstcrshome' was identical to the current CRS home.

Action: Remove '-dstcrshome path to CRS home' from the command line or specify a different CRS home.

CLSRSC-00433: This command is deprecated and has been replaced by 'rootcrs.pl -postpatch'

Cause: A deprecated command was issued.

Action: Use 'rootcrs.pl -postpatch'. See usage for complete command line options.

CLSRSC-00434: An operating system reboot is required to continue the deconfiguration.

Cause: The uninstall of the ACFS drivers failed. An operating system reboot is required to continue the deconfiguration.

Action: Reboot the node and Autostart the deconfiguration step.

CLSRSC-00435: Failed to enable CRS after successfully uninstalling the ACFS drivers.

Cause: After successfully deconfiguring ACFS during an downgrade, the root script failed to re-enable CRS using the command 'crsctl enable crs'.

Action: Correct the errors accompanying the failure of the enable command and rerun the deconfiguration step.

CLSRSC-00436: Failed to disable CRS in preparation for a node reboot.

Cause: An attempt to disable CRS in preparation for a system reboot failed. The reboot is associated with a failed removal of ACFS drivers.

Action: Correct the errors accompanying the failure of the disable command, run 'crsctl disable crs', reboot, and continue the deconfiguration step.

CLSRSC-00437: Failed to add the management database listener

Cause: An error occurred while adding the management database listener.

Action: Rerun the root.sh script after resolving the problem indicated by the accompanying messages.

CLSRSC-00438: There is a mismatch between the node list and node role list in 'string/crs/install/crsconfig\_addparams'

Cause: This is an internal error.

Action: Contact Oracle Support Services.

CLSRSC-00440: Failed to copy GPnP setup from a remote node string that belongs to an upgraded cluster

Cause: The remote node was unreachable or has not completed upgrade processing.

Action: Make sure the given node can be reached and it has been successfully upgraded, and then rerun the 'rootupgrade.sh -join -existingNode node name' command.

CLSRSC-00442: Failed to copy Oracle Clusterware configuration files from existing nodes

Cause: During the operation of adding nodes, an attempt to copy configuration files from an existing node failed because no node was unreachable or user equivalence did not work.

Action: Ensure that at least one node can be reached and user equivalence is properly configured between the local node and existing nodes, and then rerun the 'root.sh' command. Contact Oracle Support Services if the problem persists.

CLSRSC-00443: An active CSS daemon was found during CSS exclusive mode startup

Cause: This is an internal error.

Action: Contact Oracle Support Services.

CLSRSC-00444: The 'root.sh' command must first be run on node 'string' where the OUI session was invoked

Cause: The node where the 'root.sh' command was running was not the node on which the OUI session was invoked.

Action: Run the 'root.sh' command on the node where the OUI was invoked.

CLSRSC-00445: The Oracle Grid Infrastructure has already been upgraded to \[string\]

Cause: The rootupgrade.sh was successfully executed on all cluster nodes.

Action: No further action is required.

CLSRSC-00446: The upgrade has not yet been performed on this node

Cause: The rootupgrade.sh was not yet executed on the local node, and the force option was specified.

Action: Rerun rootupgrade.sh without the force option on the local node.

CLSRSC-00447: The upgrade has not yet been performed on node string

Cause: The force option was supplied when some nodes in the cluster have not yet been upgraded. The upgrade cannot be forced to complete while some nodes running Oracle Clusterware have not yet been upgraded.

Action: Rerun rootupgrade.sh without force option on the specified node.

CLSRSC-00448: Cluster-wide Grid Plug and Play profile not found on this node

Cause: The Grid Plug and Play profile was not found on this node. The node may have been unreachable when the profile was created and distributed during an earlier upgrade operation.

Action: First, force completion of the earlier upgrade on the other nodes using 'rootupgrade.sh -force'. Then issue 'rootupgrade.sh -join -existingNode <node\_name>' on the local node to rejoin this node to the cluster. Alternatively, remove this node from the cluster and then add it back.

CLSRSC-00449: Failed to retrieve the value of attribute 'check\_interval' for CVU resource during upgrade

Cause: An attempt to retrieve the value of attribute 'check\_interval' for CVU resource failed during upgrade, possibly because its configuration was corrupt or removed.

Action: Contact Oracle Support Services.

CLSRSC-00450: Failed to determine if the CVU resource was configured

Cause: During upgrade, an attempt to determine if CVU resource was configured failed, possibly because its configuration was corrupt or removed.

Action: Contact Oracle Support Services.

CLSRSC-00451: failed to deconfigure the last Hub node because there are still active Leaf nodes: string

Cause: An attempt to deconfigure the last Hub node in the cluster found one or more Leaf nodes still active.

Action: Deconfigure all other nodes before deconfiguring the last Hub node.

CLSRSC-00452: Failed to upgrade ASM on the current node during attempt to join an upgraded cluster

Cause: The ASM upgrade invoked during node join failed.

Action: Examine the accompanying messages, correct the problem and rerun the 'rootupgrade.sh -join -existingNode node name' command.

CLSRSC-00453: An operating system reboot is required to continue the downgrade

Cause: The reinstall of the older version of Oracle ASM Cluster file system (ACFS) drivers failed. An operating system reboot is required to continue the downgrade.

Action: Reboot the node before running 'crsctl start crs' from the older version of CRS home.

CLSRSC-00454: Failed to initiate the upgrade of Oracle Clusterware

Cause: An error occurred while executing the 'crsctl startupgrade' command.

Action: Rerun the rootupgrade.sh script and contact Oracle Support Services if the problem persists.

CLSRSC-00455: Failed attempt to initiate patch on a Leaf node

Cause: Pre-patch failed because of an attempt to execute 'rootcrs.pl -prepatch' on a Leaf node before any Hub node being patched.

Action: Run the 'rootcrs.pl -prepatch' command on a Hub node first, before running it on the current node.

CLSRSC-00456: The Oracle Grid Infrastructure has already been configured.

Cause: An attempt to run the configuration script was aborted because it had already been successfully executed on this node.

Action: No further action is required.

CLSRSC-00457: Oracle Restart is currently configured and cannot be deconfigured using this Oracle Clusterware deconfiguration command.

Cause: A request to deconfigure Oracle Clusterware was rejected because the existing configuration was Oracle Restart.

Action: Run the command 'roothas.pl -deconfig' to deconfigure Oracle Restart.

CLSRSC-00460: failed to start Oracle Restart stack

Cause: An error occurred when the Oracle Restart stack was automatically restarted during installation or configuration processing.

Action: Retry the configuration script root.sh. If the problem persists, contact Oracle Support Services

CLSRSC-00461: Failed to retrieve OCR locations

Cause: An error occurred while executing the 'ocrcheck -config -details' command.

Action: Correct the problem indicated in the accompanying messages.

CLSRSC-00462: Failed to copy OCR location configuration file to remote nodes

Cause: An attempt to copy configuration file to remote nodes failed because the target node was unreachable or user equivalence did not work.

Action: Ensure that the remote nodes can be reached and user equivalence is properly configured across the cluster nodes, and then rerun the 'root.sh' command. Contact Oracle Support Services if the problem persists.

CLSRSC-00463: The deconfiguration or downgrade script could not stop current Oracle Clusterware stack.

Cause: An error occurred while executing the 'crsctl stop crs -f' command from the current CRS home.

Action: After deconfiguration or downgrade completes, either manually stop the current Oracle Clusterware stack or reboot the local node to properly clean up the processes started by Oracle Clusterware.

CLSRSC-00464: Starting retrieval of the cluster configuration data

Cause: Retrieval of the cluster configuration data from the older version of Oracle Grid Infrastructure stack has started.

Action: None

CLSRSC-00465: Retrieval of the cluster configuration data has successfully completed.

Cause: Retrieval of the cluster configuration data from the older version of Oracle Grid Infrastructure stack has successfully completed.

Action: None

CLSRSC-00466: Starting shutdown of the current Oracle Grid Infrastructure stack

Cause: Shutdown of the older version of Oracle Grid Infrastructure stack has started.

Action: None

CLSRSC-00467: Shutdown of the current Oracle Grid Infrastructure stack has successfully completed.

Cause: Shutdown of the older version of Oracle Grid Infrastructure stack has successfully completed.

Action: None

CLSRSC-00468: Setting Oracle Clusterware and ASM to rolling migration mode

Cause: An attempt has been made to set Oracle Clusterware and ASM to rolling migration mode.

Action: None

CLSRSC-00469: Successfully set Oracle Clusterware and ASM to rolling migration mode

Cause: An operation to set Oracle ASM to rolling migration mode has successfully completed.

Action: None

CLSRSC-00470: Starting non-rolling migration of Oracle ASM

Cause: An attempt has been made to initiate non-rolling migration of Oracle ASM.

Action: None

CLSRSC-00471: Successfully initiated non-rolling migration of Oracle ASM

Cause: An operation to initiate non-rolling migration of Oracle ASM has successfully completed.

Action: None

CLSRSC-00472: Attempting to export the OCR

Cause: An attempt has been made to export the OCR.

Action: None

CLSRSC-00473: Successfully exported the OCR

Cause: The OCR has successfully been exported.

Action: None

CLSRSC-00474: Initiating upgrade of resource types

Cause: An attempt has been made to initiate upgrade of resource types.

Action: None

CLSRSC-00475: Upgrade of resource types successfully initiated.

Cause: Upgrade of resource types has successfully started.

Action: None

CLSRSC-00476: Finishing upgrade of resource types

Cause: An attempt has been made to finish upgrade of resource types.

Action: None

CLSRSC-00477: Successfully completed upgrade of resource types

Cause: Upgrade of resource types has successfully completed.

Action: None

CLSRSC-00478: Setting Oracle Clusterware active version on the last node to be upgraded

Cause: An attempt has been made on the last node to be upgraded to set the Oracle Clusterware active version.

Action: None

CLSRSC-00479: Successfully set Oracle Clusterware active version

Cause: An operation initiated on the last node to be upgraded to set Oracle Clusterware active version has successfully completed.

Action: None

CLSRSC-00480: Starting the process of upgrading local listeners

Cause: The process of upgrading local listeners has started.

Action: None

CLSRSC-00481: Successfully completed the process of upgrading local listeners

Cause: The process of upgrading local listeners has successfully completed.

Action: None

CLSRSC-00482: Running command: 'string'

Cause: An attempt has been made to run the command mentioned in the message.

Action: None

CLSRSC-00483: unable to run 'rootcrs.pl -prepatch' to perform rolling, in-place patching for shared Grid Infrastructure home

Cause: In the course of patching a shared Grid Infrastructure home, an attempt to execute the 'rootcrs.pl -prepatch' command failed because rolling in-place patching of a shared home is not allowed.

Action: Reissue the 'rootcrs.pl -prepatch' command with the '-nonrolling' or '-dstcrshome' option specified.

CLSRSC-00484: error querying CRS software version on node 'string'

Cause: An error occurred while executing the 'crsctl query crs softwareversion' command.

Action: Correct the problem indicated in the accompanying messages and then rerun rootupgrade.sh. Contact Oracle Support Services if the problem persists.

CLSRSC-00485: Local port=string and remote port=string should not be same.

Cause: The rootupgrade script was aborted because the specified local and remote ports were the same.

Action: Rerun the rootupgrade.sh script after changing the port numbers.

CLSRSC-00487: Check for ASM compatibility version failed during downgrade.

Cause: An attempt to downgrade the current node failed because the ASM compatibility version was already advanced after upgrade.

Action: Downgrade is not allowed in this case. Contact Oracle Support Services for further action.

CLSRSC-00488: Patching the Grid Infrastructure Management Repository database failed.

Cause: An error occurred when executing the 'sqlpatch -db -MGMTDB' command' to patch the Grid Infrastructure Management Repository database.

Action: Address the issues reported by accompanying messages and rerun the 'rootcrs.pl -postpatch' command. If the problem persists, contact Oracle Support Services.

CLSRSC-00489: Stopping the Grid Infrastructure Management Repository database failed.

Cause: An error occurred while executing the 'srvctl stop mgmtdb' command.

Action: Examine the accompanying messages, correct the problem and rerun the 'rootcrs.pl -postpatch' command.

CLSRSC-00490: Starting the Grid Infrastructure Management Repository database failed.

Cause: An error occurred while executing the 'srvctl start mgmtdb' command.

Action: Examine the accompanying messages, correct the problem and rerun the 'rootcrs.pl -postpatch' command.

CLSRSC-00491: Failed to disable the Grid Infrastructure Management Repository database

Cause: An error occurred while executing the 'srvctl disable mgmtdb' command.

Action: Examine the accompanying messages, correct the problem and rerun the 'rootcrs.pl -postpatch' command.

CLSRSC-00492: Failed to enable the Grid Infrastructure Management Repository database

Cause: An error occurred while executing the 'srvctl enable mgmtdb' command.

Action: Examine the accompanying messages, correct the problem and rerun the 'rootcrs.pl -postpatch' command.

CLSRSC-00493: failed to initiate rolling patch on the current node because there is only one active HUB node

Cause: An attempt to execute the 'rootcrs.pl -prepatch' command failed because there was only one active HUB node.

Action: Reissue the 'rootcrs.pl -prepatch' command with the '-nonrolling' option specified or configure more than one active HUB node in the cluster.

CLSRSC-00494: Failed to execute this command. Current directory is under an ACFS mount point.

Cause: An attempt to execute a command that would result in a forced / shutdown of ACFS was rejected because the current directory is on an ACFS file system. Consequently, the forced shutdown of ACFS would terminate the execution of the attempted command.

Action: Ensure that the current shell has no dependencies on ACFS file systems (i.e. current directory not on ACFS and not a sub-shell of a process whose working directory is on ACFS) and retry the command.

CLSRSC-00495: failed to get active role for the node string

Cause: An error occurred while executing the command 'crsctl get node role status -node nodename'.

Action: Examine the accompanying messages, correct the problem and retry.

CLSRSC-00496: failed to get active role for the local node

Cause: An error occurred while executing the command 'crsctl get node role status'.

Action: Examine the accompanying messages, correct the problem and retry.

CLSRSC-00497: failed to retrieve the configured cluster mode

Cause: An error occurred while executing the command 'crsctl get cluster mode config'.

Action: Examine the accompanying messages, correct the problem and retry.

CLSRSC-00498: invalid cluster mode

Cause: An internal error. The cluster mode returned by the command 'crsctl get cluster mode config' was neither 'standard' nor 'flex'.

Action: Contact Oracle Support Services.

CLSRSC-00499: Stopping the Grid Infrastructure Management Repository database failed.

Cause: An error occurred while executing the 'srvctl stop mgmtdb' command.

Action: Examine the accompanying messages, correct the problem and rerun rootupgrade.sh.

CLSRSC-00500: Starting the Grid Infrastructure Management Repository database failed.

Cause: An error occurred while executing the 'srvctl start mgmtdb' command.

Action: Examine the accompanying messages, correct the problem and rerun rootupgrade.sh.

CLSRSC-00501: failed to disable the Grid Infrastructure Management Repository database

Cause: An error occurred while executing the 'srvctl disable mgmtdb' command.

Action: Examine the accompanying messages, correct the problem and rerun rootupgrade.sh.

CLSRSC-00502: failed to enable the Grid Infrastructure Management Repository database

Cause: An error occurred while executing the 'srvctl enable mgmtdb' command.

Action: Examine the accompanying messages, correct the problem and rerun rootupgrade.sh.

CLSRSC-00503: Deleting the Grid Infrastructure Management Repository database failed.

Cause: An attempt to connect to the GI Management Repository database failed or an error occurred while executing the SQL statement 'drop database'.

Action: Examine the accompanying messages, correct the problem and rerun rootupgrade.sh.

CLSRSC-00504: The root script cannot proceed on this node string until the current first-node operations have finished on the first node string.

Cause: An attempt to run the root script on this node failed because the root script was still running on the first node and had not yet completed.

Action: Allow the root script to complete execution on the first node and then restart the root script on this node.

CLSRSC-00505: The root script cannot proceed on this node string because the root script encountered errors during execution on the first node string.

Cause: An attempt to run the root script on this node failed because the root script encountered errors during execution on the first node.

Action: Correct the problems indicated by the root script on the first node and rerun the script on that node. Following successful completion on the first node, restart the root script on this node.

CLSRSC-00506: The root script cannot proceed on this node string because the first-node operations have not completed and the first node string has crashed or gone offline.

Cause: An attempt to run the root script on this node failed because the root script did not completed successfully on the first node, and the first node has crashed or gone offline.

Action: Rerun the root script on any of the remaining nodes supplying the -force option to cause it to act as the first node.

CLSRSC-00507: The root script cannot proceed on this node string because either the first-node operations have not completed on node string or there was an error in obtaining the status of the first-node operations.

Cause: An attempt to run the root script on this node was rejected because the root script had not completed (and may not have been started) on the first node or there was an error in obtaining the status of the first node.

Action: Ensure that the root script has successfully completed execution on the first node and then restart the root script on this node. The first node is the node where the installer runs.

CLSRSC-00508: The root script cannot be started with the -first -force option on this node string, while the original first node string is still online.

Cause: An attempt to run the root script supplying the -first -force option on this node failed because the first node was still online.

Action: Run the root script on the first node. Following successful completion on the first node, restart the root script on this node.

CLSRSC-00509: invalid ASM mode

Cause: This is an internal error. The ASM mode was an undefined value at this point.

Action: Contact Oracle Support Services.

CLSRSC-00510: failed to delete the voting file on diskgroup 'string' during deconfiguration

Cause: The attempt to remove a voting file failed because an error occurred while executing the command 'crsctl delete css votedisk +diskgroup'.

Action: Retry the above command manually. If the problem persists, contact Oracle Support Services.

CLSRSC-00511: failed to set Oracle Clusterware and ASM to rolling migration mode

Cause: An error occurred while executing the command 'crsctl start rollingupgrade'.

Action: Correct the problem indicated in the accompanying messages and rerun rootupgrade.sh.

CLSRSC-00512: failed to force node string as the first node because it is not a hub node

Cause: An attempt to run the root script supplying the -force option on this node has failed because it is not a hub node.

Action: Run the root script with the -force option on a hub node.

CLSRSC-00514: failed to reset cardinality of Flex ASM to original value

Cause: An error occurred while attempting to reset Flex ASM cardinality, either in retrieving the previously stored value using 'crsctl status resource' or in restoring the previous value using 'srvctl modify asm'.

Action: Examine the accompanying messages, correct the problem and rerun rootupgrade.sh.

CLSRSC-00515: Starting OCR manual backup.

Cause: An attempt has been made to generate OCR manual backup.

Action: None

CLSRSC-00516: OCR manual backup successful.

Cause: OCR manual backup completed normally.

Action: None

CLSRSC-00518: cannot open directory 'string'

Cause: An attempt to open the specified directory has failed.

Action: Ensure that the user running root script has read permission on the directory.

CLSRSC-00519: cannot move directory string to directory string

Cause: An attempt to move the source directory has failed.

Action: Ensure that the user running root script has read permission on the source directory and write permission on destination directory.

CLSRSC-00520: Clusterware version on this node too old to join target cluster

Cause: An attempt to join the current node to an upgraded cluster failed because the join is not supported for nodes with Oracle Clusterware older than version 11.2.0.1.

Action: Delete this node and then add this node back into Clusterware using the 'add node' operation.

CLSRSC-00524: Setting Oracle Clusterware to rolling migration mode

Cause: The command 'crsctl start rollingupgrade version' to initiate rolling migration of Oracle Clusterware was issued.

Action: None

CLSRSC-00525: Successfully set Oracle Clusterware to rolling migration mode

Cause: The command 'crsctl start rollingupgrade version' to initiate a rolling migration of Oracle Clusterware completed successfully.

Action: None

CLSRSC-00526: The root script cannot run with the '-first -force' options to force current node string as the first node.

Cause: An attempt to run the root script with options '-first -force' on this node failed because first-node operations had already been done.

Action: Run the root script on this node without the options '-first -force'.

CLSRSC-00527: The root script cannot run with the '-force' option to force current node string as the last node during fresh install (case: first-node operations complete).

Cause: An attempt to run the root script with option '-force' on this node failed because there are no last node operations for a fresh install, and the first-node operations had been done.

Action: Run the root script on this node without the option '-force'.

CLSRSC-00528: The root script cannot run with the '-force' options to force current node string which is the installer node as the last node during upgrade before first-node operations have been done.

Cause: An attempt to run the root script with option '-force' on installer node failed because the first-node operations had not been done.

Action: Run the root script on this node without the option '-force'.

CLSRSC-00529: The root script cannot run with the '-force' option to force current node string as the last node during fresh install (case: first-node operations not complete).

Cause: An attempt to run the root script with option '-force' on this node failed because there are no last node operations for a fresh install, and the first-node operations had not been done.

Action: Run the root script on this node with the options '-first -force'.

CLSRSC-00530: The root script cannot run with the '-force' option to force current node string which is a non-installer node as the last node during upgrade before first-node operations have been done.

Cause: An attempt to run the root script with option '-force' on a non- installer node failed because the first-node operations had not been done.

Action: Run the root script on this node with the options '-first -force'.

CLSRSC-00531: The root script does not need the '-first -force' options to force current node string as the first node.

Cause: An attempt to run the root script with options '-first -force' on this node failed because the '-first -force' options were not needed on installer node.

Action: Run the root script on this node without the options '-first -force'.

CLSRSC-00537: The root script failed to copy the OCR backup file from node string to shared storage.

Cause: An error occurred while copying the OCR backup file to shared storage.

Action: Examine the accompanying messages, correct the problem indicated and rerun rootupgrade.sh.

CLSRSC-00538: The root script failed to get the name of the OCR backup file on the ASM diskgroup.

Cause: An error occurred while getting the OMF name of the OCR backup file using the 'asmcmd find' command.

Action: Examine the accompanying messages from the 'asmcmd find' command, and correct the problem indicated.

CLSRSC-00539: There is at least one expired OCR backup on the ASM diskgroup, and the root script failed to remove it from the ASM diskgroup.

Cause: An error occurred while removing the expired OCR backup file using the 'asmcmd rm' command.

Action: Examine the accompanying messages from the 'asmcmd rm' command, and correct the problem indicated.

CLSRSC-00540: The root script failed to get a unique name of the OCR backup file on the ASM diskgroup using string.

Cause: There are more than one OMF names corresponding to the given OCR backup file name.

Action: Remove the expired OCR backup file from the ASM diskgroup using 'asmcmd rm' command.

CLSRSC-00545: Voting files are not found.

Cause: The voting files are either removed by an earlier operation or the query for the voting files failed.

Action: Run 'crsctl query css votedisk' to check if the voting files are configured.

CLSRSC-00546: The Grid Infrastructure processes identified by the following PIDs (string) are still active.

Cause: There were still some of Grid Infrastructure processes running after shutting down the Grid Infrastructure stack.

Action: Run the 'crsctl stop crs -force' command again, or 'rootcrs.pl -prepatch -cleanpids' to terminate active processes before continuing the patch process.

CLSRSC-00549: The root script cannot downgrade this node string with last node operations because the Grid Infrastructure stack is up on at least one other cluster node.

Cause: An attempt to run the root script with last node operations on this node failed because there was at least one other cluster node with its Grid Infrastructure stack up.

Action: Run the root script on this node after the Grid Infrastructure stack is down on all other cluster nodes.

CLSRSC-00550: Local node string failed to check the status of the Grid Infrastructure stack of other cluster nodes.

Cause: An attempt to downgrade this node with last node operations failed because the root script failed to check the status of the Grid Infrastructure stack of other cluster nodes by starting CSS in exclusive mode.

Action: Correct the problem indicated in the accompanying messages and then retry downgrade.

CLSRSC-00551: unable to start rolling mode upgrade due to nodes running or to prior non-rolling upgrade

Cause: The cluster was either previously upgraded in non-rolling mode or the Oracle Grid Infrastructure stack has been started on some nodes after the non-rolling upgrade installer interview.

Action: Shutdown the Oracle Grid Infrastructure stack on all other nodes and then rerun rootupgrade.sh.

CLSRSC-00554: unable to perform an online downgrade after the cluster was upgraded completely

Cause: An attempt to downgrade a node failed because the option '-online' was specified in the downgrade command after the cluster had been upgraded completely.

Action: Reissue the downgrade command on this node without '-online' option.

CLSRSC-00556: Oracle Clusterware stack on this node has been successfully downgraded. There were some errors which can be ignored.

Cause: The downgrade was successful, but stopping the Oracle Clusterware afterwards failed.

Action: Retry the stop operation by running 'crsctl stop crs -f' from the higher version home.

CLSRSC-00557: Oracle Clusterware stack on this node has been successfully deconfigured. There were some errors which can be ignored.

Cause: The deconfiguration was successful, but stopping the Oracle Clusterware afterwards failed.

Action: Retry the stop operation by running 'crsctl stop crs -f' from the higher version home.

CLSRSC-00558: failed to deconfigure ASM

Cause: There was an error in deconfiguring ASM.

Action: Examine the accompanying messages and correct the problem.

CLSRSC-00561: The Oracle Grid Infrastructure has already been deconfigured on this node: string.

Cause: An attempt to run the deconfiguration script was rejected because it had already been successfully executed on this node.

Action: No further action is required.

CLSRSC-00562: The specified disk group cannot be dropped on this cluster because services 'string' of this cluster are still in use by other clusters: 'string'.

Cause: An attempt to remove disk groups during server deconfiguration found a disk group that was still in use by one or more clusters that are using the ASM storage, GIMR and/or RHP services of this cluster.

Action: Deconfigure or deinstall the client clusters first, then deconfigure with '-force' option or deinstall this server cluster.

CLSRSC-00563: Failed to remove the CVU resource and type during upgrade.

Cause: An error occurred when removing the CVU resource and type during upgrade.

Action: Examine the accompanying messages and correct the problem indicated and retry.

CLSRSC-00564: Failed to disable the CVU resource during upgrade.

Cause: An error occurred when disabling the CVU resource during upgrade.

Action: Examine the accompanying messages and correct the problem indicated and retry.

CLSRSC-00566: Failed to enable and start the CVU resource during upgrade.

Cause: An error occurred when enabling and starting the CVU resource during upgrade.

Action: Examine the accompanying messages and correct the problem indicated and retry.

CLSRSC-00567: Beginning Oracle Grid Infrastructure configuration.

Cause: Oracle Grid Infrastructure configuration processing was started on this node.

Action: None

CLSRSC-00568: invalid public network information retrieved

Cause: This is an internal error. The public network information retrieved was invalid at this point.

Action: Contact Oracle Support Services.

CLSRSC-00569: failed to configure the public network in an application cluster

Cause: An attempt to configure the public network in an application cluster failed because an error occurred during execution of the 'srvctl add network' command. The accompanying error messages provide detailed failure information.

Action: Correct the problem indicated in the accompanying messages and retry root.sh.

CLSRSC-00570: failed to configure an application VIP for an application cluster

Cause: An attempt to configure an application VIP for an application cluster failed because an error occurred during execution of the 'appvipcfg create' command. The accompanying error messages provide detailed failure information.

Action: Correct the problem indicated in the accompanying messages and retry root.sh.

CLSRSC-00571: failed to copy file 'string' from node 'string' to file 'string' on local node

Cause: An attempt to copy a configuration file from a remote node failed because the target node was unreachable or user equivalence did not work.

Action: Ensure that the remote node can be reached and user equivalence is properly configured across the cluster nodes, and then rerun the root script. Contact Oracle Support Services if the problem persists.

CLSRSC-00583: Invalid option

Cause: An invalid command option was supplied.

Action: Reissue the command with valid options.

CLSRSC-00584: The resource 'string' is unexpectedly not online after starting the Grid Infrastructure stack.

Cause: There was an error in starting the indicated resource.

Action: Start the resource manually using srvctl and if the problem persists, contact Oracle Support Services.

CLSRSC-00585: failed to set the cluster type to 'string'

Cause: An attempt to set the cluster to the indicated type failed because an error occurred during execution of the command 'crsctl set cluster type'. The accompanying error messages provide detailed failure information.

Action: Correct the problem indicated in the accompanying messages and retry root.sh.

CLSRSC-00586: failed to remove the application VIP 'string' in an application cluster

Cause: An attempt to remove the indicated application VIP in an application cluster failed because an error occurred during execution of the command 'appvipcfg delete'. The accompanying error messages provide detailed failure information.

Action: Correct the problem indicated in the accompanying messages and retry deconfiguration.

CLSRSC-00587: failed to remove the public network in an application cluster

Cause: An attempt to remove the public network in an application cluster failed because an error occurred during execution of the command 'srvctl remove network'. The accompanying error messages provide detailed failure information.

Action: Correct the problem indicated in the accompanying messages and retry deconfiguration.

CLSRSC-00588: failed to deconfigure Oracle Clusterware stack on this node

Cause: This is a status message.

Action: None

CLSRSC-00589: failed to deconfigure Oracle Restart on this node

Cause: This is a status message.

Action: None

CLSRSC-00591: successfully downgraded Oracle Clusterware stack on this node

Cause: This is a status message.

Action: None

CLSRSC-00592: Run 'crsctl start crs' from home string on each node to complete downgrade.

Cause: This is a status message.

Action: None

CLSRSC-00593: failed to downgrade Oracle Clusterware stack on this node

Cause: This is a status message.

Action: None

CLSRSC-00596: failed to configure Oracle Restart for a standalone server

Cause: An error occurred during the configuration of Oracle Restart for a standalone server. Specific details were included in the accompanying messages.

Action: Correct the problem indicated in the accompanying messages and then rerun the root script. Contact Oracle Support Services if the problem persists.

CLSRSC-00599: failed to start the Rapid Home Provisioning server

Cause: An error occurred when starting Rapid Home Provisioning server.

Action: Check the accompanying error messages.

CLSRSC-00600: failed to stop the Rapid Home Provisioning server

Cause: An error occurred when stopping Rapid Home Provisioning server.

Action: Check the accompanying error messages.

CLSRSC-00601: failed to upgrade the Rapid Home Provisioning repository

Cause: An error occurred when upgrading the Rapid Home Provisioning repository.

Action: Check the accompanying error messages.

CLSRSC-00602: failed to disable resource string on node string

Cause: The execution of the script rootupgrade.sh did not complete because an error occurred while executing the command 'crsctl modify resource'.

Action: Examine the accompanying messages, correct reported problems and retry rootupgrade.sh.

CLSRSC-00603: failed to retrieve ACFS resources that are enabled and online

Cause: An attempt to retrieve qualified ACFS resources failed because an error occurred during execution of the command 'crsctl stat res'. The accompanying error messages provide detailed failure information.

Action: Correct the problems indicated in the accompanying messages and retry rootupgrade.sh.

CLSRSC-00604: The value of attribute VOLUME\_DEVICE for the ACFS resource string is empty.

Cause: This is an internal error. The value of attribute VOLUME\_DEVICE for the specified ACFS resource should already have been set.

Action: Contact Oracle Support Services.

CLSRSC-00606: failed to configure 'string' as the Oracle Cluster Registry (OCR) backup location

Cause: An error occurred while configuring the Oracle Cluster Registry (OCR) backup location.

Action: Correct the problem indicated in the accompanying messages and then rerun the root script. Contact Oracle Support Services if the problem persists.

CLSRSC-00607: The prerequisite checks related to component string failed during the patching.

Cause: An error was raised in one of the checks done for the patching. This message is accompanied by others providing details of the error.

Action: Correct the problem indicated in the accompanying messages and then rerun the root script. Contact Oracle Support Services if the problem persists.

CLSRSC-00608: failed to write key 'string' to the Oracle Cluster Registry (OCR)

Cause: An error occurred when writing the given key to the Oracle Cluster Registry (OCR).

Action: Correct the problem indicated in the accompanying messages and then rerun the root script. Contact Oracle Support Services if the problem persists.

CLSRSC-00609: Check for ACFS driver support failed.

Cause: An error occurred while checking whether ACFS drivers are supported, using the command 'acfsdriverstate supported'.

Action: Examine the accompanying messages, correct the problem, and retry.

CLSRSC-00611: failed to set the value of the parameter 'string' for Cluster Synchronization Service

Cause: An error occurred when setting the value of the given parameter.

Action: Correct the problem indicated in the accompanying messages and then rerun the root script. If the problem persists contact Oracle Support Services.

CLSRSC-00612: failed to create backup disk group 'string'

Cause: An error occurred while creating the backup disk group via 'asmca'.

Action: Correct the problem indicated in the accompanying messages and then rerun the root script. Contact Oracle Support Services if the problem persists.

CLSRSC-00613: failed to downgrade the local node because the first node has not been successfully upgraded

Cause: An attempt to downgrade the local node failed because the first node had not been successfully upgraded.

Action: Start the older version GI stack if the older version stack has been shut down during upgrade. If the problem persists contact Oracle Support Services.

CLSRSC-00614: failed to get the list of configured diskgroups

Cause: An error occurred while getting the list of diskgroups using the 'asmcmd lsdg' command.

Action: Examine the accompanying messages from the 'asmcmd lsdg' command, and correct the problem indicated.

CLSRSC-00616: failed to downgrade the last Hub node because there are still active Leaf nodes: string

Cause: An attempt to downgrade the last Hub node in the cluster found one or more Leaf nodes still active.

Action: Downgrade all other nodes before downgrading the last Hub node.

CLSRSC-00617: Check for active Leaf nodes not yet downgraded failed on node string.

Cause: During the downgrade of current node, an attempt to check whether there were any active Leaf nodes not yet downgraded failed because the GI stack was down on the current node.

Action: Start the GI stack and retry the downgrade on the indicated node, which will abort and require intervention if active Leaf nodes in need of downgrading are discovered. Alternatively, to bypass the automated check and finish the downgrade, make sure any active Leaf nodes have been downgraded and retry the downgrade on the indicated node with the '-force' option.

CLSRSC-00618: failed to deconfigure the current node string because there may be active Leaf nodes and the '-force' option was not supplied

Cause: An attempt to check whether there were any active Leaf nodes not yet deconfigured failed.

Action: Rerun deconfiguration with '-force' option after making sure all active Leaf nodes have been successfully deconfigured.

CLSRSC-00619: failed to store the result after checking if the directory 'string' is shared among nodes

Cause: The root script failed to store the information after checking if the given directory is shared among nodes.

Action: Correct the problem indicated in the accompanying messages and then rerun the root script. Contact Oracle Support Services if the problem persists.

CLSRSC-00620: The configuration parameter OPC\_NAT\_ADDRESS does not include data for node 'string'.

Cause: The root script could not configure the OPC\_NAT\_ADDRESS for the given node because the node was not present in the configuration parameter OPC\_NAT\_ADDRESS.

Action: Verify the value of the OPC\_NAT\_ADDRESS parameter, add the missing information, and rerun the root script.

CLSRSC-00621: could not retrieve the node number for node 'string'

Cause: During the post configuration operations, an attempt to retrieve the node number for the indicated node failed.

Action: Correct the problem indicated in the accompanying messages and then rerun the root script. Contact Oracle Support Services if the problem persists.

CLSRSC-00622: failed to add ASM proxy configuration

Cause: An error occurred while executing the 'srvctl add asm -proxy' command.

Action: Correct the problem indicated in the accompanying messages, then rerun the root script.

CLSRSC-00623: failed to disable ASM proxy configuration

Cause: An error occurred while executing the 'srvctl disable asm -proxy' command.

Action: Correct the problem indicated in the accompanying messages, then rerun the root script.

CLSRSC-00624: The value of attribute ENABLED for the HAIP resorce is invalid.

Cause: This is an internal error.

Action: Contact Oracle Support Services.

CLSRSC-00629: Failed to downgrade local node string because the OCR backup file is not on NAS shared storage. OCR backup file 'string' must be copied to path 'string' before rerunning downgrade on local node.

Cause: An attempt to downgrade the local node was rejected because the OCR backup file was not on NAS shared storage.

Action: Copy the OCR backup file to the indicated NAS shared storage location, then rerun the downgrade.

CLSRSC-00630: Failed to downgrade local node string because the OCR backup file is not on ASM shared storage. Issue the command 'string' on the OCR master node string to copy the backup to ASM shared storage, then retry the downgrade with the '-force' option.

Cause: An attempt to downgrade the local node was rejected because the OCR backup file was not on ASM shared storage.

Action: Issue the indicated command on the OCR master node to copy the backup file to ASM shared storage, then retry the downgrade with the '-force' option.

CLSRSC-00631: failed to generate GUID (Globally Unique Identifier) for site 'string'

Cause: An error occurred while generating GUID for the indicated site.

Action: Correct the problem indicated in the accompanying messages and then rerun the root script. Contact Oracle Support Services if the problem persists.

CLSRSC-00632: failed to retrieve the status of the management database

Cause: An error occurred while retrieving the status of the management database.

Action: Correct the problem indicated in the accompanying messages and then rerun the root script. Contact Oracle Support Services if the problem persists.

CLSRSC-00634: cannot get the site information for node string

Cause: This is an internal error.

Action: Contact Oracle Support Services.

CLSRSC-00635: Failed to get EXTENDED\_CLUSTER\_SITE\_GUIDS from parameter file string. Manually copy the parameter file from an existing cluster node that has been configured.

Cause: An error occurred while reading the EXTENDED\_CLUSTER\_SITE\_GUIDS from the parameter file because the parameter file was corrupt.

Action: Copy the parameter file from an existing cluster node that has been configured and rerun the root script.

CLSRSC-00636: The site name string for node string is invalid.

Cause: This is an internal error.

Action: Contact Oracle Support Services.

CLSRSC-00637: failed to update the GPnP profile 'string' with sequence number string

Cause: An error occurred when updating the indicated GPnP profile using the 'gpnptool edit' command.

Action: Examine the accompanying messages, correct the problems indicated if possible and retry. Otherwise Contact Oracle Support Services.

CLSRSC-00638: failed to start the Oracle Grid Infrastructure stack during downgrade

Cause: An error occurred while starting the Oracle Grid Infrastructure stack during downgrade on the local node.

Action: Ensure that all active Leaf nodes have been downgraded and retry the downgrade specifying the '-force' option.

CLSRSC-00639: failed to copy GPnP setup from existing nodes

Cause: During the configuration of the local node, an attempt to copy configuration files from an existing node failed because no node was reachable or user equivalence did not work.

Action: Ensure that at least one node can be reached and user equivalence is properly configured between the local node and existing nodes, and then rerun the 'root.sh' command. Contact Oracle Support Services if the problem persists.

CLSRSC-00640: To complete the downgrade operation, ensure that the node inventory on all nodes points to the configured Grid Infrastructure home 'string'.

Cause: A downgrade operation prompted the user to ensure that the node inventory on all nodes points to the indicated Grid Infrastucture home. This step is required to complete the downgrade operations.

Action: On each node, update the node inventory to point to the indicated Grid Infrastructure home. Refer to the product documentation to update the node inventory.

CLSRSC-00641: failed to remove the file string from nodes string

Cause: An error occurred while executing the 'cluutil' command to remove the indicated file from the indicated cluster nodes.

Action: Manually remove the indicated file on the indicated nodes.

CLSRSC-00642: mismatch between nodes to add and sites

Cause: Root script failed because OUI input was not properly validated prior to install. This is an internal error.

Action: Contact Oracle Support Services.

CLSRSC-00643: The site name string for added node string is invalid.

Cause: Root script failed because the site name from OUI input was not properly validated prior to install. This is an internal error.

Action: Contact Oracle Support Services.

CLSRSC-00644: failed to retrieve the cluster class

Cause: An error occurred while executing the command 'crsctl get cluster class'.

Action: Examine the accompanying messages, correct the problem and retry.

CLSRSC-00645: Rapid Home Provisioning repository upgrade failed.

Cause: An internal error occurred when upgrading the Rapid Home Provisioning repository.

Action: Check accompanying messages and contact Oracle Support Services.

CLSRSC-00646: failed to install cvuqdisk RPM

Cause: While installing Grid Infrastructure, an attempt to install the cvuqdisk RPM failed. This is an internal error. ASM disk validation cannot be performed without this RPM, but installation will continue.

Action: Install the required version of the cvuqdisk RPM using the fix up action or manual steps as listed in the documentation.

CLSRSC-00647: failed to remove file string\\nstring

Cause: An attempt to remove the indicated file failed with the error shown.

Action: Correct the problem indicated in the appended error and remove the indicated file manually.

CLSRSC-00648: No CELL configured with the site name 'string'.

Cause: While configuring the Grid Infrastructure on Oracle Exadata, an attempt to retrieve the site and site GUID for the indicated site failed because none of the CELLs were associated with the indicated site.

Action: Either run the command 'cellcli -e alter cell siteName=<site\_name>' with the indicated site to associate a CELL with the site, or delete the site using the command 'crsctl delete cluster site <site\_name>', and then rerun the root script. Contact Oracle Support Services if the problem persists.

CLSRSC-00649: failed to disable the file system resource string

Cause: An error occurred while executing the command 'srvctl disable filesystem'. The accompanying error messages provide detailed failure information.

Action: Correct the problems indicated in the accompanying messages and retry the command.

CLSRSC-00650: failed to enable the file system resource string

Cause: An error occurred while executing the command 'srvctl enable filesystem'. The accompanying error messages provide detailed failure information.

Action: Correct the problems indicated in the accompanying messages and retry the command.

CLSRSC-00651: One or more deconfiguration steps failed, but the deconfiguration process continued because the -force option was specified.

Cause: An attempt to deconfigure Oracle Clusterware encountered one or more failures. The deconfiguration process continued after each failure because the -force option was specified. The preceding error messages provide detailed failure information.

Action: Examine the preceding error messages and address the issues described.

CLSRSC-00652: The member cluster GUID 'string' in the ASM section is different from the member cluster GUID 'string' in the GIMR section of the Cluster Manifest File 'string'.

Cause: While configuring the Member Cluster, an attempt to retrieve the Cluster Globally Unique Identifier (GUID) from the Cluster Manifest File found different GUIDs in the Automatic Storage Management (ASM) and Grid Infrastructure Management Repository (GIMR) sections of the Cluster Manifest File. This is an internal error.

Action: Recreate the Cluster Manifest File in the Domain Services Cluster specifying all the required domain services. Rerun the installer and provide the new Cluster Manifest File during the interview.

CLSRSC-00653: Failed to retrieve GUIDs from both the ASM section and the GIMR section of the Cluster Manifest File 'string'.

Cause: While configuring the Member Cluster, an attempt was made to retrieve the Cluster Globally Unique Identifier (GUID) from the Cluster Manifest File, but neither the Automatic Storage Management (ASM) section nor the Grid Infrastructure Management Repository (GIMR) sections of the file contained a GUID. This is an internal error.

Action: Recreate the Cluster Manifest File in the Domain Services Cluster specifying all the required domain services. Rerun the installer and provide the new Cluster Manifest File during the interview.

CLSRSC-00654: failed to set the network interface classification

Cause: An error occurred while executing the 'oifcfg setif' command to set the network interface classification. The accompanying error messages provide detailed failure information.

Action: Correct the problems indicated in the accompanying messages and retry the root script.

CLSRSC-00655: failed to delete the Clusterware configuration from the disk groups

Cause: An error occurred while deleting the Clusterware configuration from the disk groups because execution of the command 'kfod op=groups' failed to list the disk groups used by Clusterware.

Action: Correct the problems indicated in the accompanying messages and retry the root script. If the problem persists, retry the root script with -force option.

CLSRSC-00656: The disk group 'string' containing the Oracle ASM password file 'string' is not mounted.

Cause: An attempt to run the root script failed because the disk group where the Oracle ASM password file was stored was not mounted.

Action: Issue the command 'asmcmd mount diskgroup' to mount the indicated disk group and retry the root script.

CLSRSC-00657: The disk group 'string' containing the Oracle ASM SPFILE 'string' is not mounted.

Cause: An attempt to run the root script failed because the disk group where the Oracle ASM SPFILE was stored was not mounted.

Action: Issue the command 'asmcmd mount diskgroup' to mount the indicated disk group and retry the root script.

CLSRSC-00658: Inconsistencies detected in the Oracle ASM disk group 'string' metadata.

Cause: An attempt to run the root script failed because an inconsistency was detected in the metadata for the indicated disk group. The accompanying messages provide detailed failure information.

Action: Issue the command 'asmcmd chkdg --repair' to fix the inconsistency and retry the root script.

CLSRSC-00659: failed to retrieve the Oracle ASM SPFILE location

Cause: An attempt to run the root script failed because the Oracle ASM SPFILE location could not be retrieved. The accompanying messages provide detailed failure information.

Action: Correct the problems indicated in the accompanying messages and retry the root script.

CLSRSC-00660: failed to retrieve the Oracle ASM password file location

Cause: An attempt to run the root script failed because the location of the Oracle ASM password file could not be retrieved. The accompanying messages provide detailed failure information.

Action: Correct the problems indicated in the accompanying messages and retry the root script.

CLSRSC-00661: The Oracle ASM password file does not exist at location string.

Cause: An attempt to run the root script failed because the Oracle ASM password file did not exist at the indicated location.

Action: Ensure that the Oracle ASM password file exists at the indicated location. Refer to the product documentation to modify the location of the ASM password file. Retry the root script.

CLSRSC-00662: failed to read key 'string' from the Oracle Cluster Registry (OCR)

Cause: An attempt to execute the root script failed because an error occurred when reading the indicated key from the Oracle Cluster Registry (OCR). The accompanying messages provide detailed failure information.

Action: Correct the problem indicated in the accompanying messages and then rerun the root script. If the problem persists, contact Oracle Support Services.

CLSRSC-00663: failed to delete key 'string' from the Oracle Cluster Registry (OCR)

Cause: An attempt to execute the root script failed because an error occurred when deleting the indicated key from the Oracle Cluster Registry (OCR). The accompanying messages provide detailed failure information.

Action: Correct the problem indicated in the accompanying messages and then rerun the root script. If the problem persists, contact Oracle Support Services.

CLSRSC-00667: found multiple ASM password files under 'string'

Cause: An attempt to execute the root script failed because multiple ASM password files were found in the indicated directory.

Action: Refer to the product documentation for information about password file names and locations. Ensure that there is only one ASM password file in the indicated directory, then rerun the root script.

CLSRSC-00668: Failed to get the configured node role for the node string

Cause: An error occurred while retrieving the node role for the local node. The accompanying messages provide detailed failure information.

Action: Correct the problems indicated in the accompanying messages, then retry the operation.

CLSRSC-00669: Local node 'string' failed to rejoin the upgraded cluster, missing '-join' option to rootupgrade.sh.

Cause: An attempt to upgrade the indicated node did not complete successfully because the script rootupgrade.sh was executed without the '-join' option, which prevented the node from rejoining the upgraded cluster.

Action: Rerun the rootupgrade.sh script with '-join' option.

CLSRSC-00670: failed to configure the node due to unexpected parameter settings

Cause: An attempt to configure the node was rejected because unexpected configuration parameters were found in the parameter settings. This can occur if the node was deconfigured but not deleted or by running root.sh on an upgraded node.

Action: 1. To configure a node that has been deconfigured but not deleted, it must first be deleted completely. Delete and then re-add the node before configuring. 2. If the problem was that root.sh was run during an upgrade, run rootupgrade.sh to do the upgrade.

CLSRSC-00671: Pre-patch steps for patching GI home successfully completed.

Cause: This is a status message.

Action: None

CLSRSC-00672: Post-patch steps for patching GI home successfully completed.

Cause: This is a status message.

Action: None

CLSRSC-00673: Multiple sites 'string' are associated with the site GUID 'string'.

Cause: An attempt to check the site and site GUID information failed because multiple sites were associated with the indicated site GUID.

Action: If this problem occurred on an Oracle Exadata Database Machine (Exadata), issue the command 'cellcli alter cell siteID= site GUID', and then rerun the root script. If this problem did not occur on an Exadata machine, contact Oracle Support Services.

CLSRSC-00674: Multiple site GUIDs 'string' are associated with the site name 'string'.

Cause: An attempt to check the site and site GUID information failed because multiple site GUIDs were associated with the indicated site name.

Action: If this problem occurred on an Oracle Exadata Database Machine (Exadata), issue the command 'cellcli alter cell siteName= site name', and then rerun the root script. If this problem did not occur on an Exadata machine, contact Oracle Support Services.

CLSRSC-00675: Cluster-wide Grid Plug and Play profile not found on this node.

Cause: The Grid Plug and Play profile was not found on this node. The node may have been unreachable when the profile was created and distributed during an earlier install operation.

Action: Resolve the network connectivity issue and then resume the installation.

CLSRSC-00676: failed to install the USM driver

Cause: An attempt to install the USM driver was rejected because the environment variable ODMDIR was not set.

Action: Set the environment varialble ODMDIR and retry the operation.

CLSRSC-00677: mismatch between site name and site GUID

Cause: An attempt to execute the root script failed because the OUI input was not properly validated prior to install. This is an internal error.

Action: Contact Oracle Support Services.

CLSRSC-00678: failed to stop one or more applications using the GIMR database

Cause: An error occurred while attempting to stop one or more applications using the Grid Infrastructure Management Repository (GIMR) database. The accompanying messages provide detailed failure information.

Action: Correct the problems indicated in the accompanying messages, then retry the operation.

CLSRSC-00679: failed to disable ACFS resources with the older Clusterware

Cause: An error occurred while disabling ACFS resources during upgrade. The accompanying messages provide detailed failure information.

Action: Correct the problems indicated in the accompanying messages, then retry the operation.

CLSRSC-00680: Successfully converted Oracle Autostart to a one node cluster.

Cause: This is a status message.

Action: None

CLSRSC-00681: failed to convert Oracle Autostart to a one node cluster

Cause: An error occurred during the conversion of Oracle Autostart to a one node cluster. Specific details were included in the accompanying error messages.

Action: Correct the problems indicated in the accompanying error messages and then rerun the root script.

CLSRSC-00683: failed to add OCR to Oracle ASM disk group string

Cause: An error occurred while adding Oracle Cluster Registry (OCR) to the indicated Oracle ASM disk group. Specific details were included in the accompanying error messages.

Action: Correct the problems indicated in the accompanying error messages and then rerun the root script.

CLSRSC-00684: failed to delete OCR from location string

Cause: An error occurred while deleting Oracle Cluster Registry (OCR) from the indicated existing location. Specific details were included in the accompanying error messages.

Action: Correct the problems indicated in the accompanying error messages and then rerun the root script.

CLSRSC-00685: failed to migrate the voting files to Oracle ASM disk group string

Cause: An error occurred while migrating voting files to the indicated Oracle ASM disk group. Specific details were included in the accompanying error messages.

Action: Correct the problems indicated in the accompanying error messages and then rerun the root script.

CLSRSC-00686: failed to increase the size of the file 'string' to stringMB (error: string)

Cause: An attempt to configure a disk group on NAS failed because an error occurred while increasing the size of the indicated file. The indicated operating system error provides specific failure information.

Action: Review the accompanying operating system error for additional details. Ensure that the indicated file system has sufficient free space. Correct the problem and rerun the root script.

CLSRSC-00687: Internal error for: string

Cause: An internal error occurred. The included value is an internal identifier.

Action: Oracle internal error. Contact Oracle Support Services.

CLSRSC-00690: failed to start one or more applications which use the GIMR database

Cause: An error occurred while attempting to start one or more applications which use the Grid Infrastructure Management Repository (GIMR) database. The accompanying messages provide detailed failure information.

Action: Correct the problems indicated in the accompanying messages, then retry the operation.

CLSRSC-00694: failed to validate CRS entities for upgrade, aborting the upgrade

Cause: An attempt to upgrade CRS was aborted because an error occurred while performing pre-upgrade checks on CRS entities. Accompanying error messages provide detailed failure information.

Action: Review the root script logs for error information during the pre-upgrade checks. Contact Oracle Support Services for further action.

CLSRSC-00696: failed to remove Grid Infrastructure node applications

Cause: An error occurred while attempting to remove node applications. The accompanying messages provided detailed failure information.

Action: Examine the accompanying messages, resolve the indicated problems, and then retry the operation.

CLSRSC-00697: Failed to get the value of environment variable 'string' from the environment file 'string'

Cause: An attempt to read the value of the indicated environment variable from the indicated environment file failed, either because the file could not be read, or because the variable was missing from the file.

Action: Ensure that the indicated file exists and is readable, and that the indicated variable exists in the file.

CLSRSC-00698: Successfully upgraded Oracle Restart to Oracle Autostart.

Cause: This is a status message.

Action: None

CLSRSC-00699: Failed to upgrade Oracle Restart to Oracle Autostart.

Cause: An error occurred while attempting to upgrade to Oracle Autostart. Additional failure information is provided in the accompanying messages.

Action: Correct the problems indicated in the accompanying messages and retry the upgrade.

CLSRSC-00700: Disk group 'string' contains invalid characters in its name.

Cause: An attempt to upgrade Oracle ASM to version 12.2.0.2.0 or higher was rejected because one or more disk group names contained invalid characters. Starting in version 12.2.0.2.0, disk group names should only contain letters, numbers, and the underscore character.

Action: Use the 'renamedg' tool to change the disk group name to a valid name. Then, change the names of the disks by mounting the disk group in restricted mode and using the ASM SQL command 'ALTER DISKGROUP diskgroupname RENAME DISKS ALL'. Ensure all control files used by this disk group point to the new disk group name by using the SQL command 'ALTER SYSTEM SET CONTROL\_FILES'. Specify the new disk group name for the database and update the disk group, server parameter file and password file configuration using the command 'srvctl modify database -db <db\_unique\_name> -spfile spfile -pwfile <password\_file\_path> -diskgroup <new\_dg\_name>', and then retry the upgrade operation.

CLSRSC-00701: failed to stop Oracle Clusterware

Cause: An error occurred while executing the command 'crsctl stop cluster'.

Action: Stop Oracle Clusterware with the command 'crsctl stop cluster -f' and rerun the root script.

CLSRSC-00702: failed to convert the storage access on local node string

Cause: An attempt to convert the storage access on the local node was rejected because the operation was only supported on an Oracle Member Cluster using the Oracle ASM service from the Domain Services Cluster.

Action: Rerun the command on an Oracle Member Cluster.

CLSRSC-00703: Successfully converted storage access on local node string.

Cause: This is a status message.

Action: None

CLSRSC-00704: Successfully converted storage access on Oracle Member Cluster string.

Cause: This is a status message.

Action: None

CLSRSC-00708: failed to create directory string in directory string

Cause: An attempt to run the root script failed because an error occurred in creating the indicated directory in the indicated target directory.

Action: Ensure that the indicated target directory is writable and retry executing the root script.

CLSRSC-00709: failed to read the Cluster Manifest File string

Cause: An attempt to modify storage access of the member cluster failed because the Cluster Manifest File was not valid.

Action: Verify that the Cluster Manifest File is valid and accessible. Ensure that the user has read access permission for the Cluster Manifest File, and then rerun the root script.

CLSRSC-00710: Adding node aborting because a Grid Infrastructure software upgrade is in progress.

Cause: An attempt to add a node failed because execution of the root script aborted after detecting that a Grid Infrastructure (GI) software upgrade was in progress.

Action: Following successful completion of the GI upgrade processing on all nodes, and then retry the add-node operation from the beginning.

CLSRSC-00711: failed to modify resource string during upgrade

Cause: The execution of the script rootupgrade.sh did not complete because an error occurred while modifying the indicated resource using the command 'crsctl modify resource'.

Action: Examine the accompanying messages, correct reported problems and retry rootupgrade.sh.

CLSRSC-00712: failed to save the attributes of the OHASD resources

Cause: An attempt to record the values of the OHASD resource attributes failed because an error occurred while retrieving the values of the attributes of the OHASD resource. This message is accompanied by others providing details of the error.

Action: Correct the problems indicated by the accompanying messages and retry.

CLSRSC-00713: failed to update the attributes of the OHASD resources

Cause: An attempt to update the OHASD resources attributes failed. This message is accompanied by others providing details of the error.

Action: Correct the problems indicated by the accompanying messages and retry.

CLSRSC-00714: failed to retrieve the value of resource attributes during upgrade

Cause: The execution of the script rootupgrade.sh did not complete because an error occurred while executing the command 'crsctl query resource'.

Action: Examine the accompanying messages, correct reported problems and retry rootupgrade.sh.

CLSRSC-00715: failed to copy the RHP configuration file string during downgrade

Cause: An attempt to downgrade the Oracle Clusterware failed because an error occurred in copying the Rapid Home Provisioning (RHP) configuration files to the Oracle base. The accompanying messages provide detailed failure information.

Action: Correct the problems indicated in the accompanying messages and retry.

CLSRSC-00716: RHP could not be configured in local mode. Continuing with the Grid Infrastructure configuration to complete the install or upgrade.

Cause: An attempt to configure Rapid Home Provisioning (RHP) in local mode failed. The accompanying messages provide detailed failure information.

Action: After completion of the install or upgrade, examine the accompanying messages and resolve the indicated issues. Then configure RHP using the command 'srvctl add rhpserver -diskgroup dgname -storage storage-path -local'.

CLSRSC-00717: failed to initiate the conversion of a Standalone Clutster to a Member Cluster on a non-standalone cluster

Cause: An attempt to initiate the conversion of a Standalone Clutster to a Member Cluster failed, because the operation was not supported on a non-standalone cluster.

Action: Retry executing the root script on a Standalone Cluster.

CLSRSC-00718: Succeeded extracting cluster information on a Standalone Cluster. Copy the contents of the directory 'string' to the Domain Services Cluster before proceeding to the next step.

Cause: This is a status message.

Action: None

CLSRSC-00719: failed to create a manifest file for a Member Cluster on a non-Domain Services Cluster

Cause: An attempt to create a manifest file for a Member Cluster failed, because the operation was not initiated on a Domain Services Cluster.

Action: Retry executing the root script on the Domain Services Cluster serving the Member Cluster.

CLSRSC-00720: failed to initiate the conversion to a Member Cluster because the versions of the Standalone Cluster and the Domain Services Cluster do not match

Cause: An attempt to initiate the conversion to a Member Cluster failed, because the versions of the Standalone Cluster and the Domain Services Cluster did not match. The clusters must have the same version.

Action: Ensure that both clusters have the same version before attempting to convert a Standalone Cluster to a Member Cluster.

CLSRSC-00721: Succeeded creating the Member Cluster configuration manifest file. Copy the manifest file 'string' to the Standalone Cluster before converting it to a Member Cluster.

Cause: This is a status message.

Action: None

CLSRSC-00722: The local node has been successfully converted to a Member Cluster node.

Cause: This is a status message.

Action: None

CLSRSC-00723: failed to initiate the conversion to a Member Cluster for cluster with version less than 19c

Cause: An attempt to initiate the conversion to a Member Cluster failed, because the cluster version was lower than 19c, and conversion to Member Cluster was supported only for versions 19c and above.

Action: Upgrade the cluster to at least version 19c, and then retry executing the root script.

CLSRSC-00725: The rootcrs script is not running from the home being patched, which should be 'string'.

Cause: An attempt to patch the home failed, because the rootcrs script was not running from the home being patched.

Action: Rerun the rootcrs script from the home indicated in the message.

CLSRSC-00726: failed to set root script upgrade end marker

Cause: An attempt to execute the root script failed due to an unexpected error encountered in setting the root script upgrade end marker. The accompanying messages provide detailed failure information.

Action: Address the issues raised in the accompanying messages and rerun the root script. If the problem persists, contact Oracle Support Services.

CLSRSC-00731: unable to join the local node to a cluster that's not completely upgraded

Cause: An attempt to join the local node was rejected because the cluster to be joined had not been completely upgraded.

Action: Finish upgrade on the cluster and then retry joining this node to the upgraded cluster.

CLSRSC-00732: The Oracle home string does not exist on the nodes string.

Cause: The given Oracle home was not found on some nodes.

Action: Contact Oracle Support Services.

CLSRSC-00733: failed to delete the Oracle service 'string'

Cause: An error occurred while trying to delete the Oracle service.

Action: Delete the indicated service using Service Control with commands "sc.exe stop" and "sc.exe delete", and then retry the operation. If the problem persists, contact Oracle Support Services.

CLSRSC-00734: Failed to determine the last node for upgrade

Cause: The upgrade failed due to an error in setting the last node name in the Oracle Cluster Registry.

Action: This is an internal error, contact Oracle Support Services.

CLSRSC-00735: A non-rolling upgrade failed due to active remote nodes 'string'

Cause: The indicated nodes were down at the time the upgrade was initiated, but now they are found to be running.

Action: To perform a non-rolling upgrade, stop the Grid Infrastructure stack on the remote nodes and rerun the root script on this node. To perform a rolling upgrade, exit and rerun gridSetup.

CLSRSC-00736: failed to retrieve GUID (Globally Unique Identifier) for ASM

Cause: An error occurred while accessing GUID.

Action: Correct the problem indicated in the accompanying messages and then retry the operation. Contact Oracle Support Services if the problem persists.

CLSRSC-00737: failed to retrieve cell configuration information

Cause: An error occurred while accessing the configuration information from the cell.

Action: Correct the problem indicated in the accompanying messages and then retry the operation. Contact Oracle Support Services if the problem persists.

CLSRSC-00738: failed to find a node number for the current node 'string'

Cause: Could not find the current node in the node list.

Action: Internal Error. Contact Oracle Support Services.

CLSRSC-00739: cannot run the postpatch operation because the prepatch operation did not complete successfully

Cause: An attempt to run the postpatch operation failed because the prepatch operation did not complete successfully.

Action: Complete the prepatch operation and then retry the postpatch operation.

CLSRSC-00740: inconsistent options specified to the postpatch command

Cause: An attempt to run the postpatch operation was rejected because the specified option ('-nonrolling' or '-dstcrshome') was not earlier specified in the prepatch operation. The options specified in the prepatch and postpatch operations must be the same.

Action: Retry the postpatch operation, specifying the same options that were previously specified in the prepatch operation.

CLSRSC-00741: invalid storage type provided for Oracle Cluster Registry

Cause: The storage type provided for the Oracle Cluster Registry was invalid.

Action: Provide a valid ASM disk group or a shared NFS or Oracle Cluster File System (OCFS) location for Oracle Cluster Registry.

CLSRSC-00742: failed to disable ASM configuration

Cause: An error occurred while executing the 'srvctl disable asm' command.

Action: Correct the problem indicated in the accompanying messages, then rerun the root script.

CLSRSC-00743: failed to create key 'string' in the Oracle Cluster Registry (OCR)

Cause: An attempt to execute the root script failed because an error occurred when creating the indicated key in the Oracle Cluster Registry (OCR). The accompanying messages provide detailed failure information.

Action: Correct the problem indicated in the accompanying messages and then rerun the root script. If the problem persists, contact Oracle Support Services.

CLSRSC-00744: File string not found

Cause: The specified file either does not exist or is not accessible.

Action: Ensure the file is available for read and execute access.

CLSRSC-00745: Failed to configure ASM.

Cause: There was a failure when configuring ASM.

Action: Correct the problem indicated in the accompanying messages and then rerun the root script. If the problem persists, contact Oracle Support Services.

CLSRSC-00746: Waiting for nodes 'string' to complete the upgrade before proceeding with last node operations.

Cause: This is a status message.

Action: None

CLSRSC-00747: The root script cannot proceed on this node string until the upgrade is successfully completed on nodes 'string'.

Cause: An attempt to run the root script on this node failed because the root script had not completed on the specified nodes.

Action: Ensure that the root script upgrade has successfully completed execution on the specified nodes and then restart the root script on this node.

CLSRSC-00748: failure while waiting for all nodes to successfully complete the upgrade

Cause: An error occurred while waiting for all nodes to complete the upgrade.

Action: Correct the problem indicated in the accompanying message and then retry the root script. If the problem persists, contact Oracle Support Services.

CLSRSC-00749: Prepatch operations have already been performed successfully.

Cause: The checkpoint for ROOTCRS\_PREPATCH contains a SUCCESS value, which indicates the prepatch operations have already been performed successfully.

Action: None

CLSRSC-00750: Another invocation of the root script is running.

Cause: The invocation of the root script is stopped because another invocation is running.

Action: Wait for the current invocation of the root script to finish.

CLSRSC-00751: incorrect invocation of script string in an Oracle Restart environment

Cause: The Oracle Clusterware root script was invoked in an Oracle Restart environment.

Action: Run the root script for Oracle Restart instead.

CLSRSC-00752: incorrect invocation of script string called on a Grid Infrastructure cluster node

Cause: The Oracle Restart root script was invoked on a Grid Infrastructure cluster node.

Action: Run the root script for Oracle Clusterware instead.

CLSRSC-00753: Flex ASM credentials are not found at string

Cause: The Flex ASM credentials are not found when upgrading from a Flex ASM configuration.

Action: Contact Oracle Support Services.

CLSRSC-00754: Cannot do an upgrade to the home string since the major release version string is same as the version of the configured home string

Cause: The upgrade script was incorrectly invoked outside an upgrade context.

Action: To apply an RU or a patch, use the patching procedure.

CLSRSC-00755: Cannot patch to the home string since its major release version string is different from the version string of the configured home string

Cause: The patching script was incorrectly invoked outside a patching context.

Action: To do an upgrade, use the upgrade procedure.

CLSRSC-00756: Aborting the deconfiguration because a Grid Infrastructure upgrade is in progress

Cause: There was an attempt to deconfigure while the Grid Infrastructure (GI) upgrade was in progress, which is disallowed.

Action: If the intention is to remove the GI configuration, use the delete node procedure or the deinstall tool.

CLSRSC-00757: The oracle binary is not linked appropriately with RAC.

Cause: An attempt to run the root script failed because the oracle binary was not linked with rac\_on for a cluster environment.

Action: Relink the oracle binary by executing cd <GI\_home>/rdbms/lib; make -f ins\_rdbms.mk rac\_on ioracle.

CLSRSC-00758: The oracle binary is not linked appropriately without RAC.

Cause: An attempt to run the root script failed because the oracle binary was linked with rac\_on for a Oracle Restart environment.

Action: Relink the oracle binary by executing cd <GI\_home>/rdbms/lib; make -f ins\_rdbms.mk rac\_off ioracle.

CLSRSC-00759: Upgrading Oracle Grid Infrastructure (GI) without performing downgrade after an online abort is not supported

Cause: An attempt to run the upgrade script failed because the GI upgrade was aborted online, but the GI was not yet downgraded.

Action: Rerun the upgrade after downgrading the GI.

CLSRSC-00761: Empty site name for the local host string.

Cause: An attempt to execute the root script failed due to an unexpected error encountered in retrieving the value from the configuration information.

Action: Address the issues raised in the accompanying messages and rerun the root script. If the problem persists, contact Oracle Support Services.

CLSRSC-00762: Empty site GUID for the local site name string.

Cause: An attempt to execute the root script failed due to an unexpected error encountered in retrieving the value from the configuration information.

Action: Address the issues raised in the accompanying messages and rerun the root script. If the problem persists, contact Oracle Support Services.

CLSRSC-00763: failed to upgrade Grid Plug and Play (GPnP) wallets

Cause: An attempt to upgrade GPnP wallets failed due to an unexpected error.

Action: Address the issues raised in the accompanying messages and rerun the GPnP wallet upgrade script. If the problem persists, contact Oracle Support.

CLSRSC-00897: ACFS driver unload actions failed

Cause: An error occurred while unloading ACFS drivers using the 'acfsload stop' command. The accompanying messages provide detailed failure information.

Action: Examine the accompanying messages, resolve the indicated problems, and then retry the operation.

CLSRSC-00898: failed to import ACFS Credentials for this Member Cluster

Cause: An attempt to run the root script failed because of a failure to set up the ACFS Remote resources, which could not be accomplished because the ACFS credentials could not to be imported into the Oracle Cluster Registry (OCR) from the provided Cluster Manifest File. Additional failure information is provided in the accompanying ACFS messages.

Action: Correct the problems indicated in the accompanying ACFS messages and retry the root script. If the problem persists, contact Oracle Support Services.

CLSRSC-00899: failed to start the ACFS Remote resources

Cause: An attempt to run the root script failed because of a failure to start the ACFS Remote resources.

Action: Correct the problems indicated in the accompanying ACFS messages and retry the root script. If the problem persists, contact Oracle Support Services.

CLSRSC-00900: Failed to change the modification time on file 'string'. Error 'string'.

Cause: An attempt to change the modification time on the indicated file failed.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00901: The destination GI home specified for out-of-place patching is the same as the configured GI home.

Cause: Either the destination GI home supplied in the command line for out-of-place patching was the same as the active GI home where the GI stack was running, or the current GI home was already switched to the destination GI home as part of out-of-place patching.

Action: None

CLSRSC-00902: Zero-Downtime Oracle Grid Infrastructure Patching not supported for the current operating system: string.

Cause: An attempt to use the -transparent option during the postpatch operation was rejected because that option was not supported on the indicated operating system.

Action: Reissue the postpatch command without the -transparent option.

CLSRSC-00903: Zero-Downtime Oracle Grid Infrastructure Patching is not supported for Oracle Restart.

Cause: An attempt to use the -transparent option during the postpatch operation for an Oracle Restart Standalone Configuration was rejected because that option was not supported for that configuration.

Action: Reissue the postpatch command without the -transparent option.

CLSRSC-00905: Zero-Downtime Oracle Grid Infrastructure Patching is only supported for out-of-place patching.

Cause: An attempt to use the -transparent option during the postpatch operation was rejected because the -dstcrshome option was required, but was not provided.

Action: Reissue the postpatch command without the -transparent option, or with both the -transparent option and the -dstcrshome option.

CLSRSC-00906: Zero-Downtime Oracle Grid Infrastructure Patching requires at least 2 Hub nodes to be running.

Cause: An attempt to use the -transparent option during the postpatch operation was rejected because the Cluster had only one Hub node running.

Action: Reissue the postpatch command without the -transparent option, or at a time when at least two Hub nodes are running.

CLSRSC-00907: Zero-Downtime Oracle Grid Infrastructure Patching is not supported on a Leaf node.

Cause: An attempt to use the -transparent option during the postpatch operation was rejected because the command was issued on an Oracle Clusterware Leaf node.

Action: Reissue the postpatch command without the -transparent option or reissue the postpatch command on a Hub node.

CLSRSC-00908: The -nodriverupdate option is required for out-of-place Zero-Downtime Oracle Grid Infrastructure Patching.

Cause: An attempt to use the -transparent option during the postpatch operation was rejected because the -nodriverupdate option was required, but was not provided. The -nodriverupdate option was required because the drivers contained in the patch were different from the drivers specified in the Grid Infrastructure inventory.

Action: Reissue the postpatch command without the -transparent option, or with both the -transparent option and the -nodriverupdate option.

CLSRSC-00909: Oracle Clusterware is not running on this node.

Cause: An attempt to use the -transparent option during the postpatch operation was rejected because the Oracle Clusterware was not running.

Action: Reissue the postpatch command without the -transparent option or at a time when Oracle Clusterware is running.

CLSRSC-00910: Improper option specified for command rootcrs.pl -postpatch -transparent

Cause: An attempt to re-execute the root script to perform post patch processing with the -transparent option was rejected because it had not been specified in the previous post patch run.

Action: Retry executing the root script with -postpatch but without the -transparent option.

CLSRSC-00911: Zero-Downtime Oracle Grid Infrastructure Patching is supported only for standalone cluster.

Cause: An attempt to perform postpatch processing using the -transparent option was rejected because the cluster class is not a standalone cluster.

Action: Reissue the postpatch command without the -transparent option.

CLSRSC-00912: Zero-Downtime Oracle Grid Infrastructure Patching is supported only for Oracle Clusterware version 18.0.0.0.0 or later.

Cause: An attempt to perform postpatch processing using the -transparent option was rejected because the Oracle Clusterware active version on the cluster was earlier than 18.0.0.0.0.

Action: Reissue the postpatch command without the -transparent option, or after the cluster has been upgraded to version 18.0.0.0.0 or later.

CLSRSC-00913: Zero-Downtime Oracle Grid Infrastructure Patching cannot be performed because the system is busy.

Cause: An attempt to perform postpatch processing using the -transparent option were rejected because there was not enough resources to execute transparent patching.

Action: Reissue the postpatch command without the -transparent option, or at a time when the system is less busy.

CLSRSC-00914: ASM prepatch operation failed.

Cause: An attempt to perform prepatch for ASM failed.

Action: Correct the problems indicated in the accompanying messages and retry the root script.

CLSRSC-00915: ASM postpatch operation failed.

Cause: An attempt to perform postpatch for ASM failed.

Action: Correct the problems indicated in the accompanying messages and retry the root script.

CLSRSC-00916: Failed to connect to ASM instance with DBI.

Cause: An attempt to perform operation in ASM with DBI failed because ASM connection failed or the ASM instance handle is invalid.

Action: Ensure that the ASM is connected and ASM instance handle is valid. Retry the root script.

CLSRSC-00917: Failed to online all disks during ASM postpatch.

Cause: An attempt to online all disks during ASM postpatch failed.

Action: Ensure that all disks in all diskgroups are online during postpatch. Retry the root script.

CLSRSC-00918: Zero-Downtime Oracle Grid Infrastructure Patching cannot be performed because the Cluster Synchronization Services misscount does not meet the time required. The current Cluster Synchronization Services misscount is string seconds.

Cause: An attempt to perform postpatch processing using the -transparent option was rejected because there was not enough time to execute transparent patching. At least 30 seconds Cluster Synchronization Services misscount is required.

Action: Reissue the postpatch command without the -transparent option or change the Cluster Synchronization Services misscount to 30 seconds or higher.

CLSRSC-00919: Failed to update the available Oracle drivers versions.

Cause: An error occurred while updating the versions of available drivers.

Action: Oracle drivers version will be updated on the next Oracle Clusterware start. To force an update, stop and start Oracle Clusterware.

CLSRSC-00920: failed to unlock the GI home since the configuration file string does not exist

Cause: The home being unlocked is not configured.

Action: Run the unlock operation by providing the GI home using the -dstcrshome option.

CLSRSC-00921: failed to register Oracle High Privileged Mode (Oracle HPM) service

Cause: Internal error.

Action: If the problem persists, contact Oracle Support Services.

CLSRSC-00922: failed to start Oracle High Privileged Mode (Oracle HPM) service

Cause: An attempt to start the Oracle High Privileged Mode (Oracle HPM) service failed.

Action: Check the alert log and accompanying messages, correct the problem, and retry.

CLSRSC-00925: Invalid value for the parameter string in the crsconfig\_params file

Cause: The value of the indicated parameter is not valid or it conflicts with other parameter settings.

Action: Check the settings, correct the problem and retry.

CLSRSC-01001: Failed to add resource OC4J

Cause: An error occurred while executing the 'srvctl add oc4j' command.

Action: Correct the problem indicated in the accompanying messages.

CLSRSC-01002: Failed to create or update the wallet APPQOSADMIN

Cause: An error occurred while creating the wallet.

Action: Correct the problem indicated in the accompanying messages.

CLSRSC-01003: Failed to start resource OC4J

Cause: An error occurred while executing the 'srvctl start oc4j' command.

Action: Correct the problem indicated in the accompanying messages.

CLSRSC-01004: Failed to enable resource OC4J

Cause: An error occurred while executing the 'srvctl enable oc4j' command.

Action: Correct the problem indicated in the accompanying messages.

CLSRSC-01005: Failed to disable resource OC4J

Cause: An error occurred while executing the 'srvctl disable oc4j' command.

Action: Correct the problem indicated in the accompanying messages.

CLSRSC-01006: Failed to create the wallet APPQOSADMIN or associated users during upgrade.

Cause: An error occurred while creating the wallet APPQOSADMIN or the users oc4jadmin and qosadmin during the upgrade.

Action: Respond as follows: 1 - Correct the problem indicated in the accompanying messages. 2 - Rerun rootupgrade.sh.

CLSRSC-01007: Failed to start OC4J resource

Cause: An error occurred while executing the 'srvctl start oc4j' command.

Action: Respond as follows: 1 - Correct the problem indicated in the accompanying messages. 2 - Rerun rootupgrade.sh.

CLSRSC-01008: The script string either does not exist or is not executable.

Cause: The specified script did not exist or was not executable.

Action: Make sure the script exists and it has execute access.

CLSRSC-01009: failed to stop resource OC4J

Cause: An error occurred while executing the 'srvctl stop oc4j' command.

Action: Correct the problems indicated in the accompanying messages and rerun rootupgrade.sh

CLSRSC-01100: failed to add resource 'qosmserver'

Cause: An error occurred while executing the 'srvctl add qosmserver' command.

Action: Correct the problem indicated in the accompanying messages and retry.

CLSRSC-01101: failed to enable resource 'qosmserver'

Cause: An error occurred while executing the 'srvctl enable qosmserver' command.

Action: Correct the problem indicated in the accompanying messages and retry.

CLSRSC-01102: failed to start resource 'qosmserver'

Cause: An error occurred while executing the 'srvctl start qosmserver' command.

Action: Correct the problem indicated in the accompanying messages and retry.

CLSRSC-01103: failed to disable resource 'qosmserver'

Cause: An error occurred while executing the 'srvctl disable qosmserver' command.

Action: Correct the problem indicated in the accompanying messages and retry.

CLSRSC-01104: failed to stop resource 'qosmserver'

Cause: An error occurred while executing the 'srvctl stop qosmserver' command.

Action: Correct the problem indicated in the accompanying messages and retry.

CLSRSC-01105: failed to create the credential store for resource 'qosmserver'

Cause: An error occurred while executing the 'qosctl -install' command.

Action: Correct the problem indicated in the accompanying messages and retry.

CLSRSC-01106: failed to upgrade the credential store for resource 'qosmserver'

Cause: An error occurred while executing the 'qosctl -upgrade' command.

Action: Correct the problem indicated in the accompanying messages and retry.

CLSRSC-01107: failed to copy the 'ora.qosmserver' configuration file string during downgrade

Cause: An attempt to downgrade the 'ora.qosmserver' failed because an error occurred while copying the configuration files to the Oracle base. The accompanying messages provide detailed failure information.

Action: Correct the problems indicated in the accompanying messages and retry.

CLSRSC-01108: failed to copy the 'ora.qosmserver' configuration files from the Oracle Home string to the Oracle base string.

Cause: An error occurred while copying the 'ora.qosmserver' configuration files to the Oracle base. The accompanying messages provide detailed failure information.

Action: Correct the problems indicated in the accompanying messages and retry.

CLSRSC-01109: failed to delete the 'ora.qosmserver' configuration files from Oracle Base 'string.'

Cause: An error occurred while deleting the 'ora.qosmserver' configuration files in the Oracle Base. The accompanying messages provide detailed failure information.

Action: Correct the problems indicated in the accompanying messages and retry.

CLSRSC-02000: Failed to enable CRS after successfully installing the OKA drivers.

Cause: After successfully configuring OKA during an install, upgrade, or patch, the root script failed to enable CRS again, using the command 'crsctl enable crs'.

Action: Correct the errors accompanying the failure of the enable command and rerun the install configuration step.

CLSRSC-02001: Failed to disable CRS in preparation for a node reboot.

Cause: After failure to install OKA drivers, an attemmpt to disable CRS in preparation for a node reboot was unsuccessful.

Action: Correct the errors accompanying the failure of the disable command, run 'crsctl disable crs', reboot, and resume the install configuration step.

CLSRSC-02002: Failed to enable CRS after successfully uninstalling the OKA drivers.

Cause: After successfully deconfiguring OKA during a downgrade, the root script failed to re-enable CRS using the command 'crsctl enable crs'.

Action: Correct the errors accompanying the failure of the enable command and rerun the deconfiguration step.

CLSRSC-02003: An operating system reboot is required to continue the deconfiguration.

Cause: The uninstall of the OKA drivers failed. An operating system reboot is required to continue the deconfiguration.

Action: Reboot the node and restart the deconfiguration step.

CLSRSC-02004: Failed to disable CRS in preparation for a node reboot.

Cause: An attempt to disable CRS in preparation for a system reboot failed. The reboot is associated with a failed removal of OKA drivers.

Action: Correct the errors accompanying the failure of the disable command, run 'crsctl disable crs', reboot, and continue the deconfiguration step.

CLSRSC-02006: Failed to create the OKA drivers resource but continuing with the installation

Cause: An error occurred while creating the OKA drivers resource.

Action: Contact Oracle Support Services.

CLSRSC-02007: OKA driver install actions failed

Cause: An error occurred while installing OKA drivers using the 'okaroot install' command.

Action: Examine the accompanying messages from the 'okaroot install' command, correct the problem and retry.

CLSRSC-02008: A system reboot is required to continue installing.

Cause: The installation of new OKA drivers requires a node reboot to continue the install.

Action: Reboot the node and rerun the install configuration step.

CLSRSC-02009: Failed to create and start the OKA drivers resource but continuing with patching

Cause: An error occurred while creating and starting the OKA drivers resource.

Action: Check if your OS kernel is supported and run 'okaroot enable' to create and start the OKA drivers resource.

CLSRSC-02501: The AFD driver install actions failed.

Cause: An error occurred while installing the AFD driver using the 'afdroot install' command.

Action: Examine the accompanying messages from the 'afdroot install' command, correct the problem and retry.

CLSRSC-02502: A system reboot is required to continue installing.

Cause: Installation of the new AFD driver requires a reboot to continue.

Action: Reboot the node and rerun the install configuration step.

CLSRSC-02503: Failed to add resource 'string'

Cause: An error occurred while attempting to add AFD resource.

Action: Correct the problem indicated in the accompanying messages and retry the command.

CLSRSC-02504: Failed to rescan devices with 'afdtool -rescan'

Cause: An error occurred while executing the 'afdtool -rescan' command.

Action: Correct the problem indicated in the accompanying messages and retry the command.

CLSRSC-02505: An operating system reboot is required to continue the operation.

Cause: The uninstall of the AFD driver failed. An operating system reboot is required to continue the upgrade or deconfiguration.

Action: Reboot the node and restart the operation.

CLSRSC-02506: An operating system reboot is required at the end of the deinstall.

Cause: The uninstall of the AFD driver failed. An operating system reboot is required to complete the deinstall.

Action: Reboot the node after deinstall.

CLSRSC-02601: Failed to add Oracle Cluster Health Analysis resource

Cause: An error occurred while executing the 'srvctl add cha' command.

Action: Correct the problem indicated in the accompanying messages and retry the command.

CLSRSC-02602: Failed to forcibly add Oracle Cluster Health Analysis resource

Cause: An error occurred while executing the 'srvctl add cha -force' command.

Action: Correct the problem indicated in the accompanying messages and retry the command.

CLSRSC-02603: Failed to start Oracle Cluster Health Analysis resource

Cause: An error occurred while executing the 'srvctl start cha' command.

Action: Correct the problem indicated in the accompanying messages and retry the command.

CLSRSC-02604: Failed to set the TARGET to ONLINE for Oracle Cluster Health Analysis resource

Cause: An error occurred while executing the 'srvctl start cha' command.

Action: Correct the problem indicated in the accompanying messages and retry the command.

CLSRSC-02605: failed to export Oracle Cluster Health Analysis user models

Cause: An error occurred while exporting user models of Oracle Cluster Health Analysis.

Action: Check the read permissions on User models and write permissions on Grid Home.

CLSRSC-03000: Invalid object 'string' specified on command line.

Cause: The object specified on the command line was not recognized.

Action: Use appcluster.pl with the --help option to display valid options. Ensure that a valid option is specified.

CLSRSC-03002: Oracle Clusterware has already been configured for non-database applications.

Cause: A request to configure Oracle Clusterware for non-database applications was rejected because Clusterware is already configured for non-database applications.

Action: If this is the expected state then this is not an error. If it is not then Oracle Clusterware can be de-configured and configured.

CLSRSC-03003: Cannot configure Oracle Restart for non-database applications (Clusterware is only for clusters).

Cause: A request configure Oracle Clusterware for non-database applications was rejected because Oracle Grid Infrastructure for a stand-alone server (Oracle Restart) was configured.

Action: De-configure Oracle Restart and configure Oracle Clusterware.

CLSRSC-03004: Failed to gather the configuration information for the node applications.

Cause: An error occurred while gathering the configuration information for the node applications.

Action: Correct the problem indicated in the accompanying messages, and then retry.

CLSRSC-04000: Oracle Autonomous Health Framework (AHF) is not supported on this platform.

Cause: Informational message.

Action: None

CLSRSC-04001: Installing Oracle Autonomous Health Framework (AHF).

Cause: Informational message.

Action: None

CLSRSC-04002: Successfully installed Oracle Autonomous Health Framework (AHF).

Cause: This is a status message.

Action: None

CLSRSC-04003: Successfully patched Oracle Autonomous Health Framework (AHF).

Cause: This is a status message.

Action: None

CLSRSC-04004: Failed to install Oracle Autonomous Health Framework (AHF). Grid Infrastructure operations will continue.

Cause: The Installation of Oracle Autonomous Health Framework (AHF) failed with the accompanying errors.

Action: The Oracle Autonomous Health Framework (AHF) will not be available, but Grid Infrastructure operation is unaffected. Address the issues reported by accompanying messages and retry using the command '<GI\_Home>/crs/install/ahf\_setup -crshome <GI\_Home>'. If the problem persists, contact Oracle Support Services for further action.

CLSRSC-04005: Failed to patch Oracle Autonomous Health Framework (AHF). Grid Infrastructure operations will continue.

Cause: An attempt to patch Oracle Autonomous Health Framework (AHF) failed with the accompanying errors.

Action: The Oracle Autonomous Health Framework (AHF) may not be available, but Grid Infrastructure operation is unaffected. Address the issues reported by accompanying messages and retry using the command '<GI\_Home>/crs/install/ahf\_setup -crshome <GI\_Home>'. If the problem persists, contact Oracle Support Services for further action.

CLSRSC-04006: Removing Oracle Autonomous Health Framework (AHF).

Cause: Informational message.

Action: None

CLSRSC-04007: Successfully removed Oracle Autonomous Health Framework (AHF).

Cause: This is a status message.

Action: None

CLSRSC-04008: Failed to remove Oracle Autonomous Health Framework (AHF) from home location 'string'. Grid Infrastructure operations will continue.

Cause: The accompanying errors occurred while running the Oracle Autonomous Health Framework (AHF) uninstall script.

Action: The Oracle Autonomous Health Framework (AHF) may not be available, but Grid Infrastructure operation is unaffected. Address the issues reported by accompanying messages and retry using the command '<GI\_Home>/bin/ahfctl uninstall'. If the problem persists, contact Oracle Support Services for further action.

CLSRSC-04009: Starting Oracle Autonomous Health Framework (AHF).

Cause: Informational message.

Action: None

CLSRSC-04010: Successfully started Oracle Autonomous Health Framework (AHF).

Cause: This is a status message.

Action: None

CLSRSC-04011: Failed to start Oracle Autonomous Health Framework (AHF). Grid Infrastructure operations will continue.

Cause: The Oracle Autonomous Health Framework (AHF) failed to start with the accompanying errors.

Action: The Oracle Autonomous Health Framework (AHF) failing to start, but Grid Infrastructure operation is unaffected. Address the issues reported by accompanying messages and retry using the command '<GI\_Home>/bin/ahfctl start'. If the problem persists, contact Oracle Support Services for further action.

CLSRSC-04012: Shutting down Oracle Autonomous Health Framework (AHF).

Cause: Informational message.

Action: None

CLSRSC-04013: Successfully shut down Oracle Autonomous Health Framework (AHF).

Cause: This is a status message.

Action: None

CLSRSC-04014: Failed to shut down Oracle Autonomous Health Framework (AHF). Grid Infrastructure operations will continue.

Cause: The Oracle Autonomous Health Framework (AHF) did not shut down for patching with the accompanying errors.

Action: A forcible stop will be issued so that patching can proceed, so no action is required.

CLSRSC-04015: Performing install or upgrade action for Oracle Autonomous Health Framework (AHF).

Cause: Informational message.

Action: None

CLSRSC-04016: Oracle Autonomous Health Framework (AHF) 'string' not found. Grid Infrastructure operations will continue.

Cause: Informational message.

Action: None

CLSRSC-05000: -ip option used when network is DHCP.

Cause: An attempt was made to use the -ip option when the network was using the Dynamic Host Configuration Protocol (DHCP).

Action: When DHCP is used, the IP address is specified by DHCP. Do not specify the -ip option when the network is DHCP.

CLSRSC-05001: GNS is not enabled.

Cause: An attempt to create an application VIP using appvipcfg was rejected because the Grid Naming Service (GNS) had not been enabled when the Dynamic Host Configuration Protocol (DHCP) was in use. GNS is required when the network is configured to use DHCP.

Action: Ensure that GNS is configured before attempting to create a VIP using appvipcfg when DHCP is in use.

CLSRSC-05002: IP address was up or already in use.

Cause: An attempt was made to use an IP address that was up or already in use by another resource.

Action: Use a different IP address.

CLSRSC-05101: conversion to extended cluster failed

Cause: An attempt to convert the cluster to an extended cluster encountered an error. The accompanying messages provide detailed failure information.

Action: Examine the accompanying messages, resolve the problems identified, and retry the operation.

CLSRSC-05102: Oracle Clusterware services are not running on node 'string'

Cause: An attempt to convert the cluster to an extended cluster failed because the node did not have all Oracle Clusterware services running.

Action: Start Oracle Clusterware services on the node using the command 'crsctl start crs' and retry the operation.

CLSRSC-05103: unable to add site 'string' to configuration

Cause: An attempt to convert the cluster to an extended cluster failed because there was an error while adding a site to the configuration. The accompanying messages provide detailed failure information.

Action: Examine the accompanying messages, resolve the problems identified, and retry the operation.

CLSRSC-05104: unable to associate node 'string' to site 'string'

Cause: An attempt to convert the cluster to an extended cluster failed because an error was encountered while associating a node to one of the sites configured. The accompanying messages provide detailed failure information.

Action: Examine the accompanying messages, resolve the problems identified, and retry the operation.

CLSRSC-05105: invalid or missing argument 'string'

Cause: An attempt to convert the cluster to an extended cluster failed because the indicated arguments were invalid or missing.

Action: Retry the operation passing valid arguments. The command 'rootcrs.sbs -help' displays the available options and arguments.

CLSRSC-05106: Invalid number of sites 'string'. The number of sites cannot exceed 'string'.

Cause: An attempt to convert the cluster to an extended cluster was rejected because the number of sites specified was greater than the maximum allowed.

Action: Retry the operation specifying a number of sites which is less than or equal to the maximum allowed.

CLSRSC-05107: invalid site name 'string' specified

Cause: An attempt to convert the cluster to an extended cluster was rejected because an invalid site name was specified.

Action: Retry the operation and specify a site name which is at least one character long but no more than 15 characters in length. A site name consists of alphanumeric characters and the hyphen (-) character (a..z,A..Z,0..9,-). It cannot begin or end with the hyphen (-) character.

CLSRSC-05108: 'rootcrs.pl -converttoextended -first' has not been issued

Cause: An attempt to convert the cluster to an extended cluster failed because the '-first' option was not specified.

Action: Retry the operation specifying the '-first' option on this node or retry the operation after the command 'rootcrs.pl -converttoextended -first' has completed successfully on another node.

CLSRSC-05109: site 'string' does not exist in the cluster configuration

Cause: An attempt to convert the cluster to an extended cluster failed because the option '-first' was not passed and the site name passed was not configured in the cluster.

Action: Retry the operation, either providing a site name that exists in the configuration or specifying the '-first' option.

CLSRSC-05110: unable to update ASM cardinality to 'string'

Cause: An attempt to convert a cluster to an extended cluster failed because an error was encountered while updating the ASM cardinality. The accompanying messages provide detailed failure information.

Action: Examine the accompanying messages, resolve the problems indentified, and retry the operation.

CLSRSC-05111: Node 'string' is a Leaf node.

Cause: An attempt to convert a cluster to an extended cluster failed because the indicated node was a Leaf node. An extended cluster cannot have Leaf nodes.

Action: Update the node role from Leaf to Hub using the command 'crsctl set node role', and retry the operation.

CLSRSC-05112: unable to get the current ASM cardinality

Cause: The command 'srvctl config asm -inner' failed to return the ASM cardinality.

Action: Examine the accompanying messages, resolve the problems identified, and retry the operation.

CLSRSC-06000: failed to generate cluster root certificate wallet file

Cause: An attempt to execute the root script failed due to an unexpected error encountered in generating the cluster root certificate wallet file. The accompanying messages provide detailed failure information.

Action: Address the issues raised in the accompanying messages and rerun the root script. If the problem persists, contact Oracle Support Services.

CLSRSC-06001: failed to store cluster root certificate in OLR-CREDSTORE

Cause: An attempt to execute the root script failed due to an unexpected error encountered in storing the cluster root certificate in OLR-CREDSTORE. The accompanying messages provide detailed failure information.

Action: Address the issues raised in the accompanying messages and rerun the root script. If the problem persists, contact Oracle Support Services.

CLSRSC-06002: failed to store cluster root certificate in OCR-CREDSTORE

Cause: An attempt to execute the root script failed due to an unexpected error encountered in storing the cluster root certificate in OCR-CREDSTORE. The accompanying messages provide detailed failure information.

Action: Address the issues raised in the accompanying messages and rerun the root script. If the problem persists, contact Oracle Support Services.

CLSRSC-06003: failed to create cluster root certificate domain in the CREDSTORE. Command: 'string'

Cause: An attempt to execute the root script failed due to an unexpected error encountered in creating the cluster root certificate domain in the CREDSTORE. The accompanying messages provide detailed failure information.

Action: Address the issues raised in the accompanying messages and rerun the root script. If the problem persists, contact Oracle Support Services.

CLSRSC-06004: failed to retrieve cluster root certificate from OCR-CREDSTORE

Cause: An attempt to execute the root script failed due to an unexpected error encountered in retrieving the cluster root certificate from OCR-CREDSTORE. The accompanying messages provide detailed failure information.

Action: Address the issues raised in the accompanying messages and rerun the root script. If the problem persists, contact Oracle Support Services.

CLSRSC-06005: failed to change owner of cluster root certificate to Windows LP user.

Cause: An attempt to change owner of root certificate to Windows LP user failed.

Action: Address the issues raised in the accompanying messages and rerun the root script. If the problem persists, contact Oracle Support Services.