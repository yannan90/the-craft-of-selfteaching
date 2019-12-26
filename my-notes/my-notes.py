12/23/2019

python toturial: https://docs.python.org/3/tutorial/index.html
勾心斗角的套路历史上全都被反复用过了。倒是有本中文书值得吐血推荐，民国时代的作者连阔如先生写的《江湖丛谈》
选择阅读“有繁殖能力”的内容

12/25/2019


in 判断是否包含
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

每个变量或者常量，除了它们的值之外，同时还相当于有一个对应的布尔值。
无论数据的类型是什么，被操作符操作的总是该数据的值，及其相应的布尔值。

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




