---
title: "日志归档前准备"
book: "管理数据库"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003577588.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 日志归档前准备

#### 注意

对于小规模租户（CPU 小于或等于 4C 的租户），建议使用默认值，不要调整该配置项的值。

#### 说明

OceanBase 数据库从 V4.2.1 版本开始，`TENANT = all_user` 与 `TENANT = all`语义相同，在需要生效范围为所有用户租户时，推荐使用 `TENANT = all_user`，后续 `TENANT = all` 将废弃不再使用。

#### 说明

MySQL 模式的管理员用户为 `root` 用户，Oracle 模式的管理员用户为 `SYS` 用户。

#### 注意

OceanBase 数据库当前不会替代您设置合规保留策略，请在设置归档路径前确保 OSS Bucket 已正确设置保留策略（WORM 策略）并锁定。

#### 注意

使用对象存储作为归档介质时，对象存储路径的各项参数由 `&` 符号进行分隔，请确保您输入的参数值中仅包含英文字母大小写、数字、`/-_$+=` 以及通配符。如果您输入了上述以外的其他字符，可能会导致设置失败。

#### 注意

OceanBase 数据库当前不会替代您设置合规保留策略，请在设置归档路径前确保 OSS Bucket 已正确设置保留策略（WORM 策略）并锁定。

#### 注意

使用 NFS 作为归档介质时，需要注意以下事项：

- `LOCATION` 的值不支持设置为带有问号（?）的字符串。
- `LOCATION` 的值必须设置为绝对路径，保证 OBServer 服务器对 `LOCATION` 具有读写权限。
- 必须保证所有 OBServer 服务器都挂载了同一个服务器的 NFS。同时，为保证归档顺利进行，务必使用本文档中建议的参数挂载 NFS。挂载 NFS 的具体操作，请参见 [部署 NFS 客户端](200-deploy-nfs.md)。

#### 注意

使用对象存储作为归档介质时，对象存储路径的各项参数由 `&` 符号进行分隔，请确保您输入的参数值中仅包含英文字母大小写、数字、`/-_$+=` 以及通配符。如果您输入了上述以外的其他字符，可能会导致设置失败。

#### 注意

使用对象存储作为归档介质时，对象存储路径的各项参数由 `&` 符号进行分隔，请确保您输入的参数值中仅包含英文字母大小写、数字、`/-_$+=` 以及通配符。如果您输入了上述以外的其他字符，可能会导致设置失败。

#### 注意

在归档运行期间，不支持切换归档所使用的访问协议。例如，不支持从 S3 切换到 OSS 或从 OSS 切换到 S3。

#### 注意

- 使用对象存储作为归档介质时，对象存储路径的各项参数由 `&` 符号进行分隔，请确保您输入的参数值中仅包含英文字母大小写、数字、`/-_$+=` 以及通配符。如果您输入了上述以外的其他字符，可能会导致设置失败。
- 在使用 Azure Blob 作为归档介质时，要求 `host` 参数的前缀必须指定为 `http://` 或 `https://`。同时，由于 Azure Blob 默认开启了安全传输，默认是通过 `https://` 来访问，如果需要通过 `http://` 来访问，需要关闭 Azure Blob 的安全传输选项。关闭 Azure Blob 安全传输选项的详细操作，参见 [Azure Blob 官网文档](https://learn.microsoft.com/en-us/azure/storage/common/storage-require-secure-transfer?toc=%2Fazure%2Fstorage%2Fblobs%2Ftoc.json&bc=%2Fazure%2Fstorage%2Fblobs%2Fbreadcrumb%2Ftoc.json)。

#### 注意

在配置 `archive_lag_target` 参数时，不支持 sys 租户通过 `TENANT = all_user` 来指定所有用户租户。
