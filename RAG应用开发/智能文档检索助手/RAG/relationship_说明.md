# relationship 使用说明（小白版）

## 📚 什么是 relationship？

`relationship` 是 SQLAlchemy 提供的一个功能，它让你可以**像访问对象属性一样访问关联的数据**，而不需要写复杂的 SQL JOIN 查询。

## 🎯 简单理解

想象一下：
- **没有 relationship**：你需要手动写 SQL 查询，像 `SELECT * FROM documents JOIN parent_chunks ON ...`
- **有 relationship**：直接写 `doc.parent_chunks` 就能获取所有关联的父块

## 📖 你的数据模型关系

```
Document (文档)
  ├── 一个文档可以有多个 ParentChunk (父块)
  └── 一个文档可以有多个 ChildChunk (子块)

ParentChunk (父块)
  ├── 属于一个 Document (文档)
  └── 可以有多个 ChildChunk (子块)

ChildChunk (子块)
  ├── 属于一个 Document (文档)
  └── 属于一个 ParentChunk (父块)
```

## 💡 实际使用示例

### 1. 通过文档获取所有父块

```python
# 查询一个文档
doc = session.query(Document).first()

# 使用 relationship 直接访问所有父块（不需要写 JOIN！）
parent_chunks = doc.parent_chunks  # 这是一个列表

# 遍历所有父块
for chunk in parent_chunks:
    print(chunk.content)
```

### 2. 通过父块获取所属文档

```python
# 查询一个父块
parent_chunk = session.query(ParentChunk).first()

# 使用 relationship 直接访问所属文档（不需要写 JOIN！）
doc = parent_chunk.document  # 这是一个 Document 对象

# 访问文档属性
print(doc.filename)
print(doc.content)
```

### 3. 通过父块获取所有子块

```python
# 查询一个父块
parent_chunk = session.query(ParentChunk).first()

# 使用 relationship 直接访问所有子块
child_chunks = parent_chunk.child_chunks  # 这是一个列表

# 遍历所有子块
for chunk in child_chunks:
    print(chunk.content)
```

### 4. 通过子块获取父块和文档

```python
# 查询一个子块
child_chunk = session.query(ChildChunk).first()

# 访问所属的父块
parent = child_chunk.parent_chunk
print(parent.content)

# 访问所属的文档
doc = child_chunk.document
print(doc.filename)
```

### 5. 创建关联数据

```python
# 创建文档
doc = Document(
    filename="test.txt",
    file_path="/path/to/test.txt",
    content="文档内容"
)
session.add(doc)
session.flush()  # 获取文档ID

# 创建父块，直接关联文档对象
parent_chunk = ParentChunk(
    parent_id="parent_001",
    content="父块内容",
    document=doc  # 直接赋值文档对象，SQLAlchemy 会自动设置 document_id
)
session.add(parent_chunk)

# 创建子块，关联文档和父块
child_chunk = ChildChunk(
    child_id="child_001",
    content="子块内容",
    document=doc,  # 直接赋值文档对象
    parent_chunk=parent_chunk  # 直接赋值父块对象
)
session.add(child_chunk)

session.commit()
```

### 6. 级联删除（自动删除关联数据）

```python
# 删除文档时，会自动删除所有关联的父块和子块
# 因为设置了 cascade="all, delete-orphan"

doc = session.query(Document).first()
session.delete(doc)  # 删除文档
session.commit()

# 所有关联的 parent_chunks 和 child_chunks 也会自动删除！
```

## 🔑 关键点总结

1. **relationship 不是数据库字段**：它只在 Python 代码中有效，不会在数据库中创建列

2. **back_populates 必须成对出现**：
   - `Document` 中有 `parent_chunks = relationship("ParentChunk", back_populates="document")`
   - `ParentChunk` 中必须有 `document = relationship("Document", back_populates="parent_chunks")`
   - 两边的参数要对应！

3. **访问方式**：
   - 一对多关系：返回**列表**（如 `doc.parent_chunks`）
   - 多对一关系：返回**单个对象**（如 `parent_chunk.document`）

4. **cascade 参数**：
   - `cascade="all, delete-orphan"` 表示删除父对象时，自动删除所有子对象

## 🚀 运行示例代码

运行 `relationship_demo.py` 文件可以看到所有示例的实际效果：

```bash
python relationship_demo.py
```

## ❓ 常见问题

**Q: relationship 和 ForeignKey 有什么区别？**
- `ForeignKey`：数据库层面的外键约束，存储在数据库中
- `relationship`：Python 层面的关联关系，用于方便访问数据

**Q: 为什么需要 back_populates？**
- 它建立双向关系，让你可以从任意一方访问另一方
- 例如：可以从文档访问父块，也可以从父块访问文档

**Q: 不写 relationship 可以吗？**
- 可以，但你需要手动写 SQL JOIN 查询，代码会更复杂

