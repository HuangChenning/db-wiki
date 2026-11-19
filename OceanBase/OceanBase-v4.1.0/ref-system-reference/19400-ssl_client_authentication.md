---
title: ssl_client_authentication
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001699367.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# ssl_client_authentication

ssl_client_authentication 用于设置是否开启 SSL 连接功能。


|      **属性**      |                                                    **描述**                                                     |
|------------------|---------------------------------------------------------------------------------------------------------------|
| 参数类型             | 布尔类型                       |
| 默认值              | False                      |
| 取值范围             | <li> False：不开启   <li> True：开启    |
| 是否重启 OBServer 节点生效 | 是                          |


  <main id="notice" type='notice'>
    <h4>注意</h4>
    <p>ssl_client_authentication 配置后，仅在服务器重新启动所有 ca、cert、key 等文件后才生效。</p>
  </main>
