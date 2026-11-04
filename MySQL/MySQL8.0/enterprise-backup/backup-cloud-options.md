---
title: "20.15 Cloud Storage Options"
book: "MySQL Enterprise Backup User's Guide (Version 8.0.46)"
version: "8.0"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/8.0/en/backup-cloud-options.html"
tags:
  - mysql
  - mysql-8.0
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 8.0.46)

These options are for using cloud storage for single-file operations. See [Section 4.3.1.3, “Backing Up to Cloud Storage”](meb-backup-cloud.md), and [Section 5.2, “Restoring a Backup from Cloud Storage to a MySQL Server”](restore-cloud.md), for more information and instructions on using cloud storage with MySQL Enterprise Backup.

- *Options used for all cloud services:*
	- `--cloud-service` ``=*`SERVICE                 `*``
		Cloud service for data backup or restoration. Various types of cloud storage services are supported by **mysqlbackup**, represented by the following values for the option:
		- `OCI`: Oracle Cloud Infrastructure Object Storage
		- `openstack`: OpenStack Swift or compatible object storage services
		- `s3`: Amazon Simple Storage Service (S3) or compatible storage service
		- `GCP`: GCP object storage
	- `--cloud-trace`
		Print trace information for cloud operations. It works independently of [`--trace`](standard-options.md), which specifies the trace level for the non-cloud operations of **mysqlbackup**. Any non-zero value for the option enables the trace function.
		Default value is “0.”
	- `--cloud-proxy` ``=*`proxy-url:port                 `*``
		Proxy address and port number for overriding the environment's default proxy settings for accessing a cloud storage service.
		Note
		The [`list-image`](backup-commands-single-file.md) operation can be performed on a cloud backup only if the cloud proxy supports HTTP range headers.
	- `--cloud-ca-info` ``=*`PATH`*``
		Absolute path to the CA bundle file for host authentication for SSL connections. When the option is specified, the usage of the CA bundle file is preferred over the usage of individual `.pem` files for host authentication.
	- `--cloud-ca-path` ``=*`PATH`*``
		CA certificate directory, in addition to the system's default folder.
	- `--cloud-buffer-size` ``=*`MB`*``
		Size of the buffer for cloud operations in megabytes. **mysqlbackup** accumulates data up to the size specified by this option before initiating a cloud transfer. The value has to be between 16 to 4096.
		Default: 64
- *Options used for Oracle Cloud Infrastructure (OCI) Object Storage:*
	- `--cloud-object` ``=*`OCI_OBJECT`*``
		The storage object for the backup image. Note that names of objects within the same bucket have to be unique.
	- `--cloud-par-url` ``=*`OCI_PAR-URL`*``
		The [Pre-Authenticated Request (PAR) URL for OCI Object Storage](https://docs.cloud.oracle.com/en-us/iaas/Content/Object/Tasks/usingpreauthenticatedrequests.htm). For a backup to OCI Object Storage, it is the PAR URL for the storage bucket; for restore and other operations on an object stored on OCI, it is the PAR URL for the object.
- *Options used for OpenStack Swift Object Storage:*
	- `--cloud-object` ``=*`SWIFT_OBJECT`*``
		The storage object for the backup image. Note that names of objects within the same container have to be unique.
	- `--cloud-container` ``=*`SWIFT_CONTAINER`*``
		The Swift container for the backup image.
	- `--cloud-user-id` ``=*`SWIFT_USER-ID`*``
		User ID for accessing Swift. The user credentials are authenticated by the Swift TempAuth identity system when the `--cloud-tempauth-url` option is used, by the OpenStack Keystone identity service when the `--cloud-identity-url` option is used, and by HTTP Basic Authentication when the `--cloud-basicauth-url` option is used.
	- `--cloud-password` ``=*`SWIFT_PASSWORD`*``
		Password for accessing Swift for the user specified by the `--cloud-user-id` option. The user credentials are authenticated by the Swift TempAuth identity system when the `--cloud-tempauth-url` option is used, by the OpenStack Keystone identity service when the `--cloud-identity-url` option is used, and by HTTP Basic Authentication when the `--cloud-basicauth-url` option is used.
	- `--cloud-tempauth-url` ``=*`SWIFT_TEMPAUTH-URL`*``
		The TempAuth URL for authenticating user credentials.
	- `--cloud-basicauth-url` ``=*`SWIFT_BASICAUTH-URL`*``
		The URL for HTTP Basic Authentication.
	- `--cloud-identity-url` ``=*`SWIFT_KEYSTONE-URL`*``
		The URL of the Keystone identity service, when it is used for authenticating user credentials.
	- `--cloud-tenant` ``=*`SWIFT_KEYSTONE-TENANT`*``
		The Keystone tenant for the user specified by `--cloud-user-id`, when the Keystone identity service is used for authenticating user credentials.
	- `--cloud-region` ``=*`SWIFT_KEYSTONE-REGION`*``
		The Keystone region for the user specified by `--cloud-user-id`, when the Keystone identity service is used for authenticating user credentials.
	- `--cloud-chunked-transfer` `={true|false}`
		Use chunked transfer. When `--cloud-service=openstack`, backups are always transferred and stored as [Dynamic Large Objects (DLOs)](https://docs.openstack.org/swift/latest/overview_large_objects.html#module-swift.common.middleware.dlo), for which multiple file segments are considered as a single file. The maximum number of segments a backup can have is determined by the object storage service, and the maximum size of the segments is controlled by this option.
		If the option is set to true, **mysqlbackup** uses chunked transfer encoding to transfer the data. A backup larger than the value of ` --cloud-chunk-size` (or, larger than 5GB for release 8.0.22 and earlier) is split into multiple segments.
		If the option is set to false, **mysqlbackup** uploads the backup in segments in the size of the buffer.
		Default: false, when `--cloud-service=openstack`
		Warning
		Set the option to true only if chunked transfer is supported by your cloud storage; otherwise, the **mysqlbackup** operation may fail.
	- `--cloud-chunk-size` ``=*`SWIFT_CHUNK-SIZE`*``
		*For MySQL Enterprise Backup 8.0.23 and later:* The size of a chunk in megabytes if chunked transfer is enabled. This option is ignored if chunked transfer is disabled.
		Minimum value: 64
		Maximum value: 3072 on 32-bit machines, 5120 on 64-bit machines
		Default value: 2048
	Note
	One and only one of `--cloud-tempauth-url`, `--cloud-identity-url`, `--cloud-basicauth-url`, or `--cloud-storage-url` should be used when accessing a Swift service, or **mysqlbackup** will throw an error.
- *Options used for Amazon S3 and S3-compatible services:*
	- `--cloud-host` ``=*`S3_HOSTNAME`*                 ``
		(For MySQL Enterprise Backup 8.0.22 and later) The hostname for an S3-compatible storage service.
		Default: `s3.amazonaws.com`
	- `--cloud-bucket` ``=*`S3_BUCKET`*``
		The storage bucket on an S3-compatible storage service for the backup image.
		In order to perform cloud backups and restores with the bucket, the user identified by the `--cloud-access-key-id` option must have at least the following permissions on the bucket:
		- `s3:ListBucket`: For listing information on items in the bucket.
		- `s3:ListBucketMultipartUploads`: For listing multipart uploads in progress to the bucket.
		- `s3:GetObject`: For retrieving objects from the bucket.
		- `s3:PutObject`: For adding objects to the bucket.
	- `--cloud-object-key` ``=*`S3_OBJECT-KEY`*``
		The S3 object key for the backup image.
	- `--cloud-access-key-id` ``=*`S3_KEY-ID`*``
		Access key ID for logging onto an S3-compatible storage service.
	- `--cloud-secret-access-key` ``=*`S3_ACCESS-KEY`*``
		Secret access key for the access key id specified with `--cloud-access-key-id`.
	- `--cloud-aws-region` ``=*`S3_REGION`*``
		Region for the web service that **mysqlbackup** accesses.
- *Options used for GCP object storage (for MySQL Enterprise Backup 8.0.23 and later):*
	- `--cloud-host` ``=*`HOSTNAME`*``
		The hostname for the storage service.
		Default: `storage.googleapis.com`, when `--cloud-service=GCP`
	- `--cloud-bucket` ``=*`BUCKET`*``
		The storage bucket for the backup image.
	- `--cloud-object` ``=*`OBJECT`*``
		The storage object for the backup image. Note that names of objects within the same bucket have to be unique.
	- `--cloud-access-key` ``=*`ACCESS-KEY`*``
		Access key for the cloud account. The option is mandatory for a backup operation. If it is not provided for a restore operation, **mysqlbackup** assumes the backup image is a public object and can be accessed or downloaded without a key; if the object is not public, the restore operation fails.
	- `--cloud-secret-key` ``=*`SECRET-KEY`*``
		Secret key for the cloud account specified with `--cloud-access-key`. The option is mandatory for a backup operation.
	- `--cloud-chunked-transfer` `={true|false}`
		Use chunked transfer.
		If the option is set to true, **mysqlbackup** uses chunked transfer encoding to transfer the data. A backup larger than the value of `--cloud-chunk-size` is split into multiple segments.
		If the option is set to false, **mysqlbackup** uploads the backup in segments in the size of the buffer.
		Default: true, when `--cloud-service=GCP`
	- `--cloud-chunk-size` ``=*`CHUNK-SIZE`*``
		The size of a chunk in megabytes if chunked transfer is enabled. This option is ignored if chunked transfer is disabled.
		Minimum value: 64
		Maximum value: 3072 on 32-bit machines, 5120 on 64-bit machines
		Default value: 2048