### chatGPT-4o

| 方法类型 | 装饰器             | 第一个参数   | 作用对象   | 常见用途        |
| ---- | --------------- | ------- | ------ | ----------- |
| 实例方法 | *(无装饰器)*        | `self`  | 实例     | 访问和修改实例属性   |
| 类方法  | `@classmethod`  | `cls`   | 类      | 操作类级别的数据或行为 |
| 静态方法 | `@staticmethod` | *(无参数)* | 类或实例都可 | 工具函数，不关心状态  |

`@classmethod` 是 Python 的一个装饰器，意思是“**类方法**”，它定义的方法**不是作用于实例（对象）上的，而是作用于类本身**。

## ✅ 类方法常见用途

### 1. **工厂方法**（class method 常用模式）

你可以用 `@classmethod` 创建**多种构造方式**：

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        from datetime import datetime
        age = datetime.now().year - birth_year
        return cls(name, age)
```

使用方式：

```python
p = Person.from_birth_year("Alice", 2000)
print(p.age)  # 比如 25
```

📌 `cls(name, age)` 就相当于调用 `Person(name, age)`，而且支持子类继承。

---

### 2. **修改类属性**

```python
class Counter:
    count = 0

    @classmethod
    def increment(cls):
        cls.count += 1
```

可以直接调用：

```python
Counter.increment()
print(Counter.count)  # 1
```
### --------------------------------------------------------------------  
`@classmethod`无需创建实例，可以直接调用

```python
class MyClass:
    @classmethod
    def class_method(cls):
        print("Class method called")

MyClass.class_method()  # 无需实例化，直接调用
```
### --------------------------------------------------------------------  

`__foo__`: 表示python固定占有的一些def，比如
```python
def __getattr__(self, name):
    """Delegate all other attribute access to inner agent system."""
    return getattr(self.inner, name) 
```

### --------------------------------------------------------------------

### ChatGPT-4o
| 命名形式       | 含义                | 是否系统保留？ |
| ---------- | ----------------- | ------- |
| `name`     | 正常名称              | 否       |
| `_name`    | 内部使用约定（非强制私有）     | 否       |
| `__name`   | **名字改写，伪私有化**     | 否       |
| `__name__` | **魔术方法 / 系统定义方法** | ✅ 是     |

### --------------------------------------------------------------------  
写外面的是class variable（同享），里面是instance variable（独占）
```python
class Bands:
    death = 'yes'
    def __init__(self):
        self.age = 29
```


`hasattr` and `getattr`
```python
class Person:
    def __init__(self):
        self.name = "Alice"

p = Person()

# hasattr：判断是否有 name 属性
print(hasattr(p, 'name'))  # True
print(hasattr(p, 'age'))   # False

# getattr：获取属性值
print(getattr(p, 'name'))  # "Alice"

# getattr：尝试获取不存在的属性，不提供默认值会报错
# print(getattr(p, 'age'))  # AttributeError

# getattr：提供默认值
print(getattr(p, 'age', 30))  # 30
```
### --------------------------------------------------------------------  
`isinstance`: bool. 检查对象是否是类型之一或者继承关系  
### deepseek-v3 
`isinstance()` 是 Python 的一个内置函数，用于检查一个对象是否是指定类（或类型）的实例，或者是否是其子类的实例。  

### 基本语法：
```python
isinstance(object, classinfo)
```
- **object**：要检查的对象。
- **classinfo**：可以是一个类（类型），或者由多个类组成的元组（用于检查是否属于其中任意一个类）。

### 返回值：
- 如果 `object` 是 `classinfo` 的实例或其子类的实例，返回 `True`。
- 否则，返回 `False`。


### 示例 1：检查对象是否是某个类的实例
```python
num = 42
print(isinstance(num, int))  # True，因为 42 是 int 类型的实例
print(isinstance(num, float))  # False，因为 42 不是 float 类型
```

### 示例 2：检查对象是否是多个可能类型之一
```python
value = 3.14
print(isinstance(value, (int, float, str)))  # True，因为 3.14 是 float 类型
```

### 示例 3：检查继承关系
```python
class Animal:
    pass

class Dog(Animal):
    pass

dog = Dog()
print(isinstance(dog, Dog))  # True，dog 是 Dog 类的实例
print(isinstance(dog, Animal))  # True，Dog 继承自 Animal，所以 dog 也是 Animal 的实例
```

### --------------------------------------------------------------------  
### chatgpt-4o

`system.exit()` 中数字的含义。不填 = `0` = `None` 

| 退出码    | 含义                   | 常见场景举例                             |
| ------ | -------------------- | ---------------------------------- |
| `0` / `None`   | 成功（Success）          | 程序正常完成                             |
| `1`    | 一般性错误（General Error） | 未捕获的异常、用户输入错误                      |
| `2`    | 错误使用命令行参数            | `argparse` 默认退出码                   |
| `126`  | 命令无法执行               | 比如试图运行一个不可执行的文件                    |
| `127`  | 命令未找到                | 比如打错命令名或路径                         |
| `130`  | 用户用 Ctrl+C 中断程序      | 信号 `SIGINT`                        |
| `>128` | 被信号中断（Unix）          | `128 + 信号编号`，例如 `137` 是 SIGKILL（9） |

### -------------------------------------------------------------------- 
参数前面`**`, 收集参数成为一个字典 

```python
# 调用时
register(
    cls=SomeClass,
    name="my_agent", 
    agent_class=MyAgentClass,
    max_workers=4,           # 这些会被收集到 default_config 中
    timeout=30,              # 这些会被收集到 default_config 中
    retry_count=3,           # 这些会被收集到 default_config 中
    debug=True               # 这些会被收集到 default_config 中
)

# default_config 的值会是：
# {
#     "max_workers": 4,
#     "timeout": 30,
#     "retry_count": 3,
#     "debug": True
# }
```

### --------------------------------------------------------------------  
### --------------------------------------------------------------------  
### --------------------------------------------------------------------  
### --------------------------------------------------------------------  
### --------------------------------------------------------------------  
### --------------------------------------------------------------------  
### --------------------------------------------------------------------  
### --------------------------------------------------------------------  
### --------------------------------------------------------------------  