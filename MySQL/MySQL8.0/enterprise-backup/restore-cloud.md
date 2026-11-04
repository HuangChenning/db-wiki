---
title: "5.2 Restoring a Backup from Cloud Storage to a MySQL Server"
book: "MySQL Enterprise Backup User's Guide (Version 8.0.46)"
version: "8.0"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/8.0/en/restore-cloud.html"
tags:
  - mysql
  - mysql-8.0
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 8.0.46)

To restore a backup image from cloud storage to *`datadir`* on the server, use the [cloud storage options](backup-cloud-options.md), and also the [`--backup-dir`](backup-repository-options.md) option to specify the temporary directory into which temporary output, status files, and backup metadata will be saved:

**Example 5.13 Restoring a Single-file Backup from an Oracle Cloud Infrastructure (OCI) Object Storage to a MySQL Server**

```
mysqlbackup --defaults-file=<my.cnf> --backup-dir=/home/user/dbadmin/backuptmp \
  --datadir=<server_datadir> --with-timestamp --backup-image=-  --cloud-service=OCI \ 
  --cloud-par-url=<backup_PAR_URL> copy-back-and-apply-log
```

**Example 5.14 Restoring a Cloud Incremental Backup from an Oracle Cloud Infrastructure (OCI) Object Storage to a MySQL Server**

```
mysqlbackup --defaults-file=<my.cnf> --backup-dir=/home/user/dbadmin/backuptmp \
  --datadir=<server_datadir> --with-timestamp --backup-image=-  --cloud-service=OCI \ 
  --cloud-par-url=<incremental-backup_PAR_URL> --incremental copy-back-and-apply-log
```

**Example 5.15 Restoring a Single-file Backup from an OpenStack Object Storage to a MySQL Server**

```
mysqlbackup \
--defaults-file=<my.cnf> \
--cloud-service=openstack  --cloud-container=<swift container> \
--cloud-user-id=<keystone user> --cloud-password=<keystone password> \
--cloud-region=<keystone region> --cloud-tenant=<keystone tenant> \
--cloud-identity-url=<keystone url> --cloud-object=image_800.mbi \
--backup-dir=/home/user/dba/swiftbackuptmpdir \
--datadir=/home/user/dba/datadir \ 
--backup-image=- \
copy-back-and-apply-log
```

**Example 5.16 Restoring a Single-file Backup from Amazon S3 to a MySQL Server**

```
mysqlbackup\
--defaults-file=<my.cnf> \
--cloud-service=s3 --cloud-aws-region=<aws region> \
--cloud-access-key-id=<aws access key id> --cloud-secret-access-key=<aws secret access key> \
--cloud-bucket=<s3 bucket name> --cloud-object-key=<aws object key> \
--backup-dir=/home/user/dba/s3backuptmpdir --with-timestamp \
--datadir=/home/user/dba/datadir \
--backup-image=- \
copy-back-and-apply-log
```

**Example 5.17 Restoring a Single-file Backup from GCP Storage Service to a MySQL Server**

```
mysqlbackup\
--defaults-file=<my.cnf> \
--cloud-service=GCP \
--cloud-bucket=<bucket name> --cloud-object=<object name> \
--cloud-access-key=<access name> --cloud-secret-key=<secret key> \
--backup-dir=/home/user/dba/backuptmpdir --with-timestamp \
--datadir=/home/user/dba/datadir \
--backup-image=- \
copy-back-and-apply-log
```