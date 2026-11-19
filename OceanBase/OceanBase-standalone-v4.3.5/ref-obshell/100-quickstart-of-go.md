---
title: "obshell-sdk-go 快速上手"
book: obshell
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003976061.html"
tags:
  - oceanbase
  - standalone
  - ref-obshell
---

# obshell-sdk-go 快速上手

## 环境要求

需确保环境中的 obshell 处于运行状态。

## 操作步骤

1.  安装 obshell-sdk-go

    ```
    go get github.com/oceanbase/obshell-sdk-go
    ```

2.  创建客户端

    您可以选择创建单一版本客户端，或者创建多版本客户端集。

    创建单一版本客户端

    创建多版本客户端集

    ``` go
    package main

    import (
        "github.com/oceanbase/obshell-sdk-go/services/v1"
    )

    func main() {
        client, err := v1.NewClientWithPassword("10.10.10.1", 2886, "${password}")
        if err != nil {
            // Handle exceptions
            panic(err)
         }
    }
    ```

    ``` go
    package main

    import (
        "github.com/oceanbase/obshell-sdk-go/services"
    )

    func main() {
        clientset, err := services.NewClientWithPassword("10.10.10.1", 2886, "${password}")
        if err != nil {
            // Handle exceptions
            panic(err)
        }
    }
    ```

    示例中的 `10.10.10.1` 为目标 obshell 节点的 IP 地址，`2886` 为目标 obshell 节点的服务端口号，需根据实际情况修改为对应的 IP 和端口号。`${password}` 需配置为目标 obshell 所在集群 root@sys 用户的密码。

3.  部署 OceanBase 集群

    obshell-sdk-go 提供了两类方法来创建一个 OceanBase 集群：一是向 obshell 请求对应的 API 方法成功后，立刻返回；二是向 obshell 请求 API 成功后，等待 obshell 任务执行完成后再返回。前者任务异步执行，后者任务同步执行。示例代码如下：

    任务异步执行

    任务同步执行

    ``` go
    package main

     import (
         "github.com/oceanbase/obshell-sdk-go/services"
         "github.com/oceanbase/obshell-sdk-go/services/v1"
     )

     func main() {
         client, err := services.NewClientWithPassword("10.10.10.1", 2886, "****")
         if err != nil {
             panic(err)
         }

         // join 自己成为 MASTER
         joinRequest1 := client.V1().NewJoinRequest("10.10.10.1", 2886, "zone1")
         dag, err := client.V1().JoinSyncWithRequest(joinRequest1)
         if err != nil {
             panic(err)
         }
         if _, err = client.V1().WaitDagSucceed(dag.GenericID); err != nil {
             panic(err)
         }

         // obshell prior to 4.2.3.0 should use mysqlPort(rpcPort) instead of mysql_port(rpc_port).
         configs := map[string]string{
             "mysql_port": "2881", "rpc_port": "2882", "datafile_size": "24G", "cpu_count": "16", "memory_limit": "16G", "system_memory": "8G", "log_disk_size": "24G",
         }
         // 设置 OBServer 节点的配置项
         configObserverReq := client.V1().NewConfigObserverRequest(configs, v1.SCOPE_GLOBAL)
         dag, err = client.V1().ConfigObserverSyncWithRequest(configObserverReq)
         if err != nil {
             panic(err)
         }
         if _, err = client.V1().WaitDagSucceed(dag.GenericID); err != nil {
             panic(err)
         }

         // 设置 OceanBase 集群的配置信息
         configObclusterReq := client.V1().NewConfigObclusterRequest("obshell-sdk-test", 12358).SetRootPwd("****")
         dag, err = client.V1().ConfigObclusterSyncWithRequest(configObclusterReq)
         if err != nil {
             panic(err)
         }
         if _, err = client.V1().WaitDagSucceed(dag.GenericID); err != nil {
             panic(err)
         }

         // 初始化集群
         initReq := client.V1().NewInitRequest()
         dag, err = client.V1().InitSyncWithRequest(initReq)
         if err != nil {
             panic(err)
         }
         if _, err = client.V1().WaitDagSucceed(dag.GenericID); err != nil {
             panic(err)
         }
     }
    ```

    ``` go
    package main

     import (
         "github.com/oceanbase/obshell-sdk-go/services"
         "github.com/oceanbase/obshell-sdk-go/services/v1"
     )

     func main() {
         client, err := services.NewClientWithPassword("10.10.10.1", 2886, "****")
         if err != nil {
             panic(err)
         }

         // join 自己成为 MASTER
         joinRequest1 := client.V1().NewJoinRequest("10.10.10.1", 2886, "zone1")
         if _, err = client.V1().JoinSyncWithRequest(joinRequest1); err != nil {
             panic(err)
         }

         // obshell prior to 4.2.3.0 should use mysqlPort(rpcPort) instead of mysql_port(rpc_port).
         configs := map[string]string{
             "mysql_port": "2881", "rpc_port": "2882", "datafile_size": "24G", "cpu_count": "16", "memory_limit": "16G", "system_memory": "8G", "log_disk_size": "24G",
         }
         // 设置 OBServer 节点的配置项
         configObserverReq := client.V1().NewConfigObserverRequest(configs, v1.SCOPE_GLOBAL)
         if _, err = client.V1().ConfigObserverSyncWithRequest(configObserverReq); err != nil {
             panic(err)
         }

         // 设置 OceanBase 集群的配置信息
         configObclusterReq := client.V1().NewConfigObclusterRequest("obshell-sdk-test", 12358).SetRootPwd("****")
         if _, err = client.V1().ConfigObclusterSyncWithRequest(configObclusterReq); err != nil {
             panic(err)
         }

         // 初始化集群
         initReq := client.V1().NewInitRequest()
         if _, err = client.V1().InitSyncWithRequest(initReq); err != nil {
             panic(err)
         }
     }
    ```
