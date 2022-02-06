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