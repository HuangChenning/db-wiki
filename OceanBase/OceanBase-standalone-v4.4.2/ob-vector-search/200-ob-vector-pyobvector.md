---
title: "pyobvector Python SDK 接口说明"
book: OceanBase AI
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077516.html"
tags:
  - oceanbase
  - standalone
  - ob-vector-search
---

# pyobvector Python SDK 接口说明

pyobvector 是 OceanBase 向量存储功能的 python SDK，它提供两种使用模式：

- pymilvus 兼容模式：使用 MilvusLikeClient 对象操作数据库，提供与轻量级 MilvusClient 兼容的常用接口。

- SQLAlchemy 扩展模式：使用 ObVecClient 对象操作数据库，提供关系型数据库的 python SDK 扩展。

本文分别介绍了这两种模式下的使用接口与示例。

## MilvusLikeClient

### 构造函数

``` python

def __init__(
    self,
    uri: str = "127.0.0.1:2881",
    user: str = "root@test",
    password: str = "",
    db_name: str = "test",
    **kwargs,
)
```

### collection 相关接口

[TABLE]

### CollectionSchema & FieldSchema

MilvusLikeClient 通过 CollectionSchema 描述一个表的模式定义，一个 CollectionSchema 包含多个 FieldSchema， FieldSchema 描述一个表的列模式。

#### 通过 MilvusLikeClient 的 create_schema 创建 CollectionSchema

``` python
def __init__(
    self,
    fields: Optional[List[FieldSchema]] = None,
    partitions: Optional[ObPartition] = None,
    description: str = "",  # ignored in oceanbase
    **kwargs,
)
```

参数说明如下：

- fields：一组可选的 FieldSchema。

- partitions：分区规则（详见使用 ObPartition 定义分区规则章节）。

- description：与 Milvus 兼容用，在 OceanBase 中暂无实际作用。

#### 创建 FieldSchema 并注册到 CollectionSchema

``` python
def add_field(self, field_name: str, datatype: DataType, **kwargs)
```

- field_name：列名称。

- datatype：列数据类型（支持的数据类型请参见[兼容性说明](800-ob-vector-sdk-refer.md)）。

- kwargs：其他参数用于配置列属性，如下：

  ``` python
  def __init__(
  self,
  name: str,
  dtype: DataType,
  description: str = "",
  is_primary: bool = False,
  auto_id: bool = False,
  nullable: bool = False,
  **kwargs,
  )
  ```

  参数说明如下：

  - is_primary：是否是主键。

  - auto_id：是否是自增列。

  - nullable：是否允许为空。

#### 使用示例

``` python
schema = self.client.create_schema()
schema.add_field(field_name="id", datatype=DataType.INT64, is_primary=True)
schema.add_field(field_name="title", datatype=DataType.VARCHAR, max_length=512)
schema.add_field(
    field_name="title_vector", datatype=DataType.FLOAT_VECTOR, dim=768
)
schema.add_field(field_name="link", datatype=DataType.VARCHAR, max_length=512)
schema.add_field(field_name="reading_time", datatype=DataType.INT64)
schema.add_field(
    field_name="publication", datatype=DataType.VARCHAR, max_length=512
)
schema.add_field(field_name="claps", datatype=DataType.INT64)
schema.add_field(field_name="responses", datatype=DataType.INT64)

self.client.create_collection(
    collection_name="medium_articles_2020", schema=schema
)
```

### 索引相关

[TABLE]

## ObVecClient

### 构造函数

``` python
def __init__(
    self,
    uri: str = "127.0.0.1:2881",
    user: str = "root@test",
    password: str = "",
    db_name: str = "test",
    **kwargs,
)
```

### 表模式相关操作

[TABLE]

### DML 操作

[TABLE]

## 使用 ObPartition 定义分区规则

pyobvector 提供了以下类型来支持 range/range columns、list/list columns、hash、key 以及二级分区：

- ObRangePartition：range 一级分区。构造时设置 `is_range_columns = True` 以创建 range columns 分区。

- ObListPartition：list 一级分区。构造时设置 `is_list_columns = True` 以创建 list columns 分区。

- ObHashPartition：hash 一级分区。

- ObKeyPartition：key 一级分区。

- ObSubRangePartition：二级 range 分区。构造时设置 `is_range_columns = True` 以创建 range columns 二级分区。

- ObSubListPartition：list 二级分区。构造时设置 `is_list_columns = True` 以创建 list columns 二级分区。

- ObSubHashPartition：hash 二级分区。

- ObSubKeyPartition：key 二级分区。

### range 分区示例

``` python
range_part = ObRangePartition(
    False,
    range_part_infos=[
        RangeListPartInfo("p0", 100),
        RangeListPartInfo("p1", "maxvalue"),
    ],
    range_expr="id",
)
```

### list 分区示例

``` python
list_part = ObListPartition(
    False,
    list_part_infos=[
        RangeListPartInfo("p0", [1, 2, 3]),
        RangeListPartInfo("p1", [5, 6]),
        RangeListPartInfo("p2", "DEFAULT"),
    ],
    list_expr="col1",
)
```

### hash 分区示例

``` python
hash_part = ObHashPartition("col1", part_count=60)
```

### 多级分区示例

``` python
# 一级range分区
range_columns_part = ObRangePartition(
    True,
    range_part_infos=[
        RangeListPartInfo("p0", 100),
        RangeListPartInfo("p1", 200),
        RangeListPartInfo("p2", 300),
    ],
    col_name_list=["col1"],
)
# 二级range分区
range_sub_part = ObSubRangePartition(
    False,
    range_part_infos=[
        RangeListPartInfo("mp0", 1000),
        RangeListPartInfo("mp1", 2000),
        RangeListPartInfo("mp2", 3000),
    ],
    range_expr="col3",
)
range_columns_part.add_subpartition(range_sub_part)
```

## 纯 SQLAlchemy API 模式

如果你希望在 OceanBase 数据库的向量搜索功能下使用纯粹的 SQLAlchemy API，可以通过如下两种方式获取同步的数据库引擎：

- 方式一：使用 ObVecClient 辅助创建数据库引擎

``` python
from pyobvector import ObVecClient

client = ObVecClient(uri="127.0.0.1:2881", user="test@test")
engine = client.engine
# 接下来正常使用 SQLAlchemy 创建 session，使用 SQLAlchemy 的 API 即可
```

- 方式二：使用 ObVecClient 的 `create_engine` 接口创建数据库引擎

``` python
import pyobvector
from sqlalchemy.dialects import registry
from sqlalchemy import create_engine

uri: str = "127.0.0.1:2881"
user: str = "root@test"
password: str = ""
db_name: str = "test"
registry.register("mysql.oceanbase", "pyobvector.schema.dialect", "OceanBaseDialect")
connection_str = (
    # mysql+oceanbase 表示选择 mysql 标准并使用 OceanBase 数据库的同步驱动
    f"mysql+oceanbase://{user}:{password}@{uri}/{db_name}?charset=utf8mb4"
)
engine = create_engine(connection_str, **kwargs)
# 接下来正常使用 SQLAlchemy 创建 session，使用 SQLAlchemy 的 API 即可
```

如果期望使用 SQLAlchemy 的异步接口，可以使用 OceanBase 数据库的异步驱动：

``` python
import pyobvector
from sqlalchemy.dialects import registry
from sqlalchemy.ext.asyncio import create_async_engine

uri: str = "127.0.0.1:2881"
user: str = "root@test"
password: str = ""
db_name: str = "test"
registry.register("mysql.aoceanbase", "pyobvector", "AsyncOceanBaseDialect")
connection_str = (
    # mysql+aoceanbase 表示选择 mysql 标准并使用 OceanBase 数据库的异步驱动
    f"mysql+aoceanbase://{user}:{password}@{uri}/{db_name}?charset=utf8mb4"
)
engine = create_async_engine(connection_str)
# 接下来正常使用 SQLAlchemy 创建 session，使用 SQLAlchemy 的 API 即可
```

## 更多示例

访问 [pyobvector 代码仓库](https://github.com/oceanbase/pyobvector) 获取更多示例。
