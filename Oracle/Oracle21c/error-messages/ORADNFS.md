---
title: Database Error Messages
book: Database Error Messages
doc_id: F30283-07
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/errmg/ORADNFS.html
tags:
  - oracle
  - 21c
  - error-messages
---

ORADNFS-65000: Permission denied. You are not a member of ORA\_DBA group.

Cause: The ORADNFS utility was invoked by a user who was not in the ORA\_DBA group.

Action: Add user of this utility to ORA\_DBA group and retry, or log on as a different user (who is in the ORA\_DBA group) and retry.

ORADNFS-65001: Currently this option is supported only on Windows.

Cause: The ORADNFS command was issued on an operating system other than Windows.

Action: Run this command only on Windows.

ORADNFS-65002: NFS initialization failed, error code: number.

Cause: NFS initialization failed. error code is zero if successful, a negative error code if a software bug is encountered, or a positive error code if a hardware or user error is encountered. NEGATIVE ERROR EXAMPLES: - An impossible instance id. - context not initialized to zero. POSITIVE ERROR EXAMPLES: - Execution thread does not have privilege needed to access ODM. - Insufficient memory to allocate context

Action: Review the system configuration and correct the relevant issue.

ORADNFS-65003: failed to query user's local groups in the system, error code: number

Cause: failed to query user's local groups in the system Error code Description- 0005: The user does not have access rights to the requested information. This error is also returned if the servername parameter has a trailing blank. 0124: The system call level is not correct. This error is returned if the level parameter was not specified as 0. 0087: A parameter is incorrect. This error is returned if the flags parameter contains a value other than LG\_INCLUDE\_INDIRECT. 0234: More entries are available. Specify a large enough buffer to receive all entries. 0008: Insufficient memory was available to complete the operation. 2453: The domain controller could not be found. 2221: The user could not be found. This error is returned if the username could not be found. 1722: The RPC server is unavailable. This error is returned if the servername parameter could not be found. access denied, not enough memory, no dc controller or many more

Action: Review the system configuration and correct the relevant issue.

ORADNFS-65004: NFS registration failed, error code: number.

Cause: NFS registration failed, error code - 4 in case of error

Action: Review the system configuration and correct the relevant issue.

ORADNFS-65005: Invalid value for parameter string.

Cause: Invalid input value entered for SEEK or SKIP.

Action: Enter only numeric values.

ORADNFS-65006: Invalid use. Refer to Help for valid use.

Cause: Invalid usage of command, either some argument may be missing or some invalid value might be entered for an input flag.

Action: Check the usage in help and pass correct arguments.

ORADNFS-65007: No oranfsodm19.dll in ORACLE\_HOME\\rdbms\\lib\\odm

Cause: oranfsodm19.dll missing in ORACLE\_HOME\\rdbms\\lib\\odm

Action: Run ORADNFS DNFSENABLE command to copy the DLL.

ORADNFS-65008: No oranfstab in ORACLE\_HOME\\dbs, file: string.

Cause: oranfstab file missing in ORACLE\_HOME\\dbs

Action: Run ORADNFS DNFSENABLE & ORADNFS MOUNT to create oranfstab.

ORADNFS-65009: DNFS is enabled.

Cause: DNFS is in enabled status for given ORACLE\_HOME 1.oranfstab file present in ORACLE\_HOME\\dbs 2.oranfsodm19.dll present in ORACLE\_HOME\\rdbms\\lib\\odm 3.size of oranfstab is non zero

Action: None

ORADNFS-65010: DNFS is not enabled.

Cause: DNFS is not in enabled status for given ORACLE\_HOME

Action: Confirm that - 1.oranfstab file present in ORACLE\_HOME\\dbs 2.oranfsodm19.dll present in ORACLE\_HOME\\rdbms\\lib\\odm 3.size of oranfstab is non zero

ORADNFS-65011: No entries found in oranfstab.

Cause: size of oranfstab is zero

Action: Use the ORADNFS MOUNT command to add appropriate entries to the oranfstab file.

ORADNFS-65012: failed to discover NFS path. error code: number

Cause: failed to discover NFS path, error code- 1 no common version found 2 file system not installed 3 permission to access ODM denied 4 some other error occurred

Action: Review the system configuration and correct the relevant issue.

ORADNFS-65013: failed to get statistics of file string on local file system

Cause: failed to get statistics of file on local file system

Action: Ensure that you have read access to the file and retry.

ORADNFS-65014: Filer string may not be defined in this system.

Cause: Filer may not be defined in this system

Action: None

ORADNFS-65015: failed to set attributes of file string on local file system

Cause: failed to change attributes of file on local file system

Action: Ensure that you have required access to change parameters of file and retry.

ORADNFS-65016: source file not specified

Cause: source file not specified in command line arguments

Action: Specify source file in command line and retry.

ORADNFS-65017: destination file not specified

Cause: destination file not specified in command line arguments

Action: Specify destination file in command line and retry.

ORADNFS-65018: warning: file string already exists

Cause: It's a warning message to user saying that destination already exists.

Action: None

ORADNFS-65019: No value specified for option -IF

Cause: Input filename not specified.

Action: Specify input filename and retry.

ORADNFS-65020: Invalid value:number entered for IBS.

Cause: Invalid value entered for IBS.

Action: Value of IBS must be less than COUNT,enter a valid value and retry.

ORADNFS-65021: Invalid value: number entered for SKIP parameter.

Cause: Invalid value entered for SKIP parameter.

Action: Enter a valid value for SKIP parameter and retry. Value of SKIP should be less than file size.

ORADNFS-65022: Operation failed.

Cause: this is a generic message which tells that the given command failed

Action: Examine the preceding error messages to determine the problem.

ORADNFS-65023: Operation completed successfully.

Cause: this is a generic message which tells that the given command succeeded

Action: None

ORADNFS-65024: invalid ORADNFS command verb

Cause: An unrecognized command verb or option was specified.

Action: Issue 'oradnfs' for information on command verbs.

ORADNFS-65025: Error in seeking file: string

Cause: Error in seeking file

Action: None

ORADNFS-65026: Could not open log file: string errno: number.

Cause: failed to open log file to write traces

Action: Ensure that a writable file system path is provided.

ORADNFS-65027: NFS I/O completion failed, errno: number

Cause: NFS I/O completion failed 2 timeout 4 waitlist complete 8 completion list full 16 no more active I/O

Action: Review the system configuration and correct the relevant issue.

ORADNFS-65028: Not a directory: string.

Cause: given file is not a directory

Action: None

ORADNFS-65029: NFS file creation failed. file: string error code: number.

Cause: NFS file creation failed error code is zero if successful, a negative error code if a software bug is encountered, or a positive error code if a hardware or user error is encountered.

Action: Review the system configuration and correct the relevant issue.

ORADNFS-65030: NFS file deletion failed, file: string error code: number.

Cause: NFS file deletion failed, error code- 1 file is not an ODM file 2 file is identified so it is still in use 3 file has already been deleted

Action: Review the system configuration and correct the relevant issue.

ORADNFS-65031: failed to read directory: string

Cause: failed to read directory

Action: review the system configuration and retry

ORADNFS-65032: failed to open directory on local file system: string

Cause: failed to open directory on local file system

Action: Ensure that you have read access to path provided and retry.

ORADNFS-65033: no value specified for option -OF

Cause: Output filename not specified.

Action: specify output filename and retry

ORADNFS-65034: failed to remove directory on local file system: string

Cause: failed to remove directory on local file system

Action: Review the system configuration and correct the relevant issue.

ORADNFS-65035: failed to re-identify NFS file: error code: number

Cause: failed to re-identify NFS file error code is zero if successful, a negative error code if a software bug is encountered, or a positive error code if a hardware or user error is encountered.

Action: Review the system configuration and correct the relevant issue.

ORADNFS-65036: failed to identify NFS file: string error code: number

Cause: failed to identify NFS file, error code- 1 successfully identified the file 2 cannot be identified by ODM 3 no file exists with this path name

Action: Review the system configuration and correct the relevant issue.

ORADNFS-65037: ORACLE\_HOME not defined in environment

Cause: ORACLE\_HOME not defined in environment

Action: Define ORACLE\_HOME in environment and retry.

ORADNFS-65038: failed to delete file on local file system: string.

Cause: failed to delete file on local file system

Action: Ensure that you have write access to the path provided and retry.

ORADNFS-65039: missing required value for parameter string

Cause: value missing for -BS, -IBS, -OBS, -COUNT, -SEEK or -SKIP parameter BS means block size, it specifies the size of read and write I/O IBS means input block size, it specifies the size of read I/O OBS means output block size, it specifies the size of write I/O SEEK specifies the offset of destination file from where we should start writing SKIP specifies the offset from start of source file from where we should begin reading the file

Action: Specify the missing value of paramter and retry.

ORADNFS-65040: failed to get fully qualified user name

Cause: failed to get fully qualified user name for current user 0234: The lpNameBuffer buffer is too small. The lpnSize parameter contains the number of bytes required to receive the name. 1355: The domain controller is not available to perform the lookup 1332: The user name is not available in the specified format.

Action: Review the system configuration and correct the relevant issue.

ORADNFS-65041: no value specified for option -P (parallel)

Cause: value missing for -P command line argument -p specifies the degree of parallelism done

Action: specify whether to use parallel I/O or not

ORADNFS-65042: failed to read nfs link, file: string error code: number

Cause: failed to read nfs link,error code- 1 symbolic link is not an ODM file 2 server error 3 symbolic link does not exist

Action: Review the system configuration and correct the relevant issue.

ORADNFS-65043: failed to read NFS directory, error code: number

Cause: failed to read NFS directory, error code- 1 directory is not an ODM file 2 server error 3 directory does not exist

Action: Review the system configuration and correct the relevant issue.

ORADNFS-65044: invalid trace level for component string

Cause: invalid trace level entered for kgodm, kgnfs, skgnfs or oradnfs

Action: Enter a value between 0-4 and retry

ORADNFS-65045: failed to resize NFS file: error code: number

Cause: failed to resize NFS file. error code is zero if successful, a negative error code if a software bug is encountered, or a positive error code if a hardware or user error is encountered.

Action: Review the system configuration and correct the relevant issue.

ORADNFS-65046: failed to commit NFS file. error code: number

Cause: failed to Commit NFS file error code is zero if successful, a negative error code if a software bug is encountered, or a positive error code if a hardware or user error is encountered.

Action: None

ORADNFS-65047: invalid size suffix multiplier

Cause: Invalid unit size entered for BS, IBS or OBS

Action: unit size must be one of w, B, k, KB, M, MB, G or GB. w - BS\* 2 b,B - BS\* 512 KB,kb - BS\* 1000 K,k - BS\* 1024 MB, mb - BS\* 1000\*1000 M,m - BS\* 1024\*1024 GB, gb - BS\* 1000\*1000\*1000 G,g - BS\* 1024\*1024\*1024 Eg: -BS 1M means 1\*1024\*1024 bytes is the block size for read and write I/O

ORADNFS-65048: failed to get statistics of NFS file, file: string error code: number

Cause: failed to get statistics of NFS file,error code- 1 file is not an ODM file 2 server error 3 file does not exist

Action: Review the system configuration and correct the relevant issue.

ORADNFS-65049: File string does not exist on local file system.

Cause: File does not exist on local file system.

Action: None

ORADNFS-65050: failed to un-identify NFS file: string error code: number

Cause: failed to un-identify NFS file error code is zero if successful, a negative error code if a software bug is encountered, or a positive error code if a hardware or user error is encountered.

Action: Review the system configuration and correct the relevant issue.

ORADNFS-65059: error during validation of file specification string

Cause: Checks if input filename is of valid format or not. For example, if user is running the utility in Windows and if he gives Linux style '/' in file path, it will be converted to Windows style '' and processesed. In this case it will be considered positive validation and no error is returned. Likewise there are negative cases as well where error will be returned saying that validation failed

Action: Ensure that input filename is of valid format.

ORADNFS-65060: Failed to allocate requested amount of memory: number bytes.

Cause: Failed to allocate required memory.

Action: None

ORADNFS-65061: failed to open file string on local file system

Cause: failed to open file on local file system

Action: Ensure that you have write access to the path specified and retry.

ORADNFS-65062: failed to make directory on local file system, file: string errno: number.

Cause: failed to make directory on local file system

Action: Ensure that you have write access to the path specified and retry.

ORADNFS-65063: failed to make NFS directory: string errno:number

Cause: failed to make NFS directory,error code- 1 directory is not an ODM dir 2 server error 3 directory already exists

Action: Review the system configuration and correct the relevant issue.

ORADNFS-65064: failed to copy oranfsodm19.dll to $OH\\rdbms\\lib\\odm

Cause: failed to copy oranfsodm19.dll to $OH\\rdbms\\lib\\odm

Action: Ensure that we have write access to $OH\\rdbms\\lib\\odm.

ORADNFS-65065: failed to reap NFS I/O, errno: number

Cause: failed to reap NFS I/O 2 timeout 4 waitlist complete 8 completion list full 16 no more active I/O

Action: Review the system configuration and correct the relevant issue.

ORADNFS-65066: failed to get information of NFS file, file: string errno: number

Cause: failed to get information of NFS file,errno- 1 file is not an ODM file 2 server error 3 file does not exist

Action: Review the system configuration and correct the relevant issue.

ORADNFS-65067: failed to get attributes of NFS file: string errno: number

Cause: failed to get attributes of NFS file, errno- 1 file is not an ODM file 2 server error 3 nonexistant or stale file handle

Action: Review the system configuration and correct the relevant issue.

ORADNFS-65068: failed to set attributes of NFS file: string errno: number

Cause: failed to set attributes of NFS file, errno - 1 file is not an ODM file 2 file server error 3 nonexistant or stale file handle

Action: Review the system configuration and correct the relevant issue.

ORADNFS-65069: failed to remove NFS directory, file: string errno: number

Cause: failed to remove NFS directory, errno - 1 directory is not an ODM file 2 server error 3 directory has already been deleted 4 directory is still in use

Action: Review the system configuration and correct the relevant issue.

ORADNFS-65070: failed to submit NFS I/O, errno: number

Cause: failed to submit NFS I/O, errno - 2 timeout 4 waitlist complete 8 completion list full 16 no more active I/O

Action: Review the system configuration and correct the relevant issue.

ORADNFS-65071: Input path is DNFS enabled.

Cause: The NFS mount listed in oranfstab was a part of or matched the input path.

Action: None

ORADNFS-65072: Input path is not DNFS enabled.

Cause: The NFS mount listed in oranfstab was not a part of or did not match the input path.

Action: Ensure that the input path is specified in the mount location present in the oranfstab file.