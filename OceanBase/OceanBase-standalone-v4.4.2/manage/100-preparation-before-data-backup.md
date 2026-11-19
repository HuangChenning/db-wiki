---
title: "备份前准备"
book: "管理数据库"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077225.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 备份前准备

#### 说明

MySQL 模式的管理员用户为 ` root` 用户，Oracle 模式的管理员用户为 `SYS` 用户。

#### 注意

OceanBase 数据库当前不会替代您设置合规保留策略，请在设置备份路径前确保 OSS Bucket 已正确设置保留策略（WORM 策略）并锁定。

#### 注意

使用对象存储作为备份介质时，对象存储路径的各项参数由 `&` 符号进行分隔，请确保您输入的参数值中仅包含英文字母大小写、数字、`/-_$+=` 以及通配符。如果您输入了上述以外的其他字符，可能会导致设置失败。

#### 注意

- OceanBase 数据库当前不会替代您设置合规保留策略，请在设置备份路径前确保 OSS Bucket 已正确设置保留策略（WORM 策略）并锁定。
- 使用配置了 WORM 策略的 Bucket 作为备份路径时，推荐清理模式使用 `tagging` 模式。

#### 注意

使用 NFS 作为备份介质时，需要注意以下事项：

- `data_backup_dest` 的值不支持设置为带有问号（?）的字符串。
- `data_backup_dest` 的值必须设置为绝对路径，保证 OBServer 服务器对 `data_backup_dest` 具有写权限。
- 必须保证所有 OBServer 服务器都挂载了同一个服务器的 NFS。同时，为保证备份的顺利进行，务必使用本文档中建议的参数挂载 NFS。挂载 NFS 具体操作请参见 [部署 NFS 客户端](200-deploy-nfs.md)。

#### 注意

使用对象存储作为备份介质时，对象存储路径的各项参数由 `&` 符号进行分隔，请确保您输入的参数值中仅包含英文字母大小写、数字、`/-_$+=` 以及通配符。如果您输入了上述以外的其他字符，可能会导致设置失败。

#### 注意

- 使用对象存储作为备份介质时，对象存储路径的各项参数由 `&` 符号进行分隔，请确保您输入的参数值中仅包含英文字母大小写、数字、`/-_$+=` 以及通配符。如果您输入了上述以外的其他字符，可能会导致设置失败。
- 对于部分兼容 S3 协议的对象存储，可能不支持 AWS S3 SDK 默认的 URL 编码方式，在使用 `s3://` 协议访问时，如果出现 9129、9026 等对象存储相关的错误码，建议通过设置集群级配置项 [ob_storage_s3_url_encode_type](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005286016) 来指定 AWS S3 发送请求时的 URL 编码方式兼容 Rfc3986 标准。详细设置方法可参考下方 **使用 COS 作为备份介质的操作步骤及示例**。

#### 注意

- 使用对象存储作为备份介质时，对象存储路径的各项参数由 `&` 符号进行分隔，请确保您输入的参数值中仅包含英文字母大小写、数字、`/-_$+=` 以及通配符。如果您输入了上述以外的其他字符，可能会导致设置失败。
- 在使用 Azure Blob 作为备份介质时，要求 `host` 参数的前缀必须指定为 `http://` 或 `https://`。同时，由于 Azure Blob 默认开启了安全传输，默认是通过 `https://` 来访问，如果需要通过 `http://` 来访问，需要关闭 Azure Blob 的安全传输选项。关闭 Azure Blob 安全传输选项的详细操作，参见 [Azure Blob 官网文档](https://learn.microsoft.com/en-us/azure/storage/common/storage-require-secure-transfer?toc=%2Fazure%2Fstorage%2Fblobs%2Ftoc.json&bc=%2Fazure%2Fstorage%2Fblobs%2Fbreadcrumb%2Ftoc.json)。

#### 注意

备份秘钥后，在恢复数据前，如果源租户的加密信息触发过秘钥轮转，则需要重新备份源租户的秘钥。
