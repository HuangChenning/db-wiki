---
title: "管理死锁自动检测"
book: "组件 & 工具"
version: V4.5.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005258519.html"
tags:
  - oceanbase
  - distributed
  - ref-components-and-tools
---

# 管理死锁自动检测

死锁自动检测用于自动检测并解决死锁，为集群级别行为，默认是开启状态，将保存 7 天的死锁记录。

## 关闭死锁自动检测

1. 登录 obshell Dashboard。

2. 在左侧导航栏单击 **集群管理**，进入 **集群管理** 页面。

3. 当光标悬停于 **集群管理** 页面右上方的 **···** 时，单击出现的 **关闭死锁自动检测** 按钮。在对话框中单击 **确定** ，即可关闭。

   ![关闭死锁检测](img/036e64f798441284.png)

   <main id="notice" type='explain'>
     <h4>说明</h4>
     <p>关闭死锁自动检测后，将不再进行自动死锁检测和解决死锁，请谨慎操作。</p>
   </main>

## 开启死锁自动检测

1. 登录 obshell Dashboard。

2. 在左侧导航栏单击 **集群管理**，进入 **集群管理** 页面。

3. 当光标悬停于 **集群管理** 页面右上方的 **···** 时，单击出现的 **开启死锁自动检测** 按钮。在对话框中单击 **确定** ，即可开启，操作路径和关闭死锁检测一致。

   <main id="notice" type='explain'>
     <h4>说明</h4>
     <p>开启死锁自动检测后会自动检测并解决死锁，集群内所有租户将同步开启，本功能对集群有 2% 左右的性能损耗，请谨慎操作。</p>
   </main>

## 相关文档

查看死锁历史信息相关内容，可参见 [会话管理](../400.ob-dashboard-tenant/450.session-management.md)。
