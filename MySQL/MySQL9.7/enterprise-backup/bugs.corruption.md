---
title: "17.2 Working Around Corruption Problems"
book: "MySQL Enterprise Backup User's Guide (Version 9.7.0)"
version: "9.7"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/9.7/en/bugs.corruption.html"
tags:
  - mysql
  - mysql-9.7
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 9.7.0)

Sometimes the operating system or the hardware can corrupt a data file page at a location that does not cause a database error, but prevents **mysqlbackup** from completing:

```
170225 10:46:18 PCR1    INFO: Re-reading page at offset 0 in D:/temp/5.7_source/test/emp2.ibd
170225 10:46:18 PCR1    INFO: Re-reading page at offset 0 in D:/temp/5.7_source/test/emp2.ibd
...
170225 10:46:26 PCR1 ERROR: Page at offset 0 in D:/temp/5.7_source/test/emp2.ibd seems corrupt!
```

A corruption problem can have different causes. Here are some suggestions for dealing with it:

- The problem can occur if the MySQL server is too busy. Before trying other solutions, you might want to perform the backup again using some non-default settings for the following **mysqlbackup** options:
	- [`--page-reread-time`](backup-capacity-options.md) = *`MS`*. Try set the value to, for example, “0.05”, for faster rereads during checksum failures.
	- [`--page-reread-count`](backup-capacity-options.md) = *`retry_limit`*. Try set the value to, for example, “1000”, to allow more rereads during checksum failures before MySQL Enterprise Backup gives up and throws an error.
- Scrambled data in memory can cause the problem even though the data on disk is actually uncorrupted. Reboot the database server and the storage device to see if the problem persists.
- If the problem persists after the database server and the storage device have been restarted, you might really have a corruption on your disk. You might consider restoring data from an earlier backup and "roll forward" the recent changes to bring the database server back to its current state.
- If you want to make MySQL Enterprise Backup finish a backup anyway before you go and investigate the root cause of the issue, you can rewrite the checksum values on the disk by running the [innochecksum](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/innochecksum.html) utility on the server:
	```
	innochecksum --no-checksum --write=crc32
	```
	The option `--no-checksum` disable the verification function of the tool, and the option `             --write=crc32` makes [innochecksum](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/innochecksum.html) rewrite the checksum values on the disk.

**IMPORTANT:** Do not treat corruption problems as a minor annoyance. Find out what is wrong with the system that causes the corruption—however, such troubleshooting is beyond the scope of this manual.