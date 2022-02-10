## hw06
Readings
* http://composingprograms.com/pages/29-recursive-objects.html
* 

### Q1 : Vending Machine
* 做homework过程中发现auto testing非常重要且方便，体会到开发中UT的重要性
* use case的整理很重要，将use case转换为测试
* Python doctest 很有实用价值，自己也可以用起来，用doctest方式写UT

### Q3
```python
# str version, but not allo to use str
def build_link(n_str):
    if not n_str:
        return Link.empty
    return Link(int(n_str[0]), build_link(n_str[1:]))
    
return build_link(str(n))
```

### Q6: Next Virahanka Fibonacci Object
根据Hint
```
Hint: Keep track of the previous number by setting a new instance attribute inside next. You can create new instance attributes for objects at any point, even outside the __init__ method.
```
我们可以在next方法中给instance动态加attribute，添加一个self.previous即可。
这是动态语言的特性，根据我的code review经验，这也是Java等静态语言支持者所不提倡的做法，即动态给class/instance添加method或attribute，会使代码看起来confuse
我还是倾向于在定义class instance时把previous定义好