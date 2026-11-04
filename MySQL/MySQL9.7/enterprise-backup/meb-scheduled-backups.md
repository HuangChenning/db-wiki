---
title: "4.3.8 Making Scheduled Backups"
book: "MySQL Enterprise Backup User's Guide (Version 9.7.0)"
version: "9.7"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/9.7/en/meb-scheduled-backups.html"
tags:
  - mysql
  - mysql-9.7
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 9.7.0)

### 4.3.8 Making Scheduled Backups

Maintaining a regular backup schedule is an important measure for preventing data loss for you MySQL server. This section discusses some simple means for setting up a schedule for running MySQL Enterprise Backup.

*For Linux and other Unix-like platforms:* you can set up a cron job on your system for scheduled backups. There are two types of cron jobs. To set up a user cron job, which is owned and run by a particular user, do the following:

- Log on as the user who runs MySQL Enterprise Backup and use the following command to invoke an editor for creating (or modifying) a crontab:
	```
	$> crontab -e
	```
- In the editor, add an entry similar to the following one to the crontab, and then save your changes (make sure contents in both lines below appear in a single line in the crontab):
	```
	@daily /path-to-mysqlbackup/mysqlbackup -uroot --backup-dir=/path-to-backup-folder/cronbackups 
	  --with-timestamp --backup-image=my.mib backup-to-image  &>/dev/null
	```
	This crontab entry invokes **mysqlbackup** to create a backup under the `cronbackups` directory at `00:00:00` everyday. Outputs from the `stderr` and `stdout` streams are redirected to /dev/null/, so they will not invoke other actions on the part of the Cron server (for example, email notifications to the user).

To set up a system cron job, which is owned and run by `root`, create a file under the `/etc/cron.d` folder and put into it a similar crontab entry as the one above, adding the user (`root` in the following example) before the **mysqlbackup** command:

```
@daily root /path-to-mysqlbackup/mysqlbackup -uroot --backup-=/path-to-backup-folder/cronbackups \
  --with-timestamp --backup-image=my.mib backup-to-image  &>/dev/null
```

Check your platform's documentation for further details on the different ways to set up cron jobs for various types of schedules.

*For Windows platforms:* Use the Task Scheduler for the purpose. Check the documentation for your Windows platform for instructions.