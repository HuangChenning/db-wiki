---
title: "17.1 Exit codes of MySQL Enterprise Backup"
book: "MySQL Enterprise Backup User's Guide (Version 8.0.46)"
version: "8.0"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/8.0/en/meb-exitcodes.html"
tags:
  - mysql
  - mysql-8.0
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 8.0.46)

MySQL Enterprise Backup returns one of the following exit codes as it exits an operation. The meaning of each code is explained in Table 17.1, “MySQL Enterprise Backup Exit Codes and Messages” by its associated exit message.

**Table 17.1 MySQL Enterprise Backup Exit Codes and Messages**

| Exit Code | Exit Message |
| --- | --- |
| 0 | No error |
| 1 | Unknown Error |
| 2 | Internal Error |
| 3 | One of the required files is corrupt |
| 4 | One of the required files not found |
| 5 | Corrupt page or header encountered |
| 6 | Mismatch in config and the value obtained |
| 7 | Illegal Argument |
| 8 | One or more of the arguments are unknown |
| 9 | IO operation failed |
| 10 | Error allocating memory |
| 11 | Connection to server failed |
| 12 | Ongoing operation interrupted by user |
| 13 | User doesn't have sufficient privileges |
| 14 | No space left on device |
| 15 | Image version is not supported by this version of meb |
| 16 | The value is out of range |
| 17 | Innodb Error |
| 18 | Timedout while waiting for resource |
| 19 | Server returned error while executing sql |

The **mysqlbackup** command [`print-message`](backup-commands-other.md) takes an exit code supplied with the [`--error-code`](standard-options.md) option and returns the corresponding exit message in the `stdout` stream. Users can, for example, use a script to catch the exit code returned by **mysqlbackup**, and then pass it onto the [`print-message`](backup-commands-other.md) command to obtain an exit message. See the description for [`print-message`](backup-commands-other.md) for details.