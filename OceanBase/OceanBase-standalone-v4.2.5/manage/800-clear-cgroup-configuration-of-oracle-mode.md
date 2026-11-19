---
title: "清除 cgroup 配置"
book: "管理数据库"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000002702238.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 清除 cgroup 配置

cgroup 目录配置后，可以手动删除原来配置的 cgroup 系统目录。

## 前提条件

请确认 cgroup 配置所在的 OBServer 已停止运行。

## 操作步骤

1.  使用 `admin` 用户登录 OBServer 服务器所在的机器。

2.  删除 OceanBase 数据库软件安装目录与 cgroup 目录的软链接。

    ```
    [admin@xxx /home/admin/oceanbase]
    $ll cgroup
    lrwxrwxrwx 1 admin admin 29 Dec  8 11:09 cgroup -> /sys/fs/cgroup/cpu/oceanbase/

    [admin@xxx /home/admin/oceanbase]
    $ rm -rf cgroup
    ```

3.  删除 cgroup 系统目录 `/sys/fs/cgroup/cpu/oceanbase`。

    由于 cgroup 系统目录中的文件需要从下往上递归删除，您可以创建一个脚本文件 `deletecgroupdir.sh` 来批量删除 cgroup 的系统目录。

    1.  创建脚本文件并填入内容保存。

        ```
        [admin@xxx /home/admin]$ vim deletecgroupdir.sh
        ```

        文件中需要填入的内容如下。

        ``` JavaScript
        #! /bin/bash
        function read_dir(){
                for file in `ls $1`
                        do
                                if [ -d $1"/"$file ]
                                        then
                                                read_dir $1"/"$file

                                fi
                done
                string=$1
                echo rmdir $string
                rmdir $string
        }
        #读取第一个参数
        read_dir /sys/fs/cgroup/cpu/oceanbase
        ```

    2.  执行脚本，删除 cgroup 系统目录。

        ```
        [admin@xxx /home/admin]
        $sudo /bin/bash deletecgroupdir.sh
        ```

## 相关文档

[配置 cgroup](100-config-cgroups-of-oracle-mode.md)
