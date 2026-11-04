---
title: "许可证 (License) 的安装"
book: "DM8 安装手册"
version: "DM8"
source: https://eco.dameng.com/document/dm/zh-cn/pm/license.html
tags:
  - dameng
  - dm8
  - installation
---

用户安装 DM 时，可导入相应的许可证(License)。License 的载体是一个加密文件 dm.key，内容是达梦公司对用户使用 DM 软件的授权。DM 软件安装后，如果需要得到更多授权的用户，可联系达梦公司获取相应的 License，并按照下面的操作方法进行安装。

## 3.1 Windows 下 License 的安装

用户获得 License 文件 dm.key 后，将 dm.key 复制到 DM 安装目录下的 DM 服务器所在目录中即可。dm.key 的放置不受服务器状态影响，也不会影响正在运行的 DMServer，服务器仅定时检测并读取 dm.key 的信息。

**操作方法如下** ：

第一步，打开 DM 服务器所在的目录。当 DM 安装目录为 C:\\dmdbms 时，则 DM 服务器所在的目录为 C:\\dmdbms\\bin。将 dm.key 复制到该目录下，替换原来的 dm.key 文件。

第二步，使用 SYSDBA 登录数据库，执行以下命令，进行 DM 服务器的 LICENSE 校验，检查 LICENSE 与当前 DM 版本及系统运行环境是否一致。一致则执行成功；不一致则报错。

```
SP_LOAD_LIC_INFO();
```

第三步，查看 V$LICENSE 了解所安装的 DM 数据库的 LICENSE 信息，包括许可证版本号、LICENSE 文件序列号、服务器版本类型、服务器发布类型、服务器版本号、有效日期等，以确认新的 license 是否生效。

```
SELECT * FROM V$LICENSE;
```

说明：该目录下原有的 dm.key 文件请事先做好备份。

## 3.2 Linux(Unix)下 License 的安装

用户获得 License 文件 dm.key 后，将 dm.key 复制到 DM 安装目录下的 DM 服务器所在目录中即可。dm.key 的放置不受服务器状态影响，也不会影响正在运行的 DMServer，服务器仅定时检测并读取 dm.key 的信息。这与 Windows 下 License 的安装类似。

**操作方法如下** ：

第一步，找到 DM 服务器所在的目录，方法是以 root 用户或安装用户登录到 Linux 系统，启动终端，执行以下命令即可进入 DM 服务器程序安装的目录：

```
##注：假设安装目录为/opt/dmdbms

cd /opt/dmdbms/bin
```

然后，将 dm.key 文件拷贝到该目录，替换原有的 dm.key。

第二步，使用 SYSDBA 登录数据库，执行以下命令，进行 DM 服务器的 LICENSE 校验，检查 LICENSE 与当前 DM 版本及系统运行环境是否一致。一致则执行成功；不一致则报错。

```
SP_LOAD_LIC_INFO();
```

第三步，查看 V$LICENSE 了解所安装的 DM 数据库的 LICENSE 信息，包括许可证版本号、LICENSE 文件序列号、服务器版本类型、服务器发布类型、服务器版本号、有效日期等，以确认新的 license 是否生效。

```
SELECT * FROM V$LICENSE;
```

说明：该目录下原有的 dm.key 文件请事先做好备份。