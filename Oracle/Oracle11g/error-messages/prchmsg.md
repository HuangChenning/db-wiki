---
title: PRCH-01000 to PRCH-01060
book: Error Messages
doc_id: E17766-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e17766/prchmsg.htm
tags:
  - oracle
  - 11g
  - error-messages
---

## 83 PRCH-01000 to PRCH-01060

PRCH-01000: Failed to stop resources running from Oracle home {0}

Cause: Attempt to stop one or more resources in the specified Oracle home failed.

Action: for the individual resource stop failure and perform the steps for each resource that failed to stop.

PRCH-01001: Failed to start resources in Oracle home {0}

Cause: Attempt to start one or more resources in the specified Oracle home failed.

Action: for the individual resource start failure and perform the steps for each resource that failed to start.

PRCH-01002: Failed to stop resources running from CRS home {0}

Cause: Attempt to stop one or more resources in the specified CRS home failed.

Action: for the individual resource stop failure and perform the steps for each resource that failed to stop.

PRCH-01003: Failed to start resources in CRS home {0}

Cause: Attempt to start one or more resources in the specified CRS home failed.

Action: for the individual resource start failure and perform the steps for each resource that failed to start.

PRCH-01004: Failed to stop service

Cause: Attempt to stop a Service resource in the specified oracle home failed.

Action: Review the error messages for possible reasons and if needed, use 'srvctl stop service -d <db\_unique\_name>' to stop the service.

PRCH-01005: Failed to stop database

Cause: Attempt to stop the database resource in the specified oracle home failed.

Action: Review the error messages for possible reasons, correct the error and use 'srvctl stop database -d <db\_unique\_name>' to stop the database.

PRCH-01006: Failed to stop Listener

Cause: Attempt to stop the Listener resource in the specified oracle home failed.

Action: Review the error messages for possible reasons, correct the error and use 'srvctl stop listener' to stop the Listener.

PRCH-01007: Failed to stop Listener

Cause: Attempt to stop the Listener resource in CRS home failed.

Action: Review the error messages for possible reasons, correct the error and use 'srvctl stop listener' to stop the Listener.

PRCH-01008: Failed to start service

Cause: Attempt to start a Service resource in the specified oracle home failed.

Action: Review the error messages for possible reasons, correct the error and use 'srvctl start service -d <db\_unique\_name>' to start the service.

PRCH-01009: Failed to start database

Cause: Attempt to start the database resource in the specified oracle home failed.

Action: Review the error messages for possible reasons, correct the error and use 'srvctl start database -d <db\_unique\_name>' to start the database.

PRCH-01010: Failed to start Listener

Cause: Attempt to start the Listener resource in the specified Oracle home failed.

Action: Review the error messages for possible reasons, correct the error and use 'srvctl start listener' to start the Listener.

PRCH-01011: Failed to start Listener

Cause: Attempt to start the Listener resource in the specified CRS home failed.

Action: Review the error messages for possible reasons, correct the error and use 'srvctl start listener' to start the Listener.

PRCH-01012: Failed to stop EONS

Cause: Attempt to stop the EONS resource in the specified CRS home failed.

Action: Review the error messages for possible reasons, correct the error and use 'srvctl stop nodeapps' to stop the EONS resource.

PRCH-01013: Failed to start EONS

Cause: Attempt to start the EONS resource in the specified CRS home failed.

Action: Review the error messages for possible reasons, correct the error and use 'srvctl start nodeapps' to start the EONS resource.

PRCH-01014: Failed to stop ONS

Cause: Attempt to stop the ONS resource in the specified CRS home failed.

Action: Review the error messages for possible reasons, correct the error and use 'srvctl stop nodeapps' to stop the ONS resource.

PRCH-01015: Failed to start ONS

Cause: Attempt to start the ONS resource in the specified CRS home failed.

Action: Review the error messages for possible reasons, correct the error and use 'srvctl start nodeapps' to start the ONS resource.

PRCH-01016: Failed to stop GSD resource

Cause: Attempt to stop the GSD resource in the specified CRS home failed.

Action: Review the error messages for possible reasons, correct the error and use 'srvctl stop nodeapps' to stop the GSD resource.

PRCH-01017: Failed to start GSD resource

Cause: Attempt to start the GSD resource in the specified CRS home failed.

Action: Review the error messages for possible reasons, correct the error and use 'srvctl start nodeapps' to start the GSD resource.

PRCH-01018: Failed to stop VIP resource

Cause: Attempt to stop the VIP resource in the specified CRS home failed.

Action: Review the error messages for possible reasons, correct the error and use 'srvctl stop vip -n <node\_name>' to stop the VIP resource.

PRCH-01019: Failed to start VIP resource

Cause: Attempt to start the VIP resource in the specified CRS home failed.

Action: Review the error messages for possible reasons, correct the error and use 'srvctl start vip -n <node\_name>' to start the VIP resource.

PRCH-01020: Failed to stop Network resource

Cause: Attempt to stop the Network resource in the specified CRS home failed.

Action: Review the error messages for possible reasons, correct the error and use 'srvctl stop nodeapps' to stop the Network resource.

PRCH-01021: Failed to start Network resource

Cause: Attempt to start the Network resource in the specified CRS home failed.

Action: Review the error messages for possible reasons, correct the error and use 'srvctl start nodeapps' to start the Network resource.

PRCH-01022: Failed to stop SCAN VIP resource

Cause: Attempt to stop the SCAN VIP resource in the specified CRS home failed.

Action: Review the error messages for possible reasons, correct the error and use 'srvctl stop scan' to stop the SCAN VIP resource.

PRCH-01023: Failed to start SCAN VIP resource

Cause: Attempt to start the SCAN VIP resource in the specified CRS home failed.

Action: Review the error messages for possible reasons, correct the error and use 'srvctl start scan' to start the SCAN VIP resource.

PRCH-01024: Failed to stop SCAN Listener resource

Cause: Attempt to stop the SCAN Listener resource in the specified CRS home failed.

Action: Review the error messages for possible reasons, correct the error and use 'srvctl stop scan\_listener' to stop the SCAN Listener resource.

PRCH-01025: Failed to start SCAN Listener

Cause: Attempt to start the SCAN Listener resource in the specified CRS home failed.

Action: Review the error messages for possible reasons, correct the error and use 'srvctl start scan\_listener' to start the SCAN Listener resource.

PRCH-01026: Failed to stop ASM

Cause: Attempt to stop the ASM resource in the specified CRS home failed.

Action: Review the error messages for possible reasons, correct the error and use 'srvctl stop asm' to stop the ASM resource.

PRCH-01027: Failed to start ASM

Cause: Attempt to start the ASM resource in the specified CRS home failed.

Action: Review the accompanying error messages for possible reasons, correct the error and use 'srvctl start asm' to start the ASM resource.

PRCH-01028: One or more resources failed to start: {0}

Cause: Attempt to start one or more resources in the specified oracle home failed.

Action: for the individual resource start failure and perform the steps for each resource that failed to start.

PRCH-01029: One or more resources failed to stop: {0}

Cause: Attempt to stop one or more resources in the specified oracle home failed.

Action: for the individual resource stop failure and perform the steps for each resource that failed to stop.

PRCH-01030: One or more resources failed to stop: {0}

Cause: An attempt to stop one or more resources in the specified CRS home failed.

Action: Review the accompanying resource error messages and their documentation, and correct the problems indicated.

PRCH-01031: One or more resources failed to start: {0}

Cause: Attempt to start one or more resources in the specified CRS home failed.

Action: for the individual resource start failure and perform the steps for each resource that failed to start.

PRCH-01032: Failed to stop GNS resource

Cause: Attempt to stop the GNS resource in the specified CRS home failed.

Action: Review the error messages for possible reasons, correct the error and use 'srvctl stop gns' to stop the GNS resource.

PRCH-01033: Failed to start GNS resource

Cause: Attempt to start the GNS resource in the specified CRS home failed.

Action: Review the error messages for possible reasons, correct the error and use 'srvctl start gns' to start the GNS resource.

PRCH-01034: Failed to stop diskgroup resource

Cause: Attempt to stop the diskgroup resource in the specified home failed.

Action: Review the accompanying error messages for possible reasons, correct the error and use 'srvctl stop diskgroup -g <dg\_name>' to stop the diskgroup resource.

PRCH-01035: Failed to start diskgroup resource

Cause: Attempt to start the diskgroup resource in the specified home failed.

Action: Review the accompanying error messages for possible reasons, correct the error and use 'srvctl start diskgroup -g <dg\_name>' to start the diskgroup resource.

PRCH-01036: The state file "{0}" does not exist

Cause: The state file required for the current operation was not found.

Action: Make sure the named file exists in the file system.

PRCH-01037: The filesystem object "{0}" is not a file

Cause: The content that was expected to be a file which turned out not to be a file.

Action: Retry the 'srvctl stop home' to generate this file. If the problem still exists, contact Oracle Support Services.

PRCH-01038: "{0}" is a non-readable file

Cause: The user does not have read permissions to open the file.

Action: Modify the file permissions so that the file becomes readable or execute the command from an OS userid with the required privileges.

PRCH-01039: Failed to stop CVU resource

Cause: Attempt to stop the CVU resource failed.

Action: Review the accompanying error messages for possible reasons, correct the error and use 'srvctl stop cvu' to stop the CVU resource.

PRCH-01040: Failed to start CVU resource

Cause: Attempt to start the CVU resource failed.

Action: Review the accompanying error messages for possible reasons, correct the error and use 'srvctl start cvu' to start the CVU resource.

PRCH-01041: Failed while checking status of service "{0}"

Cause: Attempt to check the status of the listed service failed.

Action: Review the accompanying error messages for possible reasons, correct the error and retry.

PRCH-01042: Failed while checking status of database "{0}"

Cause: Attempt to check the status of the listed database failed.

Action: Review the accompanying error messages for possible reasons, correct the error and retry.

PRCH-01043: Failed while checking status of database instance "{0}"

Cause: Attempt to check the status of the listed database instance failed.

Action: Review the accompanying error messages for possible reasons, correct the error and retry.

PRCH-01044: Failed while checking status of listener "{0}"

Cause: Attempt to check the status of the listed listener failed.

Action: Review the accompanying error messages for possible reasons, correct the error and retry.

PRCH-01045: Failed while checking status of VIP "{0}"

Cause: Attempt to check the status of the listed VIP failed.

Action: Review the accompanying error messages for possible reasons, correct the error and retry.

PRCH-01046: Failed while checking status of SCAN VIP "{0}"

Cause: Attempt to check the status of the listed SCAN VIP failed.

Action: Review the accompanying error messages for possible reasons, correct the error and retry.

PRCH-01047: Failed while checking status of SCAN Listener "{0}"

Cause: Attempt to check the status of the listed SCAN Listener failed.

Action: Review the accompanying error messages for possible reasons, correct the error and retry.

PRCH-01048: Failed while checking status of CVU resource "{0}"

Cause: Attempt to check the status of the listed CVU resource failed.

Action: Review the accompanying error messages for possible reasons, correct the error and retry.

PRCH-01049: Failed while checking status of disk group "{0}"

Cause: Attempt to check the status of the listed disk group failed.

Action: Review the accompanying error messages for possible reasons, correct the error and retry.

PRCH-01050: Failed while checking status of ASM "{0}"

Cause: Attempt to check the status of the listed ASM failed.

Action: Review the accompanying error messages for possible reasons, correct the error and retry.

PRCH-01051: Failed while checking status of GNS "{0}"

Cause: Attempt to check the status of the listed GNS failed.

Action: Review the accompanying error messages for possible reasons, correct the error and retry.

PRCH-01052: Failed while checking status of GSD "{0}"

Cause: Attempt to check the status of the listed GSD failed.

Action: Review the accompanying error messages for possible reasons, correct the error and retry.

PRCH-01053: Failed while checking status of Network "{0}"

Cause: Attempt to check the status of the listed Network failed.

Action: Review the accompanying error messages for possible reasons, correct the error and retry.

PRCH-01054: Failed while checking status of ONS "{0}"

Cause: Attempt to check the status of the listed ONS failed.

Action: Review the accompanying error messages for possible reasons, correct the error and retry.

PRCH-01055: Failed to create or open file "{0}"

Cause: State file processing failed because: the file specified is a directory rather than a file, the file did not exist but could not be created, or the file exists but could not be opened.

Action: Enable state file processing by: not specifying a directory name, ensuring the the directory is writable, or ensuring that an existing state file can be overwritten.

PRCH-01056: Failed to write to file "{0}"

Cause: Attempt to write to the given file failed.

Action: If the state file already exists, then make sure that it is writable. Otherwise, make sure that parent directory of the state file path is writable.

PRCH-01057: The Clusterware resource for database "{0}" does not exist.

Cause: The Clusterware resource for the database with the given name did not exist.

Action: Make sure that Clusterware resource for the database with the given name exists.

PRCH-01058: Failed while checking status of CRS home {0}

Cause: Attempt to check the status of the CRS home failed.

Action: Review the accompanying error messages for possible reasons, correct the error and retry.

PRCH-01059: Failed while checking status of Oracle home {0}

Cause: Attempt to check the status of the Oracle home failed.

Action: Review the accompanying error messages for possible reasons, correct the error and retry.

PRCH-01060: Status check for one or more resources failed: {0}

Cause: Attempt to check the status for one or more resources in the specified Oracle home failed.

Action: Review the underlying error messages that provides the details of which resources failed to query their status, check the cause and action for the individual resource start failure and perform the steps for each resource that failed to start.