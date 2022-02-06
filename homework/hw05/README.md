homework https://inst.eecs.berkeley.edu/~cs61a/fa21/hw/hw05/

### Take away
* 作业里的Hint，主要帮助是先实现一个可以work的版本，之后再根据作业需求优化，这个思想非常好，先尝试简化方案，之后再优化

### Q2: Yield Paths
两个Hint 非常有用:
```
Hint: If you're having trouble getting started, think about how you'd approach this problem if it wasn't a generator function. What would your recursive calls be? With a generator function, what happens if you make a "recursive call" within its body?

Hint: Remember, it's possible to loop over generator objects because generators are iterators!
```

##### 递归非yield版本
```python
def path_yielder(t, value):
    def f(t, value, path):
        if t.label == value:
            print(path + [t.label])

        if t.is_leaf(): return        

        for branch in t.branches:
            f(branch, value, path + [t.label])

    return f(t, value, [])
```

##### yield from version
yield from 可以穿透generator，从多层generator中拿到结果，有点像flatMap那种flatten操作
yield from 后面接一个generator, 例如 ```yield from f(branch, value, path + [t.label])```
```python
def path_yielder(t, value):
    def f(t, value, path):
        if t.label == value:
            yield path + [t.label]

        if not t.is_leaf():
            for branch in t.branches:
                yield from f(branch, value, path + [t.label])

    return f(t, value, [])
```

##### yield version
如果不用yield from的话，我们知道每一层的递归调用都会返回一个generator，所以在上一层对下一层返回的generator结果做iteration，展开得到list结果在yield 传递出去
```python
def path_yielder(t, value):
    def f(t, value):
        if t.label == value:
            yield [t.label]
        
        if not t.is_leaf():
            for branch in t.branches:
                for sub_path in f(branch, value):
                    yield [t.label] + sub_path

    return f(t, value)
```

## Extra Questions
没做, 之后找时间