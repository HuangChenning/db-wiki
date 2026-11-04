---
title: "dmSQLAlchemy 方言包"
book: "DM8 dmPython 使用手册"
version: "DM8"
source: https://eco.dameng.com/document/dm/zh-cn/pm/dmsqlalchemy-dialect-package.html
tags:
  - dameng
  - dm8
  - dmpython
---

## 5.1 简介及安装

SQLAlchemy 是 python 下的开源软件，提供了 SQL 工具包及对象关系映射（ORM）工具，让应用程序开发人员使用上 SQL 的强大功能和灵活性。dmSQLAlchemy 方言包是 DM 提供用于 SQLAlchemy 连接 DM 数据库的方法。

1.SQLAlchemy 软件的安装。例如：SQLAlchemy-1.1.10.win-amd64-py2.7.exe。

2.dmSQLAlchemy 方言包的软件生成与安装。

dmSQLAlchemy 可以运行在任何安装了 Python 的平台上。生成工具 setup.py 位于 drivers\\python\\dmSQLAlchemy\\dmSQLAlchemyx.x 目录中。

可以使用如下命令很方便地在 Windows 和 Linux 操作系统下编译并安装 dmSQLAlchemy：

```
//进入到setup.py所在的源码目录，执行以下命令：

python setup.py install
```

也可以先生成安装文件再进行安装，不同平台生成安装包的命令如下：

```
Windows：python setup.py bdist_wininst

Linux：python setup.py bdist_rpm
```

生成之后的安装包（例如 dmSQLAlchemy-1.1.10.win-amd64.exe）位于 drivers\\python\\dmSQLAlchemy\\dmSQLAlchemyx.x\\dist 目录中。点击安装包安装即可。

DM 提供的 dmSQLAlchemy 与 SQLAlchemy 的版本对应关系如下表：

表5.1 dmSQLalchemy版本对应表

| **dmSQLAlchemy 版本** | **SQLAlchemy 版本** |
| --- | --- |
| 1.1.x | 1.3.x |
| 1.4.x | 1.4.x |
| 2.0.x | 2.0.x |

## 5.2 engine 的配置

create\_engine()返回一个数据库引擎，下面是 DM 数据库的配置方法。

```
from sqlalchemy import create_engine

engine =
create_engine('dm://SYSDBA:Dmsys_123@localhost:5236/',connect_args={'local_code':1,'connection_timeout':15})

    或

engine =
create_engine('dm+dmPython://SYSDBA:Dmsys_123@localhost:5236/',connect_args={'local_code':1,'connection_timeout':15})
```

其中，connect\_args 是字典选项，只要在 connect\_args 中以字典对象的方式配置 dmPython.connect 支持的选项即可。可以包含多个字典对象，用逗号分隔。dmPython.connect 请参考 3.1.1.1 dmPython.connect。其他官方配置参考 SQLAlchemy 官网 [http://docs.sqlalchemy.org](http://docs.sqlalchemy.org/) 文档。

同时 dmSQLAlchemy 存在独属于 dmSQLAlchemy 的配置选项：

a) compatible\_mode：此选项用来设置区分不同功能实现，可以设置为 DM、Oracle、MySQL 和 TSQL，缺省时为 DM。例如采用 MYSQL 时，对于 json 类型，返回值将返回为 dict 类型。

b) add\_quote\_all：此选项用来设置 dmSQLAlchemy 执行操作时是否对于所有表名，列名等增加引号，可以设置为 True 和 False，缺省为 False。例如设置为 True 时，将会使所有的表名与列名等完全遵循输入大小写，设置为 False 时将采用默认的 SQLAlchemy 大小写逻辑。

## 5.3 类型映射

### 5.3.1 简介

SQLAlchemy 支持了数据库中使用的大部分类型，根据映射关系，dmSQLAlchemy 方言包支持达梦数据库的下列类型：

ARRAY，BFILE，BIGINT，BINARY，BIT，BLOB，CHAR，CHARACTER，CLOB，DATE，DATETIME，DEC，DECIMAL，DOUBLE，DOUBLE PRECISION，FLOAT，JSON，JSONB，INT，INTEGER，INTERVAL YEAR，INTERVAL MONTH，INTERVAL DAY，INTERVAL HOUR，INTERVAL MINUTE，INTERVAL SECOND，INTERVAL YEAR TO MONTH，INTERVAL DAY TO HOUR，INTERVAL DAY TO MINUTE，INTERVAL DAY TO SECOND，INTERVAL HOUR TO MINUTE，INTERVAL HOUR TO SECOND，INTERVAL MINUTE TO SECOND，IMAGE，ROWID，LONG，NCLOB，NUMBER，NUMERIC，NVARCHAR2，REAL，SMALLINT，TEXT，TIME，TIME WITH TIME ZONE，TIMESTAMP，TIMESTAMP WITH LOCAL TIME ZONE，TIMESTAMP WITH TIME ZONE，TINYINT，VARBINARY，VARCHAR，VARCHAR2，VECTOR。

其中由于 SQLAlchemy 类型支持问题，DECIMAL，DEC，NUMBER 与 NUMERIC 类型在 SQLAlchemy 中均被映射为 NUMBER 类型，时间间隔数据类型（INTERVAL YEAR 等）均被映射为 INTERVAL 类型，CHARACTER 类型被映射为 CHAR 类型，TINYINT 类型被映射为 SMALLINT 类型，CLOB 类型与 LONGVARCHAR 类型被映射为 TEXT 类型 TIME WITH TIME ZONE 类型被映射为 TIME 类型。

### 5.3.2 向量类型

在 dmSQLAlchemy 2.0.8 版本新增了对于数据库中向量类型的支持，由于原生 SQLAlchemy 中不支持 VECTOR 类型，当前调用时需要使用 dmSQLAlchemy 中的方法直接调用。

#### 5.3.2.1 所需环境

由于 VECTOR 类型中部分方法需要 numpy 库支持，如果需要使用 VECTOR 类型，则需要安装 numpy 模块：

```
// 在非离线状态下，执行以下命令：
pip install numpy
// 在离线状态下，可以将whl包放到环境中，使用pip install 安装指定的包，或者直接将源码包放到环境中使用pip install .或python setup.py install安装
```

如果需要启用 VectorWordSeek，则需要使用 sentence\_transformers 库，同时需要准备本地模型，例如 all-MiniLM-L6-v2 轻量级模型等；启用 VectorImageSeek 时则需要 torch 库，同时也需要准备本地模型，例如 resnet50 轻量级模型等。

#### 5.3.2.2 简单向量数据库示例

示例一 创建一个表，表中有向量列，向其中插入向量数据，查询列以及与指定向量的欧式距离，之后删除指定行，创建 ivf 索引，重建 ivf 索引，最终查询列定义。

```
from sqlalchemy import create_engine, inspect, Identity, Integer, select, Column, Sequence
from sqlalchemy.orm import Session, sessionmaker, declarative_base
from dmSQLAlchemy import VECTOR, VectorAdaptor
Base=declarative_base()
engine =create_engine('dm+dmPython://SYSDBA:SysDBA*00@localhost:5236', echo=True)
adaptor = VectorAdaptor(engine)
Session=sessionmaker(bind=engine)
session=Session()

inspector = inspect(engine)

class ItemModel(Base):
    __tablename__ = "test_vector"
    id = Column(Integer,Identity(), primary_key=True)
    embedding = Column(VECTOR(dim=3, format='float64'))

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
session.add(ItemModel(embedding=[1, 2, 3]))# 插入Vector类型数据
session.add(ItemModel(embedding=[2, 2, 3]))
session.add(ItemModel(embedding=[5, 2, 1]))
distance = ItemModel.embedding.l1_distance([1,2,3])# 使用欧氏距离作为列输出
result = session.query(ItemModel.id, distance).all()
for row in result:
    print(row)
session.query(ItemModel).filter(ItemModel.embedding == [1, 2, 3]).delete()# 删除vector列值为[1, 2, 3]的行
session.commit()
adaptor.create_vector_ivf_index(ItemModel.embedding, metric_name = "cosine", index_name = "indexc")# 创建ivf索引
adaptor.rebuild_vector_ivf_index(ItemModel.embedding, metric_name = "cosine", index_name = "indexc")# 重建ivf索引
session.commit()

columns = inspector.get_columns('test_vector')
for row in columns:
    print(row)
```

示例二 创建以词搜词实例对象，向其中存入数据后进行以词搜词。

```
from dmSQLAlchemy import VECTOR, VectorAdaptor, VectorWordSeek

conn_str = 'dm+dmPython://SYSDBA:SysDBA*00@localhost:5236/'
wordseekmodel = VectorWordSeek(table_name='test_wordseek', connection_str = conn_str, model_path=r"path\to\model", drop_if_existing = True, engine_args = {'echo' : True})
wordseekmodel.drop_table()
wordseekmodel.create_table(True) #创建指定表
wordseekmodel.insert(texts = ['This is a flag', 'This is a notice', 'This is a camp'])

result = wordseekmodel.query(count = 2, DistanceMetric = 'COSINE', query_vector = ['dog'])
for row_dict in result:
    print(row_dict)
```

示例三 创建以词搜词实例对象，向其中存入数据后进行以词搜词。使用图像识别方式进行搜索。

```
from dmSQLAlchemy import VECTOR, VectorAdaptor, VectorWordSeek, VectorImageSeek

conn_str = 'dm+dmPython://SYSDBA:Hust4400_DBA@localhost:5236/'

wordseekmodel = VectorImageSeek(table_name='test_imageseek', drop_if_existing = True, connection_str = conn_str, engine_args = {'echo' : True}, model_path=r"path\to\model")
wordseekmodel.drop_table()
wordseekmodel.create_table(True)
wordseekmodel.insert(paths = ["path\to\images"])

result = wordseekmodel.query(count = 10, DistanceMetric = 'COSINE', query_vector = 'path\to\image')
for row_dict in result:
    print(row_dict)
```

### 5.3.3 dm\_vec\_client 向量客户端

dmSQLAlchemy 在 2.0.13 版本新增了 dm\_vec\_client 功能，该功能的实现主要依托于 dmVecClient 类，该对象用于生成一个客户端类，支持调用其下的各种方法操作数据库内表。

#### 5.3.3.1 接口类

dm\_vec\_client 中的可调用类有：DataType、FieldSchema、VecIndexType、CollectionSchema、dmVecClient，下面将详细介绍这些类的用法：

**1.** **DataType**

**功能描述**

指定创建类型。

**使用说明**

可选类型有：INT、BOOL、JSON、TEXT、BLOB、DATE、INT64、ARRAY、FLOAT、ROWID、BIGINT、DOUBLE、STRING、BINARY、VARCHAR、INTERVAL、TIMESTAMP、INT8\_VECTOR、FLOAT\_VECTOR、FLOAT32\_VECTOR、FLOAT64\_VECTOR、SPARSE\_FLOAT\_VECTOR、UNKNOWN。

其中，SPARSE\_FLOAT\_VECTOR 类型用于指定稀疏向量类型，当前数据库内暂不支持，使用时会进行报错处理。

**2.** **FieldSchema**

**功能描述**

指定表中的列。

**参数详解**

name：定义列名，string 类型。

dtype：定义列类型，DataType 类型。

description：定义列描述信息，string 类型。

is\_primary：定义列是否为主键，bool 类型，默认值为 FALSE。

auto\_id：定义列是否自增，bool 类型，默认值为 FALSE。

nullable：定义列是否可以为 null，bool 类型，默认值为 TRUE。

**3.** **VecIndexType**

**功能描述**

指定向量索引类型。

**使用说明**

当前仅支持 HNSW 与 IVF\_FLAT 两种类型。

**4.** **CollectionSchema**

**功能描述**

指定绑定表类型，用于后续在 client 的 create\_collection 等功能中指定绑定表类型。

**参数详解**

fields：定义表中各列，包含一个及以上的列定义，list 类型。

description：定义表描述信息，string 类型。

**5.** **dmVecClient**

**功能描述**

用于绑定连接，内部包含功能函数调用，可操作数据库内表。

**参数详解**

url：host 与端口号，string 类型，默认值为"localhost:5236"。

user：用户名，string 类型，默认值为"SYSDBA"。

password：用户连接密码，string 类型，默认值为""。

db\_name：默认连接模式，string 类型，默认值为""。

echo：执行时是否输出语句，bool 类型，默认值为 FALSE。

connect\_args：额外连接参数，dict 类型，默认值为{}。

token：token 验证，暂无作用，string 类型，默认值为""。

timeout：指定执行默认超时时长，int 类型，默认值为 0。

#### 5.3.3.2 client 功能函数

**1.** **create\_schema**

**功能描述**

创建空的 CollectionSchema 实例。

**参数详解**

无。

**2.** **create\_collection**

**功能描述**

创建数据库内部表对象。

**参数详解**

collection\_name：指定表名，string 类型。

dimension：创建的向量列维度，string 类型，默认值为 None。

primary\_field\_name：主键名，string 类型，默认值为"id"。

id\_type：主键类型，string 类型，默认值为"int"。

metric\_type：向量索引距离运算函数，string 类型，默认值为"COSINE"。

auto\_id：主键是否自增，bool 类型，默认值为 FALSE。

timeout：指定执行超时时长，int 类型，默认值为 0。

schema：列对象集合，CollectionSchema 实例类型，默认值为 None。

Index\_params：索引对象，IndexParams 实例类型，默认值为 None。

**3.** **prepare\_index\_params**

**功能描述**

创建空的索引对象集合。

**参数详解**

无。

**4.** **get\_collection\_stats**

**功能描述**

获取数据库内表对象的行数。

**参数详解**

collection\_name：指定表名，string 类型。

timeout：执行超时时长，int 类型，默认值为 0。

**5.** **drop\_collection**

**功能描述**

删除数据库内部表对象。

**参数详解**

collection\_name：指定表名，string 类型。

timeout：执行超时时长，int 类型，默认值为 0。

**6.** **drop\_table\_if\_exist**

**功能描述**

如果数据库内存在则删除数据库内部表对象。

**参数详解**

collection\_name：指定表名，string 类型。

timeout：执行超时时长，int 类型，默认值为 0。

**7.** **has\_collection**

**功能描述**

查询是否存在表对象。

**参数详解**

collection\_name：指定表名，string 类型。

timeout：执行超时时长，int 类型，默认值为 0。

**8.** **rename\_collection**

**功能描述**

重命名表对象。

**参数详解**

old\_name：指定旧表名，string 类型。

new\_name：指定新表名，string 类型。

timeout：执行超时时长，int 类型，默认值为 0。

**9.** **create\_index**

**功能描述**

创建索引对象。

**参数详解**

collection\_name：指定表名，string 类型。

index\_params：指定索引参数，IndexParams 实例。

timeout：执行超时时长，int 类型，默认值为 0。

**10.** **drop\_index**

**功能描述**

删除索引对象。

**参数详解**

index\_name：指定索引名，string 类型。

timeout：执行超时时长，int 类型，默认值为 0。

collection\_name：指定表名，string 类型。

**使用说明**

collection\_name 仅在 MySQL 语法中存在作用，当前由于 MySQL 语法模式暂时不支持向量类型，因此暂无作用。

**11.** **rebuild\_index**

**功能描述**

重建索引对象。

**参数详解**

collection\_name：指定表名，string 类型。

index\_params：指定索引参数，IndexParams 实例类型。

timeout：执行超时时长，int 类型，默认值为 0。

schema\_name：模式名，string 类型，默认值为 None。

metric\_type：向量索引距离运算函数，string 类型，默认值为 None。

target\_accuracy：IVF 预测准确率，int 类型，默认值为 0。

cluster\_centers：聚类中心数量，int 类型，默认值为 0。

percentage\_value：HNSW 预测准确率，int 类型，默认值为 0。

max\_connection：图节点最大连接数，int 类型，默认值为 0。

ef\_construction：图候选节点数量，int 类型，默认值为 0。

**使用说明**

当前重建索引仅支持 IVF 索引与 HNSW 索引，其中，当重建索引为 HNSW 索引时仅可设置 schema\_name、index\_name,metric\_name、percentage\_value、max\_connection、ef\_construction 参数；当重建索引为 IVF 索引时仅可设置 schema\_name、index\_name、metric\_name、target\_accuracy、cluster\_centers 参数。

**12.** **insert**

**功能描述**

向数据库表中插入数据。

**参数详解**

collection\_name：指定表名，string 类型。

data：插入数据，dict 类型。

timeout：执行超时时长，int 类型，默认值为 0。

partition\_name：分区名，string 类型，默认值为""。

**使用说明**

由于当前达梦中暂不支持指定分区，因此 partition\_name 参数暂时无效。

**13.** **commit**

**功能描述**

提交数据。

**参数详解**

无。

**14.** **delete**

**功能描述**

删除数据。

**参数详解**

collection\_name：指定表名，string 类型。

ids：主键筛选值，可为 dict/list/string/int 类型，默认值为 None。

timeout：执行超时时长，int 类型，默认值为 0。

filter：剩余筛选项，dict 类型，默认值为 None。

**15.** **upsert**

**功能描述**

插入数据，如果存在约束冲突则更新。

**参数详解**

collection\_name：指定表名，string 类型。

data：插入数据，dcit 类型。

timeout：执行超时时长，int 类型，默认值为 0。

partition\_name：分区名，string 类型，默认值为""。

**使用说明**

由于当前达梦中暂不支持指定分区，因此 partition\_name 参数暂时无效。

**16.** **get**

**功能描述**

根据主键值取值获取数据。

**参数详解**

collection\_name：指定表名，string 类型。

ids：主键筛选值，可为 dict/list/string/int 类型。

output\_fields：输出列名，可为 dict/list/string/int 类型，默认值为 None。

timeout：执行超时时长，int 类型，默认值为 0。

partition\_name：分区名，string 类型，默认值为""。

**使用说明**

由于当前达梦中暂不支持指定分区，因此 partition\_name 参数暂时无效。

**17.** **query**

**功能描述**

根据筛选条件查询。

**参数详解**

collection\_name：指定表名，string 类型。

filter：剩余筛选项，dict 类型，默认值为 None。

output\_fields：输出列名，list 类型，默认值为 None。

timeout：执行超时时长，int 类型，默认值为 0。

ids：主键筛选值，可为 dict/list/string/int 类型。

partition\_name：分区名，string 类型，默认值为""。

**使用说明**

由于当前达梦中暂不支持指定分区，因此 partition\_name 参数暂时无效。

**18.** **search**

**功能描述**

根据向量距离进行查询。

**参数详解**

collection\_name：指定表名，string 类型。

data：需要运算的向量数据，list 类型，默认值为 None。

filter：剩余筛选项，dict 类型，默认值为 None。

limit：limit 选项，dict 类型，默认值为 10。

with\_dist：输出列名，bool 类型，默认值为 FALSE。

output\_fields：输出列名，list 类型，默认值为 None。

search\_params：向量查询选项，dict 类型，默认值为 None。

timeout：执行超时时长，int 类型，默认值为 0。

partition\_name：分区名，string 类型，默认值为""。

anns\_fields：向量列名，string 类型，默认值为 None。

ids：主键筛选值，可为 dict/list/string/int 类型。

**使用说明**

由于当前达梦中暂不支持指定分区，因此 partition\_name 参数暂时无效。

#### 5.3.3.3 简单使用示例

创建一个 dmVecClient 实例 client 与一个 FieldSchema 列表，列表中包含一个映射表表，表中有向量列，向 fields 中加入 IVF 索引，通过 client 删除原有表，再执行表的创建，重建索引，通过 client 对表执行增删改查的操作。

```
from sqlalchemy.sql import text
from dmSQLAlchemy import *
import random
import numpy as np

client = dmVecClient(uri="localhost:5236", user="SYSDBA", password="Hust4400_DBA", echo=True)

fields = [
    FieldSchema(
        name="id",
        dtype=DataType.INT,
        is_primary=True,
        auto_id=True,
    ),
    FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=64),
    FieldSchema(name="metadata", dtype=DataType.JSON),
]

index_params = client.prepare_index_params()
index_params.add_index(
    field_name="embedding",
    index_name="embedding_idx",
    index_type=VecIndexType.IVF_FLAT,
    distance="IP",
    m=16,
    ef_construction=256,
)

schema = CollectionSchema(fields)
table_name = "vector_search"
client.drop_table_if_exist(table_name)
client.create_collection(table_name, schema=schema, index_params=index_params)
res = client.has_collection(table_name)
print(res)
client.rebuild_index(table_name, 'embedding_idx')
random.seed(20241023)

batch_size = 100
batch = []
for i in range(1000):
    batch.append(
        {
            "embedding": [random.uniform(-1, 1) for _ in range(64)],
            "metadata": {"idx": i},
        }
    )
    if len(batch) == batch_size:
        client.insert(collection_name=table_name, data=batch)
        batch = []

if len(batch) > 0:
    client.insert(collection_name=table_name, data=batch)
res = client.get_collection_stats(collection_name=table_name)
print(res)
data = [
    {
        "id": 1,                     # 主键，必须唯一
        "embedding": np.random.random(64).tolist(),  # 假设向量维度是128
        "metadata": {"idx": 99},
    },
    {
        "id": 2,
        "embedding": np.random.random(64).tolist(),
        "metadata": {"idx": 99},
    }
]

result = client.delete(collection_name=table_name, ids=[1, 2, 4], flter=[text("id in (100, 99, 5)"), text("id = 4")])
print(result)
result = client.upsert(collection_name=table_name, data=data)
print(result)
client.commit()
target_data = [random.uniform(-1, 1) for _ in range(64)]
res = client.search(
    collection_name=table_name,
    data=target_data,
    anns_field="embedding",
    output_fields=["id", "metadata"],
)
print(res)

columns = inspector.get_columns('test_vector')
for row in columns:
    print(row)
```

## 5.4 异步功能

### 5.4.1 简介

dmSQLAlchemy 在 2.0.7 版本支持了 SQLAlchemy 的异步功能，由于功能要求限制，当前仅支持在 SQLAlchemy 版本大于 2.0.22 的版本上使用异步功能，同时需要 python 中安装了 dmAsync 包。

### 5.4.2 使用

可以通过创建异步 connection 或者创建异步 session 两种方法来使用 dmSQLAlchemy。

#### 5.4.2.1 通过创建异步 connection 使用 dmSQLAlchemy

与正常使用 SQLAlchemy 的异步连接数据库方法相同，可以通过在创建 engine 时使用 create\_async\_engine 方法创建异步 engine，通过异步 engine 的 begin 接口创建连接，通过连接执行语句：

```
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, MetaData, text
import asyncio

engine = create_async_engine("dm+dmAsync://SYSDBA:sysDBA*00@localhost:5236/", echo=True)
AsyncSessionLocal = sessionmaker(autoflush=False, bind=engine, class_=AsyncSession)

async def async_func():
async with AsyncSessionLocal() as session:
  query = text('SELECT * FROM DUAL;')
  result = await session.execute(query)
  rows = result.fetchall()
  for row in rows:
  print(row)

   await session.commit()
   await engine.dispose()

asyncio.run(async_func())
```

#### 5.4.2.2 通过创建异步 session 使用 dmSQLAlchemy

除了通过 connection 去执行语句，更常用的方法是通过创建异步 session 去使用 SQLAlclehmy。

在创建 engine 时使用 create\_async\_engine 方法可以创建异步 engine，根据异步 engine，使用 async\_sessionmaker 方法创建 session，从而进行对数据库的异步操作

```
import asyncio
import datetime
from typing import List
from sqlalchemy import ForeignKey
from sqlalchemy import func
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import selectinload
 
class Base(AsyncAttrs, DeclarativeBase):
  pass
class B(Base):
 __tablename__ = "b"
   id: Mapped[int] = mapped_column(primary_key=True)
   a_id: Mapped[int] = mapped_column(ForeignKey("a.id"))
   data: Mapped[str]
   
class A(Base):
  __tablename__ = "a"
  id: Mapped[int] = mapped_column(primary_key=True)
  data: Mapped[str]
  create_date: Mapped[datetime.datetime] = mapped_column(server_default=func.now())
  bs: Mapped[List[B]] = relationship()

async def insert_objects(async_session: async_sessionmaker[AsyncSession]) -> None:
async with async_session() as session:
 async with session.begin():
 session.add_all(
 [  A(bs=[B(data="b1", id=1), B(data="b2", id=2)], data="a1",id=1),
    A(bs=[], data="a2",id=2),
    A(bs=[B(data="b3", id=3), B(data="b4", id=4)], data="a3",id=3),
     ]
  )
 async def select_and_update_objects(
 async_session: async_sessionmaker[AsyncSession],
) -> None:
 async with async_session() as session:
 stmt = select(A).order_by(A.id).options(selectinload(A.bs))
 result = await session.execute(stmt)
 for a in result.scalars():
 print(a, a.data)
 print(f"created at: {a.create_date}")
 for b in a.bs:
 print(b, b.data)
 result = await session.execute(select(A).order_by(A.id).limit(1))
 a1 = result.scalars().one()
 a1.data = "new data"
 await session.commit()
 print(a1.data)
 for b1 in await a1.awaitable_attrs.bs:
 print(b1, b1.data)
 
async def async_main() -> None:
  engine = create_async_engine("dm+dmAsync://SYSDBA:sysDBA*00@localhost:5236", echo=True)
  async_session = async_sessionmaker(engine, expire_on_commit=False)
  async with engine.begin() as conn:
  await conn.run_sync(Base.metadata.create_all)
  await insert_objects(async_session)
  await select_and_update_objects(async_session)
  await engine.dispose()
  
asyncio.run(async_main()
```

## 5.5 特殊说明

1、dmSQLalchemy 当前版本，主键 integer primary\_key 不会再自动形成自增列了；

2、只有当 dmPython 版本大于 2.5.9 时才可以正常使用 executemany 返回多行数据集；

3、由于表名标准化问题，克隆或迁移表时，全大写表名将无法识别，请避免使用此类表名；

4、由于当 python 中的 True 或 False 作为 JSON 类型的值时，选取时使用的 json\_value 函数在匹配时如果期望匹配 True 或 False，需要使用字符串’true’或’false’匹配。

5、由于 SQLAlchemy 对于类型返回值的检测问题，导致 JSON 类型无法返回为正常的 dict，因此暂时将从数据库中查询到的 JSON 或者 JSONB 类型列的值映射为字符串类型返回。

## 5.6 暂不支持功能

1、由于数据库语法暂不支持 LATERAL 功能，因此在 dmSQLAlchemy 中当前暂不支持使用 SQLAlchemy 提供的 lateral 方法构建子查询语句。

2、由于语法限制暂不支持使用 bulk\_insert\_mappings，supports\_default\_values，supports\_empty\_insert 等空值插入方法。

## 5.7 方言包特殊连接参数

为了适配不同情况，创建连接时可以通过 OPTIONS 设置选项，在 dmSQLAlchemy 中允许设置仅属于 dmSQLAlchemy 的特殊的连接选项，当前 dmSQLAlchemy 包含以下连接参数：

compatible\_mode 选项

简介：用来适配不同兼容模式下处理

可选值：'DM'，'MYSQL'，'TSQL'，'ORACLE'

默认值：'DM'

不同选项含义：当前仅使用'MYSQL'参数值会有区别，其余参数对于结果无影响。当参数值被设置为'MYSQL'时，对于 JSON 类型，在从数据库内部获取数据时将被转换为 dict 类型，其余情况将返回为字符串类型。

parse\_type 选项

简介：用来使方言包采用不同语法解析模块执行语句

可选值：'DM'，'MYSQL'，'TSQL'

默认值：'DM'

不同选项含义：当采用以上不同参数时，将采用对应的语法解析模块，同时，在该语法解析模式下 compatible\_mode 选项将被默认设置为对应的兼容模式，如需更改，需显式指定为其他兼容模式。

add\_quote\_all 选项

简介：用来使方言包对于所有表名、列名等信息增加双引号，保证大小写完全一致

可选值：true 或 false

默认值：false

不同选项含义：当设置为 true 时，方言包在执行语句时，将对所有表名、列名、模式名等增加双引号，从而保证所有执行操作的表名、列名、模式名等与输入时保持大小写完全一致，当设置为 false 时，则遵循 SQLAlchemy 原始设置对于部分情况下名称增加双引号。