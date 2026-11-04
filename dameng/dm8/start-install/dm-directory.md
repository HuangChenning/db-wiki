---
title: "数据库目录结构介绍"
book: "DM 数据库安装"
version: "DM8"
source: https://eco.dameng.com/document/dm/zh-cn/start/dm-directory.html
tags:
  - dameng
  - dm8
  - start-install
---

## 一、数据库安装目录

下图展示为 DM8 数据库目录。

/home/dmdba/dmdbms/bin 目录存放 DM 数据库的可执行文件，例如 disql 命令、dminit 命令、dmrman 工具等。

![image.png](img/20240130111852XJRP76WJCWROUGPCKO.png)

/home/dmdba/dmdbms/desktop/icons 存放 DM 数据库各个工具的桌面图标。

![image.png](img/20240130112000SQ3I5VCFNVCIDM5I9C.png)

/home/dmdba/dmdbms/doc 存放 DM 数据库用户手册。

![image.png](img/20240130112133AN0Q8GUUTZCO6BR5N5.png)

/home/dmdba/dmdbms/drivers 存放连接 DM 数据库的驱动文件。

![image.png](img/20240130112242AIFMLHHNUY7CIHYZ8L.png)

/home/dmdba/dmdbms/log 存放 DM 数据库日志，包括工具的日志、数据库日志、服务日志等。

![image.png](img/2024013011235450OT8JW6JB9H5CD6SM.png)

/home/dmdba/dmdbms/samples 存放 DM 数据库各类配置文件的示例文件。

![image.png](img/2024013011250046M2WPZNDKNTNIPO0X.png)

/home/dmdba/dmdbms/script/root 存放注册、注销 DM 数据库服务的工具，例如 dm\_service\_installer.sh 等。

![image.png](img/202401301126108BS3DLCU0XUREQLMCQ.png)

/home/dmdba/dmdbms/tool 存放 DM 数据库的各个工具，例如 manager 管理工具、dbca 数据库配置助手等。

![image.png](img/20240130112721G0AFHG2UWYKH1CT2FO.png)

/home/dmdba/dmdbms/uninstall 目录存放卸载 DM 数据库的脚本。

![image.png](img/20240130112847HXF1BW10EN2LJ9I7G5.png)

/home/dmdba/dmdbms/web 目录存放 DM 数据库 dem 工具的 web 环境。

![image.png](img/20240130112959VI9967Q2LNEDHK1W2Y.png)

## 二、数据库实例目录

/dmdata/data 为数据库实例目录，该目录存放各个实例的文件。

![image.png](img/20240130113403A8653ELPKCIZTZLJR6.png)

以实例 DAMENG 为例，该目录下存放 DAMENG 实例的配置文件 `*.ini、控制文件 dm.ctl、数据文件 *.DBF、日志文件 *.log` 等。

![image.png](img/20240130114133H84932DACAEGUA0VNG.png)