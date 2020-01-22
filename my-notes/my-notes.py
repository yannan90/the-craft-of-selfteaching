12/23/2019

python toturial: https://docs.python.org/3/tutorial/index.html
勾心斗角的套路历史上全都被反复用过了。倒是有本中文书值得吐血推荐，民国时代的作者连阔如先生写的《江湖丛谈》
选择阅读“有繁殖能力”的内容

12/25/2019

***value and their operators:

在 Python 程序中可以用 # 符号标示注释语句
(1,1000)含左侧1但不含右侧1000
x+=1 即 x=x+1

为了更高效使用微软办公套件，你可能会花上一两天时间研究一下 VBA；为了给自己做个网页什么的，你会顺手学会 JavaScript；为了修改某个编辑器插件，你发现人家是用 Ruby 写的，大致读读官方文档，你就可以下手用 Ruby 语言了；为了搞搞数据可视化，你会发现不学会 R 语言有点不方便……

一切计算机程序都由两个基本部分构成：evaluation & control flow

三种基本数据类型： Boolean Values, numbers, strings
针对number的操作： +、-、*、/、//、%、** —— 它们分别代表加、减、乘、除、商、余、幂
针对Boolean Values的操作： and, or, not
针对strings的操作：拼接： +或者空格；拷贝： *；逻辑运算： in, not in, <, <=, >, >=, !=, ==
strings比较大小的原则：逐一字符比较，一旦决出胜负马上停止

type() 查看某个值属于什么基本类型
ord() 显示字符的Unicode

数值计算的操作符优先级最高，其次是逻辑操作符，布尔值的操作符优先级最低

list: []
针对list的操作：与strings相同
list比较大小的原则：list内逐一元素比较，一旦决出胜负马上停止

每个变量或者常量，除了它们的值(value)之外，同时还相当于有一个对应的布尔值。
无论数据的类型是什么，被操作符操作的总是该数据的值(value)，及其相应的布尔值。

操作符：
    值运算
    逻辑运算
函数：
    内建函数（built-in function）
    其他模块（module）里的函数
    其本身所属类（class）之中所定义的函数

备注：
关于表达式：https://docs.python.org/3/reference/expressions.html
关于所有操作的优先级：https://docs.python.org/3/reference/expressions.html#operator-precedence
上一条链接不懂 BNF 的话根本读不懂：https://en.wikipedia.org/wiki/Backus-Naur_form
Python 的内建函数：https://docs.python.org/3/library/functions.html
Python 的标准数据类型：https://docs.python.org/3/library/stdtypes.html
另外，其实所有的操作符，在 Python 内部也是调用函数完成的……
https://docs.python.org/3.7/library/operator.html

12/26/2019

***control flow:
    
if语句： if, elif, else
range(a,b,step)范围包a不包b

绝大多数编程语言中，loop分两种：
    collection controlled loop: 
        for ... in ...
    condition controlled loop: 
        while ...:
            ...

与loop相关的语句还有：
    continue：忽略其后的语句，开始下一次循环
    break：结束并跳出目前的循环，执行之后的语句
    pass：什么都不干，给写程序的人占位用

for语句可以附加一个else，在没有发生break的情况下执行：
    for ...:
        if ...:
            break
    else:
        ...
    
for语句适合处理sequence type的迭代，while语句更灵活。

***functions:

print() 这个函数是可以往文件里写数据的，只要指定 file 这个参数为一个已经打开的文件对象就可以了

function的参数有两种：
    keyword arguments (kwarg): 在函数定义中，带有“=”，已为其设置好默认值的参数
    positional arguments (arg): 其他参数

为了学会使用 Python，你以后最常访问的页面一定是这个：
    https://docs.python.org/3/library/index.html
而最早反复阅读查询的页面肯定是其中的这两个：
    https://docs.python.org/3/library/functions.html
    https://docs.python.org/3/library/stdtypes.html
        
***strings:
    
标示一个字符串，有 4 种方式，用单引号、用双引号，用三个单引号或者三个双引号

字符串相关的built-in function：
    ord(): 把一个字符转换成对应的unicode
    chr(): 把一个整数（unicode）转换成其对应的字符   
    int(): 把字符串转换成整数。注：被转换对象为字符串时，字符串内容只能是整数，否则会报错
    float(): 转换为浮点数
    str(): 转换为字符串
    len(): 求字符串长度
    print()
    input()

转译符号\:
    raw字符 \' 对应的presentation字符 '
    raw字符 \" 对应的presentation字符 "
    raw字符 \n 对应presentation字符 回车
    raw字符 \t 对应presentation字符 TAB
    
字符串可以用空格 ' ' 或者 + 拼接
in 或者 not in 判断是否包含

字符串属于有序容器，可以使用 [] 作为 “索引操作符”提取字符：
    s[index] —— 返回索引值为 index 的那个字符
    s[start:] —— 返回从索引值为 start 开始一直到字符串末尾的所有字符
    s[start:stop] —— 返回从索引值为 start 开始一直到索引值为 stop 的那个字符之前的所有字符
    s[:stop] —— 返回从字符串开头一直到索引值为 stop 的那个字符之前的所有字符
    s[start:stop:step] —— 返回从索引值为 start 开始一直到索引值为 stop 的那个字符之前的，以 step 为步长提取的所有字符
    
处理字符串的Method:
    调用 str 类的 Methods 是使用 . 这个符号，比如：
    'Python'.upper()    
    str.upper() 改成大写
    str.lower() 改成小写
    str.casefold() 改成小写
    str.capitalize() 句子首字母大写
    str.title() 句子中每个单词首字母大写
    str.swapcase() 大小写替换
    str.count(sub [,start=0[, end=len(str)]]) 搜索子字符串出现的次数
    str.find() 显示字符串第一次出现的位置，没找到返回-1
    str.rfind() 显示字符串最后出现的位置，没找到返回-1
    str.index() 显示字符串最后出现的位置，没找到报错
    str.startswith() 判断字符串是否以某个子字符串开始
    str.endswith() 判断字符串是否以某个子字符串结束
    str.replace(old, new[, count]) 用new字符串替代old字符串， 替换count个
    str.strip([chars]) 去掉字符串首尾相应的字符
    str.strip() 去掉字符串首尾所有空白，包括空格、TAB、换行符等等
    str.lstrip([chars]) 去掉字符串左侧相应的字符
    str.rstrip([chars]) 去掉字符串右侧相应的字符
    拆分字符串，返回列表：str.splitlines()；str.split()；str.partition()
    str.join(_iterable_) 拼接字符串：
    str.center(width[, fillchar]) 字符串居中排版， fillchar只接收单个字符
    str.rjust(width[, fillchar]) 字符串右对齐
    str.ljust(width[, fillchar]) 字符串左对齐
    str.zfill(int) 将字符串转换成左侧由 0 填充的指定长度字符串
    
将字符串进行格式化的Method:
    str.format(*args, **kwargs)
    f-string
        f'...{...}...{...}'
        f-string 中用花括号 {} 括起来的部分是表达式，最终转换成字符串的时候，那些表达式的值（而不是变量或者表达式本身）会被插入相应的位置
        
字符串还有一系列的 Methods，返回的是布尔值，用来判断字符串的构成属性。

***numbers:
    
数值相关的built-in function：
    abs(n) 函数返回参数 n 的绝对值；
    int(n) 用来将浮点数字 n 转换成整数；
    float(n) 用来将整数 n 转换成浮点数字；
    divmod(n, m) 用来计算 n 除以 m，返回两个整数，一个是商，另外一个是余；
    pow(n, m) 用来做乘方运算，返回 n 的 m 次方；
    round(n) 返回离浮点数字 n 最近的那个整数。


12/29/2019

***containers:

Mutable: list, dictionary, set
Immutable: string, range(), Tuple, frozen set
    
*List:
    
List comprehension 可以嵌套使用 for，甚至可以加上条件 if，例如：
    a_list=[2**x for x in range(8)]
    b_list=[x for x in a_list if x%2==0]
    
List 的操作符：
    拼接：+ （不能用空格）
    复制：*
    逻辑运算：in 和 not in，<、<=、>、>=、!=、==
        两个列表也和两个字符串一样，可以被比较，即，可以进行逻辑运算；比较方式也跟字符串一样，从两个列表各自的第一个元素开始逐个比较，“一旦决出胜负马上停止”
        
根据索引提取list元素：a_list[start:stop:step] —— list是可变序列，所以，不仅可以提取，还可以删除，甚至替换
根据索引删除list元素：del a_list[start:stop:step]
根据索引替换list元素：a_list[start:stop:step]=t —— len(t) = len([start:stop:step]) 必须为真

L=list(s) 把字符串s的每个字符生成一个list L

List的built-in fuction：
    len()
    max()
    min()
    del a_list[2] 删去a_list索引2的元素
    
List（mutable）的Method:
    a.sort(reverse=False) —— 反向排序的话把reverse参数定为True
    a.append() 在末尾追加一个元素
    a.clear() 清空list
    a.copy() 拷贝一个list, 之后对一个拷贝文件操作，不会更改原件
    a.insert(1,'example') 在索引1的位置插入元素'example'
    a.pop([1]) 删除a中索引为1的元素，并返回该元素的值
    a.remove('example') 把a中'example'这个元素删掉，如果有多个，只删第一个
    
*Tuple:
    
Tuple是immutable，所以，你没办法从里面删除元素。你可以在末尾追加元素。所以，严格意义上，对元组来讲，“不可变” 的意思是说，“当前已有部分不可变”……

a=(1,) —— 创建单个元素的Tuple，无论是否使用圆括号，在那唯一的元素后面一定要补上一个逗号 ,

在将来需要更改的时候，创建 List ；在将来不需要更改的时候，创建 Tuple。其次，从计算机的角度来看，Tuple 相对于 List 占用更小的内存。
    a.__sizeof__() 查看各种container的大小

*Set:

Set不包含重复元素，它是无序的，另外它分为set(mutable), frozen set(immutable)

创建空集合的时候，必须用 set()，而不能用 {}。用{}创建的是一个dictionary

set(s) —— 将序列数据转换（Casting）为set。转换后，返回的是一个已去重的set。

Set的built-in fuction：
    len()
    max()
    min()
    
Set的操作：
    并集：| 或 a.union(b)
    交集：& 或 a.intersection(b)
    差集：- 或 a.difference(b)
    对称差集：^ 或 symmetric_difference(b)
    
Set的逻辑运算：
    set == other
    set !== other
    isdisjoint(other) set与other非重合
    issubset(other) set是other的子集
    set < other set是other的真子集
    issuperset(other) set是other的超集
    set > other set是other的真超集
    
Set的Method：
    a.add(elem)
    a.remove(elem) 从集合中删除 elem；如果集合中不包含该 elem，会产生 KeyError 错误
    a.discard(elem) 如果该元素存在于集合中，删除它
    a.pop(elem) 从集合中删除 elem，并返回 elem 的值，针对空集合做此操作会产生 KeyError 错误
    a.clear() 清空set
    a.update(*others) 更新set,加入others中的所有元素,相当于set |= other | ...
    a.intersection_update(*others) 更新 set, 保留同时存在于 set 和所有 others 之中的元素,相当于set &= other & ...
    a.difference_update(*others) 更新 set, 删除所有在 others 中存在的元素,相当于set -= other | ...
    a.symmetric_difference_update(other) 更新 set, 只保留存在于 set 或 other 中的元素，但不保留同时存在于 set 和 other 中的元素,相当于 set ^= other
    
*Frozen Set： Frozen Set 之于 Set，正如 Tuple 之于 List，前者是Immutable，后者是Mutable，无非是为了节省内存使用而设计的类别。
    有空去看看这个链接就可以了： https://docs.python.org/3/library/stdtypes.html#frozenset
        
*Dictionary：

在同一个字典里，key 都是唯一的。当创建字典的时候，如果其中有重复的 key 的话，就跟 Set 那样会 “自动去重” —— 保留的是众多重复的 key 中的最后一个 key:value_（或者说，最后一个 _key:value “之前那个 key 的 value 被更新了”）。字典这个数据类型之所以叫做 Map（映射），是因为字典里的 key 都映射且只映射一个对应的 _value_。
        
Dictionary的Method：
    