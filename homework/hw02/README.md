## hw02
这一节的作业很有启发性
https://inst.eecs.berkeley.edu/~cs61a/fa21/hw/hw02/

Reading https://composingprograms.com/pages/16-higher-order-functions.html

### Q2: Accumulate
Shown how powerful high-order function could have!
将复杂的计算过程抽象成高阶函数组合，每一个小函数的工作都比较简单，但通过组合，构建出复杂的过程

### Q3: Church numerals
不需要过度沉迷于函数嵌套一些技巧，**高阶函数的精髓在于行为抽象、行为参数化及传递**，所以这个题看看理解就好. **Q2: Accumulate才是重点**

这个题很有意思，通过函数的方式表达数字
通过这个题，我对高阶函数又有了些不同理解。
zero, one, two, ...都是以f为参数的高阶函数, 参数f接受传入的函数
one, two的定义很关键，定义好后可以帮助我们找到一般规律

##### 定义one, two
```python
def zero(f):
    '''
    模拟zero计算过程：
    > f = lambda x:x+1
    > zero(f)(5）
    > (lambda x: x)(5)
    > 5

    zero也可以改写为：
    zero = lambda f: lambda x: x
    '''
    return lambda x: x

def successor(n):
    return lambda f: lambda x: f(n(f)(x))

def one(f):
    '''
    one = successor(zero)
        = lambda f: lambda x: f(zero(f)(x))
        = lambda f: lambda x: f( (lambda x: x)(x) )
        = lambda f: lambda x: f(x)
    Then change lambda exp to def exp:
    def one(f):
        return lambda x: f(x)
    '''
    return lambda x: f(x)

def two(f):
    '''
    two = successor(one)
        = lambda f: lambda x: f(one(f)(x))
        = lambda f: lambda x: f(temp_func(x))   # temp_func = one(f) = lambda x: f(x)
        = lambda f: lambda x: f(f(x))
    '''
    return lambda x: f(f(x))
```

##### add, mul, pow
一开始我就想到通过函数组合的方式来设计计算过程，当时没想太清楚，靠着感觉组合，误打误撞先把pow, mul弄出来了，最后才弄出来add.

```python
'''
add
three = f(f(f(x)))
two = f(f(x))
five = two + three = f[f[ f(f(f(x))) ]]
从计算过程来分析:
先计算出y = three(f)(x), 之后将该结果传给two(f)(y), 相当于应用了5次函数f
'''
print(church_to_int( lambda f: lambda x: two(f)(three(f)(x)) ))

'''
mul
six 需要应用6次函数f
two的计算过程是对传入的函数f，连续应用2次
three的计算过程是对传入的函数f联系应用3次
所以构造 two(three(f))，对three的计算过程再应用2次，一共6次
'''
print(church_to_int( lambda f: lambda x: two(three(f))(x) ))

'''
pow
2**3 = 8
pow(two, three)相当于连续应用8次f
two = lambda f: lambda x: f(f(x))
three = lambda g: lambda x: g(g(g(x)))
three(two) = lambda x: two(two(two(x))) = lambda f: lambda x: two(two(two(f)))(x)
'''
print(church_to_int( three(two) ))
# same as above
# print(church_to_int( lambda f: three(two)(f) ))
# print(church_to_int( lambda f: lambda x: three(three(three(f)))(x) ))
```

##### 对函数嵌套的一些理解
有点像List，Stream, 惰性求值方式，在运行时逐层执行函数, 高阶函数也可以delay真实逻辑的执行
List(1, List(2, List(3, List(4))))
Stream(1, Stream(2, Stream(3, Stream(4))))
感觉有点分治算法的意思

注意函数只是定义了**计算过程**，但还没有真正执行，只有传入所需的参数后才会执行，参看如下例子：
```python
In [213]: def two(f):
     ...:     def xF(x):
     ...:         print('inside xF')
     ...:         return f(f(x))
     ...:     print('inside two')
     ...:     return xF
     ...:

In [214]: two
Out[214]: <function __main__.two(f)>

In [215]: two(lambda x: x+1)  # 此时才运行two中代码
inside two
Out[215]: <function __main__.two.<locals>.xF(x)>

In [217]: two(lambda x: x+1)(0)  # 此时才运行two及xF中代码
inside two
inside xF
Out[217]: 2
```


##### 注意一下两个定义是相同的：
在1.中参数x出现在lambda中，而2.中x出现在函数定义参数列表中
```python
# 1.
func = lambda x: 2*x

# 2.
def func(x):
    return 2*x
```
例如可以改写 successor
```python
def successor(n):
    return lambda f: lambda x: f(n(f)(x))

def successor(n):
    def func_f(f):
        def func_x(x):
            return f(n(f)(x))
        return func_x
    return func_f
```