---
title: PRCA-01000 to PRCA-01056
book: Error Messages
doc_id: E17766-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e17766/prcamsg.htm
tags:
  - oracle
  - 11g
  - error-messages
---

## 80 PRCA-01000 to PRCA-01056

PRCA-01000: ASM Disk Group {0} does not exist

Cause: An attempt failed to retrieve an ASM disk group that was not configured.

Action: Create the diskgroup using sqlplus if the specified diskgroup does not exist. Mount the diskgroup in ASM which registers the diskgroup with CRS.

PRCA-01001: ASM Disk Group resource does not exist

Cause: There was no disk group resource registered with CRS.

Action: Create the diskgroup using sqlplus and mount the diskgroup in ASM which registers the diskgroup with CRS.

PRCA-01002: Failed to remove CRS resource {0} for ASM Disk Group {1}

Cause: An attempt to remove the CRS resource for the specified ASM Disk Group failed.

Action: Examine the accompanying error messages for details.

PRCA-01003: Failed to create ASM {0} resource {1}

Cause: An attempt to add the CRS resource for ASM failed.

Action: Ensure that the CRS stack is running, the user running srvctl add asm is also the owner of the CRS home, and examine the accompanying error message for details.

PRCA-01005: Failed to retrieve server parameter file of ASM {0}

Cause: Cannot retrieve ASM server parameter file.

Action: Retry the request after ensuring that the CRS stack is running, the ASM resource has been configured, and the user has read permission on the ASM resource.

PRCA-01006: Failed to update server parameter file {0} of ASM {1}

Cause: Unable to update the ASM server parameter file.

Action: Retry the request after ensuring that the CRS stack is running, the ASM resource has been configured, and the user has update permission on the ASM resource.

PRCA-01007: ASM {0} is not using initialization parameters: {1}

Cause: The specified ASM instance does not use the initialization parameters shown.

Action: Examine the accompanying error messages for details.

PRCA-01016: Failed to remove ASM resource {0} for ASM instance {1}

Cause: An attempt to remove the specified ASM configuration failed.

Action: Examine the accompanying error message for details.

PRCA-01017: ASM {0} does not exist

Cause: ASM is not configured yet.

Action: Configure ASM and then retry.

PRCA-01018: Failed to retrieve ASM instance list for ASM {0}

Cause: Failed to retrieve the list of ASM instances.

Action: Make sure that the crs stack is up and the ASM resource has been configured.

PRCA-01019: ASM {0} is not running

Cause: The ASM resource does not have any running instances.

Action: Use 'srvctl start asm' command to start the asm resource.

PRCA-01020: Unable to create ACFS file system resource {0} for the volume device {1}

Cause: The ACFS file system resource for the specified volume device path could not be created. Possible causes: 1) CRS stack was not available. 2) ASM instance was not running. 3) User was not running with an account with administrative access. (root, Administrator, etc) 4) Was unable to identify the mount point that the user requested the resource to use.

Action: 1) Verify that the CRS stack is available. ( 'crsctl check crs' ) 2) Verify that ASM is running. (srvctl status asm) 3) Verify that the user is running with administrative access. 4) Verify that the mount point given to the create resource command exists.

PRCA-01021: Unable to retrieve ACFS file system for the volume device {0}

Cause: The ACFS file system resource for the specified volume device path could not be retrieved. Possible causes: 1) CRS stack was not available. 2) ASM instance was not running. 3) User was not running with an account with administrative access. (root, Administrator, etc) 4) Was unable to identify the mount point that the user requested the resource to use.

Action: 1) Verify that the CRS stack is available. ( 'crsctl check crs' ) 2) Verify that ASM is running. (srvctl status asm) 3) Verify that the user is running with administrative access. 4) Verify that the mount point given to the create resource command exists.

PRCA-01022: ACFS file system resource already exists for disk group {0} and volume {1}

Cause: The ACFS file system resource had already been created for the specified disk group and volume names.

Action: 1) Supply a different volume device path to srvctl add filesystem to create a different ACFS file system resource. -or- 2) Delete the previous resource (' srvctl remove filesystem -d \<volume device> ') and re-run the command.

PRCA-01023: Unable to add ACFS file system resource {0} for disk group {1} and volume {2}

Cause: The ACFS file system resource for the specified volume device path could not be added. Possible causes: 1) CRS stack was not available. 2) ASM instance was not running. 3) User was not running with an account with administrative access. (root, Administrator, etc) 4) Was unable to identify the mount point that the user requested the resource to use.

Action: 1) Verify that the CRS stack is available. ( 'crsctl check crs' ) 2) Verify that ASM is running. ( 'srvctl status asm' ) 3) Verify that the user is running with administrative access. 4) Verify that the mount point given to the create resource command exists.

PRCA-01024: Unable to retrieve the volume for disk group {0} and volume {1}

Cause: The ACFS file system resource for the specified volume device path was unable to be retrieved. Possible causes: 1) CRS stack was not available. 2) ASM instance was not running. 3) User was not running with an account with administrative access. (root, Administrator, etc)

Action: 1) Verify that the CRS stack is available. ( 'crsctl check crs' ) 2) Verify that ASM is running. ( 'srvctl status asm' ) 3) Verify that the user is running with administrative access.

PRCA-01025: Unable to retrieve the mountpoint path for disk group {0} and volume {1}

Cause: The ACFS file system resource for the specified volume device path was unable to be retrieved. Possible causes: 1) CRS stack was not available. 2) ASM instance was not running. 3) User was not running with an account with administrative access. (root, Administrator, etc)

Action: 1) Verify that the CRS stack is available. ( 'crsctl check crs' ) 2) Verify that ASM is running. ( 'srvctl status asm' ) 3) Verify that the user is running with administrative access.

PRCA-01026: Unable to set the user of the ACFS file system for disk group {0} and volume {1}

Cause: The user of the ACFS file system resource for the specified disk group and volume was unable to be modified. Possible causes: 1) CRS stack was not available. 2) ASM instance was not running. 3) User was not running with an account with administrative access. (root, Administrator, etc)

Action: 1) Verify that the CRS stack is available. ( 'crsctl check crs' ) 2) Verify that ASM is running. ( 'srvctl status asm' ) 3) Verify that the user is running with administrative access.

PRCA-01027: Failed to remove ACFS file system configuration for disk group {0} and volume {1}

Cause: Cannot remove the ACFS file system configuration for the specified disk group and volume.

Action: 1) Verify that the CRS stack is available. ( 'crsctl check crs' ) 2) Verify that ASM is running. ( 'srvctl status asm' ) 3) Verify that the user is running with administrative access.

PRCA-01028: Failed to retrieve listener associated with ASM {0}

Cause: Failed to retrieve listener associated with ASM.

Action: Ensure that user has read permissions on ASM resource and then retry. Also, ensure that listener specified in ASM resource's start dependencies exists.

PRCA-01029: Failed to associate listener {0} with ASM {1}

Cause: Failed to associate given listener with ASM.

Action: Ensure that user has update permissions on ASM resource and then retry.

PRCA-01030: Failed to retrieve the diskgroup associated with the volume device {0}

Cause: Unable to retrieve the diskgroup associated with the given volume device using "asmcmd volinfo -g <volume\_name>" command.

Action: Make sure that the asm instance is running; the asmcmd utility exists and the underlying ofs devices are accessible.

PRCA-01031: Unable to retrieve the diskgroup {0} associated with the volume device {1}

Cause: The ACFS file system resource for the specified volume device path was unable to be retrieved. Possible causes: 1) CRS stack was not available. 2) ASM instance was not running. 3) User was not running with an account with administrative access. (root, Administrator, etc) 4) Disk group is not mounted.

Action: 1) Verify that the CRS stack is available. ( 'crsctl check crs' ) 2) Verify that ASM is running. ( 'srvctl status asm' ) 3) Verify that the user is running with administrative access. 4) Verify that the disk group is mounted.

PRCA-01032: ASM listener {0} does not exist

Cause: ASM listener is not registered with Oracle Clusterware.

Action: Run 'srvctl add listener -l <lsnr\_name>' command with <lsnr\_name> as in above error message, or if there is another listener registered with Oracle clusterware, then try 'srvctl modify asm -l <lsnr\_name>'

PRCA-01033: ACFS file system resource does not exist for volume device {0}

Cause: The ACFS file system resource with the specified volume device was not registered with the Oracle Clusterware.

Action: Use 'srvctl add filesystem' command to create an ACFS file system resource.

PRCA-01034: ACFS file system resource does not exist in Oracle Clusterware

Cause: No ACFS file system resource was registered with the Oracle clusterware.

Action: Use 'srvctl add filesystem' command to create an ACFS file system resource.

PRCA-01035: Unable to determine the databases that use the disk group {0}

Cause: Unable to retrieve databases that have dependencies on the disk group.

Action: Make sure that the crs stack is up; the user has read permissions on database CRS resources and then retry.

PRCA-01036: An Oracle Restart environment-specific API was invoked in an Oracle Clusterware environment.

Cause: Internal error.

Action: Contact Oracle Support Services.

PRCA-01037: Failed to retrieve the diskgroup discovery string of ASM {0}

Cause: An attempt to retrieve the diskgroup discovery string for ASM failed.

Action: Retry the request after ensuring that the CRS stack is running, the ASM resource has been configured, and the user has read permission on ASM resource.

PRCA-01038: Failed to update the diskgroup discovery string {0} of ASM {1}

Cause: An attempt to update the diskgroup discovery string for ASM failed.

Action: Retry the request after ensuring that the CRS stack is running, the ASM resource has been configured, and the user has update permission on ASM resource.

PRCA-01039: Volume device {0} does not exist

Cause: The supplied volume device does not exist.

Action: Use asmca to create the volume device and then run 'srvctl add filesystem' command again.

PRCA-01040: Failed to check the existence of volume device {0}

Cause: Failed to execute acfsutil command to check for the existence of the supplied volume device.

Action: Review the underlying error messages that provide the details of why acfsutil execution failed. Resolve the reported problem and retry the command.

PRCA-01041: Failed to validate disk group {0} of volume device {1}

Cause: Failed to execute acfsutil command to validate the disk group of the volume device.

Action: Review the underlying error messages that provide the details of why acfsutil execution failed. Resolve the reported problem and retry 'srvctl add filesystem' command.

PRCA-01042: Diskgroup {0} is not valid for volume device {1}

Cause: The supplied diskgroup does not match the underlying diskgroup created for the supplied volume device.

Action: Execute 'srvctl add filesystem' command with the correct disk group value.

PRCA-01043: Failed to validate volume {0} of volume device {1}

Cause: Failed to execute acfsutil command to validate the volume of the volume device.

Action: Review the underlying error messages that provide the details of why acfsutil execution failed. Resolve the reported problem and retry 'srvctl add filesystem' command.

PRCA-01044: Volume {0} is not valid for volume device {1}

Cause: The supplied volume does not match the underlying volume created for the supplied volume device.

Action: Execute 'srvctl add filesystem' command with the correct volume value.

PRCA-01045: ACFS is not supported on this platform

Cause: A filesystem operation was requested on an unsupported platform.

Action: Run srvctl filesystem command on a supported platform.

PRCA-01046: File system for volume device {0} exists in the ACFS registry

Cause: File system for the specified volume device was registered in the ACFS registry. File system can either be in the ACFS registry or registered as a CRS resource, but not both.

Action: Either run 'acfsutil registry -d' to delete the volume device from the ACFS registry or run 'srvctl add filesystem' with a different volume device.

PRCA-01047: Unable to find ACFS file system resource for volume device {0} because of inability to get the canonical form of the volume device

Cause: An internally-issued 'advmutil canonical' command failed and the volume device recorded in the ACFS file system resource did not match the specified volume device.

Action: Review the underlying error messages that provide the details of why advmutil execution failed. Resolve the reported problem and retry.

PRCA-01048: The user "{0}" could not be found on the cluster

Cause: The user specified as the file system owner/user could not be found.

Action: Enter the name of an existing user or the owner of the specified file system.

PRCA-01049: Invalid mount point path {0} because specified mount point path was a remote path

Cause: The specified mount point path was a remote path.

Action: Make sure that the mount point path was not a remote path.

PRCA-01050: Unable to retrieve the canonical form of the volume device for disk group {0} and volume {1}

Cause: The ACFS file system resource for the specified canonical form of the volume device path was not retrieved.

Action: 1) Make sure that the CRS stack is available. ( 'crsctl check crs' ) 2) Review the accompanying error messages for details about the failure. Retry after resolving those issues.

PRCA-01056: Unable to upgrade ACFS from version {0} to version {1}

Cause: Failed to upgrade ACFS from one version to another version.

Action: Review the accompanying error messages for details about the failure. Retry after resolving those issues.